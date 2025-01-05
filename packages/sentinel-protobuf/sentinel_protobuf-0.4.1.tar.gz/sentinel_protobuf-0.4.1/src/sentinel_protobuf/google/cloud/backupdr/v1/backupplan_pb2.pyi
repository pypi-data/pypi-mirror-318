from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import field_info_pb2 as _field_info_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.type import dayofweek_pb2 as _dayofweek_pb2
from google.type import month_pb2 as _month_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class BackupPlan(_message.Message):
    __slots__ = ('name', 'description', 'labels', 'create_time', 'update_time', 'backup_rules', 'state', 'resource_type', 'etag', 'backup_vault', 'backup_vault_service_account')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[BackupPlan.State]
        CREATING: _ClassVar[BackupPlan.State]
        ACTIVE: _ClassVar[BackupPlan.State]
        DELETING: _ClassVar[BackupPlan.State]
        INACTIVE: _ClassVar[BackupPlan.State]
    STATE_UNSPECIFIED: BackupPlan.State
    CREATING: BackupPlan.State
    ACTIVE: BackupPlan.State
    DELETING: BackupPlan.State
    INACTIVE: BackupPlan.State

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    BACKUP_RULES_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    BACKUP_VAULT_FIELD_NUMBER: _ClassVar[int]
    BACKUP_VAULT_SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    labels: _containers.ScalarMap[str, str]
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    backup_rules: _containers.RepeatedCompositeFieldContainer[BackupRule]
    state: BackupPlan.State
    resource_type: str
    etag: str
    backup_vault: str
    backup_vault_service_account: str

    def __init__(self, name: _Optional[str]=..., description: _Optional[str]=..., labels: _Optional[_Mapping[str, str]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., backup_rules: _Optional[_Iterable[_Union[BackupRule, _Mapping]]]=..., state: _Optional[_Union[BackupPlan.State, str]]=..., resource_type: _Optional[str]=..., etag: _Optional[str]=..., backup_vault: _Optional[str]=..., backup_vault_service_account: _Optional[str]=...) -> None:
        ...

class BackupRule(_message.Message):
    __slots__ = ('rule_id', 'backup_retention_days', 'standard_schedule')
    RULE_ID_FIELD_NUMBER: _ClassVar[int]
    BACKUP_RETENTION_DAYS_FIELD_NUMBER: _ClassVar[int]
    STANDARD_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    rule_id: str
    backup_retention_days: int
    standard_schedule: StandardSchedule

    def __init__(self, rule_id: _Optional[str]=..., backup_retention_days: _Optional[int]=..., standard_schedule: _Optional[_Union[StandardSchedule, _Mapping]]=...) -> None:
        ...

class StandardSchedule(_message.Message):
    __slots__ = ('recurrence_type', 'hourly_frequency', 'days_of_week', 'days_of_month', 'week_day_of_month', 'months', 'backup_window', 'time_zone')

    class RecurrenceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RECURRENCE_TYPE_UNSPECIFIED: _ClassVar[StandardSchedule.RecurrenceType]
        HOURLY: _ClassVar[StandardSchedule.RecurrenceType]
        DAILY: _ClassVar[StandardSchedule.RecurrenceType]
        WEEKLY: _ClassVar[StandardSchedule.RecurrenceType]
        MONTHLY: _ClassVar[StandardSchedule.RecurrenceType]
        YEARLY: _ClassVar[StandardSchedule.RecurrenceType]
    RECURRENCE_TYPE_UNSPECIFIED: StandardSchedule.RecurrenceType
    HOURLY: StandardSchedule.RecurrenceType
    DAILY: StandardSchedule.RecurrenceType
    WEEKLY: StandardSchedule.RecurrenceType
    MONTHLY: StandardSchedule.RecurrenceType
    YEARLY: StandardSchedule.RecurrenceType
    RECURRENCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    HOURLY_FREQUENCY_FIELD_NUMBER: _ClassVar[int]
    DAYS_OF_WEEK_FIELD_NUMBER: _ClassVar[int]
    DAYS_OF_MONTH_FIELD_NUMBER: _ClassVar[int]
    WEEK_DAY_OF_MONTH_FIELD_NUMBER: _ClassVar[int]
    MONTHS_FIELD_NUMBER: _ClassVar[int]
    BACKUP_WINDOW_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    recurrence_type: StandardSchedule.RecurrenceType
    hourly_frequency: int
    days_of_week: _containers.RepeatedScalarFieldContainer[_dayofweek_pb2.DayOfWeek]
    days_of_month: _containers.RepeatedScalarFieldContainer[int]
    week_day_of_month: WeekDayOfMonth
    months: _containers.RepeatedScalarFieldContainer[_month_pb2.Month]
    backup_window: BackupWindow
    time_zone: str

    def __init__(self, recurrence_type: _Optional[_Union[StandardSchedule.RecurrenceType, str]]=..., hourly_frequency: _Optional[int]=..., days_of_week: _Optional[_Iterable[_Union[_dayofweek_pb2.DayOfWeek, str]]]=..., days_of_month: _Optional[_Iterable[int]]=..., week_day_of_month: _Optional[_Union[WeekDayOfMonth, _Mapping]]=..., months: _Optional[_Iterable[_Union[_month_pb2.Month, str]]]=..., backup_window: _Optional[_Union[BackupWindow, _Mapping]]=..., time_zone: _Optional[str]=...) -> None:
        ...

class BackupWindow(_message.Message):
    __slots__ = ('start_hour_of_day', 'end_hour_of_day')
    START_HOUR_OF_DAY_FIELD_NUMBER: _ClassVar[int]
    END_HOUR_OF_DAY_FIELD_NUMBER: _ClassVar[int]
    start_hour_of_day: int
    end_hour_of_day: int

    def __init__(self, start_hour_of_day: _Optional[int]=..., end_hour_of_day: _Optional[int]=...) -> None:
        ...

class WeekDayOfMonth(_message.Message):
    __slots__ = ('week_of_month', 'day_of_week')

    class WeekOfMonth(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        WEEK_OF_MONTH_UNSPECIFIED: _ClassVar[WeekDayOfMonth.WeekOfMonth]
        FIRST: _ClassVar[WeekDayOfMonth.WeekOfMonth]
        SECOND: _ClassVar[WeekDayOfMonth.WeekOfMonth]
        THIRD: _ClassVar[WeekDayOfMonth.WeekOfMonth]
        FOURTH: _ClassVar[WeekDayOfMonth.WeekOfMonth]
        LAST: _ClassVar[WeekDayOfMonth.WeekOfMonth]
    WEEK_OF_MONTH_UNSPECIFIED: WeekDayOfMonth.WeekOfMonth
    FIRST: WeekDayOfMonth.WeekOfMonth
    SECOND: WeekDayOfMonth.WeekOfMonth
    THIRD: WeekDayOfMonth.WeekOfMonth
    FOURTH: WeekDayOfMonth.WeekOfMonth
    LAST: WeekDayOfMonth.WeekOfMonth
    WEEK_OF_MONTH_FIELD_NUMBER: _ClassVar[int]
    DAY_OF_WEEK_FIELD_NUMBER: _ClassVar[int]
    week_of_month: WeekDayOfMonth.WeekOfMonth
    day_of_week: _dayofweek_pb2.DayOfWeek

    def __init__(self, week_of_month: _Optional[_Union[WeekDayOfMonth.WeekOfMonth, str]]=..., day_of_week: _Optional[_Union[_dayofweek_pb2.DayOfWeek, str]]=...) -> None:
        ...

class CreateBackupPlanRequest(_message.Message):
    __slots__ = ('parent', 'backup_plan_id', 'backup_plan', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    BACKUP_PLAN_ID_FIELD_NUMBER: _ClassVar[int]
    BACKUP_PLAN_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    backup_plan_id: str
    backup_plan: BackupPlan
    request_id: str

    def __init__(self, parent: _Optional[str]=..., backup_plan_id: _Optional[str]=..., backup_plan: _Optional[_Union[BackupPlan, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class ListBackupPlansRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'order_by')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=...) -> None:
        ...

class ListBackupPlansResponse(_message.Message):
    __slots__ = ('backup_plans', 'next_page_token', 'unreachable')
    BACKUP_PLANS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    backup_plans: _containers.RepeatedCompositeFieldContainer[BackupPlan]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, backup_plans: _Optional[_Iterable[_Union[BackupPlan, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetBackupPlanRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class DeleteBackupPlanRequest(_message.Message):
    __slots__ = ('name', 'request_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=...) -> None:
        ...