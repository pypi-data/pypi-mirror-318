"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ads/searchads360/v0/resources/asset_group_asset.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.searchads360.v0.enums import asset_field_type_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_enums_dot_asset__field__type__pb2
from ......google.ads.searchads360.v0.enums import asset_link_status_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_enums_dot_asset__link__status__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n<google/ads/searchads360/v0/resources/asset_group_asset.proto\x12$google.ads.searchads360.v0.resources\x1a7google/ads/searchads360/v0/enums/asset_field_type.proto\x1a8google/ads/searchads360/v0/enums/asset_link_status.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\x93\x04\n\x0fAssetGroupAsset\x12J\n\rresource_name\x18\x01 \x01(\tB3\xe0A\x05\xfaA-\n+searchads360.googleapis.com/AssetGroupAsset\x12C\n\x0basset_group\x18\x02 \x01(\tB.\xe0A\x05\xfaA(\n&searchads360.googleapis.com/AssetGroup\x128\n\x05asset\x18\x03 \x01(\tB)\xe0A\x05\xfaA#\n!searchads360.googleapis.com/Asset\x12W\n\nfield_type\x18\x04 \x01(\x0e2C.google.ads.searchads360.v0.enums.AssetFieldTypeEnum.AssetFieldType\x12U\n\x06status\x18\x05 \x01(\x0e2E.google.ads.searchads360.v0.enums.AssetLinkStatusEnum.AssetLinkStatus:\x84\x01\xeaA\x80\x01\n+searchads360.googleapis.com/AssetGroupAsset\x12Qcustomers/{customer_id}/assetGroupAssets/{asset_group_id}~{asset_id}~{field_type}B\x94\x02\n(com.google.ads.searchads360.v0.resourcesB\x14AssetGroupAssetProtoP\x01ZMgoogle.golang.org/genproto/googleapis/ads/searchads360/v0/resources;resources\xa2\x02\x07GASA360\xaa\x02$Google.Ads.SearchAds360.V0.Resources\xca\x02$Google\\Ads\\SearchAds360\\V0\\Resources\xea\x02(Google::Ads::SearchAds360::V0::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.searchads360.v0.resources.asset_group_asset_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n(com.google.ads.searchads360.v0.resourcesB\x14AssetGroupAssetProtoP\x01ZMgoogle.golang.org/genproto/googleapis/ads/searchads360/v0/resources;resources\xa2\x02\x07GASA360\xaa\x02$Google.Ads.SearchAds360.V0.Resources\xca\x02$Google\\Ads\\SearchAds360\\V0\\Resources\xea\x02(Google::Ads::SearchAds360::V0::Resources'
    _globals['_ASSETGROUPASSET'].fields_by_name['resource_name']._loaded_options = None
    _globals['_ASSETGROUPASSET'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x05\xfaA-\n+searchads360.googleapis.com/AssetGroupAsset'
    _globals['_ASSETGROUPASSET'].fields_by_name['asset_group']._loaded_options = None
    _globals['_ASSETGROUPASSET'].fields_by_name['asset_group']._serialized_options = b'\xe0A\x05\xfaA(\n&searchads360.googleapis.com/AssetGroup'
    _globals['_ASSETGROUPASSET'].fields_by_name['asset']._loaded_options = None
    _globals['_ASSETGROUPASSET'].fields_by_name['asset']._serialized_options = b'\xe0A\x05\xfaA#\n!searchads360.googleapis.com/Asset'
    _globals['_ASSETGROUPASSET']._loaded_options = None
    _globals['_ASSETGROUPASSET']._serialized_options = b'\xeaA\x80\x01\n+searchads360.googleapis.com/AssetGroupAsset\x12Qcustomers/{customer_id}/assetGroupAssets/{asset_group_id}~{asset_id}~{field_type}'
    _globals['_ASSETGROUPASSET']._serialized_start = 278
    _globals['_ASSETGROUPASSET']._serialized_end = 809