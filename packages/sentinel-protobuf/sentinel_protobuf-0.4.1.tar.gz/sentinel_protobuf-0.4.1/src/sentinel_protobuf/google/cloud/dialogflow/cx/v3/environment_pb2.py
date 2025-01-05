"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/dialogflow/cx/v3/environment.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ......google.cloud.dialogflow.cx.v3 import test_case_pb2 as google_dot_cloud_dot_dialogflow_dot_cx_dot_v3_dot_test__case__pb2
from ......google.cloud.dialogflow.cx.v3 import webhook_pb2 as google_dot_cloud_dot_dialogflow_dot_cx_dot_v3_dot_webhook__pb2
from ......google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/google/cloud/dialogflow/cx/v3/environment.proto\x12\x1dgoogle.cloud.dialogflow.cx.v3\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a-google/cloud/dialogflow/cx/v3/test_case.proto\x1a+google/cloud/dialogflow/cx/v3/webhook.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xaf\x06\n\x0bEnvironment\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x13\n\x0bdescription\x18\x03 \x01(\t\x12Q\n\x0fversion_configs\x18\x06 \x03(\x0b28.google.cloud.dialogflow.cx.v3.Environment.VersionConfig\x124\n\x0bupdate_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12U\n\x11test_cases_config\x18\x07 \x01(\x0b2:.google.cloud.dialogflow.cx.v3.Environment.TestCasesConfig\x12P\n\x0ewebhook_config\x18\n \x01(\x0b28.google.cloud.dialogflow.cx.v3.Environment.WebhookConfig\x1aK\n\rVersionConfig\x12:\n\x07version\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!dialogflow.googleapis.com/Version\x1a\x8f\x01\n\x0fTestCasesConfig\x12;\n\ntest_cases\x18\x01 \x03(\tB\'\xfaA$\n"dialogflow.googleapis.com/TestCase\x12\x1d\n\x15enable_continuous_run\x18\x02 \x01(\x08\x12 \n\x18enable_predeployment_run\x18\x03 \x01(\x08\x1aR\n\rWebhookConfig\x12A\n\x11webhook_overrides\x18\x01 \x03(\x0b2&.google.cloud.dialogflow.cx.v3.Webhook:}\xeaAz\n%dialogflow.googleapis.com/Environment\x12Qprojects/{project}/locations/{location}/agents/{agent}/environments/{environment}"\x7f\n\x17ListEnvironmentsRequest\x12=\n\x06parent\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\x12%dialogflow.googleapis.com/Environment\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"u\n\x18ListEnvironmentsResponse\x12@\n\x0cenvironments\x18\x01 \x03(\x0b2*.google.cloud.dialogflow.cx.v3.Environment\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"T\n\x15GetEnvironmentRequest\x12;\n\x04name\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%dialogflow.googleapis.com/Environment"\x9f\x01\n\x18CreateEnvironmentRequest\x12=\n\x06parent\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\x12%dialogflow.googleapis.com/Environment\x12D\n\x0benvironment\x18\x02 \x01(\x0b2*.google.cloud.dialogflow.cx.v3.EnvironmentB\x03\xe0A\x02"\x96\x01\n\x18UpdateEnvironmentRequest\x12D\n\x0benvironment\x18\x01 \x01(\x0b2*.google.cloud.dialogflow.cx.v3.EnvironmentB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02"W\n\x18DeleteEnvironmentRequest\x12;\n\x04name\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%dialogflow.googleapis.com/Environment"\x85\x01\n\x1fLookupEnvironmentHistoryRequest\x12;\n\x04name\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%dialogflow.googleapis.com/Environment\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"}\n LookupEnvironmentHistoryResponse\x12@\n\x0cenvironments\x18\x01 \x03(\x0b2*.google.cloud.dialogflow.cx.v3.Environment\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\x88\x04\n\x14ContinuousTestResult\x12\x0c\n\x04name\x18\x01 \x01(\t\x12X\n\x06result\x18\x02 \x01(\x0e2H.google.cloud.dialogflow.cx.v3.ContinuousTestResult.AggregatedTestResult\x12H\n\x11test_case_results\x18\x03 \x03(\tB-\xfaA*\n(dialogflow.googleapis.com/TestCaseResult\x12,\n\x08run_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp"V\n\x14AggregatedTestResult\x12&\n"AGGREGATED_TEST_RESULT_UNSPECIFIED\x10\x00\x12\n\n\x06PASSED\x10\x01\x12\n\n\x06FAILED\x10\x02:\xb7\x01\xeaA\xb3\x01\n.dialogflow.googleapis.com/ContinuousTestResult\x12\x80\x01projects/{project}/locations/{location}/agents/{agent}/environments/{environment}/continuousTestResults/{continuous_test_result}"^\n\x18RunContinuousTestRequest\x12B\n\x0benvironment\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%dialogflow.googleapis.com/Environment"p\n\x19RunContinuousTestResponse\x12S\n\x16continuous_test_result\x18\x01 \x01(\x0b23.google.cloud.dialogflow.cx.v3.ContinuousTestResult"U\n\x19RunContinuousTestMetadata\x128\n\x06errors\x18\x01 \x03(\x0b2(.google.cloud.dialogflow.cx.v3.TestError"\x91\x01\n ListContinuousTestResultsRequest\x12F\n\x06parent\x18\x01 \x01(\tB6\xe0A\x02\xfaA0\x12.dialogflow.googleapis.com/ContinuousTestResult\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"\x92\x01\n!ListContinuousTestResultsResponse\x12T\n\x17continuous_test_results\x18\x01 \x03(\x0b23.google.cloud.dialogflow.cx.v3.ContinuousTestResult\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\x98\x01\n\x11DeployFlowRequest\x12B\n\x0benvironment\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%dialogflow.googleapis.com/Environment\x12?\n\x0cflow_version\x18\x02 \x01(\tB)\xe0A\x02\xfaA#\n!dialogflow.googleapis.com/Version"i\n\x12DeployFlowResponse\x12?\n\x0benvironment\x18\x01 \x01(\x0b2*.google.cloud.dialogflow.cx.v3.Environment\x12\x12\n\ndeployment\x18\x02 \x01(\t"S\n\x12DeployFlowMetadata\x12=\n\x0btest_errors\x18\x01 \x03(\x0b2(.google.cloud.dialogflow.cx.v3.TestError2\xc4\x11\n\x0cEnvironments\x12\xcf\x01\n\x10ListEnvironments\x126.google.cloud.dialogflow.cx.v3.ListEnvironmentsRequest\x1a7.google.cloud.dialogflow.cx.v3.ListEnvironmentsResponse"J\xdaA\x06parent\x82\xd3\xe4\x93\x02;\x129/v3/{parent=projects/*/locations/*/agents/*}/environments\x12\xbc\x01\n\x0eGetEnvironment\x124.google.cloud.dialogflow.cx.v3.GetEnvironmentRequest\x1a*.google.cloud.dialogflow.cx.v3.Environment"H\xdaA\x04name\x82\xd3\xe4\x93\x02;\x129/v3/{name=projects/*/locations/*/agents/*/environments/*}\x12\xf9\x01\n\x11CreateEnvironment\x127.google.cloud.dialogflow.cx.v3.CreateEnvironmentRequest\x1a\x1d.google.longrunning.Operation"\x8b\x01\xcaA%\n\x0bEnvironment\x12\x16google.protobuf.Struct\xdaA\x12parent,environment\x82\xd3\xe4\x93\x02H"9/v3/{parent=projects/*/locations/*/agents/*}/environments:\x0benvironment\x12\x8a\x02\n\x11UpdateEnvironment\x127.google.cloud.dialogflow.cx.v3.UpdateEnvironmentRequest\x1a\x1d.google.longrunning.Operation"\x9c\x01\xcaA%\n\x0bEnvironment\x12\x16google.protobuf.Struct\xdaA\x17environment,update_mask\x82\xd3\xe4\x93\x02T2E/v3/{environment.name=projects/*/locations/*/agents/*/environments/*}:\x0benvironment\x12\xae\x01\n\x11DeleteEnvironment\x127.google.cloud.dialogflow.cx.v3.DeleteEnvironmentRequest\x1a\x16.google.protobuf.Empty"H\xdaA\x04name\x82\xd3\xe4\x93\x02;*9/v3/{name=projects/*/locations/*/agents/*/environments/*}\x12\xfe\x01\n\x18LookupEnvironmentHistory\x12>.google.cloud.dialogflow.cx.v3.LookupEnvironmentHistoryRequest\x1a?.google.cloud.dialogflow.cx.v3.LookupEnvironmentHistoryResponse"a\xdaA\x04name\x82\xd3\xe4\x93\x02T\x12R/v3/{name=projects/*/locations/*/agents/*/environments/*}:lookupEnvironmentHistory\x12\x84\x02\n\x11RunContinuousTest\x127.google.cloud.dialogflow.cx.v3.RunContinuousTestRequest\x1a\x1d.google.longrunning.Operation"\x96\x01\xcaA6\n\x19RunContinuousTestResponse\x12\x19RunContinuousTestMetadata\x82\xd3\xe4\x93\x02W"R/v3/{environment=projects/*/locations/*/agents/*/environments/*}:runContinuousTest:\x01*\x12\x82\x02\n\x19ListContinuousTestResults\x12?.google.cloud.dialogflow.cx.v3.ListContinuousTestResultsRequest\x1a@.google.cloud.dialogflow.cx.v3.ListContinuousTestResultsResponse"b\xdaA\x06parent\x82\xd3\xe4\x93\x02S\x12Q/v3/{parent=projects/*/locations/*/agents/*/environments/*}/continuousTestResults\x12\xe1\x01\n\nDeployFlow\x120.google.cloud.dialogflow.cx.v3.DeployFlowRequest\x1a\x1d.google.longrunning.Operation"\x81\x01\xcaA(\n\x12DeployFlowResponse\x12\x12DeployFlowMetadata\x82\xd3\xe4\x93\x02P"K/v3/{environment=projects/*/locations/*/agents/*/environments/*}:deployFlow:\x01*\x1ax\xcaA\x19dialogflow.googleapis.com\xd2AYhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflowB\xb3\x01\n!com.google.cloud.dialogflow.cx.v3B\x10EnvironmentProtoP\x01Z1cloud.google.com/go/dialogflow/cx/apiv3/cxpb;cxpb\xa2\x02\x02DF\xaa\x02\x1dGoogle.Cloud.Dialogflow.Cx.V3\xea\x02!Google::Cloud::Dialogflow::CX::V3b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.dialogflow.cx.v3.environment_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n!com.google.cloud.dialogflow.cx.v3B\x10EnvironmentProtoP\x01Z1cloud.google.com/go/dialogflow/cx/apiv3/cxpb;cxpb\xa2\x02\x02DF\xaa\x02\x1dGoogle.Cloud.Dialogflow.Cx.V3\xea\x02!Google::Cloud::Dialogflow::CX::V3'
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
    _globals['_ENVIRONMENTS'].methods_by_name['ListEnvironments']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02;\x129/v3/{parent=projects/*/locations/*/agents/*}/environments'
    _globals['_ENVIRONMENTS'].methods_by_name['GetEnvironment']._loaded_options = None
    _globals['_ENVIRONMENTS'].methods_by_name['GetEnvironment']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02;\x129/v3/{name=projects/*/locations/*/agents/*/environments/*}'
    _globals['_ENVIRONMENTS'].methods_by_name['CreateEnvironment']._loaded_options = None
    _globals['_ENVIRONMENTS'].methods_by_name['CreateEnvironment']._serialized_options = b'\xcaA%\n\x0bEnvironment\x12\x16google.protobuf.Struct\xdaA\x12parent,environment\x82\xd3\xe4\x93\x02H"9/v3/{parent=projects/*/locations/*/agents/*}/environments:\x0benvironment'
    _globals['_ENVIRONMENTS'].methods_by_name['UpdateEnvironment']._loaded_options = None
    _globals['_ENVIRONMENTS'].methods_by_name['UpdateEnvironment']._serialized_options = b'\xcaA%\n\x0bEnvironment\x12\x16google.protobuf.Struct\xdaA\x17environment,update_mask\x82\xd3\xe4\x93\x02T2E/v3/{environment.name=projects/*/locations/*/agents/*/environments/*}:\x0benvironment'
    _globals['_ENVIRONMENTS'].methods_by_name['DeleteEnvironment']._loaded_options = None
    _globals['_ENVIRONMENTS'].methods_by_name['DeleteEnvironment']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02;*9/v3/{name=projects/*/locations/*/agents/*/environments/*}'
    _globals['_ENVIRONMENTS'].methods_by_name['LookupEnvironmentHistory']._loaded_options = None
    _globals['_ENVIRONMENTS'].methods_by_name['LookupEnvironmentHistory']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02T\x12R/v3/{name=projects/*/locations/*/agents/*/environments/*}:lookupEnvironmentHistory'
    _globals['_ENVIRONMENTS'].methods_by_name['RunContinuousTest']._loaded_options = None
    _globals['_ENVIRONMENTS'].methods_by_name['RunContinuousTest']._serialized_options = b'\xcaA6\n\x19RunContinuousTestResponse\x12\x19RunContinuousTestMetadata\x82\xd3\xe4\x93\x02W"R/v3/{environment=projects/*/locations/*/agents/*/environments/*}:runContinuousTest:\x01*'
    _globals['_ENVIRONMENTS'].methods_by_name['ListContinuousTestResults']._loaded_options = None
    _globals['_ENVIRONMENTS'].methods_by_name['ListContinuousTestResults']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02S\x12Q/v3/{parent=projects/*/locations/*/agents/*/environments/*}/continuousTestResults'
    _globals['_ENVIRONMENTS'].methods_by_name['DeployFlow']._loaded_options = None
    _globals['_ENVIRONMENTS'].methods_by_name['DeployFlow']._serialized_options = b'\xcaA(\n\x12DeployFlowResponse\x12\x12DeployFlowMetadata\x82\xd3\xe4\x93\x02P"K/v3/{environment=projects/*/locations/*/agents/*/environments/*}:deployFlow:\x01*'
    _globals['_ENVIRONMENT']._serialized_start = 453
    _globals['_ENVIRONMENT']._serialized_end = 1268
    _globals['_ENVIRONMENT_VERSIONCONFIG']._serialized_start = 836
    _globals['_ENVIRONMENT_VERSIONCONFIG']._serialized_end = 911
    _globals['_ENVIRONMENT_TESTCASESCONFIG']._serialized_start = 914
    _globals['_ENVIRONMENT_TESTCASESCONFIG']._serialized_end = 1057
    _globals['_ENVIRONMENT_WEBHOOKCONFIG']._serialized_start = 1059
    _globals['_ENVIRONMENT_WEBHOOKCONFIG']._serialized_end = 1141
    _globals['_LISTENVIRONMENTSREQUEST']._serialized_start = 1270
    _globals['_LISTENVIRONMENTSREQUEST']._serialized_end = 1397
    _globals['_LISTENVIRONMENTSRESPONSE']._serialized_start = 1399
    _globals['_LISTENVIRONMENTSRESPONSE']._serialized_end = 1516
    _globals['_GETENVIRONMENTREQUEST']._serialized_start = 1518
    _globals['_GETENVIRONMENTREQUEST']._serialized_end = 1602
    _globals['_CREATEENVIRONMENTREQUEST']._serialized_start = 1605
    _globals['_CREATEENVIRONMENTREQUEST']._serialized_end = 1764
    _globals['_UPDATEENVIRONMENTREQUEST']._serialized_start = 1767
    _globals['_UPDATEENVIRONMENTREQUEST']._serialized_end = 1917
    _globals['_DELETEENVIRONMENTREQUEST']._serialized_start = 1919
    _globals['_DELETEENVIRONMENTREQUEST']._serialized_end = 2006
    _globals['_LOOKUPENVIRONMENTHISTORYREQUEST']._serialized_start = 2009
    _globals['_LOOKUPENVIRONMENTHISTORYREQUEST']._serialized_end = 2142
    _globals['_LOOKUPENVIRONMENTHISTORYRESPONSE']._serialized_start = 2144
    _globals['_LOOKUPENVIRONMENTHISTORYRESPONSE']._serialized_end = 2269
    _globals['_CONTINUOUSTESTRESULT']._serialized_start = 2272
    _globals['_CONTINUOUSTESTRESULT']._serialized_end = 2792
    _globals['_CONTINUOUSTESTRESULT_AGGREGATEDTESTRESULT']._serialized_start = 2520
    _globals['_CONTINUOUSTESTRESULT_AGGREGATEDTESTRESULT']._serialized_end = 2606
    _globals['_RUNCONTINUOUSTESTREQUEST']._serialized_start = 2794
    _globals['_RUNCONTINUOUSTESTREQUEST']._serialized_end = 2888
    _globals['_RUNCONTINUOUSTESTRESPONSE']._serialized_start = 2890
    _globals['_RUNCONTINUOUSTESTRESPONSE']._serialized_end = 3002
    _globals['_RUNCONTINUOUSTESTMETADATA']._serialized_start = 3004
    _globals['_RUNCONTINUOUSTESTMETADATA']._serialized_end = 3089
    _globals['_LISTCONTINUOUSTESTRESULTSREQUEST']._serialized_start = 3092
    _globals['_LISTCONTINUOUSTESTRESULTSREQUEST']._serialized_end = 3237
    _globals['_LISTCONTINUOUSTESTRESULTSRESPONSE']._serialized_start = 3240
    _globals['_LISTCONTINUOUSTESTRESULTSRESPONSE']._serialized_end = 3386
    _globals['_DEPLOYFLOWREQUEST']._serialized_start = 3389
    _globals['_DEPLOYFLOWREQUEST']._serialized_end = 3541
    _globals['_DEPLOYFLOWRESPONSE']._serialized_start = 3543
    _globals['_DEPLOYFLOWRESPONSE']._serialized_end = 3648
    _globals['_DEPLOYFLOWMETADATA']._serialized_start = 3650
    _globals['_DEPLOYFLOWMETADATA']._serialized_end = 3733
    _globals['_ENVIRONMENTS']._serialized_start = 3736
    _globals['_ENVIRONMENTS']._serialized_end = 5980