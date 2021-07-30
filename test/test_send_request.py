import json
import logging

import allure
import pytest

from ApiTestBasic import BaseUser, GraphqlQueryListAPi, pformat
from Schema.PlatformSchema.platform_schema import Mutation, Query
from config import *


class QueryUsers(GraphqlQueryListAPi):
    api = Query.users


@allure.story("测试query")
class TestGraphqlQuery:

    def setup_class(self):
        self.user = BaseUser(url, Mutation,
                             {"account": account, "password": password})

    @allure.title("正常query发送接口")
    def test1(self):
        q = QueryUsers(self.user)
        logging.info(q.run().result)
        assert q.result.data
        logging.info(q.query_ids().result)
        assert q.result.data
        logging.info(pformat(json.dumps(q.data)))

    @allure.title("三层query发送接口")
    def test2(self):
        q = QueryUsers(self.user)
        logging.info(q.q("data.role.id").run().result)
        assert q.result.data[0].role[0].id

    @allure.title("测试__fields__方法")
    def test3(self):
        q = QueryUsers(self.user)
        logging.info(q.q("data.__fields__", "id", "name").run().result)
        assert q.result.data[0].id
        assert q.result.data[0].name

    @allure.title("测试__fields__方法2")
    def test4(self):
        q = QueryUsers(self.user)
        logging.info(q.q("data.__fields__", id=True, name=True).run().result)
        assert q.result.data[0].id
        assert q.result.data[0].name

    @allure.title("测试__fields__方法3")
    def test5(self):
        q = QueryUsers(self.user)
        logging.info(q.q("data.__fields__", id=False).run().result)
        with pytest.raises(AttributeError):
            assert q.result.data[0].id
        assert q.result.data[0].name

    @allure.title("测试__fields__方法4")
    def test6(self):
        q = QueryUsers(self.user)
        logging.info(q.q("data.__fields__", __exclude__=("id",)).run().result)
        with pytest.raises(AttributeError):
            assert q.result.data[0].id
        assert q.result.data[0].name

    @allure.title("测试complex_op方法")
    def test6(self):
        q = QueryUsers(self.user)
        with q.complex_op("data"):
            q.set("id").set("name")
        logging.info(q.run().result)
        assert q.result.data[0].id
        assert q.result.data[0].name