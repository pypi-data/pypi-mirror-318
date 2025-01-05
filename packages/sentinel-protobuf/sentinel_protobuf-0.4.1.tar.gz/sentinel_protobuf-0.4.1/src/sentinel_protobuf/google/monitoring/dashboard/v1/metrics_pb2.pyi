from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.monitoring.dashboard.v1 import common_pb2 as _common_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class SparkChartType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SPARK_CHART_TYPE_UNSPECIFIED: _ClassVar[SparkChartType]
    SPARK_LINE: _ClassVar[SparkChartType]
    SPARK_BAR: _ClassVar[SparkChartType]
SPARK_CHART_TYPE_UNSPECIFIED: SparkChartType
SPARK_LINE: SparkChartType
SPARK_BAR: SparkChartType

class TimeSeriesQuery(_message.Message):
    __slots__ = ('time_series_filter', 'time_series_filter_ratio', 'time_series_query_language', 'prometheus_query', 'unit_override', 'output_full_duration')
    TIME_SERIES_FILTER_FIELD_NUMBER: _ClassVar[int]
    TIME_SERIES_FILTER_RATIO_FIELD_NUMBER: _ClassVar[int]
    TIME_SERIES_QUERY_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    PROMETHEUS_QUERY_FIELD_NUMBER: _ClassVar[int]
    UNIT_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_FULL_DURATION_FIELD_NUMBER: _ClassVar[int]
    time_series_filter: TimeSeriesFilter
    time_series_filter_ratio: TimeSeriesFilterRatio
    time_series_query_language: str
    prometheus_query: str
    unit_override: str
    output_full_duration: bool

    def __init__(self, time_series_filter: _Optional[_Union[TimeSeriesFilter, _Mapping]]=..., time_series_filter_ratio: _Optional[_Union[TimeSeriesFilterRatio, _Mapping]]=..., time_series_query_language: _Optional[str]=..., prometheus_query: _Optional[str]=..., unit_override: _Optional[str]=..., output_full_duration: bool=...) -> None:
        ...

class TimeSeriesFilter(_message.Message):
    __slots__ = ('filter', 'aggregation', 'secondary_aggregation', 'pick_time_series_filter', 'statistical_time_series_filter')
    FILTER_FIELD_NUMBER: _ClassVar[int]
    AGGREGATION_FIELD_NUMBER: _ClassVar[int]
    SECONDARY_AGGREGATION_FIELD_NUMBER: _ClassVar[int]
    PICK_TIME_SERIES_FILTER_FIELD_NUMBER: _ClassVar[int]
    STATISTICAL_TIME_SERIES_FILTER_FIELD_NUMBER: _ClassVar[int]
    filter: str
    aggregation: _common_pb2.Aggregation
    secondary_aggregation: _common_pb2.Aggregation
    pick_time_series_filter: _common_pb2.PickTimeSeriesFilter
    statistical_time_series_filter: _common_pb2.StatisticalTimeSeriesFilter

    def __init__(self, filter: _Optional[str]=..., aggregation: _Optional[_Union[_common_pb2.Aggregation, _Mapping]]=..., secondary_aggregation: _Optional[_Union[_common_pb2.Aggregation, _Mapping]]=..., pick_time_series_filter: _Optional[_Union[_common_pb2.PickTimeSeriesFilter, _Mapping]]=..., statistical_time_series_filter: _Optional[_Union[_common_pb2.StatisticalTimeSeriesFilter, _Mapping]]=...) -> None:
        ...

class TimeSeriesFilterRatio(_message.Message):
    __slots__ = ('numerator', 'denominator', 'secondary_aggregation', 'pick_time_series_filter', 'statistical_time_series_filter')

    class RatioPart(_message.Message):
        __slots__ = ('filter', 'aggregation')
        FILTER_FIELD_NUMBER: _ClassVar[int]
        AGGREGATION_FIELD_NUMBER: _ClassVar[int]
        filter: str
        aggregation: _common_pb2.Aggregation

        def __init__(self, filter: _Optional[str]=..., aggregation: _Optional[_Union[_common_pb2.Aggregation, _Mapping]]=...) -> None:
            ...
    NUMERATOR_FIELD_NUMBER: _ClassVar[int]
    DENOMINATOR_FIELD_NUMBER: _ClassVar[int]
    SECONDARY_AGGREGATION_FIELD_NUMBER: _ClassVar[int]
    PICK_TIME_SERIES_FILTER_FIELD_NUMBER: _ClassVar[int]
    STATISTICAL_TIME_SERIES_FILTER_FIELD_NUMBER: _ClassVar[int]
    numerator: TimeSeriesFilterRatio.RatioPart
    denominator: TimeSeriesFilterRatio.RatioPart
    secondary_aggregation: _common_pb2.Aggregation
    pick_time_series_filter: _common_pb2.PickTimeSeriesFilter
    statistical_time_series_filter: _common_pb2.StatisticalTimeSeriesFilter

    def __init__(self, numerator: _Optional[_Union[TimeSeriesFilterRatio.RatioPart, _Mapping]]=..., denominator: _Optional[_Union[TimeSeriesFilterRatio.RatioPart, _Mapping]]=..., secondary_aggregation: _Optional[_Union[_common_pb2.Aggregation, _Mapping]]=..., pick_time_series_filter: _Optional[_Union[_common_pb2.PickTimeSeriesFilter, _Mapping]]=..., statistical_time_series_filter: _Optional[_Union[_common_pb2.StatisticalTimeSeriesFilter, _Mapping]]=...) -> None:
        ...

class Threshold(_message.Message):
    __slots__ = ('label', 'value', 'color', 'direction', 'target_axis')

    class Color(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        COLOR_UNSPECIFIED: _ClassVar[Threshold.Color]
        YELLOW: _ClassVar[Threshold.Color]
        RED: _ClassVar[Threshold.Color]
    COLOR_UNSPECIFIED: Threshold.Color
    YELLOW: Threshold.Color
    RED: Threshold.Color

    class Direction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DIRECTION_UNSPECIFIED: _ClassVar[Threshold.Direction]
        ABOVE: _ClassVar[Threshold.Direction]
        BELOW: _ClassVar[Threshold.Direction]
    DIRECTION_UNSPECIFIED: Threshold.Direction
    ABOVE: Threshold.Direction
    BELOW: Threshold.Direction

    class TargetAxis(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TARGET_AXIS_UNSPECIFIED: _ClassVar[Threshold.TargetAxis]
        Y1: _ClassVar[Threshold.TargetAxis]
        Y2: _ClassVar[Threshold.TargetAxis]
    TARGET_AXIS_UNSPECIFIED: Threshold.TargetAxis
    Y1: Threshold.TargetAxis
    Y2: Threshold.TargetAxis
    LABEL_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    TARGET_AXIS_FIELD_NUMBER: _ClassVar[int]
    label: str
    value: float
    color: Threshold.Color
    direction: Threshold.Direction
    target_axis: Threshold.TargetAxis

    def __init__(self, label: _Optional[str]=..., value: _Optional[float]=..., color: _Optional[_Union[Threshold.Color, str]]=..., direction: _Optional[_Union[Threshold.Direction, str]]=..., target_axis: _Optional[_Union[Threshold.TargetAxis, str]]=...) -> None:
        ...