"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/shopping/merchant/accounts/v1beta/user.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from ......google.shopping.merchant.accounts.v1beta import accessright_pb2 as google_dot_shopping_dot_merchant_dot_accounts_dot_v1beta_dot_accessright__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3google/shopping/merchant/accounts/v1beta/user.proto\x12(google.shopping.merchant.accounts.v1beta\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a:google/shopping/merchant/accounts/v1beta/accessright.proto"\xc6\x02\n\x04User\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12H\n\x05state\x18\x02 \x01(\x0e24.google.shopping.merchant.accounts.v1beta.User.StateB\x03\xe0A\x03\x12Q\n\raccess_rights\x18\x04 \x03(\x0e25.google.shopping.merchant.accounts.v1beta.AccessRightB\x03\xe0A\x01"9\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0b\n\x07PENDING\x10\x01\x12\x0c\n\x08VERIFIED\x10\x02:S\xeaAP\n\x1fmerchantapi.googleapis.com/User\x12 accounts/{account}/users/{email}*\x05users2\x04user"G\n\x0eGetUserRequest\x125\n\x04name\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1fmerchantapi.googleapis.com/User"\xa8\x01\n\x11CreateUserRequest\x12:\n\x06parent\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\n"merchantapi.googleapis.com/Account\x12\x14\n\x07user_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12A\n\x04user\x18\x03 \x01(\x0b2..google.shopping.merchant.accounts.v1beta.UserB\x03\xe0A\x02"J\n\x11DeleteUserRequest\x125\n\x04name\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1fmerchantapi.googleapis.com/User"\x8c\x01\n\x11UpdateUserRequest\x12A\n\x04user\x18\x01 \x01(\x0b2..google.shopping.merchant.accounts.v1beta.UserB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02"\x7f\n\x10ListUsersRequest\x12:\n\x06parent\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\n"merchantapi.googleapis.com/Account\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01"k\n\x11ListUsersResponse\x12=\n\x05users\x18\x01 \x03(\x0b2..google.shopping.merchant.accounts.v1beta.User\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xfc\x07\n\x0bUserService\x12\xae\x01\n\x07GetUser\x128.google.shopping.merchant.accounts.v1beta.GetUserRequest\x1a..google.shopping.merchant.accounts.v1beta.User"9\xdaA\x04name\x82\xd3\xe4\x93\x02,\x12*/accounts/v1beta/{name=accounts/*/users/*}\x12\xc1\x01\n\nCreateUser\x12;.google.shopping.merchant.accounts.v1beta.CreateUserRequest\x1a..google.shopping.merchant.accounts.v1beta.User"F\xdaA\x0bparent,user\x82\xd3\xe4\x93\x022"*/accounts/v1beta/{parent=accounts/*}/users:\x04user\x12\x9c\x01\n\nDeleteUser\x12;.google.shopping.merchant.accounts.v1beta.DeleteUserRequest\x1a\x16.google.protobuf.Empty"9\xdaA\x04name\x82\xd3\xe4\x93\x02,**/accounts/v1beta/{name=accounts/*/users/*}\x12\xcb\x01\n\nUpdateUser\x12;.google.shopping.merchant.accounts.v1beta.UpdateUserRequest\x1a..google.shopping.merchant.accounts.v1beta.User"P\xdaA\x10user,update_mask\x82\xd3\xe4\x93\x0272//accounts/v1beta/{user.name=accounts/*/users/*}:\x04user\x12\xc1\x01\n\tListUsers\x12:.google.shopping.merchant.accounts.v1beta.ListUsersRequest\x1a;.google.shopping.merchant.accounts.v1beta.ListUsersResponse";\xdaA\x06parent\x82\xd3\xe4\x93\x02,\x12*/accounts/v1beta/{parent=accounts/*}/users\x1aG\xcaA\x1amerchantapi.googleapis.com\xd2A\'https://www.googleapis.com/auth/contentB\x8b\x01\n,com.google.shopping.merchant.accounts.v1betaB\tUserProtoP\x01ZNcloud.google.com/go/shopping/merchant/accounts/apiv1beta/accountspb;accountspbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.shopping.merchant.accounts.v1beta.user_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n,com.google.shopping.merchant.accounts.v1betaB\tUserProtoP\x01ZNcloud.google.com/go/shopping/merchant/accounts/apiv1beta/accountspb;accountspb'
    _globals['_USER'].fields_by_name['name']._loaded_options = None
    _globals['_USER'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_USER'].fields_by_name['state']._loaded_options = None
    _globals['_USER'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_USER'].fields_by_name['access_rights']._loaded_options = None
    _globals['_USER'].fields_by_name['access_rights']._serialized_options = b'\xe0A\x01'
    _globals['_USER']._loaded_options = None
    _globals['_USER']._serialized_options = b'\xeaAP\n\x1fmerchantapi.googleapis.com/User\x12 accounts/{account}/users/{email}*\x05users2\x04user'
    _globals['_GETUSERREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETUSERREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA!\n\x1fmerchantapi.googleapis.com/User'
    _globals['_CREATEUSERREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEUSERREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA$\n"merchantapi.googleapis.com/Account'
    _globals['_CREATEUSERREQUEST'].fields_by_name['user_id']._loaded_options = None
    _globals['_CREATEUSERREQUEST'].fields_by_name['user_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEUSERREQUEST'].fields_by_name['user']._loaded_options = None
    _globals['_CREATEUSERREQUEST'].fields_by_name['user']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEUSERREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEUSERREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA!\n\x1fmerchantapi.googleapis.com/User'
    _globals['_UPDATEUSERREQUEST'].fields_by_name['user']._loaded_options = None
    _globals['_UPDATEUSERREQUEST'].fields_by_name['user']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEUSERREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEUSERREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_LISTUSERSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTUSERSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA$\n"merchantapi.googleapis.com/Account'
    _globals['_LISTUSERSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTUSERSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTUSERSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTUSERSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_USERSERVICE']._loaded_options = None
    _globals['_USERSERVICE']._serialized_options = b"\xcaA\x1amerchantapi.googleapis.com\xd2A'https://www.googleapis.com/auth/content"
    _globals['_USERSERVICE'].methods_by_name['GetUser']._loaded_options = None
    _globals['_USERSERVICE'].methods_by_name['GetUser']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02,\x12*/accounts/v1beta/{name=accounts/*/users/*}'
    _globals['_USERSERVICE'].methods_by_name['CreateUser']._loaded_options = None
    _globals['_USERSERVICE'].methods_by_name['CreateUser']._serialized_options = b'\xdaA\x0bparent,user\x82\xd3\xe4\x93\x022"*/accounts/v1beta/{parent=accounts/*}/users:\x04user'
    _globals['_USERSERVICE'].methods_by_name['DeleteUser']._loaded_options = None
    _globals['_USERSERVICE'].methods_by_name['DeleteUser']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02,**/accounts/v1beta/{name=accounts/*/users/*}'
    _globals['_USERSERVICE'].methods_by_name['UpdateUser']._loaded_options = None
    _globals['_USERSERVICE'].methods_by_name['UpdateUser']._serialized_options = b'\xdaA\x10user,update_mask\x82\xd3\xe4\x93\x0272//accounts/v1beta/{user.name=accounts/*/users/*}:\x04user'
    _globals['_USERSERVICE'].methods_by_name['ListUsers']._loaded_options = None
    _globals['_USERSERVICE'].methods_by_name['ListUsers']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02,\x12*/accounts/v1beta/{parent=accounts/*}/users'
    _globals['_USER']._serialized_start = 336
    _globals['_USER']._serialized_end = 662
    _globals['_USER_STATE']._serialized_start = 520
    _globals['_USER_STATE']._serialized_end = 577
    _globals['_GETUSERREQUEST']._serialized_start = 664
    _globals['_GETUSERREQUEST']._serialized_end = 735
    _globals['_CREATEUSERREQUEST']._serialized_start = 738
    _globals['_CREATEUSERREQUEST']._serialized_end = 906
    _globals['_DELETEUSERREQUEST']._serialized_start = 908
    _globals['_DELETEUSERREQUEST']._serialized_end = 982
    _globals['_UPDATEUSERREQUEST']._serialized_start = 985
    _globals['_UPDATEUSERREQUEST']._serialized_end = 1125
    _globals['_LISTUSERSREQUEST']._serialized_start = 1127
    _globals['_LISTUSERSREQUEST']._serialized_end = 1254
    _globals['_LISTUSERSRESPONSE']._serialized_start = 1256
    _globals['_LISTUSERSRESPONSE']._serialized_end = 1363
    _globals['_USERSERVICE']._serialized_start = 1366
    _globals['_USERSERVICE']._serialized_end = 2386