"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/actions/sdk/v2/settings.proto')
_sym_db = _symbol_database.Default()
from .....google.actions.sdk.v2 import account_linking_pb2 as google_dot_actions_dot_sdk_dot_v2_dot_account__linking__pb2
from .....google.actions.sdk.v2 import localized_settings_pb2 as google_dot_actions_dot_sdk_dot_v2_dot_localized__settings__pb2
from .....google.actions.sdk.v2 import surface_pb2 as google_dot_actions_dot_sdk_dot_v2_dot_surface__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$google/actions/sdk/v2/settings.proto\x12\x15google.actions.sdk.v2\x1a+google/actions/sdk/v2/account_linking.proto\x1a.google/actions/sdk/v2/localized_settings.proto\x1a#google/actions/sdk/v2/surface.proto"\xaf\x08\n\x08Settings\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x16\n\x0edefault_locale\x18\x02 \x01(\t\x12\x17\n\x0fenabled_regions\x18\x03 \x03(\t\x12\x18\n\x10disabled_regions\x18\x04 \x03(\t\x12:\n\x08category\x18\x05 \x01(\x0e2(.google.actions.sdk.v2.Settings.Category\x12\x1d\n\x15uses_transactions_api\x18\x06 \x01(\x08\x12!\n\x19uses_digital_purchase_api\x18\x07 \x01(\x08\x12\x1f\n\x17uses_interactive_canvas\x18\x08 \x01(\x08\x12\x19\n\x11uses_home_storage\x18\x11 \x01(\x08\x12\x1b\n\x13designed_for_family\x18\t \x01(\x08\x12+\n#contains_alcohol_or_tobacco_content\x18\x0b \x01(\x08\x12\x16\n\x0ekeeps_mic_open\x18\x0c \x01(\x08\x12H\n\x14surface_requirements\x18\r \x01(\x0b2*.google.actions.sdk.v2.SurfaceRequirements\x12\x1c\n\x14testing_instructions\x18\x0e \x01(\t\x12D\n\x12localized_settings\x18\x0f \x01(\x0b2(.google.actions.sdk.v2.LocalizedSettings\x12>\n\x0faccount_linking\x18\x10 \x01(\x0b2%.google.actions.sdk.v2.AccountLinking\x12\x1d\n\x15selected_android_apps\x18\x14 \x03(\t"\x9a\x03\n\x08Category\x12\x18\n\x14CATEGORY_UNSPECIFIED\x10\x00\x12\x18\n\x14BUSINESS_AND_FINANCE\x10\x02\x12\x1b\n\x17EDUCATION_AND_REFERENCE\x10\x03\x12\x12\n\x0eFOOD_AND_DRINK\x10\x04\x12\x14\n\x10GAMES_AND_TRIVIA\x10\x05\x12\x16\n\x12HEALTH_AND_FITNESS\x10\x06\x12\x13\n\x0fKIDS_AND_FAMILY\x10\x14\x12\r\n\tLIFESTYLE\x10\x07\x12\t\n\x05LOCAL\x10\x08\x12\x11\n\rMOVIES_AND_TV\x10\t\x12\x13\n\x0fMUSIC_AND_AUDIO\x10\n\x12\x08\n\x04NEWS\x10\x01\x12\x15\n\x11NOVELTY_AND_HUMOR\x10\x0b\x12\x10\n\x0cPRODUCTIVITY\x10\x0c\x12\x0c\n\x08SHOPPING\x10\r\x12\n\n\x06SOCIAL\x10\x0e\x12\n\n\x06SPORTS\x10\x0f\x12\x1d\n\x19TRAVEL_AND_TRANSPORTATION\x10\x10\x12\r\n\tUTILITIES\x10\x11\x12\x0b\n\x07WEATHER\x10\x12\x12\x10\n\x0cHOME_CONTROL\x10\x13Bf\n\x19com.google.actions.sdk.v2B\rSettingsProtoP\x01Z8google.golang.org/genproto/googleapis/actions/sdk/v2;sdkb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.actions.sdk.v2.settings_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x19com.google.actions.sdk.v2B\rSettingsProtoP\x01Z8google.golang.org/genproto/googleapis/actions/sdk/v2;sdk'
    _globals['_SETTINGS']._serialized_start = 194
    _globals['_SETTINGS']._serialized_end = 1265
    _globals['_SETTINGS_CATEGORY']._serialized_start = 855
    _globals['_SETTINGS_CATEGORY']._serialized_end = 1265