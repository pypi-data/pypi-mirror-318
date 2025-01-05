"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/bigquery/v2/error.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$google/cloud/bigquery/v2/error.proto\x12\x18google.cloud.bigquery.v2"S\n\nErrorProto\x12\x0e\n\x06reason\x18\x01 \x01(\t\x12\x10\n\x08location\x18\x02 \x01(\t\x12\x12\n\ndebug_info\x18\x03 \x01(\t\x12\x0f\n\x07message\x18\x04 \x01(\tBX\n\x1ccom.google.cloud.bigquery.v2Z8cloud.google.com/go/bigquery/apiv2/bigquerypb;bigquerypbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.bigquery.v2.error_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ccom.google.cloud.bigquery.v2Z8cloud.google.com/go/bigquery/apiv2/bigquerypb;bigquerypb'
    _globals['_ERRORPROTO']._serialized_start = 66
    _globals['_ERRORPROTO']._serialized_end = 149