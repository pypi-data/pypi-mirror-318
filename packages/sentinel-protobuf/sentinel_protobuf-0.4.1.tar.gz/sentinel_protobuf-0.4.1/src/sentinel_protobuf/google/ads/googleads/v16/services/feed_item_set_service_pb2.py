"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ads/googleads/v16/services/feed_item_set_service.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v16.resources import feed_item_set_pb2 as google_dot_ads_dot_googleads_dot_v16_dot_resources_dot_feed__item__set__pb2
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from ......google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n=google/ads/googleads/v16/services/feed_item_set_service.proto\x12!google.ads.googleads.v16.services\x1a6google/ads/googleads/v16/resources/feed_item_set.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto\x1a\x17google/rpc/status.proto"\xb7\x01\n\x19MutateFeedItemSetsRequest\x12\x18\n\x0bcustomer_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12P\n\noperations\x18\x02 \x03(\x0b27.google.ads.googleads.v16.services.FeedItemSetOperationB\x03\xe0A\x02\x12\x17\n\x0fpartial_failure\x18\x03 \x01(\x08\x12\x15\n\rvalidate_only\x18\x04 \x01(\x08"\x97\x02\n\x14FeedItemSetOperation\x12/\n\x0bupdate_mask\x18\x04 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12A\n\x06create\x18\x01 \x01(\x0b2/.google.ads.googleads.v16.resources.FeedItemSetH\x00\x12A\n\x06update\x18\x02 \x01(\x0b2/.google.ads.googleads.v16.resources.FeedItemSetH\x00\x12;\n\x06remove\x18\x03 \x01(\tB)\xfaA&\n$googleads.googleapis.com/FeedItemSetH\x00B\x0b\n\toperation"\x9c\x01\n\x1aMutateFeedItemSetsResponse\x12K\n\x07results\x18\x01 \x03(\x0b2:.google.ads.googleads.v16.services.MutateFeedItemSetResult\x121\n\x15partial_failure_error\x18\x02 \x01(\x0b2\x12.google.rpc.Status"[\n\x17MutateFeedItemSetResult\x12@\n\rresource_name\x18\x01 \x01(\tB)\xfaA&\n$googleads.googleapis.com/FeedItemSet2\xc7\x02\n\x12FeedItemSetService\x12\xe9\x01\n\x12MutateFeedItemSets\x12<.google.ads.googleads.v16.services.MutateFeedItemSetsRequest\x1a=.google.ads.googleads.v16.services.MutateFeedItemSetsResponse"V\xdaA\x16customer_id,operations\x82\xd3\xe4\x93\x027"2/v16/customers/{customer_id=*}/feedItemSets:mutate:\x01*\x1aE\xcaA\x18googleads.googleapis.com\xd2A\'https://www.googleapis.com/auth/adwordsB\x83\x02\n%com.google.ads.googleads.v16.servicesB\x17FeedItemSetServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v16/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V16.Services\xca\x02!Google\\Ads\\GoogleAds\\V16\\Services\xea\x02%Google::Ads::GoogleAds::V16::Servicesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v16.services.feed_item_set_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.ads.googleads.v16.servicesB\x17FeedItemSetServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v16/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V16.Services\xca\x02!Google\\Ads\\GoogleAds\\V16\\Services\xea\x02%Google::Ads::GoogleAds::V16::Services'
    _globals['_MUTATEFEEDITEMSETSREQUEST'].fields_by_name['customer_id']._loaded_options = None
    _globals['_MUTATEFEEDITEMSETSREQUEST'].fields_by_name['customer_id']._serialized_options = b'\xe0A\x02'
    _globals['_MUTATEFEEDITEMSETSREQUEST'].fields_by_name['operations']._loaded_options = None
    _globals['_MUTATEFEEDITEMSETSREQUEST'].fields_by_name['operations']._serialized_options = b'\xe0A\x02'
    _globals['_FEEDITEMSETOPERATION'].fields_by_name['remove']._loaded_options = None
    _globals['_FEEDITEMSETOPERATION'].fields_by_name['remove']._serialized_options = b'\xfaA&\n$googleads.googleapis.com/FeedItemSet'
    _globals['_MUTATEFEEDITEMSETRESULT'].fields_by_name['resource_name']._loaded_options = None
    _globals['_MUTATEFEEDITEMSETRESULT'].fields_by_name['resource_name']._serialized_options = b'\xfaA&\n$googleads.googleapis.com/FeedItemSet'
    _globals['_FEEDITEMSETSERVICE']._loaded_options = None
    _globals['_FEEDITEMSETSERVICE']._serialized_options = b"\xcaA\x18googleads.googleapis.com\xd2A'https://www.googleapis.com/auth/adwords"
    _globals['_FEEDITEMSETSERVICE'].methods_by_name['MutateFeedItemSets']._loaded_options = None
    _globals['_FEEDITEMSETSERVICE'].methods_by_name['MutateFeedItemSets']._serialized_options = b'\xdaA\x16customer_id,operations\x82\xd3\xe4\x93\x027"2/v16/customers/{customer_id=*}/feedItemSets:mutate:\x01*'
    _globals['_MUTATEFEEDITEMSETSREQUEST']._serialized_start = 331
    _globals['_MUTATEFEEDITEMSETSREQUEST']._serialized_end = 514
    _globals['_FEEDITEMSETOPERATION']._serialized_start = 517
    _globals['_FEEDITEMSETOPERATION']._serialized_end = 796
    _globals['_MUTATEFEEDITEMSETSRESPONSE']._serialized_start = 799
    _globals['_MUTATEFEEDITEMSETSRESPONSE']._serialized_end = 955
    _globals['_MUTATEFEEDITEMSETRESULT']._serialized_start = 957
    _globals['_MUTATEFEEDITEMSETRESULT']._serialized_end = 1048
    _globals['_FEEDITEMSETSERVICE']._serialized_start = 1051
    _globals['_FEEDITEMSETSERVICE']._serialized_end = 1378