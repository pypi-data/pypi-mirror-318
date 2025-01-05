"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ads/googleads/v17/resources/per_store_view.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7google/ads/googleads/v17/resources/per_store_view.proto\x12"google.ads.googleads.v17.resources\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xc9\x01\n\x0cPerStoreView\x12D\n\rresource_name\x18\x01 \x01(\tB-\xe0A\x03\xfaA\'\n%googleads.googleapis.com/PerStoreView\x12\x15\n\x08place_id\x18\x02 \x01(\tB\x03\xe0A\x03:\\\xeaAY\n%googleads.googleapis.com/PerStoreView\x120customers/{customer_id}/perStoreViews/{place_id}B\x83\x02\n&com.google.ads.googleads.v17.resourcesB\x11PerStoreViewProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v17/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V17.Resources\xca\x02"Google\\Ads\\GoogleAds\\V17\\Resources\xea\x02&Google::Ads::GoogleAds::V17::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v17.resources.per_store_view_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v17.resourcesB\x11PerStoreViewProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v17/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V17.Resources\xca\x02"Google\\Ads\\GoogleAds\\V17\\Resources\xea\x02&Google::Ads::GoogleAds::V17::Resources'
    _globals['_PERSTOREVIEW'].fields_by_name['resource_name']._loaded_options = None
    _globals['_PERSTOREVIEW'].fields_by_name['resource_name']._serialized_options = b"\xe0A\x03\xfaA'\n%googleads.googleapis.com/PerStoreView"
    _globals['_PERSTOREVIEW'].fields_by_name['place_id']._loaded_options = None
    _globals['_PERSTOREVIEW'].fields_by_name['place_id']._serialized_options = b'\xe0A\x03'
    _globals['_PERSTOREVIEW']._loaded_options = None
    _globals['_PERSTOREVIEW']._serialized_options = b'\xeaAY\n%googleads.googleapis.com/PerStoreView\x120customers/{customer_id}/perStoreViews/{place_id}'
    _globals['_PERSTOREVIEW']._serialized_start = 156
    _globals['_PERSTOREVIEW']._serialized_end = 357