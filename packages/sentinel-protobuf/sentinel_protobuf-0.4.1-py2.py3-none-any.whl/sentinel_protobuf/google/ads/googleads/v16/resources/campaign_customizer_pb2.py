"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ads/googleads/v16/resources/campaign_customizer.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v16.common import customizer_value_pb2 as google_dot_ads_dot_googleads_dot_v16_dot_common_dot_customizer__value__pb2
from ......google.ads.googleads.v16.enums import customizer_value_status_pb2 as google_dot_ads_dot_googleads_dot_v16_dot_enums_dot_customizer__value__status__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n<google/ads/googleads/v16/resources/campaign_customizer.proto\x12"google.ads.googleads.v16.resources\x1a6google/ads/googleads/v16/common/customizer_value.proto\x1a<google/ads/googleads/v16/enums/customizer_value_status.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xa9\x04\n\x12CampaignCustomizer\x12J\n\rresource_name\x18\x01 \x01(\tB3\xe0A\x05\xfaA-\n+googleads.googleapis.com/CampaignCustomizer\x12;\n\x08campaign\x18\x02 \x01(\tB)\xe0A\x05\xfaA#\n!googleads.googleapis.com/Campaign\x12U\n\x14customizer_attribute\x18\x03 \x01(\tB7\xe0A\x02\xe0A\x05\xfaA.\n,googleads.googleapis.com/CustomizerAttribute\x12d\n\x06status\x18\x04 \x01(\x0e2O.google.ads.googleads.v16.enums.CustomizerValueStatusEnum.CustomizerValueStatusB\x03\xe0A\x03\x12D\n\x05value\x18\x05 \x01(\x0b20.google.ads.googleads.v16.common.CustomizerValueB\x03\xe0A\x02:\x86\x01\xeaA\x82\x01\n+googleads.googleapis.com/CampaignCustomizer\x12Scustomers/{customer_id}/campaignCustomizers/{campaign_id}~{customizer_attribute_id}B\x89\x02\n&com.google.ads.googleads.v16.resourcesB\x17CampaignCustomizerProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v16/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V16.Resources\xca\x02"Google\\Ads\\GoogleAds\\V16\\Resources\xea\x02&Google::Ads::GoogleAds::V16::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v16.resources.campaign_customizer_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v16.resourcesB\x17CampaignCustomizerProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v16/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V16.Resources\xca\x02"Google\\Ads\\GoogleAds\\V16\\Resources\xea\x02&Google::Ads::GoogleAds::V16::Resources'
    _globals['_CAMPAIGNCUSTOMIZER'].fields_by_name['resource_name']._loaded_options = None
    _globals['_CAMPAIGNCUSTOMIZER'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x05\xfaA-\n+googleads.googleapis.com/CampaignCustomizer'
    _globals['_CAMPAIGNCUSTOMIZER'].fields_by_name['campaign']._loaded_options = None
    _globals['_CAMPAIGNCUSTOMIZER'].fields_by_name['campaign']._serialized_options = b'\xe0A\x05\xfaA#\n!googleads.googleapis.com/Campaign'
    _globals['_CAMPAIGNCUSTOMIZER'].fields_by_name['customizer_attribute']._loaded_options = None
    _globals['_CAMPAIGNCUSTOMIZER'].fields_by_name['customizer_attribute']._serialized_options = b'\xe0A\x02\xe0A\x05\xfaA.\n,googleads.googleapis.com/CustomizerAttribute'
    _globals['_CAMPAIGNCUSTOMIZER'].fields_by_name['status']._loaded_options = None
    _globals['_CAMPAIGNCUSTOMIZER'].fields_by_name['status']._serialized_options = b'\xe0A\x03'
    _globals['_CAMPAIGNCUSTOMIZER'].fields_by_name['value']._loaded_options = None
    _globals['_CAMPAIGNCUSTOMIZER'].fields_by_name['value']._serialized_options = b'\xe0A\x02'
    _globals['_CAMPAIGNCUSTOMIZER']._loaded_options = None
    _globals['_CAMPAIGNCUSTOMIZER']._serialized_options = b'\xeaA\x82\x01\n+googleads.googleapis.com/CampaignCustomizer\x12Scustomers/{customer_id}/campaignCustomizers/{campaign_id}~{customizer_attribute_id}'
    _globals['_CAMPAIGNCUSTOMIZER']._serialized_start = 279
    _globals['_CAMPAIGNCUSTOMIZER']._serialized_end = 832