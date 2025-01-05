from google.analytics.data.v1alpha import data_pb2 as _data_pb2
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

class CreateRecurringAudienceListRequest(_message.Message):
    __slots__ = ("parent", "recurring_audience_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    RECURRING_AUDIENCE_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: str
    recurring_audience_list: RecurringAudienceList
    def __init__(self, parent: _Optional[str] = ..., recurring_audience_list: _Optional[_Union[RecurringAudienceList, _Mapping]] = ...) -> None: ...

class RecurringAudienceList(_message.Message):
    __slots__ = ("name", "audience", "audience_display_name", "dimensions", "active_days_remaining", "audience_lists", "webhook_notification")
    NAME_FIELD_NUMBER: _ClassVar[int]
    AUDIENCE_FIELD_NUMBER: _ClassVar[int]
    AUDIENCE_DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DIMENSIONS_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_DAYS_REMAINING_FIELD_NUMBER: _ClassVar[int]
    AUDIENCE_LISTS_FIELD_NUMBER: _ClassVar[int]
    WEBHOOK_NOTIFICATION_FIELD_NUMBER: _ClassVar[int]
    name: str
    audience: str
    audience_display_name: str
    dimensions: _containers.RepeatedCompositeFieldContainer[AudienceDimension]
    active_days_remaining: int
    audience_lists: _containers.RepeatedScalarFieldContainer[str]
    webhook_notification: WebhookNotification
    def __init__(self, name: _Optional[str] = ..., audience: _Optional[str] = ..., audience_display_name: _Optional[str] = ..., dimensions: _Optional[_Iterable[_Union[AudienceDimension, _Mapping]]] = ..., active_days_remaining: _Optional[int] = ..., audience_lists: _Optional[_Iterable[str]] = ..., webhook_notification: _Optional[_Union[WebhookNotification, _Mapping]] = ...) -> None: ...

class WebhookNotification(_message.Message):
    __slots__ = ("uri", "channel_token")
    URI_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_TOKEN_FIELD_NUMBER: _ClassVar[int]
    uri: str
    channel_token: str
    def __init__(self, uri: _Optional[str] = ..., channel_token: _Optional[str] = ...) -> None: ...

class GetRecurringAudienceListRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListRecurringAudienceListsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListRecurringAudienceListsResponse(_message.Message):
    __slots__ = ("recurring_audience_lists", "next_page_token")
    RECURRING_AUDIENCE_LISTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    recurring_audience_lists: _containers.RepeatedCompositeFieldContainer[RecurringAudienceList]
    next_page_token: str
    def __init__(self, recurring_audience_lists: _Optional[_Iterable[_Union[RecurringAudienceList, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class GetPropertyQuotasSnapshotRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class PropertyQuotasSnapshot(_message.Message):
    __slots__ = ("name", "core_property_quota", "realtime_property_quota", "funnel_property_quota")
    NAME_FIELD_NUMBER: _ClassVar[int]
    CORE_PROPERTY_QUOTA_FIELD_NUMBER: _ClassVar[int]
    REALTIME_PROPERTY_QUOTA_FIELD_NUMBER: _ClassVar[int]
    FUNNEL_PROPERTY_QUOTA_FIELD_NUMBER: _ClassVar[int]
    name: str
    core_property_quota: _data_pb2.PropertyQuota
    realtime_property_quota: _data_pb2.PropertyQuota
    funnel_property_quota: _data_pb2.PropertyQuota
    def __init__(self, name: _Optional[str] = ..., core_property_quota: _Optional[_Union[_data_pb2.PropertyQuota, _Mapping]] = ..., realtime_property_quota: _Optional[_Union[_data_pb2.PropertyQuota, _Mapping]] = ..., funnel_property_quota: _Optional[_Union[_data_pb2.PropertyQuota, _Mapping]] = ...) -> None: ...

class GetAudienceListRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListAudienceListsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListAudienceListsResponse(_message.Message):
    __slots__ = ("audience_lists", "next_page_token")
    AUDIENCE_LISTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    audience_lists: _containers.RepeatedCompositeFieldContainer[AudienceList]
    next_page_token: str
    def __init__(self, audience_lists: _Optional[_Iterable[_Union[AudienceList, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class CreateAudienceListRequest(_message.Message):
    __slots__ = ("parent", "audience_list")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    AUDIENCE_LIST_FIELD_NUMBER: _ClassVar[int]
    parent: str
    audience_list: AudienceList
    def __init__(self, parent: _Optional[str] = ..., audience_list: _Optional[_Union[AudienceList, _Mapping]] = ...) -> None: ...

class AudienceList(_message.Message):
    __slots__ = ("name", "audience", "audience_display_name", "dimensions", "state", "begin_creating_time", "creation_quota_tokens_charged", "row_count", "error_message", "percentage_completed", "recurring_audience_list", "webhook_notification")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[AudienceList.State]
        CREATING: _ClassVar[AudienceList.State]
        ACTIVE: _ClassVar[AudienceList.State]
        FAILED: _ClassVar[AudienceList.State]
    STATE_UNSPECIFIED: AudienceList.State
    CREATING: AudienceList.State
    ACTIVE: AudienceList.State
    FAILED: AudienceList.State
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
    RECURRING_AUDIENCE_LIST_FIELD_NUMBER: _ClassVar[int]
    WEBHOOK_NOTIFICATION_FIELD_NUMBER: _ClassVar[int]
    name: str
    audience: str
    audience_display_name: str
    dimensions: _containers.RepeatedCompositeFieldContainer[AudienceDimension]
    state: AudienceList.State
    begin_creating_time: _timestamp_pb2.Timestamp
    creation_quota_tokens_charged: int
    row_count: int
    error_message: str
    percentage_completed: float
    recurring_audience_list: str
    webhook_notification: WebhookNotification
    def __init__(self, name: _Optional[str] = ..., audience: _Optional[str] = ..., audience_display_name: _Optional[str] = ..., dimensions: _Optional[_Iterable[_Union[AudienceDimension, _Mapping]]] = ..., state: _Optional[_Union[AudienceList.State, str]] = ..., begin_creating_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., creation_quota_tokens_charged: _Optional[int] = ..., row_count: _Optional[int] = ..., error_message: _Optional[str] = ..., percentage_completed: _Optional[float] = ..., recurring_audience_list: _Optional[str] = ..., webhook_notification: _Optional[_Union[WebhookNotification, _Mapping]] = ...) -> None: ...

class AudienceListMetadata(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class QueryAudienceListRequest(_message.Message):
    __slots__ = ("name", "offset", "limit")
    NAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    name: str
    offset: int
    limit: int
    def __init__(self, name: _Optional[str] = ..., offset: _Optional[int] = ..., limit: _Optional[int] = ...) -> None: ...

class QueryAudienceListResponse(_message.Message):
    __slots__ = ("audience_list", "audience_rows", "row_count")
    AUDIENCE_LIST_FIELD_NUMBER: _ClassVar[int]
    AUDIENCE_ROWS_FIELD_NUMBER: _ClassVar[int]
    ROW_COUNT_FIELD_NUMBER: _ClassVar[int]
    audience_list: AudienceList
    audience_rows: _containers.RepeatedCompositeFieldContainer[AudienceRow]
    row_count: int
    def __init__(self, audience_list: _Optional[_Union[AudienceList, _Mapping]] = ..., audience_rows: _Optional[_Iterable[_Union[AudienceRow, _Mapping]]] = ..., row_count: _Optional[int] = ...) -> None: ...

class SheetExportAudienceListRequest(_message.Message):
    __slots__ = ("name", "offset", "limit")
    NAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    name: str
    offset: int
    limit: int
    def __init__(self, name: _Optional[str] = ..., offset: _Optional[int] = ..., limit: _Optional[int] = ...) -> None: ...

class SheetExportAudienceListResponse(_message.Message):
    __slots__ = ("spreadsheet_uri", "spreadsheet_id", "row_count", "audience_list")
    SPREADSHEET_URI_FIELD_NUMBER: _ClassVar[int]
    SPREADSHEET_ID_FIELD_NUMBER: _ClassVar[int]
    ROW_COUNT_FIELD_NUMBER: _ClassVar[int]
    AUDIENCE_LIST_FIELD_NUMBER: _ClassVar[int]
    spreadsheet_uri: str
    spreadsheet_id: str
    row_count: int
    audience_list: AudienceList
    def __init__(self, spreadsheet_uri: _Optional[str] = ..., spreadsheet_id: _Optional[str] = ..., row_count: _Optional[int] = ..., audience_list: _Optional[_Union[AudienceList, _Mapping]] = ...) -> None: ...

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

class RunFunnelReportRequest(_message.Message):
    __slots__ = ("property", "date_ranges", "funnel", "funnel_breakdown", "funnel_next_action", "funnel_visualization_type", "segments", "limit", "dimension_filter", "return_property_quota")
    class FunnelVisualizationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FUNNEL_VISUALIZATION_TYPE_UNSPECIFIED: _ClassVar[RunFunnelReportRequest.FunnelVisualizationType]
        STANDARD_FUNNEL: _ClassVar[RunFunnelReportRequest.FunnelVisualizationType]
        TRENDED_FUNNEL: _ClassVar[RunFunnelReportRequest.FunnelVisualizationType]
    FUNNEL_VISUALIZATION_TYPE_UNSPECIFIED: RunFunnelReportRequest.FunnelVisualizationType
    STANDARD_FUNNEL: RunFunnelReportRequest.FunnelVisualizationType
    TRENDED_FUNNEL: RunFunnelReportRequest.FunnelVisualizationType
    PROPERTY_FIELD_NUMBER: _ClassVar[int]
    DATE_RANGES_FIELD_NUMBER: _ClassVar[int]
    FUNNEL_FIELD_NUMBER: _ClassVar[int]
    FUNNEL_BREAKDOWN_FIELD_NUMBER: _ClassVar[int]
    FUNNEL_NEXT_ACTION_FIELD_NUMBER: _ClassVar[int]
    FUNNEL_VISUALIZATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    SEGMENTS_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    DIMENSION_FILTER_FIELD_NUMBER: _ClassVar[int]
    RETURN_PROPERTY_QUOTA_FIELD_NUMBER: _ClassVar[int]
    property: str
    date_ranges: _containers.RepeatedCompositeFieldContainer[_data_pb2.DateRange]
    funnel: _data_pb2.Funnel
    funnel_breakdown: _data_pb2.FunnelBreakdown
    funnel_next_action: _data_pb2.FunnelNextAction
    funnel_visualization_type: RunFunnelReportRequest.FunnelVisualizationType
    segments: _containers.RepeatedCompositeFieldContainer[_data_pb2.Segment]
    limit: int
    dimension_filter: _data_pb2.FilterExpression
    return_property_quota: bool
    def __init__(self, property: _Optional[str] = ..., date_ranges: _Optional[_Iterable[_Union[_data_pb2.DateRange, _Mapping]]] = ..., funnel: _Optional[_Union[_data_pb2.Funnel, _Mapping]] = ..., funnel_breakdown: _Optional[_Union[_data_pb2.FunnelBreakdown, _Mapping]] = ..., funnel_next_action: _Optional[_Union[_data_pb2.FunnelNextAction, _Mapping]] = ..., funnel_visualization_type: _Optional[_Union[RunFunnelReportRequest.FunnelVisualizationType, str]] = ..., segments: _Optional[_Iterable[_Union[_data_pb2.Segment, _Mapping]]] = ..., limit: _Optional[int] = ..., dimension_filter: _Optional[_Union[_data_pb2.FilterExpression, _Mapping]] = ..., return_property_quota: bool = ...) -> None: ...

class RunFunnelReportResponse(_message.Message):
    __slots__ = ("funnel_table", "funnel_visualization", "property_quota", "kind")
    FUNNEL_TABLE_FIELD_NUMBER: _ClassVar[int]
    FUNNEL_VISUALIZATION_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_QUOTA_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    funnel_table: _data_pb2.FunnelSubReport
    funnel_visualization: _data_pb2.FunnelSubReport
    property_quota: _data_pb2.PropertyQuota
    kind: str
    def __init__(self, funnel_table: _Optional[_Union[_data_pb2.FunnelSubReport, _Mapping]] = ..., funnel_visualization: _Optional[_Union[_data_pb2.FunnelSubReport, _Mapping]] = ..., property_quota: _Optional[_Union[_data_pb2.PropertyQuota, _Mapping]] = ..., kind: _Optional[str] = ...) -> None: ...

class ReportTask(_message.Message):
    __slots__ = ("name", "report_definition", "report_metadata")
    class ReportDefinition(_message.Message):
        __slots__ = ("dimensions", "metrics", "date_ranges", "dimension_filter", "metric_filter", "offset", "limit", "metric_aggregations", "order_bys", "currency_code", "cohort_spec", "keep_empty_rows", "sampling_level")
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
        SAMPLING_LEVEL_FIELD_NUMBER: _ClassVar[int]
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
        sampling_level: _data_pb2.SamplingLevel
        def __init__(self, dimensions: _Optional[_Iterable[_Union[_data_pb2.Dimension, _Mapping]]] = ..., metrics: _Optional[_Iterable[_Union[_data_pb2.Metric, _Mapping]]] = ..., date_ranges: _Optional[_Iterable[_Union[_data_pb2.DateRange, _Mapping]]] = ..., dimension_filter: _Optional[_Union[_data_pb2.FilterExpression, _Mapping]] = ..., metric_filter: _Optional[_Union[_data_pb2.FilterExpression, _Mapping]] = ..., offset: _Optional[int] = ..., limit: _Optional[int] = ..., metric_aggregations: _Optional[_Iterable[_Union[_data_pb2.MetricAggregation, str]]] = ..., order_bys: _Optional[_Iterable[_Union[_data_pb2.OrderBy, _Mapping]]] = ..., currency_code: _Optional[str] = ..., cohort_spec: _Optional[_Union[_data_pb2.CohortSpec, _Mapping]] = ..., keep_empty_rows: bool = ..., sampling_level: _Optional[_Union[_data_pb2.SamplingLevel, str]] = ...) -> None: ...
    class ReportMetadata(_message.Message):
        __slots__ = ("state", "begin_creating_time", "creation_quota_tokens_charged", "task_row_count", "error_message", "total_row_count")
        class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            STATE_UNSPECIFIED: _ClassVar[ReportTask.ReportMetadata.State]
            CREATING: _ClassVar[ReportTask.ReportMetadata.State]
            ACTIVE: _ClassVar[ReportTask.ReportMetadata.State]
            FAILED: _ClassVar[ReportTask.ReportMetadata.State]
        STATE_UNSPECIFIED: ReportTask.ReportMetadata.State
        CREATING: ReportTask.ReportMetadata.State
        ACTIVE: ReportTask.ReportMetadata.State
        FAILED: ReportTask.ReportMetadata.State
        STATE_FIELD_NUMBER: _ClassVar[int]
        BEGIN_CREATING_TIME_FIELD_NUMBER: _ClassVar[int]
        CREATION_QUOTA_TOKENS_CHARGED_FIELD_NUMBER: _ClassVar[int]
        TASK_ROW_COUNT_FIELD_NUMBER: _ClassVar[int]
        ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        TOTAL_ROW_COUNT_FIELD_NUMBER: _ClassVar[int]
        state: ReportTask.ReportMetadata.State
        begin_creating_time: _timestamp_pb2.Timestamp
        creation_quota_tokens_charged: int
        task_row_count: int
        error_message: str
        total_row_count: int
        def __init__(self, state: _Optional[_Union[ReportTask.ReportMetadata.State, str]] = ..., begin_creating_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., creation_quota_tokens_charged: _Optional[int] = ..., task_row_count: _Optional[int] = ..., error_message: _Optional[str] = ..., total_row_count: _Optional[int] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    REPORT_DEFINITION_FIELD_NUMBER: _ClassVar[int]
    REPORT_METADATA_FIELD_NUMBER: _ClassVar[int]
    name: str
    report_definition: ReportTask.ReportDefinition
    report_metadata: ReportTask.ReportMetadata
    def __init__(self, name: _Optional[str] = ..., report_definition: _Optional[_Union[ReportTask.ReportDefinition, _Mapping]] = ..., report_metadata: _Optional[_Union[ReportTask.ReportMetadata, _Mapping]] = ...) -> None: ...

class CreateReportTaskRequest(_message.Message):
    __slots__ = ("parent", "report_task")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    REPORT_TASK_FIELD_NUMBER: _ClassVar[int]
    parent: str
    report_task: ReportTask
    def __init__(self, parent: _Optional[str] = ..., report_task: _Optional[_Union[ReportTask, _Mapping]] = ...) -> None: ...

class ReportTaskMetadata(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class QueryReportTaskRequest(_message.Message):
    __slots__ = ("name", "offset", "limit")
    NAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    name: str
    offset: int
    limit: int
    def __init__(self, name: _Optional[str] = ..., offset: _Optional[int] = ..., limit: _Optional[int] = ...) -> None: ...

class QueryReportTaskResponse(_message.Message):
    __slots__ = ("dimension_headers", "metric_headers", "rows", "totals", "maximums", "minimums", "row_count", "metadata")
    DIMENSION_HEADERS_FIELD_NUMBER: _ClassVar[int]
    METRIC_HEADERS_FIELD_NUMBER: _ClassVar[int]
    ROWS_FIELD_NUMBER: _ClassVar[int]
    TOTALS_FIELD_NUMBER: _ClassVar[int]
    MAXIMUMS_FIELD_NUMBER: _ClassVar[int]
    MINIMUMS_FIELD_NUMBER: _ClassVar[int]
    ROW_COUNT_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    dimension_headers: _containers.RepeatedCompositeFieldContainer[_data_pb2.DimensionHeader]
    metric_headers: _containers.RepeatedCompositeFieldContainer[_data_pb2.MetricHeader]
    rows: _containers.RepeatedCompositeFieldContainer[_data_pb2.Row]
    totals: _containers.RepeatedCompositeFieldContainer[_data_pb2.Row]
    maximums: _containers.RepeatedCompositeFieldContainer[_data_pb2.Row]
    minimums: _containers.RepeatedCompositeFieldContainer[_data_pb2.Row]
    row_count: int
    metadata: _data_pb2.ResponseMetaData
    def __init__(self, dimension_headers: _Optional[_Iterable[_Union[_data_pb2.DimensionHeader, _Mapping]]] = ..., metric_headers: _Optional[_Iterable[_Union[_data_pb2.MetricHeader, _Mapping]]] = ..., rows: _Optional[_Iterable[_Union[_data_pb2.Row, _Mapping]]] = ..., totals: _Optional[_Iterable[_Union[_data_pb2.Row, _Mapping]]] = ..., maximums: _Optional[_Iterable[_Union[_data_pb2.Row, _Mapping]]] = ..., minimums: _Optional[_Iterable[_Union[_data_pb2.Row, _Mapping]]] = ..., row_count: _Optional[int] = ..., metadata: _Optional[_Union[_data_pb2.ResponseMetaData, _Mapping]] = ...) -> None: ...

class GetReportTaskRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListReportTasksRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListReportTasksResponse(_message.Message):
    __slots__ = ("report_tasks", "next_page_token")
    REPORT_TASKS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    report_tasks: _containers.RepeatedCompositeFieldContainer[ReportTask]
    next_page_token: str
    def __init__(self, report_tasks: _Optional[_Iterable[_Union[ReportTask, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...
