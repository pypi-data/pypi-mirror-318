"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ads/admanager/v1/role_service.proto')
_sym_db = _symbol_database.Default()
from .....google.ads.admanager.v1 import role_messages_pb2 as google_dot_ads_dot_admanager_dot_v1_dot_role__messages__pb2
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*google/ads/admanager/v1/role_service.proto\x12\x17google.ads.admanager.v1\x1a+google/ads/admanager/v1/role_messages.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"E\n\x0eGetRoleRequest\x123\n\x04name\x18\x01 \x01(\tB%\xe0A\x02\xfaA\x1f\n\x1dadmanager.googleapis.com/Role"\xbc\x01\n\x10ListRolesRequest\x128\n\x06parent\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n admanager.googleapis.com/Network\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x15\n\x08order_by\x18\x05 \x01(\tB\x03\xe0A\x01\x12\x11\n\x04skip\x18\x06 \x01(\x05B\x03\xe0A\x01"n\n\x11ListRolesResponse\x12,\n\x05roles\x18\x01 \x03(\x0b2\x1d.google.ads.admanager.v1.Role\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x12\n\ntotal_size\x18\x03 \x01(\x052\xc0\x02\n\x0bRoleService\x12\x7f\n\x07GetRole\x12\'.google.ads.admanager.v1.GetRoleRequest\x1a\x1d.google.ads.admanager.v1.Role",\xdaA\x04name\x82\xd3\xe4\x93\x02\x1f\x12\x1d/v1/{name=networks/*/roles/*}\x12\x92\x01\n\tListRoles\x12).google.ads.admanager.v1.ListRolesRequest\x1a*.google.ads.admanager.v1.ListRolesResponse".\xdaA\x06parent\x82\xd3\xe4\x93\x02\x1f\x12\x1d/v1/{parent=networks/*}/roles\x1a\x1b\xcaA\x18admanager.googleapis.comB\xc4\x01\n\x1bcom.google.ads.admanager.v1B\x10RoleServiceProtoP\x01Z@google.golang.org/genproto/googleapis/ads/admanager/v1;admanager\xaa\x02\x17Google.Ads.AdManager.V1\xca\x02\x17Google\\Ads\\AdManager\\V1\xea\x02\x1aGoogle::Ads::AdManager::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.admanager.v1.role_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1bcom.google.ads.admanager.v1B\x10RoleServiceProtoP\x01Z@google.golang.org/genproto/googleapis/ads/admanager/v1;admanager\xaa\x02\x17Google.Ads.AdManager.V1\xca\x02\x17Google\\Ads\\AdManager\\V1\xea\x02\x1aGoogle::Ads::AdManager::V1'
    _globals['_GETROLEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETROLEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA\x1f\n\x1dadmanager.googleapis.com/Role'
    _globals['_LISTROLESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTROLESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA"\n admanager.googleapis.com/Network'
    _globals['_LISTROLESREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTROLESREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTROLESREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTROLESREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTROLESREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTROLESREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_LISTROLESREQUEST'].fields_by_name['order_by']._loaded_options = None
    _globals['_LISTROLESREQUEST'].fields_by_name['order_by']._serialized_options = b'\xe0A\x01'
    _globals['_LISTROLESREQUEST'].fields_by_name['skip']._loaded_options = None
    _globals['_LISTROLESREQUEST'].fields_by_name['skip']._serialized_options = b'\xe0A\x01'
    _globals['_ROLESERVICE']._loaded_options = None
    _globals['_ROLESERVICE']._serialized_options = b'\xcaA\x18admanager.googleapis.com'
    _globals['_ROLESERVICE'].methods_by_name['GetRole']._loaded_options = None
    _globals['_ROLESERVICE'].methods_by_name['GetRole']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\x1f\x12\x1d/v1/{name=networks/*/roles/*}'
    _globals['_ROLESERVICE'].methods_by_name['ListRoles']._loaded_options = None
    _globals['_ROLESERVICE'].methods_by_name['ListRoles']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02\x1f\x12\x1d/v1/{parent=networks/*}/roles'
    _globals['_GETROLEREQUEST']._serialized_start = 231
    _globals['_GETROLEREQUEST']._serialized_end = 300
    _globals['_LISTROLESREQUEST']._serialized_start = 303
    _globals['_LISTROLESREQUEST']._serialized_end = 491
    _globals['_LISTROLESRESPONSE']._serialized_start = 493
    _globals['_LISTROLESRESPONSE']._serialized_end = 603
    _globals['_ROLESERVICE']._serialized_start = 606
    _globals['_ROLESERVICE']._serialized_end = 926