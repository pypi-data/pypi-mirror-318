"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ads/googleads/v18/services/campaign_customizer_service.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v18.enums import response_content_type_pb2 as google_dot_ads_dot_googleads_dot_v18_dot_enums_dot_response__content__type__pb2
from ......google.ads.googleads.v18.resources import campaign_customizer_pb2 as google_dot_ads_dot_googleads_dot_v18_dot_resources_dot_campaign__customizer__pb2
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ......google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nCgoogle/ads/googleads/v18/services/campaign_customizer_service.proto\x12!google.ads.googleads.v18.services\x1a:google/ads/googleads/v18/enums/response_content_type.proto\x1a<google/ads/googleads/v18/resources/campaign_customizer.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x17google/rpc/status.proto"\xb1\x02\n MutateCampaignCustomizersRequest\x12\x18\n\x0bcustomer_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12W\n\noperations\x18\x02 \x03(\x0b2>.google.ads.googleads.v18.services.CampaignCustomizerOperationB\x03\xe0A\x02\x12\x17\n\x0fpartial_failure\x18\x03 \x01(\x08\x12\x15\n\rvalidate_only\x18\x04 \x01(\x08\x12j\n\x15response_content_type\x18\x05 \x01(\x0e2K.google.ads.googleads.v18.enums.ResponseContentTypeEnum.ResponseContentType"\xb8\x01\n\x1bCampaignCustomizerOperation\x12H\n\x06create\x18\x01 \x01(\x0b26.google.ads.googleads.v18.resources.CampaignCustomizerH\x00\x12B\n\x06remove\x18\x02 \x01(\tB0\xfaA-\n+googleads.googleapis.com/CampaignCustomizerH\x00B\x0b\n\toperation"\xaa\x01\n!MutateCampaignCustomizersResponse\x12R\n\x07results\x18\x01 \x03(\x0b2A.google.ads.googleads.v18.services.MutateCampaignCustomizerResult\x121\n\x15partial_failure_error\x18\x02 \x01(\x0b2\x12.google.rpc.Status"\xbe\x01\n\x1eMutateCampaignCustomizerResult\x12G\n\rresource_name\x18\x01 \x01(\tB0\xfaA-\n+googleads.googleapis.com/CampaignCustomizer\x12S\n\x13campaign_customizer\x18\x02 \x01(\x0b26.google.ads.googleads.v18.resources.CampaignCustomizer2\xea\x02\n\x19CampaignCustomizerService\x12\x85\x02\n\x19MutateCampaignCustomizers\x12C.google.ads.googleads.v18.services.MutateCampaignCustomizersRequest\x1aD.google.ads.googleads.v18.services.MutateCampaignCustomizersResponse"]\xdaA\x16customer_id,operations\x82\xd3\xe4\x93\x02>"9/v18/customers/{customer_id=*}/campaignCustomizers:mutate:\x01*\x1aE\xcaA\x18googleads.googleapis.com\xd2A\'https://www.googleapis.com/auth/adwordsB\x8a\x02\n%com.google.ads.googleads.v18.servicesB\x1eCampaignCustomizerServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v18/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V18.Services\xca\x02!Google\\Ads\\GoogleAds\\V18\\Services\xea\x02%Google::Ads::GoogleAds::V18::Servicesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v18.services.campaign_customizer_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.ads.googleads.v18.servicesB\x1eCampaignCustomizerServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v18/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V18.Services\xca\x02!Google\\Ads\\GoogleAds\\V18\\Services\xea\x02%Google::Ads::GoogleAds::V18::Services'
    _globals['_MUTATECAMPAIGNCUSTOMIZERSREQUEST'].fields_by_name['customer_id']._loaded_options = None
    _globals['_MUTATECAMPAIGNCUSTOMIZERSREQUEST'].fields_by_name['customer_id']._serialized_options = b'\xe0A\x02'
    _globals['_MUTATECAMPAIGNCUSTOMIZERSREQUEST'].fields_by_name['operations']._loaded_options = None
    _globals['_MUTATECAMPAIGNCUSTOMIZERSREQUEST'].fields_by_name['operations']._serialized_options = b'\xe0A\x02'
    _globals['_CAMPAIGNCUSTOMIZEROPERATION'].fields_by_name['remove']._loaded_options = None
    _globals['_CAMPAIGNCUSTOMIZEROPERATION'].fields_by_name['remove']._serialized_options = b'\xfaA-\n+googleads.googleapis.com/CampaignCustomizer'
    _globals['_MUTATECAMPAIGNCUSTOMIZERRESULT'].fields_by_name['resource_name']._loaded_options = None
    _globals['_MUTATECAMPAIGNCUSTOMIZERRESULT'].fields_by_name['resource_name']._serialized_options = b'\xfaA-\n+googleads.googleapis.com/CampaignCustomizer'
    _globals['_CAMPAIGNCUSTOMIZERSERVICE']._loaded_options = None
    _globals['_CAMPAIGNCUSTOMIZERSERVICE']._serialized_options = b"\xcaA\x18googleads.googleapis.com\xd2A'https://www.googleapis.com/auth/adwords"
    _globals['_CAMPAIGNCUSTOMIZERSERVICE'].methods_by_name['MutateCampaignCustomizers']._loaded_options = None
    _globals['_CAMPAIGNCUSTOMIZERSERVICE'].methods_by_name['MutateCampaignCustomizers']._serialized_options = b'\xdaA\x16customer_id,operations\x82\xd3\xe4\x93\x02>"9/v18/customers/{customer_id=*}/campaignCustomizers:mutate:\x01*'
    _globals['_MUTATECAMPAIGNCUSTOMIZERSREQUEST']._serialized_start = 369
    _globals['_MUTATECAMPAIGNCUSTOMIZERSREQUEST']._serialized_end = 674
    _globals['_CAMPAIGNCUSTOMIZEROPERATION']._serialized_start = 677
    _globals['_CAMPAIGNCUSTOMIZEROPERATION']._serialized_end = 861
    _globals['_MUTATECAMPAIGNCUSTOMIZERSRESPONSE']._serialized_start = 864
    _globals['_MUTATECAMPAIGNCUSTOMIZERSRESPONSE']._serialized_end = 1034
    _globals['_MUTATECAMPAIGNCUSTOMIZERRESULT']._serialized_start = 1037
    _globals['_MUTATECAMPAIGNCUSTOMIZERRESULT']._serialized_end = 1227
    _globals['_CAMPAIGNCUSTOMIZERSERVICE']._serialized_start = 1230
    _globals['_CAMPAIGNCUSTOMIZERSERVICE']._serialized_end = 1592