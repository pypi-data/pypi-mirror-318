"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/chat/v1/action_status.proto')
_sym_db = _symbol_database.Default()
from ....google.rpc import code_pb2 as google_dot_rpc_dot_code__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n"google/chat/v1/action_status.proto\x12\x0egoogle.chat.v1\x1a\x15google/rpc/code.proto"R\n\x0cActionStatus\x12%\n\x0bstatus_code\x18\x01 \x01(\x0e2\x10.google.rpc.Code\x12\x1b\n\x13user_facing_message\x18\x02 \x01(\tB\xaa\x01\n\x12com.google.chat.v1B\x11ActionStatusProtoP\x01Z,cloud.google.com/go/chat/apiv1/chatpb;chatpb\xa2\x02\x0bDYNAPIProto\xaa\x02\x13Google.Apps.Chat.V1\xca\x02\x13Google\\Apps\\Chat\\V1\xea\x02\x16Google::Apps::Chat::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.chat.v1.action_status_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x12com.google.chat.v1B\x11ActionStatusProtoP\x01Z,cloud.google.com/go/chat/apiv1/chatpb;chatpb\xa2\x02\x0bDYNAPIProto\xaa\x02\x13Google.Apps.Chat.V1\xca\x02\x13Google\\Apps\\Chat\\V1\xea\x02\x16Google::Apps::Chat::V1'
    _globals['_ACTIONSTATUS']._serialized_start = 77
    _globals['_ACTIONSTATUS']._serialized_end = 159