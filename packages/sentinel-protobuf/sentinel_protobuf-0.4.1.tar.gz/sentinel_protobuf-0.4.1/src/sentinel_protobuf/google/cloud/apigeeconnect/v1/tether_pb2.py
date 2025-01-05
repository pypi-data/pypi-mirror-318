"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/apigeeconnect/v1/tether.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from .....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*google/cloud/apigeeconnect/v1/tether.proto\x12\x1dgoogle.cloud.apigeeconnect.v1\x1a\x1egoogle/protobuf/duration.proto\x1a\x17google/rpc/status.proto\x1a\x17google/api/client.proto"\xe4\x01\n\rEgressRequest\x12\n\n\x02id\x18\x01 \x01(\t\x127\n\x07payload\x18\x02 \x01(\x0b2&.google.cloud.apigeeconnect.v1.Payload\x12?\n\x08endpoint\x18\x03 \x01(\x0e2-.google.cloud.apigeeconnect.v1.TetherEndpoint\x12\x0f\n\x07project\x18\x04 \x01(\t\x12\x10\n\x08trace_id\x18\x05 \x01(\t\x12*\n\x07timeout\x18\x06 \x01(\x0b2\x19.google.protobuf.Duration"\xd0\x01\n\x07Payload\x12B\n\x0chttp_request\x18\x01 \x01(\x0b2*.google.cloud.apigeeconnect.v1.HttpRequestH\x00\x12@\n\x0bstream_info\x18\x02 \x01(\x0b2).google.cloud.apigeeconnect.v1.StreamInfoH\x00\x127\n\x06action\x18\x03 \x01(\x0e2%.google.cloud.apigeeconnect.v1.ActionH\x00B\x06\n\x04kind"\x18\n\nStreamInfo\x12\n\n\x02id\x18\x01 \x01(\t"\xf6\x01\n\x0eEgressResponse\x12\n\n\x02id\x18\x01 \x01(\t\x12B\n\rhttp_response\x18\x02 \x01(\x0b2+.google.cloud.apigeeconnect.v1.HttpResponse\x12"\n\x06status\x18\x03 \x01(\x0b2\x12.google.rpc.Status\x12\x0f\n\x07project\x18\x04 \x01(\t\x12\x10\n\x08trace_id\x18\x05 \x01(\t\x12?\n\x08endpoint\x18\x06 \x01(\x0e2-.google.cloud.apigeeconnect.v1.TetherEndpoint\x12\x0c\n\x04name\x18\x07 \x01(\t"\xa0\x01\n\x0bHttpRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06method\x18\x02 \x01(\t\x12/\n\x03url\x18\x03 \x01(\x0b2".google.cloud.apigeeconnect.v1.Url\x126\n\x07headers\x18\x04 \x03(\x0b2%.google.cloud.apigeeconnect.v1.Header\x12\x0c\n\x04body\x18\x05 \x01(\x0c"X\n\x03Url\x125\n\x06scheme\x18\x01 \x01(\x0e2%.google.cloud.apigeeconnect.v1.Scheme\x12\x0c\n\x04host\x18\x02 \x01(\t\x12\x0c\n\x04path\x18\x03 \x01(\t"%\n\x06Header\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x0e\n\x06values\x18\x02 \x03(\t"\x9d\x01\n\x0cHttpResponse\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06status\x18\x02 \x01(\t\x12\x13\n\x0bstatus_code\x18\x03 \x01(\x05\x12\x0c\n\x04body\x18\x04 \x01(\x0c\x126\n\x07headers\x18\x05 \x03(\x0b2%.google.cloud.apigeeconnect.v1.Header\x12\x16\n\x0econtent_length\x18\x06 \x01(\x03*5\n\x06Action\x12\x16\n\x12ACTION_UNSPECIFIED\x10\x00\x12\x13\n\x0fOPEN_NEW_STREAM\x10\x01*n\n\x0eTetherEndpoint\x12\x1f\n\x1bTETHER_ENDPOINT_UNSPECIFIED\x10\x00\x12\x0f\n\x0bAPIGEE_MART\x10\x01\x12\x12\n\x0eAPIGEE_RUNTIME\x10\x02\x12\x16\n\x12APIGEE_MINT_RATING\x10\x03*+\n\x06Scheme\x12\x16\n\x12SCHEME_UNSPECIFIED\x10\x00\x12\t\n\x05HTTPS\x10\x012\xc7\x01\n\x06Tether\x12k\n\x06Egress\x12-.google.cloud.apigeeconnect.v1.EgressResponse\x1a,.google.cloud.apigeeconnect.v1.EgressRequest"\x00(\x010\x01\x1aP\xcaA\x1capigeeconnect.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xde\x01\n!com.google.cloud.apigeeconnect.v1B\x0bTetherProtoP\x01ZGcloud.google.com/go/apigeeconnect/apiv1/apigeeconnectpb;apigeeconnectpb\xaa\x02\x1dGoogle.Cloud.ApigeeConnect.V1\xca\x02\x1dGoogle\\Cloud\\ApigeeConnect\\V1\xea\x02 Google::Cloud::ApigeeConnect::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.apigeeconnect.v1.tether_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n!com.google.cloud.apigeeconnect.v1B\x0bTetherProtoP\x01ZGcloud.google.com/go/apigeeconnect/apiv1/apigeeconnectpb;apigeeconnectpb\xaa\x02\x1dGoogle.Cloud.ApigeeConnect.V1\xca\x02\x1dGoogle\\Cloud\\ApigeeConnect\\V1\xea\x02 Google::Cloud::ApigeeConnect::V1'
    _globals['_TETHER']._loaded_options = None
    _globals['_TETHER']._serialized_options = b'\xcaA\x1capigeeconnect.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_ACTION']._serialized_start = 1328
    _globals['_ACTION']._serialized_end = 1381
    _globals['_TETHERENDPOINT']._serialized_start = 1383
    _globals['_TETHERENDPOINT']._serialized_end = 1493
    _globals['_SCHEME']._serialized_start = 1495
    _globals['_SCHEME']._serialized_end = 1538
    _globals['_EGRESSREQUEST']._serialized_start = 160
    _globals['_EGRESSREQUEST']._serialized_end = 388
    _globals['_PAYLOAD']._serialized_start = 391
    _globals['_PAYLOAD']._serialized_end = 599
    _globals['_STREAMINFO']._serialized_start = 601
    _globals['_STREAMINFO']._serialized_end = 625
    _globals['_EGRESSRESPONSE']._serialized_start = 628
    _globals['_EGRESSRESPONSE']._serialized_end = 874
    _globals['_HTTPREQUEST']._serialized_start = 877
    _globals['_HTTPREQUEST']._serialized_end = 1037
    _globals['_URL']._serialized_start = 1039
    _globals['_URL']._serialized_end = 1127
    _globals['_HEADER']._serialized_start = 1129
    _globals['_HEADER']._serialized_end = 1166
    _globals['_HTTPRESPONSE']._serialized_start = 1169
    _globals['_HTTPRESPONSE']._serialized_end = 1326
    _globals['_TETHER']._serialized_start = 1541
    _globals['_TETHER']._serialized_end = 1740