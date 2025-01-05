from google.iam.v1 import iam_policy_pb2 as _iam_policy_pb2
from google.iam.v1 import policy_pb2 as _policy_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class AuditData(_message.Message):
    __slots__ = ('table_insert_request', 'table_update_request', 'dataset_list_request', 'dataset_insert_request', 'dataset_update_request', 'job_insert_request', 'job_query_request', 'job_get_query_results_request', 'table_data_list_request', 'set_iam_policy_request', 'table_insert_response', 'table_update_response', 'dataset_insert_response', 'dataset_update_response', 'job_insert_response', 'job_query_response', 'job_get_query_results_response', 'job_query_done_response', 'policy_response', 'job_completed_event', 'table_data_read_events')
    TABLE_INSERT_REQUEST_FIELD_NUMBER: _ClassVar[int]
    TABLE_UPDATE_REQUEST_FIELD_NUMBER: _ClassVar[int]
    DATASET_LIST_REQUEST_FIELD_NUMBER: _ClassVar[int]
    DATASET_INSERT_REQUEST_FIELD_NUMBER: _ClassVar[int]
    DATASET_UPDATE_REQUEST_FIELD_NUMBER: _ClassVar[int]
    JOB_INSERT_REQUEST_FIELD_NUMBER: _ClassVar[int]
    JOB_QUERY_REQUEST_FIELD_NUMBER: _ClassVar[int]
    JOB_GET_QUERY_RESULTS_REQUEST_FIELD_NUMBER: _ClassVar[int]
    TABLE_DATA_LIST_REQUEST_FIELD_NUMBER: _ClassVar[int]
    SET_IAM_POLICY_REQUEST_FIELD_NUMBER: _ClassVar[int]
    TABLE_INSERT_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    TABLE_UPDATE_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    DATASET_INSERT_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    DATASET_UPDATE_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    JOB_INSERT_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    JOB_QUERY_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    JOB_GET_QUERY_RESULTS_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    JOB_QUERY_DONE_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    POLICY_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    JOB_COMPLETED_EVENT_FIELD_NUMBER: _ClassVar[int]
    TABLE_DATA_READ_EVENTS_FIELD_NUMBER: _ClassVar[int]
    table_insert_request: TableInsertRequest
    table_update_request: TableUpdateRequest
    dataset_list_request: DatasetListRequest
    dataset_insert_request: DatasetInsertRequest
    dataset_update_request: DatasetUpdateRequest
    job_insert_request: JobInsertRequest
    job_query_request: JobQueryRequest
    job_get_query_results_request: JobGetQueryResultsRequest
    table_data_list_request: TableDataListRequest
    set_iam_policy_request: _iam_policy_pb2.SetIamPolicyRequest
    table_insert_response: TableInsertResponse
    table_update_response: TableUpdateResponse
    dataset_insert_response: DatasetInsertResponse
    dataset_update_response: DatasetUpdateResponse
    job_insert_response: JobInsertResponse
    job_query_response: JobQueryResponse
    job_get_query_results_response: JobGetQueryResultsResponse
    job_query_done_response: JobQueryDoneResponse
    policy_response: _policy_pb2.Policy
    job_completed_event: JobCompletedEvent
    table_data_read_events: _containers.RepeatedCompositeFieldContainer[TableDataReadEvent]

    def __init__(self, table_insert_request: _Optional[_Union[TableInsertRequest, _Mapping]]=..., table_update_request: _Optional[_Union[TableUpdateRequest, _Mapping]]=..., dataset_list_request: _Optional[_Union[DatasetListRequest, _Mapping]]=..., dataset_insert_request: _Optional[_Union[DatasetInsertRequest, _Mapping]]=..., dataset_update_request: _Optional[_Union[DatasetUpdateRequest, _Mapping]]=..., job_insert_request: _Optional[_Union[JobInsertRequest, _Mapping]]=..., job_query_request: _Optional[_Union[JobQueryRequest, _Mapping]]=..., job_get_query_results_request: _Optional[_Union[JobGetQueryResultsRequest, _Mapping]]=..., table_data_list_request: _Optional[_Union[TableDataListRequest, _Mapping]]=..., set_iam_policy_request: _Optional[_Union[_iam_policy_pb2.SetIamPolicyRequest, _Mapping]]=..., table_insert_response: _Optional[_Union[TableInsertResponse, _Mapping]]=..., table_update_response: _Optional[_Union[TableUpdateResponse, _Mapping]]=..., dataset_insert_response: _Optional[_Union[DatasetInsertResponse, _Mapping]]=..., dataset_update_response: _Optional[_Union[DatasetUpdateResponse, _Mapping]]=..., job_insert_response: _Optional[_Union[JobInsertResponse, _Mapping]]=..., job_query_response: _Optional[_Union[JobQueryResponse, _Mapping]]=..., job_get_query_results_response: _Optional[_Union[JobGetQueryResultsResponse, _Mapping]]=..., job_query_done_response: _Optional[_Union[JobQueryDoneResponse, _Mapping]]=..., policy_response: _Optional[_Union[_policy_pb2.Policy, _Mapping]]=..., job_completed_event: _Optional[_Union[JobCompletedEvent, _Mapping]]=..., table_data_read_events: _Optional[_Iterable[_Union[TableDataReadEvent, _Mapping]]]=...) -> None:
        ...

class TableInsertRequest(_message.Message):
    __slots__ = ('resource',)
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    resource: Table

    def __init__(self, resource: _Optional[_Union[Table, _Mapping]]=...) -> None:
        ...

class TableUpdateRequest(_message.Message):
    __slots__ = ('resource',)
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    resource: Table

    def __init__(self, resource: _Optional[_Union[Table, _Mapping]]=...) -> None:
        ...

class TableInsertResponse(_message.Message):
    __slots__ = ('resource',)
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    resource: Table

    def __init__(self, resource: _Optional[_Union[Table, _Mapping]]=...) -> None:
        ...

class TableUpdateResponse(_message.Message):
    __slots__ = ('resource',)
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    resource: Table

    def __init__(self, resource: _Optional[_Union[Table, _Mapping]]=...) -> None:
        ...

class DatasetListRequest(_message.Message):
    __slots__ = ('list_all',)
    LIST_ALL_FIELD_NUMBER: _ClassVar[int]
    list_all: bool

    def __init__(self, list_all: bool=...) -> None:
        ...

class DatasetInsertRequest(_message.Message):
    __slots__ = ('resource',)
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    resource: Dataset

    def __init__(self, resource: _Optional[_Union[Dataset, _Mapping]]=...) -> None:
        ...

class DatasetInsertResponse(_message.Message):
    __slots__ = ('resource',)
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    resource: Dataset

    def __init__(self, resource: _Optional[_Union[Dataset, _Mapping]]=...) -> None:
        ...

class DatasetUpdateRequest(_message.Message):
    __slots__ = ('resource',)
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    resource: Dataset

    def __init__(self, resource: _Optional[_Union[Dataset, _Mapping]]=...) -> None:
        ...

class DatasetUpdateResponse(_message.Message):
    __slots__ = ('resource',)
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    resource: Dataset

    def __init__(self, resource: _Optional[_Union[Dataset, _Mapping]]=...) -> None:
        ...

class JobInsertRequest(_message.Message):
    __slots__ = ('resource',)
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    resource: Job

    def __init__(self, resource: _Optional[_Union[Job, _Mapping]]=...) -> None:
        ...

class JobInsertResponse(_message.Message):
    __slots__ = ('resource',)
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    resource: Job

    def __init__(self, resource: _Optional[_Union[Job, _Mapping]]=...) -> None:
        ...

class JobQueryRequest(_message.Message):
    __slots__ = ('query', 'max_results', 'default_dataset', 'project_id', 'dry_run')
    QUERY_FIELD_NUMBER: _ClassVar[int]
    MAX_RESULTS_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_DATASET_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    DRY_RUN_FIELD_NUMBER: _ClassVar[int]
    query: str
    max_results: int
    default_dataset: DatasetName
    project_id: str
    dry_run: bool

    def __init__(self, query: _Optional[str]=..., max_results: _Optional[int]=..., default_dataset: _Optional[_Union[DatasetName, _Mapping]]=..., project_id: _Optional[str]=..., dry_run: bool=...) -> None:
        ...

class JobQueryResponse(_message.Message):
    __slots__ = ('total_results', 'job')
    TOTAL_RESULTS_FIELD_NUMBER: _ClassVar[int]
    JOB_FIELD_NUMBER: _ClassVar[int]
    total_results: int
    job: Job

    def __init__(self, total_results: _Optional[int]=..., job: _Optional[_Union[Job, _Mapping]]=...) -> None:
        ...

class JobGetQueryResultsRequest(_message.Message):
    __slots__ = ('max_results', 'start_row')
    MAX_RESULTS_FIELD_NUMBER: _ClassVar[int]
    START_ROW_FIELD_NUMBER: _ClassVar[int]
    max_results: int
    start_row: int

    def __init__(self, max_results: _Optional[int]=..., start_row: _Optional[int]=...) -> None:
        ...

class JobGetQueryResultsResponse(_message.Message):
    __slots__ = ('total_results', 'job')
    TOTAL_RESULTS_FIELD_NUMBER: _ClassVar[int]
    JOB_FIELD_NUMBER: _ClassVar[int]
    total_results: int
    job: Job

    def __init__(self, total_results: _Optional[int]=..., job: _Optional[_Union[Job, _Mapping]]=...) -> None:
        ...

class JobQueryDoneResponse(_message.Message):
    __slots__ = ('job',)
    JOB_FIELD_NUMBER: _ClassVar[int]
    job: Job

    def __init__(self, job: _Optional[_Union[Job, _Mapping]]=...) -> None:
        ...

class JobCompletedEvent(_message.Message):
    __slots__ = ('event_name', 'job')
    EVENT_NAME_FIELD_NUMBER: _ClassVar[int]
    JOB_FIELD_NUMBER: _ClassVar[int]
    event_name: str
    job: Job

    def __init__(self, event_name: _Optional[str]=..., job: _Optional[_Union[Job, _Mapping]]=...) -> None:
        ...

class TableDataReadEvent(_message.Message):
    __slots__ = ('table_name', 'referenced_fields')
    TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    REFERENCED_FIELDS_FIELD_NUMBER: _ClassVar[int]
    table_name: TableName
    referenced_fields: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, table_name: _Optional[_Union[TableName, _Mapping]]=..., referenced_fields: _Optional[_Iterable[str]]=...) -> None:
        ...

class TableDataListRequest(_message.Message):
    __slots__ = ('start_row', 'max_results')
    START_ROW_FIELD_NUMBER: _ClassVar[int]
    MAX_RESULTS_FIELD_NUMBER: _ClassVar[int]
    start_row: int
    max_results: int

    def __init__(self, start_row: _Optional[int]=..., max_results: _Optional[int]=...) -> None:
        ...

class Table(_message.Message):
    __slots__ = ('table_name', 'info', 'schema_json', 'view', 'expire_time', 'create_time', 'truncate_time', 'update_time', 'encryption')
    TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_JSON_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    TRUNCATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_FIELD_NUMBER: _ClassVar[int]
    table_name: TableName
    info: TableInfo
    schema_json: str
    view: TableViewDefinition
    expire_time: _timestamp_pb2.Timestamp
    create_time: _timestamp_pb2.Timestamp
    truncate_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    encryption: EncryptionInfo

    def __init__(self, table_name: _Optional[_Union[TableName, _Mapping]]=..., info: _Optional[_Union[TableInfo, _Mapping]]=..., schema_json: _Optional[str]=..., view: _Optional[_Union[TableViewDefinition, _Mapping]]=..., expire_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., truncate_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., encryption: _Optional[_Union[EncryptionInfo, _Mapping]]=...) -> None:
        ...

class TableInfo(_message.Message):
    __slots__ = ('friendly_name', 'description', 'labels')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    FRIENDLY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    friendly_name: str
    description: str
    labels: _containers.ScalarMap[str, str]

    def __init__(self, friendly_name: _Optional[str]=..., description: _Optional[str]=..., labels: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class TableViewDefinition(_message.Message):
    __slots__ = ('query',)
    QUERY_FIELD_NUMBER: _ClassVar[int]
    query: str

    def __init__(self, query: _Optional[str]=...) -> None:
        ...

class Dataset(_message.Message):
    __slots__ = ('dataset_name', 'info', 'create_time', 'update_time', 'acl', 'default_table_expire_duration')
    DATASET_NAME_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    ACL_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_TABLE_EXPIRE_DURATION_FIELD_NUMBER: _ClassVar[int]
    dataset_name: DatasetName
    info: DatasetInfo
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    acl: BigQueryAcl
    default_table_expire_duration: _duration_pb2.Duration

    def __init__(self, dataset_name: _Optional[_Union[DatasetName, _Mapping]]=..., info: _Optional[_Union[DatasetInfo, _Mapping]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., acl: _Optional[_Union[BigQueryAcl, _Mapping]]=..., default_table_expire_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=...) -> None:
        ...

class DatasetInfo(_message.Message):
    __slots__ = ('friendly_name', 'description', 'labels')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    FRIENDLY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    friendly_name: str
    description: str
    labels: _containers.ScalarMap[str, str]

    def __init__(self, friendly_name: _Optional[str]=..., description: _Optional[str]=..., labels: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class BigQueryAcl(_message.Message):
    __slots__ = ('entries',)

    class Entry(_message.Message):
        __slots__ = ('role', 'group_email', 'user_email', 'domain', 'special_group', 'view_name')
        ROLE_FIELD_NUMBER: _ClassVar[int]
        GROUP_EMAIL_FIELD_NUMBER: _ClassVar[int]
        USER_EMAIL_FIELD_NUMBER: _ClassVar[int]
        DOMAIN_FIELD_NUMBER: _ClassVar[int]
        SPECIAL_GROUP_FIELD_NUMBER: _ClassVar[int]
        VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
        role: str
        group_email: str
        user_email: str
        domain: str
        special_group: str
        view_name: TableName

        def __init__(self, role: _Optional[str]=..., group_email: _Optional[str]=..., user_email: _Optional[str]=..., domain: _Optional[str]=..., special_group: _Optional[str]=..., view_name: _Optional[_Union[TableName, _Mapping]]=...) -> None:
            ...
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.RepeatedCompositeFieldContainer[BigQueryAcl.Entry]

    def __init__(self, entries: _Optional[_Iterable[_Union[BigQueryAcl.Entry, _Mapping]]]=...) -> None:
        ...

class Job(_message.Message):
    __slots__ = ('job_name', 'job_configuration', 'job_status', 'job_statistics')
    JOB_NAME_FIELD_NUMBER: _ClassVar[int]
    JOB_CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    JOB_STATUS_FIELD_NUMBER: _ClassVar[int]
    JOB_STATISTICS_FIELD_NUMBER: _ClassVar[int]
    job_name: JobName
    job_configuration: JobConfiguration
    job_status: JobStatus
    job_statistics: JobStatistics

    def __init__(self, job_name: _Optional[_Union[JobName, _Mapping]]=..., job_configuration: _Optional[_Union[JobConfiguration, _Mapping]]=..., job_status: _Optional[_Union[JobStatus, _Mapping]]=..., job_statistics: _Optional[_Union[JobStatistics, _Mapping]]=...) -> None:
        ...

class JobConfiguration(_message.Message):
    __slots__ = ('query', 'load', 'extract', 'table_copy', 'dry_run', 'labels')

    class Query(_message.Message):
        __slots__ = ('query', 'destination_table', 'create_disposition', 'write_disposition', 'default_dataset', 'table_definitions', 'query_priority', 'destination_table_encryption', 'statement_type')
        QUERY_FIELD_NUMBER: _ClassVar[int]
        DESTINATION_TABLE_FIELD_NUMBER: _ClassVar[int]
        CREATE_DISPOSITION_FIELD_NUMBER: _ClassVar[int]
        WRITE_DISPOSITION_FIELD_NUMBER: _ClassVar[int]
        DEFAULT_DATASET_FIELD_NUMBER: _ClassVar[int]
        TABLE_DEFINITIONS_FIELD_NUMBER: _ClassVar[int]
        QUERY_PRIORITY_FIELD_NUMBER: _ClassVar[int]
        DESTINATION_TABLE_ENCRYPTION_FIELD_NUMBER: _ClassVar[int]
        STATEMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
        query: str
        destination_table: TableName
        create_disposition: str
        write_disposition: str
        default_dataset: DatasetName
        table_definitions: _containers.RepeatedCompositeFieldContainer[TableDefinition]
        query_priority: str
        destination_table_encryption: EncryptionInfo
        statement_type: str

        def __init__(self, query: _Optional[str]=..., destination_table: _Optional[_Union[TableName, _Mapping]]=..., create_disposition: _Optional[str]=..., write_disposition: _Optional[str]=..., default_dataset: _Optional[_Union[DatasetName, _Mapping]]=..., table_definitions: _Optional[_Iterable[_Union[TableDefinition, _Mapping]]]=..., query_priority: _Optional[str]=..., destination_table_encryption: _Optional[_Union[EncryptionInfo, _Mapping]]=..., statement_type: _Optional[str]=...) -> None:
            ...

    class Load(_message.Message):
        __slots__ = ('source_uris', 'schema_json', 'destination_table', 'create_disposition', 'write_disposition', 'destination_table_encryption')
        SOURCE_URIS_FIELD_NUMBER: _ClassVar[int]
        SCHEMA_JSON_FIELD_NUMBER: _ClassVar[int]
        DESTINATION_TABLE_FIELD_NUMBER: _ClassVar[int]
        CREATE_DISPOSITION_FIELD_NUMBER: _ClassVar[int]
        WRITE_DISPOSITION_FIELD_NUMBER: _ClassVar[int]
        DESTINATION_TABLE_ENCRYPTION_FIELD_NUMBER: _ClassVar[int]
        source_uris: _containers.RepeatedScalarFieldContainer[str]
        schema_json: str
        destination_table: TableName
        create_disposition: str
        write_disposition: str
        destination_table_encryption: EncryptionInfo

        def __init__(self, source_uris: _Optional[_Iterable[str]]=..., schema_json: _Optional[str]=..., destination_table: _Optional[_Union[TableName, _Mapping]]=..., create_disposition: _Optional[str]=..., write_disposition: _Optional[str]=..., destination_table_encryption: _Optional[_Union[EncryptionInfo, _Mapping]]=...) -> None:
            ...

    class Extract(_message.Message):
        __slots__ = ('destination_uris', 'source_table')
        DESTINATION_URIS_FIELD_NUMBER: _ClassVar[int]
        SOURCE_TABLE_FIELD_NUMBER: _ClassVar[int]
        destination_uris: _containers.RepeatedScalarFieldContainer[str]
        source_table: TableName

        def __init__(self, destination_uris: _Optional[_Iterable[str]]=..., source_table: _Optional[_Union[TableName, _Mapping]]=...) -> None:
            ...

    class TableCopy(_message.Message):
        __slots__ = ('source_tables', 'destination_table', 'create_disposition', 'write_disposition', 'destination_table_encryption')
        SOURCE_TABLES_FIELD_NUMBER: _ClassVar[int]
        DESTINATION_TABLE_FIELD_NUMBER: _ClassVar[int]
        CREATE_DISPOSITION_FIELD_NUMBER: _ClassVar[int]
        WRITE_DISPOSITION_FIELD_NUMBER: _ClassVar[int]
        DESTINATION_TABLE_ENCRYPTION_FIELD_NUMBER: _ClassVar[int]
        source_tables: _containers.RepeatedCompositeFieldContainer[TableName]
        destination_table: TableName
        create_disposition: str
        write_disposition: str
        destination_table_encryption: EncryptionInfo

        def __init__(self, source_tables: _Optional[_Iterable[_Union[TableName, _Mapping]]]=..., destination_table: _Optional[_Union[TableName, _Mapping]]=..., create_disposition: _Optional[str]=..., write_disposition: _Optional[str]=..., destination_table_encryption: _Optional[_Union[EncryptionInfo, _Mapping]]=...) -> None:
            ...

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    QUERY_FIELD_NUMBER: _ClassVar[int]
    LOAD_FIELD_NUMBER: _ClassVar[int]
    EXTRACT_FIELD_NUMBER: _ClassVar[int]
    TABLE_COPY_FIELD_NUMBER: _ClassVar[int]
    DRY_RUN_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    query: JobConfiguration.Query
    load: JobConfiguration.Load
    extract: JobConfiguration.Extract
    table_copy: JobConfiguration.TableCopy
    dry_run: bool
    labels: _containers.ScalarMap[str, str]

    def __init__(self, query: _Optional[_Union[JobConfiguration.Query, _Mapping]]=..., load: _Optional[_Union[JobConfiguration.Load, _Mapping]]=..., extract: _Optional[_Union[JobConfiguration.Extract, _Mapping]]=..., table_copy: _Optional[_Union[JobConfiguration.TableCopy, _Mapping]]=..., dry_run: bool=..., labels: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class TableDefinition(_message.Message):
    __slots__ = ('name', 'source_uris')
    NAME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_URIS_FIELD_NUMBER: _ClassVar[int]
    name: str
    source_uris: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, name: _Optional[str]=..., source_uris: _Optional[_Iterable[str]]=...) -> None:
        ...

class JobStatus(_message.Message):
    __slots__ = ('state', 'error', 'additional_errors')
    STATE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_ERRORS_FIELD_NUMBER: _ClassVar[int]
    state: str
    error: _status_pb2.Status
    additional_errors: _containers.RepeatedCompositeFieldContainer[_status_pb2.Status]

    def __init__(self, state: _Optional[str]=..., error: _Optional[_Union[_status_pb2.Status, _Mapping]]=..., additional_errors: _Optional[_Iterable[_Union[_status_pb2.Status, _Mapping]]]=...) -> None:
        ...

class JobStatistics(_message.Message):
    __slots__ = ('create_time', 'start_time', 'end_time', 'total_processed_bytes', 'total_billed_bytes', 'billing_tier', 'total_slot_ms', 'reservation_usage', 'reservation', 'referenced_tables', 'total_tables_processed', 'referenced_views', 'total_views_processed', 'query_output_row_count', 'total_load_output_bytes')

    class ReservationResourceUsage(_message.Message):
        __slots__ = ('name', 'slot_ms')
        NAME_FIELD_NUMBER: _ClassVar[int]
        SLOT_MS_FIELD_NUMBER: _ClassVar[int]
        name: str
        slot_ms: int

        def __init__(self, name: _Optional[str]=..., slot_ms: _Optional[int]=...) -> None:
            ...
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    TOTAL_PROCESSED_BYTES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_BILLED_BYTES_FIELD_NUMBER: _ClassVar[int]
    BILLING_TIER_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SLOT_MS_FIELD_NUMBER: _ClassVar[int]
    RESERVATION_USAGE_FIELD_NUMBER: _ClassVar[int]
    RESERVATION_FIELD_NUMBER: _ClassVar[int]
    REFERENCED_TABLES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_TABLES_PROCESSED_FIELD_NUMBER: _ClassVar[int]
    REFERENCED_VIEWS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_VIEWS_PROCESSED_FIELD_NUMBER: _ClassVar[int]
    QUERY_OUTPUT_ROW_COUNT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_LOAD_OUTPUT_BYTES_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    total_processed_bytes: int
    total_billed_bytes: int
    billing_tier: int
    total_slot_ms: int
    reservation_usage: _containers.RepeatedCompositeFieldContainer[JobStatistics.ReservationResourceUsage]
    reservation: str
    referenced_tables: _containers.RepeatedCompositeFieldContainer[TableName]
    total_tables_processed: int
    referenced_views: _containers.RepeatedCompositeFieldContainer[TableName]
    total_views_processed: int
    query_output_row_count: int
    total_load_output_bytes: int

    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., total_processed_bytes: _Optional[int]=..., total_billed_bytes: _Optional[int]=..., billing_tier: _Optional[int]=..., total_slot_ms: _Optional[int]=..., reservation_usage: _Optional[_Iterable[_Union[JobStatistics.ReservationResourceUsage, _Mapping]]]=..., reservation: _Optional[str]=..., referenced_tables: _Optional[_Iterable[_Union[TableName, _Mapping]]]=..., total_tables_processed: _Optional[int]=..., referenced_views: _Optional[_Iterable[_Union[TableName, _Mapping]]]=..., total_views_processed: _Optional[int]=..., query_output_row_count: _Optional[int]=..., total_load_output_bytes: _Optional[int]=...) -> None:
        ...

class DatasetName(_message.Message):
    __slots__ = ('project_id', 'dataset_id')
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    DATASET_ID_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    dataset_id: str

    def __init__(self, project_id: _Optional[str]=..., dataset_id: _Optional[str]=...) -> None:
        ...

class TableName(_message.Message):
    __slots__ = ('project_id', 'dataset_id', 'table_id')
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    DATASET_ID_FIELD_NUMBER: _ClassVar[int]
    TABLE_ID_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    dataset_id: str
    table_id: str

    def __init__(self, project_id: _Optional[str]=..., dataset_id: _Optional[str]=..., table_id: _Optional[str]=...) -> None:
        ...

class JobName(_message.Message):
    __slots__ = ('project_id', 'job_id', 'location')
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    job_id: str
    location: str

    def __init__(self, project_id: _Optional[str]=..., job_id: _Optional[str]=..., location: _Optional[str]=...) -> None:
        ...

class EncryptionInfo(_message.Message):
    __slots__ = ('kms_key_name',)
    KMS_KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    kms_key_name: str

    def __init__(self, kms_key_name: _Optional[str]=...) -> None:
        ...