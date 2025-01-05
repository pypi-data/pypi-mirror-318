"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ads/googleads/v17/resources/conversion_value_rule.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v17.enums import conversion_value_rule_status_pb2 as google_dot_ads_dot_googleads_dot_v17_dot_enums_dot_conversion__value__rule__status__pb2
from ......google.ads.googleads.v17.enums import value_rule_device_type_pb2 as google_dot_ads_dot_googleads_dot_v17_dot_enums_dot_value__rule__device__type__pb2
from ......google.ads.googleads.v17.enums import value_rule_geo_location_match_type_pb2 as google_dot_ads_dot_googleads_dot_v17_dot_enums_dot_value__rule__geo__location__match__type__pb2
from ......google.ads.googleads.v17.enums import value_rule_operation_pb2 as google_dot_ads_dot_googleads_dot_v17_dot_enums_dot_value__rule__operation__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n>google/ads/googleads/v17/resources/conversion_value_rule.proto\x12"google.ads.googleads.v17.resources\x1aAgoogle/ads/googleads/v17/enums/conversion_value_rule_status.proto\x1a;google/ads/googleads/v17/enums/value_rule_device_type.proto\x1aGgoogle/ads/googleads/v17/enums/value_rule_geo_location_match_type.proto\x1a9google/ads/googleads/v17/enums/value_rule_operation.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xaa\r\n\x13ConversionValueRule\x12K\n\rresource_name\x18\x01 \x01(\tB4\xe0A\x05\xfaA.\n,googleads.googleapis.com/ConversionValueRule\x12\x0f\n\x02id\x18\x02 \x01(\x03B\x03\xe0A\x03\x12W\n\x06action\x18\x03 \x01(\x0b2G.google.ads.googleads.v17.resources.ConversionValueRule.ValueRuleAction\x12u\n\x16geo_location_condition\x18\x04 \x01(\x0b2U.google.ads.googleads.v17.resources.ConversionValueRule.ValueRuleGeoLocationCondition\x12j\n\x10device_condition\x18\x05 \x01(\x0b2P.google.ads.googleads.v17.resources.ConversionValueRule.ValueRuleDeviceCondition\x12n\n\x12audience_condition\x18\x06 \x01(\x0b2R.google.ads.googleads.v17.resources.ConversionValueRule.ValueRuleAudienceCondition\x12A\n\x0eowner_customer\x18\x07 \x01(\tB)\xe0A\x03\xfaA#\n!googleads.googleapis.com/Customer\x12g\n\x06status\x18\x08 \x01(\x0e2W.google.ads.googleads.v17.enums.ConversionValueRuleStatusEnum.ConversionValueRuleStatus\x1a~\n\x0fValueRuleAction\x12\\\n\toperation\x18\x01 \x01(\x0e2I.google.ads.googleads.v17.enums.ValueRuleOperationEnum.ValueRuleOperation\x12\r\n\x05value\x18\x02 \x01(\x01\x1a\xc2\x03\n\x1dValueRuleGeoLocationCondition\x12V\n\x1dexcluded_geo_target_constants\x18\x01 \x03(\tB/\xfaA,\n*googleads.googleapis.com/GeoTargetConstant\x12\x80\x01\n\x17excluded_geo_match_type\x18\x02 \x01(\x0e2_.google.ads.googleads.v17.enums.ValueRuleGeoLocationMatchTypeEnum.ValueRuleGeoLocationMatchType\x12M\n\x14geo_target_constants\x18\x03 \x03(\tB/\xfaA,\n*googleads.googleapis.com/GeoTargetConstant\x12w\n\x0egeo_match_type\x18\x04 \x01(\x0e2_.google.ads.googleads.v17.enums.ValueRuleGeoLocationMatchTypeEnum.ValueRuleGeoLocationMatchType\x1a}\n\x18ValueRuleDeviceCondition\x12a\n\x0cdevice_types\x18\x01 \x03(\x0e2K.google.ads.googleads.v17.enums.ValueRuleDeviceTypeEnum.ValueRuleDeviceType\x1a\x9c\x01\n\x1aValueRuleAudienceCondition\x12:\n\nuser_lists\x18\x01 \x03(\tB&\xfaA#\n!googleads.googleapis.com/UserList\x12B\n\x0euser_interests\x18\x02 \x03(\tB*\xfaA\'\n%googleads.googleapis.com/UserInterest:z\xeaAw\n,googleads.googleapis.com/ConversionValueRule\x12Gcustomers/{customer_id}/conversionValueRules/{conversion_value_rule_id}B\x8a\x02\n&com.google.ads.googleads.v17.resourcesB\x18ConversionValueRuleProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v17/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V17.Resources\xca\x02"Google\\Ads\\GoogleAds\\V17\\Resources\xea\x02&Google::Ads::GoogleAds::V17::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v17.resources.conversion_value_rule_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v17.resourcesB\x18ConversionValueRuleProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v17/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V17.Resources\xca\x02"Google\\Ads\\GoogleAds\\V17\\Resources\xea\x02&Google::Ads::GoogleAds::V17::Resources'
    _globals['_CONVERSIONVALUERULE_VALUERULEGEOLOCATIONCONDITION'].fields_by_name['excluded_geo_target_constants']._loaded_options = None
    _globals['_CONVERSIONVALUERULE_VALUERULEGEOLOCATIONCONDITION'].fields_by_name['excluded_geo_target_constants']._serialized_options = b'\xfaA,\n*googleads.googleapis.com/GeoTargetConstant'
    _globals['_CONVERSIONVALUERULE_VALUERULEGEOLOCATIONCONDITION'].fields_by_name['geo_target_constants']._loaded_options = None
    _globals['_CONVERSIONVALUERULE_VALUERULEGEOLOCATIONCONDITION'].fields_by_name['geo_target_constants']._serialized_options = b'\xfaA,\n*googleads.googleapis.com/GeoTargetConstant'
    _globals['_CONVERSIONVALUERULE_VALUERULEAUDIENCECONDITION'].fields_by_name['user_lists']._loaded_options = None
    _globals['_CONVERSIONVALUERULE_VALUERULEAUDIENCECONDITION'].fields_by_name['user_lists']._serialized_options = b'\xfaA#\n!googleads.googleapis.com/UserList'
    _globals['_CONVERSIONVALUERULE_VALUERULEAUDIENCECONDITION'].fields_by_name['user_interests']._loaded_options = None
    _globals['_CONVERSIONVALUERULE_VALUERULEAUDIENCECONDITION'].fields_by_name['user_interests']._serialized_options = b"\xfaA'\n%googleads.googleapis.com/UserInterest"
    _globals['_CONVERSIONVALUERULE'].fields_by_name['resource_name']._loaded_options = None
    _globals['_CONVERSIONVALUERULE'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x05\xfaA.\n,googleads.googleapis.com/ConversionValueRule'
    _globals['_CONVERSIONVALUERULE'].fields_by_name['id']._loaded_options = None
    _globals['_CONVERSIONVALUERULE'].fields_by_name['id']._serialized_options = b'\xe0A\x03'
    _globals['_CONVERSIONVALUERULE'].fields_by_name['owner_customer']._loaded_options = None
    _globals['_CONVERSIONVALUERULE'].fields_by_name['owner_customer']._serialized_options = b'\xe0A\x03\xfaA#\n!googleads.googleapis.com/Customer'
    _globals['_CONVERSIONVALUERULE']._loaded_options = None
    _globals['_CONVERSIONVALUERULE']._serialized_options = b'\xeaAw\n,googleads.googleapis.com/ConversionValueRule\x12Gcustomers/{customer_id}/conversionValueRules/{conversion_value_rule_id}'
    _globals['_CONVERSIONVALUERULE']._serialized_start = 423
    _globals['_CONVERSIONVALUERULE']._serialized_end = 2129
    _globals['_CONVERSIONVALUERULE_VALUERULEACTION']._serialized_start = 1140
    _globals['_CONVERSIONVALUERULE_VALUERULEACTION']._serialized_end = 1266
    _globals['_CONVERSIONVALUERULE_VALUERULEGEOLOCATIONCONDITION']._serialized_start = 1269
    _globals['_CONVERSIONVALUERULE_VALUERULEGEOLOCATIONCONDITION']._serialized_end = 1719
    _globals['_CONVERSIONVALUERULE_VALUERULEDEVICECONDITION']._serialized_start = 1721
    _globals['_CONVERSIONVALUERULE_VALUERULEDEVICECONDITION']._serialized_end = 1846
    _globals['_CONVERSIONVALUERULE_VALUERULEAUDIENCECONDITION']._serialized_start = 1849
    _globals['_CONVERSIONVALUERULE_VALUERULEAUDIENCECONDITION']._serialized_end = 2005