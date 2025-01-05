from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.bigquery.v2 import data_format_options_pb2 as _data_format_options_pb2
from google.cloud.bigquery.v2 import dataset_reference_pb2 as _dataset_reference_pb2
from google.cloud.bigquery.v2 import error_pb2 as _error_pb2
from google.cloud.bigquery.v2 import job_config_pb2 as _job_config_pb2
from google.cloud.bigquery.v2 import job_creation_reason_pb2 as _job_creation_reason_pb2
from google.cloud.bigquery.v2 import job_reference_pb2 as _job_reference_pb2
from google.cloud.bigquery.v2 import job_stats_pb2 as _job_stats_pb2
from google.cloud.bigquery.v2 import job_status_pb2 as _job_status_pb2
from google.cloud.bigquery.v2 import query_parameter_pb2 as _query_parameter_pb2
from google.cloud.bigquery.v2 import session_info_pb2 as _session_info_pb2
from google.cloud.bigquery.v2 import table_schema_pb2 as _table_schema_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Job(_message.Message):
    __slots__ = ("kind", "etag", "id", "self_link", "user_email", "configuration", "job_reference", "statistics", "status", "principal_subject", "job_creation_reason")
    KIND_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    SELF_LINK_FIELD_NUMBER: _ClassVar[int]
    USER_EMAIL_FIELD_NUMBER: _ClassVar[int]
    CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    JOB_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    STATISTICS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    PRINCIPAL_SUBJECT_FIELD_NUMBER: _ClassVar[int]
    JOB_CREATION_REASON_FIELD_NUMBER: _ClassVar[int]
    kind: str
    etag: str
    id: str
    self_link: str
    user_email: str
    configuration: _job_config_pb2.JobConfiguration
    job_reference: _job_reference_pb2.JobReference
    statistics: _job_stats_pb2.JobStatistics
    status: _job_status_pb2.JobStatus
    principal_subject: str
    job_creation_reason: _job_creation_reason_pb2.JobCreationReason
    def __init__(self, kind: _Optional[str] = ..., etag: _Optional[str] = ..., id: _Optional[str] = ..., self_link: _Optional[str] = ..., user_email: _Optional[str] = ..., configuration: _Optional[_Union[_job_config_pb2.JobConfiguration, _Mapping]] = ..., job_reference: _Optional[_Union[_job_reference_pb2.JobReference, _Mapping]] = ..., statistics: _Optional[_Union[_job_stats_pb2.JobStatistics, _Mapping]] = ..., status: _Optional[_Union[_job_status_pb2.JobStatus, _Mapping]] = ..., principal_subject: _Optional[str] = ..., job_creation_reason: _Optional[_Union[_job_creation_reason_pb2.JobCreationReason, _Mapping]] = ...) -> None: ...

class CancelJobRequest(_message.Message):
    __slots__ = ("project_id", "job_id", "location")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    job_id: str
    location: str
    def __init__(self, project_id: _Optional[str] = ..., job_id: _Optional[str] = ..., location: _Optional[str] = ...) -> None: ...

class JobCancelResponse(_message.Message):
    __slots__ = ("kind", "job")
    KIND_FIELD_NUMBER: _ClassVar[int]
    JOB_FIELD_NUMBER: _ClassVar[int]
    kind: str
    job: Job
    def __init__(self, kind: _Optional[str] = ..., job: _Optional[_Union[Job, _Mapping]] = ...) -> None: ...

class GetJobRequest(_message.Message):
    __slots__ = ("project_id", "job_id", "location")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    job_id: str
    location: str
    def __init__(self, project_id: _Optional[str] = ..., job_id: _Optional[str] = ..., location: _Optional[str] = ...) -> None: ...

class InsertJobRequest(_message.Message):
    __slots__ = ("project_id", "job")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    job: Job
    def __init__(self, project_id: _Optional[str] = ..., job: _Optional[_Union[Job, _Mapping]] = ...) -> None: ...

class DeleteJobRequest(_message.Message):
    __slots__ = ("project_id", "job_id", "location")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    job_id: str
    location: str
    def __init__(self, project_id: _Optional[str] = ..., job_id: _Optional[str] = ..., location: _Optional[str] = ...) -> None: ...

class ListJobsRequest(_message.Message):
    __slots__ = ("project_id", "all_users", "max_results", "min_creation_time", "max_creation_time", "page_token", "projection", "state_filter", "parent_job_id")
    class Projection(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        minimal: _ClassVar[ListJobsRequest.Projection]
        MINIMAL: _ClassVar[ListJobsRequest.Projection]
        full: _ClassVar[ListJobsRequest.Projection]
        FULL: _ClassVar[ListJobsRequest.Projection]
    minimal: ListJobsRequest.Projection
    MINIMAL: ListJobsRequest.Projection
    full: ListJobsRequest.Projection
    FULL: ListJobsRequest.Projection
    class StateFilter(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        done: _ClassVar[ListJobsRequest.StateFilter]
        DONE: _ClassVar[ListJobsRequest.StateFilter]
        pending: _ClassVar[ListJobsRequest.StateFilter]
        PENDING: _ClassVar[ListJobsRequest.StateFilter]
        running: _ClassVar[ListJobsRequest.StateFilter]
        RUNNING: _ClassVar[ListJobsRequest.StateFilter]
    done: ListJobsRequest.StateFilter
    DONE: ListJobsRequest.StateFilter
    pending: ListJobsRequest.StateFilter
    PENDING: ListJobsRequest.StateFilter
    running: ListJobsRequest.StateFilter
    RUNNING: ListJobsRequest.StateFilter
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    ALL_USERS_FIELD_NUMBER: _ClassVar[int]
    MAX_RESULTS_FIELD_NUMBER: _ClassVar[int]
    MIN_CREATION_TIME_FIELD_NUMBER: _ClassVar[int]
    MAX_CREATION_TIME_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PROJECTION_FIELD_NUMBER: _ClassVar[int]
    STATE_FILTER_FIELD_NUMBER: _ClassVar[int]
    PARENT_JOB_ID_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    all_users: bool
    max_results: _wrappers_pb2.Int32Value
    min_creation_time: int
    max_creation_time: _wrappers_pb2.UInt64Value
    page_token: str
    projection: ListJobsRequest.Projection
    state_filter: _containers.RepeatedScalarFieldContainer[ListJobsRequest.StateFilter]
    parent_job_id: str
    def __init__(self, project_id: _Optional[str] = ..., all_users: bool = ..., max_results: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., min_creation_time: _Optional[int] = ..., max_creation_time: _Optional[_Union[_wrappers_pb2.UInt64Value, _Mapping]] = ..., page_token: _Optional[str] = ..., projection: _Optional[_Union[ListJobsRequest.Projection, str]] = ..., state_filter: _Optional[_Iterable[_Union[ListJobsRequest.StateFilter, str]]] = ..., parent_job_id: _Optional[str] = ...) -> None: ...

class ListFormatJob(_message.Message):
    __slots__ = ("id", "kind", "job_reference", "state", "error_result", "statistics", "configuration", "status", "user_email", "principal_subject")
    ID_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    JOB_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ERROR_RESULT_FIELD_NUMBER: _ClassVar[int]
    STATISTICS_FIELD_NUMBER: _ClassVar[int]
    CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    USER_EMAIL_FIELD_NUMBER: _ClassVar[int]
    PRINCIPAL_SUBJECT_FIELD_NUMBER: _ClassVar[int]
    id: str
    kind: str
    job_reference: _job_reference_pb2.JobReference
    state: str
    error_result: _error_pb2.ErrorProto
    statistics: _job_stats_pb2.JobStatistics
    configuration: _job_config_pb2.JobConfiguration
    status: _job_status_pb2.JobStatus
    user_email: str
    principal_subject: str
    def __init__(self, id: _Optional[str] = ..., kind: _Optional[str] = ..., job_reference: _Optional[_Union[_job_reference_pb2.JobReference, _Mapping]] = ..., state: _Optional[str] = ..., error_result: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ..., statistics: _Optional[_Union[_job_stats_pb2.JobStatistics, _Mapping]] = ..., configuration: _Optional[_Union[_job_config_pb2.JobConfiguration, _Mapping]] = ..., status: _Optional[_Union[_job_status_pb2.JobStatus, _Mapping]] = ..., user_email: _Optional[str] = ..., principal_subject: _Optional[str] = ...) -> None: ...

class JobList(_message.Message):
    __slots__ = ("etag", "kind", "next_page_token", "jobs", "unreachable")
    ETAG_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    JOBS_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    etag: str
    kind: str
    next_page_token: str
    jobs: _containers.RepeatedCompositeFieldContainer[ListFormatJob]
    unreachable: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, etag: _Optional[str] = ..., kind: _Optional[str] = ..., next_page_token: _Optional[str] = ..., jobs: _Optional[_Iterable[_Union[ListFormatJob, _Mapping]]] = ..., unreachable: _Optional[_Iterable[str]] = ...) -> None: ...

class GetQueryResultsRequest(_message.Message):
    __slots__ = ("project_id", "job_id", "start_index", "page_token", "max_results", "timeout_ms", "location", "format_options")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    START_INDEX_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    MAX_RESULTS_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_MS_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    FORMAT_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    job_id: str
    start_index: _wrappers_pb2.UInt64Value
    page_token: str
    max_results: _wrappers_pb2.UInt32Value
    timeout_ms: _wrappers_pb2.UInt32Value
    location: str
    format_options: _data_format_options_pb2.DataFormatOptions
    def __init__(self, project_id: _Optional[str] = ..., job_id: _Optional[str] = ..., start_index: _Optional[_Union[_wrappers_pb2.UInt64Value, _Mapping]] = ..., page_token: _Optional[str] = ..., max_results: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., timeout_ms: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., location: _Optional[str] = ..., format_options: _Optional[_Union[_data_format_options_pb2.DataFormatOptions, _Mapping]] = ...) -> None: ...

class GetQueryResultsResponse(_message.Message):
    __slots__ = ("kind", "etag", "schema", "job_reference", "total_rows", "page_token", "rows", "total_bytes_processed", "job_complete", "errors", "cache_hit", "num_dml_affected_rows")
    KIND_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    JOB_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_ROWS_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ROWS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_BYTES_PROCESSED_FIELD_NUMBER: _ClassVar[int]
    JOB_COMPLETE_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    CACHE_HIT_FIELD_NUMBER: _ClassVar[int]
    NUM_DML_AFFECTED_ROWS_FIELD_NUMBER: _ClassVar[int]
    kind: str
    etag: str
    schema: _table_schema_pb2.TableSchema
    job_reference: _job_reference_pb2.JobReference
    total_rows: _wrappers_pb2.UInt64Value
    page_token: str
    rows: _containers.RepeatedCompositeFieldContainer[_struct_pb2.Struct]
    total_bytes_processed: _wrappers_pb2.Int64Value
    job_complete: _wrappers_pb2.BoolValue
    errors: _containers.RepeatedCompositeFieldContainer[_error_pb2.ErrorProto]
    cache_hit: _wrappers_pb2.BoolValue
    num_dml_affected_rows: _wrappers_pb2.Int64Value
    def __init__(self, kind: _Optional[str] = ..., etag: _Optional[str] = ..., schema: _Optional[_Union[_table_schema_pb2.TableSchema, _Mapping]] = ..., job_reference: _Optional[_Union[_job_reference_pb2.JobReference, _Mapping]] = ..., total_rows: _Optional[_Union[_wrappers_pb2.UInt64Value, _Mapping]] = ..., page_token: _Optional[str] = ..., rows: _Optional[_Iterable[_Union[_struct_pb2.Struct, _Mapping]]] = ..., total_bytes_processed: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., job_complete: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., errors: _Optional[_Iterable[_Union[_error_pb2.ErrorProto, _Mapping]]] = ..., cache_hit: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., num_dml_affected_rows: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ...) -> None: ...

class PostQueryRequest(_message.Message):
    __slots__ = ("project_id", "query_request")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    QUERY_REQUEST_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    query_request: QueryRequest
    def __init__(self, project_id: _Optional[str] = ..., query_request: _Optional[_Union[QueryRequest, _Mapping]] = ...) -> None: ...

class QueryRequest(_message.Message):
    __slots__ = ("kind", "query", "max_results", "default_dataset", "timeout_ms", "dry_run", "use_query_cache", "use_legacy_sql", "parameter_mode", "query_parameters", "location", "format_options", "connection_properties", "labels", "maximum_bytes_billed", "request_id", "create_session", "job_creation_mode")
    class JobCreationMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        JOB_CREATION_MODE_UNSPECIFIED: _ClassVar[QueryRequest.JobCreationMode]
        JOB_CREATION_REQUIRED: _ClassVar[QueryRequest.JobCreationMode]
        JOB_CREATION_OPTIONAL: _ClassVar[QueryRequest.JobCreationMode]
    JOB_CREATION_MODE_UNSPECIFIED: QueryRequest.JobCreationMode
    JOB_CREATION_REQUIRED: QueryRequest.JobCreationMode
    JOB_CREATION_OPTIONAL: QueryRequest.JobCreationMode
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    KIND_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    MAX_RESULTS_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_DATASET_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_MS_FIELD_NUMBER: _ClassVar[int]
    DRY_RUN_FIELD_NUMBER: _ClassVar[int]
    USE_QUERY_CACHE_FIELD_NUMBER: _ClassVar[int]
    USE_LEGACY_SQL_FIELD_NUMBER: _ClassVar[int]
    PARAMETER_MODE_FIELD_NUMBER: _ClassVar[int]
    QUERY_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    FORMAT_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_BYTES_BILLED_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    CREATE_SESSION_FIELD_NUMBER: _ClassVar[int]
    JOB_CREATION_MODE_FIELD_NUMBER: _ClassVar[int]
    kind: str
    query: str
    max_results: _wrappers_pb2.UInt32Value
    default_dataset: _dataset_reference_pb2.DatasetReference
    timeout_ms: _wrappers_pb2.UInt32Value
    dry_run: bool
    use_query_cache: _wrappers_pb2.BoolValue
    use_legacy_sql: _wrappers_pb2.BoolValue
    parameter_mode: str
    query_parameters: _containers.RepeatedCompositeFieldContainer[_query_parameter_pb2.QueryParameter]
    location: str
    format_options: _data_format_options_pb2.DataFormatOptions
    connection_properties: _containers.RepeatedCompositeFieldContainer[_job_config_pb2.ConnectionProperty]
    labels: _containers.ScalarMap[str, str]
    maximum_bytes_billed: _wrappers_pb2.Int64Value
    request_id: str
    create_session: _wrappers_pb2.BoolValue
    job_creation_mode: QueryRequest.JobCreationMode
    def __init__(self, kind: _Optional[str] = ..., query: _Optional[str] = ..., max_results: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., default_dataset: _Optional[_Union[_dataset_reference_pb2.DatasetReference, _Mapping]] = ..., timeout_ms: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., dry_run: bool = ..., use_query_cache: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., use_legacy_sql: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., parameter_mode: _Optional[str] = ..., query_parameters: _Optional[_Iterable[_Union[_query_parameter_pb2.QueryParameter, _Mapping]]] = ..., location: _Optional[str] = ..., format_options: _Optional[_Union[_data_format_options_pb2.DataFormatOptions, _Mapping]] = ..., connection_properties: _Optional[_Iterable[_Union[_job_config_pb2.ConnectionProperty, _Mapping]]] = ..., labels: _Optional[_Mapping[str, str]] = ..., maximum_bytes_billed: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., request_id: _Optional[str] = ..., create_session: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., job_creation_mode: _Optional[_Union[QueryRequest.JobCreationMode, str]] = ...) -> None: ...

class QueryResponse(_message.Message):
    __slots__ = ("kind", "schema", "job_reference", "job_creation_reason", "query_id", "total_rows", "page_token", "rows", "total_bytes_processed", "job_complete", "errors", "cache_hit", "num_dml_affected_rows", "session_info", "dml_stats")
    KIND_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    JOB_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    JOB_CREATION_REASON_FIELD_NUMBER: _ClassVar[int]
    QUERY_ID_FIELD_NUMBER: _ClassVar[int]
    TOTAL_ROWS_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ROWS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_BYTES_PROCESSED_FIELD_NUMBER: _ClassVar[int]
    JOB_COMPLETE_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    CACHE_HIT_FIELD_NUMBER: _ClassVar[int]
    NUM_DML_AFFECTED_ROWS_FIELD_NUMBER: _ClassVar[int]
    SESSION_INFO_FIELD_NUMBER: _ClassVar[int]
    DML_STATS_FIELD_NUMBER: _ClassVar[int]
    kind: str
    schema: _table_schema_pb2.TableSchema
    job_reference: _job_reference_pb2.JobReference
    job_creation_reason: _job_creation_reason_pb2.JobCreationReason
    query_id: str
    total_rows: _wrappers_pb2.UInt64Value
    page_token: str
    rows: _containers.RepeatedCompositeFieldContainer[_struct_pb2.Struct]
    total_bytes_processed: _wrappers_pb2.Int64Value
    job_complete: _wrappers_pb2.BoolValue
    errors: _containers.RepeatedCompositeFieldContainer[_error_pb2.ErrorProto]
    cache_hit: _wrappers_pb2.BoolValue
    num_dml_affected_rows: _wrappers_pb2.Int64Value
    session_info: _session_info_pb2.SessionInfo
    dml_stats: _job_stats_pb2.DmlStats
    def __init__(self, kind: _Optional[str] = ..., schema: _Optional[_Union[_table_schema_pb2.TableSchema, _Mapping]] = ..., job_reference: _Optional[_Union[_job_reference_pb2.JobReference, _Mapping]] = ..., job_creation_reason: _Optional[_Union[_job_creation_reason_pb2.JobCreationReason, _Mapping]] = ..., query_id: _Optional[str] = ..., total_rows: _Optional[_Union[_wrappers_pb2.UInt64Value, _Mapping]] = ..., page_token: _Optional[str] = ..., rows: _Optional[_Iterable[_Union[_struct_pb2.Struct, _Mapping]]] = ..., total_bytes_processed: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., job_complete: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., errors: _Optional[_Iterable[_Union[_error_pb2.ErrorProto, _Mapping]]] = ..., cache_hit: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., num_dml_affected_rows: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., session_info: _Optional[_Union[_session_info_pb2.SessionInfo, _Mapping]] = ..., dml_stats: _Optional[_Union[_job_stats_pb2.DmlStats, _Mapping]] = ...) -> None: ...
