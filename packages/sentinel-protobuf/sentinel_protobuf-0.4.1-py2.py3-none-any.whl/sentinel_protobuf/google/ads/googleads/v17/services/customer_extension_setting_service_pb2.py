"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ads/googleads/v17/services/customer_extension_setting_service.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v17.enums import response_content_type_pb2 as google_dot_ads_dot_googleads_dot_v17_dot_enums_dot_response__content__type__pb2
from ......google.ads.googleads.v17.resources import customer_extension_setting_pb2 as google_dot_ads_dot_googleads_dot_v17_dot_resources_dot_customer__extension__setting__pb2
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from ......google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nJgoogle/ads/googleads/v17/services/customer_extension_setting_service.proto\x12!google.ads.googleads.v17.services\x1a:google/ads/googleads/v17/enums/response_content_type.proto\x1aCgoogle/ads/googleads/v17/resources/customer_extension_setting.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto\x1a\x17google/rpc/status.proto"\xbd\x02\n&MutateCustomerExtensionSettingsRequest\x12\x18\n\x0bcustomer_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12]\n\noperations\x18\x02 \x03(\x0b2D.google.ads.googleads.v17.services.CustomerExtensionSettingOperationB\x03\xe0A\x02\x12\x17\n\x0fpartial_failure\x18\x03 \x01(\x08\x12\x15\n\rvalidate_only\x18\x04 \x01(\x08\x12j\n\x15response_content_type\x18\x05 \x01(\x0e2K.google.ads.googleads.v17.enums.ResponseContentTypeEnum.ResponseContentType"\xcb\x02\n!CustomerExtensionSettingOperation\x12/\n\x0bupdate_mask\x18\x04 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12N\n\x06create\x18\x01 \x01(\x0b2<.google.ads.googleads.v17.resources.CustomerExtensionSettingH\x00\x12N\n\x06update\x18\x02 \x01(\x0b2<.google.ads.googleads.v17.resources.CustomerExtensionSettingH\x00\x12H\n\x06remove\x18\x03 \x01(\tB6\xfaA3\n1googleads.googleapis.com/CustomerExtensionSettingH\x00B\x0b\n\toperation"\xb6\x01\n\'MutateCustomerExtensionSettingsResponse\x121\n\x15partial_failure_error\x18\x03 \x01(\x0b2\x12.google.rpc.Status\x12X\n\x07results\x18\x02 \x03(\x0b2G.google.ads.googleads.v17.services.MutateCustomerExtensionSettingResult"\xd7\x01\n$MutateCustomerExtensionSettingResult\x12M\n\rresource_name\x18\x01 \x01(\tB6\xfaA3\n1googleads.googleapis.com/CustomerExtensionSetting\x12`\n\x1acustomer_extension_setting\x18\x02 \x01(\x0b2<.google.ads.googleads.v17.resources.CustomerExtensionSetting2\x88\x03\n\x1fCustomerExtensionSettingService\x12\x9d\x02\n\x1fMutateCustomerExtensionSettings\x12I.google.ads.googleads.v17.services.MutateCustomerExtensionSettingsRequest\x1aJ.google.ads.googleads.v17.services.MutateCustomerExtensionSettingsResponse"c\xdaA\x16customer_id,operations\x82\xd3\xe4\x93\x02D"?/v17/customers/{customer_id=*}/customerExtensionSettings:mutate:\x01*\x1aE\xcaA\x18googleads.googleapis.com\xd2A\'https://www.googleapis.com/auth/adwordsB\x90\x02\n%com.google.ads.googleads.v17.servicesB$CustomerExtensionSettingServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v17/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V17.Services\xca\x02!Google\\Ads\\GoogleAds\\V17\\Services\xea\x02%Google::Ads::GoogleAds::V17::Servicesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v17.services.customer_extension_setting_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.ads.googleads.v17.servicesB$CustomerExtensionSettingServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v17/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V17.Services\xca\x02!Google\\Ads\\GoogleAds\\V17\\Services\xea\x02%Google::Ads::GoogleAds::V17::Services'
    _globals['_MUTATECUSTOMEREXTENSIONSETTINGSREQUEST'].fields_by_name['customer_id']._loaded_options = None
    _globals['_MUTATECUSTOMEREXTENSIONSETTINGSREQUEST'].fields_by_name['customer_id']._serialized_options = b'\xe0A\x02'
    _globals['_MUTATECUSTOMEREXTENSIONSETTINGSREQUEST'].fields_by_name['operations']._loaded_options = None
    _globals['_MUTATECUSTOMEREXTENSIONSETTINGSREQUEST'].fields_by_name['operations']._serialized_options = b'\xe0A\x02'
    _globals['_CUSTOMEREXTENSIONSETTINGOPERATION'].fields_by_name['remove']._loaded_options = None
    _globals['_CUSTOMEREXTENSIONSETTINGOPERATION'].fields_by_name['remove']._serialized_options = b'\xfaA3\n1googleads.googleapis.com/CustomerExtensionSetting'
    _globals['_MUTATECUSTOMEREXTENSIONSETTINGRESULT'].fields_by_name['resource_name']._loaded_options = None
    _globals['_MUTATECUSTOMEREXTENSIONSETTINGRESULT'].fields_by_name['resource_name']._serialized_options = b'\xfaA3\n1googleads.googleapis.com/CustomerExtensionSetting'
    _globals['_CUSTOMEREXTENSIONSETTINGSERVICE']._loaded_options = None
    _globals['_CUSTOMEREXTENSIONSETTINGSERVICE']._serialized_options = b"\xcaA\x18googleads.googleapis.com\xd2A'https://www.googleapis.com/auth/adwords"
    _globals['_CUSTOMEREXTENSIONSETTINGSERVICE'].methods_by_name['MutateCustomerExtensionSettings']._loaded_options = None
    _globals['_CUSTOMEREXTENSIONSETTINGSERVICE'].methods_by_name['MutateCustomerExtensionSettings']._serialized_options = b'\xdaA\x16customer_id,operations\x82\xd3\xe4\x93\x02D"?/v17/customers/{customer_id=*}/customerExtensionSettings:mutate:\x01*'
    _globals['_MUTATECUSTOMEREXTENSIONSETTINGSREQUEST']._serialized_start = 417
    _globals['_MUTATECUSTOMEREXTENSIONSETTINGSREQUEST']._serialized_end = 734
    _globals['_CUSTOMEREXTENSIONSETTINGOPERATION']._serialized_start = 737
    _globals['_CUSTOMEREXTENSIONSETTINGOPERATION']._serialized_end = 1068
    _globals['_MUTATECUSTOMEREXTENSIONSETTINGSRESPONSE']._serialized_start = 1071
    _globals['_MUTATECUSTOMEREXTENSIONSETTINGSRESPONSE']._serialized_end = 1253
    _globals['_MUTATECUSTOMEREXTENSIONSETTINGRESULT']._serialized_start = 1256
    _globals['_MUTATECUSTOMEREXTENSIONSETTINGRESULT']._serialized_end = 1471
    _globals['_CUSTOMEREXTENSIONSETTINGSERVICE']._serialized_start = 1474
    _globals['_CUSTOMEREXTENSIONSETTINGSERVICE']._serialized_end = 1866