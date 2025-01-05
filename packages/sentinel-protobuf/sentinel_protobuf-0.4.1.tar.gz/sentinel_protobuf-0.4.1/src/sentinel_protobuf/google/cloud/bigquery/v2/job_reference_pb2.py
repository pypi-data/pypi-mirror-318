"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/bigquery/v2/job_reference.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,google/cloud/bigquery/v2/job_reference.proto\x12\x18google.cloud.bigquery.v2\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1egoogle/protobuf/wrappers.proto"\x8f\x01\n\x0cJobReference\x12\x17\n\nproject_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x13\n\x06job_id\x18\x02 \x01(\tB\x03\xe0A\x02\x123\n\x08location\x18\x03 \x01(\x0b2\x1c.google.protobuf.StringValueB\x03\xe0A\x01\x12\x1c\n\x14location_alternative\x18\x05 \x03(\tBk\n\x1ccom.google.cloud.bigquery.v2B\x11JobReferenceProtoZ8cloud.google.com/go/bigquery/apiv2/bigquerypb;bigquerypbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.bigquery.v2.job_reference_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ccom.google.cloud.bigquery.v2B\x11JobReferenceProtoZ8cloud.google.com/go/bigquery/apiv2/bigquerypb;bigquerypb'
    _globals['_JOBREFERENCE'].fields_by_name['project_id']._loaded_options = None
    _globals['_JOBREFERENCE'].fields_by_name['project_id']._serialized_options = b'\xe0A\x02'
    _globals['_JOBREFERENCE'].fields_by_name['job_id']._loaded_options = None
    _globals['_JOBREFERENCE'].fields_by_name['job_id']._serialized_options = b'\xe0A\x02'
    _globals['_JOBREFERENCE'].fields_by_name['location']._loaded_options = None
    _globals['_JOBREFERENCE'].fields_by_name['location']._serialized_options = b'\xe0A\x01'
    _globals['_JOBREFERENCE']._serialized_start = 140
    _globals['_JOBREFERENCE']._serialized_end = 283