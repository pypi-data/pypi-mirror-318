"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/actions/sdk/v2/conversation/scene.proto')
_sym_db = _symbol_database.Default()
from ......google.actions.sdk.v2.conversation.prompt import prompt_pb2 as google_dot_actions_dot_sdk_dot_v2_dot_conversation_dot_prompt_dot_prompt__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.google/actions/sdk/v2/conversation/scene.proto\x12"google.actions.sdk.v2.conversation\x1a6google/actions/sdk/v2/conversation/prompt/prompt.proto\x1a\x1cgoogle/protobuf/struct.proto"\x86\x03\n\x04Slot\x12?\n\x04mode\x18\x01 \x01(\x0e21.google.actions.sdk.v2.conversation.Slot.SlotMode\x12C\n\x06status\x18\x02 \x01(\x0e23.google.actions.sdk.v2.conversation.Slot.SlotStatus\x12%\n\x05value\x18\x03 \x01(\x0b2\x16.google.protobuf.Value\x12\x0f\n\x07updated\x18\x04 \x01(\x08\x12:\n\x06prompt\x18\x05 \x01(\x0b2*.google.actions.sdk.v2.conversation.Prompt"<\n\x08SlotMode\x12\x14\n\x10MODE_UNSPECIFIED\x10\x00\x12\x0c\n\x08OPTIONAL\x10\x01\x12\x0c\n\x08REQUIRED\x10\x02"F\n\nSlotStatus\x12\x14\n\x10SLOT_UNSPECIFIED\x10\x00\x12\t\n\x05EMPTY\x10\x01\x12\x0b\n\x07INVALID\x10\x02\x12\n\n\x06FILLED\x10\x03*P\n\x11SlotFillingStatus\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0f\n\x0bINITIALIZED\x10\x01\x12\x0e\n\nCOLLECTING\x10\x02\x12\t\n\x05FINAL\x10\x04B\x86\x01\n&com.google.actions.sdk.v2.conversationB\nSceneProtoP\x01ZNgoogle.golang.org/genproto/googleapis/actions/sdk/v2/conversation;conversationb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.actions.sdk.v2.conversation.scene_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.actions.sdk.v2.conversationB\nSceneProtoP\x01ZNgoogle.golang.org/genproto/googleapis/actions/sdk/v2/conversation;conversation'
    _globals['_SLOTFILLINGSTATUS']._serialized_start = 565
    _globals['_SLOTFILLINGSTATUS']._serialized_end = 645
    _globals['_SLOT']._serialized_start = 173
    _globals['_SLOT']._serialized_end = 563
    _globals['_SLOT_SLOTMODE']._serialized_start = 431
    _globals['_SLOT_SLOTMODE']._serialized_end = 491
    _globals['_SLOT_SLOTSTATUS']._serialized_start = 493
    _globals['_SLOT_SLOTSTATUS']._serialized_end = 563