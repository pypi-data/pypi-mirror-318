"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/devtools/resultstore/v2/action.proto')
_sym_db = _symbol_database.Default()
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.devtools.resultstore.v2 import common_pb2 as google_dot_devtools_dot_resultstore_dot_v2_dot_common__pb2
from .....google.devtools.resultstore.v2 import coverage_pb2 as google_dot_devtools_dot_resultstore_dot_v2_dot_coverage__pb2
from .....google.devtools.resultstore.v2 import file_pb2 as google_dot_devtools_dot_resultstore_dot_v2_dot_file__pb2
from .....google.devtools.resultstore.v2 import file_processing_error_pb2 as google_dot_devtools_dot_resultstore_dot_v2_dot_file__processing__error__pb2
from .....google.devtools.resultstore.v2 import test_suite_pb2 as google_dot_devtools_dot_resultstore_dot_v2_dot_test__suite__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+google/devtools/resultstore/v2/action.proto\x12\x1egoogle.devtools.resultstore.v2\x1a\x19google/api/resource.proto\x1a+google/devtools/resultstore/v2/common.proto\x1a-google/devtools/resultstore/v2/coverage.proto\x1a)google/devtools/resultstore/v2/file.proto\x1a:google/devtools/resultstore/v2/file_processing_error.proto\x1a/google/devtools/resultstore/v2/test_suite.proto\x1a\x1egoogle/protobuf/duration.proto"\x86\x08\n\x06Action\x12\x0c\n\x04name\x18\x01 \x01(\t\x125\n\x02id\x18\x02 \x01(\x0b2).google.devtools.resultstore.v2.Action.Id\x12K\n\x11status_attributes\x18\x03 \x01(\x0b20.google.devtools.resultstore.v2.StatusAttributes\x126\n\x06timing\x18\x04 \x01(\x0b2&.google.devtools.resultstore.v2.Timing\x12C\n\x0cbuild_action\x18\t \x01(\x0b2+.google.devtools.resultstore.v2.BuildActionH\x00\x12A\n\x0btest_action\x18\n \x01(\x0b2*.google.devtools.resultstore.v2.TestActionH\x00\x12K\n\x11action_attributes\x18\x05 \x01(\x0b20.google.devtools.resultstore.v2.ActionAttributes\x12G\n\x13action_dependencies\x18\x0e \x03(\x0b2*.google.devtools.resultstore.v2.Dependency\x12<\n\nproperties\x18\x07 \x03(\x0b2(.google.devtools.resultstore.v2.Property\x123\n\x05files\x18\x08 \x03(\x0b2$.google.devtools.resultstore.v2.File\x12\x11\n\tfile_sets\x18\x0f \x03(\t\x12@\n\x08coverage\x18\x0b \x01(\x0b2..google.devtools.resultstore.v2.ActionCoverage\x12T\n\x16file_processing_errors\x18\r \x03(\x0b24.google.devtools.resultstore.v2.FileProcessingErrors\x1a[\n\x02Id\x12\x15\n\rinvocation_id\x18\x01 \x01(\t\x12\x11\n\ttarget_id\x18\x02 \x01(\t\x12\x18\n\x10configuration_id\x18\x03 \x01(\t\x12\x11\n\taction_id\x18\x04 \x01(\t:\x89\x01\xeaA\x85\x01\n!resultstore.googleapis.com/Action\x12`invocations/{invocation}/targets/{target}/configuredTargets/{configured_target}/actions/{action}B\r\n\x0baction_type"T\n\x0bBuildAction\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x1a\n\x12primary_input_path\x18\x02 \x01(\t\x12\x1b\n\x13primary_output_path\x18\x03 \x01(\t"\xad\x02\n\nTestAction\x12?\n\x0btest_timing\x18\x01 \x01(\x0b2*.google.devtools.resultstore.v2.TestTiming\x12\x14\n\x0cshard_number\x18\x02 \x01(\x05\x12\x12\n\nrun_number\x18\x03 \x01(\x05\x12\x16\n\x0eattempt_number\x18\x04 \x01(\x05\x12=\n\ntest_suite\x18\x05 \x01(\x0b2).google.devtools.resultstore.v2.TestSuite\x12=\n\x08warnings\x18\x08 \x03(\x0b2+.google.devtools.resultstore.v2.TestWarning\x12\x1e\n\x16estimated_memory_bytes\x18\n \x01(\x03"\xce\x01\n\x10ActionAttributes\x12M\n\x12execution_strategy\x18\x01 \x01(\x0e21.google.devtools.resultstore.v2.ExecutionStrategy\x12\x11\n\texit_code\x18\x02 \x01(\x05\x12\x10\n\x08hostname\x18\x03 \x01(\t\x12F\n\x0finput_file_info\x18\x04 \x01(\x0b2-.google.devtools.resultstore.v2.InputFileInfo"\x80\x01\n\rInputFileInfo\x12\r\n\x05count\x18\x01 \x01(\x03\x12\x16\n\x0edistinct_count\x18\x02 \x01(\x03\x12\x13\n\x0bcount_limit\x18\x03 \x01(\x03\x12\x16\n\x0edistinct_bytes\x18\x04 \x01(\x03\x12\x1b\n\x13distinct_byte_limit\x18\x05 \x01(\x03"K\n\x0fLocalTestTiming\x128\n\x15test_process_duration\x18\x01 \x01(\x0b2\x19.google.protobuf.Duration"\xab\x02\n\x17RemoteTestAttemptTiming\x121\n\x0equeue_duration\x18\x01 \x01(\x0b2\x19.google.protobuf.Duration\x122\n\x0fupload_duration\x18\x02 \x01(\x0b2\x19.google.protobuf.Duration\x129\n\x16machine_setup_duration\x18\x03 \x01(\x0b2\x19.google.protobuf.Duration\x128\n\x15test_process_duration\x18\x04 \x01(\x0b2\x19.google.protobuf.Duration\x124\n\x11download_duration\x18\x05 \x01(\x0b2\x19.google.protobuf.Duration"\x99\x01\n\x10RemoteTestTiming\x12:\n\x17local_analysis_duration\x18\x01 \x01(\x0b2\x19.google.protobuf.Duration\x12I\n\x08attempts\x18\x02 \x03(\x0b27.google.devtools.resultstore.v2.RemoteTestAttemptTiming"\xd1\x02\n\nTestTiming\x12@\n\x05local\x18\x01 \x01(\x0b2/.google.devtools.resultstore.v2.LocalTestTimingH\x00\x12B\n\x06remote\x18\x02 \x01(\x0b20.google.devtools.resultstore.v2.RemoteTestTimingH\x00\x127\n\x14system_time_duration\x18\x03 \x01(\x0b2\x19.google.protobuf.Duration\x125\n\x12user_time_duration\x18\x04 \x01(\x0b2\x19.google.protobuf.Duration\x12A\n\x0ctest_caching\x18\x05 \x01(\x0e2+.google.devtools.resultstore.v2.TestCachingB\n\n\x08location"&\n\x0bTestWarning\x12\x17\n\x0fwarning_message\x18\x01 \x01(\t*\x8c\x01\n\x11ExecutionStrategy\x12"\n\x1eEXECUTION_STRATEGY_UNSPECIFIED\x10\x00\x12\x15\n\x11OTHER_ENVIRONMENT\x10\x01\x12\x12\n\x0eREMOTE_SERVICE\x10\x02\x12\x12\n\x0eLOCAL_PARALLEL\x10\x03\x12\x14\n\x10LOCAL_SEQUENTIAL\x10\x04*f\n\x0bTestCaching\x12\x1c\n\x18TEST_CACHING_UNSPECIFIED\x10\x00\x12\x13\n\x0fLOCAL_CACHE_HIT\x10\x01\x12\x14\n\x10REMOTE_CACHE_HIT\x10\x02\x12\x0e\n\nCACHE_MISS\x10\x03B~\n"com.google.devtools.resultstore.v2B\x0bActionProtoP\x01ZIgoogle.golang.org/genproto/googleapis/devtools/resultstore/v2;resultstoreb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.devtools.resultstore.v2.action_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.devtools.resultstore.v2B\x0bActionProtoP\x01ZIgoogle.golang.org/genproto/googleapis/devtools/resultstore/v2;resultstore'
    _globals['_ACTION']._loaded_options = None
    _globals['_ACTION']._serialized_options = b'\xeaA\x85\x01\n!resultstore.googleapis.com/Action\x12`invocations/{invocation}/targets/{target}/configuredTargets/{configured_target}/actions/{action}'
    _globals['_EXECUTIONSTRATEGY']._serialized_start = 3061
    _globals['_EXECUTIONSTRATEGY']._serialized_end = 3201
    _globals['_TESTCACHING']._serialized_start = 3203
    _globals['_TESTCACHING']._serialized_end = 3305
    _globals['_ACTION']._serialized_start = 383
    _globals['_ACTION']._serialized_end = 1413
    _globals['_ACTION_ID']._serialized_start = 1167
    _globals['_ACTION_ID']._serialized_end = 1258
    _globals['_BUILDACTION']._serialized_start = 1415
    _globals['_BUILDACTION']._serialized_end = 1499
    _globals['_TESTACTION']._serialized_start = 1502
    _globals['_TESTACTION']._serialized_end = 1803
    _globals['_ACTIONATTRIBUTES']._serialized_start = 1806
    _globals['_ACTIONATTRIBUTES']._serialized_end = 2012
    _globals['_INPUTFILEINFO']._serialized_start = 2015
    _globals['_INPUTFILEINFO']._serialized_end = 2143
    _globals['_LOCALTESTTIMING']._serialized_start = 2145
    _globals['_LOCALTESTTIMING']._serialized_end = 2220
    _globals['_REMOTETESTATTEMPTTIMING']._serialized_start = 2223
    _globals['_REMOTETESTATTEMPTTIMING']._serialized_end = 2522
    _globals['_REMOTETESTTIMING']._serialized_start = 2525
    _globals['_REMOTETESTTIMING']._serialized_end = 2678
    _globals['_TESTTIMING']._serialized_start = 2681
    _globals['_TESTTIMING']._serialized_end = 3018
    _globals['_TESTWARNING']._serialized_start = 3020
    _globals['_TESTWARNING']._serialized_end = 3058