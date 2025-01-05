from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.monitoring.dashboard.v1 import metrics_pb2 as _metrics_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class XyChart(_message.Message):
    __slots__ = ('data_sets', 'timeshift_duration', 'thresholds', 'x_axis', 'y_axis', 'y2_axis', 'chart_options')

    class DataSet(_message.Message):
        __slots__ = ('time_series_query', 'plot_type', 'legend_template', 'min_alignment_period', 'target_axis')

        class PlotType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            PLOT_TYPE_UNSPECIFIED: _ClassVar[XyChart.DataSet.PlotType]
            LINE: _ClassVar[XyChart.DataSet.PlotType]
            STACKED_AREA: _ClassVar[XyChart.DataSet.PlotType]
            STACKED_BAR: _ClassVar[XyChart.DataSet.PlotType]
            HEATMAP: _ClassVar[XyChart.DataSet.PlotType]
        PLOT_TYPE_UNSPECIFIED: XyChart.DataSet.PlotType
        LINE: XyChart.DataSet.PlotType
        STACKED_AREA: XyChart.DataSet.PlotType
        STACKED_BAR: XyChart.DataSet.PlotType
        HEATMAP: XyChart.DataSet.PlotType

        class TargetAxis(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            TARGET_AXIS_UNSPECIFIED: _ClassVar[XyChart.DataSet.TargetAxis]
            Y1: _ClassVar[XyChart.DataSet.TargetAxis]
            Y2: _ClassVar[XyChart.DataSet.TargetAxis]
        TARGET_AXIS_UNSPECIFIED: XyChart.DataSet.TargetAxis
        Y1: XyChart.DataSet.TargetAxis
        Y2: XyChart.DataSet.TargetAxis
        TIME_SERIES_QUERY_FIELD_NUMBER: _ClassVar[int]
        PLOT_TYPE_FIELD_NUMBER: _ClassVar[int]
        LEGEND_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
        MIN_ALIGNMENT_PERIOD_FIELD_NUMBER: _ClassVar[int]
        TARGET_AXIS_FIELD_NUMBER: _ClassVar[int]
        time_series_query: _metrics_pb2.TimeSeriesQuery
        plot_type: XyChart.DataSet.PlotType
        legend_template: str
        min_alignment_period: _duration_pb2.Duration
        target_axis: XyChart.DataSet.TargetAxis

        def __init__(self, time_series_query: _Optional[_Union[_metrics_pb2.TimeSeriesQuery, _Mapping]]=..., plot_type: _Optional[_Union[XyChart.DataSet.PlotType, str]]=..., legend_template: _Optional[str]=..., min_alignment_period: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., target_axis: _Optional[_Union[XyChart.DataSet.TargetAxis, str]]=...) -> None:
            ...

    class Axis(_message.Message):
        __slots__ = ('label', 'scale')

        class Scale(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            SCALE_UNSPECIFIED: _ClassVar[XyChart.Axis.Scale]
            LINEAR: _ClassVar[XyChart.Axis.Scale]
            LOG10: _ClassVar[XyChart.Axis.Scale]
        SCALE_UNSPECIFIED: XyChart.Axis.Scale
        LINEAR: XyChart.Axis.Scale
        LOG10: XyChart.Axis.Scale
        LABEL_FIELD_NUMBER: _ClassVar[int]
        SCALE_FIELD_NUMBER: _ClassVar[int]
        label: str
        scale: XyChart.Axis.Scale

        def __init__(self, label: _Optional[str]=..., scale: _Optional[_Union[XyChart.Axis.Scale, str]]=...) -> None:
            ...
    DATA_SETS_FIELD_NUMBER: _ClassVar[int]
    TIMESHIFT_DURATION_FIELD_NUMBER: _ClassVar[int]
    THRESHOLDS_FIELD_NUMBER: _ClassVar[int]
    X_AXIS_FIELD_NUMBER: _ClassVar[int]
    Y_AXIS_FIELD_NUMBER: _ClassVar[int]
    Y2_AXIS_FIELD_NUMBER: _ClassVar[int]
    CHART_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    data_sets: _containers.RepeatedCompositeFieldContainer[XyChart.DataSet]
    timeshift_duration: _duration_pb2.Duration
    thresholds: _containers.RepeatedCompositeFieldContainer[_metrics_pb2.Threshold]
    x_axis: XyChart.Axis
    y_axis: XyChart.Axis
    y2_axis: XyChart.Axis
    chart_options: ChartOptions

    def __init__(self, data_sets: _Optional[_Iterable[_Union[XyChart.DataSet, _Mapping]]]=..., timeshift_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., thresholds: _Optional[_Iterable[_Union[_metrics_pb2.Threshold, _Mapping]]]=..., x_axis: _Optional[_Union[XyChart.Axis, _Mapping]]=..., y_axis: _Optional[_Union[XyChart.Axis, _Mapping]]=..., y2_axis: _Optional[_Union[XyChart.Axis, _Mapping]]=..., chart_options: _Optional[_Union[ChartOptions, _Mapping]]=...) -> None:
        ...

class ChartOptions(_message.Message):
    __slots__ = ('mode',)

    class Mode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MODE_UNSPECIFIED: _ClassVar[ChartOptions.Mode]
        COLOR: _ClassVar[ChartOptions.Mode]
        X_RAY: _ClassVar[ChartOptions.Mode]
        STATS: _ClassVar[ChartOptions.Mode]
    MODE_UNSPECIFIED: ChartOptions.Mode
    COLOR: ChartOptions.Mode
    X_RAY: ChartOptions.Mode
    STATS: ChartOptions.Mode
    MODE_FIELD_NUMBER: _ClassVar[int]
    mode: ChartOptions.Mode

    def __init__(self, mode: _Optional[_Union[ChartOptions.Mode, str]]=...) -> None:
        ...