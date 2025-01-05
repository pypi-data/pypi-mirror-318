from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.batch.v1 import volume_pb2 as _volume_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ComputeResource(_message.Message):
    __slots__ = ('cpu_milli', 'memory_mib', 'boot_disk_mib')
    CPU_MILLI_FIELD_NUMBER: _ClassVar[int]
    MEMORY_MIB_FIELD_NUMBER: _ClassVar[int]
    BOOT_DISK_MIB_FIELD_NUMBER: _ClassVar[int]
    cpu_milli: int
    memory_mib: int
    boot_disk_mib: int

    def __init__(self, cpu_milli: _Optional[int]=..., memory_mib: _Optional[int]=..., boot_disk_mib: _Optional[int]=...) -> None:
        ...

class StatusEvent(_message.Message):
    __slots__ = ('type', 'description', 'event_time', 'task_execution', 'task_state')
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    EVENT_TIME_FIELD_NUMBER: _ClassVar[int]
    TASK_EXECUTION_FIELD_NUMBER: _ClassVar[int]
    TASK_STATE_FIELD_NUMBER: _ClassVar[int]
    type: str
    description: str
    event_time: _timestamp_pb2.Timestamp
    task_execution: TaskExecution
    task_state: TaskStatus.State

    def __init__(self, type: _Optional[str]=..., description: _Optional[str]=..., event_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., task_execution: _Optional[_Union[TaskExecution, _Mapping]]=..., task_state: _Optional[_Union[TaskStatus.State, str]]=...) -> None:
        ...

class TaskExecution(_message.Message):
    __slots__ = ('exit_code',)
    EXIT_CODE_FIELD_NUMBER: _ClassVar[int]
    exit_code: int

    def __init__(self, exit_code: _Optional[int]=...) -> None:
        ...

class TaskStatus(_message.Message):
    __slots__ = ('state', 'status_events')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[TaskStatus.State]
        PENDING: _ClassVar[TaskStatus.State]
        ASSIGNED: _ClassVar[TaskStatus.State]
        RUNNING: _ClassVar[TaskStatus.State]
        FAILED: _ClassVar[TaskStatus.State]
        SUCCEEDED: _ClassVar[TaskStatus.State]
        UNEXECUTED: _ClassVar[TaskStatus.State]
    STATE_UNSPECIFIED: TaskStatus.State
    PENDING: TaskStatus.State
    ASSIGNED: TaskStatus.State
    RUNNING: TaskStatus.State
    FAILED: TaskStatus.State
    SUCCEEDED: TaskStatus.State
    UNEXECUTED: TaskStatus.State
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATUS_EVENTS_FIELD_NUMBER: _ClassVar[int]
    state: TaskStatus.State
    status_events: _containers.RepeatedCompositeFieldContainer[StatusEvent]

    def __init__(self, state: _Optional[_Union[TaskStatus.State, str]]=..., status_events: _Optional[_Iterable[_Union[StatusEvent, _Mapping]]]=...) -> None:
        ...

class Runnable(_message.Message):
    __slots__ = ('container', 'script', 'barrier', 'display_name', 'ignore_exit_status', 'background', 'always_run', 'environment', 'timeout', 'labels')

    class Container(_message.Message):
        __slots__ = ('image_uri', 'commands', 'entrypoint', 'volumes', 'options', 'block_external_network', 'username', 'password', 'enable_image_streaming')
        IMAGE_URI_FIELD_NUMBER: _ClassVar[int]
        COMMANDS_FIELD_NUMBER: _ClassVar[int]
        ENTRYPOINT_FIELD_NUMBER: _ClassVar[int]
        VOLUMES_FIELD_NUMBER: _ClassVar[int]
        OPTIONS_FIELD_NUMBER: _ClassVar[int]
        BLOCK_EXTERNAL_NETWORK_FIELD_NUMBER: _ClassVar[int]
        USERNAME_FIELD_NUMBER: _ClassVar[int]
        PASSWORD_FIELD_NUMBER: _ClassVar[int]
        ENABLE_IMAGE_STREAMING_FIELD_NUMBER: _ClassVar[int]
        image_uri: str
        commands: _containers.RepeatedScalarFieldContainer[str]
        entrypoint: str
        volumes: _containers.RepeatedScalarFieldContainer[str]
        options: str
        block_external_network: bool
        username: str
        password: str
        enable_image_streaming: bool

        def __init__(self, image_uri: _Optional[str]=..., commands: _Optional[_Iterable[str]]=..., entrypoint: _Optional[str]=..., volumes: _Optional[_Iterable[str]]=..., options: _Optional[str]=..., block_external_network: bool=..., username: _Optional[str]=..., password: _Optional[str]=..., enable_image_streaming: bool=...) -> None:
            ...

    class Script(_message.Message):
        __slots__ = ('path', 'text')
        PATH_FIELD_NUMBER: _ClassVar[int]
        TEXT_FIELD_NUMBER: _ClassVar[int]
        path: str
        text: str

        def __init__(self, path: _Optional[str]=..., text: _Optional[str]=...) -> None:
            ...

    class Barrier(_message.Message):
        __slots__ = ('name',)
        NAME_FIELD_NUMBER: _ClassVar[int]
        name: str

        def __init__(self, name: _Optional[str]=...) -> None:
            ...

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    CONTAINER_FIELD_NUMBER: _ClassVar[int]
    SCRIPT_FIELD_NUMBER: _ClassVar[int]
    BARRIER_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    IGNORE_EXIT_STATUS_FIELD_NUMBER: _ClassVar[int]
    BACKGROUND_FIELD_NUMBER: _ClassVar[int]
    ALWAYS_RUN_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    container: Runnable.Container
    script: Runnable.Script
    barrier: Runnable.Barrier
    display_name: str
    ignore_exit_status: bool
    background: bool
    always_run: bool
    environment: Environment
    timeout: _duration_pb2.Duration
    labels: _containers.ScalarMap[str, str]

    def __init__(self, container: _Optional[_Union[Runnable.Container, _Mapping]]=..., script: _Optional[_Union[Runnable.Script, _Mapping]]=..., barrier: _Optional[_Union[Runnable.Barrier, _Mapping]]=..., display_name: _Optional[str]=..., ignore_exit_status: bool=..., background: bool=..., always_run: bool=..., environment: _Optional[_Union[Environment, _Mapping]]=..., timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class TaskSpec(_message.Message):
    __slots__ = ('runnables', 'compute_resource', 'max_run_duration', 'max_retry_count', 'lifecycle_policies', 'environments', 'volumes', 'environment')

    class EnvironmentsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    RUNNABLES_FIELD_NUMBER: _ClassVar[int]
    COMPUTE_RESOURCE_FIELD_NUMBER: _ClassVar[int]
    MAX_RUN_DURATION_FIELD_NUMBER: _ClassVar[int]
    MAX_RETRY_COUNT_FIELD_NUMBER: _ClassVar[int]
    LIFECYCLE_POLICIES_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENTS_FIELD_NUMBER: _ClassVar[int]
    VOLUMES_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    runnables: _containers.RepeatedCompositeFieldContainer[Runnable]
    compute_resource: ComputeResource
    max_run_duration: _duration_pb2.Duration
    max_retry_count: int
    lifecycle_policies: _containers.RepeatedCompositeFieldContainer[LifecyclePolicy]
    environments: _containers.ScalarMap[str, str]
    volumes: _containers.RepeatedCompositeFieldContainer[_volume_pb2.Volume]
    environment: Environment

    def __init__(self, runnables: _Optional[_Iterable[_Union[Runnable, _Mapping]]]=..., compute_resource: _Optional[_Union[ComputeResource, _Mapping]]=..., max_run_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., max_retry_count: _Optional[int]=..., lifecycle_policies: _Optional[_Iterable[_Union[LifecyclePolicy, _Mapping]]]=..., environments: _Optional[_Mapping[str, str]]=..., volumes: _Optional[_Iterable[_Union[_volume_pb2.Volume, _Mapping]]]=..., environment: _Optional[_Union[Environment, _Mapping]]=...) -> None:
        ...

class LifecyclePolicy(_message.Message):
    __slots__ = ('action', 'action_condition')

    class Action(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ACTION_UNSPECIFIED: _ClassVar[LifecyclePolicy.Action]
        RETRY_TASK: _ClassVar[LifecyclePolicy.Action]
        FAIL_TASK: _ClassVar[LifecyclePolicy.Action]
    ACTION_UNSPECIFIED: LifecyclePolicy.Action
    RETRY_TASK: LifecyclePolicy.Action
    FAIL_TASK: LifecyclePolicy.Action

    class ActionCondition(_message.Message):
        __slots__ = ('exit_codes',)
        EXIT_CODES_FIELD_NUMBER: _ClassVar[int]
        exit_codes: _containers.RepeatedScalarFieldContainer[int]

        def __init__(self, exit_codes: _Optional[_Iterable[int]]=...) -> None:
            ...
    ACTION_FIELD_NUMBER: _ClassVar[int]
    ACTION_CONDITION_FIELD_NUMBER: _ClassVar[int]
    action: LifecyclePolicy.Action
    action_condition: LifecyclePolicy.ActionCondition

    def __init__(self, action: _Optional[_Union[LifecyclePolicy.Action, str]]=..., action_condition: _Optional[_Union[LifecyclePolicy.ActionCondition, _Mapping]]=...) -> None:
        ...

class Task(_message.Message):
    __slots__ = ('name', 'status')
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    name: str
    status: TaskStatus

    def __init__(self, name: _Optional[str]=..., status: _Optional[_Union[TaskStatus, _Mapping]]=...) -> None:
        ...

class Environment(_message.Message):
    __slots__ = ('variables', 'secret_variables', 'encrypted_variables')

    class KMSEnvMap(_message.Message):
        __slots__ = ('key_name', 'cipher_text')
        KEY_NAME_FIELD_NUMBER: _ClassVar[int]
        CIPHER_TEXT_FIELD_NUMBER: _ClassVar[int]
        key_name: str
        cipher_text: str

        def __init__(self, key_name: _Optional[str]=..., cipher_text: _Optional[str]=...) -> None:
            ...

    class VariablesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...

    class SecretVariablesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    VARIABLES_FIELD_NUMBER: _ClassVar[int]
    SECRET_VARIABLES_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTED_VARIABLES_FIELD_NUMBER: _ClassVar[int]
    variables: _containers.ScalarMap[str, str]
    secret_variables: _containers.ScalarMap[str, str]
    encrypted_variables: Environment.KMSEnvMap

    def __init__(self, variables: _Optional[_Mapping[str, str]]=..., secret_variables: _Optional[_Mapping[str, str]]=..., encrypted_variables: _Optional[_Union[Environment.KMSEnvMap, _Mapping]]=...) -> None:
        ...