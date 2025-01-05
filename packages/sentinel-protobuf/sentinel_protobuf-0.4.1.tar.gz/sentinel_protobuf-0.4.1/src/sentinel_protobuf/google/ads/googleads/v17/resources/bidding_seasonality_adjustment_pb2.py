"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ads/googleads/v17/resources/bidding_seasonality_adjustment.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v17.enums import advertising_channel_type_pb2 as google_dot_ads_dot_googleads_dot_v17_dot_enums_dot_advertising__channel__type__pb2
from ......google.ads.googleads.v17.enums import device_pb2 as google_dot_ads_dot_googleads_dot_v17_dot_enums_dot_device__pb2
from ......google.ads.googleads.v17.enums import seasonality_event_scope_pb2 as google_dot_ads_dot_googleads_dot_v17_dot_enums_dot_seasonality__event__scope__pb2
from ......google.ads.googleads.v17.enums import seasonality_event_status_pb2 as google_dot_ads_dot_googleads_dot_v17_dot_enums_dot_seasonality__event__status__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nGgoogle/ads/googleads/v17/resources/bidding_seasonality_adjustment.proto\x12"google.ads.googleads.v17.resources\x1a=google/ads/googleads/v17/enums/advertising_channel_type.proto\x1a+google/ads/googleads/v17/enums/device.proto\x1a<google/ads/googleads/v17/enums/seasonality_event_scope.proto\x1a=google/ads/googleads/v17/enums/seasonality_event_status.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xe4\x06\n\x1cBiddingSeasonalityAdjustment\x12T\n\rresource_name\x18\x01 \x01(\tB=\xe0A\x05\xfaA7\n5googleads.googleapis.com/BiddingSeasonalityAdjustment\x12&\n\x19seasonality_adjustment_id\x18\x02 \x01(\x03B\x03\xe0A\x03\x12^\n\x05scope\x18\x03 \x01(\x0e2O.google.ads.googleads.v17.enums.SeasonalityEventScopeEnum.SeasonalityEventScope\x12f\n\x06status\x18\x04 \x01(\x0e2Q.google.ads.googleads.v17.enums.SeasonalityEventStatusEnum.SeasonalityEventStatusB\x03\xe0A\x03\x12\x1c\n\x0fstart_date_time\x18\x05 \x01(\tB\x03\xe0A\x02\x12\x1a\n\rend_date_time\x18\x06 \x01(\tB\x03\xe0A\x02\x12\x0c\n\x04name\x18\x07 \x01(\t\x12\x13\n\x0bdescription\x18\x08 \x01(\t\x12B\n\x07devices\x18\t \x03(\x0e21.google.ads.googleads.v17.enums.DeviceEnum.Device\x12 \n\x18conversion_rate_modifier\x18\n \x01(\x01\x129\n\tcampaigns\x18\x0b \x03(\tB&\xfaA#\n!googleads.googleapis.com/Campaign\x12t\n\x19advertising_channel_types\x18\x0c \x03(\x0e2Q.google.ads.googleads.v17.enums.AdvertisingChannelTypeEnum.AdvertisingChannelType:\x89\x01\xeaA\x85\x01\n5googleads.googleapis.com/BiddingSeasonalityAdjustment\x12Lcustomers/{customer_id}/biddingSeasonalityAdjustments/{seasonality_event_id}B\x93\x02\n&com.google.ads.googleads.v17.resourcesB!BiddingSeasonalityAdjustmentProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v17/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V17.Resources\xca\x02"Google\\Ads\\GoogleAds\\V17\\Resources\xea\x02&Google::Ads::GoogleAds::V17::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v17.resources.bidding_seasonality_adjustment_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v17.resourcesB!BiddingSeasonalityAdjustmentProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v17/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V17.Resources\xca\x02"Google\\Ads\\GoogleAds\\V17\\Resources\xea\x02&Google::Ads::GoogleAds::V17::Resources'
    _globals['_BIDDINGSEASONALITYADJUSTMENT'].fields_by_name['resource_name']._loaded_options = None
    _globals['_BIDDINGSEASONALITYADJUSTMENT'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x05\xfaA7\n5googleads.googleapis.com/BiddingSeasonalityAdjustment'
    _globals['_BIDDINGSEASONALITYADJUSTMENT'].fields_by_name['seasonality_adjustment_id']._loaded_options = None
    _globals['_BIDDINGSEASONALITYADJUSTMENT'].fields_by_name['seasonality_adjustment_id']._serialized_options = b'\xe0A\x03'
    _globals['_BIDDINGSEASONALITYADJUSTMENT'].fields_by_name['status']._loaded_options = None
    _globals['_BIDDINGSEASONALITYADJUSTMENT'].fields_by_name['status']._serialized_options = b'\xe0A\x03'
    _globals['_BIDDINGSEASONALITYADJUSTMENT'].fields_by_name['start_date_time']._loaded_options = None
    _globals['_BIDDINGSEASONALITYADJUSTMENT'].fields_by_name['start_date_time']._serialized_options = b'\xe0A\x02'
    _globals['_BIDDINGSEASONALITYADJUSTMENT'].fields_by_name['end_date_time']._loaded_options = None
    _globals['_BIDDINGSEASONALITYADJUSTMENT'].fields_by_name['end_date_time']._serialized_options = b'\xe0A\x02'
    _globals['_BIDDINGSEASONALITYADJUSTMENT'].fields_by_name['campaigns']._loaded_options = None
    _globals['_BIDDINGSEASONALITYADJUSTMENT'].fields_by_name['campaigns']._serialized_options = b'\xfaA#\n!googleads.googleapis.com/Campaign'
    _globals['_BIDDINGSEASONALITYADJUSTMENT']._loaded_options = None
    _globals['_BIDDINGSEASONALITYADJUSTMENT']._serialized_options = b'\xeaA\x85\x01\n5googleads.googleapis.com/BiddingSeasonalityAdjustment\x12Lcustomers/{customer_id}/biddingSeasonalityAdjustments/{seasonality_event_id}'
    _globals['_BIDDINGSEASONALITYADJUSTMENT']._serialized_start = 405
    _globals['_BIDDINGSEASONALITYADJUSTMENT']._serialized_end = 1273