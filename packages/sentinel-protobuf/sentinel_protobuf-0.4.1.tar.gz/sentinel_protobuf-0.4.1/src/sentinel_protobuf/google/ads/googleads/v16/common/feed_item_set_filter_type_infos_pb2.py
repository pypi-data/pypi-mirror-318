"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ads/googleads/v16/common/feed_item_set_filter_type_infos.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v16.enums import feed_item_set_string_filter_type_pb2 as google_dot_ads_dot_googleads_dot_v16_dot_enums_dot_feed__item__set__string__filter__type__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nEgoogle/ads/googleads/v16/common/feed_item_set_filter_type_infos.proto\x12\x1fgoogle.ads.googleads.v16.common\x1aEgoogle/ads/googleads/v16/enums/feed_item_set_string_filter_type.proto"}\n\x18DynamicLocationSetFilter\x12\x0e\n\x06labels\x18\x01 \x03(\t\x12Q\n\x14business_name_filter\x18\x02 \x01(\x0b23.google.ads.googleads.v16.common.BusinessNameFilter"\x9d\x01\n\x12BusinessNameFilter\x12\x15\n\rbusiness_name\x18\x01 \x01(\t\x12p\n\x0bfilter_type\x18\x02 \x01(\x0e2[.google.ads.googleads.v16.enums.FeedItemSetStringFilterTypeEnum.FeedItemSetStringFilterType"6\n!DynamicAffiliateLocationSetFilter\x12\x11\n\tchain_ids\x18\x01 \x03(\x03B\xff\x01\n#com.google.ads.googleads.v16.commonB\x1fFeedItemSetFilterTypeInfosProtoP\x01ZEgoogle.golang.org/genproto/googleapis/ads/googleads/v16/common;common\xa2\x02\x03GAA\xaa\x02\x1fGoogle.Ads.GoogleAds.V16.Common\xca\x02\x1fGoogle\\Ads\\GoogleAds\\V16\\Common\xea\x02#Google::Ads::GoogleAds::V16::Commonb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v16.common.feed_item_set_filter_type_infos_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.ads.googleads.v16.commonB\x1fFeedItemSetFilterTypeInfosProtoP\x01ZEgoogle.golang.org/genproto/googleapis/ads/googleads/v16/common;common\xa2\x02\x03GAA\xaa\x02\x1fGoogle.Ads.GoogleAds.V16.Common\xca\x02\x1fGoogle\\Ads\\GoogleAds\\V16\\Common\xea\x02#Google::Ads::GoogleAds::V16::Common'
    _globals['_DYNAMICLOCATIONSETFILTER']._serialized_start = 177
    _globals['_DYNAMICLOCATIONSETFILTER']._serialized_end = 302
    _globals['_BUSINESSNAMEFILTER']._serialized_start = 305
    _globals['_BUSINESSNAMEFILTER']._serialized_end = 462
    _globals['_DYNAMICAFFILIATELOCATIONSETFILTER']._serialized_start = 464
    _globals['_DYNAMICAFFILIATELOCATIONSETFILTER']._serialized_end = 518