"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/bigquery/v2/biglake_config.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-google/cloud/bigquery/v2/biglake_config.proto\x12\x18google.cloud.bigquery.v2\x1a\x1fgoogle/api/field_behavior.proto"\xea\x02\n\x14BigLakeConfiguration\x12\x1a\n\rconnection_id\x18\x01 \x01(\tB\x03\xe0A\x01\x12\x18\n\x0bstorage_uri\x18\x02 \x01(\tB\x03\xe0A\x01\x12S\n\x0bfile_format\x18\x03 \x01(\x0e29.google.cloud.bigquery.v2.BigLakeConfiguration.FileFormatB\x03\xe0A\x01\x12U\n\x0ctable_format\x18\x04 \x01(\x0e2:.google.cloud.bigquery.v2.BigLakeConfiguration.TableFormatB\x03\xe0A\x01"6\n\nFileFormat\x12\x1b\n\x17FILE_FORMAT_UNSPECIFIED\x10\x00\x12\x0b\n\x07PARQUET\x10\x01"8\n\x0bTableFormat\x12\x1c\n\x18TABLE_FORMAT_UNSPECIFIED\x10\x00\x12\x0b\n\x07ICEBERG\x10\x01Bn\n\x1ccom.google.cloud.bigquery.v2B\x12BigLakeConfigProtoP\x01Z8cloud.google.com/go/bigquery/apiv2/bigquerypb;bigquerypbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.bigquery.v2.biglake_config_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ccom.google.cloud.bigquery.v2B\x12BigLakeConfigProtoP\x01Z8cloud.google.com/go/bigquery/apiv2/bigquerypb;bigquerypb'
    _globals['_BIGLAKECONFIGURATION'].fields_by_name['connection_id']._loaded_options = None
    _globals['_BIGLAKECONFIGURATION'].fields_by_name['connection_id']._serialized_options = b'\xe0A\x01'
    _globals['_BIGLAKECONFIGURATION'].fields_by_name['storage_uri']._loaded_options = None
    _globals['_BIGLAKECONFIGURATION'].fields_by_name['storage_uri']._serialized_options = b'\xe0A\x01'
    _globals['_BIGLAKECONFIGURATION'].fields_by_name['file_format']._loaded_options = None
    _globals['_BIGLAKECONFIGURATION'].fields_by_name['file_format']._serialized_options = b'\xe0A\x01'
    _globals['_BIGLAKECONFIGURATION'].fields_by_name['table_format']._loaded_options = None
    _globals['_BIGLAKECONFIGURATION'].fields_by_name['table_format']._serialized_options = b'\xe0A\x01'
    _globals['_BIGLAKECONFIGURATION']._serialized_start = 109
    _globals['_BIGLAKECONFIGURATION']._serialized_end = 471
    _globals['_BIGLAKECONFIGURATION_FILEFORMAT']._serialized_start = 359
    _globals['_BIGLAKECONFIGURATION_FILEFORMAT']._serialized_end = 413
    _globals['_BIGLAKECONFIGURATION_TABLEFORMAT']._serialized_start = 415
    _globals['_BIGLAKECONFIGURATION_TABLEFORMAT']._serialized_end = 471