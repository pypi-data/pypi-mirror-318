"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/dialogflow/cx/v3/flow.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ......google.cloud.dialogflow.cx.v3 import advanced_settings_pb2 as google_dot_cloud_dot_dialogflow_dot_cx_dot_v3_dot_advanced__settings__pb2
from ......google.cloud.dialogflow.cx.v3 import import_strategy_pb2 as google_dot_cloud_dot_dialogflow_dot_cx_dot_v3_dot_import__strategy__pb2
from ......google.cloud.dialogflow.cx.v3 import page_pb2 as google_dot_cloud_dot_dialogflow_dot_cx_dot_v3_dot_page__pb2
from ......google.cloud.dialogflow.cx.v3 import validation_message_pb2 as google_dot_cloud_dot_dialogflow_dot_cx_dot_v3_dot_validation__message__pb2
from ......google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(google/cloud/dialogflow/cx/v3/flow.proto\x12\x1dgoogle.cloud.dialogflow.cx.v3\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a5google/cloud/dialogflow/cx/v3/advanced_settings.proto\x1a3google/cloud/dialogflow/cx/v3/import_strategy.proto\x1a(google/cloud/dialogflow/cx/v3/page.proto\x1a6google/cloud/dialogflow/cx/v3/validation_message.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xac\x03\n\x0bNluSettings\x12H\n\nmodel_type\x18\x01 \x01(\x0e24.google.cloud.dialogflow.cx.v3.NluSettings.ModelType\x12 \n\x18classification_threshold\x18\x03 \x01(\x02\x12Y\n\x13model_training_mode\x18\x04 \x01(\x0e2<.google.cloud.dialogflow.cx.v3.NluSettings.ModelTrainingMode"Y\n\tModelType\x12\x1a\n\x16MODEL_TYPE_UNSPECIFIED\x10\x00\x12\x17\n\x13MODEL_TYPE_STANDARD\x10\x01\x12\x17\n\x13MODEL_TYPE_ADVANCED\x10\x03"{\n\x11ModelTrainingMode\x12#\n\x1fMODEL_TRAINING_MODE_UNSPECIFIED\x10\x00\x12!\n\x1dMODEL_TRAINING_MODE_AUTOMATIC\x10\x01\x12\x1e\n\x1aMODEL_TRAINING_MODE_MANUAL\x10\x02"\xf0\x06\n\x04Flow\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x13\n\x0bdescription\x18\x03 \x01(\t\x12I\n\x11transition_routes\x18\x04 \x03(\x0b2..google.cloud.dialogflow.cx.v3.TransitionRoute\x12C\n\x0eevent_handlers\x18\n \x03(\x0b2+.google.cloud.dialogflow.cx.v3.EventHandler\x12T\n\x17transition_route_groups\x18\x0f \x03(\tB3\xfaA0\n.dialogflow.googleapis.com/TransitionRouteGroup\x12@\n\x0cnlu_settings\x18\x0b \x01(\x0b2*.google.cloud.dialogflow.cx.v3.NluSettings\x12J\n\x11advanced_settings\x18\x0e \x01(\x0b2/.google.cloud.dialogflow.cx.v3.AdvancedSettings\x12d\n\x1cknowledge_connector_settings\x18\x12 \x01(\x0b29.google.cloud.dialogflow.cx.v3.KnowledgeConnectorSettingsB\x03\xe0A\x01\x12_\n\x17multi_language_settings\x18\x1c \x01(\x0b29.google.cloud.dialogflow.cx.v3.Flow.MultiLanguageSettingsB\x03\xe0A\x01\x12\x0e\n\x06locked\x18\x1e \x01(\x08\x1au\n\x15MultiLanguageSettings\x12,\n\x1fenable_multi_language_detection\x18\x01 \x01(\x08B\x03\xe0A\x01\x12.\n!supported_response_language_codes\x18\x02 \x03(\tB\x03\xe0A\x01:h\xeaAe\n\x1edialogflow.googleapis.com/Flow\x12Cprojects/{project}/locations/{location}/agents/{agent}/flows/{flow}"\x9a\x01\n\x11CreateFlowRequest\x126\n\x06parent\x18\x01 \x01(\tB&\xe0A\x02\xfaA \x12\x1edialogflow.googleapis.com/Flow\x126\n\x04flow\x18\x02 \x01(\x0b2#.google.cloud.dialogflow.cx.v3.FlowB\x03\xe0A\x02\x12\x15\n\rlanguage_code\x18\x03 \x01(\t"X\n\x11DeleteFlowRequest\x124\n\x04name\x18\x01 \x01(\tB&\xe0A\x02\xfaA \n\x1edialogflow.googleapis.com/Flow\x12\r\n\x05force\x18\x02 \x01(\x08"\x88\x01\n\x10ListFlowsRequest\x126\n\x06parent\x18\x01 \x01(\tB&\xe0A\x02\xfaA \x12\x1edialogflow.googleapis.com/Flow\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x15\n\rlanguage_code\x18\x04 \x01(\t"`\n\x11ListFlowsResponse\x122\n\x05flows\x18\x01 \x03(\x0b2#.google.cloud.dialogflow.cx.v3.Flow\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"]\n\x0eGetFlowRequest\x124\n\x04name\x18\x01 \x01(\tB&\xe0A\x02\xfaA \n\x1edialogflow.googleapis.com/Flow\x12\x15\n\rlanguage_code\x18\x02 \x01(\t"\x93\x01\n\x11UpdateFlowRequest\x126\n\x04flow\x18\x01 \x01(\x0b2#.google.cloud.dialogflow.cx.v3.FlowB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12\x15\n\rlanguage_code\x18\x03 \x01(\t"H\n\x10TrainFlowRequest\x124\n\x04name\x18\x01 \x01(\tB&\xe0A\x02\xfaA \n\x1edialogflow.googleapis.com/Flow"b\n\x13ValidateFlowRequest\x124\n\x04name\x18\x01 \x01(\tB&\xe0A\x02\xfaA \n\x1edialogflow.googleapis.com/Flow\x12\x15\n\rlanguage_code\x18\x02 \x01(\t"}\n\x1eGetFlowValidationResultRequest\x12D\n\x04name\x18\x01 \x01(\tB6\xe0A\x02\xfaA0\n.dialogflow.googleapis.com/FlowValidationResult\x12\x15\n\rlanguage_code\x18\x02 \x01(\t"\xb1\x02\n\x14FlowValidationResult\x12\x0c\n\x04name\x18\x01 \x01(\t\x12M\n\x13validation_messages\x18\x02 \x03(\x0b20.google.cloud.dialogflow.cx.v3.ValidationMessage\x12/\n\x0bupdate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp:\x8a\x01\xeaA\x86\x01\n.dialogflow.googleapis.com/FlowValidationResult\x12Tprojects/{project}/locations/{location}/agents/{agent}/flows/{flow}/validationResult"\xf2\x02\n\x11ImportFlowRequest\x126\n\x06parent\x18\x01 \x01(\tB&\xe0A\x02\xfaA \x12\x1edialogflow.googleapis.com/Flow\x12\x12\n\x08flow_uri\x18\x02 \x01(\tH\x00\x12\x16\n\x0cflow_content\x18\x03 \x01(\x0cH\x00\x12T\n\rimport_option\x18\x04 \x01(\x0e2=.google.cloud.dialogflow.cx.v3.ImportFlowRequest.ImportOption\x12T\n\x14flow_import_strategy\x18\x05 \x01(\x0b21.google.cloud.dialogflow.cx.v3.FlowImportStrategyB\x03\xe0A\x01"E\n\x0cImportOption\x12\x1d\n\x19IMPORT_OPTION_UNSPECIFIED\x10\x00\x12\x08\n\x04KEEP\x10\x01\x12\x0c\n\x08FALLBACK\x10\x02B\x06\n\x04flow"h\n\x12FlowImportStrategy\x12R\n\x16global_import_strategy\x18\x01 \x01(\x0e2-.google.cloud.dialogflow.cx.v3.ImportStrategyB\x03\xe0A\x01"G\n\x12ImportFlowResponse\x121\n\x04flow\x18\x01 \x01(\tB#\xfaA \n\x1edialogflow.googleapis.com/Flow"\x87\x01\n\x11ExportFlowRequest\x124\n\x04name\x18\x01 \x01(\tB&\xe0A\x02\xfaA \n\x1edialogflow.googleapis.com/Flow\x12\x15\n\x08flow_uri\x18\x02 \x01(\tB\x03\xe0A\x01\x12%\n\x18include_referenced_flows\x18\x04 \x01(\x08B\x03\xe0A\x01"H\n\x12ExportFlowResponse\x12\x12\n\x08flow_uri\x18\x01 \x01(\tH\x00\x12\x16\n\x0cflow_content\x18\x02 \x01(\x0cH\x00B\x06\n\x04flow2\x98\x10\n\x05Flows\x12\xb3\x01\n\nCreateFlow\x120.google.cloud.dialogflow.cx.v3.CreateFlowRequest\x1a#.google.cloud.dialogflow.cx.v3.Flow"N\xdaA\x0bparent,flow\x82\xd3\xe4\x93\x02:"2/v3/{parent=projects/*/locations/*/agents/*}/flows:\x04flow\x12\x99\x01\n\nDeleteFlow\x120.google.cloud.dialogflow.cx.v3.DeleteFlowRequest\x1a\x16.google.protobuf.Empty"A\xdaA\x04name\x82\xd3\xe4\x93\x024*2/v3/{name=projects/*/locations/*/agents/*/flows/*}\x12\xb3\x01\n\tListFlows\x12/.google.cloud.dialogflow.cx.v3.ListFlowsRequest\x1a0.google.cloud.dialogflow.cx.v3.ListFlowsResponse"C\xdaA\x06parent\x82\xd3\xe4\x93\x024\x122/v3/{parent=projects/*/locations/*/agents/*}/flows\x12\xa0\x01\n\x07GetFlow\x12-.google.cloud.dialogflow.cx.v3.GetFlowRequest\x1a#.google.cloud.dialogflow.cx.v3.Flow"A\xdaA\x04name\x82\xd3\xe4\x93\x024\x122/v3/{name=projects/*/locations/*/agents/*/flows/*}\x12\xbd\x01\n\nUpdateFlow\x120.google.cloud.dialogflow.cx.v3.UpdateFlowRequest\x1a#.google.cloud.dialogflow.cx.v3.Flow"X\xdaA\x10flow,update_mask\x82\xd3\xe4\x93\x02?27/v3/{flow.name=projects/*/locations/*/agents/*/flows/*}:\x04flow\x12\xd9\x01\n\tTrainFlow\x12/.google.cloud.dialogflow.cx.v3.TrainFlowRequest\x1a\x1d.google.longrunning.Operation"|\xcaA/\n\x15google.protobuf.Empty\x12\x16google.protobuf.Struct\xdaA\x04name\x82\xd3\xe4\x93\x02="8/v3/{name=projects/*/locations/*/agents/*/flows/*}:train:\x01*\x12\xbf\x01\n\x0cValidateFlow\x122.google.cloud.dialogflow.cx.v3.ValidateFlowRequest\x1a3.google.cloud.dialogflow.cx.v3.FlowValidationResult"F\x82\xd3\xe4\x93\x02@";/v3/{name=projects/*/locations/*/agents/*/flows/*}:validate:\x01*\x12\xe1\x01\n\x17GetFlowValidationResult\x12=.google.cloud.dialogflow.cx.v3.GetFlowValidationResultRequest\x1a3.google.cloud.dialogflow.cx.v3.FlowValidationResult"R\xdaA\x04name\x82\xd3\xe4\x93\x02E\x12C/v3/{name=projects/*/locations/*/agents/*/flows/*/validationResult}\x12\xd2\x01\n\nImportFlow\x120.google.cloud.dialogflow.cx.v3.ImportFlowRequest\x1a\x1d.google.longrunning.Operation"s\xcaA,\n\x12ImportFlowResponse\x12\x16google.protobuf.Struct\x82\xd3\xe4\x93\x02>"9/v3/{parent=projects/*/locations/*/agents/*}/flows:import:\x01*\x12\xd2\x01\n\nExportFlow\x120.google.cloud.dialogflow.cx.v3.ExportFlowRequest\x1a\x1d.google.longrunning.Operation"s\xcaA,\n\x12ExportFlowResponse\x12\x16google.protobuf.Struct\x82\xd3\xe4\x93\x02>"9/v3/{name=projects/*/locations/*/agents/*/flows/*}:export:\x01*\x1ax\xcaA\x19dialogflow.googleapis.com\xd2AYhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflowB\xac\x01\n!com.google.cloud.dialogflow.cx.v3B\tFlowProtoP\x01Z1cloud.google.com/go/dialogflow/cx/apiv3/cxpb;cxpb\xa2\x02\x02DF\xaa\x02\x1dGoogle.Cloud.Dialogflow.Cx.V3\xea\x02!Google::Cloud::Dialogflow::CX::V3b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.dialogflow.cx.v3.flow_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n!com.google.cloud.dialogflow.cx.v3B\tFlowProtoP\x01Z1cloud.google.com/go/dialogflow/cx/apiv3/cxpb;cxpb\xa2\x02\x02DF\xaa\x02\x1dGoogle.Cloud.Dialogflow.Cx.V3\xea\x02!Google::Cloud::Dialogflow::CX::V3'
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
    _globals['_FLOWS'].methods_by_name['CreateFlow']._serialized_options = b'\xdaA\x0bparent,flow\x82\xd3\xe4\x93\x02:"2/v3/{parent=projects/*/locations/*/agents/*}/flows:\x04flow'
    _globals['_FLOWS'].methods_by_name['DeleteFlow']._loaded_options = None
    _globals['_FLOWS'].methods_by_name['DeleteFlow']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x024*2/v3/{name=projects/*/locations/*/agents/*/flows/*}'
    _globals['_FLOWS'].methods_by_name['ListFlows']._loaded_options = None
    _globals['_FLOWS'].methods_by_name['ListFlows']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x024\x122/v3/{parent=projects/*/locations/*/agents/*}/flows'
    _globals['_FLOWS'].methods_by_name['GetFlow']._loaded_options = None
    _globals['_FLOWS'].methods_by_name['GetFlow']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x024\x122/v3/{name=projects/*/locations/*/agents/*/flows/*}'
    _globals['_FLOWS'].methods_by_name['UpdateFlow']._loaded_options = None
    _globals['_FLOWS'].methods_by_name['UpdateFlow']._serialized_options = b'\xdaA\x10flow,update_mask\x82\xd3\xe4\x93\x02?27/v3/{flow.name=projects/*/locations/*/agents/*/flows/*}:\x04flow'
    _globals['_FLOWS'].methods_by_name['TrainFlow']._loaded_options = None
    _globals['_FLOWS'].methods_by_name['TrainFlow']._serialized_options = b'\xcaA/\n\x15google.protobuf.Empty\x12\x16google.protobuf.Struct\xdaA\x04name\x82\xd3\xe4\x93\x02="8/v3/{name=projects/*/locations/*/agents/*/flows/*}:train:\x01*'
    _globals['_FLOWS'].methods_by_name['ValidateFlow']._loaded_options = None
    _globals['_FLOWS'].methods_by_name['ValidateFlow']._serialized_options = b'\x82\xd3\xe4\x93\x02@";/v3/{name=projects/*/locations/*/agents/*/flows/*}:validate:\x01*'
    _globals['_FLOWS'].methods_by_name['GetFlowValidationResult']._loaded_options = None
    _globals['_FLOWS'].methods_by_name['GetFlowValidationResult']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02E\x12C/v3/{name=projects/*/locations/*/agents/*/flows/*/validationResult}'
    _globals['_FLOWS'].methods_by_name['ImportFlow']._loaded_options = None
    _globals['_FLOWS'].methods_by_name['ImportFlow']._serialized_options = b'\xcaA,\n\x12ImportFlowResponse\x12\x16google.protobuf.Struct\x82\xd3\xe4\x93\x02>"9/v3/{parent=projects/*/locations/*/agents/*}/flows:import:\x01*'
    _globals['_FLOWS'].methods_by_name['ExportFlow']._loaded_options = None
    _globals['_FLOWS'].methods_by_name['ExportFlow']._serialized_options = b'\xcaA,\n\x12ExportFlowResponse\x12\x16google.protobuf.Struct\x82\xd3\xe4\x93\x02>"9/v3/{name=projects/*/locations/*/agents/*/flows/*}:export:\x01*'
    _globals['_NLUSETTINGS']._serialized_start = 560
    _globals['_NLUSETTINGS']._serialized_end = 988
    _globals['_NLUSETTINGS_MODELTYPE']._serialized_start = 774
    _globals['_NLUSETTINGS_MODELTYPE']._serialized_end = 863
    _globals['_NLUSETTINGS_MODELTRAININGMODE']._serialized_start = 865
    _globals['_NLUSETTINGS_MODELTRAININGMODE']._serialized_end = 988
    _globals['_FLOW']._serialized_start = 991
    _globals['_FLOW']._serialized_end = 1871
    _globals['_FLOW_MULTILANGUAGESETTINGS']._serialized_start = 1648
    _globals['_FLOW_MULTILANGUAGESETTINGS']._serialized_end = 1765
    _globals['_CREATEFLOWREQUEST']._serialized_start = 1874
    _globals['_CREATEFLOWREQUEST']._serialized_end = 2028
    _globals['_DELETEFLOWREQUEST']._serialized_start = 2030
    _globals['_DELETEFLOWREQUEST']._serialized_end = 2118
    _globals['_LISTFLOWSREQUEST']._serialized_start = 2121
    _globals['_LISTFLOWSREQUEST']._serialized_end = 2257
    _globals['_LISTFLOWSRESPONSE']._serialized_start = 2259
    _globals['_LISTFLOWSRESPONSE']._serialized_end = 2355
    _globals['_GETFLOWREQUEST']._serialized_start = 2357
    _globals['_GETFLOWREQUEST']._serialized_end = 2450
    _globals['_UPDATEFLOWREQUEST']._serialized_start = 2453
    _globals['_UPDATEFLOWREQUEST']._serialized_end = 2600
    _globals['_TRAINFLOWREQUEST']._serialized_start = 2602
    _globals['_TRAINFLOWREQUEST']._serialized_end = 2674
    _globals['_VALIDATEFLOWREQUEST']._serialized_start = 2676
    _globals['_VALIDATEFLOWREQUEST']._serialized_end = 2774
    _globals['_GETFLOWVALIDATIONRESULTREQUEST']._serialized_start = 2776
    _globals['_GETFLOWVALIDATIONRESULTREQUEST']._serialized_end = 2901
    _globals['_FLOWVALIDATIONRESULT']._serialized_start = 2904
    _globals['_FLOWVALIDATIONRESULT']._serialized_end = 3209
    _globals['_IMPORTFLOWREQUEST']._serialized_start = 3212
    _globals['_IMPORTFLOWREQUEST']._serialized_end = 3582
    _globals['_IMPORTFLOWREQUEST_IMPORTOPTION']._serialized_start = 3505
    _globals['_IMPORTFLOWREQUEST_IMPORTOPTION']._serialized_end = 3574
    _globals['_FLOWIMPORTSTRATEGY']._serialized_start = 3584
    _globals['_FLOWIMPORTSTRATEGY']._serialized_end = 3688
    _globals['_IMPORTFLOWRESPONSE']._serialized_start = 3690
    _globals['_IMPORTFLOWRESPONSE']._serialized_end = 3761
    _globals['_EXPORTFLOWREQUEST']._serialized_start = 3764
    _globals['_EXPORTFLOWREQUEST']._serialized_end = 3899
    _globals['_EXPORTFLOWRESPONSE']._serialized_start = 3901
    _globals['_EXPORTFLOWRESPONSE']._serialized_end = 3973
    _globals['_FLOWS']._serialized_start = 3976
    _globals['_FLOWS']._serialized_end = 6048