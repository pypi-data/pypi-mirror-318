"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ads/googleads/v16/resources/custom_conversion_goal.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v16.enums import custom_conversion_goal_status_pb2 as google_dot_ads_dot_googleads_dot_v16_dot_enums_dot_custom__conversion__goal__status__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n?google/ads/googleads/v16/resources/custom_conversion_goal.proto\x12"google.ads.googleads.v16.resources\x1aBgoogle/ads/googleads/v16/enums/custom_conversion_goal_status.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xa7\x03\n\x14CustomConversionGoal\x12L\n\rresource_name\x18\x01 \x01(\tB5\xe0A\x05\xfaA/\n-googleads.googleapis.com/CustomConversionGoal\x12\x0f\n\x02id\x18\x02 \x01(\x03B\x03\xe0A\x05\x12\x0c\n\x04name\x18\x03 \x01(\t\x12J\n\x12conversion_actions\x18\x04 \x03(\tB.\xfaA+\n)googleads.googleapis.com/ConversionAction\x12i\n\x06status\x18\x05 \x01(\x0e2Y.google.ads.googleads.v16.enums.CustomConversionGoalStatusEnum.CustomConversionGoalStatus:k\xeaAh\n-googleads.googleapis.com/CustomConversionGoal\x127customers/{customer_id}/customConversionGoals/{goal_id}B\x8b\x02\n&com.google.ads.googleads.v16.resourcesB\x19CustomConversionGoalProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v16/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V16.Resources\xca\x02"Google\\Ads\\GoogleAds\\V16\\Resources\xea\x02&Google::Ads::GoogleAds::V16::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v16.resources.custom_conversion_goal_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v16.resourcesB\x19CustomConversionGoalProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v16/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V16.Resources\xca\x02"Google\\Ads\\GoogleAds\\V16\\Resources\xea\x02&Google::Ads::GoogleAds::V16::Resources'
    _globals['_CUSTOMCONVERSIONGOAL'].fields_by_name['resource_name']._loaded_options = None
    _globals['_CUSTOMCONVERSIONGOAL'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x05\xfaA/\n-googleads.googleapis.com/CustomConversionGoal'
    _globals['_CUSTOMCONVERSIONGOAL'].fields_by_name['id']._loaded_options = None
    _globals['_CUSTOMCONVERSIONGOAL'].fields_by_name['id']._serialized_options = b'\xe0A\x05'
    _globals['_CUSTOMCONVERSIONGOAL'].fields_by_name['conversion_actions']._loaded_options = None
    _globals['_CUSTOMCONVERSIONGOAL'].fields_by_name['conversion_actions']._serialized_options = b'\xfaA+\n)googleads.googleapis.com/ConversionAction'
    _globals['_CUSTOMCONVERSIONGOAL']._loaded_options = None
    _globals['_CUSTOMCONVERSIONGOAL']._serialized_options = b'\xeaAh\n-googleads.googleapis.com/CustomConversionGoal\x127customers/{customer_id}/customConversionGoals/{goal_id}'
    _globals['_CUSTOMCONVERSIONGOAL']._serialized_start = 232
    _globals['_CUSTOMCONVERSIONGOAL']._serialized_end = 655