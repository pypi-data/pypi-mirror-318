"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ads/admanager/v1/role_messages.proto')
_sym_db = _symbol_database.Default()
from .....google.ads.admanager.v1 import role_enums_pb2 as google_dot_ads_dot_admanager_dot_v1_dot_role__enums__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+google/ads/admanager/v1/role_messages.proto\x12\x17google.ads.admanager.v1\x1a(google/ads/admanager/v1/role_enums.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\x9b\x02\n\x04Role\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\x14\n\x07role_id\x18\x02 \x01(\x03B\x03\xe0A\x03\x12\x19\n\x0cdisplay_name\x18\x03 \x01(\tB\x03\xe0A\x02\x12\x18\n\x0bdescription\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x15\n\x08built_in\x18\x05 \x01(\x08B\x03\xe0A\x03\x12G\n\x06status\x18\x06 \x01(\x0e22.google.ads.admanager.v1.RoleStatusEnum.RoleStatusB\x03\xe0A\x03:U\xeaAR\n\x1dadmanager.googleapis.com/Role\x12$networks/{network_code}/roles/{role}*\x05roles2\x04roleB\xc5\x01\n\x1bcom.google.ads.admanager.v1B\x11RoleMessagesProtoP\x01Z@google.golang.org/genproto/googleapis/ads/admanager/v1;admanager\xaa\x02\x17Google.Ads.AdManager.V1\xca\x02\x17Google\\Ads\\AdManager\\V1\xea\x02\x1aGoogle::Ads::AdManager::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.admanager.v1.role_messages_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1bcom.google.ads.admanager.v1B\x11RoleMessagesProtoP\x01Z@google.golang.org/genproto/googleapis/ads/admanager/v1;admanager\xaa\x02\x17Google.Ads.AdManager.V1\xca\x02\x17Google\\Ads\\AdManager\\V1\xea\x02\x1aGoogle::Ads::AdManager::V1'
    _globals['_ROLE'].fields_by_name['name']._loaded_options = None
    _globals['_ROLE'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_ROLE'].fields_by_name['role_id']._loaded_options = None
    _globals['_ROLE'].fields_by_name['role_id']._serialized_options = b'\xe0A\x03'
    _globals['_ROLE'].fields_by_name['display_name']._loaded_options = None
    _globals['_ROLE'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_ROLE'].fields_by_name['description']._loaded_options = None
    _globals['_ROLE'].fields_by_name['description']._serialized_options = b'\xe0A\x01'
    _globals['_ROLE'].fields_by_name['built_in']._loaded_options = None
    _globals['_ROLE'].fields_by_name['built_in']._serialized_options = b'\xe0A\x03'
    _globals['_ROLE'].fields_by_name['status']._loaded_options = None
    _globals['_ROLE'].fields_by_name['status']._serialized_options = b'\xe0A\x03'
    _globals['_ROLE']._loaded_options = None
    _globals['_ROLE']._serialized_options = b'\xeaAR\n\x1dadmanager.googleapis.com/Role\x12$networks/{network_code}/roles/{role}*\x05roles2\x04role'
    _globals['_ROLE']._serialized_start = 175
    _globals['_ROLE']._serialized_end = 458