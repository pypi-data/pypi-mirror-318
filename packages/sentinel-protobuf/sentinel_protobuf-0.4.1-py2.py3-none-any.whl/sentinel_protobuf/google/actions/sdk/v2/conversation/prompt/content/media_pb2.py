"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/actions/sdk/v2/conversation/prompt/content/media.proto')
_sym_db = _symbol_database.Default()
from ........google.actions.sdk.v2.conversation.prompt.content import image_pb2 as google_dot_actions_dot_sdk_dot_v2_dot_conversation_dot_prompt_dot_content_dot_image__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n=google/actions/sdk/v2/conversation/prompt/content/media.proto\x12"google.actions.sdk.v2.conversation\x1a=google/actions/sdk/v2/conversation/prompt/content/image.proto\x1a\x1egoogle/protobuf/duration.proto"\xd0\x03\n\x05Media\x12G\n\nmedia_type\x18\x08 \x01(\x0e23.google.actions.sdk.v2.conversation.Media.MediaType\x12/\n\x0cstart_offset\x18\x05 \x01(\x0b2\x19.google.protobuf.Duration\x12`\n\x17optional_media_controls\x18\x06 \x03(\x0e2?.google.actions.sdk.v2.conversation.Media.OptionalMediaControls\x12F\n\rmedia_objects\x18\x07 \x03(\x0b2/.google.actions.sdk.v2.conversation.MediaObject"H\n\tMediaType\x12\x1a\n\x16MEDIA_TYPE_UNSPECIFIED\x10\x00\x12\t\n\x05AUDIO\x10\x01\x12\x14\n\x10MEDIA_STATUS_ACK\x10\x02"Y\n\x15OptionalMediaControls\x12\'\n#OPTIONAL_MEDIA_CONTROLS_UNSPECIFIED\x10\x00\x12\n\n\x06PAUSED\x10\x01\x12\x0b\n\x07STOPPED\x10\x02"|\n\x0bMediaObject\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0bdescription\x18\x02 \x01(\t\x12\x0b\n\x03url\x18\x03 \x01(\t\x12=\n\x05image\x18\x04 \x01(\x0b2..google.actions.sdk.v2.conversation.MediaImage"\x8c\x01\n\nMediaImage\x12:\n\x05large\x18\x01 \x01(\x0b2).google.actions.sdk.v2.conversation.ImageH\x00\x129\n\x04icon\x18\x02 \x01(\x0b2).google.actions.sdk.v2.conversation.ImageH\x00B\x07\n\x05imageB\x86\x01\n&com.google.actions.sdk.v2.conversationB\nMediaProtoP\x01ZNgoogle.golang.org/genproto/googleapis/actions/sdk/v2/conversation;conversationb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.actions.sdk.v2.conversation.prompt.content.media_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.actions.sdk.v2.conversationB\nMediaProtoP\x01ZNgoogle.golang.org/genproto/googleapis/actions/sdk/v2/conversation;conversation'
    _globals['_MEDIA']._serialized_start = 197
    _globals['_MEDIA']._serialized_end = 661
    _globals['_MEDIA_MEDIATYPE']._serialized_start = 498
    _globals['_MEDIA_MEDIATYPE']._serialized_end = 570
    _globals['_MEDIA_OPTIONALMEDIACONTROLS']._serialized_start = 572
    _globals['_MEDIA_OPTIONALMEDIACONTROLS']._serialized_end = 661
    _globals['_MEDIAOBJECT']._serialized_start = 663
    _globals['_MEDIAOBJECT']._serialized_end = 787
    _globals['_MEDIAIMAGE']._serialized_start = 790
    _globals['_MEDIAIMAGE']._serialized_end = 930