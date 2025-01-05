"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ads/admanager/v1/custom_targeting_key_messages.proto')
_sym_db = _symbol_database.Default()
from .....google.ads.admanager.v1 import custom_targeting_key_enums_pb2 as google_dot_ads_dot_admanager_dot_v1_dot_custom__targeting__key__enums__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n;google/ads/admanager/v1/custom_targeting_key_messages.proto\x12\x17google.ads.admanager.v1\x1a8google/ads/admanager/v1/custom_targeting_key_enums.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xe5\x04\n\x12CustomTargetingKey\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12$\n\x17custom_targeting_key_id\x18\x02 \x01(\x03B\x03\xe0A\x03\x12\x18\n\x0bad_tag_name\x18\x03 \x01(\tB\x03\xe0A\x05\x12\x19\n\x0cdisplay_name\x18\x04 \x01(\tB\x03\xe0A\x01\x12]\n\x04type\x18\x05 \x01(\x0e2J.google.ads.admanager.v1.CustomTargetingKeyTypeEnum.CustomTargetingKeyTypeB\x03\xe0A\x02\x12c\n\x06status\x18\x06 \x01(\x0e2N.google.ads.admanager.v1.CustomTargetingKeyStatusEnum.CustomTargetingKeyStatusB\x03\xe0A\x03\x12|\n\x0freportable_type\x18\x07 \x01(\x0e2^.google.ads.admanager.v1.CustomTargetingKeyReportableTypeEnum.CustomTargetingKeyReportableTypeB\x03\xe0A\x02:\x9e\x01\xeaA\x9a\x01\n+admanager.googleapis.com/CustomTargetingKey\x12Bnetworks/{network_code}/customTargetingKeys/{custom_targeting_key}*\x13customTargetingKeys2\x12customTargetingKeyB\xd3\x01\n\x1bcom.google.ads.admanager.v1B\x1fCustomTargetingKeyMessagesProtoP\x01Z@google.golang.org/genproto/googleapis/ads/admanager/v1;admanager\xaa\x02\x17Google.Ads.AdManager.V1\xca\x02\x17Google\\Ads\\AdManager\\V1\xea\x02\x1aGoogle::Ads::AdManager::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.admanager.v1.custom_targeting_key_messages_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1bcom.google.ads.admanager.v1B\x1fCustomTargetingKeyMessagesProtoP\x01Z@google.golang.org/genproto/googleapis/ads/admanager/v1;admanager\xaa\x02\x17Google.Ads.AdManager.V1\xca\x02\x17Google\\Ads\\AdManager\\V1\xea\x02\x1aGoogle::Ads::AdManager::V1'
    _globals['_CUSTOMTARGETINGKEY'].fields_by_name['name']._loaded_options = None
    _globals['_CUSTOMTARGETINGKEY'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_CUSTOMTARGETINGKEY'].fields_by_name['custom_targeting_key_id']._loaded_options = None
    _globals['_CUSTOMTARGETINGKEY'].fields_by_name['custom_targeting_key_id']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMTARGETINGKEY'].fields_by_name['ad_tag_name']._loaded_options = None
    _globals['_CUSTOMTARGETINGKEY'].fields_by_name['ad_tag_name']._serialized_options = b'\xe0A\x05'
    _globals['_CUSTOMTARGETINGKEY'].fields_by_name['display_name']._loaded_options = None
    _globals['_CUSTOMTARGETINGKEY'].fields_by_name['display_name']._serialized_options = b'\xe0A\x01'
    _globals['_CUSTOMTARGETINGKEY'].fields_by_name['type']._loaded_options = None
    _globals['_CUSTOMTARGETINGKEY'].fields_by_name['type']._serialized_options = b'\xe0A\x02'
    _globals['_CUSTOMTARGETINGKEY'].fields_by_name['status']._loaded_options = None
    _globals['_CUSTOMTARGETINGKEY'].fields_by_name['status']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMTARGETINGKEY'].fields_by_name['reportable_type']._loaded_options = None
    _globals['_CUSTOMTARGETINGKEY'].fields_by_name['reportable_type']._serialized_options = b'\xe0A\x02'
    _globals['_CUSTOMTARGETINGKEY']._loaded_options = None
    _globals['_CUSTOMTARGETINGKEY']._serialized_options = b'\xeaA\x9a\x01\n+admanager.googleapis.com/CustomTargetingKey\x12Bnetworks/{network_code}/customTargetingKeys/{custom_targeting_key}*\x13customTargetingKeys2\x12customTargetingKey'
    _globals['_CUSTOMTARGETINGKEY']._serialized_start = 207
    _globals['_CUSTOMTARGETINGKEY']._serialized_end = 820