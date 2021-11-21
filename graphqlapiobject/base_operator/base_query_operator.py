import logging
from typing import Type, Dict, List
from functools import partial

from ..graphql_api_object import GraphqlQueryListAPi
from .base_operator import BaseOperator


class BaseQueryOperator(object):
    query_api: Type[GraphqlQueryListAPi]
    base_filter: Dict = {}
    filter_has_company: bool = True

    def __init__(self, user, company_id=None):
        self.user = user
        if self.filter_has_company:
            self.company_id = company_id or self.user.info["company"]["id"]
        else:
            self.company_id = None

        logging.info(self.company_id)
        self.base_filter["company"] = {"id": self.company_id}
        self.query: GraphqlQueryListAPi = self.query_api(self.user)

    def send_request(self, **kwargs):
        return self.query.query_full(**kwargs)

    def search_row(self, query_path, query_field, query_value, filter_dict: Dict):
        filter_dict.update(self.base_filter)
        return self.send_request(filter=filter_dict).c(
            f"{query_path}[?{query_field} == '{query_value}'] | [0]"
        )

    def filter_by(self, key, value):
        kwargs = {key: value}
        kwargs.update(self.base_filter)
        self.query.set_filter(**kwargs)
        return self.send_request()

    @property
    def ids(self):
        return self.query.ids

    def __getattr__(self, item: str):
        if item.startswith("filter_by_"):
            key = item.split("_")[-1]
            return partial(self.filter_by, key)
        else:
            raise AssertionError(f"QueryOperator object has no attribute named {item}")


class OperatorGetFromList(object):
    query_operator: Type[BaseQueryOperator]
    query_path: str
    query_field: str
    operator: Type[BaseOperator]

    def __init__(self, user, query_value: Dict, filter_dict: List[Dict], filter_has_company=True):
        """
        :param user: str
        :param query_value: {"attr":department1,"func":func,"value":"value"}
        :param filter_dict: [{"key":"company","attr_name":"company","func": return_id_input,"value":"bulabula"}]
        """
        self.user_name = user
        self.filter_dict = filter_dict
        self.query_value = query_value
        self.filter_has_company = filter_has_company

    @classmethod
    def handle_args_from_instance(cls, instance, variables):
        kwargs = {}
        for arg in variables:  # 对这种形式传入的参数来讲，必是动态参数，从instance中获取
            if arg.get("value"):  # 如果传了value直接使用
                value = arg.get("value")
            elif arg.get("func"):  # 如果没传value，那么去object里面取id，func设置id的格式
                value = arg.get("func")(getattr(instance, arg["attr_name"]))
            else:  # 默认的格式
                value = getattr(instance, arg["attr_name"]).id
            kwargs[arg["key"]] = value
        return kwargs

    def handle_value(self, instance):
        if self.query_value.get("value"):
            return self.query_value.get("value")
        elif not self.query_value.get("func"):
            return getattr(instance, self.query_value["attr"]).id
        else:
            return self.query_value.get("func")(getattr(instance, self.query_value["attr"]))

    def __get__(self, instance, owner):
        user = getattr(instance, self.user_name)
        query_filter = self.handle_args_from_instance(instance, self.filter_dict)
        value = self.handle_value(instance)
        if self.filter_has_company:
            query_filter["company"] = {"id": instance.company.id}
        query_operator = self.query_operator(user)
        info = query_operator.search_row(self.query_path, self.query_field, value, query_filter)
        return self.operator(user, info, {}, query_filter, query_operator.query_api, self.query_path)
