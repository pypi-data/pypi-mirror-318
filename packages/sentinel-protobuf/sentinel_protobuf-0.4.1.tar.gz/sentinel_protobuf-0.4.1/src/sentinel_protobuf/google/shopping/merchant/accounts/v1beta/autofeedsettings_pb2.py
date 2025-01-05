"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/shopping/merchant/accounts/v1beta/autofeedsettings.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n?google/shopping/merchant/accounts/v1beta/autofeedsettings.proto\x12(google.shopping.merchant.accounts.v1beta\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto"\xd5\x01\n\x10AutofeedSettings\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\x1c\n\x0fenable_products\x18\x02 \x01(\x08B\x03\xe0A\x02\x12\x15\n\x08eligible\x18\x03 \x01(\x08B\x03\xe0A\x03:y\xeaAv\n+merchantapi.googleapis.com/AutofeedSettings\x12#accounts/{account}/autofeedSettings*\x10autofeedSettings2\x10autofeedSettings"_\n\x1aGetAutofeedSettingsRequest\x12A\n\x04name\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+merchantapi.googleapis.com/AutofeedSettings"\xb1\x01\n\x1dUpdateAutofeedSettingsRequest\x12Z\n\x11autofeed_settings\x18\x01 \x01(\x0b2:.google.shopping.merchant.accounts.v1beta.AutofeedSettingsB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x022\xe3\x04\n\x17AutofeedSettingsService\x12\xdb\x01\n\x13GetAutofeedSettings\x12D.google.shopping.merchant.accounts.v1beta.GetAutofeedSettingsRequest\x1a:.google.shopping.merchant.accounts.v1beta.AutofeedSettings"B\xdaA\x04name\x82\xd3\xe4\x93\x025\x123/accounts/v1beta/{name=accounts/*/autofeedSettings}\x12\xa0\x02\n\x16UpdateAutofeedSettings\x12G.google.shopping.merchant.accounts.v1beta.UpdateAutofeedSettingsRequest\x1a:.google.shopping.merchant.accounts.v1beta.AutofeedSettings"\x80\x01\xdaA\x1dautofeed_settings,update_mask\x82\xd3\xe4\x93\x02Z2E/accounts/v1beta/{autofeed_settings.name=accounts/*/autofeedSettings}:\x11autofeed_settings\x1aG\xcaA\x1amerchantapi.googleapis.com\xd2A\'https://www.googleapis.com/auth/contentB\x97\x01\n,com.google.shopping.merchant.accounts.v1betaB\x15AutofeedSettingsProtoP\x01ZNcloud.google.com/go/shopping/merchant/accounts/apiv1beta/accountspb;accountspbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.shopping.merchant.accounts.v1beta.autofeedsettings_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n,com.google.shopping.merchant.accounts.v1betaB\x15AutofeedSettingsProtoP\x01ZNcloud.google.com/go/shopping/merchant/accounts/apiv1beta/accountspb;accountspb'
    _globals['_AUTOFEEDSETTINGS'].fields_by_name['name']._loaded_options = None
    _globals['_AUTOFEEDSETTINGS'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_AUTOFEEDSETTINGS'].fields_by_name['enable_products']._loaded_options = None
    _globals['_AUTOFEEDSETTINGS'].fields_by_name['enable_products']._serialized_options = b'\xe0A\x02'
    _globals['_AUTOFEEDSETTINGS'].fields_by_name['eligible']._loaded_options = None
    _globals['_AUTOFEEDSETTINGS'].fields_by_name['eligible']._serialized_options = b'\xe0A\x03'
    _globals['_AUTOFEEDSETTINGS']._loaded_options = None
    _globals['_AUTOFEEDSETTINGS']._serialized_options = b'\xeaAv\n+merchantapi.googleapis.com/AutofeedSettings\x12#accounts/{account}/autofeedSettings*\x10autofeedSettings2\x10autofeedSettings'
    _globals['_GETAUTOFEEDSETTINGSREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETAUTOFEEDSETTINGSREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA-\n+merchantapi.googleapis.com/AutofeedSettings'
    _globals['_UPDATEAUTOFEEDSETTINGSREQUEST'].fields_by_name['autofeed_settings']._loaded_options = None
    _globals['_UPDATEAUTOFEEDSETTINGSREQUEST'].fields_by_name['autofeed_settings']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEAUTOFEEDSETTINGSREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEAUTOFEEDSETTINGSREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_AUTOFEEDSETTINGSSERVICE']._loaded_options = None
    _globals['_AUTOFEEDSETTINGSSERVICE']._serialized_options = b"\xcaA\x1amerchantapi.googleapis.com\xd2A'https://www.googleapis.com/auth/content"
    _globals['_AUTOFEEDSETTINGSSERVICE'].methods_by_name['GetAutofeedSettings']._loaded_options = None
    _globals['_AUTOFEEDSETTINGSSERVICE'].methods_by_name['GetAutofeedSettings']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x025\x123/accounts/v1beta/{name=accounts/*/autofeedSettings}'
    _globals['_AUTOFEEDSETTINGSSERVICE'].methods_by_name['UpdateAutofeedSettings']._loaded_options = None
    _globals['_AUTOFEEDSETTINGSSERVICE'].methods_by_name['UpdateAutofeedSettings']._serialized_options = b'\xdaA\x1dautofeed_settings,update_mask\x82\xd3\xe4\x93\x02Z2E/accounts/v1beta/{autofeed_settings.name=accounts/*/autofeedSettings}:\x11autofeed_settings'
    _globals['_AUTOFEEDSETTINGS']._serialized_start = 259
    _globals['_AUTOFEEDSETTINGS']._serialized_end = 472
    _globals['_GETAUTOFEEDSETTINGSREQUEST']._serialized_start = 474
    _globals['_GETAUTOFEEDSETTINGSREQUEST']._serialized_end = 569
    _globals['_UPDATEAUTOFEEDSETTINGSREQUEST']._serialized_start = 572
    _globals['_UPDATEAUTOFEEDSETTINGSREQUEST']._serialized_end = 749
    _globals['_AUTOFEEDSETTINGSSERVICE']._serialized_start = 752
    _globals['_AUTOFEEDSETTINGSSERVICE']._serialized_end = 1363