from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

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

class Compatibility(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    COMPATIBILITY_UNSPECIFIED: _ClassVar[Compatibility]
    COMPATIBLE: _ClassVar[Compatibility]
    INCOMPATIBLE: _ClassVar[Compatibility]
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
COMPATIBILITY_UNSPECIFIED: Compatibility
COMPATIBLE: Compatibility
INCOMPATIBLE: Compatibility

class DateRange(_message.Message):
    __slots__ = ("start_date", "end_date", "name")
    START_DATE_FIELD_NUMBER: _ClassVar[int]
    END_DATE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    start_date: str
    end_date: str
    name: str
    def __init__(self, start_date: _Optional[str] = ..., end_date: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class MinuteRange(_message.Message):
    __slots__ = ("start_minutes_ago", "end_minutes_ago", "name")
    START_MINUTES_AGO_FIELD_NUMBER: _ClassVar[int]
    END_MINUTES_AGO_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    start_minutes_ago: int
    end_minutes_ago: int
    name: str
    def __init__(self, start_minutes_ago: _Optional[int] = ..., end_minutes_ago: _Optional[int] = ..., name: _Optional[str] = ...) -> None: ...

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

class Comparison(_message.Message):
    __slots__ = ("name", "dimension_filter", "comparison")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DIMENSION_FILTER_FIELD_NUMBER: _ClassVar[int]
    COMPARISON_FIELD_NUMBER: _ClassVar[int]
    name: str
    dimension_filter: FilterExpression
    comparison: str
    def __init__(self, name: _Optional[str] = ..., dimension_filter: _Optional[_Union[FilterExpression, _Mapping]] = ..., comparison: _Optional[str] = ...) -> None: ...

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
    class StringFilter(_message.Message):
        __slots__ = ("match_type", "value", "case_sensitive")
        class MatchType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            MATCH_TYPE_UNSPECIFIED: _ClassVar[Filter.StringFilter.MatchType]
            EXACT: _ClassVar[Filter.StringFilter.MatchType]
            BEGINS_WITH: _ClassVar[Filter.StringFilter.MatchType]
            ENDS_WITH: _ClassVar[Filter.StringFilter.MatchType]
            CONTAINS: _ClassVar[Filter.StringFilter.MatchType]
            FULL_REGEXP: _ClassVar[Filter.StringFilter.MatchType]
            PARTIAL_REGEXP: _ClassVar[Filter.StringFilter.MatchType]
        MATCH_TYPE_UNSPECIFIED: Filter.StringFilter.MatchType
        EXACT: Filter.StringFilter.MatchType
        BEGINS_WITH: Filter.StringFilter.MatchType
        ENDS_WITH: Filter.StringFilter.MatchType
        CONTAINS: Filter.StringFilter.MatchType
        FULL_REGEXP: Filter.StringFilter.MatchType
        PARTIAL_REGEXP: Filter.StringFilter.MatchType
        MATCH_TYPE_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        CASE_SENSITIVE_FIELD_NUMBER: _ClassVar[int]
        match_type: Filter.StringFilter.MatchType
        value: str
        case_sensitive: bool
        def __init__(self, match_type: _Optional[_Union[Filter.StringFilter.MatchType, str]] = ..., value: _Optional[str] = ..., case_sensitive: bool = ...) -> None: ...
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
            OPERATION_UNSPECIFIED: _ClassVar[Filter.NumericFilter.Operation]
            EQUAL: _ClassVar[Filter.NumericFilter.Operation]
            LESS_THAN: _ClassVar[Filter.NumericFilter.Operation]
            LESS_THAN_OR_EQUAL: _ClassVar[Filter.NumericFilter.Operation]
            GREATER_THAN: _ClassVar[Filter.NumericFilter.Operation]
            GREATER_THAN_OR_EQUAL: _ClassVar[Filter.NumericFilter.Operation]
        OPERATION_UNSPECIFIED: Filter.NumericFilter.Operation
        EQUAL: Filter.NumericFilter.Operation
        LESS_THAN: Filter.NumericFilter.Operation
        LESS_THAN_OR_EQUAL: Filter.NumericFilter.Operation
        GREATER_THAN: Filter.NumericFilter.Operation
        GREATER_THAN_OR_EQUAL: Filter.NumericFilter.Operation
        OPERATION_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        operation: Filter.NumericFilter.Operation
        value: NumericValue
        def __init__(self, operation: _Optional[_Union[Filter.NumericFilter.Operation, str]] = ..., value: _Optional[_Union[NumericValue, _Mapping]] = ...) -> None: ...
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
    FIELD_NAME_FIELD_NUMBER: _ClassVar[int]
    STRING_FILTER_FIELD_NUMBER: _ClassVar[int]
    IN_LIST_FILTER_FIELD_NUMBER: _ClassVar[int]
    NUMERIC_FILTER_FIELD_NUMBER: _ClassVar[int]
    BETWEEN_FILTER_FIELD_NUMBER: _ClassVar[int]
    EMPTY_FILTER_FIELD_NUMBER: _ClassVar[int]
    field_name: str
    string_filter: Filter.StringFilter
    in_list_filter: Filter.InListFilter
    numeric_filter: Filter.NumericFilter
    between_filter: Filter.BetweenFilter
    empty_filter: Filter.EmptyFilter
    def __init__(self, field_name: _Optional[str] = ..., string_filter: _Optional[_Union[Filter.StringFilter, _Mapping]] = ..., in_list_filter: _Optional[_Union[Filter.InListFilter, _Mapping]] = ..., numeric_filter: _Optional[_Union[Filter.NumericFilter, _Mapping]] = ..., between_filter: _Optional[_Union[Filter.BetweenFilter, _Mapping]] = ..., empty_filter: _Optional[_Union[Filter.EmptyFilter, _Mapping]] = ...) -> None: ...

class OrderBy(_message.Message):
    __slots__ = ("metric", "dimension", "pivot", "desc")
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
    class PivotOrderBy(_message.Message):
        __slots__ = ("metric_name", "pivot_selections")
        class PivotSelection(_message.Message):
            __slots__ = ("dimension_name", "dimension_value")
            DIMENSION_NAME_FIELD_NUMBER: _ClassVar[int]
            DIMENSION_VALUE_FIELD_NUMBER: _ClassVar[int]
            dimension_name: str
            dimension_value: str
            def __init__(self, dimension_name: _Optional[str] = ..., dimension_value: _Optional[str] = ...) -> None: ...
        METRIC_NAME_FIELD_NUMBER: _ClassVar[int]
        PIVOT_SELECTIONS_FIELD_NUMBER: _ClassVar[int]
        metric_name: str
        pivot_selections: _containers.RepeatedCompositeFieldContainer[OrderBy.PivotOrderBy.PivotSelection]
        def __init__(self, metric_name: _Optional[str] = ..., pivot_selections: _Optional[_Iterable[_Union[OrderBy.PivotOrderBy.PivotSelection, _Mapping]]] = ...) -> None: ...
    METRIC_FIELD_NUMBER: _ClassVar[int]
    DIMENSION_FIELD_NUMBER: _ClassVar[int]
    PIVOT_FIELD_NUMBER: _ClassVar[int]
    DESC_FIELD_NUMBER: _ClassVar[int]
    metric: OrderBy.MetricOrderBy
    dimension: OrderBy.DimensionOrderBy
    pivot: OrderBy.PivotOrderBy
    desc: bool
    def __init__(self, metric: _Optional[_Union[OrderBy.MetricOrderBy, _Mapping]] = ..., dimension: _Optional[_Union[OrderBy.DimensionOrderBy, _Mapping]] = ..., pivot: _Optional[_Union[OrderBy.PivotOrderBy, _Mapping]] = ..., desc: bool = ...) -> None: ...

class Pivot(_message.Message):
    __slots__ = ("field_names", "order_bys", "offset", "limit", "metric_aggregations")
    FIELD_NAMES_FIELD_NUMBER: _ClassVar[int]
    ORDER_BYS_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    METRIC_AGGREGATIONS_FIELD_NUMBER: _ClassVar[int]
    field_names: _containers.RepeatedScalarFieldContainer[str]
    order_bys: _containers.RepeatedCompositeFieldContainer[OrderBy]
    offset: int
    limit: int
    metric_aggregations: _containers.RepeatedScalarFieldContainer[MetricAggregation]
    def __init__(self, field_names: _Optional[_Iterable[str]] = ..., order_bys: _Optional[_Iterable[_Union[OrderBy, _Mapping]]] = ..., offset: _Optional[int] = ..., limit: _Optional[int] = ..., metric_aggregations: _Optional[_Iterable[_Union[MetricAggregation, str]]] = ...) -> None: ...

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

class SamplingMetadata(_message.Message):
    __slots__ = ("samples_read_count", "sampling_space_size")
    SAMPLES_READ_COUNT_FIELD_NUMBER: _ClassVar[int]
    SAMPLING_SPACE_SIZE_FIELD_NUMBER: _ClassVar[int]
    samples_read_count: int
    sampling_space_size: int
    def __init__(self, samples_read_count: _Optional[int] = ..., sampling_space_size: _Optional[int] = ...) -> None: ...

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

class PivotHeader(_message.Message):
    __slots__ = ("pivot_dimension_headers", "row_count")
    PIVOT_DIMENSION_HEADERS_FIELD_NUMBER: _ClassVar[int]
    ROW_COUNT_FIELD_NUMBER: _ClassVar[int]
    pivot_dimension_headers: _containers.RepeatedCompositeFieldContainer[PivotDimensionHeader]
    row_count: int
    def __init__(self, pivot_dimension_headers: _Optional[_Iterable[_Union[PivotDimensionHeader, _Mapping]]] = ..., row_count: _Optional[int] = ...) -> None: ...

class PivotDimensionHeader(_message.Message):
    __slots__ = ("dimension_values",)
    DIMENSION_VALUES_FIELD_NUMBER: _ClassVar[int]
    dimension_values: _containers.RepeatedCompositeFieldContainer[DimensionValue]
    def __init__(self, dimension_values: _Optional[_Iterable[_Union[DimensionValue, _Mapping]]] = ...) -> None: ...

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

class NumericValue(_message.Message):
    __slots__ = ("int64_value", "double_value")
    INT64_VALUE_FIELD_NUMBER: _ClassVar[int]
    DOUBLE_VALUE_FIELD_NUMBER: _ClassVar[int]
    int64_value: int
    double_value: float
    def __init__(self, int64_value: _Optional[int] = ..., double_value: _Optional[float] = ...) -> None: ...

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

class DimensionMetadata(_message.Message):
    __slots__ = ("api_name", "ui_name", "description", "deprecated_api_names", "custom_definition", "category")
    API_NAME_FIELD_NUMBER: _ClassVar[int]
    UI_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DEPRECATED_API_NAMES_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_DEFINITION_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    api_name: str
    ui_name: str
    description: str
    deprecated_api_names: _containers.RepeatedScalarFieldContainer[str]
    custom_definition: bool
    category: str
    def __init__(self, api_name: _Optional[str] = ..., ui_name: _Optional[str] = ..., description: _Optional[str] = ..., deprecated_api_names: _Optional[_Iterable[str]] = ..., custom_definition: bool = ..., category: _Optional[str] = ...) -> None: ...

class MetricMetadata(_message.Message):
    __slots__ = ("api_name", "ui_name", "description", "deprecated_api_names", "type", "expression", "custom_definition", "blocked_reasons", "category")
    class BlockedReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        BLOCKED_REASON_UNSPECIFIED: _ClassVar[MetricMetadata.BlockedReason]
        NO_REVENUE_METRICS: _ClassVar[MetricMetadata.BlockedReason]
        NO_COST_METRICS: _ClassVar[MetricMetadata.BlockedReason]
    BLOCKED_REASON_UNSPECIFIED: MetricMetadata.BlockedReason
    NO_REVENUE_METRICS: MetricMetadata.BlockedReason
    NO_COST_METRICS: MetricMetadata.BlockedReason
    API_NAME_FIELD_NUMBER: _ClassVar[int]
    UI_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DEPRECATED_API_NAMES_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_DEFINITION_FIELD_NUMBER: _ClassVar[int]
    BLOCKED_REASONS_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    api_name: str
    ui_name: str
    description: str
    deprecated_api_names: _containers.RepeatedScalarFieldContainer[str]
    type: MetricType
    expression: str
    custom_definition: bool
    blocked_reasons: _containers.RepeatedScalarFieldContainer[MetricMetadata.BlockedReason]
    category: str
    def __init__(self, api_name: _Optional[str] = ..., ui_name: _Optional[str] = ..., description: _Optional[str] = ..., deprecated_api_names: _Optional[_Iterable[str]] = ..., type: _Optional[_Union[MetricType, str]] = ..., expression: _Optional[str] = ..., custom_definition: bool = ..., blocked_reasons: _Optional[_Iterable[_Union[MetricMetadata.BlockedReason, str]]] = ..., category: _Optional[str] = ...) -> None: ...

class ComparisonMetadata(_message.Message):
    __slots__ = ("api_name", "ui_name", "description")
    API_NAME_FIELD_NUMBER: _ClassVar[int]
    UI_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    api_name: str
    ui_name: str
    description: str
    def __init__(self, api_name: _Optional[str] = ..., ui_name: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class DimensionCompatibility(_message.Message):
    __slots__ = ("dimension_metadata", "compatibility")
    DIMENSION_METADATA_FIELD_NUMBER: _ClassVar[int]
    COMPATIBILITY_FIELD_NUMBER: _ClassVar[int]
    dimension_metadata: DimensionMetadata
    compatibility: Compatibility
    def __init__(self, dimension_metadata: _Optional[_Union[DimensionMetadata, _Mapping]] = ..., compatibility: _Optional[_Union[Compatibility, str]] = ...) -> None: ...

class MetricCompatibility(_message.Message):
    __slots__ = ("metric_metadata", "compatibility")
    METRIC_METADATA_FIELD_NUMBER: _ClassVar[int]
    COMPATIBILITY_FIELD_NUMBER: _ClassVar[int]
    metric_metadata: MetricMetadata
    compatibility: Compatibility
    def __init__(self, metric_metadata: _Optional[_Union[MetricMetadata, _Mapping]] = ..., compatibility: _Optional[_Union[Compatibility, str]] = ...) -> None: ...
