from google.devtools.resultstore.v2 import common_pb2 as _common_pb2
from google.devtools.resultstore.v2 import file_pb2 as _file_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class TestSuite(_message.Message):
    __slots__ = ('suite_name', 'tests', 'failures', 'errors', 'timing', 'properties', 'files')
    SUITE_NAME_FIELD_NUMBER: _ClassVar[int]
    TESTS_FIELD_NUMBER: _ClassVar[int]
    FAILURES_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    TIMING_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    FILES_FIELD_NUMBER: _ClassVar[int]
    suite_name: str
    tests: _containers.RepeatedCompositeFieldContainer[Test]
    failures: _containers.RepeatedCompositeFieldContainer[TestFailure]
    errors: _containers.RepeatedCompositeFieldContainer[TestError]
    timing: _common_pb2.Timing
    properties: _containers.RepeatedCompositeFieldContainer[_common_pb2.Property]
    files: _containers.RepeatedCompositeFieldContainer[_file_pb2.File]

    def __init__(self, suite_name: _Optional[str]=..., tests: _Optional[_Iterable[_Union[Test, _Mapping]]]=..., failures: _Optional[_Iterable[_Union[TestFailure, _Mapping]]]=..., errors: _Optional[_Iterable[_Union[TestError, _Mapping]]]=..., timing: _Optional[_Union[_common_pb2.Timing, _Mapping]]=..., properties: _Optional[_Iterable[_Union[_common_pb2.Property, _Mapping]]]=..., files: _Optional[_Iterable[_Union[_file_pb2.File, _Mapping]]]=...) -> None:
        ...

class Test(_message.Message):
    __slots__ = ('test_case', 'test_suite')
    TEST_CASE_FIELD_NUMBER: _ClassVar[int]
    TEST_SUITE_FIELD_NUMBER: _ClassVar[int]
    test_case: TestCase
    test_suite: TestSuite

    def __init__(self, test_case: _Optional[_Union[TestCase, _Mapping]]=..., test_suite: _Optional[_Union[TestSuite, _Mapping]]=...) -> None:
        ...

class TestCase(_message.Message):
    __slots__ = ('case_name', 'class_name', 'result', 'failures', 'errors', 'timing', 'properties', 'files', 'retry_number', 'repeat_number')

    class Result(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RESULT_UNSPECIFIED: _ClassVar[TestCase.Result]
        COMPLETED: _ClassVar[TestCase.Result]
        INTERRUPTED: _ClassVar[TestCase.Result]
        CANCELLED: _ClassVar[TestCase.Result]
        FILTERED: _ClassVar[TestCase.Result]
        SKIPPED: _ClassVar[TestCase.Result]
        SUPPRESSED: _ClassVar[TestCase.Result]
    RESULT_UNSPECIFIED: TestCase.Result
    COMPLETED: TestCase.Result
    INTERRUPTED: TestCase.Result
    CANCELLED: TestCase.Result
    FILTERED: TestCase.Result
    SKIPPED: TestCase.Result
    SUPPRESSED: TestCase.Result
    CASE_NAME_FIELD_NUMBER: _ClassVar[int]
    CLASS_NAME_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    FAILURES_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    TIMING_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    FILES_FIELD_NUMBER: _ClassVar[int]
    RETRY_NUMBER_FIELD_NUMBER: _ClassVar[int]
    REPEAT_NUMBER_FIELD_NUMBER: _ClassVar[int]
    case_name: str
    class_name: str
    result: TestCase.Result
    failures: _containers.RepeatedCompositeFieldContainer[TestFailure]
    errors: _containers.RepeatedCompositeFieldContainer[TestError]
    timing: _common_pb2.Timing
    properties: _containers.RepeatedCompositeFieldContainer[_common_pb2.Property]
    files: _containers.RepeatedCompositeFieldContainer[_file_pb2.File]
    retry_number: int
    repeat_number: int

    def __init__(self, case_name: _Optional[str]=..., class_name: _Optional[str]=..., result: _Optional[_Union[TestCase.Result, str]]=..., failures: _Optional[_Iterable[_Union[TestFailure, _Mapping]]]=..., errors: _Optional[_Iterable[_Union[TestError, _Mapping]]]=..., timing: _Optional[_Union[_common_pb2.Timing, _Mapping]]=..., properties: _Optional[_Iterable[_Union[_common_pb2.Property, _Mapping]]]=..., files: _Optional[_Iterable[_Union[_file_pb2.File, _Mapping]]]=..., retry_number: _Optional[int]=..., repeat_number: _Optional[int]=...) -> None:
        ...

class TestFailure(_message.Message):
    __slots__ = ('failure_message', 'exception_type', 'stack_trace', 'expected', 'actual')
    FAILURE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    EXCEPTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    STACK_TRACE_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_FIELD_NUMBER: _ClassVar[int]
    ACTUAL_FIELD_NUMBER: _ClassVar[int]
    failure_message: str
    exception_type: str
    stack_trace: str
    expected: _containers.RepeatedScalarFieldContainer[str]
    actual: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, failure_message: _Optional[str]=..., exception_type: _Optional[str]=..., stack_trace: _Optional[str]=..., expected: _Optional[_Iterable[str]]=..., actual: _Optional[_Iterable[str]]=...) -> None:
        ...

class TestError(_message.Message):
    __slots__ = ('error_message', 'exception_type', 'stack_trace')
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    EXCEPTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    STACK_TRACE_FIELD_NUMBER: _ClassVar[int]
    error_message: str
    exception_type: str
    stack_trace: str

    def __init__(self, error_message: _Optional[str]=..., exception_type: _Optional[str]=..., stack_trace: _Optional[str]=...) -> None:
        ...