"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ads/googleads/v16/resources/asset_field_type_view.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v16.enums import asset_field_type_pb2 as google_dot_ads_dot_googleads_dot_v16_dot_enums_dot_asset__field__type__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n>google/ads/googleads/v16/resources/asset_field_type_view.proto\x12"google.ads.googleads.v16.resources\x1a5google/ads/googleads/v16/enums/asset_field_type.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xa8\x02\n\x12AssetFieldTypeView\x12J\n\rresource_name\x18\x01 \x01(\tB3\xe0A\x03\xfaA-\n+googleads.googleapis.com/AssetFieldTypeView\x12Z\n\nfield_type\x18\x03 \x01(\x0e2A.google.ads.googleads.v16.enums.AssetFieldTypeEnum.AssetFieldTypeB\x03\xe0A\x03:j\xeaAg\n+googleads.googleapis.com/AssetFieldTypeView\x128customers/{customer_id}/assetFieldTypeViews/{field_type}B\x89\x02\n&com.google.ads.googleads.v16.resourcesB\x17AssetFieldTypeViewProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v16/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V16.Resources\xca\x02"Google\\Ads\\GoogleAds\\V16\\Resources\xea\x02&Google::Ads::GoogleAds::V16::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v16.resources.asset_field_type_view_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v16.resourcesB\x17AssetFieldTypeViewProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v16/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V16.Resources\xca\x02"Google\\Ads\\GoogleAds\\V16\\Resources\xea\x02&Google::Ads::GoogleAds::V16::Resources'
    _globals['_ASSETFIELDTYPEVIEW'].fields_by_name['resource_name']._loaded_options = None
    _globals['_ASSETFIELDTYPEVIEW'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x03\xfaA-\n+googleads.googleapis.com/AssetFieldTypeView'
    _globals['_ASSETFIELDTYPEVIEW'].fields_by_name['field_type']._loaded_options = None
    _globals['_ASSETFIELDTYPEVIEW'].fields_by_name['field_type']._serialized_options = b'\xe0A\x03'
    _globals['_ASSETFIELDTYPEVIEW']._loaded_options = None
    _globals['_ASSETFIELDTYPEVIEW']._serialized_options = b'\xeaAg\n+googleads.googleapis.com/AssetFieldTypeView\x128customers/{customer_id}/assetFieldTypeViews/{field_type}'
    _globals['_ASSETFIELDTYPEVIEW']._serialized_start = 218
    _globals['_ASSETFIELDTYPEVIEW']._serialized_end = 514