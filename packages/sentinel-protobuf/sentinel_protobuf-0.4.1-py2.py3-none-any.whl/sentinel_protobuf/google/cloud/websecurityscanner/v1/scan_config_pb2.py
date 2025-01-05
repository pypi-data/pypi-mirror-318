"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/websecurityscanner/v1/scan_config.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4google/cloud/websecurityscanner/v1/scan_config.proto\x12"google.cloud.websecurityscanner.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xc4\r\n\nScanConfig\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0cdisplay_name\x18\x02 \x01(\t\x12\x0f\n\x07max_qps\x18\x03 \x01(\x05\x12\x15\n\rstarting_urls\x18\x04 \x03(\t\x12U\n\x0eauthentication\x18\x05 \x01(\x0b2=.google.cloud.websecurityscanner.v1.ScanConfig.Authentication\x12L\n\nuser_agent\x18\x06 \x01(\x0e28.google.cloud.websecurityscanner.v1.ScanConfig.UserAgent\x12\x1a\n\x12blacklist_patterns\x18\x07 \x03(\t\x12I\n\x08schedule\x18\x08 \x01(\x0b27.google.cloud.websecurityscanner.v1.ScanConfig.Schedule\x12w\n!export_to_security_command_center\x18\n \x01(\x0e2L.google.cloud.websecurityscanner.v1.ScanConfig.ExportToSecurityCommandCenter\x12L\n\nrisk_level\x18\x0c \x01(\x0e28.google.cloud.websecurityscanner.v1.ScanConfig.RiskLevel\x12\x14\n\x0cmanaged_scan\x18\r \x01(\x08\x12\x16\n\x0estatic_ip_scan\x18\x0e \x01(\x08\x12!\n\x19ignore_http_status_errors\x18\x0f \x01(\x08\x1a\xd7\x05\n\x0eAuthentication\x12i\n\x0egoogle_account\x18\x01 \x01(\x0b2K.google.cloud.websecurityscanner.v1.ScanConfig.Authentication.GoogleAccountB\x02\x18\x01H\x00\x12e\n\x0ecustom_account\x18\x02 \x01(\x0b2K.google.cloud.websecurityscanner.v1.ScanConfig.Authentication.CustomAccountH\x00\x12e\n\x0eiap_credential\x18\x04 \x01(\x0b2K.google.cloud.websecurityscanner.v1.ScanConfig.Authentication.IapCredentialH\x00\x1a7\n\rGoogleAccount\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t:\x02\x18\x01\x1aF\n\rCustomAccount\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\x12\x11\n\tlogin_url\x18\x03 \x01(\t\x1a\xf8\x01\n\rIapCredential\x12\x8e\x01\n\x1diap_test_service_account_info\x18\x01 \x01(\x0b2e.google.cloud.websecurityscanner.v1.ScanConfig.Authentication.IapCredential.IapTestServiceAccountInfoH\x00\x1aC\n\x19IapTestServiceAccountInfo\x12&\n\x19target_audience_client_id\x18\x01 \x01(\tB\x03\xe0A\x02B\x11\n\x0fiap_credentialsB\x10\n\x0eauthentication\x1a]\n\x08Schedule\x121\n\rschedule_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x1e\n\x16interval_duration_days\x18\x02 \x01(\x05"`\n\tUserAgent\x12\x1a\n\x16USER_AGENT_UNSPECIFIED\x10\x00\x12\x10\n\x0cCHROME_LINUX\x10\x01\x12\x12\n\x0eCHROME_ANDROID\x10\x02\x12\x11\n\rSAFARI_IPHONE\x10\x03"<\n\tRiskLevel\x12\x1a\n\x16RISK_LEVEL_UNSPECIFIED\x10\x00\x12\n\n\x06NORMAL\x10\x01\x12\x07\n\x03LOW\x10\x02"m\n\x1dExportToSecurityCommandCenter\x121\n-EXPORT_TO_SECURITY_COMMAND_CENTER_UNSPECIFIED\x10\x00\x12\x0b\n\x07ENABLED\x10\x01\x12\x0c\n\x08DISABLED\x10\x02B\x85\x02\n&com.google.cloud.websecurityscanner.v1B\x0fScanConfigProtoP\x01ZVcloud.google.com/go/websecurityscanner/apiv1/websecurityscannerpb;websecurityscannerpb\xaa\x02"Google.Cloud.WebSecurityScanner.V1\xca\x02"Google\\Cloud\\WebSecurityScanner\\V1\xea\x02%Google::Cloud::WebSecurityScanner::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.websecurityscanner.v1.scan_config_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.cloud.websecurityscanner.v1B\x0fScanConfigProtoP\x01ZVcloud.google.com/go/websecurityscanner/apiv1/websecurityscannerpb;websecurityscannerpb\xaa\x02"Google.Cloud.WebSecurityScanner.V1\xca\x02"Google\\Cloud\\WebSecurityScanner\\V1\xea\x02%Google::Cloud::WebSecurityScanner::V1'
    _globals['_SCANCONFIG_AUTHENTICATION_GOOGLEACCOUNT']._loaded_options = None
    _globals['_SCANCONFIG_AUTHENTICATION_GOOGLEACCOUNT']._serialized_options = b'\x18\x01'
    _globals['_SCANCONFIG_AUTHENTICATION_IAPCREDENTIAL_IAPTESTSERVICEACCOUNTINFO'].fields_by_name['target_audience_client_id']._loaded_options = None
    _globals['_SCANCONFIG_AUTHENTICATION_IAPCREDENTIAL_IAPTESTSERVICEACCOUNTINFO'].fields_by_name['target_audience_client_id']._serialized_options = b'\xe0A\x02'
    _globals['_SCANCONFIG_AUTHENTICATION'].fields_by_name['google_account']._loaded_options = None
    _globals['_SCANCONFIG_AUTHENTICATION'].fields_by_name['google_account']._serialized_options = b'\x18\x01'
    _globals['_SCANCONFIG']._serialized_start = 159
    _globals['_SCANCONFIG']._serialized_end = 1891
    _globals['_SCANCONFIG_AUTHENTICATION']._serialized_start = 798
    _globals['_SCANCONFIG_AUTHENTICATION']._serialized_end = 1525
    _globals['_SCANCONFIG_AUTHENTICATION_GOOGLEACCOUNT']._serialized_start = 1129
    _globals['_SCANCONFIG_AUTHENTICATION_GOOGLEACCOUNT']._serialized_end = 1184
    _globals['_SCANCONFIG_AUTHENTICATION_CUSTOMACCOUNT']._serialized_start = 1186
    _globals['_SCANCONFIG_AUTHENTICATION_CUSTOMACCOUNT']._serialized_end = 1256
    _globals['_SCANCONFIG_AUTHENTICATION_IAPCREDENTIAL']._serialized_start = 1259
    _globals['_SCANCONFIG_AUTHENTICATION_IAPCREDENTIAL']._serialized_end = 1507
    _globals['_SCANCONFIG_AUTHENTICATION_IAPCREDENTIAL_IAPTESTSERVICEACCOUNTINFO']._serialized_start = 1421
    _globals['_SCANCONFIG_AUTHENTICATION_IAPCREDENTIAL_IAPTESTSERVICEACCOUNTINFO']._serialized_end = 1488
    _globals['_SCANCONFIG_SCHEDULE']._serialized_start = 1527
    _globals['_SCANCONFIG_SCHEDULE']._serialized_end = 1620
    _globals['_SCANCONFIG_USERAGENT']._serialized_start = 1622
    _globals['_SCANCONFIG_USERAGENT']._serialized_end = 1718
    _globals['_SCANCONFIG_RISKLEVEL']._serialized_start = 1720
    _globals['_SCANCONFIG_RISKLEVEL']._serialized_end = 1780
    _globals['_SCANCONFIG_EXPORTTOSECURITYCOMMANDCENTER']._serialized_start = 1782
    _globals['_SCANCONFIG_EXPORTTOSECURITYCOMMANDCENTER']._serialized_end = 1891