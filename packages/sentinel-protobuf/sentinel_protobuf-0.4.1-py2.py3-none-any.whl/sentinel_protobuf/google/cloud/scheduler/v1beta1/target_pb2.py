"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/scheduler/v1beta1/target.proto')
_sym_db = _symbol_database.Default()
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+google/cloud/scheduler/v1beta1/target.proto\x12\x1egoogle.cloud.scheduler.v1beta1\x1a\x19google/api/resource.proto"\xfe\x02\n\nHttpTarget\x12\x0b\n\x03uri\x18\x01 \x01(\t\x12?\n\x0bhttp_method\x18\x02 \x01(\x0e2*.google.cloud.scheduler.v1beta1.HttpMethod\x12H\n\x07headers\x18\x03 \x03(\x0b27.google.cloud.scheduler.v1beta1.HttpTarget.HeadersEntry\x12\x0c\n\x04body\x18\x04 \x01(\x0c\x12A\n\x0boauth_token\x18\x05 \x01(\x0b2*.google.cloud.scheduler.v1beta1.OAuthTokenH\x00\x12?\n\noidc_token\x18\x06 \x01(\x0b2).google.cloud.scheduler.v1beta1.OidcTokenH\x00\x1a.\n\x0cHeadersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01B\x16\n\x14authorization_header"\xcb\x02\n\x13AppEngineHttpTarget\x12?\n\x0bhttp_method\x18\x01 \x01(\x0e2*.google.cloud.scheduler.v1beta1.HttpMethod\x12L\n\x12app_engine_routing\x18\x02 \x01(\x0b20.google.cloud.scheduler.v1beta1.AppEngineRouting\x12\x14\n\x0crelative_uri\x18\x03 \x01(\t\x12Q\n\x07headers\x18\x04 \x03(\x0b2@.google.cloud.scheduler.v1beta1.AppEngineHttpTarget.HeadersEntry\x12\x0c\n\x04body\x18\x05 \x01(\x0c\x1a.\n\x0cHeadersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"\xd7\x01\n\x0cPubsubTarget\x124\n\ntopic_name\x18\x01 \x01(\tB \xfaA\x1d\n\x1bpubsub.googleapis.com/Topic\x12\x0c\n\x04data\x18\x03 \x01(\x0c\x12P\n\nattributes\x18\x04 \x03(\x0b2<.google.cloud.scheduler.v1beta1.PubsubTarget.AttributesEntry\x1a1\n\x0fAttributesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"T\n\x10AppEngineRouting\x12\x0f\n\x07service\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\x12\x10\n\x08instance\x18\x03 \x01(\t\x12\x0c\n\x04host\x18\x04 \x01(\t":\n\nOAuthToken\x12\x1d\n\x15service_account_email\x18\x01 \x01(\t\x12\r\n\x05scope\x18\x02 \x01(\t"<\n\tOidcToken\x12\x1d\n\x15service_account_email\x18\x01 \x01(\t\x12\x10\n\x08audience\x18\x02 \x01(\t*s\n\nHttpMethod\x12\x1b\n\x17HTTP_METHOD_UNSPECIFIED\x10\x00\x12\x08\n\x04POST\x10\x01\x12\x07\n\x03GET\x10\x02\x12\x08\n\x04HEAD\x10\x03\x12\x07\n\x03PUT\x10\x04\x12\n\n\x06DELETE\x10\x05\x12\t\n\x05PATCH\x10\x06\x12\x0b\n\x07OPTIONS\x10\x07B\xb8\x01\n"com.google.cloud.scheduler.v1beta1B\x0bTargetProtoP\x01Z@cloud.google.com/go/scheduler/apiv1beta1/schedulerpb;schedulerpb\xeaA@\n\x1bpubsub.googleapis.com/Topic\x12!projects/{project}/topics/{topic}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.scheduler.v1beta1.target_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.cloud.scheduler.v1beta1B\x0bTargetProtoP\x01Z@cloud.google.com/go/scheduler/apiv1beta1/schedulerpb;schedulerpb\xeaA@\n\x1bpubsub.googleapis.com/Topic\x12!projects/{project}/topics/{topic}'
    _globals['_HTTPTARGET_HEADERSENTRY']._loaded_options = None
    _globals['_HTTPTARGET_HEADERSENTRY']._serialized_options = b'8\x01'
    _globals['_APPENGINEHTTPTARGET_HEADERSENTRY']._loaded_options = None
    _globals['_APPENGINEHTTPTARGET_HEADERSENTRY']._serialized_options = b'8\x01'
    _globals['_PUBSUBTARGET_ATTRIBUTESENTRY']._loaded_options = None
    _globals['_PUBSUBTARGET_ATTRIBUTESENTRY']._serialized_options = b'8\x01'
    _globals['_PUBSUBTARGET'].fields_by_name['topic_name']._loaded_options = None
    _globals['_PUBSUBTARGET'].fields_by_name['topic_name']._serialized_options = b'\xfaA\x1d\n\x1bpubsub.googleapis.com/Topic'
    _globals['_HTTPMETHOD']._serialized_start = 1251
    _globals['_HTTPMETHOD']._serialized_end = 1366
    _globals['_HTTPTARGET']._serialized_start = 107
    _globals['_HTTPTARGET']._serialized_end = 489
    _globals['_HTTPTARGET_HEADERSENTRY']._serialized_start = 419
    _globals['_HTTPTARGET_HEADERSENTRY']._serialized_end = 465
    _globals['_APPENGINEHTTPTARGET']._serialized_start = 492
    _globals['_APPENGINEHTTPTARGET']._serialized_end = 823
    _globals['_APPENGINEHTTPTARGET_HEADERSENTRY']._serialized_start = 419
    _globals['_APPENGINEHTTPTARGET_HEADERSENTRY']._serialized_end = 465
    _globals['_PUBSUBTARGET']._serialized_start = 826
    _globals['_PUBSUBTARGET']._serialized_end = 1041
    _globals['_PUBSUBTARGET_ATTRIBUTESENTRY']._serialized_start = 992
    _globals['_PUBSUBTARGET_ATTRIBUTESENTRY']._serialized_end = 1041
    _globals['_APPENGINEROUTING']._serialized_start = 1043
    _globals['_APPENGINEROUTING']._serialized_end = 1127
    _globals['_OAUTHTOKEN']._serialized_start = 1129
    _globals['_OAUTHTOKEN']._serialized_end = 1187
    _globals['_OIDCTOKEN']._serialized_start = 1189
    _globals['_OIDCTOKEN']._serialized_end = 1249