"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/dialogflow/cx/v3/deployment.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.google/cloud/dialogflow/cx/v3/deployment.proto\x12\x1dgoogle.cloud.dialogflow.cx.v3\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xb3\x05\n\nDeployment\x12\x0c\n\x04name\x18\x01 \x01(\t\x12<\n\x0cflow_version\x18\x02 \x01(\tB&\xfaA#\n!dialogflow.googleapis.com/Version\x12>\n\x05state\x18\x03 \x01(\x0e2/.google.cloud.dialogflow.cx.v3.Deployment.State\x12@\n\x06result\x18\x04 \x01(\x0b20.google.cloud.dialogflow.cx.v3.Deployment.Result\x12.\n\nstart_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12,\n\x08end_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.Timestamp\x1a\x97\x01\n\x06Result\x12N\n\x17deployment_test_results\x18\x01 \x03(\tB-\xfaA*\n(dialogflow.googleapis.com/TestCaseResult\x12=\n\nexperiment\x18\x02 \x01(\tB)\xfaA&\n$dialogflow.googleapis.com/Experiment"F\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0b\n\x07RUNNING\x10\x01\x12\r\n\tSUCCEEDED\x10\x02\x12\n\n\x06FAILED\x10\x03:\x96\x01\xeaA\x92\x01\n$dialogflow.googleapis.com/Deployment\x12jprojects/{project}/locations/{location}/agents/{agent}/environments/{environment}/deployments/{deployment}"}\n\x16ListDeploymentsRequest\x12<\n\x06parent\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\x12$dialogflow.googleapis.com/Deployment\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"r\n\x17ListDeploymentsResponse\x12>\n\x0bdeployments\x18\x01 \x03(\x0b2).google.cloud.dialogflow.cx.v3.Deployment\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"R\n\x14GetDeploymentRequest\x12:\n\x04name\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\n$dialogflow.googleapis.com/Deployment2\xae\x04\n\x0bDeployments\x12\xda\x01\n\x0fListDeployments\x125.google.cloud.dialogflow.cx.v3.ListDeploymentsRequest\x1a6.google.cloud.dialogflow.cx.v3.ListDeploymentsResponse"X\xdaA\x06parent\x82\xd3\xe4\x93\x02I\x12G/v3/{parent=projects/*/locations/*/agents/*/environments/*}/deployments\x12\xc7\x01\n\rGetDeployment\x123.google.cloud.dialogflow.cx.v3.GetDeploymentRequest\x1a).google.cloud.dialogflow.cx.v3.Deployment"V\xdaA\x04name\x82\xd3\xe4\x93\x02I\x12G/v3/{name=projects/*/locations/*/agents/*/environments/*/deployments/*}\x1ax\xcaA\x19dialogflow.googleapis.com\xd2AYhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflowB\xb5\x01\n!com.google.cloud.dialogflow.cx.v3B\x0fDeploymentProtoP\x01Z1cloud.google.com/go/dialogflow/cx/apiv3/cxpb;cxpb\xf8\x01\x01\xa2\x02\x02DF\xaa\x02\x1dGoogle.Cloud.Dialogflow.Cx.V3\xea\x02!Google::Cloud::Dialogflow::CX::V3b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.dialogflow.cx.v3.deployment_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n!com.google.cloud.dialogflow.cx.v3B\x0fDeploymentProtoP\x01Z1cloud.google.com/go/dialogflow/cx/apiv3/cxpb;cxpb\xf8\x01\x01\xa2\x02\x02DF\xaa\x02\x1dGoogle.Cloud.Dialogflow.Cx.V3\xea\x02!Google::Cloud::Dialogflow::CX::V3'
    _globals['_DEPLOYMENT_RESULT'].fields_by_name['deployment_test_results']._loaded_options = None
    _globals['_DEPLOYMENT_RESULT'].fields_by_name['deployment_test_results']._serialized_options = b'\xfaA*\n(dialogflow.googleapis.com/TestCaseResult'
    _globals['_DEPLOYMENT_RESULT'].fields_by_name['experiment']._loaded_options = None
    _globals['_DEPLOYMENT_RESULT'].fields_by_name['experiment']._serialized_options = b'\xfaA&\n$dialogflow.googleapis.com/Experiment'
    _globals['_DEPLOYMENT'].fields_by_name['flow_version']._loaded_options = None
    _globals['_DEPLOYMENT'].fields_by_name['flow_version']._serialized_options = b'\xfaA#\n!dialogflow.googleapis.com/Version'
    _globals['_DEPLOYMENT']._loaded_options = None
    _globals['_DEPLOYMENT']._serialized_options = b'\xeaA\x92\x01\n$dialogflow.googleapis.com/Deployment\x12jprojects/{project}/locations/{location}/agents/{agent}/environments/{environment}/deployments/{deployment}'
    _globals['_LISTDEPLOYMENTSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTDEPLOYMENTSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA&\x12$dialogflow.googleapis.com/Deployment'
    _globals['_GETDEPLOYMENTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETDEPLOYMENTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA&\n$dialogflow.googleapis.com/Deployment'
    _globals['_DEPLOYMENTS']._loaded_options = None
    _globals['_DEPLOYMENTS']._serialized_options = b'\xcaA\x19dialogflow.googleapis.com\xd2AYhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflow'
    _globals['_DEPLOYMENTS'].methods_by_name['ListDeployments']._loaded_options = None
    _globals['_DEPLOYMENTS'].methods_by_name['ListDeployments']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02I\x12G/v3/{parent=projects/*/locations/*/agents/*/environments/*}/deployments'
    _globals['_DEPLOYMENTS'].methods_by_name['GetDeployment']._loaded_options = None
    _globals['_DEPLOYMENTS'].methods_by_name['GetDeployment']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02I\x12G/v3/{name=projects/*/locations/*/agents/*/environments/*/deployments/*}'
    _globals['_DEPLOYMENT']._serialized_start = 230
    _globals['_DEPLOYMENT']._serialized_end = 921
    _globals['_DEPLOYMENT_RESULT']._serialized_start = 545
    _globals['_DEPLOYMENT_RESULT']._serialized_end = 696
    _globals['_DEPLOYMENT_STATE']._serialized_start = 698
    _globals['_DEPLOYMENT_STATE']._serialized_end = 768
    _globals['_LISTDEPLOYMENTSREQUEST']._serialized_start = 923
    _globals['_LISTDEPLOYMENTSREQUEST']._serialized_end = 1048
    _globals['_LISTDEPLOYMENTSRESPONSE']._serialized_start = 1050
    _globals['_LISTDEPLOYMENTSRESPONSE']._serialized_end = 1164
    _globals['_GETDEPLOYMENTREQUEST']._serialized_start = 1166
    _globals['_GETDEPLOYMENTREQUEST']._serialized_end = 1248
    _globals['_DEPLOYMENTS']._serialized_start = 1251
    _globals['_DEPLOYMENTS']._serialized_end = 1809