"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/dialogflow/cx/v3/session.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ......google.cloud.dialogflow.cx.v3 import advanced_settings_pb2 as google_dot_cloud_dot_dialogflow_dot_cx_dot_v3_dot_advanced__settings__pb2
from ......google.cloud.dialogflow.cx.v3 import audio_config_pb2 as google_dot_cloud_dot_dialogflow_dot_cx_dot_v3_dot_audio__config__pb2
from ......google.cloud.dialogflow.cx.v3 import data_store_connection_pb2 as google_dot_cloud_dot_dialogflow_dot_cx_dot_v3_dot_data__store__connection__pb2
from ......google.cloud.dialogflow.cx.v3 import flow_pb2 as google_dot_cloud_dot_dialogflow_dot_cx_dot_v3_dot_flow__pb2
from ......google.cloud.dialogflow.cx.v3 import intent_pb2 as google_dot_cloud_dot_dialogflow_dot_cx_dot_v3_dot_intent__pb2
from ......google.cloud.dialogflow.cx.v3 import page_pb2 as google_dot_cloud_dot_dialogflow_dot_cx_dot_v3_dot_page__pb2
from ......google.cloud.dialogflow.cx.v3 import response_message_pb2 as google_dot_cloud_dot_dialogflow_dot_cx_dot_v3_dot_response__message__pb2
from ......google.cloud.dialogflow.cx.v3 import session_entity_type_pb2 as google_dot_cloud_dot_dialogflow_dot_cx_dot_v3_dot_session__entity__type__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from ......google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
from ......google.type import latlng_pb2 as google_dot_type_dot_latlng__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+google/cloud/dialogflow/cx/v3/session.proto\x12\x1dgoogle.cloud.dialogflow.cx.v3\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a5google/cloud/dialogflow/cx/v3/advanced_settings.proto\x1a0google/cloud/dialogflow/cx/v3/audio_config.proto\x1a9google/cloud/dialogflow/cx/v3/data_store_connection.proto\x1a(google/cloud/dialogflow/cx/v3/flow.proto\x1a*google/cloud/dialogflow/cx/v3/intent.proto\x1a(google/cloud/dialogflow/cx/v3/page.proto\x1a4google/cloud/dialogflow/cx/v3/response_message.proto\x1a7google/cloud/dialogflow/cx/v3/session_entity_type.proto\x1a\x1egoogle/protobuf/duration.proto\x1a google/protobuf/field_mask.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x17google/rpc/status.proto\x1a\x18google/type/latlng.proto"\xd4\x02\n\x0eAnswerFeedback\x12I\n\x06rating\x18\x01 \x01(\x0e24.google.cloud.dialogflow.cx.v3.AnswerFeedback.RatingB\x03\xe0A\x01\x12V\n\rrating_reason\x18\x02 \x01(\x0b2:.google.cloud.dialogflow.cx.v3.AnswerFeedback.RatingReasonB\x03\xe0A\x01\x12\x1a\n\rcustom_rating\x18\x03 \x01(\tB\x03\xe0A\x01\x1aA\n\x0cRatingReason\x12\x1a\n\rreason_labels\x18\x03 \x03(\tB\x03\xe0A\x01\x12\x15\n\x08feedback\x18\x02 \x01(\tB\x03\xe0A\x01"@\n\x06Rating\x12\x16\n\x12RATING_UNSPECIFIED\x10\x00\x12\r\n\tTHUMBS_UP\x10\x01\x12\x0f\n\x0bTHUMBS_DOWN\x10\x02"\xf6\x01\n\x1bSubmitAnswerFeedbackRequest\x12:\n\x07session\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!dialogflow.googleapis.com/Session\x12\x18\n\x0bresponse_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12K\n\x0fanswer_feedback\x18\x03 \x01(\x0b2-.google.cloud.dialogflow.cx.v3.AnswerFeedbackB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x04 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01"\xab\x02\n\x13DetectIntentRequest\x12:\n\x07session\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!dialogflow.googleapis.com/Session\x12D\n\x0cquery_params\x18\x02 \x01(\x0b2..google.cloud.dialogflow.cx.v3.QueryParameters\x12C\n\x0bquery_input\x18\x03 \x01(\x0b2).google.cloud.dialogflow.cx.v3.QueryInputB\x03\xe0A\x02\x12M\n\x13output_audio_config\x18\x04 \x01(\x0b20.google.cloud.dialogflow.cx.v3.OutputAudioConfig"\x8e\x03\n\x14DetectIntentResponse\x12\x13\n\x0bresponse_id\x18\x01 \x01(\t\x12@\n\x0cquery_result\x18\x02 \x01(\x0b2*.google.cloud.dialogflow.cx.v3.QueryResult\x12\x14\n\x0coutput_audio\x18\x04 \x01(\x0c\x12M\n\x13output_audio_config\x18\x05 \x01(\x0b20.google.cloud.dialogflow.cx.v3.OutputAudioConfig\x12W\n\rresponse_type\x18\x06 \x01(\x0e2@.google.cloud.dialogflow.cx.v3.DetectIntentResponse.ResponseType\x12\x1a\n\x12allow_cancellation\x18\x07 \x01(\x08"E\n\x0cResponseType\x12\x1d\n\x19RESPONSE_TYPE_UNSPECIFIED\x10\x00\x12\x0b\n\x07PARTIAL\x10\x01\x12\t\n\x05FINAL\x10\x02"\xf1\x02\n\x1cStreamingDetectIntentRequest\x127\n\x07session\x18\x01 \x01(\tB&\xfaA#\n!dialogflow.googleapis.com/Session\x12D\n\x0cquery_params\x18\x02 \x01(\x0b2..google.cloud.dialogflow.cx.v3.QueryParameters\x12C\n\x0bquery_input\x18\x03 \x01(\x0b2).google.cloud.dialogflow.cx.v3.QueryInputB\x03\xe0A\x02\x12M\n\x13output_audio_config\x18\x04 \x01(\x0b20.google.cloud.dialogflow.cx.v3.OutputAudioConfig\x12\x1f\n\x17enable_partial_response\x18\x05 \x01(\x08\x12\x1d\n\x15enable_debugging_info\x18\x08 \x01(\x08"\xb0\x07\n\x1eCloudConversationDebuggingInfo\x12\x19\n\x11audio_data_chunks\x18\x01 \x01(\x05\x129\n\x16result_end_time_offset\x18\x02 \x01(\x0b2\x19.google.protobuf.Duration\x127\n\x14first_audio_duration\x18\x03 \x01(\x0b2\x19.google.protobuf.Duration\x12\x18\n\x10single_utterance\x18\x05 \x01(\x08\x12C\n speech_partial_results_end_times\x18\x06 \x03(\x0b2\x19.google.protobuf.Duration\x12A\n\x1espeech_final_results_end_times\x18\x07 \x03(\x0b2\x19.google.protobuf.Duration\x12\x19\n\x11partial_responses\x18\x08 \x01(\x05\x12,\n$speaker_id_passive_latency_ms_offset\x18\t \x01(\x05\x12\x1f\n\x17bargein_event_triggered\x18\n \x01(\x08\x12\x1f\n\x17speech_single_utterance\x18\x0b \x01(\x08\x12=\n\x1adtmf_partial_results_times\x18\x0c \x03(\x0b2\x19.google.protobuf.Duration\x12;\n\x18dtmf_final_results_times\x18\r \x03(\x0b2\x19.google.protobuf.Duration\x12C\n single_utterance_end_time_offset\x18\x0e \x01(\x0b2\x19.google.protobuf.Duration\x124\n\x11no_speech_timeout\x18\x0f \x01(\x0b2\x19.google.protobuf.Duration\x126\n\x13endpointing_timeout\x18\x13 \x01(\x0b2\x19.google.protobuf.Duration\x12\x15\n\ris_input_text\x18\x10 \x01(\x08\x12@\n\x1dclient_half_close_time_offset\x18\x11 \x01(\x0b2\x19.google.protobuf.Duration\x12J\n\'client_half_close_streaming_time_offset\x18\x12 \x01(\x0b2\x19.google.protobuf.Duration"\xb2\x02\n\x1dStreamingDetectIntentResponse\x12W\n\x12recognition_result\x18\x01 \x01(\x0b29.google.cloud.dialogflow.cx.v3.StreamingRecognitionResultH\x00\x12U\n\x16detect_intent_response\x18\x02 \x01(\x0b23.google.cloud.dialogflow.cx.v3.DetectIntentResponseH\x00\x12U\n\x0edebugging_info\x18\x04 \x01(\x0b2=.google.cloud.dialogflow.cx.v3.CloudConversationDebuggingInfoB\n\n\x08response"\xb6\x03\n\x1aStreamingRecognitionResult\x12[\n\x0cmessage_type\x18\x01 \x01(\x0e2E.google.cloud.dialogflow.cx.v3.StreamingRecognitionResult.MessageType\x12\x12\n\ntranscript\x18\x02 \x01(\t\x12\x10\n\x08is_final\x18\x03 \x01(\x08\x12\x12\n\nconfidence\x18\x04 \x01(\x02\x12\x11\n\tstability\x18\x06 \x01(\x02\x12G\n\x10speech_word_info\x18\x07 \x03(\x0b2-.google.cloud.dialogflow.cx.v3.SpeechWordInfo\x124\n\x11speech_end_offset\x18\x08 \x01(\x0b2\x19.google.protobuf.Duration\x12\x15\n\rlanguage_code\x18\n \x01(\t"X\n\x0bMessageType\x12\x1c\n\x18MESSAGE_TYPE_UNSPECIFIED\x10\x00\x12\x0e\n\nTRANSCRIPT\x10\x01\x12\x1b\n\x17END_OF_SINGLE_UTTERANCE\x10\x02"\xc0\x06\n\x0fQueryParameters\x12\x11\n\ttime_zone\x18\x01 \x01(\t\x12)\n\x0cgeo_location\x18\x02 \x01(\x0b2\x13.google.type.LatLng\x12N\n\x14session_entity_types\x18\x03 \x03(\x0b20.google.cloud.dialogflow.cx.v3.SessionEntityType\x12(\n\x07payload\x18\x04 \x01(\x0b2\x17.google.protobuf.Struct\x12+\n\nparameters\x18\x05 \x01(\x0b2\x17.google.protobuf.Struct\x129\n\x0ccurrent_page\x18\x06 \x01(\tB#\xfaA \n\x1edialogflow.googleapis.com/Page\x12\x17\n\x0fdisable_webhook\x18\x07 \x01(\x08\x12$\n\x1canalyze_query_text_sentiment\x18\x08 \x01(\x08\x12[\n\x0fwebhook_headers\x18\n \x03(\x0b2B.google.cloud.dialogflow.cx.v3.QueryParameters.WebhookHeadersEntry\x12=\n\rflow_versions\x18\x0e \x03(\tB&\xfaA#\n!dialogflow.googleapis.com/Version\x12\x0f\n\x07channel\x18\x0f \x01(\t\x123\n\x0bsession_ttl\x18\x10 \x01(\x0b2\x19.google.protobuf.DurationB\x03\xe0A\x01\x127\n\x11end_user_metadata\x18\x12 \x01(\x0b2\x17.google.protobuf.StructB\x03\xe0A\x01\x12G\n\rsearch_config\x18\x14 \x01(\x0b2+.google.cloud.dialogflow.cx.v3.SearchConfigB\x03\xe0A\x01\x123\n&populate_data_store_connection_signals\x18\x19 \x01(\x08B\x03\xe0A\x01\x1a5\n\x13WebhookHeadersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"\x9a\x01\n\x0cSearchConfig\x12C\n\x0bboost_specs\x18\x01 \x03(\x0b2).google.cloud.dialogflow.cx.v3.BoostSpecsB\x03\xe0A\x01\x12E\n\x0cfilter_specs\x18\x02 \x03(\x0b2*.google.cloud.dialogflow.cx.v3.FilterSpecsB\x03\xe0A\x01"\x9b\x07\n\tBoostSpec\x12_\n\x15condition_boost_specs\x18\x01 \x03(\x0b2;.google.cloud.dialogflow.cx.v3.BoostSpec.ConditionBoostSpecB\x03\xe0A\x01\x1a\xac\x06\n\x12ConditionBoostSpec\x12\x16\n\tcondition\x18\x01 \x01(\tB\x03\xe0A\x01\x12\x12\n\x05boost\x18\x02 \x01(\x02B\x03\xe0A\x01\x12m\n\x12boost_control_spec\x18\x04 \x01(\x0b2L.google.cloud.dialogflow.cx.v3.BoostSpec.ConditionBoostSpec.BoostControlSpecB\x03\xe0A\x01\x1a\xfa\x04\n\x10BoostControlSpec\x12\x17\n\nfield_name\x18\x01 \x01(\tB\x03\xe0A\x01\x12w\n\x0eattribute_type\x18\x02 \x01(\x0e2Z.google.cloud.dialogflow.cx.v3.BoostSpec.ConditionBoostSpec.BoostControlSpec.AttributeTypeB\x03\xe0A\x01\x12\x7f\n\x12interpolation_type\x18\x03 \x01(\x0e2^.google.cloud.dialogflow.cx.v3.BoostSpec.ConditionBoostSpec.BoostControlSpec.InterpolationTypeB\x03\xe0A\x01\x12v\n\x0econtrol_points\x18\x04 \x03(\x0b2Y.google.cloud.dialogflow.cx.v3.BoostSpec.ConditionBoostSpec.BoostControlSpec.ControlPointB\x03\xe0A\x01\x1aG\n\x0cControlPoint\x12\x1c\n\x0fattribute_value\x18\x01 \x01(\tB\x03\xe0A\x01\x12\x19\n\x0cboost_amount\x18\x02 \x01(\x02B\x03\xe0A\x01"M\n\rAttributeType\x12\x1e\n\x1aATTRIBUTE_TYPE_UNSPECIFIED\x10\x00\x12\r\n\tNUMERICAL\x10\x01\x12\r\n\tFRESHNESS\x10\x02"C\n\x11InterpolationType\x12"\n\x1eINTERPOLATION_TYPE_UNSPECIFIED\x10\x00\x12\n\n\x06LINEAR\x10\x01"\x90\x01\n\nBoostSpecs\x12E\n\x0bdata_stores\x18\x01 \x03(\tB0\xe0A\x01\xfaA*\n(discoveryengine.googleapis.com/DataStore\x12;\n\x04spec\x18\x02 \x03(\x0b2(.google.cloud.dialogflow.cx.v3.BoostSpecB\x03\xe0A\x01"i\n\x0bFilterSpecs\x12E\n\x0bdata_stores\x18\x01 \x03(\tB0\xe0A\x01\xfaA*\n(discoveryengine.googleapis.com/DataStore\x12\x13\n\x06filter\x18\x02 \x01(\tB\x03\xe0A\x01"\xdb\x02\n\nQueryInput\x128\n\x04text\x18\x02 \x01(\x0b2(.google.cloud.dialogflow.cx.v3.TextInputH\x00\x12<\n\x06intent\x18\x03 \x01(\x0b2*.google.cloud.dialogflow.cx.v3.IntentInputH\x00\x12:\n\x05audio\x18\x05 \x01(\x0b2).google.cloud.dialogflow.cx.v3.AudioInputH\x00\x12:\n\x05event\x18\x06 \x01(\x0b2).google.cloud.dialogflow.cx.v3.EventInputH\x00\x128\n\x04dtmf\x18\x07 \x01(\x0b2(.google.cloud.dialogflow.cx.v3.DtmfInputH\x00\x12\x1a\n\rlanguage_code\x18\x04 \x01(\tB\x03\xe0A\x02B\x07\n\x05input"\xae\t\n\x0bQueryResult\x12\x0e\n\x04text\x18\x01 \x01(\tH\x00\x12?\n\x0etrigger_intent\x18\x0b \x01(\tB%\xfaA"\n dialogflow.googleapis.com/IntentH\x00\x12\x14\n\ntranscript\x18\x0c \x01(\tH\x00\x12\x17\n\rtrigger_event\x18\x0e \x01(\tH\x00\x128\n\x04dtmf\x18\x17 \x01(\x0b2(.google.cloud.dialogflow.cx.v3.DtmfInputH\x00\x12\x15\n\rlanguage_code\x18\x02 \x01(\t\x12+\n\nparameters\x18\x03 \x01(\x0b2\x17.google.protobuf.Struct\x12I\n\x11response_messages\x18\x04 \x03(\x0b2..google.cloud.dialogflow.cx.v3.ResponseMessage\x12\x13\n\x0bwebhook_ids\x18\x19 \x03(\t\x12\x1d\n\x15webhook_display_names\x18\x1a \x03(\t\x124\n\x11webhook_latencies\x18\x1b \x03(\x0b2\x19.google.protobuf.Duration\x12\x14\n\x0cwebhook_tags\x18\x1d \x03(\t\x12,\n\x10webhook_statuses\x18\r \x03(\x0b2\x12.google.rpc.Status\x121\n\x10webhook_payloads\x18\x06 \x03(\x0b2\x17.google.protobuf.Struct\x129\n\x0ccurrent_page\x18\x07 \x01(\x0b2#.google.cloud.dialogflow.cx.v3.Page\x129\n\x0ccurrent_flow\x18\x1f \x01(\x0b2#.google.cloud.dialogflow.cx.v3.Flow\x129\n\x06intent\x18\x08 \x01(\x0b2%.google.cloud.dialogflow.cx.v3.IntentB\x02\x18\x01\x12\'\n\x1bintent_detection_confidence\x18\t \x01(\x02B\x02\x18\x01\x123\n\x05match\x18\x0f \x01(\x0b2$.google.cloud.dialogflow.cx.v3.Match\x120\n\x0fdiagnostic_info\x18\n \x01(\x0b2\x17.google.protobuf.Struct\x12Y\n\x19sentiment_analysis_result\x18\x11 \x01(\x0b26.google.cloud.dialogflow.cx.v3.SentimentAnalysisResult\x12J\n\x11advanced_settings\x18\x15 \x01(\x0b2/.google.cloud.dialogflow.cx.v3.AdvancedSettings\x12\x1d\n\x15allow_answer_feedback\x18  \x01(\x08\x12e\n\x1ddata_store_connection_signals\x18# \x01(\x0b29.google.cloud.dialogflow.cx.v3.DataStoreConnectionSignalsB\x03\xe0A\x01B\x07\n\x05query"\x1e\n\tTextInput\x12\x11\n\x04text\x18\x01 \x01(\tB\x03\xe0A\x02"G\n\x0bIntentInput\x128\n\x06intent\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n dialogflow.googleapis.com/Intent"a\n\nAudioInput\x12D\n\x06config\x18\x01 \x01(\x0b2/.google.cloud.dialogflow.cx.v3.InputAudioConfigB\x03\xe0A\x02\x12\r\n\x05audio\x18\x02 \x01(\x0c"\x1b\n\nEventInput\x12\r\n\x05event\x18\x01 \x01(\t"1\n\tDtmfInput\x12\x0e\n\x06digits\x18\x01 \x01(\t\x12\x14\n\x0cfinish_digit\x18\x02 \x01(\t"\x98\x03\n\x05Match\x125\n\x06intent\x18\x01 \x01(\x0b2%.google.cloud.dialogflow.cx.v3.Intent\x12\r\n\x05event\x18\x06 \x01(\t\x12+\n\nparameters\x18\x02 \x01(\x0b2\x17.google.protobuf.Struct\x12\x16\n\x0eresolved_input\x18\x03 \x01(\t\x12B\n\nmatch_type\x18\x04 \x01(\x0e2..google.cloud.dialogflow.cx.v3.Match.MatchType\x12\x12\n\nconfidence\x18\x05 \x01(\x02"\xab\x01\n\tMatchType\x12\x1a\n\x16MATCH_TYPE_UNSPECIFIED\x10\x00\x12\n\n\x06INTENT\x10\x01\x12\x11\n\rDIRECT_INTENT\x10\x02\x12\x15\n\x11PARAMETER_FILLING\x10\x03\x12\x0c\n\x08NO_MATCH\x10\x04\x12\x0c\n\x08NO_INPUT\x10\x05\x12\t\n\x05EVENT\x10\x06\x12\x17\n\x13KNOWLEDGE_CONNECTOR\x10\x08\x12\x0c\n\x08PLAYBOOK\x10\t"\xfe\x01\n\x12MatchIntentRequest\x12:\n\x07session\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!dialogflow.googleapis.com/Session\x12D\n\x0cquery_params\x18\x02 \x01(\x0b2..google.cloud.dialogflow.cx.v3.QueryParameters\x12C\n\x0bquery_input\x18\x03 \x01(\x0b2).google.cloud.dialogflow.cx.v3.QueryInputB\x03\xe0A\x02\x12!\n\x19persist_parameter_changes\x18\x05 \x01(\x08"\x90\x02\n\x13MatchIntentResponse\x12\x0e\n\x04text\x18\x01 \x01(\tH\x00\x12?\n\x0etrigger_intent\x18\x02 \x01(\tB%\xfaA"\n dialogflow.googleapis.com/IntentH\x00\x12\x14\n\ntranscript\x18\x03 \x01(\tH\x00\x12\x17\n\rtrigger_event\x18\x06 \x01(\tH\x00\x125\n\x07matches\x18\x04 \x03(\x0b2$.google.cloud.dialogflow.cx.v3.Match\x129\n\x0ccurrent_page\x18\x05 \x01(\x0b2#.google.cloud.dialogflow.cx.v3.PageB\x07\n\x05query"\xeb\x01\n\x14FulfillIntentRequest\x12O\n\x14match_intent_request\x18\x01 \x01(\x0b21.google.cloud.dialogflow.cx.v3.MatchIntentRequest\x123\n\x05match\x18\x02 \x01(\x0b2$.google.cloud.dialogflow.cx.v3.Match\x12M\n\x13output_audio_config\x18\x03 \x01(\x0b20.google.cloud.dialogflow.cx.v3.OutputAudioConfig"\xd3\x01\n\x15FulfillIntentResponse\x12\x13\n\x0bresponse_id\x18\x01 \x01(\t\x12@\n\x0cquery_result\x18\x02 \x01(\x0b2*.google.cloud.dialogflow.cx.v3.QueryResult\x12\x14\n\x0coutput_audio\x18\x03 \x01(\x0c\x12M\n\x13output_audio_config\x18\x04 \x01(\x0b20.google.cloud.dialogflow.cx.v3.OutputAudioConfig";\n\x17SentimentAnalysisResult\x12\r\n\x05score\x18\x01 \x01(\x02\x12\x11\n\tmagnitude\x18\x02 \x01(\x022\xfa\r\n\x08Sessions\x12\xa6\x02\n\x0cDetectIntent\x122.google.cloud.dialogflow.cx.v3.DetectIntentRequest\x1a3.google.cloud.dialogflow.cx.v3.DetectIntentResponse"\xac\x01\x82\xd3\xe4\x93\x02\xa5\x01"E/v3/{session=projects/*/locations/*/agents/*/sessions/*}:detectIntent:\x01*ZY"T/v3/{session=projects/*/locations/*/agents/*/environments/*/sessions/*}:detectIntent:\x01*\x12\xd5\x02\n\x1bServerStreamingDetectIntent\x122.google.cloud.dialogflow.cx.v3.DetectIntentRequest\x1a3.google.cloud.dialogflow.cx.v3.DetectIntentResponse"\xca\x01\x82\xd3\xe4\x93\x02\xc3\x01"T/v3/{session=projects/*/locations/*/agents/*/sessions/*}:serverStreamingDetectIntent:\x01*Zh"c/v3/{session=projects/*/locations/*/agents/*/environments/*/sessions/*}:serverStreamingDetectIntent:\x01*0\x01\x12\x98\x01\n\x15StreamingDetectIntent\x12;.google.cloud.dialogflow.cx.v3.StreamingDetectIntentRequest\x1a<.google.cloud.dialogflow.cx.v3.StreamingDetectIntentResponse"\x00(\x010\x01\x12\xa1\x02\n\x0bMatchIntent\x121.google.cloud.dialogflow.cx.v3.MatchIntentRequest\x1a2.google.cloud.dialogflow.cx.v3.MatchIntentResponse"\xaa\x01\x82\xd3\xe4\x93\x02\xa3\x01"D/v3/{session=projects/*/locations/*/agents/*/sessions/*}:matchIntent:\x01*ZX"S/v3/{session=projects/*/locations/*/agents/*/environments/*/sessions/*}:matchIntent:\x01*\x12\xd5\x02\n\rFulfillIntent\x123.google.cloud.dialogflow.cx.v3.FulfillIntentRequest\x1a4.google.cloud.dialogflow.cx.v3.FulfillIntentResponse"\xd8\x01\x82\xd3\xe4\x93\x02\xd1\x01"[/v3/{match_intent_request.session=projects/*/locations/*/agents/*/sessions/*}:fulfillIntent:\x01*Zo"j/v3/{match_intent_request.session=projects/*/locations/*/agents/*/environments/*/sessions/*}:fulfillIntent:\x01*\x12\xdb\x01\n\x14SubmitAnswerFeedback\x12:.google.cloud.dialogflow.cx.v3.SubmitAnswerFeedbackRequest\x1a-.google.cloud.dialogflow.cx.v3.AnswerFeedback"X\x82\xd3\xe4\x93\x02R"M/v3/{session=projects/*/locations/*/agents/*/sessions/*}:submitAnswerFeedback:\x01*\x1ax\xcaA\x19dialogflow.googleapis.com\xd2AYhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflowB\xd0\x04\n!com.google.cloud.dialogflow.cx.v3B\x0cSessionProtoP\x01Z1cloud.google.com/go/dialogflow/cx/apiv3/cxpb;cxpb\xa2\x02\x02DF\xaa\x02\x1dGoogle.Cloud.Dialogflow.Cx.V3\xea\x02!Google::Cloud::Dialogflow::CX::V3\xeaA\xd4\x01\n!dialogflow.googleapis.com/Session\x12Iprojects/{project}/locations/{location}/agents/{agent}/sessions/{session}\x12dprojects/{project}/locations/{location}/agents/{agent}/environments/{environment}/sessions/{session}\xeaA\xc5\x01\n(discoveryengine.googleapis.com/DataStore\x12?projects/{project}/locations/{location}/dataStores/{data_store}\x12Xprojects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.dialogflow.cx.v3.session_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n!com.google.cloud.dialogflow.cx.v3B\x0cSessionProtoP\x01Z1cloud.google.com/go/dialogflow/cx/apiv3/cxpb;cxpb\xa2\x02\x02DF\xaa\x02\x1dGoogle.Cloud.Dialogflow.Cx.V3\xea\x02!Google::Cloud::Dialogflow::CX::V3\xeaA\xd4\x01\n!dialogflow.googleapis.com/Session\x12Iprojects/{project}/locations/{location}/agents/{agent}/sessions/{session}\x12dprojects/{project}/locations/{location}/agents/{agent}/environments/{environment}/sessions/{session}\xeaA\xc5\x01\n(discoveryengine.googleapis.com/DataStore\x12?projects/{project}/locations/{location}/dataStores/{data_store}\x12Xprojects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}'
    _globals['_ANSWERFEEDBACK_RATINGREASON'].fields_by_name['reason_labels']._loaded_options = None
    _globals['_ANSWERFEEDBACK_RATINGREASON'].fields_by_name['reason_labels']._serialized_options = b'\xe0A\x01'
    _globals['_ANSWERFEEDBACK_RATINGREASON'].fields_by_name['feedback']._loaded_options = None
    _globals['_ANSWERFEEDBACK_RATINGREASON'].fields_by_name['feedback']._serialized_options = b'\xe0A\x01'
    _globals['_ANSWERFEEDBACK'].fields_by_name['rating']._loaded_options = None
    _globals['_ANSWERFEEDBACK'].fields_by_name['rating']._serialized_options = b'\xe0A\x01'
    _globals['_ANSWERFEEDBACK'].fields_by_name['rating_reason']._loaded_options = None
    _globals['_ANSWERFEEDBACK'].fields_by_name['rating_reason']._serialized_options = b'\xe0A\x01'
    _globals['_ANSWERFEEDBACK'].fields_by_name['custom_rating']._loaded_options = None
    _globals['_ANSWERFEEDBACK'].fields_by_name['custom_rating']._serialized_options = b'\xe0A\x01'
    _globals['_SUBMITANSWERFEEDBACKREQUEST'].fields_by_name['session']._loaded_options = None
    _globals['_SUBMITANSWERFEEDBACKREQUEST'].fields_by_name['session']._serialized_options = b'\xe0A\x02\xfaA#\n!dialogflow.googleapis.com/Session'
    _globals['_SUBMITANSWERFEEDBACKREQUEST'].fields_by_name['response_id']._loaded_options = None
    _globals['_SUBMITANSWERFEEDBACKREQUEST'].fields_by_name['response_id']._serialized_options = b'\xe0A\x02'
    _globals['_SUBMITANSWERFEEDBACKREQUEST'].fields_by_name['answer_feedback']._loaded_options = None
    _globals['_SUBMITANSWERFEEDBACKREQUEST'].fields_by_name['answer_feedback']._serialized_options = b'\xe0A\x02'
    _globals['_SUBMITANSWERFEEDBACKREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_SUBMITANSWERFEEDBACKREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x01'
    _globals['_DETECTINTENTREQUEST'].fields_by_name['session']._loaded_options = None
    _globals['_DETECTINTENTREQUEST'].fields_by_name['session']._serialized_options = b'\xe0A\x02\xfaA#\n!dialogflow.googleapis.com/Session'
    _globals['_DETECTINTENTREQUEST'].fields_by_name['query_input']._loaded_options = None
    _globals['_DETECTINTENTREQUEST'].fields_by_name['query_input']._serialized_options = b'\xe0A\x02'
    _globals['_STREAMINGDETECTINTENTREQUEST'].fields_by_name['session']._loaded_options = None
    _globals['_STREAMINGDETECTINTENTREQUEST'].fields_by_name['session']._serialized_options = b'\xfaA#\n!dialogflow.googleapis.com/Session'
    _globals['_STREAMINGDETECTINTENTREQUEST'].fields_by_name['query_input']._loaded_options = None
    _globals['_STREAMINGDETECTINTENTREQUEST'].fields_by_name['query_input']._serialized_options = b'\xe0A\x02'
    _globals['_QUERYPARAMETERS_WEBHOOKHEADERSENTRY']._loaded_options = None
    _globals['_QUERYPARAMETERS_WEBHOOKHEADERSENTRY']._serialized_options = b'8\x01'
    _globals['_QUERYPARAMETERS'].fields_by_name['current_page']._loaded_options = None
    _globals['_QUERYPARAMETERS'].fields_by_name['current_page']._serialized_options = b'\xfaA \n\x1edialogflow.googleapis.com/Page'
    _globals['_QUERYPARAMETERS'].fields_by_name['flow_versions']._loaded_options = None
    _globals['_QUERYPARAMETERS'].fields_by_name['flow_versions']._serialized_options = b'\xfaA#\n!dialogflow.googleapis.com/Version'
    _globals['_QUERYPARAMETERS'].fields_by_name['session_ttl']._loaded_options = None
    _globals['_QUERYPARAMETERS'].fields_by_name['session_ttl']._serialized_options = b'\xe0A\x01'
    _globals['_QUERYPARAMETERS'].fields_by_name['end_user_metadata']._loaded_options = None
    _globals['_QUERYPARAMETERS'].fields_by_name['end_user_metadata']._serialized_options = b'\xe0A\x01'
    _globals['_QUERYPARAMETERS'].fields_by_name['search_config']._loaded_options = None
    _globals['_QUERYPARAMETERS'].fields_by_name['search_config']._serialized_options = b'\xe0A\x01'
    _globals['_QUERYPARAMETERS'].fields_by_name['populate_data_store_connection_signals']._loaded_options = None
    _globals['_QUERYPARAMETERS'].fields_by_name['populate_data_store_connection_signals']._serialized_options = b'\xe0A\x01'
    _globals['_SEARCHCONFIG'].fields_by_name['boost_specs']._loaded_options = None
    _globals['_SEARCHCONFIG'].fields_by_name['boost_specs']._serialized_options = b'\xe0A\x01'
    _globals['_SEARCHCONFIG'].fields_by_name['filter_specs']._loaded_options = None
    _globals['_SEARCHCONFIG'].fields_by_name['filter_specs']._serialized_options = b'\xe0A\x01'
    _globals['_BOOSTSPEC_CONDITIONBOOSTSPEC_BOOSTCONTROLSPEC_CONTROLPOINT'].fields_by_name['attribute_value']._loaded_options = None
    _globals['_BOOSTSPEC_CONDITIONBOOSTSPEC_BOOSTCONTROLSPEC_CONTROLPOINT'].fields_by_name['attribute_value']._serialized_options = b'\xe0A\x01'
    _globals['_BOOSTSPEC_CONDITIONBOOSTSPEC_BOOSTCONTROLSPEC_CONTROLPOINT'].fields_by_name['boost_amount']._loaded_options = None
    _globals['_BOOSTSPEC_CONDITIONBOOSTSPEC_BOOSTCONTROLSPEC_CONTROLPOINT'].fields_by_name['boost_amount']._serialized_options = b'\xe0A\x01'
    _globals['_BOOSTSPEC_CONDITIONBOOSTSPEC_BOOSTCONTROLSPEC'].fields_by_name['field_name']._loaded_options = None
    _globals['_BOOSTSPEC_CONDITIONBOOSTSPEC_BOOSTCONTROLSPEC'].fields_by_name['field_name']._serialized_options = b'\xe0A\x01'
    _globals['_BOOSTSPEC_CONDITIONBOOSTSPEC_BOOSTCONTROLSPEC'].fields_by_name['attribute_type']._loaded_options = None
    _globals['_BOOSTSPEC_CONDITIONBOOSTSPEC_BOOSTCONTROLSPEC'].fields_by_name['attribute_type']._serialized_options = b'\xe0A\x01'
    _globals['_BOOSTSPEC_CONDITIONBOOSTSPEC_BOOSTCONTROLSPEC'].fields_by_name['interpolation_type']._loaded_options = None
    _globals['_BOOSTSPEC_CONDITIONBOOSTSPEC_BOOSTCONTROLSPEC'].fields_by_name['interpolation_type']._serialized_options = b'\xe0A\x01'
    _globals['_BOOSTSPEC_CONDITIONBOOSTSPEC_BOOSTCONTROLSPEC'].fields_by_name['control_points']._loaded_options = None
    _globals['_BOOSTSPEC_CONDITIONBOOSTSPEC_BOOSTCONTROLSPEC'].fields_by_name['control_points']._serialized_options = b'\xe0A\x01'
    _globals['_BOOSTSPEC_CONDITIONBOOSTSPEC'].fields_by_name['condition']._loaded_options = None
    _globals['_BOOSTSPEC_CONDITIONBOOSTSPEC'].fields_by_name['condition']._serialized_options = b'\xe0A\x01'
    _globals['_BOOSTSPEC_CONDITIONBOOSTSPEC'].fields_by_name['boost']._loaded_options = None
    _globals['_BOOSTSPEC_CONDITIONBOOSTSPEC'].fields_by_name['boost']._serialized_options = b'\xe0A\x01'
    _globals['_BOOSTSPEC_CONDITIONBOOSTSPEC'].fields_by_name['boost_control_spec']._loaded_options = None
    _globals['_BOOSTSPEC_CONDITIONBOOSTSPEC'].fields_by_name['boost_control_spec']._serialized_options = b'\xe0A\x01'
    _globals['_BOOSTSPEC'].fields_by_name['condition_boost_specs']._loaded_options = None
    _globals['_BOOSTSPEC'].fields_by_name['condition_boost_specs']._serialized_options = b'\xe0A\x01'
    _globals['_BOOSTSPECS'].fields_by_name['data_stores']._loaded_options = None
    _globals['_BOOSTSPECS'].fields_by_name['data_stores']._serialized_options = b'\xe0A\x01\xfaA*\n(discoveryengine.googleapis.com/DataStore'
    _globals['_BOOSTSPECS'].fields_by_name['spec']._loaded_options = None
    _globals['_BOOSTSPECS'].fields_by_name['spec']._serialized_options = b'\xe0A\x01'
    _globals['_FILTERSPECS'].fields_by_name['data_stores']._loaded_options = None
    _globals['_FILTERSPECS'].fields_by_name['data_stores']._serialized_options = b'\xe0A\x01\xfaA*\n(discoveryengine.googleapis.com/DataStore'
    _globals['_FILTERSPECS'].fields_by_name['filter']._loaded_options = None
    _globals['_FILTERSPECS'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_QUERYINPUT'].fields_by_name['language_code']._loaded_options = None
    _globals['_QUERYINPUT'].fields_by_name['language_code']._serialized_options = b'\xe0A\x02'
    _globals['_QUERYRESULT'].fields_by_name['trigger_intent']._loaded_options = None
    _globals['_QUERYRESULT'].fields_by_name['trigger_intent']._serialized_options = b'\xfaA"\n dialogflow.googleapis.com/Intent'
    _globals['_QUERYRESULT'].fields_by_name['intent']._loaded_options = None
    _globals['_QUERYRESULT'].fields_by_name['intent']._serialized_options = b'\x18\x01'
    _globals['_QUERYRESULT'].fields_by_name['intent_detection_confidence']._loaded_options = None
    _globals['_QUERYRESULT'].fields_by_name['intent_detection_confidence']._serialized_options = b'\x18\x01'
    _globals['_QUERYRESULT'].fields_by_name['data_store_connection_signals']._loaded_options = None
    _globals['_QUERYRESULT'].fields_by_name['data_store_connection_signals']._serialized_options = b'\xe0A\x01'
    _globals['_TEXTINPUT'].fields_by_name['text']._loaded_options = None
    _globals['_TEXTINPUT'].fields_by_name['text']._serialized_options = b'\xe0A\x02'
    _globals['_INTENTINPUT'].fields_by_name['intent']._loaded_options = None
    _globals['_INTENTINPUT'].fields_by_name['intent']._serialized_options = b'\xe0A\x02\xfaA"\n dialogflow.googleapis.com/Intent'
    _globals['_AUDIOINPUT'].fields_by_name['config']._loaded_options = None
    _globals['_AUDIOINPUT'].fields_by_name['config']._serialized_options = b'\xe0A\x02'
    _globals['_MATCHINTENTREQUEST'].fields_by_name['session']._loaded_options = None
    _globals['_MATCHINTENTREQUEST'].fields_by_name['session']._serialized_options = b'\xe0A\x02\xfaA#\n!dialogflow.googleapis.com/Session'
    _globals['_MATCHINTENTREQUEST'].fields_by_name['query_input']._loaded_options = None
    _globals['_MATCHINTENTREQUEST'].fields_by_name['query_input']._serialized_options = b'\xe0A\x02'
    _globals['_MATCHINTENTRESPONSE'].fields_by_name['trigger_intent']._loaded_options = None
    _globals['_MATCHINTENTRESPONSE'].fields_by_name['trigger_intent']._serialized_options = b'\xfaA"\n dialogflow.googleapis.com/Intent'
    _globals['_SESSIONS']._loaded_options = None
    _globals['_SESSIONS']._serialized_options = b'\xcaA\x19dialogflow.googleapis.com\xd2AYhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflow'
    _globals['_SESSIONS'].methods_by_name['DetectIntent']._loaded_options = None
    _globals['_SESSIONS'].methods_by_name['DetectIntent']._serialized_options = b'\x82\xd3\xe4\x93\x02\xa5\x01"E/v3/{session=projects/*/locations/*/agents/*/sessions/*}:detectIntent:\x01*ZY"T/v3/{session=projects/*/locations/*/agents/*/environments/*/sessions/*}:detectIntent:\x01*'
    _globals['_SESSIONS'].methods_by_name['ServerStreamingDetectIntent']._loaded_options = None
    _globals['_SESSIONS'].methods_by_name['ServerStreamingDetectIntent']._serialized_options = b'\x82\xd3\xe4\x93\x02\xc3\x01"T/v3/{session=projects/*/locations/*/agents/*/sessions/*}:serverStreamingDetectIntent:\x01*Zh"c/v3/{session=projects/*/locations/*/agents/*/environments/*/sessions/*}:serverStreamingDetectIntent:\x01*'
    _globals['_SESSIONS'].methods_by_name['MatchIntent']._loaded_options = None
    _globals['_SESSIONS'].methods_by_name['MatchIntent']._serialized_options = b'\x82\xd3\xe4\x93\x02\xa3\x01"D/v3/{session=projects/*/locations/*/agents/*/sessions/*}:matchIntent:\x01*ZX"S/v3/{session=projects/*/locations/*/agents/*/environments/*/sessions/*}:matchIntent:\x01*'
    _globals['_SESSIONS'].methods_by_name['FulfillIntent']._loaded_options = None
    _globals['_SESSIONS'].methods_by_name['FulfillIntent']._serialized_options = b'\x82\xd3\xe4\x93\x02\xd1\x01"[/v3/{match_intent_request.session=projects/*/locations/*/agents/*/sessions/*}:fulfillIntent:\x01*Zo"j/v3/{match_intent_request.session=projects/*/locations/*/agents/*/environments/*/sessions/*}:fulfillIntent:\x01*'
    _globals['_SESSIONS'].methods_by_name['SubmitAnswerFeedback']._loaded_options = None
    _globals['_SESSIONS'].methods_by_name['SubmitAnswerFeedback']._serialized_options = b'\x82\xd3\xe4\x93\x02R"M/v3/{session=projects/*/locations/*/agents/*/sessions/*}:submitAnswerFeedback:\x01*'
    _globals['_ANSWERFEEDBACK']._serialized_start = 744
    _globals['_ANSWERFEEDBACK']._serialized_end = 1084
    _globals['_ANSWERFEEDBACK_RATINGREASON']._serialized_start = 953
    _globals['_ANSWERFEEDBACK_RATINGREASON']._serialized_end = 1018
    _globals['_ANSWERFEEDBACK_RATING']._serialized_start = 1020
    _globals['_ANSWERFEEDBACK_RATING']._serialized_end = 1084
    _globals['_SUBMITANSWERFEEDBACKREQUEST']._serialized_start = 1087
    _globals['_SUBMITANSWERFEEDBACKREQUEST']._serialized_end = 1333
    _globals['_DETECTINTENTREQUEST']._serialized_start = 1336
    _globals['_DETECTINTENTREQUEST']._serialized_end = 1635
    _globals['_DETECTINTENTRESPONSE']._serialized_start = 1638
    _globals['_DETECTINTENTRESPONSE']._serialized_end = 2036
    _globals['_DETECTINTENTRESPONSE_RESPONSETYPE']._serialized_start = 1967
    _globals['_DETECTINTENTRESPONSE_RESPONSETYPE']._serialized_end = 2036
    _globals['_STREAMINGDETECTINTENTREQUEST']._serialized_start = 2039
    _globals['_STREAMINGDETECTINTENTREQUEST']._serialized_end = 2408
    _globals['_CLOUDCONVERSATIONDEBUGGINGINFO']._serialized_start = 2411
    _globals['_CLOUDCONVERSATIONDEBUGGINGINFO']._serialized_end = 3355
    _globals['_STREAMINGDETECTINTENTRESPONSE']._serialized_start = 3358
    _globals['_STREAMINGDETECTINTENTRESPONSE']._serialized_end = 3664
    _globals['_STREAMINGRECOGNITIONRESULT']._serialized_start = 3667
    _globals['_STREAMINGRECOGNITIONRESULT']._serialized_end = 4105
    _globals['_STREAMINGRECOGNITIONRESULT_MESSAGETYPE']._serialized_start = 4017
    _globals['_STREAMINGRECOGNITIONRESULT_MESSAGETYPE']._serialized_end = 4105
    _globals['_QUERYPARAMETERS']._serialized_start = 4108
    _globals['_QUERYPARAMETERS']._serialized_end = 4940
    _globals['_QUERYPARAMETERS_WEBHOOKHEADERSENTRY']._serialized_start = 4887
    _globals['_QUERYPARAMETERS_WEBHOOKHEADERSENTRY']._serialized_end = 4940
    _globals['_SEARCHCONFIG']._serialized_start = 4943
    _globals['_SEARCHCONFIG']._serialized_end = 5097
    _globals['_BOOSTSPEC']._serialized_start = 5100
    _globals['_BOOSTSPEC']._serialized_end = 6023
    _globals['_BOOSTSPEC_CONDITIONBOOSTSPEC']._serialized_start = 5211
    _globals['_BOOSTSPEC_CONDITIONBOOSTSPEC']._serialized_end = 6023
    _globals['_BOOSTSPEC_CONDITIONBOOSTSPEC_BOOSTCONTROLSPEC']._serialized_start = 5389
    _globals['_BOOSTSPEC_CONDITIONBOOSTSPEC_BOOSTCONTROLSPEC']._serialized_end = 6023
    _globals['_BOOSTSPEC_CONDITIONBOOSTSPEC_BOOSTCONTROLSPEC_CONTROLPOINT']._serialized_start = 5804
    _globals['_BOOSTSPEC_CONDITIONBOOSTSPEC_BOOSTCONTROLSPEC_CONTROLPOINT']._serialized_end = 5875
    _globals['_BOOSTSPEC_CONDITIONBOOSTSPEC_BOOSTCONTROLSPEC_ATTRIBUTETYPE']._serialized_start = 5877
    _globals['_BOOSTSPEC_CONDITIONBOOSTSPEC_BOOSTCONTROLSPEC_ATTRIBUTETYPE']._serialized_end = 5954
    _globals['_BOOSTSPEC_CONDITIONBOOSTSPEC_BOOSTCONTROLSPEC_INTERPOLATIONTYPE']._serialized_start = 5956
    _globals['_BOOSTSPEC_CONDITIONBOOSTSPEC_BOOSTCONTROLSPEC_INTERPOLATIONTYPE']._serialized_end = 6023
    _globals['_BOOSTSPECS']._serialized_start = 6026
    _globals['_BOOSTSPECS']._serialized_end = 6170
    _globals['_FILTERSPECS']._serialized_start = 6172
    _globals['_FILTERSPECS']._serialized_end = 6277
    _globals['_QUERYINPUT']._serialized_start = 6280
    _globals['_QUERYINPUT']._serialized_end = 6627
    _globals['_QUERYRESULT']._serialized_start = 6630
    _globals['_QUERYRESULT']._serialized_end = 7828
    _globals['_TEXTINPUT']._serialized_start = 7830
    _globals['_TEXTINPUT']._serialized_end = 7860
    _globals['_INTENTINPUT']._serialized_start = 7862
    _globals['_INTENTINPUT']._serialized_end = 7933
    _globals['_AUDIOINPUT']._serialized_start = 7935
    _globals['_AUDIOINPUT']._serialized_end = 8032
    _globals['_EVENTINPUT']._serialized_start = 8034
    _globals['_EVENTINPUT']._serialized_end = 8061
    _globals['_DTMFINPUT']._serialized_start = 8063
    _globals['_DTMFINPUT']._serialized_end = 8112
    _globals['_MATCH']._serialized_start = 8115
    _globals['_MATCH']._serialized_end = 8523
    _globals['_MATCH_MATCHTYPE']._serialized_start = 8352
    _globals['_MATCH_MATCHTYPE']._serialized_end = 8523
    _globals['_MATCHINTENTREQUEST']._serialized_start = 8526
    _globals['_MATCHINTENTREQUEST']._serialized_end = 8780
    _globals['_MATCHINTENTRESPONSE']._serialized_start = 8783
    _globals['_MATCHINTENTRESPONSE']._serialized_end = 9055
    _globals['_FULFILLINTENTREQUEST']._serialized_start = 9058
    _globals['_FULFILLINTENTREQUEST']._serialized_end = 9293
    _globals['_FULFILLINTENTRESPONSE']._serialized_start = 9296
    _globals['_FULFILLINTENTRESPONSE']._serialized_end = 9507
    _globals['_SENTIMENTANALYSISRESULT']._serialized_start = 9509
    _globals['_SENTIMENTANALYSISRESULT']._serialized_end = 9568
    _globals['_SESSIONS']._serialized_start = 9571
    _globals['_SESSIONS']._serialized_end = 11357