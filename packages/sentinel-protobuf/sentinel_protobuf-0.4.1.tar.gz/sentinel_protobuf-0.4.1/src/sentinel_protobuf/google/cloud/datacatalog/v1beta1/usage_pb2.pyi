from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class UsageStats(_message.Message):
    __slots__ = ('total_completions', 'total_failures', 'total_cancellations', 'total_execution_time_for_completions_millis')
    TOTAL_COMPLETIONS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FAILURES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_CANCELLATIONS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_EXECUTION_TIME_FOR_COMPLETIONS_MILLIS_FIELD_NUMBER: _ClassVar[int]
    total_completions: float
    total_failures: float
    total_cancellations: float
    total_execution_time_for_completions_millis: float

    def __init__(self, total_completions: _Optional[float]=..., total_failures: _Optional[float]=..., total_cancellations: _Optional[float]=..., total_execution_time_for_completions_millis: _Optional[float]=...) -> None:
        ...

class UsageSignal(_message.Message):
    __slots__ = ('update_time', 'usage_within_time_range')

    class UsageWithinTimeRangeEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: UsageStats

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[UsageStats, _Mapping]]=...) -> None:
            ...
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    USAGE_WITHIN_TIME_RANGE_FIELD_NUMBER: _ClassVar[int]
    update_time: _timestamp_pb2.Timestamp
    usage_within_time_range: _containers.MessageMap[str, UsageStats]

    def __init__(self, update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., usage_within_time_range: _Optional[_Mapping[str, UsageStats]]=...) -> None:
        ...