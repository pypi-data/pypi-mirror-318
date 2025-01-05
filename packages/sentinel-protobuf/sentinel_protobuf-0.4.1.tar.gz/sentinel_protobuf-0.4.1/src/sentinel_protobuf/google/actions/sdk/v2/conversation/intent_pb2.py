"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/actions/sdk/v2/conversation/intent.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/google/actions/sdk/v2/conversation/intent.proto\x12"google.actions.sdk.v2.conversation\x1a\x1cgoogle/protobuf/struct.proto"\xd6\x01\n\x06Intent\x12\x0c\n\x04name\x18\x01 \x01(\t\x12F\n\x06params\x18\x02 \x03(\x0b26.google.actions.sdk.v2.conversation.Intent.ParamsEntry\x12\r\n\x05query\x18\x03 \x01(\t\x1ag\n\x0bParamsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12G\n\x05value\x18\x02 \x01(\x0b28.google.actions.sdk.v2.conversation.IntentParameterValue:\x028\x01"R\n\x14IntentParameterValue\x12\x10\n\x08original\x18\x01 \x01(\t\x12(\n\x08resolved\x18\x02 \x01(\x0b2\x16.google.protobuf.ValueB\x87\x01\n&com.google.actions.sdk.v2.conversationB\x0bIntentProtoP\x01ZNgoogle.golang.org/genproto/googleapis/actions/sdk/v2/conversation;conversationb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.actions.sdk.v2.conversation.intent_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.actions.sdk.v2.conversationB\x0bIntentProtoP\x01ZNgoogle.golang.org/genproto/googleapis/actions/sdk/v2/conversation;conversation'
    _globals['_INTENT_PARAMSENTRY']._loaded_options = None
    _globals['_INTENT_PARAMSENTRY']._serialized_options = b'8\x01'
    _globals['_INTENT']._serialized_start = 118
    _globals['_INTENT']._serialized_end = 332
    _globals['_INTENT_PARAMSENTRY']._serialized_start = 229
    _globals['_INTENT_PARAMSENTRY']._serialized_end = 332
    _globals['_INTENTPARAMETERVALUE']._serialized_start = 334
    _globals['_INTENTPARAMETERVALUE']._serialized_end = 416