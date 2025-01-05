"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ads/googleads/v16/common/customizer_value.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v16.enums import customizer_attribute_type_pb2 as google_dot_ads_dot_googleads_dot_v16_dot_enums_dot_customizer__attribute__type__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6google/ads/googleads/v16/common/customizer_value.proto\x12\x1fgoogle.ads.googleads.v16.common\x1a>google/ads/googleads/v16/enums/customizer_attribute_type.proto\x1a\x1fgoogle/api/field_behavior.proto"\x94\x01\n\x0fCustomizerValue\x12f\n\x04type\x18\x01 \x01(\x0e2S.google.ads.googleads.v16.enums.CustomizerAttributeTypeEnum.CustomizerAttributeTypeB\x03\xe0A\x02\x12\x19\n\x0cstring_value\x18\x02 \x01(\tB\x03\xe0A\x02B\xf4\x01\n#com.google.ads.googleads.v16.commonB\x14CustomizerValueProtoP\x01ZEgoogle.golang.org/genproto/googleapis/ads/googleads/v16/common;common\xa2\x02\x03GAA\xaa\x02\x1fGoogle.Ads.GoogleAds.V16.Common\xca\x02\x1fGoogle\\Ads\\GoogleAds\\V16\\Common\xea\x02#Google::Ads::GoogleAds::V16::Commonb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v16.common.customizer_value_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.ads.googleads.v16.commonB\x14CustomizerValueProtoP\x01ZEgoogle.golang.org/genproto/googleapis/ads/googleads/v16/common;common\xa2\x02\x03GAA\xaa\x02\x1fGoogle.Ads.GoogleAds.V16.Common\xca\x02\x1fGoogle\\Ads\\GoogleAds\\V16\\Common\xea\x02#Google::Ads::GoogleAds::V16::Common'
    _globals['_CUSTOMIZERVALUE'].fields_by_name['type']._loaded_options = None
    _globals['_CUSTOMIZERVALUE'].fields_by_name['type']._serialized_options = b'\xe0A\x02'
    _globals['_CUSTOMIZERVALUE'].fields_by_name['string_value']._loaded_options = None
    _globals['_CUSTOMIZERVALUE'].fields_by_name['string_value']._serialized_options = b'\xe0A\x02'
    _globals['_CUSTOMIZERVALUE']._serialized_start = 189
    _globals['_CUSTOMIZERVALUE']._serialized_end = 337