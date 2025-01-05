"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/actions/sdk/v2/interactionmodel/scene.proto')
_sym_db = _symbol_database.Default()
from ......google.actions.sdk.v2.interactionmodel import conditional_event_pb2 as google_dot_actions_dot_sdk_dot_v2_dot_interactionmodel_dot_conditional__event__pb2
from ......google.actions.sdk.v2.interactionmodel import event_handler_pb2 as google_dot_actions_dot_sdk_dot_v2_dot_interactionmodel_dot_event__handler__pb2
from ......google.actions.sdk.v2.interactionmodel import intent_event_pb2 as google_dot_actions_dot_sdk_dot_v2_dot_interactionmodel_dot_intent__event__pb2
from ......google.actions.sdk.v2.interactionmodel import slot_pb2 as google_dot_actions_dot_sdk_dot_v2_dot_interactionmodel_dot_slot__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2google/actions/sdk/v2/interactionmodel/scene.proto\x12&google.actions.sdk.v2.interactionmodel\x1a>google/actions/sdk/v2/interactionmodel/conditional_event.proto\x1a:google/actions/sdk/v2/interactionmodel/event_handler.proto\x1a9google/actions/sdk/v2/interactionmodel/intent_event.proto\x1a1google/actions/sdk/v2/interactionmodel/slot.proto"\xfd\x02\n\x05Scene\x12F\n\x08on_enter\x18\x01 \x01(\x0b24.google.actions.sdk.v2.interactionmodel.EventHandler\x12J\n\rintent_events\x18\x02 \x03(\x0b23.google.actions.sdk.v2.interactionmodel.IntentEvent\x12T\n\x12conditional_events\x18\x03 \x03(\x0b28.google.actions.sdk.v2.interactionmodel.ConditionalEvent\x12;\n\x05slots\x18\x04 \x03(\x0b2,.google.actions.sdk.v2.interactionmodel.Slot\x12M\n\x0fon_slot_updated\x18\x05 \x01(\x0b24.google.actions.sdk.v2.interactionmodel.EventHandlerB\x92\x01\n*com.google.actions.sdk.v2.interactionmodelB\nSceneProtoP\x01ZVgoogle.golang.org/genproto/googleapis/actions/sdk/v2/interactionmodel;interactionmodelb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.actions.sdk.v2.interactionmodel.scene_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n*com.google.actions.sdk.v2.interactionmodelB\nSceneProtoP\x01ZVgoogle.golang.org/genproto/googleapis/actions/sdk/v2/interactionmodel;interactionmodel'
    _globals['_SCENE']._serialized_start = 329
    _globals['_SCENE']._serialized_end = 710