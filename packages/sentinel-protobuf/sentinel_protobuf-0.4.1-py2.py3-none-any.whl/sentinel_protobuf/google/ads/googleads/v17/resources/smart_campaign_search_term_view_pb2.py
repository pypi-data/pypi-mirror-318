"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ads/googleads/v17/resources/smart_campaign_search_term_view.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nHgoogle/ads/googleads/v17/resources/smart_campaign_search_term_view.proto\x12"google.ads.googleads.v17.resources\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xd2\x02\n\x1bSmartCampaignSearchTermView\x12S\n\rresource_name\x18\x01 \x01(\tB<\xe0A\x03\xfaA6\n4googleads.googleapis.com/SmartCampaignSearchTermView\x12\x18\n\x0bsearch_term\x18\x02 \x01(\tB\x03\xe0A\x03\x12;\n\x08campaign\x18\x03 \x01(\tB)\xe0A\x03\xfaA#\n!googleads.googleapis.com/Campaign:\x86\x01\xeaA\x82\x01\n4googleads.googleapis.com/SmartCampaignSearchTermView\x12Jcustomers/{customer_id}/smartCampaignSearchTermViews/{campaign_id}~{query}B\x92\x02\n&com.google.ads.googleads.v17.resourcesB SmartCampaignSearchTermViewProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v17/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V17.Resources\xca\x02"Google\\Ads\\GoogleAds\\V17\\Resources\xea\x02&Google::Ads::GoogleAds::V17::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v17.resources.smart_campaign_search_term_view_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v17.resourcesB SmartCampaignSearchTermViewProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v17/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V17.Resources\xca\x02"Google\\Ads\\GoogleAds\\V17\\Resources\xea\x02&Google::Ads::GoogleAds::V17::Resources'
    _globals['_SMARTCAMPAIGNSEARCHTERMVIEW'].fields_by_name['resource_name']._loaded_options = None
    _globals['_SMARTCAMPAIGNSEARCHTERMVIEW'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x03\xfaA6\n4googleads.googleapis.com/SmartCampaignSearchTermView'
    _globals['_SMARTCAMPAIGNSEARCHTERMVIEW'].fields_by_name['search_term']._loaded_options = None
    _globals['_SMARTCAMPAIGNSEARCHTERMVIEW'].fields_by_name['search_term']._serialized_options = b'\xe0A\x03'
    _globals['_SMARTCAMPAIGNSEARCHTERMVIEW'].fields_by_name['campaign']._loaded_options = None
    _globals['_SMARTCAMPAIGNSEARCHTERMVIEW'].fields_by_name['campaign']._serialized_options = b'\xe0A\x03\xfaA#\n!googleads.googleapis.com/Campaign'
    _globals['_SMARTCAMPAIGNSEARCHTERMVIEW']._loaded_options = None
    _globals['_SMARTCAMPAIGNSEARCHTERMVIEW']._serialized_options = b'\xeaA\x82\x01\n4googleads.googleapis.com/SmartCampaignSearchTermView\x12Jcustomers/{customer_id}/smartCampaignSearchTermViews/{campaign_id}~{query}'
    _globals['_SMARTCAMPAIGNSEARCHTERMVIEW']._serialized_start = 173
    _globals['_SMARTCAMPAIGNSEARCHTERMVIEW']._serialized_end = 511