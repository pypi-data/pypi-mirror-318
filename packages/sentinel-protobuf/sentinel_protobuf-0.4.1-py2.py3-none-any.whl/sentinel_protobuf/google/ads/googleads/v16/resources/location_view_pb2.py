"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ads/googleads/v16/resources/location_view.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6google/ads/googleads/v16/resources/location_view.proto\x12"google.ads.googleads.v16.resources\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xc4\x01\n\x0cLocationView\x12D\n\rresource_name\x18\x01 \x01(\tB-\xe0A\x03\xfaA\'\n%googleads.googleapis.com/LocationView:n\xeaAk\n%googleads.googleapis.com/LocationView\x12Bcustomers/{customer_id}/locationViews/{campaign_id}~{criterion_id}B\x83\x02\n&com.google.ads.googleads.v16.resourcesB\x11LocationViewProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v16/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V16.Resources\xca\x02"Google\\Ads\\GoogleAds\\V16\\Resources\xea\x02&Google::Ads::GoogleAds::V16::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v16.resources.location_view_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v16.resourcesB\x11LocationViewProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v16/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V16.Resources\xca\x02"Google\\Ads\\GoogleAds\\V16\\Resources\xea\x02&Google::Ads::GoogleAds::V16::Resources'
    _globals['_LOCATIONVIEW'].fields_by_name['resource_name']._loaded_options = None
    _globals['_LOCATIONVIEW'].fields_by_name['resource_name']._serialized_options = b"\xe0A\x03\xfaA'\n%googleads.googleapis.com/LocationView"
    _globals['_LOCATIONVIEW']._loaded_options = None
    _globals['_LOCATIONVIEW']._serialized_options = b'\xeaAk\n%googleads.googleapis.com/LocationView\x12Bcustomers/{customer_id}/locationViews/{campaign_id}~{criterion_id}'
    _globals['_LOCATIONVIEW']._serialized_start = 155
    _globals['_LOCATIONVIEW']._serialized_end = 351