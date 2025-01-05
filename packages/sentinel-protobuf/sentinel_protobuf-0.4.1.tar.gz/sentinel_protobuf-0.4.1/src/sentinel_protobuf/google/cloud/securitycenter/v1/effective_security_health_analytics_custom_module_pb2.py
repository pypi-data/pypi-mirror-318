"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/securitycenter/v1/effective_security_health_analytics_custom_module.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.securitycenter.v1 import security_health_analytics_custom_config_pb2 as google_dot_cloud_dot_securitycenter_dot_v1_dot_security__health__analytics__custom__config__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nVgoogle/cloud/securitycenter/v1/effective_security_health_analytics_custom_module.proto\x12\x1egoogle.cloud.securitycenter.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1aLgoogle/cloud/securitycenter/v1/security_health_analytics_custom_config.proto"\xfd\x05\n,EffectiveSecurityHealthAnalyticsCustomModule\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12H\n\rcustom_config\x18\x02 \x01(\x0b2,.google.cloud.securitycenter.v1.CustomConfigB\x03\xe0A\x03\x12{\n\x10enablement_state\x18\x03 \x01(\x0e2\\.google.cloud.securitycenter.v1.EffectiveSecurityHealthAnalyticsCustomModule.EnablementStateB\x03\xe0A\x03\x12\x19\n\x0cdisplay_name\x18\x04 \x01(\tB\x03\xe0A\x03"N\n\x0fEnablementState\x12 \n\x1cENABLEMENT_STATE_UNSPECIFIED\x10\x00\x12\x0b\n\x07ENABLED\x10\x01\x12\x0c\n\x08DISABLED\x10\x02:\x87\x03\xeaA\x83\x03\nJsecuritycenter.googleapis.com/EffectiveSecurityHealthAnalyticsCustomModule\x12morganizations/{organization}/securityHealthAnalyticsSettings/effectiveCustomModules/{effective_custom_module}\x12afolders/{folder}/securityHealthAnalyticsSettings/effectiveCustomModules/{effective_custom_module}\x12cprojects/{project}/securityHealthAnalyticsSettings/effectiveCustomModules/{effective_custom_module}B\x8b\x02\n"com.google.cloud.securitycenter.v1B1EffectiveSecurityHealthAnalyticsCustomModuleProtoP\x01ZJcloud.google.com/go/securitycenter/apiv1/securitycenterpb;securitycenterpb\xaa\x02\x1eGoogle.Cloud.SecurityCenter.V1\xca\x02\x1eGoogle\\Cloud\\SecurityCenter\\V1\xea\x02!Google::Cloud::SecurityCenter::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.securitycenter.v1.effective_security_health_analytics_custom_module_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.cloud.securitycenter.v1B1EffectiveSecurityHealthAnalyticsCustomModuleProtoP\x01ZJcloud.google.com/go/securitycenter/apiv1/securitycenterpb;securitycenterpb\xaa\x02\x1eGoogle.Cloud.SecurityCenter.V1\xca\x02\x1eGoogle\\Cloud\\SecurityCenter\\V1\xea\x02!Google::Cloud::SecurityCenter::V1'
    _globals['_EFFECTIVESECURITYHEALTHANALYTICSCUSTOMMODULE'].fields_by_name['name']._loaded_options = None
    _globals['_EFFECTIVESECURITYHEALTHANALYTICSCUSTOMMODULE'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_EFFECTIVESECURITYHEALTHANALYTICSCUSTOMMODULE'].fields_by_name['custom_config']._loaded_options = None
    _globals['_EFFECTIVESECURITYHEALTHANALYTICSCUSTOMMODULE'].fields_by_name['custom_config']._serialized_options = b'\xe0A\x03'
    _globals['_EFFECTIVESECURITYHEALTHANALYTICSCUSTOMMODULE'].fields_by_name['enablement_state']._loaded_options = None
    _globals['_EFFECTIVESECURITYHEALTHANALYTICSCUSTOMMODULE'].fields_by_name['enablement_state']._serialized_options = b'\xe0A\x03'
    _globals['_EFFECTIVESECURITYHEALTHANALYTICSCUSTOMMODULE'].fields_by_name['display_name']._loaded_options = None
    _globals['_EFFECTIVESECURITYHEALTHANALYTICSCUSTOMMODULE'].fields_by_name['display_name']._serialized_options = b'\xe0A\x03'
    _globals['_EFFECTIVESECURITYHEALTHANALYTICSCUSTOMMODULE']._loaded_options = None
    _globals['_EFFECTIVESECURITYHEALTHANALYTICSCUSTOMMODULE']._serialized_options = b'\xeaA\x83\x03\nJsecuritycenter.googleapis.com/EffectiveSecurityHealthAnalyticsCustomModule\x12morganizations/{organization}/securityHealthAnalyticsSettings/effectiveCustomModules/{effective_custom_module}\x12afolders/{folder}/securityHealthAnalyticsSettings/effectiveCustomModules/{effective_custom_module}\x12cprojects/{project}/securityHealthAnalyticsSettings/effectiveCustomModules/{effective_custom_module}'
    _globals['_EFFECTIVESECURITYHEALTHANALYTICSCUSTOMMODULE']._serialized_start = 261
    _globals['_EFFECTIVESECURITYHEALTHANALYTICSCUSTOMMODULE']._serialized_end = 1026
    _globals['_EFFECTIVESECURITYHEALTHANALYTICSCUSTOMMODULE_ENABLEMENTSTATE']._serialized_start = 554
    _globals['_EFFECTIVESECURITYHEALTHANALYTICSCUSTOMMODULE_ENABLEMENTSTATE']._serialized_end = 632