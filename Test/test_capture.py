import logging

import allure
import pytest

from GraphqlApiObject import BaseUser, GraphqlQueryListAPi
from Schema.PlatformSchema.platform_schema import Mutation, Query
from config import *



class QueryUsers(GraphqlQueryListAPi):
    api = Query.users


@allure.story("测试query")
class TestGraphqlQuery:

    def setup_class(self):
        self.user = BaseUser(url, Mutation,
                             {"account": account, "password": password})
        self.user_id = "5ba962f5-cb17-4663-9c71-23774d911f8"

    @allure.title("测试jmespath")
    @pytest.mark.parametrize(
        "path",
        [
            "data.users.data",
            "data.users.data[*].account",
            "data.users.data[?id == 'e594f4ea-283b-4c20-8e15-387d303068bb']",
        ]
    )
    def test1(self, path):
        q = QueryUsers(self.user)
        q.query()
        logging.info(q.capture(path))
