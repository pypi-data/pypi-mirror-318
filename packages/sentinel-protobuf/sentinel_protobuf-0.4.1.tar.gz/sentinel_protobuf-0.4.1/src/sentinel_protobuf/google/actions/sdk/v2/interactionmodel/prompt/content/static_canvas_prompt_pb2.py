"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/actions/sdk/v2/interactionmodel/prompt/content/static_canvas_prompt.proto')
_sym_db = _symbol_database.Default()
from ........google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nPgoogle/actions/sdk/v2/interactionmodel/prompt/content/static_canvas_prompt.proto\x12-google.actions.sdk.v2.interactionmodel.prompt\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1cgoogle/protobuf/struct.proto"\xb9\x01\n\x12StaticCanvasPrompt\x12\x10\n\x03url\x18\x01 \x01(\tB\x03\xe0A\x02\x12)\n\x04data\x18\x02 \x03(\x0b2\x16.google.protobuf.ValueB\x03\xe0A\x01\x12\x19\n\x0csuppress_mic\x18\x03 \x01(\x08B\x03\xe0A\x01\x12*\n\x1dsend_state_data_to_canvas_app\x18\x05 \x01(\x08B\x03\xe0A\x01\x12\x1f\n\x12enable_full_screen\x18\x06 \x01(\x08B\x03\xe0A\x01B\xa3\x01\n1com.google.actions.sdk.v2.interactionmodel.promptB\x17StaticCanvasPromptProtoP\x01ZSgoogle.golang.org/genproto/googleapis/actions/sdk/v2/interactionmodel/prompt;promptb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.actions.sdk.v2.interactionmodel.prompt.content.static_canvas_prompt_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n1com.google.actions.sdk.v2.interactionmodel.promptB\x17StaticCanvasPromptProtoP\x01ZSgoogle.golang.org/genproto/googleapis/actions/sdk/v2/interactionmodel/prompt;prompt'
    _globals['_STATICCANVASPROMPT'].fields_by_name['url']._loaded_options = None
    _globals['_STATICCANVASPROMPT'].fields_by_name['url']._serialized_options = b'\xe0A\x02'
    _globals['_STATICCANVASPROMPT'].fields_by_name['data']._loaded_options = None
    _globals['_STATICCANVASPROMPT'].fields_by_name['data']._serialized_options = b'\xe0A\x01'
    _globals['_STATICCANVASPROMPT'].fields_by_name['suppress_mic']._loaded_options = None
    _globals['_STATICCANVASPROMPT'].fields_by_name['suppress_mic']._serialized_options = b'\xe0A\x01'
    _globals['_STATICCANVASPROMPT'].fields_by_name['send_state_data_to_canvas_app']._loaded_options = None
    _globals['_STATICCANVASPROMPT'].fields_by_name['send_state_data_to_canvas_app']._serialized_options = b'\xe0A\x01'
    _globals['_STATICCANVASPROMPT'].fields_by_name['enable_full_screen']._loaded_options = None
    _globals['_STATICCANVASPROMPT'].fields_by_name['enable_full_screen']._serialized_options = b'\xe0A\x01'
    _globals['_STATICCANVASPROMPT']._serialized_start = 195
    _globals['_STATICCANVASPROMPT']._serialized_end = 380