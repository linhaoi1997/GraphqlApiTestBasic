### 使用步骤
**0.安装**

```shell
pip install graphqlapiobject
```


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

**2. 生成的代码中包含我们要用到的两个重要的类`Query`和`Mutation`包含所有的接口,可以从生成的py文件中找到**

**3. 在sgqlc的基础上进一步进行封装,继承字GraphqlApi的类，定义属性api指定是哪一个api可以快速定义api object,并自由设定query**

```python
import json
import logging
import allure
from GraphqlApiObject import BaseUser, GraphqlQueryListAPi, pformat
from Schema.PlatformSchema.platform_schema import Mutation, Query


class QueryUsers(GraphqlQueryListAPi):
    api = Query.users


@allure.story("测试query")
class TestGraphqlQuery:

    def setup_class(self):
        self.user = BaseUser("https://yoururl/graphql/", Mutation,
                             {"account": "account", "password": "password"})

    @allure.title("正常query发送接口")
    def test1(self):
        q = QueryUsers(self.user)
        logging.info(q.set("__fields__").run().result)
        assert q.result.data
        logging.info(q.query_ids().result)
        assert q.result.data
        logging.info(pformat(json.dumps(q.data)))

```

- 其中 `set方法` 指定接口要返回的query
- "fake_user"应该穿入User的类，User是带有token的一个client，因为业务多数情况下要做多用户的接口测试，把接口和client分开是比较有利的
- 接口发送后，把返回的`result`存储在属性`result`中，经过sgqlc处理返回的是schema中定义的返回类型，比较方便的是返回的是对象， 属性代表其的深层结构
- 原始数据存储在data属性

**4. 发送参数和返回结果**

（1）发送参数可以使用自动生成参数的方式，并通过path进行修改参数

 ```python
import allure
import logging
from GraphqlApiObject import BaseUser, GraphqlOperationAPi
from Schema.PlatformSchema.platform_schema import Mutation


class CreateUser(GraphqlOperationAPi):
    api = Mutation.create_user


@allure.story("测试query")
class TestGraphqlQuery:

    def setup_class(self):
        self.user = BaseUser("https://yoururl/graphql/", Mutation,
                             {"account": "account", "password": "password"})
        self.user_id = "5ba962f5-cb17-4663-9c71-23774d911f8d"
        self.user_name = "4公司1普通员工"

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
```

（2）返回结果使用jmespath进行取值，封装在capture方法中

```python
import logging

import allure
import pytest

from GraphqlApiObject import BaseUser, GraphqlQueryListAPi
from Schema.PlatformSchema.platform_schema import Mutation, Query


class QueryUsers(GraphqlQueryListAPi):
    api = Query.users


@allure.story("测试query")
class TestGraphqlQuery:

    def setup_class(self):
        self.user = BaseUser("https://yoururl/graphql/", Mutation,
                             {"account": "account", "password": "password"})
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

```

**5. 根据业务总结有4种接口类型，可以看情况选择继承**

```python
from GraphqlApiObject import GraphqlApi, GraphqlOperationAPi, GraphqlQueryAPi, GraphqlQueryListAPi


class GraphqlApiTest(GraphqlApi): ...  # 没有特殊处理的，可以直接使用发送接口


class GraphqlQueryAPiTest(GraphqlQueryAPi): ...  # 查询单个资源的接口，参数只有id一个


class GraphqlOperationAPiTest(GraphqlOperationAPi): ...  # 可以进行自动生成参数，对复杂参数可以继承这个接口类


class GraphqlQueryListAPiTest(GraphqlQueryListAPi): ...  # 查询列表数据，参数为limit，offset，filter，可以全量查询和查询想要查询的部分
```

**PS:更多详细使用方法参考Test测试例子**
