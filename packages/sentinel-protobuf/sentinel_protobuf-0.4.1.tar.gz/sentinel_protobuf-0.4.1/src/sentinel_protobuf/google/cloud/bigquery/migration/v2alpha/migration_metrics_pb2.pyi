from google.api import distribution_pb2 as _distribution_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import metric_pb2 as _metric_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class TimeSeries(_message.Message):
    __slots__ = ('metric', 'value_type', 'metric_kind', 'points')
    METRIC_FIELD_NUMBER: _ClassVar[int]
    VALUE_TYPE_FIELD_NUMBER: _ClassVar[int]
    METRIC_KIND_FIELD_NUMBER: _ClassVar[int]
    POINTS_FIELD_NUMBER: _ClassVar[int]
    metric: str
    value_type: _metric_pb2.MetricDescriptor.ValueType
    metric_kind: _metric_pb2.MetricDescriptor.MetricKind
    points: _containers.RepeatedCompositeFieldContainer[Point]

    def __init__(self, metric: _Optional[str]=..., value_type: _Optional[_Union[_metric_pb2.MetricDescriptor.ValueType, str]]=..., metric_kind: _Optional[_Union[_metric_pb2.MetricDescriptor.MetricKind, str]]=..., points: _Optional[_Iterable[_Union[Point, _Mapping]]]=...) -> None:
        ...

class Point(_message.Message):
    __slots__ = ('interval', 'value')
    INTERVAL_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    interval: TimeInterval
    value: TypedValue

    def __init__(self, interval: _Optional[_Union[TimeInterval, _Mapping]]=..., value: _Optional[_Union[TypedValue, _Mapping]]=...) -> None:
        ...

class TimeInterval(_message.Message):
    __slots__ = ('start_time', 'end_time')
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp

    def __init__(self, start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class TypedValue(_message.Message):
    __slots__ = ('bool_value', 'int64_value', 'double_value', 'string_value', 'distribution_value')
    BOOL_VALUE_FIELD_NUMBER: _ClassVar[int]
    INT64_VALUE_FIELD_NUMBER: _ClassVar[int]
    DOUBLE_VALUE_FIELD_NUMBER: _ClassVar[int]
    STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
    DISTRIBUTION_VALUE_FIELD_NUMBER: _ClassVar[int]
    bool_value: bool
    int64_value: int
    double_value: float
    string_value: str
    distribution_value: _distribution_pb2.Distribution

    def __init__(self, bool_value: bool=..., int64_value: _Optional[int]=..., double_value: _Optional[float]=..., string_value: _Optional[str]=..., distribution_value: _Optional[_Union[_distribution_pb2.Distribution, _Mapping]]=...) -> None:
        ...