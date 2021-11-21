import logging
from typing import Type, Dict, List

import pytest
import allure
from assert_methods import return_equal_input

from .. import BaseUser
from ..base_operator import BaseFactory, BaseOperator, BaseQueryOperator
from ..base_operator.base_data import BaseData
from hamcrest import assert_that, is_in, not_


class UpdateCasesTemplate:
    name: str = ""
    create_factory: Type[BaseFactory]  # 创建工厂
    operator: BaseOperator  # 要更新的对象
    update_args: Dict  # 更新的参数
    data: BaseData  # 数据模版
    assert_jmespath: List[str or List[str]]  # 校验jmespath
    users: List[BaseUser] = []

    @pytest.mark.parametrize("user", users)
    @allure.title(name or "{user}执行标准更新用例")
    def test_update(self, user):
        with allure.step("选定执行人"):
            self.operator.user = user
        with allure.step("构建参数"):
            kwargs = {"id": self.operator.id}
            kwargs.update(self.create_factory.handle_args_from_instance(self.data, self.update_args))
            kwargs.update(self.create_factory.make_args(user, kwargs))
        with allure.step("执行更新"):
            update = self.operator.update_all(kwargs)
        with allure.step("校验结果"):
            for detail in self.operator.detail():
                assert_that(
                    detail,
                    return_equal_input(update.variables, self.assert_jmespath)
                )


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
