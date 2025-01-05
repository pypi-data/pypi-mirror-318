"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/devtools/resultstore/v2/test_suite.proto')
_sym_db = _symbol_database.Default()
from .....google.devtools.resultstore.v2 import common_pb2 as google_dot_devtools_dot_resultstore_dot_v2_dot_common__pb2
from .....google.devtools.resultstore.v2 import file_pb2 as google_dot_devtools_dot_resultstore_dot_v2_dot_file__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/google/devtools/resultstore/v2/test_suite.proto\x12\x1egoogle.devtools.resultstore.v2\x1a+google/devtools/resultstore/v2/common.proto\x1a)google/devtools/resultstore/v2/file.proto"\xf9\x02\n\tTestSuite\x12\x12\n\nsuite_name\x18\x01 \x01(\t\x123\n\x05tests\x18\x02 \x03(\x0b2$.google.devtools.resultstore.v2.Test\x12=\n\x08failures\x18\x03 \x03(\x0b2+.google.devtools.resultstore.v2.TestFailure\x129\n\x06errors\x18\x04 \x03(\x0b2).google.devtools.resultstore.v2.TestError\x126\n\x06timing\x18\x06 \x01(\x0b2&.google.devtools.resultstore.v2.Timing\x12<\n\nproperties\x18\x07 \x03(\x0b2(.google.devtools.resultstore.v2.Property\x123\n\x05files\x18\x08 \x03(\x0b2$.google.devtools.resultstore.v2.File"\x93\x01\n\x04Test\x12=\n\ttest_case\x18\x01 \x01(\x0b2(.google.devtools.resultstore.v2.TestCaseH\x00\x12?\n\ntest_suite\x18\x02 \x01(\x0b2).google.devtools.resultstore.v2.TestSuiteH\x00B\x0b\n\ttest_type"\xc0\x04\n\x08TestCase\x12\x11\n\tcase_name\x18\x01 \x01(\t\x12\x12\n\nclass_name\x18\x02 \x01(\t\x12?\n\x06result\x18\x03 \x01(\x0e2/.google.devtools.resultstore.v2.TestCase.Result\x12=\n\x08failures\x18\x04 \x03(\x0b2+.google.devtools.resultstore.v2.TestFailure\x129\n\x06errors\x18\x05 \x03(\x0b2).google.devtools.resultstore.v2.TestError\x126\n\x06timing\x18\x07 \x01(\x0b2&.google.devtools.resultstore.v2.Timing\x12<\n\nproperties\x18\x08 \x03(\x0b2(.google.devtools.resultstore.v2.Property\x123\n\x05files\x18\t \x03(\x0b2$.google.devtools.resultstore.v2.File\x12\x14\n\x0cretry_number\x18\n \x01(\x05\x12\x15\n\rrepeat_number\x18\x0b \x01(\x05"z\n\x06Result\x12\x16\n\x12RESULT_UNSPECIFIED\x10\x00\x12\r\n\tCOMPLETED\x10\x01\x12\x0f\n\x0bINTERRUPTED\x10\x02\x12\r\n\tCANCELLED\x10\x03\x12\x0c\n\x08FILTERED\x10\x04\x12\x0b\n\x07SKIPPED\x10\x05\x12\x0e\n\nSUPPRESSED\x10\x06"u\n\x0bTestFailure\x12\x17\n\x0ffailure_message\x18\x01 \x01(\t\x12\x16\n\x0eexception_type\x18\x02 \x01(\t\x12\x13\n\x0bstack_trace\x18\x03 \x01(\t\x12\x10\n\x08expected\x18\x04 \x03(\t\x12\x0e\n\x06actual\x18\x05 \x03(\t"O\n\tTestError\x12\x15\n\rerror_message\x18\x01 \x01(\t\x12\x16\n\x0eexception_type\x18\x02 \x01(\t\x12\x13\n\x0bstack_trace\x18\x03 \x01(\tB\x81\x01\n"com.google.devtools.resultstore.v2B\x0eTestSuiteProtoP\x01ZIgoogle.golang.org/genproto/googleapis/devtools/resultstore/v2;resultstoreb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.devtools.resultstore.v2.test_suite_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.devtools.resultstore.v2B\x0eTestSuiteProtoP\x01ZIgoogle.golang.org/genproto/googleapis/devtools/resultstore/v2;resultstore'
    _globals['_TESTSUITE']._serialized_start = 172
    _globals['_TESTSUITE']._serialized_end = 549
    _globals['_TEST']._serialized_start = 552
    _globals['_TEST']._serialized_end = 699
    _globals['_TESTCASE']._serialized_start = 702
    _globals['_TESTCASE']._serialized_end = 1278
    _globals['_TESTCASE_RESULT']._serialized_start = 1156
    _globals['_TESTCASE_RESULT']._serialized_end = 1278
    _globals['_TESTFAILURE']._serialized_start = 1280
    _globals['_TESTFAILURE']._serialized_end = 1397
    _globals['_TESTERROR']._serialized_start = 1399
    _globals['_TESTERROR']._serialized_end = 1478