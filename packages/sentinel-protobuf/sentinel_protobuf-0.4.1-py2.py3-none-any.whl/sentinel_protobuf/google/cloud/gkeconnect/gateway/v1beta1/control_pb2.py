"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/gkeconnect/gateway/v1beta1/control.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5google/cloud/gkeconnect/gateway/v1beta1/control.proto\x12\'google.cloud.gkeconnect.gateway.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto"\xcd\x02\n\x1aGenerateCredentialsRequest\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x1c\n\x0fforce_use_agent\x18\x02 \x01(\x08B\x03\xe0A\x01\x12\x14\n\x07version\x18\x03 \x01(\tB\x03\xe0A\x01\x12!\n\x14kubernetes_namespace\x18\x04 \x01(\tB\x03\xe0A\x01\x12r\n\x10operating_system\x18\x05 \x01(\x0e2S.google.cloud.gkeconnect.gateway.v1beta1.GenerateCredentialsRequest.OperatingSystemB\x03\xe0A\x01"Q\n\x0fOperatingSystem\x12 \n\x1cOPERATING_SYSTEM_UNSPECIFIED\x10\x00\x12\x1c\n\x18OPERATING_SYSTEM_WINDOWS\x10\x01"C\n\x1bGenerateCredentialsResponse\x12\x12\n\nkubeconfig\x18\x01 \x01(\x0c\x12\x10\n\x08endpoint\x18\x02 \x01(\t2\xd8\x02\n\x0eGatewayControl\x12\xf2\x01\n\x13GenerateCredentials\x12C.google.cloud.gkeconnect.gateway.v1beta1.GenerateCredentialsRequest\x1aD.google.cloud.gkeconnect.gateway.v1beta1.GenerateCredentialsResponse"P\x82\xd3\xe4\x93\x02J\x12H/v1beta1/{name=projects/*/locations/*/memberships/*}:generateCredentials\x1aQ\xcaA\x1dconnectgateway.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\x86\x02\n+com.google.cloud.gkeconnect.gateway.v1beta1B\x0cControlProtoP\x01ZEcloud.google.com/go/gkeconnect/gateway/apiv1beta1/gatewaypb;gatewaypb\xaa\x02\'Google.Cloud.GkeConnect.Gateway.V1Beta1\xca\x02\'Google\\Cloud\\GkeConnect\\Gateway\\V1beta1\xea\x02+Google::Cloud::GkeConnect::Gateway::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.gkeconnect.gateway.v1beta1.control_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n+com.google.cloud.gkeconnect.gateway.v1beta1B\x0cControlProtoP\x01ZEcloud.google.com/go/gkeconnect/gateway/apiv1beta1/gatewaypb;gatewaypb\xaa\x02'Google.Cloud.GkeConnect.Gateway.V1Beta1\xca\x02'Google\\Cloud\\GkeConnect\\Gateway\\V1beta1\xea\x02+Google::Cloud::GkeConnect::Gateway::V1beta1"
    _globals['_GENERATECREDENTIALSREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GENERATECREDENTIALSREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_GENERATECREDENTIALSREQUEST'].fields_by_name['force_use_agent']._loaded_options = None
    _globals['_GENERATECREDENTIALSREQUEST'].fields_by_name['force_use_agent']._serialized_options = b'\xe0A\x01'
    _globals['_GENERATECREDENTIALSREQUEST'].fields_by_name['version']._loaded_options = None
    _globals['_GENERATECREDENTIALSREQUEST'].fields_by_name['version']._serialized_options = b'\xe0A\x01'
    _globals['_GENERATECREDENTIALSREQUEST'].fields_by_name['kubernetes_namespace']._loaded_options = None
    _globals['_GENERATECREDENTIALSREQUEST'].fields_by_name['kubernetes_namespace']._serialized_options = b'\xe0A\x01'
    _globals['_GENERATECREDENTIALSREQUEST'].fields_by_name['operating_system']._loaded_options = None
    _globals['_GENERATECREDENTIALSREQUEST'].fields_by_name['operating_system']._serialized_options = b'\xe0A\x01'
    _globals['_GATEWAYCONTROL']._loaded_options = None
    _globals['_GATEWAYCONTROL']._serialized_options = b'\xcaA\x1dconnectgateway.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_GATEWAYCONTROL'].methods_by_name['GenerateCredentials']._loaded_options = None
    _globals['_GATEWAYCONTROL'].methods_by_name['GenerateCredentials']._serialized_options = b'\x82\xd3\xe4\x93\x02J\x12H/v1beta1/{name=projects/*/locations/*/memberships/*}:generateCredentials'
    _globals['_GENERATECREDENTIALSREQUEST']._serialized_start = 187
    _globals['_GENERATECREDENTIALSREQUEST']._serialized_end = 520
    _globals['_GENERATECREDENTIALSREQUEST_OPERATINGSYSTEM']._serialized_start = 439
    _globals['_GENERATECREDENTIALSREQUEST_OPERATINGSYSTEM']._serialized_end = 520
    _globals['_GENERATECREDENTIALSRESPONSE']._serialized_start = 522
    _globals['_GENERATECREDENTIALSRESPONSE']._serialized_end = 589
    _globals['_GATEWAYCONTROL']._serialized_start = 592
    _globals['_GATEWAYCONTROL']._serialized_end = 936