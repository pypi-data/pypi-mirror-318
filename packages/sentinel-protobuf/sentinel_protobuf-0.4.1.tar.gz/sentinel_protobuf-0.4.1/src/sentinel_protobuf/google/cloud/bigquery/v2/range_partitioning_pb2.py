"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/bigquery/v2/range_partitioning.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1google/cloud/bigquery/v2/range_partitioning.proto\x12\x18google.cloud.bigquery.v2\x1a\x1fgoogle/api/field_behavior.proto"\xaf\x01\n\x11RangePartitioning\x12\x12\n\x05field\x18\x01 \x01(\tB\x03\xe0A\x02\x12@\n\x05range\x18\x02 \x01(\x0b21.google.cloud.bigquery.v2.RangePartitioning.Range\x1aD\n\x05Range\x12\x12\n\x05start\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x10\n\x03end\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x15\n\x08interval\x18\x03 \x01(\tB\x03\xe0A\x02Bp\n\x1ccom.google.cloud.bigquery.v2B\x16RangePartitioningProtoZ8cloud.google.com/go/bigquery/apiv2/bigquerypb;bigquerypbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.bigquery.v2.range_partitioning_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ccom.google.cloud.bigquery.v2B\x16RangePartitioningProtoZ8cloud.google.com/go/bigquery/apiv2/bigquerypb;bigquerypb'
    _globals['_RANGEPARTITIONING_RANGE'].fields_by_name['start']._loaded_options = None
    _globals['_RANGEPARTITIONING_RANGE'].fields_by_name['start']._serialized_options = b'\xe0A\x02'
    _globals['_RANGEPARTITIONING_RANGE'].fields_by_name['end']._loaded_options = None
    _globals['_RANGEPARTITIONING_RANGE'].fields_by_name['end']._serialized_options = b'\xe0A\x02'
    _globals['_RANGEPARTITIONING_RANGE'].fields_by_name['interval']._loaded_options = None
    _globals['_RANGEPARTITIONING_RANGE'].fields_by_name['interval']._serialized_options = b'\xe0A\x02'
    _globals['_RANGEPARTITIONING'].fields_by_name['field']._loaded_options = None
    _globals['_RANGEPARTITIONING'].fields_by_name['field']._serialized_options = b'\xe0A\x02'
    _globals['_RANGEPARTITIONING']._serialized_start = 113
    _globals['_RANGEPARTITIONING']._serialized_end = 288
    _globals['_RANGEPARTITIONING_RANGE']._serialized_start = 220
    _globals['_RANGEPARTITIONING_RANGE']._serialized_end = 288