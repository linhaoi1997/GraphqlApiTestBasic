import logging
from typing import Dict, Type, List

from ..graphql_api_object import GraphqlOperationAPi, GraphqlQueryListAPi, create_num_string
from .base_operator import BaseOperator
from .utils import dedupe


class BaseFactory:
    # 创建部分
    create_api: Type[GraphqlOperationAPi]  # 创建调用的接口
    create_args: List[Dict] = [
        {"attr": "company", "key": "company.id", "func": None}
    ]  # 创建时必填的参数

    # 查询部分
    query_api: Type[GraphqlQueryListAPi]  # 查询的列表接口
    query_args: List[Dict] = [
        {"attr": "company", "key": "company", "func": lambda x: {"id": x.id}}
    ]  # 查找时必填的filter

    default_attr = {"company": "company"}

    query_path: str = "data"  # 返回结果中对应的列表路径
    query_field: str  # 路径下对应的查找的值
    query_value_path: str or None  # 查找的值等于什么，这个是路径，从create的参数中jmespath搜索
    # 返回操作器部分
    operator: Type[BaseOperator]

    def __init__(self, resource_name, user_name: str, is_single=True, **kwargs):
        self.user_name = user_name
        self.name = resource_name
        args = list(dedupe(self.create_args + self.query_args, key=lambda x: x["attr"]))
        self.kwargs = {key: value for key, value in kwargs.items() if key in args}
        self.kwargs.update(self.default_attr)
        self.create_fixed_args = {key: create_num_string(3, value) if isinstance(value, str) else value
                                  for key, value in kwargs.items() if key not in args}
        self.is_single = is_single

    @classmethod
    def make_args(cls, user, kwargs):  # 给复杂参数预留接口
        return {}

    @classmethod
    def prepare_create_args(cls, user, kwargs: Dict):  # 创建部分
        kwargs_ = cls.make_args(user, kwargs)
        kwargs_.update(kwargs)
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
            return cls.operator(user, cls._query_single(q, query_value, create_api), create_api.variables, final_filter,
                                cls.query_api, cls.query_path)
        else:
            result = []
            for single_value in query_value:
                result.append(
                    cls.operator(user, cls._query_single(q, single_value, create_api), create_api.variables,
                                 final_filter,
                                 cls.query_api, cls.query_path))
                return result

    @classmethod
    def _query_single(cls, query_api, query_value, create_api):
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
    def _handle_args(cls, args, handle_args: list):
        result = {}
        for i in handle_args:
            result[i["key"]] = i.get("func")(args[i["attr"]]) if i.get("func") else args[i["attr"]].id
        return result

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            args = {key: getattr(instance, self.kwargs[key]) for key in self.kwargs}  # 从instance中拿到所有值
            create_kwargs = self._handle_args(args, self.create_args)  # id 参数
            create_kwargs.update(self.create_fixed_args)  # 固定参数
            query_filter = self._handle_args(args, self.query_args)
            user = getattr(instance, self.user_name)  # 从object里面获取对应的用户
            if self.is_single:  # 如果是仅创建一次，那么只创建一次，否则每次都创建一个
                if not instance.__dict__.get(self.name):
                    instance.__dict__[self.name] = self.new(user, create_kwargs, query_filter)
                return instance.__dict__[self.name]
            else:
                return self.new(user, create_kwargs, query_filter)
