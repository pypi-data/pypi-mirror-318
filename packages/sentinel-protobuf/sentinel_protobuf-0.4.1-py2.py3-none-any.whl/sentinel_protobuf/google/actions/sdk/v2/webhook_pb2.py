"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/actions/sdk/v2/webhook.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#google/actions/sdk/v2/webhook.proto\x12\x15google.actions.sdk.v2\x1a\x1fgoogle/api/field_behavior.proto"\x8a\x04\n\x07Webhook\x128\n\x08handlers\x18\x01 \x03(\x0b2&.google.actions.sdk.v2.Webhook.Handler\x12F\n\x0ehttps_endpoint\x18\x02 \x01(\x0b2,.google.actions.sdk.v2.Webhook.HttpsEndpointH\x00\x12S\n\x15inline_cloud_function\x18\x03 \x01(\x0b22.google.actions.sdk.v2.Webhook.InlineCloudFunctionH\x00\x1a\x1c\n\x07Handler\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x1a\xc8\x01\n\rHttpsEndpoint\x12\x10\n\x08base_url\x18\x01 \x01(\t\x12S\n\x0chttp_headers\x18\x02 \x03(\x0b2=.google.actions.sdk.v2.Webhook.HttpsEndpoint.HttpHeadersEntry\x12\x1c\n\x14endpoint_api_version\x18\x03 \x01(\x05\x1a2\n\x10HttpHeadersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01\x1a/\n\x13InlineCloudFunction\x12\x18\n\x10execute_function\x18\x01 \x01(\tB\x0e\n\x0cwebhook_typeBe\n\x19com.google.actions.sdk.v2B\x0cWebhookProtoP\x01Z8google.golang.org/genproto/googleapis/actions/sdk/v2;sdkb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.actions.sdk.v2.webhook_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x19com.google.actions.sdk.v2B\x0cWebhookProtoP\x01Z8google.golang.org/genproto/googleapis/actions/sdk/v2;sdk'
    _globals['_WEBHOOK_HANDLER'].fields_by_name['name']._loaded_options = None
    _globals['_WEBHOOK_HANDLER'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_WEBHOOK_HTTPSENDPOINT_HTTPHEADERSENTRY']._loaded_options = None
    _globals['_WEBHOOK_HTTPSENDPOINT_HTTPHEADERSENTRY']._serialized_options = b'8\x01'
    _globals['_WEBHOOK']._serialized_start = 96
    _globals['_WEBHOOK']._serialized_end = 618
    _globals['_WEBHOOK_HANDLER']._serialized_start = 322
    _globals['_WEBHOOK_HANDLER']._serialized_end = 350
    _globals['_WEBHOOK_HTTPSENDPOINT']._serialized_start = 353
    _globals['_WEBHOOK_HTTPSENDPOINT']._serialized_end = 553
    _globals['_WEBHOOK_HTTPSENDPOINT_HTTPHEADERSENTRY']._serialized_start = 503
    _globals['_WEBHOOK_HTTPSENDPOINT_HTTPHEADERSENTRY']._serialized_end = 553
    _globals['_WEBHOOK_INLINECLOUDFUNCTION']._serialized_start = 555
    _globals['_WEBHOOK_INLINECLOUDFUNCTION']._serialized_end = 602