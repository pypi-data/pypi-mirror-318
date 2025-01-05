"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/websecurityscanner/v1/scan_run_log.proto')
_sym_db = _symbol_database.Default()
from .....google.cloud.websecurityscanner.v1 import scan_run_pb2 as google_dot_cloud_dot_websecurityscanner_dot_v1_dot_scan__run__pb2
from .....google.cloud.websecurityscanner.v1 import scan_run_error_trace_pb2 as google_dot_cloud_dot_websecurityscanner_dot_v1_dot_scan__run__error__trace__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5google/cloud/websecurityscanner/v1/scan_run_log.proto\x12"google.cloud.websecurityscanner.v1\x1a1google/cloud/websecurityscanner/v1/scan_run.proto\x1a=google/cloud/websecurityscanner/v1/scan_run_error_trace.proto"\xe8\x02\n\nScanRunLog\x12\x0f\n\x07summary\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12S\n\x0fexecution_state\x18\x03 \x01(\x0e2:.google.cloud.websecurityscanner.v1.ScanRun.ExecutionState\x12M\n\x0cresult_state\x18\x04 \x01(\x0e27.google.cloud.websecurityscanner.v1.ScanRun.ResultState\x12\x1a\n\x12urls_crawled_count\x18\x05 \x01(\x03\x12\x19\n\x11urls_tested_count\x18\x06 \x01(\x03\x12\x14\n\x0chas_findings\x18\x07 \x01(\x08\x12J\n\x0berror_trace\x18\x08 \x01(\x0b25.google.cloud.websecurityscanner.v1.ScanRunErrorTraceB\x85\x02\n&com.google.cloud.websecurityscanner.v1B\x0fScanRunLogProtoP\x01ZVcloud.google.com/go/websecurityscanner/apiv1/websecurityscannerpb;websecurityscannerpb\xaa\x02"Google.Cloud.WebSecurityScanner.V1\xca\x02"Google\\Cloud\\WebSecurityScanner\\V1\xea\x02%Google::Cloud::WebSecurityScanner::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.websecurityscanner.v1.scan_run_log_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.cloud.websecurityscanner.v1B\x0fScanRunLogProtoP\x01ZVcloud.google.com/go/websecurityscanner/apiv1/websecurityscannerpb;websecurityscannerpb\xaa\x02"Google.Cloud.WebSecurityScanner.V1\xca\x02"Google\\Cloud\\WebSecurityScanner\\V1\xea\x02%Google::Cloud::WebSecurityScanner::V1'
    _globals['_SCANRUNLOG']._serialized_start = 208
    _globals['_SCANRUNLOG']._serialized_end = 568