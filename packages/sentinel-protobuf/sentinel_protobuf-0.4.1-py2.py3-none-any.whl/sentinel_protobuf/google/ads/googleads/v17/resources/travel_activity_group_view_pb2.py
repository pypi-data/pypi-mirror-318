"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ads/googleads/v17/resources/travel_activity_group_view.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nCgoogle/ads/googleads/v17/resources/travel_activity_group_view.proto\x12"google.ads.googleads.v17.resources\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xf2\x01\n\x17TravelActivityGroupView\x12O\n\rresource_name\x18\x01 \x01(\tB8\xe0A\x03\xfaA2\n0googleads.googleapis.com/TravelActivityGroupView:\x85\x01\xeaA\x81\x01\n0googleads.googleapis.com/TravelActivityGroupView\x12Mcustomers/{customer_id}/travelActivityGroupViews/{ad_group_id}~{criterion_id}B\x8e\x02\n&com.google.ads.googleads.v17.resourcesB\x1cTravelActivityGroupViewProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v17/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V17.Resources\xca\x02"Google\\Ads\\GoogleAds\\V17\\Resources\xea\x02&Google::Ads::GoogleAds::V17::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v17.resources.travel_activity_group_view_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v17.resourcesB\x1cTravelActivityGroupViewProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v17/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V17.Resources\xca\x02"Google\\Ads\\GoogleAds\\V17\\Resources\xea\x02&Google::Ads::GoogleAds::V17::Resources'
    _globals['_TRAVELACTIVITYGROUPVIEW'].fields_by_name['resource_name']._loaded_options = None
    _globals['_TRAVELACTIVITYGROUPVIEW'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x03\xfaA2\n0googleads.googleapis.com/TravelActivityGroupView'
    _globals['_TRAVELACTIVITYGROUPVIEW']._loaded_options = None
    _globals['_TRAVELACTIVITYGROUPVIEW']._serialized_options = b'\xeaA\x81\x01\n0googleads.googleapis.com/TravelActivityGroupView\x12Mcustomers/{customer_id}/travelActivityGroupViews/{ad_group_id}~{criterion_id}'
    _globals['_TRAVELACTIVITYGROUPVIEW']._serialized_start = 168
    _globals['_TRAVELACTIVITYGROUPVIEW']._serialized_end = 410