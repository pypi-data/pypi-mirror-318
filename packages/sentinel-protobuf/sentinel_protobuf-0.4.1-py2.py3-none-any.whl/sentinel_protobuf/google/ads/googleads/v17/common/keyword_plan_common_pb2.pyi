from google.ads.googleads.v17.common import dates_pb2 as _dates_pb2
from google.ads.googleads.v17.enums import device_pb2 as _device_pb2
from google.ads.googleads.v17.enums import keyword_plan_aggregate_metric_type_pb2 as _keyword_plan_aggregate_metric_type_pb2
from google.ads.googleads.v17.enums import keyword_plan_competition_level_pb2 as _keyword_plan_competition_level_pb2
from google.ads.googleads.v17.enums import keyword_plan_concept_group_type_pb2 as _keyword_plan_concept_group_type_pb2
from google.ads.googleads.v17.enums import month_of_year_pb2 as _month_of_year_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class KeywordPlanHistoricalMetrics(_message.Message):
    __slots__ = ("avg_monthly_searches", "monthly_search_volumes", "competition", "competition_index", "low_top_of_page_bid_micros", "high_top_of_page_bid_micros", "average_cpc_micros")
    AVG_MONTHLY_SEARCHES_FIELD_NUMBER: _ClassVar[int]
    MONTHLY_SEARCH_VOLUMES_FIELD_NUMBER: _ClassVar[int]
    COMPETITION_FIELD_NUMBER: _ClassVar[int]
    COMPETITION_INDEX_FIELD_NUMBER: _ClassVar[int]
    LOW_TOP_OF_PAGE_BID_MICROS_FIELD_NUMBER: _ClassVar[int]
    HIGH_TOP_OF_PAGE_BID_MICROS_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_CPC_MICROS_FIELD_NUMBER: _ClassVar[int]
    avg_monthly_searches: int
    monthly_search_volumes: _containers.RepeatedCompositeFieldContainer[MonthlySearchVolume]
    competition: _keyword_plan_competition_level_pb2.KeywordPlanCompetitionLevelEnum.KeywordPlanCompetitionLevel
    competition_index: int
    low_top_of_page_bid_micros: int
    high_top_of_page_bid_micros: int
    average_cpc_micros: int
    def __init__(self, avg_monthly_searches: _Optional[int] = ..., monthly_search_volumes: _Optional[_Iterable[_Union[MonthlySearchVolume, _Mapping]]] = ..., competition: _Optional[_Union[_keyword_plan_competition_level_pb2.KeywordPlanCompetitionLevelEnum.KeywordPlanCompetitionLevel, str]] = ..., competition_index: _Optional[int] = ..., low_top_of_page_bid_micros: _Optional[int] = ..., high_top_of_page_bid_micros: _Optional[int] = ..., average_cpc_micros: _Optional[int] = ...) -> None: ...

class HistoricalMetricsOptions(_message.Message):
    __slots__ = ("year_month_range", "include_average_cpc")
    YEAR_MONTH_RANGE_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_AVERAGE_CPC_FIELD_NUMBER: _ClassVar[int]
    year_month_range: _dates_pb2.YearMonthRange
    include_average_cpc: bool
    def __init__(self, year_month_range: _Optional[_Union[_dates_pb2.YearMonthRange, _Mapping]] = ..., include_average_cpc: bool = ...) -> None: ...

class MonthlySearchVolume(_message.Message):
    __slots__ = ("year", "month", "monthly_searches")
    YEAR_FIELD_NUMBER: _ClassVar[int]
    MONTH_FIELD_NUMBER: _ClassVar[int]
    MONTHLY_SEARCHES_FIELD_NUMBER: _ClassVar[int]
    year: int
    month: _month_of_year_pb2.MonthOfYearEnum.MonthOfYear
    monthly_searches: int
    def __init__(self, year: _Optional[int] = ..., month: _Optional[_Union[_month_of_year_pb2.MonthOfYearEnum.MonthOfYear, str]] = ..., monthly_searches: _Optional[int] = ...) -> None: ...

class KeywordPlanAggregateMetrics(_message.Message):
    __slots__ = ("aggregate_metric_types",)
    AGGREGATE_METRIC_TYPES_FIELD_NUMBER: _ClassVar[int]
    aggregate_metric_types: _containers.RepeatedScalarFieldContainer[_keyword_plan_aggregate_metric_type_pb2.KeywordPlanAggregateMetricTypeEnum.KeywordPlanAggregateMetricType]
    def __init__(self, aggregate_metric_types: _Optional[_Iterable[_Union[_keyword_plan_aggregate_metric_type_pb2.KeywordPlanAggregateMetricTypeEnum.KeywordPlanAggregateMetricType, str]]] = ...) -> None: ...

class KeywordPlanAggregateMetricResults(_message.Message):
    __slots__ = ("device_searches",)
    DEVICE_SEARCHES_FIELD_NUMBER: _ClassVar[int]
    device_searches: _containers.RepeatedCompositeFieldContainer[KeywordPlanDeviceSearches]
    def __init__(self, device_searches: _Optional[_Iterable[_Union[KeywordPlanDeviceSearches, _Mapping]]] = ...) -> None: ...

class KeywordPlanDeviceSearches(_message.Message):
    __slots__ = ("device", "search_count")
    DEVICE_FIELD_NUMBER: _ClassVar[int]
    SEARCH_COUNT_FIELD_NUMBER: _ClassVar[int]
    device: _device_pb2.DeviceEnum.Device
    search_count: int
    def __init__(self, device: _Optional[_Union[_device_pb2.DeviceEnum.Device, str]] = ..., search_count: _Optional[int] = ...) -> None: ...

class KeywordAnnotations(_message.Message):
    __slots__ = ("concepts",)
    CONCEPTS_FIELD_NUMBER: _ClassVar[int]
    concepts: _containers.RepeatedCompositeFieldContainer[KeywordConcept]
    def __init__(self, concepts: _Optional[_Iterable[_Union[KeywordConcept, _Mapping]]] = ...) -> None: ...

class KeywordConcept(_message.Message):
    __slots__ = ("name", "concept_group")
    NAME_FIELD_NUMBER: _ClassVar[int]
    CONCEPT_GROUP_FIELD_NUMBER: _ClassVar[int]
    name: str
    concept_group: ConceptGroup
    def __init__(self, name: _Optional[str] = ..., concept_group: _Optional[_Union[ConceptGroup, _Mapping]] = ...) -> None: ...

class ConceptGroup(_message.Message):
    __slots__ = ("name", "type")
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: _keyword_plan_concept_group_type_pb2.KeywordPlanConceptGroupTypeEnum.KeywordPlanConceptGroupType
    def __init__(self, name: _Optional[str] = ..., type: _Optional[_Union[_keyword_plan_concept_group_type_pb2.KeywordPlanConceptGroupTypeEnum.KeywordPlanConceptGroupType, str]] = ...) -> None: ...
