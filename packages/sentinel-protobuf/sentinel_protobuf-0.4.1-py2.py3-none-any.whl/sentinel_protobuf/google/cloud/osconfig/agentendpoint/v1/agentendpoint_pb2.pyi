from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.cloud.osconfig.agentendpoint.v1 import inventory_pb2 as _inventory_pb2
from google.cloud.osconfig.agentendpoint.v1 import tasks_pb2 as _tasks_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ReceiveTaskNotificationRequest(_message.Message):
    __slots__ = ('instance_id_token', 'agent_version')
    INSTANCE_ID_TOKEN_FIELD_NUMBER: _ClassVar[int]
    AGENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    instance_id_token: str
    agent_version: str

    def __init__(self, instance_id_token: _Optional[str]=..., agent_version: _Optional[str]=...) -> None:
        ...

class ReceiveTaskNotificationResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class StartNextTaskRequest(_message.Message):
    __slots__ = ('instance_id_token',)
    INSTANCE_ID_TOKEN_FIELD_NUMBER: _ClassVar[int]
    instance_id_token: str

    def __init__(self, instance_id_token: _Optional[str]=...) -> None:
        ...

class StartNextTaskResponse(_message.Message):
    __slots__ = ('task',)
    TASK_FIELD_NUMBER: _ClassVar[int]
    task: _tasks_pb2.Task

    def __init__(self, task: _Optional[_Union[_tasks_pb2.Task, _Mapping]]=...) -> None:
        ...

class ReportTaskProgressRequest(_message.Message):
    __slots__ = ('instance_id_token', 'task_id', 'task_type', 'apply_patches_task_progress', 'exec_step_task_progress', 'apply_config_task_progress')
    INSTANCE_ID_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    TASK_TYPE_FIELD_NUMBER: _ClassVar[int]
    APPLY_PATCHES_TASK_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    EXEC_STEP_TASK_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    APPLY_CONFIG_TASK_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    instance_id_token: str
    task_id: str
    task_type: _tasks_pb2.TaskType
    apply_patches_task_progress: _tasks_pb2.ApplyPatchesTaskProgress
    exec_step_task_progress: _tasks_pb2.ExecStepTaskProgress
    apply_config_task_progress: _tasks_pb2.ApplyConfigTaskProgress

    def __init__(self, instance_id_token: _Optional[str]=..., task_id: _Optional[str]=..., task_type: _Optional[_Union[_tasks_pb2.TaskType, str]]=..., apply_patches_task_progress: _Optional[_Union[_tasks_pb2.ApplyPatchesTaskProgress, _Mapping]]=..., exec_step_task_progress: _Optional[_Union[_tasks_pb2.ExecStepTaskProgress, _Mapping]]=..., apply_config_task_progress: _Optional[_Union[_tasks_pb2.ApplyConfigTaskProgress, _Mapping]]=...) -> None:
        ...

class ReportTaskProgressResponse(_message.Message):
    __slots__ = ('task_directive',)
    TASK_DIRECTIVE_FIELD_NUMBER: _ClassVar[int]
    task_directive: _tasks_pb2.TaskDirective

    def __init__(self, task_directive: _Optional[_Union[_tasks_pb2.TaskDirective, str]]=...) -> None:
        ...

class ReportTaskCompleteRequest(_message.Message):
    __slots__ = ('instance_id_token', 'task_id', 'task_type', 'error_message', 'apply_patches_task_output', 'exec_step_task_output', 'apply_config_task_output')
    INSTANCE_ID_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    TASK_TYPE_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    APPLY_PATCHES_TASK_OUTPUT_FIELD_NUMBER: _ClassVar[int]
    EXEC_STEP_TASK_OUTPUT_FIELD_NUMBER: _ClassVar[int]
    APPLY_CONFIG_TASK_OUTPUT_FIELD_NUMBER: _ClassVar[int]
    instance_id_token: str
    task_id: str
    task_type: _tasks_pb2.TaskType
    error_message: str
    apply_patches_task_output: _tasks_pb2.ApplyPatchesTaskOutput
    exec_step_task_output: _tasks_pb2.ExecStepTaskOutput
    apply_config_task_output: _tasks_pb2.ApplyConfigTaskOutput

    def __init__(self, instance_id_token: _Optional[str]=..., task_id: _Optional[str]=..., task_type: _Optional[_Union[_tasks_pb2.TaskType, str]]=..., error_message: _Optional[str]=..., apply_patches_task_output: _Optional[_Union[_tasks_pb2.ApplyPatchesTaskOutput, _Mapping]]=..., exec_step_task_output: _Optional[_Union[_tasks_pb2.ExecStepTaskOutput, _Mapping]]=..., apply_config_task_output: _Optional[_Union[_tasks_pb2.ApplyConfigTaskOutput, _Mapping]]=...) -> None:
        ...

class ReportTaskCompleteResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class RegisterAgentRequest(_message.Message):
    __slots__ = ('instance_id_token', 'agent_version', 'supported_capabilities', 'os_long_name', 'os_short_name', 'os_version', 'os_architecture')
    INSTANCE_ID_TOKEN_FIELD_NUMBER: _ClassVar[int]
    AGENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    OS_LONG_NAME_FIELD_NUMBER: _ClassVar[int]
    OS_SHORT_NAME_FIELD_NUMBER: _ClassVar[int]
    OS_VERSION_FIELD_NUMBER: _ClassVar[int]
    OS_ARCHITECTURE_FIELD_NUMBER: _ClassVar[int]
    instance_id_token: str
    agent_version: str
    supported_capabilities: _containers.RepeatedScalarFieldContainer[str]
    os_long_name: str
    os_short_name: str
    os_version: str
    os_architecture: str

    def __init__(self, instance_id_token: _Optional[str]=..., agent_version: _Optional[str]=..., supported_capabilities: _Optional[_Iterable[str]]=..., os_long_name: _Optional[str]=..., os_short_name: _Optional[str]=..., os_version: _Optional[str]=..., os_architecture: _Optional[str]=...) -> None:
        ...

class RegisterAgentResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class ReportInventoryRequest(_message.Message):
    __slots__ = ('instance_id_token', 'inventory_checksum', 'inventory')
    INSTANCE_ID_TOKEN_FIELD_NUMBER: _ClassVar[int]
    INVENTORY_CHECKSUM_FIELD_NUMBER: _ClassVar[int]
    INVENTORY_FIELD_NUMBER: _ClassVar[int]
    instance_id_token: str
    inventory_checksum: str
    inventory: _inventory_pb2.Inventory

    def __init__(self, instance_id_token: _Optional[str]=..., inventory_checksum: _Optional[str]=..., inventory: _Optional[_Union[_inventory_pb2.Inventory, _Mapping]]=...) -> None:
        ...

class ReportInventoryResponse(_message.Message):
    __slots__ = ('report_full_inventory',)
    REPORT_FULL_INVENTORY_FIELD_NUMBER: _ClassVar[int]
    report_full_inventory: bool

    def __init__(self, report_full_inventory: bool=...) -> None:
        ...