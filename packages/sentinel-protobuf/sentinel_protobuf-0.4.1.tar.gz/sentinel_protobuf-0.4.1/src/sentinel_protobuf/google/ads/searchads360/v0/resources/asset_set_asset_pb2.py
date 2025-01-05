"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ads/searchads360/v0/resources/asset_set_asset.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.searchads360.v0.enums import asset_set_asset_status_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_enums_dot_asset__set__asset__status__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:google/ads/searchads360/v0/resources/asset_set_asset.proto\x12$google.ads.searchads360.v0.resources\x1a=google/ads/searchads360/v0/enums/asset_set_asset_status.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xaa\x03\n\rAssetSetAsset\x12H\n\rresource_name\x18\x01 \x01(\tB1\xe0A\x05\xfaA+\n)searchads360.googleapis.com/AssetSetAsset\x12?\n\tasset_set\x18\x02 \x01(\tB,\xe0A\x05\xfaA&\n$searchads360.googleapis.com/AssetSet\x128\n\x05asset\x18\x03 \x01(\tB)\xe0A\x05\xfaA#\n!searchads360.googleapis.com/Asset\x12b\n\x06status\x18\x04 \x01(\x0e2M.google.ads.searchads360.v0.enums.AssetSetAssetStatusEnum.AssetSetAssetStatusB\x03\xe0A\x03:p\xeaAm\n)searchads360.googleapis.com/AssetSetAsset\x12@customers/{customer_id}/assetSetAssets/{asset_set_id}~{asset_id}B\x92\x02\n(com.google.ads.searchads360.v0.resourcesB\x12AssetSetAssetProtoP\x01ZMgoogle.golang.org/genproto/googleapis/ads/searchads360/v0/resources;resources\xa2\x02\x07GASA360\xaa\x02$Google.Ads.SearchAds360.V0.Resources\xca\x02$Google\\Ads\\SearchAds360\\V0\\Resources\xea\x02(Google::Ads::SearchAds360::V0::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.searchads360.v0.resources.asset_set_asset_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n(com.google.ads.searchads360.v0.resourcesB\x12AssetSetAssetProtoP\x01ZMgoogle.golang.org/genproto/googleapis/ads/searchads360/v0/resources;resources\xa2\x02\x07GASA360\xaa\x02$Google.Ads.SearchAds360.V0.Resources\xca\x02$Google\\Ads\\SearchAds360\\V0\\Resources\xea\x02(Google::Ads::SearchAds360::V0::Resources'
    _globals['_ASSETSETASSET'].fields_by_name['resource_name']._loaded_options = None
    _globals['_ASSETSETASSET'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x05\xfaA+\n)searchads360.googleapis.com/AssetSetAsset'
    _globals['_ASSETSETASSET'].fields_by_name['asset_set']._loaded_options = None
    _globals['_ASSETSETASSET'].fields_by_name['asset_set']._serialized_options = b'\xe0A\x05\xfaA&\n$searchads360.googleapis.com/AssetSet'
    _globals['_ASSETSETASSET'].fields_by_name['asset']._loaded_options = None
    _globals['_ASSETSETASSET'].fields_by_name['asset']._serialized_options = b'\xe0A\x05\xfaA#\n!searchads360.googleapis.com/Asset'
    _globals['_ASSETSETASSET'].fields_by_name['status']._loaded_options = None
    _globals['_ASSETSETASSET'].fields_by_name['status']._serialized_options = b'\xe0A\x03'
    _globals['_ASSETSETASSET']._loaded_options = None
    _globals['_ASSETSETASSET']._serialized_options = b'\xeaAm\n)searchads360.googleapis.com/AssetSetAsset\x12@customers/{customer_id}/assetSetAssets/{asset_set_id}~{asset_id}'
    _globals['_ASSETSETASSET']._serialized_start = 224
    _globals['_ASSETSETASSET']._serialized_end = 650