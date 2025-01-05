from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.cloud.integrations.v1alpha import coordinate_pb2 as _coordinate_pb2
from google.cloud.integrations.v1alpha import event_parameter_pb2 as _event_parameter_pb2
from google.cloud.integrations.v1alpha import json_validation_pb2 as _json_validation_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class TaskConfig(_message.Message):
    __slots__ = ('task', 'task_id', 'parameters', 'failure_policy', 'synchronous_call_failure_policy', 'conditional_failure_policies', 'next_tasks', 'next_tasks_execution_policy', 'task_execution_strategy', 'display_name', 'success_policy', 'json_validation_option', 'description', 'task_template', 'error_catcher_id', 'external_task_type', 'position')

    class NextTasksExecutionPolicy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NEXT_TASKS_EXECUTION_POLICY_UNSPECIFIED: _ClassVar[TaskConfig.NextTasksExecutionPolicy]
        RUN_ALL_MATCH: _ClassVar[TaskConfig.NextTasksExecutionPolicy]
        RUN_FIRST_MATCH: _ClassVar[TaskConfig.NextTasksExecutionPolicy]
    NEXT_TASKS_EXECUTION_POLICY_UNSPECIFIED: TaskConfig.NextTasksExecutionPolicy
    RUN_ALL_MATCH: TaskConfig.NextTasksExecutionPolicy
    RUN_FIRST_MATCH: TaskConfig.NextTasksExecutionPolicy

    class TaskExecutionStrategy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TASK_EXECUTION_STRATEGY_UNSPECIFIED: _ClassVar[TaskConfig.TaskExecutionStrategy]
        WHEN_ALL_SUCCEED: _ClassVar[TaskConfig.TaskExecutionStrategy]
        WHEN_ANY_SUCCEED: _ClassVar[TaskConfig.TaskExecutionStrategy]
        WHEN_ALL_TASKS_AND_CONDITIONS_SUCCEED: _ClassVar[TaskConfig.TaskExecutionStrategy]
    TASK_EXECUTION_STRATEGY_UNSPECIFIED: TaskConfig.TaskExecutionStrategy
    WHEN_ALL_SUCCEED: TaskConfig.TaskExecutionStrategy
    WHEN_ANY_SUCCEED: TaskConfig.TaskExecutionStrategy
    WHEN_ALL_TASKS_AND_CONDITIONS_SUCCEED: TaskConfig.TaskExecutionStrategy

    class ExternalTaskType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        EXTERNAL_TASK_TYPE_UNSPECIFIED: _ClassVar[TaskConfig.ExternalTaskType]
        NORMAL_TASK: _ClassVar[TaskConfig.ExternalTaskType]
        ERROR_TASK: _ClassVar[TaskConfig.ExternalTaskType]
    EXTERNAL_TASK_TYPE_UNSPECIFIED: TaskConfig.ExternalTaskType
    NORMAL_TASK: TaskConfig.ExternalTaskType
    ERROR_TASK: TaskConfig.ExternalTaskType

    class ParametersEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _event_parameter_pb2.EventParameter

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[_event_parameter_pb2.EventParameter, _Mapping]]=...) -> None:
            ...
    TASK_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_POLICY_FIELD_NUMBER: _ClassVar[int]
    SYNCHRONOUS_CALL_FAILURE_POLICY_FIELD_NUMBER: _ClassVar[int]
    CONDITIONAL_FAILURE_POLICIES_FIELD_NUMBER: _ClassVar[int]
    NEXT_TASKS_FIELD_NUMBER: _ClassVar[int]
    NEXT_TASKS_EXECUTION_POLICY_FIELD_NUMBER: _ClassVar[int]
    TASK_EXECUTION_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_POLICY_FIELD_NUMBER: _ClassVar[int]
    JSON_VALIDATION_OPTION_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TASK_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    ERROR_CATCHER_ID_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_TASK_TYPE_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    task: str
    task_id: str
    parameters: _containers.MessageMap[str, _event_parameter_pb2.EventParameter]
    failure_policy: FailurePolicy
    synchronous_call_failure_policy: FailurePolicy
    conditional_failure_policies: ConditionalFailurePolicies
    next_tasks: _containers.RepeatedCompositeFieldContainer[NextTask]
    next_tasks_execution_policy: TaskConfig.NextTasksExecutionPolicy
    task_execution_strategy: TaskConfig.TaskExecutionStrategy
    display_name: str
    success_policy: SuccessPolicy
    json_validation_option: _json_validation_pb2.JsonValidationOption
    description: str
    task_template: str
    error_catcher_id: str
    external_task_type: TaskConfig.ExternalTaskType
    position: _coordinate_pb2.Coordinate

    def __init__(self, task: _Optional[str]=..., task_id: _Optional[str]=..., parameters: _Optional[_Mapping[str, _event_parameter_pb2.EventParameter]]=..., failure_policy: _Optional[_Union[FailurePolicy, _Mapping]]=..., synchronous_call_failure_policy: _Optional[_Union[FailurePolicy, _Mapping]]=..., conditional_failure_policies: _Optional[_Union[ConditionalFailurePolicies, _Mapping]]=..., next_tasks: _Optional[_Iterable[_Union[NextTask, _Mapping]]]=..., next_tasks_execution_policy: _Optional[_Union[TaskConfig.NextTasksExecutionPolicy, str]]=..., task_execution_strategy: _Optional[_Union[TaskConfig.TaskExecutionStrategy, str]]=..., display_name: _Optional[str]=..., success_policy: _Optional[_Union[SuccessPolicy, _Mapping]]=..., json_validation_option: _Optional[_Union[_json_validation_pb2.JsonValidationOption, str]]=..., description: _Optional[str]=..., task_template: _Optional[str]=..., error_catcher_id: _Optional[str]=..., external_task_type: _Optional[_Union[TaskConfig.ExternalTaskType, str]]=..., position: _Optional[_Union[_coordinate_pb2.Coordinate, _Mapping]]=...) -> None:
        ...

class SuccessPolicy(_message.Message):
    __slots__ = ('final_state',)

    class FinalState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FINAL_STATE_UNSPECIFIED: _ClassVar[SuccessPolicy.FinalState]
        SUCCEEDED: _ClassVar[SuccessPolicy.FinalState]
        SUSPENDED: _ClassVar[SuccessPolicy.FinalState]
    FINAL_STATE_UNSPECIFIED: SuccessPolicy.FinalState
    SUCCEEDED: SuccessPolicy.FinalState
    SUSPENDED: SuccessPolicy.FinalState
    FINAL_STATE_FIELD_NUMBER: _ClassVar[int]
    final_state: SuccessPolicy.FinalState

    def __init__(self, final_state: _Optional[_Union[SuccessPolicy.FinalState, str]]=...) -> None:
        ...

class FailurePolicy(_message.Message):
    __slots__ = ('retry_strategy', 'max_retries', 'interval_time', 'condition')

    class RetryStrategy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RETRY_STRATEGY_UNSPECIFIED: _ClassVar[FailurePolicy.RetryStrategy]
        IGNORE: _ClassVar[FailurePolicy.RetryStrategy]
        NONE: _ClassVar[FailurePolicy.RetryStrategy]
        FATAL: _ClassVar[FailurePolicy.RetryStrategy]
        FIXED_INTERVAL: _ClassVar[FailurePolicy.RetryStrategy]
        LINEAR_BACKOFF: _ClassVar[FailurePolicy.RetryStrategy]
        EXPONENTIAL_BACKOFF: _ClassVar[FailurePolicy.RetryStrategy]
        RESTART_INTEGRATION_WITH_BACKOFF: _ClassVar[FailurePolicy.RetryStrategy]
    RETRY_STRATEGY_UNSPECIFIED: FailurePolicy.RetryStrategy
    IGNORE: FailurePolicy.RetryStrategy
    NONE: FailurePolicy.RetryStrategy
    FATAL: FailurePolicy.RetryStrategy
    FIXED_INTERVAL: FailurePolicy.RetryStrategy
    LINEAR_BACKOFF: FailurePolicy.RetryStrategy
    EXPONENTIAL_BACKOFF: FailurePolicy.RetryStrategy
    RESTART_INTEGRATION_WITH_BACKOFF: FailurePolicy.RetryStrategy
    RETRY_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    MAX_RETRIES_FIELD_NUMBER: _ClassVar[int]
    INTERVAL_TIME_FIELD_NUMBER: _ClassVar[int]
    CONDITION_FIELD_NUMBER: _ClassVar[int]
    retry_strategy: FailurePolicy.RetryStrategy
    max_retries: int
    interval_time: _timestamp_pb2.Timestamp
    condition: str

    def __init__(self, retry_strategy: _Optional[_Union[FailurePolicy.RetryStrategy, str]]=..., max_retries: _Optional[int]=..., interval_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., condition: _Optional[str]=...) -> None:
        ...

class NextTask(_message.Message):
    __slots__ = ('task_config_id', 'task_id', 'condition', 'display_name', 'description')
    TASK_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    CONDITION_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    task_config_id: str
    task_id: str
    condition: str
    display_name: str
    description: str

    def __init__(self, task_config_id: _Optional[str]=..., task_id: _Optional[str]=..., condition: _Optional[str]=..., display_name: _Optional[str]=..., description: _Optional[str]=...) -> None:
        ...

class ConditionalFailurePolicies(_message.Message):
    __slots__ = ('failure_policies', 'default_failure_policy')
    FAILURE_POLICIES_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_FAILURE_POLICY_FIELD_NUMBER: _ClassVar[int]
    failure_policies: _containers.RepeatedCompositeFieldContainer[FailurePolicy]
    default_failure_policy: FailurePolicy

    def __init__(self, failure_policies: _Optional[_Iterable[_Union[FailurePolicy, _Mapping]]]=..., default_failure_policy: _Optional[_Union[FailurePolicy, _Mapping]]=...) -> None:
        ...