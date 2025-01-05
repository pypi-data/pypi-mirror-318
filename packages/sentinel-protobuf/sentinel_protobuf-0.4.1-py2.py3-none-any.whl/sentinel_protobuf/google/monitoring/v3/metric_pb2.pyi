from google.api import label_pb2 as _label_pb2
from google.api import metric_pb2 as _metric_pb2
from google.api import monitored_resource_pb2 as _monitored_resource_pb2
from google.monitoring.v3 import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Point(_message.Message):
    __slots__ = ('interval', 'value')
    INTERVAL_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    interval: _common_pb2.TimeInterval
    value: _common_pb2.TypedValue

    def __init__(self, interval: _Optional[_Union[_common_pb2.TimeInterval, _Mapping]]=..., value: _Optional[_Union[_common_pb2.TypedValue, _Mapping]]=...) -> None:
        ...

class TimeSeries(_message.Message):
    __slots__ = ('metric', 'resource', 'metadata', 'metric_kind', 'value_type', 'points', 'unit', 'description')
    METRIC_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    METRIC_KIND_FIELD_NUMBER: _ClassVar[int]
    VALUE_TYPE_FIELD_NUMBER: _ClassVar[int]
    POINTS_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    metric: _metric_pb2.Metric
    resource: _monitored_resource_pb2.MonitoredResource
    metadata: _monitored_resource_pb2.MonitoredResourceMetadata
    metric_kind: _metric_pb2.MetricDescriptor.MetricKind
    value_type: _metric_pb2.MetricDescriptor.ValueType
    points: _containers.RepeatedCompositeFieldContainer[Point]
    unit: str
    description: str

    def __init__(self, metric: _Optional[_Union[_metric_pb2.Metric, _Mapping]]=..., resource: _Optional[_Union[_monitored_resource_pb2.MonitoredResource, _Mapping]]=..., metadata: _Optional[_Union[_monitored_resource_pb2.MonitoredResourceMetadata, _Mapping]]=..., metric_kind: _Optional[_Union[_metric_pb2.MetricDescriptor.MetricKind, str]]=..., value_type: _Optional[_Union[_metric_pb2.MetricDescriptor.ValueType, str]]=..., points: _Optional[_Iterable[_Union[Point, _Mapping]]]=..., unit: _Optional[str]=..., description: _Optional[str]=...) -> None:
        ...

class TimeSeriesDescriptor(_message.Message):
    __slots__ = ('label_descriptors', 'point_descriptors')

    class ValueDescriptor(_message.Message):
        __slots__ = ('key', 'value_type', 'metric_kind', 'unit')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_TYPE_FIELD_NUMBER: _ClassVar[int]
        METRIC_KIND_FIELD_NUMBER: _ClassVar[int]
        UNIT_FIELD_NUMBER: _ClassVar[int]
        key: str
        value_type: _metric_pb2.MetricDescriptor.ValueType
        metric_kind: _metric_pb2.MetricDescriptor.MetricKind
        unit: str

        def __init__(self, key: _Optional[str]=..., value_type: _Optional[_Union[_metric_pb2.MetricDescriptor.ValueType, str]]=..., metric_kind: _Optional[_Union[_metric_pb2.MetricDescriptor.MetricKind, str]]=..., unit: _Optional[str]=...) -> None:
            ...
    LABEL_DESCRIPTORS_FIELD_NUMBER: _ClassVar[int]
    POINT_DESCRIPTORS_FIELD_NUMBER: _ClassVar[int]
    label_descriptors: _containers.RepeatedCompositeFieldContainer[_label_pb2.LabelDescriptor]
    point_descriptors: _containers.RepeatedCompositeFieldContainer[TimeSeriesDescriptor.ValueDescriptor]

    def __init__(self, label_descriptors: _Optional[_Iterable[_Union[_label_pb2.LabelDescriptor, _Mapping]]]=..., point_descriptors: _Optional[_Iterable[_Union[TimeSeriesDescriptor.ValueDescriptor, _Mapping]]]=...) -> None:
        ...

class TimeSeriesData(_message.Message):
    __slots__ = ('label_values', 'point_data')

    class PointData(_message.Message):
        __slots__ = ('values', 'time_interval')
        VALUES_FIELD_NUMBER: _ClassVar[int]
        TIME_INTERVAL_FIELD_NUMBER: _ClassVar[int]
        values: _containers.RepeatedCompositeFieldContainer[_common_pb2.TypedValue]
        time_interval: _common_pb2.TimeInterval

        def __init__(self, values: _Optional[_Iterable[_Union[_common_pb2.TypedValue, _Mapping]]]=..., time_interval: _Optional[_Union[_common_pb2.TimeInterval, _Mapping]]=...) -> None:
            ...
    LABEL_VALUES_FIELD_NUMBER: _ClassVar[int]
    POINT_DATA_FIELD_NUMBER: _ClassVar[int]
    label_values: _containers.RepeatedCompositeFieldContainer[LabelValue]
    point_data: _containers.RepeatedCompositeFieldContainer[TimeSeriesData.PointData]

    def __init__(self, label_values: _Optional[_Iterable[_Union[LabelValue, _Mapping]]]=..., point_data: _Optional[_Iterable[_Union[TimeSeriesData.PointData, _Mapping]]]=...) -> None:
        ...

class LabelValue(_message.Message):
    __slots__ = ('bool_value', 'int64_value', 'string_value')
    BOOL_VALUE_FIELD_NUMBER: _ClassVar[int]
    INT64_VALUE_FIELD_NUMBER: _ClassVar[int]
    STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
    bool_value: bool
    int64_value: int
    string_value: str

    def __init__(self, bool_value: bool=..., int64_value: _Optional[int]=..., string_value: _Optional[str]=...) -> None:
        ...

class QueryError(_message.Message):
    __slots__ = ('locator', 'message')
    LOCATOR_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    locator: TextLocator
    message: str

    def __init__(self, locator: _Optional[_Union[TextLocator, _Mapping]]=..., message: _Optional[str]=...) -> None:
        ...

class TextLocator(_message.Message):
    __slots__ = ('source', 'start_position', 'end_position', 'nested_locator', 'nesting_reason')

    class Position(_message.Message):
        __slots__ = ('line', 'column')
        LINE_FIELD_NUMBER: _ClassVar[int]
        COLUMN_FIELD_NUMBER: _ClassVar[int]
        line: int
        column: int

        def __init__(self, line: _Optional[int]=..., column: _Optional[int]=...) -> None:
            ...
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    START_POSITION_FIELD_NUMBER: _ClassVar[int]
    END_POSITION_FIELD_NUMBER: _ClassVar[int]
    NESTED_LOCATOR_FIELD_NUMBER: _ClassVar[int]
    NESTING_REASON_FIELD_NUMBER: _ClassVar[int]
    source: str
    start_position: TextLocator.Position
    end_position: TextLocator.Position
    nested_locator: TextLocator
    nesting_reason: str

    def __init__(self, source: _Optional[str]=..., start_position: _Optional[_Union[TextLocator.Position, _Mapping]]=..., end_position: _Optional[_Union[TextLocator.Position, _Mapping]]=..., nested_locator: _Optional[_Union[TextLocator, _Mapping]]=..., nesting_reason: _Optional[str]=...) -> None:
        ...