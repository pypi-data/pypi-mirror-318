"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ads/googleads/v17/services/campaign_conversion_goal_service.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v17.resources import campaign_conversion_goal_pb2 as google_dot_ads_dot_googleads_dot_v17_dot_resources_dot_campaign__conversion__goal__pb2
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nHgoogle/ads/googleads/v17/services/campaign_conversion_goal_service.proto\x12!google.ads.googleads.v17.services\x1aAgoogle/ads/googleads/v17/resources/campaign_conversion_goal.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto"\xb4\x01\n$MutateCampaignConversionGoalsRequest\x12\x18\n\x0bcustomer_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12[\n\noperations\x18\x02 \x03(\x0b2B.google.ads.googleads.v17.services.CampaignConversionGoalOperationB\x03\xe0A\x02\x12\x15\n\rvalidate_only\x18\x03 \x01(\x08"\xad\x01\n\x1fCampaignConversionGoalOperation\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12L\n\x06update\x18\x01 \x01(\x0b2:.google.ads.googleads.v17.resources.CampaignConversionGoalH\x00B\x0b\n\toperation"\x7f\n%MutateCampaignConversionGoalsResponse\x12V\n\x07results\x18\x01 \x03(\x0b2E.google.ads.googleads.v17.services.MutateCampaignConversionGoalResult"q\n"MutateCampaignConversionGoalResult\x12K\n\rresource_name\x18\x01 \x01(\tB4\xfaA1\n/googleads.googleapis.com/CampaignConversionGoal2\xfe\x02\n\x1dCampaignConversionGoalService\x12\x95\x02\n\x1dMutateCampaignConversionGoals\x12G.google.ads.googleads.v17.services.MutateCampaignConversionGoalsRequest\x1aH.google.ads.googleads.v17.services.MutateCampaignConversionGoalsResponse"a\xdaA\x16customer_id,operations\x82\xd3\xe4\x93\x02B"=/v17/customers/{customer_id=*}/campaignConversionGoals:mutate:\x01*\x1aE\xcaA\x18googleads.googleapis.com\xd2A\'https://www.googleapis.com/auth/adwordsB\x8e\x02\n%com.google.ads.googleads.v17.servicesB"CampaignConversionGoalServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v17/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V17.Services\xca\x02!Google\\Ads\\GoogleAds\\V17\\Services\xea\x02%Google::Ads::GoogleAds::V17::Servicesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v17.services.campaign_conversion_goal_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.ads.googleads.v17.servicesB"CampaignConversionGoalServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v17/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V17.Services\xca\x02!Google\\Ads\\GoogleAds\\V17\\Services\xea\x02%Google::Ads::GoogleAds::V17::Services'
    _globals['_MUTATECAMPAIGNCONVERSIONGOALSREQUEST'].fields_by_name['customer_id']._loaded_options = None
    _globals['_MUTATECAMPAIGNCONVERSIONGOALSREQUEST'].fields_by_name['customer_id']._serialized_options = b'\xe0A\x02'
    _globals['_MUTATECAMPAIGNCONVERSIONGOALSREQUEST'].fields_by_name['operations']._loaded_options = None
    _globals['_MUTATECAMPAIGNCONVERSIONGOALSREQUEST'].fields_by_name['operations']._serialized_options = b'\xe0A\x02'
    _globals['_MUTATECAMPAIGNCONVERSIONGOALRESULT'].fields_by_name['resource_name']._loaded_options = None
    _globals['_MUTATECAMPAIGNCONVERSIONGOALRESULT'].fields_by_name['resource_name']._serialized_options = b'\xfaA1\n/googleads.googleapis.com/CampaignConversionGoal'
    _globals['_CAMPAIGNCONVERSIONGOALSERVICE']._loaded_options = None
    _globals['_CAMPAIGNCONVERSIONGOALSERVICE']._serialized_options = b"\xcaA\x18googleads.googleapis.com\xd2A'https://www.googleapis.com/auth/adwords"
    _globals['_CAMPAIGNCONVERSIONGOALSERVICE'].methods_by_name['MutateCampaignConversionGoals']._loaded_options = None
    _globals['_CAMPAIGNCONVERSIONGOALSERVICE'].methods_by_name['MutateCampaignConversionGoals']._serialized_options = b'\xdaA\x16customer_id,operations\x82\xd3\xe4\x93\x02B"=/v17/customers/{customer_id=*}/campaignConversionGoals:mutate:\x01*'
    _globals['_MUTATECAMPAIGNCONVERSIONGOALSREQUEST']._serialized_start = 328
    _globals['_MUTATECAMPAIGNCONVERSIONGOALSREQUEST']._serialized_end = 508
    _globals['_CAMPAIGNCONVERSIONGOALOPERATION']._serialized_start = 511
    _globals['_CAMPAIGNCONVERSIONGOALOPERATION']._serialized_end = 684
    _globals['_MUTATECAMPAIGNCONVERSIONGOALSRESPONSE']._serialized_start = 686
    _globals['_MUTATECAMPAIGNCONVERSIONGOALSRESPONSE']._serialized_end = 813
    _globals['_MUTATECAMPAIGNCONVERSIONGOALRESULT']._serialized_start = 815
    _globals['_MUTATECAMPAIGNCONVERSIONGOALRESULT']._serialized_end = 928
    _globals['_CAMPAIGNCONVERSIONGOALSERVICE']._serialized_start = 931
    _globals['_CAMPAIGNCONVERSIONGOALSERVICE']._serialized_end = 1313