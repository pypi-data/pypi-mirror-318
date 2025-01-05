"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ads/googleads/v18/resources/conversion_custom_variable.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v18.enums import conversion_custom_variable_status_pb2 as google_dot_ads_dot_googleads_dot_v18_dot_enums_dot_conversion__custom__variable__status__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nCgoogle/ads/googleads/v18/resources/conversion_custom_variable.proto\x12"google.ads.googleads.v18.resources\x1aFgoogle/ads/googleads/v18/enums/conversion_custom_variable_status.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xe8\x03\n\x18ConversionCustomVariable\x12P\n\rresource_name\x18\x01 \x01(\tB9\xe0A\x05\xfaA3\n1googleads.googleapis.com/ConversionCustomVariable\x12\x0f\n\x02id\x18\x02 \x01(\x03B\x03\xe0A\x03\x12\x11\n\x04name\x18\x03 \x01(\tB\x03\xe0A\x02\x12\x13\n\x03tag\x18\x04 \x01(\tB\x06\xe0A\x02\xe0A\x05\x12q\n\x06status\x18\x05 \x01(\x0e2a.google.ads.googleads.v18.enums.ConversionCustomVariableStatusEnum.ConversionCustomVariableStatus\x12A\n\x0eowner_customer\x18\x06 \x01(\tB)\xe0A\x03\xfaA#\n!googleads.googleapis.com/Customer:\x8a\x01\xeaA\x86\x01\n1googleads.googleapis.com/ConversionCustomVariable\x12Qcustomers/{customer_id}/conversionCustomVariables/{conversion_custom_variable_id}B\x8f\x02\n&com.google.ads.googleads.v18.resourcesB\x1dConversionCustomVariableProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v18/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V18.Resources\xca\x02"Google\\Ads\\GoogleAds\\V18\\Resources\xea\x02&Google::Ads::GoogleAds::V18::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v18.resources.conversion_custom_variable_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v18.resourcesB\x1dConversionCustomVariableProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v18/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V18.Resources\xca\x02"Google\\Ads\\GoogleAds\\V18\\Resources\xea\x02&Google::Ads::GoogleAds::V18::Resources'
    _globals['_CONVERSIONCUSTOMVARIABLE'].fields_by_name['resource_name']._loaded_options = None
    _globals['_CONVERSIONCUSTOMVARIABLE'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x05\xfaA3\n1googleads.googleapis.com/ConversionCustomVariable'
    _globals['_CONVERSIONCUSTOMVARIABLE'].fields_by_name['id']._loaded_options = None
    _globals['_CONVERSIONCUSTOMVARIABLE'].fields_by_name['id']._serialized_options = b'\xe0A\x03'
    _globals['_CONVERSIONCUSTOMVARIABLE'].fields_by_name['name']._loaded_options = None
    _globals['_CONVERSIONCUSTOMVARIABLE'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_CONVERSIONCUSTOMVARIABLE'].fields_by_name['tag']._loaded_options = None
    _globals['_CONVERSIONCUSTOMVARIABLE'].fields_by_name['tag']._serialized_options = b'\xe0A\x02\xe0A\x05'
    _globals['_CONVERSIONCUSTOMVARIABLE'].fields_by_name['owner_customer']._loaded_options = None
    _globals['_CONVERSIONCUSTOMVARIABLE'].fields_by_name['owner_customer']._serialized_options = b'\xe0A\x03\xfaA#\n!googleads.googleapis.com/Customer'
    _globals['_CONVERSIONCUSTOMVARIABLE']._loaded_options = None
    _globals['_CONVERSIONCUSTOMVARIABLE']._serialized_options = b'\xeaA\x86\x01\n1googleads.googleapis.com/ConversionCustomVariable\x12Qcustomers/{customer_id}/conversionCustomVariables/{conversion_custom_variable_id}'
    _globals['_CONVERSIONCUSTOMVARIABLE']._serialized_start = 240
    _globals['_CONVERSIONCUSTOMVARIABLE']._serialized_end = 728