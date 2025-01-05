"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ads/googleads/v17/services/campaign_asset_set_service.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v17.enums import response_content_type_pb2 as google_dot_ads_dot_googleads_dot_v17_dot_enums_dot_response__content__type__pb2
from ......google.ads.googleads.v17.resources import campaign_asset_set_pb2 as google_dot_ads_dot_googleads_dot_v17_dot_resources_dot_campaign__asset__set__pb2
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ......google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nBgoogle/ads/googleads/v17/services/campaign_asset_set_service.proto\x12!google.ads.googleads.v17.services\x1a:google/ads/googleads/v17/enums/response_content_type.proto\x1a;google/ads/googleads/v17/resources/campaign_asset_set.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x17google/rpc/status.proto"\xad\x02\n\x1eMutateCampaignAssetSetsRequest\x12\x18\n\x0bcustomer_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12U\n\noperations\x18\x02 \x03(\x0b2<.google.ads.googleads.v17.services.CampaignAssetSetOperationB\x03\xe0A\x02\x12\x17\n\x0fpartial_failure\x18\x03 \x01(\x08\x12\x15\n\rvalidate_only\x18\x04 \x01(\x08\x12j\n\x15response_content_type\x18\x05 \x01(\x0e2K.google.ads.googleads.v17.enums.ResponseContentTypeEnum.ResponseContentType"\xb2\x01\n\x19CampaignAssetSetOperation\x12F\n\x06create\x18\x01 \x01(\x0b24.google.ads.googleads.v17.resources.CampaignAssetSetH\x00\x12@\n\x06remove\x18\x02 \x01(\tB.\xfaA+\n)googleads.googleapis.com/CampaignAssetSetH\x00B\x0b\n\toperation"\xa6\x01\n\x1fMutateCampaignAssetSetsResponse\x12P\n\x07results\x18\x01 \x03(\x0b2?.google.ads.googleads.v17.services.MutateCampaignAssetSetResult\x121\n\x15partial_failure_error\x18\x02 \x01(\x0b2\x12.google.rpc.Status"\xb7\x01\n\x1cMutateCampaignAssetSetResult\x12E\n\rresource_name\x18\x01 \x01(\tB.\xfaA+\n)googleads.googleapis.com/CampaignAssetSet\x12P\n\x12campaign_asset_set\x18\x02 \x01(\x0b24.google.ads.googleads.v17.resources.CampaignAssetSet2\xe0\x02\n\x17CampaignAssetSetService\x12\xfd\x01\n\x17MutateCampaignAssetSets\x12A.google.ads.googleads.v17.services.MutateCampaignAssetSetsRequest\x1aB.google.ads.googleads.v17.services.MutateCampaignAssetSetsResponse"[\xdaA\x16customer_id,operations\x82\xd3\xe4\x93\x02<"7/v17/customers/{customer_id=*}/campaignAssetSets:mutate:\x01*\x1aE\xcaA\x18googleads.googleapis.com\xd2A\'https://www.googleapis.com/auth/adwordsB\x88\x02\n%com.google.ads.googleads.v17.servicesB\x1cCampaignAssetSetServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v17/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V17.Services\xca\x02!Google\\Ads\\GoogleAds\\V17\\Services\xea\x02%Google::Ads::GoogleAds::V17::Servicesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v17.services.campaign_asset_set_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.ads.googleads.v17.servicesB\x1cCampaignAssetSetServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v17/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V17.Services\xca\x02!Google\\Ads\\GoogleAds\\V17\\Services\xea\x02%Google::Ads::GoogleAds::V17::Services'
    _globals['_MUTATECAMPAIGNASSETSETSREQUEST'].fields_by_name['customer_id']._loaded_options = None
    _globals['_MUTATECAMPAIGNASSETSETSREQUEST'].fields_by_name['customer_id']._serialized_options = b'\xe0A\x02'
    _globals['_MUTATECAMPAIGNASSETSETSREQUEST'].fields_by_name['operations']._loaded_options = None
    _globals['_MUTATECAMPAIGNASSETSETSREQUEST'].fields_by_name['operations']._serialized_options = b'\xe0A\x02'
    _globals['_CAMPAIGNASSETSETOPERATION'].fields_by_name['remove']._loaded_options = None
    _globals['_CAMPAIGNASSETSETOPERATION'].fields_by_name['remove']._serialized_options = b'\xfaA+\n)googleads.googleapis.com/CampaignAssetSet'
    _globals['_MUTATECAMPAIGNASSETSETRESULT'].fields_by_name['resource_name']._loaded_options = None
    _globals['_MUTATECAMPAIGNASSETSETRESULT'].fields_by_name['resource_name']._serialized_options = b'\xfaA+\n)googleads.googleapis.com/CampaignAssetSet'
    _globals['_CAMPAIGNASSETSETSERVICE']._loaded_options = None
    _globals['_CAMPAIGNASSETSETSERVICE']._serialized_options = b"\xcaA\x18googleads.googleapis.com\xd2A'https://www.googleapis.com/auth/adwords"
    _globals['_CAMPAIGNASSETSETSERVICE'].methods_by_name['MutateCampaignAssetSets']._loaded_options = None
    _globals['_CAMPAIGNASSETSETSERVICE'].methods_by_name['MutateCampaignAssetSets']._serialized_options = b'\xdaA\x16customer_id,operations\x82\xd3\xe4\x93\x02<"7/v17/customers/{customer_id=*}/campaignAssetSets:mutate:\x01*'
    _globals['_MUTATECAMPAIGNASSETSETSREQUEST']._serialized_start = 367
    _globals['_MUTATECAMPAIGNASSETSETSREQUEST']._serialized_end = 668
    _globals['_CAMPAIGNASSETSETOPERATION']._serialized_start = 671
    _globals['_CAMPAIGNASSETSETOPERATION']._serialized_end = 849
    _globals['_MUTATECAMPAIGNASSETSETSRESPONSE']._serialized_start = 852
    _globals['_MUTATECAMPAIGNASSETSETSRESPONSE']._serialized_end = 1018
    _globals['_MUTATECAMPAIGNASSETSETRESULT']._serialized_start = 1021
    _globals['_MUTATECAMPAIGNASSETSETRESULT']._serialized_end = 1204
    _globals['_CAMPAIGNASSETSETSERVICE']._serialized_start = 1207
    _globals['_CAMPAIGNASSETSETSERVICE']._serialized_end = 1559