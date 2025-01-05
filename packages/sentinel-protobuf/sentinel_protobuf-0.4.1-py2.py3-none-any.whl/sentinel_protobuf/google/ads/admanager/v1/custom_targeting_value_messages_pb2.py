"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ads/admanager/v1/custom_targeting_value_messages.proto')
_sym_db = _symbol_database.Default()
from .....google.ads.admanager.v1 import custom_targeting_value_enums_pb2 as google_dot_ads_dot_admanager_dot_v1_dot_custom__targeting__value__enums__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n=google/ads/admanager/v1/custom_targeting_value_messages.proto\x12\x17google.ads.admanager.v1\x1a:google/ads/admanager/v1/custom_targeting_value_enums.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\x93\x04\n\x14CustomTargetingValue\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\x18\n\x0bad_tag_name\x18\x04 \x01(\tB\x03\xe0A\x05\x12\x19\n\x0cdisplay_name\x18\x05 \x01(\tB\x03\xe0A\x01\x12t\n\nmatch_type\x18\x06 \x01(\x0e2X.google.ads.admanager.v1.CustomTargetingValueMatchTypeEnum.CustomTargetingValueMatchTypeB\x06\xe0A\x05\xe0A\x02\x12g\n\x06status\x18\x07 \x01(\x0e2R.google.ads.admanager.v1.CustomTargetingValueStatusEnum.CustomTargetingValueStatusB\x03\xe0A\x03:\xd3\x01\xeaA\xcf\x01\n-admanager.googleapis.com/CustomTargetingValue\x12qnetworks/{network_code}/customTargetingKeys/{custom_targeting_key}/customTargetingValues/{custom_targeting_value}*\x15customTargetingValues2\x14customTargetingValueB\xd5\x01\n\x1bcom.google.ads.admanager.v1B!CustomTargetingValueMessagesProtoP\x01Z@google.golang.org/genproto/googleapis/ads/admanager/v1;admanager\xaa\x02\x17Google.Ads.AdManager.V1\xca\x02\x17Google\\Ads\\AdManager\\V1\xea\x02\x1aGoogle::Ads::AdManager::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.admanager.v1.custom_targeting_value_messages_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1bcom.google.ads.admanager.v1B!CustomTargetingValueMessagesProtoP\x01Z@google.golang.org/genproto/googleapis/ads/admanager/v1;admanager\xaa\x02\x17Google.Ads.AdManager.V1\xca\x02\x17Google\\Ads\\AdManager\\V1\xea\x02\x1aGoogle::Ads::AdManager::V1'
    _globals['_CUSTOMTARGETINGVALUE'].fields_by_name['name']._loaded_options = None
    _globals['_CUSTOMTARGETINGVALUE'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_CUSTOMTARGETINGVALUE'].fields_by_name['ad_tag_name']._loaded_options = None
    _globals['_CUSTOMTARGETINGVALUE'].fields_by_name['ad_tag_name']._serialized_options = b'\xe0A\x05'
    _globals['_CUSTOMTARGETINGVALUE'].fields_by_name['display_name']._loaded_options = None
    _globals['_CUSTOMTARGETINGVALUE'].fields_by_name['display_name']._serialized_options = b'\xe0A\x01'
    _globals['_CUSTOMTARGETINGVALUE'].fields_by_name['match_type']._loaded_options = None
    _globals['_CUSTOMTARGETINGVALUE'].fields_by_name['match_type']._serialized_options = b'\xe0A\x05\xe0A\x02'
    _globals['_CUSTOMTARGETINGVALUE'].fields_by_name['status']._loaded_options = None
    _globals['_CUSTOMTARGETINGVALUE'].fields_by_name['status']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMTARGETINGVALUE']._loaded_options = None
    _globals['_CUSTOMTARGETINGVALUE']._serialized_options = b'\xeaA\xcf\x01\n-admanager.googleapis.com/CustomTargetingValue\x12qnetworks/{network_code}/customTargetingKeys/{custom_targeting_key}/customTargetingValues/{custom_targeting_value}*\x15customTargetingValues2\x14customTargetingValue'
    _globals['_CUSTOMTARGETINGVALUE']._serialized_start = 211
    _globals['_CUSTOMTARGETINGVALUE']._serialized_end = 742