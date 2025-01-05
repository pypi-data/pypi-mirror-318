"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/websecurityscanner/v1beta/scan_run_warning_trace.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nCgoogle/cloud/websecurityscanner/v1beta/scan_run_warning_trace.proto\x12&google.cloud.websecurityscanner.v1beta"\xed\x01\n\x13ScanRunWarningTrace\x12N\n\x04code\x18\x01 \x01(\x0e2@.google.cloud.websecurityscanner.v1beta.ScanRunWarningTrace.Code"\x85\x01\n\x04Code\x12\x14\n\x10CODE_UNSPECIFIED\x10\x00\x12\x1e\n\x1aINSUFFICIENT_CRAWL_RESULTS\x10\x01\x12\x1a\n\x16TOO_MANY_CRAWL_RESULTS\x10\x02\x12\x17\n\x13TOO_MANY_FUZZ_TASKS\x10\x03\x12\x12\n\x0eBLOCKED_BY_IAP\x10\x04B\xa2\x02\n*com.google.cloud.websecurityscanner.v1betaB\x18ScanRunWarningTraceProtoP\x01ZZcloud.google.com/go/websecurityscanner/apiv1beta/websecurityscannerpb;websecurityscannerpb\xaa\x02&Google.Cloud.WebSecurityScanner.V1Beta\xca\x02&Google\\Cloud\\WebSecurityScanner\\V1beta\xea\x02)Google::Cloud::WebSecurityScanner::V1betab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.websecurityscanner.v1beta.scan_run_warning_trace_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n*com.google.cloud.websecurityscanner.v1betaB\x18ScanRunWarningTraceProtoP\x01ZZcloud.google.com/go/websecurityscanner/apiv1beta/websecurityscannerpb;websecurityscannerpb\xaa\x02&Google.Cloud.WebSecurityScanner.V1Beta\xca\x02&Google\\Cloud\\WebSecurityScanner\\V1beta\xea\x02)Google::Cloud::WebSecurityScanner::V1beta'
    _globals['_SCANRUNWARNINGTRACE']._serialized_start = 112
    _globals['_SCANRUNWARNINGTRACE']._serialized_end = 349
    _globals['_SCANRUNWARNINGTRACE_CODE']._serialized_start = 216
    _globals['_SCANRUNWARNINGTRACE_CODE']._serialized_end = 349