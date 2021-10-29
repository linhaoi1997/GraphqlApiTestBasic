from typing import Type, List
from ..GraphqlApi import GraphqlQueryListAPi, GraphqlQueryAPi
from contextlib import contextmanager
from hamcrest import assert_that, equal_to


class BaseOperator:
    query_api: Type[GraphqlQueryAPi] = None  # 查询id
    query_list_api: Type[GraphqlQueryListAPi]  # 从list中过滤
    query_path: str = "data"

    num_attr: List = []  # 用于计算数量的属性 [{"name":"total","path":"jmespath","describe":"拜访客户数"}]
    attr: List = []  # 用于计算其他的属性 [{"name":"status","path":"jmespath","describe":"拜访任务状态"}]

    def __init__(self, user, info, variables, query_filter):
        self.user = user
        self.info = info
        self.id = info["id"]
        self.variables = variables
        self.query_filter = query_filter
        self._query_list = self.query_list_api(self.user)
        self._query = self.query_api(self.user) if self.query_api else None
        self.attr.extend(self.num_attr)

    def detail(self):
        if self.query_api:
            yield self._query.query_full(self.id).result
        yield self._query_list.set_filter(**self.query_filter).query_full().c(
            f"{self.query_path}[?id == '{self.id}'] | [0]"
        )

    @staticmethod
    def _return_detail(details: list):
        if len(details) > 1:
            if not details[0] == details[1]:
                raise AssertionError(f"列表和detail查询结果不一致: \n1. {details[0]}\n2. {details[1]}")
        else:
            return details[0]

    def __getitem__(self, item):
        for i in self.attr:
            if item == i["name"] or item == i["describe"]:
                name = i["name"]
                break
        else:
            raise AssertionError("从定义的属性中没有找到该属性")

        details = [i[name] for i in list(self.detail())]

        return self._return_detail(details)

    def all_nums_attr(self):
        details = list(self.detail())
        result = {}
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
            if i[change_way] == "increase":
                assert_that(old_nums[i[name]] + i[change_num], equal_to(new_nums[i[name]]))
            elif i[change_way] == "decrease":
                assert_that(old_nums[i[name]] - i[change_num], equal_to(new_nums[i[name]]))
            else:
                raise AssertionError(f"unknown change way: {change_way}")

    @contextmanager
    def change_user(self, user):
        tmp = self.user
        self.user = user
        yield
        self.user = tmp
