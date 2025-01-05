"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ads/admanager/v1/network_messages.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.google/ads/admanager/v1/network_messages.proto\x12\x17google.ads.admanager.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\x99\x03\n\x07Network\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x01\x12\x19\n\x0cnetwork_code\x18\x03 \x01(\tB\x03\xe0A\x03\x12\x1a\n\rproperty_code\x18\x04 \x01(\tB\x03\xe0A\x03\x12\x16\n\ttime_zone\x18\x05 \x01(\tB\x03\xe0A\x03\x12\x1a\n\rcurrency_code\x18\x06 \x01(\tB\x03\xe0A\x03\x12%\n\x18secondary_currency_codes\x18\x07 \x03(\tB\x03\xe0A\x01\x12G\n\x16effective_root_ad_unit\x18\x08 \x01(\tB\'\xe0A\x03\xfaA!\n\x1fadmanager.googleapis.com/AdUnit\x12\x19\n\x0ctest_network\x18\n \x01(\x08B\x03\xe0A\x03\x12\x17\n\nnetwork_id\x18\x0b \x01(\x03B\x03\xe0A\x03:Q\xeaAN\n admanager.googleapis.com/Network\x12\x17networks/{network_code}*\x08networks2\x07networkB\xc8\x01\n\x1bcom.google.ads.admanager.v1B\x14NetworkMessagesProtoP\x01Z@google.golang.org/genproto/googleapis/ads/admanager/v1;admanager\xaa\x02\x17Google.Ads.AdManager.V1\xca\x02\x17Google\\Ads\\AdManager\\V1\xea\x02\x1aGoogle::Ads::AdManager::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.admanager.v1.network_messages_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1bcom.google.ads.admanager.v1B\x14NetworkMessagesProtoP\x01Z@google.golang.org/genproto/googleapis/ads/admanager/v1;admanager\xaa\x02\x17Google.Ads.AdManager.V1\xca\x02\x17Google\\Ads\\AdManager\\V1\xea\x02\x1aGoogle::Ads::AdManager::V1'
    _globals['_NETWORK'].fields_by_name['name']._loaded_options = None
    _globals['_NETWORK'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_NETWORK'].fields_by_name['display_name']._loaded_options = None
    _globals['_NETWORK'].fields_by_name['display_name']._serialized_options = b'\xe0A\x01'
    _globals['_NETWORK'].fields_by_name['network_code']._loaded_options = None
    _globals['_NETWORK'].fields_by_name['network_code']._serialized_options = b'\xe0A\x03'
    _globals['_NETWORK'].fields_by_name['property_code']._loaded_options = None
    _globals['_NETWORK'].fields_by_name['property_code']._serialized_options = b'\xe0A\x03'
    _globals['_NETWORK'].fields_by_name['time_zone']._loaded_options = None
    _globals['_NETWORK'].fields_by_name['time_zone']._serialized_options = b'\xe0A\x03'
    _globals['_NETWORK'].fields_by_name['currency_code']._loaded_options = None
    _globals['_NETWORK'].fields_by_name['currency_code']._serialized_options = b'\xe0A\x03'
    _globals['_NETWORK'].fields_by_name['secondary_currency_codes']._loaded_options = None
    _globals['_NETWORK'].fields_by_name['secondary_currency_codes']._serialized_options = b'\xe0A\x01'
    _globals['_NETWORK'].fields_by_name['effective_root_ad_unit']._loaded_options = None
    _globals['_NETWORK'].fields_by_name['effective_root_ad_unit']._serialized_options = b'\xe0A\x03\xfaA!\n\x1fadmanager.googleapis.com/AdUnit'
    _globals['_NETWORK'].fields_by_name['test_network']._loaded_options = None
    _globals['_NETWORK'].fields_by_name['test_network']._serialized_options = b'\xe0A\x03'
    _globals['_NETWORK'].fields_by_name['network_id']._loaded_options = None
    _globals['_NETWORK'].fields_by_name['network_id']._serialized_options = b'\xe0A\x03'
    _globals['_NETWORK']._loaded_options = None
    _globals['_NETWORK']._serialized_options = b'\xeaAN\n admanager.googleapis.com/Network\x12\x17networks/{network_code}*\x08networks2\x07network'
    _globals['_NETWORK']._serialized_start = 136
    _globals['_NETWORK']._serialized_end = 545