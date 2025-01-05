from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.notebooks.v1 import diagnostic_config_pb2 as _diagnostic_config_pb2
from google.cloud.notebooks.v1 import environment_pb2 as _environment_pb2
from google.cloud.notebooks.v1 import execution_pb2 as _execution_pb2
from google.cloud.notebooks.v1 import instance_pb2 as _instance_pb2
from google.cloud.notebooks.v1 import instance_config_pb2 as _instance_config_pb2
from google.cloud.notebooks.v1 import schedule_pb2 as _schedule_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class UpgradeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UPGRADE_TYPE_UNSPECIFIED: _ClassVar[UpgradeType]
    UPGRADE_FRAMEWORK: _ClassVar[UpgradeType]
    UPGRADE_OS: _ClassVar[UpgradeType]
    UPGRADE_CUDA: _ClassVar[UpgradeType]
    UPGRADE_ALL: _ClassVar[UpgradeType]
UPGRADE_TYPE_UNSPECIFIED: UpgradeType
UPGRADE_FRAMEWORK: UpgradeType
UPGRADE_OS: UpgradeType
UPGRADE_CUDA: UpgradeType
UPGRADE_ALL: UpgradeType

class OperationMetadata(_message.Message):
    __slots__ = ('create_time', 'end_time', 'target', 'verb', 'status_message', 'requested_cancellation', 'api_version', 'endpoint')
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    VERB_FIELD_NUMBER: _ClassVar[int]
    STATUS_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_CANCELLATION_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    target: str
    verb: str
    status_message: str
    requested_cancellation: bool
    api_version: str
    endpoint: str

    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., target: _Optional[str]=..., verb: _Optional[str]=..., status_message: _Optional[str]=..., requested_cancellation: bool=..., api_version: _Optional[str]=..., endpoint: _Optional[str]=...) -> None:
        ...

class ListInstancesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListInstancesResponse(_message.Message):
    __slots__ = ('instances', 'next_page_token', 'unreachable')
    INSTANCES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    instances: _containers.RepeatedCompositeFieldContainer[_instance_pb2.Instance]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, instances: _Optional[_Iterable[_Union[_instance_pb2.Instance, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetInstanceRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateInstanceRequest(_message.Message):
    __slots__ = ('parent', 'instance_id', 'instance')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    instance_id: str
    instance: _instance_pb2.Instance

    def __init__(self, parent: _Optional[str]=..., instance_id: _Optional[str]=..., instance: _Optional[_Union[_instance_pb2.Instance, _Mapping]]=...) -> None:
        ...

class RegisterInstanceRequest(_message.Message):
    __slots__ = ('parent', 'instance_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    instance_id: str

    def __init__(self, parent: _Optional[str]=..., instance_id: _Optional[str]=...) -> None:
        ...

class SetInstanceAcceleratorRequest(_message.Message):
    __slots__ = ('name', 'type', 'core_count')
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CORE_COUNT_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: _instance_pb2.Instance.AcceleratorType
    core_count: int

    def __init__(self, name: _Optional[str]=..., type: _Optional[_Union[_instance_pb2.Instance.AcceleratorType, str]]=..., core_count: _Optional[int]=...) -> None:
        ...

class SetInstanceMachineTypeRequest(_message.Message):
    __slots__ = ('name', 'machine_type')
    NAME_FIELD_NUMBER: _ClassVar[int]
    MACHINE_TYPE_FIELD_NUMBER: _ClassVar[int]
    name: str
    machine_type: str

    def __init__(self, name: _Optional[str]=..., machine_type: _Optional[str]=...) -> None:
        ...

class UpdateInstanceConfigRequest(_message.Message):
    __slots__ = ('name', 'config')
    NAME_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    name: str
    config: _instance_config_pb2.InstanceConfig

    def __init__(self, name: _Optional[str]=..., config: _Optional[_Union[_instance_config_pb2.InstanceConfig, _Mapping]]=...) -> None:
        ...

class SetInstanceLabelsRequest(_message.Message):
    __slots__ = ('name', 'labels')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    name: str
    labels: _containers.ScalarMap[str, str]

    def __init__(self, name: _Optional[str]=..., labels: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class UpdateInstanceMetadataItemsRequest(_message.Message):
    __slots__ = ('name', 'items')

    class ItemsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    name: str
    items: _containers.ScalarMap[str, str]

    def __init__(self, name: _Optional[str]=..., items: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class UpdateInstanceMetadataItemsResponse(_message.Message):
    __slots__ = ('items',)

    class ItemsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.ScalarMap[str, str]

    def __init__(self, items: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class UpdateShieldedInstanceConfigRequest(_message.Message):
    __slots__ = ('name', 'shielded_instance_config')
    NAME_FIELD_NUMBER: _ClassVar[int]
    SHIELDED_INSTANCE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    name: str
    shielded_instance_config: _instance_pb2.Instance.ShieldedInstanceConfig

    def __init__(self, name: _Optional[str]=..., shielded_instance_config: _Optional[_Union[_instance_pb2.Instance.ShieldedInstanceConfig, _Mapping]]=...) -> None:
        ...

class DeleteInstanceRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class StartInstanceRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class StopInstanceRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ResetInstanceRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ReportInstanceInfoRequest(_message.Message):
    __slots__ = ('name', 'vm_id', 'metadata')

    class MetadataEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    VM_ID_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    name: str
    vm_id: str
    metadata: _containers.ScalarMap[str, str]

    def __init__(self, name: _Optional[str]=..., vm_id: _Optional[str]=..., metadata: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class IsInstanceUpgradeableRequest(_message.Message):
    __slots__ = ('notebook_instance', 'type')
    NOTEBOOK_INSTANCE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    notebook_instance: str
    type: UpgradeType

    def __init__(self, notebook_instance: _Optional[str]=..., type: _Optional[_Union[UpgradeType, str]]=...) -> None:
        ...

class IsInstanceUpgradeableResponse(_message.Message):
    __slots__ = ('upgradeable', 'upgrade_version', 'upgrade_info', 'upgrade_image')
    UPGRADEABLE_FIELD_NUMBER: _ClassVar[int]
    UPGRADE_VERSION_FIELD_NUMBER: _ClassVar[int]
    UPGRADE_INFO_FIELD_NUMBER: _ClassVar[int]
    UPGRADE_IMAGE_FIELD_NUMBER: _ClassVar[int]
    upgradeable: bool
    upgrade_version: str
    upgrade_info: str
    upgrade_image: str

    def __init__(self, upgradeable: bool=..., upgrade_version: _Optional[str]=..., upgrade_info: _Optional[str]=..., upgrade_image: _Optional[str]=...) -> None:
        ...

class GetInstanceHealthRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class GetInstanceHealthResponse(_message.Message):
    __slots__ = ('health_state', 'health_info')

    class HealthState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        HEALTH_STATE_UNSPECIFIED: _ClassVar[GetInstanceHealthResponse.HealthState]
        HEALTHY: _ClassVar[GetInstanceHealthResponse.HealthState]
        UNHEALTHY: _ClassVar[GetInstanceHealthResponse.HealthState]
        AGENT_NOT_INSTALLED: _ClassVar[GetInstanceHealthResponse.HealthState]
        AGENT_NOT_RUNNING: _ClassVar[GetInstanceHealthResponse.HealthState]
    HEALTH_STATE_UNSPECIFIED: GetInstanceHealthResponse.HealthState
    HEALTHY: GetInstanceHealthResponse.HealthState
    UNHEALTHY: GetInstanceHealthResponse.HealthState
    AGENT_NOT_INSTALLED: GetInstanceHealthResponse.HealthState
    AGENT_NOT_RUNNING: GetInstanceHealthResponse.HealthState

    class HealthInfoEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    HEALTH_STATE_FIELD_NUMBER: _ClassVar[int]
    HEALTH_INFO_FIELD_NUMBER: _ClassVar[int]
    health_state: GetInstanceHealthResponse.HealthState
    health_info: _containers.ScalarMap[str, str]

    def __init__(self, health_state: _Optional[_Union[GetInstanceHealthResponse.HealthState, str]]=..., health_info: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class UpgradeInstanceRequest(_message.Message):
    __slots__ = ('name', 'type')
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: UpgradeType

    def __init__(self, name: _Optional[str]=..., type: _Optional[_Union[UpgradeType, str]]=...) -> None:
        ...

class RollbackInstanceRequest(_message.Message):
    __slots__ = ('name', 'target_snapshot')
    NAME_FIELD_NUMBER: _ClassVar[int]
    TARGET_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    name: str
    target_snapshot: str

    def __init__(self, name: _Optional[str]=..., target_snapshot: _Optional[str]=...) -> None:
        ...

class UpgradeInstanceInternalRequest(_message.Message):
    __slots__ = ('name', 'vm_id', 'type')
    NAME_FIELD_NUMBER: _ClassVar[int]
    VM_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    name: str
    vm_id: str
    type: UpgradeType

    def __init__(self, name: _Optional[str]=..., vm_id: _Optional[str]=..., type: _Optional[_Union[UpgradeType, str]]=...) -> None:
        ...

class ListEnvironmentsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class DiagnoseInstanceRequest(_message.Message):
    __slots__ = ('name', 'diagnostic_config')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DIAGNOSTIC_CONFIG_FIELD_NUMBER: _ClassVar[int]
    name: str
    diagnostic_config: _diagnostic_config_pb2.DiagnosticConfig

    def __init__(self, name: _Optional[str]=..., diagnostic_config: _Optional[_Union[_diagnostic_config_pb2.DiagnosticConfig, _Mapping]]=...) -> None:
        ...

class ListEnvironmentsResponse(_message.Message):
    __slots__ = ('environments', 'next_page_token', 'unreachable')
    ENVIRONMENTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    environments: _containers.RepeatedCompositeFieldContainer[_environment_pb2.Environment]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, environments: _Optional[_Iterable[_Union[_environment_pb2.Environment, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetEnvironmentRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateEnvironmentRequest(_message.Message):
    __slots__ = ('parent', 'environment_id', 'environment')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_ID_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    parent: str
    environment_id: str
    environment: _environment_pb2.Environment

    def __init__(self, parent: _Optional[str]=..., environment_id: _Optional[str]=..., environment: _Optional[_Union[_environment_pb2.Environment, _Mapping]]=...) -> None:
        ...

class DeleteEnvironmentRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListSchedulesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'order_by')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=...) -> None:
        ...

class ListSchedulesResponse(_message.Message):
    __slots__ = ('schedules', 'next_page_token', 'unreachable')
    SCHEDULES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    schedules: _containers.RepeatedCompositeFieldContainer[_schedule_pb2.Schedule]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, schedules: _Optional[_Iterable[_Union[_schedule_pb2.Schedule, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetScheduleRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class DeleteScheduleRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateScheduleRequest(_message.Message):
    __slots__ = ('parent', 'schedule_id', 'schedule')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_ID_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    schedule_id: str
    schedule: _schedule_pb2.Schedule

    def __init__(self, parent: _Optional[str]=..., schedule_id: _Optional[str]=..., schedule: _Optional[_Union[_schedule_pb2.Schedule, _Mapping]]=...) -> None:
        ...

class TriggerScheduleRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListExecutionsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'order_by')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=...) -> None:
        ...

class ListExecutionsResponse(_message.Message):
    __slots__ = ('executions', 'next_page_token', 'unreachable')
    EXECUTIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    executions: _containers.RepeatedCompositeFieldContainer[_execution_pb2.Execution]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, executions: _Optional[_Iterable[_Union[_execution_pb2.Execution, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetExecutionRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class DeleteExecutionRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateExecutionRequest(_message.Message):
    __slots__ = ('parent', 'execution_id', 'execution')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_ID_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    parent: str
    execution_id: str
    execution: _execution_pb2.Execution

    def __init__(self, parent: _Optional[str]=..., execution_id: _Optional[str]=..., execution: _Optional[_Union[_execution_pb2.Execution, _Mapping]]=...) -> None:
        ...