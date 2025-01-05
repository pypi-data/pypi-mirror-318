from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.cloud.osconfig.agentendpoint.v1beta import patch_jobs_pb2 as _patch_jobs_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class TaskDirective(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TASK_DIRECTIVE_UNSPECIFIED: _ClassVar[TaskDirective]
    CONTINUE: _ClassVar[TaskDirective]
    STOP: _ClassVar[TaskDirective]

class TaskType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TASK_TYPE_UNSPECIFIED: _ClassVar[TaskType]
    APPLY_PATCHES: _ClassVar[TaskType]
    EXEC_STEP_TASK: _ClassVar[TaskType]
TASK_DIRECTIVE_UNSPECIFIED: TaskDirective
CONTINUE: TaskDirective
STOP: TaskDirective
TASK_TYPE_UNSPECIFIED: TaskType
APPLY_PATCHES: TaskType
EXEC_STEP_TASK: TaskType

class Task(_message.Message):
    __slots__ = ('task_id', 'task_type', 'task_directive', 'apply_patches_task', 'exec_step_task', 'service_labels')

    class ServiceLabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    TASK_TYPE_FIELD_NUMBER: _ClassVar[int]
    TASK_DIRECTIVE_FIELD_NUMBER: _ClassVar[int]
    APPLY_PATCHES_TASK_FIELD_NUMBER: _ClassVar[int]
    EXEC_STEP_TASK_FIELD_NUMBER: _ClassVar[int]
    SERVICE_LABELS_FIELD_NUMBER: _ClassVar[int]
    task_id: str
    task_type: TaskType
    task_directive: TaskDirective
    apply_patches_task: ApplyPatchesTask
    exec_step_task: ExecStepTask
    service_labels: _containers.ScalarMap[str, str]

    def __init__(self, task_id: _Optional[str]=..., task_type: _Optional[_Union[TaskType, str]]=..., task_directive: _Optional[_Union[TaskDirective, str]]=..., apply_patches_task: _Optional[_Union[ApplyPatchesTask, _Mapping]]=..., exec_step_task: _Optional[_Union[ExecStepTask, _Mapping]]=..., service_labels: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class ApplyPatchesTask(_message.Message):
    __slots__ = ('patch_config', 'dry_run')
    PATCH_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DRY_RUN_FIELD_NUMBER: _ClassVar[int]
    patch_config: _patch_jobs_pb2.PatchConfig
    dry_run: bool

    def __init__(self, patch_config: _Optional[_Union[_patch_jobs_pb2.PatchConfig, _Mapping]]=..., dry_run: bool=...) -> None:
        ...

class ApplyPatchesTaskProgress(_message.Message):
    __slots__ = ('state',)

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[ApplyPatchesTaskProgress.State]
        STARTED: _ClassVar[ApplyPatchesTaskProgress.State]
        DOWNLOADING_PATCHES: _ClassVar[ApplyPatchesTaskProgress.State]
        APPLYING_PATCHES: _ClassVar[ApplyPatchesTaskProgress.State]
        REBOOTING: _ClassVar[ApplyPatchesTaskProgress.State]
    STATE_UNSPECIFIED: ApplyPatchesTaskProgress.State
    STARTED: ApplyPatchesTaskProgress.State
    DOWNLOADING_PATCHES: ApplyPatchesTaskProgress.State
    APPLYING_PATCHES: ApplyPatchesTaskProgress.State
    REBOOTING: ApplyPatchesTaskProgress.State
    STATE_FIELD_NUMBER: _ClassVar[int]
    state: ApplyPatchesTaskProgress.State

    def __init__(self, state: _Optional[_Union[ApplyPatchesTaskProgress.State, str]]=...) -> None:
        ...

class ApplyPatchesTaskOutput(_message.Message):
    __slots__ = ('state',)

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[ApplyPatchesTaskOutput.State]
        SUCCEEDED: _ClassVar[ApplyPatchesTaskOutput.State]
        SUCCEEDED_REBOOT_REQUIRED: _ClassVar[ApplyPatchesTaskOutput.State]
        FAILED: _ClassVar[ApplyPatchesTaskOutput.State]
    STATE_UNSPECIFIED: ApplyPatchesTaskOutput.State
    SUCCEEDED: ApplyPatchesTaskOutput.State
    SUCCEEDED_REBOOT_REQUIRED: ApplyPatchesTaskOutput.State
    FAILED: ApplyPatchesTaskOutput.State
    STATE_FIELD_NUMBER: _ClassVar[int]
    state: ApplyPatchesTaskOutput.State

    def __init__(self, state: _Optional[_Union[ApplyPatchesTaskOutput.State, str]]=...) -> None:
        ...

class ExecStepTask(_message.Message):
    __slots__ = ('exec_step',)
    EXEC_STEP_FIELD_NUMBER: _ClassVar[int]
    exec_step: _patch_jobs_pb2.ExecStep

    def __init__(self, exec_step: _Optional[_Union[_patch_jobs_pb2.ExecStep, _Mapping]]=...) -> None:
        ...

class ExecStepTaskProgress(_message.Message):
    __slots__ = ('state',)

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[ExecStepTaskProgress.State]
        STARTED: _ClassVar[ExecStepTaskProgress.State]
    STATE_UNSPECIFIED: ExecStepTaskProgress.State
    STARTED: ExecStepTaskProgress.State
    STATE_FIELD_NUMBER: _ClassVar[int]
    state: ExecStepTaskProgress.State

    def __init__(self, state: _Optional[_Union[ExecStepTaskProgress.State, str]]=...) -> None:
        ...

class ExecStepTaskOutput(_message.Message):
    __slots__ = ('state', 'exit_code')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[ExecStepTaskOutput.State]
        COMPLETED: _ClassVar[ExecStepTaskOutput.State]
        TIMED_OUT: _ClassVar[ExecStepTaskOutput.State]
        CANCELLED: _ClassVar[ExecStepTaskOutput.State]
    STATE_UNSPECIFIED: ExecStepTaskOutput.State
    COMPLETED: ExecStepTaskOutput.State
    TIMED_OUT: ExecStepTaskOutput.State
    CANCELLED: ExecStepTaskOutput.State
    STATE_FIELD_NUMBER: _ClassVar[int]
    EXIT_CODE_FIELD_NUMBER: _ClassVar[int]
    state: ExecStepTaskOutput.State
    exit_code: int

    def __init__(self, state: _Optional[_Union[ExecStepTaskOutput.State, str]]=..., exit_code: _Optional[int]=...) -> None:
        ...