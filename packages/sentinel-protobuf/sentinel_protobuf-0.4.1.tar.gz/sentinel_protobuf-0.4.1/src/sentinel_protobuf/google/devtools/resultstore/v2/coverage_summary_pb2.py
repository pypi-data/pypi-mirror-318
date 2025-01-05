"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/devtools/resultstore/v2/coverage_summary.proto')
_sym_db = _symbol_database.Default()
from .....google.devtools.resultstore.v2 import common_pb2 as google_dot_devtools_dot_resultstore_dot_v2_dot_common__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5google/devtools/resultstore/v2/coverage_summary.proto\x12\x1egoogle.devtools.resultstore.v2\x1a+google/devtools/resultstore/v2/common.proto"S\n\x13LineCoverageSummary\x12\x1f\n\x17instrumented_line_count\x18\x01 \x01(\x05\x12\x1b\n\x13executed_line_count\x18\x02 \x01(\x05"n\n\x15BranchCoverageSummary\x12\x1a\n\x12total_branch_count\x18\x01 \x01(\x05\x12\x1d\n\x15executed_branch_count\x18\x02 \x01(\x05\x12\x1a\n\x12taken_branch_count\x18\x03 \x01(\x05"\xef\x01\n\x17LanguageCoverageSummary\x12:\n\x08language\x18\x01 \x01(\x0e2(.google.devtools.resultstore.v2.Language\x12I\n\x0cline_summary\x18\x02 \x01(\x0b23.google.devtools.resultstore.v2.LineCoverageSummary\x12M\n\x0ebranch_summary\x18\x03 \x01(\x0b25.google.devtools.resultstore.v2.BranchCoverageSummaryB\x87\x01\n"com.google.devtools.resultstore.v2B\x14CoverageSummaryProtoP\x01ZIgoogle.golang.org/genproto/googleapis/devtools/resultstore/v2;resultstoreb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.devtools.resultstore.v2.coverage_summary_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.devtools.resultstore.v2B\x14CoverageSummaryProtoP\x01ZIgoogle.golang.org/genproto/googleapis/devtools/resultstore/v2;resultstore'
    _globals['_LINECOVERAGESUMMARY']._serialized_start = 134
    _globals['_LINECOVERAGESUMMARY']._serialized_end = 217
    _globals['_BRANCHCOVERAGESUMMARY']._serialized_start = 219
    _globals['_BRANCHCOVERAGESUMMARY']._serialized_end = 329
    _globals['_LANGUAGECOVERAGESUMMARY']._serialized_start = 332
    _globals['_LANGUAGECOVERAGESUMMARY']._serialized_end = 571