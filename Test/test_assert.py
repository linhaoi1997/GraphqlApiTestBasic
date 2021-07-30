import json
from typing import Tuple

import allure

from GraphqlApiObject import BaseUser, GraphqlQueryListAPi
from Schema.PlatformSchema.platform_schema import Mutation, Query
from hamcrest import *

from hamcrest.core.base_matcher import BaseMatcher
from config import *


class IsHasData(BaseMatcher):
    def __init__(self, data: Tuple[str, str]):
        self.path, self.value = data

    def _matches(self, item: GraphqlQueryListAPi):
        return self.value in item.capture(self.path)

    def describe_to(self, description):
        description.append_text("data's path").append_description_of(
            self.path
        ).append_text("\ncontains value").append_description_of(
            self.value
        )

    def describe_mismatch(self, item: GraphqlQueryListAPi, mismatch_description):
        mismatch_description.append_text(
            "data"
        ).append_description_of(
            json.dumps(item.capture(self.path))
        ).append_text("\nnot contains").append_description_of(
            self.value
        )


class QueryUsers(GraphqlQueryListAPi):
    api = Query.users


@allure.story("测试query")
class TestGraphqlQuery:

    def setup_class(self):
        self.user = BaseUser(url, Mutation,
                             {"account": account, "password": password})
        self.user_id = "5ba962f5-cb17-4663-9c71-23774d911f8d"

    @allure.title("测试assert方法")
    def test1(self):
        q = QueryUsers(self.user)
        q.query().assert_that(is_(IsHasData(("data.users.data[*].id", self.user_id))))
