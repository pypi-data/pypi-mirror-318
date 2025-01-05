"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/support/v2/escalation.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(google/cloud/support/v2/escalation.proto\x12\x17google.cloud.support.v2\x1a\x1fgoogle/api/field_behavior.proto"\xce\x01\n\nEscalation\x12?\n\x06reason\x18\x04 \x01(\x0e2*.google.cloud.support.v2.Escalation.ReasonB\x03\xe0A\x02\x12\x1a\n\rjustification\x18\x05 \x01(\tB\x03\xe0A\x02"c\n\x06Reason\x12\x16\n\x12REASON_UNSPECIFIED\x10\x00\x12\x13\n\x0fRESOLUTION_TIME\x10\x01\x12\x17\n\x13TECHNICAL_EXPERTISE\x10\x02\x12\x13\n\x0fBUSINESS_IMPACT\x10\x03B\xb8\x01\n\x1bcom.google.cloud.support.v2B\x0fEscalationProtoP\x01Z5cloud.google.com/go/support/apiv2/supportpb;supportpb\xaa\x02\x17Google.Cloud.Support.V2\xca\x02\x17Google\\Cloud\\Support\\V2\xea\x02\x1aGoogle::Cloud::Support::V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.support.v2.escalation_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1bcom.google.cloud.support.v2B\x0fEscalationProtoP\x01Z5cloud.google.com/go/support/apiv2/supportpb;supportpb\xaa\x02\x17Google.Cloud.Support.V2\xca\x02\x17Google\\Cloud\\Support\\V2\xea\x02\x1aGoogle::Cloud::Support::V2'
    _globals['_ESCALATION'].fields_by_name['reason']._loaded_options = None
    _globals['_ESCALATION'].fields_by_name['reason']._serialized_options = b'\xe0A\x02'
    _globals['_ESCALATION'].fields_by_name['justification']._loaded_options = None
    _globals['_ESCALATION'].fields_by_name['justification']._serialized_options = b'\xe0A\x02'
    _globals['_ESCALATION']._serialized_start = 103
    _globals['_ESCALATION']._serialized_end = 309
    _globals['_ESCALATION_REASON']._serialized_start = 210
    _globals['_ESCALATION_REASON']._serialized_end = 309