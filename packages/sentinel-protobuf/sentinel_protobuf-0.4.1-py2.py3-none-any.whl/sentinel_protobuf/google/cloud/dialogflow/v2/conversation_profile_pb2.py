"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/dialogflow/v2/conversation_profile.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.dialogflow.v2 import audio_config_pb2 as google_dot_cloud_dot_dialogflow_dot_v2_dot_audio__config__pb2
from .....google.cloud.dialogflow.v2 import participant_pb2 as google_dot_cloud_dot_dialogflow_dot_v2_dot_participant__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5google/cloud/dialogflow/v2/conversation_profile.proto\x12\x1agoogle.cloud.dialogflow.v2\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a-google/cloud/dialogflow/v2/audio_config.proto\x1a,google/cloud/dialogflow/v2/participant.proto\x1a#google/longrunning/operations.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xd9\t\n\x13ConversationProfile\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x02\x124\n\x0bcreate_time\x18\x0b \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x0c \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12P\n\x16automated_agent_config\x18\x03 \x01(\x0b20.google.cloud.dialogflow.v2.AutomatedAgentConfig\x12[\n\x1chuman_agent_assistant_config\x18\x04 \x01(\x0b25.google.cloud.dialogflow.v2.HumanAgentAssistantConfig\x12W\n\x1ahuman_agent_handoff_config\x18\x05 \x01(\x0b23.google.cloud.dialogflow.v2.HumanAgentHandoffConfig\x12K\n\x13notification_config\x18\x06 \x01(\x0b2..google.cloud.dialogflow.v2.NotificationConfig\x12A\n\x0elogging_config\x18\x07 \x01(\x0b2).google.cloud.dialogflow.v2.LoggingConfig\x12]\n%new_message_event_notification_config\x18\x08 \x01(\x0b2..google.cloud.dialogflow.v2.NotificationConfig\x12g\n*new_recognition_result_notification_config\x18\x15 \x01(\x0b2..google.cloud.dialogflow.v2.NotificationConfigB\x03\xe0A\x01\x12B\n\nstt_config\x18\t \x01(\x0b2..google.cloud.dialogflow.v2.SpeechToTextConfig\x12\x15\n\rlanguage_code\x18\n \x01(\t\x12\x11\n\ttime_zone\x18\x0e \x01(\t\x12L\n\x11security_settings\x18\r \x01(\tB1\xfaA.\n,dialogflow.googleapis.com/CXSecuritySettings\x12F\n\ntts_config\x18\x12 \x01(\x0b22.google.cloud.dialogflow.v2.SynthesizeSpeechConfig:\xc8\x01\xeaA\xc4\x01\n-dialogflow.googleapis.com/ConversationProfile\x12>projects/{project}/conversationProfiles/{conversation_profile}\x12Sprojects/{project}/locations/{location}/conversationProfiles/{conversation_profile}"\x8f\x01\n\x1fListConversationProfilesRequest\x12E\n\x06parent\x18\x01 \x01(\tB5\xe0A\x02\xfaA/\x12-dialogflow.googleapis.com/ConversationProfile\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"\x8b\x01\n ListConversationProfilesResponse\x12N\n\x15conversation_profiles\x18\x01 \x03(\x0b2/.google.cloud.dialogflow.v2.ConversationProfile\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"d\n\x1dGetConversationProfileRequest\x12C\n\x04name\x18\x01 \x01(\tB5\xe0A\x02\xfaA/\n-dialogflow.googleapis.com/ConversationProfile"\xbd\x01\n CreateConversationProfileRequest\x12E\n\x06parent\x18\x01 \x01(\tB5\xe0A\x02\xfaA/\x12-dialogflow.googleapis.com/ConversationProfile\x12R\n\x14conversation_profile\x18\x02 \x01(\x0b2/.google.cloud.dialogflow.v2.ConversationProfileB\x03\xe0A\x02"\xac\x01\n UpdateConversationProfileRequest\x12R\n\x14conversation_profile\x18\x01 \x01(\x0b2/.google.cloud.dialogflow.v2.ConversationProfileB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02"g\n DeleteConversationProfileRequest\x12C\n\x04name\x18\x01 \x01(\tB5\xe0A\x02\xfaA/\n-dialogflow.googleapis.com/ConversationProfile"\x83\x01\n\x14AutomatedAgentConfig\x126\n\x05agent\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1fdialogflow.googleapis.com/Agent\x123\n\x0bsession_ttl\x18\x03 \x01(\x0b2\x19.google.protobuf.DurationB\x03\xe0A\x01"\xd5\x1b\n\x19HumanAgentAssistantConfig\x12K\n\x13notification_config\x18\x02 \x01(\x0b2..google.cloud.dialogflow.v2.NotificationConfig\x12m\n\x1dhuman_agent_suggestion_config\x18\x03 \x01(\x0b2F.google.cloud.dialogflow.v2.HumanAgentAssistantConfig.SuggestionConfig\x12j\n\x1aend_user_suggestion_config\x18\x04 \x01(\x0b2F.google.cloud.dialogflow.v2.HumanAgentAssistantConfig.SuggestionConfig\x12l\n\x17message_analysis_config\x18\x05 \x01(\x0b2K.google.cloud.dialogflow.v2.HumanAgentAssistantConfig.MessageAnalysisConfig\x1aH\n\x19SuggestionTriggerSettings\x12\x14\n\x0cno_smalltalk\x18\x01 \x01(\x08\x12\x15\n\ronly_end_user\x18\x02 \x01(\x08\x1a\x88\x06\n\x17SuggestionFeatureConfig\x12I\n\x12suggestion_feature\x18\x05 \x01(\x0b2-.google.cloud.dialogflow.v2.SuggestionFeature\x12%\n\x1denable_event_based_suggestion\x18\x03 \x01(\x08\x12(\n\x1bdisable_agent_query_logging\x18\x0e \x01(\x08B\x03\xe0A\x01\x123\n&enable_query_suggestion_when_no_answer\x18\x0f \x01(\x08B\x03\xe0A\x01\x120\n#enable_conversation_augmented_query\x18\x10 \x01(\x08B\x03\xe0A\x01\x12)\n\x1cenable_query_suggestion_only\x18\x11 \x01(\x08B\x03\xe0A\x01\x12t\n\x1bsuggestion_trigger_settings\x18\n \x01(\x0b2O.google.cloud.dialogflow.v2.HumanAgentAssistantConfig.SuggestionTriggerSettings\x12a\n\x0cquery_config\x18\x06 \x01(\x0b2K.google.cloud.dialogflow.v2.HumanAgentAssistantConfig.SuggestionQueryConfig\x12p\n\x19conversation_model_config\x18\x07 \x01(\x0b2M.google.cloud.dialogflow.v2.HumanAgentAssistantConfig.ConversationModelConfig\x12t\n\x1bconversation_process_config\x18\x08 \x01(\x0b2O.google.cloud.dialogflow.v2.HumanAgentAssistantConfig.ConversationProcessConfig\x1a\x99\x02\n\x10SuggestionConfig\x12f\n\x0ffeature_configs\x18\x02 \x03(\x0b2M.google.cloud.dialogflow.v2.HumanAgentAssistantConfig.SuggestionFeatureConfig\x12"\n\x1agroup_suggestion_responses\x18\x03 \x01(\x08\x12?\n\ngenerators\x18\x04 \x03(\tB+\xe0A\x01\xfaA%\n#dialogflow.googleapis.com/Generator\x128\n+disable_high_latency_features_sync_delivery\x18\x05 \x01(\x08B\x03\xe0A\x01\x1a\x99\r\n\x15SuggestionQueryConfig\x12\x8b\x01\n\x1bknowledge_base_query_source\x18\x01 \x01(\x0b2d.google.cloud.dialogflow.v2.HumanAgentAssistantConfig.SuggestionQueryConfig.KnowledgeBaseQuerySourceH\x00\x12\x80\x01\n\x15document_query_source\x18\x02 \x01(\x0b2_.google.cloud.dialogflow.v2.HumanAgentAssistantConfig.SuggestionQueryConfig.DocumentQuerySourceH\x00\x12\x84\x01\n\x17dialogflow_query_source\x18\x03 \x01(\x0b2a.google.cloud.dialogflow.v2.HumanAgentAssistantConfig.SuggestionQueryConfig.DialogflowQuerySourceH\x00\x12\x13\n\x0bmax_results\x18\x04 \x01(\x05\x12\x1c\n\x14confidence_threshold\x18\x05 \x01(\x02\x12\x82\x01\n\x17context_filter_settings\x18\x07 \x01(\x0b2a.google.cloud.dialogflow.v2.HumanAgentAssistantConfig.SuggestionQueryConfig.ContextFilterSettings\x12k\n\x08sections\x18\x08 \x01(\x0b2T.google.cloud.dialogflow.v2.HumanAgentAssistantConfig.SuggestionQueryConfig.SectionsB\x03\xe0A\x01\x12\x19\n\x0ccontext_size\x18\t \x01(\x05B\x03\xe0A\x01\x1ad\n\x18KnowledgeBaseQuerySource\x12H\n\x0fknowledge_bases\x18\x01 \x03(\tB/\xe0A\x02\xfaA)\n\'dialogflow.googleapis.com/KnowledgeBase\x1aT\n\x13DocumentQuerySource\x12=\n\tdocuments\x18\x01 \x03(\tB*\xe0A\x02\xfaA$\n"dialogflow.googleapis.com/Document\x1a\xbe\x02\n\x15DialogflowQuerySource\x126\n\x05agent\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1fdialogflow.googleapis.com/Agent\x12\x9c\x01\n\x17human_agent_side_config\x18\x03 \x01(\x0b2v.google.cloud.dialogflow.v2.HumanAgentAssistantConfig.SuggestionQueryConfig.DialogflowQuerySource.HumanAgentSideConfigB\x03\xe0A\x01\x1aN\n\x14HumanAgentSideConfig\x126\n\x05agent\x18\x01 \x01(\tB\'\xe0A\x01\xfaA!\n\x1fdialogflow.googleapis.com/Agent\x1av\n\x15ContextFilterSettings\x12\x1d\n\x15drop_handoff_messages\x18\x01 \x01(\x08\x12#\n\x1bdrop_virtual_agent_messages\x18\x02 \x01(\x08\x12\x19\n\x11drop_ivr_messages\x18\x03 \x01(\x08\x1a\xa2\x02\n\x08Sections\x12w\n\rsection_types\x18\x01 \x03(\x0e2`.google.cloud.dialogflow.v2.HumanAgentAssistantConfig.SuggestionQueryConfig.Sections.SectionType"\x9c\x01\n\x0bSectionType\x12\x1c\n\x18SECTION_TYPE_UNSPECIFIED\x10\x00\x12\r\n\tSITUATION\x10\x01\x12\n\n\x06ACTION\x10\x02\x12\x0e\n\nRESOLUTION\x10\x03\x12\x1b\n\x17REASON_FOR_CANCELLATION\x10\x04\x12\x19\n\x15CUSTOMER_SATISFACTION\x10\x05\x12\x0c\n\x08ENTITIES\x10\x06B\x0e\n\x0cquery_source\x1az\n\x17ConversationModelConfig\x12?\n\x05model\x18\x01 \x01(\tB0\xfaA-\n+dialogflow.googleapis.com/ConversationModel\x12\x1e\n\x16baseline_model_version\x18\x08 \x01(\t\x1a;\n\x19ConversationProcessConfig\x12\x1e\n\x16recent_sentences_count\x18\x02 \x01(\x05\x1a\\\n\x15MessageAnalysisConfig\x12 \n\x18enable_entity_extraction\x18\x02 \x01(\x08\x12!\n\x19enable_sentiment_analysis\x18\x03 \x01(\x08"\xc4\x03\n\x17HumanAgentHandoffConfig\x12b\n\x12live_person_config\x18\x01 \x01(\x0b2D.google.cloud.dialogflow.v2.HumanAgentHandoffConfig.LivePersonConfigH\x00\x12u\n\x1csalesforce_live_agent_config\x18\x02 \x01(\x0b2M.google.cloud.dialogflow.v2.HumanAgentHandoffConfig.SalesforceLiveAgentConfigH\x00\x1a/\n\x10LivePersonConfig\x12\x1b\n\x0eaccount_number\x18\x01 \x01(\tB\x03\xe0A\x02\x1a\x8b\x01\n\x19SalesforceLiveAgentConfig\x12\x1c\n\x0forganization_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x1a\n\rdeployment_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x16\n\tbutton_id\x18\x03 \x01(\tB\x03\xe0A\x02\x12\x1c\n\x0fendpoint_domain\x18\x04 \x01(\tB\x03\xe0A\x02B\x0f\n\ragent_service"\xbf\x01\n\x12NotificationConfig\x12\r\n\x05topic\x18\x01 \x01(\t\x12T\n\x0emessage_format\x18\x02 \x01(\x0e2<.google.cloud.dialogflow.v2.NotificationConfig.MessageFormat"D\n\rMessageFormat\x12\x1e\n\x1aMESSAGE_FORMAT_UNSPECIFIED\x10\x00\x12\t\n\x05PROTO\x10\x01\x12\x08\n\x04JSON\x10\x02"3\n\rLoggingConfig\x12"\n\x1aenable_stackdriver_logging\x18\x03 \x01(\x08"\xd1\x01\n\x11SuggestionFeature\x12@\n\x04type\x18\x01 \x01(\x0e22.google.cloud.dialogflow.v2.SuggestionFeature.Type"z\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x16\n\x12ARTICLE_SUGGESTION\x10\x01\x12\x07\n\x03FAQ\x10\x02\x12\x0f\n\x0bSMART_REPLY\x10\x03\x12\x14\n\x10KNOWLEDGE_SEARCH\x10\x0e\x12\x14\n\x10KNOWLEDGE_ASSIST\x10\x0f"\x8a\x02\n!SetSuggestionFeatureConfigRequest\x12!\n\x14conversation_profile\x18\x01 \x01(\tB\x03\xe0A\x02\x12K\n\x10participant_role\x18\x02 \x01(\x0e2,.google.cloud.dialogflow.v2.Participant.RoleB\x03\xe0A\x02\x12u\n\x19suggestion_feature_config\x18\x03 \x01(\x0b2M.google.cloud.dialogflow.v2.HumanAgentAssistantConfig.SuggestionFeatureConfigB\x03\xe0A\x02"\xef\x01\n#ClearSuggestionFeatureConfigRequest\x12!\n\x14conversation_profile\x18\x01 \x01(\tB\x03\xe0A\x02\x12K\n\x10participant_role\x18\x02 \x01(\x0e2,.google.cloud.dialogflow.v2.Participant.RoleB\x03\xe0A\x02\x12X\n\x17suggestion_feature_type\x18\x03 \x01(\x0e22.google.cloud.dialogflow.v2.SuggestionFeature.TypeB\x03\xe0A\x02"\xa3\x02\n+SetSuggestionFeatureConfigOperationMetadata\x12\x1c\n\x14conversation_profile\x18\x01 \x01(\t\x12K\n\x10participant_role\x18\x02 \x01(\x0e2,.google.cloud.dialogflow.v2.Participant.RoleB\x03\xe0A\x02\x12X\n\x17suggestion_feature_type\x18\x03 \x01(\x0e22.google.cloud.dialogflow.v2.SuggestionFeature.TypeB\x03\xe0A\x02\x12/\n\x0bcreate_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp"\xa5\x02\n-ClearSuggestionFeatureConfigOperationMetadata\x12\x1c\n\x14conversation_profile\x18\x01 \x01(\t\x12K\n\x10participant_role\x18\x02 \x01(\x0e2,.google.cloud.dialogflow.v2.Participant.RoleB\x03\xe0A\x02\x12X\n\x17suggestion_feature_type\x18\x03 \x01(\x0e22.google.cloud.dialogflow.v2.SuggestionFeature.TypeB\x03\xe0A\x02\x12/\n\x0bcreate_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp2\xb3\x14\n\x14ConversationProfiles\x12\x90\x02\n\x18ListConversationProfiles\x12;.google.cloud.dialogflow.v2.ListConversationProfilesRequest\x1a<.google.cloud.dialogflow.v2.ListConversationProfilesResponse"y\xdaA\x06parent\x82\xd3\xe4\x93\x02j\x12,/v2/{parent=projects/*}/conversationProfilesZ:\x128/v2/{parent=projects/*/locations/*}/conversationProfiles\x12\xfd\x01\n\x16GetConversationProfile\x129.google.cloud.dialogflow.v2.GetConversationProfileRequest\x1a/.google.cloud.dialogflow.v2.ConversationProfile"w\xdaA\x04name\x82\xd3\xe4\x93\x02j\x12,/v2/{name=projects/*/conversationProfiles/*}Z:\x128/v2/{name=projects/*/locations/*/conversationProfiles/*}\x12\xc8\x02\n\x19CreateConversationProfile\x12<.google.cloud.dialogflow.v2.CreateConversationProfileRequest\x1a/.google.cloud.dialogflow.v2.ConversationProfile"\xbb\x01\xdaA\x1bparent,conversation_profile\x82\xd3\xe4\x93\x02\x96\x01",/v2/{parent=projects/*}/conversationProfiles:\x14conversation_profileZP"8/v2/{parent=projects/*/locations/*}/conversationProfiles:\x14conversation_profile\x12\xf7\x02\n\x19UpdateConversationProfile\x12<.google.cloud.dialogflow.v2.UpdateConversationProfileRequest\x1a/.google.cloud.dialogflow.v2.ConversationProfile"\xea\x01\xdaA conversation_profile,update_mask\x82\xd3\xe4\x93\x02\xc0\x012A/v2/{conversation_profile.name=projects/*/conversationProfiles/*}:\x14conversation_profileZe2M/v2/{conversation_profile.name=projects/*/locations/*/conversationProfiles/*}:\x14conversation_profile\x12\xea\x01\n\x19DeleteConversationProfile\x12<.google.cloud.dialogflow.v2.DeleteConversationProfileRequest\x1a\x16.google.protobuf.Empty"w\xdaA\x04name\x82\xd3\xe4\x93\x02j*,/v2/{name=projects/*/conversationProfiles/*}Z:*8/v2/{name=projects/*/locations/*/conversationProfiles/*}\x12\xe8\x03\n\x1aSetSuggestionFeatureConfig\x12=.google.cloud.dialogflow.v2.SetSuggestionFeatureConfigRequest\x1a\x1d.google.longrunning.Operation"\xeb\x02\xcaAB\n\x13ConversationProfile\x12+SetSuggestionFeatureConfigOperationMetadata\xdaA\x14conversation_profile\xdaA?conversation_profile,participant_role,suggestion_feature_config\x82\xd3\xe4\x93\x02\xc6\x01"W/v2/{conversation_profile=projects/*/conversationProfiles/*}:setSuggestionFeatureConfig:\x01*Zh"c/v2/{conversation_profile=projects/*/locations/*/conversationProfiles/*}:setSuggestionFeatureConfig:\x01*\x12\xf0\x03\n\x1cClearSuggestionFeatureConfig\x12?.google.cloud.dialogflow.v2.ClearSuggestionFeatureConfigRequest\x1a\x1d.google.longrunning.Operation"\xef\x02\xcaAD\n\x13ConversationProfile\x12-ClearSuggestionFeatureConfigOperationMetadata\xdaA\x14conversation_profile\xdaA=conversation_profile,participant_role,suggestion_feature_type\x82\xd3\xe4\x93\x02\xca\x01"Y/v2/{conversation_profile=projects/*/conversationProfiles/*}:clearSuggestionFeatureConfig:\x01*Zj"e/v2/{conversation_profile=projects/*/locations/*/conversationProfiles/*}:clearSuggestionFeatureConfig:\x01*\x1ax\xcaA\x19dialogflow.googleapis.com\xd2AYhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflowB\x9d\x02\n\x1ecom.google.cloud.dialogflow.v2B\x18ConversationProfileProtoP\x01Z>cloud.google.com/go/dialogflow/apiv2/dialogflowpb;dialogflowpb\xa2\x02\x02DF\xaa\x02\x1aGoogle.Cloud.Dialogflow.V2\xeaA|\n,dialogflow.googleapis.com/CXSecuritySettings\x12Lprojects/{project}/locations/{location}/securitySettings/{security_settings}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.dialogflow.v2.conversation_profile_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.dialogflow.v2B\x18ConversationProfileProtoP\x01Z>cloud.google.com/go/dialogflow/apiv2/dialogflowpb;dialogflowpb\xa2\x02\x02DF\xaa\x02\x1aGoogle.Cloud.Dialogflow.V2\xeaA|\n,dialogflow.googleapis.com/CXSecuritySettings\x12Lprojects/{project}/locations/{location}/securitySettings/{security_settings}'
    _globals['_CONVERSATIONPROFILE'].fields_by_name['display_name']._loaded_options = None
    _globals['_CONVERSATIONPROFILE'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_CONVERSATIONPROFILE'].fields_by_name['create_time']._loaded_options = None
    _globals['_CONVERSATIONPROFILE'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_CONVERSATIONPROFILE'].fields_by_name['update_time']._loaded_options = None
    _globals['_CONVERSATIONPROFILE'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_CONVERSATIONPROFILE'].fields_by_name['new_recognition_result_notification_config']._loaded_options = None
    _globals['_CONVERSATIONPROFILE'].fields_by_name['new_recognition_result_notification_config']._serialized_options = b'\xe0A\x01'
    _globals['_CONVERSATIONPROFILE'].fields_by_name['security_settings']._loaded_options = None
    _globals['_CONVERSATIONPROFILE'].fields_by_name['security_settings']._serialized_options = b'\xfaA.\n,dialogflow.googleapis.com/CXSecuritySettings'
    _globals['_CONVERSATIONPROFILE']._loaded_options = None
    _globals['_CONVERSATIONPROFILE']._serialized_options = b'\xeaA\xc4\x01\n-dialogflow.googleapis.com/ConversationProfile\x12>projects/{project}/conversationProfiles/{conversation_profile}\x12Sprojects/{project}/locations/{location}/conversationProfiles/{conversation_profile}'
    _globals['_LISTCONVERSATIONPROFILESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTCONVERSATIONPROFILESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA/\x12-dialogflow.googleapis.com/ConversationProfile'
    _globals['_GETCONVERSATIONPROFILEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETCONVERSATIONPROFILEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA/\n-dialogflow.googleapis.com/ConversationProfile'
    _globals['_CREATECONVERSATIONPROFILEREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATECONVERSATIONPROFILEREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA/\x12-dialogflow.googleapis.com/ConversationProfile'
    _globals['_CREATECONVERSATIONPROFILEREQUEST'].fields_by_name['conversation_profile']._loaded_options = None
    _globals['_CREATECONVERSATIONPROFILEREQUEST'].fields_by_name['conversation_profile']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATECONVERSATIONPROFILEREQUEST'].fields_by_name['conversation_profile']._loaded_options = None
    _globals['_UPDATECONVERSATIONPROFILEREQUEST'].fields_by_name['conversation_profile']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATECONVERSATIONPROFILEREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATECONVERSATIONPROFILEREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_DELETECONVERSATIONPROFILEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETECONVERSATIONPROFILEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA/\n-dialogflow.googleapis.com/ConversationProfile'
    _globals['_AUTOMATEDAGENTCONFIG'].fields_by_name['agent']._loaded_options = None
    _globals['_AUTOMATEDAGENTCONFIG'].fields_by_name['agent']._serialized_options = b'\xe0A\x02\xfaA!\n\x1fdialogflow.googleapis.com/Agent'
    _globals['_AUTOMATEDAGENTCONFIG'].fields_by_name['session_ttl']._loaded_options = None
    _globals['_AUTOMATEDAGENTCONFIG'].fields_by_name['session_ttl']._serialized_options = b'\xe0A\x01'
    _globals['_HUMANAGENTASSISTANTCONFIG_SUGGESTIONFEATURECONFIG'].fields_by_name['disable_agent_query_logging']._loaded_options = None
    _globals['_HUMANAGENTASSISTANTCONFIG_SUGGESTIONFEATURECONFIG'].fields_by_name['disable_agent_query_logging']._serialized_options = b'\xe0A\x01'
    _globals['_HUMANAGENTASSISTANTCONFIG_SUGGESTIONFEATURECONFIG'].fields_by_name['enable_query_suggestion_when_no_answer']._loaded_options = None
    _globals['_HUMANAGENTASSISTANTCONFIG_SUGGESTIONFEATURECONFIG'].fields_by_name['enable_query_suggestion_when_no_answer']._serialized_options = b'\xe0A\x01'
    _globals['_HUMANAGENTASSISTANTCONFIG_SUGGESTIONFEATURECONFIG'].fields_by_name['enable_conversation_augmented_query']._loaded_options = None
    _globals['_HUMANAGENTASSISTANTCONFIG_SUGGESTIONFEATURECONFIG'].fields_by_name['enable_conversation_augmented_query']._serialized_options = b'\xe0A\x01'
    _globals['_HUMANAGENTASSISTANTCONFIG_SUGGESTIONFEATURECONFIG'].fields_by_name['enable_query_suggestion_only']._loaded_options = None
    _globals['_HUMANAGENTASSISTANTCONFIG_SUGGESTIONFEATURECONFIG'].fields_by_name['enable_query_suggestion_only']._serialized_options = b'\xe0A\x01'
    _globals['_HUMANAGENTASSISTANTCONFIG_SUGGESTIONCONFIG'].fields_by_name['generators']._loaded_options = None
    _globals['_HUMANAGENTASSISTANTCONFIG_SUGGESTIONCONFIG'].fields_by_name['generators']._serialized_options = b'\xe0A\x01\xfaA%\n#dialogflow.googleapis.com/Generator'
    _globals['_HUMANAGENTASSISTANTCONFIG_SUGGESTIONCONFIG'].fields_by_name['disable_high_latency_features_sync_delivery']._loaded_options = None
    _globals['_HUMANAGENTASSISTANTCONFIG_SUGGESTIONCONFIG'].fields_by_name['disable_high_latency_features_sync_delivery']._serialized_options = b'\xe0A\x01'
    _globals['_HUMANAGENTASSISTANTCONFIG_SUGGESTIONQUERYCONFIG_KNOWLEDGEBASEQUERYSOURCE'].fields_by_name['knowledge_bases']._loaded_options = None
    _globals['_HUMANAGENTASSISTANTCONFIG_SUGGESTIONQUERYCONFIG_KNOWLEDGEBASEQUERYSOURCE'].fields_by_name['knowledge_bases']._serialized_options = b"\xe0A\x02\xfaA)\n'dialogflow.googleapis.com/KnowledgeBase"
    _globals['_HUMANAGENTASSISTANTCONFIG_SUGGESTIONQUERYCONFIG_DOCUMENTQUERYSOURCE'].fields_by_name['documents']._loaded_options = None
    _globals['_HUMANAGENTASSISTANTCONFIG_SUGGESTIONQUERYCONFIG_DOCUMENTQUERYSOURCE'].fields_by_name['documents']._serialized_options = b'\xe0A\x02\xfaA$\n"dialogflow.googleapis.com/Document'
    _globals['_HUMANAGENTASSISTANTCONFIG_SUGGESTIONQUERYCONFIG_DIALOGFLOWQUERYSOURCE_HUMANAGENTSIDECONFIG'].fields_by_name['agent']._loaded_options = None
    _globals['_HUMANAGENTASSISTANTCONFIG_SUGGESTIONQUERYCONFIG_DIALOGFLOWQUERYSOURCE_HUMANAGENTSIDECONFIG'].fields_by_name['agent']._serialized_options = b'\xe0A\x01\xfaA!\n\x1fdialogflow.googleapis.com/Agent'
    _globals['_HUMANAGENTASSISTANTCONFIG_SUGGESTIONQUERYCONFIG_DIALOGFLOWQUERYSOURCE'].fields_by_name['agent']._loaded_options = None
    _globals['_HUMANAGENTASSISTANTCONFIG_SUGGESTIONQUERYCONFIG_DIALOGFLOWQUERYSOURCE'].fields_by_name['agent']._serialized_options = b'\xe0A\x02\xfaA!\n\x1fdialogflow.googleapis.com/Agent'
    _globals['_HUMANAGENTASSISTANTCONFIG_SUGGESTIONQUERYCONFIG_DIALOGFLOWQUERYSOURCE'].fields_by_name['human_agent_side_config']._loaded_options = None
    _globals['_HUMANAGENTASSISTANTCONFIG_SUGGESTIONQUERYCONFIG_DIALOGFLOWQUERYSOURCE'].fields_by_name['human_agent_side_config']._serialized_options = b'\xe0A\x01'
    _globals['_HUMANAGENTASSISTANTCONFIG_SUGGESTIONQUERYCONFIG'].fields_by_name['sections']._loaded_options = None
    _globals['_HUMANAGENTASSISTANTCONFIG_SUGGESTIONQUERYCONFIG'].fields_by_name['sections']._serialized_options = b'\xe0A\x01'
    _globals['_HUMANAGENTASSISTANTCONFIG_SUGGESTIONQUERYCONFIG'].fields_by_name['context_size']._loaded_options = None
    _globals['_HUMANAGENTASSISTANTCONFIG_SUGGESTIONQUERYCONFIG'].fields_by_name['context_size']._serialized_options = b'\xe0A\x01'
    _globals['_HUMANAGENTASSISTANTCONFIG_CONVERSATIONMODELCONFIG'].fields_by_name['model']._loaded_options = None
    _globals['_HUMANAGENTASSISTANTCONFIG_CONVERSATIONMODELCONFIG'].fields_by_name['model']._serialized_options = b'\xfaA-\n+dialogflow.googleapis.com/ConversationModel'
    _globals['_HUMANAGENTHANDOFFCONFIG_LIVEPERSONCONFIG'].fields_by_name['account_number']._loaded_options = None
    _globals['_HUMANAGENTHANDOFFCONFIG_LIVEPERSONCONFIG'].fields_by_name['account_number']._serialized_options = b'\xe0A\x02'
    _globals['_HUMANAGENTHANDOFFCONFIG_SALESFORCELIVEAGENTCONFIG'].fields_by_name['organization_id']._loaded_options = None
    _globals['_HUMANAGENTHANDOFFCONFIG_SALESFORCELIVEAGENTCONFIG'].fields_by_name['organization_id']._serialized_options = b'\xe0A\x02'
    _globals['_HUMANAGENTHANDOFFCONFIG_SALESFORCELIVEAGENTCONFIG'].fields_by_name['deployment_id']._loaded_options = None
    _globals['_HUMANAGENTHANDOFFCONFIG_SALESFORCELIVEAGENTCONFIG'].fields_by_name['deployment_id']._serialized_options = b'\xe0A\x02'
    _globals['_HUMANAGENTHANDOFFCONFIG_SALESFORCELIVEAGENTCONFIG'].fields_by_name['button_id']._loaded_options = None
    _globals['_HUMANAGENTHANDOFFCONFIG_SALESFORCELIVEAGENTCONFIG'].fields_by_name['button_id']._serialized_options = b'\xe0A\x02'
    _globals['_HUMANAGENTHANDOFFCONFIG_SALESFORCELIVEAGENTCONFIG'].fields_by_name['endpoint_domain']._loaded_options = None
    _globals['_HUMANAGENTHANDOFFCONFIG_SALESFORCELIVEAGENTCONFIG'].fields_by_name['endpoint_domain']._serialized_options = b'\xe0A\x02'
    _globals['_SETSUGGESTIONFEATURECONFIGREQUEST'].fields_by_name['conversation_profile']._loaded_options = None
    _globals['_SETSUGGESTIONFEATURECONFIGREQUEST'].fields_by_name['conversation_profile']._serialized_options = b'\xe0A\x02'
    _globals['_SETSUGGESTIONFEATURECONFIGREQUEST'].fields_by_name['participant_role']._loaded_options = None
    _globals['_SETSUGGESTIONFEATURECONFIGREQUEST'].fields_by_name['participant_role']._serialized_options = b'\xe0A\x02'
    _globals['_SETSUGGESTIONFEATURECONFIGREQUEST'].fields_by_name['suggestion_feature_config']._loaded_options = None
    _globals['_SETSUGGESTIONFEATURECONFIGREQUEST'].fields_by_name['suggestion_feature_config']._serialized_options = b'\xe0A\x02'
    _globals['_CLEARSUGGESTIONFEATURECONFIGREQUEST'].fields_by_name['conversation_profile']._loaded_options = None
    _globals['_CLEARSUGGESTIONFEATURECONFIGREQUEST'].fields_by_name['conversation_profile']._serialized_options = b'\xe0A\x02'
    _globals['_CLEARSUGGESTIONFEATURECONFIGREQUEST'].fields_by_name['participant_role']._loaded_options = None
    _globals['_CLEARSUGGESTIONFEATURECONFIGREQUEST'].fields_by_name['participant_role']._serialized_options = b'\xe0A\x02'
    _globals['_CLEARSUGGESTIONFEATURECONFIGREQUEST'].fields_by_name['suggestion_feature_type']._loaded_options = None
    _globals['_CLEARSUGGESTIONFEATURECONFIGREQUEST'].fields_by_name['suggestion_feature_type']._serialized_options = b'\xe0A\x02'
    _globals['_SETSUGGESTIONFEATURECONFIGOPERATIONMETADATA'].fields_by_name['participant_role']._loaded_options = None
    _globals['_SETSUGGESTIONFEATURECONFIGOPERATIONMETADATA'].fields_by_name['participant_role']._serialized_options = b'\xe0A\x02'
    _globals['_SETSUGGESTIONFEATURECONFIGOPERATIONMETADATA'].fields_by_name['suggestion_feature_type']._loaded_options = None
    _globals['_SETSUGGESTIONFEATURECONFIGOPERATIONMETADATA'].fields_by_name['suggestion_feature_type']._serialized_options = b'\xe0A\x02'
    _globals['_CLEARSUGGESTIONFEATURECONFIGOPERATIONMETADATA'].fields_by_name['participant_role']._loaded_options = None
    _globals['_CLEARSUGGESTIONFEATURECONFIGOPERATIONMETADATA'].fields_by_name['participant_role']._serialized_options = b'\xe0A\x02'
    _globals['_CLEARSUGGESTIONFEATURECONFIGOPERATIONMETADATA'].fields_by_name['suggestion_feature_type']._loaded_options = None
    _globals['_CLEARSUGGESTIONFEATURECONFIGOPERATIONMETADATA'].fields_by_name['suggestion_feature_type']._serialized_options = b'\xe0A\x02'
    _globals['_CONVERSATIONPROFILES']._loaded_options = None
    _globals['_CONVERSATIONPROFILES']._serialized_options = b'\xcaA\x19dialogflow.googleapis.com\xd2AYhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflow'
    _globals['_CONVERSATIONPROFILES'].methods_by_name['ListConversationProfiles']._loaded_options = None
    _globals['_CONVERSATIONPROFILES'].methods_by_name['ListConversationProfiles']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02j\x12,/v2/{parent=projects/*}/conversationProfilesZ:\x128/v2/{parent=projects/*/locations/*}/conversationProfiles'
    _globals['_CONVERSATIONPROFILES'].methods_by_name['GetConversationProfile']._loaded_options = None
    _globals['_CONVERSATIONPROFILES'].methods_by_name['GetConversationProfile']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02j\x12,/v2/{name=projects/*/conversationProfiles/*}Z:\x128/v2/{name=projects/*/locations/*/conversationProfiles/*}'
    _globals['_CONVERSATIONPROFILES'].methods_by_name['CreateConversationProfile']._loaded_options = None
    _globals['_CONVERSATIONPROFILES'].methods_by_name['CreateConversationProfile']._serialized_options = b'\xdaA\x1bparent,conversation_profile\x82\xd3\xe4\x93\x02\x96\x01",/v2/{parent=projects/*}/conversationProfiles:\x14conversation_profileZP"8/v2/{parent=projects/*/locations/*}/conversationProfiles:\x14conversation_profile'
    _globals['_CONVERSATIONPROFILES'].methods_by_name['UpdateConversationProfile']._loaded_options = None
    _globals['_CONVERSATIONPROFILES'].methods_by_name['UpdateConversationProfile']._serialized_options = b'\xdaA conversation_profile,update_mask\x82\xd3\xe4\x93\x02\xc0\x012A/v2/{conversation_profile.name=projects/*/conversationProfiles/*}:\x14conversation_profileZe2M/v2/{conversation_profile.name=projects/*/locations/*/conversationProfiles/*}:\x14conversation_profile'
    _globals['_CONVERSATIONPROFILES'].methods_by_name['DeleteConversationProfile']._loaded_options = None
    _globals['_CONVERSATIONPROFILES'].methods_by_name['DeleteConversationProfile']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02j*,/v2/{name=projects/*/conversationProfiles/*}Z:*8/v2/{name=projects/*/locations/*/conversationProfiles/*}'
    _globals['_CONVERSATIONPROFILES'].methods_by_name['SetSuggestionFeatureConfig']._loaded_options = None
    _globals['_CONVERSATIONPROFILES'].methods_by_name['SetSuggestionFeatureConfig']._serialized_options = b'\xcaAB\n\x13ConversationProfile\x12+SetSuggestionFeatureConfigOperationMetadata\xdaA\x14conversation_profile\xdaA?conversation_profile,participant_role,suggestion_feature_config\x82\xd3\xe4\x93\x02\xc6\x01"W/v2/{conversation_profile=projects/*/conversationProfiles/*}:setSuggestionFeatureConfig:\x01*Zh"c/v2/{conversation_profile=projects/*/locations/*/conversationProfiles/*}:setSuggestionFeatureConfig:\x01*'
    _globals['_CONVERSATIONPROFILES'].methods_by_name['ClearSuggestionFeatureConfig']._loaded_options = None
    _globals['_CONVERSATIONPROFILES'].methods_by_name['ClearSuggestionFeatureConfig']._serialized_options = b'\xcaAD\n\x13ConversationProfile\x12-ClearSuggestionFeatureConfigOperationMetadata\xdaA\x14conversation_profile\xdaA=conversation_profile,participant_role,suggestion_feature_type\x82\xd3\xe4\x93\x02\xca\x01"Y/v2/{conversation_profile=projects/*/conversationProfiles/*}:clearSuggestionFeatureConfig:\x01*Zj"e/v2/{conversation_profile=projects/*/locations/*/conversationProfiles/*}:clearSuggestionFeatureConfig:\x01*'
    _globals['_CONVERSATIONPROFILE']._serialized_start = 459
    _globals['_CONVERSATIONPROFILE']._serialized_end = 1700
    _globals['_LISTCONVERSATIONPROFILESREQUEST']._serialized_start = 1703
    _globals['_LISTCONVERSATIONPROFILESREQUEST']._serialized_end = 1846
    _globals['_LISTCONVERSATIONPROFILESRESPONSE']._serialized_start = 1849
    _globals['_LISTCONVERSATIONPROFILESRESPONSE']._serialized_end = 1988
    _globals['_GETCONVERSATIONPROFILEREQUEST']._serialized_start = 1990
    _globals['_GETCONVERSATIONPROFILEREQUEST']._serialized_end = 2090
    _globals['_CREATECONVERSATIONPROFILEREQUEST']._serialized_start = 2093
    _globals['_CREATECONVERSATIONPROFILEREQUEST']._serialized_end = 2282
    _globals['_UPDATECONVERSATIONPROFILEREQUEST']._serialized_start = 2285
    _globals['_UPDATECONVERSATIONPROFILEREQUEST']._serialized_end = 2457
    _globals['_DELETECONVERSATIONPROFILEREQUEST']._serialized_start = 2459
    _globals['_DELETECONVERSATIONPROFILEREQUEST']._serialized_end = 2562
    _globals['_AUTOMATEDAGENTCONFIG']._serialized_start = 2565
    _globals['_AUTOMATEDAGENTCONFIG']._serialized_end = 2696
    _globals['_HUMANAGENTASSISTANTCONFIG']._serialized_start = 2699
    _globals['_HUMANAGENTASSISTANTCONFIG']._serialized_end = 6240
    _globals['_HUMANAGENTASSISTANTCONFIG_SUGGESTIONTRIGGERSETTINGS']._serialized_start = 3134
    _globals['_HUMANAGENTASSISTANTCONFIG_SUGGESTIONTRIGGERSETTINGS']._serialized_end = 3206
    _globals['_HUMANAGENTASSISTANTCONFIG_SUGGESTIONFEATURECONFIG']._serialized_start = 3209
    _globals['_HUMANAGENTASSISTANTCONFIG_SUGGESTIONFEATURECONFIG']._serialized_end = 3985
    _globals['_HUMANAGENTASSISTANTCONFIG_SUGGESTIONCONFIG']._serialized_start = 3988
    _globals['_HUMANAGENTASSISTANTCONFIG_SUGGESTIONCONFIG']._serialized_end = 4269
    _globals['_HUMANAGENTASSISTANTCONFIG_SUGGESTIONQUERYCONFIG']._serialized_start = 4272
    _globals['_HUMANAGENTASSISTANTCONFIG_SUGGESTIONQUERYCONFIG']._serialized_end = 5961
    _globals['_HUMANAGENTASSISTANTCONFIG_SUGGESTIONQUERYCONFIG_KNOWLEDGEBASEQUERYSOURCE']._serialized_start = 5025
    _globals['_HUMANAGENTASSISTANTCONFIG_SUGGESTIONQUERYCONFIG_KNOWLEDGEBASEQUERYSOURCE']._serialized_end = 5125
    _globals['_HUMANAGENTASSISTANTCONFIG_SUGGESTIONQUERYCONFIG_DOCUMENTQUERYSOURCE']._serialized_start = 5127
    _globals['_HUMANAGENTASSISTANTCONFIG_SUGGESTIONQUERYCONFIG_DOCUMENTQUERYSOURCE']._serialized_end = 5211
    _globals['_HUMANAGENTASSISTANTCONFIG_SUGGESTIONQUERYCONFIG_DIALOGFLOWQUERYSOURCE']._serialized_start = 5214
    _globals['_HUMANAGENTASSISTANTCONFIG_SUGGESTIONQUERYCONFIG_DIALOGFLOWQUERYSOURCE']._serialized_end = 5532
    _globals['_HUMANAGENTASSISTANTCONFIG_SUGGESTIONQUERYCONFIG_DIALOGFLOWQUERYSOURCE_HUMANAGENTSIDECONFIG']._serialized_start = 5454
    _globals['_HUMANAGENTASSISTANTCONFIG_SUGGESTIONQUERYCONFIG_DIALOGFLOWQUERYSOURCE_HUMANAGENTSIDECONFIG']._serialized_end = 5532
    _globals['_HUMANAGENTASSISTANTCONFIG_SUGGESTIONQUERYCONFIG_CONTEXTFILTERSETTINGS']._serialized_start = 5534
    _globals['_HUMANAGENTASSISTANTCONFIG_SUGGESTIONQUERYCONFIG_CONTEXTFILTERSETTINGS']._serialized_end = 5652
    _globals['_HUMANAGENTASSISTANTCONFIG_SUGGESTIONQUERYCONFIG_SECTIONS']._serialized_start = 5655
    _globals['_HUMANAGENTASSISTANTCONFIG_SUGGESTIONQUERYCONFIG_SECTIONS']._serialized_end = 5945
    _globals['_HUMANAGENTASSISTANTCONFIG_SUGGESTIONQUERYCONFIG_SECTIONS_SECTIONTYPE']._serialized_start = 5789
    _globals['_HUMANAGENTASSISTANTCONFIG_SUGGESTIONQUERYCONFIG_SECTIONS_SECTIONTYPE']._serialized_end = 5945
    _globals['_HUMANAGENTASSISTANTCONFIG_CONVERSATIONMODELCONFIG']._serialized_start = 5963
    _globals['_HUMANAGENTASSISTANTCONFIG_CONVERSATIONMODELCONFIG']._serialized_end = 6085
    _globals['_HUMANAGENTASSISTANTCONFIG_CONVERSATIONPROCESSCONFIG']._serialized_start = 6087
    _globals['_HUMANAGENTASSISTANTCONFIG_CONVERSATIONPROCESSCONFIG']._serialized_end = 6146
    _globals['_HUMANAGENTASSISTANTCONFIG_MESSAGEANALYSISCONFIG']._serialized_start = 6148
    _globals['_HUMANAGENTASSISTANTCONFIG_MESSAGEANALYSISCONFIG']._serialized_end = 6240
    _globals['_HUMANAGENTHANDOFFCONFIG']._serialized_start = 6243
    _globals['_HUMANAGENTHANDOFFCONFIG']._serialized_end = 6695
    _globals['_HUMANAGENTHANDOFFCONFIG_LIVEPERSONCONFIG']._serialized_start = 6489
    _globals['_HUMANAGENTHANDOFFCONFIG_LIVEPERSONCONFIG']._serialized_end = 6536
    _globals['_HUMANAGENTHANDOFFCONFIG_SALESFORCELIVEAGENTCONFIG']._serialized_start = 6539
    _globals['_HUMANAGENTHANDOFFCONFIG_SALESFORCELIVEAGENTCONFIG']._serialized_end = 6678
    _globals['_NOTIFICATIONCONFIG']._serialized_start = 6698
    _globals['_NOTIFICATIONCONFIG']._serialized_end = 6889
    _globals['_NOTIFICATIONCONFIG_MESSAGEFORMAT']._serialized_start = 6821
    _globals['_NOTIFICATIONCONFIG_MESSAGEFORMAT']._serialized_end = 6889
    _globals['_LOGGINGCONFIG']._serialized_start = 6891
    _globals['_LOGGINGCONFIG']._serialized_end = 6942
    _globals['_SUGGESTIONFEATURE']._serialized_start = 6945
    _globals['_SUGGESTIONFEATURE']._serialized_end = 7154
    _globals['_SUGGESTIONFEATURE_TYPE']._serialized_start = 7032
    _globals['_SUGGESTIONFEATURE_TYPE']._serialized_end = 7154
    _globals['_SETSUGGESTIONFEATURECONFIGREQUEST']._serialized_start = 7157
    _globals['_SETSUGGESTIONFEATURECONFIGREQUEST']._serialized_end = 7423
    _globals['_CLEARSUGGESTIONFEATURECONFIGREQUEST']._serialized_start = 7426
    _globals['_CLEARSUGGESTIONFEATURECONFIGREQUEST']._serialized_end = 7665
    _globals['_SETSUGGESTIONFEATURECONFIGOPERATIONMETADATA']._serialized_start = 7668
    _globals['_SETSUGGESTIONFEATURECONFIGOPERATIONMETADATA']._serialized_end = 7959
    _globals['_CLEARSUGGESTIONFEATURECONFIGOPERATIONMETADATA']._serialized_start = 7962
    _globals['_CLEARSUGGESTIONFEATURECONFIGOPERATIONMETADATA']._serialized_end = 8255
    _globals['_CONVERSATIONPROFILES']._serialized_start = 8258
    _globals['_CONVERSATIONPROFILES']._serialized_end = 10869