from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class OrchestratorOption(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ORCHESTRATOR_OPTION_UNSPECIFIED: _ClassVar[OrchestratorOption]
    USE_ORCHESTRATOR: _ClassVar[OrchestratorOption]
    DO_NOT_USE_ORCHESTRATOR: _ClassVar[OrchestratorOption]

class RoboMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ROBO_MODE_UNSPECIFIED: _ClassVar[RoboMode]
    ROBO_VERSION_1: _ClassVar[RoboMode]
    ROBO_VERSION_2: _ClassVar[RoboMode]

class RoboActionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ACTION_TYPE_UNSPECIFIED: _ClassVar[RoboActionType]
    SINGLE_CLICK: _ClassVar[RoboActionType]
    ENTER_TEXT: _ClassVar[RoboActionType]
    IGNORE: _ClassVar[RoboActionType]

class InvalidMatrixDetails(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    INVALID_MATRIX_DETAILS_UNSPECIFIED: _ClassVar[InvalidMatrixDetails]
    DETAILS_UNAVAILABLE: _ClassVar[InvalidMatrixDetails]
    MALFORMED_APK: _ClassVar[InvalidMatrixDetails]
    MALFORMED_TEST_APK: _ClassVar[InvalidMatrixDetails]
    NO_MANIFEST: _ClassVar[InvalidMatrixDetails]
    NO_PACKAGE_NAME: _ClassVar[InvalidMatrixDetails]
    INVALID_PACKAGE_NAME: _ClassVar[InvalidMatrixDetails]
    TEST_SAME_AS_APP: _ClassVar[InvalidMatrixDetails]
    NO_INSTRUMENTATION: _ClassVar[InvalidMatrixDetails]
    NO_SIGNATURE: _ClassVar[InvalidMatrixDetails]
    INSTRUMENTATION_ORCHESTRATOR_INCOMPATIBLE: _ClassVar[InvalidMatrixDetails]
    NO_TEST_RUNNER_CLASS: _ClassVar[InvalidMatrixDetails]
    NO_LAUNCHER_ACTIVITY: _ClassVar[InvalidMatrixDetails]
    FORBIDDEN_PERMISSIONS: _ClassVar[InvalidMatrixDetails]
    INVALID_ROBO_DIRECTIVES: _ClassVar[InvalidMatrixDetails]
    INVALID_RESOURCE_NAME: _ClassVar[InvalidMatrixDetails]
    INVALID_DIRECTIVE_ACTION: _ClassVar[InvalidMatrixDetails]
    TEST_LOOP_INTENT_FILTER_NOT_FOUND: _ClassVar[InvalidMatrixDetails]
    SCENARIO_LABEL_NOT_DECLARED: _ClassVar[InvalidMatrixDetails]
    SCENARIO_LABEL_MALFORMED: _ClassVar[InvalidMatrixDetails]
    SCENARIO_NOT_DECLARED: _ClassVar[InvalidMatrixDetails]
    DEVICE_ADMIN_RECEIVER: _ClassVar[InvalidMatrixDetails]
    MALFORMED_XC_TEST_ZIP: _ClassVar[InvalidMatrixDetails]
    BUILT_FOR_IOS_SIMULATOR: _ClassVar[InvalidMatrixDetails]
    NO_TESTS_IN_XC_TEST_ZIP: _ClassVar[InvalidMatrixDetails]
    USE_DESTINATION_ARTIFACTS: _ClassVar[InvalidMatrixDetails]
    TEST_NOT_APP_HOSTED: _ClassVar[InvalidMatrixDetails]
    PLIST_CANNOT_BE_PARSED: _ClassVar[InvalidMatrixDetails]
    TEST_ONLY_APK: _ClassVar[InvalidMatrixDetails]
    MALFORMED_IPA: _ClassVar[InvalidMatrixDetails]
    MISSING_URL_SCHEME: _ClassVar[InvalidMatrixDetails]
    MALFORMED_APP_BUNDLE: _ClassVar[InvalidMatrixDetails]
    NO_CODE_APK: _ClassVar[InvalidMatrixDetails]
    INVALID_INPUT_APK: _ClassVar[InvalidMatrixDetails]
    INVALID_APK_PREVIEW_SDK: _ClassVar[InvalidMatrixDetails]
    MATRIX_TOO_LARGE: _ClassVar[InvalidMatrixDetails]
    TEST_QUOTA_EXCEEDED: _ClassVar[InvalidMatrixDetails]
    SERVICE_NOT_ACTIVATED: _ClassVar[InvalidMatrixDetails]
    UNKNOWN_PERMISSION_ERROR: _ClassVar[InvalidMatrixDetails]

class TestState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TEST_STATE_UNSPECIFIED: _ClassVar[TestState]
    VALIDATING: _ClassVar[TestState]
    PENDING: _ClassVar[TestState]
    RUNNING: _ClassVar[TestState]
    FINISHED: _ClassVar[TestState]
    ERROR: _ClassVar[TestState]
    UNSUPPORTED_ENVIRONMENT: _ClassVar[TestState]
    INCOMPATIBLE_ENVIRONMENT: _ClassVar[TestState]
    INCOMPATIBLE_ARCHITECTURE: _ClassVar[TestState]
    CANCELLED: _ClassVar[TestState]
    INVALID: _ClassVar[TestState]

class OutcomeSummary(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OUTCOME_SUMMARY_UNSPECIFIED: _ClassVar[OutcomeSummary]
    SUCCESS: _ClassVar[OutcomeSummary]
    FAILURE: _ClassVar[OutcomeSummary]
    INCONCLUSIVE: _ClassVar[OutcomeSummary]
    SKIPPED: _ClassVar[OutcomeSummary]
ORCHESTRATOR_OPTION_UNSPECIFIED: OrchestratorOption
USE_ORCHESTRATOR: OrchestratorOption
DO_NOT_USE_ORCHESTRATOR: OrchestratorOption
ROBO_MODE_UNSPECIFIED: RoboMode
ROBO_VERSION_1: RoboMode
ROBO_VERSION_2: RoboMode
ACTION_TYPE_UNSPECIFIED: RoboActionType
SINGLE_CLICK: RoboActionType
ENTER_TEXT: RoboActionType
IGNORE: RoboActionType
INVALID_MATRIX_DETAILS_UNSPECIFIED: InvalidMatrixDetails
DETAILS_UNAVAILABLE: InvalidMatrixDetails
MALFORMED_APK: InvalidMatrixDetails
MALFORMED_TEST_APK: InvalidMatrixDetails
NO_MANIFEST: InvalidMatrixDetails
NO_PACKAGE_NAME: InvalidMatrixDetails
INVALID_PACKAGE_NAME: InvalidMatrixDetails
TEST_SAME_AS_APP: InvalidMatrixDetails
NO_INSTRUMENTATION: InvalidMatrixDetails
NO_SIGNATURE: InvalidMatrixDetails
INSTRUMENTATION_ORCHESTRATOR_INCOMPATIBLE: InvalidMatrixDetails
NO_TEST_RUNNER_CLASS: InvalidMatrixDetails
NO_LAUNCHER_ACTIVITY: InvalidMatrixDetails
FORBIDDEN_PERMISSIONS: InvalidMatrixDetails
INVALID_ROBO_DIRECTIVES: InvalidMatrixDetails
INVALID_RESOURCE_NAME: InvalidMatrixDetails
INVALID_DIRECTIVE_ACTION: InvalidMatrixDetails
TEST_LOOP_INTENT_FILTER_NOT_FOUND: InvalidMatrixDetails
SCENARIO_LABEL_NOT_DECLARED: InvalidMatrixDetails
SCENARIO_LABEL_MALFORMED: InvalidMatrixDetails
SCENARIO_NOT_DECLARED: InvalidMatrixDetails
DEVICE_ADMIN_RECEIVER: InvalidMatrixDetails
MALFORMED_XC_TEST_ZIP: InvalidMatrixDetails
BUILT_FOR_IOS_SIMULATOR: InvalidMatrixDetails
NO_TESTS_IN_XC_TEST_ZIP: InvalidMatrixDetails
USE_DESTINATION_ARTIFACTS: InvalidMatrixDetails
TEST_NOT_APP_HOSTED: InvalidMatrixDetails
PLIST_CANNOT_BE_PARSED: InvalidMatrixDetails
TEST_ONLY_APK: InvalidMatrixDetails
MALFORMED_IPA: InvalidMatrixDetails
MISSING_URL_SCHEME: InvalidMatrixDetails
MALFORMED_APP_BUNDLE: InvalidMatrixDetails
NO_CODE_APK: InvalidMatrixDetails
INVALID_INPUT_APK: InvalidMatrixDetails
INVALID_APK_PREVIEW_SDK: InvalidMatrixDetails
MATRIX_TOO_LARGE: InvalidMatrixDetails
TEST_QUOTA_EXCEEDED: InvalidMatrixDetails
SERVICE_NOT_ACTIVATED: InvalidMatrixDetails
UNKNOWN_PERMISSION_ERROR: InvalidMatrixDetails
TEST_STATE_UNSPECIFIED: TestState
VALIDATING: TestState
PENDING: TestState
RUNNING: TestState
FINISHED: TestState
ERROR: TestState
UNSUPPORTED_ENVIRONMENT: TestState
INCOMPATIBLE_ENVIRONMENT: TestState
INCOMPATIBLE_ARCHITECTURE: TestState
CANCELLED: TestState
INVALID: TestState
OUTCOME_SUMMARY_UNSPECIFIED: OutcomeSummary
SUCCESS: OutcomeSummary
FAILURE: OutcomeSummary
INCONCLUSIVE: OutcomeSummary
SKIPPED: OutcomeSummary

class TestMatrix(_message.Message):
    __slots__ = ('test_matrix_id', 'project_id', 'client_info', 'test_specification', 'environment_matrix', 'test_executions', 'result_storage', 'state', 'timestamp', 'invalid_matrix_details', 'extended_invalid_matrix_details', 'flaky_test_attempts', 'outcome_summary', 'fail_fast')
    TEST_MATRIX_ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_INFO_FIELD_NUMBER: _ClassVar[int]
    TEST_SPECIFICATION_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_MATRIX_FIELD_NUMBER: _ClassVar[int]
    TEST_EXECUTIONS_FIELD_NUMBER: _ClassVar[int]
    RESULT_STORAGE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    INVALID_MATRIX_DETAILS_FIELD_NUMBER: _ClassVar[int]
    EXTENDED_INVALID_MATRIX_DETAILS_FIELD_NUMBER: _ClassVar[int]
    FLAKY_TEST_ATTEMPTS_FIELD_NUMBER: _ClassVar[int]
    OUTCOME_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    FAIL_FAST_FIELD_NUMBER: _ClassVar[int]
    test_matrix_id: str
    project_id: str
    client_info: ClientInfo
    test_specification: TestSpecification
    environment_matrix: EnvironmentMatrix
    test_executions: _containers.RepeatedCompositeFieldContainer[TestExecution]
    result_storage: ResultStorage
    state: TestState
    timestamp: _timestamp_pb2.Timestamp
    invalid_matrix_details: InvalidMatrixDetails
    extended_invalid_matrix_details: _containers.RepeatedCompositeFieldContainer[MatrixErrorDetail]
    flaky_test_attempts: int
    outcome_summary: OutcomeSummary
    fail_fast: bool

    def __init__(self, test_matrix_id: _Optional[str]=..., project_id: _Optional[str]=..., client_info: _Optional[_Union[ClientInfo, _Mapping]]=..., test_specification: _Optional[_Union[TestSpecification, _Mapping]]=..., environment_matrix: _Optional[_Union[EnvironmentMatrix, _Mapping]]=..., test_executions: _Optional[_Iterable[_Union[TestExecution, _Mapping]]]=..., result_storage: _Optional[_Union[ResultStorage, _Mapping]]=..., state: _Optional[_Union[TestState, str]]=..., timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., invalid_matrix_details: _Optional[_Union[InvalidMatrixDetails, str]]=..., extended_invalid_matrix_details: _Optional[_Iterable[_Union[MatrixErrorDetail, _Mapping]]]=..., flaky_test_attempts: _Optional[int]=..., outcome_summary: _Optional[_Union[OutcomeSummary, str]]=..., fail_fast: bool=...) -> None:
        ...

class MatrixErrorDetail(_message.Message):
    __slots__ = ('reason', 'message')
    REASON_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    reason: str
    message: str

    def __init__(self, reason: _Optional[str]=..., message: _Optional[str]=...) -> None:
        ...

class TestExecution(_message.Message):
    __slots__ = ('id', 'matrix_id', 'project_id', 'test_specification', 'shard', 'environment', 'state', 'tool_results_step', 'timestamp', 'test_details')
    ID_FIELD_NUMBER: _ClassVar[int]
    MATRIX_ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    TEST_SPECIFICATION_FIELD_NUMBER: _ClassVar[int]
    SHARD_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    TOOL_RESULTS_STEP_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    TEST_DETAILS_FIELD_NUMBER: _ClassVar[int]
    id: str
    matrix_id: str
    project_id: str
    test_specification: TestSpecification
    shard: Shard
    environment: Environment
    state: TestState
    tool_results_step: ToolResultsStep
    timestamp: _timestamp_pb2.Timestamp
    test_details: TestDetails

    def __init__(self, id: _Optional[str]=..., matrix_id: _Optional[str]=..., project_id: _Optional[str]=..., test_specification: _Optional[_Union[TestSpecification, _Mapping]]=..., shard: _Optional[_Union[Shard, _Mapping]]=..., environment: _Optional[_Union[Environment, _Mapping]]=..., state: _Optional[_Union[TestState, str]]=..., tool_results_step: _Optional[_Union[ToolResultsStep, _Mapping]]=..., timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., test_details: _Optional[_Union[TestDetails, _Mapping]]=...) -> None:
        ...

class TestSpecification(_message.Message):
    __slots__ = ('test_timeout', 'test_setup', 'ios_test_setup', 'android_instrumentation_test', 'android_robo_test', 'android_test_loop', 'ios_xc_test', 'ios_test_loop', 'ios_robo_test', 'disable_video_recording', 'disable_performance_metrics')
    TEST_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    TEST_SETUP_FIELD_NUMBER: _ClassVar[int]
    IOS_TEST_SETUP_FIELD_NUMBER: _ClassVar[int]
    ANDROID_INSTRUMENTATION_TEST_FIELD_NUMBER: _ClassVar[int]
    ANDROID_ROBO_TEST_FIELD_NUMBER: _ClassVar[int]
    ANDROID_TEST_LOOP_FIELD_NUMBER: _ClassVar[int]
    IOS_XC_TEST_FIELD_NUMBER: _ClassVar[int]
    IOS_TEST_LOOP_FIELD_NUMBER: _ClassVar[int]
    IOS_ROBO_TEST_FIELD_NUMBER: _ClassVar[int]
    DISABLE_VIDEO_RECORDING_FIELD_NUMBER: _ClassVar[int]
    DISABLE_PERFORMANCE_METRICS_FIELD_NUMBER: _ClassVar[int]
    test_timeout: _duration_pb2.Duration
    test_setup: TestSetup
    ios_test_setup: IosTestSetup
    android_instrumentation_test: AndroidInstrumentationTest
    android_robo_test: AndroidRoboTest
    android_test_loop: AndroidTestLoop
    ios_xc_test: IosXcTest
    ios_test_loop: IosTestLoop
    ios_robo_test: IosRoboTest
    disable_video_recording: bool
    disable_performance_metrics: bool

    def __init__(self, test_timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., test_setup: _Optional[_Union[TestSetup, _Mapping]]=..., ios_test_setup: _Optional[_Union[IosTestSetup, _Mapping]]=..., android_instrumentation_test: _Optional[_Union[AndroidInstrumentationTest, _Mapping]]=..., android_robo_test: _Optional[_Union[AndroidRoboTest, _Mapping]]=..., android_test_loop: _Optional[_Union[AndroidTestLoop, _Mapping]]=..., ios_xc_test: _Optional[_Union[IosXcTest, _Mapping]]=..., ios_test_loop: _Optional[_Union[IosTestLoop, _Mapping]]=..., ios_robo_test: _Optional[_Union[IosRoboTest, _Mapping]]=..., disable_video_recording: bool=..., disable_performance_metrics: bool=...) -> None:
        ...

class SystraceSetup(_message.Message):
    __slots__ = ('duration_seconds',)
    DURATION_SECONDS_FIELD_NUMBER: _ClassVar[int]
    duration_seconds: int

    def __init__(self, duration_seconds: _Optional[int]=...) -> None:
        ...

class TestSetup(_message.Message):
    __slots__ = ('files_to_push', 'directories_to_pull', 'initial_setup_apks', 'additional_apks', 'account', 'network_profile', 'environment_variables', 'systrace', 'dont_autogrant_permissions')
    FILES_TO_PUSH_FIELD_NUMBER: _ClassVar[int]
    DIRECTORIES_TO_PULL_FIELD_NUMBER: _ClassVar[int]
    INITIAL_SETUP_APKS_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_APKS_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    NETWORK_PROFILE_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_VARIABLES_FIELD_NUMBER: _ClassVar[int]
    SYSTRACE_FIELD_NUMBER: _ClassVar[int]
    DONT_AUTOGRANT_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    files_to_push: _containers.RepeatedCompositeFieldContainer[DeviceFile]
    directories_to_pull: _containers.RepeatedScalarFieldContainer[str]
    initial_setup_apks: _containers.RepeatedCompositeFieldContainer[Apk]
    additional_apks: _containers.RepeatedCompositeFieldContainer[Apk]
    account: Account
    network_profile: str
    environment_variables: _containers.RepeatedCompositeFieldContainer[EnvironmentVariable]
    systrace: SystraceSetup
    dont_autogrant_permissions: bool

    def __init__(self, files_to_push: _Optional[_Iterable[_Union[DeviceFile, _Mapping]]]=..., directories_to_pull: _Optional[_Iterable[str]]=..., initial_setup_apks: _Optional[_Iterable[_Union[Apk, _Mapping]]]=..., additional_apks: _Optional[_Iterable[_Union[Apk, _Mapping]]]=..., account: _Optional[_Union[Account, _Mapping]]=..., network_profile: _Optional[str]=..., environment_variables: _Optional[_Iterable[_Union[EnvironmentVariable, _Mapping]]]=..., systrace: _Optional[_Union[SystraceSetup, _Mapping]]=..., dont_autogrant_permissions: bool=...) -> None:
        ...

class IosTestSetup(_message.Message):
    __slots__ = ('network_profile', 'additional_ipas', 'push_files', 'pull_directories')
    NETWORK_PROFILE_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_IPAS_FIELD_NUMBER: _ClassVar[int]
    PUSH_FILES_FIELD_NUMBER: _ClassVar[int]
    PULL_DIRECTORIES_FIELD_NUMBER: _ClassVar[int]
    network_profile: str
    additional_ipas: _containers.RepeatedCompositeFieldContainer[FileReference]
    push_files: _containers.RepeatedCompositeFieldContainer[IosDeviceFile]
    pull_directories: _containers.RepeatedCompositeFieldContainer[IosDeviceFile]

    def __init__(self, network_profile: _Optional[str]=..., additional_ipas: _Optional[_Iterable[_Union[FileReference, _Mapping]]]=..., push_files: _Optional[_Iterable[_Union[IosDeviceFile, _Mapping]]]=..., pull_directories: _Optional[_Iterable[_Union[IosDeviceFile, _Mapping]]]=...) -> None:
        ...

class EnvironmentVariable(_message.Message):
    __slots__ = ('key', 'value')
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: str

    def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
        ...

class Account(_message.Message):
    __slots__ = ('google_auto',)
    GOOGLE_AUTO_FIELD_NUMBER: _ClassVar[int]
    google_auto: GoogleAuto

    def __init__(self, google_auto: _Optional[_Union[GoogleAuto, _Mapping]]=...) -> None:
        ...

class GoogleAuto(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class Apk(_message.Message):
    __slots__ = ('location', 'package_name')
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_NAME_FIELD_NUMBER: _ClassVar[int]
    location: FileReference
    package_name: str

    def __init__(self, location: _Optional[_Union[FileReference, _Mapping]]=..., package_name: _Optional[str]=...) -> None:
        ...

class AppBundle(_message.Message):
    __slots__ = ('bundle_location',)
    BUNDLE_LOCATION_FIELD_NUMBER: _ClassVar[int]
    bundle_location: FileReference

    def __init__(self, bundle_location: _Optional[_Union[FileReference, _Mapping]]=...) -> None:
        ...

class DeviceFile(_message.Message):
    __slots__ = ('obb_file', 'regular_file')
    OBB_FILE_FIELD_NUMBER: _ClassVar[int]
    REGULAR_FILE_FIELD_NUMBER: _ClassVar[int]
    obb_file: ObbFile
    regular_file: RegularFile

    def __init__(self, obb_file: _Optional[_Union[ObbFile, _Mapping]]=..., regular_file: _Optional[_Union[RegularFile, _Mapping]]=...) -> None:
        ...

class ObbFile(_message.Message):
    __slots__ = ('obb_file_name', 'obb')
    OBB_FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    OBB_FIELD_NUMBER: _ClassVar[int]
    obb_file_name: str
    obb: FileReference

    def __init__(self, obb_file_name: _Optional[str]=..., obb: _Optional[_Union[FileReference, _Mapping]]=...) -> None:
        ...

class RegularFile(_message.Message):
    __slots__ = ('content', 'device_path')
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    DEVICE_PATH_FIELD_NUMBER: _ClassVar[int]
    content: FileReference
    device_path: str

    def __init__(self, content: _Optional[_Union[FileReference, _Mapping]]=..., device_path: _Optional[str]=...) -> None:
        ...

class IosDeviceFile(_message.Message):
    __slots__ = ('content', 'bundle_id', 'device_path')
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    BUNDLE_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_PATH_FIELD_NUMBER: _ClassVar[int]
    content: FileReference
    bundle_id: str
    device_path: str

    def __init__(self, content: _Optional[_Union[FileReference, _Mapping]]=..., bundle_id: _Optional[str]=..., device_path: _Optional[str]=...) -> None:
        ...

class AndroidTestLoop(_message.Message):
    __slots__ = ('app_apk', 'app_bundle', 'app_package_id', 'scenarios', 'scenario_labels')
    APP_APK_FIELD_NUMBER: _ClassVar[int]
    APP_BUNDLE_FIELD_NUMBER: _ClassVar[int]
    APP_PACKAGE_ID_FIELD_NUMBER: _ClassVar[int]
    SCENARIOS_FIELD_NUMBER: _ClassVar[int]
    SCENARIO_LABELS_FIELD_NUMBER: _ClassVar[int]
    app_apk: FileReference
    app_bundle: AppBundle
    app_package_id: str
    scenarios: _containers.RepeatedScalarFieldContainer[int]
    scenario_labels: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, app_apk: _Optional[_Union[FileReference, _Mapping]]=..., app_bundle: _Optional[_Union[AppBundle, _Mapping]]=..., app_package_id: _Optional[str]=..., scenarios: _Optional[_Iterable[int]]=..., scenario_labels: _Optional[_Iterable[str]]=...) -> None:
        ...

class IosXcTest(_message.Message):
    __slots__ = ('tests_zip', 'xctestrun', 'xcode_version', 'app_bundle_id', 'test_special_entitlements')
    TESTS_ZIP_FIELD_NUMBER: _ClassVar[int]
    XCTESTRUN_FIELD_NUMBER: _ClassVar[int]
    XCODE_VERSION_FIELD_NUMBER: _ClassVar[int]
    APP_BUNDLE_ID_FIELD_NUMBER: _ClassVar[int]
    TEST_SPECIAL_ENTITLEMENTS_FIELD_NUMBER: _ClassVar[int]
    tests_zip: FileReference
    xctestrun: FileReference
    xcode_version: str
    app_bundle_id: str
    test_special_entitlements: bool

    def __init__(self, tests_zip: _Optional[_Union[FileReference, _Mapping]]=..., xctestrun: _Optional[_Union[FileReference, _Mapping]]=..., xcode_version: _Optional[str]=..., app_bundle_id: _Optional[str]=..., test_special_entitlements: bool=...) -> None:
        ...

class IosTestLoop(_message.Message):
    __slots__ = ('app_ipa', 'scenarios', 'app_bundle_id')
    APP_IPA_FIELD_NUMBER: _ClassVar[int]
    SCENARIOS_FIELD_NUMBER: _ClassVar[int]
    APP_BUNDLE_ID_FIELD_NUMBER: _ClassVar[int]
    app_ipa: FileReference
    scenarios: _containers.RepeatedScalarFieldContainer[int]
    app_bundle_id: str

    def __init__(self, app_ipa: _Optional[_Union[FileReference, _Mapping]]=..., scenarios: _Optional[_Iterable[int]]=..., app_bundle_id: _Optional[str]=...) -> None:
        ...

class IosRoboTest(_message.Message):
    __slots__ = ('app_ipa', 'app_bundle_id', 'robo_script')
    APP_IPA_FIELD_NUMBER: _ClassVar[int]
    APP_BUNDLE_ID_FIELD_NUMBER: _ClassVar[int]
    ROBO_SCRIPT_FIELD_NUMBER: _ClassVar[int]
    app_ipa: FileReference
    app_bundle_id: str
    robo_script: FileReference

    def __init__(self, app_ipa: _Optional[_Union[FileReference, _Mapping]]=..., app_bundle_id: _Optional[str]=..., robo_script: _Optional[_Union[FileReference, _Mapping]]=...) -> None:
        ...

class AndroidInstrumentationTest(_message.Message):
    __slots__ = ('app_apk', 'app_bundle', 'test_apk', 'app_package_id', 'test_package_id', 'test_runner_class', 'test_targets', 'orchestrator_option', 'sharding_option')
    APP_APK_FIELD_NUMBER: _ClassVar[int]
    APP_BUNDLE_FIELD_NUMBER: _ClassVar[int]
    TEST_APK_FIELD_NUMBER: _ClassVar[int]
    APP_PACKAGE_ID_FIELD_NUMBER: _ClassVar[int]
    TEST_PACKAGE_ID_FIELD_NUMBER: _ClassVar[int]
    TEST_RUNNER_CLASS_FIELD_NUMBER: _ClassVar[int]
    TEST_TARGETS_FIELD_NUMBER: _ClassVar[int]
    ORCHESTRATOR_OPTION_FIELD_NUMBER: _ClassVar[int]
    SHARDING_OPTION_FIELD_NUMBER: _ClassVar[int]
    app_apk: FileReference
    app_bundle: AppBundle
    test_apk: FileReference
    app_package_id: str
    test_package_id: str
    test_runner_class: str
    test_targets: _containers.RepeatedScalarFieldContainer[str]
    orchestrator_option: OrchestratorOption
    sharding_option: ShardingOption

    def __init__(self, app_apk: _Optional[_Union[FileReference, _Mapping]]=..., app_bundle: _Optional[_Union[AppBundle, _Mapping]]=..., test_apk: _Optional[_Union[FileReference, _Mapping]]=..., app_package_id: _Optional[str]=..., test_package_id: _Optional[str]=..., test_runner_class: _Optional[str]=..., test_targets: _Optional[_Iterable[str]]=..., orchestrator_option: _Optional[_Union[OrchestratorOption, str]]=..., sharding_option: _Optional[_Union[ShardingOption, _Mapping]]=...) -> None:
        ...

class AndroidRoboTest(_message.Message):
    __slots__ = ('app_apk', 'app_bundle', 'app_package_id', 'app_initial_activity', 'max_depth', 'max_steps', 'robo_directives', 'robo_mode', 'robo_script', 'starting_intents')
    APP_APK_FIELD_NUMBER: _ClassVar[int]
    APP_BUNDLE_FIELD_NUMBER: _ClassVar[int]
    APP_PACKAGE_ID_FIELD_NUMBER: _ClassVar[int]
    APP_INITIAL_ACTIVITY_FIELD_NUMBER: _ClassVar[int]
    MAX_DEPTH_FIELD_NUMBER: _ClassVar[int]
    MAX_STEPS_FIELD_NUMBER: _ClassVar[int]
    ROBO_DIRECTIVES_FIELD_NUMBER: _ClassVar[int]
    ROBO_MODE_FIELD_NUMBER: _ClassVar[int]
    ROBO_SCRIPT_FIELD_NUMBER: _ClassVar[int]
    STARTING_INTENTS_FIELD_NUMBER: _ClassVar[int]
    app_apk: FileReference
    app_bundle: AppBundle
    app_package_id: str
    app_initial_activity: str
    max_depth: int
    max_steps: int
    robo_directives: _containers.RepeatedCompositeFieldContainer[RoboDirective]
    robo_mode: RoboMode
    robo_script: FileReference
    starting_intents: _containers.RepeatedCompositeFieldContainer[RoboStartingIntent]

    def __init__(self, app_apk: _Optional[_Union[FileReference, _Mapping]]=..., app_bundle: _Optional[_Union[AppBundle, _Mapping]]=..., app_package_id: _Optional[str]=..., app_initial_activity: _Optional[str]=..., max_depth: _Optional[int]=..., max_steps: _Optional[int]=..., robo_directives: _Optional[_Iterable[_Union[RoboDirective, _Mapping]]]=..., robo_mode: _Optional[_Union[RoboMode, str]]=..., robo_script: _Optional[_Union[FileReference, _Mapping]]=..., starting_intents: _Optional[_Iterable[_Union[RoboStartingIntent, _Mapping]]]=...) -> None:
        ...

class RoboDirective(_message.Message):
    __slots__ = ('resource_name', 'input_text', 'action_type')
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    INPUT_TEXT_FIELD_NUMBER: _ClassVar[int]
    ACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    input_text: str
    action_type: RoboActionType

    def __init__(self, resource_name: _Optional[str]=..., input_text: _Optional[str]=..., action_type: _Optional[_Union[RoboActionType, str]]=...) -> None:
        ...

class RoboStartingIntent(_message.Message):
    __slots__ = ('launcher_activity', 'start_activity', 'no_activity', 'timeout')
    LAUNCHER_ACTIVITY_FIELD_NUMBER: _ClassVar[int]
    START_ACTIVITY_FIELD_NUMBER: _ClassVar[int]
    NO_ACTIVITY_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    launcher_activity: LauncherActivityIntent
    start_activity: StartActivityIntent
    no_activity: NoActivityIntent
    timeout: _duration_pb2.Duration

    def __init__(self, launcher_activity: _Optional[_Union[LauncherActivityIntent, _Mapping]]=..., start_activity: _Optional[_Union[StartActivityIntent, _Mapping]]=..., no_activity: _Optional[_Union[NoActivityIntent, _Mapping]]=..., timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=...) -> None:
        ...

class LauncherActivityIntent(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class StartActivityIntent(_message.Message):
    __slots__ = ('action', 'uri', 'categories')
    ACTION_FIELD_NUMBER: _ClassVar[int]
    URI_FIELD_NUMBER: _ClassVar[int]
    CATEGORIES_FIELD_NUMBER: _ClassVar[int]
    action: str
    uri: str
    categories: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, action: _Optional[str]=..., uri: _Optional[str]=..., categories: _Optional[_Iterable[str]]=...) -> None:
        ...

class NoActivityIntent(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class EnvironmentMatrix(_message.Message):
    __slots__ = ('android_matrix', 'android_device_list', 'ios_device_list')
    ANDROID_MATRIX_FIELD_NUMBER: _ClassVar[int]
    ANDROID_DEVICE_LIST_FIELD_NUMBER: _ClassVar[int]
    IOS_DEVICE_LIST_FIELD_NUMBER: _ClassVar[int]
    android_matrix: AndroidMatrix
    android_device_list: AndroidDeviceList
    ios_device_list: IosDeviceList

    def __init__(self, android_matrix: _Optional[_Union[AndroidMatrix, _Mapping]]=..., android_device_list: _Optional[_Union[AndroidDeviceList, _Mapping]]=..., ios_device_list: _Optional[_Union[IosDeviceList, _Mapping]]=...) -> None:
        ...

class AndroidDeviceList(_message.Message):
    __slots__ = ('android_devices',)
    ANDROID_DEVICES_FIELD_NUMBER: _ClassVar[int]
    android_devices: _containers.RepeatedCompositeFieldContainer[AndroidDevice]

    def __init__(self, android_devices: _Optional[_Iterable[_Union[AndroidDevice, _Mapping]]]=...) -> None:
        ...

class IosDeviceList(_message.Message):
    __slots__ = ('ios_devices',)
    IOS_DEVICES_FIELD_NUMBER: _ClassVar[int]
    ios_devices: _containers.RepeatedCompositeFieldContainer[IosDevice]

    def __init__(self, ios_devices: _Optional[_Iterable[_Union[IosDevice, _Mapping]]]=...) -> None:
        ...

class AndroidMatrix(_message.Message):
    __slots__ = ('android_model_ids', 'android_version_ids', 'locales', 'orientations')
    ANDROID_MODEL_IDS_FIELD_NUMBER: _ClassVar[int]
    ANDROID_VERSION_IDS_FIELD_NUMBER: _ClassVar[int]
    LOCALES_FIELD_NUMBER: _ClassVar[int]
    ORIENTATIONS_FIELD_NUMBER: _ClassVar[int]
    android_model_ids: _containers.RepeatedScalarFieldContainer[str]
    android_version_ids: _containers.RepeatedScalarFieldContainer[str]
    locales: _containers.RepeatedScalarFieldContainer[str]
    orientations: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, android_model_ids: _Optional[_Iterable[str]]=..., android_version_ids: _Optional[_Iterable[str]]=..., locales: _Optional[_Iterable[str]]=..., orientations: _Optional[_Iterable[str]]=...) -> None:
        ...

class ClientInfo(_message.Message):
    __slots__ = ('name', 'client_info_details')
    NAME_FIELD_NUMBER: _ClassVar[int]
    CLIENT_INFO_DETAILS_FIELD_NUMBER: _ClassVar[int]
    name: str
    client_info_details: _containers.RepeatedCompositeFieldContainer[ClientInfoDetail]

    def __init__(self, name: _Optional[str]=..., client_info_details: _Optional[_Iterable[_Union[ClientInfoDetail, _Mapping]]]=...) -> None:
        ...

class ClientInfoDetail(_message.Message):
    __slots__ = ('key', 'value')
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: str

    def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
        ...

class ResultStorage(_message.Message):
    __slots__ = ('google_cloud_storage', 'tool_results_history', 'tool_results_execution', 'results_url')
    GOOGLE_CLOUD_STORAGE_FIELD_NUMBER: _ClassVar[int]
    TOOL_RESULTS_HISTORY_FIELD_NUMBER: _ClassVar[int]
    TOOL_RESULTS_EXECUTION_FIELD_NUMBER: _ClassVar[int]
    RESULTS_URL_FIELD_NUMBER: _ClassVar[int]
    google_cloud_storage: GoogleCloudStorage
    tool_results_history: ToolResultsHistory
    tool_results_execution: ToolResultsExecution
    results_url: str

    def __init__(self, google_cloud_storage: _Optional[_Union[GoogleCloudStorage, _Mapping]]=..., tool_results_history: _Optional[_Union[ToolResultsHistory, _Mapping]]=..., tool_results_execution: _Optional[_Union[ToolResultsExecution, _Mapping]]=..., results_url: _Optional[str]=...) -> None:
        ...

class ToolResultsHistory(_message.Message):
    __slots__ = ('project_id', 'history_id')
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    HISTORY_ID_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    history_id: str

    def __init__(self, project_id: _Optional[str]=..., history_id: _Optional[str]=...) -> None:
        ...

class ToolResultsExecution(_message.Message):
    __slots__ = ('project_id', 'history_id', 'execution_id')
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    HISTORY_ID_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_ID_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    history_id: str
    execution_id: str

    def __init__(self, project_id: _Optional[str]=..., history_id: _Optional[str]=..., execution_id: _Optional[str]=...) -> None:
        ...

class ToolResultsStep(_message.Message):
    __slots__ = ('project_id', 'history_id', 'execution_id', 'step_id')
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    HISTORY_ID_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_ID_FIELD_NUMBER: _ClassVar[int]
    STEP_ID_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    history_id: str
    execution_id: str
    step_id: str

    def __init__(self, project_id: _Optional[str]=..., history_id: _Optional[str]=..., execution_id: _Optional[str]=..., step_id: _Optional[str]=...) -> None:
        ...

class GoogleCloudStorage(_message.Message):
    __slots__ = ('gcs_path',)
    GCS_PATH_FIELD_NUMBER: _ClassVar[int]
    gcs_path: str

    def __init__(self, gcs_path: _Optional[str]=...) -> None:
        ...

class FileReference(_message.Message):
    __slots__ = ('gcs_path',)
    GCS_PATH_FIELD_NUMBER: _ClassVar[int]
    gcs_path: str

    def __init__(self, gcs_path: _Optional[str]=...) -> None:
        ...

class Environment(_message.Message):
    __slots__ = ('android_device', 'ios_device')
    ANDROID_DEVICE_FIELD_NUMBER: _ClassVar[int]
    IOS_DEVICE_FIELD_NUMBER: _ClassVar[int]
    android_device: AndroidDevice
    ios_device: IosDevice

    def __init__(self, android_device: _Optional[_Union[AndroidDevice, _Mapping]]=..., ios_device: _Optional[_Union[IosDevice, _Mapping]]=...) -> None:
        ...

class AndroidDevice(_message.Message):
    __slots__ = ('android_model_id', 'android_version_id', 'locale', 'orientation')
    ANDROID_MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    ANDROID_VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    ORIENTATION_FIELD_NUMBER: _ClassVar[int]
    android_model_id: str
    android_version_id: str
    locale: str
    orientation: str

    def __init__(self, android_model_id: _Optional[str]=..., android_version_id: _Optional[str]=..., locale: _Optional[str]=..., orientation: _Optional[str]=...) -> None:
        ...

class IosDevice(_message.Message):
    __slots__ = ('ios_model_id', 'ios_version_id', 'locale', 'orientation')
    IOS_MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    IOS_VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    ORIENTATION_FIELD_NUMBER: _ClassVar[int]
    ios_model_id: str
    ios_version_id: str
    locale: str
    orientation: str

    def __init__(self, ios_model_id: _Optional[str]=..., ios_version_id: _Optional[str]=..., locale: _Optional[str]=..., orientation: _Optional[str]=...) -> None:
        ...

class TestDetails(_message.Message):
    __slots__ = ('progress_messages', 'error_message')
    PROGRESS_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    progress_messages: _containers.RepeatedScalarFieldContainer[str]
    error_message: str

    def __init__(self, progress_messages: _Optional[_Iterable[str]]=..., error_message: _Optional[str]=...) -> None:
        ...

class InvalidRequestDetail(_message.Message):
    __slots__ = ('reason',)

    class Reason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        REASON_UNSPECIFIED: _ClassVar[InvalidRequestDetail.Reason]
        REQUEST_INVALID: _ClassVar[InvalidRequestDetail.Reason]
        RESOURCE_TOO_BIG: _ClassVar[InvalidRequestDetail.Reason]
        RESOURCE_NOT_FOUND: _ClassVar[InvalidRequestDetail.Reason]
        UNSUPPORTED: _ClassVar[InvalidRequestDetail.Reason]
        NOT_IMPLEMENTED: _ClassVar[InvalidRequestDetail.Reason]
        RESULT_STORAGE_PERMISSION_DENIED: _ClassVar[InvalidRequestDetail.Reason]
    REASON_UNSPECIFIED: InvalidRequestDetail.Reason
    REQUEST_INVALID: InvalidRequestDetail.Reason
    RESOURCE_TOO_BIG: InvalidRequestDetail.Reason
    RESOURCE_NOT_FOUND: InvalidRequestDetail.Reason
    UNSUPPORTED: InvalidRequestDetail.Reason
    NOT_IMPLEMENTED: InvalidRequestDetail.Reason
    RESULT_STORAGE_PERMISSION_DENIED: InvalidRequestDetail.Reason
    REASON_FIELD_NUMBER: _ClassVar[int]
    reason: InvalidRequestDetail.Reason

    def __init__(self, reason: _Optional[_Union[InvalidRequestDetail.Reason, str]]=...) -> None:
        ...

class ShardingOption(_message.Message):
    __slots__ = ('uniform_sharding', 'manual_sharding', 'smart_sharding')
    UNIFORM_SHARDING_FIELD_NUMBER: _ClassVar[int]
    MANUAL_SHARDING_FIELD_NUMBER: _ClassVar[int]
    SMART_SHARDING_FIELD_NUMBER: _ClassVar[int]
    uniform_sharding: UniformSharding
    manual_sharding: ManualSharding
    smart_sharding: SmartSharding

    def __init__(self, uniform_sharding: _Optional[_Union[UniformSharding, _Mapping]]=..., manual_sharding: _Optional[_Union[ManualSharding, _Mapping]]=..., smart_sharding: _Optional[_Union[SmartSharding, _Mapping]]=...) -> None:
        ...

class UniformSharding(_message.Message):
    __slots__ = ('num_shards',)
    NUM_SHARDS_FIELD_NUMBER: _ClassVar[int]
    num_shards: int

    def __init__(self, num_shards: _Optional[int]=...) -> None:
        ...

class ManualSharding(_message.Message):
    __slots__ = ('test_targets_for_shard',)
    TEST_TARGETS_FOR_SHARD_FIELD_NUMBER: _ClassVar[int]
    test_targets_for_shard: _containers.RepeatedCompositeFieldContainer[TestTargetsForShard]

    def __init__(self, test_targets_for_shard: _Optional[_Iterable[_Union[TestTargetsForShard, _Mapping]]]=...) -> None:
        ...

class TestTargetsForShard(_message.Message):
    __slots__ = ('test_targets',)
    TEST_TARGETS_FIELD_NUMBER: _ClassVar[int]
    test_targets: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, test_targets: _Optional[_Iterable[str]]=...) -> None:
        ...

class SmartSharding(_message.Message):
    __slots__ = ('targeted_shard_duration',)
    TARGETED_SHARD_DURATION_FIELD_NUMBER: _ClassVar[int]
    targeted_shard_duration: _duration_pb2.Duration

    def __init__(self, targeted_shard_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=...) -> None:
        ...

class Shard(_message.Message):
    __slots__ = ('shard_index', 'num_shards', 'test_targets_for_shard', 'estimated_shard_duration')
    SHARD_INDEX_FIELD_NUMBER: _ClassVar[int]
    NUM_SHARDS_FIELD_NUMBER: _ClassVar[int]
    TEST_TARGETS_FOR_SHARD_FIELD_NUMBER: _ClassVar[int]
    ESTIMATED_SHARD_DURATION_FIELD_NUMBER: _ClassVar[int]
    shard_index: int
    num_shards: int
    test_targets_for_shard: TestTargetsForShard
    estimated_shard_duration: _duration_pb2.Duration

    def __init__(self, shard_index: _Optional[int]=..., num_shards: _Optional[int]=..., test_targets_for_shard: _Optional[_Union[TestTargetsForShard, _Mapping]]=..., estimated_shard_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=...) -> None:
        ...

class CreateTestMatrixRequest(_message.Message):
    __slots__ = ('project_id', 'test_matrix', 'request_id')
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    TEST_MATRIX_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    test_matrix: TestMatrix
    request_id: str

    def __init__(self, project_id: _Optional[str]=..., test_matrix: _Optional[_Union[TestMatrix, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class GetTestMatrixRequest(_message.Message):
    __slots__ = ('project_id', 'test_matrix_id')
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    TEST_MATRIX_ID_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    test_matrix_id: str

    def __init__(self, project_id: _Optional[str]=..., test_matrix_id: _Optional[str]=...) -> None:
        ...

class CancelTestMatrixRequest(_message.Message):
    __slots__ = ('project_id', 'test_matrix_id')
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    TEST_MATRIX_ID_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    test_matrix_id: str

    def __init__(self, project_id: _Optional[str]=..., test_matrix_id: _Optional[str]=...) -> None:
        ...

class CancelTestMatrixResponse(_message.Message):
    __slots__ = ('test_state',)
    TEST_STATE_FIELD_NUMBER: _ClassVar[int]
    test_state: TestState

    def __init__(self, test_state: _Optional[_Union[TestState, str]]=...) -> None:
        ...