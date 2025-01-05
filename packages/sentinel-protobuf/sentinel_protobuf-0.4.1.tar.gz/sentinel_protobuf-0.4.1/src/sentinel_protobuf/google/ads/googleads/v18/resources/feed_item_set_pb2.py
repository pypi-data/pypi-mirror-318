"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ads/googleads/v18/resources/feed_item_set.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v18.common import feed_item_set_filter_type_infos_pb2 as google_dot_ads_dot_googleads_dot_v18_dot_common_dot_feed__item__set__filter__type__infos__pb2
from ......google.ads.googleads.v18.enums import feed_item_set_status_pb2 as google_dot_ads_dot_googleads_dot_v18_dot_enums_dot_feed__item__set__status__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6google/ads/googleads/v18/resources/feed_item_set.proto\x12"google.ads.googleads.v18.resources\x1aEgoogle/ads/googleads/v18/common/feed_item_set_filter_type_infos.proto\x1a9google/ads/googleads/v18/enums/feed_item_set_status.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xf5\x04\n\x0bFeedItemSet\x12C\n\rresource_name\x18\x01 \x01(\tB,\xe0A\x05\xfaA&\n$googleads.googleapis.com/FeedItemSet\x123\n\x04feed\x18\x02 \x01(\tB%\xe0A\x05\xfaA\x1f\n\x1dgoogleads.googleapis.com/Feed\x12\x1d\n\x10feed_item_set_id\x18\x03 \x01(\x03B\x03\xe0A\x03\x12\x14\n\x0cdisplay_name\x18\x04 \x01(\t\x12\\\n\x06status\x18\x08 \x01(\x0e2G.google.ads.googleads.v18.enums.FeedItemSetStatusEnum.FeedItemSetStatusB\x03\xe0A\x03\x12`\n\x1bdynamic_location_set_filter\x18\x05 \x01(\x0b29.google.ads.googleads.v18.common.DynamicLocationSetFilterH\x00\x12s\n%dynamic_affiliate_location_set_filter\x18\x06 \x01(\x0b2B.google.ads.googleads.v18.common.DynamicAffiliateLocationSetFilterH\x00:l\xeaAi\n$googleads.googleapis.com/FeedItemSet\x12Acustomers/{customer_id}/feedItemSets/{feed_id}~{feed_item_set_id}B\x14\n\x12dynamic_set_filterB\x82\x02\n&com.google.ads.googleads.v18.resourcesB\x10FeedItemSetProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v18/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V18.Resources\xca\x02"Google\\Ads\\GoogleAds\\V18\\Resources\xea\x02&Google::Ads::GoogleAds::V18::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v18.resources.feed_item_set_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v18.resourcesB\x10FeedItemSetProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v18/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V18.Resources\xca\x02"Google\\Ads\\GoogleAds\\V18\\Resources\xea\x02&Google::Ads::GoogleAds::V18::Resources'
    _globals['_FEEDITEMSET'].fields_by_name['resource_name']._loaded_options = None
    _globals['_FEEDITEMSET'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x05\xfaA&\n$googleads.googleapis.com/FeedItemSet'
    _globals['_FEEDITEMSET'].fields_by_name['feed']._loaded_options = None
    _globals['_FEEDITEMSET'].fields_by_name['feed']._serialized_options = b'\xe0A\x05\xfaA\x1f\n\x1dgoogleads.googleapis.com/Feed'
    _globals['_FEEDITEMSET'].fields_by_name['feed_item_set_id']._loaded_options = None
    _globals['_FEEDITEMSET'].fields_by_name['feed_item_set_id']._serialized_options = b'\xe0A\x03'
    _globals['_FEEDITEMSET'].fields_by_name['status']._loaded_options = None
    _globals['_FEEDITEMSET'].fields_by_name['status']._serialized_options = b'\xe0A\x03'
    _globals['_FEEDITEMSET']._loaded_options = None
    _globals['_FEEDITEMSET']._serialized_options = b'\xeaAi\n$googleads.googleapis.com/FeedItemSet\x12Acustomers/{customer_id}/feedItemSets/{feed_id}~{feed_item_set_id}'
    _globals['_FEEDITEMSET']._serialized_start = 285
    _globals['_FEEDITEMSET']._serialized_end = 914