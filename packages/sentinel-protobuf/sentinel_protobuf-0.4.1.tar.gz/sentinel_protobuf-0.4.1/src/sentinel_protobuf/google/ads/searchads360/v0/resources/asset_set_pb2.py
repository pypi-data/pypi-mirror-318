"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ads/searchads360/v0/resources/asset_set.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4google/ads/searchads360/v0/resources/asset_set.proto\x12$google.ads.searchads360.v0.resources\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xbd\x01\n\x08AssetSet\x12\x0f\n\x02id\x18\x06 \x01(\x03B\x03\xe0A\x03\x12C\n\rresource_name\x18\x01 \x01(\tB,\xe0A\x05\xfaA&\n$searchads360.googleapis.com/AssetSet:[\xeaAX\n$searchads360.googleapis.com/AssetSet\x120customers/{customer_id}/assetSets/{asset_set_id}B\x8d\x02\n(com.google.ads.searchads360.v0.resourcesB\rAssetSetProtoP\x01ZMgoogle.golang.org/genproto/googleapis/ads/searchads360/v0/resources;resources\xa2\x02\x07GASA360\xaa\x02$Google.Ads.SearchAds360.V0.Resources\xca\x02$Google\\Ads\\SearchAds360\\V0\\Resources\xea\x02(Google::Ads::SearchAds360::V0::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.searchads360.v0.resources.asset_set_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n(com.google.ads.searchads360.v0.resourcesB\rAssetSetProtoP\x01ZMgoogle.golang.org/genproto/googleapis/ads/searchads360/v0/resources;resources\xa2\x02\x07GASA360\xaa\x02$Google.Ads.SearchAds360.V0.Resources\xca\x02$Google\\Ads\\SearchAds360\\V0\\Resources\xea\x02(Google::Ads::SearchAds360::V0::Resources'
    _globals['_ASSETSET'].fields_by_name['id']._loaded_options = None
    _globals['_ASSETSET'].fields_by_name['id']._serialized_options = b'\xe0A\x03'
    _globals['_ASSETSET'].fields_by_name['resource_name']._loaded_options = None
    _globals['_ASSETSET'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x05\xfaA&\n$searchads360.googleapis.com/AssetSet'
    _globals['_ASSETSET']._loaded_options = None
    _globals['_ASSETSET']._serialized_options = b'\xeaAX\n$searchads360.googleapis.com/AssetSet\x120customers/{customer_id}/assetSets/{asset_set_id}'
    _globals['_ASSETSET']._serialized_start = 155
    _globals['_ASSETSET']._serialized_end = 344