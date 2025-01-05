"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/actions/sdk/v2/conversation/prompt/content/collection.proto')
_sym_db = _symbol_database.Default()
from ........google.actions.sdk.v2.conversation.prompt.content import image_pb2 as google_dot_actions_dot_sdk_dot_v2_dot_conversation_dot_prompt_dot_content_dot_image__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nBgoogle/actions/sdk/v2/conversation/prompt/content/collection.proto\x12"google.actions.sdk.v2.conversation\x1a=google/actions/sdk/v2/conversation/prompt/content/image.proto"\xe3\x01\n\nCollection\x12\r\n\x05title\x18\x01 \x01(\t\x12\x10\n\x08subtitle\x18\x02 \x01(\t\x12L\n\x05items\x18\x03 \x03(\x0b2=.google.actions.sdk.v2.conversation.Collection.CollectionItem\x12G\n\nimage_fill\x18\x04 \x01(\x0e23.google.actions.sdk.v2.conversation.Image.ImageFill\x1a\x1d\n\x0eCollectionItem\x12\x0b\n\x03key\x18\x01 \x01(\tB\x8b\x01\n&com.google.actions.sdk.v2.conversationB\x0fCollectionProtoP\x01ZNgoogle.golang.org/genproto/googleapis/actions/sdk/v2/conversation;conversationb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.actions.sdk.v2.conversation.prompt.content.collection_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.actions.sdk.v2.conversationB\x0fCollectionProtoP\x01ZNgoogle.golang.org/genproto/googleapis/actions/sdk/v2/conversation;conversation'
    _globals['_COLLECTION']._serialized_start = 170
    _globals['_COLLECTION']._serialized_end = 397
    _globals['_COLLECTION_COLLECTIONITEM']._serialized_start = 368
    _globals['_COLLECTION_COLLECTIONITEM']._serialized_end = 397