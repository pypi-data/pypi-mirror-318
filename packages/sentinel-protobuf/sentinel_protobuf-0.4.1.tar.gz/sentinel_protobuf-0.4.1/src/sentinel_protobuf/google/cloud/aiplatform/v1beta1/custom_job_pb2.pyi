from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.aiplatform.v1beta1 import encryption_spec_pb2 as _encryption_spec_pb2
from google.cloud.aiplatform.v1beta1 import env_var_pb2 as _env_var_pb2
from google.cloud.aiplatform.v1beta1 import io_pb2 as _io_pb2
from google.cloud.aiplatform.v1beta1 import job_state_pb2 as _job_state_pb2
from google.cloud.aiplatform.v1beta1 import machine_resources_pb2 as _machine_resources_pb2
from google.cloud.aiplatform.v1beta1 import service_networking_pb2 as _service_networking_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CustomJob(_message.Message):
    __slots__ = ('name', 'display_name', 'job_spec', 'state', 'create_time', 'start_time', 'end_time', 'update_time', 'error', 'labels', 'encryption_spec', 'web_access_uris', 'satisfies_pzs', 'satisfies_pzi')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...

    class WebAccessUrisEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    JOB_SPEC_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_SPEC_FIELD_NUMBER: _ClassVar[int]
    WEB_ACCESS_URIS_FIELD_NUMBER: _ClassVar[int]
    SATISFIES_PZS_FIELD_NUMBER: _ClassVar[int]
    SATISFIES_PZI_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    job_spec: CustomJobSpec
    state: _job_state_pb2.JobState
    create_time: _timestamp_pb2.Timestamp
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    error: _status_pb2.Status
    labels: _containers.ScalarMap[str, str]
    encryption_spec: _encryption_spec_pb2.EncryptionSpec
    web_access_uris: _containers.ScalarMap[str, str]
    satisfies_pzs: bool
    satisfies_pzi: bool

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., job_spec: _Optional[_Union[CustomJobSpec, _Mapping]]=..., state: _Optional[_Union[_job_state_pb2.JobState, str]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., error: _Optional[_Union[_status_pb2.Status, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., encryption_spec: _Optional[_Union[_encryption_spec_pb2.EncryptionSpec, _Mapping]]=..., web_access_uris: _Optional[_Mapping[str, str]]=..., satisfies_pzs: bool=..., satisfies_pzi: bool=...) -> None:
        ...

class CustomJobSpec(_message.Message):
    __slots__ = ('persistent_resource_id', 'worker_pool_specs', 'scheduling', 'service_account', 'network', 'reserved_ip_ranges', 'psc_interface_config', 'base_output_directory', 'protected_artifact_location_id', 'tensorboard', 'enable_web_access', 'enable_dashboard_access', 'experiment', 'experiment_run', 'models')
    PERSISTENT_RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    WORKER_POOL_SPECS_FIELD_NUMBER: _ClassVar[int]
    SCHEDULING_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    RESERVED_IP_RANGES_FIELD_NUMBER: _ClassVar[int]
    PSC_INTERFACE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    BASE_OUTPUT_DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    PROTECTED_ARTIFACT_LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    TENSORBOARD_FIELD_NUMBER: _ClassVar[int]
    ENABLE_WEB_ACCESS_FIELD_NUMBER: _ClassVar[int]
    ENABLE_DASHBOARD_ACCESS_FIELD_NUMBER: _ClassVar[int]
    EXPERIMENT_FIELD_NUMBER: _ClassVar[int]
    EXPERIMENT_RUN_FIELD_NUMBER: _ClassVar[int]
    MODELS_FIELD_NUMBER: _ClassVar[int]
    persistent_resource_id: str
    worker_pool_specs: _containers.RepeatedCompositeFieldContainer[WorkerPoolSpec]
    scheduling: Scheduling
    service_account: str
    network: str
    reserved_ip_ranges: _containers.RepeatedScalarFieldContainer[str]
    psc_interface_config: _service_networking_pb2.PscInterfaceConfig
    base_output_directory: _io_pb2.GcsDestination
    protected_artifact_location_id: str
    tensorboard: str
    enable_web_access: bool
    enable_dashboard_access: bool
    experiment: str
    experiment_run: str
    models: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, persistent_resource_id: _Optional[str]=..., worker_pool_specs: _Optional[_Iterable[_Union[WorkerPoolSpec, _Mapping]]]=..., scheduling: _Optional[_Union[Scheduling, _Mapping]]=..., service_account: _Optional[str]=..., network: _Optional[str]=..., reserved_ip_ranges: _Optional[_Iterable[str]]=..., psc_interface_config: _Optional[_Union[_service_networking_pb2.PscInterfaceConfig, _Mapping]]=..., base_output_directory: _Optional[_Union[_io_pb2.GcsDestination, _Mapping]]=..., protected_artifact_location_id: _Optional[str]=..., tensorboard: _Optional[str]=..., enable_web_access: bool=..., enable_dashboard_access: bool=..., experiment: _Optional[str]=..., experiment_run: _Optional[str]=..., models: _Optional[_Iterable[str]]=...) -> None:
        ...

class WorkerPoolSpec(_message.Message):
    __slots__ = ('container_spec', 'python_package_spec', 'machine_spec', 'replica_count', 'nfs_mounts', 'disk_spec')
    CONTAINER_SPEC_FIELD_NUMBER: _ClassVar[int]
    PYTHON_PACKAGE_SPEC_FIELD_NUMBER: _ClassVar[int]
    MACHINE_SPEC_FIELD_NUMBER: _ClassVar[int]
    REPLICA_COUNT_FIELD_NUMBER: _ClassVar[int]
    NFS_MOUNTS_FIELD_NUMBER: _ClassVar[int]
    DISK_SPEC_FIELD_NUMBER: _ClassVar[int]
    container_spec: ContainerSpec
    python_package_spec: PythonPackageSpec
    machine_spec: _machine_resources_pb2.MachineSpec
    replica_count: int
    nfs_mounts: _containers.RepeatedCompositeFieldContainer[_machine_resources_pb2.NfsMount]
    disk_spec: _machine_resources_pb2.DiskSpec

    def __init__(self, container_spec: _Optional[_Union[ContainerSpec, _Mapping]]=..., python_package_spec: _Optional[_Union[PythonPackageSpec, _Mapping]]=..., machine_spec: _Optional[_Union[_machine_resources_pb2.MachineSpec, _Mapping]]=..., replica_count: _Optional[int]=..., nfs_mounts: _Optional[_Iterable[_Union[_machine_resources_pb2.NfsMount, _Mapping]]]=..., disk_spec: _Optional[_Union[_machine_resources_pb2.DiskSpec, _Mapping]]=...) -> None:
        ...

class ContainerSpec(_message.Message):
    __slots__ = ('image_uri', 'command', 'args', 'env')
    IMAGE_URI_FIELD_NUMBER: _ClassVar[int]
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    ARGS_FIELD_NUMBER: _ClassVar[int]
    ENV_FIELD_NUMBER: _ClassVar[int]
    image_uri: str
    command: _containers.RepeatedScalarFieldContainer[str]
    args: _containers.RepeatedScalarFieldContainer[str]
    env: _containers.RepeatedCompositeFieldContainer[_env_var_pb2.EnvVar]

    def __init__(self, image_uri: _Optional[str]=..., command: _Optional[_Iterable[str]]=..., args: _Optional[_Iterable[str]]=..., env: _Optional[_Iterable[_Union[_env_var_pb2.EnvVar, _Mapping]]]=...) -> None:
        ...

class PythonPackageSpec(_message.Message):
    __slots__ = ('executor_image_uri', 'package_uris', 'python_module', 'args', 'env')
    EXECUTOR_IMAGE_URI_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_URIS_FIELD_NUMBER: _ClassVar[int]
    PYTHON_MODULE_FIELD_NUMBER: _ClassVar[int]
    ARGS_FIELD_NUMBER: _ClassVar[int]
    ENV_FIELD_NUMBER: _ClassVar[int]
    executor_image_uri: str
    package_uris: _containers.RepeatedScalarFieldContainer[str]
    python_module: str
    args: _containers.RepeatedScalarFieldContainer[str]
    env: _containers.RepeatedCompositeFieldContainer[_env_var_pb2.EnvVar]

    def __init__(self, executor_image_uri: _Optional[str]=..., package_uris: _Optional[_Iterable[str]]=..., python_module: _Optional[str]=..., args: _Optional[_Iterable[str]]=..., env: _Optional[_Iterable[_Union[_env_var_pb2.EnvVar, _Mapping]]]=...) -> None:
        ...

class Scheduling(_message.Message):
    __slots__ = ('timeout', 'restart_job_on_worker_restart', 'strategy', 'disable_retries', 'max_wait_duration')

    class Strategy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STRATEGY_UNSPECIFIED: _ClassVar[Scheduling.Strategy]
        ON_DEMAND: _ClassVar[Scheduling.Strategy]
        LOW_COST: _ClassVar[Scheduling.Strategy]
        STANDARD: _ClassVar[Scheduling.Strategy]
        SPOT: _ClassVar[Scheduling.Strategy]
        FLEX_START: _ClassVar[Scheduling.Strategy]
    STRATEGY_UNSPECIFIED: Scheduling.Strategy
    ON_DEMAND: Scheduling.Strategy
    LOW_COST: Scheduling.Strategy
    STANDARD: Scheduling.Strategy
    SPOT: Scheduling.Strategy
    FLEX_START: Scheduling.Strategy
    TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    RESTART_JOB_ON_WORKER_RESTART_FIELD_NUMBER: _ClassVar[int]
    STRATEGY_FIELD_NUMBER: _ClassVar[int]
    DISABLE_RETRIES_FIELD_NUMBER: _ClassVar[int]
    MAX_WAIT_DURATION_FIELD_NUMBER: _ClassVar[int]
    timeout: _duration_pb2.Duration
    restart_job_on_worker_restart: bool
    strategy: Scheduling.Strategy
    disable_retries: bool
    max_wait_duration: _duration_pb2.Duration

    def __init__(self, timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., restart_job_on_worker_restart: bool=..., strategy: _Optional[_Union[Scheduling.Strategy, str]]=..., disable_retries: bool=..., max_wait_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=...) -> None:
        ...