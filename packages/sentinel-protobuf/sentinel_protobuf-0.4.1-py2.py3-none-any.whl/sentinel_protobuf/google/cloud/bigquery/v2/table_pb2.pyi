from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.cloud.bigquery.v2 import biglake_config_pb2 as _biglake_config_pb2
from google.cloud.bigquery.v2 import clustering_pb2 as _clustering_pb2
from google.cloud.bigquery.v2 import encryption_config_pb2 as _encryption_config_pb2
from google.cloud.bigquery.v2 import error_pb2 as _error_pb2
from google.cloud.bigquery.v2 import external_catalog_table_options_pb2 as _external_catalog_table_options_pb2
from google.cloud.bigquery.v2 import external_data_config_pb2 as _external_data_config_pb2
from google.cloud.bigquery.v2 import partitioning_definition_pb2 as _partitioning_definition_pb2
from google.cloud.bigquery.v2 import privacy_policy_pb2 as _privacy_policy_pb2
from google.cloud.bigquery.v2 import range_partitioning_pb2 as _range_partitioning_pb2
from google.cloud.bigquery.v2 import restriction_config_pb2 as _restriction_config_pb2
from google.cloud.bigquery.v2 import table_constraints_pb2 as _table_constraints_pb2
from google.cloud.bigquery.v2 import table_reference_pb2 as _table_reference_pb2
from google.cloud.bigquery.v2 import table_schema_pb2 as _table_schema_pb2
from google.cloud.bigquery.v2 import time_partitioning_pb2 as _time_partitioning_pb2
from google.cloud.bigquery.v2 import udf_resource_pb2 as _udf_resource_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TableReplicationInfo(_message.Message):
    __slots__ = ("source_table", "replication_interval_ms", "replicated_source_last_refresh_time", "replication_status", "replication_error")
    class ReplicationStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        REPLICATION_STATUS_UNSPECIFIED: _ClassVar[TableReplicationInfo.ReplicationStatus]
        ACTIVE: _ClassVar[TableReplicationInfo.ReplicationStatus]
        SOURCE_DELETED: _ClassVar[TableReplicationInfo.ReplicationStatus]
        PERMISSION_DENIED: _ClassVar[TableReplicationInfo.ReplicationStatus]
        UNSUPPORTED_CONFIGURATION: _ClassVar[TableReplicationInfo.ReplicationStatus]
    REPLICATION_STATUS_UNSPECIFIED: TableReplicationInfo.ReplicationStatus
    ACTIVE: TableReplicationInfo.ReplicationStatus
    SOURCE_DELETED: TableReplicationInfo.ReplicationStatus
    PERMISSION_DENIED: TableReplicationInfo.ReplicationStatus
    UNSUPPORTED_CONFIGURATION: TableReplicationInfo.ReplicationStatus
    SOURCE_TABLE_FIELD_NUMBER: _ClassVar[int]
    REPLICATION_INTERVAL_MS_FIELD_NUMBER: _ClassVar[int]
    REPLICATED_SOURCE_LAST_REFRESH_TIME_FIELD_NUMBER: _ClassVar[int]
    REPLICATION_STATUS_FIELD_NUMBER: _ClassVar[int]
    REPLICATION_ERROR_FIELD_NUMBER: _ClassVar[int]
    source_table: _table_reference_pb2.TableReference
    replication_interval_ms: int
    replicated_source_last_refresh_time: int
    replication_status: TableReplicationInfo.ReplicationStatus
    replication_error: _error_pb2.ErrorProto
    def __init__(self, source_table: _Optional[_Union[_table_reference_pb2.TableReference, _Mapping]] = ..., replication_interval_ms: _Optional[int] = ..., replicated_source_last_refresh_time: _Optional[int] = ..., replication_status: _Optional[_Union[TableReplicationInfo.ReplicationStatus, str]] = ..., replication_error: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class ViewDefinition(_message.Message):
    __slots__ = ("query", "user_defined_function_resources", "use_legacy_sql", "use_explicit_column_names", "privacy_policy", "foreign_definitions")
    QUERY_FIELD_NUMBER: _ClassVar[int]
    USER_DEFINED_FUNCTION_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    USE_LEGACY_SQL_FIELD_NUMBER: _ClassVar[int]
    USE_EXPLICIT_COLUMN_NAMES_FIELD_NUMBER: _ClassVar[int]
    PRIVACY_POLICY_FIELD_NUMBER: _ClassVar[int]
    FOREIGN_DEFINITIONS_FIELD_NUMBER: _ClassVar[int]
    query: str
    user_defined_function_resources: _containers.RepeatedCompositeFieldContainer[_udf_resource_pb2.UserDefinedFunctionResource]
    use_legacy_sql: _wrappers_pb2.BoolValue
    use_explicit_column_names: bool
    privacy_policy: _privacy_policy_pb2.PrivacyPolicy
    foreign_definitions: _containers.RepeatedCompositeFieldContainer[ForeignViewDefinition]
    def __init__(self, query: _Optional[str] = ..., user_defined_function_resources: _Optional[_Iterable[_Union[_udf_resource_pb2.UserDefinedFunctionResource, _Mapping]]] = ..., use_legacy_sql: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., use_explicit_column_names: bool = ..., privacy_policy: _Optional[_Union[_privacy_policy_pb2.PrivacyPolicy, _Mapping]] = ..., foreign_definitions: _Optional[_Iterable[_Union[ForeignViewDefinition, _Mapping]]] = ...) -> None: ...

class ForeignViewDefinition(_message.Message):
    __slots__ = ("query", "dialect")
    QUERY_FIELD_NUMBER: _ClassVar[int]
    DIALECT_FIELD_NUMBER: _ClassVar[int]
    query: str
    dialect: str
    def __init__(self, query: _Optional[str] = ..., dialect: _Optional[str] = ...) -> None: ...

class MaterializedViewDefinition(_message.Message):
    __slots__ = ("query", "last_refresh_time", "enable_refresh", "refresh_interval_ms", "allow_non_incremental_definition")
    QUERY_FIELD_NUMBER: _ClassVar[int]
    LAST_REFRESH_TIME_FIELD_NUMBER: _ClassVar[int]
    ENABLE_REFRESH_FIELD_NUMBER: _ClassVar[int]
    REFRESH_INTERVAL_MS_FIELD_NUMBER: _ClassVar[int]
    ALLOW_NON_INCREMENTAL_DEFINITION_FIELD_NUMBER: _ClassVar[int]
    query: str
    last_refresh_time: int
    enable_refresh: _wrappers_pb2.BoolValue
    refresh_interval_ms: _wrappers_pb2.UInt64Value
    allow_non_incremental_definition: _wrappers_pb2.BoolValue
    def __init__(self, query: _Optional[str] = ..., last_refresh_time: _Optional[int] = ..., enable_refresh: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., refresh_interval_ms: _Optional[_Union[_wrappers_pb2.UInt64Value, _Mapping]] = ..., allow_non_incremental_definition: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...) -> None: ...

class MaterializedViewStatus(_message.Message):
    __slots__ = ("refresh_watermark", "last_refresh_status")
    REFRESH_WATERMARK_FIELD_NUMBER: _ClassVar[int]
    LAST_REFRESH_STATUS_FIELD_NUMBER: _ClassVar[int]
    refresh_watermark: _timestamp_pb2.Timestamp
    last_refresh_status: _error_pb2.ErrorProto
    def __init__(self, refresh_watermark: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_refresh_status: _Optional[_Union[_error_pb2.ErrorProto, _Mapping]] = ...) -> None: ...

class SnapshotDefinition(_message.Message):
    __slots__ = ("base_table_reference", "snapshot_time")
    BASE_TABLE_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_TIME_FIELD_NUMBER: _ClassVar[int]
    base_table_reference: _table_reference_pb2.TableReference
    snapshot_time: _timestamp_pb2.Timestamp
    def __init__(self, base_table_reference: _Optional[_Union[_table_reference_pb2.TableReference, _Mapping]] = ..., snapshot_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class CloneDefinition(_message.Message):
    __slots__ = ("base_table_reference", "clone_time")
    BASE_TABLE_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    CLONE_TIME_FIELD_NUMBER: _ClassVar[int]
    base_table_reference: _table_reference_pb2.TableReference
    clone_time: _timestamp_pb2.Timestamp
    def __init__(self, base_table_reference: _Optional[_Union[_table_reference_pb2.TableReference, _Mapping]] = ..., clone_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class Streamingbuffer(_message.Message):
    __slots__ = ("estimated_bytes", "estimated_rows", "oldest_entry_time")
    ESTIMATED_BYTES_FIELD_NUMBER: _ClassVar[int]
    ESTIMATED_ROWS_FIELD_NUMBER: _ClassVar[int]
    OLDEST_ENTRY_TIME_FIELD_NUMBER: _ClassVar[int]
    estimated_bytes: int
    estimated_rows: int
    oldest_entry_time: int
    def __init__(self, estimated_bytes: _Optional[int] = ..., estimated_rows: _Optional[int] = ..., oldest_entry_time: _Optional[int] = ...) -> None: ...

class Table(_message.Message):
    __slots__ = ("kind", "etag", "id", "self_link", "table_reference", "friendly_name", "description", "labels", "schema", "time_partitioning", "range_partitioning", "clustering", "require_partition_filter", "partition_definition", "num_bytes", "num_physical_bytes", "num_long_term_bytes", "num_rows", "creation_time", "expiration_time", "last_modified_time", "type", "view", "materialized_view", "materialized_view_status", "external_data_configuration", "biglake_configuration", "location", "streaming_buffer", "encryption_configuration", "snapshot_definition", "default_collation", "default_rounding_mode", "clone_definition", "num_time_travel_physical_bytes", "num_total_logical_bytes", "num_active_logical_bytes", "num_long_term_logical_bytes", "num_current_physical_bytes", "num_total_physical_bytes", "num_active_physical_bytes", "num_long_term_physical_bytes", "num_partitions", "max_staleness", "restrictions", "table_constraints", "resource_tags", "table_replication_info", "replicas", "external_catalog_table_options")
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class ResourceTagsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    KIND_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    SELF_LINK_FIELD_NUMBER: _ClassVar[int]
    TABLE_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    FRIENDLY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    TIME_PARTITIONING_FIELD_NUMBER: _ClassVar[int]
    RANGE_PARTITIONING_FIELD_NUMBER: _ClassVar[int]
    CLUSTERING_FIELD_NUMBER: _ClassVar[int]
    REQUIRE_PARTITION_FILTER_FIELD_NUMBER: _ClassVar[int]
    PARTITION_DEFINITION_FIELD_NUMBER: _ClassVar[int]
    NUM_BYTES_FIELD_NUMBER: _ClassVar[int]
    NUM_PHYSICAL_BYTES_FIELD_NUMBER: _ClassVar[int]
    NUM_LONG_TERM_BYTES_FIELD_NUMBER: _ClassVar[int]
    NUM_ROWS_FIELD_NUMBER: _ClassVar[int]
    CREATION_TIME_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_TIME_FIELD_NUMBER: _ClassVar[int]
    LAST_MODIFIED_TIME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    MATERIALIZED_VIEW_FIELD_NUMBER: _ClassVar[int]
    MATERIALIZED_VIEW_STATUS_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_DATA_CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    BIGLAKE_CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    STREAMING_BUFFER_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_DEFINITION_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_COLLATION_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_ROUNDING_MODE_FIELD_NUMBER: _ClassVar[int]
    CLONE_DEFINITION_FIELD_NUMBER: _ClassVar[int]
    NUM_TIME_TRAVEL_PHYSICAL_BYTES_FIELD_NUMBER: _ClassVar[int]
    NUM_TOTAL_LOGICAL_BYTES_FIELD_NUMBER: _ClassVar[int]
    NUM_ACTIVE_LOGICAL_BYTES_FIELD_NUMBER: _ClassVar[int]
    NUM_LONG_TERM_LOGICAL_BYTES_FIELD_NUMBER: _ClassVar[int]
    NUM_CURRENT_PHYSICAL_BYTES_FIELD_NUMBER: _ClassVar[int]
    NUM_TOTAL_PHYSICAL_BYTES_FIELD_NUMBER: _ClassVar[int]
    NUM_ACTIVE_PHYSICAL_BYTES_FIELD_NUMBER: _ClassVar[int]
    NUM_LONG_TERM_PHYSICAL_BYTES_FIELD_NUMBER: _ClassVar[int]
    NUM_PARTITIONS_FIELD_NUMBER: _ClassVar[int]
    MAX_STALENESS_FIELD_NUMBER: _ClassVar[int]
    RESTRICTIONS_FIELD_NUMBER: _ClassVar[int]
    TABLE_CONSTRAINTS_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_TAGS_FIELD_NUMBER: _ClassVar[int]
    TABLE_REPLICATION_INFO_FIELD_NUMBER: _ClassVar[int]
    REPLICAS_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_CATALOG_TABLE_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    kind: str
    etag: str
    id: str
    self_link: str
    table_reference: _table_reference_pb2.TableReference
    friendly_name: _wrappers_pb2.StringValue
    description: _wrappers_pb2.StringValue
    labels: _containers.ScalarMap[str, str]
    schema: _table_schema_pb2.TableSchema
    time_partitioning: _time_partitioning_pb2.TimePartitioning
    range_partitioning: _range_partitioning_pb2.RangePartitioning
    clustering: _clustering_pb2.Clustering
    require_partition_filter: _wrappers_pb2.BoolValue
    partition_definition: _partitioning_definition_pb2.PartitioningDefinition
    num_bytes: _wrappers_pb2.Int64Value
    num_physical_bytes: _wrappers_pb2.Int64Value
    num_long_term_bytes: _wrappers_pb2.Int64Value
    num_rows: _wrappers_pb2.UInt64Value
    creation_time: int
    expiration_time: _wrappers_pb2.Int64Value
    last_modified_time: int
    type: str
    view: ViewDefinition
    materialized_view: MaterializedViewDefinition
    materialized_view_status: MaterializedViewStatus
    external_data_configuration: _external_data_config_pb2.ExternalDataConfiguration
    biglake_configuration: _biglake_config_pb2.BigLakeConfiguration
    location: str
    streaming_buffer: Streamingbuffer
    encryption_configuration: _encryption_config_pb2.EncryptionConfiguration
    snapshot_definition: SnapshotDefinition
    default_collation: _wrappers_pb2.StringValue
    default_rounding_mode: _table_schema_pb2.TableFieldSchema.RoundingMode
    clone_definition: CloneDefinition
    num_time_travel_physical_bytes: _wrappers_pb2.Int64Value
    num_total_logical_bytes: _wrappers_pb2.Int64Value
    num_active_logical_bytes: _wrappers_pb2.Int64Value
    num_long_term_logical_bytes: _wrappers_pb2.Int64Value
    num_current_physical_bytes: _wrappers_pb2.Int64Value
    num_total_physical_bytes: _wrappers_pb2.Int64Value
    num_active_physical_bytes: _wrappers_pb2.Int64Value
    num_long_term_physical_bytes: _wrappers_pb2.Int64Value
    num_partitions: _wrappers_pb2.Int64Value
    max_staleness: str
    restrictions: _restriction_config_pb2.RestrictionConfig
    table_constraints: _table_constraints_pb2.TableConstraints
    resource_tags: _containers.ScalarMap[str, str]
    table_replication_info: TableReplicationInfo
    replicas: _containers.RepeatedCompositeFieldContainer[_table_reference_pb2.TableReference]
    external_catalog_table_options: _external_catalog_table_options_pb2.ExternalCatalogTableOptions
    def __init__(self, kind: _Optional[str] = ..., etag: _Optional[str] = ..., id: _Optional[str] = ..., self_link: _Optional[str] = ..., table_reference: _Optional[_Union[_table_reference_pb2.TableReference, _Mapping]] = ..., friendly_name: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., description: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., labels: _Optional[_Mapping[str, str]] = ..., schema: _Optional[_Union[_table_schema_pb2.TableSchema, _Mapping]] = ..., time_partitioning: _Optional[_Union[_time_partitioning_pb2.TimePartitioning, _Mapping]] = ..., range_partitioning: _Optional[_Union[_range_partitioning_pb2.RangePartitioning, _Mapping]] = ..., clustering: _Optional[_Union[_clustering_pb2.Clustering, _Mapping]] = ..., require_partition_filter: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., partition_definition: _Optional[_Union[_partitioning_definition_pb2.PartitioningDefinition, _Mapping]] = ..., num_bytes: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., num_physical_bytes: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., num_long_term_bytes: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., num_rows: _Optional[_Union[_wrappers_pb2.UInt64Value, _Mapping]] = ..., creation_time: _Optional[int] = ..., expiration_time: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., last_modified_time: _Optional[int] = ..., type: _Optional[str] = ..., view: _Optional[_Union[ViewDefinition, _Mapping]] = ..., materialized_view: _Optional[_Union[MaterializedViewDefinition, _Mapping]] = ..., materialized_view_status: _Optional[_Union[MaterializedViewStatus, _Mapping]] = ..., external_data_configuration: _Optional[_Union[_external_data_config_pb2.ExternalDataConfiguration, _Mapping]] = ..., biglake_configuration: _Optional[_Union[_biglake_config_pb2.BigLakeConfiguration, _Mapping]] = ..., location: _Optional[str] = ..., streaming_buffer: _Optional[_Union[Streamingbuffer, _Mapping]] = ..., encryption_configuration: _Optional[_Union[_encryption_config_pb2.EncryptionConfiguration, _Mapping]] = ..., snapshot_definition: _Optional[_Union[SnapshotDefinition, _Mapping]] = ..., default_collation: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., default_rounding_mode: _Optional[_Union[_table_schema_pb2.TableFieldSchema.RoundingMode, str]] = ..., clone_definition: _Optional[_Union[CloneDefinition, _Mapping]] = ..., num_time_travel_physical_bytes: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., num_total_logical_bytes: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., num_active_logical_bytes: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., num_long_term_logical_bytes: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., num_current_physical_bytes: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., num_total_physical_bytes: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., num_active_physical_bytes: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., num_long_term_physical_bytes: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., num_partitions: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., max_staleness: _Optional[str] = ..., restrictions: _Optional[_Union[_restriction_config_pb2.RestrictionConfig, _Mapping]] = ..., table_constraints: _Optional[_Union[_table_constraints_pb2.TableConstraints, _Mapping]] = ..., resource_tags: _Optional[_Mapping[str, str]] = ..., table_replication_info: _Optional[_Union[TableReplicationInfo, _Mapping]] = ..., replicas: _Optional[_Iterable[_Union[_table_reference_pb2.TableReference, _Mapping]]] = ..., external_catalog_table_options: _Optional[_Union[_external_catalog_table_options_pb2.ExternalCatalogTableOptions, _Mapping]] = ...) -> None: ...

class GetTableRequest(_message.Message):
    __slots__ = ("project_id", "dataset_id", "table_id", "selected_fields", "view")
    class TableMetadataView(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TABLE_METADATA_VIEW_UNSPECIFIED: _ClassVar[GetTableRequest.TableMetadataView]
        BASIC: _ClassVar[GetTableRequest.TableMetadataView]
        STORAGE_STATS: _ClassVar[GetTableRequest.TableMetadataView]
        FULL: _ClassVar[GetTableRequest.TableMetadataView]
    TABLE_METADATA_VIEW_UNSPECIFIED: GetTableRequest.TableMetadataView
    BASIC: GetTableRequest.TableMetadataView
    STORAGE_STATS: GetTableRequest.TableMetadataView
    FULL: GetTableRequest.TableMetadataView
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    DATASET_ID_FIELD_NUMBER: _ClassVar[int]
    TABLE_ID_FIELD_NUMBER: _ClassVar[int]
    SELECTED_FIELDS_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    dataset_id: str
    table_id: str
    selected_fields: str
    view: GetTableRequest.TableMetadataView
    def __init__(self, project_id: _Optional[str] = ..., dataset_id: _Optional[str] = ..., table_id: _Optional[str] = ..., selected_fields: _Optional[str] = ..., view: _Optional[_Union[GetTableRequest.TableMetadataView, str]] = ...) -> None: ...

class InsertTableRequest(_message.Message):
    __slots__ = ("project_id", "dataset_id", "table")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    DATASET_ID_FIELD_NUMBER: _ClassVar[int]
    TABLE_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    dataset_id: str
    table: Table
    def __init__(self, project_id: _Optional[str] = ..., dataset_id: _Optional[str] = ..., table: _Optional[_Union[Table, _Mapping]] = ...) -> None: ...

class UpdateOrPatchTableRequest(_message.Message):
    __slots__ = ("project_id", "dataset_id", "table_id", "table", "autodetect_schema")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    DATASET_ID_FIELD_NUMBER: _ClassVar[int]
    TABLE_ID_FIELD_NUMBER: _ClassVar[int]
    TABLE_FIELD_NUMBER: _ClassVar[int]
    AUTODETECT_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    dataset_id: str
    table_id: str
    table: Table
    autodetect_schema: bool
    def __init__(self, project_id: _Optional[str] = ..., dataset_id: _Optional[str] = ..., table_id: _Optional[str] = ..., table: _Optional[_Union[Table, _Mapping]] = ..., autodetect_schema: bool = ...) -> None: ...

class DeleteTableRequest(_message.Message):
    __slots__ = ("project_id", "dataset_id", "table_id")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    DATASET_ID_FIELD_NUMBER: _ClassVar[int]
    TABLE_ID_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    dataset_id: str
    table_id: str
    def __init__(self, project_id: _Optional[str] = ..., dataset_id: _Optional[str] = ..., table_id: _Optional[str] = ...) -> None: ...

class ListTablesRequest(_message.Message):
    __slots__ = ("project_id", "dataset_id", "max_results", "page_token")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    DATASET_ID_FIELD_NUMBER: _ClassVar[int]
    MAX_RESULTS_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    dataset_id: str
    max_results: _wrappers_pb2.UInt32Value
    page_token: str
    def __init__(self, project_id: _Optional[str] = ..., dataset_id: _Optional[str] = ..., max_results: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListFormatView(_message.Message):
    __slots__ = ("use_legacy_sql", "privacy_policy")
    USE_LEGACY_SQL_FIELD_NUMBER: _ClassVar[int]
    PRIVACY_POLICY_FIELD_NUMBER: _ClassVar[int]
    use_legacy_sql: _wrappers_pb2.BoolValue
    privacy_policy: _privacy_policy_pb2.PrivacyPolicy
    def __init__(self, use_legacy_sql: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., privacy_policy: _Optional[_Union[_privacy_policy_pb2.PrivacyPolicy, _Mapping]] = ...) -> None: ...

class ListFormatTable(_message.Message):
    __slots__ = ("kind", "id", "table_reference", "friendly_name", "type", "time_partitioning", "range_partitioning", "clustering", "labels", "view", "creation_time", "expiration_time", "require_partition_filter")
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    KIND_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    TABLE_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    FRIENDLY_NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    TIME_PARTITIONING_FIELD_NUMBER: _ClassVar[int]
    RANGE_PARTITIONING_FIELD_NUMBER: _ClassVar[int]
    CLUSTERING_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    CREATION_TIME_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_TIME_FIELD_NUMBER: _ClassVar[int]
    REQUIRE_PARTITION_FILTER_FIELD_NUMBER: _ClassVar[int]
    kind: str
    id: str
    table_reference: _table_reference_pb2.TableReference
    friendly_name: _wrappers_pb2.StringValue
    type: str
    time_partitioning: _time_partitioning_pb2.TimePartitioning
    range_partitioning: _range_partitioning_pb2.RangePartitioning
    clustering: _clustering_pb2.Clustering
    labels: _containers.ScalarMap[str, str]
    view: ListFormatView
    creation_time: int
    expiration_time: int
    require_partition_filter: _wrappers_pb2.BoolValue
    def __init__(self, kind: _Optional[str] = ..., id: _Optional[str] = ..., table_reference: _Optional[_Union[_table_reference_pb2.TableReference, _Mapping]] = ..., friendly_name: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., type: _Optional[str] = ..., time_partitioning: _Optional[_Union[_time_partitioning_pb2.TimePartitioning, _Mapping]] = ..., range_partitioning: _Optional[_Union[_range_partitioning_pb2.RangePartitioning, _Mapping]] = ..., clustering: _Optional[_Union[_clustering_pb2.Clustering, _Mapping]] = ..., labels: _Optional[_Mapping[str, str]] = ..., view: _Optional[_Union[ListFormatView, _Mapping]] = ..., creation_time: _Optional[int] = ..., expiration_time: _Optional[int] = ..., require_partition_filter: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...) -> None: ...

class TableList(_message.Message):
    __slots__ = ("kind", "etag", "next_page_token", "tables", "total_items")
    KIND_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TABLES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_ITEMS_FIELD_NUMBER: _ClassVar[int]
    kind: str
    etag: str
    next_page_token: str
    tables: _containers.RepeatedCompositeFieldContainer[ListFormatTable]
    total_items: _wrappers_pb2.Int32Value
    def __init__(self, kind: _Optional[str] = ..., etag: _Optional[str] = ..., next_page_token: _Optional[str] = ..., tables: _Optional[_Iterable[_Union[ListFormatTable, _Mapping]]] = ..., total_items: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ...) -> None: ...
