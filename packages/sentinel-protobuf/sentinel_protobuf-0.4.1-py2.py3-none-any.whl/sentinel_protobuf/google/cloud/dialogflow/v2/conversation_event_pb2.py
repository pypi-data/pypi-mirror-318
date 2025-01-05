"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/dialogflow/v2/conversation_event.proto')
_sym_db = _symbol_database.Default()
from .....google.cloud.dialogflow.v2 import participant_pb2 as google_dot_cloud_dot_dialogflow_dot_v2_dot_participant__pb2
from .....google.cloud.dialogflow.v2 import session_pb2 as google_dot_cloud_dot_dialogflow_dot_v2_dot_session__pb2
from .....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3google/cloud/dialogflow/v2/conversation_event.proto\x12\x1agoogle.cloud.dialogflow.v2\x1a,google/cloud/dialogflow/v2/participant.proto\x1a(google/cloud/dialogflow/v2/session.proto\x1a\x17google/rpc/status.proto"\xff\x03\n\x11ConversationEvent\x12\x14\n\x0cconversation\x18\x01 \x01(\t\x12@\n\x04type\x18\x02 \x01(\x0e22.google.cloud.dialogflow.v2.ConversationEvent.Type\x12(\n\x0cerror_status\x18\x03 \x01(\x0b2\x12.google.rpc.Status\x12B\n\x13new_message_payload\x18\x04 \x01(\x0b2#.google.cloud.dialogflow.v2.MessageH\x00\x12`\n\x1enew_recognition_result_payload\x18\x05 \x01(\x0b26.google.cloud.dialogflow.v2.StreamingRecognitionResultH\x00"\xb6\x01\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x18\n\x14CONVERSATION_STARTED\x10\x01\x12\x19\n\x15CONVERSATION_FINISHED\x10\x02\x12\x1d\n\x19HUMAN_INTERVENTION_NEEDED\x10\x03\x12\x0f\n\x0bNEW_MESSAGE\x10\x05\x12\x1a\n\x16NEW_RECOGNITION_RESULT\x10\x07\x12\x17\n\x13UNRECOVERABLE_ERROR\x10\x04B\t\n\x07payloadB\x9c\x01\n\x1ecom.google.cloud.dialogflow.v2B\x16ConversationEventProtoP\x01Z>cloud.google.com/go/dialogflow/apiv2/dialogflowpb;dialogflowpb\xa2\x02\x02DF\xaa\x02\x1aGoogle.Cloud.Dialogflow.V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.dialogflow.v2.conversation_event_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.dialogflow.v2B\x16ConversationEventProtoP\x01Z>cloud.google.com/go/dialogflow/apiv2/dialogflowpb;dialogflowpb\xa2\x02\x02DF\xaa\x02\x1aGoogle.Cloud.Dialogflow.V2'
    _globals['_CONVERSATIONEVENT']._serialized_start = 197
    _globals['_CONVERSATIONEVENT']._serialized_end = 708
    _globals['_CONVERSATIONEVENT_TYPE']._serialized_start = 515
    _globals['_CONVERSATIONEVENT_TYPE']._serialized_end = 697