"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/actions/sdk/v2/interactionmodel/conditional_event.proto')
_sym_db = _symbol_database.Default()
from ......google.actions.sdk.v2.interactionmodel import event_handler_pb2 as google_dot_actions_dot_sdk_dot_v2_dot_interactionmodel_dot_event__handler__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n>google/actions/sdk/v2/interactionmodel/conditional_event.proto\x12&google.actions.sdk.v2.interactionmodel\x1a:google/actions/sdk/v2/interactionmodel/event_handler.proto\x1a\x1fgoogle/api/field_behavior.proto"\x98\x01\n\x10ConditionalEvent\x12\x16\n\tcondition\x18\x01 \x01(\tB\x03\xe0A\x02\x12 \n\x13transition_to_scene\x18\x02 \x01(\tB\x03\xe0A\x01\x12J\n\x07handler\x18\x03 \x01(\x0b24.google.actions.sdk.v2.interactionmodel.EventHandlerB\x03\xe0A\x01B\x9d\x01\n*com.google.actions.sdk.v2.interactionmodelB\x15ConditionalEventProtoP\x01ZVgoogle.golang.org/genproto/googleapis/actions/sdk/v2/interactionmodel;interactionmodelb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.actions.sdk.v2.interactionmodel.conditional_event_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n*com.google.actions.sdk.v2.interactionmodelB\x15ConditionalEventProtoP\x01ZVgoogle.golang.org/genproto/googleapis/actions/sdk/v2/interactionmodel;interactionmodel'
    _globals['_CONDITIONALEVENT'].fields_by_name['condition']._loaded_options = None
    _globals['_CONDITIONALEVENT'].fields_by_name['condition']._serialized_options = b'\xe0A\x02'
    _globals['_CONDITIONALEVENT'].fields_by_name['transition_to_scene']._loaded_options = None
    _globals['_CONDITIONALEVENT'].fields_by_name['transition_to_scene']._serialized_options = b'\xe0A\x01'
    _globals['_CONDITIONALEVENT'].fields_by_name['handler']._loaded_options = None
    _globals['_CONDITIONALEVENT'].fields_by_name['handler']._serialized_options = b'\xe0A\x01'
    _globals['_CONDITIONALEVENT']._serialized_start = 200
    _globals['_CONDITIONALEVENT']._serialized_end = 352