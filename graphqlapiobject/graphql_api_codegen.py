import os
import importlib
import argparse


class GenCode:
    @staticmethod
    def first_up(name: str):
        name = name[0].upper() + name[1:]
        return name

    @classmethod
    def write_class(cls, type_, api):
        suffix, end = api.name.split("_")[0].lower(), api.name.split("_")[-1].lower()
        if suffix in ("create", "add"):
            return cls.__write_class(type_, api, "GraphqlOperationAPi")
        elif suffix in ("delete", "update", "set", "assign", "log", "cancel"):
            return cls.__write_class(type_, api, "GraphqlUpdateApi")
        elif end.endswith("s") or end == "list":
            return cls.__write_class(type_, api, "GraphqlQueryListAPi")
        else:
            return cls.__write_class(type_, api, "GraphqlQueryAPi")

    @classmethod
    def __write_class(cls, type_, api, base_api):
        return '''\
class {title_api_name}({base_api}):
    api = {type}.{api_name}


'''.format(
            title_api_name=cls.first_up(api.graphql_name),
            base_api=base_api,
            type=str(type_),
            api_name=api.name
        )

    @classmethod
    def write_import(cls, module_name, query_or_mutation):
        return '''\
from graphqlapiobject import graphql_api_object, GraphqlOperationAPi, GraphqlUpdateApi, GraphqlQueryListAPi, GraphqlQueryAPi
from ..%s import %s


''' % (module_name, str(query_or_mutation))

    @classmethod
    def write_init(cls, type_, des_name_):
        return '''\
from .%s import *
''' % "_".join([type_, des_name_])


def make_package(des_name_):
    os.mkdir(path=des_name_)
    with open(os.path.join(des_name_, "__init__.py"), "w") as f:
        f.write(GenCode.write_init("Query", des_name_))
        f.write(GenCode.write_init("Mutation", des_name_))


def gen(module_name, des_name_):
    schema = importlib.import_module(module_name)

    def gen_writer(file_path, des_name, type_):
        return open(os.path.join(des_name_, "_".join([str(type_), des_name])) + ".py", "w")

    def iter_create(query_or_mutation):
        writer = gen_writer(module_name, des_name_, query_or_mutation)
        writer.write(GenCode.write_import(module_name, query_or_mutation))

        for i in query_or_mutation.__field_names__:
            api = getattr(query_or_mutation, i)
            # print(api)
            writer.write(GenCode.write_class(query_or_mutation, api))
        writer.close()

    make_package(des_name_)
    iter_create(schema.Query)
    iter_create(schema.Mutation)


def main():
    parser = argparse.ArgumentParser(description='code_gen modules names')
    parser.add_argument('module_name', type=str, help='依据什么schema生成api')
    parser.add_argument('des_name', type=str, help='生成的api的存放地址')

    args = parser.parse_args()
    gen(args.module_name, args.des_name)
