"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/securitycenter/v1/organization_settings.proto')
_sym_db = _symbol_database.Default()
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:google/cloud/securitycenter/v1/organization_settings.proto\x12\x1egoogle.cloud.securitycenter.v1\x1a\x19google/api/resource.proto"\xcc\x04\n\x14OrganizationSettings\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x1e\n\x16enable_asset_discovery\x18\x02 \x01(\x08\x12i\n\x16asset_discovery_config\x18\x03 \x01(\x0b2I.google.cloud.securitycenter.v1.OrganizationSettings.AssetDiscoveryConfig\x1a\x80\x02\n\x14AssetDiscoveryConfig\x12\x13\n\x0bproject_ids\x18\x01 \x03(\t\x12o\n\x0einclusion_mode\x18\x02 \x01(\x0e2W.google.cloud.securitycenter.v1.OrganizationSettings.AssetDiscoveryConfig.InclusionMode\x12\x12\n\nfolder_ids\x18\x03 \x03(\t"N\n\rInclusionMode\x12\x1e\n\x1aINCLUSION_MODE_UNSPECIFIED\x10\x00\x12\x10\n\x0cINCLUDE_ONLY\x10\x01\x12\x0b\n\x07EXCLUDE\x10\x02:\x97\x01\xeaA\x93\x01\n2securitycenter.googleapis.com/OrganizationSettings\x121organizations/{organization}/organizationSettings*\x14organizationSettings2\x14organizationSettingsB\xd8\x01\n"com.google.cloud.securitycenter.v1P\x01ZJcloud.google.com/go/securitycenter/apiv1/securitycenterpb;securitycenterpb\xaa\x02\x1eGoogle.Cloud.SecurityCenter.V1\xca\x02\x1eGoogle\\Cloud\\SecurityCenter\\V1\xea\x02!Google::Cloud::SecurityCenter::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.securitycenter.v1.organization_settings_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.cloud.securitycenter.v1P\x01ZJcloud.google.com/go/securitycenter/apiv1/securitycenterpb;securitycenterpb\xaa\x02\x1eGoogle.Cloud.SecurityCenter.V1\xca\x02\x1eGoogle\\Cloud\\SecurityCenter\\V1\xea\x02!Google::Cloud::SecurityCenter::V1'
    _globals['_ORGANIZATIONSETTINGS']._loaded_options = None
    _globals['_ORGANIZATIONSETTINGS']._serialized_options = b'\xeaA\x93\x01\n2securitycenter.googleapis.com/OrganizationSettings\x121organizations/{organization}/organizationSettings*\x14organizationSettings2\x14organizationSettings'
    _globals['_ORGANIZATIONSETTINGS']._serialized_start = 122
    _globals['_ORGANIZATIONSETTINGS']._serialized_end = 710
    _globals['_ORGANIZATIONSETTINGS_ASSETDISCOVERYCONFIG']._serialized_start = 300
    _globals['_ORGANIZATIONSETTINGS_ASSETDISCOVERYCONFIG']._serialized_end = 556
    _globals['_ORGANIZATIONSETTINGS_ASSETDISCOVERYCONFIG_INCLUSIONMODE']._serialized_start = 478
    _globals['_ORGANIZATIONSETTINGS_ASSETDISCOVERYCONFIG_INCLUSIONMODE']._serialized_end = 556