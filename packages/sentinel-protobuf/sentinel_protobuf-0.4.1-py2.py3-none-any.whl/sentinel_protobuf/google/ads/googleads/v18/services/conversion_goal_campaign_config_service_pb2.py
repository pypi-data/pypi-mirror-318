"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ads/googleads/v18/services/conversion_goal_campaign_config_service.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v18.enums import response_content_type_pb2 as google_dot_ads_dot_googleads_dot_v18_dot_enums_dot_response__content__type__pb2
from ......google.ads.googleads.v18.resources import conversion_goal_campaign_config_pb2 as google_dot_ads_dot_googleads_dot_v18_dot_resources_dot_conversion__goal__campaign__config__pb2
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nOgoogle/ads/googleads/v18/services/conversion_goal_campaign_config_service.proto\x12!google.ads.googleads.v18.services\x1a:google/ads/googleads/v18/enums/response_content_type.proto\x1aHgoogle/ads/googleads/v18/resources/conversion_goal_campaign_config.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto"\xac\x02\n*MutateConversionGoalCampaignConfigsRequest\x12\x18\n\x0bcustomer_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12a\n\noperations\x18\x02 \x03(\x0b2H.google.ads.googleads.v18.services.ConversionGoalCampaignConfigOperationB\x03\xe0A\x02\x12\x15\n\rvalidate_only\x18\x03 \x01(\x08\x12j\n\x15response_content_type\x18\x04 \x01(\x0e2K.google.ads.googleads.v18.enums.ResponseContentTypeEnum.ResponseContentType"\xb9\x01\n%ConversionGoalCampaignConfigOperation\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12R\n\x06update\x18\x01 \x01(\x0b2@.google.ads.googleads.v18.resources.ConversionGoalCampaignConfigH\x00B\x0b\n\toperation"\x8b\x01\n+MutateConversionGoalCampaignConfigsResponse\x12\\\n\x07results\x18\x01 \x03(\x0b2K.google.ads.googleads.v18.services.MutateConversionGoalCampaignConfigResult"\xe8\x01\n(MutateConversionGoalCampaignConfigResult\x12Q\n\rresource_name\x18\x01 \x01(\tB:\xfaA7\n5googleads.googleapis.com/ConversionGoalCampaignConfig\x12i\n\x1fconversion_goal_campaign_config\x18\x02 \x01(\x0b2@.google.ads.googleads.v18.resources.ConversionGoalCampaignConfig2\x9c\x03\n#ConversionGoalCampaignConfigService\x12\xad\x02\n#MutateConversionGoalCampaignConfigs\x12M.google.ads.googleads.v18.services.MutateConversionGoalCampaignConfigsRequest\x1aN.google.ads.googleads.v18.services.MutateConversionGoalCampaignConfigsResponse"g\xdaA\x16customer_id,operations\x82\xd3\xe4\x93\x02H"C/v18/customers/{customer_id=*}/conversionGoalCampaignConfigs:mutate:\x01*\x1aE\xcaA\x18googleads.googleapis.com\xd2A\'https://www.googleapis.com/auth/adwordsB\x94\x02\n%com.google.ads.googleads.v18.servicesB(ConversionGoalCampaignConfigServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v18/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V18.Services\xca\x02!Google\\Ads\\GoogleAds\\V18\\Services\xea\x02%Google::Ads::GoogleAds::V18::Servicesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v18.services.conversion_goal_campaign_config_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.ads.googleads.v18.servicesB(ConversionGoalCampaignConfigServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v18/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V18.Services\xca\x02!Google\\Ads\\GoogleAds\\V18\\Services\xea\x02%Google::Ads::GoogleAds::V18::Services'
    _globals['_MUTATECONVERSIONGOALCAMPAIGNCONFIGSREQUEST'].fields_by_name['customer_id']._loaded_options = None
    _globals['_MUTATECONVERSIONGOALCAMPAIGNCONFIGSREQUEST'].fields_by_name['customer_id']._serialized_options = b'\xe0A\x02'
    _globals['_MUTATECONVERSIONGOALCAMPAIGNCONFIGSREQUEST'].fields_by_name['operations']._loaded_options = None
    _globals['_MUTATECONVERSIONGOALCAMPAIGNCONFIGSREQUEST'].fields_by_name['operations']._serialized_options = b'\xe0A\x02'
    _globals['_MUTATECONVERSIONGOALCAMPAIGNCONFIGRESULT'].fields_by_name['resource_name']._loaded_options = None
    _globals['_MUTATECONVERSIONGOALCAMPAIGNCONFIGRESULT'].fields_by_name['resource_name']._serialized_options = b'\xfaA7\n5googleads.googleapis.com/ConversionGoalCampaignConfig'
    _globals['_CONVERSIONGOALCAMPAIGNCONFIGSERVICE']._loaded_options = None
    _globals['_CONVERSIONGOALCAMPAIGNCONFIGSERVICE']._serialized_options = b"\xcaA\x18googleads.googleapis.com\xd2A'https://www.googleapis.com/auth/adwords"
    _globals['_CONVERSIONGOALCAMPAIGNCONFIGSERVICE'].methods_by_name['MutateConversionGoalCampaignConfigs']._loaded_options = None
    _globals['_CONVERSIONGOALCAMPAIGNCONFIGSERVICE'].methods_by_name['MutateConversionGoalCampaignConfigs']._serialized_options = b'\xdaA\x16customer_id,operations\x82\xd3\xe4\x93\x02H"C/v18/customers/{customer_id=*}/conversionGoalCampaignConfigs:mutate:\x01*'
    _globals['_MUTATECONVERSIONGOALCAMPAIGNCONFIGSREQUEST']._serialized_start = 402
    _globals['_MUTATECONVERSIONGOALCAMPAIGNCONFIGSREQUEST']._serialized_end = 702
    _globals['_CONVERSIONGOALCAMPAIGNCONFIGOPERATION']._serialized_start = 705
    _globals['_CONVERSIONGOALCAMPAIGNCONFIGOPERATION']._serialized_end = 890
    _globals['_MUTATECONVERSIONGOALCAMPAIGNCONFIGSRESPONSE']._serialized_start = 893
    _globals['_MUTATECONVERSIONGOALCAMPAIGNCONFIGSRESPONSE']._serialized_end = 1032
    _globals['_MUTATECONVERSIONGOALCAMPAIGNCONFIGRESULT']._serialized_start = 1035
    _globals['_MUTATECONVERSIONGOALCAMPAIGNCONFIGRESULT']._serialized_end = 1267
    _globals['_CONVERSIONGOALCAMPAIGNCONFIGSERVICE']._serialized_start = 1270
    _globals['_CONVERSIONGOALCAMPAIGNCONFIGSERVICE']._serialized_end = 1682