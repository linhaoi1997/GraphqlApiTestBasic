import logging
from typing import Dict, Type, List

from ..graphql_api_object import GraphqlOperationAPi, GraphqlQueryListAPi, create_num_string
from .base_operator import BaseOperator


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

    def __init__(self, resource_name, user_name: str, **kwargs):
        args = self.args(**kwargs)
        self.user_name = user_name
        self.name = resource_name
        self.kwargs = args.get("kwargs", [])
        self.query_filter = args.get("query_filter", [])
        self.is_single = args.get("is_single", True)
        self.filter_has_company = args.get("filter_has_company", True)

    @classmethod
    def args(cls, **kwargs):
        template = {
            "kwargs": kwargs.pop("kwargs", []),
            "query_filter": kwargs.pop("query_filter", []),
            "is_single": kwargs.pop("is_single", True),
            "filter_has_company": kwargs.pop("filter_has_company", True)
        }
        return cls._args(template, kwargs)

    @classmethod
    def _args(cls, template, kwargs):
        for key, value in kwargs.items():  # 添加额外参数默认create接口修改
            template["kwargs"].append(
                {"key": key, "value": create_num_string(3, value + "_") if isinstance(value, str) else value})
        return template

    @classmethod
    def make_args(cls, user, kwargs):  # 给复杂参数预留接口
        return {}

    @classmethod
    def prepare_create_args(cls, user, kwargs: Dict, assert_args=True):  # 创建部分
        # 创建
        logging.info("开始创建资源,参数为:")
        logging.info(kwargs)
        kwargs_ = cls.make_args(user, kwargs)
        kwargs_.update(kwargs)
        all_args = kwargs_.keys()
        if assert_args:
            for i in cls.create_args:
                if i not in all_args:
                    raise AssertionError(f"没有传入 {i} 必填参数")
        return kwargs_

    @classmethod
    def send_create_request(cls, user, kwargs: Dict):
        c = cls.create_api(user).auto_run(cls.prepare_create_args(user, kwargs))
        return c

    @classmethod
    def make_query_filters(cls, user, query_filter):
        return {}

    @classmethod
    def prepare_query_args(cls, user, query_filter):
        # 查找
        filter_ = cls.make_query_filters(user, query_filter)
        filter_.update(query_filter)
        logging.info(f"query_filter: {query_filter}")
        return filter_

    @classmethod
    def send_query_request(cls, user, query_filter) -> List[Dict] or Dict:  # 查找部分
        if query_filter is None:
            query_filter = {}
        final_filter = cls.prepare_query_args(user, query_filter)
        return cls.query_api(user).set_filter(**final_filter).query_full(), final_filter

    @classmethod
    def search_from_result(cls, user, create_api, query_filter):
        q, final_filter = cls.send_query_request(user, query_filter)
        if not cls.query_value_path:  # 从variables查找需要加入input
            cls.query_value_path = ".".join(["input", cls.query_field])
        query_value = create_api.search_from_input("input." + cls.query_value_path)
        if not isinstance(query_value, list):  # 可能一次创建多个对象
            return cls.operator(user, cls._query_single(q, query_value), create_api.variables, final_filter,
                                cls.query_api, cls.query_path)
        else:
            result = []
            for single_value in query_value:
                result.append(
                    cls.operator(user, cls._query_single(q, single_value), create_api.variables, final_filter,
                                 cls.query_api, cls.query_path))
                return result

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
    def new(cls, user, kwargs: Dict, query_filter=None):
        # 创建
        query_filter = query_filter or {}
        logging.info(kwargs)
        c = cls.send_create_request(user, kwargs)
        # 创建之后去查询
        return cls.search_from_result(user, c, query_filter)

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
