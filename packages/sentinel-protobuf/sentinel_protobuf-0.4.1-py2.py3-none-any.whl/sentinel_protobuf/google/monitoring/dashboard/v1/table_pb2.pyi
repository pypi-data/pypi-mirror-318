from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.monitoring.dashboard.v1 import metrics_pb2 as _metrics_pb2
from google.monitoring.dashboard.v1 import table_display_options_pb2 as _table_display_options_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class TimeSeriesTable(_message.Message):
    __slots__ = ('data_sets', 'metric_visualization', 'column_settings')

    class MetricVisualization(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        METRIC_VISUALIZATION_UNSPECIFIED: _ClassVar[TimeSeriesTable.MetricVisualization]
        NUMBER: _ClassVar[TimeSeriesTable.MetricVisualization]
        BAR: _ClassVar[TimeSeriesTable.MetricVisualization]
    METRIC_VISUALIZATION_UNSPECIFIED: TimeSeriesTable.MetricVisualization
    NUMBER: TimeSeriesTable.MetricVisualization
    BAR: TimeSeriesTable.MetricVisualization

    class TableDataSet(_message.Message):
        __slots__ = ('time_series_query', 'table_template', 'min_alignment_period', 'table_display_options')
        TIME_SERIES_QUERY_FIELD_NUMBER: _ClassVar[int]
        TABLE_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
        MIN_ALIGNMENT_PERIOD_FIELD_NUMBER: _ClassVar[int]
        TABLE_DISPLAY_OPTIONS_FIELD_NUMBER: _ClassVar[int]
        time_series_query: _metrics_pb2.TimeSeriesQuery
        table_template: str
        min_alignment_period: _duration_pb2.Duration
        table_display_options: _table_display_options_pb2.TableDisplayOptions

        def __init__(self, time_series_query: _Optional[_Union[_metrics_pb2.TimeSeriesQuery, _Mapping]]=..., table_template: _Optional[str]=..., min_alignment_period: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., table_display_options: _Optional[_Union[_table_display_options_pb2.TableDisplayOptions, _Mapping]]=...) -> None:
            ...

    class ColumnSettings(_message.Message):
        __slots__ = ('column', 'visible')
        COLUMN_FIELD_NUMBER: _ClassVar[int]
        VISIBLE_FIELD_NUMBER: _ClassVar[int]
        column: str
        visible: bool

        def __init__(self, column: _Optional[str]=..., visible: bool=...) -> None:
            ...
    DATA_SETS_FIELD_NUMBER: _ClassVar[int]
    METRIC_VISUALIZATION_FIELD_NUMBER: _ClassVar[int]
    COLUMN_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    data_sets: _containers.RepeatedCompositeFieldContainer[TimeSeriesTable.TableDataSet]
    metric_visualization: TimeSeriesTable.MetricVisualization
    column_settings: _containers.RepeatedCompositeFieldContainer[TimeSeriesTable.ColumnSettings]

    def __init__(self, data_sets: _Optional[_Iterable[_Union[TimeSeriesTable.TableDataSet, _Mapping]]]=..., metric_visualization: _Optional[_Union[TimeSeriesTable.MetricVisualization, str]]=..., column_settings: _Optional[_Iterable[_Union[TimeSeriesTable.ColumnSettings, _Mapping]]]=...) -> None:
        ...