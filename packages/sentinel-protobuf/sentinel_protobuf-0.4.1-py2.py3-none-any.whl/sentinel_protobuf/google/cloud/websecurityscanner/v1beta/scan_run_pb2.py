"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/cloud/websecurityscanner/v1beta/scan_run.proto')
_sym_db = _symbol_database.Default()
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.websecurityscanner.v1beta import scan_run_error_trace_pb2 as google_dot_cloud_dot_websecurityscanner_dot_v1beta_dot_scan__run__error__trace__pb2
from .....google.cloud.websecurityscanner.v1beta import scan_run_warning_trace_pb2 as google_dot_cloud_dot_websecurityscanner_dot_v1beta_dot_scan__run__warning__trace__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5google/cloud/websecurityscanner/v1beta/scan_run.proto\x12&google.cloud.websecurityscanner.v1beta\x1a\x19google/api/resource.proto\x1aAgoogle/cloud/websecurityscanner/v1beta/scan_run_error_trace.proto\x1aCgoogle/cloud/websecurityscanner/v1beta/scan_run_warning_trace.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xd2\x06\n\x07ScanRun\x12\x0c\n\x04name\x18\x01 \x01(\t\x12W\n\x0fexecution_state\x18\x02 \x01(\x0e2>.google.cloud.websecurityscanner.v1beta.ScanRun.ExecutionState\x12Q\n\x0cresult_state\x18\x03 \x01(\x0e2;.google.cloud.websecurityscanner.v1beta.ScanRun.ResultState\x12.\n\nstart_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12,\n\x08end_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x1a\n\x12urls_crawled_count\x18\x06 \x01(\x03\x12\x19\n\x11urls_tested_count\x18\x07 \x01(\x03\x12\x1b\n\x13has_vulnerabilities\x18\x08 \x01(\x08\x12\x18\n\x10progress_percent\x18\t \x01(\x05\x12N\n\x0berror_trace\x18\n \x01(\x0b29.google.cloud.websecurityscanner.v1beta.ScanRunErrorTrace\x12S\n\x0ewarning_traces\x18\x0b \x03(\x0b2;.google.cloud.websecurityscanner.v1beta.ScanRunWarningTrace"Y\n\x0eExecutionState\x12\x1f\n\x1bEXECUTION_STATE_UNSPECIFIED\x10\x00\x12\n\n\x06QUEUED\x10\x01\x12\x0c\n\x08SCANNING\x10\x02\x12\x0c\n\x08FINISHED\x10\x03"O\n\x0bResultState\x12\x1c\n\x18RESULT_STATE_UNSPECIFIED\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\t\n\x05ERROR\x10\x02\x12\n\n\x06KILLED\x10\x03:p\xeaAm\n)websecurityscanner.googleapis.com/ScanRun\x12@projects/{project}/scanConfigs/{scan_config}/scanRuns/{scan_run}B\x96\x02\n*com.google.cloud.websecurityscanner.v1betaB\x0cScanRunProtoP\x01ZZcloud.google.com/go/websecurityscanner/apiv1beta/websecurityscannerpb;websecurityscannerpb\xaa\x02&Google.Cloud.WebSecurityScanner.V1Beta\xca\x02&Google\\Cloud\\WebSecurityScanner\\V1beta\xea\x02)Google::Cloud::WebSecurityScanner::V1betab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.websecurityscanner.v1beta.scan_run_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n*com.google.cloud.websecurityscanner.v1betaB\x0cScanRunProtoP\x01ZZcloud.google.com/go/websecurityscanner/apiv1beta/websecurityscannerpb;websecurityscannerpb\xaa\x02&Google.Cloud.WebSecurityScanner.V1Beta\xca\x02&Google\\Cloud\\WebSecurityScanner\\V1beta\xea\x02)Google::Cloud::WebSecurityScanner::V1beta'
    _globals['_SCANRUN']._loaded_options = None
    _globals['_SCANRUN']._serialized_options = b'\xeaAm\n)websecurityscanner.googleapis.com/ScanRun\x12@projects/{project}/scanConfigs/{scan_config}/scanRuns/{scan_run}'
    _globals['_SCANRUN']._serialized_start = 294
    _globals['_SCANRUN']._serialized_end = 1144
    _globals['_SCANRUN_EXECUTIONSTATE']._serialized_start = 860
    _globals['_SCANRUN_EXECUTIONSTATE']._serialized_end = 949
    _globals['_SCANRUN_RESULTSTATE']._serialized_start = 951
    _globals['_SCANRUN_RESULTSTATE']._serialized_end = 1030