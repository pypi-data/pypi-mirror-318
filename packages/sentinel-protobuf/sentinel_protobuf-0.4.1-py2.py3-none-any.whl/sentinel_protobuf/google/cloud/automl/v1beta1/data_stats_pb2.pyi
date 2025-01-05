from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class DataStats(_message.Message):
    __slots__ = ('float64_stats', 'string_stats', 'timestamp_stats', 'array_stats', 'struct_stats', 'category_stats', 'distinct_value_count', 'null_value_count', 'valid_value_count')
    FLOAT64_STATS_FIELD_NUMBER: _ClassVar[int]
    STRING_STATS_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_STATS_FIELD_NUMBER: _ClassVar[int]
    ARRAY_STATS_FIELD_NUMBER: _ClassVar[int]
    STRUCT_STATS_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_STATS_FIELD_NUMBER: _ClassVar[int]
    DISTINCT_VALUE_COUNT_FIELD_NUMBER: _ClassVar[int]
    NULL_VALUE_COUNT_FIELD_NUMBER: _ClassVar[int]
    VALID_VALUE_COUNT_FIELD_NUMBER: _ClassVar[int]
    float64_stats: Float64Stats
    string_stats: StringStats
    timestamp_stats: TimestampStats
    array_stats: ArrayStats
    struct_stats: StructStats
    category_stats: CategoryStats
    distinct_value_count: int
    null_value_count: int
    valid_value_count: int

    def __init__(self, float64_stats: _Optional[_Union[Float64Stats, _Mapping]]=..., string_stats: _Optional[_Union[StringStats, _Mapping]]=..., timestamp_stats: _Optional[_Union[TimestampStats, _Mapping]]=..., array_stats: _Optional[_Union[ArrayStats, _Mapping]]=..., struct_stats: _Optional[_Union[StructStats, _Mapping]]=..., category_stats: _Optional[_Union[CategoryStats, _Mapping]]=..., distinct_value_count: _Optional[int]=..., null_value_count: _Optional[int]=..., valid_value_count: _Optional[int]=...) -> None:
        ...

class Float64Stats(_message.Message):
    __slots__ = ('mean', 'standard_deviation', 'quantiles', 'histogram_buckets')

    class HistogramBucket(_message.Message):
        __slots__ = ('min', 'max', 'count')
        MIN_FIELD_NUMBER: _ClassVar[int]
        MAX_FIELD_NUMBER: _ClassVar[int]
        COUNT_FIELD_NUMBER: _ClassVar[int]
        min: float
        max: float
        count: int

        def __init__(self, min: _Optional[float]=..., max: _Optional[float]=..., count: _Optional[int]=...) -> None:
            ...
    MEAN_FIELD_NUMBER: _ClassVar[int]
    STANDARD_DEVIATION_FIELD_NUMBER: _ClassVar[int]
    QUANTILES_FIELD_NUMBER: _ClassVar[int]
    HISTOGRAM_BUCKETS_FIELD_NUMBER: _ClassVar[int]
    mean: float
    standard_deviation: float
    quantiles: _containers.RepeatedScalarFieldContainer[float]
    histogram_buckets: _containers.RepeatedCompositeFieldContainer[Float64Stats.HistogramBucket]

    def __init__(self, mean: _Optional[float]=..., standard_deviation: _Optional[float]=..., quantiles: _Optional[_Iterable[float]]=..., histogram_buckets: _Optional[_Iterable[_Union[Float64Stats.HistogramBucket, _Mapping]]]=...) -> None:
        ...

class StringStats(_message.Message):
    __slots__ = ('top_unigram_stats',)

    class UnigramStats(_message.Message):
        __slots__ = ('value', 'count')
        VALUE_FIELD_NUMBER: _ClassVar[int]
        COUNT_FIELD_NUMBER: _ClassVar[int]
        value: str
        count: int

        def __init__(self, value: _Optional[str]=..., count: _Optional[int]=...) -> None:
            ...
    TOP_UNIGRAM_STATS_FIELD_NUMBER: _ClassVar[int]
    top_unigram_stats: _containers.RepeatedCompositeFieldContainer[StringStats.UnigramStats]

    def __init__(self, top_unigram_stats: _Optional[_Iterable[_Union[StringStats.UnigramStats, _Mapping]]]=...) -> None:
        ...

class TimestampStats(_message.Message):
    __slots__ = ('granular_stats',)

    class GranularStats(_message.Message):
        __slots__ = ('buckets',)

        class BucketsEntry(_message.Message):
            __slots__ = ('key', 'value')
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: int
            value: int

            def __init__(self, key: _Optional[int]=..., value: _Optional[int]=...) -> None:
                ...
        BUCKETS_FIELD_NUMBER: _ClassVar[int]
        buckets: _containers.ScalarMap[int, int]

        def __init__(self, buckets: _Optional[_Mapping[int, int]]=...) -> None:
            ...

    class GranularStatsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: TimestampStats.GranularStats

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[TimestampStats.GranularStats, _Mapping]]=...) -> None:
            ...
    GRANULAR_STATS_FIELD_NUMBER: _ClassVar[int]
    granular_stats: _containers.MessageMap[str, TimestampStats.GranularStats]

    def __init__(self, granular_stats: _Optional[_Mapping[str, TimestampStats.GranularStats]]=...) -> None:
        ...

class ArrayStats(_message.Message):
    __slots__ = ('member_stats',)
    MEMBER_STATS_FIELD_NUMBER: _ClassVar[int]
    member_stats: DataStats

    def __init__(self, member_stats: _Optional[_Union[DataStats, _Mapping]]=...) -> None:
        ...

class StructStats(_message.Message):
    __slots__ = ('field_stats',)

    class FieldStatsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: DataStats

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[DataStats, _Mapping]]=...) -> None:
            ...
    FIELD_STATS_FIELD_NUMBER: _ClassVar[int]
    field_stats: _containers.MessageMap[str, DataStats]

    def __init__(self, field_stats: _Optional[_Mapping[str, DataStats]]=...) -> None:
        ...

class CategoryStats(_message.Message):
    __slots__ = ('top_category_stats',)

    class SingleCategoryStats(_message.Message):
        __slots__ = ('value', 'count')
        VALUE_FIELD_NUMBER: _ClassVar[int]
        COUNT_FIELD_NUMBER: _ClassVar[int]
        value: str
        count: int

        def __init__(self, value: _Optional[str]=..., count: _Optional[int]=...) -> None:
            ...
    TOP_CATEGORY_STATS_FIELD_NUMBER: _ClassVar[int]
    top_category_stats: _containers.RepeatedCompositeFieldContainer[CategoryStats.SingleCategoryStats]

    def __init__(self, top_category_stats: _Optional[_Iterable[_Union[CategoryStats.SingleCategoryStats, _Mapping]]]=...) -> None:
        ...

class CorrelationStats(_message.Message):
    __slots__ = ('cramers_v',)
    CRAMERS_V_FIELD_NUMBER: _ClassVar[int]
    cramers_v: float

    def __init__(self, cramers_v: _Optional[float]=...) -> None:
        ...