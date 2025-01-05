"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/securitycenter/settings/v1beta1/settings.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ......google.cloud.securitycenter.settings.v1beta1 import billing_settings_pb2 as google_dot_cloud_dot_securitycenter_dot_settings_dot_v1beta1_dot_billing__settings__pb2
from ......google.cloud.securitycenter.settings.v1beta1 import component_settings_pb2 as google_dot_cloud_dot_securitycenter_dot_settings_dot_v1beta1_dot_component__settings__pb2
from ......google.cloud.securitycenter.settings.v1beta1 import sink_settings_pb2 as google_dot_cloud_dot_securitycenter_dot_settings_dot_v1beta1_dot_sink__settings__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n;google/cloud/securitycenter/settings/v1beta1/settings.proto\x12,google.cloud.securitycenter.settings.v1beta1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1aCgoogle/cloud/securitycenter/settings/v1beta1/billing_settings.proto\x1aEgoogle/cloud/securitycenter/settings/v1beta1/component_settings.proto\x1a@google/cloud/securitycenter/settings/v1beta1/sink_settings.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xe1\x0b\n\x08Settings\x12\x0c\n\x04name\x18\x01 \x01(\t\x12W\n\x10billing_settings\x18\x02 \x01(\x0b2=.google.cloud.securitycenter.settings.v1beta1.BillingSettings\x12U\n\x05state\x18\x03 \x01(\x0e2F.google.cloud.securitycenter.settings.v1beta1.Settings.OnboardingState\x12 \n\x13org_service_account\x18\x05 \x01(\tB\x03\xe0A\x03\x12Q\n\rsink_settings\x18\x06 \x01(\x0b2:.google.cloud.securitycenter.settings.v1beta1.SinkSettings\x12i\n\x12component_settings\x18\x07 \x03(\x0b2M.google.cloud.securitycenter.settings.v1beta1.Settings.ComponentSettingsEntry\x12r\n\x17detector_group_settings\x18\x08 \x03(\x0b2Q.google.cloud.securitycenter.settings.v1beta1.Settings.DetectorGroupSettingsEntry\x12\x0c\n\x04etag\x18\t \x01(\t\x124\n\x0bupdate_time\x18\n \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x1an\n\x15DetectorGroupSettings\x12U\n\x05state\x18\x01 \x01(\x0e2F.google.cloud.securitycenter.settings.v1beta1.ComponentEnablementState\x1ay\n\x16ComponentSettingsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12N\n\x05value\x18\x02 \x01(\x0b2?.google.cloud.securitycenter.settings.v1beta1.ComponentSettings:\x028\x01\x1a\x8a\x01\n\x1aDetectorGroupSettingsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12[\n\x05value\x18\x02 \x01(\x0b2L.google.cloud.securitycenter.settings.v1beta1.Settings.DetectorGroupSettings:\x028\x01"\xb5\x01\n\x0fOnboardingState\x12 \n\x1cONBOARDING_STATE_UNSPECIFIED\x10\x00\x12\x0b\n\x07ENABLED\x10\x01\x12\x0c\n\x08DISABLED\x10\x02\x12\x14\n\x10BILLING_SELECTED\x10\x03\x12\x16\n\x12PROVIDERS_SELECTED\x10\x04\x12\x16\n\x12RESOURCES_SELECTED\x10\x05\x12\x1f\n\x1bORG_SERVICE_ACCOUNT_CREATED\x10\x06:\xce\x02\xeaA\xca\x02\n&securitycenter.googleapis.com/Settings\x12%organizations/{organization}/settings\x12\x19folders/{folder}/settings\x12\x1bprojects/{project}/settings\x12Cprojects/{project}/locations/{location}/clusters/{cluster}/settings\x12?projects/{project}/regions/{region}/clusters/{cluster}/settings\x12;projects/{project}/zones/{zone}/clusters/{cluster}/settingsB\xa5\x02\n0com.google.cloud.securitycenter.settings.v1beta1B\rSettingsProtoP\x01ZLcloud.google.com/go/securitycenter/settings/apiv1beta1/settingspb;settingspb\xf8\x01\x01\xaa\x02,Google.Cloud.SecurityCenter.Settings.V1Beta1\xca\x02,Google\\Cloud\\SecurityCenter\\Settings\\V1beta1\xea\x020Google::Cloud::SecurityCenter::Settings::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.securitycenter.settings.v1beta1.settings_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n0com.google.cloud.securitycenter.settings.v1beta1B\rSettingsProtoP\x01ZLcloud.google.com/go/securitycenter/settings/apiv1beta1/settingspb;settingspb\xf8\x01\x01\xaa\x02,Google.Cloud.SecurityCenter.Settings.V1Beta1\xca\x02,Google\\Cloud\\SecurityCenter\\Settings\\V1beta1\xea\x020Google::Cloud::SecurityCenter::Settings::V1beta1'
    _globals['_SETTINGS_COMPONENTSETTINGSENTRY']._loaded_options = None
    _globals['_SETTINGS_COMPONENTSETTINGSENTRY']._serialized_options = b'8\x01'
    _globals['_SETTINGS_DETECTORGROUPSETTINGSENTRY']._loaded_options = None
    _globals['_SETTINGS_DETECTORGROUPSETTINGSENTRY']._serialized_options = b'8\x01'
    _globals['_SETTINGS'].fields_by_name['org_service_account']._loaded_options = None
    _globals['_SETTINGS'].fields_by_name['org_service_account']._serialized_options = b'\xe0A\x03'
    _globals['_SETTINGS'].fields_by_name['update_time']._loaded_options = None
    _globals['_SETTINGS'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_SETTINGS']._loaded_options = None
    _globals['_SETTINGS']._serialized_options = b'\xeaA\xca\x02\n&securitycenter.googleapis.com/Settings\x12%organizations/{organization}/settings\x12\x19folders/{folder}/settings\x12\x1bprojects/{project}/settings\x12Cprojects/{project}/locations/{location}/clusters/{cluster}/settings\x12?projects/{project}/regions/{region}/clusters/{cluster}/settings\x12;projects/{project}/zones/{zone}/clusters/{cluster}/settings'
    _globals['_SETTINGS']._serialized_start = 409
    _globals['_SETTINGS']._serialized_end = 1914
    _globals['_SETTINGS_DETECTORGROUPSETTINGS']._serialized_start = 1019
    _globals['_SETTINGS_DETECTORGROUPSETTINGS']._serialized_end = 1129
    _globals['_SETTINGS_COMPONENTSETTINGSENTRY']._serialized_start = 1131
    _globals['_SETTINGS_COMPONENTSETTINGSENTRY']._serialized_end = 1252
    _globals['_SETTINGS_DETECTORGROUPSETTINGSENTRY']._serialized_start = 1255
    _globals['_SETTINGS_DETECTORGROUPSETTINGSENTRY']._serialized_end = 1393
    _globals['_SETTINGS_ONBOARDINGSTATE']._serialized_start = 1396
    _globals['_SETTINGS_ONBOARDINGSTATE']._serialized_end = 1577