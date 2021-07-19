import sgqlc.types


platform_schema = sgqlc.types.Schema()



########################################################################
# Scalars and Enumerations
########################################################################
class AggregationFrame(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('MONTH', 'WEEK', 'WORKDAY', 'DAY', 'EVERY_DAY_RANGE', 'HOUR')


class AuditSparePartOutboundAction(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('APPROVE', 'REJECT')


class AuditThingRepairAction(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('APPROVE_REPAIR', 'REJECT_REPAIR', 'APPROVE_FEEDBACK', 'REJECT_FEEDBACK', 'STOP')


class AuthenticationStatus(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('CERTIFIED', 'REJECTED', 'PENDING')


class BIDataSourceType(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('PLATFORM', 'PRIVATE', 'FILE')


Boolean = sgqlc.types.Boolean

class CardType(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('IMAGE', 'TEXT', 'CARD', 'TAB')


class CockpitKeyStatistic(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('AVG', 'SUM', 'LAST')


class CockpitKeyType(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('REAL_TIME', 'STATISTIC')


class CompanyDemandStatus(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('APPROVED', 'REJECTED', 'PENDING')


class CompanyReviewOperation(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('APPROVE', 'REJECT')


class CourseSignStatus(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('UNDER_REVIEW', 'APPROVED', 'REJECTED')


class CourseStatus(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('SIGN_UP_SOON', 'SIGNING_UP', 'CLOSED', 'SIGN_UP_END')


class DataType(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('INT', 'FLOAT', 'STRING', 'BOOL')


class EnergyType(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('ELECTRICITY',)


class FalutLevel(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('LOW', 'MEDIUM', 'HIGH')


class FaultIssueAction(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('ACCEPT', 'REMARK', 'TRANSFER', 'CLOSE', 'REOPEN')


class FaultIssueStatus(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('READY', 'DEALING', 'CLOSE')


class FaultType(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('AGING', 'ABNORMAL_TEMPERATURE', 'ABNORMAL_POWER', 'OTHER')


class FieldType(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('DESCRIPTION', 'TEXT', 'DATETIME', 'NUMBER', 'CONTACT', 'IMAGE', 'ATTACHMENT', 'SINGLE_SELECTION', 'MULTI_SELECTION')


Float = sgqlc.types.Float

class FuncType(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('SUM', 'MAX')


class Gender(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('MALE', 'FEMALE')


class Granularity(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('MINUTE', 'FIVE_MINUTE', 'HOURLY', 'DAILY', 'MONTHLY', 'ANNUALLY', 'WEEKLY')


ID = sgqlc.types.ID

Int = sgqlc.types.Int

class InterfaceType(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('Ethernet', 'Serial232', 'Serial485')


class IssueAction(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('DEAL', 'REMARK', 'TRANSFER', 'CLOSE', 'REOPEN')


class IssueCategory(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('SYSTEM', 'EDUCTION', 'HELP')


class IssueReason(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('OTHER', 'ABNORMAL_DATA', 'SLOW_LOADING')


class IssueStatus(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('READY', 'DEALING', 'CLOSE')


class IssueType(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('OTHER', 'ABNORMAL_DATA', 'SLOW_LOADING')


class JSON(sgqlc.types.Scalar):
    __schema__ = platform_schema


class JSONString(sgqlc.types.Scalar):
    __schema__ = platform_schema


class JunyeMetricKind(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('TEMPERATURE', 'PRESSURE', 'FLOW', 'LIQUID_LEVEL', 'CURRENT_FEEDBACK', 'FREQUENCY_FEEDBACK')


class JunyeMetricUnit(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('CELSIUS_DEGREE', 'MEGA_PASCAL', 'CUBIC_METER_PER_HOUR', 'METER', 'AMPERE', 'HERTZ')


class LifeCycle(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('NORMAL', 'SILENT', 'PAUSE', 'OTHER')


class MarketAppType(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('RESEARCH_DESIGN', 'MANUFACTURING', 'MAINTENANCE_SERVICE', 'SAFETY_PRODUCTION', 'SUPPLY_CHAIN_MANAGEMENT', 'WAREHOUSE_AND_LOGISTICS', 'OPERATION_MANAGEMENT', 'QUALITY_CONTROL', 'ENERGY_SAVING')


class MarketConsultationType(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('APP', 'SOLUTION')


class MarketIssueAction(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('ACCEPT', 'FOLLOW', 'TRANSFER', 'CLOSE', 'REOPEN')


class MarketIssueStatus(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('READY', 'DEALING', 'CLOSE')


class MarketSolutionType(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('RESEARCH_DESIGN', 'MANUFACTURING', 'MAINTENANCE_SERVICE', 'SAFETY_PRODUCTION', 'SUPPLY_CHAIN_MANAGEMENT', 'WAREHOUSE_AND_LOGISTICS', 'OPERATION_MANAGEMENT', 'QUALITY_CONTROL', 'ENERGY_SAVING')


class MaterialType(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('OUTCOME', 'RAW')


class NotificationKind(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('APP', 'PLATFORM')


class OrderStatus(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('DRAFT', 'UN_PLANED', 'PLANED', 'FINISHED')


class PeriodFrequency(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('DAY', 'WEEK', 'TWO_WEEK', 'MONTH', 'THREE_MONTH')


class PeriodType(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('SINGLE', 'LIMITED', 'INFINITE')


class PermissionDataRange(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('ALL', 'OWN')


class PermissionType(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('APP_MENU', 'PLATFORM_MENU', 'FUNCTION')


class ProductionMachineStatus(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('RUNNING', 'STANDBY', 'STOP')


class ProductionPlanStatus(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('DRAFT', 'UN_START', 'IN_PROGRESS', 'FINISHED')


class ProductionScheduleAction(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('INSERT', 'DELETE', 'UPDATE')


class ProductionTicketPriority(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('P1', 'P2')


class ProductionTicketStatus(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('TO_ARRANGE', 'ARRANGED', 'TO_PRODUCE', 'COMPLETE', 'DELAY', 'PAUSE')


class RecruitJobSignStatus(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('PENDING', 'ADMITTED', 'REJECTED')


class RecruitJobStatus(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('AUDITING', 'REJECTED', 'APPROVED', 'FINISHED')


class RecruitStudentStatus(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('NOT_SIGN', 'PENDING', 'ADMITTED')


class RegisterStatus(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('PENDING', 'REJECTED', 'APPROVED')


class RelationType(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('ONE_TO_ONE', 'ONE_TO_MANY')


class ReviewTrainSchoolRecruitTaskAction(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('APPROVE', 'REJECT', 'CANCEL')


class RoleScope(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('PLATFORM', 'COMPANY_ADMIN')


class RouterConfigurationStatus(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('SUCCESS', 'FAIL', 'NULL')


class RouterStatus(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('ONLINE', 'OFFLINE')


class RouterThingStatus(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('ONLINE', 'OFFLINE')


class SourceRegister(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('Q', 'I', 'M', 'DB', 'T', 'C', 'V')


class SourceType(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('BIT', 'HEX', 'USHORT', 'SHORT', 'ULONG', 'LONG', 'BYTE', 'STRING', 'FLOAT', 'WFLOAT', 'DWFLOAT', 'UWFLOAT', 'UDWFLOAT')


class SparePartOutboundStatus(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('APPROVED', 'REJECTED', 'PENDING')


class SparePartSummaryField(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('NUMBER', 'VALUE')


String = sgqlc.types.String

class ThingGroupAlterOperation(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('ADD', 'REMOVE')


class ThingInspectionNumberCriteria(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('GT_LOWER_LT_UPPER', 'GE_LOWER_LT_UPPER', 'GE_LOWER_LE_UPPER', 'GT_LOWER_LE_UPPER', 'GE', 'GT', 'LE', 'LT', 'EQUAL', 'NOTEQUAL')


class ThingInspectionResult(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('NORMAL', 'ABNORMAL')


class ThingInspectionStatus(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('PENDING', 'INPROGRESS', 'UNDERREVIEW', 'FINISHED')


class ThingInspectionSubItemCategory(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('NORMAL', 'NUMBER')


class ThingMaintenanceStatus(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('PENDING', 'MAINTAINING', 'UNDERREVIEW', 'FINISHED')


class ThingRateType(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('OEE', 'OPERATION_RATE', 'PERFORMANCE_RATE', 'YIELD_RATE')


class ThingRepairStatus(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('REJECT', 'DISPATCHING', 'REPAIRING', 'FEEDBACK', 'FINISHED', 'STOP')


class ThingStatusType(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('OPERATION', 'STANDBY', 'ALARM', 'SHUTDOWN')


class Timestamp(sgqlc.types.Scalar):
    __schema__ = platform_schema


class TrainCourseRoundCategory(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('SIGN_RECORD', 'COURSE')


class TrainSchoolRecruitTaskRecordStatus(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('SIGNED', 'UN_SIGN')


class TrainSchoolRecruitTaskReviewStatus(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('PENDING', 'APPROVED', 'REJECTED')


class TrainSchoolRecruitTaskStatus(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('PENDING', 'IN_PROGRESS', 'END')


class TrainStudentStatus(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('NORMAL', 'ENLISTMENT', 'SUSPENSION', 'QUIT', 'PROMOTION')


class UpdateThingInspectionStatusAction(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('START_INSPECTION', 'COMMIT', 'APPROVE_FEEDBACK', 'REJECT_FEEDBACK')


class UpdateThingMaintenanceStatusAction(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('START_MAINTENANCE', 'APPROVE_FEEDBACK', 'REJECT_FEEDBACK')


class Upload(sgqlc.types.Scalar):
    __schema__ = platform_schema


class UserOrigin(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('REGISTED', 'ADDED')


class UserType(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('COMPANY_ADMIN', 'COMPANY_NORMAL', 'PLATFORM_ADMIN', 'JIN_HUA_SCHOOL')


class WorkGroupStatus(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('PRODUCTION', 'ON_DUTY', 'FREE')


class WorkbenchType(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('REMINDER', 'WARNING', 'NAVIGATION', 'THING', 'SIM', 'ENERGY', 'PRODUCTIVITY', 'THING_STATUS', 'APP')


class thingGroupType(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('PERSONAL', 'DEPARTMENT')



########################################################################
# Input Objects
########################################################################
class ActivateUserInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class AdapterFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('thing_type_id', 'company_id')
    thing_type_id = sgqlc.types.Field(ID, graphql_name='thingTypeId')
    company_id = sgqlc.types.Field(ID, graphql_name='companyId')


class AdapterModelFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('thing_mechanism_model_code', 'search')
    thing_mechanism_model_code = sgqlc.types.Field(String, graphql_name='thingMechanismModelCode')
    search = sgqlc.types.Field(String, graphql_name='search')


class AddCompanyAppsInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company_id', 'app_ids')
    company_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='companyID')
    app_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='appIDs')


class AlertFilter(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('search', 'period')
    search = sgqlc.types.Field(String, graphql_name='search')
    period = sgqlc.types.Field('PeriodFilter', graphql_name='period')


class AlertRuleFilter(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('search', 'thing', 'thing_type')
    search = sgqlc.types.Field(String, graphql_name='search')
    thing = sgqlc.types.Field('IDInput', graphql_name='thing')
    thing_type = sgqlc.types.Field('IDInput', graphql_name='thingType')


class ApplyRouterTemplateConfigurationInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('router_template_configuration', 'routers')
    router_template_configuration = sgqlc.types.Field(sgqlc.types.non_null('IDInput'), graphql_name='routerTemplateConfiguration')
    routers = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('IDInput'))), graphql_name='routers')


class AppsFilter(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('search',)
    search = sgqlc.types.Field(String, graphql_name='search')


class AppsOmit(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company_ids',)
    company_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='companyIDs')


class AssignProductionSubScheduleInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('timestamp', 'thing', 'shift', 'sub_schedule', 'priority')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='timestamp')
    thing = sgqlc.types.Field(sgqlc.types.non_null('IDInput'), graphql_name='thing')
    shift = sgqlc.types.Field(sgqlc.types.non_null('IDInput'), graphql_name='shift')
    sub_schedule = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('IDInput'))), graphql_name='subSchedule')
    priority = sgqlc.types.Field(ProductionTicketPriority, graphql_name='priority')


class AssignProductionTicketInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('timestamp', 'thing', 'shift', 'ticket', 'priority')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='timestamp')
    thing = sgqlc.types.Field(sgqlc.types.non_null('IDInput'), graphql_name='thing')
    shift = sgqlc.types.Field(sgqlc.types.non_null('IDInput'), graphql_name='shift')
    ticket = sgqlc.types.Field(sgqlc.types.non_null('IDInput'), graphql_name='ticket')
    priority = sgqlc.types.Field(ProductionTicketPriority, graphql_name='priority')


class AuditRecruitJobInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'is_approved', 'reject_reason')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    is_approved = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isApproved')
    reject_reason = sgqlc.types.Field(String, graphql_name='rejectReason')


class AuditRecruitJobSignRecordInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'is_admitted')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    is_admitted = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isAdmitted')


class AuditSparePartOutboundInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'action', 'details')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    action = sgqlc.types.Field(sgqlc.types.non_null(AuditSparePartOutboundAction), graphql_name='action')
    details = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('SparePartOutboundActualDetailInput')), graphql_name='details')


class AuditThingRepairInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'action', 'workers')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    action = sgqlc.types.Field(sgqlc.types.non_null(AuditThingRepairAction), graphql_name='action')
    workers = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('IDInput'))), graphql_name='workers')


class BIDashboardFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('search', 'is_published')
    search = sgqlc.types.Field(String, graphql_name='search')
    is_published = sgqlc.types.Field(Boolean, graphql_name='isPublished')


class BIDatasetFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('search', 'code')
    search = sgqlc.types.Field(String, graphql_name='search')
    code = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='code')


class BIFileDataSourceFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('search',)
    search = sgqlc.types.Field(String, graphql_name='search')


class BIFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('start', 'end', 'granularity', 'aggregation', 'metric', 'series')
    start = sgqlc.types.Field(Timestamp, graphql_name='start')
    end = sgqlc.types.Field(Timestamp, graphql_name='end')
    granularity = sgqlc.types.Field(Granularity, graphql_name='granularity')
    aggregation = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='aggregation')
    metric = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='metric')
    series = sgqlc.types.Field(String, graphql_name='series')


class BIPublishedDashboardFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('search',)
    search = sgqlc.types.Field(String, graphql_name='search')


class CheckAlterDepartmentThingGroupInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('current_dept', 'parent_dept', 'children_depts', 'thing_group', 'operation')
    current_dept = sgqlc.types.Field(sgqlc.types.non_null('IDInput'), graphql_name='currentDept')
    parent_dept = sgqlc.types.Field('IDInput', graphql_name='parentDept')
    children_depts = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='childrenDepts')
    thing_group = sgqlc.types.Field(sgqlc.types.non_null('IDInput'), graphql_name='thingGroup')
    operation = sgqlc.types.Field(sgqlc.types.non_null(ThingGroupAlterOperation), graphql_name='operation')


class CheckStudentInfoExistsInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('stu_no', 'identity')
    stu_no = sgqlc.types.Field(String, graphql_name='stuNo')
    identity = sgqlc.types.Field(String, graphql_name='identity')


class CockpitAggregationFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('thing_type_id',)
    thing_type_id = sgqlc.types.Field(ID, graphql_name='thingTypeId')


class CockpitKeyFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('thing_type_id',)
    thing_type_id = sgqlc.types.Field(ID, graphql_name='thingTypeId')


class CockpitThingListFilter(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('search', 'organization', 'type', 'status', 'duration_min', 'duration_max')
    search = sgqlc.types.Field(String, graphql_name='search')
    organization = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='organization')
    type = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='type')
    status = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ThingStatusType)), graphql_name='status')
    duration_min = sgqlc.types.Field(Int, graphql_name='durationMin')
    duration_max = sgqlc.types.Field(Int, graphql_name='durationMax')


class CollectConfigurationInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('collect_period', 'report_period', 'interface_type', 'channel_protocol', 'ethernet_channel', 'serial_channel', 'collect_points')
    collect_period = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='collectPeriod')
    report_period = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='reportPeriod')
    interface_type = sgqlc.types.Field(sgqlc.types.non_null(InterfaceType), graphql_name='interfaceType')
    channel_protocol = sgqlc.types.Field(sgqlc.types.non_null('IDInput'), graphql_name='channelProtocol')
    ethernet_channel = sgqlc.types.Field('EthernetChannelInput', graphql_name='ethernetChannel')
    serial_channel = sgqlc.types.Field('SerialChannelInput', graphql_name='serialChannel')
    collect_points = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('CollectPointInput'))), graphql_name='collectPoints')


class CollectPointInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('name', 'alias_name', 'register_type', 'data_type', 'addr_offset')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    alias_name = sgqlc.types.Field(String, graphql_name='aliasName')
    register_type = sgqlc.types.Field(sgqlc.types.non_null('IDInput'), graphql_name='registerType')
    data_type = sgqlc.types.Field(sgqlc.types.non_null('IDInput'), graphql_name='dataType')
    addr_offset = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='addrOffset')


class CompanyAdminPermissionInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'permission')
    company = sgqlc.types.Field(sgqlc.types.non_null('IDInput'), graphql_name='company')
    permission = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('IDInput')), graphql_name='permission')


class CompanyAdminUsersFilter(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('search', 'company_ids', 'department_ids')
    search = sgqlc.types.Field(String, graphql_name='search')
    company_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='companyIDs')
    department_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='departmentIDs')


class CompanyAppsFilter(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company_id',)
    company_id = sgqlc.types.Field(ID, graphql_name='companyID')


class CompanyBIDatasourceFilter(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'search')
    company = sgqlc.types.Field('IDInput', graphql_name='company')
    search = sgqlc.types.Field(String, graphql_name='search')


class CompanyDemandFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('search', 'start_at', 'end_at', 'company_id', 'status')
    search = sgqlc.types.Field(String, graphql_name='search')
    start_at = sgqlc.types.Field(Timestamp, graphql_name='startAt')
    end_at = sgqlc.types.Field(Timestamp, graphql_name='endAt')
    company_id = sgqlc.types.Field(Int, graphql_name='companyId')
    status = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(CompanyDemandStatus)), graphql_name='status')


class CompanyFilter(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('search', 'county', 'company_type')
    search = sgqlc.types.Field(String, graphql_name='search')
    county = sgqlc.types.Field(String, graphql_name='county')
    company_type = sgqlc.types.Field('IDInput', graphql_name='companyType')


class CompanyTypeFilter(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('search',)
    search = sgqlc.types.Field(String, graphql_name='search')


class CreateAdapterKeyInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('thing_type_id', 'key', 'desc', 'unit', 'type', 'precision', 'function')
    thing_type_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='thingTypeId')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    desc = sgqlc.types.Field(String, graphql_name='desc')
    unit = sgqlc.types.Field(String, graphql_name='unit')
    type = sgqlc.types.Field(DataType, graphql_name='type')
    precision = sgqlc.types.Field(Int, graphql_name='precision')
    function = sgqlc.types.Field(JSON, graphql_name='function')


class CreateAlertRuleInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('name', 'thing_type', 'alert_type', 'description', 'fx')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    thing_type = sgqlc.types.Field(sgqlc.types.non_null('IDInput'), graphql_name='thingType')
    alert_type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='alertType')
    description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='description')
    fx = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('FxObjectInput'))), graphql_name='fx')


class CreateAppInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('code', 'name', 'description', 'avatar')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    description = sgqlc.types.Field(String, graphql_name='description')
    avatar = sgqlc.types.Field('IDInput', graphql_name='avatar')


class CreateBIDashboardInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('name', 'component', 'extra', 'thumbnail', 'attachment')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    component = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(JSON))), graphql_name='component')
    extra = sgqlc.types.Field(sgqlc.types.non_null(JSON), graphql_name='extra')
    thumbnail = sgqlc.types.Field('IDInput', graphql_name='thumbnail')
    attachment = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='attachment')


class CreateBIDataSourceInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'type', 'database', 'name', 'code')
    id = sgqlc.types.Field(ID, graphql_name='id')
    type = sgqlc.types.Field(sgqlc.types.non_null(BIDataSourceType), graphql_name='type')
    database = sgqlc.types.Field('IDInput', graphql_name='database')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    code = sgqlc.types.Field(String, graphql_name='code')


class CreateBIDatabaseInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('name', 'uri')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    uri = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='uri')


class CreateBIDatasetInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('source',)
    source = sgqlc.types.Field(sgqlc.types.non_null(CreateBIDataSourceInput), graphql_name='source')


class CreateBIFileInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('name', 'length')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    length = sgqlc.types.Field(Int, graphql_name='length')


class CreateChanJiaoFileInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('name', 'length')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    length = sgqlc.types.Field(Int, graphql_name='length')


class CreateCockpitAggregation(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('thing_type_id', 'tag', 'frame', 'start', 'end')
    thing_type_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='thingTypeId')
    tag = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='tag')
    frame = sgqlc.types.Field(AggregationFrame, graphql_name='frame')
    start = sgqlc.types.Field(String, graphql_name='start')
    end = sgqlc.types.Field(String, graphql_name='end')


class CreateCockpitKey(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('thing_type_id', 'key', 'key_type', 'name', 'unit', 'type', 'precision')
    thing_type_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='thingTypeId')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    key_type = sgqlc.types.Field(sgqlc.types.non_null(CockpitKeyType), graphql_name='keyType')
    name = sgqlc.types.Field(String, graphql_name='name')
    unit = sgqlc.types.Field(String, graphql_name='unit')
    type = sgqlc.types.Field(DataType, graphql_name='type')
    precision = sgqlc.types.Field(Int, graphql_name='precision')


class CreateCockpitTargetInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('timestamp', 'company', 'organization', 'oee', 'operation_rate', 'performance_rate', 'yield_rate')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='timestamp')
    company = sgqlc.types.Field(ID, graphql_name='company')
    organization = sgqlc.types.Field(ID, graphql_name='organization')
    oee = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='OEE')
    operation_rate = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='operationRate')
    performance_rate = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='performanceRate')
    yield_rate = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='yieldRate')


class CreateCompanyAdminUserInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('account', 'name', 'company', 'phone', 'email')
    account = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='account')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    company = sgqlc.types.Field(sgqlc.types.non_null('IDInput'), graphql_name='company')
    phone = sgqlc.types.Field(String, graphql_name='phone')
    email = sgqlc.types.Field(String, graphql_name='email')


class CreateCompanyBIDatasourceInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('datasource', 'company')
    datasource = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('IDInput'))), graphql_name='datasource')
    company = sgqlc.types.Field(sgqlc.types.non_null('IDInput'), graphql_name='company')


class CreateCompanyDemandInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('name', 'is_public', 'content', 'phone', 'email', 'company_id', 'company_name')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    is_public = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isPublic')
    content = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='content')
    phone = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='phone')
    email = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='email')
    company_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='companyId')
    company_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='companyName')


class CreateCompanyInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('type', 'name', 'address', 'uscc', 'contact', 'email', 'phone', 'province', 'city', 'county')
    type = sgqlc.types.Field(sgqlc.types.non_null('IDInput'), graphql_name='type')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    address = sgqlc.types.Field(String, graphql_name='address')
    uscc = sgqlc.types.Field(String, graphql_name='uscc')
    contact = sgqlc.types.Field(String, graphql_name='contact')
    email = sgqlc.types.Field(String, graphql_name='email')
    phone = sgqlc.types.Field(String, graphql_name='phone')
    province = sgqlc.types.Field(String, graphql_name='province')
    city = sgqlc.types.Field(String, graphql_name='city')
    county = sgqlc.types.Field(String, graphql_name='county')


class CreateDepartmentInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('name', 'parent')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    parent = sgqlc.types.Field(sgqlc.types.non_null('IDInput'), graphql_name='parent')


class CreateDeviceChannelConfigurationInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('name', 'router', 'collect', 'company')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    router = sgqlc.types.Field(sgqlc.types.non_null('IDInput'), graphql_name='router')
    collect = sgqlc.types.Field(sgqlc.types.non_null(CollectConfigurationInput), graphql_name='collect')
    company = sgqlc.types.Field('IDInput', graphql_name='company')


class CreateDirectoryInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('name', 'parent')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    parent = sgqlc.types.Field('IDInput', graphql_name='parent')


class CreateEamFileInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('name', 'length')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    length = sgqlc.types.Field(Int, graphql_name='length')


class CreateEnergyGroup(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('name',)
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class CreateFaultFileInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('name', 'length')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    length = sgqlc.types.Field(Int, graphql_name='length')


class CreateFaultFxObjectInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('ast', 'result')
    ast = sgqlc.types.Field(sgqlc.types.non_null(JSONString), graphql_name='ast')
    result = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='result')


class CreateFaultIssueReasonInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('reason', 'caused_reason', 'solutions')
    reason = sgqlc.types.Field(sgqlc.types.non_null('IDInput'), graphql_name='reason')
    caused_reason = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='causedReason')
    solutions = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='solutions')


class CreateFaultReasonInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('rule', 'content')
    rule = sgqlc.types.Field(sgqlc.types.non_null('IDInput'), graphql_name='rule')
    content = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='content')


class CreateFaultRuleInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('thing_type', 'name', 'type', 'desc', 'reasons', 'fx')
    thing_type = sgqlc.types.Field(sgqlc.types.non_null('IDInput'), graphql_name='thingType')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    type = sgqlc.types.Field(sgqlc.types.non_null(FaultType), graphql_name='type')
    desc = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='desc')
    reasons = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('CreateFaultRuleReasonInput'))), graphql_name='reasons')
    fx = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CreateFaultFxObjectInput))), graphql_name='fx')


class CreateFaultRuleReasonInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('content',)
    content = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='content')


class CreateFaultSolutionInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('title', 'directory', 'brief', 'reasons', 'content', 'attachments')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    directory = sgqlc.types.Field(sgqlc.types.non_null('IDInput'), graphql_name='directory')
    brief = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='brief')
    reasons = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='reasons')
    content = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='content')
    attachments = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='attachments')


class CreateFileInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('name', 'length')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    length = sgqlc.types.Field(Int, graphql_name='length')


class CreateImageInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('name', 'length')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    length = sgqlc.types.Field(Int, graphql_name='length')


class CreateIssueInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('title', 'content', 'attachments')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    content = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='content')
    attachments = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='attachments')


class CreateMarketAppInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('title', 'type', 'cover_image', 'is_recommended', 'brief', 'description', 'screenshot')
    title = sgqlc.types.Field(String, graphql_name='title')
    type = sgqlc.types.Field(sgqlc.types.non_null(MarketAppType), graphql_name='type')
    cover_image = sgqlc.types.Field('IDInput', graphql_name='coverImage')
    is_recommended = sgqlc.types.Field(Boolean, graphql_name='isRecommended')
    brief = sgqlc.types.Field(String, graphql_name='brief')
    description = sgqlc.types.Field(String, graphql_name='description')
    screenshot = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='screenshot')


class CreateMarketFileInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('name', 'length')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    length = sgqlc.types.Field(Int, graphql_name='length')


class CreateMarketIssueInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('app', 'solution', 'type', 'company_name', 'contact', 'phone', 'email', 'content')
    app = sgqlc.types.Field('IDInput', graphql_name='app')
    solution = sgqlc.types.Field('IDInput', graphql_name='solution')
    type = sgqlc.types.Field(sgqlc.types.non_null(MarketConsultationType), graphql_name='type')
    company_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='companyName')
    contact = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='contact')
    phone = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='phone')
    email = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='email')
    content = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='content')


class CreateMarketSolutionDetailInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('title', 'items', 'image', 'content', 'type')
    title = sgqlc.types.Field(String, graphql_name='title')
    items = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('MarketCommonComponentInput')), graphql_name='items')
    image = sgqlc.types.Field('IDInput', graphql_name='image')
    content = sgqlc.types.Field(String, graphql_name='content')
    type = sgqlc.types.Field(sgqlc.types.non_null(CardType), graphql_name='type')


class CreateMarketSolutionInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('title', 'cover_image', 'type', 'is_recommended', 'brief', 'description', 'app', 'detail')
    title = sgqlc.types.Field(String, graphql_name='title')
    cover_image = sgqlc.types.Field('IDInput', graphql_name='coverImage')
    type = sgqlc.types.Field(sgqlc.types.non_null(MarketSolutionType), graphql_name='type')
    is_recommended = sgqlc.types.Field(Boolean, graphql_name='isRecommended')
    brief = sgqlc.types.Field(String, graphql_name='brief')
    description = sgqlc.types.Field(String, graphql_name='description')
    app = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='app')
    detail = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(CreateMarketSolutionDetailInput)), graphql_name='detail')


class CreateMaterialInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('name', 'type')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    type = sgqlc.types.Field(sgqlc.types.non_null(MaterialType), graphql_name='type')


class CreateOrderInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('name',)
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class CreatePeriodInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('type', 'start_at', 'end_at', 'frequency')
    type = sgqlc.types.Field(sgqlc.types.non_null(PeriodType), graphql_name='type')
    start_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='startAt')
    end_at = sgqlc.types.Field(Timestamp, graphql_name='endAt')
    frequency = sgqlc.types.Field(PeriodFrequency, graphql_name='frequency')


class CreateProcedureInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('name',)
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class CreateProcedureSegmentInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('name', 'root', 'nodes')
    name = sgqlc.types.Field(String, graphql_name='name')
    root = sgqlc.types.Field(sgqlc.types.non_null('IDInput'), graphql_name='root')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(JSONString), graphql_name='nodes')


class CreateProduct(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('material', 'target_outcome', 'delivery_date', 'delivery_shift', 'demand')
    material = sgqlc.types.Field(sgqlc.types.non_null('IDInput'), graphql_name='material')
    target_outcome = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='targetOutcome')
    delivery_date = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='deliveryDate')
    delivery_shift = sgqlc.types.Field(sgqlc.types.non_null('IDInput'), graphql_name='deliveryShift')
    demand = sgqlc.types.Field(String, graphql_name='demand')


class CreateProductionPlanInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('order', 'product', 'target_outcome', 'start_day', 'end_day', 'start_shift', 'end_shift', 'responsibles')
    order = sgqlc.types.Field(sgqlc.types.non_null('IDInput'), graphql_name='order')
    product = sgqlc.types.Field(sgqlc.types.non_null('IDInput'), graphql_name='product')
    target_outcome = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='targetOutcome')
    start_day = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='startDay')
    end_day = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='endDay')
    start_shift = sgqlc.types.Field(sgqlc.types.non_null('IDInput'), graphql_name='startShift')
    end_shift = sgqlc.types.Field(sgqlc.types.non_null('IDInput'), graphql_name='endShift')
    responsibles = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('IDInput'))), graphql_name='responsibles')


class CreateProductionProcessInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('parent', 'procedure', 'children')
    parent = sgqlc.types.Field(sgqlc.types.non_null('IDInput'), graphql_name='parent')
    procedure = sgqlc.types.Field(sgqlc.types.non_null('IDInput'), graphql_name='procedure')
    children = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ProductionProcessChildInput'))), graphql_name='children')


class CreateProductionTeamInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('name',)
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class CreateProductionTeamLeaderInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('name', 'code', 'phone', 'gender')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    code = sgqlc.types.Field(String, graphql_name='code')
    phone = sgqlc.types.Field(String, graphql_name='phone')
    gender = sgqlc.types.Field(Gender, graphql_name='gender')


class CreateProductionTeamPlusInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('name', 'leader')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    leader = sgqlc.types.Field(sgqlc.types.non_null(CreateProductionTeamLeaderInput), graphql_name='leader')


class CreateProductionTeammateInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('team', 'name', 'code', 'phone', 'gender')
    team = sgqlc.types.Field(sgqlc.types.non_null('IDInput'), graphql_name='team')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    code = sgqlc.types.Field(String, graphql_name='code')
    phone = sgqlc.types.Field(String, graphql_name='phone')
    gender = sgqlc.types.Field(Gender, graphql_name='gender')


class CreateProductionTicketFileInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('name', 'length')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    length = sgqlc.types.Field(Int, graphql_name='length')


class CreateProductionTicketInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('code', 'customer', 'product', 'model', 'thing', 'num', 'deliver_at', 'remark', 'manual', 'paper')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    customer = sgqlc.types.Field(String, graphql_name='customer')
    product = sgqlc.types.Field(String, graphql_name='product')
    model = sgqlc.types.Field(String, graphql_name='model')
    thing = sgqlc.types.Field(sgqlc.types.non_null('IDInput'), graphql_name='thing')
    num = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='num')
    deliver_at = sgqlc.types.Field(Timestamp, graphql_name='deliverAt')
    remark = sgqlc.types.Field(String, graphql_name='remark')
    manual = sgqlc.types.Field('IDInput', graphql_name='manual')
    paper = sgqlc.types.Field('IDInput', graphql_name='paper')


class CreateProductsInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('order', 'products')
    order = sgqlc.types.Field(sgqlc.types.non_null('IDInput'), graphql_name='order')
    products = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CreateProduct))), graphql_name='products')


class CreateRecruitJobInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'title', 'description', 'requirement', 'recruit_number', 'salary_start', 'salary_end', 'welfare', 'remark', 'expired_at')
    company = sgqlc.types.Field(sgqlc.types.non_null('IDNameInput'), graphql_name='company')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='description')
    requirement = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='requirement')
    recruit_number = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='recruitNumber')
    salary_start = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='salaryStart')
    salary_end = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='salaryEnd')
    welfare = sgqlc.types.Field(String, graphql_name='welfare')
    remark = sgqlc.types.Field(String, graphql_name='remark')
    expired_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='expiredAt')


class CreateRecruitStudentInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('user_id', 'name', 'gender', 'stu_no', 'stu_class', 'faculty', 'is_looking_job', 'identity', 'phone')
    user_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='userId')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    gender = sgqlc.types.Field(sgqlc.types.non_null(Gender), graphql_name='gender')
    stu_no = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='stuNo')
    stu_class = sgqlc.types.Field(sgqlc.types.non_null('IDNameInput'), graphql_name='stuClass')
    faculty = sgqlc.types.Field(sgqlc.types.non_null('IDNameInput'), graphql_name='faculty')
    is_looking_job = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isLookingJob')
    identity = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='identity')
    phone = sgqlc.types.Field(String, graphql_name='phone')


class CreateReportInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('thing_id', 'company_id', 'timestamp', 'data', 'tag')
    thing_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='thingID')
    company_id = sgqlc.types.Field(ID, graphql_name='companyID')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='timestamp')
    data = sgqlc.types.Field(sgqlc.types.non_null(JSONString), graphql_name='data')
    tag = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='tag')


class CreateRoleInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'name', 'permissions', 'desc')
    company = sgqlc.types.Field('IDInput', graphql_name='company')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    permissions = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('PermissionInput')), graphql_name='permissions')
    desc = sgqlc.types.Field(String, graphql_name='desc')


class CreateRouterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('name', 'code', 'client_id', 'model', 'images', 'detail_things', 'desc', 'location', 'contact', 'phone', 'purchased_at', 'activated_at', 'years_of_maintenance', 'company')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    client_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='clientId')
    model = sgqlc.types.Field(sgqlc.types.non_null('IDInput'), graphql_name='model')
    images = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='images')
    detail_things = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('detailThingInput')), graphql_name='detailThings')
    desc = sgqlc.types.Field(String, graphql_name='desc')
    location = sgqlc.types.Field(String, graphql_name='location')
    contact = sgqlc.types.Field(String, graphql_name='contact')
    phone = sgqlc.types.Field(String, graphql_name='phone')
    purchased_at = sgqlc.types.Field(Timestamp, graphql_name='purchasedAt')
    activated_at = sgqlc.types.Field(Timestamp, graphql_name='activatedAt')
    years_of_maintenance = sgqlc.types.Field(Int, graphql_name='yearsOfMaintenance')
    company = sgqlc.types.Field('IDInput', graphql_name='company')


class CreateRouterTemplateConfigurationInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('name', 'model', 'collects', 'company')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    model = sgqlc.types.Field(sgqlc.types.non_null('IDInput'), graphql_name='model')
    collects = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CollectConfigurationInput))), graphql_name='collects')
    company = sgqlc.types.Field('IDInput', graphql_name='company')


class CreateSocialPersonInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('user_id', 'identity', 'name', 'gender', 'is_looking_job', 'phone')
    user_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='userId')
    identity = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='identity')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    gender = sgqlc.types.Field(sgqlc.types.non_null(Gender), graphql_name='gender')
    is_looking_job = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isLookingJob')
    phone = sgqlc.types.Field(String, graphql_name='phone')


class CreateSourceKeyInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('thing_type_id', 'key', 'desc')
    thing_type_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='thingTypeId')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    desc = sgqlc.types.Field(String, graphql_name='desc')


class CreateSparePartInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('sap', 'name', 'brand', 'manufacturer', 'type', 'distributor', 'price', 'images', 'attachments', 'things', 'addition')
    sap = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='sap')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    brand = sgqlc.types.Field(String, graphql_name='brand')
    manufacturer = sgqlc.types.Field(String, graphql_name='manufacturer')
    type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='type')
    distributor = sgqlc.types.Field(String, graphql_name='distributor')
    price = sgqlc.types.Field(Float, graphql_name='price')
    images = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='images')
    attachments = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='attachments')
    things = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='things')
    addition = sgqlc.types.Field(JSONString, graphql_name='addition')


class CreateSparePartOutboundInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('operator', 'time', 'shelf', 'factory', 'reason', 'thing_repair', 'thing_maintenance', 'thing_inspection', 'details', 'addition')
    operator = sgqlc.types.Field(sgqlc.types.non_null('IDInput'), graphql_name='operator')
    time = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='time')
    shelf = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='shelf')
    factory = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='factory')
    reason = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='reason')
    thing_repair = sgqlc.types.Field('IDInput', graphql_name='thingRepair')
    thing_maintenance = sgqlc.types.Field('IDInput', graphql_name='thingMaintenance')
    thing_inspection = sgqlc.types.Field('IDInput', graphql_name='thingInspection')
    details = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('SparePartOutboundDetailInput'))), graphql_name='details')
    addition = sgqlc.types.Field(JSONString, graphql_name='addition')


class CreateSparePartReceiptInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('shelf', 'factory', 'operator', 'time', 'details', 'addition')
    shelf = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='shelf')
    factory = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='factory')
    operator = sgqlc.types.Field(sgqlc.types.non_null('IDInput'), graphql_name='operator')
    time = sgqlc.types.Field(Timestamp, graphql_name='time')
    details = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('SparePartReceiptDetailInput'))), graphql_name='details')
    addition = sgqlc.types.Field(JSONString, graphql_name='addition')


class CreateThingGroupInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('name', 'parent')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    parent = sgqlc.types.Field('IDInput', graphql_name='parent')


class CreateThingInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('code', 'sap', 'name', 'model', 'desc', 'manufacturer', 'distributor', 'purchased_at', 'activated_at', 'purchased_price', 'years_of_use', 'used_year', 'predict_residual_rate', 'depreciation_rate', 'category', 'factory', 'purpose', 'repair_contacts', 'using_status', 'addition', 'images', 'spare_parts', 'attachments', 'access_key', 'organization', 'type', 'energy_group', 'thing_group')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    sap = sgqlc.types.Field(String, graphql_name='sap')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    model = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='model')
    desc = sgqlc.types.Field(String, graphql_name='desc')
    manufacturer = sgqlc.types.Field(String, graphql_name='manufacturer')
    distributor = sgqlc.types.Field(String, graphql_name='distributor')
    purchased_at = sgqlc.types.Field(Timestamp, graphql_name='purchasedAt')
    activated_at = sgqlc.types.Field(Timestamp, graphql_name='activatedAt')
    purchased_price = sgqlc.types.Field(Float, graphql_name='purchasedPrice')
    years_of_use = sgqlc.types.Field(Float, graphql_name='yearsOfUse')
    used_year = sgqlc.types.Field(Float, graphql_name='usedYear')
    predict_residual_rate = sgqlc.types.Field(Float, graphql_name='predictResidualRate')
    depreciation_rate = sgqlc.types.Field(Float, graphql_name='depreciationRate')
    category = sgqlc.types.Field(String, graphql_name='category')
    factory = sgqlc.types.Field(String, graphql_name='factory')
    purpose = sgqlc.types.Field(String, graphql_name='purpose')
    repair_contacts = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='repairContacts')
    using_status = sgqlc.types.Field(String, graphql_name='usingStatus')
    addition = sgqlc.types.Field(JSONString, graphql_name='addition')
    images = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='images')
    spare_parts = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='spareParts')
    attachments = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='attachments')
    access_key = sgqlc.types.Field(String, graphql_name='accessKey')
    organization = sgqlc.types.Field('IDInput', graphql_name='organization')
    type = sgqlc.types.Field('IDInput', graphql_name='type')
    energy_group = sgqlc.types.Field('IDInput', graphql_name='energyGroup')
    thing_group = sgqlc.types.Field('IDInput', graphql_name='thingGroup')


class CreateThingInputRecordInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('thing_id', 'timestamp', 'product_name', 'production', 'production_beat', 'yield_number')
    thing_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='thingId')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='timestamp')
    product_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='productName')
    production = sgqlc.types.Field('ThingInputDataIntAttributeInput', graphql_name='production')
    production_beat = sgqlc.types.Field('ThingInputDataIntAttributeInput', graphql_name='productionBeat')
    yield_number = sgqlc.types.Field('ThingInputDataIntAttributeInput', graphql_name='yieldNumber')


class CreateThingInspectionInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('rule', 'operator', 'period', 'things', 'addition')
    rule = sgqlc.types.Field(sgqlc.types.non_null('IDInput'), graphql_name='rule')
    operator = sgqlc.types.Field(sgqlc.types.non_null('IDInput'), graphql_name='operator')
    period = sgqlc.types.Field(sgqlc.types.non_null(CreatePeriodInput), graphql_name='period')
    things = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('IDInput'))), graphql_name='things')
    addition = sgqlc.types.Field(JSONString, graphql_name='addition')


class CreateThingInspectionItemInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('name', 'sub_items')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    sub_items = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('CreateThingInspectionSubItemInput'))), graphql_name='subItems')


class CreateThingInspectionRuleInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('name', 'items', 'addition')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    items = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(CreateThingInspectionItemInput)), graphql_name='items')
    addition = sgqlc.types.Field(JSONString, graphql_name='addition')


class CreateThingInspectionSubItemBoundaries(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('a', 'b')
    a = sgqlc.types.Field(Int, graphql_name='a')
    b = sgqlc.types.Field(Int, graphql_name='b')


class CreateThingInspectionSubItemInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('name', 'standard', 'category', 'criteria', 'boundary')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    standard = sgqlc.types.Field(String, graphql_name='standard')
    category = sgqlc.types.Field(sgqlc.types.non_null(ThingInspectionSubItemCategory), graphql_name='category')
    criteria = sgqlc.types.Field(ThingInspectionNumberCriteria, graphql_name='criteria')
    boundary = sgqlc.types.Field(CreateThingInspectionSubItemBoundaries, graphql_name='boundary')


class CreateThingMaintenanceInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('rule', 'things', 'maintainer', 'period', 'addition')
    rule = sgqlc.types.Field(sgqlc.types.non_null('IDInput'), graphql_name='rule')
    things = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('IDInput'))), graphql_name='things')
    maintainer = sgqlc.types.Field(sgqlc.types.non_null('IDInput'), graphql_name='maintainer')
    period = sgqlc.types.Field(sgqlc.types.non_null(CreatePeriodInput), graphql_name='period')
    addition = sgqlc.types.Field(JSONString, graphql_name='addition')


class CreateThingMaintenanceItemInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('name', 'content')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    content = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='content')


class CreateThingMaintenanceRuleInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('name', 'level', 'frequency', 'items', 'addition')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    level = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='level')
    frequency = sgqlc.types.Field(String, graphql_name='frequency')
    items = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(CreateThingMaintenanceItemInput)), graphql_name='items')
    addition = sgqlc.types.Field(JSONString, graphql_name='addition')


class CreateThingOrganization(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('name', 'parent_id')
    name = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='name')
    parent_id = sgqlc.types.Field(ID, graphql_name='parentId')


class CreateThingRepairInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('thing', 'reported_at', 'fault_images', 'fault_desc', 'addition', 'is_draft')
    thing = sgqlc.types.Field(sgqlc.types.non_null('IDInput'), graphql_name='thing')
    reported_at = sgqlc.types.Field(Timestamp, graphql_name='reportedAt')
    fault_images = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='faultImages')
    fault_desc = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='faultDesc')
    addition = sgqlc.types.Field(JSONString, graphql_name='addition')
    is_draft = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isDraft')


class CreateThingStatus(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('thing_type_id', 'value', 'label', 'type')
    thing_type_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='thingTypeId')
    value = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='value')
    label = sgqlc.types.Field(String, graphql_name='label')
    type = sgqlc.types.Field(sgqlc.types.non_null(ThingStatusType), graphql_name='type')


class CreateThingTypeInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('name', 'code', 'desc')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    code = sgqlc.types.Field(String, graphql_name='code')
    desc = sgqlc.types.Field(String, graphql_name='desc')


class CreateTrainClassInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('name', 'faculty', 'class_teacher', 'graduate_at')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    faculty = sgqlc.types.Field(sgqlc.types.non_null('IDInput'), graphql_name='faculty')
    class_teacher = sgqlc.types.Field('IDInput', graphql_name='classTeacher')
    graduate_at = sgqlc.types.Field(Timestamp, graphql_name='graduateAt')


class CreateTrainCourseInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('work_type_id', 'work_type_name', 'work_level_id', 'work_level_name', 'sign_up_start_at', 'sign_up_end_at', 'introduction')
    work_type_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='workTypeId')
    work_type_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='workTypeName')
    work_level_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='workLevelId')
    work_level_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='workLevelName')
    sign_up_start_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='signUpStartAt')
    sign_up_end_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='signUpEndAt')
    introduction = sgqlc.types.Field(String, graphql_name='introduction')


class CreateTrainFacultyInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('name', 'administrator')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    administrator = sgqlc.types.Field('IDInput', graphql_name='administrator')


class CreateTrainSchoolRecruitTaskInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('name', 'start_at', 'end_at', 'stu_class', 'company')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    start_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='startAt')
    end_at = sgqlc.types.Field(Timestamp, graphql_name='endAt')
    stu_class = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='stuClass')
    company = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='company')


class CreateTrainSchoolStudentInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('stu_no', 'name', 'gender', 'faculty', 'stu_class', 'identity', 'diploma', 'phone', 'parent_phone', 'parent_name', 'status')
    stu_no = sgqlc.types.Field(String, graphql_name='stuNo')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    gender = sgqlc.types.Field(sgqlc.types.non_null(Gender), graphql_name='gender')
    faculty = sgqlc.types.Field(sgqlc.types.non_null('IDInput'), graphql_name='faculty')
    stu_class = sgqlc.types.Field(sgqlc.types.non_null('IDInput'), graphql_name='stuClass')
    identity = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='identity')
    diploma = sgqlc.types.Field(String, graphql_name='diploma')
    phone = sgqlc.types.Field(String, graphql_name='phone')
    parent_phone = sgqlc.types.Field(String, graphql_name='parentPhone')
    parent_name = sgqlc.types.Field(String, graphql_name='parentName')
    status = sgqlc.types.Field(sgqlc.types.non_null(TrainStudentStatus), graphql_name='status')


class CreateUserInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('account', 'name', 'company', 'department', 'role', 'phone', 'email', 'desc', 'is_active')
    account = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='account')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    company = sgqlc.types.Field('IDInput', graphql_name='company')
    department = sgqlc.types.Field('IDInput', graphql_name='department')
    role = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('IDInput'))), graphql_name='role')
    phone = sgqlc.types.Field(String, graphql_name='phone')
    email = sgqlc.types.Field(String, graphql_name='email')
    desc = sgqlc.types.Field(String, graphql_name='desc')
    is_active = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isActive')


class CreateWorkGroupInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('name', 'segments', 'leaders', 'members')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    segments = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('IDInput'))), graphql_name='segments')
    leaders = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('IDInput'))), graphql_name='leaders')
    members = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('IDInput'))), graphql_name='members')


class CreateWorkShiftInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('name', 'start', 'end')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    start = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='start')
    end = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='end')


class CreateWorkTypeInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('name',)
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class CreateWorkerInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('code', 'name', 'gender', 'skill', 'comment')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    gender = sgqlc.types.Field(sgqlc.types.non_null(Gender), graphql_name='gender')
    skill = sgqlc.types.Field(String, graphql_name='skill')
    comment = sgqlc.types.Field(String, graphql_name='comment')


class DebugAdapterKeyInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('data', 'type', 'precision', 'function')
    data = sgqlc.types.Field(sgqlc.types.non_null(JSON), graphql_name='data')
    type = sgqlc.types.Field(DataType, graphql_name='type')
    precision = sgqlc.types.Field(Int, graphql_name='precision')
    function = sgqlc.types.Field(JSON, graphql_name='function')


class DeleteAlertRuleInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('ids',)
    ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('IDInput'))), graphql_name='ids')


class DeleteCompaniesInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('ids',)
    ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids')


class DeleteCompanyAdminUsersInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('ids',)
    ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids')


class DeleteCompanyAppsInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company_id', 'app_ids')
    company_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='companyID')
    app_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='appIDs')


class DeleteDepartmentThingGroupInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('department', 'thing_groups')
    department = sgqlc.types.Field(sgqlc.types.non_null(JSONString), graphql_name='department')
    thing_groups = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('IDInput'))), graphql_name='thingGroups')


class DeleteDepartmentsInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('ids',)
    ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids')


class DeleteInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('ids',)
    ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids')


class DeleteProcedureSegment(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class DeleteProductionProcessInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('parent', 'child', 'procedure')
    parent = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='parent')
    child = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='child')
    procedure = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='procedure')


class DeleteSparePartOutboundsInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('ids',)
    ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids')


class DeleteSparePartReceiptInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('ids',)
    ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids')


class DeleteSparePartsInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('ids',)
    ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids')


class DeleteThingInspectionRulesInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('ids',)
    ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids')


class DeleteThingInspectionsInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('ids',)
    ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids')


class DeleteThingMaintenanceRulesInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('ids',)
    ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids')


class DeleteThingMaintenancesInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('ids',)
    ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids')


class DeleteThingRepairsInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('ids',)
    ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids')


class DeleteThingsInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('ids',)
    ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids')


class DeleteUsersInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('ids',)
    ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids')


class DepartmentListFilter(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('search', 'ids', 'current_only', 'company')
    search = sgqlc.types.Field(String, graphql_name='search')
    ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='ids')
    current_only = sgqlc.types.Field(Boolean, graphql_name='currentOnly')
    company = sgqlc.types.Field('IDInput', graphql_name='company')


class DepartmentNameSameAsSiblingsFilter(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'parent')
    id = sgqlc.types.Field(ID, graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    parent = sgqlc.types.Field(sgqlc.types.non_null('IDInput'), graphql_name='parent')


class DepartmentTreeFilter(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company',)
    company = sgqlc.types.Field('IDInput', graphql_name='company')


class DeptUserThingGroupInputFilter(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('search', 'departments', 'user')
    search = sgqlc.types.Field(String, graphql_name='search')
    departments = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='departments')
    user = sgqlc.types.Field('IDInput', graphql_name='user')


class DeviceChannelConfigurationFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('search', 'router_id')
    search = sgqlc.types.Field(String, graphql_name='search')
    router_id = sgqlc.types.Field(sgqlc.types.non_null('IDInput'), graphql_name='routerId')


class DmegcEnergyConsumptionFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('start_at', 'end_at', 'granularity')
    start_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='startAt')
    end_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='endAt')
    granularity = sgqlc.types.Field(sgqlc.types.non_null(Granularity), graphql_name='granularity')


class DmegcOEEFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('start_at', 'end_at', 'granularity')
    start_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='startAt')
    end_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='endAt')
    granularity = sgqlc.types.Field(sgqlc.types.non_null(Granularity), graphql_name='granularity')


class DmegcOperationRateFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('start_at', 'end_at', 'granularity')
    start_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='startAt')
    end_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='endAt')
    granularity = sgqlc.types.Field(sgqlc.types.non_null(Granularity), graphql_name='granularity')


class DmegcOverallFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('start_at', 'end_at')
    start_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='startAt')
    end_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='endAt')


class DmegcPerformanceRateFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('start_at', 'end_at', 'granularity')
    start_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='startAt')
    end_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='endAt')
    granularity = sgqlc.types.Field(sgqlc.types.non_null(Granularity), graphql_name='granularity')


class DmegcProductionFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('start_at', 'end_at', 'granularity')
    start_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='startAt')
    end_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='endAt')
    granularity = sgqlc.types.Field(sgqlc.types.non_null(Granularity), graphql_name='granularity')


class DmegcYieldRateFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('start_at', 'end_at', 'granularity')
    start_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='startAt')
    end_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='endAt')
    granularity = sgqlc.types.Field(sgqlc.types.non_null(Granularity), graphql_name='granularity')


class EnergyGroupFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company_id',)
    company_id = sgqlc.types.Field(ID, graphql_name='companyId')


class EprectMoldFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('search',)
    search = sgqlc.types.Field(String, graphql_name='search')


class EprectProductionRecordFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('start', 'end', 'only_the_best_arguments', 'mold', 'thing_id', 'search')
    start = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='start')
    end = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='end')
    only_the_best_arguments = sgqlc.types.Field(Boolean, graphql_name='onlyTheBestArguments')
    mold = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='mold')
    thing_id = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='thingId')
    search = sgqlc.types.Field(String, graphql_name='search')


class EthernetChannelInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('ip', 'port', 'slave_id')
    ip = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='ip')
    port = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='port')
    slave_id = sgqlc.types.Field(Int, graphql_name='slaveId')


class ExportSparePartOutboundsInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('ids',)
    ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids')


class ExportSparePartReceiptInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('ids',)
    ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids')


class ExportSparePartStockInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('ids',)
    ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids')


class ExportSparePartsInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('ids',)
    ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids')


class ExportThingInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('ids',)
    ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids')


class ExportThingInspectionRulesInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('ids',)
    ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids')


class ExportThingInspectionsInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('ids',)
    ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids')


class ExportThingMaintenanceRulesInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('ids',)
    ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids')


class ExportThingMaintenancesInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('ids',)
    ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids')


class ExportThingRepairsInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('ids',)
    ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids')


class ExportUserInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('ids',)
    ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids')


class FaultFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('start', 'end', 'things', 'level', 'type', 'search')
    start = sgqlc.types.Field(Timestamp, graphql_name='start')
    end = sgqlc.types.Field(Timestamp, graphql_name='end')
    things = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='things')
    level = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(FalutLevel)), graphql_name='level')
    type = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(FaultType)), graphql_name='type')
    search = sgqlc.types.Field(String, graphql_name='search')


class FaultIssueFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('search', 'start', 'end', 'type', 'level', 'my')
    search = sgqlc.types.Field(String, graphql_name='search')
    start = sgqlc.types.Field(Timestamp, graphql_name='start')
    end = sgqlc.types.Field(Timestamp, graphql_name='end')
    type = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(FaultType)), graphql_name='type')
    level = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(FalutLevel)), graphql_name='level')
    my = sgqlc.types.Field(Boolean, graphql_name='my')


class FaultReasonInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'content')
    id = sgqlc.types.Field(ID, graphql_name='id')
    content = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='content')


class FaultRuleFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('search', 'thing_type')
    search = sgqlc.types.Field(String, graphql_name='search')
    thing_type = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='thingType')


class FaultSolutionFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('search', 'directory')
    search = sgqlc.types.Field(String, graphql_name='search')
    directory = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='directory')


class FieldFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('field', 'values')
    field = sgqlc.types.Field(sgqlc.types.non_null('IDInput'), graphql_name='field')
    values = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='values')


class FieldMetaInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'type', 'title', 'deletable', 'required', 'field_ratio', 'hidden', 'filterable', 'prompt', 'is_single_line', 'word_count_limit', 'digit', 'show_money', 'size_limit', 'count_limit', 'candidates', 'formula', 'col_name', 'field_name', 'is_origin', 'default_desc', 'default_text', 'default_datetime', 'default_number', 'default_contact', 'default_selection')
    id = sgqlc.types.Field(ID, graphql_name='id')
    type = sgqlc.types.Field(sgqlc.types.non_null(FieldType), graphql_name='type')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    deletable = sgqlc.types.Field(Boolean, graphql_name='deletable')
    required = sgqlc.types.Field(Boolean, graphql_name='required')
    field_ratio = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='fieldRatio')
    hidden = sgqlc.types.Field(Boolean, graphql_name='hidden')
    filterable = sgqlc.types.Field(Boolean, graphql_name='filterable')
    prompt = sgqlc.types.Field(String, graphql_name='prompt')
    is_single_line = sgqlc.types.Field(Boolean, graphql_name='isSingleLine')
    word_count_limit = sgqlc.types.Field('WordCountLimitInput', graphql_name='wordCountLimit')
    digit = sgqlc.types.Field(Int, graphql_name='digit')
    show_money = sgqlc.types.Field(Boolean, graphql_name='showMoney')
    size_limit = sgqlc.types.Field(Int, graphql_name='sizeLimit')
    count_limit = sgqlc.types.Field(Int, graphql_name='countLimit')
    candidates = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='candidates')
    formula = sgqlc.types.Field(JSONString, graphql_name='formula')
    col_name = sgqlc.types.Field(String, graphql_name='colName')
    field_name = sgqlc.types.Field(String, graphql_name='fieldName')
    is_origin = sgqlc.types.Field(Boolean, graphql_name='isOrigin')
    default_desc = sgqlc.types.Field(String, graphql_name='defaultDesc')
    default_text = sgqlc.types.Field(String, graphql_name='defaultText')
    default_datetime = sgqlc.types.Field(Timestamp, graphql_name='defaultDatetime')
    default_number = sgqlc.types.Field(Float, graphql_name='defaultNumber')
    default_contact = sgqlc.types.Field(String, graphql_name='defaultContact')
    default_selection = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='defaultSelection')


class ForbiddenUserInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class FxObjectInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('ast', 'result')
    ast = sgqlc.types.Field(sgqlc.types.non_null(JSONString), graphql_name='ast')
    result = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='result')


class GrantRoleInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('user_id', 'role_id')
    user_id = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='userId')
    role_id = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='roleId')


class IDInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class IDNameInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class ImportFileInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('name', 'company')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    company = sgqlc.types.Field(IDInput, graphql_name='company')


class IssueListFilter(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('search', 'status', 'category')
    search = sgqlc.types.Field(String, graphql_name='search')
    status = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IssueStatus)), graphql_name='status')
    category = sgqlc.types.Field(sgqlc.types.non_null(IssueCategory), graphql_name='category')


class JhdvDeviceIndexDataFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('region_adcode', 'industry_id', 'start_at', 'end_at')
    region_adcode = sgqlc.types.Field(Int, graphql_name='regionAdcode')
    industry_id = sgqlc.types.Field(ID, graphql_name='industryId')
    start_at = sgqlc.types.Field(Timestamp, graphql_name='startAt')
    end_at = sgqlc.types.Field(Timestamp, graphql_name='endAt')


class JhdvDeviceRunningStatisticFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('region_adcode', 'industry_id')
    region_adcode = sgqlc.types.Field(Int, graphql_name='regionAdcode')
    industry_id = sgqlc.types.Field(ID, graphql_name='industryId')


class JhdvRegionStatisticListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('industry_id', 'start_at', 'end_at')
    industry_id = sgqlc.types.Field(ID, graphql_name='industryId')
    start_at = sgqlc.types.Field(Timestamp, graphql_name='startAt')
    end_at = sgqlc.types.Field(Timestamp, graphql_name='endAt')


class LoginInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('account', 'password')
    account = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='account')
    password = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='password')


class MadeOfNodeInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'rate')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    rate = sgqlc.types.Field('ProductionRateInput', graphql_name='rate')


class MarketAppFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('is_published', 'is_recommended', 'search', 'type')
    is_published = sgqlc.types.Field(Boolean, graphql_name='isPublished')
    is_recommended = sgqlc.types.Field(Boolean, graphql_name='isRecommended')
    search = sgqlc.types.Field(String, graphql_name='search')
    type = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(MarketAppType)), graphql_name='type')


class MarketCommonComponentInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('title', 'content', 'image')
    title = sgqlc.types.Field(String, graphql_name='title')
    content = sgqlc.types.Field(String, graphql_name='content')
    image = sgqlc.types.Field(IDInput, graphql_name='image')


class MarketIssueFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('start', 'end', 'type', 'status', 'search')
    start = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='start')
    end = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='end')
    type = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(MarketConsultationType)), graphql_name='type')
    status = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(MarketIssueStatus)), graphql_name='status')
    search = sgqlc.types.Field(String, graphql_name='search')


class MarketSolutionFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('is_published', 'is_recommended', 'type', 'search')
    is_published = sgqlc.types.Field(Boolean, graphql_name='isPublished')
    is_recommended = sgqlc.types.Field(Boolean, graphql_name='isRecommended')
    type = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(MarketSolutionType)), graphql_name='type')
    search = sgqlc.types.Field(String, graphql_name='search')


class MaterialFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('search', 'ids', 'types')
    search = sgqlc.types.Field(String, graphql_name='search')
    ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='ids')
    types = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(MaterialType)), graphql_name='types')


class MoveThingInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('thing_group', 'things')
    thing_group = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='thingGroup')
    things = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(IDInput))), graphql_name='things')


class MyAppListFilter(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company',)
    company = sgqlc.types.Field(IDInput, graphql_name='company')


class MyCompanyAppFilter(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('search',)
    search = sgqlc.types.Field(String, graphql_name='search')


class NotificationConfigFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('source_app', 'kind')
    source_app = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='sourceApp')
    kind = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(NotificationKind)), graphql_name='kind')


class NotificationFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('source_app', 'is_read')
    source_app = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='sourceApp')
    is_read = sgqlc.types.Field(Boolean, graphql_name='isRead')


class OrderFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('search',)
    search = sgqlc.types.Field(String, graphql_name='search')


class PeriodFilter(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('start', 'end')
    start = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='start')
    end = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='end')


class PermissionInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('permission', 'data_range')
    permission = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='permission')
    data_range = sgqlc.types.Field(PermissionDataRange, graphql_name='dataRange')


class PermissionTreeFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'scope')
    company = sgqlc.types.Field(IDInput, graphql_name='company')
    scope = sgqlc.types.Field(String, graphql_name='scope')


class PlatformUserListFilter(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('role', 'is_active', 'origin', 'search')
    role = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='role')
    is_active = sgqlc.types.Field(Boolean, graphql_name='isActive')
    origin = sgqlc.types.Field(UserOrigin, graphql_name='origin')
    search = sgqlc.types.Field(String, graphql_name='search')


class ProcedureFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('search',)
    search = sgqlc.types.Field(String, graphql_name='search')


class ProcedureSegmentFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('search',)
    search = sgqlc.types.Field(String, graphql_name='search')


class ProcessesFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('search', 'procedure')
    search = sgqlc.types.Field(String, graphql_name='search')
    procedure = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='procedure')


class ProductionMachineListFilter(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('thing', 'search', 'status')
    thing = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='thing')
    search = sgqlc.types.Field(String, graphql_name='search')
    status = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ProductionMachineStatus)), graphql_name='status')


class ProductionPlanFilerInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('ids', 'status', 'search')
    ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='ids')
    status = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ProductionPlanStatus)), graphql_name='status')
    search = sgqlc.types.Field(String, graphql_name='search')


class ProductionPlanFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('search',)
    search = sgqlc.types.Field(String, graphql_name='search')


class ProductionProcessChildInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('child', 'rate')
    child = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='child')
    rate = sgqlc.types.Field(sgqlc.types.non_null('ProductionRateInput'), graphql_name='rate')


class ProductionRateInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('parent_num', 'child_num')
    parent_num = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='parentNum')
    child_num = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='childNum')


class ProductionScheduleListFilter(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('search', 'start', 'end', 'timestamp', 'shift', 'thing')
    search = sgqlc.types.Field(String, graphql_name='search')
    start = sgqlc.types.Field(Timestamp, graphql_name='start')
    end = sgqlc.types.Field(Timestamp, graphql_name='end')
    timestamp = sgqlc.types.Field(Timestamp, graphql_name='timestamp')
    shift = sgqlc.types.Field(IDInput, graphql_name='shift')
    thing = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='thing')


class ProductionScheduleLogFilter(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('schedule', 'start', 'end')
    schedule = sgqlc.types.Field(IDInput, graphql_name='schedule')
    start = sgqlc.types.Field(Timestamp, graphql_name='start')
    end = sgqlc.types.Field(Timestamp, graphql_name='end')


class ProductionSubScheduleFilter(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('schedule', 'search', 'plan_start', 'plan_end', 'start', 'end', 'deliver_start', 'deliver_end', 'status', 'priority')
    schedule = sgqlc.types.Field(IDInput, graphql_name='schedule')
    search = sgqlc.types.Field(String, graphql_name='search')
    plan_start = sgqlc.types.Field(Timestamp, graphql_name='planStart')
    plan_end = sgqlc.types.Field(Timestamp, graphql_name='planEnd')
    start = sgqlc.types.Field(Timestamp, graphql_name='start')
    end = sgqlc.types.Field(Timestamp, graphql_name='end')
    deliver_start = sgqlc.types.Field(Timestamp, graphql_name='deliverStart')
    deliver_end = sgqlc.types.Field(Timestamp, graphql_name='deliverEnd')
    status = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ProductionTicketStatus)), graphql_name='status')
    priority = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ProductionTicketPriority)), graphql_name='priority')


class ProductionSubScheduleInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'ticket', 'priority')
    id = sgqlc.types.Field(ID, graphql_name='id')
    ticket = sgqlc.types.Field(IDInput, graphql_name='ticket')
    priority = sgqlc.types.Field(ProductionTicketPriority, graphql_name='priority')


class ProductionTeammateFilter(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('team',)
    team = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='team')


class ProductionTicketFilter(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('search', 'plan_start', 'plan_end', 'deliver_start', 'deliver_end', 'thing', 'status', 'priority')
    search = sgqlc.types.Field(String, graphql_name='search')
    plan_start = sgqlc.types.Field(Timestamp, graphql_name='planStart')
    plan_end = sgqlc.types.Field(Timestamp, graphql_name='planEnd')
    deliver_start = sgqlc.types.Field(Timestamp, graphql_name='deliverStart')
    deliver_end = sgqlc.types.Field(Timestamp, graphql_name='deliverEnd')
    thing = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='thing')
    status = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ProductionTicketStatus)), graphql_name='status')
    priority = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ProductionTicketPriority)), graphql_name='priority')


class PublishBIDashboardInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'category', 'name', 'role')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    category = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='category')
    name = sgqlc.types.Field(String, graphql_name='name')
    role = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='role')


class PublishedCourseFilter(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('search', 'work_type_name', 'work_level_name', 'status')
    search = sgqlc.types.Field(String, graphql_name='search')
    work_type_name = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='workTypeName')
    work_level_name = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='workLevelName')
    status = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(CourseStatus)), graphql_name='status')


class RecruitJobFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('search', 'status')
    search = sgqlc.types.Field(String, graphql_name='search')
    status = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(RecruitJobStatus)), graphql_name='status')


class RecruitJobSignRecordFilter(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('job',)
    job = sgqlc.types.Field(IDInput, graphql_name='job')


class RecruitStudentFilter(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('search', 'status')
    search = sgqlc.types.Field(String, graphql_name='search')
    status = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(RecruitStudentStatus)), graphql_name='status')


class RefFieldInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('col_name', 'title')
    col_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='colName')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')


class RegisterUserInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('account', 'password', 'role_code')
    account = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='account')
    password = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='password')
    role_code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='roleCode')


class RelationFieldFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'col_name')
    id = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id')
    col_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='colName')


class ResetPasswordInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('user_ids',)
    user_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='userIDs')


class RestartTrainCourseInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'sign_up_start_at', 'sign_up_end_at', 'introduction')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    sign_up_start_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='signUpStartAt')
    sign_up_end_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='signUpEndAt')
    introduction = sgqlc.types.Field(String, graphql_name='introduction')


class RestoreUserInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class ReviewAuthenticateTrainCourseInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'is_authenticate')
    id = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id')
    is_authenticate = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isAuthenticate')


class ReviewCompanyDemandInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'brief', 'is_approved')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    brief = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='brief')
    is_approved = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isApproved')


class ReviewSignUpTrainCourseInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'is_approved')
    id = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id')
    is_approved = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isApproved')


class ReviewSocialPersonInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'is_approved')
    id = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id')
    is_approved = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isApproved')


class ReviewTrainSchoolRecruitTaskInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'action')
    id = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='id')
    action = sgqlc.types.Field(sgqlc.types.non_null(ReviewTrainSchoolRecruitTaskAction), graphql_name='action')


class RoleExistsFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'company')
    id = sgqlc.types.Field(ID, graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    company = sgqlc.types.Field(IDInput, graphql_name='company')


class RoleFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'search', 'company', 'scope')
    id = sgqlc.types.Field(ID, graphql_name='id')
    search = sgqlc.types.Field(String, graphql_name='search')
    company = sgqlc.types.Field(IDInput, graphql_name='company')
    scope = sgqlc.types.Field(sgqlc.types.list_of(RoleScope), graphql_name='scope')


class RouterAlarmLevelFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('search',)
    search = sgqlc.types.Field(String, graphql_name='search')


class RouterAlarmRecordFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('search', 'is_restored', 'is_ack', 'occurred_start', 'occurred_end', 'alarm_levels', 'companies')
    search = sgqlc.types.Field(String, graphql_name='search')
    is_restored = sgqlc.types.Field(Boolean, graphql_name='isRestored')
    is_ack = sgqlc.types.Field(Boolean, graphql_name='isAck')
    occurred_start = sgqlc.types.Field(Timestamp, graphql_name='occurredStart')
    occurred_end = sgqlc.types.Field(Timestamp, graphql_name='occurredEnd')
    alarm_levels = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='alarmLevels')
    companies = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='companies')


class RouterAlarmRecordSummaryFilter(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('is_restored', 'is_ack', 'companies')
    is_restored = sgqlc.types.Field(Boolean, graphql_name='isRestored')
    is_ack = sgqlc.types.Field(Boolean, graphql_name='isAck')
    companies = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='companies')


class RouterAlarmRuleInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('enabled', 'type', 'level', 'threshold', 'suggestion')
    enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='enabled')
    type = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='type')
    level = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='level')
    threshold = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='threshold')
    suggestion = sgqlc.types.Field(String, graphql_name='suggestion')


class RouterAlarmTypeFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('search',)
    search = sgqlc.types.Field(String, graphql_name='search')


class RouterFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('search', 'companies', 'models', 'client_id', 'code', 'configuration_status', 'status')
    search = sgqlc.types.Field(String, graphql_name='search')
    companies = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='companies')
    models = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='models')
    client_id = sgqlc.types.Field(String, graphql_name='clientId')
    code = sgqlc.types.Field(String, graphql_name='code')
    configuration_status = sgqlc.types.Field(RouterConfigurationStatus, graphql_name='configurationStatus')
    status = sgqlc.types.Field(RouterStatus, graphql_name='status')


class RouterHistoryFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('fields', 'start', 'end')
    fields = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='fields')
    start = sgqlc.types.Field(Timestamp, graphql_name='start')
    end = sgqlc.types.Field(Timestamp, graphql_name='end')


class RouterModelFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('search',)
    search = sgqlc.types.Field(String, graphql_name='search')


class RouterSummaryFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('companies',)
    companies = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='companies')


class RouterTemplateConfigurationFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('search', 'models', 'companies')
    search = sgqlc.types.Field(String, graphql_name='search')
    models = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='models')
    companies = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='companies')


class RouterTemplateFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'router_template_name')
    company = sgqlc.types.Field(IDInput, graphql_name='company')
    router_template_name = sgqlc.types.Field(String, graphql_name='routerTemplateName')


class SerialChannelInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('slave_id', 'com_port', 'parity', 'baud', 'data_bit', 'stop_bit')
    slave_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='slaveId')
    com_port = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='comPort')
    parity = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='parity')
    baud = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='baud')
    data_bit = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='dataBit')
    stop_bit = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='stopBit')


class SetAlertConfigInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('levels', 'types')
    levels = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='levels')
    types = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='types')


class SetAlertInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('iccid', 'alert_threshold')
    iccid = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='iccid')
    alert_threshold = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='alertThreshold')


class SetCompanyRecruitBriefInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'content', 'images')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    content = sgqlc.types.Field(String, graphql_name='content')
    images = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='images')


class SetDepartmentThingGroupInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('departments', 'thing_group')
    departments = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='departments')
    thing_group = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='thingGroup')


class SetSingleDepartmentThingGroups(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('department', 'department_tree', 'thing_groups')
    department = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='department')
    department_tree = sgqlc.types.Field(sgqlc.types.non_null(JSONString), graphql_name='departmentTree')
    thing_groups = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(IDInput))), graphql_name='thingGroups')


class SetSingleUserThingGroupsInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('user', 'thing_groups')
    user = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='user')
    thing_groups = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(IDInput))), graphql_name='thingGroups')


class SetThingsAlertRulesInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('things', 'rules')
    things = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(IDInput))), graphql_name='things')
    rules = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(IDInput))), graphql_name='rules')


class SetTrainWorkLevelInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('name',)
    name = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='name')


class SetUserThingGroupInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('users', 'thing_group')
    users = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(IDInput))), graphql_name='users')
    thing_group = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='thingGroup')


class SetWorkDutyInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('start', 'end', 'shift', 'group')
    start = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='start')
    end = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='end')
    shift = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='shift')
    group = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='group')


class SetWorkbenchInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('card',)
    card = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('WorkbenchCardInput'))), graphql_name='card')


class SignCourseFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('search', 'work_type_name', 'work_level_name', 'sign_status', 'authentication_status', 'current_round', 'status')
    search = sgqlc.types.Field(String, graphql_name='search')
    work_type_name = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='workTypeName')
    work_level_name = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='workLevelName')
    sign_status = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(CourseSignStatus)), graphql_name='signStatus')
    authentication_status = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(AuthenticationStatus)), graphql_name='authenticationStatus')
    current_round = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='currentRound')
    status = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(CourseStatus)), graphql_name='status')


class SimAlertFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('search', 'start', 'end')
    search = sgqlc.types.Field(String, graphql_name='search')
    start = sgqlc.types.Field(Timestamp, graphql_name='start')
    end = sgqlc.types.Field(Timestamp, graphql_name='end')


class SimFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('search', 'start', 'end', 'life_cycle')
    search = sgqlc.types.Field(String, graphql_name='search')
    start = sgqlc.types.Field(Timestamp, graphql_name='start')
    end = sgqlc.types.Field(Timestamp, graphql_name='end')
    life_cycle = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(LifeCycle)), graphql_name='lifeCycle')


class SocialPersonListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('search', 'register_status', 'start_at', 'end_at')
    search = sgqlc.types.Field(String, graphql_name='search')
    register_status = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(RegisterStatus)), graphql_name='registerStatus')
    start_at = sgqlc.types.Field(Timestamp, graphql_name='startAt')
    end_at = sgqlc.types.Field(Timestamp, graphql_name='endAt')


class SouceKeyFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('thing_type_id',)
    thing_type_id = sgqlc.types.Field(ID, graphql_name='thingTypeId')


class SouceModelKeyFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('thing_mechanism_model_code', 'serach')
    thing_mechanism_model_code = sgqlc.types.Field(String, graphql_name='thingMechanismModelCode')
    serach = sgqlc.types.Field(String, graphql_name='serach')


class SparePartFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('search', 'field_filters', 'relation_field_filters')
    search = sgqlc.types.Field(String, graphql_name='search')
    field_filters = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(FieldFilterInput)), graphql_name='fieldFilters')
    relation_field_filters = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(RelationFieldFilterInput)), graphql_name='relationFieldFilters')


class SparePartOutboundActualDetailInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('spare_part', 'actual_number')
    spare_part = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='sparePart')
    actual_number = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='actual_number')


class SparePartOutboundDetailInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('spare_part', 'number', 'reason')
    spare_part = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='sparePart')
    number = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='number')
    reason = sgqlc.types.Field(String, graphql_name='reason')


class SparePartOutboundFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('search', 'thing_repair_ids', 'thing_maintenance_ids', 'thing_inspection_ids', 'status', 'field_filters', 'relation_field_filters')
    search = sgqlc.types.Field(String, graphql_name='search')
    thing_repair_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='thingRepairIds')
    thing_maintenance_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='thingMaintenanceIds')
    thing_inspection_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='thingInspectionIds')
    status = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(SparePartOutboundStatus)), graphql_name='status')
    field_filters = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(FieldFilterInput)), graphql_name='fieldFilters')
    relation_field_filters = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(RelationFieldFilterInput)), graphql_name='relationFieldFilters')


class SparePartReceiptDetailInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('spare_part', 'number')
    spare_part = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='sparePart')
    number = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='number')


class SparePartReceiptFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('search', 'field_filters', 'relation_field_filters')
    search = sgqlc.types.Field(String, graphql_name='search')
    field_filters = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(FieldFilterInput)), graphql_name='fieldFilters')
    relation_field_filters = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(RelationFieldFilterInput)), graphql_name='relationFieldFilters')


class SparePartStockFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('search', 'shelf', 'factory', 'field_filters', 'relation_field_filters')
    search = sgqlc.types.Field(String, graphql_name='search')
    shelf = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='shelf')
    factory = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='factory')
    field_filters = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(FieldFilterInput)), graphql_name='fieldFilters')
    relation_field_filters = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(RelationFieldFilterInput)), graphql_name='relationFieldFilters')


class StartProductionInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('schedule', 'team')
    schedule = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='schedule')
    team = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='team')


class SystemLogFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('start', 'end', 'search', 'action', 'company')
    start = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='start')
    end = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='end')
    search = sgqlc.types.Field(String, graphql_name='search')
    action = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='action')
    company = sgqlc.types.Field(IDInput, graphql_name='company')


class ThingFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('search', 'field_filters', 'relation_field_filters', 'type', 'energy_group', 'organization', 'no_organization', 'company', 'thing_group', 'current_only')
    search = sgqlc.types.Field(String, graphql_name='search')
    field_filters = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(FieldFilterInput)), graphql_name='fieldFilters')
    relation_field_filters = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(RelationFieldFilterInput)), graphql_name='relationFieldFilters')
    type = sgqlc.types.Field(sgqlc.types.list_of(IDInput), graphql_name='type')
    energy_group = sgqlc.types.Field(sgqlc.types.list_of(IDInput), graphql_name='energyGroup')
    organization = sgqlc.types.Field(sgqlc.types.list_of(IDInput), graphql_name='organization')
    no_organization = sgqlc.types.Field(Boolean, graphql_name='noOrganization')
    company = sgqlc.types.Field(sgqlc.types.list_of(IDInput), graphql_name='company')
    thing_group = sgqlc.types.Field(sgqlc.types.list_of(IDInput), graphql_name='thingGroup')
    current_only = sgqlc.types.Field(Boolean, graphql_name='currentOnly')


class ThingGroupDeptFilter(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('departments', 'thing_group', 'current_only')
    departments = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='departments')
    thing_group = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='thingGroup')
    current_only = sgqlc.types.Field(Boolean, graphql_name='currentOnly')


class ThingGroupUserFilter(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('users', 'thing_group', 'current_only')
    users = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='users')
    thing_group = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='thingGroup')
    current_only = sgqlc.types.Field(Boolean, graphql_name='currentOnly')


class ThingInputDataIntAttributeInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('value',)
    value = sgqlc.types.Field(Int, graphql_name='value')


class ThingInputRecordFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('timestamp', 'finished', 'search')
    timestamp = sgqlc.types.Field(Timestamp, graphql_name='timestamp')
    finished = sgqlc.types.Field(Boolean, graphql_name='finished')
    search = sgqlc.types.Field(String, graphql_name='search')


class ThingInputRecordSummaryFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('start', 'end', 'finished')
    start = sgqlc.types.Field(Timestamp, graphql_name='start')
    end = sgqlc.types.Field(Timestamp, graphql_name='end')
    finished = sgqlc.types.Field(Boolean, graphql_name='finished')


class ThingInspectionDetailResultInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('thing_id', 'remarks', 'records')
    thing_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='thingId')
    remarks = sgqlc.types.Field(String, graphql_name='remarks')
    records = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('ThingInspectionRecordInput')), graphql_name='records')


class ThingInspectionFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('search', 'status', 'period_types', 'field_filters', 'relation_field_filters', 'thing_repair_ids')
    search = sgqlc.types.Field(String, graphql_name='search')
    status = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ThingInspectionStatus)), graphql_name='status')
    period_types = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(PeriodType)), graphql_name='periodTypes')
    field_filters = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(FieldFilterInput)), graphql_name='fieldFilters')
    relation_field_filters = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(RelationFieldFilterInput)), graphql_name='relationFieldFilters')
    thing_repair_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='thingRepairIds')


class ThingInspectionRecordInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('sub_item_id', 'value', 'result', 'images')
    sub_item_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='subItemId')
    value = sgqlc.types.Field(Float, graphql_name='value')
    result = sgqlc.types.Field(ThingInspectionResult, graphql_name='result')
    images = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='images')


class ThingInspectionRuleFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('search', 'field_filters', 'relation_field_filters')
    search = sgqlc.types.Field(String, graphql_name='search')
    field_filters = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(FieldFilterInput)), graphql_name='fieldFilters')
    relation_field_filters = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(RelationFieldFilterInput)), graphql_name='relationFieldFilters')


class ThingMaintenanceFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('search', 'status', 'field_filters', 'relation_field_filters', 'thing_repair_ids')
    search = sgqlc.types.Field(String, graphql_name='search')
    status = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ThingMaintenanceStatus)), graphql_name='status')
    field_filters = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(FieldFilterInput)), graphql_name='fieldFilters')
    relation_field_filters = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(RelationFieldFilterInput)), graphql_name='relationFieldFilters')
    thing_repair_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='thingRepairIds')


class ThingMaintenanceRuleFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('search', 'field_filters', 'relation_field_filters')
    search = sgqlc.types.Field(String, graphql_name='search')
    field_filters = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(FieldFilterInput)), graphql_name='fieldFilters')
    relation_field_filters = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(RelationFieldFilterInput)), graphql_name='relationFieldFilters')


class ThingMechanismModelFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('search',)
    search = sgqlc.types.Field(String, graphql_name='search')


class ThingOrganizationFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('ids',)
    ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='ids')


class ThingRateFilter(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('start', 'end', 'type', 'granularity')
    start = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='start')
    end = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='end')
    type = sgqlc.types.Field(sgqlc.types.non_null(ThingRateType), graphql_name='type')
    granularity = sgqlc.types.Field(sgqlc.types.non_null(Granularity), graphql_name='granularity')


class ThingRepairFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('search', 'status', 'field_filters', 'relation_field_filters')
    search = sgqlc.types.Field(String, graphql_name='search')
    status = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ThingRepairStatus)), graphql_name='status')
    field_filters = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(FieldFilterInput)), graphql_name='fieldFilters')
    relation_field_filters = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(RelationFieldFilterInput)), graphql_name='relationFieldFilters')


class ThingStatusFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('thing_type_id', 'company_id')
    thing_type_id = sgqlc.types.Field(ID, graphql_name='thingTypeId')
    company_id = sgqlc.types.Field(ID, graphql_name='companyId')


class ThingTypeCodeFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company_id', 'search')
    company_id = sgqlc.types.Field(ID, graphql_name='companyId')
    search = sgqlc.types.Field(String, graphql_name='search')


class ThingTypeFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company_id',)
    company_id = sgqlc.types.Field(ID, graphql_name='companyId')


class TimeDistributionDataInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('start', 'end')
    start = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='start')
    end = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='end')


class TimeDistributionInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('data', 'price')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(TimeDistributionDataInput))), graphql_name='data')
    price = sgqlc.types.Field(Float, graphql_name='price')


class TimerangeFilter(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('start', 'end')
    start = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='start')
    end = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='end')


class TrainClassListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('name', 'faculty')
    name = sgqlc.types.Field(String, graphql_name='name')
    faculty = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='faculty')


class TrainCourseFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('search', 'work_type_name', 'work_level_name', 'status', 'sign_status', 'current_round', 'authentication_status')
    search = sgqlc.types.Field(String, graphql_name='search')
    work_type_name = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='workTypeName')
    work_level_name = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='workLevelName')
    status = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(CourseStatus)), graphql_name='status')
    sign_status = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(CourseSignStatus)), graphql_name='signStatus')
    current_round = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='currentRound')
    authentication_status = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(AuthenticationStatus)), graphql_name='authenticationStatus')


class TrainFacultyAdminFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('faulty',)
    faulty = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='faulty')


class TrainFacultyListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('name', 'ids')
    name = sgqlc.types.Field(String, graphql_name='name')
    ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='ids')


class TrainHumanResourceFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('search', 'work_type_name', 'work_level_name')
    search = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='search')
    work_type_name = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='workTypeName')
    work_level_name = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='workLevelName')


class TrainSchoolRecruitTaskFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('name', 'status', 'start_at', 'end_at')
    name = sgqlc.types.Field(String, graphql_name='name')
    status = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(TrainSchoolRecruitTaskStatus)), graphql_name='status')
    start_at = sgqlc.types.Field(Timestamp, graphql_name='startAt')
    end_at = sgqlc.types.Field(Timestamp, graphql_name='endAt')


class TrainSchoolRecruitTaskRecordFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('stu_class', 'sign_status', 'name', 'task', 'search', 'is_audit')
    stu_class = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='stuClass')
    sign_status = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(TrainSchoolRecruitTaskRecordStatus)), graphql_name='signStatus')
    name = sgqlc.types.Field(String, graphql_name='name')
    task = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='task')
    search = sgqlc.types.Field(String, graphql_name='search')
    is_audit = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isAudit')


class TrainSchoolStudentFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('stu_no', 'name', 'status')
    stu_no = sgqlc.types.Field(String, graphql_name='stuNo')
    name = sgqlc.types.Field(String, graphql_name='name')
    status = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(TrainStudentStatus)), graphql_name='status')


class TrainWorkTypeFilter(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('name',)
    name = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='name')


class UpdateAdapterKeyInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'thing_type_id', 'key', 'desc', 'unit', 'type', 'precision', 'function')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    thing_type_id = sgqlc.types.Field(ID, graphql_name='thingTypeId')
    key = sgqlc.types.Field(String, graphql_name='key')
    desc = sgqlc.types.Field(String, graphql_name='desc')
    unit = sgqlc.types.Field(String, graphql_name='unit')
    type = sgqlc.types.Field(DataType, graphql_name='type')
    precision = sgqlc.types.Field(Int, graphql_name='precision')
    function = sgqlc.types.Field(JSON, graphql_name='function')


class UpdateAlertRuleInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'thing_type', 'alert_type', 'description', 'fx')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    thing_type = sgqlc.types.Field(IDInput, graphql_name='thingType')
    alert_type = sgqlc.types.Field(String, graphql_name='alertType')
    description = sgqlc.types.Field(String, graphql_name='description')
    fx = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(FxObjectInput)), graphql_name='fx')


class UpdateBIDashboardInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'component', 'extra', 'thumbnail', 'attachment')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    component = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(JSON)), graphql_name='component')
    extra = sgqlc.types.Field(JSON, graphql_name='extra')
    thumbnail = sgqlc.types.Field(IDInput, graphql_name='thumbnail')
    attachment = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='attachment')


class UpdateBIDatabaseInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'uri')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    uri = sgqlc.types.Field(String, graphql_name='uri')


class UpdateCockpitAggregation(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'thing_type_id', 'tag', 'frame', 'start', 'end')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    thing_type_id = sgqlc.types.Field(ID, graphql_name='thingTypeId')
    tag = sgqlc.types.Field(String, graphql_name='tag')
    frame = sgqlc.types.Field(AggregationFrame, graphql_name='frame')
    start = sgqlc.types.Field(String, graphql_name='start')
    end = sgqlc.types.Field(String, graphql_name='end')


class UpdateCockpitKey(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'thing_type_id', 'key', 'key_type', 'name', 'unit', 'type', 'precision')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    thing_type_id = sgqlc.types.Field(ID, graphql_name='thingTypeId')
    key = sgqlc.types.Field(String, graphql_name='key')
    key_type = sgqlc.types.Field(CockpitKeyType, graphql_name='keyType')
    name = sgqlc.types.Field(String, graphql_name='name')
    unit = sgqlc.types.Field(String, graphql_name='unit')
    type = sgqlc.types.Field(DataType, graphql_name='type')
    precision = sgqlc.types.Field(Int, graphql_name='precision')


class UpdateCockpitTargetInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'timestamp', 'oee', 'operation_rate', 'performance_rate', 'yield_rate')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    timestamp = sgqlc.types.Field(Timestamp, graphql_name='timestamp')
    oee = sgqlc.types.Field(Float, graphql_name='OEE')
    operation_rate = sgqlc.types.Field(Float, graphql_name='operationRate')
    performance_rate = sgqlc.types.Field(Float, graphql_name='performanceRate')
    yield_rate = sgqlc.types.Field(Float, graphql_name='yieldRate')


class UpdateCompanyAdminUserInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'phone', 'email')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    phone = sgqlc.types.Field(String, graphql_name='phone')
    email = sgqlc.types.Field(String, graphql_name='email')


class UpdateCompanyDemandInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'is_public', 'content', 'phone', 'email', 'company_id', 'company_name')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    is_public = sgqlc.types.Field(Boolean, graphql_name='isPublic')
    content = sgqlc.types.Field(String, graphql_name='content')
    phone = sgqlc.types.Field(String, graphql_name='phone')
    email = sgqlc.types.Field(String, graphql_name='email')
    company_id = sgqlc.types.Field(ID, graphql_name='companyId')
    company_name = sgqlc.types.Field(String, graphql_name='companyName')


class UpdateCompanyInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'address', 'uscc', 'contact', 'email', 'phone', 'province', 'city', 'county', 'company_type')
    id = sgqlc.types.Field(ID, graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    address = sgqlc.types.Field(String, graphql_name='address')
    uscc = sgqlc.types.Field(String, graphql_name='uscc')
    contact = sgqlc.types.Field(String, graphql_name='contact')
    email = sgqlc.types.Field(String, graphql_name='email')
    phone = sgqlc.types.Field(String, graphql_name='phone')
    province = sgqlc.types.Field(String, graphql_name='province')
    city = sgqlc.types.Field(String, graphql_name='city')
    county = sgqlc.types.Field(String, graphql_name='county')
    company_type = sgqlc.types.Field(IDInput, graphql_name='companyType')


class UpdateDepartmentInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'parent', 'name')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    parent = sgqlc.types.Field(IDInput, graphql_name='parent')
    name = sgqlc.types.Field(String, graphql_name='name')


class UpdateDepartmentThingGroupInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('department', 'old_thing_group', 'new_thing_group')
    department = sgqlc.types.Field(sgqlc.types.non_null(JSONString), graphql_name='department')
    old_thing_group = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='oldThingGroup')
    new_thing_group = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='newThingGroup')


class UpdateDeviceChannelConfigurationInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'collect')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    collect = sgqlc.types.Field(CollectConfigurationInput, graphql_name='collect')


class UpdateDirectoryInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'parent')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    parent = sgqlc.types.Field(IDInput, graphql_name='parent')


class UpdateEnergyGroup(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')


class UpdateEnergyTimeDistribution(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('peak', 'sharp', 'valley', 'normal')
    peak = sgqlc.types.Field(TimeDistributionInput, graphql_name='peak')
    sharp = sgqlc.types.Field(TimeDistributionInput, graphql_name='sharp')
    valley = sgqlc.types.Field(TimeDistributionInput, graphql_name='valley')
    normal = sgqlc.types.Field(TimeDistributionInput, graphql_name='normal')


class UpdateFaultIssueInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'action', 'remark', 'attachments', 'receiver', 'repair_date', 'desc', 'fault_reason')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    action = sgqlc.types.Field(sgqlc.types.non_null(FaultIssueAction), graphql_name='action')
    remark = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='remark')
    attachments = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='attachments')
    receiver = sgqlc.types.Field(IDInput, graphql_name='receiver')
    repair_date = sgqlc.types.Field(Timestamp, graphql_name='repairDate')
    desc = sgqlc.types.Field(String, graphql_name='desc')
    fault_reason = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(CreateFaultIssueReasonInput)), graphql_name='faultReason')


class UpdateFaultReasonInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'content')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    content = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='content')


class UpdateFaultRuleInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'thing_type', 'name', 'type', 'desc', 'reasons', 'fx')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    thing_type = sgqlc.types.Field(IDInput, graphql_name='thingType')
    name = sgqlc.types.Field(String, graphql_name='name')
    type = sgqlc.types.Field(FaultType, graphql_name='type')
    desc = sgqlc.types.Field(String, graphql_name='desc')
    reasons = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(FaultReasonInput)), graphql_name='reasons')
    fx = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(CreateFaultFxObjectInput)), graphql_name='fx')


class UpdateFaultSolutionInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'title', 'directory', 'brief', 'reasons', 'content', 'attachments')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    title = sgqlc.types.Field(String, graphql_name='title')
    directory = sgqlc.types.Field(IDInput, graphql_name='directory')
    brief = sgqlc.types.Field(String, graphql_name='brief')
    reasons = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='reasons')
    content = sgqlc.types.Field(String, graphql_name='content')
    attachments = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='attachments')


class UpdateIssueInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'remark', 'action', 'receiver', 'attachments', 'reason')
    id = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='id')
    remark = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='remark')
    action = sgqlc.types.Field(sgqlc.types.non_null(IssueAction), graphql_name='action')
    receiver = sgqlc.types.Field(IDInput, graphql_name='receiver')
    attachments = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='attachments')
    reason = sgqlc.types.Field(IssueReason, graphql_name='reason')


class UpdateMarketAppInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'title', 'type', 'cover_image', 'is_recommended', 'brief', 'description', 'screenshot')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    title = sgqlc.types.Field(String, graphql_name='title')
    type = sgqlc.types.Field(MarketAppType, graphql_name='type')
    cover_image = sgqlc.types.Field(IDInput, graphql_name='coverImage')
    is_recommended = sgqlc.types.Field(Boolean, graphql_name='isRecommended')
    brief = sgqlc.types.Field(String, graphql_name='brief')
    description = sgqlc.types.Field(String, graphql_name='description')
    screenshot = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='screenshot')


class UpdateMarketIssueInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'action', 'receiver', 'attachment', 'description')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    action = sgqlc.types.Field(sgqlc.types.non_null(MarketIssueAction), graphql_name='action')
    receiver = sgqlc.types.Field(IDInput, graphql_name='receiver')
    attachment = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='attachment')
    description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='description')


class UpdateMarketSolutionInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'title', 'cover_image', 'type', 'is_recommended', 'brief', 'description', 'app', 'detail')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    title = sgqlc.types.Field(String, graphql_name='title')
    cover_image = sgqlc.types.Field(IDInput, graphql_name='coverImage')
    type = sgqlc.types.Field(MarketSolutionType, graphql_name='type')
    is_recommended = sgqlc.types.Field(Boolean, graphql_name='isRecommended')
    brief = sgqlc.types.Field(String, graphql_name='brief')
    description = sgqlc.types.Field(String, graphql_name='description')
    app = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='app')
    detail = sgqlc.types.Field(sgqlc.types.list_of(CreateMarketSolutionDetailInput), graphql_name='detail')


class UpdateMaterialInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'type')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    type = sgqlc.types.Field(MaterialType, graphql_name='type')


class UpdateMeInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('nickname', 'phone', 'email', 'avatar')
    nickname = sgqlc.types.Field(String, graphql_name='nickname')
    phone = sgqlc.types.Field(String, graphql_name='phone')
    email = sgqlc.types.Field(String, graphql_name='email')
    avatar = sgqlc.types.Field(IDInput, graphql_name='avatar')


class UpdateMyCompanyInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('address', 'name', 'uscc', 'email', 'phone', 'province', 'city', 'county')
    address = sgqlc.types.Field(String, graphql_name='address')
    name = sgqlc.types.Field(String, graphql_name='name')
    uscc = sgqlc.types.Field(String, graphql_name='uscc')
    email = sgqlc.types.Field(String, graphql_name='email')
    phone = sgqlc.types.Field(String, graphql_name='phone')
    province = sgqlc.types.Field(String, graphql_name='province')
    city = sgqlc.types.Field(String, graphql_name='city')
    county = sgqlc.types.Field(String, graphql_name='county')


class UpdateMyPasswordInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('old_password', 'new_password')
    old_password = sgqlc.types.Field(String, graphql_name='oldPassword')
    new_password = sgqlc.types.Field(String, graphql_name='newPassword')


class UpdateNotificationConfigInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'to_inbox', 'to_email', 'receiver_user', 'receiver_role')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    to_inbox = sgqlc.types.Field(Boolean, graphql_name='toInbox')
    to_email = sgqlc.types.Field(Boolean, graphql_name='toEmail')
    receiver_user = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='receiverUser')
    receiver_role = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='receiverRole')


class UpdateOrderInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class UpdateOrderStatusInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'status')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    status = sgqlc.types.Field(sgqlc.types.non_null(OrderStatus), graphql_name='status')


class UpdateProcedureInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class UpdateProcedureSegmentInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'nodes')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(JSONString), graphql_name='nodes')


class UpdateProduct(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'material', 'target_outcome', 'delivery_date', 'delivery_shift', 'demand')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    material = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='material')
    target_outcome = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='targetOutcome')
    delivery_date = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='deliveryDate')
    delivery_shift = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='deliveryShift')
    demand = sgqlc.types.Field(String, graphql_name='demand')


class UpdateProductionPlanInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'product', 'target_outcome', 'start_day', 'end_day', 'start_shift', 'end_shift', 'responsibles')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    product = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='product')
    target_outcome = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='targetOutcome')
    start_day = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='startDay')
    end_day = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='endDay')
    start_shift = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='startShift')
    end_shift = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='endShift')
    responsibles = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='responsibles')


class UpdateProductionPlanStatusInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'status')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    status = sgqlc.types.Field(sgqlc.types.non_null(ProductionPlanStatus), graphql_name='status')


class UpdateProductionProcessInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'parent', 'procedure', 'children')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    parent = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='parent')
    procedure = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='procedure')
    children = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ProductionProcessChildInput))), graphql_name='children')


class UpdateProductionRecordInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'actual_outcome', 'failed_outcome')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    actual_outcome = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='actualOutcome')
    failed_outcome = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='failedOutcome')


class UpdateProductionScheduleInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('timestamp', 'thing', 'shift', 'sub_schedule')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='timestamp')
    thing = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='thing')
    shift = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='shift')
    sub_schedule = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ProductionSubScheduleInput)), graphql_name='subSchedule')


class UpdateProductionSegmentInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'start_day', 'end_day', 'start_shift', 'end_shift', 'responsibles', 'work_duties')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    start_day = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='startDay')
    end_day = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='endDay')
    start_shift = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='startShift')
    end_shift = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='endShift')
    responsibles = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='responsibles')
    work_duties = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('WorkDutyInput')), graphql_name='workDuties')


class UpdateProductionSubScheduleInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'production', 'defective', 'start', 'end', 'team')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    production = sgqlc.types.Field(Int, graphql_name='production')
    defective = sgqlc.types.Field(Int, graphql_name='defective')
    start = sgqlc.types.Field(Timestamp, graphql_name='start')
    end = sgqlc.types.Field(Timestamp, graphql_name='end')
    team = sgqlc.types.Field(IDInput, graphql_name='team')


class UpdateProductionTeamInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')


class UpdateProductionTeammateInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'code', 'phone', 'gender', 'is_leader')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    code = sgqlc.types.Field(String, graphql_name='code')
    phone = sgqlc.types.Field(String, graphql_name='phone')
    gender = sgqlc.types.Field(Gender, graphql_name='gender')
    is_leader = sgqlc.types.Field(Boolean, graphql_name='isLeader')


class UpdateProductionTicketInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'remark')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    remark = sgqlc.types.Field(String, graphql_name='remark')


class UpdateProductsInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('order', 'products')
    order = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='order')
    products = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(UpdateProduct))), graphql_name='products')


class UpdateRecruitJobInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'title', 'description', 'requirement', 'recruit_number', 'salary_start', 'salary_end', 'welfare', 'remark', 'expired_at')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    title = sgqlc.types.Field(String, graphql_name='title')
    description = sgqlc.types.Field(String, graphql_name='description')
    requirement = sgqlc.types.Field(String, graphql_name='requirement')
    recruit_number = sgqlc.types.Field(Int, graphql_name='recruitNumber')
    salary_start = sgqlc.types.Field(Int, graphql_name='salaryStart')
    salary_end = sgqlc.types.Field(Int, graphql_name='salaryEnd')
    welfare = sgqlc.types.Field(String, graphql_name='welfare')
    remark = sgqlc.types.Field(String, graphql_name='remark')
    expired_at = sgqlc.types.Field(Timestamp, graphql_name='expiredAt')


class UpdateRecruitStudentInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'gender', 'stu_no', 'stu_class', 'faculty', 'is_looking_job', 'identity', 'phone')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    gender = sgqlc.types.Field(Gender, graphql_name='gender')
    stu_no = sgqlc.types.Field(String, graphql_name='stuNo')
    stu_class = sgqlc.types.Field(IDNameInput, graphql_name='stuClass')
    faculty = sgqlc.types.Field(IDNameInput, graphql_name='faculty')
    is_looking_job = sgqlc.types.Field(Boolean, graphql_name='isLookingJob')
    identity = sgqlc.types.Field(String, graphql_name='identity')
    phone = sgqlc.types.Field(String, graphql_name='phone')


class UpdateReportInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'timestamp', 'data', 'tag')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    timestamp = sgqlc.types.Field(Timestamp, graphql_name='timestamp')
    data = sgqlc.types.Field(JSONString, graphql_name='data')
    tag = sgqlc.types.Field(String, graphql_name='tag')


class UpdateRoleInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'company', 'name', 'permissions', 'desc')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    company = sgqlc.types.Field(IDInput, graphql_name='company')
    name = sgqlc.types.Field(String, graphql_name='name')
    permissions = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(PermissionInput)), graphql_name='permissions')
    desc = sgqlc.types.Field(String, graphql_name='desc')


class UpdateRouterAlarmRecordsInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('ids', 'is_ack')
    ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids')
    is_ack = sgqlc.types.Field(Boolean, graphql_name='is_ack')


class UpdateRouterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'code', 'client_id', 'model', 'images', 'detail_things', 'desc', 'location', 'contact', 'phone', 'purchased_at', 'activated_at', 'years_of_maintenance')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    code = sgqlc.types.Field(String, graphql_name='code')
    client_id = sgqlc.types.Field(String, graphql_name='clientId')
    model = sgqlc.types.Field(IDInput, graphql_name='model')
    images = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='images')
    detail_things = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('detailThingInput')), graphql_name='detailThings')
    desc = sgqlc.types.Field(String, graphql_name='desc')
    location = sgqlc.types.Field(String, graphql_name='location')
    contact = sgqlc.types.Field(String, graphql_name='contact')
    phone = sgqlc.types.Field(String, graphql_name='phone')
    purchased_at = sgqlc.types.Field(Timestamp, graphql_name='purchasedAt')
    activated_at = sgqlc.types.Field(Timestamp, graphql_name='activatedAt')
    years_of_maintenance = sgqlc.types.Field(Int, graphql_name='yearsOfMaintenance')


class UpdateRouterTemplateConfigurationInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'model', 'collects')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    model = sgqlc.types.Field(IDInput, graphql_name='model')
    collects = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(CollectConfigurationInput)), graphql_name='collects')


class UpdateRoutersAlarmRulesInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('routers', 'alarm_rules')
    routers = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(IDInput))), graphql_name='routers')
    alarm_rules = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(RouterAlarmRuleInput))), graphql_name='alarmRules')


class UpdateSocialPersonInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'user_id', 'identity', 'name', 'gender', 'is_looking_job', 'phone')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    user_id = sgqlc.types.Field(ID, graphql_name='userId')
    identity = sgqlc.types.Field(String, graphql_name='identity')
    name = sgqlc.types.Field(String, graphql_name='name')
    gender = sgqlc.types.Field(Gender, graphql_name='gender')
    is_looking_job = sgqlc.types.Field(Boolean, graphql_name='isLookingJob')
    phone = sgqlc.types.Field(String, graphql_name='phone')


class UpdateSourceKeyInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'thing_type_id', 'key', 'desc')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    thing_type_id = sgqlc.types.Field(ID, graphql_name='thingTypeId')
    key = sgqlc.types.Field(String, graphql_name='key')
    desc = sgqlc.types.Field(String, graphql_name='desc')


class UpdateSparePartInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'sap', 'name', 'brand', 'manufacturer', 'type', 'distributor', 'price', 'images', 'attachments', 'things', 'addition')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    sap = sgqlc.types.Field(String, graphql_name='sap')
    name = sgqlc.types.Field(String, graphql_name='name')
    brand = sgqlc.types.Field(String, graphql_name='brand')
    manufacturer = sgqlc.types.Field(String, graphql_name='manufacturer')
    type = sgqlc.types.Field(String, graphql_name='type')
    distributor = sgqlc.types.Field(String, graphql_name='distributor')
    price = sgqlc.types.Field(Float, graphql_name='price')
    images = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='images')
    attachments = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='attachments')
    things = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='things')
    addition = sgqlc.types.Field(JSONString, graphql_name='addition')


class UpdateSparePartOutboundInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'operator', 'time', 'shelf', 'factory', 'reason', 'thing_repair', 'thing_maintenance', 'thing_inspection', 'details', 'addition')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    operator = sgqlc.types.Field(IDInput, graphql_name='operator')
    time = sgqlc.types.Field(Timestamp, graphql_name='time')
    shelf = sgqlc.types.Field(String, graphql_name='shelf')
    factory = sgqlc.types.Field(String, graphql_name='factory')
    reason = sgqlc.types.Field(String, graphql_name='reason')
    thing_repair = sgqlc.types.Field(IDInput, graphql_name='thingRepair')
    thing_maintenance = sgqlc.types.Field(IDInput, graphql_name='thingMaintenance')
    thing_inspection = sgqlc.types.Field(IDInput, graphql_name='thingInspection')
    details = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(SparePartOutboundDetailInput)), graphql_name='details')
    addition = sgqlc.types.Field(JSONString, graphql_name='addition')


class UpdateSparePartReceiptInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'shelf', 'factory', 'operator', 'time', 'details', 'addition')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    shelf = sgqlc.types.Field(String, graphql_name='shelf')
    factory = sgqlc.types.Field(String, graphql_name='factory')
    operator = sgqlc.types.Field(IDInput, graphql_name='operator')
    time = sgqlc.types.Field(Timestamp, graphql_name='time')
    details = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(SparePartReceiptDetailInput)), graphql_name='details')
    addition = sgqlc.types.Field(JSONString, graphql_name='addition')


class UpdateThingGroupInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'parent')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    parent = sgqlc.types.Field(IDInput, graphql_name='parent')


class UpdateThingInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'code', 'sap', 'name', 'model', 'desc', 'manufacturer', 'distributor', 'purchased_at', 'activated_at', 'purchased_price', 'years_of_use', 'used_year', 'predict_residual_rate', 'depreciation_rate', 'category', 'factory', 'purpose', 'repair_contacts', 'using_status', 'addition', 'images', 'spare_parts', 'attachments', 'access_key', 'organization', 'type', 'energy_group', 'thing_group')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    code = sgqlc.types.Field(String, graphql_name='code')
    sap = sgqlc.types.Field(String, graphql_name='sap')
    name = sgqlc.types.Field(String, graphql_name='name')
    model = sgqlc.types.Field(String, graphql_name='model')
    desc = sgqlc.types.Field(String, graphql_name='desc')
    manufacturer = sgqlc.types.Field(String, graphql_name='manufacturer')
    distributor = sgqlc.types.Field(String, graphql_name='distributor')
    purchased_at = sgqlc.types.Field(Timestamp, graphql_name='purchasedAt')
    activated_at = sgqlc.types.Field(Timestamp, graphql_name='activatedAt')
    purchased_price = sgqlc.types.Field(Float, graphql_name='purchasedPrice')
    years_of_use = sgqlc.types.Field(Float, graphql_name='yearsOfUse')
    used_year = sgqlc.types.Field(Float, graphql_name='usedYear')
    predict_residual_rate = sgqlc.types.Field(Float, graphql_name='predictResidualRate')
    depreciation_rate = sgqlc.types.Field(Float, graphql_name='depreciationRate')
    category = sgqlc.types.Field(String, graphql_name='category')
    factory = sgqlc.types.Field(String, graphql_name='factory')
    purpose = sgqlc.types.Field(String, graphql_name='purpose')
    repair_contacts = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='repairContacts')
    using_status = sgqlc.types.Field(String, graphql_name='usingStatus')
    addition = sgqlc.types.Field(JSONString, graphql_name='addition')
    images = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='images')
    spare_parts = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='spareParts')
    attachments = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='attachments')
    access_key = sgqlc.types.Field(String, graphql_name='accessKey')
    organization = sgqlc.types.Field(IDInput, graphql_name='organization')
    type = sgqlc.types.Field(IDInput, graphql_name='type')
    energy_group = sgqlc.types.Field(IDInput, graphql_name='energyGroup')
    thing_group = sgqlc.types.Field(IDInput, graphql_name='thingGroup')


class UpdateThingInputRecordInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'production', 'production_beat', 'yield_number')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    production = sgqlc.types.Field(ThingInputDataIntAttributeInput, graphql_name='production')
    production_beat = sgqlc.types.Field(ThingInputDataIntAttributeInput, graphql_name='productionBeat')
    yield_number = sgqlc.types.Field(ThingInputDataIntAttributeInput, graphql_name='yieldNumber')


class UpdateThingInspectionFeedbackInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'results', 'end_at', 'thing_repairs', 'addition')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    results = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ThingInspectionDetailResultInput)), graphql_name='results')
    end_at = sgqlc.types.Field(Timestamp, graphql_name='endAt')
    thing_repairs = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='thingRepairs')
    addition = sgqlc.types.Field(JSONString, graphql_name='addition')


class UpdateThingInspectionInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'rule', 'operator', 'period', 'things', 'addition')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    rule = sgqlc.types.Field(IDInput, graphql_name='rule')
    operator = sgqlc.types.Field(IDInput, graphql_name='operator')
    period = sgqlc.types.Field(CreatePeriodInput, graphql_name='period')
    things = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='things')
    addition = sgqlc.types.Field(JSONString, graphql_name='addition')


class UpdateThingInspectionItemInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'sub_items')
    id = sgqlc.types.Field(ID, graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    sub_items = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('UpdateThingInspectionSubItemInput')), graphql_name='subItems')


class UpdateThingInspectionRuleInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'items', 'addition')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    items = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(UpdateThingInspectionItemInput)), graphql_name='items')
    addition = sgqlc.types.Field(JSONString, graphql_name='addition')


class UpdateThingInspectionStatusInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'action')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    action = sgqlc.types.Field(sgqlc.types.non_null(UpdateThingInspectionStatusAction), graphql_name='action')


class UpdateThingInspectionSubItemInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'standard', 'category', 'criteria', 'boundary')
    id = sgqlc.types.Field(ID, graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    standard = sgqlc.types.Field(String, graphql_name='standard')
    category = sgqlc.types.Field(ThingInspectionSubItemCategory, graphql_name='category')
    criteria = sgqlc.types.Field(ThingInspectionNumberCriteria, graphql_name='criteria')
    boundary = sgqlc.types.Field(CreateThingInspectionSubItemBoundaries, graphql_name='boundary')


class UpdateThingMaintenanceFeedbackInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'result', 'images', 'remarks', 'spare_part_costs', 'material_costs', 'labor_costs', 'other_costs', 'end_at', 'thing_repair', 'addition')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    result = sgqlc.types.Field(String, graphql_name='result')
    images = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='images')
    remarks = sgqlc.types.Field(String, graphql_name='remarks')
    spare_part_costs = sgqlc.types.Field(Float, graphql_name='sparePartCosts')
    material_costs = sgqlc.types.Field(Float, graphql_name='materialCosts')
    labor_costs = sgqlc.types.Field(Float, graphql_name='laborCosts')
    other_costs = sgqlc.types.Field(Float, graphql_name='otherCosts')
    end_at = sgqlc.types.Field(Timestamp, graphql_name='endAt')
    thing_repair = sgqlc.types.Field(IDInput, graphql_name='thingRepair')
    addition = sgqlc.types.Field(JSONString, graphql_name='addition')


class UpdateThingMaintenanceInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'rule', 'thing', 'maintainer', 'period', 'addition')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    rule = sgqlc.types.Field(IDInput, graphql_name='rule')
    thing = sgqlc.types.Field(IDInput, graphql_name='thing')
    maintainer = sgqlc.types.Field(IDInput, graphql_name='maintainer')
    period = sgqlc.types.Field(CreatePeriodInput, graphql_name='period')
    addition = sgqlc.types.Field(JSONString, graphql_name='addition')


class UpdateThingMaintenanceItemInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'content')
    id = sgqlc.types.Field(ID, graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    content = sgqlc.types.Field(String, graphql_name='content')


class UpdateThingMaintenanceRuleInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'level', 'frequency', 'items', 'addition')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    level = sgqlc.types.Field(String, graphql_name='level')
    frequency = sgqlc.types.Field(String, graphql_name='frequency')
    items = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(UpdateThingMaintenanceItemInput)), graphql_name='items')
    addition = sgqlc.types.Field(JSONString, graphql_name='addition')


class UpdateThingMaintenanceStatusInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'action')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    action = sgqlc.types.Field(sgqlc.types.non_null(UpdateThingMaintenanceStatusAction), graphql_name='action')


class UpdateThingOrganization(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'parent_id')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(ID, graphql_name='name')
    parent_id = sgqlc.types.Field(ID, graphql_name='parentId')


class UpdateThingRepairFeedbackInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'result', 'finished_at', 'spare_part_costs', 'material_costs', 'labor_costs', 'other_costs', 'addition')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    result = sgqlc.types.Field(String, graphql_name='result')
    finished_at = sgqlc.types.Field(Timestamp, graphql_name='finishedAt')
    spare_part_costs = sgqlc.types.Field(Float, graphql_name='sparePartCosts')
    material_costs = sgqlc.types.Field(Float, graphql_name='materialCosts')
    labor_costs = sgqlc.types.Field(Float, graphql_name='laborCosts')
    other_costs = sgqlc.types.Field(Float, graphql_name='otherCosts')
    addition = sgqlc.types.Field(JSONString, graphql_name='addition')


class UpdateThingRepairInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'thing', 'reported_at', 'fault_images', 'fault_desc', 'addition')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    thing = sgqlc.types.Field(IDInput, graphql_name='thing')
    reported_at = sgqlc.types.Field(Timestamp, graphql_name='reportedAt')
    fault_images = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='faultImages')
    fault_desc = sgqlc.types.Field(String, graphql_name='faultDesc')
    addition = sgqlc.types.Field(JSONString, graphql_name='addition')


class UpdateThingStatus(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'thing_type_id', 'value', 'label', 'type')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    thing_type_id = sgqlc.types.Field(ID, graphql_name='thingTypeId')
    value = sgqlc.types.Field(Int, graphql_name='value')
    label = sgqlc.types.Field(String, graphql_name='label')
    type = sgqlc.types.Field(ThingStatusType, graphql_name='type')


class UpdateThingTypeInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'code', 'desc')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    code = sgqlc.types.Field(String, graphql_name='code')
    desc = sgqlc.types.Field(String, graphql_name='desc')


class UpdateTrainClassInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'class_teacher', 'graduate_at')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    class_teacher = sgqlc.types.Field(IDInput, graphql_name='classTeacher')
    graduate_at = sgqlc.types.Field(Timestamp, graphql_name='graduateAt')


class UpdateTrainCourseInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'sign_up_start_at', 'sign_up_end_at', 'introduction')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    sign_up_start_at = sgqlc.types.Field(Timestamp, graphql_name='signUpStartAt')
    sign_up_end_at = sgqlc.types.Field(Timestamp, graphql_name='signUpEndAt')
    introduction = sgqlc.types.Field(String, graphql_name='introduction')


class UpdateTrainFacultyInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'administrator')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    administrator = sgqlc.types.Field(IDInput, graphql_name='administrator')


class UpdateTrainSchoolRecruitTaskInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'start_at', 'end_at', 'stu_class', 'company')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    start_at = sgqlc.types.Field(Timestamp, graphql_name='startAt')
    end_at = sgqlc.types.Field(Timestamp, graphql_name='endAt')
    stu_class = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='stuClass')
    company = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='company')


class UpdateTrainSchoolStudentInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'stu_no', 'name', 'gender', 'faculty', 'stu_class', 'identity', 'diploma', 'phone', 'parent_phone', 'parent_name', 'status')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    stu_no = sgqlc.types.Field(String, graphql_name='stuNo')
    name = sgqlc.types.Field(String, graphql_name='name')
    gender = sgqlc.types.Field(Gender, graphql_name='gender')
    faculty = sgqlc.types.Field(IDInput, graphql_name='faculty')
    stu_class = sgqlc.types.Field(IDInput, graphql_name='stuClass')
    identity = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='identity')
    diploma = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='diploma')
    phone = sgqlc.types.Field(String, graphql_name='phone')
    parent_phone = sgqlc.types.Field(String, graphql_name='parentPhone')
    parent_name = sgqlc.types.Field(String, graphql_name='parentName')
    status = sgqlc.types.Field(TrainStudentStatus, graphql_name='status')


class UpdateUserInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'department', 'phone', 'email', 'role', 'desc', 'is_active')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    department = sgqlc.types.Field(IDInput, graphql_name='department')
    phone = sgqlc.types.Field(String, graphql_name='phone')
    email = sgqlc.types.Field(String, graphql_name='email')
    role = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='role')
    desc = sgqlc.types.Field(String, graphql_name='desc')
    is_active = sgqlc.types.Field(Boolean, graphql_name='isActive')


class UpdateUserThingGroupInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('old_thing_group', 'new_thing_group')
    old_thing_group = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='oldThingGroup')
    new_thing_group = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='newThingGroup')


class UpdateWorkGroupInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'segments', 'leaders', 'members')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    segments = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='segments')
    leaders = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='leaders')
    members = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='members')


class UpdateWorkShiftInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'start', 'end')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    start = sgqlc.types.Field(Timestamp, graphql_name='start')
    end = sgqlc.types.Field(Timestamp, graphql_name='end')


class UpdateWorkTypeInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')


class UpdateWorkerInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'code', 'name', 'gender', 'skill', 'comment')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    code = sgqlc.types.Field(String, graphql_name='code')
    name = sgqlc.types.Field(String, graphql_name='name')
    gender = sgqlc.types.Field(Gender, graphql_name='gender')
    skill = sgqlc.types.Field(String, graphql_name='skill')
    comment = sgqlc.types.Field(String, graphql_name='comment')


class UploadProductionTeammateInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('team', 'name', 'length')
    team = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='team')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    length = sgqlc.types.Field(Int, graphql_name='length')


class UserListFilter(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('ids', 'company', 'department', 'role', 'is_active', 'search', 'current_only', 'type')
    ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='ids')
    company = sgqlc.types.Field(IDInput, graphql_name='company')
    department = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='department')
    role = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='role')
    is_active = sgqlc.types.Field(Boolean, graphql_name='isActive')
    search = sgqlc.types.Field(String, graphql_name='search')
    current_only = sgqlc.types.Field(Boolean, graphql_name='currentOnly')
    type = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(UserType)), graphql_name='type')


class WordCountLimitInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('min', 'max')
    min = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='min')
    max = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='max')


class WorkDutyFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('start', 'end')
    start = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='start')
    end = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='end')


class WorkDutyInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('day', 'shift', 'work_groups')
    day = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='day')
    shift = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='shift')
    work_groups = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(IDInput))), graphql_name='workGroups')


class WorkGroupsFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('search',)
    search = sgqlc.types.Field(String, graphql_name='search')


class WorkShiftFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('search',)
    search = sgqlc.types.Field(String, graphql_name='search')


class WorkbenchCardInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('type', 'field')
    type = sgqlc.types.Field(sgqlc.types.non_null(WorkbenchType), graphql_name='type')
    field = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='field')


class WorkerFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('search', 'genders')
    search = sgqlc.types.Field(String, graphql_name='search')
    genders = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Gender)), graphql_name='genders')


class companyExistsFilter(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'uscc')
    id = sgqlc.types.Field(ID, graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    uscc = sgqlc.types.Field(String, graphql_name='uscc')


class detailThingInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('thing',)
    thing = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='thing')



########################################################################
# Output Objects and Interfaces
########################################################################
class AdapterKey(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'thing_type', 'key', 'desc', 'unit', 'type', 'precision', 'function')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    thing_type = sgqlc.types.Field(sgqlc.types.non_null('ThingType'), graphql_name='thingType')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    desc = sgqlc.types.Field(String, graphql_name='desc')
    unit = sgqlc.types.Field(String, graphql_name='unit')
    type = sgqlc.types.Field(DataType, graphql_name='type')
    precision = sgqlc.types.Field(Int, graphql_name='precision')
    function = sgqlc.types.Field(JSON, graphql_name='function')


class AdapterKeyList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AdapterKey))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class AdapterKeyRealTimeData(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('adapter_key', 'timestamp', 'data')
    adapter_key = sgqlc.types.Field(sgqlc.types.non_null(AdapterKey), graphql_name='adapterKey')
    timestamp = sgqlc.types.Field(Timestamp, graphql_name='timestamp')
    data = sgqlc.types.Field(JSONString, graphql_name='data')


class AdapterKeyRealTimeDataList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AdapterKeyRealTimeData))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class AdapterModelKey(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('thing_mechanism_model', 'key', 'type', 'precision', 'function')
    thing_mechanism_model = sgqlc.types.Field(sgqlc.types.non_null('ThingMechanismModel'), graphql_name='thingMechanismModel')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    type = sgqlc.types.Field(DataType, graphql_name='type')
    precision = sgqlc.types.Field(Int, graphql_name='precision')
    function = sgqlc.types.Field(JSON, graphql_name='function')


class AdapterModelKeyList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AdapterModelKey))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class Alert(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'code', 'thing', 'thing_type', 'rule', 'level', 'created_at', 'updated_at')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    thing = sgqlc.types.Field(sgqlc.types.non_null('Thing'), graphql_name='thing')
    thing_type = sgqlc.types.Field(sgqlc.types.non_null('ThingType'), graphql_name='thingType')
    rule = sgqlc.types.Field(sgqlc.types.non_null('AlertRule'), graphql_name='rule')
    level = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='level')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='updatedAt')


class AlertConfig(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('levels', 'types')
    levels = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='levels')
    types = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='types')


class AlertList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Alert)), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class AlertRule(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'thing_type', 'alert_type', 'description', 'fx', 'is_owned')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    thing_type = sgqlc.types.Field(sgqlc.types.non_null('ThingType'), graphql_name='thingType')
    alert_type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='alertType')
    description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='description')
    fx = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('FxObject'))), graphql_name='fx')
    is_owned = sgqlc.types.Field(Boolean, graphql_name='isOwned')


class AlertRuleList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(AlertRule)), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class App(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'code', 'key', 'description', 'avatar', 'url', 'is_admin')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    code = sgqlc.types.Field(String, graphql_name='code')
    key = sgqlc.types.Field(String, graphql_name='key')
    description = sgqlc.types.Field(String, graphql_name='description')
    avatar = sgqlc.types.Field('Image', graphql_name='avatar')
    url = sgqlc.types.Field(String, graphql_name='url')
    is_admin = sgqlc.types.Field(Boolean, graphql_name='isAdmin')


class AppBIDatasourceList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('app', 'datasource')
    app = sgqlc.types.Field(App, graphql_name='app')
    datasource = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('BIDatasource'))), graphql_name='datasource')


class AppConfig(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'title', 'icon_url', 'logo_url', 'public_url', 'route_url', 'hide_sidebar', 'entries')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    icon_url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='iconUrl')
    logo_url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='logoUrl')
    public_url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='publicUrl')
    route_url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='routeUrl')
    hide_sidebar = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hideSidebar')
    entries = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('AppEntry'))), graphql_name='entries')


class AppEntry(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('path', 'label', 'icon', 'children', 'permission_key', 'hidden')
    path = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='path')
    label = sgqlc.types.Field(String, graphql_name='label')
    icon = sgqlc.types.Field(String, graphql_name='icon')
    children = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('AppEntry')), graphql_name='children')
    permission_key = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='permissionKey')
    hidden = sgqlc.types.Field(Boolean, graphql_name='hidden')


class AppList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(App)), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ApplyRouterTemplateConfigurationResult(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('total_count', 'success_count', 'failed_count')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    success_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='successCount')
    failed_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='failedCount')


class AreaEnergyConsumptionByCompany(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('company', 'energy_per_product', 'energy', 'power_on_rate')
    company = sgqlc.types.Field('Company', graphql_name='company')
    energy_per_product = sgqlc.types.Field(Float, graphql_name='energyPerProduct')
    energy = sgqlc.types.Field(Float, graphql_name='energy')
    power_on_rate = sgqlc.types.Field(Float, graphql_name='powerOnRate')


class AreaEnergyConsumptionByCompanyData(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(AreaEnergyConsumptionByCompany)), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class AreaEnergyConsumptionOverall(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('energy', 'energy_last', 'energy_to_last', 'energy_previous', 'energy_to_previsous', 'peak_rate', 'peak_rate_last', 'peak_rate_to_last', 'peak_rate_previous', 'peak_rate_to_previsous', 'peak_power', 'peak_power_last', 'peak_power_last_timestamp', 'peak_power_to_last', 'peak_power_previous', 'peak_power_previous_timestamp', 'peak_power_to_previsous', 'present_power', 'peak_power_ever', 'peak_power_ever_timestamp')
    energy = sgqlc.types.Field(Float, graphql_name='energy')
    energy_last = sgqlc.types.Field(Float, graphql_name='energyLast')
    energy_to_last = sgqlc.types.Field(Float, graphql_name='energyToLast')
    energy_previous = sgqlc.types.Field(Float, graphql_name='energyPrevious')
    energy_to_previsous = sgqlc.types.Field(Float, graphql_name='energyToPrevisous')
    peak_rate = sgqlc.types.Field(Float, graphql_name='peakRate')
    peak_rate_last = sgqlc.types.Field(Float, graphql_name='peakRateLast')
    peak_rate_to_last = sgqlc.types.Field(Float, graphql_name='peakRateToLast')
    peak_rate_previous = sgqlc.types.Field(Float, graphql_name='peakRatePrevious')
    peak_rate_to_previsous = sgqlc.types.Field(Float, graphql_name='peakRateToPrevisous')
    peak_power = sgqlc.types.Field(Float, graphql_name='peakPower')
    peak_power_last = sgqlc.types.Field(Float, graphql_name='peakPowerLast')
    peak_power_last_timestamp = sgqlc.types.Field(Timestamp, graphql_name='peakPowerLastTimestamp')
    peak_power_to_last = sgqlc.types.Field(Float, graphql_name='peakPowerToLast')
    peak_power_previous = sgqlc.types.Field(Float, graphql_name='peakPowerPrevious')
    peak_power_previous_timestamp = sgqlc.types.Field(Timestamp, graphql_name='peakPowerPreviousTimestamp')
    peak_power_to_previsous = sgqlc.types.Field(Float, graphql_name='peakPowerToPrevisous')
    present_power = sgqlc.types.Field(Float, graphql_name='presentPower')
    peak_power_ever = sgqlc.types.Field(Float, graphql_name='peakPowerEver')
    peak_power_ever_timestamp = sgqlc.types.Field(Timestamp, graphql_name='peakPowerEverTimestamp')


class AreaPeakRateByCompany(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('company', 'peak_rate', 'energy', 'peak_energy')
    company = sgqlc.types.Field('Company', graphql_name='company')
    peak_rate = sgqlc.types.Field(Float, graphql_name='peakRate')
    energy = sgqlc.types.Field(Float, graphql_name='energy')
    peak_energy = sgqlc.types.Field(Float, graphql_name='peakEnergy')


class AreaPeakRateByCompanyData(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(AreaPeakRateByCompany)), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class AreaProductionByCompany(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('company', 'products', 'to_last', 'to_previous')
    company = sgqlc.types.Field('Company', graphql_name='company')
    products = sgqlc.types.Field(Float, graphql_name='products')
    to_last = sgqlc.types.Field(Float, graphql_name='toLast')
    to_previous = sgqlc.types.Field(Float, graphql_name='toPrevious')


class AreaProductionByCompanyData(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(AreaProductionByCompany)), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class AreaProductionDistribution(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('total', 'to_last', 'to_previous')
    total = sgqlc.types.Field(Float, graphql_name='total')
    to_last = sgqlc.types.Field(Float, graphql_name='toLast')
    to_previous = sgqlc.types.Field(Float, graphql_name='toPrevious')


class AreaThingTimeseriesUnit(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('timestamp', 'num', 'rate')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='timestamp')
    num = sgqlc.types.Field(Int, graphql_name='num')
    rate = sgqlc.types.Field(Float, graphql_name='rate')


class AreaThingsByCompany(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('company', 'num', 'products', 'energy')
    company = sgqlc.types.Field('Company', graphql_name='company')
    num = sgqlc.types.Field(Float, graphql_name='num')
    products = sgqlc.types.Field(Float, graphql_name='products')
    energy = sgqlc.types.Field(Float, graphql_name='energy')


class AreaThingsByCompanyData(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(AreaThingsByCompany)), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class AreaThingsOverall(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('num', 'redundant', 'redundant_rate', 'redundant_last', 'redundant_to_last', 'redundant_previous', 'redundant_to_previous', 'bottleneck', 'bottleneck_rate', 'bottleneck_last', 'bottleneck_to_last', 'bottleneck_previous', 'bottleneck_to_previous')
    num = sgqlc.types.Field(Int, graphql_name='num')
    redundant = sgqlc.types.Field(Int, graphql_name='redundant')
    redundant_rate = sgqlc.types.Field(Float, graphql_name='redundantRate')
    redundant_last = sgqlc.types.Field(Int, graphql_name='redundantLast')
    redundant_to_last = sgqlc.types.Field(Float, graphql_name='redundantToLast')
    redundant_previous = sgqlc.types.Field(Int, graphql_name='redundantPrevious')
    redundant_to_previous = sgqlc.types.Field(Float, graphql_name='redundantToPrevious')
    bottleneck = sgqlc.types.Field(Int, graphql_name='bottleneck')
    bottleneck_rate = sgqlc.types.Field(Float, graphql_name='bottleneckRate')
    bottleneck_last = sgqlc.types.Field(Int, graphql_name='bottleneckLast')
    bottleneck_to_last = sgqlc.types.Field(Float, graphql_name='bottleneckToLast')
    bottleneck_previous = sgqlc.types.Field(Int, graphql_name='bottleneckPrevious')
    bottleneck_to_previous = sgqlc.types.Field(Float, graphql_name='bottleneckToPrevious')


class AuthInfo(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('token', 'user_id')
    token = sgqlc.types.Field(String, graphql_name='token')
    user_id = sgqlc.types.Field(String, graphql_name='userId')


class BICategory(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class BIColumn(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'type')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    type = sgqlc.types.Field(String, graphql_name='type')


class BIDashboard(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'component', 'is_published', 'extra', 'thumbnail', 'attachment', 'created_by', 'created_at', 'updated_at', 'screen')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    component = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(JSON))), graphql_name='component')
    is_published = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isPublished')
    extra = sgqlc.types.Field(sgqlc.types.non_null(JSON), graphql_name='extra')
    thumbnail = sgqlc.types.Field('File', graphql_name='thumbnail')
    attachment = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('File')), graphql_name='attachment')
    created_by = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='createdBy')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='updatedAt')
    screen = sgqlc.types.Field('BIPublishedDashboard', graphql_name='screen')


class BIDashboardList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('total_count', 'data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(BIDashboard))), graphql_name='data')


class BIDataSource(sgqlc.types.Interface):
    __schema__ = platform_schema
    __field_names__ = ('type', 'name', 'created_at')
    type = sgqlc.types.Field(sgqlc.types.non_null(BIDataSourceType), graphql_name='type')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='createdAt')


class BIDatabase(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'uri', 'created_at')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    uri = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='uri')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='createdAt')


class BIDatabaseList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('total_count', 'data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(BIDatabase))), graphql_name='data')


class BIDataset(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'source', 'created_at', 'updated_at')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    source = sgqlc.types.Field(sgqlc.types.non_null(BIDataSource), graphql_name='source')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='updatedAt')


class BIDatasetList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('total_count', 'data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(BIDataset))), graphql_name='data')


class BIDatasource(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'code', 'name', 'used')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    used = sgqlc.types.Field(Boolean, graphql_name='used')


class BIExcel(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('sheet',)
    sheet = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='sheet')


class BIFileDataSourceList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('total_count', 'data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('BIFileDataSource'))), graphql_name='data')


class BIPublishedDashboard(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'category', 'role', 'component', 'extra', 'thumbnail', 'attachment', 'created_at', 'updated_at')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    category = sgqlc.types.Field(BICategory, graphql_name='category')
    role = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('Role')), graphql_name='role')
    component = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(JSON))), graphql_name='component')
    extra = sgqlc.types.Field(sgqlc.types.non_null(JSON), graphql_name='extra')
    thumbnail = sgqlc.types.Field('File', graphql_name='thumbnail')
    attachment = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('File')), graphql_name='attachment')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='updatedAt')


class BIPublishedDashboardList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('total_count', 'data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(BIPublishedDashboard))), graphql_name='data')


class BIResult(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('timestamp', 'metric', 'value')
    timestamp = sgqlc.types.Field(Timestamp, graphql_name='timestamp')
    metric = sgqlc.types.Field(String, graphql_name='metric')
    value = sgqlc.types.Field(Float, graphql_name='value')


class BaseFieldMeta(sgqlc.types.Interface):
    __schema__ = platform_schema
    __field_names__ = ('id', 'type', 'col_name', 'field_name', 'title', 'deletable', 'required', 'field_ratio', 'is_origin', 'hidden', 'filterable', 'prompt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    type = sgqlc.types.Field(sgqlc.types.non_null(FieldType), graphql_name='type')
    col_name = sgqlc.types.Field(String, graphql_name='colName')
    field_name = sgqlc.types.Field(String, graphql_name='fieldName')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    deletable = sgqlc.types.Field(Boolean, graphql_name='deletable')
    required = sgqlc.types.Field(Boolean, graphql_name='required')
    field_ratio = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='fieldRatio')
    is_origin = sgqlc.types.Field(Boolean, graphql_name='isOrigin')
    hidden = sgqlc.types.Field(Boolean, graphql_name='hidden')
    filterable = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='filterable')
    prompt = sgqlc.types.Field(String, graphql_name='prompt')


class BaudRate(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'value')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    value = sgqlc.types.Field(Int, graphql_name='value')


class Bill(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('month', 'personal_cost', 'prod_and_fixed_cost', 'waiver_fee', 'totoal', 'paied_by_others')
    month = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='month')
    personal_cost = sgqlc.types.Field(Float, graphql_name='personalCost')
    prod_and_fixed_cost = sgqlc.types.Field(Float, graphql_name='prodAndFixedCost')
    waiver_fee = sgqlc.types.Field(Float, graphql_name='waiverFee')
    totoal = sgqlc.types.Field(Float, graphql_name='totoal')
    paied_by_others = sgqlc.types.Field(Float, graphql_name='paiedByOthers')


class BomNode(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('procedure', 'made_of', 'material')
    procedure = sgqlc.types.Field('Procedure', graphql_name='procedure')
    made_of = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('MadeOfNode')), graphql_name='madeOf')
    material = sgqlc.types.Field('Material', graphql_name='material')


class CNCAlert(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('code', 'created_at', 'duration')
    code = sgqlc.types.Field(String, graphql_name='code')
    created_at = sgqlc.types.Field(Timestamp, graphql_name='createdAt')
    duration = sgqlc.types.Field(Int, graphql_name='duration')


class CNCAlertList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(CNCAlert)), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class CNCAlertOverall(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('num', 'duration')
    num = sgqlc.types.Field(Int, graphql_name='num')
    duration = sgqlc.types.Field(Int, graphql_name='duration')


class CNCAlertTimeseries(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('timestamp', 'num', 'duration')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='timestamp')
    num = sgqlc.types.Field(Int, graphql_name='num')
    duration = sgqlc.types.Field(Int, graphql_name='duration')


class CNCOverall(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('status', 'start_at')
    status = sgqlc.types.Field(Int, graphql_name='status')
    start_at = sgqlc.types.Field(Timestamp, graphql_name='startAt')


class ChannelProtocol(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'value')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    value = sgqlc.types.Field(String, graphql_name='value')


class City(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('name', 'counties')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    counties = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('County')), graphql_name='counties')


class City_(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'province')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    province = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='province')


class CockpitAggregation(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'thing_type', 'tag', 'frame', 'start', 'end')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    thing_type = sgqlc.types.Field(sgqlc.types.non_null('ThingType'), graphql_name='thingType')
    tag = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='tag')
    frame = sgqlc.types.Field(AggregationFrame, graphql_name='frame')
    start = sgqlc.types.Field(String, graphql_name='start')
    end = sgqlc.types.Field(String, graphql_name='end')


class CockpitKey(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'thing_type', 'key', 'key_type', 'name', 'unit', 'type', 'precision', 'statistic')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    thing_type = sgqlc.types.Field(sgqlc.types.non_null('ThingType'), graphql_name='thingType')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    key_type = sgqlc.types.Field(sgqlc.types.non_null(CockpitKeyType), graphql_name='keyType')
    name = sgqlc.types.Field(String, graphql_name='name')
    unit = sgqlc.types.Field(String, graphql_name='unit')
    type = sgqlc.types.Field(DataType, graphql_name='type')
    precision = sgqlc.types.Field(Int, graphql_name='precision')
    statistic = sgqlc.types.Field(CockpitKeyStatistic, graphql_name='statistic')


class CockpitKeyList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CockpitKey))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class CockpitOrganizationRank(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('organization', 'value')
    organization = sgqlc.types.Field('ThingOrganization', graphql_name='organization')
    value = sgqlc.types.Field(Float, graphql_name='value')


class CockpitOverall(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('focus', 'live', 'total', 'number_by_organziation', 'number_by_thing_type')
    focus = sgqlc.types.Field('CockpitOverallFocus', graphql_name='focus')
    live = sgqlc.types.Field('CockpitOverallLive', graphql_name='live')
    total = sgqlc.types.Field(Int, graphql_name='total')
    number_by_organziation = sgqlc.types.Field(sgqlc.types.list_of('NumberByOrganziation'), graphql_name='numberByOrganziation')
    number_by_thing_type = sgqlc.types.Field(sgqlc.types.list_of('NumberByThingType'), graphql_name='numberByThingType')


class CockpitOverallFocus(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('alarm', 'standby')
    alarm = sgqlc.types.Field(Int, graphql_name='alarm')
    standby = sgqlc.types.Field(Int, graphql_name='standby')


class CockpitOverallLive(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('operation', 'alarm', 'standby', 'shutdown')
    operation = sgqlc.types.Field(Int, graphql_name='operation')
    alarm = sgqlc.types.Field(Int, graphql_name='alarm')
    standby = sgqlc.types.Field(Int, graphql_name='standby')
    shutdown = sgqlc.types.Field(Int, graphql_name='shutdown')


class CockpitRate(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('timestamp', 'oee', 'operation_rate', 'performance_rate', 'yield_rate')
    timestamp = sgqlc.types.Field(Timestamp, graphql_name='timestamp')
    oee = sgqlc.types.Field(Float, graphql_name='OEE')
    operation_rate = sgqlc.types.Field(Float, graphql_name='operationRate')
    performance_rate = sgqlc.types.Field(Float, graphql_name='performanceRate')
    yield_rate = sgqlc.types.Field(Float, graphql_name='yieldRate')


class CockpitRateList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CockpitRate))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class CockpitRateOverall(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('oee', 'operation_rate', 'performance_rate', 'yield_rate')
    oee = sgqlc.types.Field(Float, graphql_name='OEE')
    operation_rate = sgqlc.types.Field(Float, graphql_name='operationRate')
    performance_rate = sgqlc.types.Field(Float, graphql_name='performanceRate')
    yield_rate = sgqlc.types.Field(Float, graphql_name='yieldRate')


class CockpitTarget(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'timestamp', 'oee', 'operation_rate', 'performance_rate', 'yield_rate')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='timestamp')
    oee = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='OEE')
    operation_rate = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='operationRate')
    performance_rate = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='performanceRate')
    yield_rate = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='yieldRate')


class CockpitTargetList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CockpitTarget))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class CockpitThing(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('thing', 'status', 'duration')
    thing = sgqlc.types.Field('Thing', graphql_name='thing')
    status = sgqlc.types.Field(ThingStatusType, graphql_name='status')
    duration = sgqlc.types.Field(Int, graphql_name='duration')


class CockpitThingList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CockpitThing))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class CockpitThingTypeRank(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('type', 'value')
    type = sgqlc.types.Field('ThingType', graphql_name='type')
    value = sgqlc.types.Field(Float, graphql_name='value')


class CockpitTimeseries(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('timestamp', 'value', 'target')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='timestamp')
    value = sgqlc.types.Field(Float, graphql_name='value')
    target = sgqlc.types.Field(Float, graphql_name='target')


class CollectConfiguration(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('collect_period', 'report_period', 'interface_type', 'channel_protocol', 'ethernet_channel', 'serial_channel', 'collect_points')
    collect_period = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='collectPeriod')
    report_period = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='reportPeriod')
    interface_type = sgqlc.types.Field(sgqlc.types.non_null(InterfaceType), graphql_name='interfaceType')
    channel_protocol = sgqlc.types.Field(sgqlc.types.non_null(ChannelProtocol), graphql_name='channelProtocol')
    ethernet_channel = sgqlc.types.Field('EthernetChannel', graphql_name='ethernetChannel')
    serial_channel = sgqlc.types.Field('SerialChannel', graphql_name='serialChannel')
    collect_points = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('CollectPoint'))), graphql_name='collectPoints')


class CollectPoint(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('name', 'alias_name', 'register_type', 'data_type', 'addr_offset')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    alias_name = sgqlc.types.Field(String, graphql_name='aliasName')
    register_type = sgqlc.types.Field(sgqlc.types.non_null('RegisterType'), graphql_name='registerType')
    data_type = sgqlc.types.Field(sgqlc.types.non_null('RegisterDataType'), graphql_name='dataType')
    addr_offset = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='addrOffset')


class CommonSummary(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('key', 'value')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    value = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='value')


class Company(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'type', 'name', 'address', 'uscc', 'contact', 'email', 'phone', 'province', 'city', 'county', 'is_mine')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    type = sgqlc.types.Field(sgqlc.types.non_null('CompanyType'), graphql_name='type')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    address = sgqlc.types.Field(String, graphql_name='address')
    uscc = sgqlc.types.Field(String, graphql_name='uscc')
    contact = sgqlc.types.Field(String, graphql_name='contact')
    email = sgqlc.types.Field(String, graphql_name='email')
    phone = sgqlc.types.Field(String, graphql_name='phone')
    province = sgqlc.types.Field(String, graphql_name='province')
    city = sgqlc.types.Field(String, graphql_name='city')
    county = sgqlc.types.Field(String, graphql_name='county')
    is_mine = sgqlc.types.Field(Boolean, graphql_name='isMine')


class CompanyApps(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('company', 'apps')
    company = sgqlc.types.Field(sgqlc.types.non_null(Company), graphql_name='company')
    apps = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(App)), graphql_name='apps')


class CompanyAppsList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('total_count', 'data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(CompanyApps)), graphql_name='data')


class CompanyBIDatasource(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'app', 'datasource', 'created_at')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    app = sgqlc.types.Field(sgqlc.types.non_null(App), graphql_name='app')
    datasource = sgqlc.types.Field(sgqlc.types.non_null(BIDatasource), graphql_name='datasource')
    created_at = sgqlc.types.Field(Timestamp, graphql_name='createdAt')


class CompanyBIDatasourceList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(CompanyBIDatasource)), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class CompanyDemand(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'serial_number', 'name', 'created_at', 'updated_at', 'company_id', 'company_name', 'content', 'status', 'email', 'phone', 'created_by', 'accepted_by', 'review_record', 'is_public')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    serial_number = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='serialNumber')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='updatedAt')
    company_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='companyId')
    company_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='companyName')
    content = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='content')
    status = sgqlc.types.Field(sgqlc.types.non_null(CompanyDemandStatus), graphql_name='status')
    email = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='email')
    phone = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='phone')
    created_by = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='createdBy')
    accepted_by = sgqlc.types.Field('User', graphql_name='acceptedBy')
    review_record = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('CompanyDemandReviewRecord')), graphql_name='reviewRecord')
    is_public = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isPublic')


class CompanyDemandList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(CompanyDemand)), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class CompanyDemandReviewRecord(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'operation', 'reviewed_at', 'brief', 'reviewed_by')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    operation = sgqlc.types.Field(sgqlc.types.non_null(CompanyReviewOperation), graphql_name='operation')
    reviewed_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='reviewedAt')
    brief = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='brief')
    reviewed_by = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='reviewedBy')


class CompanyDemandSummay(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('total_count', 'approved_count', 'rejected_count', 'pending_count')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    approved_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='approvedCount')
    rejected_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='rejectedCount')
    pending_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='pendingCount')


class CompanyList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Company)), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class CompanyOverall(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('products', 'fee', 'energy')
    products = sgqlc.types.Field(Float, graphql_name='products')
    fee = sgqlc.types.Field(Float, graphql_name='fee')
    energy = sgqlc.types.Field(Float, graphql_name='energy')


class CompanyRank(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('CompanyRankDetail')), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class CompanyRankDetail(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('company', 'value')
    company = sgqlc.types.Field(Company, graphql_name='company')
    value = sgqlc.types.Field(Float, graphql_name='value')


class CompanyRecruitBrief(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'content', 'images')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    content = sgqlc.types.Field(String, graphql_name='content')
    images = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('Image')), graphql_name='images')


class CompanyThingList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('total_count', 'data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Thing'))), graphql_name='data')


class CompanyThingOrganizationNode(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('company', 'thing_organizations')
    company = sgqlc.types.Field(sgqlc.types.non_null(Company), graphql_name='company')
    thing_organizations = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('ThingOrganizationWithChildren')), graphql_name='thingOrganizations')


class CompanyType(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class CompanyTypeList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CompanyType))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class County(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('name', 'companies')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    companies = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Company)), graphql_name='companies')


class County_(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'city')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    city = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='city')


class DataBit(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'value')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    value = sgqlc.types.Field(Int, graphql_name='value')


class Department(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'path_name', 'parent_id')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    path_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='pathName')
    parent_id = sgqlc.types.Field(ID, graphql_name='parentID')


class DepartmentList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Department)), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class DeptThingGroupList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('DeptThingGroups')), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class DeptThingGroups(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('department', 'thing_groups')
    department = sgqlc.types.Field(sgqlc.types.non_null(Department), graphql_name='department')
    thing_groups = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('ThingGroup')), graphql_name='thingGroups')


class DeviceChannelConfiguration(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'model', 'collects')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    model = sgqlc.types.Field(sgqlc.types.non_null('RouterModel'), graphql_name='model')
    collects = sgqlc.types.Field(sgqlc.types.non_null(CollectConfiguration), graphql_name='collects')


class DeviceChannelConfigurationList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(DeviceChannelConfiguration))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class Directory(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class DmegcOverall(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('device_number', 'fee', 'energy', 'production', 'operation', 'operation_percentage', 'alarm', 'alarm_percentage', 'standby', 'standby_percentage', 'shutdown', 'shutdown_percentage', 'bottleneck', 'redundant')
    device_number = sgqlc.types.Field(Int, graphql_name='deviceNumber')
    fee = sgqlc.types.Field(Float, graphql_name='fee')
    energy = sgqlc.types.Field(Float, graphql_name='energy')
    production = sgqlc.types.Field(Float, graphql_name='production')
    operation = sgqlc.types.Field(Int, graphql_name='operation')
    operation_percentage = sgqlc.types.Field(Float, graphql_name='operationPercentage')
    alarm = sgqlc.types.Field(Int, graphql_name='alarm')
    alarm_percentage = sgqlc.types.Field(Float, graphql_name='alarmPercentage')
    standby = sgqlc.types.Field(Int, graphql_name='standby')
    standby_percentage = sgqlc.types.Field(Float, graphql_name='standbyPercentage')
    shutdown = sgqlc.types.Field(Int, graphql_name='shutdown')
    shutdown_percentage = sgqlc.types.Field(Float, graphql_name='shutdownPercentage')
    bottleneck = sgqlc.types.Field(Int, graphql_name='bottleneck')
    redundant = sgqlc.types.Field(Int, graphql_name='redundant')


class DmegcParetoTimeseries(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('timestamp', 'value', 'accumulative')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='timestamp')
    value = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='value')
    accumulative = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='accumulative')


class DmegcTimeseries(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('timestamp', 'value')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='timestamp')
    value = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='value')


class EnergyConsumptionComparison(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('total', 'avg', 'num', 'trends')
    total = sgqlc.types.Field(Float, graphql_name='total')
    avg = sgqlc.types.Field(Float, graphql_name='avg')
    num = sgqlc.types.Field(Int, graphql_name='num')
    trends = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('EnergyConsumptionComparisonTrend')), graphql_name='trends')


class EnergyConsumptionComparisonTrend(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('name', 'total', 'order', 'values')
    name = sgqlc.types.Field(String, graphql_name='name')
    total = sgqlc.types.Field(Float, graphql_name='total')
    order = sgqlc.types.Field(Int, graphql_name='order')
    values = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('TimeseriesUnit')), graphql_name='values')


class EnergyConsumptionToT(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('present', 'last', 'delta', 'tot')
    present = sgqlc.types.Field(Float, graphql_name='present')
    last = sgqlc.types.Field(Float, graphql_name='last')
    delta = sgqlc.types.Field(Float, graphql_name='delta')
    tot = sgqlc.types.Field(Float, graphql_name='tot')


class EnergyFeeBIResult(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('timestamp', 'energy_group', 'value')
    timestamp = sgqlc.types.Field(Timestamp, graphql_name='timestamp')
    energy_group = sgqlc.types.Field('EnergyGroup', graphql_name='energyGroup')
    value = sgqlc.types.Field(Float, graphql_name='value')


class EnergyGroup(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class EnergyGroupList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(EnergyGroup))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class EnergyTimeDistribution(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('peak', 'sharp', 'valley', 'normal')
    peak = sgqlc.types.Field('TimeDistribution', graphql_name='peak')
    sharp = sgqlc.types.Field('TimeDistribution', graphql_name='sharp')
    valley = sgqlc.types.Field('TimeDistribution', graphql_name='valley')
    normal = sgqlc.types.Field('TimeDistribution', graphql_name='normal')


class EnergyTimeDistributionList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(EnergyTimeDistribution))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class EnergyTrend(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('present', 'last')
    present = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('TimeseriesUnit')), graphql_name='present')
    last = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('TimeseriesUnit')), graphql_name='last')


class EprectMold(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'code')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')


class EprectMoldList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(EprectMold))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class EprectProductionRecord(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'thing_id', 'thing_name', 'mold_id', 'mold_name', 'mold_code', 'start', 'end', 'yield_per_unit_time', 'arguments')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    thing_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='thingId')
    thing_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='thingName')
    mold_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='moldId')
    mold_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='moldName')
    mold_code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='moldCode')
    start = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='start')
    end = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='end')
    yield_per_unit_time = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='yieldPerUnitTime')
    arguments = sgqlc.types.Field(sgqlc.types.non_null(JSONString), graphql_name='arguments')


class EprectProductionRecordList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(EprectProductionRecord))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class EthernetChannel(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('ip', 'port', 'slave_id')
    ip = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='ip')
    port = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='port')
    slave_id = sgqlc.types.Field(Int, graphql_name='slaveId')


class ExtentedFaultReason(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('reason', 'rule')
    reason = sgqlc.types.Field('FaultReason', graphql_name='reason')
    rule = sgqlc.types.Field('FaultRule', graphql_name='rule')


class Fault(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'thing', 'rule', 'level', 'created_at')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    thing = sgqlc.types.Field(sgqlc.types.non_null('Thing'), graphql_name='thing')
    rule = sgqlc.types.Field(sgqlc.types.non_null('FaultRule'), graphql_name='rule')
    level = sgqlc.types.Field(sgqlc.types.non_null(FalutLevel), graphql_name='level')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='createdAt')


class FaultFxObject(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('ast', 'result')
    ast = sgqlc.types.Field(sgqlc.types.non_null(JSONString), graphql_name='ast')
    result = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='result')


class FaultIssue(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'fault', 'code', 'created_at', 'updated_at', 'status', 'accept_account', 'issue_logs', 'reasons')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    fault = sgqlc.types.Field(sgqlc.types.non_null(Fault), graphql_name='fault')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='updatedAt')
    status = sgqlc.types.Field(sgqlc.types.non_null(FaultIssueStatus), graphql_name='status')
    accept_account = sgqlc.types.Field('User', graphql_name='acceptAccount')
    issue_logs = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('FaultIssueLog')), graphql_name='issueLogs')
    reasons = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('FaultReasonSolutionRelation')), graphql_name='reasons')


class FaultIssueList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(FaultIssue)), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class FaultIssueLog(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'action', 'timestamp', 'repair_date', 'remark', 'sender', 'receiver', 'desc', 'attachments')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    action = sgqlc.types.Field(sgqlc.types.non_null(FaultIssueAction), graphql_name='action')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='timestamp')
    repair_date = sgqlc.types.Field(Timestamp, graphql_name='repairDate')
    remark = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='remark')
    sender = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='sender')
    receiver = sgqlc.types.Field('User', graphql_name='receiver')
    desc = sgqlc.types.Field(String, graphql_name='desc')
    attachments = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('File')), graphql_name='attachments')


class FaultIssueSummary(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('total_count', 'ready_count', 'dealing_count', 'closed_count', 'high_level_count', 'medium_level_count', 'low_level_count')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    ready_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='readyCount')
    dealing_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='dealingCount')
    closed_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='closedCount')
    high_level_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='highLevelCount')
    medium_level_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='mediumLevelCount')
    low_level_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='lowLevelCount')


class FaultList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Fault)), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class FaultReason(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'content')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    content = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='content')


class FaultReasonSolutionRelation(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'reason', 'caused_reason', 'solution')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    reason = sgqlc.types.Field(sgqlc.types.non_null(FaultReason), graphql_name='reason')
    caused_reason = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='causedReason')
    solution = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('FaultSolution')), graphql_name='solution')


class FaultRule(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'desc', 'type', 'thing_type', 'fx', 'reasons')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    desc = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='desc')
    type = sgqlc.types.Field(sgqlc.types.non_null(FaultType), graphql_name='type')
    thing_type = sgqlc.types.Field(sgqlc.types.non_null('ThingType'), graphql_name='thingType')
    fx = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(FaultFxObject))), graphql_name='fx')
    reasons = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(FaultReason))), graphql_name='reasons')


class FaultRuleList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(FaultRule))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class FaultRuleReasonSolutionRelation(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('reason', 'solution')
    reason = sgqlc.types.Field(sgqlc.types.non_null(FaultReason), graphql_name='reason')
    solution = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('FaultSolution')), graphql_name='solution')


class FaultSolution(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'title', 'brief', 'directory', 'content', 'attachments', 'created_at', 'created_by', 'updated_at', 'updated_by', 'reasons')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    brief = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='brief')
    directory = sgqlc.types.Field(sgqlc.types.non_null(Directory), graphql_name='directory')
    content = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='content')
    attachments = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('File')), graphql_name='attachments')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='createdAt')
    created_by = sgqlc.types.Field('User', graphql_name='createdBy')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='updatedAt')
    updated_by = sgqlc.types.Field('User', graphql_name='updatedBy')
    reasons = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ExtentedFaultReason)), graphql_name='reasons')


class FaultSolutionList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(FaultSolution))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class Fee(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('timestamp', 'energy_consumption', 'value')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='timestamp')
    energy_consumption = sgqlc.types.Field(Float, graphql_name='energyConsumption')
    value = sgqlc.types.Field(Float, graphql_name='value')


class FeeReport(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('energy_group', 'energy_type', 'fees', 'total')
    energy_group = sgqlc.types.Field(sgqlc.types.non_null(EnergyGroup), graphql_name='energyGroup')
    energy_type = sgqlc.types.Field(EnergyType, graphql_name='energyType')
    fees = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Fee)), graphql_name='fees')
    total = sgqlc.types.Field(sgqlc.types.non_null('TotalFee'), graphql_name='total')


class FeeReportList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(FeeReport)), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class FieldCandidates(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'candidates')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    candidates = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='candidates')


class File(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'url', 'length')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')
    length = sgqlc.types.Field(Int, graphql_name='length')


class FormStruct(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('name', 'display_name', 'custom_fields')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    display_name = sgqlc.types.Field(String, graphql_name='displayName')
    custom_fields = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('FieldMeta'))), graphql_name='customFields')


class FxObject(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('ast', 'result')
    ast = sgqlc.types.Field(sgqlc.types.non_null(JSONString), graphql_name='ast')
    result = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='result')


class HistoryData(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('timestamp', 'data')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='timestamp')
    data = sgqlc.types.Field(JSONString, graphql_name='data')


class HistoryStatusData(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('timestamp',)
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='timestamp')


class IDName(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class Image(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'url')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')


class ImportStudentResult(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('sucess', 'failed')
    sucess = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='sucess')
    failed = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='failed')


class Issue(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'code', 'title', 'content', 'attachments', 'create_time', 'update_time', 'status', 'type', 'owner', 'issuer', 'company', 'logs')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    content = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='content')
    attachments = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(File)), graphql_name='attachments')
    create_time = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='createTime')
    update_time = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='updateTime')
    status = sgqlc.types.Field(sgqlc.types.non_null(IssueStatus), graphql_name='status')
    type = sgqlc.types.Field(IssueType, graphql_name='type')
    owner = sgqlc.types.Field('User', graphql_name='owner')
    issuer = sgqlc.types.Field('User', graphql_name='issuer')
    company = sgqlc.types.Field(Company, graphql_name='company')
    logs = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IssueLog')), graphql_name='logs')


class IssueList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count', 'ready', 'dealing', 'close')
    data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Issue)), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    ready = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='ready')
    dealing = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='dealing')
    close = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='close')


class IssueLog(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('timestamp', 'action', 'remark', 'attachments', 'sender', 'receiver', 'reason')
    timestamp = sgqlc.types.Field(Timestamp, graphql_name='timestamp')
    action = sgqlc.types.Field(IssueAction, graphql_name='action')
    remark = sgqlc.types.Field(String, graphql_name='remark')
    attachments = sgqlc.types.Field(sgqlc.types.list_of(File), graphql_name='attachments')
    sender = sgqlc.types.Field('User', graphql_name='sender')
    receiver = sgqlc.types.Field('User', graphql_name='receiver')
    reason = sgqlc.types.Field(IssueReason, graphql_name='reason')


class JhdvCityStatistic(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('total_company_count', 'total_device_count', 'leader_companies')
    total_company_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCompanyCount')
    total_device_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalDeviceCount')
    leader_companies = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('JhdvCompanySummary'))), graphql_name='leaderCompanies')


class JhdvCompanySummary(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('name', 'industry', 'region', 'device_running_statistic', 'device_index_data')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    industry = sgqlc.types.Field(sgqlc.types.non_null('JhdvIndustry'), graphql_name='industry')
    region = sgqlc.types.Field(sgqlc.types.non_null('JhdvRegion'), graphql_name='region')
    device_running_statistic = sgqlc.types.Field(sgqlc.types.non_null('JhdvDeviceRunningStatistic'), graphql_name='deviceRunningStatistic')
    device_index_data = sgqlc.types.Field(sgqlc.types.non_null('JhdvDeviceIndexData'), graphql_name='deviceIndexData')


class JhdvDeviceAlarmMessage(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('device_name', 'code', 'alarm_at')
    device_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='deviceName')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    alarm_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='alarmAt')


class JhdvDeviceChartData(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('label', 'value')
    label = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='label')
    value = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='value')


class JhdvDeviceIndexData(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('total_electric_quantity', 'production', 'oee', 'time_utilization', 'speed_utilization', 'yield_rate')
    total_electric_quantity = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='totalElectricQuantity')
    production = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='production')
    oee = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='oee')
    time_utilization = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='timeUtilization')
    speed_utilization = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='speedUtilization')
    yield_rate = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='yieldRate')


class JhdvDeviceIndexDataRank(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('energy', 'production', 'oee', 'time_utilization', 'speed_utilization', 'yield_rate')
    energy = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(JhdvDeviceChartData))), graphql_name='energy')
    production = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(JhdvDeviceChartData))), graphql_name='production')
    oee = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(JhdvDeviceChartData))), graphql_name='oee')
    time_utilization = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(JhdvDeviceChartData))), graphql_name='timeUtilization')
    speed_utilization = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(JhdvDeviceChartData))), graphql_name='speedUtilization')
    yield_rate = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(JhdvDeviceChartData))), graphql_name='yieldRate')


class JhdvDeviceIndexDataSummary(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('bottleneck_count', 'redundant_count', 'production', 'oee', 'total_electric_quantity')
    bottleneck_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='bottleneckCount')
    redundant_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='redundantCount')
    production = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='production')
    oee = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='oee')
    total_electric_quantity = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='totalElectricQuantity')


class JhdvDeviceRunningStatistic(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('statistic', 'alarm_messages')
    statistic = sgqlc.types.Field(sgqlc.types.non_null('JhdvDeviceStatistic'), graphql_name='statistic')
    alarm_messages = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(JhdvDeviceAlarmMessage))), graphql_name='alarmMessages')


class JhdvDeviceStatistic(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('total_count', 'operation_count', 'standby_count', 'alarm_count', 'shutdown_count')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    operation_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='operationCount')
    standby_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='standbyCount')
    alarm_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='alarmCount')
    shutdown_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='shutdownCount')


class JhdvIndustry(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class JhdvIndustryList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(JhdvIndustry))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class JhdvRegion(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('name', 'adcode')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    adcode = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='adcode')


class JhdvRegionStatistic(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('region', 'total_electric_quantity', 'production', 'total_company_count', 'total_device_count')
    region = sgqlc.types.Field(sgqlc.types.non_null(JhdvRegion), graphql_name='region')
    total_electric_quantity = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='totalElectricQuantity')
    production = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='production')
    total_company_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCompanyCount')
    total_device_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalDeviceCount')


class JhdvRegionStatisticList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(JhdvRegionStatistic))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class JunyeAlarmDistribution(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('reason', 'number')
    reason = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='reason')
    number = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='number')


class JunyeAnnualPlan(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('scheduled_count', 'actual_count')
    scheduled_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='scheduledCount')
    actual_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='actualCount')


class JunyeAnnualRevenue(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('year', 'earning', 'order_count')
    year = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='year')
    earning = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='earning')
    order_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='orderCount')


class JunyeBusinessSituation(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('annual_revenue', 'customer_constitute')
    annual_revenue = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(JunyeAnnualRevenue))), graphql_name='annualRevenue')
    customer_constitute = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('JunyeCustomerConstitute'))), graphql_name='customerConstitute')


class JunyeCustomerConstitute(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('kind', 'number')
    kind = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='kind')
    number = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='number')


class JunyeDailyIO(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('date', 'scheduled_count', 'actual_count')
    date = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='date')
    scheduled_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='scheduledCount')
    actual_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='actualCount')


class JunyeEnergyConsumption(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('date', 'electricity', 'water', 'gas')
    date = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='date')
    electricity = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='electricity')
    water = sgqlc.types.Field(Int, graphql_name='water')
    gas = sgqlc.types.Field(Int, graphql_name='gas')


class JunyeMaterialManagement(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('purchase_receipt', 'requisition', 'product_receipt')
    purchase_receipt = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(JunyeDailyIO))), graphql_name='purchaseReceipt')
    requisition = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(JunyeDailyIO))), graphql_name='requisition')
    product_receipt = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(JunyeDailyIO))), graphql_name='productReceipt')


class JunyeMetricData(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('kind', 'name', 'value', 'unit')
    kind = sgqlc.types.Field(sgqlc.types.non_null(JunyeMetricKind), graphql_name='kind')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='value')
    unit = sgqlc.types.Field(sgqlc.types.non_null(JunyeMetricUnit), graphql_name='unit')


class JunyeProductDelivery(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('product', 'scheduled_count', 'actual_count')
    product = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='product')
    scheduled_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='scheduledCount')
    actual_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='actualCount')


class JunyeProductionPlan(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('annual_plan', 'product_delivery')
    annual_plan = sgqlc.types.Field(sgqlc.types.non_null(JunyeAnnualPlan), graphql_name='annualPlan')
    product_delivery = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(JunyeProductDelivery))), graphql_name='productDelivery')


class JunyeThingStatusDistribution(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('status', 'number')
    status = sgqlc.types.Field(sgqlc.types.non_null(ThingStatusType), graphql_name='status')
    number = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='number')


class JunyeThingType(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class JunyeThingTypeDistribution(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('thing_type', 'number')
    thing_type = sgqlc.types.Field(sgqlc.types.non_null(JunyeThingType), graphql_name='thingType')
    number = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='number')


class MacroBIResult(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('timestamp', 'company', 'value')
    timestamp = sgqlc.types.Field(Timestamp, graphql_name='timestamp')
    company = sgqlc.types.Field(Company, graphql_name='company')
    value = sgqlc.types.Field(Float, graphql_name='value')


class MadeOfNode(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'rate')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    rate = sgqlc.types.Field('ProductionRate', graphql_name='rate')


class MarketApp(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'title', 'type', 'published_at', 'updated_at', 'created_by', 'is_recommended', 'brief', 'description', 'cover_image', 'screenshot')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    type = sgqlc.types.Field(sgqlc.types.non_null(MarketAppType), graphql_name='type')
    published_at = sgqlc.types.Field(Timestamp, graphql_name='publishedAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='updatedAt')
    created_by = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='createdBy')
    is_recommended = sgqlc.types.Field(Boolean, graphql_name='isRecommended')
    brief = sgqlc.types.Field(String, graphql_name='brief')
    description = sgqlc.types.Field(String, graphql_name='description')
    cover_image = sgqlc.types.Field(File, graphql_name='coverImage')
    screenshot = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(File)), graphql_name='screenshot')


class MarketAppList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(MarketApp)), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class MarketAppSummary(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('published', 'draft', 'total')
    published = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='published')
    draft = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='draft')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')


class MarketCommonComponent(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('title', 'content', 'image')
    title = sgqlc.types.Field(String, graphql_name='title')
    content = sgqlc.types.Field(String, graphql_name='content')
    image = sgqlc.types.Field(File, graphql_name='image')


class MarketIssue(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'code', 'type', 'app', 'solution', 'created_at', 'updated_at', 'company_name', 'phone', 'email', 'contact', 'status', 'owner', 'content', 'issue_log')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    code = sgqlc.types.Field(String, graphql_name='code')
    type = sgqlc.types.Field(sgqlc.types.non_null(MarketConsultationType), graphql_name='type')
    app = sgqlc.types.Field(MarketApp, graphql_name='app')
    solution = sgqlc.types.Field('MarketSolution', graphql_name='solution')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='createdAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='updatedAt')
    company_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='companyName')
    phone = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='phone')
    email = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='email')
    contact = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='contact')
    status = sgqlc.types.Field(sgqlc.types.non_null(MarketIssueStatus), graphql_name='status')
    owner = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='owner')
    content = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='content')
    issue_log = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('MarketIssueLog')), graphql_name='issueLog')


class MarketIssueList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(MarketIssue)), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class MarketIssueLog(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'action', 'operated_at', 'sender', 'receiver', 'description', 'attachment')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    action = sgqlc.types.Field(sgqlc.types.non_null(MarketIssueAction), graphql_name='action')
    operated_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='operatedAt')
    sender = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='sender')
    receiver = sgqlc.types.Field('User', graphql_name='receiver')
    description = sgqlc.types.Field(String, graphql_name='description')
    attachment = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(File)), graphql_name='attachment')


class MarketIssueSummary(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('ready', 'dealing', 'close')
    ready = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='ready')
    dealing = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='dealing')
    close = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='close')


class MarketSolution(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'title', 'cover_image', 'type', 'is_recommended', 'brief', 'description', 'app', 'published_at', 'updated_at', 'created_by', 'detail')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    cover_image = sgqlc.types.Field(File, graphql_name='coverImage')
    type = sgqlc.types.Field(sgqlc.types.non_null(MarketSolutionType), graphql_name='type')
    is_recommended = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isRecommended')
    brief = sgqlc.types.Field(String, graphql_name='brief')
    description = sgqlc.types.Field(String, graphql_name='description')
    app = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(MarketApp)), graphql_name='app')
    published_at = sgqlc.types.Field(Timestamp, graphql_name='publishedAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='updatedAt')
    created_by = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='createdBy')
    detail = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('MarketSolutionDetail')), graphql_name='detail')


class MarketSolutionDetail(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('title', 'items', 'image', 'content', 'type')
    title = sgqlc.types.Field(String, graphql_name='title')
    items = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(MarketCommonComponent)), graphql_name='items')
    image = sgqlc.types.Field(File, graphql_name='image')
    content = sgqlc.types.Field(String, graphql_name='content')
    type = sgqlc.types.Field(sgqlc.types.non_null(CardType), graphql_name='type')


class MarketSolutionList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(MarketSolution)), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class MarketSolutionSummary(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('published', 'draft', 'total')
    published = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='published')
    draft = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='draft')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')


class Material(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'type', 'procedure_segment')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    type = sgqlc.types.Field(sgqlc.types.non_null(MaterialType), graphql_name='type')
    procedure_segment = sgqlc.types.Field('ProcedureSegment', graphql_name='procedureSegment')


class MaterialList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Material))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class MonthlyTrafficUsage(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('prod_name', 'total', 'used', 'left')
    prod_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='prodName')
    total = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='total')
    used = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='used')
    left = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='left')


class Mutation(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('create_bifile', 'create_bifiles', 'create_bicategory', 'create_bidashboard', 'update_bidashboard', 'publish_bidashboard', 'unpublish_bidashboard', 'delete_bidashboard', 'copy_bidashboard', 'create_bidatabase', 'update_bidatabase', 'delete_bidatabase', 'delete_bifile_data_source', 'create_bidataset', 'delete_bidataset', 'refresh_bidataset', 'create_train_school_recruit_task', 'update_train_school_recruit_task', 'sign_train_school_recruit_task', 'review_train_school_recruit_task', 'close_train_school_recruit_task', 'create_chan_jiao_file', 'create_chan_jiao_files', 'create_social_person', 'update_social_person', 'review_social_person', 'create_recruit_job', 'update_recruit_job', 'audit_recruit_job', 'delete_recruit_job', 'sign_recruit_job', 'audit_recruit_job_sign_record', 'set_company_recruit_brief', 'create_recruit_student', 'update_recruit_student', 'sign_train_course', 'create_train_course', 'update_train_course', 'review_sign_up_train_course', 'review_authenticate_train_course', 'close_train_course', 'restart_train_course', 'import_authentication', 'create_train_school_student', 'update_train_school_student', 'delete_train_school_student', 'import_student_info', 'create_train_work_type', 'update_train_work_type', 'delete_train_work_type', 'set_train_work_level', 'create_train_faculty', 'update_train_faculty', 'delete_train_faculty', 'create_train_class', 'update_train_class', 'delete_train_class', 'create_company_demand', 'update_company_demand', 'review_company_demand', 'create_report', 'update_report', 'notify_energy_consumption', 'create_cockpit_target', 'update_cockpit_target', 'delete_cockpit_target', 'create_thing_input_record', 'update_thing_input_record', 'delete_thing_input_record', 'create_eam_file', 'create_eam_files', 'create_thing_inspection', 'update_thing_inspection', 'update_thing_inspection_status', 'update_thing_inspection_feedback', 'delete_thing_inspections', 'create_thing_inspection_rule', 'update_thing_inspection_rule', 'delete_inspection_rules', 'create_spare_part_receipt', 'update_spare_part_receipt', 'delete_spare_part_receipts', 'create_thing_maintenance_rule', 'update_thing_maintenance_rule', 'delete_thing_maintenance_rules', 'create_thing_maintenance', 'update_thing_maintenance', 'update_thing_maintenance_feedback', 'update_thing_maintenance_status', 'delete_thing_maintenances', 'create_thing', 'update_thing', 'delete_things', 'import_things', 'create_thing_group', 'update_thing_group', 'delete_thing_group', 'set_users_thing_group', 'set_departments_thing_group', 'set_single_user_thing_groups', 'set_single_department_thing_groups', 'update_department_thing_group', 'update_user_thing_group', 'move_things', 'delete_user_thing_groups', 'delete_department_thing_groups', 'update_form_struct', 'create_spare_part', 'update_spare_part', 'delete_spare_parts', 'import_spare_parts', 'create_thing_repair', 'create_thing_repairs', 'update_thing_repair', 'update_thing_repair_feedback', 'audit_thing_repair', 'delete_thing_repairs', 'create_spare_part_outbound', 'update_spare_part_outbound', 'audit_spare_part_outbound', 'delete_spare_part_outbounds', 'create_edm_file', 'create_edm_files', 'create_router_template_configuration', 'update_router_template_configuration', 'delete_router_template_configuration', 'create_device_channel_configuration', 'update_device_channel_configuration', 'delete_device_channel_configuration', 'apply_router_template_configuration', 'create_router', 'update_router', 'delete_router', 'import_router', 'update_routers_alarm_rules', 'update_router_alarm_records', 'create_fault_file', 'create_fault_files', 'create_fault_reason', 'update_fault_issue', 'create_fault_solution', 'update_fault_solution', 'delete_fault_solution', 'create_fault_rule', 'update_fault_rule', 'delete_fault_rule', 'create_directory', 'update_directory', 'delete_directory', 'move_fault_solution', 'create_production_ticket_file', 'create_production_team', 'create_production_team_plus', 'update_production_team', 'delete_production_team', 'create_production_teammate', 'update_production_teammate', 'delete_production_teammate', 'upload_production_teammate', 'update_production_schedule', 'delete_production_schedule', 'start_production_sub_schedule', 'update_production_sub_schedule', 'assign_production_sub_schedule', 'assign_production_ticket', 'create_production_ticket', 'update_production_ticket', 'delete_production_ticket', 'start_production', 'end_production', '_junye_dummy', 'junye_flush_metric', 'create_thing_type', 'update_thing_type', 'delete_thing_types', 'create_source_key', 'update_source_key', 'delete_source_keys', 'create_adapter_key', 'debug_adapter_key', 'update_adapter_key', 'delete_adapter_keys', 'create_cockpit_key', 'update_cockpit_key', 'delete_cockpit_keys', 'create_cockpit_aggregation', 'update_cockpit_aggregation', 'delete_cockpit_aggregations', 'create_thing_status', 'update_thing_status', 'delete_thing_statuses', 'create_energy_group', 'update_energy_group', 'delete_energy_groups', 'update_energy_time_distribution', 'create_thing_organization', 'update_thing_organization', 'delete_thing_organizations', 'create_worker', 'update_worker', 'delete_workers', 'create_work_group', 'update_work_group', 'delete_work_groups', 'create_work_shift', 'update_work_shift', 'delete_work_shifts', 'create_material', 'update_material', 'delete_material', 'create_procedure', 'update_procedure', 'delete_procedures', 'create_procedure_segment', 'update_procedure_segment', 'delete_procedure_segments', 'set_work_duty', 'create_production_process', 'update_production_process', 'delete_production_processes', 'create_order', 'update_order', 'delete_order', 'update_order_status', 'create_products', 'update_products', 'delete_products', 'create_production_plan', 'update_production_plan', 'delete_production_plan', 'update_production_plan_status', 'update_production_segment', 'update_production_record', 'create_alert_rule', 'update_alert_rule', 'delete_alert_rules', 'set_alert_config', 'set_things_alert_rules', 'sim_set_alert', 'sim_open_alert', 'sim_secret_load', 'create_file', 'create_files', 'create_image', 'create_images', 'create_market_file', 'create_market_files', 'update_notification_config', 'read_notification', 'read_all_notification', 'add_company_apps', 'delete_company_apps', 'visit_app', 'set_quick_access_app', 'create_system_issue', 'update_system_issue', 'create_education_issue', 'update_education_issue', 'create_help_issue', 'update_help_issue', 'create_market_issue', 'update_market_issue', 'create_company', 'update_company', 'delete_companies', 'update_my_company', 'create_department', 'update_department', 'delete_department', 'create_company_bidatasource', 'delete_company_bidatasource', 'set_workbench', 'create_market_solution', 'update_market_solution', 'publish_market_solution', 'delete_market_solution', 'create_role', 'update_role', 'delete_role', 'set_company_admin_permission', 'create_market_app', 'update_market_app', 'publish_market_app', 'delete_market_app', 'register_user', 'login', 'logout', 'create_company_admin_user', 'update_company_admin_user', 'delete_company_admin_users', 'create_user', 'update_user', 'import_user', 'delete_users', 'update_me', 'update_my_password', 'reset_password', 'restore_user', 'activate_user', 'forbidden_user')
    create_bifile = sgqlc.types.Field(sgqlc.types.non_null(File), graphql_name='createBIFile', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateBIFileInput), graphql_name='input', default=None)),
))
    )
    create_bifiles = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(File)), graphql_name='createBIFiles', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(CreateBIFileInput)), graphql_name='input', default=None)),
))
    )
    create_bicategory = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='createBICategory', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='input', default=None)),
))
    )
    create_bidashboard = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='createBIDashboard', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateBIDashboardInput), graphql_name='input', default=None)),
))
    )
    update_bidashboard = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateBIDashboard', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateBIDashboardInput), graphql_name='input', default=None)),
))
    )
    publish_bidashboard = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='publishBIDashboard', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(PublishBIDashboardInput), graphql_name='input', default=None)),
))
    )
    unpublish_bidashboard = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='unpublishBIDashboard', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    delete_bidashboard = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteBIDashboard', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    copy_bidashboard = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='copyBIDashboard', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    create_bidatabase = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='createBIDatabase', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateBIDatabaseInput), graphql_name='input', default=None)),
))
    )
    update_bidatabase = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateBIDatabase', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateBIDatabaseInput), graphql_name='input', default=None)),
))
    )
    delete_bidatabase = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteBIDatabase', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='id', default=None)),
))
    )
    delete_bifile_data_source = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteBIFileDataSource', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='id', default=None)),
))
    )
    create_bidataset = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='createBIDataset', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CreateBIDatasetInput))), graphql_name='input', default=None)),
))
    )
    delete_bidataset = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteBIDataset', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='id', default=None)),
))
    )
    refresh_bidataset = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='refreshBIDataset', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    create_train_school_recruit_task = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='createTrainSchoolRecruitTask', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(CreateTrainSchoolRecruitTaskInput, graphql_name='input', default=None)),
))
    )
    update_train_school_recruit_task = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateTrainSchoolRecruitTask', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(UpdateTrainSchoolRecruitTaskInput, graphql_name='input', default=None)),
))
    )
    sign_train_school_recruit_task = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='signTrainSchoolRecruitTask', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.list_of(IDInput), graphql_name='input', default=None)),
))
    )
    review_train_school_recruit_task = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='reviewTrainSchoolRecruitTask', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ReviewTrainSchoolRecruitTaskInput), graphql_name='input', default=None)),
))
    )
    close_train_school_recruit_task = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='closeTrainSchoolRecruitTask', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    create_chan_jiao_file = sgqlc.types.Field(File, graphql_name='createChanJiaoFile', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateChanJiaoFileInput), graphql_name='input', default=None)),
))
    )
    create_chan_jiao_files = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(File)), graphql_name='createChanJiaoFiles', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(CreateChanJiaoFileInput)), graphql_name='input', default=None)),
))
    )
    create_social_person = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='createSocialPerson', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(CreateSocialPersonInput, graphql_name='input', default=None)),
))
    )
    update_social_person = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateSocialPerson', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(UpdateSocialPersonInput, graphql_name='input', default=None)),
))
    )
    review_social_person = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='reviewSocialPerson', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ReviewSocialPersonInput), graphql_name='input', default=None)),
))
    )
    create_recruit_job = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='createRecruitJob', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateRecruitJobInput), graphql_name='input', default=None)),
))
    )
    update_recruit_job = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateRecruitJob', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateRecruitJobInput), graphql_name='input', default=None)),
))
    )
    audit_recruit_job = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='auditRecruitJob', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(AuditRecruitJobInput), graphql_name='input', default=None)),
))
    )
    delete_recruit_job = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteRecruitJob', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    sign_recruit_job = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='signRecruitJob', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    audit_recruit_job_sign_record = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='auditRecruitJobSignRecord', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(AuditRecruitJobSignRecordInput), graphql_name='input', default=None)),
))
    )
    set_company_recruit_brief = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='setCompanyRecruitBrief', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(SetCompanyRecruitBriefInput, graphql_name='input', default=None)),
))
    )
    create_recruit_student = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='createRecruitStudent', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(CreateRecruitStudentInput, graphql_name='input', default=None)),
))
    )
    update_recruit_student = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateRecruitStudent', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(UpdateRecruitStudentInput, graphql_name='input', default=None)),
))
    )
    sign_train_course = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='signTrainCourse', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    create_train_course = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='createTrainCourse', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateTrainCourseInput), graphql_name='input', default=None)),
))
    )
    update_train_course = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateTrainCourse', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateTrainCourseInput), graphql_name='input', default=None)),
))
    )
    review_sign_up_train_course = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='reviewSignUpTrainCourse', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ReviewSignUpTrainCourseInput), graphql_name='input', default=None)),
))
    )
    review_authenticate_train_course = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='reviewAuthenticateTrainCourse', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ReviewAuthenticateTrainCourseInput), graphql_name='input', default=None)),
))
    )
    close_train_course = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='closeTrainCourse', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    restart_train_course = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='restartTrainCourse', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(RestartTrainCourseInput), graphql_name='input', default=None)),
))
    )
    import_authentication = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='importAuthentication', args=sgqlc.types.ArgDict((
        ('file', sgqlc.types.Arg(sgqlc.types.non_null(CreateChanJiaoFileInput), graphql_name='file', default=None)),
))
    )
    create_train_school_student = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='createTrainSchoolStudent', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(CreateTrainSchoolStudentInput, graphql_name='input', default=None)),
))
    )
    update_train_school_student = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateTrainSchoolStudent', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(UpdateTrainSchoolStudentInput, graphql_name='input', default=None)),
))
    )
    delete_train_school_student = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteTrainSchoolStudent', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.list_of(ID), graphql_name='id', default=None)),
))
    )
    import_student_info = sgqlc.types.Field(sgqlc.types.non_null(ImportStudentResult), graphql_name='importStudentInfo', args=sgqlc.types.ArgDict((
        ('file', sgqlc.types.Arg(sgqlc.types.non_null(CreateChanJiaoFileInput), graphql_name='file', default=None)),
))
    )
    create_train_work_type = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='createTrainWorkType', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateWorkTypeInput), graphql_name='input', default=None)),
))
    )
    update_train_work_type = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateTrainWorkType', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateWorkTypeInput), graphql_name='input', default=None)),
))
    )
    delete_train_work_type = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteTrainWorkType', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    set_train_work_level = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='setTrainWorkLevel', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SetTrainWorkLevelInput), graphql_name='input', default=None)),
))
    )
    create_train_faculty = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='createTrainFaculty', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateTrainFacultyInput), graphql_name='input', default=None)),
))
    )
    update_train_faculty = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateTrainFaculty', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateTrainFacultyInput), graphql_name='input', default=None)),
))
    )
    delete_train_faculty = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteTrainFaculty', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    create_train_class = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='createTrainClass', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateTrainClassInput), graphql_name='input', default=None)),
))
    )
    update_train_class = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateTrainClass', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateTrainClassInput), graphql_name='input', default=None)),
))
    )
    delete_train_class = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteTrainClass', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    create_company_demand = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='createCompanyDemand', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateCompanyDemandInput), graphql_name='input', default=None)),
))
    )
    update_company_demand = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateCompanyDemand', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateCompanyDemandInput), graphql_name='input', default=None)),
))
    )
    review_company_demand = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='reviewCompanyDemand', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ReviewCompanyDemandInput), graphql_name='input', default=None)),
))
    )
    create_report = sgqlc.types.Field('RawData', graphql_name='createReport', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateReportInput), graphql_name='input', default=None)),
))
    )
    update_report = sgqlc.types.Field('RawData', graphql_name='updateReport', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateReportInput), graphql_name='input', default=None)),
))
    )
    notify_energy_consumption = sgqlc.types.Field(Boolean, graphql_name='notifyEnergyConsumption', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(IDInput))), graphql_name='ids', default=None)),
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('granularity', sgqlc.types.Arg(sgqlc.types.non_null(Granularity), graphql_name='granularity', default=None)),
        ('county', sgqlc.types.Arg(String, graphql_name='county', default=None)),
))
    )
    create_cockpit_target = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='createCockpitTarget', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CreateCockpitTargetInput))), graphql_name='input', default=None)),
))
    )
    update_cockpit_target = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateCockpitTarget', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateCockpitTargetInput), graphql_name='input', default=None)),
))
    )
    delete_cockpit_target = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteCockpitTarget', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='id', default=None)),
))
    )
    create_thing_input_record = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='createThingInputRecord', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateThingInputRecordInput), graphql_name='input', default=None)),
))
    )
    update_thing_input_record = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateThingInputRecord', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateThingInputRecordInput), graphql_name='input', default=None)),
))
    )
    delete_thing_input_record = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteThingInputRecord', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='id', default=None)),
))
    )
    create_eam_file = sgqlc.types.Field(sgqlc.types.non_null(File), graphql_name='createEamFile', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(CreateEamFileInput, graphql_name='input', default=None)),
))
    )
    create_eam_files = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(File)), graphql_name='createEamFiles', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CreateEamFileInput))), graphql_name='input', default=None)),
))
    )
    create_thing_inspection = sgqlc.types.Field(sgqlc.types.non_null('ThingInspection'), graphql_name='createThingInspection', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateThingInspectionInput), graphql_name='input', default=None)),
))
    )
    update_thing_inspection = sgqlc.types.Field(sgqlc.types.non_null('ThingInspection'), graphql_name='updateThingInspection', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateThingInspectionInput), graphql_name='input', default=None)),
))
    )
    update_thing_inspection_status = sgqlc.types.Field(sgqlc.types.non_null('ThingInspection'), graphql_name='updateThingInspectionStatus', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateThingInspectionStatusInput), graphql_name='input', default=None)),
))
    )
    update_thing_inspection_feedback = sgqlc.types.Field(sgqlc.types.non_null('ThingInspection'), graphql_name='updateThingInspectionFeedback', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateThingInspectionFeedbackInput), graphql_name='input', default=None)),
))
    )
    delete_thing_inspections = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(ID)), graphql_name='deleteThingInspections', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteThingInspectionsInput), graphql_name='input', default=None)),
))
    )
    create_thing_inspection_rule = sgqlc.types.Field(sgqlc.types.non_null('ThingInspectionRule'), graphql_name='createThingInspectionRule', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateThingInspectionRuleInput), graphql_name='input', default=None)),
))
    )
    update_thing_inspection_rule = sgqlc.types.Field(sgqlc.types.non_null('ThingInspectionRule'), graphql_name='updateThingInspectionRule', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateThingInspectionRuleInput), graphql_name='input', default=None)),
))
    )
    delete_inspection_rules = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(ID)), graphql_name='deleteInspectionRules', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteThingInspectionRulesInput), graphql_name='input', default=None)),
))
    )
    create_spare_part_receipt = sgqlc.types.Field(sgqlc.types.non_null('SparePartReceipt'), graphql_name='createSparePartReceipt', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateSparePartReceiptInput), graphql_name='input', default=None)),
))
    )
    update_spare_part_receipt = sgqlc.types.Field(sgqlc.types.non_null('SparePartReceipt'), graphql_name='updateSparePartReceipt', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateSparePartReceiptInput), graphql_name='input', default=None)),
))
    )
    delete_spare_part_receipts = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='deleteSparePartReceipts', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteSparePartReceiptInput), graphql_name='input', default=None)),
))
    )
    create_thing_maintenance_rule = sgqlc.types.Field(sgqlc.types.non_null('ThingMaintenanceRule'), graphql_name='createThingMaintenanceRule', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateThingMaintenanceRuleInput), graphql_name='input', default=None)),
))
    )
    update_thing_maintenance_rule = sgqlc.types.Field(sgqlc.types.non_null('ThingMaintenanceRule'), graphql_name='updateThingMaintenanceRule', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateThingMaintenanceRuleInput), graphql_name='input', default=None)),
))
    )
    delete_thing_maintenance_rules = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(ID)), graphql_name='deleteThingMaintenanceRules', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteThingMaintenanceRulesInput), graphql_name='input', default=None)),
))
    )
    create_thing_maintenance = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='createThingMaintenance', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateThingMaintenanceInput), graphql_name='input', default=None)),
))
    )
    update_thing_maintenance = sgqlc.types.Field(sgqlc.types.non_null('ThingMaintenance'), graphql_name='updateThingMaintenance', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateThingMaintenanceInput), graphql_name='input', default=None)),
))
    )
    update_thing_maintenance_feedback = sgqlc.types.Field(sgqlc.types.non_null('ThingMaintenance'), graphql_name='updateThingMaintenanceFeedback', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateThingMaintenanceFeedbackInput), graphql_name='input', default=None)),
))
    )
    update_thing_maintenance_status = sgqlc.types.Field(sgqlc.types.non_null('ThingMaintenance'), graphql_name='updateThingMaintenanceStatus', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateThingMaintenanceStatusInput), graphql_name='input', default=None)),
))
    )
    delete_thing_maintenances = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(ID)), graphql_name='deleteThingMaintenances', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteThingMaintenancesInput), graphql_name='input', default=None)),
))
    )
    create_thing = sgqlc.types.Field(sgqlc.types.non_null('Thing'), graphql_name='createThing', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateThingInput), graphql_name='input', default=None)),
))
    )
    update_thing = sgqlc.types.Field(sgqlc.types.non_null('Thing'), graphql_name='updateThing', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateThingInput), graphql_name='input', default=None)),
))
    )
    delete_things = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='deleteThings', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteThingsInput), graphql_name='input', default=None)),
))
    )
    import_things = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='importThings', args=sgqlc.types.ArgDict((
        ('file', sgqlc.types.Arg(sgqlc.types.non_null(CreateEamFileInput), graphql_name='file', default=None)),
))
    )
    create_thing_group = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='createThingGroup', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateThingGroupInput), graphql_name='input', default=None)),
))
    )
    update_thing_group = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateThingGroup', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateThingGroupInput), graphql_name='input', default=None)),
))
    )
    delete_thing_group = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteThingGroup', args=sgqlc.types.ArgDict((
        ('thing_group', sgqlc.types.Arg(sgqlc.types.non_null(IDInput), graphql_name='thingGroup', default=None)),
))
    )
    set_users_thing_group = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='setUsersThingGroup', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SetUserThingGroupInput), graphql_name='input', default=None)),
))
    )
    set_departments_thing_group = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='setDepartmentsThingGroup', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SetDepartmentThingGroupInput), graphql_name='input', default=None)),
))
    )
    set_single_user_thing_groups = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='setSingleUserThingGroups', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SetSingleUserThingGroupsInput), graphql_name='input', default=None)),
))
    )
    set_single_department_thing_groups = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='setSingleDepartmentThingGroups', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(SetSingleDepartmentThingGroups, graphql_name='input', default=None)),
))
    )
    update_department_thing_group = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateDepartmentThingGroup', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateDepartmentThingGroupInput), graphql_name='input', default=None)),
))
    )
    update_user_thing_group = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateUserThingGroup', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateUserThingGroupInput), graphql_name='input', default=None)),
))
    )
    move_things = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='moveThings', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(MoveThingInput, graphql_name='input', default=None)),
))
    )
    delete_user_thing_groups = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteUserThingGroups', args=sgqlc.types.ArgDict((
        ('thing_groups', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='thingGroups', default=None)),
))
    )
    delete_department_thing_groups = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteDepartmentThingGroups', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteDepartmentThingGroupInput), graphql_name='input', default=None)),
))
    )
    update_form_struct = sgqlc.types.Field(sgqlc.types.non_null(FormStruct), graphql_name='updateFormStruct', args=sgqlc.types.ArgDict((
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
        ('custom_fields', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(FieldMetaInput))), graphql_name='customFields', default=None)),
        ('is_publish', sgqlc.types.Arg(sgqlc.types.non_null(Boolean), graphql_name='isPublish', default=None)),
))
    )
    create_spare_part = sgqlc.types.Field(sgqlc.types.non_null('SparePart'), graphql_name='createSparePart', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateSparePartInput), graphql_name='input', default=None)),
))
    )
    update_spare_part = sgqlc.types.Field(sgqlc.types.non_null('SparePart'), graphql_name='updateSparePart', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateSparePartInput), graphql_name='input', default=None)),
))
    )
    delete_spare_parts = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='deleteSpareParts', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteSparePartsInput), graphql_name='input', default=None)),
))
    )
    import_spare_parts = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='importSpareParts', args=sgqlc.types.ArgDict((
        ('file', sgqlc.types.Arg(sgqlc.types.non_null(CreateEamFileInput), graphql_name='file', default=None)),
))
    )
    create_thing_repair = sgqlc.types.Field(sgqlc.types.non_null('ThingRepair'), graphql_name='createThingRepair', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateThingRepairInput), graphql_name='input', default=None)),
))
    )
    create_thing_repairs = sgqlc.types.Field(sgqlc.types.non_null('ThingRepairList'), graphql_name='createThingRepairs', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(CreateThingRepairInput)), graphql_name='input', default=None)),
))
    )
    update_thing_repair = sgqlc.types.Field(sgqlc.types.non_null('ThingRepair'), graphql_name='updateThingRepair', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateThingRepairInput), graphql_name='input', default=None)),
))
    )
    update_thing_repair_feedback = sgqlc.types.Field(sgqlc.types.non_null('ThingRepair'), graphql_name='updateThingRepairFeedback', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateThingRepairFeedbackInput), graphql_name='input', default=None)),
))
    )
    audit_thing_repair = sgqlc.types.Field(sgqlc.types.non_null('ThingRepair'), graphql_name='auditThingRepair', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(AuditThingRepairInput), graphql_name='input', default=None)),
))
    )
    delete_thing_repairs = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='deleteThingRepairs', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteThingRepairsInput), graphql_name='input', default=None)),
))
    )
    create_spare_part_outbound = sgqlc.types.Field(sgqlc.types.non_null('SparePartOutbound'), graphql_name='createSparePartOutbound', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateSparePartOutboundInput), graphql_name='input', default=None)),
))
    )
    update_spare_part_outbound = sgqlc.types.Field(sgqlc.types.non_null('SparePartOutbound'), graphql_name='updateSparePartOutbound', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateSparePartOutboundInput), graphql_name='input', default=None)),
))
    )
    audit_spare_part_outbound = sgqlc.types.Field(sgqlc.types.non_null('SparePartOutbound'), graphql_name='auditSparePartOutbound', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(AuditSparePartOutboundInput), graphql_name='input', default=None)),
))
    )
    delete_spare_part_outbounds = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='deleteSparePartOutbounds', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteSparePartOutboundsInput), graphql_name='input', default=None)),
))
    )
    create_edm_file = sgqlc.types.Field(sgqlc.types.non_null(File), graphql_name='createEdmFile', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateFileInput), graphql_name='input', default=None)),
))
    )
    create_edm_files = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(File))), graphql_name='createEdmFiles', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CreateFileInput))), graphql_name='input', default=None)),
))
    )
    create_router_template_configuration = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='createRouterTemplateConfiguration', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateRouterTemplateConfigurationInput), graphql_name='input', default=None)),
))
    )
    update_router_template_configuration = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateRouterTemplateConfiguration', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateRouterTemplateConfigurationInput), graphql_name='input', default=None)),
))
    )
    delete_router_template_configuration = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteRouterTemplateConfiguration', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='id', default=None)),
))
    )
    create_device_channel_configuration = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='createDeviceChannelConfiguration', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateDeviceChannelConfigurationInput), graphql_name='input', default=None)),
))
    )
    update_device_channel_configuration = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateDeviceChannelConfiguration', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateDeviceChannelConfigurationInput), graphql_name='input', default=None)),
))
    )
    delete_device_channel_configuration = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteDeviceChannelConfiguration', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='id', default=None)),
))
    )
    apply_router_template_configuration = sgqlc.types.Field(sgqlc.types.non_null(ApplyRouterTemplateConfigurationResult), graphql_name='applyRouterTemplateConfiguration', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ApplyRouterTemplateConfigurationInput), graphql_name='input', default=None)),
))
    )
    create_router = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='createRouter', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateRouterInput), graphql_name='input', default=None)),
))
    )
    update_router = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateRouter', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateRouterInput), graphql_name='input', default=None)),
))
    )
    delete_router = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteRouter', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='id', default=None)),
))
    )
    import_router = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='importRouter', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ImportFileInput), graphql_name='input', default=None)),
))
    )
    update_routers_alarm_rules = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateRoutersAlarmRules', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(UpdateRoutersAlarmRulesInput, graphql_name='input', default=None)),
))
    )
    update_router_alarm_records = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateRouterAlarmRecords', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(UpdateRouterAlarmRecordsInput, graphql_name='input', default=None)),
))
    )
    create_fault_file = sgqlc.types.Field(sgqlc.types.non_null(File), graphql_name='createFaultFile', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateFaultFileInput), graphql_name='input', default=None)),
))
    )
    create_fault_files = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(File)), graphql_name='createFaultFiles', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(CreateFaultFileInput)), graphql_name='input', default=None)),
))
    )
    create_fault_reason = sgqlc.types.Field(sgqlc.types.non_null(FaultReason), graphql_name='createFaultReason', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateFaultReasonInput), graphql_name='input', default=None)),
))
    )
    update_fault_issue = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateFaultIssue', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateFaultIssueInput), graphql_name='input', default=None)),
))
    )
    create_fault_solution = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='createFaultSolution', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateFaultSolutionInput), graphql_name='input', default=None)),
))
    )
    update_fault_solution = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateFaultSolution', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(UpdateFaultSolutionInput, graphql_name='input', default=None)),
))
    )
    delete_fault_solution = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteFaultSolution', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='id', default=None)),
))
    )
    create_fault_rule = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='createFaultRule', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateFaultRuleInput), graphql_name='input', default=None)),
))
    )
    update_fault_rule = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateFaultRule', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateFaultRuleInput), graphql_name='input', default=None)),
))
    )
    delete_fault_rule = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteFaultRule', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(IDInput))), graphql_name='ids', default=None)),
))
    )
    create_directory = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='createDirectory', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateDirectoryInput), graphql_name='input', default=None)),
))
    )
    update_directory = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateDirectory', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateDirectoryInput), graphql_name='input', default=None)),
))
    )
    delete_directory = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteDirectory', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='id', default=None)),
))
    )
    move_fault_solution = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='moveFaultSolution', args=sgqlc.types.ArgDict((
        ('directory', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='directory', default=None)),
        ('fault_solution', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='faultSolution', default=None)),
))
    )
    create_production_ticket_file = sgqlc.types.Field(sgqlc.types.non_null(File), graphql_name='createProductionTicketFile', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateProductionTicketFileInput), graphql_name='input', default=None)),
))
    )
    create_production_team = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='createProductionTeam', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateProductionTeamInput), graphql_name='input', default=None)),
))
    )
    create_production_team_plus = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='createProductionTeamPlus', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateProductionTeamPlusInput), graphql_name='input', default=None)),
))
    )
    update_production_team = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateProductionTeam', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateProductionTeamInput), graphql_name='input', default=None)),
))
    )
    delete_production_team = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteProductionTeam', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='id', default=None)),
))
    )
    create_production_teammate = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='createProductionTeammate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateProductionTeammateInput), graphql_name='input', default=None)),
))
    )
    update_production_teammate = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateProductionTeammate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateProductionTeammateInput), graphql_name='input', default=None)),
))
    )
    delete_production_teammate = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteProductionTeammate', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='id', default=None)),
))
    )
    upload_production_teammate = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='uploadProductionTeammate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UploadProductionTeammateInput), graphql_name='input', default=None)),
))
    )
    update_production_schedule = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateProductionSchedule', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateProductionScheduleInput), graphql_name='input', default=None)),
))
    )
    delete_production_schedule = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteProductionSchedule', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    start_production_sub_schedule = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='startProductionSubSchedule', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    update_production_sub_schedule = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateProductionSubSchedule', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateProductionSubScheduleInput), graphql_name='input', default=None)),
))
    )
    assign_production_sub_schedule = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='assignProductionSubSchedule', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(AssignProductionSubScheduleInput), graphql_name='input', default=None)),
))
    )
    assign_production_ticket = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='assignProductionTicket', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(AssignProductionTicketInput), graphql_name='input', default=None)),
))
    )
    create_production_ticket = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='createProductionTicket', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateProductionTicketInput), graphql_name='input', default=None)),
))
    )
    update_production_ticket = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateProductionTicket', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateProductionTicketInput), graphql_name='input', default=None)),
))
    )
    delete_production_ticket = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteProductionTicket', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    start_production = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='startProduction', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(StartProductionInput), graphql_name='input', default=None)),
))
    )
    end_production = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='endProduction', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    _junye_dummy = sgqlc.types.Field(Boolean, graphql_name='_junyeDummy')
    junye_flush_metric = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='junyeFlushMetric')
    create_thing_type = sgqlc.types.Field('ThingType', graphql_name='createThingType', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateThingTypeInput), graphql_name='input', default=None)),
))
    )
    update_thing_type = sgqlc.types.Field(Boolean, graphql_name='updateThingType', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateThingTypeInput), graphql_name='input', default=None)),
))
    )
    delete_thing_types = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='deleteThingTypes', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteInput), graphql_name='input', default=None)),
))
    )
    create_source_key = sgqlc.types.Field('SourceKey', graphql_name='createSourceKey', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateSourceKeyInput), graphql_name='input', default=None)),
))
    )
    update_source_key = sgqlc.types.Field(Boolean, graphql_name='updateSourceKey', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateSourceKeyInput), graphql_name='input', default=None)),
))
    )
    delete_source_keys = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='deleteSourceKeys', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteInput), graphql_name='input', default=None)),
))
    )
    create_adapter_key = sgqlc.types.Field(AdapterKey, graphql_name='createAdapterKey', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateAdapterKeyInput), graphql_name='input', default=None)),
))
    )
    debug_adapter_key = sgqlc.types.Field(JSON, graphql_name='debugAdapterKey', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DebugAdapterKeyInput), graphql_name='input', default=None)),
))
    )
    update_adapter_key = sgqlc.types.Field(Boolean, graphql_name='updateAdapterKey', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateAdapterKeyInput), graphql_name='input', default=None)),
))
    )
    delete_adapter_keys = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='deleteAdapterKeys', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteInput), graphql_name='input', default=None)),
))
    )
    create_cockpit_key = sgqlc.types.Field(CockpitKey, graphql_name='createCockpitKey', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateCockpitKey), graphql_name='input', default=None)),
))
    )
    update_cockpit_key = sgqlc.types.Field(Boolean, graphql_name='updateCockpitKey', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateCockpitKey), graphql_name='input', default=None)),
))
    )
    delete_cockpit_keys = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='deleteCockpitKeys', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteInput), graphql_name='input', default=None)),
))
    )
    create_cockpit_aggregation = sgqlc.types.Field(CockpitAggregation, graphql_name='createCockpitAggregation', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateCockpitAggregation), graphql_name='input', default=None)),
))
    )
    update_cockpit_aggregation = sgqlc.types.Field(Boolean, graphql_name='updateCockpitAggregation', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateCockpitAggregation), graphql_name='input', default=None)),
))
    )
    delete_cockpit_aggregations = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='deleteCockpitAggregations', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteInput), graphql_name='input', default=None)),
))
    )
    create_thing_status = sgqlc.types.Field('ThingStatus', graphql_name='createThingStatus', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateThingStatus), graphql_name='input', default=None)),
))
    )
    update_thing_status = sgqlc.types.Field(Boolean, graphql_name='updateThingStatus', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateThingStatus), graphql_name='input', default=None)),
))
    )
    delete_thing_statuses = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='deleteThingStatuses', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteInput), graphql_name='input', default=None)),
))
    )
    create_energy_group = sgqlc.types.Field(EnergyGroup, graphql_name='createEnergyGroup', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateEnergyGroup), graphql_name='input', default=None)),
))
    )
    update_energy_group = sgqlc.types.Field(Boolean, graphql_name='updateEnergyGroup', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateEnergyGroup), graphql_name='input', default=None)),
))
    )
    delete_energy_groups = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='deleteEnergyGroups', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteInput), graphql_name='input', default=None)),
))
    )
    update_energy_time_distribution = sgqlc.types.Field(EnergyTimeDistribution, graphql_name='updateEnergyTimeDistribution', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateEnergyTimeDistribution), graphql_name='input', default=None)),
))
    )
    create_thing_organization = sgqlc.types.Field('ThingOrganization', graphql_name='createThingOrganization', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateThingOrganization), graphql_name='input', default=None)),
))
    )
    update_thing_organization = sgqlc.types.Field(Boolean, graphql_name='updateThingOrganization', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateThingOrganization), graphql_name='input', default=None)),
))
    )
    delete_thing_organizations = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='deleteThingOrganizations', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteInput), graphql_name='input', default=None)),
))
    )
    create_worker = sgqlc.types.Field(sgqlc.types.non_null('Worker'), graphql_name='createWorker', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateWorkerInput), graphql_name='input', default=None)),
))
    )
    update_worker = sgqlc.types.Field(sgqlc.types.non_null('Worker'), graphql_name='updateWorker', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateWorkerInput), graphql_name='input', default=None)),
))
    )
    delete_workers = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteWorkers', args=sgqlc.types.ArgDict((
        ('workers', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(IDInput))), graphql_name='workers', default=None)),
))
    )
    create_work_group = sgqlc.types.Field(sgqlc.types.non_null('WorkGroup'), graphql_name='createWorkGroup', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateWorkGroupInput), graphql_name='input', default=None)),
))
    )
    update_work_group = sgqlc.types.Field(sgqlc.types.non_null('WorkGroup'), graphql_name='updateWorkGroup', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateWorkGroupInput), graphql_name='input', default=None)),
))
    )
    delete_work_groups = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteWorkGroups', args=sgqlc.types.ArgDict((
        ('groups', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(IDInput))), graphql_name='groups', default=None)),
))
    )
    create_work_shift = sgqlc.types.Field(sgqlc.types.non_null('WorkShift'), graphql_name='createWorkShift', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateWorkShiftInput), graphql_name='input', default=None)),
))
    )
    update_work_shift = sgqlc.types.Field(sgqlc.types.non_null('WorkShift'), graphql_name='updateWorkShift', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateWorkShiftInput), graphql_name='input', default=None)),
))
    )
    delete_work_shifts = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteWorkShifts', args=sgqlc.types.ArgDict((
        ('shifts', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(IDInput))), graphql_name='shifts', default=None)),
))
    )
    create_material = sgqlc.types.Field(sgqlc.types.non_null(Material), graphql_name='createMaterial', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateMaterialInput), graphql_name='input', default=None)),
))
    )
    update_material = sgqlc.types.Field(sgqlc.types.non_null(Material), graphql_name='updateMaterial', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateMaterialInput), graphql_name='input', default=None)),
))
    )
    delete_material = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteMaterial', args=sgqlc.types.ArgDict((
        ('material', sgqlc.types.Arg(sgqlc.types.non_null(IDInput), graphql_name='material', default=None)),
))
    )
    create_procedure = sgqlc.types.Field(sgqlc.types.non_null('Procedure'), graphql_name='createProcedure', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateProcedureInput), graphql_name='input', default=None)),
))
    )
    update_procedure = sgqlc.types.Field(sgqlc.types.non_null('Procedure'), graphql_name='updateProcedure', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateProcedureInput), graphql_name='input', default=None)),
))
    )
    delete_procedures = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteProcedures', args=sgqlc.types.ArgDict((
        ('procedures', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(IDInput))), graphql_name='procedures', default=None)),
))
    )
    create_procedure_segment = sgqlc.types.Field(sgqlc.types.non_null('ProcedureSegment'), graphql_name='createProcedureSegment', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateProcedureSegmentInput), graphql_name='input', default=None)),
))
    )
    update_procedure_segment = sgqlc.types.Field(sgqlc.types.non_null('ProcedureSegment'), graphql_name='updateProcedureSegment', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateProcedureSegmentInput), graphql_name='input', default=None)),
))
    )
    delete_procedure_segments = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteProcedureSegments', args=sgqlc.types.ArgDict((
        ('segments', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(IDInput))), graphql_name='segments', default=None)),
))
    )
    set_work_duty = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='setWorkDuty', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SetWorkDutyInput), graphql_name='input', default=None)),
))
    )
    create_production_process = sgqlc.types.Field(sgqlc.types.non_null('ProductionProcess'), graphql_name='createProductionProcess', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateProductionProcessInput), graphql_name='input', default=None)),
))
    )
    update_production_process = sgqlc.types.Field(sgqlc.types.non_null('ProductionProcess'), graphql_name='updateProductionProcess', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateProductionProcessInput), graphql_name='input', default=None)),
))
    )
    delete_production_processes = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteProductionProcesses', args=sgqlc.types.ArgDict((
        ('processes', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(IDInput))), graphql_name='processes', default=None)),
))
    )
    create_order = sgqlc.types.Field('Order', graphql_name='createOrder', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateOrderInput), graphql_name='input', default=None)),
))
    )
    update_order = sgqlc.types.Field('Order', graphql_name='updateOrder', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateOrderInput), graphql_name='input', default=None)),
))
    )
    delete_order = sgqlc.types.Field(Boolean, graphql_name='deleteOrder', args=sgqlc.types.ArgDict((
        ('order', sgqlc.types.Arg(sgqlc.types.non_null(IDInput), graphql_name='order', default=None)),
))
    )
    update_order_status = sgqlc.types.Field('Order', graphql_name='updateOrderStatus', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateOrderStatusInput), graphql_name='input', default=None)),
))
    )
    create_products = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Product'))), graphql_name='createProducts', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateProductsInput), graphql_name='input', default=None)),
))
    )
    update_products = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Product'))), graphql_name='updateProducts', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateProductsInput), graphql_name='input', default=None)),
))
    )
    delete_products = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteProducts', args=sgqlc.types.ArgDict((
        ('products', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(IDInput))), graphql_name='products', default=None)),
))
    )
    create_production_plan = sgqlc.types.Field(sgqlc.types.non_null('ProductionPlan'), graphql_name='createProductionPlan', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(CreateProductionPlanInput, graphql_name='input', default=None)),
))
    )
    update_production_plan = sgqlc.types.Field(sgqlc.types.non_null('ProductionPlan'), graphql_name='updateProductionPlan', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(UpdateProductionPlanInput, graphql_name='input', default=None)),
))
    )
    delete_production_plan = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteProductionPlan', args=sgqlc.types.ArgDict((
        ('plan', sgqlc.types.Arg(sgqlc.types.non_null(IDInput), graphql_name='plan', default=None)),
))
    )
    update_production_plan_status = sgqlc.types.Field('ProductionPlan', graphql_name='updateProductionPlanStatus', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateProductionPlanStatusInput), graphql_name='input', default=None)),
))
    )
    update_production_segment = sgqlc.types.Field(sgqlc.types.non_null('ProductionSegment'), graphql_name='updateProductionSegment', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(UpdateProductionSegmentInput, graphql_name='input', default=None)),
))
    )
    update_production_record = sgqlc.types.Field(sgqlc.types.non_null('ProductionRecord'), graphql_name='updateProductionRecord', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(UpdateProductionRecordInput, graphql_name='input', default=None)),
))
    )
    create_alert_rule = sgqlc.types.Field(sgqlc.types.non_null(AlertRule), graphql_name='createAlertRule', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateAlertRuleInput), graphql_name='input', default=None)),
))
    )
    update_alert_rule = sgqlc.types.Field(sgqlc.types.non_null(AlertRule), graphql_name='updateAlertRule', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateAlertRuleInput), graphql_name='input', default=None)),
))
    )
    delete_alert_rules = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteAlertRules', args=sgqlc.types.ArgDict((
        ('rules', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(IDInput))), graphql_name='rules', default=None)),
))
    )
    set_alert_config = sgqlc.types.Field(sgqlc.types.non_null(AlertConfig), graphql_name='setAlertConfig', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SetAlertConfigInput), graphql_name='input', default=None)),
))
    )
    set_things_alert_rules = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='setThingsAlertRules', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SetThingsAlertRulesInput), graphql_name='input', default=None)),
))
    )
    sim_set_alert = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='simSetAlert', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.list_of(SetAlertInput), graphql_name='input', default=None)),
))
    )
    sim_open_alert = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='simOpenAlert', args=sgqlc.types.ArgDict((
        ('open', sgqlc.types.Arg(sgqlc.types.non_null(Boolean), graphql_name='open', default=None)),
))
    )
    sim_secret_load = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='simSecretLoad')
    create_file = sgqlc.types.Field(File, graphql_name='createFile', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateFileInput), graphql_name='input', default=None)),
))
    )
    create_files = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(File)), graphql_name='createFiles', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(CreateFileInput)), graphql_name='input', default=None)),
))
    )
    create_image = sgqlc.types.Field(Image, graphql_name='createImage', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateImageInput), graphql_name='input', default=None)),
))
    )
    create_images = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Image)), graphql_name='createImages', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(CreateImageInput)), graphql_name='input', default=None)),
))
    )
    create_market_file = sgqlc.types.Field(sgqlc.types.non_null(File), graphql_name='createMarketFile', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateMarketFileInput), graphql_name='input', default=None)),
))
    )
    create_market_files = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(File)), graphql_name='createMarketFiles', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(CreateMarketFileInput)), graphql_name='input', default=None)),
))
    )
    update_notification_config = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateNotificationConfig', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(UpdateNotificationConfigInput))), graphql_name='input', default=None)),
))
    )
    read_notification = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='readNotification', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='id', default=None)),
))
    )
    read_all_notification = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='readAllNotification', args=sgqlc.types.ArgDict((
        ('source_app', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='sourceApp', default=None)),
))
    )
    add_company_apps = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='addCompanyApps', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(AddCompanyAppsInput), graphql_name='input', default=None)),
))
    )
    delete_company_apps = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteCompanyApps', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteCompanyAppsInput), graphql_name='input', default=None)),
))
    )
    visit_app = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='visitApp', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    set_quick_access_app = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='setQuickAccessApp', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='id', default=None)),
))
    )
    create_system_issue = sgqlc.types.Field(sgqlc.types.non_null(Issue), graphql_name='createSystemIssue', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(CreateIssueInput, graphql_name='input', default=None)),
))
    )
    update_system_issue = sgqlc.types.Field(sgqlc.types.non_null(Issue), graphql_name='updateSystemIssue', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(UpdateIssueInput, graphql_name='input', default=None)),
))
    )
    create_education_issue = sgqlc.types.Field(sgqlc.types.non_null(Issue), graphql_name='createEducationIssue', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(CreateIssueInput, graphql_name='input', default=None)),
))
    )
    update_education_issue = sgqlc.types.Field(sgqlc.types.non_null(Issue), graphql_name='updateEducationIssue', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(UpdateIssueInput, graphql_name='input', default=None)),
))
    )
    create_help_issue = sgqlc.types.Field(sgqlc.types.non_null(Issue), graphql_name='createHelpIssue', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(CreateIssueInput, graphql_name='input', default=None)),
))
    )
    update_help_issue = sgqlc.types.Field(sgqlc.types.non_null(Issue), graphql_name='updateHelpIssue', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(UpdateIssueInput, graphql_name='input', default=None)),
))
    )
    create_market_issue = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='createMarketIssue', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateMarketIssueInput), graphql_name='input', default=None)),
))
    )
    update_market_issue = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateMarketIssue', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateMarketIssueInput), graphql_name='input', default=None)),
))
    )
    create_company = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='createCompany', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateCompanyInput), graphql_name='input', default=None)),
))
    )
    update_company = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateCompany', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateCompanyInput), graphql_name='input', default=None)),
        ('perm', sgqlc.types.Arg(String, graphql_name='perm', default=None)),
))
    )
    delete_companies = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteCompanies', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteCompaniesInput), graphql_name='input', default=None)),
))
    )
    update_my_company = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateMyCompany', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(UpdateMyCompanyInput, graphql_name='input', default=None)),
))
    )
    create_department = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='createDepartment', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(CreateDepartmentInput, graphql_name='input', default=None)),
))
    )
    update_department = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateDepartment', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(UpdateDepartmentInput, graphql_name='input', default=None)),
))
    )
    delete_department = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteDepartment', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    create_company_bidatasource = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='createCompanyBIDatasource', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateCompanyBIDatasourceInput), graphql_name='input', default=None)),
))
    )
    delete_company_bidatasource = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteCompanyBIDatasource', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='id', default=None)),
))
    )
    set_workbench = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='setWorkbench', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(WorkbenchCardInput))), graphql_name='input', default=None)),
))
    )
    create_market_solution = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='createMarketSolution', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateMarketSolutionInput), graphql_name='input', default=None)),
))
    )
    update_market_solution = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateMarketSolution', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateMarketSolutionInput), graphql_name='input', default=None)),
))
    )
    publish_market_solution = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='publishMarketSolution', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    delete_market_solution = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteMarketSolution', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='id', default=None)),
))
    )
    create_role = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='createRole', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateRoleInput), graphql_name='input', default=None)),
))
    )
    update_role = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateRole', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateRoleInput), graphql_name='input', default=None)),
))
    )
    delete_role = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteRole', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='id', default=None)),
))
    )
    set_company_admin_permission = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='setCompanyAdminPermission', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(CompanyAdminPermissionInput, graphql_name='input', default=None)),
))
    )
    create_market_app = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='createMarketApp', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateMarketAppInput), graphql_name='input', default=None)),
))
    )
    update_market_app = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateMarketApp', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateMarketAppInput), graphql_name='input', default=None)),
))
    )
    publish_market_app = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='publishMarketApp', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    delete_market_app = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteMarketApp', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='id', default=None)),
))
    )
    register_user = sgqlc.types.Field(sgqlc.types.non_null(AuthInfo), graphql_name='registerUser', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(RegisterUserInput, graphql_name='input', default=None)),
))
    )
    login = sgqlc.types.Field(sgqlc.types.non_null(AuthInfo), graphql_name='login', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(LoginInput), graphql_name='input', default=None)),
))
    )
    logout = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='logout')
    create_company_admin_user = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='createCompanyAdminUser', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(CreateCompanyAdminUserInput, graphql_name='input', default=None)),
))
    )
    update_company_admin_user = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateCompanyAdminUser', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(UpdateCompanyAdminUserInput, graphql_name='input', default=None)),
))
    )
    delete_company_admin_users = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteCompanyAdminUsers', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(DeleteCompanyAdminUsersInput, graphql_name='input', default=None)),
))
    )
    create_user = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='createUser', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateUserInput), graphql_name='input', default=None)),
))
    )
    update_user = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateUser', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateUserInput), graphql_name='input', default=None)),
))
    )
    import_user = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='importUser', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateFileInput), graphql_name='input', default=None)),
))
    )
    delete_users = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteUsers', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteUsersInput), graphql_name='input', default=None)),
))
    )
    update_me = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateMe', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateMeInput), graphql_name='input', default=None)),
))
    )
    update_my_password = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateMyPassword', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(UpdateMyPasswordInput, graphql_name='input', default=None)),
))
    )
    reset_password = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('User'))), graphql_name='resetPassword', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(ResetPasswordInput, graphql_name='input', default=None)),
        ('perm', sgqlc.types.Arg(String, graphql_name='perm', default=None)),
))
    )
    restore_user = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='restoreUser', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(RestoreUserInput), graphql_name='input', default=None)),
))
    )
    activate_user = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='activateUser', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ActivateUserInput), graphql_name='input', default=None)),
))
    )
    forbidden_user = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='forbiddenUser', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ForbiddenUserInput), graphql_name='input', default=None)),
))
    )


class MyRecruitSignStatus(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('job_id', 'sign_status')
    job_id = sgqlc.types.Field(ID, graphql_name='jobId')
    sign_status = sgqlc.types.Field(sgqlc.types.non_null(RecruitStudentStatus), graphql_name='signStatus')


class Notification(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'kind', 'source_app', 'content', 'created_at', 'is_read', 'url')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    kind = sgqlc.types.Field(sgqlc.types.non_null(NotificationKind), graphql_name='kind')
    source_app = sgqlc.types.Field(App, graphql_name='sourceApp')
    content = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='content')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='createdAt')
    is_read = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isRead')
    url = sgqlc.types.Field(String, graphql_name='url')


class NotificationConfig(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'source_app', 'description', 'to_inbox', 'to_email', 'receiver_user', 'receiver_role', 'template', 'kind')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    source_app = sgqlc.types.Field(App, graphql_name='sourceApp')
    description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='description')
    to_inbox = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='toInbox')
    to_email = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='toEmail')
    receiver_user = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('User'))), graphql_name='receiverUser')
    receiver_role = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Role'))), graphql_name='receiverRole')
    template = sgqlc.types.Field(sgqlc.types.non_null('NotificationTemplate'), graphql_name='template')
    kind = sgqlc.types.Field(sgqlc.types.non_null(NotificationKind), graphql_name='kind')


class NotificationConfigList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(NotificationConfig))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class NotificationList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count', 'read_count', 'unread_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Notification))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    read_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='readCount')
    unread_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='unreadCount')


class NotificationTemplate(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('inbox', 'email')
    inbox = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='inbox')
    email = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='email')


class NumberByOrganziation(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('organization', 'num')
    organization = sgqlc.types.Field('ThingOrganization', graphql_name='organization')
    num = sgqlc.types.Field(Int, graphql_name='num')


class NumberByThingType(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('type', 'num')
    type = sgqlc.types.Field('ThingType', graphql_name='type')
    num = sgqlc.types.Field(Int, graphql_name='num')


class Order(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'code', 'name', 'status', 'products', 'delivery_date', 'delivery_shift')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    status = sgqlc.types.Field(sgqlc.types.non_null(OrderStatus), graphql_name='status')
    products = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('Product')), graphql_name='products')
    delivery_date = sgqlc.types.Field(Timestamp, graphql_name='deliveryDate')
    delivery_shift = sgqlc.types.Field('WorkShift', graphql_name='deliveryShift')


class OrderList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Order))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ParetoTimeseries(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('timestamp', 'value', 'accumulative')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='timestamp')
    value = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='value')
    accumulative = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='accumulative')


class Period(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('type', 'start_at', 'end_at', 'frequency')
    type = sgqlc.types.Field(sgqlc.types.non_null(PeriodType), graphql_name='type')
    start_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='startAt')
    end_at = sgqlc.types.Field(Timestamp, graphql_name='endAt')
    frequency = sgqlc.types.Field(PeriodFrequency, graphql_name='frequency')


class Permission(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'desc', 'code', 'type', 'range')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    desc = sgqlc.types.Field(String, graphql_name='desc')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    type = sgqlc.types.Field(PermissionType, graphql_name='type')
    range = sgqlc.types.Field(PermissionDataRange, graphql_name='range')


class Procedure(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class ProcedureList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Procedure))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ProcedureSegment(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'nodes')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(JSONString), graphql_name='nodes')


class ProcedureSegmentList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ProcedureSegment))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class Process(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('parent', 'procedure', 'children')
    parent = sgqlc.types.Field(sgqlc.types.non_null(Material), graphql_name='parent')
    procedure = sgqlc.types.Field(Procedure, graphql_name='procedure')
    children = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ProductionProcessChild'))), graphql_name='children')


class ProdFeeInfoItem(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('prod_name', 'prod_eff_time', 'prod_exp_time', 'prod_desc')
    prod_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='prodName')
    prod_eff_time = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='prodEffTime')
    prod_exp_time = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='prodExpTime')
    prod_desc = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='prodDesc')


class Product(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'material', 'target_outcome', 'delivery_date', 'delivery_shift', 'demand', 'production_plan')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    material = sgqlc.types.Field(sgqlc.types.non_null(Material), graphql_name='material')
    target_outcome = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='targetOutcome')
    delivery_date = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='deliveryDate')
    delivery_shift = sgqlc.types.Field(sgqlc.types.non_null('WorkShift'), graphql_name='deliveryShift')
    demand = sgqlc.types.Field(String, graphql_name='demand')
    production_plan = sgqlc.types.Field('ProductionPlan', graphql_name='productionPlan')


class ProductionFinishSubScheduleData(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('production', 'defective', 'start', 'end')
    production = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='production')
    defective = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='defective')
    start = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='start')
    end = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='end')


class ProductionMachine(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'code', 'thing', 'status', 'latest_ticket', 'team')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    thing = sgqlc.types.Field(sgqlc.types.non_null('Thing'), graphql_name='thing')
    status = sgqlc.types.Field(sgqlc.types.non_null(ProductionMachineStatus), graphql_name='status')
    latest_ticket = sgqlc.types.Field('ProductionTicket', graphql_name='latestTicket')
    team = sgqlc.types.Field('ProductionTeam', graphql_name='team')


class ProductionMachineList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ProductionMachine))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ProductionPlan(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'code', 'order', 'status', 'product', 'current_outcome', 'target_outcome', 'start_day', 'end_day', 'start_shift', 'end_shift', 'responsibles', 'production_segments', 'production_records')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    order = sgqlc.types.Field(sgqlc.types.non_null(Order), graphql_name='order')
    status = sgqlc.types.Field(sgqlc.types.non_null(ProductionPlanStatus), graphql_name='status')
    product = sgqlc.types.Field(sgqlc.types.non_null(Product), graphql_name='product')
    current_outcome = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='currentOutcome')
    target_outcome = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='targetOutcome')
    start_day = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='startDay')
    end_day = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='endDay')
    start_shift = sgqlc.types.Field(sgqlc.types.non_null('WorkShift'), graphql_name='startShift')
    end_shift = sgqlc.types.Field(sgqlc.types.non_null('WorkShift'), graphql_name='endShift')
    responsibles = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Worker'))), graphql_name='responsibles')
    production_segments = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ProductionSegment'))), graphql_name='productionSegments')
    production_records = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('ProductionRecord')), graphql_name='productionRecords')


class ProductionPlanList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ProductionPlan))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ProductionProcess(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'process')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    process = sgqlc.types.Field(sgqlc.types.non_null(Process), graphql_name='process')


class ProductionProcessChild(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('rate', 'child')
    rate = sgqlc.types.Field('ProductionRate', graphql_name='rate')
    child = sgqlc.types.Field(Material, graphql_name='child')


class ProductionProcessesList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.list_of(ProductionProcess), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ProductionRate(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('parent_num', 'child_num')
    parent_num = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='parentNum')
    child_num = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='childNum')


class ProductionRecord(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'day', 'shift', 'group', 'material', 'collected_outcome', 'actual_outcome', 'failed_outcome', 'reporter')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    day = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='day')
    shift = sgqlc.types.Field(sgqlc.types.non_null('WorkShift'), graphql_name='shift')
    group = sgqlc.types.Field(sgqlc.types.non_null('WorkGroup'), graphql_name='group')
    material = sgqlc.types.Field(sgqlc.types.non_null(Material), graphql_name='material')
    collected_outcome = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='collectedOutcome')
    actual_outcome = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='actualOutcome')
    failed_outcome = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='failedOutcome')
    reporter = sgqlc.types.Field(sgqlc.types.non_null('Worker'), graphql_name='reporter')


class ProductionRecordList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ProductionRecord))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ProductionSchedule(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'timestamp', 'thing', 'shift', 'rate', 'ticket_no', 'total_num')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='timestamp')
    thing = sgqlc.types.Field(sgqlc.types.non_null('Thing'), graphql_name='thing')
    shift = sgqlc.types.Field(sgqlc.types.non_null('ProductionShift'), graphql_name='shift')
    rate = sgqlc.types.Field(Float, graphql_name='rate')
    ticket_no = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='ticketNo')
    total_num = sgqlc.types.Field(Int, graphql_name='totalNum')


class ProductionScheduleList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('total_count', 'data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ProductionSchedule)), graphql_name='data')


class ProductionScheduleLog(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('timestamp', 'action', 'ticket', 'user')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='timestamp')
    action = sgqlc.types.Field(ProductionScheduleAction, graphql_name='action')
    ticket = sgqlc.types.Field('ProductionTicket', graphql_name='ticket')
    user = sgqlc.types.Field('User', graphql_name='user')


class ProductionScheduleLogList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('total_count', 'data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    data = sgqlc.types.Field(sgqlc.types.list_of(ProductionScheduleLog), graphql_name='data')


class ProductionSegment(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'material', 'start_day', 'end_day', 'start_shift', 'end_shift', 'target_outcome', 'current_outcome', 'failed_outcome', 'responsibles', 'work_duties')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    material = sgqlc.types.Field(sgqlc.types.non_null(Material), graphql_name='material')
    start_day = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='startDay')
    end_day = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='endDay')
    start_shift = sgqlc.types.Field(sgqlc.types.non_null('WorkShift'), graphql_name='startShift')
    end_shift = sgqlc.types.Field(sgqlc.types.non_null('WorkShift'), graphql_name='endShift')
    target_outcome = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='targetOutcome')
    current_outcome = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='currentOutcome')
    failed_outcome = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='failedOutcome')
    responsibles = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('Worker')), graphql_name='responsibles')
    work_duties = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('WorkDuty')), graphql_name='workDuties')


class ProductionShift(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'start', 'end')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    start = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='start')
    end = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='end')


class ProductionSubSchedule(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'ticket', 'production', 'defective', 'lack_num', 'end', 'tags', 'priority')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    ticket = sgqlc.types.Field(sgqlc.types.non_null('ProductionTicket'), graphql_name='ticket')
    production = sgqlc.types.Field(Int, graphql_name='production')
    defective = sgqlc.types.Field(Int, graphql_name='defective')
    lack_num = sgqlc.types.Field(Int, graphql_name='lackNum')
    end = sgqlc.types.Field(Timestamp, graphql_name='end')
    tags = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='tags')
    priority = sgqlc.types.Field(ProductionTicketPriority, graphql_name='priority')


class ProductionSubScheduleList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('total_count', 'data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ProductionSubSchedule)), graphql_name='data')


class ProductionTeam(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'leader')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    leader = sgqlc.types.Field('ProductionTeammate', graphql_name='leader')


class ProductionTeammate(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'code', 'phone', 'gender', 'is_leader')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    code = sgqlc.types.Field(String, graphql_name='code')
    phone = sgqlc.types.Field(String, graphql_name='phone')
    gender = sgqlc.types.Field(sgqlc.types.non_null(Gender), graphql_name='gender')
    is_leader = sgqlc.types.Field(Boolean, graphql_name='isLeader')


class ProductionTeammateList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('total_count', 'data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ProductionTeammate)), graphql_name='data')


class ProductionTicket(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'code', 'replenishment_seq', 'customer', 'product', 'model', 'thing', 'num', 'yield_num', 'lack_num', 'defective', 'deliver_at', 'plan_at', 'end', 'shift', 'remark', 'status', 'priority', 'tags', 'manual', 'paper')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    replenishment_seq = sgqlc.types.Field(Int, graphql_name='replenishmentSeq')
    customer = sgqlc.types.Field(String, graphql_name='customer')
    product = sgqlc.types.Field(String, graphql_name='product')
    model = sgqlc.types.Field(String, graphql_name='model')
    thing = sgqlc.types.Field(sgqlc.types.non_null('Thing'), graphql_name='thing')
    num = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='num')
    yield_num = sgqlc.types.Field(Int, graphql_name='yieldNum')
    lack_num = sgqlc.types.Field(Int, graphql_name='lackNum')
    defective = sgqlc.types.Field(Int, graphql_name='defective')
    deliver_at = sgqlc.types.Field(Timestamp, graphql_name='deliverAt')
    plan_at = sgqlc.types.Field(Timestamp, graphql_name='planAt')
    end = sgqlc.types.Field(Timestamp, graphql_name='end')
    shift = sgqlc.types.Field(ProductionShift, graphql_name='shift')
    remark = sgqlc.types.Field(String, graphql_name='remark')
    status = sgqlc.types.Field(sgqlc.types.non_null(ProductionTicketStatus), graphql_name='status')
    priority = sgqlc.types.Field(ProductionTicketPriority, graphql_name='priority')
    tags = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='tags')
    manual = sgqlc.types.Field(File, graphql_name='manual')
    paper = sgqlc.types.Field(File, graphql_name='paper')


class ProductionTicketList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('total_count', 'data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ProductionTicket)), graphql_name='data')


class Province(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class Query(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('bi_file', 'bi_explore', 'bi_category', 'bi_dashboard_list', 'bi_dashboard', 'bi_published_dashboard_list', 'bi_published_dashboard', 'bi_database_list', 'bi_test_database_uri', 'bi_private_data_source_list', 'bi_file_data_source_list', 'bi_dataset_list', 'bi_column_list', 'bi_excel_info', 'train_school_recruit_task_summary', 'train_school_recruit_task_list', 'train_school_recruit_task', 'train_school_recruit_task_record_list', 'export_train_school_recruit_task_sign_record', 'export_train_school_recruit_task_review_record', 'social_person_list', 'social_person', 'social_person_account_summary', 'recruit_job_overview', 'recruit_job_list', 'recruit_job', 'recruit_job_sign_record_list', 'recruit_student_list', 'recruit_student', 'recruit_student_overview', 'my_recruit_sign_status', 'company_recruit_brief', 'student_faculty', 'stu_no_exists', 'train_course_list', 'train_course', 'my_train_sign_course_record_list', 'train_sign_course_record_list', 'check_train_course_exists', 'train_course_round', 'export_chan_jiao_auth_template', 'train_school_student_list', 'train_school_student', 'check_student_info_exists', 'export_student_info', 'export_chan_jiao_student_info_template', 'train_human_resource_list', 'train_work_type_list', 'train_work_level', 'check_work_type_exists', 'train_faculty_list', 'train_class_list', 'check_faculty_exists', 'check_stu_class_exists', 'is_faculty_admin', 'is_class_teacher', 'company_demand_overview_list', 'company_demand_list', 'company_demand', 'company_demand_summary', 'eprect_production_record', 'eprect_production_record_list', 'eprect_mold_list', 'bi_energy_device', 'bi_energy_operation_time', 'bi_energy_electric_quantity', 'bi_energy_fee', 'bi_macro_electric_quantity', 'bi_macro_peak_rate', 'current_date_data', 'current_shift_data', 'history_status_data', 'history_data', 'range_data', 'history_raw', 'multi_history_raw', 'real_raw', 'history_report', 'history_report_list', 'export_history_report', 'export_thing_energy_detail', 'export_thing_energy_detail_daily', 'real_report', 'total_report', 'thing_report_list', 'export_thing_report_list', 'fee_report_list', 'export_fee_report_list', 'thing_total_report_list', 'export_thing_total_report_list', 'energy_consumption_to_t', 'energy_consumption_trend', 'energy_power_trend', 'energy_power_daily_trend', 'energy_consumption_comparison_by_group', 'energy_consumption_comparison_by_type', 'things_overall', 'things_peak_rate_rank', 'things_energy_consumption_rank', 'things_operation_rate_rank', 'things_power_on_rate_rank', 'things_energy_consumption_overall', 'things_energy_consumption_overall_sub', 'area_energy_consumption_overall', 'area_things_overall', 'area_energy_consumption', 'area_peak_power', 'area_production', 'area_redundants', 'area_bottlenecks', 'area_energy_per_product_rank', 'area_energy_consumption_rank', 'area_power_on_rate_rank', 'area_production_distribution', 'area_peak_rate_by_company', 'area_energy_consumption_by_company', 'area_redundant_by_company', 'area_bottleneck_by_company', 'area_production_by_company', 'export_area_production_by_company', 'export_area_redundant_by_company', 'export_area_bottleneck_by_company', 'export_area_peak_rate_by_company', 'export_area_energy_consumption_by_company', 'cockpit_overall', 'cockpit_rate_overall', 'cockpit_rate_list', 'export_cockpit_rate_list', 'cockpit_oee', 'export_cockpit_oee', 'cockpit_operation_rate', 'export_cockpit_operation_rate', 'cockpit_performance_rate', 'export_cockpit_performance_rate', 'cockpit_yield_rate', 'export_cockpit_yield_rate', 'cockpit_organization_oeerank', 'cockpit_organization_operation_rate_rank', 'cockpit_organization_performance_rate_rank', 'cockpit_organization_yield_rate_rank', 'cockpit_thing_type_oeerank', 'cockpit_thing_type_operation_rate_rank', 'cockpit_thing_type_performance_rate_rank', 'cockpit_thing_type_yield_rate_rank', 'cockpit_thing_list', 'export_cockpit_thing_list', 'cockpit_target_list', 'cnc_overall', 'cnc_current_alerts', 'thing_rate_overall', 'thing_rate', 'cnc_alert_overall', 'cnc_alert_list', 'cnc_alerts', 'company_production', 'company_energy', 'company_overall', 'company_bottleneck', 'company_redundant', 'thing_input_record_summary_list', 'thing_input_record_list', 'spare_part_stock', 'spare_part_stocks', 'export_spare_part_stock', 'thing_inspection', 'thing_inspections', 'export_thing_inspections', 'thing_inspection_rule', 'thing_inspection_rules', 'export_thing_inspection_rules', 'spare_part_receipt', 'spare_part_receipts', 'export_spare_part_receipts', 'thing_overview', 'thing_summary', 'spare_part_summary', 'task_summary', 'export_thing_summary', 'export_spare_part_summary', 'export_task_summary', 'thing_maintenance_rule', 'thing_maintenance_rules', 'export_thing_maintenance_rules', 'thing_maintenance', 'thing_maintenances', 'export_thing_maintenances', 'thing', 'thing_by_qr_code', 'things', 'export_things', 'things_template', 'thing_group_tree', 'thing_group', 'thing_group_users', 'thing_group_depts', 'dept_user_thing_groups', 'check_alter_department_thing_group', 'check_delete_department', 'form_struct', 'form_structs', 'filter_values', 'filter_relation_values', 'user_relation_filter_values', 'department_relation_filter_values', 'spare_part', 'spare_parts', 'export_spare_parts', 'spare_parts_template', 'thing_repair', 'thing_repairs', 'export_thing_repairs', 'spare_part_outbound', 'spare_part_outbounds', 'export_spare_part_outbounds', 'upload_edm_config', 'upload_edm_configs', 'exists_router_template_name', 'device_channel_protocols', 'device_channel_serial_com_ports', 'device_channel_baud_rate', 'device_channel_serial_parities', 'device_channel_stop_bit', 'device_channel_data_bit', 'device_channel_register_types', 'device_channel_register_data_types', 'router_template_configuration_list', 'router_template_configuration', 'device_channel_channel_list', 'device_channel_configuration', 'router_model_list', 'router', 'router_list', 'export_router', 'router_summary', 'exist_router', 'router_thing_adapter_key_real_time_data_list', 'router_thing_history_data', 'router_alarm_type_list', 'router_alarm_level_list', 'router_alarm_record_list', 'router_alarm_record_summary', 'bi_fdifault', 'fault', 'fault_list', 'fault_issue_summary', 'fault_issue', 'fault_issue_list', 'fault_reason_list', 'fault_rule', 'fault_rule_list', 'fault_solution', 'fault_solution_list', 'directory', 'production_team', 'production_teammate_list', 'production_ticket_list', 'production_shift', 'production_finish_sub_schedule_data', 'production_schedule_list', 'production_sub_schedule_list', 'export_production_sub_schedule', 'production_machine_list', 'production_schedule_log', 'production_teammate_template', 'production_current_thing', 'dmegc_energy_consumption', 'dmegc_production', 'dmegc_overall', 'dmegc_alerts', 'dmegc_oee', 'dmegc_operation_rate', 'dmegc_performance_rate', 'dmegc_yield_rate', 'jhdv_industry_list', 'jhdv_region_statistic_list', 'jhdv_city_statistic', 'jhdv_device_running_statistic', 'jhdv_device_index_data_rank', 'jhdv_device_index_data_summary', 'junye_thing_location_map', 'junye_thing_group_location_map', 'junye_business_situation', 'junye_production_plan', 'junye_material_management', 'junye_thing_status_distribution', 'junye_alarm_distribution', 'junye_thing_type_distribution', 'junye_daily_energy_consumption_history', 'junye_current_month_energy_consumption', 'junye_last_month_energy_consumption', 'thing_type', 'thing_types', 'thing_type_list', 'thing_type_code_list', 'thing_mechanism_model', 'source_key', 'source_key_list', 'source_model_key_list', 'adapter_key', 'adapter_key_list', 'adapter_model_key_list', 'cockpit_key', 'cockpit_key_list', 'cockpit_aggregation', 'cockpit_aggregations', 'thing_status', 'thing_statuses', 'energy_group', 'energy_group_list', 'energy_time_distribution', 'worker', 'workers', 'work_group', 'work_groups', 'work_shift', 'work_shifts', 'materials', 'procedures', 'procedure_segment', 'procedure_segments', 'work_duties', 'production_process', 'production_processes', 'bom', 'order', 'orders', 'production_plans', 'bi_pdmalert', 'alert_rules', 'alert_config', 'alerts', 'export_alerts', 'sim_summary', 'sim', 'sims', 'sim_traffic', 'sim_bill', 'sim_alerts', 'export_sims', 'sim_alert_status', 'upload_config', 'upload_configs', 'notification_config_list', 'notification_config', 'notification_list', 'notification', 'notification_config_app', 'notification_app', 'apps', 'company_apps', 'my_company_apps', 'my_app_list', 'quick_access_app', 'recent_app', 'app_config', 'bi_issue_issue', 'system_log_list', 'system_log_action', 'issues', 'export_issues', 'issue', 'market_issue_list', 'market_issue', 'market_issue_summary', 'company_exists', 'company_type_list', 'provinces', 'cities', 'counties', 'company', 'companies', 'city_companies', 'type_companies', 'my_company', 'department_tree', 'department_list', 'department_name_same_as_siblings', 'company_bidatasource_list', 'company_bidatasource_tree', 'workbench', 'workbench_card_field', 'workbench_card_option', 'market_solution_list', 'market_solution', 'market_solution_summary', 'role_list', 'permission_tree', 'role_exists', 'market_app_list', 'market_app', 'market_app_summary', 'account_exists', 'me', 'company_admin_users', 'platform_admin_users', 'users', 'platform_user_list', 'user', 'user_template', 'export_user', 'support_users')
    bi_file = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(File)), graphql_name='biFile', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='id', default=None)),
))
    )
    bi_explore = sgqlc.types.Field(sgqlc.types.non_null(JSON), graphql_name='biExplore', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(JSON), graphql_name='input', default=None)),
))
    )
    bi_category = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(BICategory))), graphql_name='biCategory')
    bi_dashboard_list = sgqlc.types.Field(sgqlc.types.non_null(BIDashboardList), graphql_name='biDashboardList', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('filter', sgqlc.types.Arg(BIDashboardFilterInput, graphql_name='filter', default=None)),
))
    )
    bi_dashboard = sgqlc.types.Field(sgqlc.types.non_null(BIDashboard), graphql_name='biDashboard', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    bi_published_dashboard_list = sgqlc.types.Field(sgqlc.types.non_null(BIPublishedDashboardList), graphql_name='biPublishedDashboardList', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('filter', sgqlc.types.Arg(BIPublishedDashboardFilterInput, graphql_name='filter', default=None)),
))
    )
    bi_published_dashboard = sgqlc.types.Field(sgqlc.types.non_null(BIPublishedDashboard), graphql_name='biPublishedDashboard', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    bi_database_list = sgqlc.types.Field(sgqlc.types.non_null(BIDatabaseList), graphql_name='biDatabaseList', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
))
    )
    bi_test_database_uri = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='biTestDatabaseUri', args=sgqlc.types.ArgDict((
        ('uri', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='uri', default=None)),
))
    )
    bi_private_data_source_list = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('BIPrivateDataSource'))), graphql_name='biPrivateDataSourceList', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    bi_file_data_source_list = sgqlc.types.Field(sgqlc.types.non_null(BIFileDataSourceList), graphql_name='biFileDataSourceList', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('filter', sgqlc.types.Arg(BIFileDataSourceFilterInput, graphql_name='filter', default=None)),
))
    )
    bi_dataset_list = sgqlc.types.Field(sgqlc.types.non_null(BIDatasetList), graphql_name='biDatasetList', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('filter', sgqlc.types.Arg(BIDatasetFilterInput, graphql_name='filter', default=None)),
))
    )
    bi_column_list = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(BIColumn))), graphql_name='biColumnList', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    bi_excel_info = sgqlc.types.Field(sgqlc.types.non_null(BIExcel), graphql_name='biExcelInfo', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    train_school_recruit_task_summary = sgqlc.types.Field('TrainSchoolRecruitTaskSummary', graphql_name='trainSchoolRecruitTaskSummary')
    train_school_recruit_task_list = sgqlc.types.Field(sgqlc.types.non_null('TrainSchoolRecruitTaskList'), graphql_name='trainSchoolRecruitTaskList', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(TrainSchoolRecruitTaskFilterInput, graphql_name='filter', default=None)),
))
    )
    train_school_recruit_task = sgqlc.types.Field(sgqlc.types.non_null('TrainSchoolRecruitTask'), graphql_name='trainSchoolRecruitTask', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(ID, graphql_name='id', default=None)),
))
    )
    train_school_recruit_task_record_list = sgqlc.types.Field(sgqlc.types.non_null('TrainSchoolRecruitTaskRecordList'), graphql_name='trainSchoolRecruitTaskRecordList', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(TrainSchoolRecruitTaskRecordFilterInput), graphql_name='filter', default=None)),
))
    )
    export_train_school_recruit_task_sign_record = sgqlc.types.Field(sgqlc.types.non_null('RawFile'), graphql_name='exportTrainSchoolRecruitTaskSignRecord', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    export_train_school_recruit_task_review_record = sgqlc.types.Field(sgqlc.types.non_null('RawFile'), graphql_name='exportTrainSchoolRecruitTaskReviewRecord', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    social_person_list = sgqlc.types.Field(sgqlc.types.non_null('SocialPersonList'), graphql_name='socialPersonList', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(SocialPersonListFilterInput, graphql_name='filter', default=None)),
))
    )
    social_person = sgqlc.types.Field(sgqlc.types.non_null('SocialPerson'), graphql_name='socialPerson', args=sgqlc.types.ArgDict((
        ('user_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='userId', default=None)),
))
    )
    social_person_account_summary = sgqlc.types.Field(sgqlc.types.non_null('SocialPersonAccountSummary'), graphql_name='socialPersonAccountSummary', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(SocialPersonListFilterInput, graphql_name='filter', default=None)),
))
    )
    recruit_job_overview = sgqlc.types.Field(sgqlc.types.non_null('RecruitJobOverview'), graphql_name='recruitJobOverview')
    recruit_job_list = sgqlc.types.Field(sgqlc.types.non_null('RecruitJobList'), graphql_name='recruitJobList', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('status', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(RecruitJobStatus)), graphql_name='status', default=None)),
        ('filter', sgqlc.types.Arg(RecruitJobFilterInput, graphql_name='filter', default=None)),
))
    )
    recruit_job = sgqlc.types.Field(sgqlc.types.non_null('RecruitJob'), graphql_name='recruitJob', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    recruit_job_sign_record_list = sgqlc.types.Field(sgqlc.types.non_null('RecruitJobSignRecordList'), graphql_name='recruitJobSignRecordList', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(RecruitJobSignRecordFilter, graphql_name='filter', default=None)),
))
    )
    recruit_student_list = sgqlc.types.Field(sgqlc.types.non_null('RecruitStudentList'), graphql_name='recruitStudentList', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(RecruitStudentFilter, graphql_name='filter', default=None)),
))
    )
    recruit_student = sgqlc.types.Field(sgqlc.types.non_null('RecruitStudent'), graphql_name='recruitStudent', args=sgqlc.types.ArgDict((
        ('user_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='userId', default=None)),
))
    )
    recruit_student_overview = sgqlc.types.Field(sgqlc.types.non_null('RecruitStudentOverview'), graphql_name='recruitStudentOverview')
    my_recruit_sign_status = sgqlc.types.Field(sgqlc.types.non_null(MyRecruitSignStatus), graphql_name='myRecruitSignStatus')
    company_recruit_brief = sgqlc.types.Field(sgqlc.types.non_null(CompanyRecruitBrief), graphql_name='companyRecruitBrief', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    student_faculty = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('RecruitFaculty'))), graphql_name='studentFaculty')
    stu_no_exists = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='stuNoExists', args=sgqlc.types.ArgDict((
        ('stu_no', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='stuNo', default=None)),
))
    )
    train_course_list = sgqlc.types.Field(sgqlc.types.non_null('TrainCourseList'), graphql_name='trainCourseList', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(TrainCourseFilterInput, graphql_name='filter', default=None)),
))
    )
    train_course = sgqlc.types.Field(sgqlc.types.non_null('TrainCourse'), graphql_name='trainCourse', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    my_train_sign_course_record_list = sgqlc.types.Field(sgqlc.types.non_null('TrainSignCourseRecordList'), graphql_name='myTrainSignCourseRecordList', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(SignCourseFilterInput, graphql_name='filter', default=None)),
))
    )
    train_sign_course_record_list = sgqlc.types.Field(sgqlc.types.non_null('TrainSignCourseRecordList'), graphql_name='trainSignCourseRecordList', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(SignCourseFilterInput, graphql_name='filter', default=None)),
))
    )
    check_train_course_exists = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='checkTrainCourseExists', args=sgqlc.types.ArgDict((
        ('work_type_id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='workTypeId', default=None)),
        ('work_level_id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='workLevelId', default=None)),
))
    )
    train_course_round = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='trainCourseRound', args=sgqlc.types.ArgDict((
        ('category', sgqlc.types.Arg(sgqlc.types.non_null(TrainCourseRoundCategory), graphql_name='category', default=None)),
))
    )
    export_chan_jiao_auth_template = sgqlc.types.Field(sgqlc.types.non_null('RawFile'), graphql_name='exportChanJiaoAuthTemplate')
    train_school_student_list = sgqlc.types.Field('TrainSchoolStudentList', graphql_name='trainSchoolStudentList', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(TrainSchoolStudentFilterInput, graphql_name='filter', default=None)),
))
    )
    train_school_student = sgqlc.types.Field(sgqlc.types.non_null('TrainSchoolStudent'), graphql_name='trainSchoolStudent', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    check_student_info_exists = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='checkStudentInfoExists', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(CheckStudentInfoExistsInput, graphql_name='input', default=None)),
))
    )
    export_student_info = sgqlc.types.Field(sgqlc.types.non_null('RawFile'), graphql_name='exportStudentInfo')
    export_chan_jiao_student_info_template = sgqlc.types.Field(sgqlc.types.non_null('RawFile'), graphql_name='exportChanJiaoStudentInfoTemplate')
    train_human_resource_list = sgqlc.types.Field(sgqlc.types.non_null('TrainHumanResourceList'), graphql_name='trainHumanResourceList', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(TrainHumanResourceFilterInput, graphql_name='filter', default=None)),
))
    )
    train_work_type_list = sgqlc.types.Field(sgqlc.types.non_null('TrainWorkTypeList'), graphql_name='trainWorkTypeList', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(TrainWorkTypeFilter, graphql_name='filter', default=None)),
))
    )
    train_work_level = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('TrainWorkLevel')), graphql_name='trainWorkLevel')
    check_work_type_exists = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='checkWorkTypeExists', args=sgqlc.types.ArgDict((
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
))
    )
    train_faculty_list = sgqlc.types.Field(sgqlc.types.non_null('TrainFacultyList'), graphql_name='trainFacultyList', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(TrainFacultyListFilterInput, graphql_name='filter', default=None)),
))
    )
    train_class_list = sgqlc.types.Field(sgqlc.types.non_null('TrainClassList'), graphql_name='trainClassList', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(TrainClassListFilterInput, graphql_name='filter', default=None)),
))
    )
    check_faculty_exists = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='checkFacultyExists', args=sgqlc.types.ArgDict((
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
))
    )
    check_stu_class_exists = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='checkStuClassExists', args=sgqlc.types.ArgDict((
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
))
    )
    is_faculty_admin = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isFacultyAdmin', args=sgqlc.types.ArgDict((
        ('user_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='user_id', default=None)),
))
    )
    is_class_teacher = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isClassTeacher', args=sgqlc.types.ArgDict((
        ('user_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='user_id', default=None)),
))
    )
    company_demand_overview_list = sgqlc.types.Field(sgqlc.types.non_null(CompanyDemandList), graphql_name='companyDemandOverviewList', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(CompanyDemandFilterInput, graphql_name='filter', default=None)),
))
    )
    company_demand_list = sgqlc.types.Field(sgqlc.types.non_null(CompanyDemandList), graphql_name='companyDemandList', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(CompanyDemandFilterInput, graphql_name='filter', default=None)),
))
    )
    company_demand = sgqlc.types.Field(sgqlc.types.non_null(CompanyDemand), graphql_name='companyDemand', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    company_demand_summary = sgqlc.types.Field(sgqlc.types.non_null(CompanyDemandSummay), graphql_name='companyDemandSummary', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(CompanyDemandFilterInput, graphql_name='filter', default=None)),
))
    )
    eprect_production_record = sgqlc.types.Field(sgqlc.types.non_null(EprectProductionRecord), graphql_name='eprectProductionRecord', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    eprect_production_record_list = sgqlc.types.Field(sgqlc.types.non_null(EprectProductionRecordList), graphql_name='eprectProductionRecordList', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(EprectProductionRecordFilterInput), graphql_name='filter', default=None)),
))
    )
    eprect_mold_list = sgqlc.types.Field(sgqlc.types.non_null(EprectMoldList), graphql_name='eprectMoldList', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(EprectMoldFilterInput, graphql_name='filter', default=None)),
))
    )
    bi_energy_device = sgqlc.types.Field(sgqlc.types.list_of(BIResult), graphql_name='biEnergyDevice', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(BIFilterInput, graphql_name='filter', default=None)),
))
    )
    bi_energy_operation_time = sgqlc.types.Field(sgqlc.types.list_of(BIResult), graphql_name='biEnergyOperationTime', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(BIFilterInput, graphql_name='filter', default=None)),
))
    )
    bi_energy_electric_quantity = sgqlc.types.Field(sgqlc.types.list_of(BIResult), graphql_name='biEnergyElectricQuantity', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(BIFilterInput, graphql_name='filter', default=None)),
))
    )
    bi_energy_fee = sgqlc.types.Field(sgqlc.types.list_of(EnergyFeeBIResult), graphql_name='biEnergyFee', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(BIFilterInput, graphql_name='filter', default=None)),
))
    )
    bi_macro_electric_quantity = sgqlc.types.Field(sgqlc.types.list_of(MacroBIResult), graphql_name='biMacroElectricQuantity', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(BIFilterInput, graphql_name='filter', default=None)),
))
    )
    bi_macro_peak_rate = sgqlc.types.Field(sgqlc.types.list_of(MacroBIResult), graphql_name='biMacroPeakRate', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(BIFilterInput, graphql_name='filter', default=None)),
))
    )
    current_date_data = sgqlc.types.Field('ThingData', graphql_name='currentDateData', args=sgqlc.types.ArgDict((
        ('thing_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='thingID', default=None)),
))
    )
    current_shift_data = sgqlc.types.Field('ThingData', graphql_name='currentShiftData', args=sgqlc.types.ArgDict((
        ('thing_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='thingID', default=None)),
))
    )
    history_status_data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(HistoryStatusData)), graphql_name='historyStatusData', args=sgqlc.types.ArgDict((
        ('company_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='companyID', default=None)),
        ('thing_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='thingID', default=None)),
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
))
    )
    history_data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('ThingData')), graphql_name='historyData', args=sgqlc.types.ArgDict((
        ('thing_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='thingID', default=None)),
))
    )
    range_data = sgqlc.types.Field('RangeData', graphql_name='rangeData', args=sgqlc.types.ArgDict((
        ('thing_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='thingID', default=None)),
        ('shift', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='shift', default=None)),
        ('start_date', sgqlc.types.Arg(Timestamp, graphql_name='startDate', default=None)),
        ('start_shift', sgqlc.types.Arg(Int, graphql_name='startShift', default=None)),
        ('end_date', sgqlc.types.Arg(Timestamp, graphql_name='endDate', default=None)),
        ('end_shift', sgqlc.types.Arg(Int, graphql_name='endShift', default=None)),
        ('duty_person', sgqlc.types.Arg(String, graphql_name='dutyPerson', default=None)),
))
    )
    history_raw = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('RawData')), graphql_name='historyRaw', args=sgqlc.types.ArgDict((
        ('thing_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='thingID', default=None)),
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('field', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='field', default=None)),
        ('granularity', sgqlc.types.Arg(Granularity, graphql_name='granularity', default=None)),
))
    )
    multi_history_raw = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('RawData')), graphql_name='multiHistoryRaw', args=sgqlc.types.ArgDict((
        ('thing_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='thingID', default=None)),
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('fields', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='fields', default=None)),
        ('granularity', sgqlc.types.Arg(Granularity, graphql_name='granularity', default=None)),
        ('func_type', sgqlc.types.Arg(FuncType, graphql_name='funcType', default=None)),
))
    )
    real_raw = sgqlc.types.Field(JSONString, graphql_name='realRaw', args=sgqlc.types.ArgDict((
        ('thing_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='thingID', default=None)),
        ('fields', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='fields', default=None)),
))
    )
    history_report = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('RawData')), graphql_name='historyReport', args=sgqlc.types.ArgDict((
        ('thing_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='thingID', default=None)),
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('tags', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='tags', default=None)),
        ('fields', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='fields', default=None)),
))
    )
    history_report_list = sgqlc.types.Field('RawDataList', graphql_name='historyReportList', args=sgqlc.types.ArgDict((
        ('thing_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='thingID', default=None)),
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('tags', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='tags', default=None)),
        ('fields', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='fields', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    export_history_report = sgqlc.types.Field('RawFile', graphql_name='exportHistoryReport', args=sgqlc.types.ArgDict((
        ('thing_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='thingID', default=None)),
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('tag', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='tag', default=None)),
        ('fields', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='fields', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    export_thing_energy_detail = sgqlc.types.Field('RawFile', graphql_name='exportThingEnergyDetail', args=sgqlc.types.ArgDict((
        ('thing_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='thingID', default=None)),
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    export_thing_energy_detail_daily = sgqlc.types.Field('RawFile', graphql_name='exportThingEnergyDetailDaily', args=sgqlc.types.ArgDict((
        ('thing_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='thingID', default=None)),
        ('timestamp', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='timestamp', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    real_report = sgqlc.types.Field(JSONString, graphql_name='realReport', args=sgqlc.types.ArgDict((
        ('thing_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='thingID', default=None)),
        ('tags', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='tags', default=None)),
        ('fields', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='fields', default=None)),
))
    )
    total_report = sgqlc.types.Field(JSONString, graphql_name='totalReport', args=sgqlc.types.ArgDict((
        ('thing_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='thingID', default=None)),
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('tags', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='tags', default=None)),
        ('fields', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='fields', default=None)),
))
    )
    thing_report_list = sgqlc.types.Field('ThingReportList', graphql_name='thingReportList', args=sgqlc.types.ArgDict((
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('tag', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='tag', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('search', sgqlc.types.Arg(String, graphql_name='search', default=None)),
        ('types', sgqlc.types.Arg(sgqlc.types.list_of(IDInput), graphql_name='types', default=None)),
        ('energy_group', sgqlc.types.Arg(sgqlc.types.list_of(IDInput), graphql_name='energyGroup', default=None)),
        ('energy_type', sgqlc.types.Arg(sgqlc.types.list_of(EnergyType), graphql_name='energyType', default=None)),
        ('company_id', sgqlc.types.Arg(ID, graphql_name='companyID', default=None)),
))
    )
    export_thing_report_list = sgqlc.types.Field(sgqlc.types.non_null('RawFile'), graphql_name='exportThingReportList', args=sgqlc.types.ArgDict((
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('tag', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='tag', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('search', sgqlc.types.Arg(String, graphql_name='search', default=None)),
        ('types', sgqlc.types.Arg(sgqlc.types.list_of(IDInput), graphql_name='types', default=None)),
        ('energy_group', sgqlc.types.Arg(sgqlc.types.list_of(IDInput), graphql_name='energyGroup', default=None)),
        ('energy_type', sgqlc.types.Arg(sgqlc.types.list_of(EnergyType), graphql_name='energyType', default=None)),
        ('company_id', sgqlc.types.Arg(ID, graphql_name='companyID', default=None)),
))
    )
    fee_report_list = sgqlc.types.Field(FeeReportList, graphql_name='feeReportList', args=sgqlc.types.ArgDict((
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('granularity', sgqlc.types.Arg(sgqlc.types.non_null(Granularity), graphql_name='granularity', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('energy_type', sgqlc.types.Arg(sgqlc.types.list_of(EnergyType), graphql_name='energyType', default=None)),
        ('company_id', sgqlc.types.Arg(ID, graphql_name='companyID', default=None)),
))
    )
    export_fee_report_list = sgqlc.types.Field('RawFile', graphql_name='exportFeeReportList', args=sgqlc.types.ArgDict((
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('granularity', sgqlc.types.Arg(sgqlc.types.non_null(Granularity), graphql_name='granularity', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('energy_type', sgqlc.types.Arg(sgqlc.types.list_of(EnergyType), graphql_name='energyType', default=None)),
        ('company_id', sgqlc.types.Arg(ID, graphql_name='companyID', default=None)),
))
    )
    thing_total_report_list = sgqlc.types.Field('ThingTotalReportList', graphql_name='thingTotalReportList', args=sgqlc.types.ArgDict((
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('energy_type', sgqlc.types.Arg(sgqlc.types.list_of(EnergyType), graphql_name='energyType', default=None)),
        ('company_id', sgqlc.types.Arg(ID, graphql_name='companyID', default=None)),
))
    )
    export_thing_total_report_list = sgqlc.types.Field('RawFile', graphql_name='exportThingTotalReportList', args=sgqlc.types.ArgDict((
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('energy_type', sgqlc.types.Arg(sgqlc.types.list_of(EnergyType), graphql_name='energyType', default=None)),
        ('company_id', sgqlc.types.Arg(ID, graphql_name='companyID', default=None)),
))
    )
    energy_consumption_to_t = sgqlc.types.Field(EnergyConsumptionToT, graphql_name='energyConsumptionToT', args=sgqlc.types.ArgDict((
        ('timestamp', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='timestamp', default=None)),
        ('type', sgqlc.types.Arg(sgqlc.types.non_null(Granularity), graphql_name='type', default=None)),
        ('company_id', sgqlc.types.Arg(ID, graphql_name='companyID', default=None)),
))
    )
    energy_consumption_trend = sgqlc.types.Field(EnergyTrend, graphql_name='energyConsumptionTrend', args=sgqlc.types.ArgDict((
        ('timestamp', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='timestamp', default=None)),
        ('company_id', sgqlc.types.Arg(ID, graphql_name='companyID', default=None)),
))
    )
    energy_power_trend = sgqlc.types.Field(EnergyTrend, graphql_name='energyPowerTrend', args=sgqlc.types.ArgDict((
        ('timestamp', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='timestamp', default=None)),
        ('company_id', sgqlc.types.Arg(ID, graphql_name='companyID', default=None)),
))
    )
    energy_power_daily_trend = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TimeseriesUnit'))), graphql_name='energyPowerDailyTrend', args=sgqlc.types.ArgDict((
        ('start_at', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='startAt', default=None)),
        ('end_at', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='endAt', default=None)),
        ('company_id', sgqlc.types.Arg(ID, graphql_name='companyID', default=None)),
))
    )
    energy_consumption_comparison_by_group = sgqlc.types.Field(EnergyConsumptionComparison, graphql_name='energyConsumptionComparisonByGroup', args=sgqlc.types.ArgDict((
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('granularity', sgqlc.types.Arg(sgqlc.types.non_null(Granularity), graphql_name='granularity', default=None)),
        ('company_id', sgqlc.types.Arg(ID, graphql_name='companyID', default=None)),
))
    )
    energy_consumption_comparison_by_type = sgqlc.types.Field(EnergyConsumptionComparison, graphql_name='energyConsumptionComparisonByType', args=sgqlc.types.ArgDict((
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('granularity', sgqlc.types.Arg(sgqlc.types.non_null(Granularity), graphql_name='granularity', default=None)),
        ('company_id', sgqlc.types.Arg(ID, graphql_name='companyID', default=None)),
))
    )
    things_overall = sgqlc.types.Field('ThingsOverall', graphql_name='thingsOverall', args=sgqlc.types.ArgDict((
        ('company_id', sgqlc.types.Arg(ID, graphql_name='companyID', default=None)),
        ('organization_id', sgqlc.types.Arg(ID, graphql_name='organizationID', default=None)),
        ('thing_type', sgqlc.types.Arg(ID, graphql_name='thingType', default=None)),
))
    )
    things_peak_rate_rank = sgqlc.types.Field('ThingsRank', graphql_name='thingsPeakRateRank', args=sgqlc.types.ArgDict((
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('company_id', sgqlc.types.Arg(ID, graphql_name='companyID', default=None)),
        ('organization_id', sgqlc.types.Arg(ID, graphql_name='organizationID', default=None)),
        ('thing_type', sgqlc.types.Arg(ID, graphql_name='thingType', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    things_energy_consumption_rank = sgqlc.types.Field('ThingsRank', graphql_name='thingsEnergyConsumptionRank', args=sgqlc.types.ArgDict((
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('company_id', sgqlc.types.Arg(ID, graphql_name='companyID', default=None)),
        ('organization_id', sgqlc.types.Arg(ID, graphql_name='organizationID', default=None)),
        ('thing_type', sgqlc.types.Arg(ID, graphql_name='thingType', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    things_operation_rate_rank = sgqlc.types.Field('ThingsRank', graphql_name='thingsOperationRateRank', args=sgqlc.types.ArgDict((
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('company_id', sgqlc.types.Arg(ID, graphql_name='companyID', default=None)),
        ('organization_id', sgqlc.types.Arg(ID, graphql_name='organizationID', default=None)),
        ('thing_type', sgqlc.types.Arg(ID, graphql_name='thingType', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    things_power_on_rate_rank = sgqlc.types.Field('ThingsRank', graphql_name='thingsPowerOnRateRank', args=sgqlc.types.ArgDict((
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('company_id', sgqlc.types.Arg(ID, graphql_name='companyID', default=None)),
        ('organization_id', sgqlc.types.Arg(ID, graphql_name='organizationID', default=None)),
        ('thing_type', sgqlc.types.Arg(ID, graphql_name='thingType', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    things_energy_consumption_overall = sgqlc.types.Field('ThingsEnergyConsumptionOverall', graphql_name='thingsEnergyConsumptionOverall', args=sgqlc.types.ArgDict((
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('company_id', sgqlc.types.Arg(ID, graphql_name='companyID', default=None)),
        ('organization_id', sgqlc.types.Arg(ID, graphql_name='organizationID', default=None)),
        ('thing_type', sgqlc.types.Arg(ID, graphql_name='thingType', default=None)),
))
    )
    things_energy_consumption_overall_sub = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('ThingsEnergyConsumptionOverall')), graphql_name='thingsEnergyConsumptionOverallSub', args=sgqlc.types.ArgDict((
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('organizations', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='organizations', default=None)),
        ('company_id', sgqlc.types.Arg(ID, graphql_name='companyID', default=None)),
        ('thing_type', sgqlc.types.Arg(ID, graphql_name='thingType', default=None)),
))
    )
    area_energy_consumption_overall = sgqlc.types.Field(AreaEnergyConsumptionOverall, graphql_name='areaEnergyConsumptionOverall', args=sgqlc.types.ArgDict((
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('granularity', sgqlc.types.Arg(sgqlc.types.non_null(Granularity), graphql_name='granularity', default=None)),
        ('county', sgqlc.types.Arg(String, graphql_name='county', default=None)),
))
    )
    area_things_overall = sgqlc.types.Field(AreaThingsOverall, graphql_name='areaThingsOverall', args=sgqlc.types.ArgDict((
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('granularity', sgqlc.types.Arg(sgqlc.types.non_null(Granularity), graphql_name='granularity', default=None)),
        ('county', sgqlc.types.Arg(String, graphql_name='county', default=None)),
        ('company_type', sgqlc.types.Arg(IDInput, graphql_name='companyType', default=None)),
        ('thing_type', sgqlc.types.Arg(ID, graphql_name='thingType', default=None)),
))
    )
    area_energy_consumption = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('TimeseriesUnit')), graphql_name='areaEnergyConsumption', args=sgqlc.types.ArgDict((
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('granularity', sgqlc.types.Arg(sgqlc.types.non_null(Granularity), graphql_name='granularity', default=None)),
        ('county', sgqlc.types.Arg(String, graphql_name='county', default=None)),
))
    )
    area_peak_power = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('TimeseriesUnit')), graphql_name='areaPeakPower', args=sgqlc.types.ArgDict((
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('granularity', sgqlc.types.Arg(sgqlc.types.non_null(Granularity), graphql_name='granularity', default=None)),
        ('county', sgqlc.types.Arg(String, graphql_name='county', default=None)),
))
    )
    area_production = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('TimeseriesUnit')), graphql_name='areaProduction', args=sgqlc.types.ArgDict((
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('granularity', sgqlc.types.Arg(sgqlc.types.non_null(Granularity), graphql_name='granularity', default=None)),
        ('county', sgqlc.types.Arg(String, graphql_name='county', default=None)),
        ('company_type', sgqlc.types.Arg(IDInput, graphql_name='companyType', default=None)),
))
    )
    area_redundants = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(AreaThingTimeseriesUnit)), graphql_name='areaRedundants', args=sgqlc.types.ArgDict((
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('granularity', sgqlc.types.Arg(sgqlc.types.non_null(Granularity), graphql_name='granularity', default=None)),
        ('county', sgqlc.types.Arg(String, graphql_name='county', default=None)),
        ('company_type', sgqlc.types.Arg(IDInput, graphql_name='companyType', default=None)),
        ('thing_type', sgqlc.types.Arg(ID, graphql_name='thingType', default=None)),
))
    )
    area_bottlenecks = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(AreaThingTimeseriesUnit)), graphql_name='areaBottlenecks', args=sgqlc.types.ArgDict((
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('granularity', sgqlc.types.Arg(sgqlc.types.non_null(Granularity), graphql_name='granularity', default=None)),
        ('county', sgqlc.types.Arg(String, graphql_name='county', default=None)),
        ('company_type', sgqlc.types.Arg(IDInput, graphql_name='companyType', default=None)),
        ('thing_type', sgqlc.types.Arg(ID, graphql_name='thingType', default=None)),
))
    )
    area_energy_per_product_rank = sgqlc.types.Field(CompanyRank, graphql_name='areaEnergyPerProductRank', args=sgqlc.types.ArgDict((
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('granularity', sgqlc.types.Arg(sgqlc.types.non_null(Granularity), graphql_name='granularity', default=None)),
        ('county', sgqlc.types.Arg(String, graphql_name='county', default=None)),
        ('company_type', sgqlc.types.Arg(IDInput, graphql_name='companyType', default=None)),
        ('thing_type', sgqlc.types.Arg(ID, graphql_name='thingType', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    area_energy_consumption_rank = sgqlc.types.Field(CompanyRank, graphql_name='areaEnergyConsumptionRank', args=sgqlc.types.ArgDict((
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('granularity', sgqlc.types.Arg(sgqlc.types.non_null(Granularity), graphql_name='granularity', default=None)),
        ('county', sgqlc.types.Arg(String, graphql_name='county', default=None)),
        ('company_type', sgqlc.types.Arg(IDInput, graphql_name='companyType', default=None)),
        ('thing_type', sgqlc.types.Arg(ID, graphql_name='thingType', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    area_power_on_rate_rank = sgqlc.types.Field(CompanyRank, graphql_name='areaPowerOnRateRank', args=sgqlc.types.ArgDict((
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('granularity', sgqlc.types.Arg(sgqlc.types.non_null(Granularity), graphql_name='granularity', default=None)),
        ('county', sgqlc.types.Arg(String, graphql_name='county', default=None)),
        ('company_type', sgqlc.types.Arg(IDInput, graphql_name='companyType', default=None)),
        ('thing_type', sgqlc.types.Arg(ID, graphql_name='thingType', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    area_production_distribution = sgqlc.types.Field(AreaProductionDistribution, graphql_name='areaProductionDistribution', args=sgqlc.types.ArgDict((
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('granularity', sgqlc.types.Arg(sgqlc.types.non_null(Granularity), graphql_name='granularity', default=None)),
        ('county', sgqlc.types.Arg(String, graphql_name='county', default=None)),
        ('company_type', sgqlc.types.Arg(IDInput, graphql_name='companyType', default=None)),
))
    )
    area_peak_rate_by_company = sgqlc.types.Field(AreaPeakRateByCompanyData, graphql_name='areaPeakRateByCompany', args=sgqlc.types.ArgDict((
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('granularity', sgqlc.types.Arg(sgqlc.types.non_null(Granularity), graphql_name='granularity', default=None)),
        ('county', sgqlc.types.Arg(String, graphql_name='county', default=None)),
        ('search', sgqlc.types.Arg(String, graphql_name='search', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    area_energy_consumption_by_company = sgqlc.types.Field(AreaEnergyConsumptionByCompanyData, graphql_name='areaEnergyConsumptionByCompany', args=sgqlc.types.ArgDict((
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('granularity', sgqlc.types.Arg(sgqlc.types.non_null(Granularity), graphql_name='granularity', default=None)),
        ('county', sgqlc.types.Arg(String, graphql_name='county', default=None)),
        ('company_type', sgqlc.types.Arg(IDInput, graphql_name='companyType', default=None)),
        ('thing_type', sgqlc.types.Arg(ID, graphql_name='thingType', default=None)),
        ('search', sgqlc.types.Arg(String, graphql_name='search', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    area_redundant_by_company = sgqlc.types.Field(AreaThingsByCompanyData, graphql_name='areaRedundantByCompany', args=sgqlc.types.ArgDict((
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('granularity', sgqlc.types.Arg(sgqlc.types.non_null(Granularity), graphql_name='granularity', default=None)),
        ('county', sgqlc.types.Arg(String, graphql_name='county', default=None)),
        ('company_type', sgqlc.types.Arg(IDInput, graphql_name='companyType', default=None)),
        ('thing_type', sgqlc.types.Arg(ID, graphql_name='thingType', default=None)),
        ('search', sgqlc.types.Arg(String, graphql_name='search', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    area_bottleneck_by_company = sgqlc.types.Field(AreaThingsByCompanyData, graphql_name='areaBottleneckByCompany', args=sgqlc.types.ArgDict((
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('granularity', sgqlc.types.Arg(sgqlc.types.non_null(Granularity), graphql_name='granularity', default=None)),
        ('county', sgqlc.types.Arg(String, graphql_name='county', default=None)),
        ('company_type', sgqlc.types.Arg(IDInput, graphql_name='companyType', default=None)),
        ('thing_type', sgqlc.types.Arg(ID, graphql_name='thingType', default=None)),
        ('search', sgqlc.types.Arg(String, graphql_name='search', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    area_production_by_company = sgqlc.types.Field(AreaProductionByCompanyData, graphql_name='areaProductionByCompany', args=sgqlc.types.ArgDict((
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('granularity', sgqlc.types.Arg(sgqlc.types.non_null(Granularity), graphql_name='granularity', default=None)),
        ('county', sgqlc.types.Arg(String, graphql_name='county', default=None)),
        ('company_type', sgqlc.types.Arg(IDInput, graphql_name='companyType', default=None)),
        ('search', sgqlc.types.Arg(String, graphql_name='search', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    export_area_production_by_company = sgqlc.types.Field('RawFile', graphql_name='exportAreaProductionByCompany', args=sgqlc.types.ArgDict((
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('granularity', sgqlc.types.Arg(sgqlc.types.non_null(Granularity), graphql_name='granularity', default=None)),
        ('county', sgqlc.types.Arg(String, graphql_name='county', default=None)),
        ('company_type', sgqlc.types.Arg(IDInput, graphql_name='companyType', default=None)),
        ('search', sgqlc.types.Arg(String, graphql_name='search', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    export_area_redundant_by_company = sgqlc.types.Field('RawFile', graphql_name='exportAreaRedundantByCompany', args=sgqlc.types.ArgDict((
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('granularity', sgqlc.types.Arg(sgqlc.types.non_null(Granularity), graphql_name='granularity', default=None)),
        ('county', sgqlc.types.Arg(String, graphql_name='county', default=None)),
        ('company_type', sgqlc.types.Arg(IDInput, graphql_name='companyType', default=None)),
        ('thing_type', sgqlc.types.Arg(ID, graphql_name='thingType', default=None)),
        ('search', sgqlc.types.Arg(String, graphql_name='search', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    export_area_bottleneck_by_company = sgqlc.types.Field('RawFile', graphql_name='exportAreaBottleneckByCompany', args=sgqlc.types.ArgDict((
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('granularity', sgqlc.types.Arg(sgqlc.types.non_null(Granularity), graphql_name='granularity', default=None)),
        ('county', sgqlc.types.Arg(String, graphql_name='county', default=None)),
        ('company_type', sgqlc.types.Arg(IDInput, graphql_name='companyType', default=None)),
        ('thing_type', sgqlc.types.Arg(ID, graphql_name='thingType', default=None)),
        ('search', sgqlc.types.Arg(String, graphql_name='search', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    export_area_peak_rate_by_company = sgqlc.types.Field('RawFile', graphql_name='exportAreaPeakRateByCompany', args=sgqlc.types.ArgDict((
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('granularity', sgqlc.types.Arg(sgqlc.types.non_null(Granularity), graphql_name='granularity', default=None)),
        ('county', sgqlc.types.Arg(String, graphql_name='county', default=None)),
        ('search', sgqlc.types.Arg(String, graphql_name='search', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    export_area_energy_consumption_by_company = sgqlc.types.Field('RawFile', graphql_name='exportAreaEnergyConsumptionByCompany', args=sgqlc.types.ArgDict((
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('granularity', sgqlc.types.Arg(sgqlc.types.non_null(Granularity), graphql_name='granularity', default=None)),
        ('county', sgqlc.types.Arg(String, graphql_name='county', default=None)),
        ('company_type', sgqlc.types.Arg(IDInput, graphql_name='companyType', default=None)),
        ('thing_type', sgqlc.types.Arg(ID, graphql_name='thingType', default=None)),
        ('search', sgqlc.types.Arg(String, graphql_name='search', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    cockpit_overall = sgqlc.types.Field(CockpitOverall, graphql_name='cockpitOverall', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='company', default=None)),
        ('organization', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='organization', default=None)),
        ('thing_type', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='thingType', default=None)),
))
    )
    cockpit_rate_overall = sgqlc.types.Field(CockpitRateOverall, graphql_name='cockpitRateOverall', args=sgqlc.types.ArgDict((
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('company', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='company', default=None)),
        ('organization', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='organization', default=None)),
))
    )
    cockpit_rate_list = sgqlc.types.Field(CockpitRateList, graphql_name='cockpitRateList', args=sgqlc.types.ArgDict((
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('company', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='company', default=None)),
        ('organization', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='organization', default=None)),
        ('granularity', sgqlc.types.Arg(sgqlc.types.non_null(Granularity), graphql_name='granularity', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    export_cockpit_rate_list = sgqlc.types.Field('RawFile', graphql_name='exportCockpitRateList', args=sgqlc.types.ArgDict((
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('company', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='company', default=None)),
        ('organization', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='organization', default=None)),
        ('granularity', sgqlc.types.Arg(sgqlc.types.non_null(Granularity), graphql_name='granularity', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    cockpit_oee = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CockpitTimeseries))), graphql_name='cockpitOEE', args=sgqlc.types.ArgDict((
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('company', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='company', default=None)),
        ('organization', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='organization', default=None)),
        ('target', sgqlc.types.Arg(ID, graphql_name='target', default=None)),
        ('granularity', sgqlc.types.Arg(sgqlc.types.non_null(Granularity), graphql_name='granularity', default=None)),
))
    )
    export_cockpit_oee = sgqlc.types.Field('RawFile', graphql_name='exportCockpitOEE', args=sgqlc.types.ArgDict((
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('company', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='company', default=None)),
        ('organization', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='organization', default=None)),
        ('target', sgqlc.types.Arg(ID, graphql_name='target', default=None)),
        ('granularity', sgqlc.types.Arg(sgqlc.types.non_null(Granularity), graphql_name='granularity', default=None)),
))
    )
    cockpit_operation_rate = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CockpitTimeseries))), graphql_name='cockpitOperationRate', args=sgqlc.types.ArgDict((
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('company', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='company', default=None)),
        ('organization', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='organization', default=None)),
        ('target', sgqlc.types.Arg(ID, graphql_name='target', default=None)),
        ('granularity', sgqlc.types.Arg(sgqlc.types.non_null(Granularity), graphql_name='granularity', default=None)),
))
    )
    export_cockpit_operation_rate = sgqlc.types.Field('RawFile', graphql_name='exportCockpitOperationRate', args=sgqlc.types.ArgDict((
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('company', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='company', default=None)),
        ('organization', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='organization', default=None)),
        ('target', sgqlc.types.Arg(ID, graphql_name='target', default=None)),
        ('granularity', sgqlc.types.Arg(sgqlc.types.non_null(Granularity), graphql_name='granularity', default=None)),
))
    )
    cockpit_performance_rate = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CockpitTimeseries))), graphql_name='cockpitPerformanceRate', args=sgqlc.types.ArgDict((
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('company', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='company', default=None)),
        ('organization', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='organization', default=None)),
        ('target', sgqlc.types.Arg(ID, graphql_name='target', default=None)),
        ('granularity', sgqlc.types.Arg(sgqlc.types.non_null(Granularity), graphql_name='granularity', default=None)),
))
    )
    export_cockpit_performance_rate = sgqlc.types.Field('RawFile', graphql_name='exportCockpitPerformanceRate', args=sgqlc.types.ArgDict((
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('company', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='company', default=None)),
        ('organization', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='organization', default=None)),
        ('target', sgqlc.types.Arg(ID, graphql_name='target', default=None)),
        ('granularity', sgqlc.types.Arg(sgqlc.types.non_null(Granularity), graphql_name='granularity', default=None)),
))
    )
    cockpit_yield_rate = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CockpitTimeseries))), graphql_name='cockpitYieldRate', args=sgqlc.types.ArgDict((
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('company', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='company', default=None)),
        ('organization', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='organization', default=None)),
        ('target', sgqlc.types.Arg(ID, graphql_name='target', default=None)),
        ('granularity', sgqlc.types.Arg(sgqlc.types.non_null(Granularity), graphql_name='granularity', default=None)),
))
    )
    export_cockpit_yield_rate = sgqlc.types.Field('RawFile', graphql_name='exportCockpitYieldRate', args=sgqlc.types.ArgDict((
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('company', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='company', default=None)),
        ('organization', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='organization', default=None)),
        ('target', sgqlc.types.Arg(ID, graphql_name='target', default=None)),
        ('granularity', sgqlc.types.Arg(sgqlc.types.non_null(Granularity), graphql_name='granularity', default=None)),
))
    )
    cockpit_organization_oeerank = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CockpitOrganizationRank))), graphql_name='cockpitOrganizationOEERank', args=sgqlc.types.ArgDict((
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('company', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='company', default=None)),
        ('organization', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='organization', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    cockpit_organization_operation_rate_rank = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CockpitOrganizationRank))), graphql_name='cockpitOrganizationOperationRateRank', args=sgqlc.types.ArgDict((
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('company', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='company', default=None)),
        ('organization', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='organization', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    cockpit_organization_performance_rate_rank = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CockpitOrganizationRank))), graphql_name='cockpitOrganizationPerformanceRateRank', args=sgqlc.types.ArgDict((
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('company', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='company', default=None)),
        ('organization', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='organization', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    cockpit_organization_yield_rate_rank = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CockpitOrganizationRank))), graphql_name='cockpitOrganizationYieldRateRank', args=sgqlc.types.ArgDict((
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('company', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='company', default=None)),
        ('organization', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='organization', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    cockpit_thing_type_oeerank = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CockpitThingTypeRank))), graphql_name='cockpitThingTypeOEERank', args=sgqlc.types.ArgDict((
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('company', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='company', default=None)),
        ('organization', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='organization', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    cockpit_thing_type_operation_rate_rank = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CockpitThingTypeRank))), graphql_name='cockpitThingTypeOperationRateRank', args=sgqlc.types.ArgDict((
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('company', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='company', default=None)),
        ('organization', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='organization', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    cockpit_thing_type_performance_rate_rank = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CockpitThingTypeRank))), graphql_name='cockpitThingTypePerformanceRateRank', args=sgqlc.types.ArgDict((
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('company', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='company', default=None)),
        ('organization', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='organization', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    cockpit_thing_type_yield_rate_rank = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CockpitThingTypeRank))), graphql_name='cockpitThingTypeYieldRateRank', args=sgqlc.types.ArgDict((
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('company', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='company', default=None)),
        ('organization', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='organization', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    cockpit_thing_list = sgqlc.types.Field(sgqlc.types.non_null(CockpitThingList), graphql_name='cockpitThingList', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='company', default=None)),
        ('organization', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='organization', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(CockpitThingListFilter, graphql_name='filter', default=None)),
))
    )
    export_cockpit_thing_list = sgqlc.types.Field('RawFile', graphql_name='exportCockpitThingList', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='company', default=None)),
        ('organization', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='organization', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(CockpitThingListFilter, graphql_name='filter', default=None)),
))
    )
    cockpit_target_list = sgqlc.types.Field(sgqlc.types.non_null(CockpitTargetList), graphql_name='cockpitTargetList', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='company', default=None)),
        ('organization', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='organization', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    cnc_overall = sgqlc.types.Field(sgqlc.types.non_null(CNCOverall), graphql_name='cncOverall', args=sgqlc.types.ArgDict((
        ('thing_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='thingID', default=None)),
))
    )
    cnc_current_alerts = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CNCAlert))), graphql_name='cncCurrentAlerts', args=sgqlc.types.ArgDict((
        ('thing_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='thingID', default=None)),
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
))
    )
    thing_rate_overall = sgqlc.types.Field(CockpitRateOverall, graphql_name='thingRateOverall', args=sgqlc.types.ArgDict((
        ('thing_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='thingID', default=None)),
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(TimerangeFilter), graphql_name='filter', default=None)),
))
    )
    thing_rate = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TimeseriesUnit'))), graphql_name='thingRate', args=sgqlc.types.ArgDict((
        ('thing_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='thingID', default=None)),
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(ThingRateFilter), graphql_name='filter', default=None)),
))
    )
    cnc_alert_overall = sgqlc.types.Field(CNCAlertOverall, graphql_name='cncAlertOverall', args=sgqlc.types.ArgDict((
        ('thing_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='thingID', default=None)),
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(TimerangeFilter), graphql_name='filter', default=None)),
))
    )
    cnc_alert_list = sgqlc.types.Field(CNCAlertList, graphql_name='cncAlertList', args=sgqlc.types.ArgDict((
        ('thing_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='thingID', default=None)),
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(TimerangeFilter), graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
))
    )
    cnc_alerts = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CNCAlertTimeseries))), graphql_name='cncAlerts', args=sgqlc.types.ArgDict((
        ('thing_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='thingID', default=None)),
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(TimerangeFilter), graphql_name='filter', default=None)),
))
    )
    company_production = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ParetoTimeseries)), graphql_name='companyProduction', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='company', default=None)),
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('granularity', sgqlc.types.Arg(sgqlc.types.non_null(Granularity), graphql_name='granularity', default=None)),
))
    )
    company_energy = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ParetoTimeseries)), graphql_name='companyEnergy', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='company', default=None)),
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('granularity', sgqlc.types.Arg(sgqlc.types.non_null(Granularity), graphql_name='granularity', default=None)),
))
    )
    company_overall = sgqlc.types.Field(sgqlc.types.non_null(CompanyOverall), graphql_name='companyOverall', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='company', default=None)),
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
))
    )
    company_bottleneck = sgqlc.types.Field(sgqlc.types.non_null(CompanyThingList), graphql_name='companyBottleneck', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='company', default=None)),
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    company_redundant = sgqlc.types.Field(sgqlc.types.non_null(CompanyThingList), graphql_name='companyRedundant', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='company', default=None)),
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    thing_input_record_summary_list = sgqlc.types.Field(sgqlc.types.non_null('ThingInputRecordSummaryList'), graphql_name='thingInputRecordSummaryList', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('filter', sgqlc.types.Arg(ThingInputRecordSummaryFilterInput, graphql_name='filter', default=None)),
))
    )
    thing_input_record_list = sgqlc.types.Field(sgqlc.types.non_null('ThingInputRecordList'), graphql_name='thingInputRecordList', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('filter', sgqlc.types.Arg(ThingInputRecordFilterInput, graphql_name='filter', default=None)),
))
    )
    spare_part_stock = sgqlc.types.Field('SparePartStock', graphql_name='sparePartStock', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    spare_part_stocks = sgqlc.types.Field(sgqlc.types.non_null('SparePartStockList'), graphql_name='sparePartStocks', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('filter', sgqlc.types.Arg(SparePartStockFilterInput, graphql_name='filter', default=None)),
))
    )
    export_spare_part_stock = sgqlc.types.Field(sgqlc.types.non_null('RawFile'), graphql_name='exportSparePartStock', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(ExportSparePartStockInput, graphql_name='input', default=None)),
))
    )
    thing_inspection = sgqlc.types.Field('ThingInspection', graphql_name='thingInspection', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    thing_inspections = sgqlc.types.Field(sgqlc.types.non_null('ThingInspectionList'), graphql_name='thingInspections', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('filter', sgqlc.types.Arg(ThingInspectionFilterInput, graphql_name='filter', default=None)),
))
    )
    export_thing_inspections = sgqlc.types.Field(sgqlc.types.non_null('RawFile'), graphql_name='exportThingInspections', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(ExportThingInspectionsInput, graphql_name='input', default=None)),
))
    )
    thing_inspection_rule = sgqlc.types.Field('ThingInspectionRule', graphql_name='thingInspectionRule', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    thing_inspection_rules = sgqlc.types.Field(sgqlc.types.non_null('ThingInspectionRuleList'), graphql_name='thingInspectionRules', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('filter', sgqlc.types.Arg(ThingInspectionRuleFilterInput, graphql_name='filter', default=None)),
))
    )
    export_thing_inspection_rules = sgqlc.types.Field(sgqlc.types.non_null('RawFile'), graphql_name='exportThingInspectionRules', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(ExportThingInspectionRulesInput, graphql_name='input', default=None)),
))
    )
    spare_part_receipt = sgqlc.types.Field(sgqlc.types.non_null('SparePartReceipt'), graphql_name='sparePartReceipt', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    spare_part_receipts = sgqlc.types.Field(sgqlc.types.non_null('SparePartReceiptList'), graphql_name='sparePartReceipts', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('filter', sgqlc.types.Arg(SparePartReceiptFilterInput, graphql_name='filter', default=None)),
))
    )
    export_spare_part_receipts = sgqlc.types.Field(sgqlc.types.non_null('RawFile'), graphql_name='exportSparePartReceipts', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(ExportSparePartReceiptInput, graphql_name='input', default=None)),
))
    )
    thing_overview = sgqlc.types.Field(sgqlc.types.non_null('ThingOverview'), graphql_name='thingOverview')
    thing_summary = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CommonSummary))), graphql_name='thingSummary', args=sgqlc.types.ArgDict((
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
))
    )
    spare_part_summary = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CommonSummary))), graphql_name='sparePartSummary', args=sgqlc.types.ArgDict((
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(SparePartSummaryField), graphql_name='name', default=None)),
))
    )
    task_summary = sgqlc.types.Field(sgqlc.types.non_null('TaskSummary'), graphql_name='taskSummary', args=sgqlc.types.ArgDict((
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
))
    )
    export_thing_summary = sgqlc.types.Field(sgqlc.types.non_null('RawFile'), graphql_name='exportThingSummary')
    export_spare_part_summary = sgqlc.types.Field(sgqlc.types.non_null('RawFile'), graphql_name='exportSparePartSummary', args=sgqlc.types.ArgDict((
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
))
    )
    export_task_summary = sgqlc.types.Field(sgqlc.types.non_null('RawFile'), graphql_name='exportTaskSummary', args=sgqlc.types.ArgDict((
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
))
    )
    thing_maintenance_rule = sgqlc.types.Field('ThingMaintenanceRule', graphql_name='thingMaintenanceRule', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(ID, graphql_name='id', default=None)),
))
    )
    thing_maintenance_rules = sgqlc.types.Field(sgqlc.types.non_null('ThingMaintenanceRuleList'), graphql_name='thingMaintenanceRules', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('filter', sgqlc.types.Arg(ThingMaintenanceRuleFilterInput, graphql_name='filter', default=None)),
))
    )
    export_thing_maintenance_rules = sgqlc.types.Field(sgqlc.types.non_null('RawFile'), graphql_name='exportThingMaintenanceRules', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(ExportThingMaintenanceRulesInput, graphql_name='input', default=None)),
))
    )
    thing_maintenance = sgqlc.types.Field('ThingMaintenance', graphql_name='thingMaintenance', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    thing_maintenances = sgqlc.types.Field(sgqlc.types.non_null('ThingMaintenanceList'), graphql_name='thingMaintenances', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('filter', sgqlc.types.Arg(ThingMaintenanceFilterInput, graphql_name='filter', default=None)),
))
    )
    export_thing_maintenances = sgqlc.types.Field(sgqlc.types.non_null('RawFile'), graphql_name='exportThingMaintenances', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(ExportThingMaintenancesInput, graphql_name='input', default=None)),
))
    )
    thing = sgqlc.types.Field('Thing', graphql_name='thing', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    thing_by_qr_code = sgqlc.types.Field('Thing', graphql_name='thingByQrCode', args=sgqlc.types.ArgDict((
        ('qr_code', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='qrCode', default=None)),
))
    )
    things = sgqlc.types.Field(sgqlc.types.non_null('ThingList'), graphql_name='things', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('filter', sgqlc.types.Arg(ThingFilterInput, graphql_name='filter', default=None)),
))
    )
    export_things = sgqlc.types.Field(sgqlc.types.non_null('RawFile'), graphql_name='exportThings', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(ExportThingInput, graphql_name='input', default=None)),
))
    )
    things_template = sgqlc.types.Field(sgqlc.types.non_null('RawFile'), graphql_name='thingsTemplate')
    thing_group_tree = sgqlc.types.Field(sgqlc.types.non_null(JSONString), graphql_name='thingGroupTree')
    thing_group = sgqlc.types.Field(sgqlc.types.non_null('ThingGroup'), graphql_name='thingGroup', args=sgqlc.types.ArgDict((
        ('thing_group', sgqlc.types.Arg(sgqlc.types.non_null(IDInput), graphql_name='thingGroup', default=None)),
))
    )
    thing_group_users = sgqlc.types.Field(sgqlc.types.non_null('UserThingGroupList'), graphql_name='thingGroupUsers', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(ThingGroupUserFilter), graphql_name='filter', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
))
    )
    thing_group_depts = sgqlc.types.Field(sgqlc.types.non_null(DeptThingGroupList), graphql_name='thingGroupDepts', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(ThingGroupDeptFilter), graphql_name='filter', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
))
    )
    dept_user_thing_groups = sgqlc.types.Field(sgqlc.types.non_null('ThingGroupList'), graphql_name='deptUserThingGroups', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(DeptUserThingGroupInputFilter), graphql_name='filter', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
))
    )
    check_alter_department_thing_group = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='checkAlterDepartmentThingGroup', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CheckAlterDepartmentThingGroupInput), graphql_name='input', default=None)),
))
    )
    check_delete_department = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='checkDeleteDepartment', args=sgqlc.types.ArgDict((
        ('department', sgqlc.types.Arg(sgqlc.types.non_null(IDInput), graphql_name='department', default=None)),
))
    )
    form_struct = sgqlc.types.Field(sgqlc.types.non_null(FormStruct), graphql_name='formStruct', args=sgqlc.types.ArgDict((
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
        ('is_draft', sgqlc.types.Arg(Boolean, graphql_name='isDraft', default=None)),
))
    )
    form_structs = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(FormStruct))), graphql_name='formStructs', args=sgqlc.types.ArgDict((
        ('is_draft', sgqlc.types.Arg(Boolean, graphql_name='isDraft', default=None)),
))
    )
    filter_values = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(FieldCandidates))), graphql_name='filterValues', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='form', default=None)),
        ('fields', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(IDInput))), graphql_name='fields', default=None)),
))
    )
    filter_relation_values = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('RelationFieldCandidates'))), graphql_name='filterRelationValues', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='form', default=None)),
        ('ref_col_name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='refColName', default=None)),
        ('shown_col_name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='shownColName', default=None)),
))
    )
    user_relation_filter_values = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('User'))), graphql_name='userRelationFilterValues', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='form', default=None)),
        ('ref_col_name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='refColName', default=None)),
))
    )
    department_relation_filter_values = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Department))), graphql_name='departmentRelationFilterValues', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='form', default=None)),
        ('ref_col_name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='refColName', default=None)),
))
    )
    spare_part = sgqlc.types.Field('SparePart', graphql_name='sparePart', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    spare_parts = sgqlc.types.Field(sgqlc.types.non_null('SparePartList'), graphql_name='spareParts', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('filter', sgqlc.types.Arg(SparePartFilterInput, graphql_name='filter', default=None)),
))
    )
    export_spare_parts = sgqlc.types.Field(sgqlc.types.non_null('RawFile'), graphql_name='exportSpareParts', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(ExportSparePartsInput, graphql_name='input', default=None)),
))
    )
    spare_parts_template = sgqlc.types.Field(sgqlc.types.non_null('RawFile'), graphql_name='sparePartsTemplate')
    thing_repair = sgqlc.types.Field('ThingRepair', graphql_name='thingRepair', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    thing_repairs = sgqlc.types.Field(sgqlc.types.non_null('ThingRepairList'), graphql_name='thingRepairs', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('filter', sgqlc.types.Arg(ThingRepairFilterInput, graphql_name='filter', default=None)),
))
    )
    export_thing_repairs = sgqlc.types.Field(sgqlc.types.non_null('RawFile'), graphql_name='exportThingRepairs', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(ExportThingRepairsInput, graphql_name='input', default=None)),
))
    )
    spare_part_outbound = sgqlc.types.Field('SparePartOutbound', graphql_name='sparePartOutbound', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    spare_part_outbounds = sgqlc.types.Field(sgqlc.types.non_null('SparePartOutboundList'), graphql_name='sparePartOutbounds', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('filter', sgqlc.types.Arg(SparePartOutboundFilterInput, graphql_name='filter', default=None)),
))
    )
    export_spare_part_outbounds = sgqlc.types.Field(sgqlc.types.non_null('RawFile'), graphql_name='exportSparePartOutbounds', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(ExportSparePartOutboundsInput, graphql_name='input', default=None)),
))
    )
    upload_edm_config = sgqlc.types.Field(sgqlc.types.non_null('UploadConfig'), graphql_name='uploadEdmConfig', args=sgqlc.types.ArgDict((
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
))
    )
    upload_edm_configs = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UploadConfig'))), graphql_name='uploadEdmConfigs', args=sgqlc.types.ArgDict((
        ('names', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='names', default=None)),
))
    )
    exists_router_template_name = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='existsRouterTemplateName', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(RouterTemplateFilterInput), graphql_name='filter', default=None)),
))
    )
    device_channel_protocols = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ChannelProtocol))), graphql_name='deviceChannelProtocols', args=sgqlc.types.ArgDict((
        ('model_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='modelId', default=None)),
        ('interface_type', sgqlc.types.Arg(sgqlc.types.non_null(InterfaceType), graphql_name='interfaceType', default=None)),
))
    )
    device_channel_serial_com_ports = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('SerialComPort'))), graphql_name='deviceChannelSerialComPorts', args=sgqlc.types.ArgDict((
        ('model_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='modelId', default=None)),
))
    )
    device_channel_baud_rate = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(BaudRate))), graphql_name='deviceChannelBaudRate', args=sgqlc.types.ArgDict((
        ('model_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='modelId', default=None)),
))
    )
    device_channel_serial_parities = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('SerialParity'))), graphql_name='deviceChannelSerialParities', args=sgqlc.types.ArgDict((
        ('model_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='modelId', default=None)),
))
    )
    device_channel_stop_bit = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('StopBit'))), graphql_name='deviceChannelStopBit', args=sgqlc.types.ArgDict((
        ('model_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='modelId', default=None)),
))
    )
    device_channel_data_bit = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(DataBit))), graphql_name='deviceChannelDataBit', args=sgqlc.types.ArgDict((
        ('model_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='modelId', default=None)),
))
    )
    device_channel_register_types = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('RegisterType'))), graphql_name='deviceChannelRegisterTypes', args=sgqlc.types.ArgDict((
        ('model_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='modelId', default=None)),
        ('protolcol_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='protolcolId', default=None)),
))
    )
    device_channel_register_data_types = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('RegisterDataType'))), graphql_name='deviceChannelRegisterDataTypes', args=sgqlc.types.ArgDict((
        ('model_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='modelId', default=None)),
))
    )
    router_template_configuration_list = sgqlc.types.Field(sgqlc.types.non_null('RouterTemplateConfigurationList'), graphql_name='routerTemplateConfigurationList', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(RouterTemplateConfigurationFilterInput, graphql_name='filter', default=None)),
))
    )
    router_template_configuration = sgqlc.types.Field('RouterTemplateConfiguration', graphql_name='routerTemplateConfiguration', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    device_channel_channel_list = sgqlc.types.Field(sgqlc.types.non_null(DeviceChannelConfigurationList), graphql_name='deviceChannelChannelList', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(DeviceChannelConfigurationFilterInput, graphql_name='filter', default=None)),
))
    )
    device_channel_configuration = sgqlc.types.Field(DeviceChannelConfiguration, graphql_name='deviceChannelConfiguration', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    router_model_list = sgqlc.types.Field(sgqlc.types.non_null('RouterModelList'), graphql_name='routerModelList', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(RouterModelFilterInput, graphql_name='filter', default=None)),
))
    )
    router = sgqlc.types.Field('Router', graphql_name='router', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    router_list = sgqlc.types.Field(sgqlc.types.non_null('RouterList'), graphql_name='routerList', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(RouterFilterInput, graphql_name='filter', default=None)),
))
    )
    export_router = sgqlc.types.Field('RawFile', graphql_name='exportRouter', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(RouterFilterInput, graphql_name='filter', default=None)),
))
    )
    router_summary = sgqlc.types.Field('RouterSummary', graphql_name='routerSummary', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(RouterSummaryFilterInput, graphql_name='filter', default=None)),
))
    )
    exist_router = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='existRouter', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(RouterFilterInput, graphql_name='filter', default=None)),
))
    )
    router_thing_adapter_key_real_time_data_list = sgqlc.types.Field(sgqlc.types.non_null(AdapterKeyRealTimeDataList), graphql_name='routerThingAdapterKeyRealTimeDataList', args=sgqlc.types.ArgDict((
        ('thing_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='thingId', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
))
    )
    router_thing_history_data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(HistoryData))), graphql_name='routerThingHistoryData', args=sgqlc.types.ArgDict((
        ('thing_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='thingId', default=None)),
        ('filter', sgqlc.types.Arg(RouterHistoryFilterInput, graphql_name='filter', default=None)),
))
    )
    router_alarm_type_list = sgqlc.types.Field(sgqlc.types.non_null('RouterAlarmTypeList'), graphql_name='routerAlarmTypeList', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(RouterAlarmTypeFilterInput, graphql_name='filter', default=None)),
))
    )
    router_alarm_level_list = sgqlc.types.Field(sgqlc.types.non_null('RouterAlarmLevelList'), graphql_name='routerAlarmLevelList', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(RouterAlarmLevelFilterInput, graphql_name='filter', default=None)),
))
    )
    router_alarm_record_list = sgqlc.types.Field(sgqlc.types.non_null('RouterAlarmRecrodList'), graphql_name='routerAlarmRecordList', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(RouterAlarmRecordFilterInput, graphql_name='filter', default=None)),
))
    )
    router_alarm_record_summary = sgqlc.types.Field(sgqlc.types.non_null('RouterAlarmRecordSummary'), graphql_name='routerAlarmRecordSummary', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(RouterAlarmRecordSummaryFilter, graphql_name='filter', default=None)),
))
    )
    bi_fdifault = sgqlc.types.Field(sgqlc.types.list_of(BIResult), graphql_name='biFDIFault', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(BIFilterInput, graphql_name='filter', default=None)),
))
    )
    fault = sgqlc.types.Field(sgqlc.types.non_null(Fault), graphql_name='fault', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    fault_list = sgqlc.types.Field(sgqlc.types.non_null(FaultList), graphql_name='faultList', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(FaultFilterInput, graphql_name='filter', default=None)),
))
    )
    fault_issue_summary = sgqlc.types.Field(sgqlc.types.non_null(FaultIssueSummary), graphql_name='faultIssueSummary', args=sgqlc.types.ArgDict((
        ('start', sgqlc.types.Arg(Timestamp, graphql_name='start', default=None)),
        ('end', sgqlc.types.Arg(Timestamp, graphql_name='end', default=None)),
))
    )
    fault_issue = sgqlc.types.Field(sgqlc.types.non_null(FaultIssue), graphql_name='faultIssue', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    fault_issue_list = sgqlc.types.Field(sgqlc.types.non_null(FaultIssueList), graphql_name='faultIssueList', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(FaultIssueFilterInput, graphql_name='filter', default=None)),
))
    )
    fault_reason_list = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(FaultRuleReasonSolutionRelation))), graphql_name='faultReasonList', args=sgqlc.types.ArgDict((
        ('fault_rule_id', sgqlc.types.Arg(sgqlc.types.non_null(IDInput), graphql_name='faultRuleID', default=None)),
))
    )
    fault_rule = sgqlc.types.Field(sgqlc.types.non_null(FaultRule), graphql_name='faultRule', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    fault_rule_list = sgqlc.types.Field(sgqlc.types.non_null(FaultRuleList), graphql_name='faultRuleList', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(FaultRuleFilterInput, graphql_name='filter', default=None)),
))
    )
    fault_solution = sgqlc.types.Field(sgqlc.types.non_null(FaultSolution), graphql_name='faultSolution', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    fault_solution_list = sgqlc.types.Field(sgqlc.types.non_null(FaultSolutionList), graphql_name='faultSolutionList', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(FaultSolutionFilterInput, graphql_name='filter', default=None)),
))
    )
    directory = sgqlc.types.Field(sgqlc.types.non_null(JSONString), graphql_name='directory')
    production_team = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ProductionTeam))), graphql_name='productionTeam')
    production_teammate_list = sgqlc.types.Field(ProductionTeammateList, graphql_name='productionTeammateList', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(ProductionTeammateFilter, graphql_name='filter', default=None)),
))
    )
    production_ticket_list = sgqlc.types.Field(ProductionTicketList, graphql_name='productionTicketList', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(ProductionTicketFilter, graphql_name='filter', default=None)),
))
    )
    production_shift = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ProductionShift)), graphql_name='productionShift')
    production_finish_sub_schedule_data = sgqlc.types.Field(sgqlc.types.non_null(ProductionFinishSubScheduleData), graphql_name='productionFinishSubScheduleData', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(Int, graphql_name='id', default=None)),
))
    )
    production_schedule_list = sgqlc.types.Field(ProductionScheduleList, graphql_name='productionScheduleList', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(ProductionScheduleListFilter, graphql_name='filter', default=None)),
))
    )
    production_sub_schedule_list = sgqlc.types.Field(sgqlc.types.non_null(ProductionSubScheduleList), graphql_name='productionSubScheduleList', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(ProductionSubScheduleFilter, graphql_name='filter', default=None)),
))
    )
    export_production_sub_schedule = sgqlc.types.Field('RawFile', graphql_name='exportProductionSubSchedule', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(ProductionSubScheduleFilter, graphql_name='filter', default=None)),
))
    )
    production_machine_list = sgqlc.types.Field(sgqlc.types.non_null(ProductionMachineList), graphql_name='productionMachineList', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(ProductionMachineListFilter, graphql_name='filter', default=None)),
))
    )
    production_schedule_log = sgqlc.types.Field(ProductionScheduleLogList, graphql_name='productionScheduleLog', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(ProductionScheduleLogFilter, graphql_name='filter', default=None)),
))
    )
    production_teammate_template = sgqlc.types.Field('RawFile', graphql_name='productionTeammateTemplate')
    production_current_thing = sgqlc.types.Field('Thing', graphql_name='productionCurrentThing')
    dmegc_energy_consumption = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(DmegcParetoTimeseries))), graphql_name='dmegcEnergyConsumption', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(DmegcEnergyConsumptionFilterInput), graphql_name='filter', default=None)),
))
    )
    dmegc_production = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(DmegcParetoTimeseries))), graphql_name='dmegcProduction', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(DmegcProductionFilterInput), graphql_name='filter', default=None)),
))
    )
    dmegc_overall = sgqlc.types.Field(DmegcOverall, graphql_name='dmegcOverall', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(DmegcOverallFilterInput), graphql_name='filter', default=None)),
))
    )
    dmegc_alerts = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(JhdvDeviceAlarmMessage))), graphql_name='dmegcAlerts')
    dmegc_oee = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(DmegcTimeseries))), graphql_name='dmegcOEE', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(DmegcOEEFilterInput), graphql_name='filter', default=None)),
))
    )
    dmegc_operation_rate = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(DmegcTimeseries))), graphql_name='dmegcOperationRate', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(DmegcOperationRateFilterInput), graphql_name='filter', default=None)),
))
    )
    dmegc_performance_rate = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(DmegcTimeseries))), graphql_name='dmegcPerformanceRate', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(DmegcPerformanceRateFilterInput), graphql_name='filter', default=None)),
))
    )
    dmegc_yield_rate = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(DmegcTimeseries))), graphql_name='dmegcYieldRate', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(DmegcYieldRateFilterInput), graphql_name='filter', default=None)),
))
    )
    jhdv_industry_list = sgqlc.types.Field(sgqlc.types.non_null(JhdvIndustryList), graphql_name='jhdvIndustryList', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
))
    )
    jhdv_region_statistic_list = sgqlc.types.Field(sgqlc.types.non_null(JhdvRegionStatisticList), graphql_name='jhdvRegionStatisticList', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('filter', sgqlc.types.Arg(JhdvRegionStatisticListFilterInput, graphql_name='filter', default=None)),
))
    )
    jhdv_city_statistic = sgqlc.types.Field(sgqlc.types.non_null(JhdvCityStatistic), graphql_name='jhdvCityStatistic')
    jhdv_device_running_statistic = sgqlc.types.Field(sgqlc.types.non_null(JhdvDeviceRunningStatistic), graphql_name='jhdvDeviceRunningStatistic', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(JhdvDeviceRunningStatisticFilterInput, graphql_name='filter', default=None)),
))
    )
    jhdv_device_index_data_rank = sgqlc.types.Field(sgqlc.types.non_null(JhdvDeviceIndexDataRank), graphql_name='jhdvDeviceIndexDataRank', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(JhdvDeviceIndexDataFilterInput, graphql_name='filter', default=None)),
))
    )
    jhdv_device_index_data_summary = sgqlc.types.Field(sgqlc.types.non_null(JhdvDeviceIndexDataSummary), graphql_name='jhdvDeviceIndexDataSummary', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(JhdvDeviceIndexDataFilterInput, graphql_name='filter', default=None)),
))
    )
    junye_thing_location_map = sgqlc.types.Field(sgqlc.types.non_null(JSONString), graphql_name='junyeThingLocationMap')
    junye_thing_group_location_map = sgqlc.types.Field(sgqlc.types.non_null(JSONString), graphql_name='junyeThingGroupLocationMap')
    junye_business_situation = sgqlc.types.Field(sgqlc.types.non_null(JunyeBusinessSituation), graphql_name='junyeBusinessSituation')
    junye_production_plan = sgqlc.types.Field(sgqlc.types.non_null(JunyeProductionPlan), graphql_name='junyeProductionPlan')
    junye_material_management = sgqlc.types.Field(sgqlc.types.non_null(JunyeMaterialManagement), graphql_name='junyeMaterialManagement')
    junye_thing_status_distribution = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(JunyeThingStatusDistribution))), graphql_name='junyeThingStatusDistribution', args=sgqlc.types.ArgDict((
        ('thing_group_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='thingGroupId', default=None)),
))
    )
    junye_alarm_distribution = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(JunyeAlarmDistribution))), graphql_name='junyeAlarmDistribution', args=sgqlc.types.ArgDict((
        ('thing_group_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='thingGroupId', default=None)),
))
    )
    junye_thing_type_distribution = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(JunyeThingTypeDistribution))), graphql_name='junyeThingTypeDistribution', args=sgqlc.types.ArgDict((
        ('thing_group_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='thingGroupId', default=None)),
))
    )
    junye_daily_energy_consumption_history = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(JunyeEnergyConsumption))), graphql_name='junyeDailyEnergyConsumptionHistory', args=sgqlc.types.ArgDict((
        ('thing_group_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='thingGroupId', default=None)),
        ('day', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='day', default=None)),
))
    )
    junye_current_month_energy_consumption = sgqlc.types.Field(sgqlc.types.non_null(JunyeEnergyConsumption), graphql_name='junyeCurrentMonthEnergyConsumption', args=sgqlc.types.ArgDict((
        ('thing_group_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='thingGroupId', default=None)),
))
    )
    junye_last_month_energy_consumption = sgqlc.types.Field(sgqlc.types.non_null(JunyeEnergyConsumption), graphql_name='junyeLastMonthEnergyConsumption', args=sgqlc.types.ArgDict((
        ('thing_group_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='thingGroupId', default=None)),
))
    )
    thing_type = sgqlc.types.Field('ThingType', graphql_name='thingType', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    thing_types = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ThingType'))), graphql_name='thingTypes', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(String, graphql_name='search', default=None)),
        ('filter', sgqlc.types.Arg(ThingTypeFilterInput, graphql_name='filter', default=None)),
))
    )
    thing_type_list = sgqlc.types.Field(sgqlc.types.non_null('ThingTypeList'), graphql_name='thingTypeList', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('search', sgqlc.types.Arg(String, graphql_name='search', default=None)),
        ('filter', sgqlc.types.Arg(ThingTypeFilterInput, graphql_name='filter', default=None)),
))
    )
    thing_type_code_list = sgqlc.types.Field(sgqlc.types.non_null('ThingTypeCodeList'), graphql_name='thingTypeCodeList', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(ThingTypeCodeFilterInput, graphql_name='filter', default=None)),
))
    )
    thing_mechanism_model = sgqlc.types.Field(sgqlc.types.non_null('ThingMechanismModelList'), graphql_name='thingMechanismModel', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(ThingMechanismModelFilterInput, graphql_name='filter', default=None)),
))
    )
    source_key = sgqlc.types.Field('SourceKey', graphql_name='sourceKey', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    source_key_list = sgqlc.types.Field(sgqlc.types.non_null('SourceKeyList'), graphql_name='sourceKeyList', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('search', sgqlc.types.Arg(String, graphql_name='search', default=None)),
        ('filter', sgqlc.types.Arg(SouceKeyFilterInput, graphql_name='filter', default=None)),
))
    )
    source_model_key_list = sgqlc.types.Field(sgqlc.types.non_null('SourceModelKeyList'), graphql_name='sourceModelKeyList', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('filter', sgqlc.types.Arg(SouceModelKeyFilterInput, graphql_name='filter', default=None)),
))
    )
    adapter_key = sgqlc.types.Field(AdapterKey, graphql_name='adapterKey', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    adapter_key_list = sgqlc.types.Field(sgqlc.types.non_null(AdapterKeyList), graphql_name='adapterKeyList', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('search', sgqlc.types.Arg(String, graphql_name='search', default=None)),
        ('filter', sgqlc.types.Arg(AdapterFilterInput, graphql_name='filter', default=None)),
))
    )
    adapter_model_key_list = sgqlc.types.Field(sgqlc.types.non_null(AdapterModelKeyList), graphql_name='adapterModelKeyList', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('filter', sgqlc.types.Arg(AdapterModelFilterInput, graphql_name='filter', default=None)),
))
    )
    cockpit_key = sgqlc.types.Field(CockpitKey, graphql_name='cockpitKey', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    cockpit_key_list = sgqlc.types.Field(sgqlc.types.non_null(CockpitKeyList), graphql_name='cockpitKeyList', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('search', sgqlc.types.Arg(String, graphql_name='search', default=None)),
        ('filter', sgqlc.types.Arg(CockpitKeyFilterInput, graphql_name='filter', default=None)),
))
    )
    cockpit_aggregation = sgqlc.types.Field(CockpitAggregation, graphql_name='cockpitAggregation', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    cockpit_aggregations = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CockpitAggregation))), graphql_name='cockpitAggregations', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(CockpitAggregationFilterInput, graphql_name='filter', default=None)),
))
    )
    thing_status = sgqlc.types.Field('ThingStatus', graphql_name='thingStatus', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    thing_statuses = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ThingStatus'))), graphql_name='thingStatuses', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(ThingStatusFilterInput, graphql_name='filter', default=None)),
))
    )
    energy_group = sgqlc.types.Field(EnergyGroup, graphql_name='energyGroup', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    energy_group_list = sgqlc.types.Field(sgqlc.types.non_null(EnergyGroupList), graphql_name='energyGroupList', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('search', sgqlc.types.Arg(String, graphql_name='search', default=None)),
        ('filter', sgqlc.types.Arg(EnergyGroupFilterInput, graphql_name='filter', default=None)),
))
    )
    energy_time_distribution = sgqlc.types.Field(EnergyTimeDistribution, graphql_name='energyTimeDistribution')
    worker = sgqlc.types.Field(sgqlc.types.non_null('Worker'), graphql_name='worker', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    workers = sgqlc.types.Field(sgqlc.types.non_null('WorkerList'), graphql_name='workers', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('filter', sgqlc.types.Arg(WorkerFilterInput, graphql_name='filter', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    work_group = sgqlc.types.Field(sgqlc.types.non_null('WorkGroup'), graphql_name='workGroup', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    work_groups = sgqlc.types.Field(sgqlc.types.non_null('WorkGroupList'), graphql_name='workGroups', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('filter', sgqlc.types.Arg(WorkGroupsFilterInput, graphql_name='filter', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    work_shift = sgqlc.types.Field(sgqlc.types.non_null('WorkShift'), graphql_name='workShift', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    work_shifts = sgqlc.types.Field(sgqlc.types.non_null('WorkShiftList'), graphql_name='workShifts', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('filter', sgqlc.types.Arg(WorkShiftFilterInput, graphql_name='filter', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    materials = sgqlc.types.Field(sgqlc.types.non_null(MaterialList), graphql_name='materials', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(MaterialFilterInput, graphql_name='filter', default=None)),
))
    )
    procedures = sgqlc.types.Field(sgqlc.types.non_null(ProcedureList), graphql_name='procedures', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(ProcedureFilterInput, graphql_name='filter', default=None)),
))
    )
    procedure_segment = sgqlc.types.Field(sgqlc.types.non_null(ProcedureSegment), graphql_name='procedureSegment', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    procedure_segments = sgqlc.types.Field(sgqlc.types.non_null(ProcedureSegmentList), graphql_name='procedureSegments', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('filter', sgqlc.types.Arg(ProcedureSegmentFilterInput, graphql_name='filter', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    work_duties = sgqlc.types.Field(sgqlc.types.non_null('WorkDutyList'), graphql_name='workDuties', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(WorkDutyFilterInput), graphql_name='filter', default=None)),
))
    )
    production_process = sgqlc.types.Field(sgqlc.types.non_null(ProductionProcess), graphql_name='productionProcess', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    production_processes = sgqlc.types.Field(sgqlc.types.non_null(ProductionProcessesList), graphql_name='productionProcesses', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(ProcessesFilterInput, graphql_name='filter', default=None)),
))
    )
    bom = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(BomNode))), graphql_name='bom', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    order = sgqlc.types.Field(Order, graphql_name='order', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    orders = sgqlc.types.Field(sgqlc.types.non_null(OrderList), graphql_name='orders', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(OrderFilterInput, graphql_name='filter', default=None)),
))
    )
    production_plans = sgqlc.types.Field(sgqlc.types.non_null(ProductionPlanList), graphql_name='productionPlans', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(ProductionPlanFilerInput, graphql_name='filter', default=None)),
))
    )
    bi_pdmalert = sgqlc.types.Field(sgqlc.types.list_of(BIResult), graphql_name='biPDMAlert', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(BIFilterInput, graphql_name='filter', default=None)),
))
    )
    alert_rules = sgqlc.types.Field(AlertRuleList, graphql_name='alertRules', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('filter', sgqlc.types.Arg(AlertRuleFilter, graphql_name='filter', default=None)),
))
    )
    alert_config = sgqlc.types.Field(AlertConfig, graphql_name='alertConfig')
    alerts = sgqlc.types.Field(AlertList, graphql_name='alerts', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(AlertFilter, graphql_name='filter', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    export_alerts = sgqlc.types.Field('RawFile', graphql_name='exportAlerts', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(AlertFilter, graphql_name='filter', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    sim_summary = sgqlc.types.Field(sgqlc.types.non_null('SimSummary'), graphql_name='simSummary')
    sim = sgqlc.types.Field(sgqlc.types.non_null('Sim'), graphql_name='sim', args=sgqlc.types.ArgDict((
        ('iccid', sgqlc.types.Arg(ID, graphql_name='iccid', default=None)),
))
    )
    sims = sgqlc.types.Field(sgqlc.types.non_null('SimList'), graphql_name='sims', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('filter', sgqlc.types.Arg(SimFilterInput, graphql_name='filter', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    sim_traffic = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('SimTraffic'))), graphql_name='simTraffic', args=sgqlc.types.ArgDict((
        ('iccid', sgqlc.types.Arg(ID, graphql_name='iccid', default=None)),
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
))
    )
    sim_bill = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Bill))), graphql_name='simBill', args=sgqlc.types.ArgDict((
        ('iccid', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='iccid', default=None)),
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
))
    )
    sim_alerts = sgqlc.types.Field(sgqlc.types.non_null('SimAlertList'), graphql_name='simAlerts', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('filter', sgqlc.types.Arg(SimAlertFilterInput, graphql_name='filter', default=None)),
))
    )
    export_sims = sgqlc.types.Field(sgqlc.types.non_null('RawFile'), graphql_name='exportSims', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('filter', sgqlc.types.Arg(SimFilterInput, graphql_name='filter', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    sim_alert_status = sgqlc.types.Field(sgqlc.types.non_null('SimAlertStatus'), graphql_name='simAlertStatus')
    upload_config = sgqlc.types.Field('UploadConfig', graphql_name='uploadConfig', args=sgqlc.types.ArgDict((
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
))
    )
    upload_configs = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('UploadConfig')), graphql_name='uploadConfigs', args=sgqlc.types.ArgDict((
        ('names', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='names', default=None)),
))
    )
    notification_config_list = sgqlc.types.Field(sgqlc.types.non_null(NotificationConfigList), graphql_name='notificationConfigList', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(NotificationConfigFilterInput, graphql_name='filter', default=None)),
))
    )
    notification_config = sgqlc.types.Field(sgqlc.types.non_null(NotificationConfig), graphql_name='notificationConfig', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    notification_list = sgqlc.types.Field(sgqlc.types.non_null(NotificationList), graphql_name='notificationList', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(NotificationFilterInput, graphql_name='filter', default=None)),
))
    )
    notification = sgqlc.types.Field(sgqlc.types.non_null(Notification), graphql_name='notification', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    notification_config_app = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(App)), graphql_name='notificationConfigApp')
    notification_app = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(App)), graphql_name='notificationApp')
    apps = sgqlc.types.Field(sgqlc.types.non_null(AppList), graphql_name='apps', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('filter', sgqlc.types.Arg(AppsFilter, graphql_name='filter', default=None)),
        ('omit', sgqlc.types.Arg(AppsOmit, graphql_name='omit', default=None)),
))
    )
    company_apps = sgqlc.types.Field(sgqlc.types.non_null(AppList), graphql_name='companyApps', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('filter', sgqlc.types.Arg(CompanyAppsFilter, graphql_name='filter', default=None)),
))
    )
    my_company_apps = sgqlc.types.Field(sgqlc.types.non_null(AppList), graphql_name='myCompanyApps', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('filter', sgqlc.types.Arg(MyCompanyAppFilter, graphql_name='filter', default=None)),
))
    )
    my_app_list = sgqlc.types.Field(sgqlc.types.non_null(AppList), graphql_name='myAppList', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('filter', sgqlc.types.Arg(MyAppListFilter, graphql_name='filter', default=None)),
))
    )
    quick_access_app = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(App))), graphql_name='quickAccessApp')
    recent_app = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(App))), graphql_name='recentApp', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='limit', default=None)),
))
    )
    app_config = sgqlc.types.Field(sgqlc.types.non_null(AppConfig), graphql_name='appConfig', args=sgqlc.types.ArgDict((
        ('app_code', sgqlc.types.Arg(String, graphql_name='appCode', default='main')),
))
    )
    bi_issue_issue = sgqlc.types.Field(sgqlc.types.list_of(BIResult), graphql_name='biIssueIssue', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(BIFilterInput, graphql_name='filter', default=None)),
))
    )
    system_log_list = sgqlc.types.Field(sgqlc.types.non_null('SystemLogList'), graphql_name='systemLogList', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(SystemLogFilterInput), graphql_name='filter', default=None)),
))
    )
    system_log_action = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='systemLogAction', args=sgqlc.types.ArgDict((
        ('company_id', sgqlc.types.Arg(ID, graphql_name='companyId', default=None)),
))
    )
    issues = sgqlc.types.Field(IssueList, graphql_name='issues', args=sgqlc.types.ArgDict((
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('filter', sgqlc.types.Arg(IssueListFilter, graphql_name='filter', default=None)),
        ('mine_only', sgqlc.types.Arg(Boolean, graphql_name='mineOnly', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    export_issues = sgqlc.types.Field('RawFile', graphql_name='exportIssues', args=sgqlc.types.ArgDict((
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('filter', sgqlc.types.Arg(IssueListFilter, graphql_name='filter', default=None)),
        ('mine_only', sgqlc.types.Arg(Boolean, graphql_name='mineOnly', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    issue = sgqlc.types.Field(Issue, graphql_name='issue', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(ID, graphql_name='id', default=None)),
))
    )
    market_issue_list = sgqlc.types.Field(sgqlc.types.non_null(MarketIssueList), graphql_name='marketIssueList', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(MarketIssueFilterInput), graphql_name='filter', default=None)),
))
    )
    market_issue = sgqlc.types.Field(sgqlc.types.non_null(MarketIssue), graphql_name='marketIssue', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    market_issue_summary = sgqlc.types.Field(sgqlc.types.non_null(MarketIssueSummary), graphql_name='marketIssueSummary', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(MarketIssueFilterInput), graphql_name='filter', default=None)),
))
    )
    company_exists = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='companyExists', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(companyExistsFilter), graphql_name='filter', default=None)),
))
    )
    company_type_list = sgqlc.types.Field(sgqlc.types.non_null(CompanyTypeList), graphql_name='companyTypeList', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(CompanyTypeFilter, graphql_name='filter', default=None)),
))
    )
    provinces = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Province)), graphql_name='provinces')
    cities = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(City_)), graphql_name='cities', args=sgqlc.types.ArgDict((
        ('province_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='provinceID', default=None)),
))
    )
    counties = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(County_)), graphql_name='counties', args=sgqlc.types.ArgDict((
        ('city_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='cityID', default=None)),
))
    )
    company = sgqlc.types.Field(sgqlc.types.non_null(Company), graphql_name='company', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(ID, graphql_name='id', default=None)),
))
    )
    companies = sgqlc.types.Field(sgqlc.types.non_null(CompanyList), graphql_name='companies', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('filter', sgqlc.types.Arg(CompanyFilter, graphql_name='filter', default=None)),
))
    )
    city_companies = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(City)), graphql_name='cityCompanies')
    type_companies = sgqlc.types.Field(sgqlc.types.non_null('TypeCompaniesList'), graphql_name='typeCompanies', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(CompanyFilter, graphql_name='filter', default=None)),
        ('perm', sgqlc.types.Arg(String, graphql_name='perm', default=None)),
))
    )
    my_company = sgqlc.types.Field(sgqlc.types.non_null(Company), graphql_name='myCompany')
    department_tree = sgqlc.types.Field(sgqlc.types.non_null(JSONString), graphql_name='departmentTree', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(DepartmentTreeFilter, graphql_name='filter', default=None)),
))
    )
    department_list = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Department)), graphql_name='departmentList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(DepartmentListFilter), graphql_name='filter', default=None)),
))
    )
    department_name_same_as_siblings = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='departmentNameSameAsSiblings', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(DepartmentNameSameAsSiblingsFilter), graphql_name='filter', default=None)),
))
    )
    company_bidatasource_list = sgqlc.types.Field(sgqlc.types.non_null(CompanyBIDatasourceList), graphql_name='companyBIDatasourceList', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('filter', sgqlc.types.Arg(CompanyBIDatasourceFilter, graphql_name='filter', default=None)),
))
    )
    company_bidatasource_tree = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(AppBIDatasourceList)), graphql_name='companyBIDatasourceTree', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(CompanyBIDatasourceFilter, graphql_name='filter', default=None)),
))
    )
    workbench = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('WorkbenchCard'))), graphql_name='workbench')
    workbench_card_field = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='workbenchCardField', args=sgqlc.types.ArgDict((
        ('type', sgqlc.types.Arg(sgqlc.types.non_null(WorkbenchType), graphql_name='type', default=None)),
))
    )
    workbench_card_option = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(WorkbenchType))), graphql_name='workbenchCardOption')
    market_solution_list = sgqlc.types.Field(sgqlc.types.non_null(MarketSolutionList), graphql_name='marketSolutionList', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(MarketSolutionFilterInput, graphql_name='filter', default=None)),
))
    )
    market_solution = sgqlc.types.Field(sgqlc.types.non_null(MarketSolution), graphql_name='marketSolution', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    market_solution_summary = sgqlc.types.Field(sgqlc.types.non_null(MarketSolutionSummary), graphql_name='marketSolutionSummary')
    role_list = sgqlc.types.Field(sgqlc.types.non_null('RoleList'), graphql_name='roleList', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(RoleFilterInput, graphql_name='filter', default=None)),
))
    )
    permission_tree = sgqlc.types.Field(sgqlc.types.non_null(JSON), graphql_name='permissionTree', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(PermissionTreeFilterInput, graphql_name='filter', default=None)),
))
    )
    role_exists = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='roleExists', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(RoleExistsFilterInput, graphql_name='filter', default=None)),
))
    )
    market_app_list = sgqlc.types.Field(sgqlc.types.non_null(MarketAppList), graphql_name='marketAppList', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('filter', sgqlc.types.Arg(MarketAppFilterInput, graphql_name='filter', default=None)),
))
    )
    market_app = sgqlc.types.Field(sgqlc.types.non_null(MarketApp), graphql_name='marketApp', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    market_app_summary = sgqlc.types.Field(sgqlc.types.non_null(MarketAppSummary), graphql_name='marketAppSummary')
    account_exists = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='accountExists', args=sgqlc.types.ArgDict((
        ('account', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='account', default=None)),
))
    )
    me = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='me')
    company_admin_users = sgqlc.types.Field(sgqlc.types.non_null('UserList'), graphql_name='companyAdminUsers', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('filter', sgqlc.types.Arg(CompanyAdminUsersFilter, graphql_name='filter', default=None)),
))
    )
    platform_admin_users = sgqlc.types.Field(sgqlc.types.non_null('UserList'), graphql_name='platformAdminUsers', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
))
    )
    users = sgqlc.types.Field(sgqlc.types.non_null('UserList'), graphql_name='users', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('filter', sgqlc.types.Arg(UserListFilter, graphql_name='filter', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    platform_user_list = sgqlc.types.Field(sgqlc.types.non_null('UserList'), graphql_name='platformUserList', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('filter', sgqlc.types.Arg(PlatformUserListFilter, graphql_name='filter', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    user = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='user', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    user_template = sgqlc.types.Field(sgqlc.types.non_null('RawFile'), graphql_name='userTemplate')
    export_user = sgqlc.types.Field(sgqlc.types.non_null('RawFile'), graphql_name='exportUser', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(ExportUserInput, graphql_name='input', default=None)),
))
    )
    support_users = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('User')), graphql_name='supportUsers')


class RangeData(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('total', 'detail')
    total = sgqlc.types.Field('ThingData', graphql_name='total')
    detail = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('ThingData')), graphql_name='detail')


class RawData(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'timestamp', 'data', 'tag', 'thing_id', 'company_id')
    id = sgqlc.types.Field(ID, graphql_name='id')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='timestamp')
    data = sgqlc.types.Field(JSONString, graphql_name='data')
    tag = sgqlc.types.Field(String, graphql_name='tag')
    thing_id = sgqlc.types.Field(ID, graphql_name='thingID')
    company_id = sgqlc.types.Field(ID, graphql_name='companyID')


class RawDataList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(RawData)), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class RawFile(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'name')
    data = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='data')
    name = sgqlc.types.Field(String, graphql_name='name')


class RecruitFaculty(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'stu_class')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    stu_class = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('RecruitStuClass')), graphql_name='stuClass')


class RecruitJob(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'serial_number', 'title', 'company', 'description', 'requirement', 'recruit_number', 'salary_start', 'salary_end', 'welfare', 'remark', 'expired_at', 'status', 'reject_reason', 'signed_number', 'admitted_number')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    serial_number = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='serialNumber')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    company = sgqlc.types.Field(sgqlc.types.non_null(IDName), graphql_name='company')
    description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='description')
    requirement = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='requirement')
    recruit_number = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='recruitNumber')
    salary_start = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='salaryStart')
    salary_end = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='salaryEnd')
    welfare = sgqlc.types.Field(String, graphql_name='welfare')
    remark = sgqlc.types.Field(String, graphql_name='remark')
    expired_at = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='expiredAt')
    status = sgqlc.types.Field(sgqlc.types.non_null(RecruitJobStatus), graphql_name='status')
    reject_reason = sgqlc.types.Field(String, graphql_name='rejectReason')
    signed_number = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='signedNumber')
    admitted_number = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='admittedNumber')


class RecruitJobList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(RecruitJob))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class RecruitJobOverview(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('auditing', 'published', 'rejected', 'company_number')
    auditing = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='auditing')
    published = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='published')
    rejected = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='rejected')
    company_number = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='companyNumber')


class RecruitJobSignRecord(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'student', 'status')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    student = sgqlc.types.Field(sgqlc.types.non_null('RecruitStudent'), graphql_name='student')
    status = sgqlc.types.Field(sgqlc.types.non_null(RecruitJobSignStatus), graphql_name='status')


class RecruitJobSignRecordList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(RecruitJobSignRecord))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class RecruitStuClass(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class RecruitStudent(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'gender', 'stu_no', 'stu_class', 'faculty', 'sign_status', 'job', 'company', 'is_looking_job', 'work', 'identity', 'phone')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    gender = sgqlc.types.Field(sgqlc.types.non_null(Gender), graphql_name='gender')
    stu_no = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='stuNo')
    stu_class = sgqlc.types.Field(sgqlc.types.non_null(IDName), graphql_name='stuClass')
    faculty = sgqlc.types.Field(sgqlc.types.non_null(IDName), graphql_name='faculty')
    sign_status = sgqlc.types.Field(sgqlc.types.non_null(RecruitStudentStatus), graphql_name='signStatus')
    job = sgqlc.types.Field(IDName, graphql_name='job')
    company = sgqlc.types.Field(IDName, graphql_name='company')
    is_looking_job = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isLookingJob')
    work = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='work')
    identity = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='identity')
    phone = sgqlc.types.Field(String, graphql_name='phone')


class RecruitStudentList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(RecruitStudent))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class RecruitStudentOverview(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('not_sign', 'admitted', 'pending')
    not_sign = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='notSign')
    admitted = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='admitted')
    pending = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='pending')


class RefField(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('col_name', 'title')
    col_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='colName')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')


class RegisterDataType(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'value')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    value = sgqlc.types.Field(String, graphql_name='value')


class RegisterType(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'value')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    value = sgqlc.types.Field(String, graphql_name='value')


class RelationFieldCandidates(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'value')
    id = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='id')
    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='value')


class Role(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'permissions', 'desc', 'updated_at', 'created_at', 'app')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    permissions = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Permission))), graphql_name='permissions')
    desc = sgqlc.types.Field(String, graphql_name='desc')
    updated_at = sgqlc.types.Field(Timestamp, graphql_name='updatedAt')
    created_at = sgqlc.types.Field(Timestamp, graphql_name='createdAt')
    app = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(App)), graphql_name='app')


class RoleList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Role))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class Router(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'code', 'client_id', 'model', 'alarm_rules', 'status', 'status_duration', 'thing_status', 'latest_data_at', 'images', 'detail_things', 'desc', 'location', 'contact', 'phone', 'purchased_at', 'activated_at', 'years_of_maintenance', 'configuration_status', 'last_update_at')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    client_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='clientId')
    model = sgqlc.types.Field(sgqlc.types.non_null('RouterModel'), graphql_name='model')
    alarm_rules = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('RouterAlarmRule'))), graphql_name='alarmRules')
    status = sgqlc.types.Field(sgqlc.types.non_null(RouterStatus), graphql_name='status')
    status_duration = sgqlc.types.Field(Int, graphql_name='statusDuration')
    thing_status = sgqlc.types.Field(sgqlc.types.non_null(RouterThingStatus), graphql_name='thingStatus')
    latest_data_at = sgqlc.types.Field(Timestamp, graphql_name='latestDataAt')
    images = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(File)), graphql_name='images')
    detail_things = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('RouterDetailThing')), graphql_name='detailThings')
    desc = sgqlc.types.Field(String, graphql_name='desc')
    location = sgqlc.types.Field(String, graphql_name='location')
    contact = sgqlc.types.Field(String, graphql_name='contact')
    phone = sgqlc.types.Field(String, graphql_name='phone')
    purchased_at = sgqlc.types.Field(Timestamp, graphql_name='purchasedAt')
    activated_at = sgqlc.types.Field(Timestamp, graphql_name='activatedAt')
    years_of_maintenance = sgqlc.types.Field(Int, graphql_name='yearsOfMaintenance')
    configuration_status = sgqlc.types.Field(RouterConfigurationStatus, graphql_name='configurationStatus')
    last_update_at = sgqlc.types.Field(Timestamp, graphql_name='lastUpdateAt')


class RouterAlarmLevel(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'weight')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    weight = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='weight')


class RouterAlarmLevelList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(RouterAlarmLevel))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class RouterAlarmRecordLevelSummary(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('level', 'count')
    level = sgqlc.types.Field(sgqlc.types.non_null(RouterAlarmLevel), graphql_name='level')
    count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='count')


class RouterAlarmRecordSummary(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('levels_summary',)
    levels_summary = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(RouterAlarmRecordLevelSummary))), graphql_name='levelsSummary')


class RouterAlarmRecrod(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'level_name', 'content', 'router_id', 'router_name', 'router_location', 'suggestion', 'occurred_at', 'is_restored', 'restored_at', 'is_ack', 'ack_at')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    level_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='levelName')
    content = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='content')
    router_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='routerId')
    router_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='routerName')
    router_location = sgqlc.types.Field(String, graphql_name='routerLocation')
    suggestion = sgqlc.types.Field(String, graphql_name='suggestion')
    occurred_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='occurredAt')
    is_restored = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isRestored')
    restored_at = sgqlc.types.Field(Timestamp, graphql_name='restoredAt')
    is_ack = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isAck')
    ack_at = sgqlc.types.Field(Timestamp, graphql_name='ackAt')


class RouterAlarmRecrodList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(RouterAlarmRecrod))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class RouterAlarmRule(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('enabled', 'type', 'level', 'threshold', 'suggestion')
    enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='enabled')
    type = sgqlc.types.Field(sgqlc.types.non_null('RouterAlarmType'), graphql_name='type')
    level = sgqlc.types.Field(sgqlc.types.non_null(RouterAlarmLevel), graphql_name='level')
    threshold = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='threshold')
    suggestion = sgqlc.types.Field(String, graphql_name='suggestion')


class RouterAlarmType(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class RouterAlarmTypeList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(RouterAlarmType))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class RouterDetailThing(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('thing', 'status')
    thing = sgqlc.types.Field(sgqlc.types.non_null('Thing'), graphql_name='thing')
    status = sgqlc.types.Field(sgqlc.types.non_null(RouterThingStatus), graphql_name='status')


class RouterList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Router))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class RouterModel(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'manufacturer')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    manufacturer = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='manufacturer')


class RouterModelList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(RouterModel))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class RouterSummary(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('total_count', 'online_count', 'offline_count')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    online_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='OnlineCount')
    offline_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='OfflineCount')


class RouterTemplateConfiguration(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'model', 'interface_type_names', 'collects')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    model = sgqlc.types.Field(sgqlc.types.non_null(RouterModel), graphql_name='model')
    interface_type_names = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='interfaceTypeNames')
    collects = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CollectConfiguration))), graphql_name='collects')


class RouterTemplateConfigurationList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(RouterTemplateConfiguration))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class RouterType(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'value')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='value')


class SerialChannel(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('slave_id', 'com_port', 'parity', 'baud', 'data_bit', 'stop_bit')
    slave_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='slaveId')
    com_port = sgqlc.types.Field(sgqlc.types.non_null('SerialComPort'), graphql_name='comPort')
    parity = sgqlc.types.Field(sgqlc.types.non_null('SerialParity'), graphql_name='parity')
    baud = sgqlc.types.Field(sgqlc.types.non_null(BaudRate), graphql_name='baud')
    data_bit = sgqlc.types.Field(sgqlc.types.non_null(DataBit), graphql_name='dataBit')
    stop_bit = sgqlc.types.Field(sgqlc.types.non_null('StopBit'), graphql_name='stopBit')


class SerialComPort(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'value')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    value = sgqlc.types.Field(String, graphql_name='value')


class SerialParity(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'value')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    value = sgqlc.types.Field(String, graphql_name='value')


class Sim(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('iccid', 'msisdn', 'imsi', 'life_cycle', 'create_date', 'active_date', 'monthly_traffic', 'total_traffic', 'os_status_desc', 'card_type', 'alert_threshold', 'monthly_traffic_usages', 'balance', 'prod_fee_info', 'left_ratio')
    iccid = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='iccid')
    msisdn = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='msisdn')
    imsi = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='imsi')
    life_cycle = sgqlc.types.Field(sgqlc.types.non_null(LifeCycle), graphql_name='lifeCycle')
    create_date = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='createDate')
    active_date = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='activeDate')
    monthly_traffic = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='monthlyTraffic')
    total_traffic = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='totalTraffic')
    os_status_desc = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='osStatusDesc')
    card_type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cardType')
    alert_threshold = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='alertThreshold')
    monthly_traffic_usages = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(MonthlyTrafficUsage))), graphql_name='monthlyTrafficUsages')
    balance = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='balance')
    prod_fee_info = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ProdFeeInfoItem))), graphql_name='prodFeeInfo')
    left_ratio = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='leftRatio')


class SimAlert(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('msisdn', 'iccid', 'imsi', 'date', 'alert_threshold')
    msisdn = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='msisdn')
    iccid = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='iccid')
    imsi = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='imsi')
    date = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='date')
    alert_threshold = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='alertThreshold')


class SimAlertList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('total_count', 'data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(SimAlert))), graphql_name='data')


class SimAlertStatus(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('status',)
    status = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='status')


class SimList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('total_count', 'data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Sim))), graphql_name='data')


class SimSummary(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('total', 'normal_count', 'test_count', 'silent_count', 'other_count', 'alert_count')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')
    normal_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='normalCount')
    test_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='testCount')
    silent_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='silentCount')
    other_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='otherCount')
    alert_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='alertCount')


class SimTraffic(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('month', 'traffic')
    month = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='month')
    traffic = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='traffic')


class SocialPerson(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'gender', 'is_looking_job', 'identity', 'register_status', 'phone', 'created_at', 'work')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    gender = sgqlc.types.Field(sgqlc.types.non_null(Gender), graphql_name='gender')
    is_looking_job = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isLookingJob')
    identity = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='identity')
    register_status = sgqlc.types.Field(sgqlc.types.non_null(RegisterStatus), graphql_name='registerStatus')
    phone = sgqlc.types.Field(String, graphql_name='phone')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='createdAt')
    work = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='work')


class SocialPersonAccountSummary(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('total_count', 'approved_count', 'rejected_count', 'pending_count')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    approved_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='approvedCount')
    rejected_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='rejectedCount')
    pending_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='pendingCount')


class SocialPersonList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(SocialPerson)), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class SourceKey(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'thing_type', 'key', 'desc')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    thing_type = sgqlc.types.Field(sgqlc.types.non_null('ThingType'), graphql_name='thingType')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    desc = sgqlc.types.Field(String, graphql_name='desc')


class SourceKeyList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(SourceKey))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class SourceModelKey(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('thing_mechanism_model', 'key', 'desc')
    thing_mechanism_model = sgqlc.types.Field(sgqlc.types.non_null('ThingMechanismModel'), graphql_name='thingMechanismModel')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    desc = sgqlc.types.Field(String, graphql_name='desc')


class SourceModelKeyList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(SourceModelKey))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class SparePart(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'sap', 'name', 'brand', 'manufacturer', 'type', 'distributor', 'price', 'images', 'attachments', 'things', 'addition')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    sap = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='sap')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    brand = sgqlc.types.Field(String, graphql_name='brand')
    manufacturer = sgqlc.types.Field(String, graphql_name='manufacturer')
    type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='type')
    distributor = sgqlc.types.Field(String, graphql_name='distributor')
    price = sgqlc.types.Field(Float, graphql_name='price')
    images = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(File)), graphql_name='images')
    attachments = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(File)), graphql_name='attachments')
    things = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('Thing')), graphql_name='things')
    addition = sgqlc.types.Field(JSONString, graphql_name='addition')


class SparePartList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(SparePart)), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class SparePartOutbound(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'code', 'operator', 'time', 'shelf', 'factory', 'status', 'reason', 'thing_repair', 'thing_maintenance', 'thing_inspection', 'details', 'addition')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    operator = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='operator')
    time = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='time')
    shelf = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='shelf')
    factory = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='factory')
    status = sgqlc.types.Field(sgqlc.types.non_null(SparePartOutboundStatus), graphql_name='status')
    reason = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='reason')
    thing_repair = sgqlc.types.Field('ThingRepair', graphql_name='thingRepair')
    thing_maintenance = sgqlc.types.Field('ThingMaintenance', graphql_name='thingMaintenance')
    thing_inspection = sgqlc.types.Field('ThingInspection', graphql_name='thingInspection')
    details = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('SparePartOutboundDetail'))), graphql_name='details')
    addition = sgqlc.types.Field(JSONString, graphql_name='addition')


class SparePartOutboundDetail(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('spare_part', 'stock', 'number', 'actual_number', 'reason', 'total_price')
    spare_part = sgqlc.types.Field(sgqlc.types.non_null(SparePart), graphql_name='sparePart')
    stock = sgqlc.types.Field(sgqlc.types.non_null('SparePartStock'), graphql_name='stock')
    number = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='number')
    actual_number = sgqlc.types.Field(Int, graphql_name='actual_number')
    reason = sgqlc.types.Field(String, graphql_name='reason')
    total_price = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='totalPrice')


class SparePartOutboundList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(SparePartOutbound)), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class SparePartReceipt(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'code', 'shelf', 'factory', 'operator', 'time', 'details', 'addition')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    shelf = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='shelf')
    factory = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='factory')
    operator = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='operator')
    time = sgqlc.types.Field(Timestamp, graphql_name='time')
    details = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('SparePartReceiptDetail'))), graphql_name='details')
    addition = sgqlc.types.Field(JSONString, graphql_name='addition')


class SparePartReceiptDetail(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('spare_part', 'number')
    spare_part = sgqlc.types.Field(sgqlc.types.non_null(SparePart), graphql_name='sparePart')
    number = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='number')


class SparePartReceiptList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(SparePartReceipt)), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class SparePartStock(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'spare_part', 'shelf', 'factory', 'inventory')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    spare_part = sgqlc.types.Field(SparePart, graphql_name='sparePart')
    shelf = sgqlc.types.Field(String, graphql_name='shelf')
    factory = sgqlc.types.Field(String, graphql_name='factory')
    inventory = sgqlc.types.Field(Int, graphql_name='inventory')


class SparePartStockList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(SparePartStock)), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class StatusDistribution(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('operation', 'standby', 'shutdown')
    operation = sgqlc.types.Field(Int, graphql_name='operation')
    standby = sgqlc.types.Field(Int, graphql_name='standby')
    shutdown = sgqlc.types.Field(Int, graphql_name='shutdown')


class StopBit(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'value')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    value = sgqlc.types.Field(Int, graphql_name='value')


class SystemLog(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'user', 'timestamp', 'action', 'resource', 'app')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    user = sgqlc.types.Field('User', graphql_name='user')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='timestamp')
    action = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='action')
    resource = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='resource')
    app = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='app')


class SystemLogList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(SystemLog))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class TaskDetail(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('total', 'finished', 'rate')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')
    finished = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='finished')
    rate = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='rate')


class TaskSummary(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('thing_repair', 'thing_maintenance', 'thing_inspection')
    thing_repair = sgqlc.types.Field(sgqlc.types.non_null(TaskDetail), graphql_name='thingRepair')
    thing_maintenance = sgqlc.types.Field(sgqlc.types.non_null(TaskDetail), graphql_name='thingMaintenance')
    thing_inspection = sgqlc.types.Field(sgqlc.types.non_null(TaskDetail), graphql_name='thingInspection')


class Thing(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'code', 'sap', 'name', 'model', 'desc', 'manufacturer', 'distributor', 'purchased_at', 'activated_at', 'purchased_price', 'years_of_use', 'used_year', 'predict_residual_rate', 'depreciation_rate', 'category', 'factory', 'purpose', 'repair_contacts', 'using_status', 'qr_code', 'addition', 'images', 'spare_parts', 'attachments', 'thing_group', 'access_key', 'organization', 'type', 'energy_group', 'company_id', 'updated_at', 'status', 'junye_type', 'junye_metric_data', 'junye_runtime', 'junye_product', 'junye_production_time')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    sap = sgqlc.types.Field(String, graphql_name='sap')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    model = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='model')
    desc = sgqlc.types.Field(String, graphql_name='desc')
    manufacturer = sgqlc.types.Field(String, graphql_name='manufacturer')
    distributor = sgqlc.types.Field(String, graphql_name='distributor')
    purchased_at = sgqlc.types.Field(Timestamp, graphql_name='purchasedAt')
    activated_at = sgqlc.types.Field(Timestamp, graphql_name='activatedAt')
    purchased_price = sgqlc.types.Field(Float, graphql_name='purchasedPrice')
    years_of_use = sgqlc.types.Field(Float, graphql_name='yearsOfUse')
    used_year = sgqlc.types.Field(Float, graphql_name='usedYear')
    predict_residual_rate = sgqlc.types.Field(Float, graphql_name='predictResidualRate')
    depreciation_rate = sgqlc.types.Field(Float, graphql_name='depreciationRate')
    category = sgqlc.types.Field(String, graphql_name='category')
    factory = sgqlc.types.Field(String, graphql_name='factory')
    purpose = sgqlc.types.Field(String, graphql_name='purpose')
    repair_contacts = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('User')), graphql_name='repairContacts')
    using_status = sgqlc.types.Field(String, graphql_name='usingStatus')
    qr_code = sgqlc.types.Field(String, graphql_name='qrCode')
    addition = sgqlc.types.Field(JSONString, graphql_name='addition')
    images = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(File)), graphql_name='images')
    spare_parts = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(SparePart)), graphql_name='spareParts')
    attachments = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(File)), graphql_name='attachments')
    thing_group = sgqlc.types.Field('ThingGroup', graphql_name='thingGroup')
    access_key = sgqlc.types.Field(String, graphql_name='accessKey')
    organization = sgqlc.types.Field('ThingOrganization', graphql_name='organization')
    type = sgqlc.types.Field('ThingType', graphql_name='type')
    energy_group = sgqlc.types.Field(EnergyGroup, graphql_name='energyGroup')
    company_id = sgqlc.types.Field(ID, graphql_name='companyID')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='updatedAt')
    status = sgqlc.types.Field(Int, graphql_name='status')
    junye_type = sgqlc.types.Field(sgqlc.types.non_null(JunyeThingType), graphql_name='junyeType')
    junye_metric_data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(JunyeMetricData))), graphql_name='junyeMetricData')
    junye_runtime = sgqlc.types.Field(Int, graphql_name='junyeRuntime')
    junye_product = sgqlc.types.Field(String, graphql_name='junyeProduct')
    junye_production_time = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Timestamp)), graphql_name='junyeProductionTime')


class ThingConfig(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'thing', 'thing_key', 'thing_type', 'thing_organization', 'energy_group', 'extra_data')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    thing = sgqlc.types.Field(Thing, graphql_name='thing')
    thing_key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='thingKey')
    thing_type = sgqlc.types.Field('ThingType', graphql_name='thingType')
    thing_organization = sgqlc.types.Field('ThingOrganization', graphql_name='thingOrganization')
    energy_group = sgqlc.types.Field(EnergyGroup, graphql_name='energyGroup')
    extra_data = sgqlc.types.Field(JSON, graphql_name='extraData')


class ThingConfigList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ThingConfig))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ThingData(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('production', 'target_production', 'electric_quantity', 'time_utilization', 'speed_utilization', 'status_distribution', 'operation_time', 'standby_time', 'shutdown_time', 'shift', 'date')
    production = sgqlc.types.Field(Int, graphql_name='production')
    target_production = sgqlc.types.Field(Int, graphql_name='targetProduction')
    electric_quantity = sgqlc.types.Field(Float, graphql_name='electricQuantity')
    time_utilization = sgqlc.types.Field(Float, graphql_name='timeUtilization')
    speed_utilization = sgqlc.types.Field(Float, graphql_name='speedUtilization')
    status_distribution = sgqlc.types.Field(StatusDistribution, graphql_name='statusDistribution')
    operation_time = sgqlc.types.Field(Int, graphql_name='operationTime')
    standby_time = sgqlc.types.Field(Int, graphql_name='standbyTime')
    shutdown_time = sgqlc.types.Field(Int, graphql_name='shutdownTime')
    shift = sgqlc.types.Field(Int, graphql_name='shift')
    date = sgqlc.types.Field(Timestamp, graphql_name='date')


class ThingGroup(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'parent_id', 'name', 'path_name', 'is_selected')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    parent_id = sgqlc.types.Field(ID, graphql_name='parentID')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    path_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='pathName')
    is_selected = sgqlc.types.Field(Boolean, graphql_name='isSelected')


class ThingGroupList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ThingGroup)), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ThingInputDataIntAttribute(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('value', 'editable')
    value = sgqlc.types.Field(Int, graphql_name='value')
    editable = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='editable')


class ThingInputRecord(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'timestamp', 'thing', 'product_name', 'production', 'production_beat', 'yield_number', 'finished', 'deletable')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='timestamp')
    thing = sgqlc.types.Field(sgqlc.types.non_null(Thing), graphql_name='thing')
    product_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='productName')
    production = sgqlc.types.Field(sgqlc.types.non_null(ThingInputDataIntAttribute), graphql_name='production')
    production_beat = sgqlc.types.Field(sgqlc.types.non_null(ThingInputDataIntAttribute), graphql_name='productionBeat')
    yield_number = sgqlc.types.Field(sgqlc.types.non_null(ThingInputDataIntAttribute), graphql_name='yieldNumber')
    finished = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='finished')
    deletable = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deletable')


class ThingInputRecordList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ThingInputRecord))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ThingInputRecordSummary(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('timestamp', 'finished_count', 'total_count', 'finished')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='timestamp')
    finished_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='finishedCount')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    finished = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='finished')


class ThingInputRecordSummaryList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ThingInputRecordSummary))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ThingInspection(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'code', 'rule', 'status', 'operator', 'period', 'start_at', 'end_at', 'things', 'results', 'thing_repairs', 'addition')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    rule = sgqlc.types.Field(sgqlc.types.non_null('ThingInspectionRule'), graphql_name='rule')
    status = sgqlc.types.Field(sgqlc.types.non_null(ThingInspectionStatus), graphql_name='status')
    operator = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='operator')
    period = sgqlc.types.Field(sgqlc.types.non_null(Period), graphql_name='period')
    start_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='startAt')
    end_at = sgqlc.types.Field(Timestamp, graphql_name='endAt')
    things = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Thing))), graphql_name='things')
    results = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('ThingInspectionDetailResult')), graphql_name='results')
    thing_repairs = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('ThingRepair')), graphql_name='thingRepairs')
    addition = sgqlc.types.Field(JSONString, graphql_name='addition')


class ThingInspectionDetailResult(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('thing_id', 'remarks', 'records')
    thing_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='thingId')
    remarks = sgqlc.types.Field(String, graphql_name='remarks')
    records = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('ThingInspectionRecord')), graphql_name='records')


class ThingInspectionItem(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'sub_items')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    sub_items = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ThingInspectionSubItem'))), graphql_name='subItems')


class ThingInspectionList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ThingInspection)), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ThingInspectionRecord(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('sub_item_id', 'value', 'result', 'images')
    sub_item_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='subItemId')
    value = sgqlc.types.Field(Float, graphql_name='value')
    result = sgqlc.types.Field(ThingInspectionResult, graphql_name='result')
    images = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(File)), graphql_name='images')


class ThingInspectionRule(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'code', 'name', 'items', 'updated_at', 'addition')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    items = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ThingInspectionItem)), graphql_name='items')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='updatedAt')
    addition = sgqlc.types.Field(JSONString, graphql_name='addition')


class ThingInspectionRuleList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ThingInspectionRule)), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ThingInspectionSubItem(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'standard', 'category', 'criteria', 'boundary')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    standard = sgqlc.types.Field(String, graphql_name='standard')
    category = sgqlc.types.Field(sgqlc.types.non_null(ThingInspectionSubItemCategory), graphql_name='category')
    criteria = sgqlc.types.Field(ThingInspectionNumberCriteria, graphql_name='criteria')
    boundary = sgqlc.types.Field('ThingInspectionSubItemBoundaries', graphql_name='boundary')


class ThingInspectionSubItemBoundaries(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('a', 'b')
    a = sgqlc.types.Field(Int, graphql_name='a')
    b = sgqlc.types.Field(Int, graphql_name='b')


class ThingList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Thing)), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ThingMaintenance(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'code', 'thing', 'rule', 'status', 'maintainer', 'start_at', 'period', 'result', 'result_history', 'images', 'remarks', 'spare_part_costs', 'material_costs', 'labor_costs', 'other_costs', 'total_costs', 'end_at', 'thing_repair', 'addition')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    thing = sgqlc.types.Field(sgqlc.types.non_null(Thing), graphql_name='thing')
    rule = sgqlc.types.Field(sgqlc.types.non_null('ThingMaintenanceRule'), graphql_name='rule')
    status = sgqlc.types.Field(sgqlc.types.non_null(ThingMaintenanceStatus), graphql_name='status')
    maintainer = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='maintainer')
    start_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='startAt')
    period = sgqlc.types.Field(sgqlc.types.non_null(Period), graphql_name='period')
    result = sgqlc.types.Field(String, graphql_name='result')
    result_history = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='resultHistory')
    images = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(File)), graphql_name='images')
    remarks = sgqlc.types.Field(String, graphql_name='remarks')
    spare_part_costs = sgqlc.types.Field(Float, graphql_name='sparePartCosts')
    material_costs = sgqlc.types.Field(Float, graphql_name='materialCosts')
    labor_costs = sgqlc.types.Field(Float, graphql_name='laborCosts')
    other_costs = sgqlc.types.Field(Float, graphql_name='otherCosts')
    total_costs = sgqlc.types.Field(Float, graphql_name='totalCosts')
    end_at = sgqlc.types.Field(Timestamp, graphql_name='endAt')
    thing_repair = sgqlc.types.Field('ThingRepair', graphql_name='thingRepair')
    addition = sgqlc.types.Field(JSONString, graphql_name='addition')


class ThingMaintenanceItem(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'content')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    content = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='content')


class ThingMaintenanceList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ThingMaintenance)), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ThingMaintenanceRule(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'code', 'name', 'level', 'frequency', 'items', 'updated_at', 'addition')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    level = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='level')
    frequency = sgqlc.types.Field(String, graphql_name='frequency')
    items = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ThingMaintenanceItem)), graphql_name='items')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='updatedAt')
    addition = sgqlc.types.Field(JSONString, graphql_name='addition')


class ThingMaintenanceRuleList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ThingMaintenanceRule)), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ThingMechanismModel(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'code')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')


class ThingMechanismModelList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ThingMechanismModel))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ThingOrganization(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'parent_id')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='name')
    parent_id = sgqlc.types.Field(ID, graphql_name='parentId')


class ThingOrganizationWithChildren(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'children')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='name')
    children = sgqlc.types.Field(JSON, graphql_name='children')


class ThingOverview(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('thing_total_count', 'thing_total_value', 'thing_repair_to_finished_count', 'thing_inspection_to_finished_count', 'thing_maintenance_to_finished_count', 'spare_part_outbound_to_finished_count')
    thing_total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='thingTotalCount')
    thing_total_value = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='thingTotalValue')
    thing_repair_to_finished_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='thingRepairToFinishedCount')
    thing_inspection_to_finished_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='thingInspectionToFinishedCount')
    thing_maintenance_to_finished_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='thingMaintenanceToFinishedCount')
    spare_part_outbound_to_finished_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='sparePartOutboundToFinishedCount')


class ThingRankDetail(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('thing', 'value')
    thing = sgqlc.types.Field(Thing, graphql_name='thing')
    value = sgqlc.types.Field(Float, graphql_name='value')


class ThingRepair(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'is_draft', 'code', 'thing', 'reported_at', 'report_department', 'fault_images', 'fault_desc', 'assignees', 'workers', 'status', 'result', 'result_history', 'finished_at', 'spare_part_costs', 'material_costs', 'labor_costs', 'other_costs', 'total_costs', 'addition', 'created_by')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    is_draft = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isDraft')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    thing = sgqlc.types.Field(sgqlc.types.non_null(Thing), graphql_name='thing')
    reported_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='reportedAt')
    report_department = sgqlc.types.Field(sgqlc.types.non_null(Department), graphql_name='reportDepartment')
    fault_images = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(File)), graphql_name='faultImages')
    fault_desc = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='faultDesc')
    assignees = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('User'))), graphql_name='assignees')
    workers = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('User'))), graphql_name='workers')
    status = sgqlc.types.Field(ThingRepairStatus, graphql_name='status')
    result = sgqlc.types.Field(String, graphql_name='result')
    result_history = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='resultHistory')
    finished_at = sgqlc.types.Field(Timestamp, graphql_name='finishedAt')
    spare_part_costs = sgqlc.types.Field(Float, graphql_name='sparePartCosts')
    material_costs = sgqlc.types.Field(Float, graphql_name='materialCosts')
    labor_costs = sgqlc.types.Field(Float, graphql_name='laborCosts')
    other_costs = sgqlc.types.Field(Float, graphql_name='otherCosts')
    total_costs = sgqlc.types.Field(Float, graphql_name='totalCosts')
    addition = sgqlc.types.Field(JSONString, graphql_name='addition')
    created_by = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='createdBy')


class ThingRepairList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ThingRepair)), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ThingReport(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('thing', 'energy_group', 'energy_consumption', 'operation_time')
    thing = sgqlc.types.Field(sgqlc.types.non_null(Thing), graphql_name='thing')
    energy_group = sgqlc.types.Field(sgqlc.types.non_null(EnergyGroup), graphql_name='energyGroup')
    energy_consumption = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='energyConsumption')
    operation_time = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='operationTime')


class ThingReportList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ThingReport)), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ThingStatus(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'thing_type', 'value', 'label')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    thing_type = sgqlc.types.Field(sgqlc.types.non_null('ThingType'), graphql_name='thingType')
    value = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='value')
    label = sgqlc.types.Field(String, graphql_name='label')


class ThingStatusData(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('key', 'name', 'time_key', 'time_key_name')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    time_key = sgqlc.types.Field(String, graphql_name='timeKey')
    time_key_name = sgqlc.types.Field(String, graphql_name='timeKeyName')


class ThingTotalReport(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('timestamp', 'thing_total', 'working_thing_total', 'energy_type', 'energy_consumption', 'delta')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='timestamp')
    thing_total = sgqlc.types.Field(Int, graphql_name='thingTotal')
    working_thing_total = sgqlc.types.Field(Int, graphql_name='workingThingTotal')
    energy_type = sgqlc.types.Field(EnergyType, graphql_name='energyType')
    energy_consumption = sgqlc.types.Field(Float, graphql_name='energyConsumption')
    delta = sgqlc.types.Field(Float, graphql_name='delta')


class ThingTotalReportList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ThingTotalReport)), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ThingType(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'code', 'mechanism_model_name', 'desc')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    code = sgqlc.types.Field(String, graphql_name='code')
    mechanism_model_name = sgqlc.types.Field(String, graphql_name='mechanismModelName')
    desc = sgqlc.types.Field(String, graphql_name='desc')


class ThingTypeCode(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'code')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')


class ThingTypeCodeList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ThingTypeCode))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ThingTypeList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ThingType))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ThingsEnergyConsumptionOverall(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('name', 'num', 'operation_total', 'operation_rate', 'power_on_total', 'power_on_rate', 'peak_rate', 'energy_total', 'bottleneck', 'redundant', 'alert')
    name = sgqlc.types.Field(String, graphql_name='name')
    num = sgqlc.types.Field(Int, graphql_name='num')
    operation_total = sgqlc.types.Field(Float, graphql_name='operationTotal')
    operation_rate = sgqlc.types.Field(Float, graphql_name='operationRate')
    power_on_total = sgqlc.types.Field(Float, graphql_name='powerOnTotal')
    power_on_rate = sgqlc.types.Field(Float, graphql_name='powerOnRate')
    peak_rate = sgqlc.types.Field(Float, graphql_name='peakRate')
    energy_total = sgqlc.types.Field(Float, graphql_name='energyTotal')
    bottleneck = sgqlc.types.Field(Int, graphql_name='bottleneck')
    redundant = sgqlc.types.Field(Int, graphql_name='redundant')
    alert = sgqlc.types.Field(Int, graphql_name='alert')


class ThingsOverall(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('total', 'status')
    total = sgqlc.types.Field(Int, graphql_name='total')
    status = sgqlc.types.Field(JSONString, graphql_name='status')


class ThingsRank(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ThingRankDetail)), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class TimeDistribution(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'price')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TimeDistributionData'))), graphql_name='data')
    price = sgqlc.types.Field(Float, graphql_name='price')


class TimeDistributionData(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('start', 'end')
    start = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='start')
    end = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='end')


class TimeseriesUnit(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('timestamp', 'value')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='timestamp')
    value = sgqlc.types.Field(Float, graphql_name='value')


class TotalFee(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('energy_consumption', 'value')
    energy_consumption = sgqlc.types.Field(Float, graphql_name='energyConsumption')
    value = sgqlc.types.Field(Float, graphql_name='value')


class TrainClass(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'faculty', 'stu_count', 'graduate_at', 'class_teacher')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    faculty = sgqlc.types.Field(sgqlc.types.non_null('TrainFaculty'), graphql_name='faculty')
    stu_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='stuCount')
    graduate_at = sgqlc.types.Field(Timestamp, graphql_name='graduateAt')
    class_teacher = sgqlc.types.Field('User', graphql_name='classTeacher')


class TrainClassList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(TrainClass)), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class TrainCompany(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class TrainCourse(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'work_type_id', 'work_type_name', 'work_level_id', 'work_level_name', 'status', 'sign_up_start_at', 'sign_up_end_at', 'introduction', 'current_round', 'sign_up_number', 'training_number', 'approved_number')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    work_type_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='workTypeID')
    work_type_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='workTypeName')
    work_level_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='workLevelId')
    work_level_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='workLevelName')
    status = sgqlc.types.Field(sgqlc.types.non_null(CourseStatus), graphql_name='status')
    sign_up_start_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='signUpStartAt')
    sign_up_end_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='signUpEndAt')
    introduction = sgqlc.types.Field(String, graphql_name='introduction')
    current_round = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='currentRound')
    sign_up_number = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='signUpNumber')
    training_number = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='trainingNumber')
    approved_number = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='approvedNumber')


class TrainCourseList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(TrainCourse)), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class TrainFaculty(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'administrator')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    administrator = sgqlc.types.Field('User', graphql_name='administrator')


class TrainFacultyAdmin(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('User')), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class TrainFacultyList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(TrainFaculty)), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class TrainHumanResource(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('work_type_name', 'work_level_name', 'job_interest_number', 'job_not_interest_number', 'total_number')
    work_type_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='workTypeName')
    work_level_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='workLevelName')
    job_interest_number = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='jobInterestNumber')
    job_not_interest_number = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='jobNotInterestNumber')
    total_number = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalNumber')


class TrainHumanResourceList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(TrainHumanResource))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class TrainSchoolRecruitTask(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'created_at', 'start_at', 'end_at', 'status', 'class_count', 'company_count', 'stu_class', 'company')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='createdAt')
    start_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='startAt')
    end_at = sgqlc.types.Field(Timestamp, graphql_name='endAt')
    status = sgqlc.types.Field(sgqlc.types.non_null(TrainSchoolRecruitTaskStatus), graphql_name='status')
    class_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='classCount')
    company_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='companyCount')
    stu_class = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(RecruitStuClass)), graphql_name='stuClass')
    company = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Company)), graphql_name='company')


class TrainSchoolRecruitTaskList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(TrainSchoolRecruitTask))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class TrainSchoolRecruitTaskRecord(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'student', 'company', 'sign_at', 'sign_status', 'review_status')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    student = sgqlc.types.Field(sgqlc.types.non_null('TrainSchoolStudent'), graphql_name='student')
    company = sgqlc.types.Field(sgqlc.types.non_null(Company), graphql_name='company')
    sign_at = sgqlc.types.Field(Timestamp, graphql_name='signAt')
    sign_status = sgqlc.types.Field(sgqlc.types.non_null(TrainSchoolRecruitTaskRecordStatus), graphql_name='signStatus')
    review_status = sgqlc.types.Field(TrainSchoolRecruitTaskReviewStatus, graphql_name='reviewStatus')


class TrainSchoolRecruitTaskRecordList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(TrainSchoolRecruitTaskRecord))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class TrainSchoolRecruitTaskSummary(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('total_count', 'pending_count', 'in_progress_count', 'end_count')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    pending_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='pendingCount')
    in_progress_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='inProgressCount')
    end_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='endCount')


class TrainSchoolStudent(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'stu_no', 'name', 'gender', 'faculty', 'stu_class', 'identity', 'diploma', 'phone', 'parent_phone', 'parent_name', 'status')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    stu_no = sgqlc.types.Field(String, graphql_name='stuNo')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    gender = sgqlc.types.Field(sgqlc.types.non_null(Gender), graphql_name='gender')
    faculty = sgqlc.types.Field(sgqlc.types.non_null(TrainFaculty), graphql_name='faculty')
    stu_class = sgqlc.types.Field(sgqlc.types.non_null(TrainClass), graphql_name='stuClass')
    identity = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='identity')
    diploma = sgqlc.types.Field(String, graphql_name='diploma')
    phone = sgqlc.types.Field(String, graphql_name='phone')
    parent_phone = sgqlc.types.Field(String, graphql_name='parentPhone')
    parent_name = sgqlc.types.Field(String, graphql_name='parentName')
    status = sgqlc.types.Field(sgqlc.types.non_null(TrainStudentStatus), graphql_name='status')


class TrainSchoolStudentList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(TrainSchoolStudent)), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class TrainSignCourseRecord(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'student', 'social_person', 'sign_up_at', 'course', 'sign_status', 'authentication_status', 'current_round')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    student = sgqlc.types.Field(RecruitStudent, graphql_name='student')
    social_person = sgqlc.types.Field(SocialPerson, graphql_name='socialPerson')
    sign_up_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='signUpAt')
    course = sgqlc.types.Field(sgqlc.types.non_null(TrainCourse), graphql_name='course')
    sign_status = sgqlc.types.Field(sgqlc.types.non_null(CourseSignStatus), graphql_name='signStatus')
    authentication_status = sgqlc.types.Field(sgqlc.types.non_null(AuthenticationStatus), graphql_name='authenticationStatus')
    current_round = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='currentRound')


class TrainSignCourseRecordList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(TrainSignCourseRecord)), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class TrainWork(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(ID, graphql_name='id')


class TrainWorkLevel(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class TrainWorkType(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'has_course')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    has_course = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasCourse')


class TrainWorkTypeList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(TrainWorkType)), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class TypeCompanies(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('type', 'companies')
    type = sgqlc.types.Field(sgqlc.types.non_null(CompanyType), graphql_name='type')
    companies = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Company)), graphql_name='companies')


class TypeCompaniesList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(TypeCompanies)), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class UploadConfig(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('url', 'name')
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class User(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'account', 'name', 'company', 'department', 'password', 'nickname', 'phone', 'email', 'avatar', 'desc', 'type', 'counties', 'role', 'is_active', 'create_time', 'update_time', 'origin', 'is_mine', 'thing_groups')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    account = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='account')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    company = sgqlc.types.Field(Company, graphql_name='company')
    department = sgqlc.types.Field(Department, graphql_name='department')
    password = sgqlc.types.Field(String, graphql_name='password')
    nickname = sgqlc.types.Field(String, graphql_name='nickname')
    phone = sgqlc.types.Field(String, graphql_name='phone')
    email = sgqlc.types.Field(String, graphql_name='email')
    avatar = sgqlc.types.Field(Image, graphql_name='avatar')
    desc = sgqlc.types.Field(String, graphql_name='desc')
    type = sgqlc.types.Field(sgqlc.types.non_null(UserType), graphql_name='type')
    counties = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='counties')
    role = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Role))), graphql_name='role')
    is_active = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isActive')
    create_time = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='createTime')
    update_time = sgqlc.types.Field(Timestamp, graphql_name='updateTime')
    origin = sgqlc.types.Field(UserOrigin, graphql_name='origin')
    is_mine = sgqlc.types.Field(Boolean, graphql_name='isMine')
    thing_groups = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ThingGroup)), graphql_name='thingGroups')


class UserList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(User)), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class UserThingGroupList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('UserThingGroups')), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class UserThingGroups(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('user', 'thing_groups')
    user = sgqlc.types.Field(sgqlc.types.non_null(User), graphql_name='user')
    thing_groups = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ThingGroup)), graphql_name='thingGroups')


class WordCountLimit(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('min', 'max')
    min = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='min')
    max = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='max')


class WorkDuty(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('day', 'shift', 'work_groups')
    day = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='day')
    shift = sgqlc.types.Field(sgqlc.types.non_null('WorkShift'), graphql_name='shift')
    work_groups = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('WorkGroup'))), graphql_name='workGroups')


class WorkDutyList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(WorkDuty))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class WorkGroup(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'status', 'segments', 'leaders', 'members')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    status = sgqlc.types.Field(sgqlc.types.non_null(WorkGroupStatus), graphql_name='status')
    segments = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ProcedureSegment))), graphql_name='segments')
    leaders = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Worker'))), graphql_name='leaders')
    members = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Worker'))), graphql_name='members')


class WorkGroupList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(WorkGroup))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class WorkShift(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'start', 'end')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    start = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='start')
    end = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='end')


class WorkShiftList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(WorkShift))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class WorkbenchCard(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('type', 'field')
    type = sgqlc.types.Field(sgqlc.types.non_null(WorkbenchType), graphql_name='type')
    field = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='field')


class Worker(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'code', 'name', 'gender', 'skill', 'comment')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    gender = sgqlc.types.Field(sgqlc.types.non_null(Gender), graphql_name='gender')
    skill = sgqlc.types.Field(String, graphql_name='skill')
    comment = sgqlc.types.Field(String, graphql_name='comment')


class WorkerList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Worker))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class thingOrganizationList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ThingOrganization))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class AttachmentFieldMeta(sgqlc.types.Type, BaseFieldMeta):
    __schema__ = platform_schema
    __field_names__ = ('formula', 'size_limit', 'count_limit')
    formula = sgqlc.types.Field(JSONString, graphql_name='formula')
    size_limit = sgqlc.types.Field(Int, graphql_name='sizeLimit')
    count_limit = sgqlc.types.Field(Int, graphql_name='countLimit')


class BIFileDataSource(sgqlc.types.Type, BIDataSource):
    __schema__ = platform_schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(ID, graphql_name='id')


class BIPlatformDataSource(sgqlc.types.Type, BIDataSource):
    __schema__ = platform_schema
    __field_names__ = ('id', 'source')
    id = sgqlc.types.Field(ID, graphql_name='id')
    source = sgqlc.types.Field(sgqlc.types.non_null(BIDatasource), graphql_name='source')


class BIPrivateDataSource(sgqlc.types.Type, BIDataSource):
    __schema__ = platform_schema
    __field_names__ = ('id', 'database', 'is_added')
    id = sgqlc.types.Field(ID, graphql_name='id')
    database = sgqlc.types.Field(sgqlc.types.non_null(BIDatabase), graphql_name='database')
    is_added = sgqlc.types.Field(Boolean, graphql_name='isAdded')


class ContactFieldMeta(sgqlc.types.Type, BaseFieldMeta):
    __schema__ = platform_schema
    __field_names__ = ('formula', 'default_contact')
    formula = sgqlc.types.Field(JSONString, graphql_name='formula')
    default_contact = sgqlc.types.Field(String, graphql_name='defaultContact')


class DatetimeFieldMeta(sgqlc.types.Type, BaseFieldMeta):
    __schema__ = platform_schema
    __field_names__ = ('formula', 'default_datetime')
    formula = sgqlc.types.Field(JSONString, graphql_name='formula')
    default_datetime = sgqlc.types.Field(Timestamp, graphql_name='defaultDatetime')


class DescriptionFieldMeta(sgqlc.types.Type, BaseFieldMeta):
    __schema__ = platform_schema
    __field_names__ = ('formula', 'default_desc')
    formula = sgqlc.types.Field(JSONString, graphql_name='formula')
    default_desc = sgqlc.types.Field(String, graphql_name='defaultDesc')


class ImageFieldMeta(sgqlc.types.Type, BaseFieldMeta):
    __schema__ = platform_schema
    __field_names__ = ('formula', 'size_limit', 'count_limit')
    formula = sgqlc.types.Field(JSONString, graphql_name='formula')
    size_limit = sgqlc.types.Field(Int, graphql_name='sizeLimit')
    count_limit = sgqlc.types.Field(Int, graphql_name='countLimit')


class MultiSelectionFieldMeta(sgqlc.types.Type, BaseFieldMeta):
    __schema__ = platform_schema
    __field_names__ = ('default_selection', 'candidates', 'disable_candidates_update')
    default_selection = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='defaultSelection')
    candidates = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='candidates')
    disable_candidates_update = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='disableCandidatesUpdate')


class NumberFieldMeta(sgqlc.types.Type, BaseFieldMeta):
    __schema__ = platform_schema
    __field_names__ = ('formula', 'default_number', 'digit', 'show_money')
    formula = sgqlc.types.Field(JSONString, graphql_name='formula')
    default_number = sgqlc.types.Field(Float, graphql_name='defaultNumber')
    digit = sgqlc.types.Field(Int, graphql_name='digit')
    show_money = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='showMoney')


class SingleSelectionFieldMeta(sgqlc.types.Type, BaseFieldMeta):
    __schema__ = platform_schema
    __field_names__ = ('formula', 'default_selection', 'candidates', 'disable_candidates_update')
    formula = sgqlc.types.Field(JSONString, graphql_name='formula')
    default_selection = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='defaultSelection')
    candidates = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='candidates')
    disable_candidates_update = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='disableCandidatesUpdate')


class TextFieldMeta(sgqlc.types.Type, BaseFieldMeta):
    __schema__ = platform_schema
    __field_names__ = ('formula', 'default_text', 'is_single_line', 'word_count_limit')
    formula = sgqlc.types.Field(JSONString, graphql_name='formula')
    default_text = sgqlc.types.Field(String, graphql_name='defaultText')
    is_single_line = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isSingleLine')
    word_count_limit = sgqlc.types.Field(WordCountLimit, graphql_name='wordCountLimit')



########################################################################
# Unions
########################################################################
class FieldMeta(sgqlc.types.Union):
    __schema__ = platform_schema
    __types__ = (DescriptionFieldMeta, TextFieldMeta, DatetimeFieldMeta, NumberFieldMeta, ContactFieldMeta, AttachmentFieldMeta, ImageFieldMeta, SingleSelectionFieldMeta, MultiSelectionFieldMeta)



########################################################################
# Schema Entry Points
########################################################################
platform_schema.query_type = Query
platform_schema.mutation_type = Mutation
platform_schema.subscription_type = None

