"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/dialogflow/v2/human_agent_assistant_event.proto')
_sym_db = _symbol_database.Default()
from .....google.cloud.dialogflow.v2 import participant_pb2 as google_dot_cloud_dot_dialogflow_dot_v2_dot_participant__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n<google/cloud/dialogflow/v2/human_agent_assistant_event.proto\x12\x1agoogle.cloud.dialogflow.v2\x1a,google/cloud/dialogflow/v2/participant.proto"\x8f\x01\n\x18HumanAgentAssistantEvent\x12\x14\n\x0cconversation\x18\x01 \x01(\t\x12\x13\n\x0bparticipant\x18\x03 \x01(\t\x12H\n\x12suggestion_results\x18\x05 \x03(\x0b2,.google.cloud.dialogflow.v2.SuggestionResultB\xa3\x01\n\x1ecom.google.cloud.dialogflow.v2B\x1dHumanAgentAssistantEventProtoP\x01Z>cloud.google.com/go/dialogflow/apiv2/dialogflowpb;dialogflowpb\xa2\x02\x02DF\xaa\x02\x1aGoogle.Cloud.Dialogflow.V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.dialogflow.v2.human_agent_assistant_event_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.dialogflow.v2B\x1dHumanAgentAssistantEventProtoP\x01Z>cloud.google.com/go/dialogflow/apiv2/dialogflowpb;dialogflowpb\xa2\x02\x02DF\xaa\x02\x1aGoogle.Cloud.Dialogflow.V2'
    _globals['_HUMANAGENTASSISTANTEVENT']._serialized_start = 139
    _globals['_HUMANAGENTASSISTANTEVENT']._serialized_end = 282