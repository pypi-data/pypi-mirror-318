"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ads/googleads/v18/services/user_list_customer_type_service.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v18.resources import user_list_customer_type_pb2 as google_dot_ads_dot_googleads_dot_v18_dot_resources_dot_user__list__customer__type__pb2
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ......google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nGgoogle/ads/googleads/v18/services/user_list_customer_type_service.proto\x12!google.ads.googleads.v18.services\x1a@google/ads/googleads/v18/resources/user_list_customer_type.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x17google/rpc/status.proto"\xd3\x01\n"MutateUserListCustomerTypesRequest\x12\x18\n\x0bcustomer_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12Y\n\noperations\x18\x02 \x03(\x0b2@.google.ads.googleads.v18.services.UserListCustomerTypeOperationB\x03\xe0A\x02\x12\x1c\n\x0fpartial_failure\x18\x03 \x01(\x08B\x03\xe0A\x01\x12\x1a\n\rvalidate_only\x18\x04 \x01(\x08B\x03\xe0A\x01"\xbe\x01\n\x1dUserListCustomerTypeOperation\x12J\n\x06create\x18\x01 \x01(\x0b28.google.ads.googleads.v18.resources.UserListCustomerTypeH\x00\x12D\n\x06remove\x18\x02 \x01(\tB2\xfaA/\n-googleads.googleapis.com/UserListCustomerTypeH\x00B\x0b\n\toperation"\xae\x01\n#MutateUserListCustomerTypesResponse\x121\n\x15partial_failure_error\x18\x01 \x01(\x0b2\x12.google.rpc.Status\x12T\n\x07results\x18\x02 \x03(\x0b2C.google.ads.googleads.v18.services.MutateUserListCustomerTypeResult"m\n MutateUserListCustomerTypeResult\x12I\n\rresource_name\x18\x01 \x01(\tB2\xfaA/\n-googleads.googleapis.com/UserListCustomerType2\xf4\x02\n\x1bUserListCustomerTypeService\x12\x8d\x02\n\x1bMutateUserListCustomerTypes\x12E.google.ads.googleads.v18.services.MutateUserListCustomerTypesRequest\x1aF.google.ads.googleads.v18.services.MutateUserListCustomerTypesResponse"_\xdaA\x16customer_id,operations\x82\xd3\xe4\x93\x02@";/v18/customers/{customer_id=*}/userListCustomerTypes:mutate:\x01*\x1aE\xcaA\x18googleads.googleapis.com\xd2A\'https://www.googleapis.com/auth/adwordsB\x8c\x02\n%com.google.ads.googleads.v18.servicesB UserListCustomerTypeServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v18/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V18.Services\xca\x02!Google\\Ads\\GoogleAds\\V18\\Services\xea\x02%Google::Ads::GoogleAds::V18::Servicesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v18.services.user_list_customer_type_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.ads.googleads.v18.servicesB UserListCustomerTypeServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v18/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V18.Services\xca\x02!Google\\Ads\\GoogleAds\\V18\\Services\xea\x02%Google::Ads::GoogleAds::V18::Services'
    _globals['_MUTATEUSERLISTCUSTOMERTYPESREQUEST'].fields_by_name['customer_id']._loaded_options = None
    _globals['_MUTATEUSERLISTCUSTOMERTYPESREQUEST'].fields_by_name['customer_id']._serialized_options = b'\xe0A\x02'
    _globals['_MUTATEUSERLISTCUSTOMERTYPESREQUEST'].fields_by_name['operations']._loaded_options = None
    _globals['_MUTATEUSERLISTCUSTOMERTYPESREQUEST'].fields_by_name['operations']._serialized_options = b'\xe0A\x02'
    _globals['_MUTATEUSERLISTCUSTOMERTYPESREQUEST'].fields_by_name['partial_failure']._loaded_options = None
    _globals['_MUTATEUSERLISTCUSTOMERTYPESREQUEST'].fields_by_name['partial_failure']._serialized_options = b'\xe0A\x01'
    _globals['_MUTATEUSERLISTCUSTOMERTYPESREQUEST'].fields_by_name['validate_only']._loaded_options = None
    _globals['_MUTATEUSERLISTCUSTOMERTYPESREQUEST'].fields_by_name['validate_only']._serialized_options = b'\xe0A\x01'
    _globals['_USERLISTCUSTOMERTYPEOPERATION'].fields_by_name['remove']._loaded_options = None
    _globals['_USERLISTCUSTOMERTYPEOPERATION'].fields_by_name['remove']._serialized_options = b'\xfaA/\n-googleads.googleapis.com/UserListCustomerType'
    _globals['_MUTATEUSERLISTCUSTOMERTYPERESULT'].fields_by_name['resource_name']._loaded_options = None
    _globals['_MUTATEUSERLISTCUSTOMERTYPERESULT'].fields_by_name['resource_name']._serialized_options = b'\xfaA/\n-googleads.googleapis.com/UserListCustomerType'
    _globals['_USERLISTCUSTOMERTYPESERVICE']._loaded_options = None
    _globals['_USERLISTCUSTOMERTYPESERVICE']._serialized_options = b"\xcaA\x18googleads.googleapis.com\xd2A'https://www.googleapis.com/auth/adwords"
    _globals['_USERLISTCUSTOMERTYPESERVICE'].methods_by_name['MutateUserListCustomerTypes']._loaded_options = None
    _globals['_USERLISTCUSTOMERTYPESERVICE'].methods_by_name['MutateUserListCustomerTypes']._serialized_options = b'\xdaA\x16customer_id,operations\x82\xd3\xe4\x93\x02@";/v18/customers/{customer_id=*}/userListCustomerTypes:mutate:\x01*'
    _globals['_MUTATEUSERLISTCUSTOMERTYPESREQUEST']._serialized_start = 317
    _globals['_MUTATEUSERLISTCUSTOMERTYPESREQUEST']._serialized_end = 528
    _globals['_USERLISTCUSTOMERTYPEOPERATION']._serialized_start = 531
    _globals['_USERLISTCUSTOMERTYPEOPERATION']._serialized_end = 721
    _globals['_MUTATEUSERLISTCUSTOMERTYPESRESPONSE']._serialized_start = 724
    _globals['_MUTATEUSERLISTCUSTOMERTYPESRESPONSE']._serialized_end = 898
    _globals['_MUTATEUSERLISTCUSTOMERTYPERESULT']._serialized_start = 900
    _globals['_MUTATEUSERLISTCUSTOMERTYPERESULT']._serialized_end = 1009
    _globals['_USERLISTCUSTOMERTYPESERVICE']._serialized_start = 1012
    _globals['_USERLISTCUSTOMERTYPESERVICE']._serialized_end = 1384