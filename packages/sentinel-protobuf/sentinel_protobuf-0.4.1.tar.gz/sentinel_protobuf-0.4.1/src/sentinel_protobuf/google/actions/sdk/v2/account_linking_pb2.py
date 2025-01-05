"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/actions/sdk/v2/account_linking.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+google/actions/sdk/v2/account_linking.proto\x12\x15google.actions.sdk.v2\x1a\x1fgoogle/api/field_behavior.proto"\xba\x04\n\x0eAccountLinking\x12$\n\x17enable_account_creation\x18\x01 \x01(\x08B\x03\xe0A\x02\x12L\n\x0clinking_type\x18\x02 \x01(\x0e21.google.actions.sdk.v2.AccountLinking.LinkingTypeB\x03\xe0A\x02\x12Q\n\x0fauth_grant_type\x18\x03 \x01(\x0e23.google.actions.sdk.v2.AccountLinking.AuthGrantTypeB\x03\xe0A\x01\x12\x1a\n\rapp_client_id\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x1e\n\x11authorization_url\x18\x05 \x01(\tB\x03\xe0A\x01\x12\x16\n\ttoken_url\x18\x06 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06scopes\x18\x07 \x03(\tB\x03\xe0A\x01\x12\x1b\n\x0elearn_more_url\x18\x08 \x01(\tB\x03\xe0A\x01\x12"\n\x15use_basic_auth_header\x18\t \x01(\x08B\x03\xe0A\x01"h\n\x0bLinkingType\x12\x1c\n\x18LINKING_TYPE_UNSPECIFIED\x10\x00\x12\x12\n\x0eGOOGLE_SIGN_IN\x10\x01\x12\x1c\n\x18OAUTH_AND_GOOGLE_SIGN_IN\x10\x02\x12\t\n\x05OAUTH\x10\x03"M\n\rAuthGrantType\x12\x1f\n\x1bAUTH_GRANT_TYPE_UNSPECIFIED\x10\x00\x12\r\n\tAUTH_CODE\x10\x01\x12\x0c\n\x08IMPLICIT\x10\x02Bl\n\x19com.google.actions.sdk.v2B\x13AccountLinkingProtoP\x01Z8google.golang.org/genproto/googleapis/actions/sdk/v2;sdkb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.actions.sdk.v2.account_linking_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x19com.google.actions.sdk.v2B\x13AccountLinkingProtoP\x01Z8google.golang.org/genproto/googleapis/actions/sdk/v2;sdk'
    _globals['_ACCOUNTLINKING'].fields_by_name['enable_account_creation']._loaded_options = None
    _globals['_ACCOUNTLINKING'].fields_by_name['enable_account_creation']._serialized_options = b'\xe0A\x02'
    _globals['_ACCOUNTLINKING'].fields_by_name['linking_type']._loaded_options = None
    _globals['_ACCOUNTLINKING'].fields_by_name['linking_type']._serialized_options = b'\xe0A\x02'
    _globals['_ACCOUNTLINKING'].fields_by_name['auth_grant_type']._loaded_options = None
    _globals['_ACCOUNTLINKING'].fields_by_name['auth_grant_type']._serialized_options = b'\xe0A\x01'
    _globals['_ACCOUNTLINKING'].fields_by_name['app_client_id']._loaded_options = None
    _globals['_ACCOUNTLINKING'].fields_by_name['app_client_id']._serialized_options = b'\xe0A\x01'
    _globals['_ACCOUNTLINKING'].fields_by_name['authorization_url']._loaded_options = None
    _globals['_ACCOUNTLINKING'].fields_by_name['authorization_url']._serialized_options = b'\xe0A\x01'
    _globals['_ACCOUNTLINKING'].fields_by_name['token_url']._loaded_options = None
    _globals['_ACCOUNTLINKING'].fields_by_name['token_url']._serialized_options = b'\xe0A\x01'
    _globals['_ACCOUNTLINKING'].fields_by_name['scopes']._loaded_options = None
    _globals['_ACCOUNTLINKING'].fields_by_name['scopes']._serialized_options = b'\xe0A\x01'
    _globals['_ACCOUNTLINKING'].fields_by_name['learn_more_url']._loaded_options = None
    _globals['_ACCOUNTLINKING'].fields_by_name['learn_more_url']._serialized_options = b'\xe0A\x01'
    _globals['_ACCOUNTLINKING'].fields_by_name['use_basic_auth_header']._loaded_options = None
    _globals['_ACCOUNTLINKING'].fields_by_name['use_basic_auth_header']._serialized_options = b'\xe0A\x01'
    _globals['_ACCOUNTLINKING']._serialized_start = 104
    _globals['_ACCOUNTLINKING']._serialized_end = 674
    _globals['_ACCOUNTLINKING_LINKINGTYPE']._serialized_start = 491
    _globals['_ACCOUNTLINKING_LINKINGTYPE']._serialized_end = 595
    _globals['_ACCOUNTLINKING_AUTHGRANTTYPE']._serialized_start = 597
    _globals['_ACCOUNTLINKING_AUTHGRANTTYPE']._serialized_end = 674