"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ads/googleads/v17/resources/feed_placeholder_view.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v17.enums import placeholder_type_pb2 as google_dot_ads_dot_googleads_dot_v17_dot_enums_dot_placeholder__type__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n>google/ads/googleads/v17/resources/feed_placeholder_view.proto\x12"google.ads.googleads.v17.resources\x1a5google/ads/googleads/v17/enums/placeholder_type.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xba\x02\n\x13FeedPlaceholderView\x12K\n\rresource_name\x18\x01 \x01(\tB4\xe0A\x03\xfaA.\n,googleads.googleapis.com/FeedPlaceholderView\x12b\n\x10placeholder_type\x18\x02 \x01(\x0e2C.google.ads.googleads.v17.enums.PlaceholderTypeEnum.PlaceholderTypeB\x03\xe0A\x03:r\xeaAo\n,googleads.googleapis.com/FeedPlaceholderView\x12?customers/{customer_id}/feedPlaceholderViews/{placeholder_type}B\x8a\x02\n&com.google.ads.googleads.v17.resourcesB\x18FeedPlaceholderViewProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v17/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V17.Resources\xca\x02"Google\\Ads\\GoogleAds\\V17\\Resources\xea\x02&Google::Ads::GoogleAds::V17::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v17.resources.feed_placeholder_view_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v17.resourcesB\x18FeedPlaceholderViewProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v17/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V17.Resources\xca\x02"Google\\Ads\\GoogleAds\\V17\\Resources\xea\x02&Google::Ads::GoogleAds::V17::Resources'
    _globals['_FEEDPLACEHOLDERVIEW'].fields_by_name['resource_name']._loaded_options = None
    _globals['_FEEDPLACEHOLDERVIEW'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x03\xfaA.\n,googleads.googleapis.com/FeedPlaceholderView'
    _globals['_FEEDPLACEHOLDERVIEW'].fields_by_name['placeholder_type']._loaded_options = None
    _globals['_FEEDPLACEHOLDERVIEW'].fields_by_name['placeholder_type']._serialized_options = b'\xe0A\x03'
    _globals['_FEEDPLACEHOLDERVIEW']._loaded_options = None
    _globals['_FEEDPLACEHOLDERVIEW']._serialized_options = b'\xeaAo\n,googleads.googleapis.com/FeedPlaceholderView\x12?customers/{customer_id}/feedPlaceholderViews/{placeholder_type}'
    _globals['_FEEDPLACEHOLDERVIEW']._serialized_start = 218
    _globals['_FEEDPLACEHOLDERVIEW']._serialized_end = 532