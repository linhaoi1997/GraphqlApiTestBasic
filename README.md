### 使用步骤

**1. 根据schema快速生成graphql接口**

```
python \
    -m sgqlc.introspection \
    --exclude-deprecated \
    --exclude-description \
    https://your_url/graphql/ \
    platform_schema.json || exit 1

sgqlc-codegen schema platform_schema.json platform_schema.py;
```
ps: 如果报错无法识别https，安装证书也许可以解决
```
bash /Applications/Python*/Install\ Certificates.command
```

**2.  生成的代码中包含我们要用到的两个重要的类`Query`和`Mutation`包含所有的接口**
```python
class Query(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('bi_file', 'bi_explore','me', 'company_admin_users', 'platform_admin_users', 'users', 'platform_user_list', 'user', 'user_template', 'export_user', 'support_users') # 等等等等
    bi_file = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(File)), graphql_name='biFile', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='id', default=None)),
))
    )
    bi_explore = sgqlc.types.Field(sgqlc.types.non_null(JSON), graphql_name='biExplore', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(JSON), graphql_name='input', default=None)),
))
    )
```

**3. 在sgqlc的基础上进一步进行封装,继承字GraphqlApi的类，定义属性api指定是哪一个api可以快速定义api object**

```python
from ApiTestBasic import GraphqlApi, Decorator, GenParams, GraphqlApiExtension
from Schema.platform_schema import Query, platform_schema, Mutation
from ApiTestBasic import BaseUser
from sgqlc.operation import Operation


class User(BaseUser):
    def __init__(self, login):
        super(User, self).__init__("url", Mutation, login)
        self.id_ = None

    @property
    def id(self):
        if not self.id_:
            op = Operation(Query)
            op.me()
            self.id_ = self.f("me", op).me.id
        return self.id_


admin_user = User({"account": "account", "password": "password"})


class SpareParts(GraphqlApiExtension.GraphqlQueryListAPi):
    api = Query.spare_parts


class CreateThing(GraphqlApi):
    api = Mutation.create_thing

    @Decorator.set_query()
    def create(self, **kwargs):
        GenParams(platform_schema).gen(self.api)
        self.api(**kwargs)

    def test(self):
        print(self.register_api)


print(CreateThing(admin_user).create(name="name").result)

```
- 其中 `@Decorator.set_query()` 指定接口要返回的query
- `GenParams(platform_schema).gen(self.api)` 根据schema自动生成参数，免于关注不必要的参数
- "fake_user"应该穿入User的类，User是带有token的一个client，因为业务多数情况下要做多用户的接口测试，把接口和client分开是比较有利的
- 接口发送后，把返回的`result`存储在属性`result`中，经过sgqlc处理返回的是schema中定义的返回类型，比较方便的是返回的是对象，属性代表其的深层结构

**4. 发送参数和返回结果**

 （1）以eam为例，通过ApiTestBasic使用api object进行接口自动化测试可以写出这样的接口类，并进行调用
 ```python
from ApiTestBasic import GraphqlApi, BaseUser
from Schema.platform_schema import Query, platform_schema, Mutation

user = BaseUser("https://test.teletraan.io/graphql/", Mutation, {"account": "admin", "password": "teletraan"})

class Apps(GraphqlApi):
    api = Query.apps

a = Apps(user)
print(a.run().result)
AppList(data=[App(id='2', name='***', code='jhdv', key='c10c7cd3-27c7-4666-92b6-46b426e01493', description=None, url='/app/jhdv', is_admin=None), 1], total_count=32)
```
（2）返回结果简单取值
```python
print(result.data.name)
# 返回结果
['***']
```
（3）并可以自动生成接口参数，并简单的修改

```python
from ApiTestBasic import GenParams
from Schema.platform_schema import platform_schema, Query, Mutation

gen = GenParams(platform_schema)
var1 = gen.gen(Query.apps)
var1.offset = 1
var1.omit.companyIDs = [1, 2, 3]
print(var1)
# 返回结果
{'offset': 1, 'limit': 4500, 'filter': {'search': 'search_a19mp'}, 'omit': {'companyIDs': [1, 2, 3]}}
```

**5. 根据业务总结有5种接口类型扩展，可以看情况选择继承**

```python
class GraphqlApiExtension:
    GraphqlQueryListAPi = GraphqlQueryListAPi # 查询列表类的接口
    GraphqlQueryAPi = GraphqlQueryAPi # 查询单个资源的接口
    GraphqlOperationAPi = GraphqlOperationAPi # 创建资源/复杂参数的接口，内部有方法自动生成参数
    GraphqlUpdateAPi = GraphqlUpdateAPi # 更新类型的接口
```
