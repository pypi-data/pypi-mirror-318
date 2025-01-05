"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/bigquery/v2/time_partitioning.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0google/cloud/bigquery/v2/time_partitioning.proto\x12\x18google.cloud.bigquery.v2\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1egoogle/protobuf/wrappers.proto"\x90\x01\n\x10TimePartitioning\x12\x11\n\x04type\x18\x01 \x01(\tB\x03\xe0A\x02\x127\n\rexpiration_ms\x18\x02 \x01(\x0b2\x1b.google.protobuf.Int64ValueB\x03\xe0A\x01\x120\n\x05field\x18\x03 \x01(\x0b2\x1c.google.protobuf.StringValueB\x03\xe0A\x01Bo\n\x1ccom.google.cloud.bigquery.v2B\x15TimePartitioningProtoZ8cloud.google.com/go/bigquery/apiv2/bigquerypb;bigquerypbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.bigquery.v2.time_partitioning_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ccom.google.cloud.bigquery.v2B\x15TimePartitioningProtoZ8cloud.google.com/go/bigquery/apiv2/bigquerypb;bigquerypb'
    _globals['_TIMEPARTITIONING'].fields_by_name['type']._loaded_options = None
    _globals['_TIMEPARTITIONING'].fields_by_name['type']._serialized_options = b'\xe0A\x02'
    _globals['_TIMEPARTITIONING'].fields_by_name['expiration_ms']._loaded_options = None
    _globals['_TIMEPARTITIONING'].fields_by_name['expiration_ms']._serialized_options = b'\xe0A\x01'
    _globals['_TIMEPARTITIONING'].fields_by_name['field']._loaded_options = None
    _globals['_TIMEPARTITIONING'].fields_by_name['field']._serialized_options = b'\xe0A\x01'
    _globals['_TIMEPARTITIONING']._serialized_start = 144
    _globals['_TIMEPARTITIONING']._serialized_end = 288