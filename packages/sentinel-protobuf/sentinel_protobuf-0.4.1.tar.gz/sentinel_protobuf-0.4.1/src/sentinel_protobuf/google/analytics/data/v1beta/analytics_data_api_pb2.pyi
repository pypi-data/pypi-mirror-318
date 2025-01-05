from google.analytics.data.v1beta import data_pb2 as _data_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CheckCompatibilityRequest(_message.Message):
    __slots__ = ("property", "dimensions", "metrics", "dimension_filter", "metric_filter", "compatibility_filter")
    PROPERTY_FIELD_NUMBER: _ClassVar[int]
    DIMENSIONS_FIELD_NUMBER: _ClassVar[int]
    METRICS_FIELD_NUMBER: _ClassVar[int]
    DIMENSION_FILTER_FIELD_NUMBER: _ClassVar[int]
    METRIC_FILTER_FIELD_NUMBER: _ClassVar[int]
    COMPATIBILITY_FILTER_FIELD_NUMBER: _ClassVar[int]
    property: str
    dimensions: _containers.RepeatedCompositeFieldContainer[_data_pb2.Dimension]
    metrics: _containers.RepeatedCompositeFieldContainer[_data_pb2.Metric]
    dimension_filter: _data_pb2.FilterExpression
    metric_filter: _data_pb2.FilterExpression
    compatibility_filter: _data_pb2.Compatibility
    def __init__(self, property: _Optional[str] = ..., dimensions: _Optional[_Iterable[_Union[_data_pb2.Dimension, _Mapping]]] = ..., metrics: _Optional[_Iterable[_Union[_data_pb2.Metric, _Mapping]]] = ..., dimension_filter: _Optional[_Union[_data_pb2.FilterExpression, _Mapping]] = ..., metric_filter: _Optional[_Union[_data_pb2.FilterExpression, _Mapping]] = ..., compatibility_filter: _Optional[_Union[_data_pb2.Compatibility, str]] = ...) -> None: ...

class CheckCompatibilityResponse(_message.Message):
    __slots__ = ("dimension_compatibilities", "metric_compatibilities")
    DIMENSION_COMPATIBILITIES_FIELD_NUMBER: _ClassVar[int]
    METRIC_COMPATIBILITIES_FIELD_NUMBER: _ClassVar[int]
    dimension_compatibilities: _containers.RepeatedCompositeFieldContainer[_data_pb2.DimensionCompatibility]
    metric_compatibilities: _containers.RepeatedCompositeFieldContainer[_data_pb2.MetricCompatibility]
    def __init__(self, dimension_compatibilities: _Optional[_Iterable[_Union[_data_pb2.DimensionCompatibility, _Mapping]]] = ..., metric_compatibilities: _Optional[_Iterable[_Union[_data_pb2.MetricCompatibility, _Mapping]]] = ...) -> None: ...

class Metadata(_message.Message):
    __slots__ = ("name", "dimensions", "metrics", "comparisons")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DIMENSIONS_FIELD_NUMBER: _ClassVar[int]
    METRICS_FIELD_NUMBER: _ClassVar[int]
    COMPARISONS_FIELD_NUMBER: _ClassVar[int]
    name: str
    dimensions: _containers.RepeatedCompositeFieldContainer[_data_pb2.DimensionMetadata]
    metrics: _containers.RepeatedCompositeFieldContainer[_data_pb2.MetricMetadata]
    comparisons: _containers.RepeatedCompositeFieldContainer[_data_pb2.ComparisonMetadata]
    def __init__(self, name: _Optional[str] = ..., dimensions: _Optional[_Iterable[_Union[_data_pb2.DimensionMetadata, _Mapping]]] = ..., metrics: _Optional[_Iterable[_Union[_data_pb2.MetricMetadata, _Mapping]]] = ..., comparisons: _Optional[_Iterable[_Union[_data_pb2.ComparisonMetadata, _Mapping]]] = ...) -> None: ...

class RunReportRequest(_message.Message):
    __slots__ = ("property", "dimensions", "metrics", "date_ranges", "dimension_filter", "metric_filter", "offset", "limit", "metric_aggregations", "order_bys", "currency_code", "cohort_spec", "keep_empty_rows", "return_property_quota", "comparisons")
    PROPERTY_FIELD_NUMBER: _ClassVar[int]
    DIMENSIONS_FIELD_NUMBER: _ClassVar[int]
    METRICS_FIELD_NUMBER: _ClassVar[int]
    DATE_RANGES_FIELD_NUMBER: _ClassVar[int]
    DIMENSION_FILTER_FIELD_NUMBER: _ClassVar[int]
    METRIC_FILTER_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    METRIC_AGGREGATIONS_FIELD_NUMBER: _ClassVar[int]
    ORDER_BYS_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_CODE_FIELD_NUMBER: _ClassVar[int]
    COHORT_SPEC_FIELD_NUMBER: _ClassVar[int]
    KEEP_EMPTY_ROWS_FIELD_NUMBER: _ClassVar[int]
    RETURN_PROPERTY_QUOTA_FIELD_NUMBER: _ClassVar[int]
    COMPARISONS_FIELD_NUMBER: _ClassVar[int]
    property: str
    dimensions: _containers.RepeatedCompositeFieldContainer[_data_pb2.Dimension]
    metrics: _containers.RepeatedCompositeFieldContainer[_data_pb2.Metric]
    date_ranges: _containers.RepeatedCompositeFieldContainer[_data_pb2.DateRange]
    dimension_filter: _data_pb2.FilterExpression
    metric_filter: _data_pb2.FilterExpression
    offset: int
    limit: int
    metric_aggregations: _containers.RepeatedScalarFieldContainer[_data_pb2.MetricAggregation]
    order_bys: _containers.RepeatedCompositeFieldContainer[_data_pb2.OrderBy]
    currency_code: str
    cohort_spec: _data_pb2.CohortSpec
    keep_empty_rows: bool
    return_property_quota: bool
    comparisons: _containers.RepeatedCompositeFieldContainer[_data_pb2.Comparison]
    def __init__(self, property: _Optional[str] = ..., dimensions: _Optional[_Iterable[_Union[_data_pb2.Dimension, _Mapping]]] = ..., metrics: _Optional[_Iterable[_Union[_data_pb2.Metric, _Mapping]]] = ..., date_ranges: _Optional[_Iterable[_Union[_data_pb2.DateRange, _Mapping]]] = ..., dimension_filter: _Optional[_Union[_data_pb2.FilterExpression, _Mapping]] = ..., metric_filter: _Optional[_Union[_data_pb2.FilterExpression, _Mapping]] = ..., offset: _Optional[int] = ..., limit: _Optional[int] = ..., metric_aggregations: _Optional[_Iterable[_Union[_data_pb2.MetricAggregation, str]]] = ..., order_bys: _Optional[_Iterable[_Union[_data_pb2.OrderBy, _Mapping]]] = ..., currency_code: _Optional[str] = ..., cohort_spec: _Optional[_Union[_data_pb2.CohortSpec, _Mapping]] = ..., keep_empty_rows: bool = ..., return_property_quota: bool = ..., comparisons: _Optional[_Iterable[_Union[_data_pb2.Comparison, _Mapping]]] = ...) -> None: ...

class RunReportResponse(_message.Message):
    __slots__ = ("dimension_headers", "metric_headers", "rows", "totals", "maximums", "minimums", "row_count", "metadata", "property_quota", "kind")
    DIMENSION_HEADERS_FIELD_NUMBER: _ClassVar[int]
    METRIC_HEADERS_FIELD_NUMBER: _ClassVar[int]
    ROWS_FIELD_NUMBER: _ClassVar[int]
    TOTALS_FIELD_NUMBER: _ClassVar[int]
    MAXIMUMS_FIELD_NUMBER: _ClassVar[int]
    MINIMUMS_FIELD_NUMBER: _ClassVar[int]
    ROW_COUNT_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_QUOTA_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    dimension_headers: _containers.RepeatedCompositeFieldContainer[_data_pb2.DimensionHeader]
    metric_headers: _containers.RepeatedCompositeFieldContainer[_data_pb2.MetricHeader]
    rows: _containers.RepeatedCompositeFieldContainer[_data_pb2.Row]
    totals: _containers.RepeatedCompositeFieldContainer[_data_pb2.Row]
    maximums: _containers.RepeatedCompositeFieldContainer[_data_pb2.Row]
    minimums: _containers.RepeatedCompositeFieldContainer[_data_pb2.Row]
    row_count: int
    metadata: _data_pb2.ResponseMetaData
    property_quota: _data_pb2.PropertyQuota
    kind: str
    def __init__(self, dimension_headers: _Optional[_Iterable[_Union[_data_pb2.DimensionHeader, _Mapping]]] = ..., metric_headers: _Optional[_Iterable[_Union[_data_pb2.MetricHeader, _Mapping]]] = ..., rows: _Optional[_Iterable[_Union[_data_pb2.Row, _Mapping]]] = ..., totals: _Optional[_Iterable[_Union[_data_pb2.Row, _Mapping]]] = ..., maximums: _Optional[_Iterable[_Union[_data_pb2.Row, _Mapping]]] = ..., minimums: _Optional[_Iterable[_Union[_data_pb2.Row, _Mapping]]] = ..., row_count: _Optional[int] = ..., metadata: _Optional[_Union[_data_pb2.ResponseMetaData, _Mapping]] = ..., property_quota: _Optional[_Union[_data_pb2.PropertyQuota, _Mapping]] = ..., kind: _Optional[str] = ...) -> None: ...

class RunPivotReportRequest(_message.Message):
    __slots__ = ("property", "dimensions", "metrics", "date_ranges", "pivots", "dimension_filter", "metric_filter", "currency_code", "cohort_spec", "keep_empty_rows", "return_property_quota", "comparisons")
    PROPERTY_FIELD_NUMBER: _ClassVar[int]
    DIMENSIONS_FIELD_NUMBER: _ClassVar[int]
    METRICS_FIELD_NUMBER: _ClassVar[int]
    DATE_RANGES_FIELD_NUMBER: _ClassVar[int]
    PIVOTS_FIELD_NUMBER: _ClassVar[int]
    DIMENSION_FILTER_FIELD_NUMBER: _ClassVar[int]
    METRIC_FILTER_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_CODE_FIELD_NUMBER: _ClassVar[int]
    COHORT_SPEC_FIELD_NUMBER: _ClassVar[int]
    KEEP_EMPTY_ROWS_FIELD_NUMBER: _ClassVar[int]
    RETURN_PROPERTY_QUOTA_FIELD_NUMBER: _ClassVar[int]
    COMPARISONS_FIELD_NUMBER: _ClassVar[int]
    property: str
    dimensions: _containers.RepeatedCompositeFieldContainer[_data_pb2.Dimension]
    metrics: _containers.RepeatedCompositeFieldContainer[_data_pb2.Metric]
    date_ranges: _containers.RepeatedCompositeFieldContainer[_data_pb2.DateRange]
    pivots: _containers.RepeatedCompositeFieldContainer[_data_pb2.Pivot]
    dimension_filter: _data_pb2.FilterExpression
    metric_filter: _data_pb2.FilterExpression
    currency_code: str
    cohort_spec: _data_pb2.CohortSpec
    keep_empty_rows: bool
    return_property_quota: bool
    comparisons: _containers.RepeatedCompositeFieldContainer[_data_pb2.Comparison]
    def __init__(self, property: _Optional[str] = ..., dimensions: _Optional[_Iterable[_Union[_data_pb2.Dimension, _Mapping]]] = ..., metrics: _Optional[_Iterable[_Union[_data_pb2.Metric, _Mapping]]] = ..., date_ranges: _Optional[_Iterable[_Union[_data_pb2.DateRange, _Mapping]]] = ..., pivots: _Optional[_Iterable[_Union[_data_pb2.Pivot, _Mapping]]] = ..., dimension_filter: _Optional[_Union[_data_pb2.FilterExpression, _Mapping]] = ..., metric_filter: _Optional[_Union[_data_pb2.FilterExpression, _Mapping]] = ..., currency_code: _Optional[str] = ..., cohort_spec: _Optional[_Union[_data_pb2.CohortSpec, _Mapping]] = ..., keep_empty_rows: bool = ..., return_property_quota: bool = ..., comparisons: _Optional[_Iterable[_Union[_data_pb2.Comparison, _Mapping]]] = ...) -> None: ...

class RunPivotReportResponse(_message.Message):
    __slots__ = ("pivot_headers", "dimension_headers", "metric_headers", "rows", "aggregates", "metadata", "property_quota", "kind")
    PIVOT_HEADERS_FIELD_NUMBER: _ClassVar[int]
    DIMENSION_HEADERS_FIELD_NUMBER: _ClassVar[int]
    METRIC_HEADERS_FIELD_NUMBER: _ClassVar[int]
    ROWS_FIELD_NUMBER: _ClassVar[int]
    AGGREGATES_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_QUOTA_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    pivot_headers: _containers.RepeatedCompositeFieldContainer[_data_pb2.PivotHeader]
    dimension_headers: _containers.RepeatedCompositeFieldContainer[_data_pb2.DimensionHeader]
    metric_headers: _containers.RepeatedCompositeFieldContainer[_data_pb2.MetricHeader]
    rows: _containers.RepeatedCompositeFieldContainer[_data_pb2.Row]
    aggregates: _containers.RepeatedCompositeFieldContainer[_data_pb2.Row]
    metadata: _data_pb2.ResponseMetaData
    property_quota: _data_pb2.PropertyQuota
    kind: str
    def __init__(self, pivot_headers: _Optional[_Iterable[_Union[_data_pb2.PivotHeader, _Mapping]]] = ..., dimension_headers: _Optional[_Iterable[_Union[_data_pb2.DimensionHeader, _Mapping]]] = ..., metric_headers: _Optional[_Iterable[_Union[_data_pb2.MetricHeader, _Mapping]]] = ..., rows: _Optional[_Iterable[_Union[_data_pb2.Row, _Mapping]]] = ..., aggregates: _Optional[_Iterable[_Union[_data_pb2.Row, _Mapping]]] = ..., metadata: _Optional[_Union[_data_pb2.ResponseMetaData, _Mapping]] = ..., property_quota: _Optional[_Union[_data_pb2.PropertyQuota, _Mapping]] = ..., kind: _Optional[str] = ...) -> None: ...

class BatchRunReportsRequest(_message.Message):
    __slots__ = ("property", "requests")
    PROPERTY_FIELD_NUMBER: _ClassVar[int]
    REQUESTS_FIELD_NUMBER: _ClassVar[int]
    property: str
    requests: _containers.RepeatedCompositeFieldContainer[RunReportRequest]
    def __init__(self, property: _Optional[str] = ..., requests: _Optional[_Iterable[_Union[RunReportRequest, _Mapping]]] = ...) -> None: ...

class BatchRunReportsResponse(_message.Message):
    __slots__ = ("reports", "kind")
    REPORTS_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    reports: _containers.RepeatedCompositeFieldContainer[RunReportResponse]
    kind: str
    def __init__(self, reports: _Optional[_Iterable[_Union[RunReportResponse, _Mapping]]] = ..., kind: _Optional[str] = ...) -> None: ...

class BatchRunPivotReportsRequest(_message.Message):
    __slots__ = ("property", "requests")
    PROPERTY_FIELD_NUMBER: _ClassVar[int]
    REQUESTS_FIELD_NUMBER: _ClassVar[int]
    property: str
    requests: _containers.RepeatedCompositeFieldContainer[RunPivotReportRequest]
    def __init__(self, property: _Optional[str] = ..., requests: _Optional[_Iterable[_Union[RunPivotReportRequest, _Mapping]]] = ...) -> None: ...

class BatchRunPivotReportsResponse(_message.Message):
    __slots__ = ("pivot_reports", "kind")
    PIVOT_REPORTS_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    pivot_reports: _containers.RepeatedCompositeFieldContainer[RunPivotReportResponse]
    kind: str
    def __init__(self, pivot_reports: _Optional[_Iterable[_Union[RunPivotReportResponse, _Mapping]]] = ..., kind: _Optional[str] = ...) -> None: ...

class GetMetadataRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class RunRealtimeReportRequest(_message.Message):
    __slots__ = ("property", "dimensions", "metrics", "dimension_filter", "metric_filter", "limit", "metric_aggregations", "order_bys", "return_property_quota", "minute_ranges")
    PROPERTY_FIELD_NUMBER: _ClassVar[int]
    DIMENSIONS_FIELD_NUMBER: _ClassVar[int]
    METRICS_FIELD_NUMBER: _ClassVar[int]
    DIMENSION_FILTER_FIELD_NUMBER: _ClassVar[int]
    METRIC_FILTER_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    METRIC_AGGREGATIONS_FIELD_NUMBER: _ClassVar[int]
    ORDER_BYS_FIELD_NUMBER: _ClassVar[int]
    RETURN_PROPERTY_QUOTA_FIELD_NUMBER: _ClassVar[int]
    MINUTE_RANGES_FIELD_NUMBER: _ClassVar[int]
    property: str
    dimensions: _containers.RepeatedCompositeFieldContainer[_data_pb2.Dimension]
    metrics: _containers.RepeatedCompositeFieldContainer[_data_pb2.Metric]
    dimension_filter: _data_pb2.FilterExpression
    metric_filter: _data_pb2.FilterExpression
    limit: int
    metric_aggregations: _containers.RepeatedScalarFieldContainer[_data_pb2.MetricAggregation]
    order_bys: _containers.RepeatedCompositeFieldContainer[_data_pb2.OrderBy]
    return_property_quota: bool
    minute_ranges: _containers.RepeatedCompositeFieldContainer[_data_pb2.MinuteRange]
    def __init__(self, property: _Optional[str] = ..., dimensions: _Optional[_Iterable[_Union[_data_pb2.Dimension, _Mapping]]] = ..., metrics: _Optional[_Iterable[_Union[_data_pb2.Metric, _Mapping]]] = ..., dimension_filter: _Optional[_Union[_data_pb2.FilterExpression, _Mapping]] = ..., metric_filter: _Optional[_Union[_data_pb2.FilterExpression, _Mapping]] = ..., limit: _Optional[int] = ..., metric_aggregations: _Optional[_Iterable[_Union[_data_pb2.MetricAggregation, str]]] = ..., order_bys: _Optional[_Iterable[_Union[_data_pb2.OrderBy, _Mapping]]] = ..., return_property_quota: bool = ..., minute_ranges: _Optional[_Iterable[_Union[_data_pb2.MinuteRange, _Mapping]]] = ...) -> None: ...

class RunRealtimeReportResponse(_message.Message):
    __slots__ = ("dimension_headers", "metric_headers", "rows", "totals", "maximums", "minimums", "row_count", "property_quota", "kind")
    DIMENSION_HEADERS_FIELD_NUMBER: _ClassVar[int]
    METRIC_HEADERS_FIELD_NUMBER: _ClassVar[int]
    ROWS_FIELD_NUMBER: _ClassVar[int]
    TOTALS_FIELD_NUMBER: _ClassVar[int]
    MAXIMUMS_FIELD_NUMBER: _ClassVar[int]
    MINIMUMS_FIELD_NUMBER: _ClassVar[int]
    ROW_COUNT_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_QUOTA_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    dimension_headers: _containers.RepeatedCompositeFieldContainer[_data_pb2.DimensionHeader]
    metric_headers: _containers.RepeatedCompositeFieldContainer[_data_pb2.MetricHeader]
    rows: _containers.RepeatedCompositeFieldContainer[_data_pb2.Row]
    totals: _containers.RepeatedCompositeFieldContainer[_data_pb2.Row]
    maximums: _containers.RepeatedCompositeFieldContainer[_data_pb2.Row]
    minimums: _containers.RepeatedCompositeFieldContainer[_data_pb2.Row]
    row_count: int
    property_quota: _data_pb2.PropertyQuota
    kind: str
    def __init__(self, dimension_headers: _Optional[_Iterable[_Union[_data_pb2.DimensionHeader, _Mapping]]] = ..., metric_headers: _Optional[_Iterable[_Union[_data_pb2.MetricHeader, _Mapping]]] = ..., rows: _Optional[_Iterable[_Union[_data_pb2.Row, _Mapping]]] = ..., totals: _Optional[_Iterable[_Union[_data_pb2.Row, _Mapping]]] = ..., maximums: _Optional[_Iterable[_Union[_data_pb2.Row, _Mapping]]] = ..., minimums: _Optional[_Iterable[_Union[_data_pb2.Row, _Mapping]]] = ..., row_count: _Optional[int] = ..., property_quota: _Optional[_Union[_data_pb2.PropertyQuota, _Mapping]] = ..., kind: _Optional[str] = ...) -> None: ...

class GetAudienceExportRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListAudienceExportsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListAudienceExportsResponse(_message.Message):
    __slots__ = ("audience_exports", "next_page_token")
    AUDIENCE_EXPORTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    audience_exports: _containers.RepeatedCompositeFieldContainer[AudienceExport]
    next_page_token: str
    def __init__(self, audience_exports: _Optional[_Iterable[_Union[AudienceExport, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class CreateAudienceExportRequest(_message.Message):
    __slots__ = ("parent", "audience_export")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    AUDIENCE_EXPORT_FIELD_NUMBER: _ClassVar[int]
    parent: str
    audience_export: AudienceExport
    def __init__(self, parent: _Optional[str] = ..., audience_export: _Optional[_Union[AudienceExport, _Mapping]] = ...) -> None: ...

class AudienceExport(_message.Message):
    __slots__ = ("name", "audience", "audience_display_name", "dimensions", "state", "begin_creating_time", "creation_quota_tokens_charged", "row_count", "error_message", "percentage_completed")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[AudienceExport.State]
        CREATING: _ClassVar[AudienceExport.State]
        ACTIVE: _ClassVar[AudienceExport.State]
        FAILED: _ClassVar[AudienceExport.State]
    STATE_UNSPECIFIED: AudienceExport.State
    CREATING: AudienceExport.State
    ACTIVE: AudienceExport.State
    FAILED: AudienceExport.State
    NAME_FIELD_NUMBER: _ClassVar[int]
    AUDIENCE_FIELD_NUMBER: _ClassVar[int]
    AUDIENCE_DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DIMENSIONS_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    BEGIN_CREATING_TIME_FIELD_NUMBER: _ClassVar[int]
    CREATION_QUOTA_TOKENS_CHARGED_FIELD_NUMBER: _ClassVar[int]
    ROW_COUNT_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    PERCENTAGE_COMPLETED_FIELD_NUMBER: _ClassVar[int]
    name: str
    audience: str
    audience_display_name: str
    dimensions: _containers.RepeatedCompositeFieldContainer[AudienceDimension]
    state: AudienceExport.State
    begin_creating_time: _timestamp_pb2.Timestamp
    creation_quota_tokens_charged: int
    row_count: int
    error_message: str
    percentage_completed: float
    def __init__(self, name: _Optional[str] = ..., audience: _Optional[str] = ..., audience_display_name: _Optional[str] = ..., dimensions: _Optional[_Iterable[_Union[AudienceDimension, _Mapping]]] = ..., state: _Optional[_Union[AudienceExport.State, str]] = ..., begin_creating_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., creation_quota_tokens_charged: _Optional[int] = ..., row_count: _Optional[int] = ..., error_message: _Optional[str] = ..., percentage_completed: _Optional[float] = ...) -> None: ...

class AudienceExportMetadata(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class QueryAudienceExportRequest(_message.Message):
    __slots__ = ("name", "offset", "limit")
    NAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    name: str
    offset: int
    limit: int
    def __init__(self, name: _Optional[str] = ..., offset: _Optional[int] = ..., limit: _Optional[int] = ...) -> None: ...

class QueryAudienceExportResponse(_message.Message):
    __slots__ = ("audience_export", "audience_rows", "row_count")
    AUDIENCE_EXPORT_FIELD_NUMBER: _ClassVar[int]
    AUDIENCE_ROWS_FIELD_NUMBER: _ClassVar[int]
    ROW_COUNT_FIELD_NUMBER: _ClassVar[int]
    audience_export: AudienceExport
    audience_rows: _containers.RepeatedCompositeFieldContainer[AudienceRow]
    row_count: int
    def __init__(self, audience_export: _Optional[_Union[AudienceExport, _Mapping]] = ..., audience_rows: _Optional[_Iterable[_Union[AudienceRow, _Mapping]]] = ..., row_count: _Optional[int] = ...) -> None: ...

class AudienceRow(_message.Message):
    __slots__ = ("dimension_values",)
    DIMENSION_VALUES_FIELD_NUMBER: _ClassVar[int]
    dimension_values: _containers.RepeatedCompositeFieldContainer[AudienceDimensionValue]
    def __init__(self, dimension_values: _Optional[_Iterable[_Union[AudienceDimensionValue, _Mapping]]] = ...) -> None: ...

class AudienceDimension(_message.Message):
    __slots__ = ("dimension_name",)
    DIMENSION_NAME_FIELD_NUMBER: _ClassVar[int]
    dimension_name: str
    def __init__(self, dimension_name: _Optional[str] = ...) -> None: ...

class AudienceDimensionValue(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: str
    def __init__(self, value: _Optional[str] = ...) -> None: ...
