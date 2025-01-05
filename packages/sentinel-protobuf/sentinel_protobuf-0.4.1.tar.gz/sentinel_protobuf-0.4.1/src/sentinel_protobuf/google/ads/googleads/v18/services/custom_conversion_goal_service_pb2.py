"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ads/googleads/v18/services/custom_conversion_goal_service.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v18.enums import response_content_type_pb2 as google_dot_ads_dot_googleads_dot_v18_dot_enums_dot_response__content__type__pb2
from ......google.ads.googleads.v18.resources import custom_conversion_goal_pb2 as google_dot_ads_dot_googleads_dot_v18_dot_resources_dot_custom__conversion__goal__pb2
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nFgoogle/ads/googleads/v18/services/custom_conversion_goal_service.proto\x12!google.ads.googleads.v18.services\x1a:google/ads/googleads/v18/enums/response_content_type.proto\x1a?google/ads/googleads/v18/resources/custom_conversion_goal.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto"\x9c\x02\n"MutateCustomConversionGoalsRequest\x12\x18\n\x0bcustomer_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12Y\n\noperations\x18\x02 \x03(\x0b2@.google.ads.googleads.v18.services.CustomConversionGoalOperationB\x03\xe0A\x02\x12\x15\n\rvalidate_only\x18\x03 \x01(\x08\x12j\n\x15response_content_type\x18\x04 \x01(\x0e2K.google.ads.googleads.v18.enums.ResponseContentTypeEnum.ResponseContentType"\xbb\x02\n\x1dCustomConversionGoalOperation\x12/\n\x0bupdate_mask\x18\x04 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12J\n\x06create\x18\x01 \x01(\x0b28.google.ads.googleads.v18.resources.CustomConversionGoalH\x00\x12J\n\x06update\x18\x02 \x01(\x0b28.google.ads.googleads.v18.resources.CustomConversionGoalH\x00\x12D\n\x06remove\x18\x03 \x01(\tB2\xfaA/\n-googleads.googleapis.com/CustomConversionGoalH\x00B\x0b\n\toperation"{\n#MutateCustomConversionGoalsResponse\x12T\n\x07results\x18\x01 \x03(\x0b2C.google.ads.googleads.v18.services.MutateCustomConversionGoalResult"\xc7\x01\n MutateCustomConversionGoalResult\x12I\n\rresource_name\x18\x01 \x01(\tB2\xfaA/\n-googleads.googleapis.com/CustomConversionGoal\x12X\n\x16custom_conversion_goal\x18\x02 \x01(\x0b28.google.ads.googleads.v18.resources.CustomConversionGoal2\xf4\x02\n\x1bCustomConversionGoalService\x12\x8d\x02\n\x1bMutateCustomConversionGoals\x12E.google.ads.googleads.v18.services.MutateCustomConversionGoalsRequest\x1aF.google.ads.googleads.v18.services.MutateCustomConversionGoalsResponse"_\xdaA\x16customer_id,operations\x82\xd3\xe4\x93\x02@";/v18/customers/{customer_id=*}/customConversionGoals:mutate:\x01*\x1aE\xcaA\x18googleads.googleapis.com\xd2A\'https://www.googleapis.com/auth/adwordsB\x8c\x02\n%com.google.ads.googleads.v18.servicesB CustomConversionGoalServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v18/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V18.Services\xca\x02!Google\\Ads\\GoogleAds\\V18\\Services\xea\x02%Google::Ads::GoogleAds::V18::Servicesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v18.services.custom_conversion_goal_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.ads.googleads.v18.servicesB CustomConversionGoalServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v18/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V18.Services\xca\x02!Google\\Ads\\GoogleAds\\V18\\Services\xea\x02%Google::Ads::GoogleAds::V18::Services'
    _globals['_MUTATECUSTOMCONVERSIONGOALSREQUEST'].fields_by_name['customer_id']._loaded_options = None
    _globals['_MUTATECUSTOMCONVERSIONGOALSREQUEST'].fields_by_name['customer_id']._serialized_options = b'\xe0A\x02'
    _globals['_MUTATECUSTOMCONVERSIONGOALSREQUEST'].fields_by_name['operations']._loaded_options = None
    _globals['_MUTATECUSTOMCONVERSIONGOALSREQUEST'].fields_by_name['operations']._serialized_options = b'\xe0A\x02'
    _globals['_CUSTOMCONVERSIONGOALOPERATION'].fields_by_name['remove']._loaded_options = None
    _globals['_CUSTOMCONVERSIONGOALOPERATION'].fields_by_name['remove']._serialized_options = b'\xfaA/\n-googleads.googleapis.com/CustomConversionGoal'
    _globals['_MUTATECUSTOMCONVERSIONGOALRESULT'].fields_by_name['resource_name']._loaded_options = None
    _globals['_MUTATECUSTOMCONVERSIONGOALRESULT'].fields_by_name['resource_name']._serialized_options = b'\xfaA/\n-googleads.googleapis.com/CustomConversionGoal'
    _globals['_CUSTOMCONVERSIONGOALSERVICE']._loaded_options = None
    _globals['_CUSTOMCONVERSIONGOALSERVICE']._serialized_options = b"\xcaA\x18googleads.googleapis.com\xd2A'https://www.googleapis.com/auth/adwords"
    _globals['_CUSTOMCONVERSIONGOALSERVICE'].methods_by_name['MutateCustomConversionGoals']._loaded_options = None
    _globals['_CUSTOMCONVERSIONGOALSERVICE'].methods_by_name['MutateCustomConversionGoals']._serialized_options = b'\xdaA\x16customer_id,operations\x82\xd3\xe4\x93\x02@";/v18/customers/{customer_id=*}/customConversionGoals:mutate:\x01*'
    _globals['_MUTATECUSTOMCONVERSIONGOALSREQUEST']._serialized_start = 384
    _globals['_MUTATECUSTOMCONVERSIONGOALSREQUEST']._serialized_end = 668
    _globals['_CUSTOMCONVERSIONGOALOPERATION']._serialized_start = 671
    _globals['_CUSTOMCONVERSIONGOALOPERATION']._serialized_end = 986
    _globals['_MUTATECUSTOMCONVERSIONGOALSRESPONSE']._serialized_start = 988
    _globals['_MUTATECUSTOMCONVERSIONGOALSRESPONSE']._serialized_end = 1111
    _globals['_MUTATECUSTOMCONVERSIONGOALRESULT']._serialized_start = 1114
    _globals['_MUTATECUSTOMCONVERSIONGOALRESULT']._serialized_end = 1313
    _globals['_CUSTOMCONVERSIONGOALSERVICE']._serialized_start = 1316
    _globals['_CUSTOMCONVERSIONGOALSERVICE']._serialized_end = 1688