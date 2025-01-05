"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/scheduler/v1/target.proto')
_sym_db = _symbol_database.Default()
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&google/cloud/scheduler/v1/target.proto\x12\x19google.cloud.scheduler.v1\x1a\x19google/api/resource.proto"\xea\x02\n\nHttpTarget\x12\x0b\n\x03uri\x18\x01 \x01(\t\x12:\n\x0bhttp_method\x18\x02 \x01(\x0e2%.google.cloud.scheduler.v1.HttpMethod\x12C\n\x07headers\x18\x03 \x03(\x0b22.google.cloud.scheduler.v1.HttpTarget.HeadersEntry\x12\x0c\n\x04body\x18\x04 \x01(\x0c\x12<\n\x0boauth_token\x18\x05 \x01(\x0b2%.google.cloud.scheduler.v1.OAuthTokenH\x00\x12:\n\noidc_token\x18\x06 \x01(\x0b2$.google.cloud.scheduler.v1.OidcTokenH\x00\x1a.\n\x0cHeadersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01B\x16\n\x14authorization_header"\xbc\x02\n\x13AppEngineHttpTarget\x12:\n\x0bhttp_method\x18\x01 \x01(\x0e2%.google.cloud.scheduler.v1.HttpMethod\x12G\n\x12app_engine_routing\x18\x02 \x01(\x0b2+.google.cloud.scheduler.v1.AppEngineRouting\x12\x14\n\x0crelative_uri\x18\x03 \x01(\t\x12L\n\x07headers\x18\x04 \x03(\x0b2;.google.cloud.scheduler.v1.AppEngineHttpTarget.HeadersEntry\x12\x0c\n\x04body\x18\x05 \x01(\x0c\x1a.\n\x0cHeadersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"\xd2\x01\n\x0cPubsubTarget\x124\n\ntopic_name\x18\x01 \x01(\tB \xfaA\x1d\n\x1bpubsub.googleapis.com/Topic\x12\x0c\n\x04data\x18\x03 \x01(\x0c\x12K\n\nattributes\x18\x04 \x03(\x0b27.google.cloud.scheduler.v1.PubsubTarget.AttributesEntry\x1a1\n\x0fAttributesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"T\n\x10AppEngineRouting\x12\x0f\n\x07service\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\x12\x10\n\x08instance\x18\x03 \x01(\t\x12\x0c\n\x04host\x18\x04 \x01(\t":\n\nOAuthToken\x12\x1d\n\x15service_account_email\x18\x01 \x01(\t\x12\r\n\x05scope\x18\x02 \x01(\t"<\n\tOidcToken\x12\x1d\n\x15service_account_email\x18\x01 \x01(\t\x12\x10\n\x08audience\x18\x02 \x01(\t*s\n\nHttpMethod\x12\x1b\n\x17HTTP_METHOD_UNSPECIFIED\x10\x00\x12\x08\n\x04POST\x10\x01\x12\x07\n\x03GET\x10\x02\x12\x08\n\x04HEAD\x10\x03\x12\x07\n\x03PUT\x10\x04\x12\n\n\x06DELETE\x10\x05\x12\t\n\x05PATCH\x10\x06\x12\x0b\n\x07OPTIONS\x10\x07B\xae\x01\n\x1dcom.google.cloud.scheduler.v1B\x0bTargetProtoP\x01Z;cloud.google.com/go/scheduler/apiv1/schedulerpb;schedulerpb\xeaA@\n\x1bpubsub.googleapis.com/Topic\x12!projects/{project}/topics/{topic}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.scheduler.v1.target_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1dcom.google.cloud.scheduler.v1B\x0bTargetProtoP\x01Z;cloud.google.com/go/scheduler/apiv1/schedulerpb;schedulerpb\xeaA@\n\x1bpubsub.googleapis.com/Topic\x12!projects/{project}/topics/{topic}'
    _globals['_HTTPTARGET_HEADERSENTRY']._loaded_options = None
    _globals['_HTTPTARGET_HEADERSENTRY']._serialized_options = b'8\x01'
    _globals['_APPENGINEHTTPTARGET_HEADERSENTRY']._loaded_options = None
    _globals['_APPENGINEHTTPTARGET_HEADERSENTRY']._serialized_options = b'8\x01'
    _globals['_PUBSUBTARGET_ATTRIBUTESENTRY']._loaded_options = None
    _globals['_PUBSUBTARGET_ATTRIBUTESENTRY']._serialized_options = b'8\x01'
    _globals['_PUBSUBTARGET'].fields_by_name['topic_name']._loaded_options = None
    _globals['_PUBSUBTARGET'].fields_by_name['topic_name']._serialized_options = b'\xfaA\x1d\n\x1bpubsub.googleapis.com/Topic'
    _globals['_HTTPMETHOD']._serialized_start = 1201
    _globals['_HTTPMETHOD']._serialized_end = 1316
    _globals['_HTTPTARGET']._serialized_start = 97
    _globals['_HTTPTARGET']._serialized_end = 459
    _globals['_HTTPTARGET_HEADERSENTRY']._serialized_start = 389
    _globals['_HTTPTARGET_HEADERSENTRY']._serialized_end = 435
    _globals['_APPENGINEHTTPTARGET']._serialized_start = 462
    _globals['_APPENGINEHTTPTARGET']._serialized_end = 778
    _globals['_APPENGINEHTTPTARGET_HEADERSENTRY']._serialized_start = 389
    _globals['_APPENGINEHTTPTARGET_HEADERSENTRY']._serialized_end = 435
    _globals['_PUBSUBTARGET']._serialized_start = 781
    _globals['_PUBSUBTARGET']._serialized_end = 991
    _globals['_PUBSUBTARGET_ATTRIBUTESENTRY']._serialized_start = 942
    _globals['_PUBSUBTARGET_ATTRIBUTESENTRY']._serialized_end = 991
    _globals['_APPENGINEROUTING']._serialized_start = 993
    _globals['_APPENGINEROUTING']._serialized_end = 1077
    _globals['_OAUTHTOKEN']._serialized_start = 1079
    _globals['_OAUTHTOKEN']._serialized_end = 1137
    _globals['_OIDCTOKEN']._serialized_start = 1139
    _globals['_OIDCTOKEN']._serialized_end = 1199