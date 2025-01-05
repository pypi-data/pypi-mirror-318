"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ads/googleads/v17/resources/asset_group_top_combination_view.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v17.common import asset_usage_pb2 as google_dot_ads_dot_googleads_dot_v17_dot_common_dot_asset__usage__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nIgoogle/ads/googleads/v17/resources/asset_group_top_combination_view.proto\x12"google.ads.googleads.v17.resources\x1a1google/ads/googleads/v17/common/asset_usage.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\x86\x03\n\x1cAssetGroupTopCombinationView\x12T\n\rresource_name\x18\x01 \x01(\tB=\xe0A\x03\xfaA7\n5googleads.googleapis.com/AssetGroupTopCombinationView\x12m\n\x1casset_group_top_combinations\x18\x02 \x03(\x0b2B.google.ads.googleads.v17.resources.AssetGroupAssetCombinationDataB\x03\xe0A\x03:\xa0\x01\xeaA\x9c\x01\n5googleads.googleapis.com/AssetGroupTopCombinationView\x12ccustomers/{customer_id}/assetGroupTopCombinationViews/{asset_group_id}~{asset_combination_category}"{\n\x1eAssetGroupAssetCombinationData\x12Y\n\x1fasset_combination_served_assets\x18\x01 \x03(\x0b2+.google.ads.googleads.v17.common.AssetUsageB\x03\xe0A\x03B\x93\x02\n&com.google.ads.googleads.v17.resourcesB!AssetGroupTopCombinationViewProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v17/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V17.Resources\xca\x02"Google\\Ads\\GoogleAds\\V17\\Resources\xea\x02&Google::Ads::GoogleAds::V17::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v17.resources.asset_group_top_combination_view_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v17.resourcesB!AssetGroupTopCombinationViewProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v17/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V17.Resources\xca\x02"Google\\Ads\\GoogleAds\\V17\\Resources\xea\x02&Google::Ads::GoogleAds::V17::Resources'
    _globals['_ASSETGROUPTOPCOMBINATIONVIEW'].fields_by_name['resource_name']._loaded_options = None
    _globals['_ASSETGROUPTOPCOMBINATIONVIEW'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x03\xfaA7\n5googleads.googleapis.com/AssetGroupTopCombinationView'
    _globals['_ASSETGROUPTOPCOMBINATIONVIEW'].fields_by_name['asset_group_top_combinations']._loaded_options = None
    _globals['_ASSETGROUPTOPCOMBINATIONVIEW'].fields_by_name['asset_group_top_combinations']._serialized_options = b'\xe0A\x03'
    _globals['_ASSETGROUPTOPCOMBINATIONVIEW']._loaded_options = None
    _globals['_ASSETGROUPTOPCOMBINATIONVIEW']._serialized_options = b'\xeaA\x9c\x01\n5googleads.googleapis.com/AssetGroupTopCombinationView\x12ccustomers/{customer_id}/assetGroupTopCombinationViews/{asset_group_id}~{asset_combination_category}'
    _globals['_ASSETGROUPASSETCOMBINATIONDATA'].fields_by_name['asset_combination_served_assets']._loaded_options = None
    _globals['_ASSETGROUPASSETCOMBINATIONDATA'].fields_by_name['asset_combination_served_assets']._serialized_options = b'\xe0A\x03'
    _globals['_ASSETGROUPTOPCOMBINATIONVIEW']._serialized_start = 225
    _globals['_ASSETGROUPTOPCOMBINATIONVIEW']._serialized_end = 615
    _globals['_ASSETGROUPASSETCOMBINATIONDATA']._serialized_start = 617
    _globals['_ASSETGROUPASSETCOMBINATIONDATA']._serialized_end = 740