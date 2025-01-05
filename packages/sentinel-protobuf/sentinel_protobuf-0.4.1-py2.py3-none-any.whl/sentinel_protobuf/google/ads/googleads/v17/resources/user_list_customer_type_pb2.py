"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/ads/googleads/v17/resources/user_list_customer_type.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v17.enums import user_list_customer_type_category_pb2 as google_dot_ads_dot_googleads_dot_v17_dot_enums_dot_user__list__customer__type__category__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n@google/ads/googleads/v17/resources/user_list_customer_type.proto\x12"google.ads.googleads.v17.resources\x1aEgoogle/ads/googleads/v17/enums/user_list_customer_type_category.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xab\x03\n\x14UserListCustomerType\x12L\n\rresource_name\x18\x01 \x01(\tB5\xe0A\x05\xfaA/\n-googleads.googleapis.com/UserListCustomerType\x12<\n\tuser_list\x18\x02 \x01(\tB)\xe0A\x05\xfaA#\n!googleads.googleapis.com/UserList\x12\x82\x01\n\x16customer_type_category\x18\x03 \x01(\x0e2].google.ads.googleads.v17.enums.UserListCustomerTypeCategoryEnum.UserListCustomerTypeCategoryB\x03\xe0A\x05:\x81\x01\xeaA~\n-googleads.googleapis.com/UserListCustomerType\x12Mcustomers/{customer_id}/userListCustomerTypes/{user_list_id}~{semantic_label}B\x8b\x02\n&com.google.ads.googleads.v17.resourcesB\x19UserListCustomerTypeProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v17/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V17.Resources\xca\x02"Google\\Ads\\GoogleAds\\V17\\Resources\xea\x02&Google::Ads::GoogleAds::V17::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v17.resources.user_list_customer_type_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v17.resourcesB\x19UserListCustomerTypeProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v17/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V17.Resources\xca\x02"Google\\Ads\\GoogleAds\\V17\\Resources\xea\x02&Google::Ads::GoogleAds::V17::Resources'
    _globals['_USERLISTCUSTOMERTYPE'].fields_by_name['resource_name']._loaded_options = None
    _globals['_USERLISTCUSTOMERTYPE'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x05\xfaA/\n-googleads.googleapis.com/UserListCustomerType'
    _globals['_USERLISTCUSTOMERTYPE'].fields_by_name['user_list']._loaded_options = None
    _globals['_USERLISTCUSTOMERTYPE'].fields_by_name['user_list']._serialized_options = b'\xe0A\x05\xfaA#\n!googleads.googleapis.com/UserList'
    _globals['_USERLISTCUSTOMERTYPE'].fields_by_name['customer_type_category']._loaded_options = None
    _globals['_USERLISTCUSTOMERTYPE'].fields_by_name['customer_type_category']._serialized_options = b'\xe0A\x05'
    _globals['_USERLISTCUSTOMERTYPE']._loaded_options = None
    _globals['_USERLISTCUSTOMERTYPE']._serialized_options = b'\xeaA~\n-googleads.googleapis.com/UserListCustomerType\x12Mcustomers/{customer_id}/userListCustomerTypes/{user_list_id}~{semantic_label}'
    _globals['_USERLISTCUSTOMERTYPE']._serialized_start = 236
    _globals['_USERLISTCUSTOMERTYPE']._serialized_end = 663