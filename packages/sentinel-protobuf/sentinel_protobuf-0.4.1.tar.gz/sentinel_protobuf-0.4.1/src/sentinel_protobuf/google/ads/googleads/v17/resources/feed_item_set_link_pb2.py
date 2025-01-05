"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ads/googleads/v17/resources/feed_item_set_link.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n;google/ads/googleads/v17/resources/feed_item_set_link.proto\x12"google.ads.googleads.v17.resources\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xe4\x02\n\x0fFeedItemSetLink\x12G\n\rresource_name\x18\x01 \x01(\tB0\xe0A\x05\xfaA*\n(googleads.googleapis.com/FeedItemSetLink\x12<\n\tfeed_item\x18\x02 \x01(\tB)\xe0A\x05\xfaA#\n!googleads.googleapis.com/FeedItem\x12C\n\rfeed_item_set\x18\x03 \x01(\tB,\xe0A\x05\xfaA&\n$googleads.googleapis.com/FeedItemSet:\x84\x01\xeaA\x80\x01\n(googleads.googleapis.com/FeedItemSetLink\x12Tcustomers/{customer_id}/feedItemSetLinks/{feed_id}~{feed_item_set_id}~{feed_item_id}B\x86\x02\n&com.google.ads.googleads.v17.resourcesB\x14FeedItemSetLinkProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v17/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V17.Resources\xca\x02"Google\\Ads\\GoogleAds\\V17\\Resources\xea\x02&Google::Ads::GoogleAds::V17::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v17.resources.feed_item_set_link_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v17.resourcesB\x14FeedItemSetLinkProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v17/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V17.Resources\xca\x02"Google\\Ads\\GoogleAds\\V17\\Resources\xea\x02&Google::Ads::GoogleAds::V17::Resources'
    _globals['_FEEDITEMSETLINK'].fields_by_name['resource_name']._loaded_options = None
    _globals['_FEEDITEMSETLINK'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x05\xfaA*\n(googleads.googleapis.com/FeedItemSetLink'
    _globals['_FEEDITEMSETLINK'].fields_by_name['feed_item']._loaded_options = None
    _globals['_FEEDITEMSETLINK'].fields_by_name['feed_item']._serialized_options = b'\xe0A\x05\xfaA#\n!googleads.googleapis.com/FeedItem'
    _globals['_FEEDITEMSETLINK'].fields_by_name['feed_item_set']._loaded_options = None
    _globals['_FEEDITEMSETLINK'].fields_by_name['feed_item_set']._serialized_options = b'\xe0A\x05\xfaA&\n$googleads.googleapis.com/FeedItemSet'
    _globals['_FEEDITEMSETLINK']._loaded_options = None
    _globals['_FEEDITEMSETLINK']._serialized_options = b'\xeaA\x80\x01\n(googleads.googleapis.com/FeedItemSetLink\x12Tcustomers/{customer_id}/feedItemSetLinks/{feed_id}~{feed_item_set_id}~{feed_item_id}'
    _globals['_FEEDITEMSETLINK']._serialized_start = 160
    _globals['_FEEDITEMSETLINK']._serialized_end = 516