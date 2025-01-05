"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/actions/sdk/v2/interactionmodel/prompt/content/static_image_prompt.proto')
_sym_db = _symbol_database.Default()
from ........google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nOgoogle/actions/sdk/v2/interactionmodel/prompt/content/static_image_prompt.proto\x12-google.actions.sdk.v2.interactionmodel.prompt\x1a\x1fgoogle/api/field_behavior.proto"\xa0\x01\n\x11StaticImagePrompt\x12\x10\n\x03url\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x10\n\x03alt\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x13\n\x06height\x18\x03 \x01(\x05B\x03\xe0A\x01\x12\x12\n\x05width\x18\x04 \x01(\x05B\x03\xe0A\x01">\n\tImageFill\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x08\n\x04GRAY\x10\x01\x12\t\n\x05WHITE\x10\x02\x12\x0b\n\x07CROPPED\x10\x03B\xa2\x01\n1com.google.actions.sdk.v2.interactionmodel.promptB\x16StaticImagePromptProtoP\x01ZSgoogle.golang.org/genproto/googleapis/actions/sdk/v2/interactionmodel/prompt;promptb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.actions.sdk.v2.interactionmodel.prompt.content.static_image_prompt_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n1com.google.actions.sdk.v2.interactionmodel.promptB\x16StaticImagePromptProtoP\x01ZSgoogle.golang.org/genproto/googleapis/actions/sdk/v2/interactionmodel/prompt;prompt'
    _globals['_STATICIMAGEPROMPT'].fields_by_name['url']._loaded_options = None
    _globals['_STATICIMAGEPROMPT'].fields_by_name['url']._serialized_options = b'\xe0A\x02'
    _globals['_STATICIMAGEPROMPT'].fields_by_name['alt']._loaded_options = None
    _globals['_STATICIMAGEPROMPT'].fields_by_name['alt']._serialized_options = b'\xe0A\x02'
    _globals['_STATICIMAGEPROMPT'].fields_by_name['height']._loaded_options = None
    _globals['_STATICIMAGEPROMPT'].fields_by_name['height']._serialized_options = b'\xe0A\x01'
    _globals['_STATICIMAGEPROMPT'].fields_by_name['width']._loaded_options = None
    _globals['_STATICIMAGEPROMPT'].fields_by_name['width']._serialized_options = b'\xe0A\x01'
    _globals['_STATICIMAGEPROMPT']._serialized_start = 164
    _globals['_STATICIMAGEPROMPT']._serialized_end = 324
    _globals['_STATICIMAGEPROMPT_IMAGEFILL']._serialized_start = 262
    _globals['_STATICIMAGEPROMPT_IMAGEFILL']._serialized_end = 324