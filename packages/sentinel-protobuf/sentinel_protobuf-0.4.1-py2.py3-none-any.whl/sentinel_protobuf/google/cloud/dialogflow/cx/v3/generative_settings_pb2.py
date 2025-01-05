"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/dialogflow/cx/v3/generative_settings.proto')
_sym_db = _symbol_database.Default()
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ......google.cloud.dialogflow.cx.v3 import safety_settings_pb2 as google_dot_cloud_dot_dialogflow_dot_cx_dot_v3_dot_safety__settings__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7google/cloud/dialogflow/cx/v3/generative_settings.proto\x12\x1dgoogle.cloud.dialogflow.cx.v3\x1a\x19google/api/resource.proto\x1a3google/cloud/dialogflow/cx/v3/safety_settings.proto"\xfb\x06\n\x12GenerativeSettings\x12\x0c\n\x04name\x18\x05 \x01(\t\x12]\n\x11fallback_settings\x18\x01 \x01(\x0b2B.google.cloud.dialogflow.cx.v3.GenerativeSettings.FallbackSettings\x12Q\n\x1agenerative_safety_settings\x18\x03 \x01(\x0b2-.google.cloud.dialogflow.cx.v3.SafetySettings\x12r\n\x1cknowledge_connector_settings\x18\x07 \x01(\x0b2L.google.cloud.dialogflow.cx.v3.GenerativeSettings.KnowledgeConnectorSettings\x12\x15\n\rlanguage_code\x18\x04 \x01(\t\x1a\xe5\x01\n\x10FallbackSettings\x12\x17\n\x0fselected_prompt\x18\x03 \x01(\t\x12k\n\x10prompt_templates\x18\x04 \x03(\x0b2Q.google.cloud.dialogflow.cx.v3.GenerativeSettings.FallbackSettings.PromptTemplate\x1aK\n\x0ePromptTemplate\x12\x14\n\x0cdisplay_name\x18\x01 \x01(\t\x12\x13\n\x0bprompt_text\x18\x02 \x01(\t\x12\x0e\n\x06frozen\x18\x03 \x01(\x08\x1a\xad\x01\n\x1aKnowledgeConnectorSettings\x12\x10\n\x08business\x18\x01 \x01(\t\x12\r\n\x05agent\x18\x02 \x01(\t\x12\x16\n\x0eagent_identity\x18\x03 \x01(\t\x12\x1c\n\x14business_description\x18\x04 \x01(\t\x12\x13\n\x0bagent_scope\x18\x05 \x01(\t\x12#\n\x1bdisable_data_store_fallback\x18\x08 \x01(\x08:\x81\x01\xeaA~\n1dialogflow.googleapis.com/AgentGenerativeSettings\x12Iprojects/{project}/locations/{location}/agents/{agent}/generativeSettingsB\xba\x01\n!com.google.cloud.dialogflow.cx.v3B\x17GenerativeSettingsProtoP\x01Z1cloud.google.com/go/dialogflow/cx/apiv3/cxpb;cxpb\xa2\x02\x02DF\xaa\x02\x1dGoogle.Cloud.Dialogflow.Cx.V3\xea\x02!Google::Cloud::Dialogflow::CX::V3b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.dialogflow.cx.v3.generative_settings_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n!com.google.cloud.dialogflow.cx.v3B\x17GenerativeSettingsProtoP\x01Z1cloud.google.com/go/dialogflow/cx/apiv3/cxpb;cxpb\xa2\x02\x02DF\xaa\x02\x1dGoogle.Cloud.Dialogflow.Cx.V3\xea\x02!Google::Cloud::Dialogflow::CX::V3'
    _globals['_GENERATIVESETTINGS']._loaded_options = None
    _globals['_GENERATIVESETTINGS']._serialized_options = b'\xeaA~\n1dialogflow.googleapis.com/AgentGenerativeSettings\x12Iprojects/{project}/locations/{location}/agents/{agent}/generativeSettings'
    _globals['_GENERATIVESETTINGS']._serialized_start = 171
    _globals['_GENERATIVESETTINGS']._serialized_end = 1062
    _globals['_GENERATIVESETTINGS_FALLBACKSETTINGS']._serialized_start = 525
    _globals['_GENERATIVESETTINGS_FALLBACKSETTINGS']._serialized_end = 754
    _globals['_GENERATIVESETTINGS_FALLBACKSETTINGS_PROMPTTEMPLATE']._serialized_start = 679
    _globals['_GENERATIVESETTINGS_FALLBACKSETTINGS_PROMPTTEMPLATE']._serialized_end = 754
    _globals['_GENERATIVESETTINGS_KNOWLEDGECONNECTORSETTINGS']._serialized_start = 757
    _globals['_GENERATIVESETTINGS_KNOWLEDGECONNECTORSETTINGS']._serialized_end = 930