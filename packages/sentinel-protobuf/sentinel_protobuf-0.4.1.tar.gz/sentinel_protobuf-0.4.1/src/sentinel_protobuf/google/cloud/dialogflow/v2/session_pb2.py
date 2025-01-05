"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/dialogflow/v2/session.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.dialogflow.v2 import audio_config_pb2 as google_dot_cloud_dot_dialogflow_dot_v2_dot_audio__config__pb2
from .....google.cloud.dialogflow.v2 import context_pb2 as google_dot_cloud_dot_dialogflow_dot_v2_dot_context__pb2
from .....google.cloud.dialogflow.v2 import intent_pb2 as google_dot_cloud_dot_dialogflow_dot_v2_dot_intent__pb2
from .....google.cloud.dialogflow.v2 import session_entity_type_pb2 as google_dot_cloud_dot_dialogflow_dot_v2_dot_session__entity__type__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from .....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
from .....google.type import latlng_pb2 as google_dot_type_dot_latlng__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(google/cloud/dialogflow/v2/session.proto\x12\x1agoogle.cloud.dialogflow.v2\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a-google/cloud/dialogflow/v2/audio_config.proto\x1a(google/cloud/dialogflow/v2/context.proto\x1a\'google/cloud/dialogflow/v2/intent.proto\x1a4google/cloud/dialogflow/v2/session_entity_type.proto\x1a\x1egoogle/protobuf/duration.proto\x1a google/protobuf/field_mask.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x17google/rpc/status.proto\x1a\x18google/type/latlng.proto"\xf5\x02\n\x13DetectIntentRequest\x12:\n\x07session\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!dialogflow.googleapis.com/Session\x12A\n\x0cquery_params\x18\x02 \x01(\x0b2+.google.cloud.dialogflow.v2.QueryParameters\x12@\n\x0bquery_input\x18\x03 \x01(\x0b2&.google.cloud.dialogflow.v2.QueryInputB\x03\xe0A\x02\x12J\n\x13output_audio_config\x18\x04 \x01(\x0b2-.google.cloud.dialogflow.v2.OutputAudioConfig\x12<\n\x18output_audio_config_mask\x18\x07 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12\x13\n\x0binput_audio\x18\x05 \x01(\x0c"\xf8\x01\n\x14DetectIntentResponse\x12\x13\n\x0bresponse_id\x18\x01 \x01(\t\x12=\n\x0cquery_result\x18\x02 \x01(\x0b2\'.google.cloud.dialogflow.v2.QueryResult\x12*\n\x0ewebhook_status\x18\x03 \x01(\x0b2\x12.google.rpc.Status\x12\x14\n\x0coutput_audio\x18\x04 \x01(\x0c\x12J\n\x13output_audio_config\x18\x06 \x01(\x0b2-.google.cloud.dialogflow.v2.OutputAudioConfig"\x9f\x04\n\x0fQueryParameters\x12\x11\n\ttime_zone\x18\x01 \x01(\t\x12)\n\x0cgeo_location\x18\x02 \x01(\x0b2\x13.google.type.LatLng\x125\n\x08contexts\x18\x03 \x03(\x0b2#.google.cloud.dialogflow.v2.Context\x12\x16\n\x0ereset_contexts\x18\x04 \x01(\x08\x12K\n\x14session_entity_types\x18\x05 \x03(\x0b2-.google.cloud.dialogflow.v2.SessionEntityType\x12(\n\x07payload\x18\x06 \x01(\x0b2\x17.google.protobuf.Struct\x12e\n!sentiment_analysis_request_config\x18\n \x01(\x0b2:.google.cloud.dialogflow.v2.SentimentAnalysisRequestConfig\x12X\n\x0fwebhook_headers\x18\x0e \x03(\x0b2?.google.cloud.dialogflow.v2.QueryParameters.WebhookHeadersEntry\x12\x10\n\x08platform\x18\x12 \x01(\t\x1a5\n\x13WebhookHeadersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"\xcb\x01\n\nQueryInput\x12D\n\x0caudio_config\x18\x01 \x01(\x0b2,.google.cloud.dialogflow.v2.InputAudioConfigH\x00\x125\n\x04text\x18\x02 \x01(\x0b2%.google.cloud.dialogflow.v2.TextInputH\x00\x127\n\x05event\x18\x03 \x01(\x0b2&.google.cloud.dialogflow.v2.EventInputH\x00B\x07\n\x05input"\xae\x05\n\x0bQueryResult\x12\x12\n\nquery_text\x18\x01 \x01(\t\x12\x15\n\rlanguage_code\x18\x0f \x01(\t\x12%\n\x1dspeech_recognition_confidence\x18\x02 \x01(\x02\x12\x0e\n\x06action\x18\x03 \x01(\t\x12+\n\nparameters\x18\x04 \x01(\x0b2\x17.google.protobuf.Struct\x12#\n\x1ball_required_params_present\x18\x05 \x01(\x08\x12\x1c\n\x14cancels_slot_filling\x18\x15 \x01(\x08\x12\x18\n\x10fulfillment_text\x18\x06 \x01(\t\x12H\n\x14fulfillment_messages\x18\x07 \x03(\x0b2*.google.cloud.dialogflow.v2.Intent.Message\x12\x16\n\x0ewebhook_source\x18\x08 \x01(\t\x120\n\x0fwebhook_payload\x18\t \x01(\x0b2\x17.google.protobuf.Struct\x12<\n\x0foutput_contexts\x18\n \x03(\x0b2#.google.cloud.dialogflow.v2.Context\x122\n\x06intent\x18\x0b \x01(\x0b2".google.cloud.dialogflow.v2.Intent\x12#\n\x1bintent_detection_confidence\x18\x0c \x01(\x02\x120\n\x0fdiagnostic_info\x18\x0e \x01(\x0b2\x17.google.protobuf.Struct\x12V\n\x19sentiment_analysis_result\x18\x11 \x01(\x0b23.google.cloud.dialogflow.v2.SentimentAnalysisResult"\xbb\x03\n\x1cStreamingDetectIntentRequest\x12:\n\x07session\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!dialogflow.googleapis.com/Session\x12A\n\x0cquery_params\x18\x02 \x01(\x0b2+.google.cloud.dialogflow.v2.QueryParameters\x12@\n\x0bquery_input\x18\x03 \x01(\x0b2&.google.cloud.dialogflow.v2.QueryInputB\x03\xe0A\x02\x12\x1c\n\x10single_utterance\x18\x04 \x01(\x08B\x02\x18\x01\x12J\n\x13output_audio_config\x18\x05 \x01(\x0b2-.google.cloud.dialogflow.v2.OutputAudioConfig\x12<\n\x18output_audio_config_mask\x18\x07 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12\x13\n\x0binput_audio\x18\x06 \x01(\x0c\x12\x1d\n\x15enable_debugging_info\x18\x08 \x01(\x08"\xb0\x07\n\x1eCloudConversationDebuggingInfo\x12\x19\n\x11audio_data_chunks\x18\x01 \x01(\x05\x129\n\x16result_end_time_offset\x18\x02 \x01(\x0b2\x19.google.protobuf.Duration\x127\n\x14first_audio_duration\x18\x03 \x01(\x0b2\x19.google.protobuf.Duration\x12\x18\n\x10single_utterance\x18\x05 \x01(\x08\x12C\n speech_partial_results_end_times\x18\x06 \x03(\x0b2\x19.google.protobuf.Duration\x12A\n\x1espeech_final_results_end_times\x18\x07 \x03(\x0b2\x19.google.protobuf.Duration\x12\x19\n\x11partial_responses\x18\x08 \x01(\x05\x12,\n$speaker_id_passive_latency_ms_offset\x18\t \x01(\x05\x12\x1f\n\x17bargein_event_triggered\x18\n \x01(\x08\x12\x1f\n\x17speech_single_utterance\x18\x0b \x01(\x08\x12=\n\x1adtmf_partial_results_times\x18\x0c \x03(\x0b2\x19.google.protobuf.Duration\x12;\n\x18dtmf_final_results_times\x18\r \x03(\x0b2\x19.google.protobuf.Duration\x12C\n single_utterance_end_time_offset\x18\x0e \x01(\x0b2\x19.google.protobuf.Duration\x124\n\x11no_speech_timeout\x18\x0f \x01(\x0b2\x19.google.protobuf.Duration\x126\n\x13endpointing_timeout\x18\x13 \x01(\x0b2\x19.google.protobuf.Duration\x12\x15\n\ris_input_text\x18\x10 \x01(\x08\x12@\n\x1dclient_half_close_time_offset\x18\x11 \x01(\x0b2\x19.google.protobuf.Duration\x12J\n\'client_half_close_streaming_time_offset\x18\x12 \x01(\x0b2\x19.google.protobuf.Duration"\xa9\x03\n\x1dStreamingDetectIntentResponse\x12\x13\n\x0bresponse_id\x18\x01 \x01(\t\x12R\n\x12recognition_result\x18\x02 \x01(\x0b26.google.cloud.dialogflow.v2.StreamingRecognitionResult\x12=\n\x0cquery_result\x18\x03 \x01(\x0b2\'.google.cloud.dialogflow.v2.QueryResult\x12*\n\x0ewebhook_status\x18\x04 \x01(\x0b2\x12.google.rpc.Status\x12\x14\n\x0coutput_audio\x18\x05 \x01(\x0c\x12J\n\x13output_audio_config\x18\x06 \x01(\x0b2-.google.cloud.dialogflow.v2.OutputAudioConfig\x12R\n\x0edebugging_info\x18\x08 \x01(\x0b2:.google.cloud.dialogflow.v2.CloudConversationDebuggingInfo"\x9d\x03\n\x1aStreamingRecognitionResult\x12X\n\x0cmessage_type\x18\x01 \x01(\x0e2B.google.cloud.dialogflow.v2.StreamingRecognitionResult.MessageType\x12\x12\n\ntranscript\x18\x02 \x01(\t\x12\x10\n\x08is_final\x18\x03 \x01(\x08\x12\x12\n\nconfidence\x18\x04 \x01(\x02\x12D\n\x10speech_word_info\x18\x07 \x03(\x0b2*.google.cloud.dialogflow.v2.SpeechWordInfo\x124\n\x11speech_end_offset\x18\x08 \x01(\x0b2\x19.google.protobuf.Duration\x12\x15\n\rlanguage_code\x18\n \x01(\t"X\n\x0bMessageType\x12\x1c\n\x18MESSAGE_TYPE_UNSPECIFIED\x10\x00\x12\x0e\n\nTRANSCRIPT\x10\x01\x12\x1b\n\x17END_OF_SINGLE_UTTERANCE\x10\x02":\n\tTextInput\x12\x11\n\x04text\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x1a\n\rlanguage_code\x18\x02 \x01(\tB\x03\xe0A\x02"h\n\nEventInput\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x12+\n\nparameters\x18\x02 \x01(\x0b2\x17.google.protobuf.Struct\x12\x1a\n\rlanguage_code\x18\x03 \x01(\tB\x03\xe0A\x02"F\n\x1eSentimentAnalysisRequestConfig\x12$\n\x1canalyze_query_text_sentiment\x18\x01 \x01(\x08"^\n\x17SentimentAnalysisResult\x12C\n\x14query_text_sentiment\x18\x01 \x01(\x0b2%.google.cloud.dialogflow.v2.Sentiment"-\n\tSentiment\x12\r\n\x05score\x18\x01 \x01(\x02\x12\x11\n\tmagnitude\x18\x02 \x01(\x022\xe5\x05\n\x08Sessions\x12\xc9\x03\n\x0cDetectIntent\x12/.google.cloud.dialogflow.v2.DetectIntentRequest\x1a0.google.cloud.dialogflow.v2.DetectIntentResponse"\xd5\x02\xdaA\x13session,query_input\x82\xd3\xe4\x93\x02\xb8\x02"6/v2/{session=projects/*/agent/sessions/*}:detectIntent:\x01*ZR"M/v2/{session=projects/*/agent/environments/*/users/*/sessions/*}:detectIntent:\x01*ZG"B/v2/{session=projects/*/locations/*/agent/sessions/*}:detectIntent:\x01*Z^"Y/v2/{session=projects/*/locations/*/agent/environments/*/users/*/sessions/*}:detectIntent:\x01*\x12\x92\x01\n\x15StreamingDetectIntent\x128.google.cloud.dialogflow.v2.StreamingDetectIntentRequest\x1a9.google.cloud.dialogflow.v2.StreamingDetectIntentResponse"\x00(\x010\x01\x1ax\xcaA\x19dialogflow.googleapis.com\xd2AYhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflowB\xea\x03\n\x1ecom.google.cloud.dialogflow.v2B\x0cSessionProtoP\x01Z>cloud.google.com/go/dialogflow/apiv2/dialogflowpb;dialogflowpb\xf8\x01\x01\xa2\x02\x02DF\xaa\x02\x1aGoogle.Cloud.Dialogflow.V2\xeaA\xd1\x02\n!dialogflow.googleapis.com/Session\x12+projects/{project}/agent/sessions/{session}\x12Sprojects/{project}/agent/environments/{environment}/users/{user}/sessions/{session}\x12@projects/{project}/locations/{location}/agent/sessions/{session}\x12hprojects/{project}/locations/{location}/agent/environments/{environment}/users/{user}/sessions/{session}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.dialogflow.v2.session_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.dialogflow.v2B\x0cSessionProtoP\x01Z>cloud.google.com/go/dialogflow/apiv2/dialogflowpb;dialogflowpb\xf8\x01\x01\xa2\x02\x02DF\xaa\x02\x1aGoogle.Cloud.Dialogflow.V2\xeaA\xd1\x02\n!dialogflow.googleapis.com/Session\x12+projects/{project}/agent/sessions/{session}\x12Sprojects/{project}/agent/environments/{environment}/users/{user}/sessions/{session}\x12@projects/{project}/locations/{location}/agent/sessions/{session}\x12hprojects/{project}/locations/{location}/agent/environments/{environment}/users/{user}/sessions/{session}'
    _globals['_DETECTINTENTREQUEST'].fields_by_name['session']._loaded_options = None
    _globals['_DETECTINTENTREQUEST'].fields_by_name['session']._serialized_options = b'\xe0A\x02\xfaA#\n!dialogflow.googleapis.com/Session'
    _globals['_DETECTINTENTREQUEST'].fields_by_name['query_input']._loaded_options = None
    _globals['_DETECTINTENTREQUEST'].fields_by_name['query_input']._serialized_options = b'\xe0A\x02'
    _globals['_QUERYPARAMETERS_WEBHOOKHEADERSENTRY']._loaded_options = None
    _globals['_QUERYPARAMETERS_WEBHOOKHEADERSENTRY']._serialized_options = b'8\x01'
    _globals['_STREAMINGDETECTINTENTREQUEST'].fields_by_name['session']._loaded_options = None
    _globals['_STREAMINGDETECTINTENTREQUEST'].fields_by_name['session']._serialized_options = b'\xe0A\x02\xfaA#\n!dialogflow.googleapis.com/Session'
    _globals['_STREAMINGDETECTINTENTREQUEST'].fields_by_name['query_input']._loaded_options = None
    _globals['_STREAMINGDETECTINTENTREQUEST'].fields_by_name['query_input']._serialized_options = b'\xe0A\x02'
    _globals['_STREAMINGDETECTINTENTREQUEST'].fields_by_name['single_utterance']._loaded_options = None
    _globals['_STREAMINGDETECTINTENTREQUEST'].fields_by_name['single_utterance']._serialized_options = b'\x18\x01'
    _globals['_TEXTINPUT'].fields_by_name['text']._loaded_options = None
    _globals['_TEXTINPUT'].fields_by_name['text']._serialized_options = b'\xe0A\x02'
    _globals['_TEXTINPUT'].fields_by_name['language_code']._loaded_options = None
    _globals['_TEXTINPUT'].fields_by_name['language_code']._serialized_options = b'\xe0A\x02'
    _globals['_EVENTINPUT'].fields_by_name['name']._loaded_options = None
    _globals['_EVENTINPUT'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_EVENTINPUT'].fields_by_name['language_code']._loaded_options = None
    _globals['_EVENTINPUT'].fields_by_name['language_code']._serialized_options = b'\xe0A\x02'
    _globals['_SESSIONS']._loaded_options = None
    _globals['_SESSIONS']._serialized_options = b'\xcaA\x19dialogflow.googleapis.com\xd2AYhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflow'
    _globals['_SESSIONS'].methods_by_name['DetectIntent']._loaded_options = None
    _globals['_SESSIONS'].methods_by_name['DetectIntent']._serialized_options = b'\xdaA\x13session,query_input\x82\xd3\xe4\x93\x02\xb8\x02"6/v2/{session=projects/*/agent/sessions/*}:detectIntent:\x01*ZR"M/v2/{session=projects/*/agent/environments/*/users/*/sessions/*}:detectIntent:\x01*ZG"B/v2/{session=projects/*/locations/*/agent/sessions/*}:detectIntent:\x01*Z^"Y/v2/{session=projects/*/locations/*/agent/environments/*/users/*/sessions/*}:detectIntent:\x01*'
    _globals['_DETECTINTENTREQUEST']._serialized_start = 519
    _globals['_DETECTINTENTREQUEST']._serialized_end = 892
    _globals['_DETECTINTENTRESPONSE']._serialized_start = 895
    _globals['_DETECTINTENTRESPONSE']._serialized_end = 1143
    _globals['_QUERYPARAMETERS']._serialized_start = 1146
    _globals['_QUERYPARAMETERS']._serialized_end = 1689
    _globals['_QUERYPARAMETERS_WEBHOOKHEADERSENTRY']._serialized_start = 1636
    _globals['_QUERYPARAMETERS_WEBHOOKHEADERSENTRY']._serialized_end = 1689
    _globals['_QUERYINPUT']._serialized_start = 1692
    _globals['_QUERYINPUT']._serialized_end = 1895
    _globals['_QUERYRESULT']._serialized_start = 1898
    _globals['_QUERYRESULT']._serialized_end = 2584
    _globals['_STREAMINGDETECTINTENTREQUEST']._serialized_start = 2587
    _globals['_STREAMINGDETECTINTENTREQUEST']._serialized_end = 3030
    _globals['_CLOUDCONVERSATIONDEBUGGINGINFO']._serialized_start = 3033
    _globals['_CLOUDCONVERSATIONDEBUGGINGINFO']._serialized_end = 3977
    _globals['_STREAMINGDETECTINTENTRESPONSE']._serialized_start = 3980
    _globals['_STREAMINGDETECTINTENTRESPONSE']._serialized_end = 4405
    _globals['_STREAMINGRECOGNITIONRESULT']._serialized_start = 4408
    _globals['_STREAMINGRECOGNITIONRESULT']._serialized_end = 4821
    _globals['_STREAMINGRECOGNITIONRESULT_MESSAGETYPE']._serialized_start = 4733
    _globals['_STREAMINGRECOGNITIONRESULT_MESSAGETYPE']._serialized_end = 4821
    _globals['_TEXTINPUT']._serialized_start = 4823
    _globals['_TEXTINPUT']._serialized_end = 4881
    _globals['_EVENTINPUT']._serialized_start = 4883
    _globals['_EVENTINPUT']._serialized_end = 4987
    _globals['_SENTIMENTANALYSISREQUESTCONFIG']._serialized_start = 4989
    _globals['_SENTIMENTANALYSISREQUESTCONFIG']._serialized_end = 5059
    _globals['_SENTIMENTANALYSISRESULT']._serialized_start = 5061
    _globals['_SENTIMENTANALYSISRESULT']._serialized_end = 5155
    _globals['_SENTIMENT']._serialized_start = 5157
    _globals['_SENTIMENT']._serialized_end = 5202
    _globals['_SESSIONS']._serialized_start = 5205
    _globals['_SESSIONS']._serialized_end = 5946