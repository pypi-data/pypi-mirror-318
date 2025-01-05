"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ads/googleads/v16/resources/android_privacy_shared_key_google_ad_group.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v16.enums import android_privacy_interaction_type_pb2 as google_dot_ads_dot_googleads_dot_v16_dot_enums_dot_android__privacy__interaction__type__pb2
from ......google.ads.googleads.v16.enums import android_privacy_network_type_pb2 as google_dot_ads_dot_googleads_dot_v16_dot_enums_dot_android__privacy__network__type__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nSgoogle/ads/googleads/v16/resources/android_privacy_shared_key_google_ad_group.proto\x12"google.ads.googleads.v16.resources\x1aEgoogle/ads/googleads/v16/enums/android_privacy_interaction_type.proto\x1aAgoogle/ads/googleads/v16/enums/android_privacy_network_type.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xa6\x06\n$AndroidPrivacySharedKeyGoogleAdGroup\x12\\\n\rresource_name\x18\x01 \x01(\tBE\xe0A\x03\xfaA?\n=googleads.googleapis.com/AndroidPrivacySharedKeyGoogleAdGroup\x12\x18\n\x0bcampaign_id\x18\x02 \x01(\x03B\x03\xe0A\x03\x12\x8e\x01\n android_privacy_interaction_type\x18\x03 \x01(\x0e2_.google.ads.googleads.v16.enums.AndroidPrivacyInteractionTypeEnum.AndroidPrivacyInteractionTypeB\x03\xe0A\x03\x12-\n android_privacy_interaction_date\x18\x04 \x01(\tB\x03\xe0A\x03\x12\x82\x01\n\x1candroid_privacy_network_type\x18\x05 \x01(\x0e2W.google.ads.googleads.v16.enums.AndroidPrivacyNetworkTypeEnum.AndroidPrivacyNetworkTypeB\x03\xe0A\x03\x12\x18\n\x0bad_group_id\x18\x06 \x01(\x03B\x03\xe0A\x03\x12 \n\x13shared_ad_group_key\x18\x07 \x01(\tB\x03\xe0A\x03:\x84\x02\xeaA\x80\x02\n=googleads.googleapis.com/AndroidPrivacySharedKeyGoogleAdGroup\x12\xbe\x01customers/{customer_id}/androidPrivacySharedKeyGoogleAdGroups/{campaign_id}~{ad_group_id}~{android_privacy_interaction_type}~{android_privacy_network_type}~{android_privacy_interaction_date}B\x9b\x02\n&com.google.ads.googleads.v16.resourcesB)AndroidPrivacySharedKeyGoogleAdGroupProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v16/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V16.Resources\xca\x02"Google\\Ads\\GoogleAds\\V16\\Resources\xea\x02&Google::Ads::GoogleAds::V16::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v16.resources.android_privacy_shared_key_google_ad_group_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v16.resourcesB)AndroidPrivacySharedKeyGoogleAdGroupProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v16/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V16.Resources\xca\x02"Google\\Ads\\GoogleAds\\V16\\Resources\xea\x02&Google::Ads::GoogleAds::V16::Resources'
    _globals['_ANDROIDPRIVACYSHAREDKEYGOOGLEADGROUP'].fields_by_name['resource_name']._loaded_options = None
    _globals['_ANDROIDPRIVACYSHAREDKEYGOOGLEADGROUP'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x03\xfaA?\n=googleads.googleapis.com/AndroidPrivacySharedKeyGoogleAdGroup'
    _globals['_ANDROIDPRIVACYSHAREDKEYGOOGLEADGROUP'].fields_by_name['campaign_id']._loaded_options = None
    _globals['_ANDROIDPRIVACYSHAREDKEYGOOGLEADGROUP'].fields_by_name['campaign_id']._serialized_options = b'\xe0A\x03'
    _globals['_ANDROIDPRIVACYSHAREDKEYGOOGLEADGROUP'].fields_by_name['android_privacy_interaction_type']._loaded_options = None
    _globals['_ANDROIDPRIVACYSHAREDKEYGOOGLEADGROUP'].fields_by_name['android_privacy_interaction_type']._serialized_options = b'\xe0A\x03'
    _globals['_ANDROIDPRIVACYSHAREDKEYGOOGLEADGROUP'].fields_by_name['android_privacy_interaction_date']._loaded_options = None
    _globals['_ANDROIDPRIVACYSHAREDKEYGOOGLEADGROUP'].fields_by_name['android_privacy_interaction_date']._serialized_options = b'\xe0A\x03'
    _globals['_ANDROIDPRIVACYSHAREDKEYGOOGLEADGROUP'].fields_by_name['android_privacy_network_type']._loaded_options = None
    _globals['_ANDROIDPRIVACYSHAREDKEYGOOGLEADGROUP'].fields_by_name['android_privacy_network_type']._serialized_options = b'\xe0A\x03'
    _globals['_ANDROIDPRIVACYSHAREDKEYGOOGLEADGROUP'].fields_by_name['ad_group_id']._loaded_options = None
    _globals['_ANDROIDPRIVACYSHAREDKEYGOOGLEADGROUP'].fields_by_name['ad_group_id']._serialized_options = b'\xe0A\x03'
    _globals['_ANDROIDPRIVACYSHAREDKEYGOOGLEADGROUP'].fields_by_name['shared_ad_group_key']._loaded_options = None
    _globals['_ANDROIDPRIVACYSHAREDKEYGOOGLEADGROUP'].fields_by_name['shared_ad_group_key']._serialized_options = b'\xe0A\x03'
    _globals['_ANDROIDPRIVACYSHAREDKEYGOOGLEADGROUP']._loaded_options = None
    _globals['_ANDROIDPRIVACYSHAREDKEYGOOGLEADGROUP']._serialized_options = b'\xeaA\x80\x02\n=googleads.googleapis.com/AndroidPrivacySharedKeyGoogleAdGroup\x12\xbe\x01customers/{customer_id}/androidPrivacySharedKeyGoogleAdGroups/{campaign_id}~{ad_group_id}~{android_privacy_interaction_type}~{android_privacy_network_type}~{android_privacy_interaction_date}'
    _globals['_ANDROIDPRIVACYSHAREDKEYGOOGLEADGROUP']._serialized_start = 322
    _globals['_ANDROIDPRIVACYSHAREDKEYGOOGLEADGROUP']._serialized_end = 1128