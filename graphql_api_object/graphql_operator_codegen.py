import argparse
import os


def snake_to_camel(name):
    name = ''.join(word.title() for word in name.split('_'))
    return name


class CodeGen:

    @classmethod
    def gen_init(cls, name: str):
        return f"""from .{name}_factory import {snake_to_camel(name)}Factory
from .{name}_operator import {snake_to_camel(name)}Operator
from .{name}_query_operator import {snake_to_camel(name)}QueryOperator
"""

    @classmethod
    def gen_factory(cls, name: str):
        return f"""from graphqlapiobject.base_operator import BaseFactory
from .{name}_operator import {snake_to_camel(name)}Operator
from ...apis.Mutation_apis import 
from ...apis.Query_apis import 


class {snake_to_camel(name)}Factory(BaseFactory):
    # 创建部分
    create_api: Type[GraphqlOperationAPi] =  # 创建调用的接口
    create_args: List[str] =   # 创建时必填的参数

    # 查询部分
    query_api: Type[GraphqlQueryListAPi] =  # 查询的列表接口
    query_args: List[str] =   # 查找时必填的filter

    query_path: str = "data"  # 返回结果中对应的列表路径
    query_field: str =   # 路径下对应的查找的值
    query_value_path: str or None =  # 查找的值等于什么，这个是路径，从create的参数中jmespath搜索
    # 返回操作器部分
    operator: Type[base_operator] = {snake_to_camel(name)}Operator

    @classmethod
    def make_args(cls, user, kwargs):
        return {{}}
        
    @classmethod
    def args(cls, **kwargs):
        template = {{
            "kwargs": [],
            "query_filter": [],
            "is_single": kwargs.pop("is_single", True),
            "filter_has_company": kwargs.pop("filter_has_company", True)
        }}
        return cls._args(template, kwargs)
"""

    @classmethod
    def gen_operator(cls, name: str):
        return """from graphqlapiobject import base_operator
from ...apis.Mutation_apis import 


class %sOperator(base_operator):
    query_api: Type[GraphqlQueryAPi] =   # 查询id

    num_attr: List = []  # 用于计算数量的属性 [{"name":"total","path":"jmespath","describe":"拜访客户数"}]
    attr: List = []  # 用于计算其他的属性 [{"name":"status","path":"jmespath","describe":"拜访任务状态"}]
    
    update_api = 
    delete_api = 

    def delete(self):
        return self.delete_api(self.user).run(id = [self.id])
""" % snake_to_camel(name)

    @classmethod
    def gen_query_operator(cls, name: str):
        return f"""from graphqlapiobject import BaseQueryOperator
from ...apis.Query_apis import 


class %sQueryOperator(BaseQueryOperator):
    query_api : Type[GraphqlQueryListAPi] = 
    base_filter: Dict = 
    filter_has_company: bool = True

""" % snake_to_camel(name)

    @classmethod
    def gen(cls, name):
        os.mkdir(name)
        with open(f"{name}/__init__.py", "w") as f:
            f.write(cls.gen_init(name))

        with open(f"{name}/{name}_factory.py", "w") as f:
            f.write(cls.gen_factory(name))

        with open(f"{name}/{name}_operator.py", "w") as f:
            f.write(cls.gen_operator(name))

        with open(f"{name}/{name}_query_operator.py", "w") as f:
            f.write(cls.gen_query_operator(name))


def main():
    parser = argparse.ArgumentParser(description='operator_code_gen')
    parser.add_argument('name', type=str, help='创建操作器的目录是什么')

    args = parser.parse_args()
    CodeGen.gen(args.name)


if __name__ == '__main__':
    print(CodeGen.gen_query_operator("ces"))
