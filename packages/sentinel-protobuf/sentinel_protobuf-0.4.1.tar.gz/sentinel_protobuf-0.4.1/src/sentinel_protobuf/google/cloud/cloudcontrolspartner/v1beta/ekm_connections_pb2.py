"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/cloudcontrolspartner/v1beta/ekm_connections.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n>google/cloud/cloudcontrolspartner/v1beta/ekm_connections.proto\x12(google.cloud.cloudcontrolspartner.v1beta\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\x9c\x02\n\x0eEkmConnections\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12P\n\x0fekm_connections\x18\x02 \x03(\x0b27.google.cloud.cloudcontrolspartner.v1beta.EkmConnection:\xa4\x01\xeaA\xa0\x01\n2cloudcontrolspartner.googleapis.com/EkmConnections\x12jorganizations/{organization}/locations/{location}/customers/{customer}/workloads/{workload}/ekmConnections"d\n\x18GetEkmConnectionsRequest\x12H\n\x04name\x18\x01 \x01(\tB:\xe0A\x02\xfaA4\n2cloudcontrolspartner.googleapis.com/EkmConnections"\xac\x03\n\rEkmConnection\x12\x17\n\x0fconnection_name\x18\x01 \x01(\t\x12f\n\x10connection_state\x18\x02 \x01(\x0e2G.google.cloud.cloudcontrolspartner.v1beta.EkmConnection.ConnectionStateB\x03\xe0A\x03\x12a\n\x10connection_error\x18\x03 \x01(\x0b2G.google.cloud.cloudcontrolspartner.v1beta.EkmConnection.ConnectionError\x1a>\n\x0fConnectionError\x12\x14\n\x0cerror_domain\x18\x01 \x01(\t\x12\x15\n\rerror_message\x18\x02 \x01(\t"w\n\x0fConnectionState\x12 \n\x1cCONNECTION_STATE_UNSPECIFIED\x10\x00\x12\r\n\tAVAILABLE\x10\x01\x12\x11\n\rNOT_AVAILABLE\x10\x02\x12\t\n\x05ERROR\x10\x03\x12\x15\n\x11PERMISSION_DENIED\x10\x04B\xab\x02\n,com.google.cloud.cloudcontrolspartner.v1betaB\x13EkmConnectionsProtoP\x01Z`cloud.google.com/go/cloudcontrolspartner/apiv1beta/cloudcontrolspartnerpb;cloudcontrolspartnerpb\xaa\x02(Google.Cloud.CloudControlsPartner.V1Beta\xca\x02(Google\\Cloud\\CloudControlsPartner\\V1beta\xea\x02+Google::Cloud::CloudControlsPartner::V1betab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.cloudcontrolspartner.v1beta.ekm_connections_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n,com.google.cloud.cloudcontrolspartner.v1betaB\x13EkmConnectionsProtoP\x01Z`cloud.google.com/go/cloudcontrolspartner/apiv1beta/cloudcontrolspartnerpb;cloudcontrolspartnerpb\xaa\x02(Google.Cloud.CloudControlsPartner.V1Beta\xca\x02(Google\\Cloud\\CloudControlsPartner\\V1beta\xea\x02+Google::Cloud::CloudControlsPartner::V1beta'
    _globals['_EKMCONNECTIONS'].fields_by_name['name']._loaded_options = None
    _globals['_EKMCONNECTIONS'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_EKMCONNECTIONS']._loaded_options = None
    _globals['_EKMCONNECTIONS']._serialized_options = b'\xeaA\xa0\x01\n2cloudcontrolspartner.googleapis.com/EkmConnections\x12jorganizations/{organization}/locations/{location}/customers/{customer}/workloads/{workload}/ekmConnections'
    _globals['_GETEKMCONNECTIONSREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETEKMCONNECTIONSREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA4\n2cloudcontrolspartner.googleapis.com/EkmConnections'
    _globals['_EKMCONNECTION'].fields_by_name['connection_state']._loaded_options = None
    _globals['_EKMCONNECTION'].fields_by_name['connection_state']._serialized_options = b'\xe0A\x03'
    _globals['_EKMCONNECTIONS']._serialized_start = 169
    _globals['_EKMCONNECTIONS']._serialized_end = 453
    _globals['_GETEKMCONNECTIONSREQUEST']._serialized_start = 455
    _globals['_GETEKMCONNECTIONSREQUEST']._serialized_end = 555
    _globals['_EKMCONNECTION']._serialized_start = 558
    _globals['_EKMCONNECTION']._serialized_end = 986
    _globals['_EKMCONNECTION_CONNECTIONERROR']._serialized_start = 803
    _globals['_EKMCONNECTION_CONNECTIONERROR']._serialized_end = 865
    _globals['_EKMCONNECTION_CONNECTIONSTATE']._serialized_start = 867
    _globals['_EKMCONNECTION_CONNECTIONSTATE']._serialized_end = 986