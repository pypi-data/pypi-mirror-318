"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ads/googleads/v16/services/conversion_value_rule_set_service.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v16.enums import response_content_type_pb2 as google_dot_ads_dot_googleads_dot_v16_dot_enums_dot_response__content__type__pb2
from ......google.ads.googleads.v16.resources import conversion_value_rule_set_pb2 as google_dot_ads_dot_googleads_dot_v16_dot_resources_dot_conversion__value__rule__set__pb2
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from ......google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nIgoogle/ads/googleads/v16/services/conversion_value_rule_set_service.proto\x12!google.ads.googleads.v16.services\x1a:google/ads/googleads/v16/enums/response_content_type.proto\x1aBgoogle/ads/googleads/v16/resources/conversion_value_rule_set.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto\x1a\x17google/rpc/status.proto"\xb9\x02\n$MutateConversionValueRuleSetsRequest\x12\x18\n\x0bcustomer_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12[\n\noperations\x18\x02 \x03(\x0b2B.google.ads.googleads.v16.services.ConversionValueRuleSetOperationB\x03\xe0A\x02\x12\x17\n\x0fpartial_failure\x18\x05 \x01(\x08\x12\x15\n\rvalidate_only\x18\x03 \x01(\x08\x12j\n\x15response_content_type\x18\x04 \x01(\x0e2K.google.ads.googleads.v16.enums.ResponseContentTypeEnum.ResponseContentType"\xc3\x02\n\x1fConversionValueRuleSetOperation\x12/\n\x0bupdate_mask\x18\x04 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12L\n\x06create\x18\x01 \x01(\x0b2:.google.ads.googleads.v16.resources.ConversionValueRuleSetH\x00\x12L\n\x06update\x18\x02 \x01(\x0b2:.google.ads.googleads.v16.resources.ConversionValueRuleSetH\x00\x12F\n\x06remove\x18\x03 \x01(\tB4\xfaA1\n/googleads.googleapis.com/ConversionValueRuleSetH\x00B\x0b\n\toperation"\xb2\x01\n%MutateConversionValueRuleSetsResponse\x12V\n\x07results\x18\x01 \x03(\x0b2E.google.ads.googleads.v16.services.MutateConversionValueRuleSetResult\x121\n\x15partial_failure_error\x18\x02 \x01(\x0b2\x12.google.rpc.Status"\xd0\x01\n"MutateConversionValueRuleSetResult\x12K\n\rresource_name\x18\x01 \x01(\tB4\xfaA1\n/googleads.googleapis.com/ConversionValueRuleSet\x12]\n\x19conversion_value_rule_set\x18\x02 \x01(\x0b2:.google.ads.googleads.v16.resources.ConversionValueRuleSet2\xfe\x02\n\x1dConversionValueRuleSetService\x12\x95\x02\n\x1dMutateConversionValueRuleSets\x12G.google.ads.googleads.v16.services.MutateConversionValueRuleSetsRequest\x1aH.google.ads.googleads.v16.services.MutateConversionValueRuleSetsResponse"a\xdaA\x16customer_id,operations\x82\xd3\xe4\x93\x02B"=/v16/customers/{customer_id=*}/conversionValueRuleSets:mutate:\x01*\x1aE\xcaA\x18googleads.googleapis.com\xd2A\'https://www.googleapis.com/auth/adwordsB\x8e\x02\n%com.google.ads.googleads.v16.servicesB"ConversionValueRuleSetServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v16/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V16.Services\xca\x02!Google\\Ads\\GoogleAds\\V16\\Services\xea\x02%Google::Ads::GoogleAds::V16::Servicesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v16.services.conversion_value_rule_set_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.ads.googleads.v16.servicesB"ConversionValueRuleSetServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v16/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V16.Services\xca\x02!Google\\Ads\\GoogleAds\\V16\\Services\xea\x02%Google::Ads::GoogleAds::V16::Services'
    _globals['_MUTATECONVERSIONVALUERULESETSREQUEST'].fields_by_name['customer_id']._loaded_options = None
    _globals['_MUTATECONVERSIONVALUERULESETSREQUEST'].fields_by_name['customer_id']._serialized_options = b'\xe0A\x02'
    _globals['_MUTATECONVERSIONVALUERULESETSREQUEST'].fields_by_name['operations']._loaded_options = None
    _globals['_MUTATECONVERSIONVALUERULESETSREQUEST'].fields_by_name['operations']._serialized_options = b'\xe0A\x02'
    _globals['_CONVERSIONVALUERULESETOPERATION'].fields_by_name['remove']._loaded_options = None
    _globals['_CONVERSIONVALUERULESETOPERATION'].fields_by_name['remove']._serialized_options = b'\xfaA1\n/googleads.googleapis.com/ConversionValueRuleSet'
    _globals['_MUTATECONVERSIONVALUERULESETRESULT'].fields_by_name['resource_name']._loaded_options = None
    _globals['_MUTATECONVERSIONVALUERULESETRESULT'].fields_by_name['resource_name']._serialized_options = b'\xfaA1\n/googleads.googleapis.com/ConversionValueRuleSet'
    _globals['_CONVERSIONVALUERULESETSERVICE']._loaded_options = None
    _globals['_CONVERSIONVALUERULESETSERVICE']._serialized_options = b"\xcaA\x18googleads.googleapis.com\xd2A'https://www.googleapis.com/auth/adwords"
    _globals['_CONVERSIONVALUERULESETSERVICE'].methods_by_name['MutateConversionValueRuleSets']._loaded_options = None
    _globals['_CONVERSIONVALUERULESETSERVICE'].methods_by_name['MutateConversionValueRuleSets']._serialized_options = b'\xdaA\x16customer_id,operations\x82\xd3\xe4\x93\x02B"=/v16/customers/{customer_id=*}/conversionValueRuleSets:mutate:\x01*'
    _globals['_MUTATECONVERSIONVALUERULESETSREQUEST']._serialized_start = 415
    _globals['_MUTATECONVERSIONVALUERULESETSREQUEST']._serialized_end = 728
    _globals['_CONVERSIONVALUERULESETOPERATION']._serialized_start = 731
    _globals['_CONVERSIONVALUERULESETOPERATION']._serialized_end = 1054
    _globals['_MUTATECONVERSIONVALUERULESETSRESPONSE']._serialized_start = 1057
    _globals['_MUTATECONVERSIONVALUERULESETSRESPONSE']._serialized_end = 1235
    _globals['_MUTATECONVERSIONVALUERULESETRESULT']._serialized_start = 1238
    _globals['_MUTATECONVERSIONVALUERULESETRESULT']._serialized_end = 1446
    _globals['_CONVERSIONVALUERULESETSERVICE']._serialized_start = 1449
    _globals['_CONVERSIONVALUERULESETSERVICE']._serialized_end = 1831