"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/actions/sdk/v2/interactionmodel/prompt/content/static_table_prompt.proto')
_sym_db = _symbol_database.Default()
from ........google.actions.sdk.v2.interactionmodel.prompt.content import static_image_prompt_pb2 as google_dot_actions_dot_sdk_dot_v2_dot_interactionmodel_dot_prompt_dot_content_dot_static__image__prompt__pb2
from ........google.actions.sdk.v2.interactionmodel.prompt.content import static_link_prompt_pb2 as google_dot_actions_dot_sdk_dot_v2_dot_interactionmodel_dot_prompt_dot_content_dot_static__link__prompt__pb2
from ........google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nOgoogle/actions/sdk/v2/interactionmodel/prompt/content/static_table_prompt.proto\x12-google.actions.sdk.v2.interactionmodel.prompt\x1aOgoogle/actions/sdk/v2/interactionmodel/prompt/content/static_image_prompt.proto\x1aNgoogle/actions/sdk/v2/interactionmodel/prompt/content/static_link_prompt.proto\x1a\x1fgoogle/api/field_behavior.proto"\x88\x03\n\x11StaticTablePrompt\x12\x12\n\x05title\x18\x01 \x01(\tB\x03\xe0A\x01\x12\x15\n\x08subtitle\x18\x02 \x01(\tB\x03\xe0A\x01\x12T\n\x05image\x18\x03 \x01(\x0b2@.google.actions.sdk.v2.interactionmodel.prompt.StaticImagePromptB\x03\xe0A\x01\x12P\n\x07columns\x18\x04 \x03(\x0b2:.google.actions.sdk.v2.interactionmodel.prompt.TableColumnB\x03\xe0A\x01\x12J\n\x04rows\x18\x05 \x03(\x0b27.google.actions.sdk.v2.interactionmodel.prompt.TableRowB\x03\xe0A\x01\x12T\n\x06button\x18\x06 \x01(\x0b2?.google.actions.sdk.v2.interactionmodel.prompt.StaticLinkPromptB\x03\xe0A\x01"\xcb\x01\n\x0bTableColumn\x12\x0e\n\x06header\x18\x01 \x01(\t\x12]\n\x05align\x18\x02 \x01(\x0e2N.google.actions.sdk.v2.interactionmodel.prompt.TableColumn.HorizontalAlignment"M\n\x13HorizontalAlignment\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07LEADING\x10\x01\x12\n\n\x06CENTER\x10\x02\x12\x0c\n\x08TRAILING\x10\x03"\x19\n\tTableCell\x12\x0c\n\x04text\x18\x01 \x01(\t"d\n\x08TableRow\x12G\n\x05cells\x18\x01 \x03(\x0b28.google.actions.sdk.v2.interactionmodel.prompt.TableCell\x12\x0f\n\x07divider\x18\x02 \x01(\x08B\xa2\x01\n1com.google.actions.sdk.v2.interactionmodel.promptB\x16StaticTablePromptProtoP\x01ZSgoogle.golang.org/genproto/googleapis/actions/sdk/v2/interactionmodel/prompt;promptb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.actions.sdk.v2.interactionmodel.prompt.content.static_table_prompt_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n1com.google.actions.sdk.v2.interactionmodel.promptB\x16StaticTablePromptProtoP\x01ZSgoogle.golang.org/genproto/googleapis/actions/sdk/v2/interactionmodel/prompt;prompt'
    _globals['_STATICTABLEPROMPT'].fields_by_name['title']._loaded_options = None
    _globals['_STATICTABLEPROMPT'].fields_by_name['title']._serialized_options = b'\xe0A\x01'
    _globals['_STATICTABLEPROMPT'].fields_by_name['subtitle']._loaded_options = None
    _globals['_STATICTABLEPROMPT'].fields_by_name['subtitle']._serialized_options = b'\xe0A\x01'
    _globals['_STATICTABLEPROMPT'].fields_by_name['image']._loaded_options = None
    _globals['_STATICTABLEPROMPT'].fields_by_name['image']._serialized_options = b'\xe0A\x01'
    _globals['_STATICTABLEPROMPT'].fields_by_name['columns']._loaded_options = None
    _globals['_STATICTABLEPROMPT'].fields_by_name['columns']._serialized_options = b'\xe0A\x01'
    _globals['_STATICTABLEPROMPT'].fields_by_name['rows']._loaded_options = None
    _globals['_STATICTABLEPROMPT'].fields_by_name['rows']._serialized_options = b'\xe0A\x01'
    _globals['_STATICTABLEPROMPT'].fields_by_name['button']._loaded_options = None
    _globals['_STATICTABLEPROMPT'].fields_by_name['button']._serialized_options = b'\xe0A\x01'
    _globals['_STATICTABLEPROMPT']._serialized_start = 325
    _globals['_STATICTABLEPROMPT']._serialized_end = 717
    _globals['_TABLECOLUMN']._serialized_start = 720
    _globals['_TABLECOLUMN']._serialized_end = 923
    _globals['_TABLECOLUMN_HORIZONTALALIGNMENT']._serialized_start = 846
    _globals['_TABLECOLUMN_HORIZONTALALIGNMENT']._serialized_end = 923
    _globals['_TABLECELL']._serialized_start = 925
    _globals['_TABLECELL']._serialized_end = 950
    _globals['_TABLEROW']._serialized_start = 952
    _globals['_TABLEROW']._serialized_end = 1052