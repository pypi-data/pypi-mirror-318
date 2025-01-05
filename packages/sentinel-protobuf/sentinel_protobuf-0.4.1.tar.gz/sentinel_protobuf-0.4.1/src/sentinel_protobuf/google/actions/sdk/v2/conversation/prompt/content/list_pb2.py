"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/actions/sdk/v2/conversation/prompt/content/list.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n<google/actions/sdk/v2/conversation/prompt/content/list.proto\x12"google.actions.sdk.v2.conversation"\x82\x01\n\x04List\x12\r\n\x05title\x18\x01 \x01(\t\x12\x10\n\x08subtitle\x18\x02 \x01(\t\x12@\n\x05items\x18\x03 \x03(\x0b21.google.actions.sdk.v2.conversation.List.ListItem\x1a\x17\n\x08ListItem\x12\x0b\n\x03key\x18\x01 \x01(\tB\x85\x01\n&com.google.actions.sdk.v2.conversationB\tListProtoP\x01ZNgoogle.golang.org/genproto/googleapis/actions/sdk/v2/conversation;conversationb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.actions.sdk.v2.conversation.prompt.content.list_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.actions.sdk.v2.conversationB\tListProtoP\x01ZNgoogle.golang.org/genproto/googleapis/actions/sdk/v2/conversation;conversation'
    _globals['_LIST']._serialized_start = 101
    _globals['_LIST']._serialized_end = 231
    _globals['_LIST_LISTITEM']._serialized_start = 208
    _globals['_LIST_LISTITEM']._serialized_end = 231