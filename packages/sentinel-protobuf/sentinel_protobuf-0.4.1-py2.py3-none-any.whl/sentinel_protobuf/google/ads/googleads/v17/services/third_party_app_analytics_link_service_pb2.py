"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ads/googleads/v17/services/third_party_app_analytics_link_service.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nNgoogle/ads/googleads/v17/services/third_party_app_analytics_link_service.proto\x12!google.ads.googleads.v17.services\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x19google/api/resource.proto"s\n RegenerateShareableLinkIdRequest\x12O\n\rresource_name\x18\x01 \x01(\tB8\xfaA5\n3googleads.googleapis.com/ThirdPartyAppAnalyticsLink"#\n!RegenerateShareableLinkIdResponse2\xf8\x02\n!ThirdPartyAppAnalyticsLinkService\x12\x8b\x02\n\x19RegenerateShareableLinkId\x12C.google.ads.googleads.v17.services.RegenerateShareableLinkIdRequest\x1aD.google.ads.googleads.v17.services.RegenerateShareableLinkIdResponse"c\x82\xd3\xe4\x93\x02]"X/v17/{resource_name=customers/*/thirdPartyAppAnalyticsLinks/*}:regenerateShareableLinkId:\x01*\x1aE\xcaA\x18googleads.googleapis.com\xd2A\'https://www.googleapis.com/auth/adwordsB\x92\x02\n%com.google.ads.googleads.v17.servicesB&ThirdPartyAppAnalyticsLinkServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v17/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V17.Services\xca\x02!Google\\Ads\\GoogleAds\\V17\\Services\xea\x02%Google::Ads::GoogleAds::V17::Servicesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v17.services.third_party_app_analytics_link_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.ads.googleads.v17.servicesB&ThirdPartyAppAnalyticsLinkServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v17/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V17.Services\xca\x02!Google\\Ads\\GoogleAds\\V17\\Services\xea\x02%Google::Ads::GoogleAds::V17::Services'
    _globals['_REGENERATESHAREABLELINKIDREQUEST'].fields_by_name['resource_name']._loaded_options = None
    _globals['_REGENERATESHAREABLELINKIDREQUEST'].fields_by_name['resource_name']._serialized_options = b'\xfaA5\n3googleads.googleapis.com/ThirdPartyAppAnalyticsLink'
    _globals['_THIRDPARTYAPPANALYTICSLINKSERVICE']._loaded_options = None
    _globals['_THIRDPARTYAPPANALYTICSLINKSERVICE']._serialized_options = b"\xcaA\x18googleads.googleapis.com\xd2A'https://www.googleapis.com/auth/adwords"
    _globals['_THIRDPARTYAPPANALYTICSLINKSERVICE'].methods_by_name['RegenerateShareableLinkId']._loaded_options = None
    _globals['_THIRDPARTYAPPANALYTICSLINKSERVICE'].methods_by_name['RegenerateShareableLinkId']._serialized_options = b'\x82\xd3\xe4\x93\x02]"X/v17/{resource_name=customers/*/thirdPartyAppAnalyticsLinks/*}:regenerateShareableLinkId:\x01*'
    _globals['_REGENERATESHAREABLELINKIDREQUEST']._serialized_start = 199
    _globals['_REGENERATESHAREABLELINKIDREQUEST']._serialized_end = 314
    _globals['_REGENERATESHAREABLELINKIDRESPONSE']._serialized_start = 316
    _globals['_REGENERATESHAREABLELINKIDRESPONSE']._serialized_end = 351
    _globals['_THIRDPARTYAPPANALYTICSLINKSERVICE']._serialized_start = 354
    _globals['_THIRDPARTYAPPANALYTICSLINKSERVICE']._serialized_end = 730