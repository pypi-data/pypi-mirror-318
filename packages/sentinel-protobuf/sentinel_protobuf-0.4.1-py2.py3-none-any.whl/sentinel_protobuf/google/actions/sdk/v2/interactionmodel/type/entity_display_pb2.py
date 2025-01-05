"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/actions/sdk/v2/interactionmodel/type/entity_display.proto')
_sym_db = _symbol_database.Default()
from .......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n@google/actions/sdk/v2/interactionmodel/type/entity_display.proto\x12+google.actions.sdk.v2.interactionmodel.type\x1a\x1fgoogle/api/field_behavior.proto"?\n\rEntityDisplay\x12\x17\n\nicon_title\x18\x01 \x01(\tB\x03\xe0A\x01\x12\x15\n\x08icon_url\x18\x02 \x01(\tB\x03\xe0A\x02B\x93\x01\n/com.google.actions.sdk.v2.interactionmodel.typeB\x12EntityDisplayProtoP\x01ZJgoogle.golang.org/genproto/googleapis/actions/sdk/v2/interactionmodel/typeb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.actions.sdk.v2.interactionmodel.type.entity_display_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n/com.google.actions.sdk.v2.interactionmodel.typeB\x12EntityDisplayProtoP\x01ZJgoogle.golang.org/genproto/googleapis/actions/sdk/v2/interactionmodel/type'
    _globals['_ENTITYDISPLAY'].fields_by_name['icon_title']._loaded_options = None
    _globals['_ENTITYDISPLAY'].fields_by_name['icon_title']._serialized_options = b'\xe0A\x01'
    _globals['_ENTITYDISPLAY'].fields_by_name['icon_url']._loaded_options = None
    _globals['_ENTITYDISPLAY'].fields_by_name['icon_url']._serialized_options = b'\xe0A\x02'
    _globals['_ENTITYDISPLAY']._serialized_start = 146
    _globals['_ENTITYDISPLAY']._serialized_end = 209