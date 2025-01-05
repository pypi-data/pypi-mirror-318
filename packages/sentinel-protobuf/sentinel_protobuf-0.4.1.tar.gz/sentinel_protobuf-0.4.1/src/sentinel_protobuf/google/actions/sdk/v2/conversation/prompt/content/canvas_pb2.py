"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/actions/sdk/v2/conversation/prompt/content/canvas.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n>google/actions/sdk/v2/conversation/prompt/content/canvas.proto\x12"google.actions.sdk.v2.conversation\x1a\x1cgoogle/protobuf/struct.proto"m\n\x06Canvas\x12\x0b\n\x03url\x18\x01 \x01(\t\x12$\n\x04data\x18\x04 \x03(\x0b2\x16.google.protobuf.Value\x12\x14\n\x0csuppress_mic\x18\x03 \x01(\x08\x12\x1a\n\x12enable_full_screen\x18\x08 \x01(\x08B\x87\x01\n&com.google.actions.sdk.v2.conversationB\x0bCanvasProtoP\x01ZNgoogle.golang.org/genproto/googleapis/actions/sdk/v2/conversation;conversationb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.actions.sdk.v2.conversation.prompt.content.canvas_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.actions.sdk.v2.conversationB\x0bCanvasProtoP\x01ZNgoogle.golang.org/genproto/googleapis/actions/sdk/v2/conversation;conversation'
    _globals['_CANVAS']._serialized_start = 132
    _globals['_CANVAS']._serialized_end = 241