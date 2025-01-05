from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.bigquery.v2 import clustering_pb2 as _clustering_pb2
from google.cloud.bigquery.v2 import dataset_reference_pb2 as _dataset_reference_pb2
from google.cloud.bigquery.v2 import decimal_target_types_pb2 as _decimal_target_types_pb2
from google.cloud.bigquery.v2 import encryption_config_pb2 as _encryption_config_pb2
from google.cloud.bigquery.v2 import external_data_config_pb2 as _external_data_config_pb2
from google.cloud.bigquery.v2 import file_set_specification_type_pb2 as _file_set_specification_type_pb2
from google.cloud.bigquery.v2 import hive_partitioning_pb2 as _hive_partitioning_pb2
from google.cloud.bigquery.v2 import json_extension_pb2 as _json_extension_pb2
from google.cloud.bigquery.v2 import model_reference_pb2 as _model_reference_pb2
from google.cloud.bigquery.v2 import query_parameter_pb2 as _query_parameter_pb2
from google.cloud.bigquery.v2 import range_partitioning_pb2 as _range_partitioning_pb2
from google.cloud.bigquery.v2 import system_variable_pb2 as _system_variable_pb2
from google.cloud.bigquery.v2 import table_reference_pb2 as _table_reference_pb2
from google.cloud.bigquery.v2 import table_schema_pb2 as _table_schema_pb2
from google.cloud.bigquery.v2 import time_partitioning_pb2 as _time_partitioning_pb2
from google.cloud.bigquery.v2 import udf_resource_pb2 as _udf_resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DestinationTableProperties(_message.Message):
    __slots__ = ("friendly_name", "description", "labels")
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    FRIENDLY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    friendly_name: _wrappers_pb2.StringValue
    description: _wrappers_pb2.StringValue
    labels: _containers.ScalarMap[str, str]
    def __init__(self, friendly_name: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., description: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., labels: _Optional[_Mapping[str, str]] = ...) -> None: ...

class ConnectionProperty(_message.Message):
    __slots__ = ("key", "value")
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: str
    def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class JobConfigurationQuery(_message.Message):
    __slots__ = ("query", "destination_table", "external_table_definitions", "user_defined_function_resources", "create_disposition", "write_disposition", "default_dataset", "priority", "allow_large_results", "use_query_cache", "flatten_results", "maximum_bytes_billed", "use_legacy_sql", "parameter_mode", "query_parameters", "system_variables", "schema_update_options", "time_partitioning", "range_partitioning", "clustering", "destination_encryption_configuration", "script_options", "connection_properties", "create_session", "continuous")
    class ExternalTableDefinitionsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _external_data_config_pb2.ExternalDataConfiguration
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_external_data_config_pb2.ExternalDataConfiguration, _Mapping]] = ...) -> None: ...
    QUERY_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_TABLE_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_TABLE_DEFINITIONS_FIELD_NUMBER: _ClassVar[int]
    USER_DEFINED_FUNCTION_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    CREATE_DISPOSITION_FIELD_NUMBER: _ClassVar[int]
    WRITE_DISPOSITION_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_DATASET_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    ALLOW_LARGE_RESULTS_FIELD_NUMBER: _ClassVar[int]
    USE_QUERY_CACHE_FIELD_NUMBER: _ClassVar[int]
    FLATTEN_RESULTS_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_BYTES_BILLED_FIELD_NUMBER: _ClassVar[int]
    USE_LEGACY_SQL_FIELD_NUMBER: _ClassVar[int]
    PARAMETER_MODE_FIELD_NUMBER: _ClassVar[int]
    QUERY_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_VARIABLES_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_UPDATE_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    TIME_PARTITIONING_FIELD_NUMBER: _ClassVar[int]
    RANGE_PARTITIONING_FIELD_NUMBER: _ClassVar[int]
    CLUSTERING_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_ENCRYPTION_CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    SCRIPT_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    CREATE_SESSION_FIELD_NUMBER: _ClassVar[int]
    CONTINUOUS_FIELD_NUMBER: _ClassVar[int]
    query: str
    destination_table: _table_reference_pb2.TableReference
    external_table_definitions: _containers.MessageMap[str, _external_data_config_pb2.ExternalDataConfiguration]
    user_defined_function_resources: _containers.RepeatedCompositeFieldContainer[_udf_resource_pb2.UserDefinedFunctionResource]
    create_disposition: str
    write_disposition: str
    default_dataset: _dataset_reference_pb2.DatasetReference
    priority: str
    allow_large_results: _wrappers_pb2.BoolValue
    use_query_cache: _wrappers_pb2.BoolValue
    flatten_results: _wrappers_pb2.BoolValue
    maximum_bytes_billed: _wrappers_pb2.Int64Value
    use_legacy_sql: _wrappers_pb2.BoolValue
    parameter_mode: str
    query_parameters: _containers.RepeatedCompositeFieldContainer[_query_parameter_pb2.QueryParameter]
    system_variables: _system_variable_pb2.SystemVariables
    schema_update_options: _containers.RepeatedScalarFieldContainer[str]
    time_partitioning: _time_partitioning_pb2.TimePartitioning
    range_partitioning: _range_partitioning_pb2.RangePartitioning
    clustering: _clustering_pb2.Clustering
    destination_encryption_configuration: _encryption_config_pb2.EncryptionConfiguration
    script_options: ScriptOptions
    connection_properties: _containers.RepeatedCompositeFieldContainer[ConnectionProperty]
    create_session: _wrappers_pb2.BoolValue
    continuous: _wrappers_pb2.BoolValue
    def __init__(self, query: _Optional[str] = ..., destination_table: _Optional[_Union[_table_reference_pb2.TableReference, _Mapping]] = ..., external_table_definitions: _Optional[_Mapping[str, _external_data_config_pb2.ExternalDataConfiguration]] = ..., user_defined_function_resources: _Optional[_Iterable[_Union[_udf_resource_pb2.UserDefinedFunctionResource, _Mapping]]] = ..., create_disposition: _Optional[str] = ..., write_disposition: _Optional[str] = ..., default_dataset: _Optional[_Union[_dataset_reference_pb2.DatasetReference, _Mapping]] = ..., priority: _Optional[str] = ..., allow_large_results: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., use_query_cache: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., flatten_results: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., maximum_bytes_billed: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., use_legacy_sql: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., parameter_mode: _Optional[str] = ..., query_parameters: _Optional[_Iterable[_Union[_query_parameter_pb2.QueryParameter, _Mapping]]] = ..., system_variables: _Optional[_Union[_system_variable_pb2.SystemVariables, _Mapping]] = ..., schema_update_options: _Optional[_Iterable[str]] = ..., time_partitioning: _Optional[_Union[_time_partitioning_pb2.TimePartitioning, _Mapping]] = ..., range_partitioning: _Optional[_Union[_range_partitioning_pb2.RangePartitioning, _Mapping]] = ..., clustering: _Optional[_Union[_clustering_pb2.Clustering, _Mapping]] = ..., destination_encryption_configuration: _Optional[_Union[_encryption_config_pb2.EncryptionConfiguration, _Mapping]] = ..., script_options: _Optional[_Union[ScriptOptions, _Mapping]] = ..., connection_properties: _Optional[_Iterable[_Union[ConnectionProperty, _Mapping]]] = ..., create_session: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., continuous: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...) -> None: ...

class ScriptOptions(_message.Message):
    __slots__ = ("statement_timeout_ms", "statement_byte_budget", "key_result_statement")
    class KeyResultStatementKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        KEY_RESULT_STATEMENT_KIND_UNSPECIFIED: _ClassVar[ScriptOptions.KeyResultStatementKind]
        LAST: _ClassVar[ScriptOptions.KeyResultStatementKind]
        FIRST_SELECT: _ClassVar[ScriptOptions.KeyResultStatementKind]
    KEY_RESULT_STATEMENT_KIND_UNSPECIFIED: ScriptOptions.KeyResultStatementKind
    LAST: ScriptOptions.KeyResultStatementKind
    FIRST_SELECT: ScriptOptions.KeyResultStatementKind
    STATEMENT_TIMEOUT_MS_FIELD_NUMBER: _ClassVar[int]
    STATEMENT_BYTE_BUDGET_FIELD_NUMBER: _ClassVar[int]
    KEY_RESULT_STATEMENT_FIELD_NUMBER: _ClassVar[int]
    statement_timeout_ms: _wrappers_pb2.Int64Value
    statement_byte_budget: _wrappers_pb2.Int64Value
    key_result_statement: ScriptOptions.KeyResultStatementKind
    def __init__(self, statement_timeout_ms: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., statement_byte_budget: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., key_result_statement: _Optional[_Union[ScriptOptions.KeyResultStatementKind, str]] = ...) -> None: ...

class JobConfigurationLoad(_message.Message):
    __slots__ = ("source_uris", "file_set_spec_type", "schema", "destination_table", "destination_table_properties", "create_disposition", "write_disposition", "null_marker", "field_delimiter", "skip_leading_rows", "encoding", "quote", "max_bad_records", "allow_quoted_newlines", "source_format", "allow_jagged_rows", "ignore_unknown_values", "projection_fields", "autodetect", "schema_update_options", "time_partitioning", "range_partitioning", "clustering", "destination_encryption_configuration", "use_avro_logical_types", "reference_file_schema_uri", "hive_partitioning_options", "decimal_target_types", "json_extension", "parquet_options", "preserve_ascii_control_characters", "connection_properties", "create_session", "column_name_character_map", "copy_files_only")
    class ColumnNameCharacterMap(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        COLUMN_NAME_CHARACTER_MAP_UNSPECIFIED: _ClassVar[JobConfigurationLoad.ColumnNameCharacterMap]
        STRICT: _ClassVar[JobConfigurationLoad.ColumnNameCharacterMap]
        V1: _ClassVar[JobConfigurationLoad.ColumnNameCharacterMap]
        V2: _ClassVar[JobConfigurationLoad.ColumnNameCharacterMap]
    COLUMN_NAME_CHARACTER_MAP_UNSPECIFIED: JobConfigurationLoad.ColumnNameCharacterMap
    STRICT: JobConfigurationLoad.ColumnNameCharacterMap
    V1: JobConfigurationLoad.ColumnNameCharacterMap
    V2: JobConfigurationLoad.ColumnNameCharacterMap
    SOURCE_URIS_FIELD_NUMBER: _ClassVar[int]
    FILE_SET_SPEC_TYPE_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_TABLE_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_TABLE_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    CREATE_DISPOSITION_FIELD_NUMBER: _ClassVar[int]
    WRITE_DISPOSITION_FIELD_NUMBER: _ClassVar[int]
    NULL_MARKER_FIELD_NUMBER: _ClassVar[int]
    FIELD_DELIMITER_FIELD_NUMBER: _ClassVar[int]
    SKIP_LEADING_ROWS_FIELD_NUMBER: _ClassVar[int]
    ENCODING_FIELD_NUMBER: _ClassVar[int]
    QUOTE_FIELD_NUMBER: _ClassVar[int]
    MAX_BAD_RECORDS_FIELD_NUMBER: _ClassVar[int]
    ALLOW_QUOTED_NEWLINES_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FORMAT_FIELD_NUMBER: _ClassVar[int]
    ALLOW_JAGGED_ROWS_FIELD_NUMBER: _ClassVar[int]
    IGNORE_UNKNOWN_VALUES_FIELD_NUMBER: _ClassVar[int]
    PROJECTION_FIELDS_FIELD_NUMBER: _ClassVar[int]
    AUTODETECT_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_UPDATE_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    TIME_PARTITIONING_FIELD_NUMBER: _ClassVar[int]
    RANGE_PARTITIONING_FIELD_NUMBER: _ClassVar[int]
    CLUSTERING_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_ENCRYPTION_CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    USE_AVRO_LOGICAL_TYPES_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_FILE_SCHEMA_URI_FIELD_NUMBER: _ClassVar[int]
    HIVE_PARTITIONING_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    DECIMAL_TARGET_TYPES_FIELD_NUMBER: _ClassVar[int]
    JSON_EXTENSION_FIELD_NUMBER: _ClassVar[int]
    PARQUET_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    PRESERVE_ASCII_CONTROL_CHARACTERS_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    CREATE_SESSION_FIELD_NUMBER: _ClassVar[int]
    COLUMN_NAME_CHARACTER_MAP_FIELD_NUMBER: _ClassVar[int]
    COPY_FILES_ONLY_FIELD_NUMBER: _ClassVar[int]
    source_uris: _containers.RepeatedScalarFieldContainer[str]
    file_set_spec_type: _file_set_specification_type_pb2.FileSetSpecType
    schema: _table_schema_pb2.TableSchema
    destination_table: _table_reference_pb2.TableReference
    destination_table_properties: DestinationTableProperties
    create_disposition: str
    write_disposition: str
    null_marker: _wrappers_pb2.StringValue
    field_delimiter: str
    skip_leading_rows: _wrappers_pb2.Int32Value
    encoding: str
    quote: _wrappers_pb2.StringValue
    max_bad_records: _wrappers_pb2.Int32Value
    allow_quoted_newlines: _wrappers_pb2.BoolValue
    source_format: str
    allow_jagged_rows: _wrappers_pb2.BoolValue
    ignore_unknown_values: _wrappers_pb2.BoolValue
    projection_fields: _containers.RepeatedScalarFieldContainer[str]
    autodetect: _wrappers_pb2.BoolValue
    schema_update_options: _containers.RepeatedScalarFieldContainer[str]
    time_partitioning: _time_partitioning_pb2.TimePartitioning
    range_partitioning: _range_partitioning_pb2.RangePartitioning
    clustering: _clustering_pb2.Clustering
    destination_encryption_configuration: _encryption_config_pb2.EncryptionConfiguration
    use_avro_logical_types: _wrappers_pb2.BoolValue
    reference_file_schema_uri: _wrappers_pb2.StringValue
    hive_partitioning_options: _hive_partitioning_pb2.HivePartitioningOptions
    decimal_target_types: _containers.RepeatedScalarFieldContainer[_decimal_target_types_pb2.DecimalTargetType]
    json_extension: _json_extension_pb2.JsonExtension
    parquet_options: _external_data_config_pb2.ParquetOptions
    preserve_ascii_control_characters: _wrappers_pb2.BoolValue
    connection_properties: _containers.RepeatedCompositeFieldContainer[ConnectionProperty]
    create_session: _wrappers_pb2.BoolValue
    column_name_character_map: JobConfigurationLoad.ColumnNameCharacterMap
    copy_files_only: _wrappers_pb2.BoolValue
    def __init__(self, source_uris: _Optional[_Iterable[str]] = ..., file_set_spec_type: _Optional[_Union[_file_set_specification_type_pb2.FileSetSpecType, str]] = ..., schema: _Optional[_Union[_table_schema_pb2.TableSchema, _Mapping]] = ..., destination_table: _Optional[_Union[_table_reference_pb2.TableReference, _Mapping]] = ..., destination_table_properties: _Optional[_Union[DestinationTableProperties, _Mapping]] = ..., create_disposition: _Optional[str] = ..., write_disposition: _Optional[str] = ..., null_marker: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., field_delimiter: _Optional[str] = ..., skip_leading_rows: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., encoding: _Optional[str] = ..., quote: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., max_bad_records: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., allow_quoted_newlines: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., source_format: _Optional[str] = ..., allow_jagged_rows: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., ignore_unknown_values: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., projection_fields: _Optional[_Iterable[str]] = ..., autodetect: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., schema_update_options: _Optional[_Iterable[str]] = ..., time_partitioning: _Optional[_Union[_time_partitioning_pb2.TimePartitioning, _Mapping]] = ..., range_partitioning: _Optional[_Union[_range_partitioning_pb2.RangePartitioning, _Mapping]] = ..., clustering: _Optional[_Union[_clustering_pb2.Clustering, _Mapping]] = ..., destination_encryption_configuration: _Optional[_Union[_encryption_config_pb2.EncryptionConfiguration, _Mapping]] = ..., use_avro_logical_types: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., reference_file_schema_uri: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., hive_partitioning_options: _Optional[_Union[_hive_partitioning_pb2.HivePartitioningOptions, _Mapping]] = ..., decimal_target_types: _Optional[_Iterable[_Union[_decimal_target_types_pb2.DecimalTargetType, str]]] = ..., json_extension: _Optional[_Union[_json_extension_pb2.JsonExtension, str]] = ..., parquet_options: _Optional[_Union[_external_data_config_pb2.ParquetOptions, _Mapping]] = ..., preserve_ascii_control_characters: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., connection_properties: _Optional[_Iterable[_Union[ConnectionProperty, _Mapping]]] = ..., create_session: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., column_name_character_map: _Optional[_Union[JobConfigurationLoad.ColumnNameCharacterMap, str]] = ..., copy_files_only: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...) -> None: ...

class JobConfigurationTableCopy(_message.Message):
    __slots__ = ("source_table", "source_tables", "destination_table", "create_disposition", "write_disposition", "destination_encryption_configuration", "operation_type", "destination_expiration_time")
    class OperationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        OPERATION_TYPE_UNSPECIFIED: _ClassVar[JobConfigurationTableCopy.OperationType]
        COPY: _ClassVar[JobConfigurationTableCopy.OperationType]
        SNAPSHOT: _ClassVar[JobConfigurationTableCopy.OperationType]
        RESTORE: _ClassVar[JobConfigurationTableCopy.OperationType]
        CLONE: _ClassVar[JobConfigurationTableCopy.OperationType]
    OPERATION_TYPE_UNSPECIFIED: JobConfigurationTableCopy.OperationType
    COPY: JobConfigurationTableCopy.OperationType
    SNAPSHOT: JobConfigurationTableCopy.OperationType
    RESTORE: JobConfigurationTableCopy.OperationType
    CLONE: JobConfigurationTableCopy.OperationType
    SOURCE_TABLE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_TABLES_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_TABLE_FIELD_NUMBER: _ClassVar[int]
    CREATE_DISPOSITION_FIELD_NUMBER: _ClassVar[int]
    WRITE_DISPOSITION_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_ENCRYPTION_CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    OPERATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_EXPIRATION_TIME_FIELD_NUMBER: _ClassVar[int]
    source_table: _table_reference_pb2.TableReference
    source_tables: _containers.RepeatedCompositeFieldContainer[_table_reference_pb2.TableReference]
    destination_table: _table_reference_pb2.TableReference
    create_disposition: str
    write_disposition: str
    destination_encryption_configuration: _encryption_config_pb2.EncryptionConfiguration
    operation_type: JobConfigurationTableCopy.OperationType
    destination_expiration_time: _timestamp_pb2.Timestamp
    def __init__(self, source_table: _Optional[_Union[_table_reference_pb2.TableReference, _Mapping]] = ..., source_tables: _Optional[_Iterable[_Union[_table_reference_pb2.TableReference, _Mapping]]] = ..., destination_table: _Optional[_Union[_table_reference_pb2.TableReference, _Mapping]] = ..., create_disposition: _Optional[str] = ..., write_disposition: _Optional[str] = ..., destination_encryption_configuration: _Optional[_Union[_encryption_config_pb2.EncryptionConfiguration, _Mapping]] = ..., operation_type: _Optional[_Union[JobConfigurationTableCopy.OperationType, str]] = ..., destination_expiration_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class JobConfigurationExtract(_message.Message):
    __slots__ = ("source_table", "source_model", "destination_uris", "print_header", "field_delimiter", "destination_format", "compression", "use_avro_logical_types", "model_extract_options")
    class ModelExtractOptions(_message.Message):
        __slots__ = ("trial_id",)
        TRIAL_ID_FIELD_NUMBER: _ClassVar[int]
        trial_id: _wrappers_pb2.Int64Value
        def __init__(self, trial_id: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ...) -> None: ...
    SOURCE_TABLE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_MODEL_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_URIS_FIELD_NUMBER: _ClassVar[int]
    PRINT_HEADER_FIELD_NUMBER: _ClassVar[int]
    FIELD_DELIMITER_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_FORMAT_FIELD_NUMBER: _ClassVar[int]
    COMPRESSION_FIELD_NUMBER: _ClassVar[int]
    USE_AVRO_LOGICAL_TYPES_FIELD_NUMBER: _ClassVar[int]
    MODEL_EXTRACT_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    source_table: _table_reference_pb2.TableReference
    source_model: _model_reference_pb2.ModelReference
    destination_uris: _containers.RepeatedScalarFieldContainer[str]
    print_header: _wrappers_pb2.BoolValue
    field_delimiter: str
    destination_format: str
    compression: str
    use_avro_logical_types: _wrappers_pb2.BoolValue
    model_extract_options: JobConfigurationExtract.ModelExtractOptions
    def __init__(self, source_table: _Optional[_Union[_table_reference_pb2.TableReference, _Mapping]] = ..., source_model: _Optional[_Union[_model_reference_pb2.ModelReference, _Mapping]] = ..., destination_uris: _Optional[_Iterable[str]] = ..., print_header: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., field_delimiter: _Optional[str] = ..., destination_format: _Optional[str] = ..., compression: _Optional[str] = ..., use_avro_logical_types: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., model_extract_options: _Optional[_Union[JobConfigurationExtract.ModelExtractOptions, _Mapping]] = ...) -> None: ...

class JobConfiguration(_message.Message):
    __slots__ = ("job_type", "query", "load", "copy", "extract", "dry_run", "job_timeout_ms", "labels")
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    JOB_TYPE_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    LOAD_FIELD_NUMBER: _ClassVar[int]
    COPY_FIELD_NUMBER: _ClassVar[int]
    EXTRACT_FIELD_NUMBER: _ClassVar[int]
    DRY_RUN_FIELD_NUMBER: _ClassVar[int]
    JOB_TIMEOUT_MS_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    job_type: str
    query: JobConfigurationQuery
    load: JobConfigurationLoad
    copy: JobConfigurationTableCopy
    extract: JobConfigurationExtract
    dry_run: _wrappers_pb2.BoolValue
    job_timeout_ms: _wrappers_pb2.Int64Value
    labels: _containers.ScalarMap[str, str]
    def __init__(self, job_type: _Optional[str] = ..., query: _Optional[_Union[JobConfigurationQuery, _Mapping]] = ..., load: _Optional[_Union[JobConfigurationLoad, _Mapping]] = ..., copy: _Optional[_Union[JobConfigurationTableCopy, _Mapping]] = ..., extract: _Optional[_Union[JobConfigurationExtract, _Mapping]] = ..., dry_run: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., job_timeout_ms: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., labels: _Optional[_Mapping[str, str]] = ...) -> None: ...
