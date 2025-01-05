"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/bigquery/v2/system_variable.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.cloud.bigquery.v2 import standard_sql_pb2 as google_dot_cloud_dot_bigquery_dot_v2_dot_standard__sql__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.google/cloud/bigquery/v2/system_variable.proto\x12\x18google.cloud.bigquery.v2\x1a\x1fgoogle/api/field_behavior.proto\x1a+google/cloud/bigquery/v2/standard_sql.proto\x1a\x1cgoogle/protobuf/struct.proto"\xe6\x01\n\x0fSystemVariables\x12H\n\x05types\x18\x01 \x03(\x0b24.google.cloud.bigquery.v2.SystemVariables.TypesEntryB\x03\xe0A\x03\x12,\n\x06values\x18\x02 \x01(\x0b2\x17.google.protobuf.StructB\x03\xe0A\x03\x1a[\n\nTypesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12<\n\x05value\x18\x02 \x01(\x0b2-.google.cloud.bigquery.v2.StandardSqlDataType:\x028\x01Bo\n\x1ccom.google.cloud.bigquery.v2B\x13SystemVariableProtoP\x01Z8cloud.google.com/go/bigquery/apiv2/bigquerypb;bigquerypbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.bigquery.v2.system_variable_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ccom.google.cloud.bigquery.v2B\x13SystemVariableProtoP\x01Z8cloud.google.com/go/bigquery/apiv2/bigquerypb;bigquerypb'
    _globals['_SYSTEMVARIABLES_TYPESENTRY']._loaded_options = None
    _globals['_SYSTEMVARIABLES_TYPESENTRY']._serialized_options = b'8\x01'
    _globals['_SYSTEMVARIABLES'].fields_by_name['types']._loaded_options = None
    _globals['_SYSTEMVARIABLES'].fields_by_name['types']._serialized_options = b'\xe0A\x03'
    _globals['_SYSTEMVARIABLES'].fields_by_name['values']._loaded_options = None
    _globals['_SYSTEMVARIABLES'].fields_by_name['values']._serialized_options = b'\xe0A\x03'
    _globals['_SYSTEMVARIABLES']._serialized_start = 185
    _globals['_SYSTEMVARIABLES']._serialized_end = 415
    _globals['_SYSTEMVARIABLES_TYPESENTRY']._serialized_start = 324
    _globals['_SYSTEMVARIABLES_TYPESENTRY']._serialized_end = 415