from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Component(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    COMPONENT_UNSPECIFIED: _ClassVar[Component]
    ANACONDA: _ClassVar[Component]
    DOCKER: _ClassVar[Component]
    DRUID: _ClassVar[Component]
    FLINK: _ClassVar[Component]
    HBASE: _ClassVar[Component]
    HIVE_WEBHCAT: _ClassVar[Component]
    HUDI: _ClassVar[Component]
    JUPYTER: _ClassVar[Component]
    PRESTO: _ClassVar[Component]
    TRINO: _ClassVar[Component]
    RANGER: _ClassVar[Component]
    SOLR: _ClassVar[Component]
    ZEPPELIN: _ClassVar[Component]
    ZOOKEEPER: _ClassVar[Component]

class FailureAction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FAILURE_ACTION_UNSPECIFIED: _ClassVar[FailureAction]
    NO_ACTION: _ClassVar[FailureAction]
    DELETE: _ClassVar[FailureAction]
COMPONENT_UNSPECIFIED: Component
ANACONDA: Component
DOCKER: Component
DRUID: Component
FLINK: Component
HBASE: Component
HIVE_WEBHCAT: Component
HUDI: Component
JUPYTER: Component
PRESTO: Component
TRINO: Component
RANGER: Component
SOLR: Component
ZEPPELIN: Component
ZOOKEEPER: Component
FAILURE_ACTION_UNSPECIFIED: FailureAction
NO_ACTION: FailureAction
DELETE: FailureAction

class RuntimeConfig(_message.Message):
    __slots__ = ('version', 'container_image', 'properties', 'repository_config', 'autotuning_config', 'cohort')

    class PropertiesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    VERSION_FIELD_NUMBER: _ClassVar[int]
    CONTAINER_IMAGE_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    REPOSITORY_CONFIG_FIELD_NUMBER: _ClassVar[int]
    AUTOTUNING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    COHORT_FIELD_NUMBER: _ClassVar[int]
    version: str
    container_image: str
    properties: _containers.ScalarMap[str, str]
    repository_config: RepositoryConfig
    autotuning_config: AutotuningConfig
    cohort: str

    def __init__(self, version: _Optional[str]=..., container_image: _Optional[str]=..., properties: _Optional[_Mapping[str, str]]=..., repository_config: _Optional[_Union[RepositoryConfig, _Mapping]]=..., autotuning_config: _Optional[_Union[AutotuningConfig, _Mapping]]=..., cohort: _Optional[str]=...) -> None:
        ...

class EnvironmentConfig(_message.Message):
    __slots__ = ('execution_config', 'peripherals_config')
    EXECUTION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    PERIPHERALS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    execution_config: ExecutionConfig
    peripherals_config: PeripheralsConfig

    def __init__(self, execution_config: _Optional[_Union[ExecutionConfig, _Mapping]]=..., peripherals_config: _Optional[_Union[PeripheralsConfig, _Mapping]]=...) -> None:
        ...

class ExecutionConfig(_message.Message):
    __slots__ = ('service_account', 'network_uri', 'subnetwork_uri', 'network_tags', 'kms_key', 'idle_ttl', 'ttl', 'staging_bucket')
    SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    NETWORK_URI_FIELD_NUMBER: _ClassVar[int]
    SUBNETWORK_URI_FIELD_NUMBER: _ClassVar[int]
    NETWORK_TAGS_FIELD_NUMBER: _ClassVar[int]
    KMS_KEY_FIELD_NUMBER: _ClassVar[int]
    IDLE_TTL_FIELD_NUMBER: _ClassVar[int]
    TTL_FIELD_NUMBER: _ClassVar[int]
    STAGING_BUCKET_FIELD_NUMBER: _ClassVar[int]
    service_account: str
    network_uri: str
    subnetwork_uri: str
    network_tags: _containers.RepeatedScalarFieldContainer[str]
    kms_key: str
    idle_ttl: _duration_pb2.Duration
    ttl: _duration_pb2.Duration
    staging_bucket: str

    def __init__(self, service_account: _Optional[str]=..., network_uri: _Optional[str]=..., subnetwork_uri: _Optional[str]=..., network_tags: _Optional[_Iterable[str]]=..., kms_key: _Optional[str]=..., idle_ttl: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., ttl: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., staging_bucket: _Optional[str]=...) -> None:
        ...

class SparkHistoryServerConfig(_message.Message):
    __slots__ = ('dataproc_cluster',)
    DATAPROC_CLUSTER_FIELD_NUMBER: _ClassVar[int]
    dataproc_cluster: str

    def __init__(self, dataproc_cluster: _Optional[str]=...) -> None:
        ...

class PeripheralsConfig(_message.Message):
    __slots__ = ('metastore_service', 'spark_history_server_config')
    METASTORE_SERVICE_FIELD_NUMBER: _ClassVar[int]
    SPARK_HISTORY_SERVER_CONFIG_FIELD_NUMBER: _ClassVar[int]
    metastore_service: str
    spark_history_server_config: SparkHistoryServerConfig

    def __init__(self, metastore_service: _Optional[str]=..., spark_history_server_config: _Optional[_Union[SparkHistoryServerConfig, _Mapping]]=...) -> None:
        ...

class RuntimeInfo(_message.Message):
    __slots__ = ('endpoints', 'output_uri', 'diagnostic_output_uri', 'approximate_usage', 'current_usage')

    class EndpointsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    ENDPOINTS_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_URI_FIELD_NUMBER: _ClassVar[int]
    DIAGNOSTIC_OUTPUT_URI_FIELD_NUMBER: _ClassVar[int]
    APPROXIMATE_USAGE_FIELD_NUMBER: _ClassVar[int]
    CURRENT_USAGE_FIELD_NUMBER: _ClassVar[int]
    endpoints: _containers.ScalarMap[str, str]
    output_uri: str
    diagnostic_output_uri: str
    approximate_usage: UsageMetrics
    current_usage: UsageSnapshot

    def __init__(self, endpoints: _Optional[_Mapping[str, str]]=..., output_uri: _Optional[str]=..., diagnostic_output_uri: _Optional[str]=..., approximate_usage: _Optional[_Union[UsageMetrics, _Mapping]]=..., current_usage: _Optional[_Union[UsageSnapshot, _Mapping]]=...) -> None:
        ...

class UsageMetrics(_message.Message):
    __slots__ = ('milli_dcu_seconds', 'shuffle_storage_gb_seconds', 'milli_accelerator_seconds', 'accelerator_type')
    MILLI_DCU_SECONDS_FIELD_NUMBER: _ClassVar[int]
    SHUFFLE_STORAGE_GB_SECONDS_FIELD_NUMBER: _ClassVar[int]
    MILLI_ACCELERATOR_SECONDS_FIELD_NUMBER: _ClassVar[int]
    ACCELERATOR_TYPE_FIELD_NUMBER: _ClassVar[int]
    milli_dcu_seconds: int
    shuffle_storage_gb_seconds: int
    milli_accelerator_seconds: int
    accelerator_type: str

    def __init__(self, milli_dcu_seconds: _Optional[int]=..., shuffle_storage_gb_seconds: _Optional[int]=..., milli_accelerator_seconds: _Optional[int]=..., accelerator_type: _Optional[str]=...) -> None:
        ...

class UsageSnapshot(_message.Message):
    __slots__ = ('milli_dcu', 'shuffle_storage_gb', 'milli_dcu_premium', 'shuffle_storage_gb_premium', 'milli_accelerator', 'accelerator_type', 'snapshot_time')
    MILLI_DCU_FIELD_NUMBER: _ClassVar[int]
    SHUFFLE_STORAGE_GB_FIELD_NUMBER: _ClassVar[int]
    MILLI_DCU_PREMIUM_FIELD_NUMBER: _ClassVar[int]
    SHUFFLE_STORAGE_GB_PREMIUM_FIELD_NUMBER: _ClassVar[int]
    MILLI_ACCELERATOR_FIELD_NUMBER: _ClassVar[int]
    ACCELERATOR_TYPE_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_TIME_FIELD_NUMBER: _ClassVar[int]
    milli_dcu: int
    shuffle_storage_gb: int
    milli_dcu_premium: int
    shuffle_storage_gb_premium: int
    milli_accelerator: int
    accelerator_type: str
    snapshot_time: _timestamp_pb2.Timestamp

    def __init__(self, milli_dcu: _Optional[int]=..., shuffle_storage_gb: _Optional[int]=..., milli_dcu_premium: _Optional[int]=..., shuffle_storage_gb_premium: _Optional[int]=..., milli_accelerator: _Optional[int]=..., accelerator_type: _Optional[str]=..., snapshot_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class GkeClusterConfig(_message.Message):
    __slots__ = ('gke_cluster_target', 'node_pool_target')
    GKE_CLUSTER_TARGET_FIELD_NUMBER: _ClassVar[int]
    NODE_POOL_TARGET_FIELD_NUMBER: _ClassVar[int]
    gke_cluster_target: str
    node_pool_target: _containers.RepeatedCompositeFieldContainer[GkeNodePoolTarget]

    def __init__(self, gke_cluster_target: _Optional[str]=..., node_pool_target: _Optional[_Iterable[_Union[GkeNodePoolTarget, _Mapping]]]=...) -> None:
        ...

class KubernetesClusterConfig(_message.Message):
    __slots__ = ('kubernetes_namespace', 'gke_cluster_config', 'kubernetes_software_config')
    KUBERNETES_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    GKE_CLUSTER_CONFIG_FIELD_NUMBER: _ClassVar[int]
    KUBERNETES_SOFTWARE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    kubernetes_namespace: str
    gke_cluster_config: GkeClusterConfig
    kubernetes_software_config: KubernetesSoftwareConfig

    def __init__(self, kubernetes_namespace: _Optional[str]=..., gke_cluster_config: _Optional[_Union[GkeClusterConfig, _Mapping]]=..., kubernetes_software_config: _Optional[_Union[KubernetesSoftwareConfig, _Mapping]]=...) -> None:
        ...

class KubernetesSoftwareConfig(_message.Message):
    __slots__ = ('component_version', 'properties')

    class ComponentVersionEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...

    class PropertiesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    COMPONENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    component_version: _containers.ScalarMap[str, str]
    properties: _containers.ScalarMap[str, str]

    def __init__(self, component_version: _Optional[_Mapping[str, str]]=..., properties: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class GkeNodePoolTarget(_message.Message):
    __slots__ = ('node_pool', 'roles', 'node_pool_config')

    class Role(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ROLE_UNSPECIFIED: _ClassVar[GkeNodePoolTarget.Role]
        DEFAULT: _ClassVar[GkeNodePoolTarget.Role]
        CONTROLLER: _ClassVar[GkeNodePoolTarget.Role]
        SPARK_DRIVER: _ClassVar[GkeNodePoolTarget.Role]
        SPARK_EXECUTOR: _ClassVar[GkeNodePoolTarget.Role]
    ROLE_UNSPECIFIED: GkeNodePoolTarget.Role
    DEFAULT: GkeNodePoolTarget.Role
    CONTROLLER: GkeNodePoolTarget.Role
    SPARK_DRIVER: GkeNodePoolTarget.Role
    SPARK_EXECUTOR: GkeNodePoolTarget.Role
    NODE_POOL_FIELD_NUMBER: _ClassVar[int]
    ROLES_FIELD_NUMBER: _ClassVar[int]
    NODE_POOL_CONFIG_FIELD_NUMBER: _ClassVar[int]
    node_pool: str
    roles: _containers.RepeatedScalarFieldContainer[GkeNodePoolTarget.Role]
    node_pool_config: GkeNodePoolConfig

    def __init__(self, node_pool: _Optional[str]=..., roles: _Optional[_Iterable[_Union[GkeNodePoolTarget.Role, str]]]=..., node_pool_config: _Optional[_Union[GkeNodePoolConfig, _Mapping]]=...) -> None:
        ...

class GkeNodePoolConfig(_message.Message):
    __slots__ = ('config', 'locations', 'autoscaling')

    class GkeNodeConfig(_message.Message):
        __slots__ = ('machine_type', 'local_ssd_count', 'preemptible', 'accelerators', 'min_cpu_platform', 'boot_disk_kms_key', 'spot')
        MACHINE_TYPE_FIELD_NUMBER: _ClassVar[int]
        LOCAL_SSD_COUNT_FIELD_NUMBER: _ClassVar[int]
        PREEMPTIBLE_FIELD_NUMBER: _ClassVar[int]
        ACCELERATORS_FIELD_NUMBER: _ClassVar[int]
        MIN_CPU_PLATFORM_FIELD_NUMBER: _ClassVar[int]
        BOOT_DISK_KMS_KEY_FIELD_NUMBER: _ClassVar[int]
        SPOT_FIELD_NUMBER: _ClassVar[int]
        machine_type: str
        local_ssd_count: int
        preemptible: bool
        accelerators: _containers.RepeatedCompositeFieldContainer[GkeNodePoolConfig.GkeNodePoolAcceleratorConfig]
        min_cpu_platform: str
        boot_disk_kms_key: str
        spot: bool

        def __init__(self, machine_type: _Optional[str]=..., local_ssd_count: _Optional[int]=..., preemptible: bool=..., accelerators: _Optional[_Iterable[_Union[GkeNodePoolConfig.GkeNodePoolAcceleratorConfig, _Mapping]]]=..., min_cpu_platform: _Optional[str]=..., boot_disk_kms_key: _Optional[str]=..., spot: bool=...) -> None:
            ...

    class GkeNodePoolAcceleratorConfig(_message.Message):
        __slots__ = ('accelerator_count', 'accelerator_type', 'gpu_partition_size')
        ACCELERATOR_COUNT_FIELD_NUMBER: _ClassVar[int]
        ACCELERATOR_TYPE_FIELD_NUMBER: _ClassVar[int]
        GPU_PARTITION_SIZE_FIELD_NUMBER: _ClassVar[int]
        accelerator_count: int
        accelerator_type: str
        gpu_partition_size: str

        def __init__(self, accelerator_count: _Optional[int]=..., accelerator_type: _Optional[str]=..., gpu_partition_size: _Optional[str]=...) -> None:
            ...

    class GkeNodePoolAutoscalingConfig(_message.Message):
        __slots__ = ('min_node_count', 'max_node_count')
        MIN_NODE_COUNT_FIELD_NUMBER: _ClassVar[int]
        MAX_NODE_COUNT_FIELD_NUMBER: _ClassVar[int]
        min_node_count: int
        max_node_count: int

        def __init__(self, min_node_count: _Optional[int]=..., max_node_count: _Optional[int]=...) -> None:
            ...
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    LOCATIONS_FIELD_NUMBER: _ClassVar[int]
    AUTOSCALING_FIELD_NUMBER: _ClassVar[int]
    config: GkeNodePoolConfig.GkeNodeConfig
    locations: _containers.RepeatedScalarFieldContainer[str]
    autoscaling: GkeNodePoolConfig.GkeNodePoolAutoscalingConfig

    def __init__(self, config: _Optional[_Union[GkeNodePoolConfig.GkeNodeConfig, _Mapping]]=..., locations: _Optional[_Iterable[str]]=..., autoscaling: _Optional[_Union[GkeNodePoolConfig.GkeNodePoolAutoscalingConfig, _Mapping]]=...) -> None:
        ...

class AutotuningConfig(_message.Message):
    __slots__ = ('scenarios',)

    class Scenario(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SCENARIO_UNSPECIFIED: _ClassVar[AutotuningConfig.Scenario]
        SCALING: _ClassVar[AutotuningConfig.Scenario]
        BROADCAST_HASH_JOIN: _ClassVar[AutotuningConfig.Scenario]
        MEMORY: _ClassVar[AutotuningConfig.Scenario]
    SCENARIO_UNSPECIFIED: AutotuningConfig.Scenario
    SCALING: AutotuningConfig.Scenario
    BROADCAST_HASH_JOIN: AutotuningConfig.Scenario
    MEMORY: AutotuningConfig.Scenario
    SCENARIOS_FIELD_NUMBER: _ClassVar[int]
    scenarios: _containers.RepeatedScalarFieldContainer[AutotuningConfig.Scenario]

    def __init__(self, scenarios: _Optional[_Iterable[_Union[AutotuningConfig.Scenario, str]]]=...) -> None:
        ...

class RepositoryConfig(_message.Message):
    __slots__ = ('pypi_repository_config',)
    PYPI_REPOSITORY_CONFIG_FIELD_NUMBER: _ClassVar[int]
    pypi_repository_config: PyPiRepositoryConfig

    def __init__(self, pypi_repository_config: _Optional[_Union[PyPiRepositoryConfig, _Mapping]]=...) -> None:
        ...

class PyPiRepositoryConfig(_message.Message):
    __slots__ = ('pypi_repository',)
    PYPI_REPOSITORY_FIELD_NUMBER: _ClassVar[int]
    pypi_repository: str

    def __init__(self, pypi_repository: _Optional[str]=...) -> None:
        ...