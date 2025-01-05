"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/dialogflow/cx/v3beta1/environment.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ......google.cloud.dialogflow.cx.v3beta1 import test_case_pb2 as google_dot_cloud_dot_dialogflow_dot_cx_dot_v3beta1_dot_test__case__pb2
from ......google.cloud.dialogflow.cx.v3beta1 import webhook_pb2 as google_dot_cloud_dot_dialogflow_dot_cx_dot_v3beta1_dot_webhook__pb2
from ......google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4google/cloud/dialogflow/cx/v3beta1/environment.proto\x12"google.cloud.dialogflow.cx.v3beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a2google/cloud/dialogflow/cx/v3beta1/test_case.proto\x1a0google/cloud/dialogflow/cx/v3beta1/webhook.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xc3\x06\n\x0bEnvironment\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x13\n\x0bdescription\x18\x03 \x01(\t\x12V\n\x0fversion_configs\x18\x06 \x03(\x0b2=.google.cloud.dialogflow.cx.v3beta1.Environment.VersionConfig\x124\n\x0bupdate_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12Z\n\x11test_cases_config\x18\x07 \x01(\x0b2?.google.cloud.dialogflow.cx.v3beta1.Environment.TestCasesConfig\x12U\n\x0ewebhook_config\x18\n \x01(\x0b2=.google.cloud.dialogflow.cx.v3beta1.Environment.WebhookConfig\x1aK\n\rVersionConfig\x12:\n\x07version\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!dialogflow.googleapis.com/Version\x1a\x8f\x01\n\x0fTestCasesConfig\x12;\n\ntest_cases\x18\x01 \x03(\tB\'\xfaA$\n"dialogflow.googleapis.com/TestCase\x12\x1d\n\x15enable_continuous_run\x18\x02 \x01(\x08\x12 \n\x18enable_predeployment_run\x18\x03 \x01(\x08\x1aW\n\rWebhookConfig\x12F\n\x11webhook_overrides\x18\x01 \x03(\x0b2+.google.cloud.dialogflow.cx.v3beta1.Webhook:}\xeaAz\n%dialogflow.googleapis.com/Environment\x12Qprojects/{project}/locations/{location}/agents/{agent}/environments/{environment}"\x7f\n\x17ListEnvironmentsRequest\x12=\n\x06parent\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\x12%dialogflow.googleapis.com/Environment\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"z\n\x18ListEnvironmentsResponse\x12E\n\x0cenvironments\x18\x01 \x03(\x0b2/.google.cloud.dialogflow.cx.v3beta1.Environment\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"T\n\x15GetEnvironmentRequest\x12;\n\x04name\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%dialogflow.googleapis.com/Environment"\xa4\x01\n\x18CreateEnvironmentRequest\x12=\n\x06parent\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\x12%dialogflow.googleapis.com/Environment\x12I\n\x0benvironment\x18\x02 \x01(\x0b2/.google.cloud.dialogflow.cx.v3beta1.EnvironmentB\x03\xe0A\x02"\x9b\x01\n\x18UpdateEnvironmentRequest\x12I\n\x0benvironment\x18\x01 \x01(\x0b2/.google.cloud.dialogflow.cx.v3beta1.EnvironmentB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02"W\n\x18DeleteEnvironmentRequest\x12;\n\x04name\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%dialogflow.googleapis.com/Environment"\x85\x01\n\x1fLookupEnvironmentHistoryRequest\x12;\n\x04name\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%dialogflow.googleapis.com/Environment\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"\x82\x01\n LookupEnvironmentHistoryResponse\x12E\n\x0cenvironments\x18\x01 \x03(\x0b2/.google.cloud.dialogflow.cx.v3beta1.Environment\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\x8d\x04\n\x14ContinuousTestResult\x12\x0c\n\x04name\x18\x01 \x01(\t\x12]\n\x06result\x18\x02 \x01(\x0e2M.google.cloud.dialogflow.cx.v3beta1.ContinuousTestResult.AggregatedTestResult\x12H\n\x11test_case_results\x18\x03 \x03(\tB-\xfaA*\n(dialogflow.googleapis.com/TestCaseResult\x12,\n\x08run_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp"V\n\x14AggregatedTestResult\x12&\n"AGGREGATED_TEST_RESULT_UNSPECIFIED\x10\x00\x12\n\n\x06PASSED\x10\x01\x12\n\n\x06FAILED\x10\x02:\xb7\x01\xeaA\xb3\x01\n.dialogflow.googleapis.com/ContinuousTestResult\x12\x80\x01projects/{project}/locations/{location}/agents/{agent}/environments/{environment}/continuousTestResults/{continuous_test_result}"^\n\x18RunContinuousTestRequest\x12B\n\x0benvironment\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%dialogflow.googleapis.com/Environment"u\n\x19RunContinuousTestResponse\x12X\n\x16continuous_test_result\x18\x01 \x01(\x0b28.google.cloud.dialogflow.cx.v3beta1.ContinuousTestResult"Z\n\x19RunContinuousTestMetadata\x12=\n\x06errors\x18\x01 \x03(\x0b2-.google.cloud.dialogflow.cx.v3beta1.TestError"\x91\x01\n ListContinuousTestResultsRequest\x12F\n\x06parent\x18\x01 \x01(\tB6\xe0A\x02\xfaA0\x12.dialogflow.googleapis.com/ContinuousTestResult\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"\x97\x01\n!ListContinuousTestResultsResponse\x12Y\n\x17continuous_test_results\x18\x01 \x03(\x0b28.google.cloud.dialogflow.cx.v3beta1.ContinuousTestResult\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\x98\x01\n\x11DeployFlowRequest\x12B\n\x0benvironment\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%dialogflow.googleapis.com/Environment\x12?\n\x0cflow_version\x18\x02 \x01(\tB)\xe0A\x02\xfaA#\n!dialogflow.googleapis.com/Version"n\n\x12DeployFlowResponse\x12D\n\x0benvironment\x18\x01 \x01(\x0b2/.google.cloud.dialogflow.cx.v3beta1.Environment\x12\x12\n\ndeployment\x18\x02 \x01(\t"X\n\x12DeployFlowMetadata\x12B\n\x0btest_errors\x18\x01 \x03(\x0b2-.google.cloud.dialogflow.cx.v3beta1.TestError2\xb2\x12\n\x0cEnvironments\x12\xde\x01\n\x10ListEnvironments\x12;.google.cloud.dialogflow.cx.v3beta1.ListEnvironmentsRequest\x1a<.google.cloud.dialogflow.cx.v3beta1.ListEnvironmentsResponse"O\xdaA\x06parent\x82\xd3\xe4\x93\x02@\x12>/v3beta1/{parent=projects/*/locations/*/agents/*}/environments\x12\xcb\x01\n\x0eGetEnvironment\x129.google.cloud.dialogflow.cx.v3beta1.GetEnvironmentRequest\x1a/.google.cloud.dialogflow.cx.v3beta1.Environment"M\xdaA\x04name\x82\xd3\xe4\x93\x02@\x12>/v3beta1/{name=projects/*/locations/*/agents/*/environments/*}\x12\x83\x02\n\x11CreateEnvironment\x12<.google.cloud.dialogflow.cx.v3beta1.CreateEnvironmentRequest\x1a\x1d.google.longrunning.Operation"\x90\x01\xcaA%\n\x0bEnvironment\x12\x16google.protobuf.Struct\xdaA\x12parent,environment\x82\xd3\xe4\x93\x02M">/v3beta1/{parent=projects/*/locations/*/agents/*}/environments:\x0benvironment\x12\x94\x02\n\x11UpdateEnvironment\x12<.google.cloud.dialogflow.cx.v3beta1.UpdateEnvironmentRequest\x1a\x1d.google.longrunning.Operation"\xa1\x01\xcaA%\n\x0bEnvironment\x12\x16google.protobuf.Struct\xdaA\x17environment,update_mask\x82\xd3\xe4\x93\x02Y2J/v3beta1/{environment.name=projects/*/locations/*/agents/*/environments/*}:\x0benvironment\x12\xb8\x01\n\x11DeleteEnvironment\x12<.google.cloud.dialogflow.cx.v3beta1.DeleteEnvironmentRequest\x1a\x16.google.protobuf.Empty"M\xdaA\x04name\x82\xd3\xe4\x93\x02@*>/v3beta1/{name=projects/*/locations/*/agents/*/environments/*}\x12\x8d\x02\n\x18LookupEnvironmentHistory\x12C.google.cloud.dialogflow.cx.v3beta1.LookupEnvironmentHistoryRequest\x1aD.google.cloud.dialogflow.cx.v3beta1.LookupEnvironmentHistoryResponse"f\xdaA\x04name\x82\xd3\xe4\x93\x02Y\x12W/v3beta1/{name=projects/*/locations/*/agents/*/environments/*}:lookupEnvironmentHistory\x12\x8e\x02\n\x11RunContinuousTest\x12<.google.cloud.dialogflow.cx.v3beta1.RunContinuousTestRequest\x1a\x1d.google.longrunning.Operation"\x9b\x01\xcaA6\n\x19RunContinuousTestResponse\x12\x19RunContinuousTestMetadata\x82\xd3\xe4\x93\x02\\"W/v3beta1/{environment=projects/*/locations/*/agents/*/environments/*}:runContinuousTest:\x01*\x12\x91\x02\n\x19ListContinuousTestResults\x12D.google.cloud.dialogflow.cx.v3beta1.ListContinuousTestResultsRequest\x1aE.google.cloud.dialogflow.cx.v3beta1.ListContinuousTestResultsResponse"g\xdaA\x06parent\x82\xd3\xe4\x93\x02X\x12V/v3beta1/{parent=projects/*/locations/*/agents/*/environments/*}/continuousTestResults\x12\xeb\x01\n\nDeployFlow\x125.google.cloud.dialogflow.cx.v3beta1.DeployFlowRequest\x1a\x1d.google.longrunning.Operation"\x86\x01\xcaA(\n\x12DeployFlowResponse\x12\x12DeployFlowMetadata\x82\xd3\xe4\x93\x02U"P/v3beta1/{environment=projects/*/locations/*/agents/*/environments/*}:deployFlow:\x01*\x1ax\xcaA\x19dialogflow.googleapis.com\xd2AYhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflowB\xca\x01\n&com.google.cloud.dialogflow.cx.v3beta1B\x10EnvironmentProtoP\x01Z6cloud.google.com/go/dialogflow/cx/apiv3beta1/cxpb;cxpb\xf8\x01\x01\xa2\x02\x02DF\xaa\x02"Google.Cloud.Dialogflow.Cx.V3Beta1\xea\x02&Google::Cloud::Dialogflow::CX::V3beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.dialogflow.cx.v3beta1.environment_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.cloud.dialogflow.cx.v3beta1B\x10EnvironmentProtoP\x01Z6cloud.google.com/go/dialogflow/cx/apiv3beta1/cxpb;cxpb\xf8\x01\x01\xa2\x02\x02DF\xaa\x02"Google.Cloud.Dialogflow.Cx.V3Beta1\xea\x02&Google::Cloud::Dialogflow::CX::V3beta1'
    _globals['_ENVIRONMENT_VERSIONCONFIG'].fields_by_name['version']._loaded_options = None
    _globals['_ENVIRONMENT_VERSIONCONFIG'].fields_by_name['version']._serialized_options = b'\xe0A\x02\xfaA#\n!dialogflow.googleapis.com/Version'
    _globals['_ENVIRONMENT_TESTCASESCONFIG'].fields_by_name['test_cases']._loaded_options = None
    _globals['_ENVIRONMENT_TESTCASESCONFIG'].fields_by_name['test_cases']._serialized_options = b'\xfaA$\n"dialogflow.googleapis.com/TestCase'
    _globals['_ENVIRONMENT'].fields_by_name['display_name']._loaded_options = None
    _globals['_ENVIRONMENT'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_ENVIRONMENT'].fields_by_name['update_time']._loaded_options = None
    _globals['_ENVIRONMENT'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_ENVIRONMENT']._loaded_options = None
    _globals['_ENVIRONMENT']._serialized_options = b'\xeaAz\n%dialogflow.googleapis.com/Environment\x12Qprojects/{project}/locations/{location}/agents/{agent}/environments/{environment}'
    _globals['_LISTENVIRONMENTSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTENVIRONMENTSREQUEST'].fields_by_name['parent']._serialized_options = b"\xe0A\x02\xfaA'\x12%dialogflow.googleapis.com/Environment"
    _globals['_GETENVIRONMENTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETENVIRONMENTREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA'\n%dialogflow.googleapis.com/Environment"
    _globals['_CREATEENVIRONMENTREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEENVIRONMENTREQUEST'].fields_by_name['parent']._serialized_options = b"\xe0A\x02\xfaA'\x12%dialogflow.googleapis.com/Environment"
    _globals['_CREATEENVIRONMENTREQUEST'].fields_by_name['environment']._loaded_options = None
    _globals['_CREATEENVIRONMENTREQUEST'].fields_by_name['environment']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEENVIRONMENTREQUEST'].fields_by_name['environment']._loaded_options = None
    _globals['_UPDATEENVIRONMENTREQUEST'].fields_by_name['environment']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEENVIRONMENTREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEENVIRONMENTREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEENVIRONMENTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEENVIRONMENTREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA'\n%dialogflow.googleapis.com/Environment"
    _globals['_LOOKUPENVIRONMENTHISTORYREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_LOOKUPENVIRONMENTHISTORYREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA'\n%dialogflow.googleapis.com/Environment"
    _globals['_CONTINUOUSTESTRESULT'].fields_by_name['test_case_results']._loaded_options = None
    _globals['_CONTINUOUSTESTRESULT'].fields_by_name['test_case_results']._serialized_options = b'\xfaA*\n(dialogflow.googleapis.com/TestCaseResult'
    _globals['_CONTINUOUSTESTRESULT']._loaded_options = None
    _globals['_CONTINUOUSTESTRESULT']._serialized_options = b'\xeaA\xb3\x01\n.dialogflow.googleapis.com/ContinuousTestResult\x12\x80\x01projects/{project}/locations/{location}/agents/{agent}/environments/{environment}/continuousTestResults/{continuous_test_result}'
    _globals['_RUNCONTINUOUSTESTREQUEST'].fields_by_name['environment']._loaded_options = None
    _globals['_RUNCONTINUOUSTESTREQUEST'].fields_by_name['environment']._serialized_options = b"\xe0A\x02\xfaA'\n%dialogflow.googleapis.com/Environment"
    _globals['_LISTCONTINUOUSTESTRESULTSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTCONTINUOUSTESTRESULTSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA0\x12.dialogflow.googleapis.com/ContinuousTestResult'
    _globals['_DEPLOYFLOWREQUEST'].fields_by_name['environment']._loaded_options = None
    _globals['_DEPLOYFLOWREQUEST'].fields_by_name['environment']._serialized_options = b"\xe0A\x02\xfaA'\n%dialogflow.googleapis.com/Environment"
    _globals['_DEPLOYFLOWREQUEST'].fields_by_name['flow_version']._loaded_options = None
    _globals['_DEPLOYFLOWREQUEST'].fields_by_name['flow_version']._serialized_options = b'\xe0A\x02\xfaA#\n!dialogflow.googleapis.com/Version'
    _globals['_ENVIRONMENTS']._loaded_options = None
    _globals['_ENVIRONMENTS']._serialized_options = b'\xcaA\x19dialogflow.googleapis.com\xd2AYhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflow'
    _globals['_ENVIRONMENTS'].methods_by_name['ListEnvironments']._loaded_options = None
    _globals['_ENVIRONMENTS'].methods_by_name['ListEnvironments']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02@\x12>/v3beta1/{parent=projects/*/locations/*/agents/*}/environments'
    _globals['_ENVIRONMENTS'].methods_by_name['GetEnvironment']._loaded_options = None
    _globals['_ENVIRONMENTS'].methods_by_name['GetEnvironment']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02@\x12>/v3beta1/{name=projects/*/locations/*/agents/*/environments/*}'
    _globals['_ENVIRONMENTS'].methods_by_name['CreateEnvironment']._loaded_options = None
    _globals['_ENVIRONMENTS'].methods_by_name['CreateEnvironment']._serialized_options = b'\xcaA%\n\x0bEnvironment\x12\x16google.protobuf.Struct\xdaA\x12parent,environment\x82\xd3\xe4\x93\x02M">/v3beta1/{parent=projects/*/locations/*/agents/*}/environments:\x0benvironment'
    _globals['_ENVIRONMENTS'].methods_by_name['UpdateEnvironment']._loaded_options = None
    _globals['_ENVIRONMENTS'].methods_by_name['UpdateEnvironment']._serialized_options = b'\xcaA%\n\x0bEnvironment\x12\x16google.protobuf.Struct\xdaA\x17environment,update_mask\x82\xd3\xe4\x93\x02Y2J/v3beta1/{environment.name=projects/*/locations/*/agents/*/environments/*}:\x0benvironment'
    _globals['_ENVIRONMENTS'].methods_by_name['DeleteEnvironment']._loaded_options = None
    _globals['_ENVIRONMENTS'].methods_by_name['DeleteEnvironment']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02@*>/v3beta1/{name=projects/*/locations/*/agents/*/environments/*}'
    _globals['_ENVIRONMENTS'].methods_by_name['LookupEnvironmentHistory']._loaded_options = None
    _globals['_ENVIRONMENTS'].methods_by_name['LookupEnvironmentHistory']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02Y\x12W/v3beta1/{name=projects/*/locations/*/agents/*/environments/*}:lookupEnvironmentHistory'
    _globals['_ENVIRONMENTS'].methods_by_name['RunContinuousTest']._loaded_options = None
    _globals['_ENVIRONMENTS'].methods_by_name['RunContinuousTest']._serialized_options = b'\xcaA6\n\x19RunContinuousTestResponse\x12\x19RunContinuousTestMetadata\x82\xd3\xe4\x93\x02\\"W/v3beta1/{environment=projects/*/locations/*/agents/*/environments/*}:runContinuousTest:\x01*'
    _globals['_ENVIRONMENTS'].methods_by_name['ListContinuousTestResults']._loaded_options = None
    _globals['_ENVIRONMENTS'].methods_by_name['ListContinuousTestResults']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02X\x12V/v3beta1/{parent=projects/*/locations/*/agents/*/environments/*}/continuousTestResults'
    _globals['_ENVIRONMENTS'].methods_by_name['DeployFlow']._loaded_options = None
    _globals['_ENVIRONMENTS'].methods_by_name['DeployFlow']._serialized_options = b'\xcaA(\n\x12DeployFlowResponse\x12\x12DeployFlowMetadata\x82\xd3\xe4\x93\x02U"P/v3beta1/{environment=projects/*/locations/*/agents/*/environments/*}:deployFlow:\x01*'
    _globals['_ENVIRONMENT']._serialized_start = 473
    _globals['_ENVIRONMENT']._serialized_end = 1308
    _globals['_ENVIRONMENT_VERSIONCONFIG']._serialized_start = 871
    _globals['_ENVIRONMENT_VERSIONCONFIG']._serialized_end = 946
    _globals['_ENVIRONMENT_TESTCASESCONFIG']._serialized_start = 949
    _globals['_ENVIRONMENT_TESTCASESCONFIG']._serialized_end = 1092
    _globals['_ENVIRONMENT_WEBHOOKCONFIG']._serialized_start = 1094
    _globals['_ENVIRONMENT_WEBHOOKCONFIG']._serialized_end = 1181
    _globals['_LISTENVIRONMENTSREQUEST']._serialized_start = 1310
    _globals['_LISTENVIRONMENTSREQUEST']._serialized_end = 1437
    _globals['_LISTENVIRONMENTSRESPONSE']._serialized_start = 1439
    _globals['_LISTENVIRONMENTSRESPONSE']._serialized_end = 1561
    _globals['_GETENVIRONMENTREQUEST']._serialized_start = 1563
    _globals['_GETENVIRONMENTREQUEST']._serialized_end = 1647
    _globals['_CREATEENVIRONMENTREQUEST']._serialized_start = 1650
    _globals['_CREATEENVIRONMENTREQUEST']._serialized_end = 1814
    _globals['_UPDATEENVIRONMENTREQUEST']._serialized_start = 1817
    _globals['_UPDATEENVIRONMENTREQUEST']._serialized_end = 1972
    _globals['_DELETEENVIRONMENTREQUEST']._serialized_start = 1974
    _globals['_DELETEENVIRONMENTREQUEST']._serialized_end = 2061
    _globals['_LOOKUPENVIRONMENTHISTORYREQUEST']._serialized_start = 2064
    _globals['_LOOKUPENVIRONMENTHISTORYREQUEST']._serialized_end = 2197
    _globals['_LOOKUPENVIRONMENTHISTORYRESPONSE']._serialized_start = 2200
    _globals['_LOOKUPENVIRONMENTHISTORYRESPONSE']._serialized_end = 2330
    _globals['_CONTINUOUSTESTRESULT']._serialized_start = 2333
    _globals['_CONTINUOUSTESTRESULT']._serialized_end = 2858
    _globals['_CONTINUOUSTESTRESULT_AGGREGATEDTESTRESULT']._serialized_start = 2586
    _globals['_CONTINUOUSTESTRESULT_AGGREGATEDTESTRESULT']._serialized_end = 2672
    _globals['_RUNCONTINUOUSTESTREQUEST']._serialized_start = 2860
    _globals['_RUNCONTINUOUSTESTREQUEST']._serialized_end = 2954
    _globals['_RUNCONTINUOUSTESTRESPONSE']._serialized_start = 2956
    _globals['_RUNCONTINUOUSTESTRESPONSE']._serialized_end = 3073
    _globals['_RUNCONTINUOUSTESTMETADATA']._serialized_start = 3075
    _globals['_RUNCONTINUOUSTESTMETADATA']._serialized_end = 3165
    _globals['_LISTCONTINUOUSTESTRESULTSREQUEST']._serialized_start = 3168
    _globals['_LISTCONTINUOUSTESTRESULTSREQUEST']._serialized_end = 3313
    _globals['_LISTCONTINUOUSTESTRESULTSRESPONSE']._serialized_start = 3316
    _globals['_LISTCONTINUOUSTESTRESULTSRESPONSE']._serialized_end = 3467
    _globals['_DEPLOYFLOWREQUEST']._serialized_start = 3470
    _globals['_DEPLOYFLOWREQUEST']._serialized_end = 3622
    _globals['_DEPLOYFLOWRESPONSE']._serialized_start = 3624
    _globals['_DEPLOYFLOWRESPONSE']._serialized_end = 3734
    _globals['_DEPLOYFLOWMETADATA']._serialized_start = 3736
    _globals['_DEPLOYFLOWMETADATA']._serialized_end = 3824
    _globals['_ENVIRONMENTS']._serialized_start = 3827
    _globals['_ENVIRONMENTS']._serialized_end = 6181