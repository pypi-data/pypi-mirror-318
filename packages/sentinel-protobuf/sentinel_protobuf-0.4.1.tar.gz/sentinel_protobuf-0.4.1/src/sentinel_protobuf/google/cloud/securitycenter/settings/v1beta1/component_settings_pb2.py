"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/securitycenter/settings/v1beta1/component_settings.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nEgoogle/cloud/securitycenter/settings/v1beta1/component_settings.proto\x12,google.cloud.securitycenter.settings.v1beta1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xa7\x0c\n\x11ComponentSettings\x12\x0c\n\x04name\x18\x01 \x01(\t\x12U\n\x05state\x18\x02 \x01(\x0e2F.google.cloud.securitycenter.settings.v1beta1.ComponentEnablementState\x12$\n\x17project_service_account\x18\x03 \x01(\tB\x03\xe0A\x03\x12p\n\x11detector_settings\x18\x04 \x03(\x0b2U.google.cloud.securitycenter.settings.v1beta1.ComponentSettings.DetectorSettingsEntry\x12\x11\n\x04etag\x18\x05 \x01(\tB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12}\n#container_threat_detection_settings\x18) \x01(\x0b2N.google.cloud.securitycenter.settings.v1beta1.ContainerThreatDetectionSettingsH\x00\x12u\n\x1fevent_threat_detection_settings\x18* \x01(\x0b2J.google.cloud.securitycenter.settings.v1beta1.EventThreatDetectionSettingsH\x00\x12{\n"security_health_analytics_settings\x18, \x01(\x0b2M.google.cloud.securitycenter.settings.v1beta1.SecurityHealthAnalyticsSettingsH\x00\x12i\n\x1dweb_security_scanner_settings\x18( \x01(\x0b2@.google.cloud.securitycenter.settings.v1beta1.WebSecurityScannerH\x00\x1ai\n\x10DetectorSettings\x12U\n\x05state\x18\x01 \x01(\x0e2F.google.cloud.securitycenter.settings.v1beta1.ComponentEnablementState\x1a\x89\x01\n\x15DetectorSettingsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12_\n\x05value\x18\x02 \x01(\x0b2P.google.cloud.securitycenter.settings.v1beta1.ComponentSettings.DetectorSettings:\x028\x01:\xe1\x03\xeaA\xdd\x03\n/securitycenter.googleapis.com/ComponentSettings\x12<organizations/{organization}/components/{component}/settings\x120folders/{folder}/components/{component}/settings\x122projects/{project}/components/{component}/settings\x12Zprojects/{project}/locations/{location}/clusters/{cluster}/components/{component}/settings\x12Vprojects/{project}/regions/{region}/clusters/{cluster}/components/{component}/settings\x12Rprojects/{project}/zones/{zone}/clusters/{cluster}/components/{component}/settingsB\x13\n\x11specific_settings"\x14\n\x12WebSecurityScanner""\n ContainerThreatDetectionSettings"\x1e\n\x1cEventThreatDetectionSettings"\xb6\x03\n\x1fSecurityHealthAnalyticsSettings\x12\x8a\x01\n\x1bnon_org_iam_member_settings\x18\x01 \x01(\x0b2e.google.cloud.securitycenter.settings.v1beta1.SecurityHealthAnalyticsSettings.NonOrgIamMemberSettings\x12\x91\x01\n\x1eadmin_service_account_settings\x18\x02 \x01(\x0b2i.google.cloud.securitycenter.settings.v1beta1.SecurityHealthAnalyticsSettings.AdminServiceAccountSettings\x1a6\n\x17NonOrgIamMemberSettings\x12\x1b\n\x13approved_identities\x18\x01 \x03(\t\x1a:\n\x1bAdminServiceAccountSettings\x12\x1b\n\x13approved_identities\x18\x01 \x03(\t*l\n\x18ComponentEnablementState\x12*\n&COMPONENT_ENABLEMENT_STATE_UNSPECIFIED\x10\x00\x12\x0b\n\x07DISABLE\x10\x01\x12\n\n\x06ENABLE\x10\x02\x12\x0b\n\x07INHERIT\x10\x03B\xae\x02\n0com.google.cloud.securitycenter.settings.v1beta1B\x16ComponentSettingsProtoP\x01ZLcloud.google.com/go/securitycenter/settings/apiv1beta1/settingspb;settingspb\xf8\x01\x01\xaa\x02,Google.Cloud.SecurityCenter.Settings.V1Beta1\xca\x02,Google\\Cloud\\SecurityCenter\\Settings\\V1beta1\xea\x020Google::Cloud::SecurityCenter::Settings::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.securitycenter.settings.v1beta1.component_settings_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n0com.google.cloud.securitycenter.settings.v1beta1B\x16ComponentSettingsProtoP\x01ZLcloud.google.com/go/securitycenter/settings/apiv1beta1/settingspb;settingspb\xf8\x01\x01\xaa\x02,Google.Cloud.SecurityCenter.Settings.V1Beta1\xca\x02,Google\\Cloud\\SecurityCenter\\Settings\\V1beta1\xea\x020Google::Cloud::SecurityCenter::Settings::V1beta1'
    _globals['_COMPONENTSETTINGS_DETECTORSETTINGSENTRY']._loaded_options = None
    _globals['_COMPONENTSETTINGS_DETECTORSETTINGSENTRY']._serialized_options = b'8\x01'
    _globals['_COMPONENTSETTINGS'].fields_by_name['project_service_account']._loaded_options = None
    _globals['_COMPONENTSETTINGS'].fields_by_name['project_service_account']._serialized_options = b'\xe0A\x03'
    _globals['_COMPONENTSETTINGS'].fields_by_name['etag']._loaded_options = None
    _globals['_COMPONENTSETTINGS'].fields_by_name['etag']._serialized_options = b'\xe0A\x03'
    _globals['_COMPONENTSETTINGS'].fields_by_name['update_time']._loaded_options = None
    _globals['_COMPONENTSETTINGS'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_COMPONENTSETTINGS']._loaded_options = None
    _globals['_COMPONENTSETTINGS']._serialized_options = b'\xeaA\xdd\x03\n/securitycenter.googleapis.com/ComponentSettings\x12<organizations/{organization}/components/{component}/settings\x120folders/{folder}/components/{component}/settings\x122projects/{project}/components/{component}/settings\x12Zprojects/{project}/locations/{location}/clusters/{cluster}/components/{component}/settings\x12Vprojects/{project}/regions/{region}/clusters/{cluster}/components/{component}/settings\x12Rprojects/{project}/zones/{zone}/clusters/{cluster}/components/{component}/settings'
    _globals['_COMPONENTENABLEMENTSTATE']._serialized_start = 2321
    _globals['_COMPONENTENABLEMENTSTATE']._serialized_end = 2429
    _globals['_COMPONENTSETTINGS']._serialized_start = 213
    _globals['_COMPONENTSETTINGS']._serialized_end = 1788
    _globals['_COMPONENTSETTINGS_DETECTORSETTINGS']._serialized_start = 1038
    _globals['_COMPONENTSETTINGS_DETECTORSETTINGS']._serialized_end = 1143
    _globals['_COMPONENTSETTINGS_DETECTORSETTINGSENTRY']._serialized_start = 1146
    _globals['_COMPONENTSETTINGS_DETECTORSETTINGSENTRY']._serialized_end = 1283
    _globals['_WEBSECURITYSCANNER']._serialized_start = 1790
    _globals['_WEBSECURITYSCANNER']._serialized_end = 1810
    _globals['_CONTAINERTHREATDETECTIONSETTINGS']._serialized_start = 1812
    _globals['_CONTAINERTHREATDETECTIONSETTINGS']._serialized_end = 1846
    _globals['_EVENTTHREATDETECTIONSETTINGS']._serialized_start = 1848
    _globals['_EVENTTHREATDETECTIONSETTINGS']._serialized_end = 1878
    _globals['_SECURITYHEALTHANALYTICSSETTINGS']._serialized_start = 1881
    _globals['_SECURITYHEALTHANALYTICSSETTINGS']._serialized_end = 2319
    _globals['_SECURITYHEALTHANALYTICSSETTINGS_NONORGIAMMEMBERSETTINGS']._serialized_start = 2205
    _globals['_SECURITYHEALTHANALYTICSSETTINGS_NONORGIAMMEMBERSETTINGS']._serialized_end = 2259
    _globals['_SECURITYHEALTHANALYTICSSETTINGS_ADMINSERVICEACCOUNTSETTINGS']._serialized_start = 2261
    _globals['_SECURITYHEALTHANALYTICSSETTINGS_ADMINSERVICEACCOUNTSETTINGS']._serialized_end = 2319