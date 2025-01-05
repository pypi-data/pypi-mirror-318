"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/actions/sdk/v2/interactionmodel/event_handler.proto')
_sym_db = _symbol_database.Default()
from ......google.actions.sdk.v2.interactionmodel.prompt import static_prompt_pb2 as google_dot_actions_dot_sdk_dot_v2_dot_interactionmodel_dot_prompt_dot_static__prompt__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:google/actions/sdk/v2/interactionmodel/event_handler.proto\x12&google.actions.sdk.v2.interactionmodel\x1aAgoogle/actions/sdk/v2/interactionmodel/prompt/static_prompt.proto"\xa5\x01\n\x0cEventHandler\x12\x17\n\x0fwebhook_handler\x18\x01 \x01(\t\x12T\n\rstatic_prompt\x18\x02 \x01(\x0b2;.google.actions.sdk.v2.interactionmodel.prompt.StaticPromptH\x00\x12\x1c\n\x12static_prompt_name\x18\x03 \x01(\tH\x00B\x08\n\x06promptB\x99\x01\n*com.google.actions.sdk.v2.interactionmodelB\x11EventHandlerProtoP\x01ZVgoogle.golang.org/genproto/googleapis/actions/sdk/v2/interactionmodel;interactionmodelb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.actions.sdk.v2.interactionmodel.event_handler_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n*com.google.actions.sdk.v2.interactionmodelB\x11EventHandlerProtoP\x01ZVgoogle.golang.org/genproto/googleapis/actions/sdk/v2/interactionmodel;interactionmodel'
    _globals['_EVENTHANDLER']._serialized_start = 170
    _globals['_EVENTHANDLER']._serialized_end = 335