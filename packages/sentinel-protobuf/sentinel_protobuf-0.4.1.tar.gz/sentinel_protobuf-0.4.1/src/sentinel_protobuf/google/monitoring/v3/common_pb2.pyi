from google.api import distribution_pb2 as _distribution_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ComparisonType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    COMPARISON_UNSPECIFIED: _ClassVar[ComparisonType]
    COMPARISON_GT: _ClassVar[ComparisonType]
    COMPARISON_GE: _ClassVar[ComparisonType]
    COMPARISON_LT: _ClassVar[ComparisonType]
    COMPARISON_LE: _ClassVar[ComparisonType]
    COMPARISON_EQ: _ClassVar[ComparisonType]
    COMPARISON_NE: _ClassVar[ComparisonType]

class ServiceTier(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SERVICE_TIER_UNSPECIFIED: _ClassVar[ServiceTier]
    SERVICE_TIER_BASIC: _ClassVar[ServiceTier]
    SERVICE_TIER_PREMIUM: _ClassVar[ServiceTier]
COMPARISON_UNSPECIFIED: ComparisonType
COMPARISON_GT: ComparisonType
COMPARISON_GE: ComparisonType
COMPARISON_LT: ComparisonType
COMPARISON_LE: ComparisonType
COMPARISON_EQ: ComparisonType
COMPARISON_NE: ComparisonType
SERVICE_TIER_UNSPECIFIED: ServiceTier
SERVICE_TIER_BASIC: ServiceTier
SERVICE_TIER_PREMIUM: ServiceTier

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

class TimeInterval(_message.Message):
    __slots__ = ('end_time', 'start_time')
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    end_time: _timestamp_pb2.Timestamp
    start_time: _timestamp_pb2.Timestamp

    def __init__(self, end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

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