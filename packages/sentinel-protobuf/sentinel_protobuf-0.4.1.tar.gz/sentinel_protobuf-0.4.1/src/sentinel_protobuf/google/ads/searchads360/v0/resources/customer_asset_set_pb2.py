"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ads/searchads360/v0/resources/customer_asset_set.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.searchads360.v0.enums import asset_set_link_status_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_enums_dot_asset__set__link__status__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n=google/ads/searchads360/v0/resources/customer_asset_set.proto\x12$google.ads.searchads360.v0.resources\x1a<google/ads/searchads360/v0/enums/asset_set_link_status.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xaf\x03\n\x10CustomerAssetSet\x12K\n\rresource_name\x18\x01 \x01(\tB4\xe0A\x05\xfaA.\n,searchads360.googleapis.com/CustomerAssetSet\x12?\n\tasset_set\x18\x02 \x01(\tB,\xe0A\x05\xfaA&\n$searchads360.googleapis.com/AssetSet\x12>\n\x08customer\x18\x03 \x01(\tB,\xe0A\x05\xfaA&\n$searchads360.googleapis.com/Customer\x12`\n\x06status\x18\x04 \x01(\x0e2K.google.ads.searchads360.v0.enums.AssetSetLinkStatusEnum.AssetSetLinkStatusB\x03\xe0A\x03:k\xeaAh\n,searchads360.googleapis.com/CustomerAssetSet\x128customers/{customer_id}/customerAssetSets/{asset_set_id}B\x95\x02\n(com.google.ads.searchads360.v0.resourcesB\x15CustomerAssetSetProtoP\x01ZMgoogle.golang.org/genproto/googleapis/ads/searchads360/v0/resources;resources\xa2\x02\x07GASA360\xaa\x02$Google.Ads.SearchAds360.V0.Resources\xca\x02$Google\\Ads\\SearchAds360\\V0\\Resources\xea\x02(Google::Ads::SearchAds360::V0::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.searchads360.v0.resources.customer_asset_set_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n(com.google.ads.searchads360.v0.resourcesB\x15CustomerAssetSetProtoP\x01ZMgoogle.golang.org/genproto/googleapis/ads/searchads360/v0/resources;resources\xa2\x02\x07GASA360\xaa\x02$Google.Ads.SearchAds360.V0.Resources\xca\x02$Google\\Ads\\SearchAds360\\V0\\Resources\xea\x02(Google::Ads::SearchAds360::V0::Resources'
    _globals['_CUSTOMERASSETSET'].fields_by_name['resource_name']._loaded_options = None
    _globals['_CUSTOMERASSETSET'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x05\xfaA.\n,searchads360.googleapis.com/CustomerAssetSet'
    _globals['_CUSTOMERASSETSET'].fields_by_name['asset_set']._loaded_options = None
    _globals['_CUSTOMERASSETSET'].fields_by_name['asset_set']._serialized_options = b'\xe0A\x05\xfaA&\n$searchads360.googleapis.com/AssetSet'
    _globals['_CUSTOMERASSETSET'].fields_by_name['customer']._loaded_options = None
    _globals['_CUSTOMERASSETSET'].fields_by_name['customer']._serialized_options = b'\xe0A\x05\xfaA&\n$searchads360.googleapis.com/Customer'
    _globals['_CUSTOMERASSETSET'].fields_by_name['status']._loaded_options = None
    _globals['_CUSTOMERASSETSET'].fields_by_name['status']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMERASSETSET']._loaded_options = None
    _globals['_CUSTOMERASSETSET']._serialized_options = b'\xeaAh\n,searchads360.googleapis.com/CustomerAssetSet\x128customers/{customer_id}/customerAssetSets/{asset_set_id}'
    _globals['_CUSTOMERASSETSET']._serialized_start = 226
    _globals['_CUSTOMERASSETSET']._serialized_end = 657