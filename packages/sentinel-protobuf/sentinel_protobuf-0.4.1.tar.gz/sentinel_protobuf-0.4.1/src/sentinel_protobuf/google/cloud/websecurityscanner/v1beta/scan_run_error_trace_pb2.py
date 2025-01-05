"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/websecurityscanner/v1beta/scan_run_error_trace.proto')
_sym_db = _symbol_database.Default()
from .....google.cloud.websecurityscanner.v1beta import scan_config_error_pb2 as google_dot_cloud_dot_websecurityscanner_dot_v1beta_dot_scan__config__error__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nAgoogle/cloud/websecurityscanner/v1beta/scan_run_error_trace.proto\x12&google.cloud.websecurityscanner.v1beta\x1a>google/cloud/websecurityscanner/v1beta/scan_config_error.proto"\x95\x03\n\x11ScanRunErrorTrace\x12L\n\x04code\x18\x01 \x01(\x0e2>.google.cloud.websecurityscanner.v1beta.ScanRunErrorTrace.Code\x12R\n\x11scan_config_error\x18\x02 \x01(\x0b27.google.cloud.websecurityscanner.v1beta.ScanConfigError\x12#\n\x1bmost_common_http_error_code\x18\x03 \x01(\x05"\xb8\x01\n\x04Code\x12\x14\n\x10CODE_UNSPECIFIED\x10\x00\x12\x12\n\x0eINTERNAL_ERROR\x10\x01\x12\x15\n\x11SCAN_CONFIG_ISSUE\x10\x02\x12\x1f\n\x1bAUTHENTICATION_CONFIG_ISSUE\x10\x03\x12\x1c\n\x18TIMED_OUT_WHILE_SCANNING\x10\x04\x12\x16\n\x12TOO_MANY_REDIRECTS\x10\x05\x12\x18\n\x14TOO_MANY_HTTP_ERRORS\x10\x06B\xa0\x02\n*com.google.cloud.websecurityscanner.v1betaB\x16ScanRunErrorTraceProtoP\x01ZZcloud.google.com/go/websecurityscanner/apiv1beta/websecurityscannerpb;websecurityscannerpb\xaa\x02&Google.Cloud.WebSecurityScanner.V1Beta\xca\x02&Google\\Cloud\\WebSecurityScanner\\V1beta\xea\x02)Google::Cloud::WebSecurityScanner::V1betab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.websecurityscanner.v1beta.scan_run_error_trace_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n*com.google.cloud.websecurityscanner.v1betaB\x16ScanRunErrorTraceProtoP\x01ZZcloud.google.com/go/websecurityscanner/apiv1beta/websecurityscannerpb;websecurityscannerpb\xaa\x02&Google.Cloud.WebSecurityScanner.V1Beta\xca\x02&Google\\Cloud\\WebSecurityScanner\\V1beta\xea\x02)Google::Cloud::WebSecurityScanner::V1beta'
    _globals['_SCANRUNERRORTRACE']._serialized_start = 174
    _globals['_SCANRUNERRORTRACE']._serialized_end = 579
    _globals['_SCANRUNERRORTRACE_CODE']._serialized_start = 395
    _globals['_SCANRUNERRORTRACE_CODE']._serialized_end = 579