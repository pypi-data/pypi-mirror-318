"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ads/googleads/v17/resources/combined_audience.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v17.enums import combined_audience_status_pb2 as google_dot_ads_dot_googleads_dot_v17_dot_enums_dot_combined__audience__status__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:google/ads/googleads/v17/resources/combined_audience.proto\x12"google.ads.googleads.v17.resources\x1a=google/ads/googleads/v17/enums/combined_audience_status.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xf4\x02\n\x10CombinedAudience\x12H\n\rresource_name\x18\x01 \x01(\tB1\xe0A\x05\xfaA+\n)googleads.googleapis.com/CombinedAudience\x12\x0f\n\x02id\x18\x02 \x01(\x03B\x03\xe0A\x03\x12f\n\x06status\x18\x03 \x01(\x0e2Q.google.ads.googleads.v17.enums.CombinedAudienceStatusEnum.CombinedAudienceStatusB\x03\xe0A\x03\x12\x11\n\x04name\x18\x04 \x01(\tB\x03\xe0A\x03\x12\x18\n\x0bdescription\x18\x05 \x01(\tB\x03\xe0A\x03:p\xeaAm\n)googleads.googleapis.com/CombinedAudience\x12@customers/{customer_id}/combinedAudiences/{combined_audience_id}B\x87\x02\n&com.google.ads.googleads.v17.resourcesB\x15CombinedAudienceProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v17/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V17.Resources\xca\x02"Google\\Ads\\GoogleAds\\V17\\Resources\xea\x02&Google::Ads::GoogleAds::V17::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v17.resources.combined_audience_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v17.resourcesB\x15CombinedAudienceProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v17/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V17.Resources\xca\x02"Google\\Ads\\GoogleAds\\V17\\Resources\xea\x02&Google::Ads::GoogleAds::V17::Resources'
    _globals['_COMBINEDAUDIENCE'].fields_by_name['resource_name']._loaded_options = None
    _globals['_COMBINEDAUDIENCE'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x05\xfaA+\n)googleads.googleapis.com/CombinedAudience'
    _globals['_COMBINEDAUDIENCE'].fields_by_name['id']._loaded_options = None
    _globals['_COMBINEDAUDIENCE'].fields_by_name['id']._serialized_options = b'\xe0A\x03'
    _globals['_COMBINEDAUDIENCE'].fields_by_name['status']._loaded_options = None
    _globals['_COMBINEDAUDIENCE'].fields_by_name['status']._serialized_options = b'\xe0A\x03'
    _globals['_COMBINEDAUDIENCE'].fields_by_name['name']._loaded_options = None
    _globals['_COMBINEDAUDIENCE'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_COMBINEDAUDIENCE'].fields_by_name['description']._loaded_options = None
    _globals['_COMBINEDAUDIENCE'].fields_by_name['description']._serialized_options = b'\xe0A\x03'
    _globals['_COMBINEDAUDIENCE']._loaded_options = None
    _globals['_COMBINEDAUDIENCE']._serialized_options = b'\xeaAm\n)googleads.googleapis.com/CombinedAudience\x12@customers/{customer_id}/combinedAudiences/{combined_audience_id}'
    _globals['_COMBINEDAUDIENCE']._serialized_start = 222
    _globals['_COMBINEDAUDIENCE']._serialized_end = 594