"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/apigeeconnect/v1/connection.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.google/cloud/apigeeconnect/v1/connection.proto\x12\x1dgoogle.cloud.apigeeconnect.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"~\n\x16ListConnectionsRequest\x12=\n\x06parent\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%apigeeconnect.googleapis.com/Endpoint\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"r\n\x17ListConnectionsResponse\x12>\n\x0bconnections\x18\x01 \x03(\x0b2).google.cloud.apigeeconnect.v1.Connection\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"m\n\nConnection\x12\x10\n\x08endpoint\x18\x01 \x01(\t\x127\n\x07cluster\x18\x02 \x01(\x0b2&.google.cloud.apigeeconnect.v1.Cluster\x12\x14\n\x0cstream_count\x18\x03 \x01(\x05"\'\n\x07Cluster\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06region\x18\x02 \x01(\t2\xaa\x02\n\x11ConnectionService\x12\xc2\x01\n\x0fListConnections\x125.google.cloud.apigeeconnect.v1.ListConnectionsRequest\x1a6.google.cloud.apigeeconnect.v1.ListConnectionsResponse"@\xdaA\x06parent\x82\xd3\xe4\x93\x021\x12//v1/{parent=projects/*/endpoints/*}/connections\x1aP\xcaA\x1capigeeconnect.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xb5\x02\n!com.google.cloud.apigeeconnect.v1B\x0fConnectionProtoP\x01ZGcloud.google.com/go/apigeeconnect/apiv1/apigeeconnectpb;apigeeconnectpb\xaa\x02\x1dGoogle.Cloud.ApigeeConnect.V1\xca\x02\x1dGoogle\\Cloud\\ApigeeConnect\\V1\xea\x02 Google::Cloud::ApigeeConnect::V1\xeaAP\n%apigeeconnect.googleapis.com/Endpoint\x12\'projects/{project}/endpoints/{endpoint}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.apigeeconnect.v1.connection_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n!com.google.cloud.apigeeconnect.v1B\x0fConnectionProtoP\x01ZGcloud.google.com/go/apigeeconnect/apiv1/apigeeconnectpb;apigeeconnectpb\xaa\x02\x1dGoogle.Cloud.ApigeeConnect.V1\xca\x02\x1dGoogle\\Cloud\\ApigeeConnect\\V1\xea\x02 Google::Cloud::ApigeeConnect::V1\xeaAP\n%apigeeconnect.googleapis.com/Endpoint\x12'projects/{project}/endpoints/{endpoint}"
    _globals['_LISTCONNECTIONSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTCONNECTIONSREQUEST'].fields_by_name['parent']._serialized_options = b"\xe0A\x02\xfaA'\n%apigeeconnect.googleapis.com/Endpoint"
    _globals['_CONNECTIONSERVICE']._loaded_options = None
    _globals['_CONNECTIONSERVICE']._serialized_options = b'\xcaA\x1capigeeconnect.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_CONNECTIONSERVICE'].methods_by_name['ListConnections']._loaded_options = None
    _globals['_CONNECTIONSERVICE'].methods_by_name['ListConnections']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x021\x12//v1/{parent=projects/*/endpoints/*}/connections'
    _globals['_LISTCONNECTIONSREQUEST']._serialized_start = 196
    _globals['_LISTCONNECTIONSREQUEST']._serialized_end = 322
    _globals['_LISTCONNECTIONSRESPONSE']._serialized_start = 324
    _globals['_LISTCONNECTIONSRESPONSE']._serialized_end = 438
    _globals['_CONNECTION']._serialized_start = 440
    _globals['_CONNECTION']._serialized_end = 549
    _globals['_CLUSTER']._serialized_start = 551
    _globals['_CLUSTER']._serialized_end = 590
    _globals['_CONNECTIONSERVICE']._serialized_start = 593
    _globals['_CONNECTIONSERVICE']._serialized_end = 891