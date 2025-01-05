from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.cloud.integrations.v1alpha import cloud_logging_details_pb2 as _cloud_logging_details_pb2
from google.cloud.integrations.v1alpha import event_parameter_pb2 as _event_parameter_pb2
from google.cloud.integrations.v1alpha import integration_state_pb2 as _integration_state_pb2
from google.cloud.integrations.v1alpha import task_config_pb2 as _task_config_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ExecutionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EXECUTION_TYPE_UNSPECIFIED: _ClassVar[ExecutionType]
    INTEGRATION_VERSION: _ClassVar[ExecutionType]
    TEST_CASE: _ClassVar[ExecutionType]
EXECUTION_TYPE_UNSPECIFIED: ExecutionType
INTEGRATION_VERSION: ExecutionType
TEST_CASE: ExecutionType

class ExecutionInfo(_message.Message):
    __slots__ = ("integration", "project_id", "trigger_id", "request_params", "response_params", "errors", "task_configs", "integration_version_number", "execution_id", "integration_version_state", "enable_database_persistence", "cloud_logging_details", "integration_execution_details", "execution_type", "execution_method", "integration_snapshot_number", "replay_info")
    class ExecutionMethod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        EXECUTION_METHOD_UNSPECIFIED: _ClassVar[ExecutionInfo.ExecutionMethod]
        POST: _ClassVar[ExecutionInfo.ExecutionMethod]
        SCHEDULE: _ClassVar[ExecutionInfo.ExecutionMethod]
        POST_TO_QUEUE: _ClassVar[ExecutionInfo.ExecutionMethod]
    EXECUTION_METHOD_UNSPECIFIED: ExecutionInfo.ExecutionMethod
    POST: ExecutionInfo.ExecutionMethod
    SCHEDULE: ExecutionInfo.ExecutionMethod
    POST_TO_QUEUE: ExecutionInfo.ExecutionMethod
    class ReplayInfo(_message.Message):
        __slots__ = ("original_execution_info_id", "replayed_execution_info_ids", "replay_reason")
        ORIGINAL_EXECUTION_INFO_ID_FIELD_NUMBER: _ClassVar[int]
        REPLAYED_EXECUTION_INFO_IDS_FIELD_NUMBER: _ClassVar[int]
        REPLAY_REASON_FIELD_NUMBER: _ClassVar[int]
        original_execution_info_id: str
        replayed_execution_info_ids: _containers.RepeatedScalarFieldContainer[str]
        replay_reason: str
        def __init__(self, original_execution_info_id: _Optional[str] = ..., replayed_execution_info_ids: _Optional[_Iterable[str]] = ..., replay_reason: _Optional[str] = ...) -> None: ...
    class RequestParamsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _event_parameter_pb2.EventParameter
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_event_parameter_pb2.EventParameter, _Mapping]] = ...) -> None: ...
    class ResponseParamsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _event_parameter_pb2.EventParameter
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_event_parameter_pb2.EventParameter, _Mapping]] = ...) -> None: ...
    INTEGRATION_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_ID_FIELD_NUMBER: _ClassVar[int]
    REQUEST_PARAMS_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    TASK_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    INTEGRATION_VERSION_NUMBER_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_ID_FIELD_NUMBER: _ClassVar[int]
    INTEGRATION_VERSION_STATE_FIELD_NUMBER: _ClassVar[int]
    ENABLE_DATABASE_PERSISTENCE_FIELD_NUMBER: _ClassVar[int]
    CLOUD_LOGGING_DETAILS_FIELD_NUMBER: _ClassVar[int]
    INTEGRATION_EXECUTION_DETAILS_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_METHOD_FIELD_NUMBER: _ClassVar[int]
    INTEGRATION_SNAPSHOT_NUMBER_FIELD_NUMBER: _ClassVar[int]
    REPLAY_INFO_FIELD_NUMBER: _ClassVar[int]
    integration: str
    project_id: str
    trigger_id: str
    request_params: _containers.MessageMap[str, _event_parameter_pb2.EventParameter]
    response_params: _containers.MessageMap[str, _event_parameter_pb2.EventParameter]
    errors: _containers.RepeatedCompositeFieldContainer[ErrorDetail]
    task_configs: _containers.RepeatedCompositeFieldContainer[_task_config_pb2.TaskConfig]
    integration_version_number: str
    execution_id: str
    integration_version_state: _integration_state_pb2.IntegrationState
    enable_database_persistence: bool
    cloud_logging_details: _cloud_logging_details_pb2.CloudLoggingDetails
    integration_execution_details: IntegrationExecutionDetails
    execution_type: ExecutionType
    execution_method: ExecutionInfo.ExecutionMethod
    integration_snapshot_number: int
    replay_info: ExecutionInfo.ReplayInfo
    def __init__(self, integration: _Optional[str] = ..., project_id: _Optional[str] = ..., trigger_id: _Optional[str] = ..., request_params: _Optional[_Mapping[str, _event_parameter_pb2.EventParameter]] = ..., response_params: _Optional[_Mapping[str, _event_parameter_pb2.EventParameter]] = ..., errors: _Optional[_Iterable[_Union[ErrorDetail, _Mapping]]] = ..., task_configs: _Optional[_Iterable[_Union[_task_config_pb2.TaskConfig, _Mapping]]] = ..., integration_version_number: _Optional[str] = ..., execution_id: _Optional[str] = ..., integration_version_state: _Optional[_Union[_integration_state_pb2.IntegrationState, str]] = ..., enable_database_persistence: bool = ..., cloud_logging_details: _Optional[_Union[_cloud_logging_details_pb2.CloudLoggingDetails, _Mapping]] = ..., integration_execution_details: _Optional[_Union[IntegrationExecutionDetails, _Mapping]] = ..., execution_type: _Optional[_Union[ExecutionType, str]] = ..., execution_method: _Optional[_Union[ExecutionInfo.ExecutionMethod, str]] = ..., integration_snapshot_number: _Optional[int] = ..., replay_info: _Optional[_Union[ExecutionInfo.ReplayInfo, _Mapping]] = ...) -> None: ...

class IntegrationExecutionDetails(_message.Message):
    __slots__ = ("integration_execution_state", "integration_execution_snapshot", "execution_attempt_stats", "next_execution_time", "execution_retries_count", "cancel_reason")
    class IntegrationExecutionState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        INTEGRATION_EXECUTION_STATE_UNSPECIFIED: _ClassVar[IntegrationExecutionDetails.IntegrationExecutionState]
        ON_HOLD: _ClassVar[IntegrationExecutionDetails.IntegrationExecutionState]
        IN_PROCESS: _ClassVar[IntegrationExecutionDetails.IntegrationExecutionState]
        SUCCEEDED: _ClassVar[IntegrationExecutionDetails.IntegrationExecutionState]
        FAILED: _ClassVar[IntegrationExecutionDetails.IntegrationExecutionState]
        CANCELLED: _ClassVar[IntegrationExecutionDetails.IntegrationExecutionState]
        RETRY_ON_HOLD: _ClassVar[IntegrationExecutionDetails.IntegrationExecutionState]
        SUSPENDED: _ClassVar[IntegrationExecutionDetails.IntegrationExecutionState]
    INTEGRATION_EXECUTION_STATE_UNSPECIFIED: IntegrationExecutionDetails.IntegrationExecutionState
    ON_HOLD: IntegrationExecutionDetails.IntegrationExecutionState
    IN_PROCESS: IntegrationExecutionDetails.IntegrationExecutionState
    SUCCEEDED: IntegrationExecutionDetails.IntegrationExecutionState
    FAILED: IntegrationExecutionDetails.IntegrationExecutionState
    CANCELLED: IntegrationExecutionDetails.IntegrationExecutionState
    RETRY_ON_HOLD: IntegrationExecutionDetails.IntegrationExecutionState
    SUSPENDED: IntegrationExecutionDetails.IntegrationExecutionState
    INTEGRATION_EXECUTION_STATE_FIELD_NUMBER: _ClassVar[int]
    INTEGRATION_EXECUTION_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_ATTEMPT_STATS_FIELD_NUMBER: _ClassVar[int]
    NEXT_EXECUTION_TIME_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_RETRIES_COUNT_FIELD_NUMBER: _ClassVar[int]
    CANCEL_REASON_FIELD_NUMBER: _ClassVar[int]
    integration_execution_state: IntegrationExecutionDetails.IntegrationExecutionState
    integration_execution_snapshot: _containers.RepeatedCompositeFieldContainer[IntegrationExecutionSnapshot]
    execution_attempt_stats: _containers.RepeatedCompositeFieldContainer[AttemptStats]
    next_execution_time: _timestamp_pb2.Timestamp
    execution_retries_count: int
    cancel_reason: str
    def __init__(self, integration_execution_state: _Optional[_Union[IntegrationExecutionDetails.IntegrationExecutionState, str]] = ..., integration_execution_snapshot: _Optional[_Iterable[_Union[IntegrationExecutionSnapshot, _Mapping]]] = ..., execution_attempt_stats: _Optional[_Iterable[_Union[AttemptStats, _Mapping]]] = ..., next_execution_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., execution_retries_count: _Optional[int] = ..., cancel_reason: _Optional[str] = ...) -> None: ...

class IntegrationExecutionSnapshot(_message.Message):
    __slots__ = ("checkpoint_task_number", "snapshot_time", "integration_execution_snapshot_metadata", "task_execution_details", "condition_results", "execution_params")
    class IntegrationExecutionSnapshotMetadata(_message.Message):
        __slots__ = ("task_number", "task", "integration_execution_attempt_num", "task_attempt_num", "task_label", "ancestor_task_numbers", "ancestor_iteration_numbers", "integration")
        TASK_NUMBER_FIELD_NUMBER: _ClassVar[int]
        TASK_FIELD_NUMBER: _ClassVar[int]
        INTEGRATION_EXECUTION_ATTEMPT_NUM_FIELD_NUMBER: _ClassVar[int]
        TASK_ATTEMPT_NUM_FIELD_NUMBER: _ClassVar[int]
        TASK_LABEL_FIELD_NUMBER: _ClassVar[int]
        ANCESTOR_TASK_NUMBERS_FIELD_NUMBER: _ClassVar[int]
        ANCESTOR_ITERATION_NUMBERS_FIELD_NUMBER: _ClassVar[int]
        INTEGRATION_FIELD_NUMBER: _ClassVar[int]
        task_number: str
        task: str
        integration_execution_attempt_num: int
        task_attempt_num: int
        task_label: str
        ancestor_task_numbers: _containers.RepeatedScalarFieldContainer[str]
        ancestor_iteration_numbers: _containers.RepeatedScalarFieldContainer[str]
        integration: str
        def __init__(self, task_number: _Optional[str] = ..., task: _Optional[str] = ..., integration_execution_attempt_num: _Optional[int] = ..., task_attempt_num: _Optional[int] = ..., task_label: _Optional[str] = ..., ancestor_task_numbers: _Optional[_Iterable[str]] = ..., ancestor_iteration_numbers: _Optional[_Iterable[str]] = ..., integration: _Optional[str] = ...) -> None: ...
    class ExecutionParamsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _event_parameter_pb2.EventParameter
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_event_parameter_pb2.EventParameter, _Mapping]] = ...) -> None: ...
    CHECKPOINT_TASK_NUMBER_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_TIME_FIELD_NUMBER: _ClassVar[int]
    INTEGRATION_EXECUTION_SNAPSHOT_METADATA_FIELD_NUMBER: _ClassVar[int]
    TASK_EXECUTION_DETAILS_FIELD_NUMBER: _ClassVar[int]
    CONDITION_RESULTS_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_PARAMS_FIELD_NUMBER: _ClassVar[int]
    checkpoint_task_number: str
    snapshot_time: _timestamp_pb2.Timestamp
    integration_execution_snapshot_metadata: IntegrationExecutionSnapshot.IntegrationExecutionSnapshotMetadata
    task_execution_details: _containers.RepeatedCompositeFieldContainer[TaskExecutionDetails]
    condition_results: _containers.RepeatedCompositeFieldContainer[ConditionResult]
    execution_params: _containers.MessageMap[str, _event_parameter_pb2.EventParameter]
    def __init__(self, checkpoint_task_number: _Optional[str] = ..., snapshot_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., integration_execution_snapshot_metadata: _Optional[_Union[IntegrationExecutionSnapshot.IntegrationExecutionSnapshotMetadata, _Mapping]] = ..., task_execution_details: _Optional[_Iterable[_Union[TaskExecutionDetails, _Mapping]]] = ..., condition_results: _Optional[_Iterable[_Union[ConditionResult, _Mapping]]] = ..., execution_params: _Optional[_Mapping[str, _event_parameter_pb2.EventParameter]] = ...) -> None: ...

class TaskExecutionDetails(_message.Message):
    __slots__ = ("task_number", "task_execution_state", "task_attempt_stats")
    class TaskExecutionState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TASK_EXECUTION_STATE_UNSPECIFIED: _ClassVar[TaskExecutionDetails.TaskExecutionState]
        PENDING_EXECUTION: _ClassVar[TaskExecutionDetails.TaskExecutionState]
        IN_PROCESS: _ClassVar[TaskExecutionDetails.TaskExecutionState]
        SUCCEED: _ClassVar[TaskExecutionDetails.TaskExecutionState]
        FAILED: _ClassVar[TaskExecutionDetails.TaskExecutionState]
        FATAL: _ClassVar[TaskExecutionDetails.TaskExecutionState]
        RETRY_ON_HOLD: _ClassVar[TaskExecutionDetails.TaskExecutionState]
        SKIPPED: _ClassVar[TaskExecutionDetails.TaskExecutionState]
        CANCELLED: _ClassVar[TaskExecutionDetails.TaskExecutionState]
        PENDING_ROLLBACK: _ClassVar[TaskExecutionDetails.TaskExecutionState]
        ROLLBACK_IN_PROCESS: _ClassVar[TaskExecutionDetails.TaskExecutionState]
        ROLLEDBACK: _ClassVar[TaskExecutionDetails.TaskExecutionState]
        SUSPENDED: _ClassVar[TaskExecutionDetails.TaskExecutionState]
    TASK_EXECUTION_STATE_UNSPECIFIED: TaskExecutionDetails.TaskExecutionState
    PENDING_EXECUTION: TaskExecutionDetails.TaskExecutionState
    IN_PROCESS: TaskExecutionDetails.TaskExecutionState
    SUCCEED: TaskExecutionDetails.TaskExecutionState
    FAILED: TaskExecutionDetails.TaskExecutionState
    FATAL: TaskExecutionDetails.TaskExecutionState
    RETRY_ON_HOLD: TaskExecutionDetails.TaskExecutionState
    SKIPPED: TaskExecutionDetails.TaskExecutionState
    CANCELLED: TaskExecutionDetails.TaskExecutionState
    PENDING_ROLLBACK: TaskExecutionDetails.TaskExecutionState
    ROLLBACK_IN_PROCESS: TaskExecutionDetails.TaskExecutionState
    ROLLEDBACK: TaskExecutionDetails.TaskExecutionState
    SUSPENDED: TaskExecutionDetails.TaskExecutionState
    TASK_NUMBER_FIELD_NUMBER: _ClassVar[int]
    TASK_EXECUTION_STATE_FIELD_NUMBER: _ClassVar[int]
    TASK_ATTEMPT_STATS_FIELD_NUMBER: _ClassVar[int]
    task_number: str
    task_execution_state: TaskExecutionDetails.TaskExecutionState
    task_attempt_stats: _containers.RepeatedCompositeFieldContainer[AttemptStats]
    def __init__(self, task_number: _Optional[str] = ..., task_execution_state: _Optional[_Union[TaskExecutionDetails.TaskExecutionState, str]] = ..., task_attempt_stats: _Optional[_Iterable[_Union[AttemptStats, _Mapping]]] = ...) -> None: ...

class AttemptStats(_message.Message):
    __slots__ = ("start_time", "end_time")
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    def __init__(self, start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ErrorDetail(_message.Message):
    __slots__ = ("error_message", "task_number")
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TASK_NUMBER_FIELD_NUMBER: _ClassVar[int]
    error_message: str
    task_number: int
    def __init__(self, error_message: _Optional[str] = ..., task_number: _Optional[int] = ...) -> None: ...

class ConditionResult(_message.Message):
    __slots__ = ("current_task_number", "next_task_number", "result")
    CURRENT_TASK_NUMBER_FIELD_NUMBER: _ClassVar[int]
    NEXT_TASK_NUMBER_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    current_task_number: str
    next_task_number: str
    result: bool
    def __init__(self, current_task_number: _Optional[str] = ..., next_task_number: _Optional[str] = ..., result: bool = ...) -> None: ...
