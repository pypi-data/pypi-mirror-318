from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.devtools.clouderrorreporting.v1beta1 import common_pb2 as _common_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class TimedCountAlignment(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ERROR_COUNT_ALIGNMENT_UNSPECIFIED: _ClassVar[TimedCountAlignment]
    ALIGNMENT_EQUAL_ROUNDED: _ClassVar[TimedCountAlignment]
    ALIGNMENT_EQUAL_AT_END: _ClassVar[TimedCountAlignment]

class ErrorGroupOrder(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GROUP_ORDER_UNSPECIFIED: _ClassVar[ErrorGroupOrder]
    COUNT_DESC: _ClassVar[ErrorGroupOrder]
    LAST_SEEN_DESC: _ClassVar[ErrorGroupOrder]
    CREATED_DESC: _ClassVar[ErrorGroupOrder]
    AFFECTED_USERS_DESC: _ClassVar[ErrorGroupOrder]
ERROR_COUNT_ALIGNMENT_UNSPECIFIED: TimedCountAlignment
ALIGNMENT_EQUAL_ROUNDED: TimedCountAlignment
ALIGNMENT_EQUAL_AT_END: TimedCountAlignment
GROUP_ORDER_UNSPECIFIED: ErrorGroupOrder
COUNT_DESC: ErrorGroupOrder
LAST_SEEN_DESC: ErrorGroupOrder
CREATED_DESC: ErrorGroupOrder
AFFECTED_USERS_DESC: ErrorGroupOrder

class ListGroupStatsRequest(_message.Message):
    __slots__ = ('project_name', 'group_id', 'service_filter', 'time_range', 'timed_count_duration', 'alignment', 'alignment_time', 'order', 'page_size', 'page_token')
    PROJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FILTER_FIELD_NUMBER: _ClassVar[int]
    TIME_RANGE_FIELD_NUMBER: _ClassVar[int]
    TIMED_COUNT_DURATION_FIELD_NUMBER: _ClassVar[int]
    ALIGNMENT_FIELD_NUMBER: _ClassVar[int]
    ALIGNMENT_TIME_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    project_name: str
    group_id: _containers.RepeatedScalarFieldContainer[str]
    service_filter: ServiceContextFilter
    time_range: QueryTimeRange
    timed_count_duration: _duration_pb2.Duration
    alignment: TimedCountAlignment
    alignment_time: _timestamp_pb2.Timestamp
    order: ErrorGroupOrder
    page_size: int
    page_token: str

    def __init__(self, project_name: _Optional[str]=..., group_id: _Optional[_Iterable[str]]=..., service_filter: _Optional[_Union[ServiceContextFilter, _Mapping]]=..., time_range: _Optional[_Union[QueryTimeRange, _Mapping]]=..., timed_count_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., alignment: _Optional[_Union[TimedCountAlignment, str]]=..., alignment_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., order: _Optional[_Union[ErrorGroupOrder, str]]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListGroupStatsResponse(_message.Message):
    __slots__ = ('error_group_stats', 'next_page_token', 'time_range_begin')
    ERROR_GROUP_STATS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TIME_RANGE_BEGIN_FIELD_NUMBER: _ClassVar[int]
    error_group_stats: _containers.RepeatedCompositeFieldContainer[ErrorGroupStats]
    next_page_token: str
    time_range_begin: _timestamp_pb2.Timestamp

    def __init__(self, error_group_stats: _Optional[_Iterable[_Union[ErrorGroupStats, _Mapping]]]=..., next_page_token: _Optional[str]=..., time_range_begin: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class ErrorGroupStats(_message.Message):
    __slots__ = ('group', 'count', 'affected_users_count', 'timed_counts', 'first_seen_time', 'last_seen_time', 'affected_services', 'num_affected_services', 'representative')
    GROUP_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    AFFECTED_USERS_COUNT_FIELD_NUMBER: _ClassVar[int]
    TIMED_COUNTS_FIELD_NUMBER: _ClassVar[int]
    FIRST_SEEN_TIME_FIELD_NUMBER: _ClassVar[int]
    LAST_SEEN_TIME_FIELD_NUMBER: _ClassVar[int]
    AFFECTED_SERVICES_FIELD_NUMBER: _ClassVar[int]
    NUM_AFFECTED_SERVICES_FIELD_NUMBER: _ClassVar[int]
    REPRESENTATIVE_FIELD_NUMBER: _ClassVar[int]
    group: _common_pb2.ErrorGroup
    count: int
    affected_users_count: int
    timed_counts: _containers.RepeatedCompositeFieldContainer[TimedCount]
    first_seen_time: _timestamp_pb2.Timestamp
    last_seen_time: _timestamp_pb2.Timestamp
    affected_services: _containers.RepeatedCompositeFieldContainer[_common_pb2.ServiceContext]
    num_affected_services: int
    representative: _common_pb2.ErrorEvent

    def __init__(self, group: _Optional[_Union[_common_pb2.ErrorGroup, _Mapping]]=..., count: _Optional[int]=..., affected_users_count: _Optional[int]=..., timed_counts: _Optional[_Iterable[_Union[TimedCount, _Mapping]]]=..., first_seen_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., last_seen_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., affected_services: _Optional[_Iterable[_Union[_common_pb2.ServiceContext, _Mapping]]]=..., num_affected_services: _Optional[int]=..., representative: _Optional[_Union[_common_pb2.ErrorEvent, _Mapping]]=...) -> None:
        ...

class TimedCount(_message.Message):
    __slots__ = ('count', 'start_time', 'end_time')
    COUNT_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    count: int
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp

    def __init__(self, count: _Optional[int]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class ListEventsRequest(_message.Message):
    __slots__ = ('project_name', 'group_id', 'service_filter', 'time_range', 'page_size', 'page_token')
    PROJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FILTER_FIELD_NUMBER: _ClassVar[int]
    TIME_RANGE_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    project_name: str
    group_id: str
    service_filter: ServiceContextFilter
    time_range: QueryTimeRange
    page_size: int
    page_token: str

    def __init__(self, project_name: _Optional[str]=..., group_id: _Optional[str]=..., service_filter: _Optional[_Union[ServiceContextFilter, _Mapping]]=..., time_range: _Optional[_Union[QueryTimeRange, _Mapping]]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListEventsResponse(_message.Message):
    __slots__ = ('error_events', 'next_page_token', 'time_range_begin')
    ERROR_EVENTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TIME_RANGE_BEGIN_FIELD_NUMBER: _ClassVar[int]
    error_events: _containers.RepeatedCompositeFieldContainer[_common_pb2.ErrorEvent]
    next_page_token: str
    time_range_begin: _timestamp_pb2.Timestamp

    def __init__(self, error_events: _Optional[_Iterable[_Union[_common_pb2.ErrorEvent, _Mapping]]]=..., next_page_token: _Optional[str]=..., time_range_begin: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class QueryTimeRange(_message.Message):
    __slots__ = ('period',)

    class Period(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PERIOD_UNSPECIFIED: _ClassVar[QueryTimeRange.Period]
        PERIOD_1_HOUR: _ClassVar[QueryTimeRange.Period]
        PERIOD_6_HOURS: _ClassVar[QueryTimeRange.Period]
        PERIOD_1_DAY: _ClassVar[QueryTimeRange.Period]
        PERIOD_1_WEEK: _ClassVar[QueryTimeRange.Period]
        PERIOD_30_DAYS: _ClassVar[QueryTimeRange.Period]
    PERIOD_UNSPECIFIED: QueryTimeRange.Period
    PERIOD_1_HOUR: QueryTimeRange.Period
    PERIOD_6_HOURS: QueryTimeRange.Period
    PERIOD_1_DAY: QueryTimeRange.Period
    PERIOD_1_WEEK: QueryTimeRange.Period
    PERIOD_30_DAYS: QueryTimeRange.Period
    PERIOD_FIELD_NUMBER: _ClassVar[int]
    period: QueryTimeRange.Period

    def __init__(self, period: _Optional[_Union[QueryTimeRange.Period, str]]=...) -> None:
        ...

class ServiceContextFilter(_message.Message):
    __slots__ = ('service', 'version', 'resource_type')
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    service: str
    version: str
    resource_type: str

    def __init__(self, service: _Optional[str]=..., version: _Optional[str]=..., resource_type: _Optional[str]=...) -> None:
        ...

class DeleteEventsRequest(_message.Message):
    __slots__ = ('project_name',)
    PROJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    project_name: str

    def __init__(self, project_name: _Optional[str]=...) -> None:
        ...

class DeleteEventsResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...