import logging

import allure

from GraphqlApiObject import BaseUser, GraphqlQueryAPi, GraphqlOperationAPi, GraphqlQueryListAPi
from Schema.PlatformSchema.platform_schema import Mutation, Query
from config import *


class QueryUser(GraphqlQueryAPi):
    api = Query.user


class QueryUsers(GraphqlQueryListAPi):
    api = Query.users


class CreateUser(GraphqlOperationAPi):
    api = Mutation.create_user


@allure.story("测试query")
class TestGraphqlQuery:

    def setup_class(self):
        self.user = BaseUser(url, Mutation,
                             {"account": account, "password": password})
        self.user_id = "5ba962f5-cb17-4663-9c71-23774d911f8d"
        self.user_name = "4公司1普通员工"

    @allure.title("测试GraphqlQueryAPi")
    def test1(self):
        q = QueryUser(self.user)
        logging.info(q.query(self.user_id).result)
        logging.info(q.query_full(self.user_id).result)

    @allure.title("测试GraphqlQueryListAPi的filter_result方法")
    def test2(self):
        q = QueryUsers(self.user)
        logging.info(q.query().data)
        logging.info(q.query().filter_result("id", self.user_id))
        assert q.filter_result("id", self.user_id)

    @allure.title("测试GraphqlQueryListAPi的search_result方法")
    def test3(self):
        q = QueryUsers(self.user)
        logging.info(q.query().data)
        logging.info(q.query().search_result("id", self.user_id))
        assert q.search_result("id", self.user_id)

    @allure.title("测试GraphqlQueryListAPi的random方法")
    def test4(self):
        q = QueryUsers(self.user)
        q.query()
        logging.info(q.random()["id"])
        assert q.random()
        assert q.random(2)

    @allure.title("测试GraphqlOperationAPi的方法")
    def test5(self):
        q = CreateUser(self.user)
        q.auto_run(
            {
                "input.company.id": "869",
                "input.department.id": "813",
                "input.role": [{"id": "1292"}]
            }
        )
        logging.info(q.variables)
        logging.info(q.result)
        assert q.result

    @allure.title("测试GraphqlOperationAPi的方法2")
    def test6(self):
        q = CreateUser(self.user)
        q.auto_tidy_run(
            {
                "input.company.id": "869",
                "input.department.id": "813",
                "input.role": [{"id": "1292"}]
            }
        )
        logging.info(q.variables)
        logging.info(q.result)
        assert q.result

    @allure.title("find")
    def test7(self):
        q = QueryUsers(self.user)
        from GraphqlApiObject.GraphqlApi.tools import create_num_string
        ac = create_num_string(5, "a")
        with q.find("account", ac):
            c = CreateUser(self.user)
            c.auto_tidy_run(
                {
                    "input.account": ac,
                    "input.company.id": "869",
                    "input.department.id": "813",
                    "input.role": [{"id": "1292"}]
                }
            )
        logging.info(q.run().result)
        assert q.query().result.data[0].id == q.id
