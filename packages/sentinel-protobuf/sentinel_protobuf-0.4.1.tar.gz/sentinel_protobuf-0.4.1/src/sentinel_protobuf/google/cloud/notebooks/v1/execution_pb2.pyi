from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ExecutionTemplate(_message.Message):
    __slots__ = ('scale_tier', 'master_type', 'accelerator_config', 'labels', 'input_notebook_file', 'container_image_uri', 'output_notebook_folder', 'params_yaml_file', 'parameters', 'service_account', 'job_type', 'dataproc_parameters', 'vertex_ai_parameters', 'kernel_spec', 'tensorboard')

    class ScaleTier(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SCALE_TIER_UNSPECIFIED: _ClassVar[ExecutionTemplate.ScaleTier]
        BASIC: _ClassVar[ExecutionTemplate.ScaleTier]
        STANDARD_1: _ClassVar[ExecutionTemplate.ScaleTier]
        PREMIUM_1: _ClassVar[ExecutionTemplate.ScaleTier]
        BASIC_GPU: _ClassVar[ExecutionTemplate.ScaleTier]
        BASIC_TPU: _ClassVar[ExecutionTemplate.ScaleTier]
        CUSTOM: _ClassVar[ExecutionTemplate.ScaleTier]
    SCALE_TIER_UNSPECIFIED: ExecutionTemplate.ScaleTier
    BASIC: ExecutionTemplate.ScaleTier
    STANDARD_1: ExecutionTemplate.ScaleTier
    PREMIUM_1: ExecutionTemplate.ScaleTier
    BASIC_GPU: ExecutionTemplate.ScaleTier
    BASIC_TPU: ExecutionTemplate.ScaleTier
    CUSTOM: ExecutionTemplate.ScaleTier

    class SchedulerAcceleratorType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SCHEDULER_ACCELERATOR_TYPE_UNSPECIFIED: _ClassVar[ExecutionTemplate.SchedulerAcceleratorType]
        NVIDIA_TESLA_K80: _ClassVar[ExecutionTemplate.SchedulerAcceleratorType]
        NVIDIA_TESLA_P100: _ClassVar[ExecutionTemplate.SchedulerAcceleratorType]
        NVIDIA_TESLA_V100: _ClassVar[ExecutionTemplate.SchedulerAcceleratorType]
        NVIDIA_TESLA_P4: _ClassVar[ExecutionTemplate.SchedulerAcceleratorType]
        NVIDIA_TESLA_T4: _ClassVar[ExecutionTemplate.SchedulerAcceleratorType]
        NVIDIA_TESLA_A100: _ClassVar[ExecutionTemplate.SchedulerAcceleratorType]
        TPU_V2: _ClassVar[ExecutionTemplate.SchedulerAcceleratorType]
        TPU_V3: _ClassVar[ExecutionTemplate.SchedulerAcceleratorType]
    SCHEDULER_ACCELERATOR_TYPE_UNSPECIFIED: ExecutionTemplate.SchedulerAcceleratorType
    NVIDIA_TESLA_K80: ExecutionTemplate.SchedulerAcceleratorType
    NVIDIA_TESLA_P100: ExecutionTemplate.SchedulerAcceleratorType
    NVIDIA_TESLA_V100: ExecutionTemplate.SchedulerAcceleratorType
    NVIDIA_TESLA_P4: ExecutionTemplate.SchedulerAcceleratorType
    NVIDIA_TESLA_T4: ExecutionTemplate.SchedulerAcceleratorType
    NVIDIA_TESLA_A100: ExecutionTemplate.SchedulerAcceleratorType
    TPU_V2: ExecutionTemplate.SchedulerAcceleratorType
    TPU_V3: ExecutionTemplate.SchedulerAcceleratorType

    class JobType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        JOB_TYPE_UNSPECIFIED: _ClassVar[ExecutionTemplate.JobType]
        VERTEX_AI: _ClassVar[ExecutionTemplate.JobType]
        DATAPROC: _ClassVar[ExecutionTemplate.JobType]
    JOB_TYPE_UNSPECIFIED: ExecutionTemplate.JobType
    VERTEX_AI: ExecutionTemplate.JobType
    DATAPROC: ExecutionTemplate.JobType

    class SchedulerAcceleratorConfig(_message.Message):
        __slots__ = ('type', 'core_count')
        TYPE_FIELD_NUMBER: _ClassVar[int]
        CORE_COUNT_FIELD_NUMBER: _ClassVar[int]
        type: ExecutionTemplate.SchedulerAcceleratorType
        core_count: int

        def __init__(self, type: _Optional[_Union[ExecutionTemplate.SchedulerAcceleratorType, str]]=..., core_count: _Optional[int]=...) -> None:
            ...

    class DataprocParameters(_message.Message):
        __slots__ = ('cluster',)
        CLUSTER_FIELD_NUMBER: _ClassVar[int]
        cluster: str

        def __init__(self, cluster: _Optional[str]=...) -> None:
            ...

    class VertexAIParameters(_message.Message):
        __slots__ = ('network', 'env')

        class EnvEntry(_message.Message):
            __slots__ = ('key', 'value')
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str

            def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
                ...
        NETWORK_FIELD_NUMBER: _ClassVar[int]
        ENV_FIELD_NUMBER: _ClassVar[int]
        network: str
        env: _containers.ScalarMap[str, str]

        def __init__(self, network: _Optional[str]=..., env: _Optional[_Mapping[str, str]]=...) -> None:
            ...

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    SCALE_TIER_FIELD_NUMBER: _ClassVar[int]
    MASTER_TYPE_FIELD_NUMBER: _ClassVar[int]
    ACCELERATOR_CONFIG_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    INPUT_NOTEBOOK_FILE_FIELD_NUMBER: _ClassVar[int]
    CONTAINER_IMAGE_URI_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_NOTEBOOK_FOLDER_FIELD_NUMBER: _ClassVar[int]
    PARAMS_YAML_FILE_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    JOB_TYPE_FIELD_NUMBER: _ClassVar[int]
    DATAPROC_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    VERTEX_AI_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    KERNEL_SPEC_FIELD_NUMBER: _ClassVar[int]
    TENSORBOARD_FIELD_NUMBER: _ClassVar[int]
    scale_tier: ExecutionTemplate.ScaleTier
    master_type: str
    accelerator_config: ExecutionTemplate.SchedulerAcceleratorConfig
    labels: _containers.ScalarMap[str, str]
    input_notebook_file: str
    container_image_uri: str
    output_notebook_folder: str
    params_yaml_file: str
    parameters: str
    service_account: str
    job_type: ExecutionTemplate.JobType
    dataproc_parameters: ExecutionTemplate.DataprocParameters
    vertex_ai_parameters: ExecutionTemplate.VertexAIParameters
    kernel_spec: str
    tensorboard: str

    def __init__(self, scale_tier: _Optional[_Union[ExecutionTemplate.ScaleTier, str]]=..., master_type: _Optional[str]=..., accelerator_config: _Optional[_Union[ExecutionTemplate.SchedulerAcceleratorConfig, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., input_notebook_file: _Optional[str]=..., container_image_uri: _Optional[str]=..., output_notebook_folder: _Optional[str]=..., params_yaml_file: _Optional[str]=..., parameters: _Optional[str]=..., service_account: _Optional[str]=..., job_type: _Optional[_Union[ExecutionTemplate.JobType, str]]=..., dataproc_parameters: _Optional[_Union[ExecutionTemplate.DataprocParameters, _Mapping]]=..., vertex_ai_parameters: _Optional[_Union[ExecutionTemplate.VertexAIParameters, _Mapping]]=..., kernel_spec: _Optional[str]=..., tensorboard: _Optional[str]=...) -> None:
        ...

class Execution(_message.Message):
    __slots__ = ('execution_template', 'name', 'display_name', 'description', 'create_time', 'update_time', 'state', 'output_notebook_file', 'job_uri')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Execution.State]
        QUEUED: _ClassVar[Execution.State]
        PREPARING: _ClassVar[Execution.State]
        RUNNING: _ClassVar[Execution.State]
        SUCCEEDED: _ClassVar[Execution.State]
        FAILED: _ClassVar[Execution.State]
        CANCELLING: _ClassVar[Execution.State]
        CANCELLED: _ClassVar[Execution.State]
        EXPIRED: _ClassVar[Execution.State]
        INITIALIZING: _ClassVar[Execution.State]
    STATE_UNSPECIFIED: Execution.State
    QUEUED: Execution.State
    PREPARING: Execution.State
    RUNNING: Execution.State
    SUCCEEDED: Execution.State
    FAILED: Execution.State
    CANCELLING: Execution.State
    CANCELLED: Execution.State
    EXPIRED: Execution.State
    INITIALIZING: Execution.State
    EXECUTION_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_NOTEBOOK_FILE_FIELD_NUMBER: _ClassVar[int]
    JOB_URI_FIELD_NUMBER: _ClassVar[int]
    execution_template: ExecutionTemplate
    name: str
    display_name: str
    description: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    state: Execution.State
    output_notebook_file: str
    job_uri: str

    def __init__(self, execution_template: _Optional[_Union[ExecutionTemplate, _Mapping]]=..., name: _Optional[str]=..., display_name: _Optional[str]=..., description: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., state: _Optional[_Union[Execution.State, str]]=..., output_notebook_file: _Optional[str]=..., job_uri: _Optional[str]=...) -> None:
        ...