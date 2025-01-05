"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/api/control.proto')
_sym_db = _symbol_database.Default()
from ...google.api import policy_pb2 as google_dot_api_dot_policy__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18google/api/control.proto\x12\ngoogle.api\x1a\x17google/api/policy.proto"Q\n\x07Control\x12\x13\n\x0benvironment\x18\x01 \x01(\t\x121\n\x0fmethod_policies\x18\x04 \x03(\x0b2\x18.google.api.MethodPolicyBn\n\x0ecom.google.apiB\x0cControlProtoP\x01ZEgoogle.golang.org/genproto/googleapis/api/serviceconfig;serviceconfig\xa2\x02\x04GAPIb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.api.control_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x0ecom.google.apiB\x0cControlProtoP\x01ZEgoogle.golang.org/genproto/googleapis/api/serviceconfig;serviceconfig\xa2\x02\x04GAPI'
    _globals['_CONTROL']._serialized_start = 65
    _globals['_CONTROL']._serialized_end = 146