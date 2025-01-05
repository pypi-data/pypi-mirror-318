"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/actions/sdk/v2/conversation/prompt/content/link.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n<google/actions/sdk/v2/conversation/prompt/content/link.proto\x12"google.actions.sdk.v2.conversation"O\n\x04Link\x12\x0c\n\x04name\x18\x01 \x01(\t\x129\n\x04open\x18\x02 \x01(\x0b2+.google.actions.sdk.v2.conversation.OpenUrl"Q\n\x07OpenUrl\x12\x0b\n\x03url\x18\x01 \x01(\t\x129\n\x04hint\x18\x02 \x01(\x0e2+.google.actions.sdk.v2.conversation.UrlHint*(\n\x07UrlHint\x12\x14\n\x10LINK_UNSPECIFIED\x10\x00\x12\x07\n\x03AMP\x10\x01B\x85\x01\n&com.google.actions.sdk.v2.conversationB\tLinkProtoP\x01ZNgoogle.golang.org/genproto/googleapis/actions/sdk/v2/conversation;conversationb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.actions.sdk.v2.conversation.prompt.content.link_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.actions.sdk.v2.conversationB\tLinkProtoP\x01ZNgoogle.golang.org/genproto/googleapis/actions/sdk/v2/conversation;conversation'
    _globals['_URLHINT']._serialized_start = 264
    _globals['_URLHINT']._serialized_end = 304
    _globals['_LINK']._serialized_start = 100
    _globals['_LINK']._serialized_end = 179
    _globals['_OPENURL']._serialized_start = 181
    _globals['_OPENURL']._serialized_end = 262