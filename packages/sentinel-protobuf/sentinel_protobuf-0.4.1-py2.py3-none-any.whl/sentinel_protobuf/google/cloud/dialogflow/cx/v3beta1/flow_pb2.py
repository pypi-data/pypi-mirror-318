"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/dialogflow/cx/v3beta1/flow.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ......google.cloud.dialogflow.cx.v3beta1 import advanced_settings_pb2 as google_dot_cloud_dot_dialogflow_dot_cx_dot_v3beta1_dot_advanced__settings__pb2
from ......google.cloud.dialogflow.cx.v3beta1 import import_strategy_pb2 as google_dot_cloud_dot_dialogflow_dot_cx_dot_v3beta1_dot_import__strategy__pb2
from ......google.cloud.dialogflow.cx.v3beta1 import page_pb2 as google_dot_cloud_dot_dialogflow_dot_cx_dot_v3beta1_dot_page__pb2
from ......google.cloud.dialogflow.cx.v3beta1 import validation_message_pb2 as google_dot_cloud_dot_dialogflow_dot_cx_dot_v3beta1_dot_validation__message__pb2
from ......google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-google/cloud/dialogflow/cx/v3beta1/flow.proto\x12"google.cloud.dialogflow.cx.v3beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a:google/cloud/dialogflow/cx/v3beta1/advanced_settings.proto\x1a8google/cloud/dialogflow/cx/v3beta1/import_strategy.proto\x1a-google/cloud/dialogflow/cx/v3beta1/page.proto\x1a;google/cloud/dialogflow/cx/v3beta1/validation_message.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xb6\x03\n\x0bNluSettings\x12M\n\nmodel_type\x18\x01 \x01(\x0e29.google.cloud.dialogflow.cx.v3beta1.NluSettings.ModelType\x12 \n\x18classification_threshold\x18\x03 \x01(\x02\x12^\n\x13model_training_mode\x18\x04 \x01(\x0e2A.google.cloud.dialogflow.cx.v3beta1.NluSettings.ModelTrainingMode"Y\n\tModelType\x12\x1a\n\x16MODEL_TYPE_UNSPECIFIED\x10\x00\x12\x17\n\x13MODEL_TYPE_STANDARD\x10\x01\x12\x17\n\x13MODEL_TYPE_ADVANCED\x10\x03"{\n\x11ModelTrainingMode\x12#\n\x1fMODEL_TRAINING_MODE_UNSPECIFIED\x10\x00\x12!\n\x1dMODEL_TRAINING_MODE_AUTOMATIC\x10\x01\x12\x1e\n\x1aMODEL_TRAINING_MODE_MANUAL\x10\x02"\x8e\x07\n\x04Flow\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x13\n\x0bdescription\x18\x03 \x01(\t\x12N\n\x11transition_routes\x18\x04 \x03(\x0b23.google.cloud.dialogflow.cx.v3beta1.TransitionRoute\x12H\n\x0eevent_handlers\x18\n \x03(\x0b20.google.cloud.dialogflow.cx.v3beta1.EventHandler\x12T\n\x17transition_route_groups\x18\x0f \x03(\tB3\xfaA0\n.dialogflow.googleapis.com/TransitionRouteGroup\x12E\n\x0cnlu_settings\x18\x0b \x01(\x0b2/.google.cloud.dialogflow.cx.v3beta1.NluSettings\x12O\n\x11advanced_settings\x18\x0e \x01(\x0b24.google.cloud.dialogflow.cx.v3beta1.AdvancedSettings\x12i\n\x1cknowledge_connector_settings\x18\x12 \x01(\x0b2>.google.cloud.dialogflow.cx.v3beta1.KnowledgeConnectorSettingsB\x03\xe0A\x01\x12d\n\x17multi_language_settings\x18\x1c \x01(\x0b2>.google.cloud.dialogflow.cx.v3beta1.Flow.MultiLanguageSettingsB\x03\xe0A\x01\x12\x0e\n\x06locked\x18\x1e \x01(\x08\x1au\n\x15MultiLanguageSettings\x12,\n\x1fenable_multi_language_detection\x18\x01 \x01(\x08B\x03\xe0A\x01\x12.\n!supported_response_language_codes\x18\x02 \x03(\tB\x03\xe0A\x01:h\xeaAe\n\x1edialogflow.googleapis.com/Flow\x12Cprojects/{project}/locations/{location}/agents/{agent}/flows/{flow}"\x9f\x01\n\x11CreateFlowRequest\x126\n\x06parent\x18\x01 \x01(\tB&\xe0A\x02\xfaA \x12\x1edialogflow.googleapis.com/Flow\x12;\n\x04flow\x18\x02 \x01(\x0b2(.google.cloud.dialogflow.cx.v3beta1.FlowB\x03\xe0A\x02\x12\x15\n\rlanguage_code\x18\x03 \x01(\t"X\n\x11DeleteFlowRequest\x124\n\x04name\x18\x01 \x01(\tB&\xe0A\x02\xfaA \n\x1edialogflow.googleapis.com/Flow\x12\r\n\x05force\x18\x02 \x01(\x08"\x88\x01\n\x10ListFlowsRequest\x126\n\x06parent\x18\x01 \x01(\tB&\xe0A\x02\xfaA \x12\x1edialogflow.googleapis.com/Flow\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x15\n\rlanguage_code\x18\x04 \x01(\t"e\n\x11ListFlowsResponse\x127\n\x05flows\x18\x01 \x03(\x0b2(.google.cloud.dialogflow.cx.v3beta1.Flow\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"]\n\x0eGetFlowRequest\x124\n\x04name\x18\x01 \x01(\tB&\xe0A\x02\xfaA \n\x1edialogflow.googleapis.com/Flow\x12\x15\n\rlanguage_code\x18\x02 \x01(\t"\x98\x01\n\x11UpdateFlowRequest\x12;\n\x04flow\x18\x01 \x01(\x0b2(.google.cloud.dialogflow.cx.v3beta1.FlowB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12\x15\n\rlanguage_code\x18\x03 \x01(\t"H\n\x10TrainFlowRequest\x124\n\x04name\x18\x01 \x01(\tB&\xe0A\x02\xfaA \n\x1edialogflow.googleapis.com/Flow"b\n\x13ValidateFlowRequest\x124\n\x04name\x18\x01 \x01(\tB&\xe0A\x02\xfaA \n\x1edialogflow.googleapis.com/Flow\x12\x15\n\rlanguage_code\x18\x02 \x01(\t"}\n\x1eGetFlowValidationResultRequest\x12D\n\x04name\x18\x01 \x01(\tB6\xe0A\x02\xfaA0\n.dialogflow.googleapis.com/FlowValidationResult\x12\x15\n\rlanguage_code\x18\x02 \x01(\t"\xb6\x02\n\x14FlowValidationResult\x12\x0c\n\x04name\x18\x01 \x01(\t\x12R\n\x13validation_messages\x18\x02 \x03(\x0b25.google.cloud.dialogflow.cx.v3beta1.ValidationMessage\x12/\n\x0bupdate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp:\x8a\x01\xeaA\x86\x01\n.dialogflow.googleapis.com/FlowValidationResult\x12Tprojects/{project}/locations/{location}/agents/{agent}/flows/{flow}/validationResult"\xfc\x02\n\x11ImportFlowRequest\x126\n\x06parent\x18\x01 \x01(\tB&\xe0A\x02\xfaA \x12\x1edialogflow.googleapis.com/Flow\x12\x12\n\x08flow_uri\x18\x02 \x01(\tH\x00\x12\x16\n\x0cflow_content\x18\x03 \x01(\x0cH\x00\x12Y\n\rimport_option\x18\x04 \x01(\x0e2B.google.cloud.dialogflow.cx.v3beta1.ImportFlowRequest.ImportOption\x12Y\n\x14flow_import_strategy\x18\x05 \x01(\x0b26.google.cloud.dialogflow.cx.v3beta1.FlowImportStrategyB\x03\xe0A\x01"E\n\x0cImportOption\x12\x1d\n\x19IMPORT_OPTION_UNSPECIFIED\x10\x00\x12\x08\n\x04KEEP\x10\x01\x12\x0c\n\x08FALLBACK\x10\x02B\x06\n\x04flow"m\n\x12FlowImportStrategy\x12W\n\x16global_import_strategy\x18\x01 \x01(\x0e22.google.cloud.dialogflow.cx.v3beta1.ImportStrategyB\x03\xe0A\x01"G\n\x12ImportFlowResponse\x121\n\x04flow\x18\x01 \x01(\tB#\xfaA \n\x1edialogflow.googleapis.com/Flow"\x87\x01\n\x11ExportFlowRequest\x124\n\x04name\x18\x01 \x01(\tB&\xe0A\x02\xfaA \n\x1edialogflow.googleapis.com/Flow\x12\x15\n\x08flow_uri\x18\x02 \x01(\tB\x03\xe0A\x01\x12%\n\x18include_referenced_flows\x18\x04 \x01(\x08B\x03\xe0A\x01"H\n\x12ExportFlowResponse\x12\x12\n\x08flow_uri\x18\x01 \x01(\tH\x00\x12\x16\n\x0cflow_content\x18\x02 \x01(\x0cH\x00B\x06\n\x04flow2\x9b\x11\n\x05Flows\x12\xc2\x01\n\nCreateFlow\x125.google.cloud.dialogflow.cx.v3beta1.CreateFlowRequest\x1a(.google.cloud.dialogflow.cx.v3beta1.Flow"S\xdaA\x0bparent,flow\x82\xd3\xe4\x93\x02?"7/v3beta1/{parent=projects/*/locations/*/agents/*}/flows:\x04flow\x12\xa3\x01\n\nDeleteFlow\x125.google.cloud.dialogflow.cx.v3beta1.DeleteFlowRequest\x1a\x16.google.protobuf.Empty"F\xdaA\x04name\x82\xd3\xe4\x93\x029*7/v3beta1/{name=projects/*/locations/*/agents/*/flows/*}\x12\xc2\x01\n\tListFlows\x124.google.cloud.dialogflow.cx.v3beta1.ListFlowsRequest\x1a5.google.cloud.dialogflow.cx.v3beta1.ListFlowsResponse"H\xdaA\x06parent\x82\xd3\xe4\x93\x029\x127/v3beta1/{parent=projects/*/locations/*/agents/*}/flows\x12\xaf\x01\n\x07GetFlow\x122.google.cloud.dialogflow.cx.v3beta1.GetFlowRequest\x1a(.google.cloud.dialogflow.cx.v3beta1.Flow"F\xdaA\x04name\x82\xd3\xe4\x93\x029\x127/v3beta1/{name=projects/*/locations/*/agents/*/flows/*}\x12\xcc\x01\n\nUpdateFlow\x125.google.cloud.dialogflow.cx.v3beta1.UpdateFlowRequest\x1a(.google.cloud.dialogflow.cx.v3beta1.Flow"]\xdaA\x10flow,update_mask\x82\xd3\xe4\x93\x02D2</v3beta1/{flow.name=projects/*/locations/*/agents/*/flows/*}:\x04flow\x12\xe4\x01\n\tTrainFlow\x124.google.cloud.dialogflow.cx.v3beta1.TrainFlowRequest\x1a\x1d.google.longrunning.Operation"\x81\x01\xcaA/\n\x15google.protobuf.Empty\x12\x16google.protobuf.Struct\xdaA\x04name\x82\xd3\xe4\x93\x02B"=/v3beta1/{name=projects/*/locations/*/agents/*/flows/*}:train:\x01*\x12\xce\x01\n\x0cValidateFlow\x127.google.cloud.dialogflow.cx.v3beta1.ValidateFlowRequest\x1a8.google.cloud.dialogflow.cx.v3beta1.FlowValidationResult"K\x82\xd3\xe4\x93\x02E"@/v3beta1/{name=projects/*/locations/*/agents/*/flows/*}:validate:\x01*\x12\xf0\x01\n\x17GetFlowValidationResult\x12B.google.cloud.dialogflow.cx.v3beta1.GetFlowValidationResultRequest\x1a8.google.cloud.dialogflow.cx.v3beta1.FlowValidationResult"W\xdaA\x04name\x82\xd3\xe4\x93\x02J\x12H/v3beta1/{name=projects/*/locations/*/agents/*/flows/*/validationResult}\x12\xdc\x01\n\nImportFlow\x125.google.cloud.dialogflow.cx.v3beta1.ImportFlowRequest\x1a\x1d.google.longrunning.Operation"x\xcaA,\n\x12ImportFlowResponse\x12\x16google.protobuf.Struct\x82\xd3\xe4\x93\x02C">/v3beta1/{parent=projects/*/locations/*/agents/*}/flows:import:\x01*\x12\xdc\x01\n\nExportFlow\x125.google.cloud.dialogflow.cx.v3beta1.ExportFlowRequest\x1a\x1d.google.longrunning.Operation"x\xcaA,\n\x12ExportFlowResponse\x12\x16google.protobuf.Struct\x82\xd3\xe4\x93\x02C">/v3beta1/{name=projects/*/locations/*/agents/*/flows/*}:export:\x01*\x1ax\xcaA\x19dialogflow.googleapis.com\xd2AYhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflowB\xc3\x01\n&com.google.cloud.dialogflow.cx.v3beta1B\tFlowProtoP\x01Z6cloud.google.com/go/dialogflow/cx/apiv3beta1/cxpb;cxpb\xf8\x01\x01\xa2\x02\x02DF\xaa\x02"Google.Cloud.Dialogflow.Cx.V3Beta1\xea\x02&Google::Cloud::Dialogflow::CX::V3beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.dialogflow.cx.v3beta1.flow_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.cloud.dialogflow.cx.v3beta1B\tFlowProtoP\x01Z6cloud.google.com/go/dialogflow/cx/apiv3beta1/cxpb;cxpb\xf8\x01\x01\xa2\x02\x02DF\xaa\x02"Google.Cloud.Dialogflow.Cx.V3Beta1\xea\x02&Google::Cloud::Dialogflow::CX::V3beta1'
    _globals['_FLOW_MULTILANGUAGESETTINGS'].fields_by_name['enable_multi_language_detection']._loaded_options = None
    _globals['_FLOW_MULTILANGUAGESETTINGS'].fields_by_name['enable_multi_language_detection']._serialized_options = b'\xe0A\x01'
    _globals['_FLOW_MULTILANGUAGESETTINGS'].fields_by_name['supported_response_language_codes']._loaded_options = None
    _globals['_FLOW_MULTILANGUAGESETTINGS'].fields_by_name['supported_response_language_codes']._serialized_options = b'\xe0A\x01'
    _globals['_FLOW'].fields_by_name['display_name']._loaded_options = None
    _globals['_FLOW'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_FLOW'].fields_by_name['transition_route_groups']._loaded_options = None
    _globals['_FLOW'].fields_by_name['transition_route_groups']._serialized_options = b'\xfaA0\n.dialogflow.googleapis.com/TransitionRouteGroup'
    _globals['_FLOW'].fields_by_name['knowledge_connector_settings']._loaded_options = None
    _globals['_FLOW'].fields_by_name['knowledge_connector_settings']._serialized_options = b'\xe0A\x01'
    _globals['_FLOW'].fields_by_name['multi_language_settings']._loaded_options = None
    _globals['_FLOW'].fields_by_name['multi_language_settings']._serialized_options = b'\xe0A\x01'
    _globals['_FLOW']._loaded_options = None
    _globals['_FLOW']._serialized_options = b'\xeaAe\n\x1edialogflow.googleapis.com/Flow\x12Cprojects/{project}/locations/{location}/agents/{agent}/flows/{flow}'
    _globals['_CREATEFLOWREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEFLOWREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA \x12\x1edialogflow.googleapis.com/Flow'
    _globals['_CREATEFLOWREQUEST'].fields_by_name['flow']._loaded_options = None
    _globals['_CREATEFLOWREQUEST'].fields_by_name['flow']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEFLOWREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEFLOWREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA \n\x1edialogflow.googleapis.com/Flow'
    _globals['_LISTFLOWSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTFLOWSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA \x12\x1edialogflow.googleapis.com/Flow'
    _globals['_GETFLOWREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETFLOWREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA \n\x1edialogflow.googleapis.com/Flow'
    _globals['_UPDATEFLOWREQUEST'].fields_by_name['flow']._loaded_options = None
    _globals['_UPDATEFLOWREQUEST'].fields_by_name['flow']._serialized_options = b'\xe0A\x02'
    _globals['_TRAINFLOWREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_TRAINFLOWREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA \n\x1edialogflow.googleapis.com/Flow'
    _globals['_VALIDATEFLOWREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_VALIDATEFLOWREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA \n\x1edialogflow.googleapis.com/Flow'
    _globals['_GETFLOWVALIDATIONRESULTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETFLOWVALIDATIONRESULTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA0\n.dialogflow.googleapis.com/FlowValidationResult'
    _globals['_FLOWVALIDATIONRESULT']._loaded_options = None
    _globals['_FLOWVALIDATIONRESULT']._serialized_options = b'\xeaA\x86\x01\n.dialogflow.googleapis.com/FlowValidationResult\x12Tprojects/{project}/locations/{location}/agents/{agent}/flows/{flow}/validationResult'
    _globals['_IMPORTFLOWREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_IMPORTFLOWREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA \x12\x1edialogflow.googleapis.com/Flow'
    _globals['_IMPORTFLOWREQUEST'].fields_by_name['flow_import_strategy']._loaded_options = None
    _globals['_IMPORTFLOWREQUEST'].fields_by_name['flow_import_strategy']._serialized_options = b'\xe0A\x01'
    _globals['_FLOWIMPORTSTRATEGY'].fields_by_name['global_import_strategy']._loaded_options = None
    _globals['_FLOWIMPORTSTRATEGY'].fields_by_name['global_import_strategy']._serialized_options = b'\xe0A\x01'
    _globals['_IMPORTFLOWRESPONSE'].fields_by_name['flow']._loaded_options = None
    _globals['_IMPORTFLOWRESPONSE'].fields_by_name['flow']._serialized_options = b'\xfaA \n\x1edialogflow.googleapis.com/Flow'
    _globals['_EXPORTFLOWREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_EXPORTFLOWREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA \n\x1edialogflow.googleapis.com/Flow'
    _globals['_EXPORTFLOWREQUEST'].fields_by_name['flow_uri']._loaded_options = None
    _globals['_EXPORTFLOWREQUEST'].fields_by_name['flow_uri']._serialized_options = b'\xe0A\x01'
    _globals['_EXPORTFLOWREQUEST'].fields_by_name['include_referenced_flows']._loaded_options = None
    _globals['_EXPORTFLOWREQUEST'].fields_by_name['include_referenced_flows']._serialized_options = b'\xe0A\x01'
    _globals['_FLOWS']._loaded_options = None
    _globals['_FLOWS']._serialized_options = b'\xcaA\x19dialogflow.googleapis.com\xd2AYhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflow'
    _globals['_FLOWS'].methods_by_name['CreateFlow']._loaded_options = None
    _globals['_FLOWS'].methods_by_name['CreateFlow']._serialized_options = b'\xdaA\x0bparent,flow\x82\xd3\xe4\x93\x02?"7/v3beta1/{parent=projects/*/locations/*/agents/*}/flows:\x04flow'
    _globals['_FLOWS'].methods_by_name['DeleteFlow']._loaded_options = None
    _globals['_FLOWS'].methods_by_name['DeleteFlow']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x029*7/v3beta1/{name=projects/*/locations/*/agents/*/flows/*}'
    _globals['_FLOWS'].methods_by_name['ListFlows']._loaded_options = None
    _globals['_FLOWS'].methods_by_name['ListFlows']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x029\x127/v3beta1/{parent=projects/*/locations/*/agents/*}/flows'
    _globals['_FLOWS'].methods_by_name['GetFlow']._loaded_options = None
    _globals['_FLOWS'].methods_by_name['GetFlow']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x029\x127/v3beta1/{name=projects/*/locations/*/agents/*/flows/*}'
    _globals['_FLOWS'].methods_by_name['UpdateFlow']._loaded_options = None
    _globals['_FLOWS'].methods_by_name['UpdateFlow']._serialized_options = b'\xdaA\x10flow,update_mask\x82\xd3\xe4\x93\x02D2</v3beta1/{flow.name=projects/*/locations/*/agents/*/flows/*}:\x04flow'
    _globals['_FLOWS'].methods_by_name['TrainFlow']._loaded_options = None
    _globals['_FLOWS'].methods_by_name['TrainFlow']._serialized_options = b'\xcaA/\n\x15google.protobuf.Empty\x12\x16google.protobuf.Struct\xdaA\x04name\x82\xd3\xe4\x93\x02B"=/v3beta1/{name=projects/*/locations/*/agents/*/flows/*}:train:\x01*'
    _globals['_FLOWS'].methods_by_name['ValidateFlow']._loaded_options = None
    _globals['_FLOWS'].methods_by_name['ValidateFlow']._serialized_options = b'\x82\xd3\xe4\x93\x02E"@/v3beta1/{name=projects/*/locations/*/agents/*/flows/*}:validate:\x01*'
    _globals['_FLOWS'].methods_by_name['GetFlowValidationResult']._loaded_options = None
    _globals['_FLOWS'].methods_by_name['GetFlowValidationResult']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02J\x12H/v3beta1/{name=projects/*/locations/*/agents/*/flows/*/validationResult}'
    _globals['_FLOWS'].methods_by_name['ImportFlow']._loaded_options = None
    _globals['_FLOWS'].methods_by_name['ImportFlow']._serialized_options = b'\xcaA,\n\x12ImportFlowResponse\x12\x16google.protobuf.Struct\x82\xd3\xe4\x93\x02C">/v3beta1/{parent=projects/*/locations/*/agents/*}/flows:import:\x01*'
    _globals['_FLOWS'].methods_by_name['ExportFlow']._loaded_options = None
    _globals['_FLOWS'].methods_by_name['ExportFlow']._serialized_options = b'\xcaA,\n\x12ExportFlowResponse\x12\x16google.protobuf.Struct\x82\xd3\xe4\x93\x02C">/v3beta1/{name=projects/*/locations/*/agents/*/flows/*}:export:\x01*'
    _globals['_NLUSETTINGS']._serialized_start = 590
    _globals['_NLUSETTINGS']._serialized_end = 1028
    _globals['_NLUSETTINGS_MODELTYPE']._serialized_start = 814
    _globals['_NLUSETTINGS_MODELTYPE']._serialized_end = 903
    _globals['_NLUSETTINGS_MODELTRAININGMODE']._serialized_start = 905
    _globals['_NLUSETTINGS_MODELTRAININGMODE']._serialized_end = 1028
    _globals['_FLOW']._serialized_start = 1031
    _globals['_FLOW']._serialized_end = 1941
    _globals['_FLOW_MULTILANGUAGESETTINGS']._serialized_start = 1718
    _globals['_FLOW_MULTILANGUAGESETTINGS']._serialized_end = 1835
    _globals['_CREATEFLOWREQUEST']._serialized_start = 1944
    _globals['_CREATEFLOWREQUEST']._serialized_end = 2103
    _globals['_DELETEFLOWREQUEST']._serialized_start = 2105
    _globals['_DELETEFLOWREQUEST']._serialized_end = 2193
    _globals['_LISTFLOWSREQUEST']._serialized_start = 2196
    _globals['_LISTFLOWSREQUEST']._serialized_end = 2332
    _globals['_LISTFLOWSRESPONSE']._serialized_start = 2334
    _globals['_LISTFLOWSRESPONSE']._serialized_end = 2435
    _globals['_GETFLOWREQUEST']._serialized_start = 2437
    _globals['_GETFLOWREQUEST']._serialized_end = 2530
    _globals['_UPDATEFLOWREQUEST']._serialized_start = 2533
    _globals['_UPDATEFLOWREQUEST']._serialized_end = 2685
    _globals['_TRAINFLOWREQUEST']._serialized_start = 2687
    _globals['_TRAINFLOWREQUEST']._serialized_end = 2759
    _globals['_VALIDATEFLOWREQUEST']._serialized_start = 2761
    _globals['_VALIDATEFLOWREQUEST']._serialized_end = 2859
    _globals['_GETFLOWVALIDATIONRESULTREQUEST']._serialized_start = 2861
    _globals['_GETFLOWVALIDATIONRESULTREQUEST']._serialized_end = 2986
    _globals['_FLOWVALIDATIONRESULT']._serialized_start = 2989
    _globals['_FLOWVALIDATIONRESULT']._serialized_end = 3299
    _globals['_IMPORTFLOWREQUEST']._serialized_start = 3302
    _globals['_IMPORTFLOWREQUEST']._serialized_end = 3682
    _globals['_IMPORTFLOWREQUEST_IMPORTOPTION']._serialized_start = 3605
    _globals['_IMPORTFLOWREQUEST_IMPORTOPTION']._serialized_end = 3674
    _globals['_FLOWIMPORTSTRATEGY']._serialized_start = 3684
    _globals['_FLOWIMPORTSTRATEGY']._serialized_end = 3793
    _globals['_IMPORTFLOWRESPONSE']._serialized_start = 3795
    _globals['_IMPORTFLOWRESPONSE']._serialized_end = 3866
    _globals['_EXPORTFLOWREQUEST']._serialized_start = 3869
    _globals['_EXPORTFLOWREQUEST']._serialized_end = 4004
    _globals['_EXPORTFLOWRESPONSE']._serialized_start = 4006
    _globals['_EXPORTFLOWRESPONSE']._serialized_end = 4078
    _globals['_FLOWS']._serialized_start = 4081
    _globals['_FLOWS']._serialized_end = 6284