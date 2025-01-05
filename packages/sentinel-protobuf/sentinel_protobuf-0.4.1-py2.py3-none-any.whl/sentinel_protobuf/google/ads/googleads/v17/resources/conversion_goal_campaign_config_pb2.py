"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ads/googleads/v17/resources/conversion_goal_campaign_config.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v17.enums import goal_config_level_pb2 as google_dot_ads_dot_googleads_dot_v17_dot_enums_dot_goal__config__level__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nHgoogle/ads/googleads/v17/resources/conversion_goal_campaign_config.proto\x12"google.ads.googleads.v17.resources\x1a6google/ads/googleads/v17/enums/goal_config_level.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xe6\x03\n\x1cConversionGoalCampaignConfig\x12T\n\rresource_name\x18\x01 \x01(\tB=\xe0A\x05\xfaA7\n5googleads.googleapis.com/ConversionGoalCampaignConfig\x12;\n\x08campaign\x18\x02 \x01(\tB)\xe0A\x05\xfaA#\n!googleads.googleapis.com/Campaign\x12^\n\x11goal_config_level\x18\x03 \x01(\x0e2C.google.ads.googleads.v17.enums.GoalConfigLevelEnum.GoalConfigLevel\x12R\n\x16custom_conversion_goal\x18\x04 \x01(\tB2\xfaA/\n-googleads.googleapis.com/CustomConversionGoal:\x7f\xeaA|\n5googleads.googleapis.com/ConversionGoalCampaignConfig\x12Ccustomers/{customer_id}/conversionGoalCampaignConfigs/{campaign_id}B\x93\x02\n&com.google.ads.googleads.v17.resourcesB!ConversionGoalCampaignConfigProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v17/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V17.Resources\xca\x02"Google\\Ads\\GoogleAds\\V17\\Resources\xea\x02&Google::Ads::GoogleAds::V17::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v17.resources.conversion_goal_campaign_config_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v17.resourcesB!ConversionGoalCampaignConfigProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v17/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V17.Resources\xca\x02"Google\\Ads\\GoogleAds\\V17\\Resources\xea\x02&Google::Ads::GoogleAds::V17::Resources'
    _globals['_CONVERSIONGOALCAMPAIGNCONFIG'].fields_by_name['resource_name']._loaded_options = None
    _globals['_CONVERSIONGOALCAMPAIGNCONFIG'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x05\xfaA7\n5googleads.googleapis.com/ConversionGoalCampaignConfig'
    _globals['_CONVERSIONGOALCAMPAIGNCONFIG'].fields_by_name['campaign']._loaded_options = None
    _globals['_CONVERSIONGOALCAMPAIGNCONFIG'].fields_by_name['campaign']._serialized_options = b'\xe0A\x05\xfaA#\n!googleads.googleapis.com/Campaign'
    _globals['_CONVERSIONGOALCAMPAIGNCONFIG'].fields_by_name['custom_conversion_goal']._loaded_options = None
    _globals['_CONVERSIONGOALCAMPAIGNCONFIG'].fields_by_name['custom_conversion_goal']._serialized_options = b'\xfaA/\n-googleads.googleapis.com/CustomConversionGoal'
    _globals['_CONVERSIONGOALCAMPAIGNCONFIG']._loaded_options = None
    _globals['_CONVERSIONGOALCAMPAIGNCONFIG']._serialized_options = b'\xeaA|\n5googleads.googleapis.com/ConversionGoalCampaignConfig\x12Ccustomers/{customer_id}/conversionGoalCampaignConfigs/{campaign_id}'
    _globals['_CONVERSIONGOALCAMPAIGNCONFIG']._serialized_start = 229
    _globals['_CONVERSIONGOALCAMPAIGNCONFIG']._serialized_end = 715