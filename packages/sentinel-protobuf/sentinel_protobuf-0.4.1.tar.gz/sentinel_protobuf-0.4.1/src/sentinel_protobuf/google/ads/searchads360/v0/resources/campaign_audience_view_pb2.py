"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ads/searchads360/v0/resources/campaign_audience_view.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nAgoogle/ads/searchads360/v0/resources/campaign_audience_view.proto\x12$google.ads.searchads360.v0.resources\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xeb\x01\n\x14CampaignAudienceView\x12O\n\rresource_name\x18\x01 \x01(\tB8\xe0A\x03\xfaA2\n0searchads360.googleapis.com/CampaignAudienceView:\x81\x01\xeaA~\n0searchads360.googleapis.com/CampaignAudienceView\x12Jcustomers/{customer_id}/campaignAudienceViews/{campaign_id}~{criterion_id}B\x99\x02\n(com.google.ads.searchads360.v0.resourcesB\x19CampaignAudienceViewProtoP\x01ZMgoogle.golang.org/genproto/googleapis/ads/searchads360/v0/resources;resources\xa2\x02\x07GASA360\xaa\x02$Google.Ads.SearchAds360.V0.Resources\xca\x02$Google\\Ads\\SearchAds360\\V0\\Resources\xea\x02(Google::Ads::SearchAds360::V0::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.searchads360.v0.resources.campaign_audience_view_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n(com.google.ads.searchads360.v0.resourcesB\x19CampaignAudienceViewProtoP\x01ZMgoogle.golang.org/genproto/googleapis/ads/searchads360/v0/resources;resources\xa2\x02\x07GASA360\xaa\x02$Google.Ads.SearchAds360.V0.Resources\xca\x02$Google\\Ads\\SearchAds360\\V0\\Resources\xea\x02(Google::Ads::SearchAds360::V0::Resources'
    _globals['_CAMPAIGNAUDIENCEVIEW'].fields_by_name['resource_name']._loaded_options = None
    _globals['_CAMPAIGNAUDIENCEVIEW'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x03\xfaA2\n0searchads360.googleapis.com/CampaignAudienceView'
    _globals['_CAMPAIGNAUDIENCEVIEW']._loaded_options = None
    _globals['_CAMPAIGNAUDIENCEVIEW']._serialized_options = b'\xeaA~\n0searchads360.googleapis.com/CampaignAudienceView\x12Jcustomers/{customer_id}/campaignAudienceViews/{campaign_id}~{criterion_id}'
    _globals['_CAMPAIGNAUDIENCEVIEW']._serialized_start = 168
    _globals['_CAMPAIGNAUDIENCEVIEW']._serialized_end = 403