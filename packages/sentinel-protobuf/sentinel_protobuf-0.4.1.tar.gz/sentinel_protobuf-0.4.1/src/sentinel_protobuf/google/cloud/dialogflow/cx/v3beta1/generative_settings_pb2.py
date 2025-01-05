"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/dialogflow/cx/v3beta1/generative_settings.proto')
_sym_db = _symbol_database.Default()
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ......google.cloud.dialogflow.cx.v3beta1 import safety_settings_pb2 as google_dot_cloud_dot_dialogflow_dot_cx_dot_v3beta1_dot_safety__settings__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n<google/cloud/dialogflow/cx/v3beta1/generative_settings.proto\x12"google.cloud.dialogflow.cx.v3beta1\x1a\x19google/api/resource.proto\x1a8google/cloud/dialogflow/cx/v3beta1/safety_settings.proto"\xe1\x07\n\x12GenerativeSettings\x12\x0c\n\x04name\x18\x05 \x01(\t\x12b\n\x11fallback_settings\x18\x01 \x01(\x0b2G.google.cloud.dialogflow.cx.v3beta1.GenerativeSettings.FallbackSettings\x12V\n\x1agenerative_safety_settings\x18\x03 \x01(\x0b22.google.cloud.dialogflow.cx.v3beta1.SafetySettings\x12w\n\x1cknowledge_connector_settings\x18\x07 \x01(\x0b2Q.google.cloud.dialogflow.cx.v3beta1.GenerativeSettings.KnowledgeConnectorSettings\x12\x15\n\rlanguage_code\x18\x04 \x01(\t\x12P\n\x12llm_model_settings\x18\x08 \x01(\x0b24.google.cloud.dialogflow.cx.v3beta1.LlmModelSettings\x1a\xea\x01\n\x10FallbackSettings\x12\x17\n\x0fselected_prompt\x18\x03 \x01(\t\x12p\n\x10prompt_templates\x18\x04 \x03(\x0b2V.google.cloud.dialogflow.cx.v3beta1.GenerativeSettings.FallbackSettings.PromptTemplate\x1aK\n\x0ePromptTemplate\x12\x14\n\x0cdisplay_name\x18\x01 \x01(\t\x12\x13\n\x0bprompt_text\x18\x02 \x01(\t\x12\x0e\n\x06frozen\x18\x03 \x01(\x08\x1a\xad\x01\n\x1aKnowledgeConnectorSettings\x12\x10\n\x08business\x18\x01 \x01(\t\x12\r\n\x05agent\x18\x02 \x01(\t\x12\x16\n\x0eagent_identity\x18\x03 \x01(\t\x12\x1c\n\x14business_description\x18\x04 \x01(\t\x12\x13\n\x0bagent_scope\x18\x05 \x01(\t\x12#\n\x1bdisable_data_store_fallback\x18\x08 \x01(\x08:\x81\x01\xeaA~\n1dialogflow.googleapis.com/AgentGenerativeSettings\x12Iprojects/{project}/locations/{location}/agents/{agent}/generativeSettings"6\n\x10LlmModelSettings\x12\r\n\x05model\x18\x01 \x01(\t\x12\x13\n\x0bprompt_text\x18\x02 \x01(\tB\xd1\x01\n&com.google.cloud.dialogflow.cx.v3beta1B\x17GenerativeSettingsProtoP\x01Z6cloud.google.com/go/dialogflow/cx/apiv3beta1/cxpb;cxpb\xf8\x01\x01\xa2\x02\x02DF\xaa\x02"Google.Cloud.Dialogflow.Cx.V3Beta1\xea\x02&Google::Cloud::Dialogflow::CX::V3beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.dialogflow.cx.v3beta1.generative_settings_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.cloud.dialogflow.cx.v3beta1B\x17GenerativeSettingsProtoP\x01Z6cloud.google.com/go/dialogflow/cx/apiv3beta1/cxpb;cxpb\xf8\x01\x01\xa2\x02\x02DF\xaa\x02"Google.Cloud.Dialogflow.Cx.V3Beta1\xea\x02&Google::Cloud::Dialogflow::CX::V3beta1'
    _globals['_GENERATIVESETTINGS']._loaded_options = None
    _globals['_GENERATIVESETTINGS']._serialized_options = b'\xeaA~\n1dialogflow.googleapis.com/AgentGenerativeSettings\x12Iprojects/{project}/locations/{location}/agents/{agent}/generativeSettings'
    _globals['_GENERATIVESETTINGS']._serialized_start = 186
    _globals['_GENERATIVESETTINGS']._serialized_end = 1179
    _globals['_GENERATIVESETTINGS_FALLBACKSETTINGS']._serialized_start = 637
    _globals['_GENERATIVESETTINGS_FALLBACKSETTINGS']._serialized_end = 871
    _globals['_GENERATIVESETTINGS_FALLBACKSETTINGS_PROMPTTEMPLATE']._serialized_start = 796
    _globals['_GENERATIVESETTINGS_FALLBACKSETTINGS_PROMPTTEMPLATE']._serialized_end = 871
    _globals['_GENERATIVESETTINGS_KNOWLEDGECONNECTORSETTINGS']._serialized_start = 874
    _globals['_GENERATIVESETTINGS_KNOWLEDGECONNECTORSETTINGS']._serialized_end = 1047
    _globals['_LLMMODELSETTINGS']._serialized_start = 1181
    _globals['_LLMMODELSETTINGS']._serialized_end = 1235