"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ads/admanager/v1/user_messages.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+google/ads/admanager/v1/user_messages.proto\x12\x17google.ads.admanager.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xdf\x02\n\x04User\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\x14\n\x07user_id\x18\n \x01(\x03B\x03\xe0A\x03\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x12\n\x05email\x18\x03 \x01(\tB\x03\xe0A\x02\x123\n\x04role\x18\x04 \x01(\tB%\xe0A\x02\xfaA\x1f\n\x1dadmanager.googleapis.com/Role\x12\x13\n\x06active\x18\x06 \x01(\x08B\x03\xe0A\x03\x12\x18\n\x0bexternal_id\x18\x07 \x01(\tB\x03\xe0A\x01\x12\x1c\n\x0fservice_account\x18\x08 \x01(\x08B\x03\xe0A\x03\x12&\n\x19orders_ui_local_time_zone\x18\t \x01(\tB\x03\xe0A\x01:U\xeaAR\n\x1dadmanager.googleapis.com/User\x12$networks/{network_code}/users/{user}*\x05users2\x04userB\xc5\x01\n\x1bcom.google.ads.admanager.v1B\x11UserMessagesProtoP\x01Z@google.golang.org/genproto/googleapis/ads/admanager/v1;admanager\xaa\x02\x17Google.Ads.AdManager.V1\xca\x02\x17Google\\Ads\\AdManager\\V1\xea\x02\x1aGoogle::Ads::AdManager::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.admanager.v1.user_messages_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1bcom.google.ads.admanager.v1B\x11UserMessagesProtoP\x01Z@google.golang.org/genproto/googleapis/ads/admanager/v1;admanager\xaa\x02\x17Google.Ads.AdManager.V1\xca\x02\x17Google\\Ads\\AdManager\\V1\xea\x02\x1aGoogle::Ads::AdManager::V1'
    _globals['_USER'].fields_by_name['name']._loaded_options = None
    _globals['_USER'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_USER'].fields_by_name['user_id']._loaded_options = None
    _globals['_USER'].fields_by_name['user_id']._serialized_options = b'\xe0A\x03'
    _globals['_USER'].fields_by_name['display_name']._loaded_options = None
    _globals['_USER'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_USER'].fields_by_name['email']._loaded_options = None
    _globals['_USER'].fields_by_name['email']._serialized_options = b'\xe0A\x02'
    _globals['_USER'].fields_by_name['role']._loaded_options = None
    _globals['_USER'].fields_by_name['role']._serialized_options = b'\xe0A\x02\xfaA\x1f\n\x1dadmanager.googleapis.com/Role'
    _globals['_USER'].fields_by_name['active']._loaded_options = None
    _globals['_USER'].fields_by_name['active']._serialized_options = b'\xe0A\x03'
    _globals['_USER'].fields_by_name['external_id']._loaded_options = None
    _globals['_USER'].fields_by_name['external_id']._serialized_options = b'\xe0A\x01'
    _globals['_USER'].fields_by_name['service_account']._loaded_options = None
    _globals['_USER'].fields_by_name['service_account']._serialized_options = b'\xe0A\x03'
    _globals['_USER'].fields_by_name['orders_ui_local_time_zone']._loaded_options = None
    _globals['_USER'].fields_by_name['orders_ui_local_time_zone']._serialized_options = b'\xe0A\x01'
    _globals['_USER']._loaded_options = None
    _globals['_USER']._serialized_options = b'\xeaAR\n\x1dadmanager.googleapis.com/User\x12$networks/{network_code}/users/{user}*\x05users2\x04user'
    _globals['_USER']._serialized_start = 133
    _globals['_USER']._serialized_end = 484