from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import field_info_pb2 as _field_info_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.batch.v1alpha import notification_pb2 as _notification_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.type import interval_pb2 as _interval_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CalendarPeriod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CALENDAR_PERIOD_UNSPECIFIED: _ClassVar[CalendarPeriod]
    MONTH: _ClassVar[CalendarPeriod]
    QUARTER: _ClassVar[CalendarPeriod]
    YEAR: _ClassVar[CalendarPeriod]
    WEEK: _ClassVar[CalendarPeriod]
    DAY: _ClassVar[CalendarPeriod]

class ResourceAllowanceState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RESOURCE_ALLOWANCE_STATE_UNSPECIFIED: _ClassVar[ResourceAllowanceState]
    RESOURCE_ALLOWANCE_ACTIVE: _ClassVar[ResourceAllowanceState]
    RESOURCE_ALLOWANCE_DEPLETED: _ClassVar[ResourceAllowanceState]
CALENDAR_PERIOD_UNSPECIFIED: CalendarPeriod
MONTH: CalendarPeriod
QUARTER: CalendarPeriod
YEAR: CalendarPeriod
WEEK: CalendarPeriod
DAY: CalendarPeriod
RESOURCE_ALLOWANCE_STATE_UNSPECIFIED: ResourceAllowanceState
RESOURCE_ALLOWANCE_ACTIVE: ResourceAllowanceState
RESOURCE_ALLOWANCE_DEPLETED: ResourceAllowanceState

class ResourceAllowance(_message.Message):
    __slots__ = ("usage_resource_allowance", "name", "uid", "create_time", "labels", "notifications")
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    USAGE_RESOURCE_ALLOWANCE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATIONS_FIELD_NUMBER: _ClassVar[int]
    usage_resource_allowance: UsageResourceAllowance
    name: str
    uid: str
    create_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    notifications: _containers.RepeatedCompositeFieldContainer[_notification_pb2.Notification]
    def __init__(self, usage_resource_allowance: _Optional[_Union[UsageResourceAllowance, _Mapping]] = ..., name: _Optional[str] = ..., uid: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., labels: _Optional[_Mapping[str, str]] = ..., notifications: _Optional[_Iterable[_Union[_notification_pb2.Notification, _Mapping]]] = ...) -> None: ...

class UsageResourceAllowance(_message.Message):
    __slots__ = ("spec", "status")
    SPEC_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    spec: UsageResourceAllowanceSpec
    status: UsageResourceAllowanceStatus
    def __init__(self, spec: _Optional[_Union[UsageResourceAllowanceSpec, _Mapping]] = ..., status: _Optional[_Union[UsageResourceAllowanceStatus, _Mapping]] = ...) -> None: ...

class UsageResourceAllowanceSpec(_message.Message):
    __slots__ = ("type", "limit")
    class Limit(_message.Message):
        __slots__ = ("calendar_period", "limit")
        CALENDAR_PERIOD_FIELD_NUMBER: _ClassVar[int]
        LIMIT_FIELD_NUMBER: _ClassVar[int]
        calendar_period: CalendarPeriod
        limit: float
        def __init__(self, calendar_period: _Optional[_Union[CalendarPeriod, str]] = ..., limit: _Optional[float] = ...) -> None: ...
    TYPE_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    type: str
    limit: UsageResourceAllowanceSpec.Limit
    def __init__(self, type: _Optional[str] = ..., limit: _Optional[_Union[UsageResourceAllowanceSpec.Limit, _Mapping]] = ...) -> None: ...

class UsageResourceAllowanceStatus(_message.Message):
    __slots__ = ("state", "limit_status", "report")
    class LimitStatus(_message.Message):
        __slots__ = ("consumption_interval", "limit", "consumed")
        CONSUMPTION_INTERVAL_FIELD_NUMBER: _ClassVar[int]
        LIMIT_FIELD_NUMBER: _ClassVar[int]
        CONSUMED_FIELD_NUMBER: _ClassVar[int]
        consumption_interval: _interval_pb2.Interval
        limit: float
        consumed: float
        def __init__(self, consumption_interval: _Optional[_Union[_interval_pb2.Interval, _Mapping]] = ..., limit: _Optional[float] = ..., consumed: _Optional[float] = ...) -> None: ...
    class PeriodConsumption(_message.Message):
        __slots__ = ("consumption_interval", "consumed")
        CONSUMPTION_INTERVAL_FIELD_NUMBER: _ClassVar[int]
        CONSUMED_FIELD_NUMBER: _ClassVar[int]
        consumption_interval: _interval_pb2.Interval
        consumed: float
        def __init__(self, consumption_interval: _Optional[_Union[_interval_pb2.Interval, _Mapping]] = ..., consumed: _Optional[float] = ...) -> None: ...
    class ConsumptionReport(_message.Message):
        __slots__ = ("latest_period_consumptions",)
        class LatestPeriodConsumptionsEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: UsageResourceAllowanceStatus.PeriodConsumption
            def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[UsageResourceAllowanceStatus.PeriodConsumption, _Mapping]] = ...) -> None: ...
        LATEST_PERIOD_CONSUMPTIONS_FIELD_NUMBER: _ClassVar[int]
        latest_period_consumptions: _containers.MessageMap[str, UsageResourceAllowanceStatus.PeriodConsumption]
        def __init__(self, latest_period_consumptions: _Optional[_Mapping[str, UsageResourceAllowanceStatus.PeriodConsumption]] = ...) -> None: ...
    STATE_FIELD_NUMBER: _ClassVar[int]
    LIMIT_STATUS_FIELD_NUMBER: _ClassVar[int]
    REPORT_FIELD_NUMBER: _ClassVar[int]
    state: ResourceAllowanceState
    limit_status: UsageResourceAllowanceStatus.LimitStatus
    report: UsageResourceAllowanceStatus.ConsumptionReport
    def __init__(self, state: _Optional[_Union[ResourceAllowanceState, str]] = ..., limit_status: _Optional[_Union[UsageResourceAllowanceStatus.LimitStatus, _Mapping]] = ..., report: _Optional[_Union[UsageResourceAllowanceStatus.ConsumptionReport, _Mapping]] = ...) -> None: ...
