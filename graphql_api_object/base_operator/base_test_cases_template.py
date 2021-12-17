import logging
from typing import Type, List, Callable

import pytest
import allure
from assert_methods import return_equal_input
from .base_query_operator import BaseQueryOperator
from ..graphql_api_object.special_graphql_api import GraphqlQueryListAPi

from hamcrest import assert_that, is_in, not_


class CreateCasesTemplate:
    operator: str  # 要更新的对象
    assert_jmespath: List[str or List[str]]  # 校验jmespath

    @allure.title("执行标准创建用例")
    def test_create(self, data):
        operator = getattr(data, self.operator)
        with allure.step("校验创建返回相等"):
            for detail in operator.details():
                assert_that(
                    detail,
                    return_equal_input(operator.variables, self.assert_jmespath)
                )


class DeleteCasesTemplate:
    operator: str  # 要删除的对象

    @allure.title("执行删除创建用例")
    def test_delete(self, data):
        operator = getattr(data, self.operator)
        with allure.step("删除资源"):
            operator.delete()
        with allure.step("查询不到资源"):
            detail = operator.details()
            while True:
                try:
                    with pytest.raises(AssertionError):
                        next(detail)
                except StopIteration:
                    break


class QueryFilterCasesTemplate:
    query: Type[BaseQueryOperator]
    user: str
    company: str = None

    filters_info = [
        {
            "filter_key": "department",
            "data": [
                {"filter_value": Callable, "value": ["department1", "department2"]},
                {"filter_value": Callable, "value": ["department3", "department4"]},
            ]
        }
    ]

    @allure.title("执行标准查询筛选用例")
    def test_filter(self, data):
        company_id = getattr(data, self.company).id if self.company else None
        user = getattr(data, self.user)
        query = self.query(user, company_id)

        def collect_id(value):
            result = []
            for operator in value:
                data_ = getattr(data, operator)
                if isinstance(data_, list):
                    result.extend([o.id for o in data_])
                else:
                    result.append(data_.id)
            return result

        for filter_info in self.filters_info:
            with allure.step("拿到所有id list"):
                id_list = []
                for i in filter_info["data"]:
                    j = {"filter_value": i["filter_value"], "value": collect_id(i["value"])}
                    logging.info(f'筛选项: {j["filter_value"]}')
                    logging.info(f'对应id: {j["value"]}')
                    id_list.append(j)

            for i in id_list:
                i["filter_value"] = i["filter_value"](data)

            for i in id_list:
                filter_value = i['filter_value']
                logging.info(f"开始筛选: {filter_value}")
                with allure.step("按照筛选条件查询"):
                    ids = query.filter_by(filter_info["filter_key"], filter_value).ids

                in_ids = []
                not_in_ids = []
                for j in id_list:
                    if j["filter_value"] == filter_value:
                        in_ids.extend(j["value"])
                    else:
                        not_in_ids.extend(j["value"])
                logging.info(f"结果不应该包含的id: {not_in_ids}")
                logging.info(f"结果应该包含的id: {in_ids}")

                with allure.step("校验应该查询到的值"):
                    for k in in_ids:
                        assert_that(k, is_in(ids))

                with allure.step("校验不应该查询到的值"):
                    for k in not_in_ids:
                        assert_that(k, not_(is_in(ids)))


class QueryPagingCasesTemplate:
    query_api: Type[GraphqlQueryListAPi]
    user: str
    resource: str  # base_data中的属性,用于创建资源

    @allure.title("执行标准分页用例")
    def test(self, data):
        query_args = self.make_query_args(data)
        query = self.query_api(getattr(data, self.user))
        total = query.set("total_count").run(**query_args).result.total_count
        if total < 15:
            create_num = 15 - total
            for i in range(create_num):
                getattr(data, self.resource)

        self.assert_page(query, query_args, total)

    def make_query_args(self, data):
        return {"filter": {"company": {"id": getattr(data, "company").id}}}

    def assert_page(self, api, query_args, total):
        ids = []
        offset = 0
        flag = True
        while offset < total and flag:
            for i in api.query_ids(offset=offset, **query_args).c("data[*].id"):
                if i in ids:
                    raise AssertionError(f"重复的id{i}")
                ids.append(i)
            offset += 10
        if flag and len(ids) < total:
            raise AssertionError(f"得到长度与totalcount不符：{len(ids)} != {total}")
