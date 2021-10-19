import logging

from GraphqlApiObject.GraphqlApi.gen_params import GenParams

from Schema.GitHubSchema.github_schema import Mutation, github_schema
from jsonschema import validate, draft7_format_checker
import allure

input_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "input": {
            "type": "object",
            "properties": {
                "ownerId": {
                    "type": "integer"
                },
                "name": {
                    "type": "string"
                },
                "body": {
                    "type": "string"
                },
                "template": {
                    "type": "string",
                    "enum": ['BASIC_KANBAN', 'AUTOMATED_KANBAN_V2', 'AUTOMATED_REVIEWS_KANBAN', 'BUG_TRIAGE']
                },
                "repositoryIds": {
                    "type": "array",
                    "items": {
                        "type": "integer"
                    }
                },
                "clientMutationId": {
                    "type": "string"
                }
            }

        }
    }
}

option_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "input": {
            "type": "object",
            "properties": {
                "ownerId": {
                    "type": "integer"
                },
                "name": {
                    "type": "string"
                }
            }

        }
    }
}


class TestGenParams:

    @allure.title("正常生成参数")
    def test_gen(self):
        data = GenParams(github_schema).gen(Mutation.create_project).result
        validate(
            instance=GenParams(github_schema).gen(Mutation.create_project).result,
            schema=input_schema,
            format_checker=draft7_format_checker
        )
        logging.info(data)

    @allure.title("生成只有必填的参数")
    def test_gen_not_optional_params(self):
        data = GenParams(github_schema).gen(Mutation.create_project, optional=True).result
        validate(
            instance=GenParams(github_schema).gen(Mutation.create_project).result,
            schema=option_schema,
            format_checker=draft7_format_checker
        )
        logging.info(data)

    @allure.title("改变参数，无路径")
    def test_change_param(self):
        data = GenParams(github_schema).gen(Mutation.create_project).change("name", "ces")
        logging.info(data)
        assert data["input"]["name"] == "ces"

    @allure.title("改变参数，无路径")
    def test_change_param2(self):
        data = GenParams(github_schema).gen(Mutation.create_project).change("name", None)
        logging.info(data)
        assert data["input"]["name"] is None

    @allure.title("改变参数，复杂路径")
    def test_change_params2(self):
        data = GenParams(github_schema).gen(Mutation.create_project).change("input.template", "AUTOMATED_KANBAN_V2")
        logging.info(data)
        assert data["input"]["template"] == "AUTOMATED_KANBAN_V2"

    @allure.title("改变参数，列表简单路径")
    def test_change_params3(self):
        data = GenParams(github_schema).gen(Mutation.create_project).change("repositoryIds[0]", 0)
        logging.info(data)
        assert data["input"]["repositoryIds"][0] == 0

    @allure.title("改变参数，列表复杂路径")
    def test_change_params4(self):
        data = GenParams(github_schema).gen(Mutation.create_project).change("input.repositoryIds[1]", 0)
        logging.info(data)
        assert data["input"]["repositoryIds"][1] == 0

    @allure.title("改变参数，列表匹配所有")
    def test_change_params5(self):
        data = GenParams(github_schema).gen(Mutation.create_project).change("input.repositoryIds[*]", 0)
        logging.info(data)
        assert data["input"]["repositoryIds"] == [0, 0, 0]

    @allure.title("改变参数，三层以上复杂参数")
    def test_change_params6(self):
        from Schema.PlatformSchema.platform_schema import platform_schema, Mutation
        data = GenParams(platform_schema).gen(Mutation.create_user).change("role[*].id", 2)
        logging.info(data)
        assert data["input"]["role"][0]["id"] == 2
        assert data["input"]["role"][1]["id"] == 2
        assert data["input"]["role"][2]["id"] == 2

    @allure.title("改变参数，替换整个列表")
    def test_change_params7(self):
        from Schema.PlatformSchema.platform_schema import platform_schema, Mutation
        data = GenParams(platform_schema).gen(Mutation.create_user).change("role", [{"id": 10}])
        logging.info(data)
        assert data["input"]["role"][0]["id"] == 10

    @allure.title("改变参数，替换列表为列表")
    def test_change_params8(self):
        from Schema.PlatformSchema.platform_schema import platform_schema, Mutation
        data = GenParams(platform_schema).gen(Mutation.create_user).change("role[*].id", [2, 3, 4])
        logging.info(data)
        assert data["input"]["role"][0]["id"] == 2
        assert data["input"]["role"][1]["id"] == 3
        assert data["input"]["role"][2]["id"] == 4

    @allure.title("改变参数，替换列表为列表2")
    def test_change_params8(self):
        from Schema.PlatformSchema.platform_schema import platform_schema, Mutation
        data = GenParams(platform_schema).gen(Mutation.create_user).change("role[*]", [2, 3, 4])
        logging.info(data)
        assert data["input"]["role"][0] == 2
        assert data["input"]["role"][1] == 3
        assert data["input"]["role"][2] == 4

    @allure.title("改变参数")
    def test_change_params9(self):
        from Schema.PlatformSchema.platform_schema import platform_schema, Mutation
        data = GenParams(platform_schema).gen(Mutation.set_erp_order_check_config).change("editable", True)
        logging.info(data)
        assert data["input"]["editable"] == True

    def test(self):
        from Schema.PlatformSchema.platform_schema import platform_schema, Mutation, ErpProductionTaskInput
        data = GenParams(platform_schema).gen_part(ErpProductionTaskInput)
        logging.info(data)
