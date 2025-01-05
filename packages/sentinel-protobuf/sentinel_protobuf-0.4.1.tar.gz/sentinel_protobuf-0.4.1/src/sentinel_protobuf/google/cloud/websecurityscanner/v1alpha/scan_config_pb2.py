"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/websecurityscanner/v1alpha/scan_config.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.websecurityscanner.v1alpha import scan_run_pb2 as google_dot_cloud_dot_websecurityscanner_dot_v1alpha_dot_scan__run__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n9google/cloud/websecurityscanner/v1alpha/scan_config.proto\x12\'google.cloud.websecurityscanner.v1alpha\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a6google/cloud/websecurityscanner/v1alpha/scan_run.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xb1\n\n\nScanConfig\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x0f\n\x07max_qps\x18\x03 \x01(\x05\x12\x1a\n\rstarting_urls\x18\x04 \x03(\tB\x03\xe0A\x02\x12Z\n\x0eauthentication\x18\x05 \x01(\x0b2B.google.cloud.websecurityscanner.v1alpha.ScanConfig.Authentication\x12Q\n\nuser_agent\x18\x06 \x01(\x0e2=.google.cloud.websecurityscanner.v1alpha.ScanConfig.UserAgent\x12\x1a\n\x12blacklist_patterns\x18\x07 \x03(\t\x12N\n\x08schedule\x18\x08 \x01(\x0b2<.google.cloud.websecurityscanner.v1alpha.ScanConfig.Schedule\x12\\\n\x10target_platforms\x18\t \x03(\x0e2B.google.cloud.websecurityscanner.v1alpha.ScanConfig.TargetPlatform\x12D\n\nlatest_run\x18\x0b \x01(\x0b20.google.cloud.websecurityscanner.v1alpha.ScanRun\x1a\x96\x03\n\x0eAuthentication\x12j\n\x0egoogle_account\x18\x01 \x01(\x0b2P.google.cloud.websecurityscanner.v1alpha.ScanConfig.Authentication.GoogleAccountH\x00\x12j\n\x0ecustom_account\x18\x02 \x01(\x0b2P.google.cloud.websecurityscanner.v1alpha.ScanConfig.Authentication.CustomAccountH\x00\x1a@\n\rGoogleAccount\x12\x15\n\x08username\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x18\n\x08password\x18\x02 \x01(\tB\x06\xe0A\x02\xe0A\x04\x1aX\n\rCustomAccount\x12\x15\n\x08username\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x18\n\x08password\x18\x02 \x01(\tB\x06\xe0A\x02\xe0A\x04\x12\x16\n\tlogin_url\x18\x03 \x01(\tB\x03\xe0A\x02B\x10\n\x0eauthentication\x1ab\n\x08Schedule\x121\n\rschedule_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12#\n\x16interval_duration_days\x18\x02 \x01(\x05B\x03\xe0A\x02"`\n\tUserAgent\x12\x1a\n\x16USER_AGENT_UNSPECIFIED\x10\x00\x12\x10\n\x0cCHROME_LINUX\x10\x01\x12\x12\n\x0eCHROME_ANDROID\x10\x02\x12\x11\n\rSAFARI_IPHONE\x10\x03"N\n\x0eTargetPlatform\x12\x1f\n\x1bTARGET_PLATFORM_UNSPECIFIED\x10\x00\x12\x0e\n\nAPP_ENGINE\x10\x01\x12\x0b\n\x07COMPUTE\x10\x02:_\xeaA\\\n,websecurityscanner.googleapis.com/ScanConfig\x12,projects/{project}/scanConfigs/{scan_config}B\x9d\x01\n+com.google.cloud.websecurityscanner.v1alphaB\x0fScanConfigProtoP\x01Z[cloud.google.com/go/websecurityscanner/apiv1alpha/websecurityscannerpb;websecurityscannerpbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.websecurityscanner.v1alpha.scan_config_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n+com.google.cloud.websecurityscanner.v1alphaB\x0fScanConfigProtoP\x01Z[cloud.google.com/go/websecurityscanner/apiv1alpha/websecurityscannerpb;websecurityscannerpb'
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
    _globals['_SCANCONFIG']._serialized_start = 252
    _globals['_SCANCONFIG']._serialized_end = 1581
    _globals['_SCANCONFIG_AUTHENTICATION']._serialized_start = 800
    _globals['_SCANCONFIG_AUTHENTICATION']._serialized_end = 1206
    _globals['_SCANCONFIG_AUTHENTICATION_GOOGLEACCOUNT']._serialized_start = 1034
    _globals['_SCANCONFIG_AUTHENTICATION_GOOGLEACCOUNT']._serialized_end = 1098
    _globals['_SCANCONFIG_AUTHENTICATION_CUSTOMACCOUNT']._serialized_start = 1100
    _globals['_SCANCONFIG_AUTHENTICATION_CUSTOMACCOUNT']._serialized_end = 1188
    _globals['_SCANCONFIG_SCHEDULE']._serialized_start = 1208
    _globals['_SCANCONFIG_SCHEDULE']._serialized_end = 1306
    _globals['_SCANCONFIG_USERAGENT']._serialized_start = 1308
    _globals['_SCANCONFIG_USERAGENT']._serialized_end = 1404
    _globals['_SCANCONFIG_TARGETPLATFORM']._serialized_start = 1406
    _globals['_SCANCONFIG_TARGETPLATFORM']._serialized_end = 1484