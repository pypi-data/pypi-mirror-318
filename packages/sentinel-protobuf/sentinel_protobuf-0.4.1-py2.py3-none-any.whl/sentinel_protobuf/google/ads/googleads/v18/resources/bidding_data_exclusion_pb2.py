"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ads/googleads/v18/resources/bidding_data_exclusion.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v18.enums import advertising_channel_type_pb2 as google_dot_ads_dot_googleads_dot_v18_dot_enums_dot_advertising__channel__type__pb2
from ......google.ads.googleads.v18.enums import device_pb2 as google_dot_ads_dot_googleads_dot_v18_dot_enums_dot_device__pb2
from ......google.ads.googleads.v18.enums import seasonality_event_scope_pb2 as google_dot_ads_dot_googleads_dot_v18_dot_enums_dot_seasonality__event__scope__pb2
from ......google.ads.googleads.v18.enums import seasonality_event_status_pb2 as google_dot_ads_dot_googleads_dot_v18_dot_enums_dot_seasonality__event__status__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n?google/ads/googleads/v18/resources/bidding_data_exclusion.proto\x12"google.ads.googleads.v18.resources\x1a=google/ads/googleads/v18/enums/advertising_channel_type.proto\x1a+google/ads/googleads/v18/enums/device.proto\x1a<google/ads/googleads/v18/enums/seasonality_event_scope.proto\x1a=google/ads/googleads/v18/enums/seasonality_event_status.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\x98\x06\n\x14BiddingDataExclusion\x12L\n\rresource_name\x18\x01 \x01(\tB5\xe0A\x05\xfaA/\n-googleads.googleapis.com/BiddingDataExclusion\x12\x1e\n\x11data_exclusion_id\x18\x02 \x01(\x03B\x03\xe0A\x03\x12^\n\x05scope\x18\x03 \x01(\x0e2O.google.ads.googleads.v18.enums.SeasonalityEventScopeEnum.SeasonalityEventScope\x12f\n\x06status\x18\x04 \x01(\x0e2Q.google.ads.googleads.v18.enums.SeasonalityEventStatusEnum.SeasonalityEventStatusB\x03\xe0A\x03\x12\x1c\n\x0fstart_date_time\x18\x05 \x01(\tB\x03\xe0A\x02\x12\x1a\n\rend_date_time\x18\x06 \x01(\tB\x03\xe0A\x02\x12\x0c\n\x04name\x18\x07 \x01(\t\x12\x13\n\x0bdescription\x18\x08 \x01(\t\x12B\n\x07devices\x18\t \x03(\x0e21.google.ads.googleads.v18.enums.DeviceEnum.Device\x129\n\tcampaigns\x18\n \x03(\tB&\xfaA#\n!googleads.googleapis.com/Campaign\x12t\n\x19advertising_channel_types\x18\x0b \x03(\x0e2Q.google.ads.googleads.v18.enums.AdvertisingChannelTypeEnum.AdvertisingChannelType:x\xeaAu\n-googleads.googleapis.com/BiddingDataExclusion\x12Dcustomers/{customer_id}/biddingDataExclusions/{seasonality_event_id}B\x8b\x02\n&com.google.ads.googleads.v18.resourcesB\x19BiddingDataExclusionProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v18/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V18.Resources\xca\x02"Google\\Ads\\GoogleAds\\V18\\Resources\xea\x02&Google::Ads::GoogleAds::V18::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v18.resources.bidding_data_exclusion_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v18.resourcesB\x19BiddingDataExclusionProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v18/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V18.Resources\xca\x02"Google\\Ads\\GoogleAds\\V18\\Resources\xea\x02&Google::Ads::GoogleAds::V18::Resources'
    _globals['_BIDDINGDATAEXCLUSION'].fields_by_name['resource_name']._loaded_options = None
    _globals['_BIDDINGDATAEXCLUSION'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x05\xfaA/\n-googleads.googleapis.com/BiddingDataExclusion'
    _globals['_BIDDINGDATAEXCLUSION'].fields_by_name['data_exclusion_id']._loaded_options = None
    _globals['_BIDDINGDATAEXCLUSION'].fields_by_name['data_exclusion_id']._serialized_options = b'\xe0A\x03'
    _globals['_BIDDINGDATAEXCLUSION'].fields_by_name['status']._loaded_options = None
    _globals['_BIDDINGDATAEXCLUSION'].fields_by_name['status']._serialized_options = b'\xe0A\x03'
    _globals['_BIDDINGDATAEXCLUSION'].fields_by_name['start_date_time']._loaded_options = None
    _globals['_BIDDINGDATAEXCLUSION'].fields_by_name['start_date_time']._serialized_options = b'\xe0A\x02'
    _globals['_BIDDINGDATAEXCLUSION'].fields_by_name['end_date_time']._loaded_options = None
    _globals['_BIDDINGDATAEXCLUSION'].fields_by_name['end_date_time']._serialized_options = b'\xe0A\x02'
    _globals['_BIDDINGDATAEXCLUSION'].fields_by_name['campaigns']._loaded_options = None
    _globals['_BIDDINGDATAEXCLUSION'].fields_by_name['campaigns']._serialized_options = b'\xfaA#\n!googleads.googleapis.com/Campaign'
    _globals['_BIDDINGDATAEXCLUSION']._loaded_options = None
    _globals['_BIDDINGDATAEXCLUSION']._serialized_options = b'\xeaAu\n-googleads.googleapis.com/BiddingDataExclusion\x12Dcustomers/{customer_id}/biddingDataExclusions/{seasonality_event_id}'
    _globals['_BIDDINGDATAEXCLUSION']._serialized_start = 397
    _globals['_BIDDINGDATAEXCLUSION']._serialized_end = 1189