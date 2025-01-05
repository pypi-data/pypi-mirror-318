"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/api/context.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18google/api/context.proto\x12\ngoogle.api"1\n\x07Context\x12&\n\x05rules\x18\x01 \x03(\x0b2\x17.google.api.ContextRule"\x8d\x01\n\x0bContextRule\x12\x10\n\x08selector\x18\x01 \x01(\t\x12\x11\n\trequested\x18\x02 \x03(\t\x12\x10\n\x08provided\x18\x03 \x03(\t\x12"\n\x1aallowed_request_extensions\x18\x04 \x03(\t\x12#\n\x1ballowed_response_extensions\x18\x05 \x03(\tBn\n\x0ecom.google.apiB\x0cContextProtoP\x01ZEgoogle.golang.org/genproto/googleapis/api/serviceconfig;serviceconfig\xa2\x02\x04GAPIb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.api.context_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x0ecom.google.apiB\x0cContextProtoP\x01ZEgoogle.golang.org/genproto/googleapis/api/serviceconfig;serviceconfig\xa2\x02\x04GAPI'
    _globals['_CONTEXT']._serialized_start = 40
    _globals['_CONTEXT']._serialized_end = 89
    _globals['_CONTEXTRULE']._serialized_start = 92
    _globals['_CONTEXTRULE']._serialized_end = 233