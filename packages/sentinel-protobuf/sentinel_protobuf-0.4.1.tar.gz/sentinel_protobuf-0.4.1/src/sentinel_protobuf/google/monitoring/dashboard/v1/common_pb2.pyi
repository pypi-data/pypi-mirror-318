from google.protobuf import duration_pb2 as _duration_pb2
from google.type import interval_pb2 as _interval_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Aggregation(_message.Message):
    __slots__ = ('alignment_period', 'per_series_aligner', 'cross_series_reducer', 'group_by_fields')

    class Aligner(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ALIGN_NONE: _ClassVar[Aggregation.Aligner]
        ALIGN_DELTA: _ClassVar[Aggregation.Aligner]
        ALIGN_RATE: _ClassVar[Aggregation.Aligner]
        ALIGN_INTERPOLATE: _ClassVar[Aggregation.Aligner]
        ALIGN_NEXT_OLDER: _ClassVar[Aggregation.Aligner]
        ALIGN_MIN: _ClassVar[Aggregation.Aligner]
        ALIGN_MAX: _ClassVar[Aggregation.Aligner]
        ALIGN_MEAN: _ClassVar[Aggregation.Aligner]
        ALIGN_COUNT: _ClassVar[Aggregation.Aligner]
        ALIGN_SUM: _ClassVar[Aggregation.Aligner]
        ALIGN_STDDEV: _ClassVar[Aggregation.Aligner]
        ALIGN_COUNT_TRUE: _ClassVar[Aggregation.Aligner]
        ALIGN_COUNT_FALSE: _ClassVar[Aggregation.Aligner]
        ALIGN_FRACTION_TRUE: _ClassVar[Aggregation.Aligner]
        ALIGN_PERCENTILE_99: _ClassVar[Aggregation.Aligner]
        ALIGN_PERCENTILE_95: _ClassVar[Aggregation.Aligner]
        ALIGN_PERCENTILE_50: _ClassVar[Aggregation.Aligner]
        ALIGN_PERCENTILE_05: _ClassVar[Aggregation.Aligner]
        ALIGN_PERCENT_CHANGE: _ClassVar[Aggregation.Aligner]
    ALIGN_NONE: Aggregation.Aligner
    ALIGN_DELTA: Aggregation.Aligner
    ALIGN_RATE: Aggregation.Aligner
    ALIGN_INTERPOLATE: Aggregation.Aligner
    ALIGN_NEXT_OLDER: Aggregation.Aligner
    ALIGN_MIN: Aggregation.Aligner
    ALIGN_MAX: Aggregation.Aligner
    ALIGN_MEAN: Aggregation.Aligner
    ALIGN_COUNT: Aggregation.Aligner
    ALIGN_SUM: Aggregation.Aligner
    ALIGN_STDDEV: Aggregation.Aligner
    ALIGN_COUNT_TRUE: Aggregation.Aligner
    ALIGN_COUNT_FALSE: Aggregation.Aligner
    ALIGN_FRACTION_TRUE: Aggregation.Aligner
    ALIGN_PERCENTILE_99: Aggregation.Aligner
    ALIGN_PERCENTILE_95: Aggregation.Aligner
    ALIGN_PERCENTILE_50: Aggregation.Aligner
    ALIGN_PERCENTILE_05: Aggregation.Aligner
    ALIGN_PERCENT_CHANGE: Aggregation.Aligner

    class Reducer(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        REDUCE_NONE: _ClassVar[Aggregation.Reducer]
        REDUCE_MEAN: _ClassVar[Aggregation.Reducer]
        REDUCE_MIN: _ClassVar[Aggregation.Reducer]
        REDUCE_MAX: _ClassVar[Aggregation.Reducer]
        REDUCE_SUM: _ClassVar[Aggregation.Reducer]
        REDUCE_STDDEV: _ClassVar[Aggregation.Reducer]
        REDUCE_COUNT: _ClassVar[Aggregation.Reducer]
        REDUCE_COUNT_TRUE: _ClassVar[Aggregation.Reducer]
        REDUCE_COUNT_FALSE: _ClassVar[Aggregation.Reducer]
        REDUCE_FRACTION_TRUE: _ClassVar[Aggregation.Reducer]
        REDUCE_PERCENTILE_99: _ClassVar[Aggregation.Reducer]
        REDUCE_PERCENTILE_95: _ClassVar[Aggregation.Reducer]
        REDUCE_PERCENTILE_50: _ClassVar[Aggregation.Reducer]
        REDUCE_PERCENTILE_05: _ClassVar[Aggregation.Reducer]
    REDUCE_NONE: Aggregation.Reducer
    REDUCE_MEAN: Aggregation.Reducer
    REDUCE_MIN: Aggregation.Reducer
    REDUCE_MAX: Aggregation.Reducer
    REDUCE_SUM: Aggregation.Reducer
    REDUCE_STDDEV: Aggregation.Reducer
    REDUCE_COUNT: Aggregation.Reducer
    REDUCE_COUNT_TRUE: Aggregation.Reducer
    REDUCE_COUNT_FALSE: Aggregation.Reducer
    REDUCE_FRACTION_TRUE: Aggregation.Reducer
    REDUCE_PERCENTILE_99: Aggregation.Reducer
    REDUCE_PERCENTILE_95: Aggregation.Reducer
    REDUCE_PERCENTILE_50: Aggregation.Reducer
    REDUCE_PERCENTILE_05: Aggregation.Reducer
    ALIGNMENT_PERIOD_FIELD_NUMBER: _ClassVar[int]
    PER_SERIES_ALIGNER_FIELD_NUMBER: _ClassVar[int]
    CROSS_SERIES_REDUCER_FIELD_NUMBER: _ClassVar[int]
    GROUP_BY_FIELDS_FIELD_NUMBER: _ClassVar[int]
    alignment_period: _duration_pb2.Duration
    per_series_aligner: Aggregation.Aligner
    cross_series_reducer: Aggregation.Reducer
    group_by_fields: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, alignment_period: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., per_series_aligner: _Optional[_Union[Aggregation.Aligner, str]]=..., cross_series_reducer: _Optional[_Union[Aggregation.Reducer, str]]=..., group_by_fields: _Optional[_Iterable[str]]=...) -> None:
        ...

class PickTimeSeriesFilter(_message.Message):
    __slots__ = ('ranking_method', 'num_time_series', 'direction', 'interval')

    class Method(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        METHOD_UNSPECIFIED: _ClassVar[PickTimeSeriesFilter.Method]
        METHOD_MEAN: _ClassVar[PickTimeSeriesFilter.Method]
        METHOD_MAX: _ClassVar[PickTimeSeriesFilter.Method]
        METHOD_MIN: _ClassVar[PickTimeSeriesFilter.Method]
        METHOD_SUM: _ClassVar[PickTimeSeriesFilter.Method]
        METHOD_LATEST: _ClassVar[PickTimeSeriesFilter.Method]
    METHOD_UNSPECIFIED: PickTimeSeriesFilter.Method
    METHOD_MEAN: PickTimeSeriesFilter.Method
    METHOD_MAX: PickTimeSeriesFilter.Method
    METHOD_MIN: PickTimeSeriesFilter.Method
    METHOD_SUM: PickTimeSeriesFilter.Method
    METHOD_LATEST: PickTimeSeriesFilter.Method

    class Direction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DIRECTION_UNSPECIFIED: _ClassVar[PickTimeSeriesFilter.Direction]
        TOP: _ClassVar[PickTimeSeriesFilter.Direction]
        BOTTOM: _ClassVar[PickTimeSeriesFilter.Direction]
    DIRECTION_UNSPECIFIED: PickTimeSeriesFilter.Direction
    TOP: PickTimeSeriesFilter.Direction
    BOTTOM: PickTimeSeriesFilter.Direction
    RANKING_METHOD_FIELD_NUMBER: _ClassVar[int]
    NUM_TIME_SERIES_FIELD_NUMBER: _ClassVar[int]
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    INTERVAL_FIELD_NUMBER: _ClassVar[int]
    ranking_method: PickTimeSeriesFilter.Method
    num_time_series: int
    direction: PickTimeSeriesFilter.Direction
    interval: _interval_pb2.Interval

    def __init__(self, ranking_method: _Optional[_Union[PickTimeSeriesFilter.Method, str]]=..., num_time_series: _Optional[int]=..., direction: _Optional[_Union[PickTimeSeriesFilter.Direction, str]]=..., interval: _Optional[_Union[_interval_pb2.Interval, _Mapping]]=...) -> None:
        ...

class StatisticalTimeSeriesFilter(_message.Message):
    __slots__ = ('ranking_method', 'num_time_series')

    class Method(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        METHOD_UNSPECIFIED: _ClassVar[StatisticalTimeSeriesFilter.Method]
        METHOD_CLUSTER_OUTLIER: _ClassVar[StatisticalTimeSeriesFilter.Method]
    METHOD_UNSPECIFIED: StatisticalTimeSeriesFilter.Method
    METHOD_CLUSTER_OUTLIER: StatisticalTimeSeriesFilter.Method
    RANKING_METHOD_FIELD_NUMBER: _ClassVar[int]
    NUM_TIME_SERIES_FIELD_NUMBER: _ClassVar[int]
    ranking_method: StatisticalTimeSeriesFilter.Method
    num_time_series: int

    def __init__(self, ranking_method: _Optional[_Union[StatisticalTimeSeriesFilter.Method, str]]=..., num_time_series: _Optional[int]=...) -> None:
        ...