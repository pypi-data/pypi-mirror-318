from google.api import resource_pb2 as _resource_pb2
from google.devtools.resultstore.v2 import common_pb2 as _common_pb2
from google.devtools.resultstore.v2 import coverage_pb2 as _coverage_pb2
from google.devtools.resultstore.v2 import file_pb2 as _file_pb2
from google.devtools.resultstore.v2 import file_processing_error_pb2 as _file_processing_error_pb2
from google.devtools.resultstore.v2 import test_suite_pb2 as _test_suite_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ExecutionStrategy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EXECUTION_STRATEGY_UNSPECIFIED: _ClassVar[ExecutionStrategy]
    OTHER_ENVIRONMENT: _ClassVar[ExecutionStrategy]
    REMOTE_SERVICE: _ClassVar[ExecutionStrategy]
    LOCAL_PARALLEL: _ClassVar[ExecutionStrategy]
    LOCAL_SEQUENTIAL: _ClassVar[ExecutionStrategy]

class TestCaching(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TEST_CACHING_UNSPECIFIED: _ClassVar[TestCaching]
    LOCAL_CACHE_HIT: _ClassVar[TestCaching]
    REMOTE_CACHE_HIT: _ClassVar[TestCaching]
    CACHE_MISS: _ClassVar[TestCaching]
EXECUTION_STRATEGY_UNSPECIFIED: ExecutionStrategy
OTHER_ENVIRONMENT: ExecutionStrategy
REMOTE_SERVICE: ExecutionStrategy
LOCAL_PARALLEL: ExecutionStrategy
LOCAL_SEQUENTIAL: ExecutionStrategy
TEST_CACHING_UNSPECIFIED: TestCaching
LOCAL_CACHE_HIT: TestCaching
REMOTE_CACHE_HIT: TestCaching
CACHE_MISS: TestCaching

class Action(_message.Message):
    __slots__ = ('name', 'id', 'status_attributes', 'timing', 'build_action', 'test_action', 'action_attributes', 'action_dependencies', 'properties', 'files', 'file_sets', 'coverage', 'file_processing_errors')

    class Id(_message.Message):
        __slots__ = ('invocation_id', 'target_id', 'configuration_id', 'action_id')
        INVOCATION_ID_FIELD_NUMBER: _ClassVar[int]
        TARGET_ID_FIELD_NUMBER: _ClassVar[int]
        CONFIGURATION_ID_FIELD_NUMBER: _ClassVar[int]
        ACTION_ID_FIELD_NUMBER: _ClassVar[int]
        invocation_id: str
        target_id: str
        configuration_id: str
        action_id: str

        def __init__(self, invocation_id: _Optional[str]=..., target_id: _Optional[str]=..., configuration_id: _Optional[str]=..., action_id: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    TIMING_FIELD_NUMBER: _ClassVar[int]
    BUILD_ACTION_FIELD_NUMBER: _ClassVar[int]
    TEST_ACTION_FIELD_NUMBER: _ClassVar[int]
    ACTION_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    ACTION_DEPENDENCIES_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    FILES_FIELD_NUMBER: _ClassVar[int]
    FILE_SETS_FIELD_NUMBER: _ClassVar[int]
    COVERAGE_FIELD_NUMBER: _ClassVar[int]
    FILE_PROCESSING_ERRORS_FIELD_NUMBER: _ClassVar[int]
    name: str
    id: Action.Id
    status_attributes: _common_pb2.StatusAttributes
    timing: _common_pb2.Timing
    build_action: BuildAction
    test_action: TestAction
    action_attributes: ActionAttributes
    action_dependencies: _containers.RepeatedCompositeFieldContainer[_common_pb2.Dependency]
    properties: _containers.RepeatedCompositeFieldContainer[_common_pb2.Property]
    files: _containers.RepeatedCompositeFieldContainer[_file_pb2.File]
    file_sets: _containers.RepeatedScalarFieldContainer[str]
    coverage: _coverage_pb2.ActionCoverage
    file_processing_errors: _containers.RepeatedCompositeFieldContainer[_file_processing_error_pb2.FileProcessingErrors]

    def __init__(self, name: _Optional[str]=..., id: _Optional[_Union[Action.Id, _Mapping]]=..., status_attributes: _Optional[_Union[_common_pb2.StatusAttributes, _Mapping]]=..., timing: _Optional[_Union[_common_pb2.Timing, _Mapping]]=..., build_action: _Optional[_Union[BuildAction, _Mapping]]=..., test_action: _Optional[_Union[TestAction, _Mapping]]=..., action_attributes: _Optional[_Union[ActionAttributes, _Mapping]]=..., action_dependencies: _Optional[_Iterable[_Union[_common_pb2.Dependency, _Mapping]]]=..., properties: _Optional[_Iterable[_Union[_common_pb2.Property, _Mapping]]]=..., files: _Optional[_Iterable[_Union[_file_pb2.File, _Mapping]]]=..., file_sets: _Optional[_Iterable[str]]=..., coverage: _Optional[_Union[_coverage_pb2.ActionCoverage, _Mapping]]=..., file_processing_errors: _Optional[_Iterable[_Union[_file_processing_error_pb2.FileProcessingErrors, _Mapping]]]=...) -> None:
        ...

class BuildAction(_message.Message):
    __slots__ = ('type', 'primary_input_path', 'primary_output_path')
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_INPUT_PATH_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_OUTPUT_PATH_FIELD_NUMBER: _ClassVar[int]
    type: str
    primary_input_path: str
    primary_output_path: str

    def __init__(self, type: _Optional[str]=..., primary_input_path: _Optional[str]=..., primary_output_path: _Optional[str]=...) -> None:
        ...

class TestAction(_message.Message):
    __slots__ = ('test_timing', 'shard_number', 'run_number', 'attempt_number', 'test_suite', 'warnings', 'estimated_memory_bytes')
    TEST_TIMING_FIELD_NUMBER: _ClassVar[int]
    SHARD_NUMBER_FIELD_NUMBER: _ClassVar[int]
    RUN_NUMBER_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_NUMBER_FIELD_NUMBER: _ClassVar[int]
    TEST_SUITE_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    ESTIMATED_MEMORY_BYTES_FIELD_NUMBER: _ClassVar[int]
    test_timing: TestTiming
    shard_number: int
    run_number: int
    attempt_number: int
    test_suite: _test_suite_pb2.TestSuite
    warnings: _containers.RepeatedCompositeFieldContainer[TestWarning]
    estimated_memory_bytes: int

    def __init__(self, test_timing: _Optional[_Union[TestTiming, _Mapping]]=..., shard_number: _Optional[int]=..., run_number: _Optional[int]=..., attempt_number: _Optional[int]=..., test_suite: _Optional[_Union[_test_suite_pb2.TestSuite, _Mapping]]=..., warnings: _Optional[_Iterable[_Union[TestWarning, _Mapping]]]=..., estimated_memory_bytes: _Optional[int]=...) -> None:
        ...

class ActionAttributes(_message.Message):
    __slots__ = ('execution_strategy', 'exit_code', 'hostname', 'input_file_info')
    EXECUTION_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    EXIT_CODE_FIELD_NUMBER: _ClassVar[int]
    HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    INPUT_FILE_INFO_FIELD_NUMBER: _ClassVar[int]
    execution_strategy: ExecutionStrategy
    exit_code: int
    hostname: str
    input_file_info: InputFileInfo

    def __init__(self, execution_strategy: _Optional[_Union[ExecutionStrategy, str]]=..., exit_code: _Optional[int]=..., hostname: _Optional[str]=..., input_file_info: _Optional[_Union[InputFileInfo, _Mapping]]=...) -> None:
        ...

class InputFileInfo(_message.Message):
    __slots__ = ('count', 'distinct_count', 'count_limit', 'distinct_bytes', 'distinct_byte_limit')
    COUNT_FIELD_NUMBER: _ClassVar[int]
    DISTINCT_COUNT_FIELD_NUMBER: _ClassVar[int]
    COUNT_LIMIT_FIELD_NUMBER: _ClassVar[int]
    DISTINCT_BYTES_FIELD_NUMBER: _ClassVar[int]
    DISTINCT_BYTE_LIMIT_FIELD_NUMBER: _ClassVar[int]
    count: int
    distinct_count: int
    count_limit: int
    distinct_bytes: int
    distinct_byte_limit: int

    def __init__(self, count: _Optional[int]=..., distinct_count: _Optional[int]=..., count_limit: _Optional[int]=..., distinct_bytes: _Optional[int]=..., distinct_byte_limit: _Optional[int]=...) -> None:
        ...

class LocalTestTiming(_message.Message):
    __slots__ = ('test_process_duration',)
    TEST_PROCESS_DURATION_FIELD_NUMBER: _ClassVar[int]
    test_process_duration: _duration_pb2.Duration

    def __init__(self, test_process_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=...) -> None:
        ...

class RemoteTestAttemptTiming(_message.Message):
    __slots__ = ('queue_duration', 'upload_duration', 'machine_setup_duration', 'test_process_duration', 'download_duration')
    QUEUE_DURATION_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_DURATION_FIELD_NUMBER: _ClassVar[int]
    MACHINE_SETUP_DURATION_FIELD_NUMBER: _ClassVar[int]
    TEST_PROCESS_DURATION_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_DURATION_FIELD_NUMBER: _ClassVar[int]
    queue_duration: _duration_pb2.Duration
    upload_duration: _duration_pb2.Duration
    machine_setup_duration: _duration_pb2.Duration
    test_process_duration: _duration_pb2.Duration
    download_duration: _duration_pb2.Duration

    def __init__(self, queue_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., upload_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., machine_setup_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., test_process_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., download_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=...) -> None:
        ...

class RemoteTestTiming(_message.Message):
    __slots__ = ('local_analysis_duration', 'attempts')
    LOCAL_ANALYSIS_DURATION_FIELD_NUMBER: _ClassVar[int]
    ATTEMPTS_FIELD_NUMBER: _ClassVar[int]
    local_analysis_duration: _duration_pb2.Duration
    attempts: _containers.RepeatedCompositeFieldContainer[RemoteTestAttemptTiming]

    def __init__(self, local_analysis_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., attempts: _Optional[_Iterable[_Union[RemoteTestAttemptTiming, _Mapping]]]=...) -> None:
        ...

class TestTiming(_message.Message):
    __slots__ = ('local', 'remote', 'system_time_duration', 'user_time_duration', 'test_caching')
    LOCAL_FIELD_NUMBER: _ClassVar[int]
    REMOTE_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_TIME_DURATION_FIELD_NUMBER: _ClassVar[int]
    USER_TIME_DURATION_FIELD_NUMBER: _ClassVar[int]
    TEST_CACHING_FIELD_NUMBER: _ClassVar[int]
    local: LocalTestTiming
    remote: RemoteTestTiming
    system_time_duration: _duration_pb2.Duration
    user_time_duration: _duration_pb2.Duration
    test_caching: TestCaching

    def __init__(self, local: _Optional[_Union[LocalTestTiming, _Mapping]]=..., remote: _Optional[_Union[RemoteTestTiming, _Mapping]]=..., system_time_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., user_time_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., test_caching: _Optional[_Union[TestCaching, str]]=...) -> None:
        ...

class TestWarning(_message.Message):
    __slots__ = ('warning_message',)
    WARNING_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    warning_message: str

    def __init__(self, warning_message: _Optional[str]=...) -> None:
        ...