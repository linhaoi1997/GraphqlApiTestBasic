import logging
from typing import Type, List

import pytest
import allure
from assert_methods import return_equal_input

from .. import GraphqlQueryListAPi
from ..base_operator import BaseOperator, BaseQueryOperator
from ..base_operator.base_data import BaseData
from hamcrest import assert_that, is_in, not_


class CreateCasesTemplate:
    name: str = ""
    operator: BaseOperator  # 要更新的对象
    assert_jmespath: List[str or List[str]]  # 校验jmespath

    @allure.title(name or "执行标准创建用例")
    def test_update(self, user):
        with allure.step("校验创建返回相等"):
            for detail in self.operator.detail():
                assert_that(
                    detail,
                    return_equal_input(self.operator.variables, self.assert_jmespath)
                )


class DeleteCasesTemplate:
    name: str = ""
    operator: BaseOperator  # 要更新的对象

    @allure.title(name or "执行标准创建用例")
    def test_update(self, user):
        with allure.step("删除资源"):
            self.operator.delete()
        with allure.step("查询不到资源"):
            with pytest.raises(AssertionError):
                for i in self.operator.detail():
                    logging.info(i)


class QueryFilterCasesTemplate:
    name: str = ""
    data: BaseData  # 创建工厂
    query: BaseQueryOperator

    filters_info = [
        {
            "filter_key": "department",
            "data": [
                {"filter_value": {"id": "id1"}, "value": ["department1", "department2"]},
                {"filter_value": {"id": "id2"}, "value": ["department3", "department4"]},
            ]
        }
    ]

    @pytest.mark.parametrize("filter_info", filters_info)
    @allure.title("执行标准查询用例: {filter_key}")
    def test_filter(self, filter_info):

        def collect_id(value):
            result = []
            for v in value:
                data = getattr(self.data, v)
                if isinstance(data, list):
                    result.extend([o.id for o in data])
                else:
                    result.append(data.id)
            return result

        with allure.step("拿到所有id list"):
            id_list = []
            for i in filter_info["data"]:
                j = {"filter_value": i["filter_value"], "value": collect_id(i["value"])}
                logging.info(f'筛选项: {j["filter_value"]}')
                logging.info(f'对应id: {j["value"]}')
                id_list.append(j)

        for i in id_list:
            filter_value = i['filter_value']
            logging.info(f"开始筛选: {filter_value}")
            with allure.step("按照筛选条件查询"):
                ids = self.query.filter_by(filter_info["filter_key"], filter_value).ids

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

    @staticmethod
    def make_query_args(data):
        return {"filter": {"company": {"id": getattr(data, "company").id}}}

    @staticmethod
    def assert_page(api, query_args, total):
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
