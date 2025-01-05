"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/actions/sdk/v2/conversation/prompt/content/card.proto')
_sym_db = _symbol_database.Default()
from ........google.actions.sdk.v2.conversation.prompt.content import image_pb2 as google_dot_actions_dot_sdk_dot_v2_dot_conversation_dot_prompt_dot_content_dot_image__pb2
from ........google.actions.sdk.v2.conversation.prompt.content import link_pb2 as google_dot_actions_dot_sdk_dot_v2_dot_conversation_dot_prompt_dot_content_dot_link__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n<google/actions/sdk/v2/conversation/prompt/content/card.proto\x12"google.actions.sdk.v2.conversation\x1a=google/actions/sdk/v2/conversation/prompt/content/image.proto\x1a<google/actions/sdk/v2/conversation/prompt/content/link.proto"\xf2\x01\n\x04Card\x12\r\n\x05title\x18\x01 \x01(\t\x12\x10\n\x08subtitle\x18\x02 \x01(\t\x12\x0c\n\x04text\x18\x03 \x01(\t\x128\n\x05image\x18\x04 \x01(\x0b2).google.actions.sdk.v2.conversation.Image\x12G\n\nimage_fill\x18\x05 \x01(\x0e23.google.actions.sdk.v2.conversation.Image.ImageFill\x128\n\x06button\x18\x06 \x01(\x0b2(.google.actions.sdk.v2.conversation.LinkB\x85\x01\n&com.google.actions.sdk.v2.conversationB\tCardProtoP\x01ZNgoogle.golang.org/genproto/googleapis/actions/sdk/v2/conversation;conversationb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.actions.sdk.v2.conversation.prompt.content.card_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.actions.sdk.v2.conversationB\tCardProtoP\x01ZNgoogle.golang.org/genproto/googleapis/actions/sdk/v2/conversation;conversation'
    _globals['_CARD']._serialized_start = 226
    _globals['_CARD']._serialized_end = 468