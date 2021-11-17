import logging
from typing import Dict, Type, List

from ..GraphqlApi import GraphqlOperationAPi, GraphqlQueryListAPi
from .base_operator import BaseOperator

"""发现在初始化的时候要加上查询的参数，创建需要参数，查询也需要参数，并且都可能是动态的，__get__这部分代码要重构，目前不好维护"""


class BaseFactory:
    # 创建部分
    create_api: Type[GraphqlOperationAPi]  # 创建调用的接口
    create_args: List[str] = []  # 创建时必填的参数

    # 查询部分
    query_api: Type[GraphqlQueryListAPi]  # 查询的列表接口
    query_args: List[str] = []  # 查找时必填的filter

    query_path: str = "data"  # 返回结果中对应的列表路径
    query_field: str  # 路径下对应的查找的值
    query_value_path: str or None  # 查找的值等于什么，这个是路径，从create的参数中jmespath搜索
    # 返回操作器部分
    operator: Type[BaseOperator]

    def __init__(self, name, user_name: str, kwargs: list = None, query_filter: list = None, is_single=True,
                 filter_has_company=True):
        """
        :param name: 在类中的名称
        :param user_name: 使用人员的属性
        :param kwargs: 创建的字典[{"key":"jmespath","attr_name":"department","func": return_id_input,"value":"bulabula"}]
        :param kwargs: 创建的字典[{"key":"company","attr_name":"company","func": return_id_input,"value":"bulabula"}]
        :param is_single: 是否仅创建一次，再次创建返回之前创建的对象，还是说每次都创建新的对象
        """
        if query_filter is None:
            query_filter = []
        if kwargs is None:
            kwargs = []
        self.user_name = user_name
        self.name = name
        self.kwargs = kwargs
        self.query_filter = query_filter
        self.is_single = is_single
        self.filter_has_company = filter_has_company

    @classmethod
    def _create(cls, user, kwargs: Dict):  # 创建部分
        # 创建
        logging.info("开始创建资源,参数为:")
        logging.info(kwargs)
        kwargs_ = cls.make_args(user, kwargs)
        kwargs_.update(kwargs)
        all_args = kwargs_.keys()
        for i in cls.create_args:
            if i not in all_args:
                raise AssertionError(f"没有传入 {i} 必填参数")
        c = cls.create_api(user).auto_run(kwargs_)
        return c

    @classmethod
    def make_args(cls, user, kwargs):  # 给复杂参数预留接口
        return {}

    @classmethod
    def _query_single(cls, query_api, query_value):
        logging.info("开始查询资源")
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
    def _query_from_list(cls, user, create_api: GraphqlOperationAPi, query_filter) -> List[Dict] or Dict:  # 查找部分
        if not cls.query_value_path:  # 从variables查找需要加入input
            cls.query_value_path = ".".join(["input", cls.query_field])
        query_value = create_api.search_from_input("input." + cls.query_value_path)
        # 查找
        filter_ = cls.make_query_filters()
        filter_.update(query_filter)
        logging.info(f"query_filter: {query_filter}")
        q = cls.query_api(user).set_filter(**filter_).query_full()
        if not isinstance(query_value, list):  # 可能一次创建多个对象
            info = cls._query_single(q, query_value)
            return info
        else:
            infos = []
            for single_value in query_value:
                infos.append(cls._query_single(q, single_value))
            return infos

    @classmethod
    def make_query_filters(cls):
        return {}

    @classmethod
    def new(cls, user, kwargs: Dict, query_filter=None):
        # 创建
        query_filter = query_filter or {}
        logging.info(kwargs)
        c = cls._create(user, kwargs)
        # 创建之后去查询
        info = cls._query_from_list(user, c, query_filter)
        # 返回操作对象
        if isinstance(info, List):
            return [cls.operator(user, i, c.variables, query_filter) for i in info]
        return cls.operator(user, info, c.variables, query_filter)

    @classmethod
    def handle_args_from_instance(cls, instance, variables):
        kwargs = {}
        for arg in variables:  # 对这种形式传入的参数来讲，必是动态参数，从instance中获取
            if arg.get("value"):  # 如果传了value直接使用
                value = arg.get("value")
            elif arg.get("func"):  # 如果没传value，那么去object里面取id，func设置id的格式
                attr = [getattr(instance, i) for i in arg["attr_name"]] if isinstance(arg["attr_name"], list) else \
                    getattr(instance, arg["attr_name"])
                value = arg.get("func")(attr)
            else:  # 默认的格式
                value = getattr(instance, arg["attr_name"]).id
            kwargs[arg["key"]] = value
        return kwargs

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            create_kwargs = self.handle_args_from_instance(instance, self.kwargs)
            query_filter = self.handle_args_from_instance(instance, self.query_filter)
            if self.filter_has_company:
                query_filter["company"] = {"id": instance.company.id}
            user = getattr(instance, self.user_name)  # 从object里面获取对应的用户
            if self.is_single:  # 如果是仅创建一次，那么只创建一次，否则每次都创建一个
                if not instance.__dict__.get(self.name):
                    instance.__dict__[self.name] = self.new(user, create_kwargs, query_filter)
                return instance.__dict__[self.name]
            else:
                return self.new(user, create_kwargs, query_filter)


class ManyOperatorsFactory:
    def __init__(self, factory: Type[BaseFactory], num, name, user_name: str, kwargs: List, query_filter: List,
                 is_single=True):
        self.factory = factory
        self.num = num
        self.name = name
        self.user_name = user_name
        self.kwargs = kwargs
        self.query_filter = query_filter
        self.is_single = is_single

    def __get__(self, instance, owner):
        if self.is_single and not instance.__dict__.get(self.name):
            result = []
            for i in range(self.num):
                name = "__".join([self.name, str(i)])
                setattr(instance, name,
                        self.factory(self.name, self.user_name, self.kwargs, self.query_filter, self.is_single))
                result.append(getattr(instance, name))
            instance.__dict__[self.name] = result
            return instance.__dict__[self.name]
        else:
            return instance.__dict__[self.name]


class CreateAllOfCreateArgsFactory:
    """
    与第一个工厂不同的是格式kwargs的格式不同
    [{"key":"jmespath","attr_name":"department","func": return_id_input,"is_list":False,"value":"bulabula"}]
    is_list标记参数为列表值，把列表值拆解为一个一个值，依次发送接口创建资源
    """

    def __init__(self, factory: Type[BaseFactory], name, user_name: str, kwargs: List, query_filter: List,
                 is_single=True):
        self.factory = factory
        self.name = name
        self.user_name = user_name
        self.kwargs = kwargs
        self.query_filter = query_filter
        self.is_single = is_single

    def yield_kwargs(self, instance):
        kwargs = []
        list_kwargs = []
        values = []
        for i in self.kwargs:
            if i["is_list"]:
                list_kwargs.append(i)
                if i.get("func"):
                    values.append(i["func"](getattr(instance, i["attr_name"])))
                else:
                    values.append(getattr(instance, i["attr_name"]).id)
            else:
                kwargs.append(i)
        for i in range(len(values[0])):
            result = kwargs.copy()
            for j in range(len(list_kwargs)):
                list_kwargs[j]["value"] = values[j][i]
            result.extend(list_kwargs)
            yield result

    def __get__(self, instance, owner):
        if self.is_single and not instance.__dict__.get(self.name):
            result = []
            for i in self.yield_kwargs(instance):
                name = "__".join([self.name, str(i)])
                setattr(instance, name,
                        self.factory(self.name, self.user_name, i, self.query_filter, self.is_single))
                result.append(getattr(instance, name))
            instance.__dict__[self.name] = result
            return instance.__dict__[self.name]
        else:
            return instance.__dict__[self.name]


class IdDictBuilder:

    @staticmethod
    def id(operator: BaseOperator):
        return operator.id

    @staticmethod
    def id_to_list(operator: BaseOperator):
        return [operator.id]

    @staticmethod
    def id_to_dict_list(operator: BaseOperator):
        return [{"id": operator.id}]

    @staticmethod
    def id_dict(operator: BaseOperator):
        return {"id": operator.id}

    @staticmethod
    def id_list(operators: List[BaseOperator]):
        return [i.id for i in operators]

    @staticmethod
    def id_dict_list(operators: List[BaseOperator]):
        return [{"id": i.id} for i in operators]
