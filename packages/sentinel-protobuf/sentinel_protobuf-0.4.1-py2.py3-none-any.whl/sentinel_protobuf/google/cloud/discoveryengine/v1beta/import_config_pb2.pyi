from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.discoveryengine.v1beta import completion_pb2 as _completion_pb2
from google.cloud.discoveryengine.v1beta import document_pb2 as _document_pb2
from google.cloud.discoveryengine.v1beta import sample_query_pb2 as _sample_query_pb2
from google.cloud.discoveryengine.v1beta import user_event_pb2 as _user_event_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.rpc import status_pb2 as _status_pb2
from google.type import date_pb2 as _date_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GcsSource(_message.Message):
    __slots__ = ("input_uris", "data_schema")
    INPUT_URIS_FIELD_NUMBER: _ClassVar[int]
    DATA_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    input_uris: _containers.RepeatedScalarFieldContainer[str]
    data_schema: str
    def __init__(self, input_uris: _Optional[_Iterable[str]] = ..., data_schema: _Optional[str] = ...) -> None: ...

class BigQuerySource(_message.Message):
    __slots__ = ("partition_date", "project_id", "dataset_id", "table_id", "gcs_staging_dir", "data_schema")
    PARTITION_DATE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    DATASET_ID_FIELD_NUMBER: _ClassVar[int]
    TABLE_ID_FIELD_NUMBER: _ClassVar[int]
    GCS_STAGING_DIR_FIELD_NUMBER: _ClassVar[int]
    DATA_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    partition_date: _date_pb2.Date
    project_id: str
    dataset_id: str
    table_id: str
    gcs_staging_dir: str
    data_schema: str
    def __init__(self, partition_date: _Optional[_Union[_date_pb2.Date, _Mapping]] = ..., project_id: _Optional[str] = ..., dataset_id: _Optional[str] = ..., table_id: _Optional[str] = ..., gcs_staging_dir: _Optional[str] = ..., data_schema: _Optional[str] = ...) -> None: ...

class SpannerSource(_message.Message):
    __slots__ = ("project_id", "instance_id", "database_id", "table_id", "enable_data_boost")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    DATABASE_ID_FIELD_NUMBER: _ClassVar[int]
    TABLE_ID_FIELD_NUMBER: _ClassVar[int]
    ENABLE_DATA_BOOST_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    instance_id: str
    database_id: str
    table_id: str
    enable_data_boost: bool
    def __init__(self, project_id: _Optional[str] = ..., instance_id: _Optional[str] = ..., database_id: _Optional[str] = ..., table_id: _Optional[str] = ..., enable_data_boost: bool = ...) -> None: ...

class BigtableOptions(_message.Message):
    __slots__ = ("key_field_name", "families")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[BigtableOptions.Type]
        STRING: _ClassVar[BigtableOptions.Type]
        NUMBER: _ClassVar[BigtableOptions.Type]
        INTEGER: _ClassVar[BigtableOptions.Type]
        VAR_INTEGER: _ClassVar[BigtableOptions.Type]
        BIG_NUMERIC: _ClassVar[BigtableOptions.Type]
        BOOLEAN: _ClassVar[BigtableOptions.Type]
        JSON: _ClassVar[BigtableOptions.Type]
    TYPE_UNSPECIFIED: BigtableOptions.Type
    STRING: BigtableOptions.Type
    NUMBER: BigtableOptions.Type
    INTEGER: BigtableOptions.Type
    VAR_INTEGER: BigtableOptions.Type
    BIG_NUMERIC: BigtableOptions.Type
    BOOLEAN: BigtableOptions.Type
    JSON: BigtableOptions.Type
    class Encoding(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ENCODING_UNSPECIFIED: _ClassVar[BigtableOptions.Encoding]
        TEXT: _ClassVar[BigtableOptions.Encoding]
        BINARY: _ClassVar[BigtableOptions.Encoding]
    ENCODING_UNSPECIFIED: BigtableOptions.Encoding
    TEXT: BigtableOptions.Encoding
    BINARY: BigtableOptions.Encoding
    class BigtableColumnFamily(_message.Message):
        __slots__ = ("field_name", "encoding", "type", "columns")
        FIELD_NAME_FIELD_NUMBER: _ClassVar[int]
        ENCODING_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        COLUMNS_FIELD_NUMBER: _ClassVar[int]
        field_name: str
        encoding: BigtableOptions.Encoding
        type: BigtableOptions.Type
        columns: _containers.RepeatedCompositeFieldContainer[BigtableOptions.BigtableColumn]
        def __init__(self, field_name: _Optional[str] = ..., encoding: _Optional[_Union[BigtableOptions.Encoding, str]] = ..., type: _Optional[_Union[BigtableOptions.Type, str]] = ..., columns: _Optional[_Iterable[_Union[BigtableOptions.BigtableColumn, _Mapping]]] = ...) -> None: ...
    class BigtableColumn(_message.Message):
        __slots__ = ("qualifier", "field_name", "encoding", "type")
        QUALIFIER_FIELD_NUMBER: _ClassVar[int]
        FIELD_NAME_FIELD_NUMBER: _ClassVar[int]
        ENCODING_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        qualifier: bytes
        field_name: str
        encoding: BigtableOptions.Encoding
        type: BigtableOptions.Type
        def __init__(self, qualifier: _Optional[bytes] = ..., field_name: _Optional[str] = ..., encoding: _Optional[_Union[BigtableOptions.Encoding, str]] = ..., type: _Optional[_Union[BigtableOptions.Type, str]] = ...) -> None: ...
    class FamiliesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: BigtableOptions.BigtableColumnFamily
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[BigtableOptions.BigtableColumnFamily, _Mapping]] = ...) -> None: ...
    KEY_FIELD_NAME_FIELD_NUMBER: _ClassVar[int]
    FAMILIES_FIELD_NUMBER: _ClassVar[int]
    key_field_name: str
    families: _containers.MessageMap[str, BigtableOptions.BigtableColumnFamily]
    def __init__(self, key_field_name: _Optional[str] = ..., families: _Optional[_Mapping[str, BigtableOptions.BigtableColumnFamily]] = ...) -> None: ...

class BigtableSource(_message.Message):
    __slots__ = ("project_id", "instance_id", "table_id", "bigtable_options")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    TABLE_ID_FIELD_NUMBER: _ClassVar[int]
    BIGTABLE_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    instance_id: str
    table_id: str
    bigtable_options: BigtableOptions
    def __init__(self, project_id: _Optional[str] = ..., instance_id: _Optional[str] = ..., table_id: _Optional[str] = ..., bigtable_options: _Optional[_Union[BigtableOptions, _Mapping]] = ...) -> None: ...

class FhirStoreSource(_message.Message):
    __slots__ = ("fhir_store", "gcs_staging_dir", "resource_types")
    FHIR_STORE_FIELD_NUMBER: _ClassVar[int]
    GCS_STAGING_DIR_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_TYPES_FIELD_NUMBER: _ClassVar[int]
    fhir_store: str
    gcs_staging_dir: str
    resource_types: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, fhir_store: _Optional[str] = ..., gcs_staging_dir: _Optional[str] = ..., resource_types: _Optional[_Iterable[str]] = ...) -> None: ...

class CloudSqlSource(_message.Message):
    __slots__ = ("project_id", "instance_id", "database_id", "table_id", "gcs_staging_dir", "offload")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    DATABASE_ID_FIELD_NUMBER: _ClassVar[int]
    TABLE_ID_FIELD_NUMBER: _ClassVar[int]
    GCS_STAGING_DIR_FIELD_NUMBER: _ClassVar[int]
    OFFLOAD_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    instance_id: str
    database_id: str
    table_id: str
    gcs_staging_dir: str
    offload: bool
    def __init__(self, project_id: _Optional[str] = ..., instance_id: _Optional[str] = ..., database_id: _Optional[str] = ..., table_id: _Optional[str] = ..., gcs_staging_dir: _Optional[str] = ..., offload: bool = ...) -> None: ...

class AlloyDbSource(_message.Message):
    __slots__ = ("project_id", "location_id", "cluster_id", "database_id", "table_id", "gcs_staging_dir")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    DATABASE_ID_FIELD_NUMBER: _ClassVar[int]
    TABLE_ID_FIELD_NUMBER: _ClassVar[int]
    GCS_STAGING_DIR_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    location_id: str
    cluster_id: str
    database_id: str
    table_id: str
    gcs_staging_dir: str
    def __init__(self, project_id: _Optional[str] = ..., location_id: _Optional[str] = ..., cluster_id: _Optional[str] = ..., database_id: _Optional[str] = ..., table_id: _Optional[str] = ..., gcs_staging_dir: _Optional[str] = ...) -> None: ...

class FirestoreSource(_message.Message):
    __slots__ = ("project_id", "database_id", "collection_id", "gcs_staging_dir")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    DATABASE_ID_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    GCS_STAGING_DIR_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    database_id: str
    collection_id: str
    gcs_staging_dir: str
    def __init__(self, project_id: _Optional[str] = ..., database_id: _Optional[str] = ..., collection_id: _Optional[str] = ..., gcs_staging_dir: _Optional[str] = ...) -> None: ...

class ImportErrorConfig(_message.Message):
    __slots__ = ("gcs_prefix",)
    GCS_PREFIX_FIELD_NUMBER: _ClassVar[int]
    gcs_prefix: str
    def __init__(self, gcs_prefix: _Optional[str] = ...) -> None: ...

class ImportUserEventsRequest(_message.Message):
    __slots__ = ("inline_source", "gcs_source", "bigquery_source", "parent", "error_config")
    class InlineSource(_message.Message):
        __slots__ = ("user_events",)
        USER_EVENTS_FIELD_NUMBER: _ClassVar[int]
        user_events: _containers.RepeatedCompositeFieldContainer[_user_event_pb2.UserEvent]
        def __init__(self, user_events: _Optional[_Iterable[_Union[_user_event_pb2.UserEvent, _Mapping]]] = ...) -> None: ...
    INLINE_SOURCE_FIELD_NUMBER: _ClassVar[int]
    GCS_SOURCE_FIELD_NUMBER: _ClassVar[int]
    BIGQUERY_SOURCE_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ERROR_CONFIG_FIELD_NUMBER: _ClassVar[int]
    inline_source: ImportUserEventsRequest.InlineSource
    gcs_source: GcsSource
    bigquery_source: BigQuerySource
    parent: str
    error_config: ImportErrorConfig
    def __init__(self, inline_source: _Optional[_Union[ImportUserEventsRequest.InlineSource, _Mapping]] = ..., gcs_source: _Optional[_Union[GcsSource, _Mapping]] = ..., bigquery_source: _Optional[_Union[BigQuerySource, _Mapping]] = ..., parent: _Optional[str] = ..., error_config: _Optional[_Union[ImportErrorConfig, _Mapping]] = ...) -> None: ...

class ImportUserEventsResponse(_message.Message):
    __slots__ = ("error_samples", "error_config", "joined_events_count", "unjoined_events_count")
    ERROR_SAMPLES_FIELD_NUMBER: _ClassVar[int]
    ERROR_CONFIG_FIELD_NUMBER: _ClassVar[int]
    JOINED_EVENTS_COUNT_FIELD_NUMBER: _ClassVar[int]
    UNJOINED_EVENTS_COUNT_FIELD_NUMBER: _ClassVar[int]
    error_samples: _containers.RepeatedCompositeFieldContainer[_status_pb2.Status]
    error_config: ImportErrorConfig
    joined_events_count: int
    unjoined_events_count: int
    def __init__(self, error_samples: _Optional[_Iterable[_Union[_status_pb2.Status, _Mapping]]] = ..., error_config: _Optional[_Union[ImportErrorConfig, _Mapping]] = ..., joined_events_count: _Optional[int] = ..., unjoined_events_count: _Optional[int] = ...) -> None: ...

class ImportUserEventsMetadata(_message.Message):
    __slots__ = ("create_time", "update_time", "success_count", "failure_count")
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_COUNT_FIELD_NUMBER: _ClassVar[int]
    FAILURE_COUNT_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    success_count: int
    failure_count: int
    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., success_count: _Optional[int] = ..., failure_count: _Optional[int] = ...) -> None: ...

class ImportDocumentsMetadata(_message.Message):
    __slots__ = ("create_time", "update_time", "success_count", "failure_count", "total_count")
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_COUNT_FIELD_NUMBER: _ClassVar[int]
    FAILURE_COUNT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    success_count: int
    failure_count: int
    total_count: int
    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., success_count: _Optional[int] = ..., failure_count: _Optional[int] = ..., total_count: _Optional[int] = ...) -> None: ...

class ImportDocumentsRequest(_message.Message):
    __slots__ = ("inline_source", "gcs_source", "bigquery_source", "fhir_store_source", "spanner_source", "cloud_sql_source", "firestore_source", "alloy_db_source", "bigtable_source", "parent", "error_config", "reconciliation_mode", "update_mask", "auto_generate_ids", "id_field")
    class ReconciliationMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RECONCILIATION_MODE_UNSPECIFIED: _ClassVar[ImportDocumentsRequest.ReconciliationMode]
        INCREMENTAL: _ClassVar[ImportDocumentsRequest.ReconciliationMode]
        FULL: _ClassVar[ImportDocumentsRequest.ReconciliationMode]
    RECONCILIATION_MODE_UNSPECIFIED: ImportDocumentsRequest.ReconciliationMode
    INCREMENTAL: ImportDocumentsRequest.ReconciliationMode
    FULL: ImportDocumentsRequest.ReconciliationMode
    class InlineSource(_message.Message):
        __slots__ = ("documents",)
        DOCUMENTS_FIELD_NUMBER: _ClassVar[int]
        documents: _containers.RepeatedCompositeFieldContainer[_document_pb2.Document]
        def __init__(self, documents: _Optional[_Iterable[_Union[_document_pb2.Document, _Mapping]]] = ...) -> None: ...
    INLINE_SOURCE_FIELD_NUMBER: _ClassVar[int]
    GCS_SOURCE_FIELD_NUMBER: _ClassVar[int]
    BIGQUERY_SOURCE_FIELD_NUMBER: _ClassVar[int]
    FHIR_STORE_SOURCE_FIELD_NUMBER: _ClassVar[int]
    SPANNER_SOURCE_FIELD_NUMBER: _ClassVar[int]
    CLOUD_SQL_SOURCE_FIELD_NUMBER: _ClassVar[int]
    FIRESTORE_SOURCE_FIELD_NUMBER: _ClassVar[int]
    ALLOY_DB_SOURCE_FIELD_NUMBER: _ClassVar[int]
    BIGTABLE_SOURCE_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ERROR_CONFIG_FIELD_NUMBER: _ClassVar[int]
    RECONCILIATION_MODE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    AUTO_GENERATE_IDS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_FIELD_NUMBER: _ClassVar[int]
    inline_source: ImportDocumentsRequest.InlineSource
    gcs_source: GcsSource
    bigquery_source: BigQuerySource
    fhir_store_source: FhirStoreSource
    spanner_source: SpannerSource
    cloud_sql_source: CloudSqlSource
    firestore_source: FirestoreSource
    alloy_db_source: AlloyDbSource
    bigtable_source: BigtableSource
    parent: str
    error_config: ImportErrorConfig
    reconciliation_mode: ImportDocumentsRequest.ReconciliationMode
    update_mask: _field_mask_pb2.FieldMask
    auto_generate_ids: bool
    id_field: str
    def __init__(self, inline_source: _Optional[_Union[ImportDocumentsRequest.InlineSource, _Mapping]] = ..., gcs_source: _Optional[_Union[GcsSource, _Mapping]] = ..., bigquery_source: _Optional[_Union[BigQuerySource, _Mapping]] = ..., fhir_store_source: _Optional[_Union[FhirStoreSource, _Mapping]] = ..., spanner_source: _Optional[_Union[SpannerSource, _Mapping]] = ..., cloud_sql_source: _Optional[_Union[CloudSqlSource, _Mapping]] = ..., firestore_source: _Optional[_Union[FirestoreSource, _Mapping]] = ..., alloy_db_source: _Optional[_Union[AlloyDbSource, _Mapping]] = ..., bigtable_source: _Optional[_Union[BigtableSource, _Mapping]] = ..., parent: _Optional[str] = ..., error_config: _Optional[_Union[ImportErrorConfig, _Mapping]] = ..., reconciliation_mode: _Optional[_Union[ImportDocumentsRequest.ReconciliationMode, str]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., auto_generate_ids: bool = ..., id_field: _Optional[str] = ...) -> None: ...

class ImportDocumentsResponse(_message.Message):
    __slots__ = ("error_samples", "error_config")
    ERROR_SAMPLES_FIELD_NUMBER: _ClassVar[int]
    ERROR_CONFIG_FIELD_NUMBER: _ClassVar[int]
    error_samples: _containers.RepeatedCompositeFieldContainer[_status_pb2.Status]
    error_config: ImportErrorConfig
    def __init__(self, error_samples: _Optional[_Iterable[_Union[_status_pb2.Status, _Mapping]]] = ..., error_config: _Optional[_Union[ImportErrorConfig, _Mapping]] = ...) -> None: ...

class ImportSuggestionDenyListEntriesRequest(_message.Message):
    __slots__ = ("inline_source", "gcs_source", "parent")
    class InlineSource(_message.Message):
        __slots__ = ("entries",)
        ENTRIES_FIELD_NUMBER: _ClassVar[int]
        entries: _containers.RepeatedCompositeFieldContainer[_completion_pb2.SuggestionDenyListEntry]
        def __init__(self, entries: _Optional[_Iterable[_Union[_completion_pb2.SuggestionDenyListEntry, _Mapping]]] = ...) -> None: ...
    INLINE_SOURCE_FIELD_NUMBER: _ClassVar[int]
    GCS_SOURCE_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    inline_source: ImportSuggestionDenyListEntriesRequest.InlineSource
    gcs_source: GcsSource
    parent: str
    def __init__(self, inline_source: _Optional[_Union[ImportSuggestionDenyListEntriesRequest.InlineSource, _Mapping]] = ..., gcs_source: _Optional[_Union[GcsSource, _Mapping]] = ..., parent: _Optional[str] = ...) -> None: ...

class ImportSuggestionDenyListEntriesResponse(_message.Message):
    __slots__ = ("error_samples", "imported_entries_count", "failed_entries_count")
    ERROR_SAMPLES_FIELD_NUMBER: _ClassVar[int]
    IMPORTED_ENTRIES_COUNT_FIELD_NUMBER: _ClassVar[int]
    FAILED_ENTRIES_COUNT_FIELD_NUMBER: _ClassVar[int]
    error_samples: _containers.RepeatedCompositeFieldContainer[_status_pb2.Status]
    imported_entries_count: int
    failed_entries_count: int
    def __init__(self, error_samples: _Optional[_Iterable[_Union[_status_pb2.Status, _Mapping]]] = ..., imported_entries_count: _Optional[int] = ..., failed_entries_count: _Optional[int] = ...) -> None: ...

class ImportSuggestionDenyListEntriesMetadata(_message.Message):
    __slots__ = ("create_time", "update_time")
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ImportCompletionSuggestionsRequest(_message.Message):
    __slots__ = ("inline_source", "gcs_source", "bigquery_source", "parent", "error_config")
    class InlineSource(_message.Message):
        __slots__ = ("suggestions",)
        SUGGESTIONS_FIELD_NUMBER: _ClassVar[int]
        suggestions: _containers.RepeatedCompositeFieldContainer[_completion_pb2.CompletionSuggestion]
        def __init__(self, suggestions: _Optional[_Iterable[_Union[_completion_pb2.CompletionSuggestion, _Mapping]]] = ...) -> None: ...
    INLINE_SOURCE_FIELD_NUMBER: _ClassVar[int]
    GCS_SOURCE_FIELD_NUMBER: _ClassVar[int]
    BIGQUERY_SOURCE_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ERROR_CONFIG_FIELD_NUMBER: _ClassVar[int]
    inline_source: ImportCompletionSuggestionsRequest.InlineSource
    gcs_source: GcsSource
    bigquery_source: BigQuerySource
    parent: str
    error_config: ImportErrorConfig
    def __init__(self, inline_source: _Optional[_Union[ImportCompletionSuggestionsRequest.InlineSource, _Mapping]] = ..., gcs_source: _Optional[_Union[GcsSource, _Mapping]] = ..., bigquery_source: _Optional[_Union[BigQuerySource, _Mapping]] = ..., parent: _Optional[str] = ..., error_config: _Optional[_Union[ImportErrorConfig, _Mapping]] = ...) -> None: ...

class ImportCompletionSuggestionsResponse(_message.Message):
    __slots__ = ("error_samples", "error_config")
    ERROR_SAMPLES_FIELD_NUMBER: _ClassVar[int]
    ERROR_CONFIG_FIELD_NUMBER: _ClassVar[int]
    error_samples: _containers.RepeatedCompositeFieldContainer[_status_pb2.Status]
    error_config: ImportErrorConfig
    def __init__(self, error_samples: _Optional[_Iterable[_Union[_status_pb2.Status, _Mapping]]] = ..., error_config: _Optional[_Union[ImportErrorConfig, _Mapping]] = ...) -> None: ...

class ImportCompletionSuggestionsMetadata(_message.Message):
    __slots__ = ("create_time", "update_time", "success_count", "failure_count")
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_COUNT_FIELD_NUMBER: _ClassVar[int]
    FAILURE_COUNT_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    success_count: int
    failure_count: int
    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., success_count: _Optional[int] = ..., failure_count: _Optional[int] = ...) -> None: ...

class ImportSampleQueriesRequest(_message.Message):
    __slots__ = ("inline_source", "gcs_source", "bigquery_source", "parent", "error_config")
    class InlineSource(_message.Message):
        __slots__ = ("sample_queries",)
        SAMPLE_QUERIES_FIELD_NUMBER: _ClassVar[int]
        sample_queries: _containers.RepeatedCompositeFieldContainer[_sample_query_pb2.SampleQuery]
        def __init__(self, sample_queries: _Optional[_Iterable[_Union[_sample_query_pb2.SampleQuery, _Mapping]]] = ...) -> None: ...
    INLINE_SOURCE_FIELD_NUMBER: _ClassVar[int]
    GCS_SOURCE_FIELD_NUMBER: _ClassVar[int]
    BIGQUERY_SOURCE_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ERROR_CONFIG_FIELD_NUMBER: _ClassVar[int]
    inline_source: ImportSampleQueriesRequest.InlineSource
    gcs_source: GcsSource
    bigquery_source: BigQuerySource
    parent: str
    error_config: ImportErrorConfig
    def __init__(self, inline_source: _Optional[_Union[ImportSampleQueriesRequest.InlineSource, _Mapping]] = ..., gcs_source: _Optional[_Union[GcsSource, _Mapping]] = ..., bigquery_source: _Optional[_Union[BigQuerySource, _Mapping]] = ..., parent: _Optional[str] = ..., error_config: _Optional[_Union[ImportErrorConfig, _Mapping]] = ...) -> None: ...

class ImportSampleQueriesResponse(_message.Message):
    __slots__ = ("error_samples", "error_config")
    ERROR_SAMPLES_FIELD_NUMBER: _ClassVar[int]
    ERROR_CONFIG_FIELD_NUMBER: _ClassVar[int]
    error_samples: _containers.RepeatedCompositeFieldContainer[_status_pb2.Status]
    error_config: ImportErrorConfig
    def __init__(self, error_samples: _Optional[_Iterable[_Union[_status_pb2.Status, _Mapping]]] = ..., error_config: _Optional[_Union[ImportErrorConfig, _Mapping]] = ...) -> None: ...

class ImportSampleQueriesMetadata(_message.Message):
    __slots__ = ("create_time", "update_time", "success_count", "failure_count", "total_count")
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_COUNT_FIELD_NUMBER: _ClassVar[int]
    FAILURE_COUNT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    success_count: int
    failure_count: int
    total_count: int
    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., success_count: _Optional[int] = ..., failure_count: _Optional[int] = ..., total_count: _Optional[int] = ...) -> None: ...
