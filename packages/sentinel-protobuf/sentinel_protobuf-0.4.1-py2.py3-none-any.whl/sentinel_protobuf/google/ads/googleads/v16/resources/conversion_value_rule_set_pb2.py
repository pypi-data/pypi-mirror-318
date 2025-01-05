"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ads/googleads/v16/resources/conversion_value_rule_set.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v16.enums import conversion_action_category_pb2 as google_dot_ads_dot_googleads_dot_v16_dot_enums_dot_conversion__action__category__pb2
from ......google.ads.googleads.v16.enums import conversion_value_rule_set_status_pb2 as google_dot_ads_dot_googleads_dot_v16_dot_enums_dot_conversion__value__rule__set__status__pb2
from ......google.ads.googleads.v16.enums import value_rule_set_attachment_type_pb2 as google_dot_ads_dot_googleads_dot_v16_dot_enums_dot_value__rule__set__attachment__type__pb2
from ......google.ads.googleads.v16.enums import value_rule_set_dimension_pb2 as google_dot_ads_dot_googleads_dot_v16_dot_enums_dot_value__rule__set__dimension__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nBgoogle/ads/googleads/v16/resources/conversion_value_rule_set.proto\x12"google.ads.googleads.v16.resources\x1a?google/ads/googleads/v16/enums/conversion_action_category.proto\x1aEgoogle/ads/googleads/v16/enums/conversion_value_rule_set_status.proto\x1aCgoogle/ads/googleads/v16/enums/value_rule_set_attachment_type.proto\x1a=google/ads/googleads/v16/enums/value_rule_set_dimension.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xa6\x07\n\x16ConversionValueRuleSet\x12N\n\rresource_name\x18\x01 \x01(\tB7\xe0A\x05\xfaA1\n/googleads.googleapis.com/ConversionValueRuleSet\x12\x0f\n\x02id\x18\x02 \x01(\x03B\x03\xe0A\x03\x12Q\n\x16conversion_value_rules\x18\x03 \x03(\tB1\xfaA.\n,googleads.googleapis.com/ConversionValueRule\x12c\n\ndimensions\x18\x04 \x03(\x0e2O.google.ads.googleads.v16.enums.ValueRuleSetDimensionEnum.ValueRuleSetDimension\x12A\n\x0eowner_customer\x18\x05 \x01(\tB)\xe0A\x03\xfaA#\n!googleads.googleapis.com/Customer\x12w\n\x0fattachment_type\x18\x06 \x01(\x0e2Y.google.ads.googleads.v16.enums.ValueRuleSetAttachmentTypeEnum.ValueRuleSetAttachmentTypeB\x03\xe0A\x05\x128\n\x08campaign\x18\x07 \x01(\tB&\xfaA#\n!googleads.googleapis.com/Campaign\x12r\n\x06status\x18\x08 \x01(\x0e2].google.ads.googleads.v16.enums.ConversionValueRuleSetStatusEnum.ConversionValueRuleSetStatusB\x03\xe0A\x03\x12\x80\x01\n\x1cconversion_action_categories\x18\t \x03(\x0e2U.google.ads.googleads.v16.enums.ConversionActionCategoryEnum.ConversionActionCategoryB\x03\xe0A\x05:\x85\x01\xeaA\x81\x01\n/googleads.googleapis.com/ConversionValueRuleSet\x12Ncustomers/{customer_id}/conversionValueRuleSets/{conversion_value_rule_set_id}B\x8d\x02\n&com.google.ads.googleads.v16.resourcesB\x1bConversionValueRuleSetProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v16/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V16.Resources\xca\x02"Google\\Ads\\GoogleAds\\V16\\Resources\xea\x02&Google::Ads::GoogleAds::V16::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v16.resources.conversion_value_rule_set_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v16.resourcesB\x1bConversionValueRuleSetProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v16/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V16.Resources\xca\x02"Google\\Ads\\GoogleAds\\V16\\Resources\xea\x02&Google::Ads::GoogleAds::V16::Resources'
    _globals['_CONVERSIONVALUERULESET'].fields_by_name['resource_name']._loaded_options = None
    _globals['_CONVERSIONVALUERULESET'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x05\xfaA1\n/googleads.googleapis.com/ConversionValueRuleSet'
    _globals['_CONVERSIONVALUERULESET'].fields_by_name['id']._loaded_options = None
    _globals['_CONVERSIONVALUERULESET'].fields_by_name['id']._serialized_options = b'\xe0A\x03'
    _globals['_CONVERSIONVALUERULESET'].fields_by_name['conversion_value_rules']._loaded_options = None
    _globals['_CONVERSIONVALUERULESET'].fields_by_name['conversion_value_rules']._serialized_options = b'\xfaA.\n,googleads.googleapis.com/ConversionValueRule'
    _globals['_CONVERSIONVALUERULESET'].fields_by_name['owner_customer']._loaded_options = None
    _globals['_CONVERSIONVALUERULESET'].fields_by_name['owner_customer']._serialized_options = b'\xe0A\x03\xfaA#\n!googleads.googleapis.com/Customer'
    _globals['_CONVERSIONVALUERULESET'].fields_by_name['attachment_type']._loaded_options = None
    _globals['_CONVERSIONVALUERULESET'].fields_by_name['attachment_type']._serialized_options = b'\xe0A\x05'
    _globals['_CONVERSIONVALUERULESET'].fields_by_name['campaign']._loaded_options = None
    _globals['_CONVERSIONVALUERULESET'].fields_by_name['campaign']._serialized_options = b'\xfaA#\n!googleads.googleapis.com/Campaign'
    _globals['_CONVERSIONVALUERULESET'].fields_by_name['status']._loaded_options = None
    _globals['_CONVERSIONVALUERULESET'].fields_by_name['status']._serialized_options = b'\xe0A\x03'
    _globals['_CONVERSIONVALUERULESET'].fields_by_name['conversion_action_categories']._loaded_options = None
    _globals['_CONVERSIONVALUERULESET'].fields_by_name['conversion_action_categories']._serialized_options = b'\xe0A\x05'
    _globals['_CONVERSIONVALUERULESET']._loaded_options = None
    _globals['_CONVERSIONVALUERULESET']._serialized_options = b'\xeaA\x81\x01\n/googleads.googleapis.com/ConversionValueRuleSet\x12Ncustomers/{customer_id}/conversionValueRuleSets/{conversion_value_rule_set_id}'
    _globals['_CONVERSIONVALUERULESET']._serialized_start = 435
    _globals['_CONVERSIONVALUERULESET']._serialized_end = 1369