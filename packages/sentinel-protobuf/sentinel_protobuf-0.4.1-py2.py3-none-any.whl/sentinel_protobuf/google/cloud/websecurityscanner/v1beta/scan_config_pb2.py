"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/websecurityscanner/v1beta/scan_config.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.websecurityscanner.v1beta import scan_run_pb2 as google_dot_cloud_dot_websecurityscanner_dot_v1beta_dot_scan__run__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8google/cloud/websecurityscanner/v1beta/scan_config.proto\x12&google.cloud.websecurityscanner.v1beta\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a5google/cloud/websecurityscanner/v1beta/scan_run.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xa6\r\n\nScanConfig\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x0f\n\x07max_qps\x18\x03 \x01(\x05\x12\x1a\n\rstarting_urls\x18\x04 \x03(\tB\x03\xe0A\x02\x12Y\n\x0eauthentication\x18\x05 \x01(\x0b2A.google.cloud.websecurityscanner.v1beta.ScanConfig.Authentication\x12P\n\nuser_agent\x18\x06 \x01(\x0e2<.google.cloud.websecurityscanner.v1beta.ScanConfig.UserAgent\x12\x1a\n\x12blacklist_patterns\x18\x07 \x03(\t\x12M\n\x08schedule\x18\x08 \x01(\x0b2;.google.cloud.websecurityscanner.v1beta.ScanConfig.Schedule\x12[\n\x10target_platforms\x18\t \x03(\x0e2A.google.cloud.websecurityscanner.v1beta.ScanConfig.TargetPlatform\x12{\n!export_to_security_command_center\x18\n \x01(\x0e2P.google.cloud.websecurityscanner.v1beta.ScanConfig.ExportToSecurityCommandCenter\x12C\n\nlatest_run\x18\x0b \x01(\x0b2/.google.cloud.websecurityscanner.v1beta.ScanRun\x12P\n\nrisk_level\x18\x0c \x01(\x0e2<.google.cloud.websecurityscanner.v1beta.ScanConfig.RiskLevel\x1a\x94\x03\n\x0eAuthentication\x12i\n\x0egoogle_account\x18\x01 \x01(\x0b2O.google.cloud.websecurityscanner.v1beta.ScanConfig.Authentication.GoogleAccountH\x00\x12i\n\x0ecustom_account\x18\x02 \x01(\x0b2O.google.cloud.websecurityscanner.v1beta.ScanConfig.Authentication.CustomAccountH\x00\x1a@\n\rGoogleAccount\x12\x15\n\x08username\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x18\n\x08password\x18\x02 \x01(\tB\x06\xe0A\x02\xe0A\x04\x1aX\n\rCustomAccount\x12\x15\n\x08username\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x18\n\x08password\x18\x02 \x01(\tB\x06\xe0A\x02\xe0A\x04\x12\x16\n\tlogin_url\x18\x03 \x01(\tB\x03\xe0A\x02B\x10\n\x0eauthentication\x1ab\n\x08Schedule\x121\n\rschedule_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12#\n\x16interval_duration_days\x18\x02 \x01(\x05B\x03\xe0A\x02"`\n\tUserAgent\x12\x1a\n\x16USER_AGENT_UNSPECIFIED\x10\x00\x12\x10\n\x0cCHROME_LINUX\x10\x01\x12\x12\n\x0eCHROME_ANDROID\x10\x02\x12\x11\n\rSAFARI_IPHONE\x10\x03"N\n\x0eTargetPlatform\x12\x1f\n\x1bTARGET_PLATFORM_UNSPECIFIED\x10\x00\x12\x0e\n\nAPP_ENGINE\x10\x01\x12\x0b\n\x07COMPUTE\x10\x02"<\n\tRiskLevel\x12\x1a\n\x16RISK_LEVEL_UNSPECIFIED\x10\x00\x12\n\n\x06NORMAL\x10\x01\x12\x07\n\x03LOW\x10\x02"m\n\x1dExportToSecurityCommandCenter\x121\n-EXPORT_TO_SECURITY_COMMAND_CENTER_UNSPECIFIED\x10\x00\x12\x0b\n\x07ENABLED\x10\x01\x12\x0c\n\x08DISABLED\x10\x02:_\xeaA\\\n,websecurityscanner.googleapis.com/ScanConfig\x12,projects/{project}/scanConfigs/{scan_config}B\x99\x02\n*com.google.cloud.websecurityscanner.v1betaB\x0fScanConfigProtoP\x01ZZcloud.google.com/go/websecurityscanner/apiv1beta/websecurityscannerpb;websecurityscannerpb\xaa\x02&Google.Cloud.WebSecurityScanner.V1Beta\xca\x02&Google\\Cloud\\WebSecurityScanner\\V1beta\xea\x02)Google::Cloud::WebSecurityScanner::V1betab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.websecurityscanner.v1beta.scan_config_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n*com.google.cloud.websecurityscanner.v1betaB\x0fScanConfigProtoP\x01ZZcloud.google.com/go/websecurityscanner/apiv1beta/websecurityscannerpb;websecurityscannerpb\xaa\x02&Google.Cloud.WebSecurityScanner.V1Beta\xca\x02&Google\\Cloud\\WebSecurityScanner\\V1beta\xea\x02)Google::Cloud::WebSecurityScanner::V1beta'
    _globals['_SCANCONFIG_AUTHENTICATION_GOOGLEACCOUNT'].fields_by_name['username']._loaded_options = None
    _globals['_SCANCONFIG_AUTHENTICATION_GOOGLEACCOUNT'].fields_by_name['username']._serialized_options = b'\xe0A\x02'
    _globals['_SCANCONFIG_AUTHENTICATION_GOOGLEACCOUNT'].fields_by_name['password']._loaded_options = None
    _globals['_SCANCONFIG_AUTHENTICATION_GOOGLEACCOUNT'].fields_by_name['password']._serialized_options = b'\xe0A\x02\xe0A\x04'
    _globals['_SCANCONFIG_AUTHENTICATION_CUSTOMACCOUNT'].fields_by_name['username']._loaded_options = None
    _globals['_SCANCONFIG_AUTHENTICATION_CUSTOMACCOUNT'].fields_by_name['username']._serialized_options = b'\xe0A\x02'
    _globals['_SCANCONFIG_AUTHENTICATION_CUSTOMACCOUNT'].fields_by_name['password']._loaded_options = None
    _globals['_SCANCONFIG_AUTHENTICATION_CUSTOMACCOUNT'].fields_by_name['password']._serialized_options = b'\xe0A\x02\xe0A\x04'
    _globals['_SCANCONFIG_AUTHENTICATION_CUSTOMACCOUNT'].fields_by_name['login_url']._loaded_options = None
    _globals['_SCANCONFIG_AUTHENTICATION_CUSTOMACCOUNT'].fields_by_name['login_url']._serialized_options = b'\xe0A\x02'
    _globals['_SCANCONFIG_SCHEDULE'].fields_by_name['interval_duration_days']._loaded_options = None
    _globals['_SCANCONFIG_SCHEDULE'].fields_by_name['interval_duration_days']._serialized_options = b'\xe0A\x02'
    _globals['_SCANCONFIG'].fields_by_name['display_name']._loaded_options = None
    _globals['_SCANCONFIG'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_SCANCONFIG'].fields_by_name['starting_urls']._loaded_options = None
    _globals['_SCANCONFIG'].fields_by_name['starting_urls']._serialized_options = b'\xe0A\x02'
    _globals['_SCANCONFIG']._loaded_options = None
    _globals['_SCANCONFIG']._serialized_options = b'\xeaA\\\n,websecurityscanner.googleapis.com/ScanConfig\x12,projects/{project}/scanConfigs/{scan_config}'
    _globals['_SCANCONFIG']._serialized_start = 249
    _globals['_SCANCONFIG']._serialized_end = 1951
    _globals['_SCANCONFIG_AUTHENTICATION']._serialized_start = 999
    _globals['_SCANCONFIG_AUTHENTICATION']._serialized_end = 1403
    _globals['_SCANCONFIG_AUTHENTICATION_GOOGLEACCOUNT']._serialized_start = 1231
    _globals['_SCANCONFIG_AUTHENTICATION_GOOGLEACCOUNT']._serialized_end = 1295
    _globals['_SCANCONFIG_AUTHENTICATION_CUSTOMACCOUNT']._serialized_start = 1297
    _globals['_SCANCONFIG_AUTHENTICATION_CUSTOMACCOUNT']._serialized_end = 1385
    _globals['_SCANCONFIG_SCHEDULE']._serialized_start = 1405
    _globals['_SCANCONFIG_SCHEDULE']._serialized_end = 1503
    _globals['_SCANCONFIG_USERAGENT']._serialized_start = 1505
    _globals['_SCANCONFIG_USERAGENT']._serialized_end = 1601
    _globals['_SCANCONFIG_TARGETPLATFORM']._serialized_start = 1603
    _globals['_SCANCONFIG_TARGETPLATFORM']._serialized_end = 1681
    _globals['_SCANCONFIG_RISKLEVEL']._serialized_start = 1683
    _globals['_SCANCONFIG_RISKLEVEL']._serialized_end = 1743
    _globals['_SCANCONFIG_EXPORTTOSECURITYCOMMANDCENTER']._serialized_start = 1745
    _globals['_SCANCONFIG_EXPORTTOSECURITYCOMMANDCENTER']._serialized_end = 1854