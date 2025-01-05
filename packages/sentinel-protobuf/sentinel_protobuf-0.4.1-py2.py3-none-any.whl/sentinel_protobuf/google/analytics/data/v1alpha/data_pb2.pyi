from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UserCriteriaScoping(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    USER_CRITERIA_SCOPING_UNSPECIFIED: _ClassVar[UserCriteriaScoping]
    USER_CRITERIA_WITHIN_SAME_EVENT: _ClassVar[UserCriteriaScoping]
    USER_CRITERIA_WITHIN_SAME_SESSION: _ClassVar[UserCriteriaScoping]
    USER_CRITERIA_ACROSS_ALL_SESSIONS: _ClassVar[UserCriteriaScoping]

class UserExclusionDuration(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    USER_EXCLUSION_DURATION_UNSPECIFIED: _ClassVar[UserExclusionDuration]
    USER_EXCLUSION_TEMPORARY: _ClassVar[UserExclusionDuration]
    USER_EXCLUSION_PERMANENT: _ClassVar[UserExclusionDuration]

class SessionCriteriaScoping(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SESSION_CRITERIA_SCOPING_UNSPECIFIED: _ClassVar[SessionCriteriaScoping]
    SESSION_CRITERIA_WITHIN_SAME_EVENT: _ClassVar[SessionCriteriaScoping]
    SESSION_CRITERIA_WITHIN_SAME_SESSION: _ClassVar[SessionCriteriaScoping]

class SessionExclusionDuration(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SESSION_EXCLUSION_DURATION_UNSPECIFIED: _ClassVar[SessionExclusionDuration]
    SESSION_EXCLUSION_TEMPORARY: _ClassVar[SessionExclusionDuration]
    SESSION_EXCLUSION_PERMANENT: _ClassVar[SessionExclusionDuration]

class EventCriteriaScoping(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EVENT_CRITERIA_SCOPING_UNSPECIFIED: _ClassVar[EventCriteriaScoping]
    EVENT_CRITERIA_WITHIN_SAME_EVENT: _ClassVar[EventCriteriaScoping]

class EventExclusionDuration(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EVENT_EXCLUSION_DURATION_UNSPECIFIED: _ClassVar[EventExclusionDuration]
    EVENT_EXCLUSION_PERMANENT: _ClassVar[EventExclusionDuration]

class MetricAggregation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    METRIC_AGGREGATION_UNSPECIFIED: _ClassVar[MetricAggregation]
    TOTAL: _ClassVar[MetricAggregation]
    MINIMUM: _ClassVar[MetricAggregation]
    MAXIMUM: _ClassVar[MetricAggregation]
    COUNT: _ClassVar[MetricAggregation]

class MetricType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    METRIC_TYPE_UNSPECIFIED: _ClassVar[MetricType]
    TYPE_INTEGER: _ClassVar[MetricType]
    TYPE_FLOAT: _ClassVar[MetricType]
    TYPE_SECONDS: _ClassVar[MetricType]
    TYPE_MILLISECONDS: _ClassVar[MetricType]
    TYPE_MINUTES: _ClassVar[MetricType]
    TYPE_HOURS: _ClassVar[MetricType]
    TYPE_STANDARD: _ClassVar[MetricType]
    TYPE_CURRENCY: _ClassVar[MetricType]
    TYPE_FEET: _ClassVar[MetricType]
    TYPE_MILES: _ClassVar[MetricType]
    TYPE_METERS: _ClassVar[MetricType]
    TYPE_KILOMETERS: _ClassVar[MetricType]

class RestrictedMetricType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RESTRICTED_METRIC_TYPE_UNSPECIFIED: _ClassVar[RestrictedMetricType]
    COST_DATA: _ClassVar[RestrictedMetricType]
    REVENUE_DATA: _ClassVar[RestrictedMetricType]

class SamplingLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SAMPLING_LEVEL_UNSPECIFIED: _ClassVar[SamplingLevel]
    LOW: _ClassVar[SamplingLevel]
    MEDIUM: _ClassVar[SamplingLevel]
    UNSAMPLED: _ClassVar[SamplingLevel]
USER_CRITERIA_SCOPING_UNSPECIFIED: UserCriteriaScoping
USER_CRITERIA_WITHIN_SAME_EVENT: UserCriteriaScoping
USER_CRITERIA_WITHIN_SAME_SESSION: UserCriteriaScoping
USER_CRITERIA_ACROSS_ALL_SESSIONS: UserCriteriaScoping
USER_EXCLUSION_DURATION_UNSPECIFIED: UserExclusionDuration
USER_EXCLUSION_TEMPORARY: UserExclusionDuration
USER_EXCLUSION_PERMANENT: UserExclusionDuration
SESSION_CRITERIA_SCOPING_UNSPECIFIED: SessionCriteriaScoping
SESSION_CRITERIA_WITHIN_SAME_EVENT: SessionCriteriaScoping
SESSION_CRITERIA_WITHIN_SAME_SESSION: SessionCriteriaScoping
SESSION_EXCLUSION_DURATION_UNSPECIFIED: SessionExclusionDuration
SESSION_EXCLUSION_TEMPORARY: SessionExclusionDuration
SESSION_EXCLUSION_PERMANENT: SessionExclusionDuration
EVENT_CRITERIA_SCOPING_UNSPECIFIED: EventCriteriaScoping
EVENT_CRITERIA_WITHIN_SAME_EVENT: EventCriteriaScoping
EVENT_EXCLUSION_DURATION_UNSPECIFIED: EventExclusionDuration
EVENT_EXCLUSION_PERMANENT: EventExclusionDuration
METRIC_AGGREGATION_UNSPECIFIED: MetricAggregation
TOTAL: MetricAggregation
MINIMUM: MetricAggregation
MAXIMUM: MetricAggregation
COUNT: MetricAggregation
METRIC_TYPE_UNSPECIFIED: MetricType
TYPE_INTEGER: MetricType
TYPE_FLOAT: MetricType
TYPE_SECONDS: MetricType
TYPE_MILLISECONDS: MetricType
TYPE_MINUTES: MetricType
TYPE_HOURS: MetricType
TYPE_STANDARD: MetricType
TYPE_CURRENCY: MetricType
TYPE_FEET: MetricType
TYPE_MILES: MetricType
TYPE_METERS: MetricType
TYPE_KILOMETERS: MetricType
RESTRICTED_METRIC_TYPE_UNSPECIFIED: RestrictedMetricType
COST_DATA: RestrictedMetricType
REVENUE_DATA: RestrictedMetricType
SAMPLING_LEVEL_UNSPECIFIED: SamplingLevel
LOW: SamplingLevel
MEDIUM: SamplingLevel
UNSAMPLED: SamplingLevel

class DateRange(_message.Message):
    __slots__ = ("start_date", "end_date", "name")
    START_DATE_FIELD_NUMBER: _ClassVar[int]
    END_DATE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    start_date: str
    end_date: str
    name: str
    def __init__(self, start_date: _Optional[str] = ..., end_date: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class Dimension(_message.Message):
    __slots__ = ("name", "dimension_expression")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DIMENSION_EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    name: str
    dimension_expression: DimensionExpression
    def __init__(self, name: _Optional[str] = ..., dimension_expression: _Optional[_Union[DimensionExpression, _Mapping]] = ...) -> None: ...

class DimensionExpression(_message.Message):
    __slots__ = ("lower_case", "upper_case", "concatenate")
    class CaseExpression(_message.Message):
        __slots__ = ("dimension_name",)
        DIMENSION_NAME_FIELD_NUMBER: _ClassVar[int]
        dimension_name: str
        def __init__(self, dimension_name: _Optional[str] = ...) -> None: ...
    class ConcatenateExpression(_message.Message):
        __slots__ = ("dimension_names", "delimiter")
        DIMENSION_NAMES_FIELD_NUMBER: _ClassVar[int]
        DELIMITER_FIELD_NUMBER: _ClassVar[int]
        dimension_names: _containers.RepeatedScalarFieldContainer[str]
        delimiter: str
        def __init__(self, dimension_names: _Optional[_Iterable[str]] = ..., delimiter: _Optional[str] = ...) -> None: ...
    LOWER_CASE_FIELD_NUMBER: _ClassVar[int]
    UPPER_CASE_FIELD_NUMBER: _ClassVar[int]
    CONCATENATE_FIELD_NUMBER: _ClassVar[int]
    lower_case: DimensionExpression.CaseExpression
    upper_case: DimensionExpression.CaseExpression
    concatenate: DimensionExpression.ConcatenateExpression
    def __init__(self, lower_case: _Optional[_Union[DimensionExpression.CaseExpression, _Mapping]] = ..., upper_case: _Optional[_Union[DimensionExpression.CaseExpression, _Mapping]] = ..., concatenate: _Optional[_Union[DimensionExpression.ConcatenateExpression, _Mapping]] = ...) -> None: ...

class Metric(_message.Message):
    __slots__ = ("name", "expression", "invisible")
    NAME_FIELD_NUMBER: _ClassVar[int]
    EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    INVISIBLE_FIELD_NUMBER: _ClassVar[int]
    name: str
    expression: str
    invisible: bool
    def __init__(self, name: _Optional[str] = ..., expression: _Optional[str] = ..., invisible: bool = ...) -> None: ...

class FilterExpression(_message.Message):
    __slots__ = ("and_group", "or_group", "not_expression", "filter")
    AND_GROUP_FIELD_NUMBER: _ClassVar[int]
    OR_GROUP_FIELD_NUMBER: _ClassVar[int]
    NOT_EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    and_group: FilterExpressionList
    or_group: FilterExpressionList
    not_expression: FilterExpression
    filter: Filter
    def __init__(self, and_group: _Optional[_Union[FilterExpressionList, _Mapping]] = ..., or_group: _Optional[_Union[FilterExpressionList, _Mapping]] = ..., not_expression: _Optional[_Union[FilterExpression, _Mapping]] = ..., filter: _Optional[_Union[Filter, _Mapping]] = ...) -> None: ...

class FilterExpressionList(_message.Message):
    __slots__ = ("expressions",)
    EXPRESSIONS_FIELD_NUMBER: _ClassVar[int]
    expressions: _containers.RepeatedCompositeFieldContainer[FilterExpression]
    def __init__(self, expressions: _Optional[_Iterable[_Union[FilterExpression, _Mapping]]] = ...) -> None: ...

class Filter(_message.Message):
    __slots__ = ("field_name", "string_filter", "in_list_filter", "numeric_filter", "between_filter", "empty_filter")
    FIELD_NAME_FIELD_NUMBER: _ClassVar[int]
    STRING_FILTER_FIELD_NUMBER: _ClassVar[int]
    IN_LIST_FILTER_FIELD_NUMBER: _ClassVar[int]
    NUMERIC_FILTER_FIELD_NUMBER: _ClassVar[int]
    BETWEEN_FILTER_FIELD_NUMBER: _ClassVar[int]
    EMPTY_FILTER_FIELD_NUMBER: _ClassVar[int]
    field_name: str
    string_filter: StringFilter
    in_list_filter: InListFilter
    numeric_filter: NumericFilter
    between_filter: BetweenFilter
    empty_filter: EmptyFilter
    def __init__(self, field_name: _Optional[str] = ..., string_filter: _Optional[_Union[StringFilter, _Mapping]] = ..., in_list_filter: _Optional[_Union[InListFilter, _Mapping]] = ..., numeric_filter: _Optional[_Union[NumericFilter, _Mapping]] = ..., between_filter: _Optional[_Union[BetweenFilter, _Mapping]] = ..., empty_filter: _Optional[_Union[EmptyFilter, _Mapping]] = ...) -> None: ...

class StringFilter(_message.Message):
    __slots__ = ("match_type", "value", "case_sensitive")
    class MatchType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MATCH_TYPE_UNSPECIFIED: _ClassVar[StringFilter.MatchType]
        EXACT: _ClassVar[StringFilter.MatchType]
        BEGINS_WITH: _ClassVar[StringFilter.MatchType]
        ENDS_WITH: _ClassVar[StringFilter.MatchType]
        CONTAINS: _ClassVar[StringFilter.MatchType]
        FULL_REGEXP: _ClassVar[StringFilter.MatchType]
        PARTIAL_REGEXP: _ClassVar[StringFilter.MatchType]
    MATCH_TYPE_UNSPECIFIED: StringFilter.MatchType
    EXACT: StringFilter.MatchType
    BEGINS_WITH: StringFilter.MatchType
    ENDS_WITH: StringFilter.MatchType
    CONTAINS: StringFilter.MatchType
    FULL_REGEXP: StringFilter.MatchType
    PARTIAL_REGEXP: StringFilter.MatchType
    MATCH_TYPE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    CASE_SENSITIVE_FIELD_NUMBER: _ClassVar[int]
    match_type: StringFilter.MatchType
    value: str
    case_sensitive: bool
    def __init__(self, match_type: _Optional[_Union[StringFilter.MatchType, str]] = ..., value: _Optional[str] = ..., case_sensitive: bool = ...) -> None: ...

class InListFilter(_message.Message):
    __slots__ = ("values", "case_sensitive")
    VALUES_FIELD_NUMBER: _ClassVar[int]
    CASE_SENSITIVE_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedScalarFieldContainer[str]
    case_sensitive: bool
    def __init__(self, values: _Optional[_Iterable[str]] = ..., case_sensitive: bool = ...) -> None: ...

class NumericFilter(_message.Message):
    __slots__ = ("operation", "value")
    class Operation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        OPERATION_UNSPECIFIED: _ClassVar[NumericFilter.Operation]
        EQUAL: _ClassVar[NumericFilter.Operation]
        LESS_THAN: _ClassVar[NumericFilter.Operation]
        LESS_THAN_OR_EQUAL: _ClassVar[NumericFilter.Operation]
        GREATER_THAN: _ClassVar[NumericFilter.Operation]
        GREATER_THAN_OR_EQUAL: _ClassVar[NumericFilter.Operation]
    OPERATION_UNSPECIFIED: NumericFilter.Operation
    EQUAL: NumericFilter.Operation
    LESS_THAN: NumericFilter.Operation
    LESS_THAN_OR_EQUAL: NumericFilter.Operation
    GREATER_THAN: NumericFilter.Operation
    GREATER_THAN_OR_EQUAL: NumericFilter.Operation
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    operation: NumericFilter.Operation
    value: NumericValue
    def __init__(self, operation: _Optional[_Union[NumericFilter.Operation, str]] = ..., value: _Optional[_Union[NumericValue, _Mapping]] = ...) -> None: ...

class OrderBy(_message.Message):
    __slots__ = ("metric", "dimension", "desc")
    class MetricOrderBy(_message.Message):
        __slots__ = ("metric_name",)
        METRIC_NAME_FIELD_NUMBER: _ClassVar[int]
        metric_name: str
        def __init__(self, metric_name: _Optional[str] = ...) -> None: ...
    class DimensionOrderBy(_message.Message):
        __slots__ = ("dimension_name", "order_type")
        class OrderType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            ORDER_TYPE_UNSPECIFIED: _ClassVar[OrderBy.DimensionOrderBy.OrderType]
            ALPHANUMERIC: _ClassVar[OrderBy.DimensionOrderBy.OrderType]
            CASE_INSENSITIVE_ALPHANUMERIC: _ClassVar[OrderBy.DimensionOrderBy.OrderType]
            NUMERIC: _ClassVar[OrderBy.DimensionOrderBy.OrderType]
        ORDER_TYPE_UNSPECIFIED: OrderBy.DimensionOrderBy.OrderType
        ALPHANUMERIC: OrderBy.DimensionOrderBy.OrderType
        CASE_INSENSITIVE_ALPHANUMERIC: OrderBy.DimensionOrderBy.OrderType
        NUMERIC: OrderBy.DimensionOrderBy.OrderType
        DIMENSION_NAME_FIELD_NUMBER: _ClassVar[int]
        ORDER_TYPE_FIELD_NUMBER: _ClassVar[int]
        dimension_name: str
        order_type: OrderBy.DimensionOrderBy.OrderType
        def __init__(self, dimension_name: _Optional[str] = ..., order_type: _Optional[_Union[OrderBy.DimensionOrderBy.OrderType, str]] = ...) -> None: ...
    METRIC_FIELD_NUMBER: _ClassVar[int]
    DIMENSION_FIELD_NUMBER: _ClassVar[int]
    DESC_FIELD_NUMBER: _ClassVar[int]
    metric: OrderBy.MetricOrderBy
    dimension: OrderBy.DimensionOrderBy
    desc: bool
    def __init__(self, metric: _Optional[_Union[OrderBy.MetricOrderBy, _Mapping]] = ..., dimension: _Optional[_Union[OrderBy.DimensionOrderBy, _Mapping]] = ..., desc: bool = ...) -> None: ...

class BetweenFilter(_message.Message):
    __slots__ = ("from_value", "to_value")
    FROM_VALUE_FIELD_NUMBER: _ClassVar[int]
    TO_VALUE_FIELD_NUMBER: _ClassVar[int]
    from_value: NumericValue
    to_value: NumericValue
    def __init__(self, from_value: _Optional[_Union[NumericValue, _Mapping]] = ..., to_value: _Optional[_Union[NumericValue, _Mapping]] = ...) -> None: ...

class EmptyFilter(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class NumericValue(_message.Message):
    __slots__ = ("int64_value", "double_value")
    INT64_VALUE_FIELD_NUMBER: _ClassVar[int]
    DOUBLE_VALUE_FIELD_NUMBER: _ClassVar[int]
    int64_value: int
    double_value: float
    def __init__(self, int64_value: _Optional[int] = ..., double_value: _Optional[float] = ...) -> None: ...

class CohortSpec(_message.Message):
    __slots__ = ("cohorts", "cohorts_range", "cohort_report_settings")
    COHORTS_FIELD_NUMBER: _ClassVar[int]
    COHORTS_RANGE_FIELD_NUMBER: _ClassVar[int]
    COHORT_REPORT_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    cohorts: _containers.RepeatedCompositeFieldContainer[Cohort]
    cohorts_range: CohortsRange
    cohort_report_settings: CohortReportSettings
    def __init__(self, cohorts: _Optional[_Iterable[_Union[Cohort, _Mapping]]] = ..., cohorts_range: _Optional[_Union[CohortsRange, _Mapping]] = ..., cohort_report_settings: _Optional[_Union[CohortReportSettings, _Mapping]] = ...) -> None: ...

class Cohort(_message.Message):
    __slots__ = ("name", "dimension", "date_range")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DIMENSION_FIELD_NUMBER: _ClassVar[int]
    DATE_RANGE_FIELD_NUMBER: _ClassVar[int]
    name: str
    dimension: str
    date_range: DateRange
    def __init__(self, name: _Optional[str] = ..., dimension: _Optional[str] = ..., date_range: _Optional[_Union[DateRange, _Mapping]] = ...) -> None: ...

class CohortsRange(_message.Message):
    __slots__ = ("granularity", "start_offset", "end_offset")
    class Granularity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        GRANULARITY_UNSPECIFIED: _ClassVar[CohortsRange.Granularity]
        DAILY: _ClassVar[CohortsRange.Granularity]
        WEEKLY: _ClassVar[CohortsRange.Granularity]
        MONTHLY: _ClassVar[CohortsRange.Granularity]
    GRANULARITY_UNSPECIFIED: CohortsRange.Granularity
    DAILY: CohortsRange.Granularity
    WEEKLY: CohortsRange.Granularity
    MONTHLY: CohortsRange.Granularity
    GRANULARITY_FIELD_NUMBER: _ClassVar[int]
    START_OFFSET_FIELD_NUMBER: _ClassVar[int]
    END_OFFSET_FIELD_NUMBER: _ClassVar[int]
    granularity: CohortsRange.Granularity
    start_offset: int
    end_offset: int
    def __init__(self, granularity: _Optional[_Union[CohortsRange.Granularity, str]] = ..., start_offset: _Optional[int] = ..., end_offset: _Optional[int] = ...) -> None: ...

class CohortReportSettings(_message.Message):
    __slots__ = ("accumulate",)
    ACCUMULATE_FIELD_NUMBER: _ClassVar[int]
    accumulate: bool
    def __init__(self, accumulate: bool = ...) -> None: ...

class ResponseMetaData(_message.Message):
    __slots__ = ("data_loss_from_other_row", "schema_restriction_response", "currency_code", "time_zone", "empty_reason", "subject_to_thresholding", "sampling_metadatas")
    class SchemaRestrictionResponse(_message.Message):
        __slots__ = ("active_metric_restrictions",)
        class ActiveMetricRestriction(_message.Message):
            __slots__ = ("metric_name", "restricted_metric_types")
            METRIC_NAME_FIELD_NUMBER: _ClassVar[int]
            RESTRICTED_METRIC_TYPES_FIELD_NUMBER: _ClassVar[int]
            metric_name: str
            restricted_metric_types: _containers.RepeatedScalarFieldContainer[RestrictedMetricType]
            def __init__(self, metric_name: _Optional[str] = ..., restricted_metric_types: _Optional[_Iterable[_Union[RestrictedMetricType, str]]] = ...) -> None: ...
        ACTIVE_METRIC_RESTRICTIONS_FIELD_NUMBER: _ClassVar[int]
        active_metric_restrictions: _containers.RepeatedCompositeFieldContainer[ResponseMetaData.SchemaRestrictionResponse.ActiveMetricRestriction]
        def __init__(self, active_metric_restrictions: _Optional[_Iterable[_Union[ResponseMetaData.SchemaRestrictionResponse.ActiveMetricRestriction, _Mapping]]] = ...) -> None: ...
    DATA_LOSS_FROM_OTHER_ROW_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_RESTRICTION_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_CODE_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    EMPTY_REASON_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_TO_THRESHOLDING_FIELD_NUMBER: _ClassVar[int]
    SAMPLING_METADATAS_FIELD_NUMBER: _ClassVar[int]
    data_loss_from_other_row: bool
    schema_restriction_response: ResponseMetaData.SchemaRestrictionResponse
    currency_code: str
    time_zone: str
    empty_reason: str
    subject_to_thresholding: bool
    sampling_metadatas: _containers.RepeatedCompositeFieldContainer[SamplingMetadata]
    def __init__(self, data_loss_from_other_row: bool = ..., schema_restriction_response: _Optional[_Union[ResponseMetaData.SchemaRestrictionResponse, _Mapping]] = ..., currency_code: _Optional[str] = ..., time_zone: _Optional[str] = ..., empty_reason: _Optional[str] = ..., subject_to_thresholding: bool = ..., sampling_metadatas: _Optional[_Iterable[_Union[SamplingMetadata, _Mapping]]] = ...) -> None: ...

class DimensionHeader(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class MetricHeader(_message.Message):
    __slots__ = ("name", "type")
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: MetricType
    def __init__(self, name: _Optional[str] = ..., type: _Optional[_Union[MetricType, str]] = ...) -> None: ...

class Row(_message.Message):
    __slots__ = ("dimension_values", "metric_values")
    DIMENSION_VALUES_FIELD_NUMBER: _ClassVar[int]
    METRIC_VALUES_FIELD_NUMBER: _ClassVar[int]
    dimension_values: _containers.RepeatedCompositeFieldContainer[DimensionValue]
    metric_values: _containers.RepeatedCompositeFieldContainer[MetricValue]
    def __init__(self, dimension_values: _Optional[_Iterable[_Union[DimensionValue, _Mapping]]] = ..., metric_values: _Optional[_Iterable[_Union[MetricValue, _Mapping]]] = ...) -> None: ...

class DimensionValue(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: str
    def __init__(self, value: _Optional[str] = ...) -> None: ...

class MetricValue(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: str
    def __init__(self, value: _Optional[str] = ...) -> None: ...

class PropertyQuota(_message.Message):
    __slots__ = ("tokens_per_day", "tokens_per_hour", "concurrent_requests", "server_errors_per_project_per_hour", "potentially_thresholded_requests_per_hour", "tokens_per_project_per_hour")
    TOKENS_PER_DAY_FIELD_NUMBER: _ClassVar[int]
    TOKENS_PER_HOUR_FIELD_NUMBER: _ClassVar[int]
    CONCURRENT_REQUESTS_FIELD_NUMBER: _ClassVar[int]
    SERVER_ERRORS_PER_PROJECT_PER_HOUR_FIELD_NUMBER: _ClassVar[int]
    POTENTIALLY_THRESHOLDED_REQUESTS_PER_HOUR_FIELD_NUMBER: _ClassVar[int]
    TOKENS_PER_PROJECT_PER_HOUR_FIELD_NUMBER: _ClassVar[int]
    tokens_per_day: QuotaStatus
    tokens_per_hour: QuotaStatus
    concurrent_requests: QuotaStatus
    server_errors_per_project_per_hour: QuotaStatus
    potentially_thresholded_requests_per_hour: QuotaStatus
    tokens_per_project_per_hour: QuotaStatus
    def __init__(self, tokens_per_day: _Optional[_Union[QuotaStatus, _Mapping]] = ..., tokens_per_hour: _Optional[_Union[QuotaStatus, _Mapping]] = ..., concurrent_requests: _Optional[_Union[QuotaStatus, _Mapping]] = ..., server_errors_per_project_per_hour: _Optional[_Union[QuotaStatus, _Mapping]] = ..., potentially_thresholded_requests_per_hour: _Optional[_Union[QuotaStatus, _Mapping]] = ..., tokens_per_project_per_hour: _Optional[_Union[QuotaStatus, _Mapping]] = ...) -> None: ...

class QuotaStatus(_message.Message):
    __slots__ = ("consumed", "remaining")
    CONSUMED_FIELD_NUMBER: _ClassVar[int]
    REMAINING_FIELD_NUMBER: _ClassVar[int]
    consumed: int
    remaining: int
    def __init__(self, consumed: _Optional[int] = ..., remaining: _Optional[int] = ...) -> None: ...

class FunnelBreakdown(_message.Message):
    __slots__ = ("breakdown_dimension", "limit")
    BREAKDOWN_DIMENSION_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    breakdown_dimension: Dimension
    limit: int
    def __init__(self, breakdown_dimension: _Optional[_Union[Dimension, _Mapping]] = ..., limit: _Optional[int] = ...) -> None: ...

class FunnelNextAction(_message.Message):
    __slots__ = ("next_action_dimension", "limit")
    NEXT_ACTION_DIMENSION_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    next_action_dimension: Dimension
    limit: int
    def __init__(self, next_action_dimension: _Optional[_Union[Dimension, _Mapping]] = ..., limit: _Optional[int] = ...) -> None: ...

class Funnel(_message.Message):
    __slots__ = ("is_open_funnel", "steps")
    IS_OPEN_FUNNEL_FIELD_NUMBER: _ClassVar[int]
    STEPS_FIELD_NUMBER: _ClassVar[int]
    is_open_funnel: bool
    steps: _containers.RepeatedCompositeFieldContainer[FunnelStep]
    def __init__(self, is_open_funnel: bool = ..., steps: _Optional[_Iterable[_Union[FunnelStep, _Mapping]]] = ...) -> None: ...

class FunnelStep(_message.Message):
    __slots__ = ("name", "is_directly_followed_by", "within_duration_from_prior_step", "filter_expression")
    NAME_FIELD_NUMBER: _ClassVar[int]
    IS_DIRECTLY_FOLLOWED_BY_FIELD_NUMBER: _ClassVar[int]
    WITHIN_DURATION_FROM_PRIOR_STEP_FIELD_NUMBER: _ClassVar[int]
    FILTER_EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    name: str
    is_directly_followed_by: bool
    within_duration_from_prior_step: _duration_pb2.Duration
    filter_expression: FunnelFilterExpression
    def __init__(self, name: _Optional[str] = ..., is_directly_followed_by: bool = ..., within_duration_from_prior_step: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., filter_expression: _Optional[_Union[FunnelFilterExpression, _Mapping]] = ...) -> None: ...

class FunnelSubReport(_message.Message):
    __slots__ = ("dimension_headers", "metric_headers", "rows", "metadata")
    DIMENSION_HEADERS_FIELD_NUMBER: _ClassVar[int]
    METRIC_HEADERS_FIELD_NUMBER: _ClassVar[int]
    ROWS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    dimension_headers: _containers.RepeatedCompositeFieldContainer[DimensionHeader]
    metric_headers: _containers.RepeatedCompositeFieldContainer[MetricHeader]
    rows: _containers.RepeatedCompositeFieldContainer[Row]
    metadata: FunnelResponseMetadata
    def __init__(self, dimension_headers: _Optional[_Iterable[_Union[DimensionHeader, _Mapping]]] = ..., metric_headers: _Optional[_Iterable[_Union[MetricHeader, _Mapping]]] = ..., rows: _Optional[_Iterable[_Union[Row, _Mapping]]] = ..., metadata: _Optional[_Union[FunnelResponseMetadata, _Mapping]] = ...) -> None: ...

class UserSegment(_message.Message):
    __slots__ = ("user_inclusion_criteria", "exclusion")
    USER_INCLUSION_CRITERIA_FIELD_NUMBER: _ClassVar[int]
    EXCLUSION_FIELD_NUMBER: _ClassVar[int]
    user_inclusion_criteria: UserSegmentCriteria
    exclusion: UserSegmentExclusion
    def __init__(self, user_inclusion_criteria: _Optional[_Union[UserSegmentCriteria, _Mapping]] = ..., exclusion: _Optional[_Union[UserSegmentExclusion, _Mapping]] = ...) -> None: ...

class UserSegmentCriteria(_message.Message):
    __slots__ = ("and_condition_groups", "and_sequence_groups")
    AND_CONDITION_GROUPS_FIELD_NUMBER: _ClassVar[int]
    AND_SEQUENCE_GROUPS_FIELD_NUMBER: _ClassVar[int]
    and_condition_groups: _containers.RepeatedCompositeFieldContainer[UserSegmentConditionGroup]
    and_sequence_groups: _containers.RepeatedCompositeFieldContainer[UserSegmentSequenceGroup]
    def __init__(self, and_condition_groups: _Optional[_Iterable[_Union[UserSegmentConditionGroup, _Mapping]]] = ..., and_sequence_groups: _Optional[_Iterable[_Union[UserSegmentSequenceGroup, _Mapping]]] = ...) -> None: ...

class UserSegmentConditionGroup(_message.Message):
    __slots__ = ("condition_scoping", "segment_filter_expression")
    CONDITION_SCOPING_FIELD_NUMBER: _ClassVar[int]
    SEGMENT_FILTER_EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    condition_scoping: UserCriteriaScoping
    segment_filter_expression: SegmentFilterExpression
    def __init__(self, condition_scoping: _Optional[_Union[UserCriteriaScoping, str]] = ..., segment_filter_expression: _Optional[_Union[SegmentFilterExpression, _Mapping]] = ...) -> None: ...

class UserSegmentSequenceGroup(_message.Message):
    __slots__ = ("sequence_scoping", "sequence_maximum_duration", "user_sequence_steps")
    SEQUENCE_SCOPING_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_MAXIMUM_DURATION_FIELD_NUMBER: _ClassVar[int]
    USER_SEQUENCE_STEPS_FIELD_NUMBER: _ClassVar[int]
    sequence_scoping: UserCriteriaScoping
    sequence_maximum_duration: _duration_pb2.Duration
    user_sequence_steps: _containers.RepeatedCompositeFieldContainer[UserSequenceStep]
    def __init__(self, sequence_scoping: _Optional[_Union[UserCriteriaScoping, str]] = ..., sequence_maximum_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., user_sequence_steps: _Optional[_Iterable[_Union[UserSequenceStep, _Mapping]]] = ...) -> None: ...

class UserSequenceStep(_message.Message):
    __slots__ = ("is_directly_followed_by", "step_scoping", "segment_filter_expression")
    IS_DIRECTLY_FOLLOWED_BY_FIELD_NUMBER: _ClassVar[int]
    STEP_SCOPING_FIELD_NUMBER: _ClassVar[int]
    SEGMENT_FILTER_EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    is_directly_followed_by: bool
    step_scoping: UserCriteriaScoping
    segment_filter_expression: SegmentFilterExpression
    def __init__(self, is_directly_followed_by: bool = ..., step_scoping: _Optional[_Union[UserCriteriaScoping, str]] = ..., segment_filter_expression: _Optional[_Union[SegmentFilterExpression, _Mapping]] = ...) -> None: ...

class UserSegmentExclusion(_message.Message):
    __slots__ = ("user_exclusion_duration", "user_exclusion_criteria")
    USER_EXCLUSION_DURATION_FIELD_NUMBER: _ClassVar[int]
    USER_EXCLUSION_CRITERIA_FIELD_NUMBER: _ClassVar[int]
    user_exclusion_duration: UserExclusionDuration
    user_exclusion_criteria: UserSegmentCriteria
    def __init__(self, user_exclusion_duration: _Optional[_Union[UserExclusionDuration, str]] = ..., user_exclusion_criteria: _Optional[_Union[UserSegmentCriteria, _Mapping]] = ...) -> None: ...

class SessionSegment(_message.Message):
    __slots__ = ("session_inclusion_criteria", "exclusion")
    SESSION_INCLUSION_CRITERIA_FIELD_NUMBER: _ClassVar[int]
    EXCLUSION_FIELD_NUMBER: _ClassVar[int]
    session_inclusion_criteria: SessionSegmentCriteria
    exclusion: SessionSegmentExclusion
    def __init__(self, session_inclusion_criteria: _Optional[_Union[SessionSegmentCriteria, _Mapping]] = ..., exclusion: _Optional[_Union[SessionSegmentExclusion, _Mapping]] = ...) -> None: ...

class SessionSegmentCriteria(_message.Message):
    __slots__ = ("and_condition_groups",)
    AND_CONDITION_GROUPS_FIELD_NUMBER: _ClassVar[int]
    and_condition_groups: _containers.RepeatedCompositeFieldContainer[SessionSegmentConditionGroup]
    def __init__(self, and_condition_groups: _Optional[_Iterable[_Union[SessionSegmentConditionGroup, _Mapping]]] = ...) -> None: ...

class SessionSegmentConditionGroup(_message.Message):
    __slots__ = ("condition_scoping", "segment_filter_expression")
    CONDITION_SCOPING_FIELD_NUMBER: _ClassVar[int]
    SEGMENT_FILTER_EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    condition_scoping: SessionCriteriaScoping
    segment_filter_expression: SegmentFilterExpression
    def __init__(self, condition_scoping: _Optional[_Union[SessionCriteriaScoping, str]] = ..., segment_filter_expression: _Optional[_Union[SegmentFilterExpression, _Mapping]] = ...) -> None: ...

class SessionSegmentExclusion(_message.Message):
    __slots__ = ("session_exclusion_duration", "session_exclusion_criteria")
    SESSION_EXCLUSION_DURATION_FIELD_NUMBER: _ClassVar[int]
    SESSION_EXCLUSION_CRITERIA_FIELD_NUMBER: _ClassVar[int]
    session_exclusion_duration: SessionExclusionDuration
    session_exclusion_criteria: SessionSegmentCriteria
    def __init__(self, session_exclusion_duration: _Optional[_Union[SessionExclusionDuration, str]] = ..., session_exclusion_criteria: _Optional[_Union[SessionSegmentCriteria, _Mapping]] = ...) -> None: ...

class EventSegment(_message.Message):
    __slots__ = ("event_inclusion_criteria", "exclusion")
    EVENT_INCLUSION_CRITERIA_FIELD_NUMBER: _ClassVar[int]
    EXCLUSION_FIELD_NUMBER: _ClassVar[int]
    event_inclusion_criteria: EventSegmentCriteria
    exclusion: EventSegmentExclusion
    def __init__(self, event_inclusion_criteria: _Optional[_Union[EventSegmentCriteria, _Mapping]] = ..., exclusion: _Optional[_Union[EventSegmentExclusion, _Mapping]] = ...) -> None: ...

class EventSegmentCriteria(_message.Message):
    __slots__ = ("and_condition_groups",)
    AND_CONDITION_GROUPS_FIELD_NUMBER: _ClassVar[int]
    and_condition_groups: _containers.RepeatedCompositeFieldContainer[EventSegmentConditionGroup]
    def __init__(self, and_condition_groups: _Optional[_Iterable[_Union[EventSegmentConditionGroup, _Mapping]]] = ...) -> None: ...

class EventSegmentConditionGroup(_message.Message):
    __slots__ = ("condition_scoping", "segment_filter_expression")
    CONDITION_SCOPING_FIELD_NUMBER: _ClassVar[int]
    SEGMENT_FILTER_EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    condition_scoping: EventCriteriaScoping
    segment_filter_expression: SegmentFilterExpression
    def __init__(self, condition_scoping: _Optional[_Union[EventCriteriaScoping, str]] = ..., segment_filter_expression: _Optional[_Union[SegmentFilterExpression, _Mapping]] = ...) -> None: ...

class EventSegmentExclusion(_message.Message):
    __slots__ = ("event_exclusion_duration", "event_exclusion_criteria")
    EVENT_EXCLUSION_DURATION_FIELD_NUMBER: _ClassVar[int]
    EVENT_EXCLUSION_CRITERIA_FIELD_NUMBER: _ClassVar[int]
    event_exclusion_duration: EventExclusionDuration
    event_exclusion_criteria: EventSegmentCriteria
    def __init__(self, event_exclusion_duration: _Optional[_Union[EventExclusionDuration, str]] = ..., event_exclusion_criteria: _Optional[_Union[EventSegmentCriteria, _Mapping]] = ...) -> None: ...

class Segment(_message.Message):
    __slots__ = ("name", "user_segment", "session_segment", "event_segment")
    NAME_FIELD_NUMBER: _ClassVar[int]
    USER_SEGMENT_FIELD_NUMBER: _ClassVar[int]
    SESSION_SEGMENT_FIELD_NUMBER: _ClassVar[int]
    EVENT_SEGMENT_FIELD_NUMBER: _ClassVar[int]
    name: str
    user_segment: UserSegment
    session_segment: SessionSegment
    event_segment: EventSegment
    def __init__(self, name: _Optional[str] = ..., user_segment: _Optional[_Union[UserSegment, _Mapping]] = ..., session_segment: _Optional[_Union[SessionSegment, _Mapping]] = ..., event_segment: _Optional[_Union[EventSegment, _Mapping]] = ...) -> None: ...

class SegmentFilterExpression(_message.Message):
    __slots__ = ("and_group", "or_group", "not_expression", "segment_filter", "segment_event_filter")
    AND_GROUP_FIELD_NUMBER: _ClassVar[int]
    OR_GROUP_FIELD_NUMBER: _ClassVar[int]
    NOT_EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    SEGMENT_FILTER_FIELD_NUMBER: _ClassVar[int]
    SEGMENT_EVENT_FILTER_FIELD_NUMBER: _ClassVar[int]
    and_group: SegmentFilterExpressionList
    or_group: SegmentFilterExpressionList
    not_expression: SegmentFilterExpression
    segment_filter: SegmentFilter
    segment_event_filter: SegmentEventFilter
    def __init__(self, and_group: _Optional[_Union[SegmentFilterExpressionList, _Mapping]] = ..., or_group: _Optional[_Union[SegmentFilterExpressionList, _Mapping]] = ..., not_expression: _Optional[_Union[SegmentFilterExpression, _Mapping]] = ..., segment_filter: _Optional[_Union[SegmentFilter, _Mapping]] = ..., segment_event_filter: _Optional[_Union[SegmentEventFilter, _Mapping]] = ...) -> None: ...

class SegmentFilterExpressionList(_message.Message):
    __slots__ = ("expressions",)
    EXPRESSIONS_FIELD_NUMBER: _ClassVar[int]
    expressions: _containers.RepeatedCompositeFieldContainer[SegmentFilterExpression]
    def __init__(self, expressions: _Optional[_Iterable[_Union[SegmentFilterExpression, _Mapping]]] = ...) -> None: ...

class SegmentFilter(_message.Message):
    __slots__ = ("field_name", "string_filter", "in_list_filter", "numeric_filter", "between_filter", "filter_scoping")
    FIELD_NAME_FIELD_NUMBER: _ClassVar[int]
    STRING_FILTER_FIELD_NUMBER: _ClassVar[int]
    IN_LIST_FILTER_FIELD_NUMBER: _ClassVar[int]
    NUMERIC_FILTER_FIELD_NUMBER: _ClassVar[int]
    BETWEEN_FILTER_FIELD_NUMBER: _ClassVar[int]
    FILTER_SCOPING_FIELD_NUMBER: _ClassVar[int]
    field_name: str
    string_filter: StringFilter
    in_list_filter: InListFilter
    numeric_filter: NumericFilter
    between_filter: BetweenFilter
    filter_scoping: SegmentFilterScoping
    def __init__(self, field_name: _Optional[str] = ..., string_filter: _Optional[_Union[StringFilter, _Mapping]] = ..., in_list_filter: _Optional[_Union[InListFilter, _Mapping]] = ..., numeric_filter: _Optional[_Union[NumericFilter, _Mapping]] = ..., between_filter: _Optional[_Union[BetweenFilter, _Mapping]] = ..., filter_scoping: _Optional[_Union[SegmentFilterScoping, _Mapping]] = ...) -> None: ...

class SegmentFilterScoping(_message.Message):
    __slots__ = ("at_any_point_in_time",)
    AT_ANY_POINT_IN_TIME_FIELD_NUMBER: _ClassVar[int]
    at_any_point_in_time: bool
    def __init__(self, at_any_point_in_time: bool = ...) -> None: ...

class SegmentEventFilter(_message.Message):
    __slots__ = ("event_name", "segment_parameter_filter_expression")
    EVENT_NAME_FIELD_NUMBER: _ClassVar[int]
    SEGMENT_PARAMETER_FILTER_EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    event_name: str
    segment_parameter_filter_expression: SegmentParameterFilterExpression
    def __init__(self, event_name: _Optional[str] = ..., segment_parameter_filter_expression: _Optional[_Union[SegmentParameterFilterExpression, _Mapping]] = ...) -> None: ...

class SegmentParameterFilterExpression(_message.Message):
    __slots__ = ("and_group", "or_group", "not_expression", "segment_parameter_filter")
    AND_GROUP_FIELD_NUMBER: _ClassVar[int]
    OR_GROUP_FIELD_NUMBER: _ClassVar[int]
    NOT_EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    SEGMENT_PARAMETER_FILTER_FIELD_NUMBER: _ClassVar[int]
    and_group: SegmentParameterFilterExpressionList
    or_group: SegmentParameterFilterExpressionList
    not_expression: SegmentParameterFilterExpression
    segment_parameter_filter: SegmentParameterFilter
    def __init__(self, and_group: _Optional[_Union[SegmentParameterFilterExpressionList, _Mapping]] = ..., or_group: _Optional[_Union[SegmentParameterFilterExpressionList, _Mapping]] = ..., not_expression: _Optional[_Union[SegmentParameterFilterExpression, _Mapping]] = ..., segment_parameter_filter: _Optional[_Union[SegmentParameterFilter, _Mapping]] = ...) -> None: ...

class SegmentParameterFilterExpressionList(_message.Message):
    __slots__ = ("expressions",)
    EXPRESSIONS_FIELD_NUMBER: _ClassVar[int]
    expressions: _containers.RepeatedCompositeFieldContainer[SegmentParameterFilterExpression]
    def __init__(self, expressions: _Optional[_Iterable[_Union[SegmentParameterFilterExpression, _Mapping]]] = ...) -> None: ...

class SegmentParameterFilter(_message.Message):
    __slots__ = ("event_parameter_name", "item_parameter_name", "string_filter", "in_list_filter", "numeric_filter", "between_filter", "filter_scoping")
    EVENT_PARAMETER_NAME_FIELD_NUMBER: _ClassVar[int]
    ITEM_PARAMETER_NAME_FIELD_NUMBER: _ClassVar[int]
    STRING_FILTER_FIELD_NUMBER: _ClassVar[int]
    IN_LIST_FILTER_FIELD_NUMBER: _ClassVar[int]
    NUMERIC_FILTER_FIELD_NUMBER: _ClassVar[int]
    BETWEEN_FILTER_FIELD_NUMBER: _ClassVar[int]
    FILTER_SCOPING_FIELD_NUMBER: _ClassVar[int]
    event_parameter_name: str
    item_parameter_name: str
    string_filter: StringFilter
    in_list_filter: InListFilter
    numeric_filter: NumericFilter
    between_filter: BetweenFilter
    filter_scoping: SegmentParameterFilterScoping
    def __init__(self, event_parameter_name: _Optional[str] = ..., item_parameter_name: _Optional[str] = ..., string_filter: _Optional[_Union[StringFilter, _Mapping]] = ..., in_list_filter: _Optional[_Union[InListFilter, _Mapping]] = ..., numeric_filter: _Optional[_Union[NumericFilter, _Mapping]] = ..., between_filter: _Optional[_Union[BetweenFilter, _Mapping]] = ..., filter_scoping: _Optional[_Union[SegmentParameterFilterScoping, _Mapping]] = ...) -> None: ...

class SegmentParameterFilterScoping(_message.Message):
    __slots__ = ("in_any_n_day_period",)
    IN_ANY_N_DAY_PERIOD_FIELD_NUMBER: _ClassVar[int]
    in_any_n_day_period: int
    def __init__(self, in_any_n_day_period: _Optional[int] = ...) -> None: ...

class FunnelFilterExpression(_message.Message):
    __slots__ = ("and_group", "or_group", "not_expression", "funnel_field_filter", "funnel_event_filter")
    AND_GROUP_FIELD_NUMBER: _ClassVar[int]
    OR_GROUP_FIELD_NUMBER: _ClassVar[int]
    NOT_EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    FUNNEL_FIELD_FILTER_FIELD_NUMBER: _ClassVar[int]
    FUNNEL_EVENT_FILTER_FIELD_NUMBER: _ClassVar[int]
    and_group: FunnelFilterExpressionList
    or_group: FunnelFilterExpressionList
    not_expression: FunnelFilterExpression
    funnel_field_filter: FunnelFieldFilter
    funnel_event_filter: FunnelEventFilter
    def __init__(self, and_group: _Optional[_Union[FunnelFilterExpressionList, _Mapping]] = ..., or_group: _Optional[_Union[FunnelFilterExpressionList, _Mapping]] = ..., not_expression: _Optional[_Union[FunnelFilterExpression, _Mapping]] = ..., funnel_field_filter: _Optional[_Union[FunnelFieldFilter, _Mapping]] = ..., funnel_event_filter: _Optional[_Union[FunnelEventFilter, _Mapping]] = ...) -> None: ...

class FunnelFilterExpressionList(_message.Message):
    __slots__ = ("expressions",)
    EXPRESSIONS_FIELD_NUMBER: _ClassVar[int]
    expressions: _containers.RepeatedCompositeFieldContainer[FunnelFilterExpression]
    def __init__(self, expressions: _Optional[_Iterable[_Union[FunnelFilterExpression, _Mapping]]] = ...) -> None: ...

class FunnelFieldFilter(_message.Message):
    __slots__ = ("field_name", "string_filter", "in_list_filter", "numeric_filter", "between_filter")
    FIELD_NAME_FIELD_NUMBER: _ClassVar[int]
    STRING_FILTER_FIELD_NUMBER: _ClassVar[int]
    IN_LIST_FILTER_FIELD_NUMBER: _ClassVar[int]
    NUMERIC_FILTER_FIELD_NUMBER: _ClassVar[int]
    BETWEEN_FILTER_FIELD_NUMBER: _ClassVar[int]
    field_name: str
    string_filter: StringFilter
    in_list_filter: InListFilter
    numeric_filter: NumericFilter
    between_filter: BetweenFilter
    def __init__(self, field_name: _Optional[str] = ..., string_filter: _Optional[_Union[StringFilter, _Mapping]] = ..., in_list_filter: _Optional[_Union[InListFilter, _Mapping]] = ..., numeric_filter: _Optional[_Union[NumericFilter, _Mapping]] = ..., between_filter: _Optional[_Union[BetweenFilter, _Mapping]] = ...) -> None: ...

class FunnelEventFilter(_message.Message):
    __slots__ = ("event_name", "funnel_parameter_filter_expression")
    EVENT_NAME_FIELD_NUMBER: _ClassVar[int]
    FUNNEL_PARAMETER_FILTER_EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    event_name: str
    funnel_parameter_filter_expression: FunnelParameterFilterExpression
    def __init__(self, event_name: _Optional[str] = ..., funnel_parameter_filter_expression: _Optional[_Union[FunnelParameterFilterExpression, _Mapping]] = ...) -> None: ...

class FunnelParameterFilterExpression(_message.Message):
    __slots__ = ("and_group", "or_group", "not_expression", "funnel_parameter_filter")
    AND_GROUP_FIELD_NUMBER: _ClassVar[int]
    OR_GROUP_FIELD_NUMBER: _ClassVar[int]
    NOT_EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    FUNNEL_PARAMETER_FILTER_FIELD_NUMBER: _ClassVar[int]
    and_group: FunnelParameterFilterExpressionList
    or_group: FunnelParameterFilterExpressionList
    not_expression: FunnelParameterFilterExpression
    funnel_parameter_filter: FunnelParameterFilter
    def __init__(self, and_group: _Optional[_Union[FunnelParameterFilterExpressionList, _Mapping]] = ..., or_group: _Optional[_Union[FunnelParameterFilterExpressionList, _Mapping]] = ..., not_expression: _Optional[_Union[FunnelParameterFilterExpression, _Mapping]] = ..., funnel_parameter_filter: _Optional[_Union[FunnelParameterFilter, _Mapping]] = ...) -> None: ...

class FunnelParameterFilterExpressionList(_message.Message):
    __slots__ = ("expressions",)
    EXPRESSIONS_FIELD_NUMBER: _ClassVar[int]
    expressions: _containers.RepeatedCompositeFieldContainer[FunnelParameterFilterExpression]
    def __init__(self, expressions: _Optional[_Iterable[_Union[FunnelParameterFilterExpression, _Mapping]]] = ...) -> None: ...

class FunnelParameterFilter(_message.Message):
    __slots__ = ("event_parameter_name", "item_parameter_name", "string_filter", "in_list_filter", "numeric_filter", "between_filter")
    EVENT_PARAMETER_NAME_FIELD_NUMBER: _ClassVar[int]
    ITEM_PARAMETER_NAME_FIELD_NUMBER: _ClassVar[int]
    STRING_FILTER_FIELD_NUMBER: _ClassVar[int]
    IN_LIST_FILTER_FIELD_NUMBER: _ClassVar[int]
    NUMERIC_FILTER_FIELD_NUMBER: _ClassVar[int]
    BETWEEN_FILTER_FIELD_NUMBER: _ClassVar[int]
    event_parameter_name: str
    item_parameter_name: str
    string_filter: StringFilter
    in_list_filter: InListFilter
    numeric_filter: NumericFilter
    between_filter: BetweenFilter
    def __init__(self, event_parameter_name: _Optional[str] = ..., item_parameter_name: _Optional[str] = ..., string_filter: _Optional[_Union[StringFilter, _Mapping]] = ..., in_list_filter: _Optional[_Union[InListFilter, _Mapping]] = ..., numeric_filter: _Optional[_Union[NumericFilter, _Mapping]] = ..., between_filter: _Optional[_Union[BetweenFilter, _Mapping]] = ...) -> None: ...

class FunnelResponseMetadata(_message.Message):
    __slots__ = ("sampling_metadatas",)
    SAMPLING_METADATAS_FIELD_NUMBER: _ClassVar[int]
    sampling_metadatas: _containers.RepeatedCompositeFieldContainer[SamplingMetadata]
    def __init__(self, sampling_metadatas: _Optional[_Iterable[_Union[SamplingMetadata, _Mapping]]] = ...) -> None: ...

class SamplingMetadata(_message.Message):
    __slots__ = ("samples_read_count", "sampling_space_size")
    SAMPLES_READ_COUNT_FIELD_NUMBER: _ClassVar[int]
    SAMPLING_SPACE_SIZE_FIELD_NUMBER: _ClassVar[int]
    samples_read_count: int
    sampling_space_size: int
    def __init__(self, samples_read_count: _Optional[int] = ..., sampling_space_size: _Optional[int] = ...) -> None: ...
