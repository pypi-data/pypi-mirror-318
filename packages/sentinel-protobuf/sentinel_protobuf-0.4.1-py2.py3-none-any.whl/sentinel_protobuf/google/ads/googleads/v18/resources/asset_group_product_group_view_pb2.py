"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ads/googleads/v18/resources/asset_group_product_group_view.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nGgoogle/ads/googleads/v18/resources/asset_group_product_group_view.proto\x12"google.ads.googleads.v18.resources\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xb7\x03\n\x1aAssetGroupProductGroupView\x12R\n\rresource_name\x18\x01 \x01(\tB;\xe0A\x03\xfaA5\n3googleads.googleapis.com/AssetGroupProductGroupView\x12@\n\x0basset_group\x18\x02 \x01(\tB+\xe0A\x03\xfaA%\n#googleads.googleapis.com/AssetGroup\x12g\n asset_group_listing_group_filter\x18\x04 \x01(\tB=\xe0A\x03\xfaA7\n5googleads.googleapis.com/AssetGroupListingGroupFilter:\x99\x01\xeaA\x95\x01\n3googleads.googleapis.com/AssetGroupProductGroupView\x12^customers/{customer_id}/assetGroupProductGroupViews/{asset_group_id}~{listing_group_filter_id}B\x91\x02\n&com.google.ads.googleads.v18.resourcesB\x1fAssetGroupProductGroupViewProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v18/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V18.Resources\xca\x02"Google\\Ads\\GoogleAds\\V18\\Resources\xea\x02&Google::Ads::GoogleAds::V18::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v18.resources.asset_group_product_group_view_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v18.resourcesB\x1fAssetGroupProductGroupViewProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v18/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V18.Resources\xca\x02"Google\\Ads\\GoogleAds\\V18\\Resources\xea\x02&Google::Ads::GoogleAds::V18::Resources'
    _globals['_ASSETGROUPPRODUCTGROUPVIEW'].fields_by_name['resource_name']._loaded_options = None
    _globals['_ASSETGROUPPRODUCTGROUPVIEW'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x03\xfaA5\n3googleads.googleapis.com/AssetGroupProductGroupView'
    _globals['_ASSETGROUPPRODUCTGROUPVIEW'].fields_by_name['asset_group']._loaded_options = None
    _globals['_ASSETGROUPPRODUCTGROUPVIEW'].fields_by_name['asset_group']._serialized_options = b'\xe0A\x03\xfaA%\n#googleads.googleapis.com/AssetGroup'
    _globals['_ASSETGROUPPRODUCTGROUPVIEW'].fields_by_name['asset_group_listing_group_filter']._loaded_options = None
    _globals['_ASSETGROUPPRODUCTGROUPVIEW'].fields_by_name['asset_group_listing_group_filter']._serialized_options = b'\xe0A\x03\xfaA7\n5googleads.googleapis.com/AssetGroupListingGroupFilter'
    _globals['_ASSETGROUPPRODUCTGROUPVIEW']._loaded_options = None
    _globals['_ASSETGROUPPRODUCTGROUPVIEW']._serialized_options = b'\xeaA\x95\x01\n3googleads.googleapis.com/AssetGroupProductGroupView\x12^customers/{customer_id}/assetGroupProductGroupViews/{asset_group_id}~{listing_group_filter_id}'
    _globals['_ASSETGROUPPRODUCTGROUPVIEW']._serialized_start = 172
    _globals['_ASSETGROUPPRODUCTGROUPVIEW']._serialized_end = 611