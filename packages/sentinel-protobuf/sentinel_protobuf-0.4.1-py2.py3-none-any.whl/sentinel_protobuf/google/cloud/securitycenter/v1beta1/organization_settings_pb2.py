"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/securitycenter/v1beta1/organization_settings.proto')
_sym_db = _symbol_database.Default()
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n?google/cloud/securitycenter/v1beta1/organization_settings.proto\x12#google.cloud.securitycenter.v1beta1\x1a\x19google/api/resource.proto"\x94\x04\n\x14OrganizationSettings\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x1e\n\x16enable_asset_discovery\x18\x02 \x01(\x08\x12n\n\x16asset_discovery_config\x18\x03 \x01(\x0b2N.google.cloud.securitycenter.v1beta1.OrganizationSettings.AssetDiscoveryConfig\x1a\xf1\x01\n\x14AssetDiscoveryConfig\x12\x13\n\x0bproject_ids\x18\x01 \x03(\t\x12t\n\x0einclusion_mode\x18\x02 \x01(\x0e2\\.google.cloud.securitycenter.v1beta1.OrganizationSettings.AssetDiscoveryConfig.InclusionMode"N\n\rInclusionMode\x12\x1e\n\x1aINCLUSION_MODE_UNSPECIFIED\x10\x00\x12\x10\n\x0cINCLUDE_ONLY\x10\x01\x12\x0b\n\x07EXCLUDE\x10\x02:j\xeaAg\n2securitycenter.googleapis.com/OrganizationSettings\x121organizations/{organization}/organizationSettingsB|\n\'com.google.cloud.securitycenter.v1beta1P\x01ZOcloud.google.com/go/securitycenter/apiv1beta1/securitycenterpb;securitycenterpbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.securitycenter.v1beta1.organization_settings_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n'com.google.cloud.securitycenter.v1beta1P\x01ZOcloud.google.com/go/securitycenter/apiv1beta1/securitycenterpb;securitycenterpb"
    _globals['_ORGANIZATIONSETTINGS']._loaded_options = None
    _globals['_ORGANIZATIONSETTINGS']._serialized_options = b'\xeaAg\n2securitycenter.googleapis.com/OrganizationSettings\x121organizations/{organization}/organizationSettings'
    _globals['_ORGANIZATIONSETTINGS']._serialized_start = 132
    _globals['_ORGANIZATIONSETTINGS']._serialized_end = 664
    _globals['_ORGANIZATIONSETTINGS_ASSETDISCOVERYCONFIG']._serialized_start = 315
    _globals['_ORGANIZATIONSETTINGS_ASSETDISCOVERYCONFIG']._serialized_end = 556
    _globals['_ORGANIZATIONSETTINGS_ASSETDISCOVERYCONFIG_INCLUSIONMODE']._serialized_start = 478
    _globals['_ORGANIZATIONSETTINGS_ASSETDISCOVERYCONFIG_INCLUSIONMODE']._serialized_end = 556