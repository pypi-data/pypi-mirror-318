"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/dialogflow/v2beta1/conversation_event.proto')
_sym_db = _symbol_database.Default()
from .....google.cloud.dialogflow.v2beta1 import participant_pb2 as google_dot_cloud_dot_dialogflow_dot_v2beta1_dot_participant__pb2
from .....google.cloud.dialogflow.v2beta1 import session_pb2 as google_dot_cloud_dot_dialogflow_dot_v2beta1_dot_session__pb2
from .....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8google/cloud/dialogflow/v2beta1/conversation_event.proto\x12\x1fgoogle.cloud.dialogflow.v2beta1\x1a1google/cloud/dialogflow/v2beta1/participant.proto\x1a-google/cloud/dialogflow/v2beta1/session.proto\x1a\x17google/rpc/status.proto"\x8e\x04\n\x11ConversationEvent\x12\x14\n\x0cconversation\x18\x01 \x01(\t\x12E\n\x04type\x18\x02 \x01(\x0e27.google.cloud.dialogflow.v2beta1.ConversationEvent.Type\x12(\n\x0cerror_status\x18\x03 \x01(\x0b2\x12.google.rpc.Status\x12G\n\x13new_message_payload\x18\x04 \x01(\x0b2(.google.cloud.dialogflow.v2beta1.MessageH\x00\x12e\n\x1enew_recognition_result_payload\x18\x05 \x01(\x0b2;.google.cloud.dialogflow.v2beta1.StreamingRecognitionResultH\x00"\xb6\x01\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x18\n\x14CONVERSATION_STARTED\x10\x01\x12\x19\n\x15CONVERSATION_FINISHED\x10\x02\x12\x1d\n\x19HUMAN_INTERVENTION_NEEDED\x10\x03\x12\x0f\n\x0bNEW_MESSAGE\x10\x05\x12\x1a\n\x16NEW_RECOGNITION_RESULT\x10\x07\x12\x17\n\x13UNRECOVERABLE_ERROR\x10\x04B\t\n\x07payloadB\xab\x01\n#com.google.cloud.dialogflow.v2beta1B\x16ConversationEventProtoP\x01ZCcloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb;dialogflowpb\xa2\x02\x02DF\xaa\x02\x1fGoogle.Cloud.Dialogflow.V2Beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.dialogflow.v2beta1.conversation_event_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.dialogflow.v2beta1B\x16ConversationEventProtoP\x01ZCcloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb;dialogflowpb\xa2\x02\x02DF\xaa\x02\x1fGoogle.Cloud.Dialogflow.V2Beta1'
    _globals['_CONVERSATIONEVENT']._serialized_start = 217
    _globals['_CONVERSATIONEVENT']._serialized_end = 743
    _globals['_CONVERSATIONEVENT_TYPE']._serialized_start = 550
    _globals['_CONVERSATIONEVENT_TYPE']._serialized_end = 732