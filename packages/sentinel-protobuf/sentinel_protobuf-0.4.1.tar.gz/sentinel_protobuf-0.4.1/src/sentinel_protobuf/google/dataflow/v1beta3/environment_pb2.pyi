from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class JobType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    JOB_TYPE_UNKNOWN: _ClassVar[JobType]
    JOB_TYPE_BATCH: _ClassVar[JobType]
    JOB_TYPE_STREAMING: _ClassVar[JobType]

class FlexResourceSchedulingGoal(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FLEXRS_UNSPECIFIED: _ClassVar[FlexResourceSchedulingGoal]
    FLEXRS_SPEED_OPTIMIZED: _ClassVar[FlexResourceSchedulingGoal]
    FLEXRS_COST_OPTIMIZED: _ClassVar[FlexResourceSchedulingGoal]

class TeardownPolicy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TEARDOWN_POLICY_UNKNOWN: _ClassVar[TeardownPolicy]
    TEARDOWN_ALWAYS: _ClassVar[TeardownPolicy]
    TEARDOWN_ON_SUCCESS: _ClassVar[TeardownPolicy]
    TEARDOWN_NEVER: _ClassVar[TeardownPolicy]

class DefaultPackageSet(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DEFAULT_PACKAGE_SET_UNKNOWN: _ClassVar[DefaultPackageSet]
    DEFAULT_PACKAGE_SET_NONE: _ClassVar[DefaultPackageSet]
    DEFAULT_PACKAGE_SET_JAVA: _ClassVar[DefaultPackageSet]
    DEFAULT_PACKAGE_SET_PYTHON: _ClassVar[DefaultPackageSet]

class AutoscalingAlgorithm(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AUTOSCALING_ALGORITHM_UNKNOWN: _ClassVar[AutoscalingAlgorithm]
    AUTOSCALING_ALGORITHM_NONE: _ClassVar[AutoscalingAlgorithm]
    AUTOSCALING_ALGORITHM_BASIC: _ClassVar[AutoscalingAlgorithm]

class WorkerIPAddressConfiguration(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    WORKER_IP_UNSPECIFIED: _ClassVar[WorkerIPAddressConfiguration]
    WORKER_IP_PUBLIC: _ClassVar[WorkerIPAddressConfiguration]
    WORKER_IP_PRIVATE: _ClassVar[WorkerIPAddressConfiguration]

class ShuffleMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SHUFFLE_MODE_UNSPECIFIED: _ClassVar[ShuffleMode]
    VM_BASED: _ClassVar[ShuffleMode]
    SERVICE_BASED: _ClassVar[ShuffleMode]
JOB_TYPE_UNKNOWN: JobType
JOB_TYPE_BATCH: JobType
JOB_TYPE_STREAMING: JobType
FLEXRS_UNSPECIFIED: FlexResourceSchedulingGoal
FLEXRS_SPEED_OPTIMIZED: FlexResourceSchedulingGoal
FLEXRS_COST_OPTIMIZED: FlexResourceSchedulingGoal
TEARDOWN_POLICY_UNKNOWN: TeardownPolicy
TEARDOWN_ALWAYS: TeardownPolicy
TEARDOWN_ON_SUCCESS: TeardownPolicy
TEARDOWN_NEVER: TeardownPolicy
DEFAULT_PACKAGE_SET_UNKNOWN: DefaultPackageSet
DEFAULT_PACKAGE_SET_NONE: DefaultPackageSet
DEFAULT_PACKAGE_SET_JAVA: DefaultPackageSet
DEFAULT_PACKAGE_SET_PYTHON: DefaultPackageSet
AUTOSCALING_ALGORITHM_UNKNOWN: AutoscalingAlgorithm
AUTOSCALING_ALGORITHM_NONE: AutoscalingAlgorithm
AUTOSCALING_ALGORITHM_BASIC: AutoscalingAlgorithm
WORKER_IP_UNSPECIFIED: WorkerIPAddressConfiguration
WORKER_IP_PUBLIC: WorkerIPAddressConfiguration
WORKER_IP_PRIVATE: WorkerIPAddressConfiguration
SHUFFLE_MODE_UNSPECIFIED: ShuffleMode
VM_BASED: ShuffleMode
SERVICE_BASED: ShuffleMode

class Environment(_message.Message):
    __slots__ = ('temp_storage_prefix', 'cluster_manager_api_service', 'experiments', 'service_options', 'service_kms_key_name', 'worker_pools', 'user_agent', 'version', 'dataset', 'sdk_pipeline_options', 'internal_experiments', 'service_account_email', 'flex_resource_scheduling_goal', 'worker_region', 'worker_zone', 'shuffle_mode', 'debug_options')
    TEMP_STORAGE_PREFIX_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_MANAGER_API_SERVICE_FIELD_NUMBER: _ClassVar[int]
    EXPERIMENTS_FIELD_NUMBER: _ClassVar[int]
    SERVICE_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    SERVICE_KMS_KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    WORKER_POOLS_FIELD_NUMBER: _ClassVar[int]
    USER_AGENT_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    DATASET_FIELD_NUMBER: _ClassVar[int]
    SDK_PIPELINE_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    INTERNAL_EXPERIMENTS_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_EMAIL_FIELD_NUMBER: _ClassVar[int]
    FLEX_RESOURCE_SCHEDULING_GOAL_FIELD_NUMBER: _ClassVar[int]
    WORKER_REGION_FIELD_NUMBER: _ClassVar[int]
    WORKER_ZONE_FIELD_NUMBER: _ClassVar[int]
    SHUFFLE_MODE_FIELD_NUMBER: _ClassVar[int]
    DEBUG_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    temp_storage_prefix: str
    cluster_manager_api_service: str
    experiments: _containers.RepeatedScalarFieldContainer[str]
    service_options: _containers.RepeatedScalarFieldContainer[str]
    service_kms_key_name: str
    worker_pools: _containers.RepeatedCompositeFieldContainer[WorkerPool]
    user_agent: _struct_pb2.Struct
    version: _struct_pb2.Struct
    dataset: str
    sdk_pipeline_options: _struct_pb2.Struct
    internal_experiments: _any_pb2.Any
    service_account_email: str
    flex_resource_scheduling_goal: FlexResourceSchedulingGoal
    worker_region: str
    worker_zone: str
    shuffle_mode: ShuffleMode
    debug_options: DebugOptions

    def __init__(self, temp_storage_prefix: _Optional[str]=..., cluster_manager_api_service: _Optional[str]=..., experiments: _Optional[_Iterable[str]]=..., service_options: _Optional[_Iterable[str]]=..., service_kms_key_name: _Optional[str]=..., worker_pools: _Optional[_Iterable[_Union[WorkerPool, _Mapping]]]=..., user_agent: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=..., version: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=..., dataset: _Optional[str]=..., sdk_pipeline_options: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=..., internal_experiments: _Optional[_Union[_any_pb2.Any, _Mapping]]=..., service_account_email: _Optional[str]=..., flex_resource_scheduling_goal: _Optional[_Union[FlexResourceSchedulingGoal, str]]=..., worker_region: _Optional[str]=..., worker_zone: _Optional[str]=..., shuffle_mode: _Optional[_Union[ShuffleMode, str]]=..., debug_options: _Optional[_Union[DebugOptions, _Mapping]]=...) -> None:
        ...

class Package(_message.Message):
    __slots__ = ('name', 'location')
    NAME_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    name: str
    location: str

    def __init__(self, name: _Optional[str]=..., location: _Optional[str]=...) -> None:
        ...

class Disk(_message.Message):
    __slots__ = ('size_gb', 'disk_type', 'mount_point')
    SIZE_GB_FIELD_NUMBER: _ClassVar[int]
    DISK_TYPE_FIELD_NUMBER: _ClassVar[int]
    MOUNT_POINT_FIELD_NUMBER: _ClassVar[int]
    size_gb: int
    disk_type: str
    mount_point: str

    def __init__(self, size_gb: _Optional[int]=..., disk_type: _Optional[str]=..., mount_point: _Optional[str]=...) -> None:
        ...

class WorkerSettings(_message.Message):
    __slots__ = ('base_url', 'reporting_enabled', 'service_path', 'shuffle_service_path', 'worker_id', 'temp_storage_prefix')
    BASE_URL_FIELD_NUMBER: _ClassVar[int]
    REPORTING_ENABLED_FIELD_NUMBER: _ClassVar[int]
    SERVICE_PATH_FIELD_NUMBER: _ClassVar[int]
    SHUFFLE_SERVICE_PATH_FIELD_NUMBER: _ClassVar[int]
    WORKER_ID_FIELD_NUMBER: _ClassVar[int]
    TEMP_STORAGE_PREFIX_FIELD_NUMBER: _ClassVar[int]
    base_url: str
    reporting_enabled: bool
    service_path: str
    shuffle_service_path: str
    worker_id: str
    temp_storage_prefix: str

    def __init__(self, base_url: _Optional[str]=..., reporting_enabled: bool=..., service_path: _Optional[str]=..., shuffle_service_path: _Optional[str]=..., worker_id: _Optional[str]=..., temp_storage_prefix: _Optional[str]=...) -> None:
        ...

class TaskRunnerSettings(_message.Message):
    __slots__ = ('task_user', 'task_group', 'oauth_scopes', 'base_url', 'dataflow_api_version', 'parallel_worker_settings', 'base_task_dir', 'continue_on_exception', 'log_to_serialconsole', 'alsologtostderr', 'log_upload_location', 'log_dir', 'temp_storage_prefix', 'harness_command', 'workflow_file_name', 'commandlines_file_name', 'vm_id', 'language_hint', 'streaming_worker_main_class')
    TASK_USER_FIELD_NUMBER: _ClassVar[int]
    TASK_GROUP_FIELD_NUMBER: _ClassVar[int]
    OAUTH_SCOPES_FIELD_NUMBER: _ClassVar[int]
    BASE_URL_FIELD_NUMBER: _ClassVar[int]
    DATAFLOW_API_VERSION_FIELD_NUMBER: _ClassVar[int]
    PARALLEL_WORKER_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    BASE_TASK_DIR_FIELD_NUMBER: _ClassVar[int]
    CONTINUE_ON_EXCEPTION_FIELD_NUMBER: _ClassVar[int]
    LOG_TO_SERIALCONSOLE_FIELD_NUMBER: _ClassVar[int]
    ALSOLOGTOSTDERR_FIELD_NUMBER: _ClassVar[int]
    LOG_UPLOAD_LOCATION_FIELD_NUMBER: _ClassVar[int]
    LOG_DIR_FIELD_NUMBER: _ClassVar[int]
    TEMP_STORAGE_PREFIX_FIELD_NUMBER: _ClassVar[int]
    HARNESS_COMMAND_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    COMMANDLINES_FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    VM_ID_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_HINT_FIELD_NUMBER: _ClassVar[int]
    STREAMING_WORKER_MAIN_CLASS_FIELD_NUMBER: _ClassVar[int]
    task_user: str
    task_group: str
    oauth_scopes: _containers.RepeatedScalarFieldContainer[str]
    base_url: str
    dataflow_api_version: str
    parallel_worker_settings: WorkerSettings
    base_task_dir: str
    continue_on_exception: bool
    log_to_serialconsole: bool
    alsologtostderr: bool
    log_upload_location: str
    log_dir: str
    temp_storage_prefix: str
    harness_command: str
    workflow_file_name: str
    commandlines_file_name: str
    vm_id: str
    language_hint: str
    streaming_worker_main_class: str

    def __init__(self, task_user: _Optional[str]=..., task_group: _Optional[str]=..., oauth_scopes: _Optional[_Iterable[str]]=..., base_url: _Optional[str]=..., dataflow_api_version: _Optional[str]=..., parallel_worker_settings: _Optional[_Union[WorkerSettings, _Mapping]]=..., base_task_dir: _Optional[str]=..., continue_on_exception: bool=..., log_to_serialconsole: bool=..., alsologtostderr: bool=..., log_upload_location: _Optional[str]=..., log_dir: _Optional[str]=..., temp_storage_prefix: _Optional[str]=..., harness_command: _Optional[str]=..., workflow_file_name: _Optional[str]=..., commandlines_file_name: _Optional[str]=..., vm_id: _Optional[str]=..., language_hint: _Optional[str]=..., streaming_worker_main_class: _Optional[str]=...) -> None:
        ...

class AutoscalingSettings(_message.Message):
    __slots__ = ('algorithm', 'max_num_workers')
    ALGORITHM_FIELD_NUMBER: _ClassVar[int]
    MAX_NUM_WORKERS_FIELD_NUMBER: _ClassVar[int]
    algorithm: AutoscalingAlgorithm
    max_num_workers: int

    def __init__(self, algorithm: _Optional[_Union[AutoscalingAlgorithm, str]]=..., max_num_workers: _Optional[int]=...) -> None:
        ...

class SdkHarnessContainerImage(_message.Message):
    __slots__ = ('container_image', 'use_single_core_per_container', 'environment_id', 'capabilities')
    CONTAINER_IMAGE_FIELD_NUMBER: _ClassVar[int]
    USE_SINGLE_CORE_PER_CONTAINER_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_ID_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    container_image: str
    use_single_core_per_container: bool
    environment_id: str
    capabilities: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, container_image: _Optional[str]=..., use_single_core_per_container: bool=..., environment_id: _Optional[str]=..., capabilities: _Optional[_Iterable[str]]=...) -> None:
        ...

class WorkerPool(_message.Message):
    __slots__ = ('kind', 'num_workers', 'packages', 'default_package_set', 'machine_type', 'teardown_policy', 'disk_size_gb', 'disk_type', 'disk_source_image', 'zone', 'taskrunner_settings', 'on_host_maintenance', 'data_disks', 'metadata', 'autoscaling_settings', 'pool_args', 'network', 'subnetwork', 'worker_harness_container_image', 'num_threads_per_worker', 'ip_configuration', 'sdk_harness_container_images')

    class MetadataEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    KIND_FIELD_NUMBER: _ClassVar[int]
    NUM_WORKERS_FIELD_NUMBER: _ClassVar[int]
    PACKAGES_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_PACKAGE_SET_FIELD_NUMBER: _ClassVar[int]
    MACHINE_TYPE_FIELD_NUMBER: _ClassVar[int]
    TEARDOWN_POLICY_FIELD_NUMBER: _ClassVar[int]
    DISK_SIZE_GB_FIELD_NUMBER: _ClassVar[int]
    DISK_TYPE_FIELD_NUMBER: _ClassVar[int]
    DISK_SOURCE_IMAGE_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    TASKRUNNER_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    ON_HOST_MAINTENANCE_FIELD_NUMBER: _ClassVar[int]
    DATA_DISKS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    AUTOSCALING_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    POOL_ARGS_FIELD_NUMBER: _ClassVar[int]
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    SUBNETWORK_FIELD_NUMBER: _ClassVar[int]
    WORKER_HARNESS_CONTAINER_IMAGE_FIELD_NUMBER: _ClassVar[int]
    NUM_THREADS_PER_WORKER_FIELD_NUMBER: _ClassVar[int]
    IP_CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    SDK_HARNESS_CONTAINER_IMAGES_FIELD_NUMBER: _ClassVar[int]
    kind: str
    num_workers: int
    packages: _containers.RepeatedCompositeFieldContainer[Package]
    default_package_set: DefaultPackageSet
    machine_type: str
    teardown_policy: TeardownPolicy
    disk_size_gb: int
    disk_type: str
    disk_source_image: str
    zone: str
    taskrunner_settings: TaskRunnerSettings
    on_host_maintenance: str
    data_disks: _containers.RepeatedCompositeFieldContainer[Disk]
    metadata: _containers.ScalarMap[str, str]
    autoscaling_settings: AutoscalingSettings
    pool_args: _any_pb2.Any
    network: str
    subnetwork: str
    worker_harness_container_image: str
    num_threads_per_worker: int
    ip_configuration: WorkerIPAddressConfiguration
    sdk_harness_container_images: _containers.RepeatedCompositeFieldContainer[SdkHarnessContainerImage]

    def __init__(self, kind: _Optional[str]=..., num_workers: _Optional[int]=..., packages: _Optional[_Iterable[_Union[Package, _Mapping]]]=..., default_package_set: _Optional[_Union[DefaultPackageSet, str]]=..., machine_type: _Optional[str]=..., teardown_policy: _Optional[_Union[TeardownPolicy, str]]=..., disk_size_gb: _Optional[int]=..., disk_type: _Optional[str]=..., disk_source_image: _Optional[str]=..., zone: _Optional[str]=..., taskrunner_settings: _Optional[_Union[TaskRunnerSettings, _Mapping]]=..., on_host_maintenance: _Optional[str]=..., data_disks: _Optional[_Iterable[_Union[Disk, _Mapping]]]=..., metadata: _Optional[_Mapping[str, str]]=..., autoscaling_settings: _Optional[_Union[AutoscalingSettings, _Mapping]]=..., pool_args: _Optional[_Union[_any_pb2.Any, _Mapping]]=..., network: _Optional[str]=..., subnetwork: _Optional[str]=..., worker_harness_container_image: _Optional[str]=..., num_threads_per_worker: _Optional[int]=..., ip_configuration: _Optional[_Union[WorkerIPAddressConfiguration, str]]=..., sdk_harness_container_images: _Optional[_Iterable[_Union[SdkHarnessContainerImage, _Mapping]]]=...) -> None:
        ...

class DebugOptions(_message.Message):
    __slots__ = ('enable_hot_key_logging',)
    ENABLE_HOT_KEY_LOGGING_FIELD_NUMBER: _ClassVar[int]
    enable_hot_key_logging: bool

    def __init__(self, enable_hot_key_logging: bool=...) -> None:
        ...