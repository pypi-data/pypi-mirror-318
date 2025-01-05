"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/tasks/v2/target.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n"google/cloud/tasks/v2/target.proto\x12\x15google.cloud.tasks.v2\x1a\x1fgoogle/api/field_behavior.proto"\xe1\x02\n\x0bHttpRequest\x12\x10\n\x03url\x18\x01 \x01(\tB\x03\xe0A\x02\x126\n\x0bhttp_method\x18\x02 \x01(\x0e2!.google.cloud.tasks.v2.HttpMethod\x12@\n\x07headers\x18\x03 \x03(\x0b2/.google.cloud.tasks.v2.HttpRequest.HeadersEntry\x12\x0c\n\x04body\x18\x04 \x01(\x0c\x128\n\x0boauth_token\x18\x05 \x01(\x0b2!.google.cloud.tasks.v2.OAuthTokenH\x00\x126\n\noidc_token\x18\x06 \x01(\x0b2 .google.cloud.tasks.v2.OidcTokenH\x00\x1a.\n\x0cHeadersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01B\x16\n\x14authorization_header"\xb2\x02\n\x14AppEngineHttpRequest\x126\n\x0bhttp_method\x18\x01 \x01(\x0e2!.google.cloud.tasks.v2.HttpMethod\x12C\n\x12app_engine_routing\x18\x02 \x01(\x0b2\'.google.cloud.tasks.v2.AppEngineRouting\x12\x14\n\x0crelative_uri\x18\x03 \x01(\t\x12I\n\x07headers\x18\x04 \x03(\x0b28.google.cloud.tasks.v2.AppEngineHttpRequest.HeadersEntry\x12\x0c\n\x04body\x18\x05 \x01(\x0c\x1a.\n\x0cHeadersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"T\n\x10AppEngineRouting\x12\x0f\n\x07service\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\x12\x10\n\x08instance\x18\x03 \x01(\t\x12\x0c\n\x04host\x18\x04 \x01(\t":\n\nOAuthToken\x12\x1d\n\x15service_account_email\x18\x01 \x01(\t\x12\r\n\x05scope\x18\x02 \x01(\t"<\n\tOidcToken\x12\x1d\n\x15service_account_email\x18\x01 \x01(\t\x12\x10\n\x08audience\x18\x02 \x01(\t*s\n\nHttpMethod\x12\x1b\n\x17HTTP_METHOD_UNSPECIFIED\x10\x00\x12\x08\n\x04POST\x10\x01\x12\x07\n\x03GET\x10\x02\x12\x08\n\x04HEAD\x10\x03\x12\x07\n\x03PUT\x10\x04\x12\n\n\x06DELETE\x10\x05\x12\t\n\x05PATCH\x10\x06\x12\x0b\n\x07OPTIONS\x10\x07Bj\n\x19com.google.cloud.tasks.v2B\x0bTargetProtoP\x01Z>cloud.google.com/go/cloudtasks/apiv2/cloudtaskspb;cloudtaskspbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.tasks.v2.target_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x19com.google.cloud.tasks.v2B\x0bTargetProtoP\x01Z>cloud.google.com/go/cloudtasks/apiv2/cloudtaskspb;cloudtaskspb'
    _globals['_HTTPREQUEST_HEADERSENTRY']._loaded_options = None
    _globals['_HTTPREQUEST_HEADERSENTRY']._serialized_options = b'8\x01'
    _globals['_HTTPREQUEST'].fields_by_name['url']._loaded_options = None
    _globals['_HTTPREQUEST'].fields_by_name['url']._serialized_options = b'\xe0A\x02'
    _globals['_APPENGINEHTTPREQUEST_HEADERSENTRY']._loaded_options = None
    _globals['_APPENGINEHTTPREQUEST_HEADERSENTRY']._serialized_options = b'8\x01'
    _globals['_HTTPMETHOD']._serialized_start = 967
    _globals['_HTTPMETHOD']._serialized_end = 1082
    _globals['_HTTPREQUEST']._serialized_start = 95
    _globals['_HTTPREQUEST']._serialized_end = 448
    _globals['_HTTPREQUEST_HEADERSENTRY']._serialized_start = 378
    _globals['_HTTPREQUEST_HEADERSENTRY']._serialized_end = 424
    _globals['_APPENGINEHTTPREQUEST']._serialized_start = 451
    _globals['_APPENGINEHTTPREQUEST']._serialized_end = 757
    _globals['_APPENGINEHTTPREQUEST_HEADERSENTRY']._serialized_start = 378
    _globals['_APPENGINEHTTPREQUEST_HEADERSENTRY']._serialized_end = 424
    _globals['_APPENGINEROUTING']._serialized_start = 759
    _globals['_APPENGINEROUTING']._serialized_end = 843
    _globals['_OAUTHTOKEN']._serialized_start = 845
    _globals['_OAUTHTOKEN']._serialized_end = 903
    _globals['_OIDCTOKEN']._serialized_start = 905
    _globals['_OIDCTOKEN']._serialized_end = 965