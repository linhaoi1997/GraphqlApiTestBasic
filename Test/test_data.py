import random

from GraphqlApiObject.BaseOperator.base_data import BaseData


class RealCompany:

    def __init__(self, name):
        print("create")

        self.name = name


class Company:

    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        if not instance.__dict__.get(self.name):
            setattr(instance, self.name, RealCompany(self.name + random.choice("123abcdefghigklmn")))
        return instance.__dict__.get(self.name)
        # print("get")
        # return RealCompany(self.name + random.choice("123"))


class Data(BaseData):
    company1 = Company("company1")

    def setup(self):
        print("mysetup")


def test():
    data = Data()
    print(data.company1.name)
    print(data.company1.name)
    data2 = Data(data)
    print(data2.company1.name)
    print(data2.company1.name)
