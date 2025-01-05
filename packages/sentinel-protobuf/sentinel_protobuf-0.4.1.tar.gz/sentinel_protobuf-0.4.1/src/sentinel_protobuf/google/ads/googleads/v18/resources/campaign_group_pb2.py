"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ads/googleads/v18/resources/campaign_group.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v18.enums import campaign_group_status_pb2 as google_dot_ads_dot_googleads_dot_v18_dot_enums_dot_campaign__group__status__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7google/ads/googleads/v18/resources/campaign_group.proto\x12"google.ads.googleads.v18.resources\x1a:google/ads/googleads/v18/enums/campaign_group_status.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xbb\x02\n\rCampaignGroup\x12E\n\rresource_name\x18\x01 \x01(\tB.\xe0A\x05\xfaA(\n&googleads.googleapis.com/CampaignGroup\x12\x0f\n\x02id\x18\x03 \x01(\x03B\x03\xe0A\x03\x12\x0c\n\x04name\x18\x04 \x01(\t\x12[\n\x06status\x18\x05 \x01(\x0e2K.google.ads.googleads.v18.enums.CampaignGroupStatusEnum.CampaignGroupStatus:g\xeaAd\n&googleads.googleapis.com/CampaignGroup\x12:customers/{customer_id}/campaignGroups/{campaign_group_id}B\x84\x02\n&com.google.ads.googleads.v18.resourcesB\x12CampaignGroupProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v18/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V18.Resources\xca\x02"Google\\Ads\\GoogleAds\\V18\\Resources\xea\x02&Google::Ads::GoogleAds::V18::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v18.resources.campaign_group_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v18.resourcesB\x12CampaignGroupProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v18/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V18.Resources\xca\x02"Google\\Ads\\GoogleAds\\V18\\Resources\xea\x02&Google::Ads::GoogleAds::V18::Resources'
    _globals['_CAMPAIGNGROUP'].fields_by_name['resource_name']._loaded_options = None
    _globals['_CAMPAIGNGROUP'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x05\xfaA(\n&googleads.googleapis.com/CampaignGroup'
    _globals['_CAMPAIGNGROUP'].fields_by_name['id']._loaded_options = None
    _globals['_CAMPAIGNGROUP'].fields_by_name['id']._serialized_options = b'\xe0A\x03'
    _globals['_CAMPAIGNGROUP']._loaded_options = None
    _globals['_CAMPAIGNGROUP']._serialized_options = b'\xeaAd\n&googleads.googleapis.com/CampaignGroup\x12:customers/{customer_id}/campaignGroups/{campaign_group_id}'
    _globals['_CAMPAIGNGROUP']._serialized_start = 216
    _globals['_CAMPAIGNGROUP']._serialized_end = 531