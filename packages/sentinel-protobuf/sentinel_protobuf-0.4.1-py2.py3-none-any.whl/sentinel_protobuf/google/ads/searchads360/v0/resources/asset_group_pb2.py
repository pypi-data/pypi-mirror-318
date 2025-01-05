"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ads/searchads360/v0/resources/asset_group.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.searchads360.v0.enums import ad_strength_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_enums_dot_ad__strength__pb2
from ......google.ads.searchads360.v0.enums import asset_group_status_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_enums_dot_asset__group__status__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6google/ads/searchads360/v0/resources/asset_group.proto\x12$google.ads.searchads360.v0.resources\x1a2google/ads/searchads360/v0/enums/ad_strength.proto\x1a9google/ads/searchads360/v0/enums/asset_group_status.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\x97\x04\n\nAssetGroup\x12E\n\rresource_name\x18\x01 \x01(\tB.\xe0A\x05\xfaA(\n&searchads360.googleapis.com/AssetGroup\x12\x0f\n\x02id\x18\t \x01(\x03B\x03\xe0A\x03\x12>\n\x08campaign\x18\x02 \x01(\tB,\xe0A\x05\xfaA&\n$searchads360.googleapis.com/Campaign\x12\x11\n\x04name\x18\x03 \x01(\tB\x03\xe0A\x02\x12\x12\n\nfinal_urls\x18\x04 \x03(\t\x12\x19\n\x11final_mobile_urls\x18\x05 \x03(\t\x12W\n\x06status\x18\x06 \x01(\x0e2G.google.ads.searchads360.v0.enums.AssetGroupStatusEnum.AssetGroupStatus\x12\r\n\x05path1\x18\x07 \x01(\t\x12\r\n\x05path2\x18\x08 \x01(\t\x12U\n\x0bad_strength\x18\n \x01(\x0e2;.google.ads.searchads360.v0.enums.AdStrengthEnum.AdStrengthB\x03\xe0A\x03:a\xeaA^\n&searchads360.googleapis.com/AssetGroup\x124customers/{customer_id}/assetGroups/{asset_group_id}B\x8f\x02\n(com.google.ads.searchads360.v0.resourcesB\x0fAssetGroupProtoP\x01ZMgoogle.golang.org/genproto/googleapis/ads/searchads360/v0/resources;resources\xa2\x02\x07GASA360\xaa\x02$Google.Ads.SearchAds360.V0.Resources\xca\x02$Google\\Ads\\SearchAds360\\V0\\Resources\xea\x02(Google::Ads::SearchAds360::V0::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.searchads360.v0.resources.asset_group_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n(com.google.ads.searchads360.v0.resourcesB\x0fAssetGroupProtoP\x01ZMgoogle.golang.org/genproto/googleapis/ads/searchads360/v0/resources;resources\xa2\x02\x07GASA360\xaa\x02$Google.Ads.SearchAds360.V0.Resources\xca\x02$Google\\Ads\\SearchAds360\\V0\\Resources\xea\x02(Google::Ads::SearchAds360::V0::Resources'
    _globals['_ASSETGROUP'].fields_by_name['resource_name']._loaded_options = None
    _globals['_ASSETGROUP'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x05\xfaA(\n&searchads360.googleapis.com/AssetGroup'
    _globals['_ASSETGROUP'].fields_by_name['id']._loaded_options = None
    _globals['_ASSETGROUP'].fields_by_name['id']._serialized_options = b'\xe0A\x03'
    _globals['_ASSETGROUP'].fields_by_name['campaign']._loaded_options = None
    _globals['_ASSETGROUP'].fields_by_name['campaign']._serialized_options = b'\xe0A\x05\xfaA&\n$searchads360.googleapis.com/Campaign'
    _globals['_ASSETGROUP'].fields_by_name['name']._loaded_options = None
    _globals['_ASSETGROUP'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_ASSETGROUP'].fields_by_name['ad_strength']._loaded_options = None
    _globals['_ASSETGROUP'].fields_by_name['ad_strength']._serialized_options = b'\xe0A\x03'
    _globals['_ASSETGROUP']._loaded_options = None
    _globals['_ASSETGROUP']._serialized_options = b'\xeaA^\n&searchads360.googleapis.com/AssetGroup\x124customers/{customer_id}/assetGroups/{asset_group_id}'
    _globals['_ASSETGROUP']._serialized_start = 268
    _globals['_ASSETGROUP']._serialized_end = 803