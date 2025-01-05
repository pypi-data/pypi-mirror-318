"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/devtools/resultstore/v2/coverage.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-google/devtools/resultstore/v2/coverage.proto\x12\x1egoogle.devtools.resultstore.v2"B\n\x0cLineCoverage\x12\x1a\n\x12instrumented_lines\x18\x01 \x01(\x0c\x12\x16\n\x0eexecuted_lines\x18\x02 \x01(\x0c"c\n\x0eBranchCoverage\x12\x16\n\x0ebranch_present\x18\x01 \x01(\x0c\x12\x18\n\x10branches_in_line\x18\x02 \x03(\x05\x12\x10\n\x08executed\x18\x03 \x01(\x0c\x12\r\n\x05taken\x18\x04 \x01(\x0c"\xaa\x01\n\x0cFileCoverage\x12\x0c\n\x04path\x18\x01 \x01(\t\x12C\n\rline_coverage\x18\x02 \x01(\x0b2,.google.devtools.resultstore.v2.LineCoverage\x12G\n\x0fbranch_coverage\x18\x03 \x01(\x0b2..google.devtools.resultstore.v2.BranchCoverage"V\n\x0eActionCoverage\x12D\n\x0efile_coverages\x18\x02 \x03(\x0b2,.google.devtools.resultstore.v2.FileCoverage"Y\n\x11AggregateCoverage\x12D\n\x0efile_coverages\x18\x01 \x03(\x0b2,.google.devtools.resultstore.v2.FileCoverageB\x80\x01\n"com.google.devtools.resultstore.v2B\rCoverageProtoP\x01ZIgoogle.golang.org/genproto/googleapis/devtools/resultstore/v2;resultstoreb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.devtools.resultstore.v2.coverage_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.devtools.resultstore.v2B\rCoverageProtoP\x01ZIgoogle.golang.org/genproto/googleapis/devtools/resultstore/v2;resultstore'
    _globals['_LINECOVERAGE']._serialized_start = 81
    _globals['_LINECOVERAGE']._serialized_end = 147
    _globals['_BRANCHCOVERAGE']._serialized_start = 149
    _globals['_BRANCHCOVERAGE']._serialized_end = 248
    _globals['_FILECOVERAGE']._serialized_start = 251
    _globals['_FILECOVERAGE']._serialized_end = 421
    _globals['_ACTIONCOVERAGE']._serialized_start = 423
    _globals['_ACTIONCOVERAGE']._serialized_end = 509
    _globals['_AGGREGATECOVERAGE']._serialized_start = 511
    _globals['_AGGREGATECOVERAGE']._serialized_end = 600