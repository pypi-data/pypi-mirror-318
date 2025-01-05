"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ads/googleads/v18/resources/call_view.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v18.enums import call_tracking_display_location_pb2 as google_dot_ads_dot_googleads_dot_v18_dot_enums_dot_call__tracking__display__location__pb2
from ......google.ads.googleads.v18.enums import call_type_pb2 as google_dot_ads_dot_googleads_dot_v18_dot_enums_dot_call__type__pb2
from ......google.ads.googleads.v18.enums import google_voice_call_status_pb2 as google_dot_ads_dot_googleads_dot_v18_dot_enums_dot_google__voice__call__status__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2google/ads/googleads/v18/resources/call_view.proto\x12"google.ads.googleads.v18.resources\x1aCgoogle/ads/googleads/v18/enums/call_tracking_display_location.proto\x1a.google/ads/googleads/v18/enums/call_type.proto\x1a=google/ads/googleads/v18/enums/google_voice_call_status.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\x91\x05\n\x08CallView\x12@\n\rresource_name\x18\x01 \x01(\tB)\xe0A\x03\xfaA#\n!googleads.googleapis.com/CallView\x12 \n\x13caller_country_code\x18\x02 \x01(\tB\x03\xe0A\x03\x12\x1d\n\x10caller_area_code\x18\x03 \x01(\tB\x03\xe0A\x03\x12"\n\x15call_duration_seconds\x18\x04 \x01(\x03B\x03\xe0A\x03\x12!\n\x14start_call_date_time\x18\x05 \x01(\tB\x03\xe0A\x03\x12\x1f\n\x12end_call_date_time\x18\x06 \x01(\tB\x03\xe0A\x03\x12\x88\x01\n\x1ecall_tracking_display_location\x18\x07 \x01(\x0e2[.google.ads.googleads.v18.enums.CallTrackingDisplayLocationEnum.CallTrackingDisplayLocationB\x03\xe0A\x03\x12H\n\x04type\x18\x08 \x01(\x0e25.google.ads.googleads.v18.enums.CallTypeEnum.CallTypeB\x03\xe0A\x03\x12i\n\x0bcall_status\x18\t \x01(\x0e2O.google.ads.googleads.v18.enums.GoogleVoiceCallStatusEnum.GoogleVoiceCallStatusB\x03\xe0A\x03:Z\xeaAW\n!googleads.googleapis.com/CallView\x122customers/{customer_id}/callViews/{call_detail_id}B\xff\x01\n&com.google.ads.googleads.v18.resourcesB\rCallViewProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v18/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V18.Resources\xca\x02"Google\\Ads\\GoogleAds\\V18\\Resources\xea\x02&Google::Ads::GoogleAds::V18::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v18.resources.call_view_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v18.resourcesB\rCallViewProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v18/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V18.Resources\xca\x02"Google\\Ads\\GoogleAds\\V18\\Resources\xea\x02&Google::Ads::GoogleAds::V18::Resources'
    _globals['_CALLVIEW'].fields_by_name['resource_name']._loaded_options = None
    _globals['_CALLVIEW'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x03\xfaA#\n!googleads.googleapis.com/CallView'
    _globals['_CALLVIEW'].fields_by_name['caller_country_code']._loaded_options = None
    _globals['_CALLVIEW'].fields_by_name['caller_country_code']._serialized_options = b'\xe0A\x03'
    _globals['_CALLVIEW'].fields_by_name['caller_area_code']._loaded_options = None
    _globals['_CALLVIEW'].fields_by_name['caller_area_code']._serialized_options = b'\xe0A\x03'
    _globals['_CALLVIEW'].fields_by_name['call_duration_seconds']._loaded_options = None
    _globals['_CALLVIEW'].fields_by_name['call_duration_seconds']._serialized_options = b'\xe0A\x03'
    _globals['_CALLVIEW'].fields_by_name['start_call_date_time']._loaded_options = None
    _globals['_CALLVIEW'].fields_by_name['start_call_date_time']._serialized_options = b'\xe0A\x03'
    _globals['_CALLVIEW'].fields_by_name['end_call_date_time']._loaded_options = None
    _globals['_CALLVIEW'].fields_by_name['end_call_date_time']._serialized_options = b'\xe0A\x03'
    _globals['_CALLVIEW'].fields_by_name['call_tracking_display_location']._loaded_options = None
    _globals['_CALLVIEW'].fields_by_name['call_tracking_display_location']._serialized_options = b'\xe0A\x03'
    _globals['_CALLVIEW'].fields_by_name['type']._loaded_options = None
    _globals['_CALLVIEW'].fields_by_name['type']._serialized_options = b'\xe0A\x03'
    _globals['_CALLVIEW'].fields_by_name['call_status']._loaded_options = None
    _globals['_CALLVIEW'].fields_by_name['call_status']._serialized_options = b'\xe0A\x03'
    _globals['_CALLVIEW']._loaded_options = None
    _globals['_CALLVIEW']._serialized_options = b'\xeaAW\n!googleads.googleapis.com/CallView\x122customers/{customer_id}/callViews/{call_detail_id}'
    _globals['_CALLVIEW']._serialized_start = 331
    _globals['_CALLVIEW']._serialized_end = 988