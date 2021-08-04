import sgqlc.types


seely_schema = sgqlc.types.Schema()



########################################################################
# Scalars and Enumerations
########################################################################
class AccessType(sgqlc.types.Enum):
    __schema__ = seely_schema
    __choices__ = ('FORBIDDEN', 'NORMAL', 'ILLEGAL', 'BLACKLIST', 'MULTI_MATCH', 'HIGH_TEMP', 'LOW_TEMP')


Boolean = sgqlc.types.Boolean

class CalendarType(sgqlc.types.Enum):
    __schema__ = seely_schema
    __choices__ = ('WEEKDAY', 'WEEKEND', 'HOLIDAY')


class Day(sgqlc.types.Enum):
    __schema__ = seely_schema
    __choices__ = ('MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY')


class DeviceStatus(sgqlc.types.Enum):
    __schema__ = seely_schema
    __choices__ = ('ONLINE', 'OFFLINE', 'FAULT')


class DeviceType(sgqlc.types.Enum):
    __schema__ = seely_schema
    __choices__ = ('ANDROID', 'IPC')


class DeviceUsedFor(sgqlc.types.Enum):
    __schema__ = seely_schema
    __choices__ = ('ALL', 'PERSON', 'VEHICLE')


class EventStatus(sgqlc.types.Enum):
    __schema__ = seely_schema
    __choices__ = ('APPROVED', 'WAIT', 'CANCEL', 'CHECK_IN', 'CHECK_OUT', 'CHECK_IN_DELAY', 'REVIEW_DELAY')


class FeedBackType(sgqlc.types.Enum):
    __schema__ = seely_schema
    __choices__ = ('USAGE_PROBLEM', 'BUG_REPORT', 'IMPROVE_SUGGEST', 'OTHER')


class FieldType(sgqlc.types.Enum):
    __schema__ = seely_schema
    __choices__ = ('TEXT', 'TIME', 'DATE', 'CHECKBOX', 'SELECT', 'TEXTAREA', 'UPLOAD', 'MULTI_SELECT', 'TAG', 'PASSWORD', 'NUMBER', 'UPLOAD_AUDIO')


Float = sgqlc.types.Float

ID = sgqlc.types.ID

class IDType(sgqlc.types.Enum):
    __schema__ = seely_schema
    __choices__ = ('ID_CARD', 'PASSPORT', 'HK', 'OTHER')


class IdentityType(sgqlc.types.Enum):
    __schema__ = seely_schema
    __choices__ = ('STRANGER', 'ID', 'OTHER', 'TEMP_VISITOR', 'BLACKLIST')


Int = sgqlc.types.Int

class IssueType(sgqlc.types.Enum):
    __schema__ = seely_schema
    __choices__ = ('PROBLEM', 'COOPERATION')


class JSONString(sgqlc.types.Scalar):
    __schema__ = seely_schema


class MemberExport(sgqlc.types.Enum):
    __schema__ = seely_schema
    __choices__ = ('TABLE', 'PHOTO', 'FULL')


class MemberRecordExport(sgqlc.types.Enum):
    __schema__ = seely_schema
    __choices__ = ('TABLE', 'PHOTO')


class MemberStatus(sgqlc.types.Enum):
    __schema__ = seely_schema
    __choices__ = ('NORMAL', 'REMOVED', 'DELETED')


class MessageChannel(sgqlc.types.Enum):
    __schema__ = seely_schema
    __choices__ = ('SITE_MAIL', 'EMAIL')


class NotificationCategory(sgqlc.types.Enum):
    __schema__ = seely_schema
    __choices__ = ('Warning', 'Error', 'Success', 'Message', 'Reminder')


class NotificationType(sgqlc.types.Enum):
    __schema__ = seely_schema
    __choices__ = ('VISIT_WAIT', 'VISIT_NEW', 'VISIT_CANCEL', 'VISIT_ARRIVE', 'BLACKLIST_ALERT', 'ABNORMAL_ACCESS', 'DEVICE_ONLINE', 'DEVICE_OFFLINE', 'MEMBER_UPLOAD_SUCCESS', 'MEMBER_UPLOAD_ERROR', 'PHOTO_UPLOAD_SUCCESS', 'PHOTO_UPLOAD_ERROR', 'MEMBER_DOWNLOAD_SUCCESS', 'MEMBER_DOWNLOAD_ERROR', 'BACKUP_SUCCESS', 'BACKUP_ERROR', 'MEMBER_RECORD_DOWNLOAD_SUCCESS', 'MEMBER_RECORD_DOWNLOAD_ERROR', 'HIGH_TEMP', 'LOW_TEMP')


class OperationAction(sgqlc.types.Enum):
    __schema__ = seely_schema
    __choices__ = ('CREATE', 'DELETE', 'UPDATE', 'INVITE_VISIT', 'APPROVE_VISIT', 'DENY_VISIT', 'CANCEL_VISIT', 'REMOVE', 'DESTROY', 'REVERT', 'BATCH_UPLOAD', 'EXPORT', 'LOGIN', 'UPDATE_PASSWORD', 'ONLINE', 'OFFLINE')


class OperationObject(sgqlc.types.Enum):
    __schema__ = seely_schema
    __choices__ = ('ID', 'OTHER_PERSON', 'ORGANIZATION', 'DEPARTMENT', 'JOB_LEVEL', 'TITLE', 'DEVICE', 'PERSONAL_INFO', 'ACCESS_PERMISSION', 'VEHICLE', 'VISIT_EVENT', 'MEMBER_RECORD', 'VEHICLE_RECORD', 'BLACKLIST')


class OrganizationType(sgqlc.types.Enum):
    __schema__ = seely_schema
    __choices__ = ('COMPANY', 'PROPERTY')


class OrganizationVersion(sgqlc.types.Enum):
    __schema__ = seely_schema
    __choices__ = ('VISITOR', 'ACCESS')


class PermissionAction(sgqlc.types.Enum):
    __schema__ = seely_schema
    __choices__ = ('ADD', 'OVERWRITE')


class ScheduleType(sgqlc.types.Enum):
    __schema__ = seely_schema
    __choices__ = ('WEEK', 'WEEKDAY_WEEKEND', 'CUSTOMIZED')


String = sgqlc.types.String

class SystemModule(sgqlc.types.Enum):
    __schema__ = seely_schema
    __choices__ = ('PERSONAL_CENTER', 'ID_MANAGEMENT', 'ADMIN_CENTER', 'ACCESS_MANAGEMENT', 'ACCESS_LOG', 'VEHICLE_MANAGEMENT', 'VISITOR_MANAGEMENT', 'BLACKLIST')


class Table(sgqlc.types.Enum):
    __schema__ = seely_schema
    __choices__ = ('MEMBER', 'OTHER_PERSON', 'DEVICE', 'VISITOR')


class TagType(sgqlc.types.Enum):
    __schema__ = seely_schema
    __choices__ = ('MEMBER', 'OTHER_PERSON', 'OTHER_PERSON_TYPE', 'VEHICLE', 'DEVICE')


class TaskStatus(sgqlc.types.Enum):
    __schema__ = seely_schema
    __choices__ = ('WAIT', 'RUNNING', 'SUCCEED', 'FAIL')


class TaskType(sgqlc.types.Enum):
    __schema__ = seely_schema
    __choices__ = ('UPLOAD_MEMBER', 'UPLOAD_PHOTO', 'DOWNLOAD_MEMBER', 'BACKUP', 'DOWNLOAD_PHOTO', 'DOWNLOAD_MEMBER_RECORD', 'DOWNLOAD_MEMBER_RECORD_CAPTURE')


class Timestamp(sgqlc.types.Scalar):
    __schema__ = seely_schema


class Upload(sgqlc.types.Scalar):
    __schema__ = seely_schema


class UploadMemberFailReason(sgqlc.types.Enum):
    __schema__ = seely_schema
    __choices__ = ('FORMAT', 'REQUIRED')


class UploadPhotoFailReason(sgqlc.types.Enum):
    __schema__ = seely_schema
    __choices__ = ('ILLEGAL', 'INEXISTENCE')


class VisitReason(sgqlc.types.Enum):
    __schema__ = seely_schema
    __choices__ = ('BUSINESS', 'INTERVIEW', 'EVENT', 'SEMINAR', 'OTHER')


class VisitTotalType(sgqlc.types.Enum):
    __schema__ = seely_schema
    __choices__ = ('PER_DAY', 'PER_HOUR', 'PER_DEVICE', 'PER_DEVICE_TAG', 'PER_PERMISSION', 'PER_DEPARTMENT', 'PER_MONTH')



########################################################################
# Input Objects
########################################################################
class AccessReportFilter(sgqlc.types.Input):
    __schema__ = seely_schema
    __field_names__ = ('start', 'end', 'device', 'permission', 'identity')
    start = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='start')
    end = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='end')
    device = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='device')
    permission = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='permission')
    identity = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IdentityFilter')), graphql_name='identity')


class BlacklistFilterInput(sgqlc.types.Input):
    __schema__ = seely_schema
    __field_names__ = ('search', 'order_by')
    search = sgqlc.types.Field(String, graphql_name='search')
    order_by = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy')


class CreatAttendanceSettingInput(sgqlc.types.Input):
    __schema__ = seely_schema
    __field_names__ = ('arrival', 'leaving', 'over_time', 'over_time_unit', 'leave_time_unit')
    arrival = sgqlc.types.Field(String, graphql_name='arrival')
    leaving = sgqlc.types.Field(String, graphql_name='leaving')
    over_time = sgqlc.types.Field(String, graphql_name='overTime')
    over_time_unit = sgqlc.types.Field(String, graphql_name='overTimeUnit')
    leave_time_unit = sgqlc.types.Field(String, graphql_name='leaveTimeUnit')


class CreateBlacklistInput(sgqlc.types.Input):
    __schema__ = seely_schema
    __field_names__ = ('name', 'photo', 'remark')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    photo = sgqlc.types.Field('PhotoInput', graphql_name='photo')
    remark = sgqlc.types.Field(String, graphql_name='remark')


class CreateCoopConsultationInput(sgqlc.types.Input):
    __schema__ = seely_schema
    __field_names__ = ('contact', 'email', 'phone', 'company', 'detail')
    contact = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='contact')
    email = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='email')
    phone = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='phone')
    company = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='company')
    detail = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='detail')


class CreateEventInput(sgqlc.types.Input):
    __schema__ = seely_schema
    __field_names__ = ('visitors', 'target', 'target_organization', 'notify_target', 'reason', 'book_time', 'deadline', 'derived', 'permissions')
    visitors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('EventVisitorInput'))), graphql_name='visitors')
    target = sgqlc.types.Field('IDInput', graphql_name='target')
    target_organization = sgqlc.types.Field('IDInput', graphql_name='targetOrganization')
    notify_target = sgqlc.types.Field(Boolean, graphql_name='notifyTarget')
    reason = sgqlc.types.Field(VisitReason, graphql_name='reason')
    book_time = sgqlc.types.Field(Timestamp, graphql_name='bookTime')
    deadline = sgqlc.types.Field(Timestamp, graphql_name='deadline')
    derived = sgqlc.types.Field('IDInput', graphql_name='derived')
    permissions = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='permissions')


class CreateFeedbackInput(sgqlc.types.Input):
    __schema__ = seely_schema
    __field_names__ = ('type', 'detail', 'contact_me', 'join_test')
    type = sgqlc.types.Field(sgqlc.types.non_null(FeedBackType), graphql_name='type')
    detail = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='detail')
    contact_me = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='contactMe')
    join_test = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='joinTest')


class CreateMemberInput(sgqlc.types.Input):
    __schema__ = seely_schema
    __field_names__ = ('name', 'email', 'blacklist', 'phone', 'password', 'role', 'photo', 'id_card', 'serial_number', 'door_card_number', 'department', 'job_level', 'title', 'permissions', 'tags', 'greeting', 'display_name', 'probation', 'hire_date', 'correction_time', 'extra_data', 'remark')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    email = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='email')
    blacklist = sgqlc.types.Field(Boolean, graphql_name='blacklist')
    phone = sgqlc.types.Field(String, graphql_name='phone')
    password = sgqlc.types.Field(String, graphql_name='password')
    role = sgqlc.types.Field('IDInput', graphql_name='role')
    photo = sgqlc.types.Field('PhotoInput', graphql_name='photo')
    id_card = sgqlc.types.Field(String, graphql_name='idCard')
    serial_number = sgqlc.types.Field(String, graphql_name='serialNumber')
    door_card_number = sgqlc.types.Field(String, graphql_name='doorCardNumber')
    department = sgqlc.types.Field('IDInput', graphql_name='department')
    job_level = sgqlc.types.Field('IDInput', graphql_name='jobLevel')
    title = sgqlc.types.Field('IDInput', graphql_name='title')
    permissions = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='permissions')
    tags = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='tags')
    greeting = sgqlc.types.Field(String, graphql_name='greeting')
    display_name = sgqlc.types.Field(String, graphql_name='displayName')
    probation = sgqlc.types.Field(Boolean, graphql_name='probation')
    hire_date = sgqlc.types.Field(Timestamp, graphql_name='hireDate')
    correction_time = sgqlc.types.Field(Timestamp, graphql_name='correctionTime')
    extra_data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('FieldValueInput')), graphql_name='extraData')
    remark = sgqlc.types.Field(String, graphql_name='remark')


class CreateMemberPermission(sgqlc.types.Input):
    __schema__ = seely_schema
    __field_names__ = ('name', 'schedule_type', 'schedules', 'departments', 'devices', 'remarks')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    schedule_type = sgqlc.types.Field(sgqlc.types.non_null(ScheduleType), graphql_name='scheduleType')
    schedules = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('PermissionScheduleInput'))), graphql_name='schedules')
    departments = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='departments')
    devices = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='devices')
    remarks = sgqlc.types.Field(String, graphql_name='remarks')


class CreateMemberRecordInput(sgqlc.types.Input):
    __schema__ = seely_schema
    __field_names__ = ('start', 'device_uuid', 'access_type', 'identity_type', 'member', 'visitor', 'capture', 'video', 'end', 'stranger_uid', 'extra')
    start = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='start')
    device_uuid = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='deviceUuid')
    access_type = sgqlc.types.Field(sgqlc.types.non_null(AccessType), graphql_name='accessType')
    identity_type = sgqlc.types.Field(sgqlc.types.non_null(IdentityType), graphql_name='identityType')
    member = sgqlc.types.Field('IDInput', graphql_name='member')
    visitor = sgqlc.types.Field('IDInput', graphql_name='visitor')
    capture = sgqlc.types.Field('IDInput', graphql_name='capture')
    video = sgqlc.types.Field('IDInput', graphql_name='video')
    end = sgqlc.types.Field(Timestamp, graphql_name='end')
    stranger_uid = sgqlc.types.Field(String, graphql_name='strangerUid')
    extra = sgqlc.types.Field(JSONString, graphql_name='extra')


class CreateOtherPersonInput(sgqlc.types.Input):
    __schema__ = seely_schema
    __field_names__ = ('name', 'phone', 'photo', 'type', 'id_card', 'serial_number', 'door_card_number', 'email', 'permissions', 'tags', 'greeting', 'display_name', 'extra_data')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    phone = sgqlc.types.Field(String, graphql_name='phone')
    photo = sgqlc.types.Field('PhotoInput', graphql_name='photo')
    type = sgqlc.types.Field(String, graphql_name='type')
    id_card = sgqlc.types.Field(String, graphql_name='idCard')
    serial_number = sgqlc.types.Field(String, graphql_name='serialNumber')
    door_card_number = sgqlc.types.Field(String, graphql_name='doorCardNumber')
    email = sgqlc.types.Field(String, graphql_name='email')
    permissions = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='permissions')
    tags = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='tags')
    greeting = sgqlc.types.Field(String, graphql_name='greeting')
    display_name = sgqlc.types.Field(String, graphql_name='displayName')
    extra_data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('FieldValueInput')), graphql_name='extraData')


class CreateServerInput(sgqlc.types.Input):
    __schema__ = seely_schema
    __field_names__ = ('name', 'uuid')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    uuid = sgqlc.types.Field(String, graphql_name='uuid')


class CreateUserInput(sgqlc.types.Input):
    __schema__ = seely_schema
    __field_names__ = ('account', 'roles', 'password', 'member', 'to_notify', 'phone', 'language')
    account = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='account')
    roles = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('IDInput'))), graphql_name='roles')
    password = sgqlc.types.Field(String, graphql_name='password')
    member = sgqlc.types.Field('IDInput', graphql_name='member')
    to_notify = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='toNotify')
    phone = sgqlc.types.Field(String, graphql_name='phone')
    language = sgqlc.types.Field(String, graphql_name='language')


class CreateVehicleInput(sgqlc.types.Input):
    __schema__ = seely_schema
    __field_names__ = ('license_plate', 'is_active', 'owner', 'phone', 'tags', 'member')
    license_plate = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='licensePlate')
    is_active = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isActive')
    owner = sgqlc.types.Field(String, graphql_name='owner')
    phone = sgqlc.types.Field(String, graphql_name='phone')
    tags = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='tags')
    member = sgqlc.types.Field('IDInput', graphql_name='member')


class CreateVehicleRecordInput(sgqlc.types.Input):
    __schema__ = seely_schema
    __field_names__ = ('start', 'device_uuid', 'access_type', 'identity_type', 'vehicle', 'end', 'strange_plate')
    start = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='start')
    device_uuid = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='deviceUuid')
    access_type = sgqlc.types.Field(sgqlc.types.non_null(AccessType), graphql_name='accessType')
    identity_type = sgqlc.types.Field(sgqlc.types.non_null(IdentityType), graphql_name='identityType')
    vehicle = sgqlc.types.Field('IDInput', graphql_name='vehicle')
    end = sgqlc.types.Field(Timestamp, graphql_name='end')
    strange_plate = sgqlc.types.Field(String, graphql_name='strangePlate')


class DailyAttendanceFilter(sgqlc.types.Input):
    __schema__ = seely_schema
    __field_names__ = ('member', 'month')
    member = sgqlc.types.Field(sgqlc.types.non_null('IDInput'), graphql_name='member')
    month = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='month')


class DailyAttendanceUpdatedInput(sgqlc.types.Input):
    __schema__ = seely_schema
    __field_names__ = ('f_absence', 'f_annual_leave', 'f_early_leave', 'f_early_leave_min', 'f_funeral_leave', 'f_late', 'f_late_min', 'f_leave_of_absence', 'f_sick_leave', 'f_wedding_leave', 'f_over_hour_of_holiday', 'f_over_hour_of_weekend', 'f_over_hour_of_workingday', 'f_time_in', 'f_time_out', 'remarks')
    f_absence = sgqlc.types.Field(Int, graphql_name='fAbsence')
    f_annual_leave = sgqlc.types.Field(Float, graphql_name='fAnnualLeave')
    f_early_leave = sgqlc.types.Field(Int, graphql_name='fEarlyLeave')
    f_early_leave_min = sgqlc.types.Field(Int, graphql_name='fEarlyLeaveMin')
    f_funeral_leave = sgqlc.types.Field(Float, graphql_name='fFuneralLeave')
    f_late = sgqlc.types.Field(Int, graphql_name='fLate')
    f_late_min = sgqlc.types.Field(Int, graphql_name='fLateMin')
    f_leave_of_absence = sgqlc.types.Field(Float, graphql_name='fLeaveOfAbsence')
    f_sick_leave = sgqlc.types.Field(Float, graphql_name='fSickLeave')
    f_wedding_leave = sgqlc.types.Field(Float, graphql_name='fWeddingLeave')
    f_over_hour_of_holiday = sgqlc.types.Field(Float, graphql_name='fOverHourOfHoliday')
    f_over_hour_of_weekend = sgqlc.types.Field(Float, graphql_name='fOverHourOfWeekend')
    f_over_hour_of_workingday = sgqlc.types.Field(Float, graphql_name='fOverHourOfWorkingday')
    f_time_in = sgqlc.types.Field(String, graphql_name='fTimeIn')
    f_time_out = sgqlc.types.Field(String, graphql_name='fTimeOut')
    remarks = sgqlc.types.Field(String, graphql_name='remarks')


class DeviceFilter(sgqlc.types.Input):
    __schema__ = seely_schema
    __field_names__ = ('search', 'model', 'version', 'type', 'status', 'used_for', 'organization', 'tags')
    search = sgqlc.types.Field(String, graphql_name='search')
    model = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='model')
    version = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='version')
    type = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(DeviceType)), graphql_name='type')
    status = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(DeviceStatus)), graphql_name='status')
    used_for = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(DeviceUsedFor)), graphql_name='usedFor')
    organization = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='organization')
    tags = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='tags')


class EditableBoolInput(sgqlc.types.Input):
    __schema__ = seely_schema
    __field_names__ = ('editable', 'value')
    editable = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='editable')
    value = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='value')


class EventFilter(sgqlc.types.Input):
    __schema__ = seely_schema
    __field_names__ = ('search', 'name', 'start', 'end', 'reason', 'status', 'is_latest', 'group_id', 'my_visitor_only', 'order_by')
    search = sgqlc.types.Field(String, graphql_name='search')
    name = sgqlc.types.Field(String, graphql_name='name')
    start = sgqlc.types.Field(Timestamp, graphql_name='start')
    end = sgqlc.types.Field(Timestamp, graphql_name='end')
    reason = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(VisitReason)), graphql_name='reason')
    status = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(EventStatus)), graphql_name='status')
    is_latest = sgqlc.types.Field(Boolean, graphql_name='isLatest')
    group_id = sgqlc.types.Field(ID, graphql_name='groupId')
    my_visitor_only = sgqlc.types.Field(Boolean, graphql_name='myVisitorOnly')
    order_by = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy')


class EventVisitorInput(sgqlc.types.Input):
    __schema__ = seely_schema
    __field_names__ = ('name', 'phone', 'email', 'id_type', 'id_number', 'door_card_number', 'plate', 'photo', 'company', 'department', 'extra_data', 'is_notify', 'remark', 'allow_invite')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    phone = sgqlc.types.Field(String, graphql_name='phone')
    email = sgqlc.types.Field(String, graphql_name='email')
    id_type = sgqlc.types.Field(IDType, graphql_name='idType')
    id_number = sgqlc.types.Field(String, graphql_name='idNumber')
    door_card_number = sgqlc.types.Field(String, graphql_name='doorCardNumber')
    plate = sgqlc.types.Field(String, graphql_name='plate')
    photo = sgqlc.types.Field('IDInput', graphql_name='photo')
    company = sgqlc.types.Field(String, graphql_name='company')
    department = sgqlc.types.Field(String, graphql_name='department')
    extra_data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('FieldValueInput')), graphql_name='extraData')
    is_notify = sgqlc.types.Field(Boolean, graphql_name='isNotify')
    remark = sgqlc.types.Field(String, graphql_name='remark')
    allow_invite = sgqlc.types.Field(Boolean, graphql_name='allowInvite')


class EventVisitorUpdateInput(sgqlc.types.Input):
    __schema__ = seely_schema
    __field_names__ = ('name', 'phone', 'email', 'id_type', 'id_number', 'door_card_number', 'plate', 'photo', 'company', 'department', 'extra_data', 'remark')
    name = sgqlc.types.Field(String, graphql_name='name')
    phone = sgqlc.types.Field(String, graphql_name='phone')
    email = sgqlc.types.Field(String, graphql_name='email')
    id_type = sgqlc.types.Field(IDType, graphql_name='idType')
    id_number = sgqlc.types.Field(String, graphql_name='idNumber')
    door_card_number = sgqlc.types.Field(String, graphql_name='doorCardNumber')
    plate = sgqlc.types.Field(String, graphql_name='plate')
    photo = sgqlc.types.Field('IDInput', graphql_name='photo')
    company = sgqlc.types.Field(String, graphql_name='company')
    department = sgqlc.types.Field(String, graphql_name='department')
    extra_data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('FieldValueInput')), graphql_name='extraData')
    remark = sgqlc.types.Field(String, graphql_name='remark')


class FieldConfigInput(sgqlc.types.Input):
    __schema__ = seely_schema
    __field_names__ = ('id', 'name', 'enable', 'required', 'visible', 'description')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    enable = sgqlc.types.Field(sgqlc.types.non_null(EditableBoolInput), graphql_name='enable')
    required = sgqlc.types.Field(sgqlc.types.non_null(EditableBoolInput), graphql_name='required')
    visible = sgqlc.types.Field(sgqlc.types.non_null(EditableBoolInput), graphql_name='visible')
    description = sgqlc.types.Field('MultiLanguageItemInput', graphql_name='description')


class FieldValueInput(sgqlc.types.Input):
    __schema__ = seely_schema
    __field_names__ = ('key', 'type', 'checkbox', 'text', 'time', 'date', 'select')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    type = sgqlc.types.Field(sgqlc.types.non_null(FieldType), graphql_name='type')
    checkbox = sgqlc.types.Field(Boolean, graphql_name='checkbox')
    text = sgqlc.types.Field(String, graphql_name='text')
    time = sgqlc.types.Field(Timestamp, graphql_name='time')
    date = sgqlc.types.Field(Timestamp, graphql_name='date')
    select = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='select')


class FormFieldInput(sgqlc.types.Input):
    __schema__ = seely_schema
    __field_names__ = ('name', 'type', 'major', 'custom', 'key', 'select_options')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    type = sgqlc.types.Field(sgqlc.types.non_null(FieldType), graphql_name='type')
    major = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='major')
    custom = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='custom')
    key = sgqlc.types.Field(String, graphql_name='key')
    select_options = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='selectOptions')


class GreetingsInput(sgqlc.types.Input):
    __schema__ = seely_schema
    __field_names__ = ('authorized', 'vip', 'unauthorized', 'illegal_time')
    authorized = sgqlc.types.Field(String, graphql_name='authorized')
    vip = sgqlc.types.Field(String, graphql_name='vip')
    unauthorized = sgqlc.types.Field(String, graphql_name='unauthorized')
    illegal_time = sgqlc.types.Field(String, graphql_name='illegalTime')


class IDInput(sgqlc.types.Input):
    __schema__ = seely_schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class IdentityFilter(sgqlc.types.Input):
    __schema__ = seely_schema
    __field_names__ = ('type', 'department')
    type = sgqlc.types.Field(sgqlc.types.non_null(IdentityType), graphql_name='type')
    department = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='department')


class MemberFilter(sgqlc.types.Input):
    __schema__ = seely_schema
    __field_names__ = ('search', 'role', 'departments', 'titles', 'job_levels', 'branches', 'permissions', 'tags', 'custom_filters', 'order_by', 'is_authorized', 'serial_number', 'email', 'with_blacklist', 'ids')
    search = sgqlc.types.Field(String, graphql_name='search')
    role = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='role')
    departments = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='departments')
    titles = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='titles')
    job_levels = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='jobLevels')
    branches = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='branches')
    permissions = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='permissions')
    tags = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='tags')
    custom_filters = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(FieldValueInput)), graphql_name='customFilters')
    order_by = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy')
    is_authorized = sgqlc.types.Field(Boolean, graphql_name='isAuthorized')
    serial_number = sgqlc.types.Field(String, graphql_name='serialNumber')
    email = sgqlc.types.Field(String, graphql_name='email')
    with_blacklist = sgqlc.types.Field(Boolean, graphql_name='withBlacklist')
    ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='ids')


class MemberPermissionFilter(sgqlc.types.Input):
    __schema__ = seely_schema
    __field_names__ = ('search', 'departments')
    search = sgqlc.types.Field(String, graphql_name='search')
    departments = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='departments')


class MemberPermissionInput(sgqlc.types.Input):
    __schema__ = seely_schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class MemberRecordFilter(sgqlc.types.Input):
    __schema__ = seely_schema
    __field_names__ = ('search', 'device', 'access_type', 'start', 'end', 'identity')
    search = sgqlc.types.Field(String, graphql_name='search')
    device = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='device')
    access_type = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(AccessType)), graphql_name='accessType')
    start = sgqlc.types.Field(Timestamp, graphql_name='start')
    end = sgqlc.types.Field(Timestamp, graphql_name='end')
    identity = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IdentityFilter)), graphql_name='identity')


class MonthlyAttendanceFilter(sgqlc.types.Input):
    __schema__ = seely_schema
    __field_names__ = ('month', 'search', 'order_by')
    month = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='month')
    search = sgqlc.types.Field(String, graphql_name='search')
    order_by = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy')


class MultiLanguageItemInput(sgqlc.types.Input):
    __schema__ = seely_schema
    __field_names__ = ('cn', 'en')
    cn = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cn')
    en = sgqlc.types.Field(String, graphql_name='en')


class NotificationFilter(sgqlc.types.Input):
    __schema__ = seely_schema
    __field_names__ = ('user_id', 'is_read', 'start', 'end')
    user_id = sgqlc.types.Field(Int, graphql_name='userId')
    is_read = sgqlc.types.Field(Boolean, graphql_name='isRead')
    start = sgqlc.types.Field(Timestamp, graphql_name='start')
    end = sgqlc.types.Field(Timestamp, graphql_name='end')


class NotificationUpdateInput(sgqlc.types.Input):
    __schema__ = seely_schema
    __field_names__ = ('is_read',)
    is_read = sgqlc.types.Field(Boolean, graphql_name='isRead')


class OperationLogFilter(sgqlc.types.Input):
    __schema__ = seely_schema
    __field_names__ = ('search', 'roles', 'modules', 'action', 'start', 'end')
    search = sgqlc.types.Field(String, graphql_name='search')
    roles = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='roles')
    modules = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(SystemModule)), graphql_name='modules')
    action = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(OperationAction)), graphql_name='action')
    start = sgqlc.types.Field(Timestamp, graphql_name='start')
    end = sgqlc.types.Field(Timestamp, graphql_name='end')


class OrganizationCreateInput(sgqlc.types.Input):
    __schema__ = seely_schema
    __field_names__ = ('name', 'timezone', 'short_name', 'province', 'city', 'district', 'address', 'greetings')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    timezone = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='timezone')
    short_name = sgqlc.types.Field(String, graphql_name='shortName')
    province = sgqlc.types.Field(String, graphql_name='province')
    city = sgqlc.types.Field(String, graphql_name='city')
    district = sgqlc.types.Field(String, graphql_name='district')
    address = sgqlc.types.Field(String, graphql_name='address')
    greetings = sgqlc.types.Field(GreetingsInput, graphql_name='greetings')


class OrganizationUpdateInput(sgqlc.types.Input):
    __schema__ = seely_schema
    __field_names__ = ('name', 'timezone', 'short_name', 'province', 'city', 'district', 'address', 'greetings')
    name = sgqlc.types.Field(String, graphql_name='name')
    timezone = sgqlc.types.Field(String, graphql_name='timezone')
    short_name = sgqlc.types.Field(String, graphql_name='shortName')
    province = sgqlc.types.Field(String, graphql_name='province')
    city = sgqlc.types.Field(String, graphql_name='city')
    district = sgqlc.types.Field(String, graphql_name='district')
    address = sgqlc.types.Field(String, graphql_name='address')
    greetings = sgqlc.types.Field(GreetingsInput, graphql_name='greetings')


class OtherPersonFilter(sgqlc.types.Input):
    __schema__ = seely_schema
    __field_names__ = ('search', 'role', 'departments', 'titles', 'job_levels', 'branches', 'permissions', 'tags', 'custom_filters', 'order_by', 'is_authorized', 'serial_number', 'email', 'with_blacklist', 'ids')
    search = sgqlc.types.Field(String, graphql_name='search')
    role = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='role')
    departments = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='departments')
    titles = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='titles')
    job_levels = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='jobLevels')
    branches = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='branches')
    permissions = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='permissions')
    tags = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='tags')
    custom_filters = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(FieldValueInput)), graphql_name='customFilters')
    order_by = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy')
    is_authorized = sgqlc.types.Field(Boolean, graphql_name='isAuthorized')
    serial_number = sgqlc.types.Field(String, graphql_name='serialNumber')
    email = sgqlc.types.Field(String, graphql_name='email')
    with_blacklist = sgqlc.types.Field(Boolean, graphql_name='withBlacklist')
    ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='ids')


class Page(sgqlc.types.Input):
    __schema__ = seely_schema
    __field_names__ = ('page', 'page_size', 'no_page')
    page = sgqlc.types.Field(Int, graphql_name='page')
    page_size = sgqlc.types.Field(Int, graphql_name='pageSize')
    no_page = sgqlc.types.Field(Boolean, graphql_name='noPage')


class PermissionScheduleInput(sgqlc.types.Input):
    __schema__ = seely_schema
    __field_names__ = ('days', 'is_full', 'start', 'end')
    days = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Day))), graphql_name='days')
    is_full = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isFull')
    start = sgqlc.types.Field(String, graphql_name='start')
    end = sgqlc.types.Field(String, graphql_name='end')


class PhotoInput(sgqlc.types.Input):
    __schema__ = seely_schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class PlatformOrganizationCreateInput(sgqlc.types.Input):
    __schema__ = seely_schema
    __field_names__ = ('name', 'timezone', 'short_name', 'province', 'city', 'district', 'address', 'greetings', 'platform_organization_id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    timezone = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='timezone')
    short_name = sgqlc.types.Field(String, graphql_name='shortName')
    province = sgqlc.types.Field(String, graphql_name='province')
    city = sgqlc.types.Field(String, graphql_name='city')
    district = sgqlc.types.Field(String, graphql_name='district')
    address = sgqlc.types.Field(String, graphql_name='address')
    greetings = sgqlc.types.Field(GreetingsInput, graphql_name='greetings')
    platform_organization_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='platformOrganizationId')


class PlatformRegisterUserInput(sgqlc.types.Input):
    __schema__ = seely_schema
    __field_names__ = ('account', 'phone', 'platform_organization_id', 'is_admin', 'company')
    account = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='account')
    phone = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='phone')
    platform_organization_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='platformOrganizationId')
    is_admin = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isAdmin')
    company = sgqlc.types.Field(String, graphql_name='company')


class RegisterDeviceInput(sgqlc.types.Input):
    __schema__ = seely_schema
    __field_names__ = ('uuid', 'name', 'type', 'model', 'location', 'version', 'sdk_version', 'url', 'used_for', 'tags')
    uuid = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='uuid')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    type = sgqlc.types.Field(sgqlc.types.non_null(DeviceType), graphql_name='type')
    model = sgqlc.types.Field(String, graphql_name='model')
    location = sgqlc.types.Field(String, graphql_name='location')
    version = sgqlc.types.Field(String, graphql_name='version')
    sdk_version = sgqlc.types.Field(String, graphql_name='sdkVersion')
    url = sgqlc.types.Field(String, graphql_name='url')
    used_for = sgqlc.types.Field(DeviceUsedFor, graphql_name='usedFor')
    tags = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='tags')


class RegisterUserInput(sgqlc.types.Input):
    __schema__ = seely_schema
    __field_names__ = ('account', 'password', 'company', 'contact', 'phone', 'organization_type', 'organization_version', 'timezone')
    account = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='account')
    password = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='password')
    company = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='company')
    contact = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='contact')
    phone = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='phone')
    organization_type = sgqlc.types.Field(OrganizationType, graphql_name='organizationType')
    organization_version = sgqlc.types.Field(OrganizationVersion, graphql_name='organizationVersion')
    timezone = sgqlc.types.Field(String, graphql_name='timezone')


class ReportFilter(sgqlc.types.Input):
    __schema__ = seely_schema
    __field_names__ = ('start', 'end')
    start = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='start')
    end = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='end')


class ResetPasswordInput(sgqlc.types.Input):
    __schema__ = seely_schema
    __field_names__ = ('new_password', 'signature')
    new_password = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='newPassword')
    signature = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='signature')


class RoleFilter(sgqlc.types.Input):
    __schema__ = seely_schema
    __field_names__ = ('search',)
    search = sgqlc.types.Field(String, graphql_name='search')


class SetBlacklistConfigInput(sgqlc.types.Input):
    __schema__ = seely_schema
    __field_names__ = ('enable_notify', 'notify_roles', 'channels')
    enable_notify = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='enableNotify')
    notify_roles = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='notifyRoles')
    channels = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(MessageChannel)), graphql_name='channels')


class TableConfigInput(sgqlc.types.Input):
    __schema__ = seely_schema
    __field_names__ = ('page_size', 'fields')
    page_size = sgqlc.types.Field(Int, graphql_name='pageSize')
    fields = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('TableFieldInput')), graphql_name='fields')


class TableFieldInput(sgqlc.types.Input):
    __schema__ = seely_schema
    __field_names__ = ('key', 'visible')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    visible = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='visible')


class TagFilter(sgqlc.types.Input):
    __schema__ = seely_schema
    __field_names__ = ('name', 'type')
    name = sgqlc.types.Field(String, graphql_name='name')
    type = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(TagType)), graphql_name='type')


class TaskFilter(sgqlc.types.Input):
    __schema__ = seely_schema
    __field_names__ = ('type', 'start', 'end', 'order_by')
    type = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(TaskType)), graphql_name='type')
    start = sgqlc.types.Field(Timestamp, graphql_name='start')
    end = sgqlc.types.Field(Timestamp, graphql_name='end')
    order_by = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy')


class UpdateBlacklistInput(sgqlc.types.Input):
    __schema__ = seely_schema
    __field_names__ = ('name', 'photo', 'remark')
    name = sgqlc.types.Field(String, graphql_name='name')
    photo = sgqlc.types.Field(PhotoInput, graphql_name='photo')
    remark = sgqlc.types.Field(String, graphql_name='remark')


class UpdateDeviceInput(sgqlc.types.Input):
    __schema__ = seely_schema
    __field_names__ = ('name', 'organization', 'tags', 'timezone', 'show_username', 'show_face_rect', 'enable_screen_saver', 'screen_saver_time', 'screen_saver_photo', 'audio', 'config', 'version', 'sdk_version')
    name = sgqlc.types.Field(String, graphql_name='name')
    organization = sgqlc.types.Field(IDInput, graphql_name='organization')
    tags = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='tags')
    timezone = sgqlc.types.Field(String, graphql_name='timezone')
    show_username = sgqlc.types.Field(Boolean, graphql_name='showUsername')
    show_face_rect = sgqlc.types.Field(Boolean, graphql_name='showFaceRect')
    enable_screen_saver = sgqlc.types.Field(Boolean, graphql_name='enableScreenSaver')
    screen_saver_time = sgqlc.types.Field(Int, graphql_name='screenSaverTime')
    screen_saver_photo = sgqlc.types.Field(PhotoInput, graphql_name='screenSaverPhoto')
    audio = sgqlc.types.Field('VideoInput', graphql_name='audio')
    config = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(FieldValueInput)), graphql_name='config')
    version = sgqlc.types.Field(String, graphql_name='version')
    sdk_version = sgqlc.types.Field(String, graphql_name='sdkVersion')


class UpdateEventInput(sgqlc.types.Input):
    __schema__ = seely_schema
    __field_names__ = ('status', 'visitor', 'target', 'target_organization', 'reason', 'book_time', 'deadline', 'permissions')
    status = sgqlc.types.Field(EventStatus, graphql_name='status')
    visitor = sgqlc.types.Field(EventVisitorUpdateInput, graphql_name='visitor')
    target = sgqlc.types.Field(IDInput, graphql_name='target')
    target_organization = sgqlc.types.Field(IDInput, graphql_name='targetOrganization')
    reason = sgqlc.types.Field(VisitReason, graphql_name='reason')
    book_time = sgqlc.types.Field(Timestamp, graphql_name='bookTime')
    deadline = sgqlc.types.Field(Timestamp, graphql_name='deadline')
    permissions = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='permissions')


class UpdateMeInput(sgqlc.types.Input):
    __schema__ = seely_schema
    __field_names__ = ('username', 'photo', 'phone', 'old_password', 'new_password', 'wechat_code', 'language')
    username = sgqlc.types.Field(String, graphql_name='username')
    photo = sgqlc.types.Field(PhotoInput, graphql_name='photo')
    phone = sgqlc.types.Field(String, graphql_name='phone')
    old_password = sgqlc.types.Field(String, graphql_name='oldPassword')
    new_password = sgqlc.types.Field(String, graphql_name='newPassword')
    wechat_code = sgqlc.types.Field(String, graphql_name='wechatCode')
    language = sgqlc.types.Field(String, graphql_name='language')


class UpdateMemberInput(sgqlc.types.Input):
    __schema__ = seely_schema
    __field_names__ = ('phone', 'photo', 'name', 'blacklist', 'role', 'id_card', 'serial_number', 'door_card_number', 'department', 'job_level', 'title', 'permissions', 'tags', 'greeting', 'display_name', 'probation', 'hire_date', 'correction_time', 'extra_data', 'remark')
    phone = sgqlc.types.Field(String, graphql_name='phone')
    photo = sgqlc.types.Field(PhotoInput, graphql_name='photo')
    name = sgqlc.types.Field(String, graphql_name='name')
    blacklist = sgqlc.types.Field(Boolean, graphql_name='blacklist')
    role = sgqlc.types.Field(IDInput, graphql_name='role')
    id_card = sgqlc.types.Field(String, graphql_name='idCard')
    serial_number = sgqlc.types.Field(String, graphql_name='serialNumber')
    door_card_number = sgqlc.types.Field(String, graphql_name='doorCardNumber')
    department = sgqlc.types.Field(IDInput, graphql_name='department')
    job_level = sgqlc.types.Field(IDInput, graphql_name='jobLevel')
    title = sgqlc.types.Field(IDInput, graphql_name='title')
    permissions = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='permissions')
    tags = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='tags')
    greeting = sgqlc.types.Field(String, graphql_name='greeting')
    display_name = sgqlc.types.Field(String, graphql_name='displayName')
    probation = sgqlc.types.Field(Boolean, graphql_name='probation')
    hire_date = sgqlc.types.Field(Timestamp, graphql_name='hireDate')
    correction_time = sgqlc.types.Field(Timestamp, graphql_name='correctionTime')
    extra_data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(FieldValueInput)), graphql_name='extraData')
    remark = sgqlc.types.Field(String, graphql_name='remark')


class UpdateMemberPermission(sgqlc.types.Input):
    __schema__ = seely_schema
    __field_names__ = ('name', 'schedule_type', 'schedules', 'departments', 'devices', 'remarks')
    name = sgqlc.types.Field(String, graphql_name='name')
    schedule_type = sgqlc.types.Field(ScheduleType, graphql_name='scheduleType')
    schedules = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(PermissionScheduleInput)), graphql_name='schedules')
    departments = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='departments')
    devices = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='devices')
    remarks = sgqlc.types.Field(String, graphql_name='remarks')


class UpdateMemberPermissionInput(sgqlc.types.Input):
    __schema__ = seely_schema
    __field_names__ = ('ids', 'permissions', 'action')
    ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids')
    permissions = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(MemberPermissionInput))), graphql_name='permissions')
    action = sgqlc.types.Field(sgqlc.types.non_null(PermissionAction), graphql_name='action')


class UpdateMemberRecordInput(sgqlc.types.Input):
    __schema__ = seely_schema
    __field_names__ = ('end', 'capture', 'video')
    end = sgqlc.types.Field(Timestamp, graphql_name='end')
    capture = sgqlc.types.Field(IDInput, graphql_name='capture')
    video = sgqlc.types.Field(IDInput, graphql_name='video')


class UpdateOtherPersonInput(sgqlc.types.Input):
    __schema__ = seely_schema
    __field_names__ = ('name', 'phone', 'photo', 'type', 'id_card', 'serial_number', 'door_card_number', 'email', 'permissions', 'tags', 'greeting', 'display_name', 'extra_data')
    name = sgqlc.types.Field(String, graphql_name='name')
    phone = sgqlc.types.Field(String, graphql_name='phone')
    photo = sgqlc.types.Field(PhotoInput, graphql_name='photo')
    type = sgqlc.types.Field(String, graphql_name='type')
    id_card = sgqlc.types.Field(String, graphql_name='idCard')
    serial_number = sgqlc.types.Field(String, graphql_name='serialNumber')
    door_card_number = sgqlc.types.Field(String, graphql_name='doorCardNumber')
    email = sgqlc.types.Field(String, graphql_name='email')
    permissions = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='permissions')
    tags = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='tags')
    greeting = sgqlc.types.Field(String, graphql_name='greeting')
    display_name = sgqlc.types.Field(String, graphql_name='displayName')
    extra_data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(FieldValueInput)), graphql_name='extraData')


class UpdateUserInput(sgqlc.types.Input):
    __schema__ = seely_schema
    __field_names__ = ('username', 'phone', 'email', 'roles', 'member', 'is_removed')
    username = sgqlc.types.Field(String, graphql_name='username')
    phone = sgqlc.types.Field(String, graphql_name='phone')
    email = sgqlc.types.Field(String, graphql_name='email')
    roles = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='roles')
    member = sgqlc.types.Field(IDInput, graphql_name='member')
    is_removed = sgqlc.types.Field(Boolean, graphql_name='isRemoved')


class UpdateVehicleInput(sgqlc.types.Input):
    __schema__ = seely_schema
    __field_names__ = ('license_plate', 'is_active', 'owner', 'phone', 'tags', 'member')
    license_plate = sgqlc.types.Field(String, graphql_name='licensePlate')
    is_active = sgqlc.types.Field(Boolean, graphql_name='isActive')
    owner = sgqlc.types.Field(String, graphql_name='owner')
    phone = sgqlc.types.Field(String, graphql_name='phone')
    tags = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='tags')
    member = sgqlc.types.Field(IDInput, graphql_name='member')


class UpdateVehicleRecordInput(sgqlc.types.Input):
    __schema__ = seely_schema
    __field_names__ = ('end',)
    end = sgqlc.types.Field(Timestamp, graphql_name='end')


class UserFilter(sgqlc.types.Input):
    __schema__ = seely_schema
    __field_names__ = ('search', 'managed_organizations', 'roles', 'order_by')
    search = sgqlc.types.Field(String, graphql_name='search')
    managed_organizations = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='managedOrganizations')
    roles = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='roles')
    order_by = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy')


class VehicleFilter(sgqlc.types.Input):
    __schema__ = seely_schema
    __field_names__ = ('is_active', 'search', 'tags', 'order_by')
    is_active = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Boolean)), graphql_name='isActive')
    search = sgqlc.types.Field(String, graphql_name='search')
    tags = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='tags')
    order_by = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy')


class VehicleRecordFilter(sgqlc.types.Input):
    __schema__ = seely_schema
    __field_names__ = ('search', 'device', 'access_type', 'start', 'end', 'identity')
    search = sgqlc.types.Field(String, graphql_name='search')
    device = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='device')
    access_type = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(AccessType)), graphql_name='accessType')
    start = sgqlc.types.Field(Timestamp, graphql_name='start')
    end = sgqlc.types.Field(Timestamp, graphql_name='end')
    identity = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IdentityFilter)), graphql_name='identity')


class VideoInput(sgqlc.types.Input):
    __schema__ = seely_schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class VisitCheckoutConfigInput(sgqlc.types.Input):
    __schema__ = seely_schema
    __field_names__ = ('enable', 'timestamp')
    enable = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='enable')
    timestamp = sgqlc.types.Field(Timestamp, graphql_name='timestamp')


class VisitConfigInput(sgqlc.types.Input):
    __schema__ = seely_schema
    __field_names__ = ('checkout_config',)
    checkout_config = sgqlc.types.Field(VisitCheckoutConfigInput, graphql_name='checkoutConfig')


class WxUpdateMeInput(sgqlc.types.Input):
    __schema__ = seely_schema
    __field_names__ = ('name', 'company', 'department', 'email', 'photo', 'id_type', 'id_number', 'plate')
    name = sgqlc.types.Field(String, graphql_name='name')
    company = sgqlc.types.Field(String, graphql_name='company')
    department = sgqlc.types.Field(String, graphql_name='department')
    email = sgqlc.types.Field(String, graphql_name='email')
    photo = sgqlc.types.Field(PhotoInput, graphql_name='photo')
    id_type = sgqlc.types.Field(IDType, graphql_name='idType')
    id_number = sgqlc.types.Field(String, graphql_name='idNumber')
    plate = sgqlc.types.Field(String, graphql_name='plate')



########################################################################
# Output Objects and Interfaces
########################################################################
class AccessVisitTotal(sgqlc.types.Type):
    __schema__ = seely_schema
    __field_names__ = ('name', 'illegal', 'normal', 'blacklist', 'forbidden', 'multimatch')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    illegal = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='illegal')
    normal = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='normal')
    blacklist = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='blacklist')
    forbidden = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='forbidden')
    multimatch = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='multimatch')


class AuthInfo(sgqlc.types.Type):
    __schema__ = seely_schema
    __field_names__ = ('is_active', 'token', 'reset_signature')
    is_active = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isActive')
    token = sgqlc.types.Field(String, graphql_name='token')
    reset_signature = sgqlc.types.Field(String, graphql_name='resetSignature')


class BlacklistConfig(sgqlc.types.Type):
    __schema__ = seely_schema
    __field_names__ = ('enable_notify', 'notify_roles', 'channels')
    enable_notify = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='enableNotify')
    notify_roles = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('Role')), graphql_name='notifyRoles')
    channels = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(MessageChannel)), graphql_name='channels')


class City(sgqlc.types.Type):
    __schema__ = seely_schema
    __field_names__ = ('id', 'name', 'province')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    province = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='province')


class ContentUnit(sgqlc.types.Type):
    __schema__ = seely_schema
    __field_names__ = ('key', 'value', 'new_value')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='value')
    new_value = sgqlc.types.Field(String, graphql_name='newValue')


class CreateEventResult(sgqlc.types.Type):
    __schema__ = seely_schema
    __field_names__ = ('is_success', 'ids')
    is_success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isSuccess')
    ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids')


class DailyAttendanceTotal(sgqlc.types.Type):
    __schema__ = seely_schema
    __field_names__ = ('late_times', 'late_min', 'early_leave_times', 'early_leave_min', 'absence_times', 'absence_leave_times', 'annual_leave', 'funeral_leave', 'wedding_leave', 'welfare_leave_times', 'sick_leave_times', 'over_hour_of_holiday', 'over_hour_of_weekend', 'over_hour_of_workingday', 'total_over_hour_of_holiday', 'total_over_hour_of_weekend', 'total_over_hour_of_workingday')
    late_times = sgqlc.types.Field(Int, graphql_name='lateTimes')
    late_min = sgqlc.types.Field(Int, graphql_name='lateMin')
    early_leave_times = sgqlc.types.Field(Int, graphql_name='earlyLeaveTimes')
    early_leave_min = sgqlc.types.Field(Int, graphql_name='earlyLeaveMin')
    absence_times = sgqlc.types.Field(Int, graphql_name='absenceTimes')
    absence_leave_times = sgqlc.types.Field(Int, graphql_name='absenceLeaveTimes')
    annual_leave = sgqlc.types.Field(Float, graphql_name='annualLeave')
    funeral_leave = sgqlc.types.Field(Float, graphql_name='funeralLeave')
    wedding_leave = sgqlc.types.Field(Float, graphql_name='weddingLeave')
    welfare_leave_times = sgqlc.types.Field(Float, graphql_name='welfareLeaveTimes')
    sick_leave_times = sgqlc.types.Field(Float, graphql_name='sickLeaveTimes')
    over_hour_of_holiday = sgqlc.types.Field(Float, graphql_name='overHourOfHoliday')
    over_hour_of_weekend = sgqlc.types.Field(Float, graphql_name='overHourOfWeekend')
    over_hour_of_workingday = sgqlc.types.Field(Float, graphql_name='overHourOfWorkingday')
    total_over_hour_of_holiday = sgqlc.types.Field(Float, graphql_name='totalOverHourOfHoliday')
    total_over_hour_of_weekend = sgqlc.types.Field(Float, graphql_name='totalOverHourOfWeekend')
    total_over_hour_of_workingday = sgqlc.types.Field(Float, graphql_name='totalOverHourOfWorkingday')


class DepartmentMembers(sgqlc.types.Type):
    __schema__ = seely_schema
    __field_names__ = ('name', 'members')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    members = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='members')


class District(sgqlc.types.Type):
    __schema__ = seely_schema
    __field_names__ = ('id', 'name', 'city')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    city = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='city')


class EditableValue(sgqlc.types.Interface):
    __schema__ = seely_schema
    __field_names__ = ('editable',)
    editable = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='editable')


class EventVisitor(sgqlc.types.Type):
    __schema__ = seely_schema
    __field_names__ = ('name', 'phone', 'email', 'id_type', 'id_number', 'plate', 'photo', 'company', 'department', 'extra_data', 'remark', 'allow_invite', 'door_card_number')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    phone = sgqlc.types.Field(String, graphql_name='phone')
    email = sgqlc.types.Field(String, graphql_name='email')
    id_type = sgqlc.types.Field(IDType, graphql_name='idType')
    id_number = sgqlc.types.Field(String, graphql_name='idNumber')
    plate = sgqlc.types.Field(String, graphql_name='plate')
    photo = sgqlc.types.Field('Photo', graphql_name='photo')
    company = sgqlc.types.Field(String, graphql_name='company')
    department = sgqlc.types.Field(String, graphql_name='department')
    extra_data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('FieldValue')), graphql_name='extraData')
    remark = sgqlc.types.Field(String, graphql_name='remark')
    allow_invite = sgqlc.types.Field(Boolean, graphql_name='allowInvite')
    door_card_number = sgqlc.types.Field(String, graphql_name='doorCardNumber')


class Excel(sgqlc.types.Type):
    __schema__ = seely_schema
    __field_names__ = ('content',)
    content = sgqlc.types.Field(String, graphql_name='content')


class Field(sgqlc.types.Interface):
    __schema__ = seely_schema
    __field_names__ = ('key', 'name', 'type', 'required')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    type = sgqlc.types.Field(sgqlc.types.non_null(FieldType), graphql_name='type')
    required = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='required')


class FieldConfig(sgqlc.types.Type):
    __schema__ = seely_schema
    __field_names__ = ('id', 'name', 'enable', 'required', 'visible', 'description')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    enable = sgqlc.types.Field(sgqlc.types.non_null('EditableBool'), graphql_name='enable')
    required = sgqlc.types.Field(sgqlc.types.non_null('EditableBool'), graphql_name='required')
    visible = sgqlc.types.Field(sgqlc.types.non_null('EditableBool'), graphql_name='visible')
    description = sgqlc.types.Field('MultiLanguageItem', graphql_name='description')


class FieldValue(sgqlc.types.Type):
    __schema__ = seely_schema
    __field_names__ = ('key', 'type', 'checkbox', 'text', 'time', 'date', 'select')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    type = sgqlc.types.Field(sgqlc.types.non_null(FieldType), graphql_name='type')
    checkbox = sgqlc.types.Field(Boolean, graphql_name='checkbox')
    text = sgqlc.types.Field(String, graphql_name='text')
    time = sgqlc.types.Field(Timestamp, graphql_name='time')
    date = sgqlc.types.Field(Timestamp, graphql_name='date')
    select = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='select')


class Greetings(sgqlc.types.Type):
    __schema__ = seely_schema
    __field_names__ = ('authorized', 'vip', 'unauthorized', 'illegal_time')
    authorized = sgqlc.types.Field(String, graphql_name='authorized')
    vip = sgqlc.types.Field(String, graphql_name='vip')
    unauthorized = sgqlc.types.Field(String, graphql_name='unauthorized')
    illegal_time = sgqlc.types.Field(String, graphql_name='illegalTime')


class IDNode(sgqlc.types.Interface):
    __schema__ = seely_schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class ListResponse(sgqlc.types.Type):
    __schema__ = seely_schema
    __field_names__ = ('count', 'data')
    count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(IDNode))), graphql_name='data')


class MemberIdentity(sgqlc.types.Type):
    __schema__ = seely_schema
    __field_names__ = ('type', 'department')
    type = sgqlc.types.Field(sgqlc.types.non_null(IdentityType), graphql_name='type')
    department = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('Department')), graphql_name='department')


class MemberRecordErrorReport(sgqlc.types.Type):
    __schema__ = seely_schema
    __field_names__ = ('illegal', 'multi_match', 'forbidden', 'blacklist')
    illegal = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='illegal')
    multi_match = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='multiMatch')
    forbidden = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='forbidden')
    blacklist = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='blacklist')


class MemberRecordIdentityDistribution(sgqlc.types.Type):
    __schema__ = seely_schema
    __field_names__ = ('stranger', 'id', 'other', 'temp_visitor', 'blacklist')
    stranger = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='stranger')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    other = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='other')
    temp_visitor = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='tempVisitor')
    blacklist = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='blacklist')


class MemberRecordTotal(sgqlc.types.Type):
    __schema__ = seely_schema
    __field_names__ = ('normal_visit', 'normal_visitor', 'abnormal')
    normal_visit = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='normalVisit')
    normal_visitor = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='normalVisitor')
    abnormal = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='abnormal')


class MultiLanguageItem(sgqlc.types.Type):
    __schema__ = seely_schema
    __field_names__ = ('cn', 'en')
    cn = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cn')
    en = sgqlc.types.Field(String, graphql_name='en')


class Mutation(sgqlc.types.Type):
    __schema__ = seely_schema
    __field_names__ = ('set_organization_form_config', 'set_user_table_config', 'set_visitor_form_config', 'device_heartbeat', 'register_device', 'register_server', 'update_device', 'delete_device', 'create_member', 'update_member', 'batch_update_member_permissions', 'delete_member', 'remove_member', 'revert_member', 'create_other_person', 'update_other_person', 'batch_update_other_person_permissions', 'delete_other_person', 'remove_other_person', 'revert_other_person', 'upload_members', 'upload_other_persons', 'upload_photos', 'save_department', 'save_title', 'save_job_level', 'delete_department', 'delete_title', 'delete_job_level', 'visit_authorization_to', 'upload_member_feature', 'login', 'register_user', 'platform_register_user', 'update_me', 'create_feedback', 'create_coop_consultation', 'send_reset_password_email', 'reset_password', 'update_user', 'delete_user', 'platform_delete_user', 'create_user', 'create_organization', 'platform_create_organization', 'update_organization', 'delete_organization', 'move_organization', 'create_permission', 'update_permission', 'delete_permission', 'upload_image', 'upload_video', 'upload_image_base64', 'create_member_record', 'update_member_record', 'create_vehicle', 'update_vehicle', 'delete_vehicle', 'create_vehicle_record', 'update_vehicle_record', 'create_event', 'acquire_event_qr_code', 'update_event', 'set_visit_checkout_config', 'set_visit_config', 'delete_visitors', 'upload_visitor_feature', 'create_blacklist', 'update_blacklist', 'delete_blacklist', 'set_blacklist_config', 'create_issue', 'wx_login', 'wx_close_account', 'wx_update_me', 'wx_bind_visitor_phone', 'wx_unbind_visitor_phone', 'wx_submit_form_id', 'delete_task', 'database_backup', 'update_notification', 'delete_notification', 'upload_calendar', 'set_attendance_setting', 'set_daily_attendance', 'debug_calculate_attendance')
    set_organization_form_config = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='setOrganizationFormConfig', args=sgqlc.types.ArgDict((
        ('table', sgqlc.types.Arg(sgqlc.types.non_null(Table), graphql_name='table', default=None)),
        ('fields', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(FormFieldInput))), graphql_name='fields', default=None)),
))
    )
    set_user_table_config = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='setUserTableConfig', args=sgqlc.types.ArgDict((
        ('table', sgqlc.types.Arg(sgqlc.types.non_null(Table), graphql_name='table', default=None)),
        ('config', sgqlc.types.Arg(sgqlc.types.non_null(TableConfigInput), graphql_name='config', default=None)),
))
    )
    set_visitor_form_config = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='setVisitorFormConfig', args=sgqlc.types.ArgDict((
        ('fields', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(FieldConfigInput))), graphql_name='fields', default=None)),
))
    )
    device_heartbeat = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deviceHeartbeat', args=sgqlc.types.ArgDict((
        ('uuid', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='uuid', default=None)),
))
    )
    register_device = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='registerDevice', args=sgqlc.types.ArgDict((
        ('device', sgqlc.types.Arg(sgqlc.types.non_null(RegisterDeviceInput), graphql_name='device', default=None)),
))
    )
    register_server = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='registerServer', args=sgqlc.types.ArgDict((
        ('server', sgqlc.types.Arg(sgqlc.types.non_null(CreateServerInput), graphql_name='server', default=None)),
))
    )
    update_device = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateDevice', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids', default=None)),
        ('device', sgqlc.types.Arg(sgqlc.types.non_null(UpdateDeviceInput), graphql_name='device', default=None)),
))
    )
    delete_device = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteDevice', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids', default=None)),
))
    )
    create_member = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='createMember', args=sgqlc.types.ArgDict((
        ('member', sgqlc.types.Arg(sgqlc.types.non_null(CreateMemberInput), graphql_name='member', default=None)),
))
    )
    update_member = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateMember', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids', default=None)),
        ('member', sgqlc.types.Arg(sgqlc.types.non_null(UpdateMemberInput), graphql_name='member', default=None)),
))
    )
    batch_update_member_permissions = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='batchUpdateMemberPermissions', args=sgqlc.types.ArgDict((
        ('update_permission_input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateMemberPermissionInput), graphql_name='updatePermissionInput', default=None)),
))
    )
    delete_member = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteMember', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids', default=None)),
))
    )
    remove_member = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='removeMember', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids', default=None)),
))
    )
    revert_member = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='revertMember', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids', default=None)),
))
    )
    create_other_person = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='createOtherPerson', args=sgqlc.types.ArgDict((
        ('other_person', sgqlc.types.Arg(sgqlc.types.non_null(CreateOtherPersonInput), graphql_name='otherPerson', default=None)),
))
    )
    update_other_person = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateOtherPerson', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids', default=None)),
        ('other_person', sgqlc.types.Arg(sgqlc.types.non_null(UpdateOtherPersonInput), graphql_name='otherPerson', default=None)),
))
    )
    batch_update_other_person_permissions = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='batchUpdateOtherPersonPermissions', args=sgqlc.types.ArgDict((
        ('update_permission_input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateMemberPermissionInput), graphql_name='updatePermissionInput', default=None)),
))
    )
    delete_other_person = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteOtherPerson', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids', default=None)),
))
    )
    remove_other_person = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='removeOtherPerson', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids', default=None)),
))
    )
    revert_other_person = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='revertOtherPerson', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids', default=None)),
))
    )
    upload_members = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='uploadMembers', args=sgqlc.types.ArgDict((
        ('file', sgqlc.types.Arg(sgqlc.types.non_null(Upload), graphql_name='file', default=None)),
))
    )
    upload_other_persons = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='uploadOtherPersons', args=sgqlc.types.ArgDict((
        ('file', sgqlc.types.Arg(sgqlc.types.non_null(Upload), graphql_name='file', default=None)),
))
    )
    upload_photos = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='uploadPhotos', args=sgqlc.types.ArgDict((
        ('file', sgqlc.types.Arg(Upload, graphql_name='file', default=None)),
))
    )
    save_department = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='saveDepartment', args=sgqlc.types.ArgDict((
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
        ('id', sgqlc.types.Arg(ID, graphql_name='id', default=None)),
))
    )
    save_title = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='saveTitle', args=sgqlc.types.ArgDict((
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
        ('id', sgqlc.types.Arg(ID, graphql_name='id', default=None)),
))
    )
    save_job_level = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='saveJobLevel', args=sgqlc.types.ArgDict((
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
        ('id', sgqlc.types.Arg(ID, graphql_name='id', default=None)),
))
    )
    delete_department = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteDepartment', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    delete_title = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteTitle', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    delete_job_level = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteJobLevel', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    visit_authorization_to = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='visitAuthorizationTo', args=sgqlc.types.ArgDict((
        ('member', sgqlc.types.Arg(IDInput, graphql_name='member', default=None)),
))
    )
    upload_member_feature = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='uploadMemberFeature', args=sgqlc.types.ArgDict((
        ('member_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='memberId', default=None)),
        ('photo_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='photoId', default=None)),
        ('valid', sgqlc.types.Arg(sgqlc.types.non_null(Boolean), graphql_name='valid', default=None)),
        ('linux_feature', sgqlc.types.Arg(String, graphql_name='linuxFeature', default=None)),
        ('feature', sgqlc.types.Arg(String, graphql_name='feature', default=None)),
        ('version', sgqlc.types.Arg(String, graphql_name='version', default=None)),
))
    )
    login = sgqlc.types.Field(sgqlc.types.non_null(AuthInfo), graphql_name='login', args=sgqlc.types.ArgDict((
        ('account', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='account', default=None)),
        ('password', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='password', default=None)),
))
    )
    register_user = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='registerUser', args=sgqlc.types.ArgDict((
        ('user', sgqlc.types.Arg(sgqlc.types.non_null(RegisterUserInput), graphql_name='user', default=None)),
))
    )
    platform_register_user = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='platformRegisterUser', args=sgqlc.types.ArgDict((
        ('user', sgqlc.types.Arg(sgqlc.types.non_null(PlatformRegisterUserInput), graphql_name='user', default=None)),
))
    )
    update_me = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateMe', args=sgqlc.types.ArgDict((
        ('me', sgqlc.types.Arg(sgqlc.types.non_null(UpdateMeInput), graphql_name='me', default=None)),
))
    )
    create_feedback = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='createFeedback', args=sgqlc.types.ArgDict((
        ('feedback', sgqlc.types.Arg(sgqlc.types.non_null(CreateFeedbackInput), graphql_name='feedback', default=None)),
))
    )
    create_coop_consultation = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='createCoopConsultation', args=sgqlc.types.ArgDict((
        ('coop_consultation', sgqlc.types.Arg(sgqlc.types.non_null(CreateCoopConsultationInput), graphql_name='coopConsultation', default=None)),
))
    )
    send_reset_password_email = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='sendResetPasswordEmail', args=sgqlc.types.ArgDict((
        ('email', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='email', default=None)),
))
    )
    reset_password = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='resetPassword', args=sgqlc.types.ArgDict((
        ('reset_password_input', sgqlc.types.Arg(sgqlc.types.non_null(ResetPasswordInput), graphql_name='resetPasswordInput', default=None)),
))
    )
    update_user = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateUser', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids', default=None)),
        ('user', sgqlc.types.Arg(sgqlc.types.non_null(UpdateUserInput), graphql_name='user', default=None)),
))
    )
    delete_user = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteUser', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids', default=None)),
))
    )
    platform_delete_user = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='platformDeleteUser', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids', default=None)),
))
    )
    create_user = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='createUser', args=sgqlc.types.ArgDict((
        ('user', sgqlc.types.Arg(sgqlc.types.non_null(CreateUserInput), graphql_name='user', default=None)),
))
    )
    create_organization = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='createOrganization', args=sgqlc.types.ArgDict((
        ('organization', sgqlc.types.Arg(sgqlc.types.non_null(OrganizationCreateInput), graphql_name='organization', default=None)),
        ('parent_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='parentId', default=None)),
))
    )
    platform_create_organization = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='platformCreateOrganization', args=sgqlc.types.ArgDict((
        ('organization', sgqlc.types.Arg(sgqlc.types.non_null(PlatformOrganizationCreateInput), graphql_name='organization', default=None)),
))
    )
    update_organization = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateOrganization', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids', default=None)),
        ('organization', sgqlc.types.Arg(sgqlc.types.non_null(OrganizationUpdateInput), graphql_name='organization', default=None)),
))
    )
    delete_organization = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteOrganization', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids', default=None)),
))
    )
    move_organization = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='moveOrganization', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('destination', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='destination', default=None)),
))
    )
    create_permission = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='createPermission', args=sgqlc.types.ArgDict((
        ('permission', sgqlc.types.Arg(sgqlc.types.non_null(CreateMemberPermission), graphql_name='permission', default=None)),
))
    )
    update_permission = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updatePermission', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids', default=None)),
        ('permission', sgqlc.types.Arg(sgqlc.types.non_null(UpdateMemberPermission), graphql_name='permission', default=None)),
))
    )
    delete_permission = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deletePermission', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids', default=None)),
))
    )
    upload_image = sgqlc.types.Field(sgqlc.types.non_null('UploadImage'), graphql_name='uploadImage', args=sgqlc.types.ArgDict((
        ('file', sgqlc.types.Arg(Upload, graphql_name='file', default=None)),
))
    )
    upload_video = sgqlc.types.Field(sgqlc.types.non_null('UploadVideo'), graphql_name='uploadVideo', args=sgqlc.types.ArgDict((
        ('file', sgqlc.types.Arg(Upload, graphql_name='file', default=None)),
))
    )
    upload_image_base64 = sgqlc.types.Field(sgqlc.types.non_null('UploadImage'), graphql_name='uploadImageBase64', args=sgqlc.types.ArgDict((
        ('file', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='file', default=None)),
))
    )
    create_member_record = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='createMemberRecord', args=sgqlc.types.ArgDict((
        ('member_record', sgqlc.types.Arg(sgqlc.types.non_null(CreateMemberRecordInput), graphql_name='memberRecord', default=None)),
))
    )
    update_member_record = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateMemberRecord', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('member_record', sgqlc.types.Arg(sgqlc.types.non_null(UpdateMemberRecordInput), graphql_name='memberRecord', default=None)),
))
    )
    create_vehicle = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='createVehicle', args=sgqlc.types.ArgDict((
        ('vehicle', sgqlc.types.Arg(sgqlc.types.non_null(CreateVehicleInput), graphql_name='vehicle', default=None)),
))
    )
    update_vehicle = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateVehicle', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids', default=None)),
        ('vehicle', sgqlc.types.Arg(sgqlc.types.non_null(UpdateVehicleInput), graphql_name='vehicle', default=None)),
))
    )
    delete_vehicle = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteVehicle', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids', default=None)),
))
    )
    create_vehicle_record = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='createVehicleRecord', args=sgqlc.types.ArgDict((
        ('vehicle_record', sgqlc.types.Arg(sgqlc.types.non_null(CreateVehicleRecordInput), graphql_name='vehicleRecord', default=None)),
))
    )
    update_vehicle_record = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateVehicleRecord', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('vehicle_record', sgqlc.types.Arg(sgqlc.types.non_null(UpdateVehicleRecordInput), graphql_name='vehicleRecord', default=None)),
))
    )
    create_event = sgqlc.types.Field(CreateEventResult, graphql_name='createEvent', args=sgqlc.types.ArgDict((
        ('event', sgqlc.types.Arg(sgqlc.types.non_null(CreateEventInput), graphql_name='event', default=None)),
))
    )
    acquire_event_qr_code = sgqlc.types.Field(String, graphql_name='acquireEventQrCode', args=sgqlc.types.ArgDict((
        ('event_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='eventId', default=None)),
))
    )
    update_event = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateEvent', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids', default=None)),
        ('event', sgqlc.types.Arg(sgqlc.types.non_null(UpdateEventInput), graphql_name='event', default=None)),
))
    )
    set_visit_checkout_config = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='setVisitCheckoutConfig', args=sgqlc.types.ArgDict((
        ('config', sgqlc.types.Arg(sgqlc.types.non_null(VisitCheckoutConfigInput), graphql_name='config', default=None)),
))
    )
    set_visit_config = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='setVisitConfig', args=sgqlc.types.ArgDict((
        ('config', sgqlc.types.Arg(sgqlc.types.non_null(VisitConfigInput), graphql_name='config', default=None)),
))
    )
    delete_visitors = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteVisitors', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids', default=None)),
))
    )
    upload_visitor_feature = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='uploadVisitorFeature', args=sgqlc.types.ArgDict((
        ('visitor_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='visitorId', default=None)),
        ('photo_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='photoId', default=None)),
        ('valid', sgqlc.types.Arg(sgqlc.types.non_null(Boolean), graphql_name='valid', default=None)),
        ('linux_feature', sgqlc.types.Arg(String, graphql_name='linuxFeature', default=None)),
        ('feature', sgqlc.types.Arg(String, graphql_name='feature', default=None)),
        ('version', sgqlc.types.Arg(String, graphql_name='version', default=None)),
))
    )
    create_blacklist = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='createBlacklist', args=sgqlc.types.ArgDict((
        ('blacklist', sgqlc.types.Arg(sgqlc.types.non_null(CreateBlacklistInput), graphql_name='blacklist', default=None)),
))
    )
    update_blacklist = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateBlacklist', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids', default=None)),
        ('blacklist', sgqlc.types.Arg(sgqlc.types.non_null(UpdateBlacklistInput), graphql_name='blacklist', default=None)),
))
    )
    delete_blacklist = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteBlacklist', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids', default=None)),
))
    )
    set_blacklist_config = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='setBlacklistConfig', args=sgqlc.types.ArgDict((
        ('config', sgqlc.types.Arg(sgqlc.types.non_null(SetBlacklistConfigInput), graphql_name='config', default=None)),
))
    )
    create_issue = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='createIssue', args=sgqlc.types.ArgDict((
        ('type', sgqlc.types.Arg(sgqlc.types.non_null(IssueType), graphql_name='type', default=None)),
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
        ('phone', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='phone', default=None)),
        ('email', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='email', default=None)),
        ('topic', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='topic', default=None)),
        ('content', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='content', default=None)),
        ('company', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='company', default=None)),
))
    )
    wx_login = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='wxLogin', args=sgqlc.types.ArgDict((
        ('code', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='code', default=None)),
))
    )
    wx_close_account = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='wxCloseAccount')
    wx_update_me = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='wxUpdateMe', args=sgqlc.types.ArgDict((
        ('me', sgqlc.types.Arg(sgqlc.types.non_null(WxUpdateMeInput), graphql_name='me', default=None)),
))
    )
    wx_bind_visitor_phone = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='wxBindVisitorPhone', args=sgqlc.types.ArgDict((
        ('iv', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='iv', default=None)),
        ('data', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='data', default=None)),
))
    )
    wx_unbind_visitor_phone = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='wxUnbindVisitorPhone')
    wx_submit_form_id = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='wxSubmitFormId', args=sgqlc.types.ArgDict((
        ('form_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='formId', default=None)),
))
    )
    delete_task = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteTask', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids', default=None)),
))
    )
    database_backup = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='databaseBackup')
    update_notification = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateNotification', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids', default=None)),
        ('notification', sgqlc.types.Arg(sgqlc.types.non_null(NotificationUpdateInput), graphql_name='notification', default=None)),
))
    )
    delete_notification = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteNotification', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids', default=None)),
))
    )
    upload_calendar = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='uploadCalendar', args=sgqlc.types.ArgDict((
        ('file', sgqlc.types.Arg(sgqlc.types.non_null(Upload), graphql_name='file', default=None)),
))
    )
    set_attendance_setting = sgqlc.types.Field(sgqlc.types.non_null('AttendanceSetting'), graphql_name='setAttendanceSetting', args=sgqlc.types.ArgDict((
        ('setting', sgqlc.types.Arg(sgqlc.types.non_null(CreatAttendanceSettingInput), graphql_name='setting', default=None)),
))
    )
    set_daily_attendance = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='setDailyAttendance', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('attendance', sgqlc.types.Arg(sgqlc.types.non_null(DailyAttendanceUpdatedInput), graphql_name='attendance', default=None)),
))
    )
    debug_calculate_attendance = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='debugCalculateAttendance')


class OperationDataInterface(sgqlc.types.Interface):
    __schema__ = seely_schema
    __field_names__ = ('object',)
    object = sgqlc.types.Field(String, graphql_name='object')


class OrganizationInTree(sgqlc.types.Type):
    __schema__ = seely_schema
    __field_names__ = ('id', 'name', 'children')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    children = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('OrganizationInTree')), graphql_name='children')


class PermissionSchedule(sgqlc.types.Type):
    __schema__ = seely_schema
    __field_names__ = ('days', 'is_full', 'start', 'end')
    days = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Day))), graphql_name='days')
    is_full = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isFull')
    start = sgqlc.types.Field(String, graphql_name='start')
    end = sgqlc.types.Field(String, graphql_name='end')


class Province(sgqlc.types.Type):
    __schema__ = seely_schema
    __field_names__ = ('id', 'name')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class Query(sgqlc.types.Type):
    __schema__ = seely_schema
    __field_names__ = ('organization_form_config', 'user_table_config', 'visitor_form_config', 'device_models', 'device_versions', 'device_tags', 'devices', 'export_devices', 'device', 'tag_devices', 'sync_clock', 'member_tags', 'other_person_tags', 'member_permissions', 'members', 'export_members', 'removed_members', 'member_template', 'other_template', 'other_persons', 'export_other_persons', 'removed_other_persons', 'sync_member_ids', 'batch_sync_member', 'departments', 'titles', 'job_levels', 'member_authorized_to', 'account_exist', 'me', 'user_company', 'roles', 'users', 'organization_tree', 'organization', 'organizations', 'provinces', 'cities', 'districts', 'timezone', 'member_access_permissions', 'permission_members', 'image', 'member_records', 'export_member_records', 'vehicles', 'vehicle_tags', 'vehicle_records', 'export_vehicle_records', 'events', 'event', 'export_events', 'visit_config', 'sync_visitor', 'visitors', 'blacklist', 'blacklist_config', 'operation_logs', 'export_operation_logs', 'tags', 'tags_info', 'wx_me', 'member_record_total', 'member_record_error_report', 'member_record_visit_total', 'member_record_identity_distribution', 'member_record_access_visit_total', 'tasks', 'has_unread_notification', 'notifications', 'calendar_template', 'attendance_setting', 'daily_attendance', 'monthly_attendance', 'daily_attendance_total', 'export_daily_attendance', 'export_monthly_attendance')
    organization_form_config = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('FormField'))), graphql_name='organizationFormConfig', args=sgqlc.types.ArgDict((
        ('table', sgqlc.types.Arg(sgqlc.types.non_null(Table), graphql_name='table', default=None)),
))
    )
    user_table_config = sgqlc.types.Field(sgqlc.types.non_null('TableConfig'), graphql_name='userTableConfig', args=sgqlc.types.ArgDict((
        ('table', sgqlc.types.Arg(sgqlc.types.non_null(Table), graphql_name='table', default=None)),
))
    )
    visitor_form_config = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(FieldConfig))), graphql_name='visitorFormConfig', args=sgqlc.types.ArgDict((
        ('event_id', sgqlc.types.Arg(ID, graphql_name='eventId', default=None)),
))
    )
    device_models = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='deviceModels')
    device_versions = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='deviceVersions')
    device_tags = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='deviceTags')
    devices = sgqlc.types.Field(sgqlc.types.non_null(ListResponse), graphql_name='devices', args=sgqlc.types.ArgDict((
        ('page', sgqlc.types.Arg(sgqlc.types.non_null(Page), graphql_name='page', default=None)),
        ('filter', sgqlc.types.Arg(DeviceFilter, graphql_name='filter', default=None)),
))
    )
    export_devices = sgqlc.types.Field(sgqlc.types.non_null(Excel), graphql_name='exportDevices', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(DeviceFilter, graphql_name='filter', default=None)),
))
    )
    device = sgqlc.types.Field(sgqlc.types.non_null('Device'), graphql_name='device', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    tag_devices = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TagDevices'))), graphql_name='tagDevices')
    sync_clock = sgqlc.types.Field(sgqlc.types.non_null('SyncClock'), graphql_name='syncClock')
    member_tags = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='memberTags')
    other_person_tags = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='otherPersonTags')
    member_permissions = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('MemberPermission'))), graphql_name='memberPermissions', args=sgqlc.types.ArgDict((
        ('department', sgqlc.types.Arg(String, graphql_name='department', default=None)),
))
    )
    members = sgqlc.types.Field(sgqlc.types.non_null(ListResponse), graphql_name='members', args=sgqlc.types.ArgDict((
        ('page', sgqlc.types.Arg(sgqlc.types.non_null(Page), graphql_name='page', default=None)),
        ('filter', sgqlc.types.Arg(MemberFilter, graphql_name='filter', default=None)),
))
    )
    export_members = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='exportMembers', args=sgqlc.types.ArgDict((
        ('file_type', sgqlc.types.Arg(sgqlc.types.non_null(MemberExport), graphql_name='fileType', default=None)),
        ('filter', sgqlc.types.Arg(MemberFilter, graphql_name='filter', default=None)),
))
    )
    removed_members = sgqlc.types.Field(sgqlc.types.non_null(ListResponse), graphql_name='removedMembers', args=sgqlc.types.ArgDict((
        ('page', sgqlc.types.Arg(sgqlc.types.non_null(Page), graphql_name='page', default=None)),
        ('filter', sgqlc.types.Arg(MemberFilter, graphql_name='filter', default=None)),
))
    )
    member_template = sgqlc.types.Field(sgqlc.types.non_null(Excel), graphql_name='memberTemplate', args=sgqlc.types.ArgDict((
        ('with_data', sgqlc.types.Arg(Boolean, graphql_name='withData', default=False)),
))
    )
    other_template = sgqlc.types.Field(sgqlc.types.non_null(Excel), graphql_name='otherTemplate', args=sgqlc.types.ArgDict((
        ('with_data', sgqlc.types.Arg(Boolean, graphql_name='withData', default=False)),
))
    )
    other_persons = sgqlc.types.Field(sgqlc.types.non_null(ListResponse), graphql_name='otherPersons', args=sgqlc.types.ArgDict((
        ('page', sgqlc.types.Arg(sgqlc.types.non_null(Page), graphql_name='page', default=None)),
        ('filter', sgqlc.types.Arg(OtherPersonFilter, graphql_name='filter', default=None)),
))
    )
    export_other_persons = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='exportOtherPersons', args=sgqlc.types.ArgDict((
        ('file_type', sgqlc.types.Arg(sgqlc.types.non_null(MemberExport), graphql_name='fileType', default=None)),
        ('filter', sgqlc.types.Arg(OtherPersonFilter, graphql_name='filter', default=None)),
))
    )
    removed_other_persons = sgqlc.types.Field(sgqlc.types.non_null(ListResponse), graphql_name='removedOtherPersons', args=sgqlc.types.ArgDict((
        ('page', sgqlc.types.Arg(sgqlc.types.non_null(Page), graphql_name='page', default=None)),
        ('filter', sgqlc.types.Arg(OtherPersonFilter, graphql_name='filter', default=None)),
))
    )
    sync_member_ids = sgqlc.types.Field(sgqlc.types.non_null('SyncIds'), graphql_name='syncMemberIds', args=sgqlc.types.ArgDict((
        ('uuid', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='uuid', default=None)),
        ('current', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='current', default=None)),
))
    )
    batch_sync_member = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('SyncMember'))), graphql_name='batchSyncMember', args=sgqlc.types.ArgDict((
        ('uuid', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='uuid', default=None)),
        ('members', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='members', default=None)),
))
    )
    departments = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Department'))), graphql_name='departments', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(String, graphql_name='search', default=None)),
))
    )
    titles = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Title'))), graphql_name='titles', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(String, graphql_name='search', default=None)),
))
    )
    job_levels = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('JobLevel'))), graphql_name='jobLevels', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(String, graphql_name='search', default=None)),
))
    )
    member_authorized_to = sgqlc.types.Field('Member', graphql_name='memberAuthorizedTo')
    account_exist = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='accountExist', args=sgqlc.types.ArgDict((
        ('account', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='account', default=None)),
))
    )
    me = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='me')
    user_company = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='userCompany')
    roles = sgqlc.types.Field(sgqlc.types.non_null(ListResponse), graphql_name='roles', args=sgqlc.types.ArgDict((
        ('page', sgqlc.types.Arg(sgqlc.types.non_null(Page), graphql_name='page', default=None)),
        ('filter', sgqlc.types.Arg(RoleFilter, graphql_name='filter', default=None)),
))
    )
    users = sgqlc.types.Field(sgqlc.types.non_null(ListResponse), graphql_name='users', args=sgqlc.types.ArgDict((
        ('page', sgqlc.types.Arg(sgqlc.types.non_null(Page), graphql_name='page', default=None)),
        ('filter', sgqlc.types.Arg(UserFilter, graphql_name='filter', default=None)),
))
    )
    organization_tree = sgqlc.types.Field(sgqlc.types.non_null(JSONString), graphql_name='organizationTree', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(ID, graphql_name='id', default=None)),
))
    )
    organization = sgqlc.types.Field(sgqlc.types.non_null('Organization'), graphql_name='organization', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(ID, graphql_name='id', default=None)),
))
    )
    organizations = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Organization'))), graphql_name='organizations')
    provinces = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Province))), graphql_name='provinces')
    cities = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(City))), graphql_name='cities', args=sgqlc.types.ArgDict((
        ('province_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='provinceId', default=None)),
))
    )
    districts = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(District))), graphql_name='districts', args=sgqlc.types.ArgDict((
        ('city_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='cityId', default=None)),
))
    )
    timezone = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='timezone', args=sgqlc.types.ArgDict((
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
))
    )
    member_access_permissions = sgqlc.types.Field(sgqlc.types.non_null(ListResponse), graphql_name='memberAccessPermissions', args=sgqlc.types.ArgDict((
        ('page', sgqlc.types.Arg(sgqlc.types.non_null(Page), graphql_name='page', default=None)),
        ('filter', sgqlc.types.Arg(MemberPermissionFilter, graphql_name='filter', default=None)),
))
    )
    permission_members = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(DepartmentMembers))), graphql_name='permissionMembers', args=sgqlc.types.ArgDict((
        ('permission', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='permission', default=None)),
))
    )
    image = sgqlc.types.Field(sgqlc.types.non_null('Photo'), graphql_name='image', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('size', sgqlc.types.Arg(String, graphql_name='size', default='200x200')),
))
    )
    member_records = sgqlc.types.Field(sgqlc.types.non_null(ListResponse), graphql_name='memberRecords', args=sgqlc.types.ArgDict((
        ('page', sgqlc.types.Arg(sgqlc.types.non_null(Page), graphql_name='page', default=None)),
        ('filter', sgqlc.types.Arg(MemberRecordFilter, graphql_name='filter', default=None)),
))
    )
    export_member_records = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='exportMemberRecords', args=sgqlc.types.ArgDict((
        ('file_type', sgqlc.types.Arg(sgqlc.types.non_null(MemberRecordExport), graphql_name='fileType', default=None)),
        ('filter', sgqlc.types.Arg(MemberRecordFilter, graphql_name='filter', default=None)),
))
    )
    vehicles = sgqlc.types.Field(sgqlc.types.non_null(ListResponse), graphql_name='vehicles', args=sgqlc.types.ArgDict((
        ('page', sgqlc.types.Arg(sgqlc.types.non_null(Page), graphql_name='page', default=None)),
        ('filter', sgqlc.types.Arg(VehicleFilter, graphql_name='filter', default=None)),
))
    )
    vehicle_tags = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='vehicleTags')
    vehicle_records = sgqlc.types.Field(sgqlc.types.non_null(ListResponse), graphql_name='vehicleRecords', args=sgqlc.types.ArgDict((
        ('page', sgqlc.types.Arg(sgqlc.types.non_null(Page), graphql_name='page', default=None)),
        ('filter', sgqlc.types.Arg(VehicleRecordFilter, graphql_name='filter', default=None)),
))
    )
    export_vehicle_records = sgqlc.types.Field(sgqlc.types.non_null(Excel), graphql_name='exportVehicleRecords', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(VehicleRecordFilter, graphql_name='filter', default=None)),
))
    )
    events = sgqlc.types.Field(sgqlc.types.non_null(ListResponse), graphql_name='events', args=sgqlc.types.ArgDict((
        ('page', sgqlc.types.Arg(sgqlc.types.non_null(Page), graphql_name='page', default=None)),
        ('filter', sgqlc.types.Arg(EventFilter, graphql_name='filter', default=None)),
))
    )
    event = sgqlc.types.Field(sgqlc.types.non_null('Event'), graphql_name='event', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    export_events = sgqlc.types.Field(sgqlc.types.non_null(Excel), graphql_name='exportEvents', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(EventFilter, graphql_name='filter', default=None)),
))
    )
    visit_config = sgqlc.types.Field(sgqlc.types.non_null('VisitConfig'), graphql_name='visitConfig', args=sgqlc.types.ArgDict((
        ('event_id', sgqlc.types.Arg(ID, graphql_name='eventId', default=None)),
))
    )
    sync_visitor = sgqlc.types.Field('SyncData', graphql_name='syncVisitor', args=sgqlc.types.ArgDict((
        ('uuid', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='uuid', default=None)),
        ('current', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='current', default=None)),
))
    )
    visitors = sgqlc.types.Field(sgqlc.types.non_null(ListResponse), graphql_name='visitors', args=sgqlc.types.ArgDict((
        ('page', sgqlc.types.Arg(sgqlc.types.non_null(Page), graphql_name='page', default=None)),
))
    )
    blacklist = sgqlc.types.Field(sgqlc.types.non_null(ListResponse), graphql_name='blacklist', args=sgqlc.types.ArgDict((
        ('page', sgqlc.types.Arg(sgqlc.types.non_null(Page), graphql_name='page', default=None)),
        ('filter', sgqlc.types.Arg(BlacklistFilterInput, graphql_name='filter', default=None)),
))
    )
    blacklist_config = sgqlc.types.Field(sgqlc.types.non_null(BlacklistConfig), graphql_name='blacklistConfig')
    operation_logs = sgqlc.types.Field(sgqlc.types.non_null(ListResponse), graphql_name='operationLogs', args=sgqlc.types.ArgDict((
        ('page', sgqlc.types.Arg(sgqlc.types.non_null(Page), graphql_name='page', default=None)),
        ('filter', sgqlc.types.Arg(OperationLogFilter, graphql_name='filter', default=None)),
))
    )
    export_operation_logs = sgqlc.types.Field(sgqlc.types.non_null(Excel), graphql_name='exportOperationLogs', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(OperationLogFilter, graphql_name='filter', default=None)),
))
    )
    tags = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='tags', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(TagFilter, graphql_name='filter', default=None)),
))
    )
    tags_info = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Tag'))), graphql_name='tagsInfo', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(TagFilter, graphql_name='filter', default=None)),
))
    )
    wx_me = sgqlc.types.Field(sgqlc.types.non_null('WeChatUser'), graphql_name='wxMe')
    member_record_total = sgqlc.types.Field(sgqlc.types.non_null(MemberRecordTotal), graphql_name='memberRecordTotal', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(ReportFilter), graphql_name='filter', default=None)),
))
    )
    member_record_error_report = sgqlc.types.Field(sgqlc.types.non_null(MemberRecordErrorReport), graphql_name='memberRecordErrorReport', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(ReportFilter), graphql_name='filter', default=None)),
))
    )
    member_record_visit_total = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('VisitTotal'))), graphql_name='memberRecordVisitTotal', args=sgqlc.types.ArgDict((
        ('type', sgqlc.types.Arg(sgqlc.types.non_null(VisitTotalType), graphql_name='type', default=None)),
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(ReportFilter), graphql_name='filter', default=None)),
))
    )
    member_record_identity_distribution = sgqlc.types.Field(sgqlc.types.non_null(MemberRecordIdentityDistribution), graphql_name='memberRecordIdentityDistribution', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(ReportFilter), graphql_name='filter', default=None)),
))
    )
    member_record_access_visit_total = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AccessVisitTotal))), graphql_name='memberRecordAccessVisitTotal', args=sgqlc.types.ArgDict((
        ('type', sgqlc.types.Arg(sgqlc.types.non_null(VisitTotalType), graphql_name='type', default=None)),
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(AccessReportFilter), graphql_name='filter', default=None)),
))
    )
    tasks = sgqlc.types.Field(sgqlc.types.non_null(ListResponse), graphql_name='tasks', args=sgqlc.types.ArgDict((
        ('page', sgqlc.types.Arg(sgqlc.types.non_null(Page), graphql_name='page', default=None)),
        ('filter', sgqlc.types.Arg(TaskFilter, graphql_name='filter', default=None)),
))
    )
    has_unread_notification = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasUnreadNotification')
    notifications = sgqlc.types.Field(sgqlc.types.non_null(ListResponse), graphql_name='notifications', args=sgqlc.types.ArgDict((
        ('page', sgqlc.types.Arg(sgqlc.types.non_null(Page), graphql_name='page', default=None)),
        ('filter', sgqlc.types.Arg(NotificationFilter, graphql_name='filter', default=None)),
))
    )
    calendar_template = sgqlc.types.Field(sgqlc.types.non_null(Excel), graphql_name='calendarTemplate')
    attendance_setting = sgqlc.types.Field(sgqlc.types.non_null('AttendanceSetting'), graphql_name='attendanceSetting')
    daily_attendance = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('DailyAttendance'))), graphql_name='dailyAttendance', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(DailyAttendanceFilter), graphql_name='filter', default=None)),
))
    )
    monthly_attendance = sgqlc.types.Field(sgqlc.types.non_null(ListResponse), graphql_name='monthlyAttendance', args=sgqlc.types.ArgDict((
        ('page', sgqlc.types.Arg(sgqlc.types.non_null(Page), graphql_name='page', default=None)),
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(MonthlyAttendanceFilter), graphql_name='filter', default=None)),
))
    )
    daily_attendance_total = sgqlc.types.Field(DailyAttendanceTotal, graphql_name='dailyAttendanceTotal', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(DailyAttendanceFilter), graphql_name='filter', default=None)),
))
    )
    export_daily_attendance = sgqlc.types.Field(sgqlc.types.non_null(Excel), graphql_name='exportDailyAttendance', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(DailyAttendanceFilter), graphql_name='filter', default=None)),
))
    )
    export_monthly_attendance = sgqlc.types.Field(sgqlc.types.non_null(Excel), graphql_name='exportMonthlyAttendance', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(MonthlyAttendanceFilter), graphql_name='filter', default=None)),
        ('ids', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='ids', default=None)),
))
    )


class SyncClock(sgqlc.types.Type):
    __schema__ = seely_schema
    __field_names__ = ('clock', 'timezone')
    clock = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='clock')
    timezone = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='timezone')


class SyncData(sgqlc.types.Type):
    __schema__ = seely_schema
    __field_names__ = ('latest', 'edit', 'delete', 'timezone')
    latest = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='latest')
    edit = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('SyncVisitor')), graphql_name='edit')
    delete = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='delete')
    timezone = sgqlc.types.Field(String, graphql_name='timezone')


class SyncDateSchedule(sgqlc.types.Type):
    __schema__ = seely_schema
    __field_names__ = ('date', 'start', 'end')
    date = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='date')
    start = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='start')
    end = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='end')


class SyncIds(sgqlc.types.Type):
    __schema__ = seely_schema
    __field_names__ = ('edit', 'delete', 'latest')
    edit = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='edit')
    delete = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='delete')
    latest = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='latest')


class SyncSchedule(sgqlc.types.Type):
    __schema__ = seely_schema
    __field_names__ = ('day', 'start', 'end')
    day = sgqlc.types.Field(sgqlc.types.non_null(Day), graphql_name='day')
    start = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='start')
    end = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='end')


class TableConfig(sgqlc.types.Type):
    __schema__ = seely_schema
    __field_names__ = ('page_size', 'fields')
    page_size = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='pageSize')
    fields = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TableField'))), graphql_name='fields')


class TagDevices(sgqlc.types.Type):
    __schema__ = seely_schema
    __field_names__ = ('name', 'devices')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    devices = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Device'))), graphql_name='devices')


class UploadImage(sgqlc.types.Type):
    __schema__ = seely_schema
    __field_names__ = ('image',)
    image = sgqlc.types.Field(sgqlc.types.non_null('Photo'), graphql_name='image')


class UploadMemberError(sgqlc.types.Type):
    __schema__ = seely_schema
    __field_names__ = ('row', 'reason')
    row = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='row')
    reason = sgqlc.types.Field(sgqlc.types.non_null(UploadMemberFailReason), graphql_name='reason')


class UploadPhotoFailError(sgqlc.types.Type):
    __schema__ = seely_schema
    __field_names__ = ('name', 'reason')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    reason = sgqlc.types.Field(sgqlc.types.non_null(UploadPhotoFailReason), graphql_name='reason')


class UploadVideo(sgqlc.types.Type):
    __schema__ = seely_schema
    __field_names__ = ('video',)
    video = sgqlc.types.Field(sgqlc.types.non_null('Video'), graphql_name='video')


class VehicleIdentity(sgqlc.types.Type):
    __schema__ = seely_schema
    __field_names__ = ('type', 'department')
    type = sgqlc.types.Field(sgqlc.types.non_null(IdentityType), graphql_name='type')
    department = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('Department')), graphql_name='department')


class VisitCheckoutConfig(sgqlc.types.Type):
    __schema__ = seely_schema
    __field_names__ = ('enable', 'timestamp')
    enable = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='enable')
    timestamp = sgqlc.types.Field(Timestamp, graphql_name='timestamp')


class VisitConfig(sgqlc.types.Type):
    __schema__ = seely_schema
    __field_names__ = ('checkout_config',)
    checkout_config = sgqlc.types.Field(sgqlc.types.non_null(VisitCheckoutConfig), graphql_name='checkoutConfig')


class VisitTotal(sgqlc.types.Type):
    __schema__ = seely_schema
    __field_names__ = ('name', 'normal', 'abnormal')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    normal = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='normal')
    abnormal = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='abnormal')


class WeChatUser(sgqlc.types.Type):
    __schema__ = seely_schema
    __field_names__ = ('wechat_id', 'name', 'phone', 'company', 'department', 'email', 'photo', 'id_type', 'id_number', 'plate', 'is_updated')
    wechat_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='wechatId')
    name = sgqlc.types.Field(String, graphql_name='name')
    phone = sgqlc.types.Field(String, graphql_name='phone')
    company = sgqlc.types.Field(String, graphql_name='company')
    department = sgqlc.types.Field(String, graphql_name='department')
    email = sgqlc.types.Field(String, graphql_name='email')
    photo = sgqlc.types.Field('Photo', graphql_name='photo')
    id_type = sgqlc.types.Field(IDType, graphql_name='idType')
    id_number = sgqlc.types.Field(String, graphql_name='idNumber')
    plate = sgqlc.types.Field(String, graphql_name='plate')
    is_updated = sgqlc.types.Field(Boolean, graphql_name='isUpdated')


class AttendanceSetting(sgqlc.types.Type, IDNode):
    __schema__ = seely_schema
    __field_names__ = ('str_time_in', 'str_time_out', 'str_over_time_point', 'str_over_time_unit', 'str_leave_time_unit')
    str_time_in = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='strTimeIn')
    str_time_out = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='strTimeOut')
    str_over_time_point = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='strOverTimePoint')
    str_over_time_unit = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='strOverTimeUnit')
    str_leave_time_unit = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='strLeaveTimeUnit')


class Blacklist(sgqlc.types.Type, IDNode):
    __schema__ = seely_schema
    __field_names__ = ('name', 'photo', 'remark', 'last_seen')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    photo = sgqlc.types.Field('Photo', graphql_name='photo')
    remark = sgqlc.types.Field(String, graphql_name='remark')
    last_seen = sgqlc.types.Field(Timestamp, graphql_name='lastSeen')


class DailyAttendance(sgqlc.types.Type, IDNode):
    __schema__ = seely_schema
    __field_names__ = ('year', 'month', 'day_of_month', 'day_of_week', 'day_type', 'member_id', 'o_absence', 'f_absence', 'o_annual_leave', 'f_annual_leave', 'o_early_leave', 'f_early_leave', 'o_early_leave_min', 'f_early_leave_min', 'o_funeral_leave', 'f_funeral_leave', 'o_late', 'f_late', 'o_late_min', 'f_late_min', 'o_leave_of_absence', 'f_leave_of_absence', 'o_sick_leave', 'f_sick_leave', 'o_wedding_leave', 'f_wedding_leave', 'over_hour_of_holiday', 'f_over_hour_of_holiday', 'over_hour_of_weekend', 'f_over_hour_of_weekend', 'over_hour_of_workingday', 'f_over_hour_of_workingday', 'time_in', 'time_out', 'f_time_in', 'f_time_out', 'remarks')
    year = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='year')
    month = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='month')
    day_of_month = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='dayOfMonth')
    day_of_week = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='dayOfWeek')
    day_type = sgqlc.types.Field(sgqlc.types.non_null(CalendarType), graphql_name='dayType')
    member_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='memberId')
    o_absence = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='oAbsence')
    f_absence = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='fAbsence')
    o_annual_leave = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='oAnnualLeave')
    f_annual_leave = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='fAnnualLeave')
    o_early_leave = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='oEarlyLeave')
    f_early_leave = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='fEarlyLeave')
    o_early_leave_min = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='oEarlyLeaveMin')
    f_early_leave_min = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='fEarlyLeaveMin')
    o_funeral_leave = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='oFuneralLeave')
    f_funeral_leave = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='fFuneralLeave')
    o_late = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='oLate')
    f_late = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='fLate')
    o_late_min = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='oLateMin')
    f_late_min = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='fLateMin')
    o_leave_of_absence = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='oLeaveOfAbsence')
    f_leave_of_absence = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='fLeaveOfAbsence')
    o_sick_leave = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='oSickLeave')
    f_sick_leave = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='fSickLeave')
    o_wedding_leave = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='oWeddingLeave')
    f_wedding_leave = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='fWeddingLeave')
    over_hour_of_holiday = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='overHourOfHoliday')
    f_over_hour_of_holiday = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='fOverHourOfHoliday')
    over_hour_of_weekend = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='overHourOfWeekend')
    f_over_hour_of_weekend = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='fOverHourOfWeekend')
    over_hour_of_workingday = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='overHourOfWorkingday')
    f_over_hour_of_workingday = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='fOverHourOfWorkingday')
    time_in = sgqlc.types.Field(Timestamp, graphql_name='timeIn')
    time_out = sgqlc.types.Field(Timestamp, graphql_name='timeOut')
    f_time_in = sgqlc.types.Field(String, graphql_name='fTimeIn')
    f_time_out = sgqlc.types.Field(String, graphql_name='fTimeOut')
    remarks = sgqlc.types.Field(String, graphql_name='remarks')


class Department(sgqlc.types.Type, IDNode):
    __schema__ = seely_schema
    __field_names__ = ('name', 'member_count')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    member_count = sgqlc.types.Field(Int, graphql_name='memberCount')


class Device(sgqlc.types.Type, IDNode):
    __schema__ = seely_schema
    __field_names__ = ('uuid', 'name', 'type', 'model', 'location', 'version', 'organization', 'last_seen', 'status', 'url', 'used_for', 'tags', 'timezone', 'show_username', 'show_face_rect', 'enable_screen_saver', 'screen_saver_time', 'screen_saver_photo', 'audio', 'config')
    uuid = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='uuid')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    type = sgqlc.types.Field(sgqlc.types.non_null(DeviceType), graphql_name='type')
    model = sgqlc.types.Field(String, graphql_name='model')
    location = sgqlc.types.Field(String, graphql_name='location')
    version = sgqlc.types.Field(String, graphql_name='version')
    organization = sgqlc.types.Field('Organization', graphql_name='organization')
    last_seen = sgqlc.types.Field(Timestamp, graphql_name='lastSeen')
    status = sgqlc.types.Field(DeviceStatus, graphql_name='status')
    url = sgqlc.types.Field(String, graphql_name='url')
    used_for = sgqlc.types.Field(DeviceUsedFor, graphql_name='usedFor')
    tags = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='tags')
    timezone = sgqlc.types.Field(String, graphql_name='timezone')
    show_username = sgqlc.types.Field(Boolean, graphql_name='showUsername')
    show_face_rect = sgqlc.types.Field(Boolean, graphql_name='showFaceRect')
    enable_screen_saver = sgqlc.types.Field(Boolean, graphql_name='enableScreenSaver')
    screen_saver_time = sgqlc.types.Field(Int, graphql_name='screenSaverTime')
    screen_saver_photo = sgqlc.types.Field('Photo', graphql_name='screenSaverPhoto')
    audio = sgqlc.types.Field('Video', graphql_name='audio')
    config = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(FieldValue)), graphql_name='config')


class EditableBool(sgqlc.types.Type, EditableValue):
    __schema__ = seely_schema
    __field_names__ = ('value',)
    value = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='value')


class EnhancedPhoto(sgqlc.types.Type, IDNode):
    __schema__ = seely_schema
    __field_names__ = ('src', 'name', 'thumbnail', 'feature')
    src = sgqlc.types.Field(String, graphql_name='src')
    name = sgqlc.types.Field(String, graphql_name='name')
    thumbnail = sgqlc.types.Field(String, graphql_name='thumbnail')
    feature = sgqlc.types.Field(String, graphql_name='feature')


class Event(sgqlc.types.Type, IDNode):
    __schema__ = seely_schema
    __field_names__ = ('visitor', 'status', 'target', 'target_organization', 'notify_target', 'reason', 'book_time', 'deadline', 'arrival_time', 'leave_time', 'derived', 'partners', 'qrcode', 'permissions')
    visitor = sgqlc.types.Field(sgqlc.types.non_null(EventVisitor), graphql_name='visitor')
    status = sgqlc.types.Field(sgqlc.types.non_null(EventStatus), graphql_name='status')
    target = sgqlc.types.Field('Member', graphql_name='target')
    target_organization = sgqlc.types.Field('Organization', graphql_name='targetOrganization')
    notify_target = sgqlc.types.Field(Boolean, graphql_name='notifyTarget')
    reason = sgqlc.types.Field(VisitReason, graphql_name='reason')
    book_time = sgqlc.types.Field(Timestamp, graphql_name='bookTime')
    deadline = sgqlc.types.Field(Timestamp, graphql_name='deadline')
    arrival_time = sgqlc.types.Field(Timestamp, graphql_name='arrivalTime')
    leave_time = sgqlc.types.Field(Timestamp, graphql_name='leaveTime')
    derived = sgqlc.types.Field('Event', graphql_name='derived')
    partners = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='partners')
    qrcode = sgqlc.types.Field(String, graphql_name='qrcode')
    permissions = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('MemberPermission')), graphql_name='permissions')


class File(sgqlc.types.Type, IDNode):
    __schema__ = seely_schema
    __field_names__ = ('src', 'name')
    src = sgqlc.types.Field(String, graphql_name='src')
    name = sgqlc.types.Field(String, graphql_name='name')


class FormField(sgqlc.types.Type, Field):
    __schema__ = seely_schema
    __field_names__ = ('order', 'major', 'custom', 'select_options')
    order = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='order')
    major = sgqlc.types.Field(sgqlc.types.non_null(EditableBool), graphql_name='major')
    custom = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='custom')
    select_options = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='selectOptions')


class JobLevel(sgqlc.types.Type, IDNode):
    __schema__ = seely_schema
    __field_names__ = ('name', 'member_count')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    member_count = sgqlc.types.Field(Int, graphql_name='memberCount')


class Member(sgqlc.types.Type, IDNode):
    __schema__ = seely_schema
    __field_names__ = ('name', 'status', 'phone', 'role', 'photo', 'id_card', 'serial_number', 'email', 'door_card_number', 'permissions', 'tags', 'greeting', 'display_name', 'campus', 'branch', 'department', 'job_level', 'title', 'hire_date', 'probation', 'correction_time', 'remove_time', 'organization', 'extra_data')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    status = sgqlc.types.Field(sgqlc.types.non_null(MemberStatus), graphql_name='status')
    phone = sgqlc.types.Field(String, graphql_name='phone')
    role = sgqlc.types.Field('Role', graphql_name='role')
    photo = sgqlc.types.Field('Photo', graphql_name='photo')
    id_card = sgqlc.types.Field(String, graphql_name='idCard')
    serial_number = sgqlc.types.Field(String, graphql_name='serialNumber')
    email = sgqlc.types.Field(String, graphql_name='email')
    door_card_number = sgqlc.types.Field(String, graphql_name='doorCardNumber')
    permissions = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('MemberPermission')), graphql_name='permissions')
    tags = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='tags')
    greeting = sgqlc.types.Field(String, graphql_name='greeting')
    display_name = sgqlc.types.Field(String, graphql_name='displayName')
    campus = sgqlc.types.Field(String, graphql_name='campus')
    branch = sgqlc.types.Field(String, graphql_name='branch')
    department = sgqlc.types.Field(Department, graphql_name='department')
    job_level = sgqlc.types.Field(JobLevel, graphql_name='jobLevel')
    title = sgqlc.types.Field('Title', graphql_name='title')
    hire_date = sgqlc.types.Field(Timestamp, graphql_name='hireDate')
    probation = sgqlc.types.Field(Boolean, graphql_name='probation')
    correction_time = sgqlc.types.Field(Timestamp, graphql_name='correctionTime')
    remove_time = sgqlc.types.Field(Timestamp, graphql_name='removeTime')
    organization = sgqlc.types.Field('Organization', graphql_name='organization')
    extra_data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(FieldValue)), graphql_name='extraData')


class MemberPermission(sgqlc.types.Type, IDNode):
    __schema__ = seely_schema
    __field_names__ = ('name', 'apply_all', 'is_general', 'schedule_type', 'schedules', 'departments', 'devices', 'remarks')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    apply_all = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='applyAll')
    is_general = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isGeneral')
    schedule_type = sgqlc.types.Field(sgqlc.types.non_null(ScheduleType), graphql_name='scheduleType')
    schedules = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(PermissionSchedule)), graphql_name='schedules')
    departments = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Department)), graphql_name='departments')
    devices = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Device)), graphql_name='devices')
    remarks = sgqlc.types.Field(String, graphql_name='remarks')


class MemberRecord(sgqlc.types.Type, IDNode):
    __schema__ = seely_schema
    __field_names__ = ('start', 'device', 'identity', 'access_type', 'capture', 'video', 'member', 'visitor', 'temperature', 'distance')
    start = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='start')
    device = sgqlc.types.Field(sgqlc.types.non_null(Device), graphql_name='device')
    identity = sgqlc.types.Field(sgqlc.types.non_null(MemberIdentity), graphql_name='identity')
    access_type = sgqlc.types.Field(sgqlc.types.non_null(AccessType), graphql_name='accessType')
    capture = sgqlc.types.Field('Photo', graphql_name='capture')
    video = sgqlc.types.Field('Video', graphql_name='video')
    member = sgqlc.types.Field(Member, graphql_name='member')
    visitor = sgqlc.types.Field(EventVisitor, graphql_name='visitor')
    temperature = sgqlc.types.Field(Float, graphql_name='temperature')
    distance = sgqlc.types.Field(Float, graphql_name='distance')


class MonthlyAttendance(sgqlc.types.Type, IDNode):
    __schema__ = seely_schema
    __field_names__ = ('serial_number', 'title', 'name', 'department', 'late_times', 'late_min', 'early_leave_times', 'early_leave_min', 'absence_times', 'absence_leave_times', 'annual_leave', 'funeral_leave', 'wedding_leave', 'sick_leave_times', 'welfare_leave', 'over_hour_of_holiday', 'over_hour_of_weekend', 'over_hour_of_workingday', 'over_hour_of_holiday_total', 'over_hour_of_weekend_total', 'over_hour_of_workingday_total')
    serial_number = sgqlc.types.Field(String, graphql_name='serialNumber')
    title = sgqlc.types.Field(String, graphql_name='title')
    name = sgqlc.types.Field(String, graphql_name='name')
    department = sgqlc.types.Field(String, graphql_name='department')
    late_times = sgqlc.types.Field(Int, graphql_name='lateTimes')
    late_min = sgqlc.types.Field(Int, graphql_name='lateMin')
    early_leave_times = sgqlc.types.Field(Int, graphql_name='earlyLeaveTimes')
    early_leave_min = sgqlc.types.Field(Int, graphql_name='earlyLeaveMin')
    absence_times = sgqlc.types.Field(Int, graphql_name='absenceTimes')
    absence_leave_times = sgqlc.types.Field(Float, graphql_name='absenceLeaveTimes')
    annual_leave = sgqlc.types.Field(Float, graphql_name='annualLeave')
    funeral_leave = sgqlc.types.Field(Float, graphql_name='funeralLeave')
    wedding_leave = sgqlc.types.Field(Float, graphql_name='weddingLeave')
    sick_leave_times = sgqlc.types.Field(Float, graphql_name='sickLeaveTimes')
    welfare_leave = sgqlc.types.Field(Float, graphql_name='welfareLeave')
    over_hour_of_holiday = sgqlc.types.Field(Float, graphql_name='overHourOfHoliday')
    over_hour_of_weekend = sgqlc.types.Field(Float, graphql_name='overHourOfWeekend')
    over_hour_of_workingday = sgqlc.types.Field(Float, graphql_name='overHourOfWorkingday')
    over_hour_of_holiday_total = sgqlc.types.Field(Float, graphql_name='overHourOfHolidayTotal')
    over_hour_of_weekend_total = sgqlc.types.Field(Float, graphql_name='overHourOfWeekendTotal')
    over_hour_of_workingday_total = sgqlc.types.Field(Float, graphql_name='overHourOfWorkingdayTotal')


class Notification(sgqlc.types.Type, IDNode):
    __schema__ = seely_schema
    __field_names__ = ('category', 'type', 'is_read', 'time', 'content')
    category = sgqlc.types.Field(sgqlc.types.non_null(NotificationCategory), graphql_name='category')
    type = sgqlc.types.Field(sgqlc.types.non_null(NotificationType), graphql_name='type')
    is_read = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isRead')
    time = sgqlc.types.Field(Timestamp, graphql_name='time')
    content = sgqlc.types.Field(JSONString, graphql_name='content')


class OperationData(sgqlc.types.Type, OperationDataInterface):
    __schema__ = seely_schema
    __field_names__ = ()


class OperationLog(sgqlc.types.Type, IDNode):
    __schema__ = seely_schema
    __field_names__ = ('organization_id', 'username', 'role', 'module', 'time', 'action', 'object', 'count', 'data')
    organization_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='organizationId')
    username = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='username')
    role = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='role')
    module = sgqlc.types.Field(sgqlc.types.non_null(SystemModule), graphql_name='module')
    time = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='time')
    action = sgqlc.types.Field(OperationAction, graphql_name='action')
    object = sgqlc.types.Field(OperationObject, graphql_name='object')
    count = sgqlc.types.Field(Int, graphql_name='count')
    data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(OperationDataInterface)), graphql_name='data')


class Organization(sgqlc.types.Type, IDNode):
    __schema__ = seely_schema
    __field_names__ = ('name', 'type', 'timezone', 'short_name', 'address', 'province', 'city', 'district', 'greetings')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    type = sgqlc.types.Field(sgqlc.types.non_null(OrganizationType), graphql_name='type')
    timezone = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='timezone')
    short_name = sgqlc.types.Field(String, graphql_name='shortName')
    address = sgqlc.types.Field(String, graphql_name='address')
    province = sgqlc.types.Field(Province, graphql_name='province')
    city = sgqlc.types.Field(City, graphql_name='city')
    district = sgqlc.types.Field(District, graphql_name='district')
    greetings = sgqlc.types.Field(Greetings, graphql_name='greetings')


class OtherPerson(sgqlc.types.Type, IDNode):
    __schema__ = seely_schema
    __field_names__ = ('name', 'photo', 'phone', 'id_card', 'serial_number', 'email', 'door_card_number', 'permissions', 'tags', 'greeting', 'display_name', 'remove_time', 'extra_data')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    photo = sgqlc.types.Field('Photo', graphql_name='photo')
    phone = sgqlc.types.Field(String, graphql_name='phone')
    id_card = sgqlc.types.Field(String, graphql_name='idCard')
    serial_number = sgqlc.types.Field(String, graphql_name='serialNumber')
    email = sgqlc.types.Field(String, graphql_name='email')
    door_card_number = sgqlc.types.Field(String, graphql_name='doorCardNumber')
    permissions = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(MemberPermission)), graphql_name='permissions')
    tags = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='tags')
    greeting = sgqlc.types.Field(String, graphql_name='greeting')
    display_name = sgqlc.types.Field(String, graphql_name='displayName')
    remove_time = sgqlc.types.Field(Timestamp, graphql_name='removeTime')
    extra_data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(FieldValue)), graphql_name='extraData')


class Photo(sgqlc.types.Type, IDNode):
    __schema__ = seely_schema
    __field_names__ = ('src', 'name', 'thumbnail')
    src = sgqlc.types.Field(String, graphql_name='src')
    name = sgqlc.types.Field(String, graphql_name='name')
    thumbnail = sgqlc.types.Field(String, graphql_name='thumbnail')


class Role(sgqlc.types.Type, IDNode):
    __schema__ = seely_schema
    __field_names__ = ('name', 'is_admin')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    is_admin = sgqlc.types.Field(Boolean, graphql_name='isAdmin')


class StaticResourceOpData(sgqlc.types.Type, OperationDataInterface):
    __schema__ = seely_schema
    __field_names__ = ('filename', 'link')
    filename = sgqlc.types.Field(String, graphql_name='filename')
    link = sgqlc.types.Field(String, graphql_name='link')


class SyncMember(sgqlc.types.Type, IDNode):
    __schema__ = seely_schema
    __field_names__ = ('name', 'type', 'uuid', 'is_active', 'organization_id', 'serial_number', 'door_card_number', 'greeting', 'schedules', 'department', 'job_level', 'title', 'avatar', 'photos', 'extra_data', 'timezone')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    type = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='type')
    uuid = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='uuid')
    is_active = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isActive')
    organization_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='organizationId')
    serial_number = sgqlc.types.Field(String, graphql_name='serialNumber')
    door_card_number = sgqlc.types.Field(String, graphql_name='doorCardNumber')
    greeting = sgqlc.types.Field(String, graphql_name='greeting')
    schedules = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(SyncSchedule))), graphql_name='schedules')
    department = sgqlc.types.Field(String, graphql_name='department')
    job_level = sgqlc.types.Field(String, graphql_name='jobLevel')
    title = sgqlc.types.Field(String, graphql_name='title')
    avatar = sgqlc.types.Field(EnhancedPhoto, graphql_name='avatar')
    photos = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(EnhancedPhoto)), graphql_name='photos')
    extra_data = sgqlc.types.Field(String, graphql_name='extraData')
    timezone = sgqlc.types.Field(String, graphql_name='timezone')


class SyncVisitor(sgqlc.types.Type, IDNode):
    __schema__ = seely_schema
    __field_names__ = ('name', 'target', 'schedules', 'avatar', 'photos', 'door_card_number')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    target = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='target')
    schedules = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(SyncDateSchedule))), graphql_name='schedules')
    avatar = sgqlc.types.Field(EnhancedPhoto, graphql_name='avatar')
    photos = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(EnhancedPhoto)), graphql_name='photos')
    door_card_number = sgqlc.types.Field(String, graphql_name='doorCardNumber')


class TableField(sgqlc.types.Type, Field):
    __schema__ = seely_schema
    __field_names__ = ('visible', 'order', 'select_options')
    visible = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='visible')
    order = sgqlc.types.Field(Int, graphql_name='order')
    select_options = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='selectOptions')


class Tag(sgqlc.types.Type, IDNode):
    __schema__ = seely_schema
    __field_names__ = ('name', 'type', 'organization_id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    type = sgqlc.types.Field(sgqlc.types.non_null(TagType), graphql_name='type')
    organization_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='organizationId')


class Task(sgqlc.types.Type, IDNode):
    __schema__ = seely_schema
    __field_names__ = ('type', 'status', 'created', 'file', 'extra')
    type = sgqlc.types.Field(sgqlc.types.non_null(TaskType), graphql_name='type')
    status = sgqlc.types.Field(sgqlc.types.non_null(TaskStatus), graphql_name='status')
    created = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='created')
    file = sgqlc.types.Field(File, graphql_name='file')
    extra = sgqlc.types.Field(JSONString, graphql_name='extra')


class TimeRangeOpData(sgqlc.types.Type, OperationDataInterface):
    __schema__ = seely_schema
    __field_names__ = ('start', 'end')
    start = sgqlc.types.Field(Timestamp, graphql_name='start')
    end = sgqlc.types.Field(Timestamp, graphql_name='end')


class Title(sgqlc.types.Type, IDNode):
    __schema__ = seely_schema
    __field_names__ = ('name', 'member_count')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    member_count = sgqlc.types.Field(Int, graphql_name='memberCount')


class UpdateOpData(sgqlc.types.Type, OperationDataInterface):
    __schema__ = seely_schema
    __field_names__ = ('content',)
    content = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ContentUnit)), graphql_name='content')


class User(sgqlc.types.Type, IDNode):
    __schema__ = seely_schema
    __field_names__ = ('account', 'username', 'is_active', 'roles', 'managed_organization', 'has_wechat', 'phone', 'company_id', 'photo', 'last_login', 'permissions', 'related_member_id', 'language')
    account = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='account')
    username = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='username')
    is_active = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isActive')
    roles = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Role))), graphql_name='roles')
    managed_organization = sgqlc.types.Field(sgqlc.types.non_null(Organization), graphql_name='managedOrganization')
    has_wechat = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasWechat')
    phone = sgqlc.types.Field(String, graphql_name='phone')
    company_id = sgqlc.types.Field(ID, graphql_name='companyId')
    photo = sgqlc.types.Field(Photo, graphql_name='photo')
    last_login = sgqlc.types.Field(Timestamp, graphql_name='lastLogin')
    permissions = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='permissions')
    related_member_id = sgqlc.types.Field(ID, graphql_name='relatedMemberId')
    language = sgqlc.types.Field(String, graphql_name='language')


class Vehicle(sgqlc.types.Type, IDNode):
    __schema__ = seely_schema
    __field_names__ = ('license_plate', 'owner', 'phone', 'is_active', 'tags', 'member')
    license_plate = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='licensePlate')
    owner = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='owner')
    phone = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='phone')
    is_active = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isActive')
    tags = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='tags')
    member = sgqlc.types.Field(Member, graphql_name='member')


class VehicleRecord(sgqlc.types.Type, IDNode):
    __schema__ = seely_schema
    __field_names__ = ('start', 'device', 'identity', 'license_plate', 'vehicle', 'visitor')
    start = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='start')
    device = sgqlc.types.Field(sgqlc.types.non_null(Device), graphql_name='device')
    identity = sgqlc.types.Field(sgqlc.types.non_null(VehicleIdentity), graphql_name='identity')
    license_plate = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='licensePlate')
    vehicle = sgqlc.types.Field(Vehicle, graphql_name='vehicle')
    visitor = sgqlc.types.Field(EventVisitor, graphql_name='visitor')


class Video(sgqlc.types.Type, IDNode):
    __schema__ = seely_schema
    __field_names__ = ('src', 'name')
    src = sgqlc.types.Field(String, graphql_name='src')
    name = sgqlc.types.Field(String, graphql_name='name')


class VisitEventOpData(sgqlc.types.Type, OperationDataInterface):
    __schema__ = seely_schema
    __field_names__ = ('visitor', 'target')
    visitor = sgqlc.types.Field(String, graphql_name='visitor')
    target = sgqlc.types.Field(String, graphql_name='target')


class Visitor(sgqlc.types.Type, IDNode):
    __schema__ = seely_schema
    __field_names__ = ('phone', 'name', 'email', 'id_type', 'id_number', 'plate', 'photo', 'company', 'department')
    phone = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='phone')
    name = sgqlc.types.Field(String, graphql_name='name')
    email = sgqlc.types.Field(String, graphql_name='email')
    id_type = sgqlc.types.Field(IDType, graphql_name='idType')
    id_number = sgqlc.types.Field(String, graphql_name='idNumber')
    plate = sgqlc.types.Field(String, graphql_name='plate')
    photo = sgqlc.types.Field(Photo, graphql_name='photo')
    company = sgqlc.types.Field(String, graphql_name='company')
    department = sgqlc.types.Field(String, graphql_name='department')



########################################################################
# Unions
########################################################################

########################################################################
# Schema Entry Points
########################################################################
seely_schema.query_type = Query
seely_schema.mutation_type = Mutation
seely_schema.subscription_type = None

