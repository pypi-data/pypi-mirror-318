from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.cloud.bigquery.v2 import decimal_target_types_pb2 as _decimal_target_types_pb2
from google.cloud.bigquery.v2 import file_set_specification_type_pb2 as _file_set_specification_type_pb2
from google.cloud.bigquery.v2 import hive_partitioning_pb2 as _hive_partitioning_pb2
from google.cloud.bigquery.v2 import json_extension_pb2 as _json_extension_pb2
from google.cloud.bigquery.v2 import map_target_type_pb2 as _map_target_type_pb2
from google.cloud.bigquery.v2 import table_schema_pb2 as _table_schema_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AvroOptions(_message.Message):
    __slots__ = ("use_avro_logical_types",)
    USE_AVRO_LOGICAL_TYPES_FIELD_NUMBER: _ClassVar[int]
    use_avro_logical_types: _wrappers_pb2.BoolValue
    def __init__(self, use_avro_logical_types: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...) -> None: ...

class ParquetOptions(_message.Message):
    __slots__ = ("enum_as_string", "enable_list_inference", "map_target_type")
    ENUM_AS_STRING_FIELD_NUMBER: _ClassVar[int]
    ENABLE_LIST_INFERENCE_FIELD_NUMBER: _ClassVar[int]
    MAP_TARGET_TYPE_FIELD_NUMBER: _ClassVar[int]
    enum_as_string: _wrappers_pb2.BoolValue
    enable_list_inference: _wrappers_pb2.BoolValue
    map_target_type: _map_target_type_pb2.MapTargetType
    def __init__(self, enum_as_string: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., enable_list_inference: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., map_target_type: _Optional[_Union[_map_target_type_pb2.MapTargetType, str]] = ...) -> None: ...

class CsvOptions(_message.Message):
    __slots__ = ("field_delimiter", "skip_leading_rows", "quote", "allow_quoted_newlines", "allow_jagged_rows", "encoding", "preserve_ascii_control_characters", "null_marker")
    FIELD_DELIMITER_FIELD_NUMBER: _ClassVar[int]
    SKIP_LEADING_ROWS_FIELD_NUMBER: _ClassVar[int]
    QUOTE_FIELD_NUMBER: _ClassVar[int]
    ALLOW_QUOTED_NEWLINES_FIELD_NUMBER: _ClassVar[int]
    ALLOW_JAGGED_ROWS_FIELD_NUMBER: _ClassVar[int]
    ENCODING_FIELD_NUMBER: _ClassVar[int]
    PRESERVE_ASCII_CONTROL_CHARACTERS_FIELD_NUMBER: _ClassVar[int]
    NULL_MARKER_FIELD_NUMBER: _ClassVar[int]
    field_delimiter: str
    skip_leading_rows: _wrappers_pb2.Int64Value
    quote: _wrappers_pb2.StringValue
    allow_quoted_newlines: _wrappers_pb2.BoolValue
    allow_jagged_rows: _wrappers_pb2.BoolValue
    encoding: str
    preserve_ascii_control_characters: _wrappers_pb2.BoolValue
    null_marker: _wrappers_pb2.StringValue
    def __init__(self, field_delimiter: _Optional[str] = ..., skip_leading_rows: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., quote: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., allow_quoted_newlines: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., allow_jagged_rows: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., encoding: _Optional[str] = ..., preserve_ascii_control_characters: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., null_marker: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...

class JsonOptions(_message.Message):
    __slots__ = ("encoding",)
    ENCODING_FIELD_NUMBER: _ClassVar[int]
    encoding: str
    def __init__(self, encoding: _Optional[str] = ...) -> None: ...

class BigtableColumn(_message.Message):
    __slots__ = ("qualifier_encoded", "qualifier_string", "field_name", "type", "encoding", "only_read_latest")
    QUALIFIER_ENCODED_FIELD_NUMBER: _ClassVar[int]
    QUALIFIER_STRING_FIELD_NUMBER: _ClassVar[int]
    FIELD_NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ENCODING_FIELD_NUMBER: _ClassVar[int]
    ONLY_READ_LATEST_FIELD_NUMBER: _ClassVar[int]
    qualifier_encoded: _wrappers_pb2.BytesValue
    qualifier_string: _wrappers_pb2.StringValue
    field_name: str
    type: str
    encoding: str
    only_read_latest: _wrappers_pb2.BoolValue
    def __init__(self, qualifier_encoded: _Optional[_Union[_wrappers_pb2.BytesValue, _Mapping]] = ..., qualifier_string: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., field_name: _Optional[str] = ..., type: _Optional[str] = ..., encoding: _Optional[str] = ..., only_read_latest: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...) -> None: ...

class BigtableColumnFamily(_message.Message):
    __slots__ = ("family_id", "type", "encoding", "columns", "only_read_latest")
    FAMILY_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ENCODING_FIELD_NUMBER: _ClassVar[int]
    COLUMNS_FIELD_NUMBER: _ClassVar[int]
    ONLY_READ_LATEST_FIELD_NUMBER: _ClassVar[int]
    family_id: str
    type: str
    encoding: str
    columns: _containers.RepeatedCompositeFieldContainer[BigtableColumn]
    only_read_latest: _wrappers_pb2.BoolValue
    def __init__(self, family_id: _Optional[str] = ..., type: _Optional[str] = ..., encoding: _Optional[str] = ..., columns: _Optional[_Iterable[_Union[BigtableColumn, _Mapping]]] = ..., only_read_latest: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...) -> None: ...

class BigtableOptions(_message.Message):
    __slots__ = ("column_families", "ignore_unspecified_column_families", "read_rowkey_as_string", "output_column_families_as_json")
    COLUMN_FAMILIES_FIELD_NUMBER: _ClassVar[int]
    IGNORE_UNSPECIFIED_COLUMN_FAMILIES_FIELD_NUMBER: _ClassVar[int]
    READ_ROWKEY_AS_STRING_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_COLUMN_FAMILIES_AS_JSON_FIELD_NUMBER: _ClassVar[int]
    column_families: _containers.RepeatedCompositeFieldContainer[BigtableColumnFamily]
    ignore_unspecified_column_families: _wrappers_pb2.BoolValue
    read_rowkey_as_string: _wrappers_pb2.BoolValue
    output_column_families_as_json: _wrappers_pb2.BoolValue
    def __init__(self, column_families: _Optional[_Iterable[_Union[BigtableColumnFamily, _Mapping]]] = ..., ignore_unspecified_column_families: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., read_rowkey_as_string: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., output_column_families_as_json: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...) -> None: ...

class GoogleSheetsOptions(_message.Message):
    __slots__ = ("skip_leading_rows", "range")
    SKIP_LEADING_ROWS_FIELD_NUMBER: _ClassVar[int]
    RANGE_FIELD_NUMBER: _ClassVar[int]
    skip_leading_rows: _wrappers_pb2.Int64Value
    range: str
    def __init__(self, skip_leading_rows: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., range: _Optional[str] = ...) -> None: ...

class ExternalDataConfiguration(_message.Message):
    __slots__ = ("source_uris", "file_set_spec_type", "schema", "source_format", "max_bad_records", "autodetect", "ignore_unknown_values", "compression", "csv_options", "json_options", "bigtable_options", "google_sheets_options", "hive_partitioning_options", "connection_id", "decimal_target_types", "avro_options", "json_extension", "parquet_options", "object_metadata", "reference_file_schema_uri", "metadata_cache_mode")
    class ObjectMetadata(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        OBJECT_METADATA_UNSPECIFIED: _ClassVar[ExternalDataConfiguration.ObjectMetadata]
        DIRECTORY: _ClassVar[ExternalDataConfiguration.ObjectMetadata]
        SIMPLE: _ClassVar[ExternalDataConfiguration.ObjectMetadata]
    OBJECT_METADATA_UNSPECIFIED: ExternalDataConfiguration.ObjectMetadata
    DIRECTORY: ExternalDataConfiguration.ObjectMetadata
    SIMPLE: ExternalDataConfiguration.ObjectMetadata
    class MetadataCacheMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        METADATA_CACHE_MODE_UNSPECIFIED: _ClassVar[ExternalDataConfiguration.MetadataCacheMode]
        AUTOMATIC: _ClassVar[ExternalDataConfiguration.MetadataCacheMode]
        MANUAL: _ClassVar[ExternalDataConfiguration.MetadataCacheMode]
    METADATA_CACHE_MODE_UNSPECIFIED: ExternalDataConfiguration.MetadataCacheMode
    AUTOMATIC: ExternalDataConfiguration.MetadataCacheMode
    MANUAL: ExternalDataConfiguration.MetadataCacheMode
    SOURCE_URIS_FIELD_NUMBER: _ClassVar[int]
    FILE_SET_SPEC_TYPE_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FORMAT_FIELD_NUMBER: _ClassVar[int]
    MAX_BAD_RECORDS_FIELD_NUMBER: _ClassVar[int]
    AUTODETECT_FIELD_NUMBER: _ClassVar[int]
    IGNORE_UNKNOWN_VALUES_FIELD_NUMBER: _ClassVar[int]
    COMPRESSION_FIELD_NUMBER: _ClassVar[int]
    CSV_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    JSON_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    BIGTABLE_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    GOOGLE_SHEETS_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    HIVE_PARTITIONING_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
    DECIMAL_TARGET_TYPES_FIELD_NUMBER: _ClassVar[int]
    AVRO_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    JSON_EXTENSION_FIELD_NUMBER: _ClassVar[int]
    PARQUET_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    OBJECT_METADATA_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_FILE_SCHEMA_URI_FIELD_NUMBER: _ClassVar[int]
    METADATA_CACHE_MODE_FIELD_NUMBER: _ClassVar[int]
    source_uris: _containers.RepeatedScalarFieldContainer[str]
    file_set_spec_type: _file_set_specification_type_pb2.FileSetSpecType
    schema: _table_schema_pb2.TableSchema
    source_format: str
    max_bad_records: _wrappers_pb2.Int32Value
    autodetect: _wrappers_pb2.BoolValue
    ignore_unknown_values: _wrappers_pb2.BoolValue
    compression: str
    csv_options: CsvOptions
    json_options: JsonOptions
    bigtable_options: BigtableOptions
    google_sheets_options: GoogleSheetsOptions
    hive_partitioning_options: _hive_partitioning_pb2.HivePartitioningOptions
    connection_id: str
    decimal_target_types: _containers.RepeatedScalarFieldContainer[_decimal_target_types_pb2.DecimalTargetType]
    avro_options: AvroOptions
    json_extension: _json_extension_pb2.JsonExtension
    parquet_options: ParquetOptions
    object_metadata: ExternalDataConfiguration.ObjectMetadata
    reference_file_schema_uri: _wrappers_pb2.StringValue
    metadata_cache_mode: ExternalDataConfiguration.MetadataCacheMode
    def __init__(self, source_uris: _Optional[_Iterable[str]] = ..., file_set_spec_type: _Optional[_Union[_file_set_specification_type_pb2.FileSetSpecType, str]] = ..., schema: _Optional[_Union[_table_schema_pb2.TableSchema, _Mapping]] = ..., source_format: _Optional[str] = ..., max_bad_records: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., autodetect: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., ignore_unknown_values: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., compression: _Optional[str] = ..., csv_options: _Optional[_Union[CsvOptions, _Mapping]] = ..., json_options: _Optional[_Union[JsonOptions, _Mapping]] = ..., bigtable_options: _Optional[_Union[BigtableOptions, _Mapping]] = ..., google_sheets_options: _Optional[_Union[GoogleSheetsOptions, _Mapping]] = ..., hive_partitioning_options: _Optional[_Union[_hive_partitioning_pb2.HivePartitioningOptions, _Mapping]] = ..., connection_id: _Optional[str] = ..., decimal_target_types: _Optional[_Iterable[_Union[_decimal_target_types_pb2.DecimalTargetType, str]]] = ..., avro_options: _Optional[_Union[AvroOptions, _Mapping]] = ..., json_extension: _Optional[_Union[_json_extension_pb2.JsonExtension, str]] = ..., parquet_options: _Optional[_Union[ParquetOptions, _Mapping]] = ..., object_metadata: _Optional[_Union[ExternalDataConfiguration.ObjectMetadata, str]] = ..., reference_file_schema_uri: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., metadata_cache_mode: _Optional[_Union[ExternalDataConfiguration.MetadataCacheMode, str]] = ...) -> None: ...
