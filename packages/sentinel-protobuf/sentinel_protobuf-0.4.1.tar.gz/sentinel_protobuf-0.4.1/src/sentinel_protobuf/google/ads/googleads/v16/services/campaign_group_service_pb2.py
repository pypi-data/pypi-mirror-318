"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ads/googleads/v16/services/campaign_group_service.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v16.enums import response_content_type_pb2 as google_dot_ads_dot_googleads_dot_v16_dot_enums_dot_response__content__type__pb2
from ......google.ads.googleads.v16.resources import campaign_group_pb2 as google_dot_ads_dot_googleads_dot_v16_dot_resources_dot_campaign__group__pb2
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from ......google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n>google/ads/googleads/v16/services/campaign_group_service.proto\x12!google.ads.googleads.v16.services\x1a:google/ads/googleads/v16/enums/response_content_type.proto\x1a7google/ads/googleads/v16/resources/campaign_group.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto\x1a\x17google/rpc/status.proto"\xa7\x02\n\x1bMutateCampaignGroupsRequest\x12\x18\n\x0bcustomer_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12R\n\noperations\x18\x02 \x03(\x0b29.google.ads.googleads.v16.services.CampaignGroupOperationB\x03\xe0A\x02\x12\x17\n\x0fpartial_failure\x18\x03 \x01(\x08\x12\x15\n\rvalidate_only\x18\x04 \x01(\x08\x12j\n\x15response_content_type\x18\x05 \x01(\x0e2K.google.ads.googleads.v16.enums.ResponseContentTypeEnum.ResponseContentType"\x9f\x02\n\x16CampaignGroupOperation\x12/\n\x0bupdate_mask\x18\x04 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12C\n\x06create\x18\x01 \x01(\x0b21.google.ads.googleads.v16.resources.CampaignGroupH\x00\x12C\n\x06update\x18\x02 \x01(\x0b21.google.ads.googleads.v16.resources.CampaignGroupH\x00\x12=\n\x06remove\x18\x03 \x01(\tB+\xfaA(\n&googleads.googleapis.com/CampaignGroupH\x00B\x0b\n\toperation"\xa0\x01\n\x1cMutateCampaignGroupsResponse\x12M\n\x07results\x18\x02 \x03(\x0b2<.google.ads.googleads.v16.services.MutateCampaignGroupResult\x121\n\x15partial_failure_error\x18\x03 \x01(\x0b2\x12.google.rpc.Status"\xad\x01\n\x19MutateCampaignGroupResult\x12E\n\rresource_name\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\n&googleads.googleapis.com/CampaignGroup\x12I\n\x0ecampaign_group\x18\x02 \x01(\x0b21.google.ads.googleads.v16.resources.CampaignGroup2\xd1\x02\n\x14CampaignGroupService\x12\xf1\x01\n\x14MutateCampaignGroups\x12>.google.ads.googleads.v16.services.MutateCampaignGroupsRequest\x1a?.google.ads.googleads.v16.services.MutateCampaignGroupsResponse"X\xdaA\x16customer_id,operations\x82\xd3\xe4\x93\x029"4/v16/customers/{customer_id=*}/campaignGroups:mutate:\x01*\x1aE\xcaA\x18googleads.googleapis.com\xd2A\'https://www.googleapis.com/auth/adwordsB\x85\x02\n%com.google.ads.googleads.v16.servicesB\x19CampaignGroupServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v16/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V16.Services\xca\x02!Google\\Ads\\GoogleAds\\V16\\Services\xea\x02%Google::Ads::GoogleAds::V16::Servicesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v16.services.campaign_group_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.ads.googleads.v16.servicesB\x19CampaignGroupServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v16/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V16.Services\xca\x02!Google\\Ads\\GoogleAds\\V16\\Services\xea\x02%Google::Ads::GoogleAds::V16::Services'
    _globals['_MUTATECAMPAIGNGROUPSREQUEST'].fields_by_name['customer_id']._loaded_options = None
    _globals['_MUTATECAMPAIGNGROUPSREQUEST'].fields_by_name['customer_id']._serialized_options = b'\xe0A\x02'
    _globals['_MUTATECAMPAIGNGROUPSREQUEST'].fields_by_name['operations']._loaded_options = None
    _globals['_MUTATECAMPAIGNGROUPSREQUEST'].fields_by_name['operations']._serialized_options = b'\xe0A\x02'
    _globals['_CAMPAIGNGROUPOPERATION'].fields_by_name['remove']._loaded_options = None
    _globals['_CAMPAIGNGROUPOPERATION'].fields_by_name['remove']._serialized_options = b'\xfaA(\n&googleads.googleapis.com/CampaignGroup'
    _globals['_MUTATECAMPAIGNGROUPRESULT'].fields_by_name['resource_name']._loaded_options = None
    _globals['_MUTATECAMPAIGNGROUPRESULT'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x02\xfaA(\n&googleads.googleapis.com/CampaignGroup'
    _globals['_CAMPAIGNGROUPSERVICE']._loaded_options = None
    _globals['_CAMPAIGNGROUPSERVICE']._serialized_options = b"\xcaA\x18googleads.googleapis.com\xd2A'https://www.googleapis.com/auth/adwords"
    _globals['_CAMPAIGNGROUPSERVICE'].methods_by_name['MutateCampaignGroups']._loaded_options = None
    _globals['_CAMPAIGNGROUPSERVICE'].methods_by_name['MutateCampaignGroups']._serialized_options = b'\xdaA\x16customer_id,operations\x82\xd3\xe4\x93\x029"4/v16/customers/{customer_id=*}/campaignGroups:mutate:\x01*'
    _globals['_MUTATECAMPAIGNGROUPSREQUEST']._serialized_start = 393
    _globals['_MUTATECAMPAIGNGROUPSREQUEST']._serialized_end = 688
    _globals['_CAMPAIGNGROUPOPERATION']._serialized_start = 691
    _globals['_CAMPAIGNGROUPOPERATION']._serialized_end = 978
    _globals['_MUTATECAMPAIGNGROUPSRESPONSE']._serialized_start = 981
    _globals['_MUTATECAMPAIGNGROUPSRESPONSE']._serialized_end = 1141
    _globals['_MUTATECAMPAIGNGROUPRESULT']._serialized_start = 1144
    _globals['_MUTATECAMPAIGNGROUPRESULT']._serialized_end = 1317
    _globals['_CAMPAIGNGROUPSERVICE']._serialized_start = 1320
    _globals['_CAMPAIGNGROUPSERVICE']._serialized_end = 1657