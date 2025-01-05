from google.api import annotations_pb2 as _annotations_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.rpc import code_pb2 as _code_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ComputeEngine(_message.Message):
    __slots__ = ('instance_name', 'zone', 'machine_type', 'disk_names')
    INSTANCE_NAME_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    MACHINE_TYPE_FIELD_NUMBER: _ClassVar[int]
    DISK_NAMES_FIELD_NUMBER: _ClassVar[int]
    instance_name: str
    zone: str
    machine_type: str
    disk_names: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, instance_name: _Optional[str]=..., zone: _Optional[str]=..., machine_type: _Optional[str]=..., disk_names: _Optional[_Iterable[str]]=...) -> None:
        ...

class RuntimeMetadata(_message.Message):
    __slots__ = ('compute_engine',)
    COMPUTE_ENGINE_FIELD_NUMBER: _ClassVar[int]
    compute_engine: ComputeEngine

    def __init__(self, compute_engine: _Optional[_Union[ComputeEngine, _Mapping]]=...) -> None:
        ...

class Pipeline(_message.Message):
    __slots__ = ('project_id', 'name', 'description', 'input_parameters', 'output_parameters', 'docker', 'resources', 'pipeline_id')
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    INPUT_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    DOCKER_FIELD_NUMBER: _ClassVar[int]
    RESOURCES_FIELD_NUMBER: _ClassVar[int]
    PIPELINE_ID_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    name: str
    description: str
    input_parameters: _containers.RepeatedCompositeFieldContainer[PipelineParameter]
    output_parameters: _containers.RepeatedCompositeFieldContainer[PipelineParameter]
    docker: DockerExecutor
    resources: PipelineResources
    pipeline_id: str

    def __init__(self, project_id: _Optional[str]=..., name: _Optional[str]=..., description: _Optional[str]=..., input_parameters: _Optional[_Iterable[_Union[PipelineParameter, _Mapping]]]=..., output_parameters: _Optional[_Iterable[_Union[PipelineParameter, _Mapping]]]=..., docker: _Optional[_Union[DockerExecutor, _Mapping]]=..., resources: _Optional[_Union[PipelineResources, _Mapping]]=..., pipeline_id: _Optional[str]=...) -> None:
        ...

class CreatePipelineRequest(_message.Message):
    __slots__ = ('pipeline',)
    PIPELINE_FIELD_NUMBER: _ClassVar[int]
    pipeline: Pipeline

    def __init__(self, pipeline: _Optional[_Union[Pipeline, _Mapping]]=...) -> None:
        ...

class RunPipelineArgs(_message.Message):
    __slots__ = ('project_id', 'inputs', 'outputs', 'service_account', 'client_id', 'resources', 'logging', 'keep_vm_alive_on_failure_duration', 'labels')

    class InputsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...

    class OutputsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    INPUTS_FIELD_NUMBER: _ClassVar[int]
    OUTPUTS_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    RESOURCES_FIELD_NUMBER: _ClassVar[int]
    LOGGING_FIELD_NUMBER: _ClassVar[int]
    KEEP_VM_ALIVE_ON_FAILURE_DURATION_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    inputs: _containers.ScalarMap[str, str]
    outputs: _containers.ScalarMap[str, str]
    service_account: ServiceAccount
    client_id: str
    resources: PipelineResources
    logging: LoggingOptions
    keep_vm_alive_on_failure_duration: _duration_pb2.Duration
    labels: _containers.ScalarMap[str, str]

    def __init__(self, project_id: _Optional[str]=..., inputs: _Optional[_Mapping[str, str]]=..., outputs: _Optional[_Mapping[str, str]]=..., service_account: _Optional[_Union[ServiceAccount, _Mapping]]=..., client_id: _Optional[str]=..., resources: _Optional[_Union[PipelineResources, _Mapping]]=..., logging: _Optional[_Union[LoggingOptions, _Mapping]]=..., keep_vm_alive_on_failure_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class RunPipelineRequest(_message.Message):
    __slots__ = ('pipeline_id', 'ephemeral_pipeline', 'pipeline_args')
    PIPELINE_ID_FIELD_NUMBER: _ClassVar[int]
    EPHEMERAL_PIPELINE_FIELD_NUMBER: _ClassVar[int]
    PIPELINE_ARGS_FIELD_NUMBER: _ClassVar[int]
    pipeline_id: str
    ephemeral_pipeline: Pipeline
    pipeline_args: RunPipelineArgs

    def __init__(self, pipeline_id: _Optional[str]=..., ephemeral_pipeline: _Optional[_Union[Pipeline, _Mapping]]=..., pipeline_args: _Optional[_Union[RunPipelineArgs, _Mapping]]=...) -> None:
        ...

class GetPipelineRequest(_message.Message):
    __slots__ = ('pipeline_id',)
    PIPELINE_ID_FIELD_NUMBER: _ClassVar[int]
    pipeline_id: str

    def __init__(self, pipeline_id: _Optional[str]=...) -> None:
        ...

class ListPipelinesRequest(_message.Message):
    __slots__ = ('project_id', 'name_prefix', 'page_size', 'page_token')
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_PREFIX_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    name_prefix: str
    page_size: int
    page_token: str

    def __init__(self, project_id: _Optional[str]=..., name_prefix: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListPipelinesResponse(_message.Message):
    __slots__ = ('pipelines', 'next_page_token')
    PIPELINES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    pipelines: _containers.RepeatedCompositeFieldContainer[Pipeline]
    next_page_token: str

    def __init__(self, pipelines: _Optional[_Iterable[_Union[Pipeline, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class DeletePipelineRequest(_message.Message):
    __slots__ = ('pipeline_id',)
    PIPELINE_ID_FIELD_NUMBER: _ClassVar[int]
    pipeline_id: str

    def __init__(self, pipeline_id: _Optional[str]=...) -> None:
        ...

class GetControllerConfigRequest(_message.Message):
    __slots__ = ('operation_id', 'validation_token')
    OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    VALIDATION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    operation_id: str
    validation_token: int

    def __init__(self, operation_id: _Optional[str]=..., validation_token: _Optional[int]=...) -> None:
        ...

class ControllerConfig(_message.Message):
    __slots__ = ('image', 'cmd', 'gcs_log_path', 'machine_type', 'vars', 'disks', 'gcs_sources', 'gcs_sinks')

    class RepeatedString(_message.Message):
        __slots__ = ('values',)
        VALUES_FIELD_NUMBER: _ClassVar[int]
        values: _containers.RepeatedScalarFieldContainer[str]

        def __init__(self, values: _Optional[_Iterable[str]]=...) -> None:
            ...

    class VarsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...

    class DisksEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...

    class GcsSourcesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ControllerConfig.RepeatedString

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[ControllerConfig.RepeatedString, _Mapping]]=...) -> None:
            ...

    class GcsSinksEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ControllerConfig.RepeatedString

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[ControllerConfig.RepeatedString, _Mapping]]=...) -> None:
            ...
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    CMD_FIELD_NUMBER: _ClassVar[int]
    GCS_LOG_PATH_FIELD_NUMBER: _ClassVar[int]
    MACHINE_TYPE_FIELD_NUMBER: _ClassVar[int]
    VARS_FIELD_NUMBER: _ClassVar[int]
    DISKS_FIELD_NUMBER: _ClassVar[int]
    GCS_SOURCES_FIELD_NUMBER: _ClassVar[int]
    GCS_SINKS_FIELD_NUMBER: _ClassVar[int]
    image: str
    cmd: str
    gcs_log_path: str
    machine_type: str
    vars: _containers.ScalarMap[str, str]
    disks: _containers.ScalarMap[str, str]
    gcs_sources: _containers.MessageMap[str, ControllerConfig.RepeatedString]
    gcs_sinks: _containers.MessageMap[str, ControllerConfig.RepeatedString]

    def __init__(self, image: _Optional[str]=..., cmd: _Optional[str]=..., gcs_log_path: _Optional[str]=..., machine_type: _Optional[str]=..., vars: _Optional[_Mapping[str, str]]=..., disks: _Optional[_Mapping[str, str]]=..., gcs_sources: _Optional[_Mapping[str, ControllerConfig.RepeatedString]]=..., gcs_sinks: _Optional[_Mapping[str, ControllerConfig.RepeatedString]]=...) -> None:
        ...

class TimestampEvent(_message.Message):
    __slots__ = ('description', 'timestamp')
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    description: str
    timestamp: _timestamp_pb2.Timestamp

    def __init__(self, description: _Optional[str]=..., timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class SetOperationStatusRequest(_message.Message):
    __slots__ = ('operation_id', 'timestamp_events', 'error_code', 'error_message', 'validation_token')
    OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_EVENTS_FIELD_NUMBER: _ClassVar[int]
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    VALIDATION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    operation_id: str
    timestamp_events: _containers.RepeatedCompositeFieldContainer[TimestampEvent]
    error_code: _code_pb2.Code
    error_message: str
    validation_token: int

    def __init__(self, operation_id: _Optional[str]=..., timestamp_events: _Optional[_Iterable[_Union[TimestampEvent, _Mapping]]]=..., error_code: _Optional[_Union[_code_pb2.Code, str]]=..., error_message: _Optional[str]=..., validation_token: _Optional[int]=...) -> None:
        ...

class ServiceAccount(_message.Message):
    __slots__ = ('email', 'scopes')
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    SCOPES_FIELD_NUMBER: _ClassVar[int]
    email: str
    scopes: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, email: _Optional[str]=..., scopes: _Optional[_Iterable[str]]=...) -> None:
        ...

class LoggingOptions(_message.Message):
    __slots__ = ('gcs_path',)
    GCS_PATH_FIELD_NUMBER: _ClassVar[int]
    gcs_path: str

    def __init__(self, gcs_path: _Optional[str]=...) -> None:
        ...

class PipelineResources(_message.Message):
    __slots__ = ('minimum_cpu_cores', 'preemptible', 'minimum_ram_gb', 'disks', 'zones', 'boot_disk_size_gb', 'no_address')

    class Disk(_message.Message):
        __slots__ = ('name', 'type', 'size_gb', 'source', 'auto_delete', 'mount_point')

        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            TYPE_UNSPECIFIED: _ClassVar[PipelineResources.Disk.Type]
            PERSISTENT_HDD: _ClassVar[PipelineResources.Disk.Type]
            PERSISTENT_SSD: _ClassVar[PipelineResources.Disk.Type]
            LOCAL_SSD: _ClassVar[PipelineResources.Disk.Type]
        TYPE_UNSPECIFIED: PipelineResources.Disk.Type
        PERSISTENT_HDD: PipelineResources.Disk.Type
        PERSISTENT_SSD: PipelineResources.Disk.Type
        LOCAL_SSD: PipelineResources.Disk.Type
        NAME_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        SIZE_GB_FIELD_NUMBER: _ClassVar[int]
        SOURCE_FIELD_NUMBER: _ClassVar[int]
        AUTO_DELETE_FIELD_NUMBER: _ClassVar[int]
        MOUNT_POINT_FIELD_NUMBER: _ClassVar[int]
        name: str
        type: PipelineResources.Disk.Type
        size_gb: int
        source: str
        auto_delete: bool
        mount_point: str

        def __init__(self, name: _Optional[str]=..., type: _Optional[_Union[PipelineResources.Disk.Type, str]]=..., size_gb: _Optional[int]=..., source: _Optional[str]=..., auto_delete: bool=..., mount_point: _Optional[str]=...) -> None:
            ...
    MINIMUM_CPU_CORES_FIELD_NUMBER: _ClassVar[int]
    PREEMPTIBLE_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_RAM_GB_FIELD_NUMBER: _ClassVar[int]
    DISKS_FIELD_NUMBER: _ClassVar[int]
    ZONES_FIELD_NUMBER: _ClassVar[int]
    BOOT_DISK_SIZE_GB_FIELD_NUMBER: _ClassVar[int]
    NO_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    minimum_cpu_cores: int
    preemptible: bool
    minimum_ram_gb: float
    disks: _containers.RepeatedCompositeFieldContainer[PipelineResources.Disk]
    zones: _containers.RepeatedScalarFieldContainer[str]
    boot_disk_size_gb: int
    no_address: bool

    def __init__(self, minimum_cpu_cores: _Optional[int]=..., preemptible: bool=..., minimum_ram_gb: _Optional[float]=..., disks: _Optional[_Iterable[_Union[PipelineResources.Disk, _Mapping]]]=..., zones: _Optional[_Iterable[str]]=..., boot_disk_size_gb: _Optional[int]=..., no_address: bool=...) -> None:
        ...

class PipelineParameter(_message.Message):
    __slots__ = ('name', 'description', 'default_value', 'local_copy')

    class LocalCopy(_message.Message):
        __slots__ = ('path', 'disk')
        PATH_FIELD_NUMBER: _ClassVar[int]
        DISK_FIELD_NUMBER: _ClassVar[int]
        path: str
        disk: str

        def __init__(self, path: _Optional[str]=..., disk: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_VALUE_FIELD_NUMBER: _ClassVar[int]
    LOCAL_COPY_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    default_value: str
    local_copy: PipelineParameter.LocalCopy

    def __init__(self, name: _Optional[str]=..., description: _Optional[str]=..., default_value: _Optional[str]=..., local_copy: _Optional[_Union[PipelineParameter.LocalCopy, _Mapping]]=...) -> None:
        ...

class DockerExecutor(_message.Message):
    __slots__ = ('image_name', 'cmd')
    IMAGE_NAME_FIELD_NUMBER: _ClassVar[int]
    CMD_FIELD_NUMBER: _ClassVar[int]
    image_name: str
    cmd: str

    def __init__(self, image_name: _Optional[str]=..., cmd: _Optional[str]=...) -> None:
        ...