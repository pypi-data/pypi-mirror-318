"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/actions/sdk/v2/interactionmodel/slot.proto')
_sym_db = _symbol_database.Default()
from ......google.actions.sdk.v2.interactionmodel import event_handler_pb2 as google_dot_actions_dot_sdk_dot_v2_dot_interactionmodel_dot_event__handler__pb2
from ......google.actions.sdk.v2.interactionmodel.type import class_reference_pb2 as google_dot_actions_dot_sdk_dot_v2_dot_interactionmodel_dot_type_dot_class__reference__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1google/actions/sdk/v2/interactionmodel/slot.proto\x12&google.actions.sdk.v2.interactionmodel\x1a:google/actions/sdk/v2/interactionmodel/event_handler.proto\x1aAgoogle/actions/sdk/v2/interactionmodel/type/class_reference.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1cgoogle/protobuf/struct.proto"\x8f\t\n\x04Slot\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x12N\n\x04type\x18\x02 \x01(\x0b2;.google.actions.sdk.v2.interactionmodel.type.ClassReferenceB\x03\xe0A\x02\x12\x15\n\x08required\x18\x03 \x01(\x08B\x03\xe0A\x01\x12Y\n\x0fprompt_settings\x18\x04 \x01(\x0b2;.google.actions.sdk.v2.interactionmodel.Slot.PromptSettingsB\x03\xe0A\x01\x12Y\n\x0fcommit_behavior\x18\x05 \x01(\x0b2;.google.actions.sdk.v2.interactionmodel.Slot.CommitBehaviorB\x03\xe0A\x01\x12+\n\x06config\x18\x06 \x01(\x0b2\x16.google.protobuf.ValueB\x03\xe0A\x01\x12U\n\rdefault_value\x18\x07 \x01(\x0b29.google.actions.sdk.v2.interactionmodel.Slot.DefaultValueB\x03\xe0A\x01\x1a\xc8\x04\n\x0ePromptSettings\x12L\n\x0einitial_prompt\x18\x01 \x01(\x0b24.google.actions.sdk.v2.interactionmodel.EventHandler\x12N\n\x10no_match_prompt1\x18\x02 \x01(\x0b24.google.actions.sdk.v2.interactionmodel.EventHandler\x12N\n\x10no_match_prompt2\x18\x03 \x01(\x0b24.google.actions.sdk.v2.interactionmodel.EventHandler\x12S\n\x15no_match_final_prompt\x18\x04 \x01(\x0b24.google.actions.sdk.v2.interactionmodel.EventHandler\x12N\n\x10no_input_prompt1\x18\x05 \x01(\x0b24.google.actions.sdk.v2.interactionmodel.EventHandler\x12N\n\x10no_input_prompt2\x18\x06 \x01(\x0b24.google.actions.sdk.v2.interactionmodel.EventHandler\x12S\n\x15no_input_final_prompt\x18\x07 \x01(\x0b24.google.actions.sdk.v2.interactionmodel.EventHandler\x1a-\n\x0eCommitBehavior\x12\x1b\n\x13write_session_param\x18\x01 \x01(\t\x1aY\n\x0cDefaultValue\x12\x1a\n\rsession_param\x18\x01 \x01(\tB\x03\xe0A\x01\x12-\n\x08constant\x18\x02 \x01(\x0b2\x16.google.protobuf.ValueB\x03\xe0A\x01B\x91\x01\n*com.google.actions.sdk.v2.interactionmodelB\tSlotProtoP\x01ZVgoogle.golang.org/genproto/googleapis/actions/sdk/v2/interactionmodel;interactionmodelb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.actions.sdk.v2.interactionmodel.slot_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n*com.google.actions.sdk.v2.interactionmodelB\tSlotProtoP\x01ZVgoogle.golang.org/genproto/googleapis/actions/sdk/v2/interactionmodel;interactionmodel'
    _globals['_SLOT_DEFAULTVALUE'].fields_by_name['session_param']._loaded_options = None
    _globals['_SLOT_DEFAULTVALUE'].fields_by_name['session_param']._serialized_options = b'\xe0A\x01'
    _globals['_SLOT_DEFAULTVALUE'].fields_by_name['constant']._loaded_options = None
    _globals['_SLOT_DEFAULTVALUE'].fields_by_name['constant']._serialized_options = b'\xe0A\x01'
    _globals['_SLOT'].fields_by_name['name']._loaded_options = None
    _globals['_SLOT'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_SLOT'].fields_by_name['type']._loaded_options = None
    _globals['_SLOT'].fields_by_name['type']._serialized_options = b'\xe0A\x02'
    _globals['_SLOT'].fields_by_name['required']._loaded_options = None
    _globals['_SLOT'].fields_by_name['required']._serialized_options = b'\xe0A\x01'
    _globals['_SLOT'].fields_by_name['prompt_settings']._loaded_options = None
    _globals['_SLOT'].fields_by_name['prompt_settings']._serialized_options = b'\xe0A\x01'
    _globals['_SLOT'].fields_by_name['commit_behavior']._loaded_options = None
    _globals['_SLOT'].fields_by_name['commit_behavior']._serialized_options = b'\xe0A\x01'
    _globals['_SLOT'].fields_by_name['config']._loaded_options = None
    _globals['_SLOT'].fields_by_name['config']._serialized_options = b'\xe0A\x01'
    _globals['_SLOT'].fields_by_name['default_value']._loaded_options = None
    _globals['_SLOT'].fields_by_name['default_value']._serialized_options = b'\xe0A\x01'
    _globals['_SLOT']._serialized_start = 284
    _globals['_SLOT']._serialized_end = 1451
    _globals['_SLOT_PROMPTSETTINGS']._serialized_start = 729
    _globals['_SLOT_PROMPTSETTINGS']._serialized_end = 1313
    _globals['_SLOT_COMMITBEHAVIOR']._serialized_start = 1315
    _globals['_SLOT_COMMITBEHAVIOR']._serialized_end = 1360
    _globals['_SLOT_DEFAULTVALUE']._serialized_start = 1362
    _globals['_SLOT_DEFAULTVALUE']._serialized_end = 1451