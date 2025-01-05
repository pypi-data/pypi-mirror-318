"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/dialogflow/cx/v3beta1/conversation_history.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ......google.cloud.dialogflow.cx.v3beta1 import environment_pb2 as google_dot_cloud_dot_dialogflow_dot_cx_dot_v3beta1_dot_environment__pb2
from ......google.cloud.dialogflow.cx.v3beta1 import flow_pb2 as google_dot_cloud_dot_dialogflow_dot_cx_dot_v3beta1_dot_flow__pb2
from ......google.cloud.dialogflow.cx.v3beta1 import intent_pb2 as google_dot_cloud_dot_dialogflow_dot_cx_dot_v3beta1_dot_intent__pb2
from ......google.cloud.dialogflow.cx.v3beta1 import page_pb2 as google_dot_cloud_dot_dialogflow_dot_cx_dot_v3beta1_dot_page__pb2
from ......google.cloud.dialogflow.cx.v3beta1 import session_pb2 as google_dot_cloud_dot_dialogflow_dot_cx_dot_v3beta1_dot_session__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n=google/cloud/dialogflow/cx/v3beta1/conversation_history.proto\x12"google.cloud.dialogflow.cx.v3beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a4google/cloud/dialogflow/cx/v3beta1/environment.proto\x1a-google/cloud/dialogflow/cx/v3beta1/flow.proto\x1a/google/cloud/dialogflow/cx/v3beta1/intent.proto\x1a-google/cloud/dialogflow/cx/v3beta1/page.proto\x1a0google/cloud/dialogflow/cx/v3beta1/session.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto"V\n\x16GetConversationRequest\x12<\n\x04name\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\n&dialogflow.googleapis.com/Conversation"Y\n\x19DeleteConversationRequest\x12<\n\x04name\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\n&dialogflow.googleapis.com/Conversation"\xa0\x01\n\x18ListConversationsRequest\x12>\n\x06parent\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\x12&dialogflow.googleapis.com/Conversation\x12\x13\n\x06filter\x18\x02 \x01(\tB\x03\xe0A\x01\x12\x16\n\tpage_size\x18\x03 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x04 \x01(\tB\x03\xe0A\x01"}\n\x19ListConversationsResponse\x12G\n\rconversations\x18\x01 \x03(\x0b20.google.cloud.dialogflow.cx.v3beta1.Conversation\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xb1\x12\n\x0cConversation\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12C\n\x04type\x18\x02 \x01(\x0e25.google.cloud.dialogflow.cx.v3beta1.Conversation.Type\x12\x15\n\rlanguage_code\x18\x03 \x01(\t\x12.\n\nstart_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12+\n\x08duration\x18\x05 \x01(\x0b2\x19.google.protobuf.Duration\x12I\n\x07metrics\x18\x06 \x01(\x0b28.google.cloud.dialogflow.cx.v3beta1.Conversation.Metrics\x12;\n\x07intents\x18\x07 \x03(\x0b2*.google.cloud.dialogflow.cx.v3beta1.Intent\x127\n\x05flows\x18\x08 \x03(\x0b2(.google.cloud.dialogflow.cx.v3beta1.Flow\x127\n\x05pages\x18\t \x03(\x0b2(.google.cloud.dialogflow.cx.v3beta1.Page\x12R\n\x0cinteractions\x18\n \x03(\x0b2<.google.cloud.dialogflow.cx.v3beta1.Conversation.Interaction\x12D\n\x0benvironment\x18\x0b \x01(\x0b2/.google.cloud.dialogflow.cx.v3beta1.Environment\x12Y\n\rflow_versions\x18\x0c \x03(\x0b2B.google.cloud.dialogflow.cx.v3beta1.Conversation.FlowVersionsEntry\x1a\xb8\x06\n\x07Metrics\x12\x19\n\x11interaction_count\x18\x01 \x01(\x05\x127\n\x14input_audio_duration\x18\x02 \x01(\x0b2\x19.google.protobuf.Duration\x128\n\x15output_audio_duration\x18\x03 \x01(\x0b2\x19.google.protobuf.Duration\x126\n\x13max_webhook_latency\x18\x04 \x01(\x0b2\x19.google.protobuf.Duration\x12\x1b\n\x13has_end_interaction\x18\x05 \x01(\x08\x12\x1e\n\x16has_live_agent_handoff\x18\x06 \x01(\x08\x12 \n\x18average_match_confidence\x18\x07 \x01(\x02\x12c\n\x11query_input_count\x18\x08 \x01(\x0b2H.google.cloud.dialogflow.cx.v3beta1.Conversation.Metrics.QueryInputCount\x12a\n\x10match_type_count\x18\t \x01(\x0b2G.google.cloud.dialogflow.cx.v3beta1.Conversation.Metrics.MatchTypeCount\x1ay\n\x0fQueryInputCount\x12\x12\n\ntext_count\x18\x01 \x01(\x05\x12\x14\n\x0cintent_count\x18\x02 \x01(\x05\x12\x13\n\x0baudio_count\x18\x03 \x01(\x05\x12\x13\n\x0bevent_count\x18\x04 \x01(\x05\x12\x12\n\ndtmf_count\x18\x05 \x01(\x05\x1a\xc4\x01\n\x0eMatchTypeCount\x12\x19\n\x11unspecified_count\x18\x01 \x01(\x05\x12\x14\n\x0cintent_count\x18\x02 \x01(\x05\x12\x1b\n\x13direct_intent_count\x18\x03 \x01(\x05\x12\x1f\n\x17parameter_filling_count\x18\x04 \x01(\x05\x12\x16\n\x0eno_match_count\x18\x05 \x01(\x05\x12\x16\n\x0eno_input_count\x18\x06 \x01(\x05\x12\x13\n\x0bevent_count\x18\x07 \x01(\x05\x1a\x8f\x04\n\x0bInteraction\x12H\n\x07request\x18\x01 \x01(\x0b27.google.cloud.dialogflow.cx.v3beta1.DetectIntentRequest\x12J\n\x08response\x18\x02 \x01(\x0b28.google.cloud.dialogflow.cx.v3beta1.DetectIntentResponse\x12S\n\x11partial_responses\x18\x03 \x03(\x0b28.google.cloud.dialogflow.cx.v3beta1.DetectIntentResponse\x12\x1a\n\x12request_utterances\x18\x04 \x01(\t\x12\x1b\n\x13response_utterances\x18\x05 \x01(\t\x12/\n\x0bcreate_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12j\n\x12missing_transition\x18\x08 \x01(\x0b2N.google.cloud.dialogflow.cx.v3beta1.Conversation.Interaction.MissingTransition\x1a?\n\x11MissingTransition\x12\x1b\n\x13intent_display_name\x18\x01 \x01(\t\x12\r\n\x05score\x18\x02 \x01(\x02\x1a3\n\x11FlowVersionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x03:\x028\x01"C\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\t\n\x05AUDIO\x10\x01\x12\x08\n\x04TEXT\x10\x02\x12\x10\n\x0cUNDETERMINED\x10\x03:\x9e\x01\xeaA\x9a\x01\n&dialogflow.googleapis.com/Conversation\x12Sprojects/{project}/locations/{location}/agents/{agent}/conversations/{conversation}*\rconversations2\x0cconversation2\x84\x06\n\x13ConversationHistory\x12\xe2\x01\n\x11ListConversations\x12<.google.cloud.dialogflow.cx.v3beta1.ListConversationsRequest\x1a=.google.cloud.dialogflow.cx.v3beta1.ListConversationsResponse"P\xdaA\x06parent\x82\xd3\xe4\x93\x02A\x12?/v3beta1/{parent=projects/*/locations/*/agents/*}/conversations\x12\xcf\x01\n\x0fGetConversation\x12:.google.cloud.dialogflow.cx.v3beta1.GetConversationRequest\x1a0.google.cloud.dialogflow.cx.v3beta1.Conversation"N\xdaA\x04name\x82\xd3\xe4\x93\x02A\x12?/v3beta1/{name=projects/*/locations/*/agents/*/conversations/*}\x12\xbb\x01\n\x12DeleteConversation\x12=.google.cloud.dialogflow.cx.v3beta1.DeleteConversationRequest\x1a\x16.google.protobuf.Empty"N\xdaA\x04name\x82\xd3\xe4\x93\x02A*?/v3beta1/{name=projects/*/locations/*/agents/*/conversations/*}\x1ax\xcaA\x19dialogflow.googleapis.com\xd2AYhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflowB\xcf\x01\n&com.google.cloud.dialogflow.cx.v3beta1B\x18ConversationHistoryProtoP\x01Z6cloud.google.com/go/dialogflow/cx/apiv3beta1/cxpb;cxpb\xa2\x02\x02DF\xaa\x02"Google.Cloud.Dialogflow.Cx.V3Beta1\xea\x02&Google::Cloud::Dialogflow::CX::V3beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.dialogflow.cx.v3beta1.conversation_history_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.cloud.dialogflow.cx.v3beta1B\x18ConversationHistoryProtoP\x01Z6cloud.google.com/go/dialogflow/cx/apiv3beta1/cxpb;cxpb\xa2\x02\x02DF\xaa\x02"Google.Cloud.Dialogflow.Cx.V3Beta1\xea\x02&Google::Cloud::Dialogflow::CX::V3beta1'
    _globals['_GETCONVERSATIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETCONVERSATIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA(\n&dialogflow.googleapis.com/Conversation'
    _globals['_DELETECONVERSATIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETECONVERSATIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA(\n&dialogflow.googleapis.com/Conversation'
    _globals['_LISTCONVERSATIONSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTCONVERSATIONSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA(\x12&dialogflow.googleapis.com/Conversation'
    _globals['_LISTCONVERSATIONSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTCONVERSATIONSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_LISTCONVERSATIONSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTCONVERSATIONSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTCONVERSATIONSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTCONVERSATIONSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_CONVERSATION_FLOWVERSIONSENTRY']._loaded_options = None
    _globals['_CONVERSATION_FLOWVERSIONSENTRY']._serialized_options = b'8\x01'
    _globals['_CONVERSATION'].fields_by_name['name']._loaded_options = None
    _globals['_CONVERSATION'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_CONVERSATION']._loaded_options = None
    _globals['_CONVERSATION']._serialized_options = b'\xeaA\x9a\x01\n&dialogflow.googleapis.com/Conversation\x12Sprojects/{project}/locations/{location}/agents/{agent}/conversations/{conversation}*\rconversations2\x0cconversation'
    _globals['_CONVERSATIONHISTORY']._loaded_options = None
    _globals['_CONVERSATIONHISTORY']._serialized_options = b'\xcaA\x19dialogflow.googleapis.com\xd2AYhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflow'
    _globals['_CONVERSATIONHISTORY'].methods_by_name['ListConversations']._loaded_options = None
    _globals['_CONVERSATIONHISTORY'].methods_by_name['ListConversations']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02A\x12?/v3beta1/{parent=projects/*/locations/*/agents/*}/conversations'
    _globals['_CONVERSATIONHISTORY'].methods_by_name['GetConversation']._loaded_options = None
    _globals['_CONVERSATIONHISTORY'].methods_by_name['GetConversation']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02A\x12?/v3beta1/{name=projects/*/locations/*/agents/*/conversations/*}'
    _globals['_CONVERSATIONHISTORY'].methods_by_name['DeleteConversation']._loaded_options = None
    _globals['_CONVERSATIONHISTORY'].methods_by_name['DeleteConversation']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02A*?/v3beta1/{name=projects/*/locations/*/agents/*/conversations/*}'
    _globals['_GETCONVERSATIONREQUEST']._serialized_start = 557
    _globals['_GETCONVERSATIONREQUEST']._serialized_end = 643
    _globals['_DELETECONVERSATIONREQUEST']._serialized_start = 645
    _globals['_DELETECONVERSATIONREQUEST']._serialized_end = 734
    _globals['_LISTCONVERSATIONSREQUEST']._serialized_start = 737
    _globals['_LISTCONVERSATIONSREQUEST']._serialized_end = 897
    _globals['_LISTCONVERSATIONSRESPONSE']._serialized_start = 899
    _globals['_LISTCONVERSATIONSRESPONSE']._serialized_end = 1024
    _globals['_CONVERSATION']._serialized_start = 1027
    _globals['_CONVERSATION']._serialized_end = 3380
    _globals['_CONVERSATION_METRICS']._serialized_start = 1743
    _globals['_CONVERSATION_METRICS']._serialized_end = 2567
    _globals['_CONVERSATION_METRICS_QUERYINPUTCOUNT']._serialized_start = 2247
    _globals['_CONVERSATION_METRICS_QUERYINPUTCOUNT']._serialized_end = 2368
    _globals['_CONVERSATION_METRICS_MATCHTYPECOUNT']._serialized_start = 2371
    _globals['_CONVERSATION_METRICS_MATCHTYPECOUNT']._serialized_end = 2567
    _globals['_CONVERSATION_INTERACTION']._serialized_start = 2570
    _globals['_CONVERSATION_INTERACTION']._serialized_end = 3097
    _globals['_CONVERSATION_INTERACTION_MISSINGTRANSITION']._serialized_start = 3034
    _globals['_CONVERSATION_INTERACTION_MISSINGTRANSITION']._serialized_end = 3097
    _globals['_CONVERSATION_FLOWVERSIONSENTRY']._serialized_start = 3099
    _globals['_CONVERSATION_FLOWVERSIONSENTRY']._serialized_end = 3150
    _globals['_CONVERSATION_TYPE']._serialized_start = 3152
    _globals['_CONVERSATION_TYPE']._serialized_end = 3219
    _globals['_CONVERSATIONHISTORY']._serialized_start = 3383
    _globals['_CONVERSATIONHISTORY']._serialized_end = 4155