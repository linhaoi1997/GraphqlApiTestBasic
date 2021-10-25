import logging
from typing import Dict, Type, List

from ..GraphqlApi import GraphqlOperationAPi, GraphqlQueryListAPi
from .base_operator import BaseOperator


class BaseFactory:
    # 创建部分
    create_api: Type[GraphqlOperationAPi]  # 创建调用的接口
    create_args: Dict = {}  # 创建默认的参数,基本参数如company id
    create_has_company: bool = True  # 创建时是否加上company_id
    # 查询部分
    query_api: Type[GraphqlQueryListAPi]  # 查询的列表接口
    query_filter: Dict = {}  # 查询的参数，如果不传默认为None
    filter_has_company: bool = True
    query_path: str = "data"  # 返回结果中对应的列表路径
    query_field: str  # 路径下对应的查找的值
    query_value_path: str or None  # 查找的值等于什么，这个是路径，从create的参数中jmespath搜索
    # 返回操作器部分
    operator: Type[BaseOperator]
    return_has_company: bool = True

    @classmethod
    def _create(cls, user, kwargs: Dict):  # 创建部分
        # 创建
        from copy import deepcopy
        args = deepcopy(cls.create_args)
        if cls.create_has_company:
            cls.create_args["company"] = cls.make_company_id(user, kwargs)
        kwargs.update(cls.make_args(user))
        args.update(kwargs)
        c = cls.create_api(user).auto_run(args)
        return c

    @classmethod
    def make_args(cls, user):
        return {}

    @classmethod
    def make_company_id(cls, user, kwargs):
        company_id = kwargs.get("company_id") or user.info["company"]["id"]
        return {"id": company_id}

    @classmethod
    def _query_single(cls, query_api, query_value):
        expression = f"{cls.query_path}[?{cls.query_field} == '{query_value}'] | [0]"
        info = query_api.c(
            expression
        )
        if not info:
            raise AssertionError(f"从\n{query_api.result}\n中jmespath: {expression} 取值为None")
        else:
            logging.info(f"从\n{query_api.result}\n中jmespath: {expression} 取值为: {info}")
        return info

    @classmethod
    def _query_from_list(cls, user, create_api: GraphqlOperationAPi, kwargs) -> List[Dict] or Dict:  # 查找部分
        if cls.filter_has_company:  # query如果需要company id
            cls.query_filter["company"] = cls.make_company_id(user, kwargs)
        if not cls.query_value_path:  # 从variables查找需要加入input
            cls.query_value_path = ".".join(["input", cls.query_field])
        query_value = create_api.search_from_input("input." + cls.query_value_path)
        # 查找
        q = cls.query_api(user).query_full(filter=cls.query_filter)
        if not isinstance(query_value, list):  # 可能一次创建多个对象
            info = cls._query_single(q, query_value)
            return info
        else:
            infos = []
            for single_value in query_value:
                infos.append(cls._query_single(q, single_value))
            return infos

    @classmethod
    def new(cls, user, kwargs: Dict):
        # 创建
        logging.info(kwargs)
        c = cls._create(user, kwargs)
        # 创建之后去查询
        info = cls._query_from_list(user, c, kwargs)
        # 返回操作对象
        company_id = cls.make_company_id(user, kwargs) if cls.return_has_company else None
        if isinstance(info, List):
            return [BaseOperator(user, i, c.variables, company_id) for i in info]
        return cls.operator(user, info, c.variables, company_id)

    def __init__(self, name, user_name: str, kwargs: List, is_single=True, is_list=False):
        """
        :param name: 在类中的名称
        :param user_name: 使用人员的属性
        :param kwargs: 创建的字典[{"path":"jmespath","attr_name":"department","func": return_id_input,"is_list":False,
                                "value":"bulabula"}]
        :param is_single: 是否仅创建一次，再次创建返回之前创建的对象，还是说每次都创建新的对象
        """
        self.user_name = user_name
        self.name = name
        self.kwargs = kwargs
        self.is_single = is_single
        self.is_list = is_list

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            if not self.is_list:  # 如果不是生成多个值
                kwargs = {}
                for arg in self.kwargs:  # 对这种形式传入的参数来讲，必是动态参数，从instance中获取
                    if arg.get("value"):  # 如果传了value直接使用
                        value = arg.get("value")
                    elif arg.get("func"):  # 如果没传value，那么去object里面取id，func设置id的格式
                        value = arg.get("func")(getattr(instance, arg["attr_name"]))
                    else:  # 默认的格式
                        value = getattr(instance, arg["attr_name"]).id
                    kwargs[arg["path"]] = value
                user = getattr(instance, self.user_name)  # 从object里面获取对应的用户
                if self.is_single:  # 如果是仅创建一次，那么只创建一次，否则每次都创建一个
                    if not instance.__dict__.get(self.name):
                        instance.__dict__[self.name] = self.new(user, kwargs)
                    return instance.__dict__[self.name]
                else:
                    return self.new(user, kwargs)
            else:
                def single_kwarg(kwargs_):
                    """如果要生成多个需要处理参数，带is_list 标记的为list，接口传参时，列表的单个项表示一个输入"""
                    base_kwarg = {}
                    list_kwargs = {}
                    length = 1
                    for arg_ in self.kwargs:  # 处理逻辑与之前一致
                        if not arg.get("value"):
                            value_ = arg.get("value")
                        elif arg.get("func"):
                            value_ = arg_.get("func")(getattr(instance, arg_["attr_name"]))
                        else:
                            value_ = IdDictBuilder.return_id(getattr(instance, arg_["attr_name"]))
                        if not arg_.get("is_list"):  # 如果有is_list标记先存起来
                            base_kwarg[arg_["path"]] = value_
                        else:
                            length = len(value_)
                            list_kwargs[arg_["path"]] = value_
                    for i in range(length):  # is_list标记的每个值生成一个参数
                        for arg_ in list_kwargs:
                            base_kwarg[arg_] = list_kwargs[arg_][i]
                        yield base_kwarg

                user = getattr(instance, self.user_name)
                if self.is_single:
                    if not instance.__dict__.get(self.name):
                        instance.__dict__[self.name] = [self.new(user, kwargs) for kwargs in single_kwarg(self.kwargs)]
                    return instance.__dict__[self.name]
                else:
                    return [self.new(user, kwargs) for kwargs in single_kwarg(self.kwargs)]


class IdDictBuilder:

    @staticmethod
    def return_id_dict(id_or_ids: List[BaseOperator] or BaseOperator):
        if isinstance(id_or_ids, List):
            return [{"id": i.id} for i in id_or_ids]
        return {"id": id_or_ids.id}

    @staticmethod
    def return_id_dict_list(id_or_ids: List[BaseOperator] or BaseOperator):
        if isinstance(id_or_ids, List):
            return [{"id": i.id} for i in id_or_ids]
        return [{"id": id_or_ids.id}]

    @staticmethod
    def return_id(id_or_ids: List[BaseOperator] or BaseOperator):
        if isinstance(id_or_ids, List):
            return [i.id for i in id_or_ids]
        return id_or_ids.id
