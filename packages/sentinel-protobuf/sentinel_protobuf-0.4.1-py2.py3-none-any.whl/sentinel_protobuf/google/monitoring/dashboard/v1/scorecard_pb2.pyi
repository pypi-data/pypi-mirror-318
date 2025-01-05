from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.monitoring.dashboard.v1 import metrics_pb2 as _metrics_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Scorecard(_message.Message):
    __slots__ = ('time_series_query', 'gauge_view', 'spark_chart_view', 'blank_view', 'thresholds')

    class GaugeView(_message.Message):
        __slots__ = ('lower_bound', 'upper_bound')
        LOWER_BOUND_FIELD_NUMBER: _ClassVar[int]
        UPPER_BOUND_FIELD_NUMBER: _ClassVar[int]
        lower_bound: float
        upper_bound: float

        def __init__(self, lower_bound: _Optional[float]=..., upper_bound: _Optional[float]=...) -> None:
            ...

    class SparkChartView(_message.Message):
        __slots__ = ('spark_chart_type', 'min_alignment_period')
        SPARK_CHART_TYPE_FIELD_NUMBER: _ClassVar[int]
        MIN_ALIGNMENT_PERIOD_FIELD_NUMBER: _ClassVar[int]
        spark_chart_type: _metrics_pb2.SparkChartType
        min_alignment_period: _duration_pb2.Duration

        def __init__(self, spark_chart_type: _Optional[_Union[_metrics_pb2.SparkChartType, str]]=..., min_alignment_period: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=...) -> None:
            ...
    TIME_SERIES_QUERY_FIELD_NUMBER: _ClassVar[int]
    GAUGE_VIEW_FIELD_NUMBER: _ClassVar[int]
    SPARK_CHART_VIEW_FIELD_NUMBER: _ClassVar[int]
    BLANK_VIEW_FIELD_NUMBER: _ClassVar[int]
    THRESHOLDS_FIELD_NUMBER: _ClassVar[int]
    time_series_query: _metrics_pb2.TimeSeriesQuery
    gauge_view: Scorecard.GaugeView
    spark_chart_view: Scorecard.SparkChartView
    blank_view: _empty_pb2.Empty
    thresholds: _containers.RepeatedCompositeFieldContainer[_metrics_pb2.Threshold]

    def __init__(self, time_series_query: _Optional[_Union[_metrics_pb2.TimeSeriesQuery, _Mapping]]=..., gauge_view: _Optional[_Union[Scorecard.GaugeView, _Mapping]]=..., spark_chart_view: _Optional[_Union[Scorecard.SparkChartView, _Mapping]]=..., blank_view: _Optional[_Union[_empty_pb2.Empty, _Mapping]]=..., thresholds: _Optional[_Iterable[_Union[_metrics_pb2.Threshold, _Mapping]]]=...) -> None:
        ...