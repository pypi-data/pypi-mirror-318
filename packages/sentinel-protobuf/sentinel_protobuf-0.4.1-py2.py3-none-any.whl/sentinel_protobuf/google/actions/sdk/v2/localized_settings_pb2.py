"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/actions/sdk/v2/localized_settings.proto')
_sym_db = _symbol_database.Default()
from .....google.actions.sdk.v2 import theme_customization_pb2 as google_dot_actions_dot_sdk_dot_v2_dot_theme__customization__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.google/actions/sdk/v2/localized_settings.proto\x12\x15google.actions.sdk.v2\x1a/google/actions/sdk/v2/theme_customization.proto\x1a\x1fgoogle/api/field_behavior.proto"\xe5\x03\n\x11LocalizedSettings\x12\x19\n\x0cdisplay_name\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x1a\n\rpronunciation\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x1e\n\x11short_description\x18\x03 \x01(\tB\x03\xe0A\x02\x12\x1d\n\x10full_description\x18\x04 \x01(\tB\x03\xe0A\x02\x12\x1d\n\x10small_logo_image\x18\x05 \x01(\tB\x03\xe0A\x02\x12\x1f\n\x12large_banner_image\x18\x06 \x01(\tB\x03\xe0A\x01\x12\x1b\n\x0edeveloper_name\x18\x07 \x01(\tB\x03\xe0A\x02\x12\x1c\n\x0fdeveloper_email\x18\x08 \x01(\tB\x03\xe0A\x02\x12!\n\x14terms_of_service_url\x18\t \x01(\tB\x03\xe0A\x01\x12\x12\n\x05voice\x18\n \x01(\tB\x03\xe0A\x02\x12\x19\n\x0cvoice_locale\x18\x0e \x01(\tB\x03\xe0A\x01\x12\x1f\n\x12privacy_policy_url\x18\x0b \x01(\tB\x03\xe0A\x02\x12\x1f\n\x12sample_invocations\x18\x0c \x03(\tB\x03\xe0A\x01\x12K\n\x13theme_customization\x18\r \x01(\x0b2).google.actions.sdk.v2.ThemeCustomizationB\x03\xe0A\x01Bo\n\x19com.google.actions.sdk.v2B\x16LocalizedSettingsProtoP\x01Z8google.golang.org/genproto/googleapis/actions/sdk/v2;sdkb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.actions.sdk.v2.localized_settings_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x19com.google.actions.sdk.v2B\x16LocalizedSettingsProtoP\x01Z8google.golang.org/genproto/googleapis/actions/sdk/v2;sdk'
    _globals['_LOCALIZEDSETTINGS'].fields_by_name['display_name']._loaded_options = None
    _globals['_LOCALIZEDSETTINGS'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_LOCALIZEDSETTINGS'].fields_by_name['pronunciation']._loaded_options = None
    _globals['_LOCALIZEDSETTINGS'].fields_by_name['pronunciation']._serialized_options = b'\xe0A\x02'
    _globals['_LOCALIZEDSETTINGS'].fields_by_name['short_description']._loaded_options = None
    _globals['_LOCALIZEDSETTINGS'].fields_by_name['short_description']._serialized_options = b'\xe0A\x02'
    _globals['_LOCALIZEDSETTINGS'].fields_by_name['full_description']._loaded_options = None
    _globals['_LOCALIZEDSETTINGS'].fields_by_name['full_description']._serialized_options = b'\xe0A\x02'
    _globals['_LOCALIZEDSETTINGS'].fields_by_name['small_logo_image']._loaded_options = None
    _globals['_LOCALIZEDSETTINGS'].fields_by_name['small_logo_image']._serialized_options = b'\xe0A\x02'
    _globals['_LOCALIZEDSETTINGS'].fields_by_name['large_banner_image']._loaded_options = None
    _globals['_LOCALIZEDSETTINGS'].fields_by_name['large_banner_image']._serialized_options = b'\xe0A\x01'
    _globals['_LOCALIZEDSETTINGS'].fields_by_name['developer_name']._loaded_options = None
    _globals['_LOCALIZEDSETTINGS'].fields_by_name['developer_name']._serialized_options = b'\xe0A\x02'
    _globals['_LOCALIZEDSETTINGS'].fields_by_name['developer_email']._loaded_options = None
    _globals['_LOCALIZEDSETTINGS'].fields_by_name['developer_email']._serialized_options = b'\xe0A\x02'
    _globals['_LOCALIZEDSETTINGS'].fields_by_name['terms_of_service_url']._loaded_options = None
    _globals['_LOCALIZEDSETTINGS'].fields_by_name['terms_of_service_url']._serialized_options = b'\xe0A\x01'
    _globals['_LOCALIZEDSETTINGS'].fields_by_name['voice']._loaded_options = None
    _globals['_LOCALIZEDSETTINGS'].fields_by_name['voice']._serialized_options = b'\xe0A\x02'
    _globals['_LOCALIZEDSETTINGS'].fields_by_name['voice_locale']._loaded_options = None
    _globals['_LOCALIZEDSETTINGS'].fields_by_name['voice_locale']._serialized_options = b'\xe0A\x01'
    _globals['_LOCALIZEDSETTINGS'].fields_by_name['privacy_policy_url']._loaded_options = None
    _globals['_LOCALIZEDSETTINGS'].fields_by_name['privacy_policy_url']._serialized_options = b'\xe0A\x02'
    _globals['_LOCALIZEDSETTINGS'].fields_by_name['sample_invocations']._loaded_options = None
    _globals['_LOCALIZEDSETTINGS'].fields_by_name['sample_invocations']._serialized_options = b'\xe0A\x01'
    _globals['_LOCALIZEDSETTINGS'].fields_by_name['theme_customization']._loaded_options = None
    _globals['_LOCALIZEDSETTINGS'].fields_by_name['theme_customization']._serialized_options = b'\xe0A\x01'
    _globals['_LOCALIZEDSETTINGS']._serialized_start = 156
    _globals['_LOCALIZEDSETTINGS']._serialized_end = 641