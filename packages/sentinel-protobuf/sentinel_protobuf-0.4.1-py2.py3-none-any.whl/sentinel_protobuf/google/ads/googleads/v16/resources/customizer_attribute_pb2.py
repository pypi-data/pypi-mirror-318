"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ads/googleads/v16/resources/customizer_attribute.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v16.enums import customizer_attribute_status_pb2 as google_dot_ads_dot_googleads_dot_v16_dot_enums_dot_customizer__attribute__status__pb2
from ......google.ads.googleads.v16.enums import customizer_attribute_type_pb2 as google_dot_ads_dot_googleads_dot_v16_dot_enums_dot_customizer__attribute__type__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n=google/ads/googleads/v16/resources/customizer_attribute.proto\x12"google.ads.googleads.v16.resources\x1a@google/ads/googleads/v16/enums/customizer_attribute_status.proto\x1a>google/ads/googleads/v16/enums/customizer_attribute_type.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xda\x03\n\x13CustomizerAttribute\x12K\n\rresource_name\x18\x01 \x01(\tB4\xe0A\x05\xfaA.\n,googleads.googleapis.com/CustomizerAttribute\x12\x0f\n\x02id\x18\x02 \x01(\x03B\x03\xe0A\x03\x12\x14\n\x04name\x18\x03 \x01(\tB\x06\xe0A\x02\xe0A\x05\x12f\n\x04type\x18\x04 \x01(\x0e2S.google.ads.googleads.v16.enums.CustomizerAttributeTypeEnum.CustomizerAttributeTypeB\x03\xe0A\x05\x12l\n\x06status\x18\x05 \x01(\x0e2W.google.ads.googleads.v16.enums.CustomizerAttributeStatusEnum.CustomizerAttributeStatusB\x03\xe0A\x03:y\xeaAv\n,googleads.googleapis.com/CustomizerAttribute\x12Fcustomers/{customer_id}/customizerAttributes/{customizer_attribute_id}B\x8a\x02\n&com.google.ads.googleads.v16.resourcesB\x18CustomizerAttributeProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v16/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V16.Resources\xca\x02"Google\\Ads\\GoogleAds\\V16\\Resources\xea\x02&Google::Ads::GoogleAds::V16::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v16.resources.customizer_attribute_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v16.resourcesB\x18CustomizerAttributeProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v16/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V16.Resources\xca\x02"Google\\Ads\\GoogleAds\\V16\\Resources\xea\x02&Google::Ads::GoogleAds::V16::Resources'
    _globals['_CUSTOMIZERATTRIBUTE'].fields_by_name['resource_name']._loaded_options = None
    _globals['_CUSTOMIZERATTRIBUTE'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x05\xfaA.\n,googleads.googleapis.com/CustomizerAttribute'
    _globals['_CUSTOMIZERATTRIBUTE'].fields_by_name['id']._loaded_options = None
    _globals['_CUSTOMIZERATTRIBUTE'].fields_by_name['id']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMIZERATTRIBUTE'].fields_by_name['name']._loaded_options = None
    _globals['_CUSTOMIZERATTRIBUTE'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xe0A\x05'
    _globals['_CUSTOMIZERATTRIBUTE'].fields_by_name['type']._loaded_options = None
    _globals['_CUSTOMIZERATTRIBUTE'].fields_by_name['type']._serialized_options = b'\xe0A\x05'
    _globals['_CUSTOMIZERATTRIBUTE'].fields_by_name['status']._loaded_options = None
    _globals['_CUSTOMIZERATTRIBUTE'].fields_by_name['status']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMIZERATTRIBUTE']._loaded_options = None
    _globals['_CUSTOMIZERATTRIBUTE']._serialized_options = b'\xeaAv\n,googleads.googleapis.com/CustomizerAttribute\x12Fcustomers/{customer_id}/customizerAttributes/{customizer_attribute_id}'
    _globals['_CUSTOMIZERATTRIBUTE']._serialized_start = 292
    _globals['_CUSTOMIZERATTRIBUTE']._serialized_end = 766