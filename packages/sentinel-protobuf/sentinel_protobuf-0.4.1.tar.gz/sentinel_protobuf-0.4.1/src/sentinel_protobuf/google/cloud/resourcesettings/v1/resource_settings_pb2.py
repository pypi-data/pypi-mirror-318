"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/resourcesettings/v1/resource_settings.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8google/cloud/resourcesettings/v1/resource_settings.proto\x12 google.cloud.resourcesettings.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xb7\x03\n\x07Setting\x12\x0c\n\x04name\x18\x01 \x01(\t\x12H\n\x08metadata\x18\x07 \x01(\x0b21.google.cloud.resourcesettings.v1.SettingMetadataB\x03\xe0A\x03\x12<\n\x0blocal_value\x18\x08 \x01(\x0b2\'.google.cloud.resourcesettings.v1.Value\x12E\n\x0feffective_value\x18\t \x01(\x0b2\'.google.cloud.resourcesettings.v1.ValueB\x03\xe0A\x03\x12\x0c\n\x04etag\x18\n \x01(\t:\xc0\x01\xeaA\xbc\x01\n\'resourcesettings.googleapis.com/Setting\x121projects/{project_number}/settings/{setting_name}\x12(folders/{folder}/settings/{setting_name}\x124organizations/{organization}/settings/{setting_name}"\xbe\x02\n\x0fSettingMetadata\x12\x14\n\x0cdisplay_name\x18\x01 \x01(\t\x12\x13\n\x0bdescription\x18\x02 \x01(\t\x12\x11\n\tread_only\x18\x03 \x01(\x08\x12M\n\tdata_type\x18\x04 \x01(\x0e2:.google.cloud.resourcesettings.v1.SettingMetadata.DataType\x12>\n\rdefault_value\x18\x05 \x01(\x0b2\'.google.cloud.resourcesettings.v1.Value"^\n\x08DataType\x12\x19\n\x15DATA_TYPE_UNSPECIFIED\x10\x00\x12\x0b\n\x07BOOLEAN\x10\x01\x12\n\n\x06STRING\x10\x02\x12\x0e\n\nSTRING_SET\x10\x03\x12\x0e\n\nENUM_VALUE\x10\x04"\x92\x02\n\x05Value\x12\x17\n\rboolean_value\x18\x01 \x01(\x08H\x00\x12\x16\n\x0cstring_value\x18\x02 \x01(\tH\x00\x12M\n\x10string_set_value\x18\x03 \x01(\x0b21.google.cloud.resourcesettings.v1.Value.StringSetH\x00\x12G\n\nenum_value\x18\x04 \x01(\x0b21.google.cloud.resourcesettings.v1.Value.EnumValueH\x00\x1a\x1b\n\tStringSet\x12\x0e\n\x06values\x18\x01 \x03(\t\x1a\x1a\n\tEnumValue\x12\r\n\x05value\x18\x01 \x01(\tB\x07\n\x05value"\x94\x01\n\x13ListSettingsRequest\x12\x19\n\x06parent\x18\x01 \x01(\tB\t\xe0A\x02\xfaA\x03\n\x01*\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12;\n\x04view\x18\x04 \x01(\x0e2-.google.cloud.resourcesettings.v1.SettingView"l\n\x14ListSettingsResponse\x12;\n\x08settings\x18\x01 \x03(\x0b2).google.cloud.resourcesettings.v1.Setting\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\x8f\x01\n\x11GetSettingRequest\x12=\n\x04name\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'resourcesettings.googleapis.com/Setting\x12;\n\x04view\x18\x02 \x01(\x0e2-.google.cloud.resourcesettings.v1.SettingView"W\n\x14UpdateSettingRequest\x12?\n\x07setting\x18\x01 \x01(\x0b2).google.cloud.resourcesettings.v1.SettingB\x03\xe0A\x02*\x83\x01\n\x0bSettingView\x12\x1c\n\x18SETTING_VIEW_UNSPECIFIED\x10\x00\x12\x16\n\x12SETTING_VIEW_BASIC\x10\x01\x12 \n\x1cSETTING_VIEW_EFFECTIVE_VALUE\x10\x02\x12\x1c\n\x18SETTING_VIEW_LOCAL_VALUE\x10\x032\xfc\x06\n\x17ResourceSettingsService\x12\xfc\x01\n\x0cListSettings\x125.google.cloud.resourcesettings.v1.ListSettingsRequest\x1a6.google.cloud.resourcesettings.v1.ListSettingsResponse"}\xdaA\x06parent\x82\xd3\xe4\x93\x02n\x12%/v1/{parent=organizations/*}/settingsZ!\x12\x1f/v1/{parent=folders/*}/settingsZ"\x12 /v1/{parent=projects/*}/settings\x12\xe9\x01\n\nGetSetting\x123.google.cloud.resourcesettings.v1.GetSettingRequest\x1a).google.cloud.resourcesettings.v1.Setting"{\xdaA\x04name\x82\xd3\xe4\x93\x02n\x12%/v1/{name=organizations/*/settings/*}Z!\x12\x1f/v1/{name=folders/*/settings/*}Z"\x12 /v1/{name=projects/*/settings/*}\x12\x9d\x02\n\rUpdateSetting\x126.google.cloud.resourcesettings.v1.UpdateSettingRequest\x1a).google.cloud.resourcesettings.v1.Setting"\xa8\x01\x82\xd3\xe4\x93\x02\xa1\x012-/v1/{setting.name=organizations/*/settings/*}:\x07settingZ22\'/v1/{setting.name=folders/*/settings/*}:\x07settingZ32(/v1/{setting.name=projects/*/settings/*}:\x07setting\x1aV\x88\x02\x01\xcaA\x1fresourcesettings.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\x80\x02\n$com.google.cloud.resourcesettings.v1B\x15ResourceSettingsProtoP\x01ZPcloud.google.com/go/resourcesettings/apiv1/resourcesettingspb;resourcesettingspb\xf8\x01\x01\xaa\x02 Google.Cloud.ResourceSettings.V1\xca\x02 Google\\Cloud\\ResourceSettings\\V1\xea\x02#Google::Cloud::ResourceSettings::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.resourcesettings.v1.resource_settings_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n$com.google.cloud.resourcesettings.v1B\x15ResourceSettingsProtoP\x01ZPcloud.google.com/go/resourcesettings/apiv1/resourcesettingspb;resourcesettingspb\xf8\x01\x01\xaa\x02 Google.Cloud.ResourceSettings.V1\xca\x02 Google\\Cloud\\ResourceSettings\\V1\xea\x02#Google::Cloud::ResourceSettings::V1'
    _globals['_SETTING'].fields_by_name['metadata']._loaded_options = None
    _globals['_SETTING'].fields_by_name['metadata']._serialized_options = b'\xe0A\x03'
    _globals['_SETTING'].fields_by_name['effective_value']._loaded_options = None
    _globals['_SETTING'].fields_by_name['effective_value']._serialized_options = b'\xe0A\x03'
    _globals['_SETTING']._loaded_options = None
    _globals['_SETTING']._serialized_options = b"\xeaA\xbc\x01\n'resourcesettings.googleapis.com/Setting\x121projects/{project_number}/settings/{setting_name}\x12(folders/{folder}/settings/{setting_name}\x124organizations/{organization}/settings/{setting_name}"
    _globals['_LISTSETTINGSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTSETTINGSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA\x03\n\x01*'
    _globals['_GETSETTINGREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETSETTINGREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA)\n'resourcesettings.googleapis.com/Setting"
    _globals['_UPDATESETTINGREQUEST'].fields_by_name['setting']._loaded_options = None
    _globals['_UPDATESETTINGREQUEST'].fields_by_name['setting']._serialized_options = b'\xe0A\x02'
    _globals['_RESOURCESETTINGSSERVICE']._loaded_options = None
    _globals['_RESOURCESETTINGSSERVICE']._serialized_options = b'\x88\x02\x01\xcaA\x1fresourcesettings.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_RESOURCESETTINGSSERVICE'].methods_by_name['ListSettings']._loaded_options = None
    _globals['_RESOURCESETTINGSSERVICE'].methods_by_name['ListSettings']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02n\x12%/v1/{parent=organizations/*}/settingsZ!\x12\x1f/v1/{parent=folders/*}/settingsZ"\x12 /v1/{parent=projects/*}/settings'
    _globals['_RESOURCESETTINGSSERVICE'].methods_by_name['GetSetting']._loaded_options = None
    _globals['_RESOURCESETTINGSSERVICE'].methods_by_name['GetSetting']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02n\x12%/v1/{name=organizations/*/settings/*}Z!\x12\x1f/v1/{name=folders/*/settings/*}Z"\x12 /v1/{name=projects/*/settings/*}'
    _globals['_RESOURCESETTINGSSERVICE'].methods_by_name['UpdateSetting']._loaded_options = None
    _globals['_RESOURCESETTINGSSERVICE'].methods_by_name['UpdateSetting']._serialized_options = b"\x82\xd3\xe4\x93\x02\xa1\x012-/v1/{setting.name=organizations/*/settings/*}:\x07settingZ22'/v1/{setting.name=folders/*/settings/*}:\x07settingZ32(/v1/{setting.name=projects/*/settings/*}:\x07setting"
    _globals['_SETTINGVIEW']._serialized_start = 1746
    _globals['_SETTINGVIEW']._serialized_end = 1877
    _globals['_SETTING']._serialized_start = 210
    _globals['_SETTING']._serialized_end = 649
    _globals['_SETTINGMETADATA']._serialized_start = 652
    _globals['_SETTINGMETADATA']._serialized_end = 970
    _globals['_SETTINGMETADATA_DATATYPE']._serialized_start = 876
    _globals['_SETTINGMETADATA_DATATYPE']._serialized_end = 970
    _globals['_VALUE']._serialized_start = 973
    _globals['_VALUE']._serialized_end = 1247
    _globals['_VALUE_STRINGSET']._serialized_start = 1183
    _globals['_VALUE_STRINGSET']._serialized_end = 1210
    _globals['_VALUE_ENUMVALUE']._serialized_start = 1212
    _globals['_VALUE_ENUMVALUE']._serialized_end = 1238
    _globals['_LISTSETTINGSREQUEST']._serialized_start = 1250
    _globals['_LISTSETTINGSREQUEST']._serialized_end = 1398
    _globals['_LISTSETTINGSRESPONSE']._serialized_start = 1400
    _globals['_LISTSETTINGSRESPONSE']._serialized_end = 1508
    _globals['_GETSETTINGREQUEST']._serialized_start = 1511
    _globals['_GETSETTINGREQUEST']._serialized_end = 1654
    _globals['_UPDATESETTINGREQUEST']._serialized_start = 1656
    _globals['_UPDATESETTINGREQUEST']._serialized_end = 1743
    _globals['_RESOURCESETTINGSSERVICE']._serialized_start = 1880
    _globals['_RESOURCESETTINGSSERVICE']._serialized_end = 2772