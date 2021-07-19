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
AppList(data=[App(id='2', name='金华工业互联网平台', code='jhdv', key='c10c7cd3-27c7-4666-92b6-46b426e01493', description=None, url='/app/jhdv', is_admin=None), App(id='13', name='企业运营总览', code='chart', key='88234d95-6f7d-4a85-b7cb-c02a14af108e', description='自助式BI分析，数据可视化，报表统计，数据填报，多用户权限分配与管理，报表推送计划', url='http://52.83.254.8:51980', is_admin=None), App(id='12', name='智慧安防', code='seely', key='6e740b69-f80a-4685-8130-0c5450e1bb52', description='人脸识别门禁、访客管理系统、车辆识别、人脸识别防入侵、实时移动端消息推送', url='https://tv.teletraan.io', is_admin=None), App(id='27', name='帮扶平台', code='bangfu', key='d8b9f58c-9455-4d71-a928-2f6b6d327a28', description=None, url=None, is_admin=None), App(id='30', name='机理模型管理', code='metaadmin', key='372585f1-d1d4-4ec0-97d7-71615365dc3c', description=None, url='/meta-admin', is_admin=None), App(id='1', name='行业信息总览', code='macro', key='72a989ae-f3af-486a-85ca-9f0b7169b58d', description='从宏观角度对全市、全区企业的总览。包括能源数据、企业用能、企业经营分析、设备分析等模块', url=None, is_admin=None), App(id='22', name='企业指标', code='index', key='aae6215a-86e8-4bc2-8fc7-9143d5b0f31c', description='展示企业各种状态指标，从各个维度分析展示企业现状，包括开机率、作业率、利用率、尖峰率等，并能根据各维度进行分析管理', url=None, is_admin=None), App(id='40', name='生产管理(工艺优化)', code='propt', key='e9383abc-7596-48d1-bfd6-f47ce2fd11b3', description=None, url='https://propt.teletraan.io', is_admin=None), App(id='3', name='能源管理总览', code='energy', key='ca0b5a6f-5767-4f84-b8d1-32f17f0c37bd', description='为整个平台使用用户提供能源管理、能源对标、能源绩效、能源计划、重点设备能源分析等服务。帮助管理者从不同维度了解企业能耗状况。', url=None, is_admin=None), App(id='43', name='BI', code='bi', key='ca7eb00f-158a-4853-83dc-53cd67b6a472', description=None, url=None, is_admin=None), App(id='25', name='故障检测', code='fdi', key='2f2bccd5-c416-41d0-ba3e-91ea0bfc7878', description=None, url=None, is_admin=None), App(id='5', name='生产管理', code='pms', key='5f7420a8-a03f-4db3-9fa4-d86b8ee66d47', description='用于销售、管理人员对订单的整个生产情况进行跟踪。订单跟踪能及时、准确、方便的帮助销售和管理人员掌控生产情况，对相应的决策提供有力的依据和支撑', url=None, is_admin=None), App(id='35', name='生产任务管理', code='hypms', key='98d08136-d6bc-4b31-acdb-35807d7e947c', description=None, url=None, is_admin=None), App(id='6', name='生产设备管理', code='cockpit', key='074284f9-aef7-4404-a9de-6d412eac9ca9', description='通过设备状态，设备指标及设备详情的实时综合呈现和历史数据分析，展示整个企业的生产状态。帮助管理者了解生产情况，协助制定生产计划。', url=None, is_admin=None), App(id='7', name='系统工单管理', code='issue', key='c3642909-a231-428c-ae0a-6be93409cc90', description=None, url=None, is_admin=None), App(id='8', name='设备配置管理', code='eam', key='d05b5e5c-29f5-4c13-90fe-5d4c00bde94d', description='管理设备信息，提供设备资产远程监控、故障告警；数据资产管理等服务。并且能够定制巡检、保养服务。', url=None, is_admin=None), App(id='44', name='生产设备维护', code='pdm', key='7c4f45d3-6b86-4f90-912f-09de019b7829', description='设备实时监控和诊断，设备故障预警与预测，故障根本原因分析及操作建议，维修计划制定及工单下达，提供专家系统', url=None, is_admin=None), App(id='10', name='元数据管理', code='thing-access', key='7e131532-4b56-45f2-9a86-da9b0535bf9d', description=None, url=None, is_admin=None), App(id='38', name='群升5G+智慧工厂', code='qunsheng', key='5be175e4-6f89-4911-862f-3412ebbb14d8', description=None, url='/app/dv?id=3', is_admin=None), App(id='21', name='今飞5G+智慧工厂', code='jinfei', key='36d11428-7728-4d43-b2d3-d965a758a173', description=None, url='/app/dv?id=12', is_admin=None), App(id='18', name='杭机5G+智慧工厂', code='hangji', key='e13c8243-05a6-464e-85e3-4923ed38b9da', description=None, url='/app/dv?id=16', is_admin=None), App(id='11', name='东磁5G+智慧工厂', code='dongci', key='df0ed032-2d4c-4911-8c36-34592fad289a', description=None, url='/app/dongci', is_admin=None), App(id='47', name='浦江工业互联网平台', code='pujiang', key='f0723883-42ce-43a6-820e-e31075c44d68', description='浦江工业互联网平台', url='https://static-f0723883-42ce-43a6-820e-e31075c44d68.bspapp.com/#/pages/menu/menuList', is_admin=None), App(id='26', name='产教平台', code='chanjiao', key='20376593-829f-4666-8b5a-43d4467bc73b', description=None, url=None, is_admin=None), App(id='46', name='轻骑兵', code='qingqibin', key='983656c2-885d-423a-b4ba-0c9dec8e81e6', description='轻骑兵', url='http://211.140.151.142:88/d/SkJQay5Mk/jin-hua-dong-ci-5gbo-ce-xi-tong?orgId=1&refresh=30s', is_admin=None), App(id='33', name='5G商城', code='5G', key='054ec0a1-b3e2-428a-98e9-736803c95aeb', description=None, url='http://open5g.cmccopen.cn/', is_admin=None), App(id='24', name='SIM卡管理', code='sim', key='eba49012-c2c1-47d2-980c-cbd6df52a43c', description=None, url=None, is_admin=None), App(id='37', name='数据录入', code='data', key='65c687f6-8442-48b0-8fa0-7a56942958d5', description=None, url=None, is_admin=None), App(id='23', name='设备接入', code='yidong', key='f470c52e-f20d-4bac-9bc5-095526f94738', description='管理设备基础信息和档案，备件关联及备件库，自定义维修保养与巡检，库存监控和预警，设备数据分析，云端设备控制，SCADA，故障预测与预警', url='http://52.83.254.8:9999', is_admin=None), App(id='15', name='危险品安监系统', code='weihuaanjian', key='c88ba6e5-6b65-49df-8794-ddadc077e1e6', description='重大危险源检测预警，安全生产全流程管理，企业安全风险分区管理，生产人员在岗在位管理', url='http://52.83.254.8:9501/', is_admin=None), App(id='16', name='化工业可视化', code='chemical', key='4dfcd260-cf4a-42e8-b169-5e54974e25d6', description='用于展示化工行业主要特性数据，诸如设备情况、产品情况、原料情况、订单情况等，并配合警报机制进行警报监管，帮助企业借助BI可视化技术进行企业生产', url='http://52.83.254.8:9999/charts/industry/', is_admin=None), App(id='17', name='纺织业可视化', code='sewing', key='92991421-3175-4042-9900-efa24c2b3d1a', description='用于展示纺织行业企业重点关注数据，包括设备效率、停机状况、生产效率、库存情况等，并可以实时监控企业设备连接状态，借助BI技术，帮助企业实时全面掌握企业生产动态', url='http://52.83.254.8:9999/charts/textile/', is_admin=None)], total_count=32)
```
（2）返回结果简单取值
```python
print(result.data.name)
# 返回结果
['金华工业互联网平台', '企业运营总览', '智慧安防', '帮扶平台', '机理模型管理', '行业信息总览', '企业指标', '生产管理(工艺优化)', '能源管理总览', 'BI', '故障检测', '生产管理', '生产任务管理', '生产设备管理', '系统工单管理', '设备配置管理', '生产设备维护', '元数据管理', '群升5G+智慧工厂', '今飞5G+智慧工厂', '杭机5G+智慧工厂', '东磁5G+智慧工厂', '浦江工业互联网平台', '产教平台', '轻骑兵', '5G商城', 'SIM卡管理', '数据录入', '设备接入', '危险品安监系统', '化工业可视化', '纺织业可视化']
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

var2 = gen.gen(Mutation.create_thing)
var2.input.images.id=[1,2,3]
print(var2)
# 返回结果
{'input': {'code': 'BZD6341', 'sap': 'sap_yq3gj', 'name': 'Janet Simmons', 'model': 'model_folhp', 'desc': 'desc_qskwd', 'manufacturer': '罗技', 'distributor': '经销商1', 'purchasedAt': 1620788694381, 'activatedAt': 1620788694381, 'purchasedPrice': -787807117.0, 'yearsOfUse': 451430985.0, 'usedYear': -218611309129582.0, 'predictResidualRate': 85096.69979, 'depreciationRate': 9407172.413558, 'category': '辅助设备', 'factory': '测试工厂', 'purpose': '辅助', 'repairContacts': [{'id': 1}, {'id': 1}, {'id': 1}], 'usingStatus': 'using_status_m1tsq', 'addition': '[]', 'images': [{'id': 1}, {'id': 2}, {'id': 3}], 'spareParts': [{'id': 1}, {'id': 1}, {'id': 1}], 'attachments': [{'id': 1}, {'id': 1}, {'id': 1}], 'accessKey': 'access_key_uvc7e', 'organization': {'id': 1}, 'type': {'id': 1}, 'energyGroup': {'id': 1}, 'thingGroup': {'id': 1}}}
```

**5. 根据业务总结有5种接口类型扩展，可以看情况选择继承**

```python
class GraphqlApiExtension:
    GraphqlQueryListAPi = GraphqlQueryListAPi # 查询列表类的接口
    GraphqlQueryAPi = GraphqlQueryAPi # 查询单个资源的接口
    GraphqlOperationAPi = GraphqlOperationAPi # 创建资源/复杂参数的接口，内部有方法自动生成参数
    GraphqlUpdateAPi = GraphqlUpdateAPi # 更新类型的接口
```
