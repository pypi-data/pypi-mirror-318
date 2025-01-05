"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/securitycenter/v1/security_health_analytics_custom_module.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.securitycenter.v1 import security_health_analytics_custom_config_pb2 as google_dot_cloud_dot_securitycenter_dot_v1_dot_security__health__analytics__custom__config__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nLgoogle/cloud/securitycenter/v1/security_health_analytics_custom_module.proto\x12\x1egoogle.cloud.securitycenter.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1aLgoogle/cloud/securitycenter/v1/security_health_analytics_custom_config.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xdd\x06\n#SecurityHealthAnalyticsCustomModule\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x05\x12\x14\n\x0cdisplay_name\x18\x02 \x01(\t\x12m\n\x10enablement_state\x18\x04 \x01(\x0e2S.google.cloud.securitycenter.v1.SecurityHealthAnalyticsCustomModule.EnablementState\x124\n\x0bupdate_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x18\n\x0blast_editor\x18\x06 \x01(\tB\x03\xe0A\x03\x12b\n\x0fancestor_module\x18\x07 \x01(\tBI\xe0A\x03\xfaAC\nAsecuritycenter.googleapis.com/SecurityHealthAnalyticsCustomModule\x12C\n\rcustom_config\x18\x08 \x01(\x0b2,.google.cloud.securitycenter.v1.CustomConfig"]\n\x0fEnablementState\x12 \n\x1cENABLEMENT_STATE_UNSPECIFIED\x10\x00\x12\x0b\n\x07ENABLED\x10\x01\x12\x0c\n\x08DISABLED\x10\x02\x12\r\n\tINHERITED\x10\x03:\xc5\x02\xeaA\xc1\x02\nAsecuritycenter.googleapis.com/SecurityHealthAnalyticsCustomModule\x12Zorganizations/{organization}/securityHealthAnalyticsSettings/customModules/{custom_module}\x12Nfolders/{folder}/securityHealthAnalyticsSettings/customModules/{custom_module}\x12Pprojects/{project}/securityHealthAnalyticsSettings/customModules/{custom_module}B\xe9\x03\n"com.google.cloud.securitycenter.v1B(SecurityHealthAnalyticsCustomModuleProtoP\x01ZJcloud.google.com/go/securitycenter/apiv1/securitycenterpb;securitycenterpb\xaa\x02\x1eGoogle.Cloud.SecurityCenter.V1\xca\x02\x1eGoogle\\Cloud\\SecurityCenter\\V1\xea\x02!Google::Cloud::SecurityCenter::V1\xeaA\xe3\x01\n=securitycenter.googleapis.com/SecurityHealthAnalyticsSettings\x12<organizations/{organization}/securityHealthAnalyticsSettings\x120folders/{folder}/securityHealthAnalyticsSettings\x122projects/{project}/securityHealthAnalyticsSettingsb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.securitycenter.v1.security_health_analytics_custom_module_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.cloud.securitycenter.v1B(SecurityHealthAnalyticsCustomModuleProtoP\x01ZJcloud.google.com/go/securitycenter/apiv1/securitycenterpb;securitycenterpb\xaa\x02\x1eGoogle.Cloud.SecurityCenter.V1\xca\x02\x1eGoogle\\Cloud\\SecurityCenter\\V1\xea\x02!Google::Cloud::SecurityCenter::V1\xeaA\xe3\x01\n=securitycenter.googleapis.com/SecurityHealthAnalyticsSettings\x12<organizations/{organization}/securityHealthAnalyticsSettings\x120folders/{folder}/securityHealthAnalyticsSettings\x122projects/{project}/securityHealthAnalyticsSettings'
    _globals['_SECURITYHEALTHANALYTICSCUSTOMMODULE'].fields_by_name['name']._loaded_options = None
    _globals['_SECURITYHEALTHANALYTICSCUSTOMMODULE'].fields_by_name['name']._serialized_options = b'\xe0A\x05'
    _globals['_SECURITYHEALTHANALYTICSCUSTOMMODULE'].fields_by_name['update_time']._loaded_options = None
    _globals['_SECURITYHEALTHANALYTICSCUSTOMMODULE'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_SECURITYHEALTHANALYTICSCUSTOMMODULE'].fields_by_name['last_editor']._loaded_options = None
    _globals['_SECURITYHEALTHANALYTICSCUSTOMMODULE'].fields_by_name['last_editor']._serialized_options = b'\xe0A\x03'
    _globals['_SECURITYHEALTHANALYTICSCUSTOMMODULE'].fields_by_name['ancestor_module']._loaded_options = None
    _globals['_SECURITYHEALTHANALYTICSCUSTOMMODULE'].fields_by_name['ancestor_module']._serialized_options = b'\xe0A\x03\xfaAC\nAsecuritycenter.googleapis.com/SecurityHealthAnalyticsCustomModule'
    _globals['_SECURITYHEALTHANALYTICSCUSTOMMODULE']._loaded_options = None
    _globals['_SECURITYHEALTHANALYTICSCUSTOMMODULE']._serialized_options = b'\xeaA\xc1\x02\nAsecuritycenter.googleapis.com/SecurityHealthAnalyticsCustomModule\x12Zorganizations/{organization}/securityHealthAnalyticsSettings/customModules/{custom_module}\x12Nfolders/{folder}/securityHealthAnalyticsSettings/customModules/{custom_module}\x12Pprojects/{project}/securityHealthAnalyticsSettings/customModules/{custom_module}'
    _globals['_SECURITYHEALTHANALYTICSCUSTOMMODULE']._serialized_start = 284
    _globals['_SECURITYHEALTHANALYTICSCUSTOMMODULE']._serialized_end = 1145
    _globals['_SECURITYHEALTHANALYTICSCUSTOMMODULE_ENABLEMENTSTATE']._serialized_start = 724
    _globals['_SECURITYHEALTHANALYTICSCUSTOMMODULE_ENABLEMENTSTATE']._serialized_end = 817