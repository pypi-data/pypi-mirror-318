from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.monitoring.dashboard.v1 import metrics_pb2 as _metrics_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class PieChart(_message.Message):
    __slots__ = ('data_sets', 'chart_type', 'show_labels')

    class PieChartType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PIE_CHART_TYPE_UNSPECIFIED: _ClassVar[PieChart.PieChartType]
        PIE: _ClassVar[PieChart.PieChartType]
        DONUT: _ClassVar[PieChart.PieChartType]
    PIE_CHART_TYPE_UNSPECIFIED: PieChart.PieChartType
    PIE: PieChart.PieChartType
    DONUT: PieChart.PieChartType

    class PieChartDataSet(_message.Message):
        __slots__ = ('time_series_query', 'slice_name_template', 'min_alignment_period')
        TIME_SERIES_QUERY_FIELD_NUMBER: _ClassVar[int]
        SLICE_NAME_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
        MIN_ALIGNMENT_PERIOD_FIELD_NUMBER: _ClassVar[int]
        time_series_query: _metrics_pb2.TimeSeriesQuery
        slice_name_template: str
        min_alignment_period: _duration_pb2.Duration

        def __init__(self, time_series_query: _Optional[_Union[_metrics_pb2.TimeSeriesQuery, _Mapping]]=..., slice_name_template: _Optional[str]=..., min_alignment_period: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=...) -> None:
            ...
    DATA_SETS_FIELD_NUMBER: _ClassVar[int]
    CHART_TYPE_FIELD_NUMBER: _ClassVar[int]
    SHOW_LABELS_FIELD_NUMBER: _ClassVar[int]
    data_sets: _containers.RepeatedCompositeFieldContainer[PieChart.PieChartDataSet]
    chart_type: PieChart.PieChartType
    show_labels: bool

    def __init__(self, data_sets: _Optional[_Iterable[_Union[PieChart.PieChartDataSet, _Mapping]]]=..., chart_type: _Optional[_Union[PieChart.PieChartType, str]]=..., show_labels: bool=...) -> None:
        ...