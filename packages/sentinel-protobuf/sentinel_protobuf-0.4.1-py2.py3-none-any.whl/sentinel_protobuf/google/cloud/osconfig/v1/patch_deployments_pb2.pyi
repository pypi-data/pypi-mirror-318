from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.osconfig.v1 import patch_jobs_pb2 as _patch_jobs_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.type import datetime_pb2 as _datetime_pb2
from google.type import dayofweek_pb2 as _dayofweek_pb2
from google.type import timeofday_pb2 as _timeofday_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class PatchDeployment(_message.Message):
    __slots__ = ('name', 'description', 'instance_filter', 'patch_config', 'duration', 'one_time_schedule', 'recurring_schedule', 'create_time', 'update_time', 'last_execute_time', 'rollout', 'state')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[PatchDeployment.State]
        ACTIVE: _ClassVar[PatchDeployment.State]
        PAUSED: _ClassVar[PatchDeployment.State]
    STATE_UNSPECIFIED: PatchDeployment.State
    ACTIVE: PatchDeployment.State
    PAUSED: PatchDeployment.State
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FILTER_FIELD_NUMBER: _ClassVar[int]
    PATCH_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    ONE_TIME_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    RECURRING_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LAST_EXECUTE_TIME_FIELD_NUMBER: _ClassVar[int]
    ROLLOUT_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    instance_filter: _patch_jobs_pb2.PatchInstanceFilter
    patch_config: _patch_jobs_pb2.PatchConfig
    duration: _duration_pb2.Duration
    one_time_schedule: OneTimeSchedule
    recurring_schedule: RecurringSchedule
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    last_execute_time: _timestamp_pb2.Timestamp
    rollout: _patch_jobs_pb2.PatchRollout
    state: PatchDeployment.State

    def __init__(self, name: _Optional[str]=..., description: _Optional[str]=..., instance_filter: _Optional[_Union[_patch_jobs_pb2.PatchInstanceFilter, _Mapping]]=..., patch_config: _Optional[_Union[_patch_jobs_pb2.PatchConfig, _Mapping]]=..., duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., one_time_schedule: _Optional[_Union[OneTimeSchedule, _Mapping]]=..., recurring_schedule: _Optional[_Union[RecurringSchedule, _Mapping]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., last_execute_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., rollout: _Optional[_Union[_patch_jobs_pb2.PatchRollout, _Mapping]]=..., state: _Optional[_Union[PatchDeployment.State, str]]=...) -> None:
        ...

class OneTimeSchedule(_message.Message):
    __slots__ = ('execute_time',)
    EXECUTE_TIME_FIELD_NUMBER: _ClassVar[int]
    execute_time: _timestamp_pb2.Timestamp

    def __init__(self, execute_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class RecurringSchedule(_message.Message):
    __slots__ = ('time_zone', 'start_time', 'end_time', 'time_of_day', 'frequency', 'weekly', 'monthly', 'last_execute_time', 'next_execute_time')

    class Frequency(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FREQUENCY_UNSPECIFIED: _ClassVar[RecurringSchedule.Frequency]
        WEEKLY: _ClassVar[RecurringSchedule.Frequency]
        MONTHLY: _ClassVar[RecurringSchedule.Frequency]
        DAILY: _ClassVar[RecurringSchedule.Frequency]
    FREQUENCY_UNSPECIFIED: RecurringSchedule.Frequency
    WEEKLY: RecurringSchedule.Frequency
    MONTHLY: RecurringSchedule.Frequency
    DAILY: RecurringSchedule.Frequency
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    TIME_OF_DAY_FIELD_NUMBER: _ClassVar[int]
    FREQUENCY_FIELD_NUMBER: _ClassVar[int]
    WEEKLY_FIELD_NUMBER: _ClassVar[int]
    MONTHLY_FIELD_NUMBER: _ClassVar[int]
    LAST_EXECUTE_TIME_FIELD_NUMBER: _ClassVar[int]
    NEXT_EXECUTE_TIME_FIELD_NUMBER: _ClassVar[int]
    time_zone: _datetime_pb2.TimeZone
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    time_of_day: _timeofday_pb2.TimeOfDay
    frequency: RecurringSchedule.Frequency
    weekly: WeeklySchedule
    monthly: MonthlySchedule
    last_execute_time: _timestamp_pb2.Timestamp
    next_execute_time: _timestamp_pb2.Timestamp

    def __init__(self, time_zone: _Optional[_Union[_datetime_pb2.TimeZone, _Mapping]]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., time_of_day: _Optional[_Union[_timeofday_pb2.TimeOfDay, _Mapping]]=..., frequency: _Optional[_Union[RecurringSchedule.Frequency, str]]=..., weekly: _Optional[_Union[WeeklySchedule, _Mapping]]=..., monthly: _Optional[_Union[MonthlySchedule, _Mapping]]=..., last_execute_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., next_execute_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class WeeklySchedule(_message.Message):
    __slots__ = ('day_of_week',)
    DAY_OF_WEEK_FIELD_NUMBER: _ClassVar[int]
    day_of_week: _dayofweek_pb2.DayOfWeek

    def __init__(self, day_of_week: _Optional[_Union[_dayofweek_pb2.DayOfWeek, str]]=...) -> None:
        ...

class MonthlySchedule(_message.Message):
    __slots__ = ('week_day_of_month', 'month_day')
    WEEK_DAY_OF_MONTH_FIELD_NUMBER: _ClassVar[int]
    MONTH_DAY_FIELD_NUMBER: _ClassVar[int]
    week_day_of_month: WeekDayOfMonth
    month_day: int

    def __init__(self, week_day_of_month: _Optional[_Union[WeekDayOfMonth, _Mapping]]=..., month_day: _Optional[int]=...) -> None:
        ...

class WeekDayOfMonth(_message.Message):
    __slots__ = ('week_ordinal', 'day_of_week', 'day_offset')
    WEEK_ORDINAL_FIELD_NUMBER: _ClassVar[int]
    DAY_OF_WEEK_FIELD_NUMBER: _ClassVar[int]
    DAY_OFFSET_FIELD_NUMBER: _ClassVar[int]
    week_ordinal: int
    day_of_week: _dayofweek_pb2.DayOfWeek
    day_offset: int

    def __init__(self, week_ordinal: _Optional[int]=..., day_of_week: _Optional[_Union[_dayofweek_pb2.DayOfWeek, str]]=..., day_offset: _Optional[int]=...) -> None:
        ...

class CreatePatchDeploymentRequest(_message.Message):
    __slots__ = ('parent', 'patch_deployment_id', 'patch_deployment')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PATCH_DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    PATCH_DEPLOYMENT_FIELD_NUMBER: _ClassVar[int]
    parent: str
    patch_deployment_id: str
    patch_deployment: PatchDeployment

    def __init__(self, parent: _Optional[str]=..., patch_deployment_id: _Optional[str]=..., patch_deployment: _Optional[_Union[PatchDeployment, _Mapping]]=...) -> None:
        ...

class GetPatchDeploymentRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListPatchDeploymentsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListPatchDeploymentsResponse(_message.Message):
    __slots__ = ('patch_deployments', 'next_page_token')
    PATCH_DEPLOYMENTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    patch_deployments: _containers.RepeatedCompositeFieldContainer[PatchDeployment]
    next_page_token: str

    def __init__(self, patch_deployments: _Optional[_Iterable[_Union[PatchDeployment, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class DeletePatchDeploymentRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdatePatchDeploymentRequest(_message.Message):
    __slots__ = ('patch_deployment', 'update_mask')
    PATCH_DEPLOYMENT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    patch_deployment: PatchDeployment
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, patch_deployment: _Optional[_Union[PatchDeployment, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class PausePatchDeploymentRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ResumePatchDeploymentRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...