"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/shopping/merchant/accounts/v1beta/emailpreferences.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n?google/shopping/merchant/accounts/v1beta/emailpreferences.proto\x12(google.shopping.merchant.accounts.v1beta\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto"\xed\x02\n\x10EmailPreferences\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12a\n\rnews_and_tips\x18\x02 \x01(\x0e2E.google.shopping.merchant.accounts.v1beta.EmailPreferences.OptInStateB\x03\xe0A\x01"X\n\nOptInState\x12\x1c\n\x18OPT_IN_STATE_UNSPECIFIED\x10\x00\x12\r\n\tOPTED_OUT\x10\x01\x12\x0c\n\x08OPTED_IN\x10\x02\x12\x0f\n\x0bUNCONFIRMED\x10\x03:\x88\x01\xeaA\x84\x01\n+merchantapi.googleapis.com/EmailPreferences\x121accounts/{account}/users/{email}/emailPreferences*\x10emailPreferences2\x10emailPreferences"_\n\x1aGetEmailPreferencesRequest\x12A\n\x04name\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+merchantapi.googleapis.com/EmailPreferences"\xb1\x01\n\x1dUpdateEmailPreferencesRequest\x12Z\n\x11email_preferences\x18\x01 \x01(\x0b2:.google.shopping.merchant.accounts.v1beta.EmailPreferencesB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x022\xf3\x04\n\x17EmailPreferencesService\x12\xe3\x01\n\x13GetEmailPreferences\x12D.google.shopping.merchant.accounts.v1beta.GetEmailPreferencesRequest\x1a:.google.shopping.merchant.accounts.v1beta.EmailPreferences"J\xdaA\x04name\x82\xd3\xe4\x93\x02=\x12;/accounts/v1beta/{name=accounts/*/users/*/emailPreferences}\x12\xa8\x02\n\x16UpdateEmailPreferences\x12G.google.shopping.merchant.accounts.v1beta.UpdateEmailPreferencesRequest\x1a:.google.shopping.merchant.accounts.v1beta.EmailPreferences"\x88\x01\xdaA\x1demail_preferences,update_mask\x82\xd3\xe4\x93\x02b2M/accounts/v1beta/{email_preferences.name=accounts/*/users/*/emailPreferences}:\x11email_preferences\x1aG\xcaA\x1amerchantapi.googleapis.com\xd2A\'https://www.googleapis.com/auth/contentB\x97\x01\n,com.google.shopping.merchant.accounts.v1betaB\x15EmailPreferencesProtoP\x01ZNcloud.google.com/go/shopping/merchant/accounts/apiv1beta/accountspb;accountspbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.shopping.merchant.accounts.v1beta.emailpreferences_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n,com.google.shopping.merchant.accounts.v1betaB\x15EmailPreferencesProtoP\x01ZNcloud.google.com/go/shopping/merchant/accounts/apiv1beta/accountspb;accountspb'
    _globals['_EMAILPREFERENCES'].fields_by_name['name']._loaded_options = None
    _globals['_EMAILPREFERENCES'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_EMAILPREFERENCES'].fields_by_name['news_and_tips']._loaded_options = None
    _globals['_EMAILPREFERENCES'].fields_by_name['news_and_tips']._serialized_options = b'\xe0A\x01'
    _globals['_EMAILPREFERENCES']._loaded_options = None
    _globals['_EMAILPREFERENCES']._serialized_options = b'\xeaA\x84\x01\n+merchantapi.googleapis.com/EmailPreferences\x121accounts/{account}/users/{email}/emailPreferences*\x10emailPreferences2\x10emailPreferences'
    _globals['_GETEMAILPREFERENCESREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETEMAILPREFERENCESREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA-\n+merchantapi.googleapis.com/EmailPreferences'
    _globals['_UPDATEEMAILPREFERENCESREQUEST'].fields_by_name['email_preferences']._loaded_options = None
    _globals['_UPDATEEMAILPREFERENCESREQUEST'].fields_by_name['email_preferences']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEEMAILPREFERENCESREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEEMAILPREFERENCESREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_EMAILPREFERENCESSERVICE']._loaded_options = None
    _globals['_EMAILPREFERENCESSERVICE']._serialized_options = b"\xcaA\x1amerchantapi.googleapis.com\xd2A'https://www.googleapis.com/auth/content"
    _globals['_EMAILPREFERENCESSERVICE'].methods_by_name['GetEmailPreferences']._loaded_options = None
    _globals['_EMAILPREFERENCESSERVICE'].methods_by_name['GetEmailPreferences']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02=\x12;/accounts/v1beta/{name=accounts/*/users/*/emailPreferences}'
    _globals['_EMAILPREFERENCESSERVICE'].methods_by_name['UpdateEmailPreferences']._loaded_options = None
    _globals['_EMAILPREFERENCESSERVICE'].methods_by_name['UpdateEmailPreferences']._serialized_options = b'\xdaA\x1demail_preferences,update_mask\x82\xd3\xe4\x93\x02b2M/accounts/v1beta/{email_preferences.name=accounts/*/users/*/emailPreferences}:\x11email_preferences'
    _globals['_EMAILPREFERENCES']._serialized_start = 259
    _globals['_EMAILPREFERENCES']._serialized_end = 624
    _globals['_EMAILPREFERENCES_OPTINSTATE']._serialized_start = 397
    _globals['_EMAILPREFERENCES_OPTINSTATE']._serialized_end = 485
    _globals['_GETEMAILPREFERENCESREQUEST']._serialized_start = 626
    _globals['_GETEMAILPREFERENCESREQUEST']._serialized_end = 721
    _globals['_UPDATEEMAILPREFERENCESREQUEST']._serialized_start = 724
    _globals['_UPDATEEMAILPREFERENCESREQUEST']._serialized_end = 901
    _globals['_EMAILPREFERENCESSERVICE']._serialized_start = 904
    _globals['_EMAILPREFERENCESSERVICE']._serialized_end = 1531