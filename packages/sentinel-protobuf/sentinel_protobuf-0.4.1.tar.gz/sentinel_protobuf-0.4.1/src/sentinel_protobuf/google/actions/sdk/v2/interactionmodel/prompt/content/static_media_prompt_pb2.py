"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/actions/sdk/v2/interactionmodel/prompt/content/static_media_prompt.proto')
_sym_db = _symbol_database.Default()
from ........google.actions.sdk.v2.interactionmodel.prompt.content import static_image_prompt_pb2 as google_dot_actions_dot_sdk_dot_v2_dot_interactionmodel_dot_prompt_dot_content_dot_static__image__prompt__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nOgoogle/actions/sdk/v2/interactionmodel/prompt/content/static_media_prompt.proto\x12-google.actions.sdk.v2.interactionmodel.prompt\x1aOgoogle/actions/sdk/v2/interactionmodel/prompt/content/static_image_prompt.proto\x1a\x1egoogle/protobuf/duration.proto"\xb4\x05\n\x11StaticMediaPrompt\x12^\n\nmedia_type\x18\x08 \x01(\x0e2J.google.actions.sdk.v2.interactionmodel.prompt.StaticMediaPrompt.MediaType\x12/\n\x0cstart_offset\x18\x05 \x01(\x0b2\x19.google.protobuf.Duration\x12w\n\x17optional_media_controls\x18\x06 \x03(\x0e2V.google.actions.sdk.v2.interactionmodel.prompt.StaticMediaPrompt.OptionalMediaControls\x12Q\n\rmedia_objects\x18\x07 \x03(\x0b2:.google.actions.sdk.v2.interactionmodel.prompt.MediaObject\x12`\n\x0brepeat_mode\x18\t \x01(\x0e2K.google.actions.sdk.v2.interactionmodel.prompt.StaticMediaPrompt.RepeatMode"H\n\tMediaType\x12\x1a\n\x16MEDIA_TYPE_UNSPECIFIED\x10\x00\x12\t\n\x05AUDIO\x10\x01\x12\x14\n\x10MEDIA_STATUS_ACK\x10\x02"Y\n\x15OptionalMediaControls\x12\'\n#OPTIONAL_MEDIA_CONTROLS_UNSPECIFIED\x10\x00\x12\n\n\x06PAUSED\x10\x01\x12\x0b\n\x07STOPPED\x10\x02";\n\nRepeatMode\x12\x1b\n\x17REPEAT_MODE_UNSPECIFIED\x10\x00\x12\x07\n\x03OFF\x10\x01\x12\x07\n\x03ALL\x10\x02"\x87\x01\n\x0bMediaObject\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0bdescription\x18\x02 \x01(\t\x12\x0b\n\x03url\x18\x03 \x01(\t\x12H\n\x05image\x18\x04 \x01(\x0b29.google.actions.sdk.v2.interactionmodel.prompt.MediaImage"\xba\x01\n\nMediaImage\x12Q\n\x05large\x18\x01 \x01(\x0b2@.google.actions.sdk.v2.interactionmodel.prompt.StaticImagePromptH\x00\x12P\n\x04icon\x18\x02 \x01(\x0b2@.google.actions.sdk.v2.interactionmodel.prompt.StaticImagePromptH\x00B\x07\n\x05imageB\xa2\x01\n1com.google.actions.sdk.v2.interactionmodel.promptB\x16StaticMediaPromptProtoP\x01ZSgoogle.golang.org/genproto/googleapis/actions/sdk/v2/interactionmodel/prompt;promptb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.actions.sdk.v2.interactionmodel.prompt.content.static_media_prompt_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n1com.google.actions.sdk.v2.interactionmodel.promptB\x16StaticMediaPromptProtoP\x01ZSgoogle.golang.org/genproto/googleapis/actions/sdk/v2/interactionmodel/prompt;prompt'
    _globals['_STATICMEDIAPROMPT']._serialized_start = 244
    _globals['_STATICMEDIAPROMPT']._serialized_end = 936
    _globals['_STATICMEDIAPROMPT_MEDIATYPE']._serialized_start = 712
    _globals['_STATICMEDIAPROMPT_MEDIATYPE']._serialized_end = 784
    _globals['_STATICMEDIAPROMPT_OPTIONALMEDIACONTROLS']._serialized_start = 786
    _globals['_STATICMEDIAPROMPT_OPTIONALMEDIACONTROLS']._serialized_end = 875
    _globals['_STATICMEDIAPROMPT_REPEATMODE']._serialized_start = 877
    _globals['_STATICMEDIAPROMPT_REPEATMODE']._serialized_end = 936
    _globals['_MEDIAOBJECT']._serialized_start = 939
    _globals['_MEDIAOBJECT']._serialized_end = 1074
    _globals['_MEDIAIMAGE']._serialized_start = 1077
    _globals['_MEDIAIMAGE']._serialized_end = 1263