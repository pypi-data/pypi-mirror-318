"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ads/admanager/v1/user_service.proto')
_sym_db = _symbol_database.Default()
from .....google.ads.admanager.v1 import user_messages_pb2 as google_dot_ads_dot_admanager_dot_v1_dot_user__messages__pb2
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*google/ads/admanager/v1/user_service.proto\x12\x17google.ads.admanager.v1\x1a+google/ads/admanager/v1/user_messages.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"E\n\x0eGetUserRequest\x123\n\x04name\x18\x01 \x01(\tB%\xe0A\x02\xfaA\x1f\n\x1dadmanager.googleapis.com/User2\xab\x01\n\x0bUserService\x12\x7f\n\x07GetUser\x12\'.google.ads.admanager.v1.GetUserRequest\x1a\x1d.google.ads.admanager.v1.User",\xdaA\x04name\x82\xd3\xe4\x93\x02\x1f\x12\x1d/v1/{name=networks/*/users/*}\x1a\x1b\xcaA\x18admanager.googleapis.comB\xc4\x01\n\x1bcom.google.ads.admanager.v1B\x10UserServiceProtoP\x01Z@google.golang.org/genproto/googleapis/ads/admanager/v1;admanager\xaa\x02\x17Google.Ads.AdManager.V1\xca\x02\x17Google\\Ads\\AdManager\\V1\xea\x02\x1aGoogle::Ads::AdManager::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.admanager.v1.user_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1bcom.google.ads.admanager.v1B\x10UserServiceProtoP\x01Z@google.golang.org/genproto/googleapis/ads/admanager/v1;admanager\xaa\x02\x17Google.Ads.AdManager.V1\xca\x02\x17Google\\Ads\\AdManager\\V1\xea\x02\x1aGoogle::Ads::AdManager::V1'
    _globals['_GETUSERREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETUSERREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA\x1f\n\x1dadmanager.googleapis.com/User'
    _globals['_USERSERVICE']._loaded_options = None
    _globals['_USERSERVICE']._serialized_options = b'\xcaA\x18admanager.googleapis.com'
    _globals['_USERSERVICE'].methods_by_name['GetUser']._loaded_options = None
    _globals['_USERSERVICE'].methods_by_name['GetUser']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\x1f\x12\x1d/v1/{name=networks/*/users/*}'
    _globals['_GETUSERREQUEST']._serialized_start = 231
    _globals['_GETUSERREQUEST']._serialized_end = 300
    _globals['_USERSERVICE']._serialized_start = 303
    _globals['_USERSERVICE']._serialized_end = 474