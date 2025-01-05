"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ads/googleads/v17/resources/custom_audience.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v17.enums import custom_audience_member_type_pb2 as google_dot_ads_dot_googleads_dot_v17_dot_enums_dot_custom__audience__member__type__pb2
from ......google.ads.googleads.v17.enums import custom_audience_status_pb2 as google_dot_ads_dot_googleads_dot_v17_dot_enums_dot_custom__audience__status__pb2
from ......google.ads.googleads.v17.enums import custom_audience_type_pb2 as google_dot_ads_dot_googleads_dot_v17_dot_enums_dot_custom__audience__type__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8google/ads/googleads/v17/resources/custom_audience.proto\x12"google.ads.googleads.v17.resources\x1a@google/ads/googleads/v17/enums/custom_audience_member_type.proto\x1a;google/ads/googleads/v17/enums/custom_audience_status.proto\x1a9google/ads/googleads/v17/enums/custom_audience_type.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\x80\x04\n\x0eCustomAudience\x12F\n\rresource_name\x18\x01 \x01(\tB/\xe0A\x05\xfaA)\n\'googleads.googleapis.com/CustomAudience\x12\x0f\n\x02id\x18\x02 \x01(\x03B\x03\xe0A\x03\x12b\n\x06status\x18\x03 \x01(\x0e2M.google.ads.googleads.v17.enums.CustomAudienceStatusEnum.CustomAudienceStatusB\x03\xe0A\x03\x12\x0c\n\x04name\x18\x04 \x01(\t\x12W\n\x04type\x18\x05 \x01(\x0e2I.google.ads.googleads.v17.enums.CustomAudienceTypeEnum.CustomAudienceType\x12\x13\n\x0bdescription\x18\x06 \x01(\t\x12I\n\x07members\x18\x07 \x03(\x0b28.google.ads.googleads.v17.resources.CustomAudienceMember:j\xeaAg\n\'googleads.googleapis.com/CustomAudience\x12<customers/{customer_id}/customAudiences/{custom_audience_id}"\xd6\x01\n\x14CustomAudienceMember\x12j\n\x0bmember_type\x18\x01 \x01(\x0e2U.google.ads.googleads.v17.enums.CustomAudienceMemberTypeEnum.CustomAudienceMemberType\x12\x11\n\x07keyword\x18\x02 \x01(\tH\x00\x12\r\n\x03url\x18\x03 \x01(\tH\x00\x12\x18\n\x0eplace_category\x18\x04 \x01(\x03H\x00\x12\r\n\x03app\x18\x05 \x01(\tH\x00B\x07\n\x05valueB\x85\x02\n&com.google.ads.googleads.v17.resourcesB\x13CustomAudienceProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v17/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V17.Resources\xca\x02"Google\\Ads\\GoogleAds\\V17\\Resources\xea\x02&Google::Ads::GoogleAds::V17::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v17.resources.custom_audience_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v17.resourcesB\x13CustomAudienceProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v17/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V17.Resources\xca\x02"Google\\Ads\\GoogleAds\\V17\\Resources\xea\x02&Google::Ads::GoogleAds::V17::Resources'
    _globals['_CUSTOMAUDIENCE'].fields_by_name['resource_name']._loaded_options = None
    _globals['_CUSTOMAUDIENCE'].fields_by_name['resource_name']._serialized_options = b"\xe0A\x05\xfaA)\n'googleads.googleapis.com/CustomAudience"
    _globals['_CUSTOMAUDIENCE'].fields_by_name['id']._loaded_options = None
    _globals['_CUSTOMAUDIENCE'].fields_by_name['id']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMAUDIENCE'].fields_by_name['status']._loaded_options = None
    _globals['_CUSTOMAUDIENCE'].fields_by_name['status']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMAUDIENCE']._loaded_options = None
    _globals['_CUSTOMAUDIENCE']._serialized_options = b"\xeaAg\n'googleads.googleapis.com/CustomAudience\x12<customers/{customer_id}/customAudiences/{custom_audience_id}"
    _globals['_CUSTOMAUDIENCE']._serialized_start = 343
    _globals['_CUSTOMAUDIENCE']._serialized_end = 855
    _globals['_CUSTOMAUDIENCEMEMBER']._serialized_start = 858
    _globals['_CUSTOMAUDIENCEMEMBER']._serialized_end = 1072