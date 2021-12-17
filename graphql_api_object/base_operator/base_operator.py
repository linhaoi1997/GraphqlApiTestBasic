import logging
from typing import Type, List
from ..graphql_api_object import GraphqlQueryAPi, GraphqlUpdateApi, GraphqlApi
from contextlib import contextmanager
from hamcrest import assert_that, equal_to


class BaseOperator:
    query_api: Type[GraphqlQueryAPi] = None  # 查询id

    num_attr: List = []  # 用于计算数量的属性 [{"name":"total","path":"jmespath","describe":"拜访客户数"}]
    attr: List = []  # 用于计算其他的属性 [{"name":"status","path":"jmespath","describe":"拜访任务状态"}]

    update_api: Type[GraphqlUpdateApi]
    delete_api: Type[GraphqlApi]

    def __init__(self, user, info, variables, query_filter, query_list_api, query_path):
        self.user = user
        self.info = info
        self.id = info.get("id")
        self.variables = variables
        self.query_filter = query_filter
        self._query_list = query_list_api(self.user)
        self.query_path = query_path
        self._query = self.query_api(self.user) if self.query_api else None
        self.attr.extend(self.num_attr)

    def details(self):
        detail = self.detail
        detail_from_list = self.detail_from_list
        if detail:
            yield self.detail
        if detail_from_list:
            yield self.detail_from_list

    @property
    def detail(self):
        if self.query_api:
            logging.info("查询单接口")
            return self._query.query_full(self.id).c()

    @property
    def detail_from_list(self):
        logging.info("查询接口列表")
        result = self._query_list.set_filter(**self.query_filter).query_full().c(
            f"{self.query_path}[?id == '{self.id}'] | [0]"
        )
        if not result:
            logging.info(f"查询结果: {self._query_list.result}")
            logging.info(f"jmespath: {self.query_path}[?id == '{self.id}'] | [0]")
            raise AssertionError("not found id")
        else:
            return result

    @property
    def ids_from_list(self):
        return self._query_list.set_filter(**self.query_filter).query_ids(limit=100).ids

    @staticmethod
    def _return_detail(details: list):
        if len(details) > 1:
            if not details[0] == details[1]:
                raise AssertionError(f"列表和detail查询结果不一致: \n1. {details[0]}\n2. {details[1]}")
        return details[0]

    def __getitem__(self, item):
        details = [i[item] for i in list(self.details())]
        logging.info(details)
        return self._return_detail(details)

    def all_nums_attr(self):
        details = list(self.details())
        result = {}
        logging.info(details)
        for i in self.num_attr:
            result[i["name"]] = self._return_detail([j[i["name"]] for j in details])
        return result

    @contextmanager
    def change_account(self, change_info):
        """
        :param change_info: [{"name":"total","change_way":"increase or decrease","change_num":10}]
        :return:
        """
        old_nums = self.all_nums_attr()
        yield
        new_nums = self.all_nums_attr()
        for i in change_info:
            name = i["name"]
            change_way = i["change_way"]
            change_num = i["change_num"]
            if change_way == "increase":
                assert_that(old_nums[name] + change_num, equal_to(new_nums[name]))
            elif change_way == "decrease":
                assert_that(old_nums[name] - change_num, equal_to(new_nums[change_way]))
            else:
                raise AssertionError(f"unknown change way: {change_way}")

    @contextmanager
    def change_user(self, user):
        tmp = self.user
        self.user = user
        yield
        self.user = tmp

    def update_all(self, kwargs):
        kwargs["input.id"] = self.id
        return self.update_api(self.user).auto_run(
            kwargs
        )

    def update_part(self, kwargs):
        kwargs["id"] = self.id
        return self.update_api(self.user).run(
            **{"input": kwargs}
        )

    def delete(self):
        return self.delete_api(self.user).run(
            ids=[self.id]
        )
