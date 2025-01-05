"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/dialogflow/v2beta1/agent.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.dialogflow.v2beta1 import validation_result_pb2 as google_dot_cloud_dot_dialogflow_dot_v2beta1_dot_validation__result__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+google/cloud/dialogflow/v2beta1/agent.proto\x12\x1fgoogle.cloud.dialogflow.v2beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a7google/cloud/dialogflow/v2beta1/validation_result.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1cgoogle/protobuf/struct.proto"\xff\x06\n\x05Agent\x12C\n\x06parent\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project\x12\x14\n\x0cdisplay_name\x18\x02 \x01(\t\x12\x1d\n\x15default_language_code\x18\x03 \x01(\t\x12 \n\x18supported_language_codes\x18\x04 \x03(\t\x12\x11\n\ttime_zone\x18\x05 \x01(\t\x12\x13\n\x0bdescription\x18\x06 \x01(\t\x12\x12\n\navatar_uri\x18\x07 \x01(\t\x12\x16\n\x0eenable_logging\x18\x08 \x01(\x08\x12H\n\nmatch_mode\x18\t \x01(\x0e20.google.cloud.dialogflow.v2beta1.Agent.MatchModeB\x02\x18\x01\x12 \n\x18classification_threshold\x18\n \x01(\x02\x12F\n\x0bapi_version\x18\x0e \x01(\x0e21.google.cloud.dialogflow.v2beta1.Agent.ApiVersion\x129\n\x04tier\x18\x0f \x01(\x0e2+.google.cloud.dialogflow.v2beta1.Agent.Tier"V\n\tMatchMode\x12\x1a\n\x16MATCH_MODE_UNSPECIFIED\x10\x00\x12\x15\n\x11MATCH_MODE_HYBRID\x10\x01\x12\x16\n\x12MATCH_MODE_ML_ONLY\x10\x02"l\n\nApiVersion\x12\x1b\n\x17API_VERSION_UNSPECIFIED\x10\x00\x12\x12\n\x0eAPI_VERSION_V1\x10\x01\x12\x12\n\x0eAPI_VERSION_V2\x10\x02\x12\x19\n\x15API_VERSION_V2_BETA_1\x10\x03"b\n\x04Tier\x12\x14\n\x10TIER_UNSPECIFIED\x10\x00\x12\x11\n\rTIER_STANDARD\x10\x01\x12\x13\n\x0fTIER_ENTERPRISE\x10\x02\x12\x1c\n\x14TIER_ENTERPRISE_PLUS\x10\x03\x1a\x02\x08\x01:m\xeaAj\n\x1fdialogflow.googleapis.com/Agent\x12\x18projects/{project}/agent\x12-projects/{project}/locations/{location}/agent"J\n\x0fGetAgentRequest\x127\n\x06parent\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\x12\x1fdialogflow.googleapis.com/Agent"~\n\x0fSetAgentRequest\x12:\n\x05agent\x18\x01 \x01(\x0b2&.google.cloud.dialogflow.v2beta1.AgentB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"M\n\x12DeleteAgentRequest\x127\n\x06parent\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\x12\x1fdialogflow.googleapis.com/Agent"0\n\x08SubAgent\x12\x0f\n\x07project\x18\x01 \x01(\t\x12\x13\n\x0benvironment\x18\x02 \x01(\t"u\n\x13SearchAgentsRequest\x127\n\x06parent\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\x12\x1fdialogflow.googleapis.com/Agent\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"g\n\x14SearchAgentsResponse\x126\n\x06agents\x18\x01 \x03(\x0b2&.google.cloud.dialogflow.v2beta1.Agent\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"L\n\x11TrainAgentRequest\x127\n\x06parent\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\x12\x1fdialogflow.googleapis.com/Agent"`\n\x12ExportAgentRequest\x127\n\x06parent\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\x12\x1fdialogflow.googleapis.com/Agent\x12\x11\n\tagent_uri\x18\x02 \x01(\t"L\n\x13ExportAgentResponse\x12\x13\n\tagent_uri\x18\x01 \x01(\tH\x00\x12\x17\n\ragent_content\x18\x02 \x01(\x0cH\x00B\x07\n\x05agent"\x84\x01\n\x12ImportAgentRequest\x127\n\x06parent\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\x12\x1fdialogflow.googleapis.com/Agent\x12\x13\n\tagent_uri\x18\x02 \x01(\tH\x00\x12\x17\n\ragent_content\x18\x03 \x01(\x0cH\x00B\x07\n\x05agent"\x85\x01\n\x13RestoreAgentRequest\x127\n\x06parent\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\x12\x1fdialogflow.googleapis.com/Agent\x12\x13\n\tagent_uri\x18\x02 \x01(\tH\x00\x12\x17\n\ragent_content\x18\x03 \x01(\x0cH\x00B\x07\n\x05agent"q\n\x1aGetValidationResultRequest\x127\n\x06parent\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\x12\x1fdialogflow.googleapis.com/Agent\x12\x1a\n\rlanguage_code\x18\x03 \x01(\tB\x03\xe0A\x012\xca\x12\n\x06Agents\x12\xcb\x01\n\x08GetAgent\x120.google.cloud.dialogflow.v2beta1.GetAgentRequest\x1a&.google.cloud.dialogflow.v2beta1.Agent"e\xdaA\x06parent\x82\xd3\xe4\x93\x02V\x12"/v2beta1/{parent=projects/*}/agentZ0\x12./v2beta1/{parent=projects/*/locations/*}/agent\x12\xe4\x01\n\x08SetAgent\x120.google.cloud.dialogflow.v2beta1.SetAgentRequest\x1a&.google.cloud.dialogflow.v2beta1.Agent"~\xdaA\x05agent\x82\xd3\xe4\x93\x02p"(/v2beta1/{agent.parent=projects/*}/agent:\x05agentZ="4/v2beta1/{agent.parent=projects/*/locations/*}/agent:\x05agent\x12\xc1\x01\n\x0bDeleteAgent\x123.google.cloud.dialogflow.v2beta1.DeleteAgentRequest\x1a\x16.google.protobuf.Empty"e\xdaA\x06parent\x82\xd3\xe4\x93\x02V*"/v2beta1/{parent=projects/*}/agentZ0*./v2beta1/{parent=projects/*/locations/*}/agent\x12\xf0\x01\n\x0cSearchAgents\x124.google.cloud.dialogflow.v2beta1.SearchAgentsRequest\x1a5.google.cloud.dialogflow.v2beta1.SearchAgentsResponse"s\xdaA\x06parent\x82\xd3\xe4\x93\x02d\x12)/v2beta1/{parent=projects/*}/agent:searchZ7\x125/v2beta1/{parent=projects/*/locations/*}/agent:search\x12\x8b\x02\n\nTrainAgent\x122.google.cloud.dialogflow.v2beta1.TrainAgentRequest\x1a\x1d.google.longrunning.Operation"\xa9\x01\xcaA/\n\x15google.protobuf.Empty\x12\x16google.protobuf.Struct\xdaA\x06parent\x82\xd3\xe4\x93\x02h"(/v2beta1/{parent=projects/*}/agent:train:\x01*Z9"4/v2beta1/{parent=projects/*/locations/*}/agent:train:\x01*\x12\xad\x02\n\x0bExportAgent\x123.google.cloud.dialogflow.v2beta1.ExportAgentRequest\x1a\x1d.google.longrunning.Operation"\xc9\x01\xcaAM\n3google.cloud.dialogflow.v2beta1.ExportAgentResponse\x12\x16google.protobuf.Struct\xdaA\x06parent\x82\xd3\xe4\x93\x02j")/v2beta1/{parent=projects/*}/agent:export:\x01*Z:"5/v2beta1/{parent=projects/*/locations/*}/agent:export:\x01*\x12\x86\x02\n\x0bImportAgent\x123.google.cloud.dialogflow.v2beta1.ImportAgentRequest\x1a\x1d.google.longrunning.Operation"\xa2\x01\xcaA/\n\x15google.protobuf.Empty\x12\x16google.protobuf.Struct\x82\xd3\xe4\x93\x02j")/v2beta1/{parent=projects/*}/agent:import:\x01*Z:"5/v2beta1/{parent=projects/*/locations/*}/agent:import:\x01*\x12\x8a\x02\n\x0cRestoreAgent\x124.google.cloud.dialogflow.v2beta1.RestoreAgentRequest\x1a\x1d.google.longrunning.Operation"\xa4\x01\xcaA/\n\x15google.protobuf.Empty\x12\x16google.protobuf.Struct\x82\xd3\xe4\x93\x02l"*/v2beta1/{parent=projects/*}/agent:restore:\x01*Z;"6/v2beta1/{parent=projects/*/locations/*}/agent:restore:\x01*\x12\x85\x02\n\x13GetValidationResult\x12;.google.cloud.dialogflow.v2beta1.GetValidationResultRequest\x1a1.google.cloud.dialogflow.v2beta1.ValidationResult"~\x82\xd3\xe4\x93\x02x\x123/v2beta1/{parent=projects/*}/agent/validationResultZA\x12?/v2beta1/{parent=projects/*/locations/*}/agent/validationResult\x1ax\xcaA\x19dialogflow.googleapis.com\xd2AYhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflowB\xa2\x01\n#com.google.cloud.dialogflow.v2beta1B\nAgentProtoP\x01ZCcloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb;dialogflowpb\xf8\x01\x01\xa2\x02\x02DF\xaa\x02\x1fGoogle.Cloud.Dialogflow.V2Beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.dialogflow.v2beta1.agent_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.dialogflow.v2beta1B\nAgentProtoP\x01ZCcloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb;dialogflowpb\xf8\x01\x01\xa2\x02\x02DF\xaa\x02\x1fGoogle.Cloud.Dialogflow.V2Beta1'
    _globals['_AGENT_TIER'].values_by_name['TIER_ENTERPRISE_PLUS']._loaded_options = None
    _globals['_AGENT_TIER'].values_by_name['TIER_ENTERPRISE_PLUS']._serialized_options = b'\x08\x01'
    _globals['_AGENT'].fields_by_name['parent']._loaded_options = None
    _globals['_AGENT'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project'
    _globals['_AGENT'].fields_by_name['match_mode']._loaded_options = None
    _globals['_AGENT'].fields_by_name['match_mode']._serialized_options = b'\x18\x01'
    _globals['_AGENT']._loaded_options = None
    _globals['_AGENT']._serialized_options = b'\xeaAj\n\x1fdialogflow.googleapis.com/Agent\x12\x18projects/{project}/agent\x12-projects/{project}/locations/{location}/agent'
    _globals['_GETAGENTREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_GETAGENTREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA!\x12\x1fdialogflow.googleapis.com/Agent'
    _globals['_SETAGENTREQUEST'].fields_by_name['agent']._loaded_options = None
    _globals['_SETAGENTREQUEST'].fields_by_name['agent']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEAGENTREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_DELETEAGENTREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA!\x12\x1fdialogflow.googleapis.com/Agent'
    _globals['_SEARCHAGENTSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_SEARCHAGENTSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA!\x12\x1fdialogflow.googleapis.com/Agent'
    _globals['_TRAINAGENTREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_TRAINAGENTREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA!\x12\x1fdialogflow.googleapis.com/Agent'
    _globals['_EXPORTAGENTREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_EXPORTAGENTREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA!\x12\x1fdialogflow.googleapis.com/Agent'
    _globals['_IMPORTAGENTREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_IMPORTAGENTREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA!\x12\x1fdialogflow.googleapis.com/Agent'
    _globals['_RESTOREAGENTREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_RESTOREAGENTREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA!\x12\x1fdialogflow.googleapis.com/Agent'
    _globals['_GETVALIDATIONRESULTREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_GETVALIDATIONRESULTREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA!\x12\x1fdialogflow.googleapis.com/Agent'
    _globals['_GETVALIDATIONRESULTREQUEST'].fields_by_name['language_code']._loaded_options = None
    _globals['_GETVALIDATIONRESULTREQUEST'].fields_by_name['language_code']._serialized_options = b'\xe0A\x01'
    _globals['_AGENTS']._loaded_options = None
    _globals['_AGENTS']._serialized_options = b'\xcaA\x19dialogflow.googleapis.com\xd2AYhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflow'
    _globals['_AGENTS'].methods_by_name['GetAgent']._loaded_options = None
    _globals['_AGENTS'].methods_by_name['GetAgent']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02V\x12"/v2beta1/{parent=projects/*}/agentZ0\x12./v2beta1/{parent=projects/*/locations/*}/agent'
    _globals['_AGENTS'].methods_by_name['SetAgent']._loaded_options = None
    _globals['_AGENTS'].methods_by_name['SetAgent']._serialized_options = b'\xdaA\x05agent\x82\xd3\xe4\x93\x02p"(/v2beta1/{agent.parent=projects/*}/agent:\x05agentZ="4/v2beta1/{agent.parent=projects/*/locations/*}/agent:\x05agent'
    _globals['_AGENTS'].methods_by_name['DeleteAgent']._loaded_options = None
    _globals['_AGENTS'].methods_by_name['DeleteAgent']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02V*"/v2beta1/{parent=projects/*}/agentZ0*./v2beta1/{parent=projects/*/locations/*}/agent'
    _globals['_AGENTS'].methods_by_name['SearchAgents']._loaded_options = None
    _globals['_AGENTS'].methods_by_name['SearchAgents']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02d\x12)/v2beta1/{parent=projects/*}/agent:searchZ7\x125/v2beta1/{parent=projects/*/locations/*}/agent:search'
    _globals['_AGENTS'].methods_by_name['TrainAgent']._loaded_options = None
    _globals['_AGENTS'].methods_by_name['TrainAgent']._serialized_options = b'\xcaA/\n\x15google.protobuf.Empty\x12\x16google.protobuf.Struct\xdaA\x06parent\x82\xd3\xe4\x93\x02h"(/v2beta1/{parent=projects/*}/agent:train:\x01*Z9"4/v2beta1/{parent=projects/*/locations/*}/agent:train:\x01*'
    _globals['_AGENTS'].methods_by_name['ExportAgent']._loaded_options = None
    _globals['_AGENTS'].methods_by_name['ExportAgent']._serialized_options = b'\xcaAM\n3google.cloud.dialogflow.v2beta1.ExportAgentResponse\x12\x16google.protobuf.Struct\xdaA\x06parent\x82\xd3\xe4\x93\x02j")/v2beta1/{parent=projects/*}/agent:export:\x01*Z:"5/v2beta1/{parent=projects/*/locations/*}/agent:export:\x01*'
    _globals['_AGENTS'].methods_by_name['ImportAgent']._loaded_options = None
    _globals['_AGENTS'].methods_by_name['ImportAgent']._serialized_options = b'\xcaA/\n\x15google.protobuf.Empty\x12\x16google.protobuf.Struct\x82\xd3\xe4\x93\x02j")/v2beta1/{parent=projects/*}/agent:import:\x01*Z:"5/v2beta1/{parent=projects/*/locations/*}/agent:import:\x01*'
    _globals['_AGENTS'].methods_by_name['RestoreAgent']._loaded_options = None
    _globals['_AGENTS'].methods_by_name['RestoreAgent']._serialized_options = b'\xcaA/\n\x15google.protobuf.Empty\x12\x16google.protobuf.Struct\x82\xd3\xe4\x93\x02l"*/v2beta1/{parent=projects/*}/agent:restore:\x01*Z;"6/v2beta1/{parent=projects/*/locations/*}/agent:restore:\x01*'
    _globals['_AGENTS'].methods_by_name['GetValidationResult']._loaded_options = None
    _globals['_AGENTS'].methods_by_name['GetValidationResult']._serialized_options = b'\x82\xd3\xe4\x93\x02x\x123/v2beta1/{parent=projects/*}/agent/validationResultZA\x12?/v2beta1/{parent=projects/*/locations/*}/agent/validationResult'
    _globals['_AGENT']._serialized_start = 383
    _globals['_AGENT']._serialized_end = 1278
    _globals['_AGENT_MATCHMODE']._serialized_start = 871
    _globals['_AGENT_MATCHMODE']._serialized_end = 957
    _globals['_AGENT_APIVERSION']._serialized_start = 959
    _globals['_AGENT_APIVERSION']._serialized_end = 1067
    _globals['_AGENT_TIER']._serialized_start = 1069
    _globals['_AGENT_TIER']._serialized_end = 1167
    _globals['_GETAGENTREQUEST']._serialized_start = 1280
    _globals['_GETAGENTREQUEST']._serialized_end = 1354
    _globals['_SETAGENTREQUEST']._serialized_start = 1356
    _globals['_SETAGENTREQUEST']._serialized_end = 1482
    _globals['_DELETEAGENTREQUEST']._serialized_start = 1484
    _globals['_DELETEAGENTREQUEST']._serialized_end = 1561
    _globals['_SUBAGENT']._serialized_start = 1563
    _globals['_SUBAGENT']._serialized_end = 1611
    _globals['_SEARCHAGENTSREQUEST']._serialized_start = 1613
    _globals['_SEARCHAGENTSREQUEST']._serialized_end = 1730
    _globals['_SEARCHAGENTSRESPONSE']._serialized_start = 1732
    _globals['_SEARCHAGENTSRESPONSE']._serialized_end = 1835
    _globals['_TRAINAGENTREQUEST']._serialized_start = 1837
    _globals['_TRAINAGENTREQUEST']._serialized_end = 1913
    _globals['_EXPORTAGENTREQUEST']._serialized_start = 1915
    _globals['_EXPORTAGENTREQUEST']._serialized_end = 2011
    _globals['_EXPORTAGENTRESPONSE']._serialized_start = 2013
    _globals['_EXPORTAGENTRESPONSE']._serialized_end = 2089
    _globals['_IMPORTAGENTREQUEST']._serialized_start = 2092
    _globals['_IMPORTAGENTREQUEST']._serialized_end = 2224
    _globals['_RESTOREAGENTREQUEST']._serialized_start = 2227
    _globals['_RESTOREAGENTREQUEST']._serialized_end = 2360
    _globals['_GETVALIDATIONRESULTREQUEST']._serialized_start = 2362
    _globals['_GETVALIDATIONRESULTREQUEST']._serialized_end = 2475
    _globals['_AGENTS']._serialized_start = 2478
    _globals['_AGENTS']._serialized_end = 4856