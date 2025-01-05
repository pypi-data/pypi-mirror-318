from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.dataproc.v1 import operations_pb2 as _operations_pb2
from google.cloud.dataproc.v1 import shared_pb2 as _shared_pb2
from google.longrunning import operations_pb2 as _operations_pb2_1
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.type import interval_pb2 as _interval_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Cluster(_message.Message):
    __slots__ = ("project_id", "cluster_name", "config", "virtual_cluster_config", "labels", "status", "status_history", "cluster_uuid", "metrics")
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_NAME_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    VIRTUAL_CLUSTER_CONFIG_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    STATUS_HISTORY_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_UUID_FIELD_NUMBER: _ClassVar[int]
    METRICS_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    cluster_name: str
    config: ClusterConfig
    virtual_cluster_config: VirtualClusterConfig
    labels: _containers.ScalarMap[str, str]
    status: ClusterStatus
    status_history: _containers.RepeatedCompositeFieldContainer[ClusterStatus]
    cluster_uuid: str
    metrics: ClusterMetrics
    def __init__(self, project_id: _Optional[str] = ..., cluster_name: _Optional[str] = ..., config: _Optional[_Union[ClusterConfig, _Mapping]] = ..., virtual_cluster_config: _Optional[_Union[VirtualClusterConfig, _Mapping]] = ..., labels: _Optional[_Mapping[str, str]] = ..., status: _Optional[_Union[ClusterStatus, _Mapping]] = ..., status_history: _Optional[_Iterable[_Union[ClusterStatus, _Mapping]]] = ..., cluster_uuid: _Optional[str] = ..., metrics: _Optional[_Union[ClusterMetrics, _Mapping]] = ...) -> None: ...

class ClusterConfig(_message.Message):
    __slots__ = ("config_bucket", "temp_bucket", "gce_cluster_config", "master_config", "worker_config", "secondary_worker_config", "software_config", "initialization_actions", "encryption_config", "autoscaling_config", "security_config", "lifecycle_config", "endpoint_config", "metastore_config", "dataproc_metric_config", "auxiliary_node_groups")
    CONFIG_BUCKET_FIELD_NUMBER: _ClassVar[int]
    TEMP_BUCKET_FIELD_NUMBER: _ClassVar[int]
    GCE_CLUSTER_CONFIG_FIELD_NUMBER: _ClassVar[int]
    MASTER_CONFIG_FIELD_NUMBER: _ClassVar[int]
    WORKER_CONFIG_FIELD_NUMBER: _ClassVar[int]
    SECONDARY_WORKER_CONFIG_FIELD_NUMBER: _ClassVar[int]
    SOFTWARE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    INITIALIZATION_ACTIONS_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    AUTOSCALING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    SECURITY_CONFIG_FIELD_NUMBER: _ClassVar[int]
    LIFECYCLE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    METASTORE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DATAPROC_METRIC_CONFIG_FIELD_NUMBER: _ClassVar[int]
    AUXILIARY_NODE_GROUPS_FIELD_NUMBER: _ClassVar[int]
    config_bucket: str
    temp_bucket: str
    gce_cluster_config: GceClusterConfig
    master_config: InstanceGroupConfig
    worker_config: InstanceGroupConfig
    secondary_worker_config: InstanceGroupConfig
    software_config: SoftwareConfig
    initialization_actions: _containers.RepeatedCompositeFieldContainer[NodeInitializationAction]
    encryption_config: EncryptionConfig
    autoscaling_config: AutoscalingConfig
    security_config: SecurityConfig
    lifecycle_config: LifecycleConfig
    endpoint_config: EndpointConfig
    metastore_config: MetastoreConfig
    dataproc_metric_config: DataprocMetricConfig
    auxiliary_node_groups: _containers.RepeatedCompositeFieldContainer[AuxiliaryNodeGroup]
    def __init__(self, config_bucket: _Optional[str] = ..., temp_bucket: _Optional[str] = ..., gce_cluster_config: _Optional[_Union[GceClusterConfig, _Mapping]] = ..., master_config: _Optional[_Union[InstanceGroupConfig, _Mapping]] = ..., worker_config: _Optional[_Union[InstanceGroupConfig, _Mapping]] = ..., secondary_worker_config: _Optional[_Union[InstanceGroupConfig, _Mapping]] = ..., software_config: _Optional[_Union[SoftwareConfig, _Mapping]] = ..., initialization_actions: _Optional[_Iterable[_Union[NodeInitializationAction, _Mapping]]] = ..., encryption_config: _Optional[_Union[EncryptionConfig, _Mapping]] = ..., autoscaling_config: _Optional[_Union[AutoscalingConfig, _Mapping]] = ..., security_config: _Optional[_Union[SecurityConfig, _Mapping]] = ..., lifecycle_config: _Optional[_Union[LifecycleConfig, _Mapping]] = ..., endpoint_config: _Optional[_Union[EndpointConfig, _Mapping]] = ..., metastore_config: _Optional[_Union[MetastoreConfig, _Mapping]] = ..., dataproc_metric_config: _Optional[_Union[DataprocMetricConfig, _Mapping]] = ..., auxiliary_node_groups: _Optional[_Iterable[_Union[AuxiliaryNodeGroup, _Mapping]]] = ...) -> None: ...

class VirtualClusterConfig(_message.Message):
    __slots__ = ("staging_bucket", "kubernetes_cluster_config", "auxiliary_services_config")
    STAGING_BUCKET_FIELD_NUMBER: _ClassVar[int]
    KUBERNETES_CLUSTER_CONFIG_FIELD_NUMBER: _ClassVar[int]
    AUXILIARY_SERVICES_CONFIG_FIELD_NUMBER: _ClassVar[int]
    staging_bucket: str
    kubernetes_cluster_config: _shared_pb2.KubernetesClusterConfig
    auxiliary_services_config: AuxiliaryServicesConfig
    def __init__(self, staging_bucket: _Optional[str] = ..., kubernetes_cluster_config: _Optional[_Union[_shared_pb2.KubernetesClusterConfig, _Mapping]] = ..., auxiliary_services_config: _Optional[_Union[AuxiliaryServicesConfig, _Mapping]] = ...) -> None: ...

class AuxiliaryServicesConfig(_message.Message):
    __slots__ = ("metastore_config", "spark_history_server_config")
    METASTORE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    SPARK_HISTORY_SERVER_CONFIG_FIELD_NUMBER: _ClassVar[int]
    metastore_config: MetastoreConfig
    spark_history_server_config: _shared_pb2.SparkHistoryServerConfig
    def __init__(self, metastore_config: _Optional[_Union[MetastoreConfig, _Mapping]] = ..., spark_history_server_config: _Optional[_Union[_shared_pb2.SparkHistoryServerConfig, _Mapping]] = ...) -> None: ...

class EndpointConfig(_message.Message):
    __slots__ = ("http_ports", "enable_http_port_access")
    class HttpPortsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    HTTP_PORTS_FIELD_NUMBER: _ClassVar[int]
    ENABLE_HTTP_PORT_ACCESS_FIELD_NUMBER: _ClassVar[int]
    http_ports: _containers.ScalarMap[str, str]
    enable_http_port_access: bool
    def __init__(self, http_ports: _Optional[_Mapping[str, str]] = ..., enable_http_port_access: bool = ...) -> None: ...

class AutoscalingConfig(_message.Message):
    __slots__ = ("policy_uri",)
    POLICY_URI_FIELD_NUMBER: _ClassVar[int]
    policy_uri: str
    def __init__(self, policy_uri: _Optional[str] = ...) -> None: ...

class EncryptionConfig(_message.Message):
    __slots__ = ("gce_pd_kms_key_name", "kms_key")
    GCE_PD_KMS_KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    KMS_KEY_FIELD_NUMBER: _ClassVar[int]
    gce_pd_kms_key_name: str
    kms_key: str
    def __init__(self, gce_pd_kms_key_name: _Optional[str] = ..., kms_key: _Optional[str] = ...) -> None: ...

class GceClusterConfig(_message.Message):
    __slots__ = ("zone_uri", "network_uri", "subnetwork_uri", "internal_ip_only", "private_ipv6_google_access", "service_account", "service_account_scopes", "tags", "metadata", "reservation_affinity", "node_group_affinity", "shielded_instance_config", "confidential_instance_config")
    class PrivateIpv6GoogleAccess(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PRIVATE_IPV6_GOOGLE_ACCESS_UNSPECIFIED: _ClassVar[GceClusterConfig.PrivateIpv6GoogleAccess]
        INHERIT_FROM_SUBNETWORK: _ClassVar[GceClusterConfig.PrivateIpv6GoogleAccess]
        OUTBOUND: _ClassVar[GceClusterConfig.PrivateIpv6GoogleAccess]
        BIDIRECTIONAL: _ClassVar[GceClusterConfig.PrivateIpv6GoogleAccess]
    PRIVATE_IPV6_GOOGLE_ACCESS_UNSPECIFIED: GceClusterConfig.PrivateIpv6GoogleAccess
    INHERIT_FROM_SUBNETWORK: GceClusterConfig.PrivateIpv6GoogleAccess
    OUTBOUND: GceClusterConfig.PrivateIpv6GoogleAccess
    BIDIRECTIONAL: GceClusterConfig.PrivateIpv6GoogleAccess
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ZONE_URI_FIELD_NUMBER: _ClassVar[int]
    NETWORK_URI_FIELD_NUMBER: _ClassVar[int]
    SUBNETWORK_URI_FIELD_NUMBER: _ClassVar[int]
    INTERNAL_IP_ONLY_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_IPV6_GOOGLE_ACCESS_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_SCOPES_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    RESERVATION_AFFINITY_FIELD_NUMBER: _ClassVar[int]
    NODE_GROUP_AFFINITY_FIELD_NUMBER: _ClassVar[int]
    SHIELDED_INSTANCE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CONFIDENTIAL_INSTANCE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    zone_uri: str
    network_uri: str
    subnetwork_uri: str
    internal_ip_only: bool
    private_ipv6_google_access: GceClusterConfig.PrivateIpv6GoogleAccess
    service_account: str
    service_account_scopes: _containers.RepeatedScalarFieldContainer[str]
    tags: _containers.RepeatedScalarFieldContainer[str]
    metadata: _containers.ScalarMap[str, str]
    reservation_affinity: ReservationAffinity
    node_group_affinity: NodeGroupAffinity
    shielded_instance_config: ShieldedInstanceConfig
    confidential_instance_config: ConfidentialInstanceConfig
    def __init__(self, zone_uri: _Optional[str] = ..., network_uri: _Optional[str] = ..., subnetwork_uri: _Optional[str] = ..., internal_ip_only: bool = ..., private_ipv6_google_access: _Optional[_Union[GceClusterConfig.PrivateIpv6GoogleAccess, str]] = ..., service_account: _Optional[str] = ..., service_account_scopes: _Optional[_Iterable[str]] = ..., tags: _Optional[_Iterable[str]] = ..., metadata: _Optional[_Mapping[str, str]] = ..., reservation_affinity: _Optional[_Union[ReservationAffinity, _Mapping]] = ..., node_group_affinity: _Optional[_Union[NodeGroupAffinity, _Mapping]] = ..., shielded_instance_config: _Optional[_Union[ShieldedInstanceConfig, _Mapping]] = ..., confidential_instance_config: _Optional[_Union[ConfidentialInstanceConfig, _Mapping]] = ...) -> None: ...

class NodeGroupAffinity(_message.Message):
    __slots__ = ("node_group_uri",)
    NODE_GROUP_URI_FIELD_NUMBER: _ClassVar[int]
    node_group_uri: str
    def __init__(self, node_group_uri: _Optional[str] = ...) -> None: ...

class ShieldedInstanceConfig(_message.Message):
    __slots__ = ("enable_secure_boot", "enable_vtpm", "enable_integrity_monitoring")
    ENABLE_SECURE_BOOT_FIELD_NUMBER: _ClassVar[int]
    ENABLE_VTPM_FIELD_NUMBER: _ClassVar[int]
    ENABLE_INTEGRITY_MONITORING_FIELD_NUMBER: _ClassVar[int]
    enable_secure_boot: bool
    enable_vtpm: bool
    enable_integrity_monitoring: bool
    def __init__(self, enable_secure_boot: bool = ..., enable_vtpm: bool = ..., enable_integrity_monitoring: bool = ...) -> None: ...

class ConfidentialInstanceConfig(_message.Message):
    __slots__ = ("enable_confidential_compute",)
    ENABLE_CONFIDENTIAL_COMPUTE_FIELD_NUMBER: _ClassVar[int]
    enable_confidential_compute: bool
    def __init__(self, enable_confidential_compute: bool = ...) -> None: ...

class InstanceGroupConfig(_message.Message):
    __slots__ = ("num_instances", "instance_names", "instance_references", "image_uri", "machine_type_uri", "disk_config", "is_preemptible", "preemptibility", "managed_group_config", "accelerators", "min_cpu_platform", "min_num_instances", "instance_flexibility_policy", "startup_config")
    class Preemptibility(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PREEMPTIBILITY_UNSPECIFIED: _ClassVar[InstanceGroupConfig.Preemptibility]
        NON_PREEMPTIBLE: _ClassVar[InstanceGroupConfig.Preemptibility]
        PREEMPTIBLE: _ClassVar[InstanceGroupConfig.Preemptibility]
        SPOT: _ClassVar[InstanceGroupConfig.Preemptibility]
    PREEMPTIBILITY_UNSPECIFIED: InstanceGroupConfig.Preemptibility
    NON_PREEMPTIBLE: InstanceGroupConfig.Preemptibility
    PREEMPTIBLE: InstanceGroupConfig.Preemptibility
    SPOT: InstanceGroupConfig.Preemptibility
    NUM_INSTANCES_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_NAMES_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_REFERENCES_FIELD_NUMBER: _ClassVar[int]
    IMAGE_URI_FIELD_NUMBER: _ClassVar[int]
    MACHINE_TYPE_URI_FIELD_NUMBER: _ClassVar[int]
    DISK_CONFIG_FIELD_NUMBER: _ClassVar[int]
    IS_PREEMPTIBLE_FIELD_NUMBER: _ClassVar[int]
    PREEMPTIBILITY_FIELD_NUMBER: _ClassVar[int]
    MANAGED_GROUP_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ACCELERATORS_FIELD_NUMBER: _ClassVar[int]
    MIN_CPU_PLATFORM_FIELD_NUMBER: _ClassVar[int]
    MIN_NUM_INSTANCES_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FLEXIBILITY_POLICY_FIELD_NUMBER: _ClassVar[int]
    STARTUP_CONFIG_FIELD_NUMBER: _ClassVar[int]
    num_instances: int
    instance_names: _containers.RepeatedScalarFieldContainer[str]
    instance_references: _containers.RepeatedCompositeFieldContainer[InstanceReference]
    image_uri: str
    machine_type_uri: str
    disk_config: DiskConfig
    is_preemptible: bool
    preemptibility: InstanceGroupConfig.Preemptibility
    managed_group_config: ManagedGroupConfig
    accelerators: _containers.RepeatedCompositeFieldContainer[AcceleratorConfig]
    min_cpu_platform: str
    min_num_instances: int
    instance_flexibility_policy: InstanceFlexibilityPolicy
    startup_config: StartupConfig
    def __init__(self, num_instances: _Optional[int] = ..., instance_names: _Optional[_Iterable[str]] = ..., instance_references: _Optional[_Iterable[_Union[InstanceReference, _Mapping]]] = ..., image_uri: _Optional[str] = ..., machine_type_uri: _Optional[str] = ..., disk_config: _Optional[_Union[DiskConfig, _Mapping]] = ..., is_preemptible: bool = ..., preemptibility: _Optional[_Union[InstanceGroupConfig.Preemptibility, str]] = ..., managed_group_config: _Optional[_Union[ManagedGroupConfig, _Mapping]] = ..., accelerators: _Optional[_Iterable[_Union[AcceleratorConfig, _Mapping]]] = ..., min_cpu_platform: _Optional[str] = ..., min_num_instances: _Optional[int] = ..., instance_flexibility_policy: _Optional[_Union[InstanceFlexibilityPolicy, _Mapping]] = ..., startup_config: _Optional[_Union[StartupConfig, _Mapping]] = ...) -> None: ...

class StartupConfig(_message.Message):
    __slots__ = ("required_registration_fraction",)
    REQUIRED_REGISTRATION_FRACTION_FIELD_NUMBER: _ClassVar[int]
    required_registration_fraction: float
    def __init__(self, required_registration_fraction: _Optional[float] = ...) -> None: ...

class InstanceReference(_message.Message):
    __slots__ = ("instance_name", "instance_id", "public_key", "public_ecies_key")
    INSTANCE_NAME_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_ECIES_KEY_FIELD_NUMBER: _ClassVar[int]
    instance_name: str
    instance_id: str
    public_key: str
    public_ecies_key: str
    def __init__(self, instance_name: _Optional[str] = ..., instance_id: _Optional[str] = ..., public_key: _Optional[str] = ..., public_ecies_key: _Optional[str] = ...) -> None: ...

class ManagedGroupConfig(_message.Message):
    __slots__ = ("instance_template_name", "instance_group_manager_name", "instance_group_manager_uri")
    INSTANCE_TEMPLATE_NAME_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_GROUP_MANAGER_NAME_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_GROUP_MANAGER_URI_FIELD_NUMBER: _ClassVar[int]
    instance_template_name: str
    instance_group_manager_name: str
    instance_group_manager_uri: str
    def __init__(self, instance_template_name: _Optional[str] = ..., instance_group_manager_name: _Optional[str] = ..., instance_group_manager_uri: _Optional[str] = ...) -> None: ...

class InstanceFlexibilityPolicy(_message.Message):
    __slots__ = ("provisioning_model_mix", "instance_selection_list", "instance_selection_results")
    class ProvisioningModelMix(_message.Message):
        __slots__ = ("standard_capacity_base", "standard_capacity_percent_above_base")
        STANDARD_CAPACITY_BASE_FIELD_NUMBER: _ClassVar[int]
        STANDARD_CAPACITY_PERCENT_ABOVE_BASE_FIELD_NUMBER: _ClassVar[int]
        standard_capacity_base: int
        standard_capacity_percent_above_base: int
        def __init__(self, standard_capacity_base: _Optional[int] = ..., standard_capacity_percent_above_base: _Optional[int] = ...) -> None: ...
    class InstanceSelection(_message.Message):
        __slots__ = ("machine_types", "rank")
        MACHINE_TYPES_FIELD_NUMBER: _ClassVar[int]
        RANK_FIELD_NUMBER: _ClassVar[int]
        machine_types: _containers.RepeatedScalarFieldContainer[str]
        rank: int
        def __init__(self, machine_types: _Optional[_Iterable[str]] = ..., rank: _Optional[int] = ...) -> None: ...
    class InstanceSelectionResult(_message.Message):
        __slots__ = ("machine_type", "vm_count")
        MACHINE_TYPE_FIELD_NUMBER: _ClassVar[int]
        VM_COUNT_FIELD_NUMBER: _ClassVar[int]
        machine_type: str
        vm_count: int
        def __init__(self, machine_type: _Optional[str] = ..., vm_count: _Optional[int] = ...) -> None: ...
    PROVISIONING_MODEL_MIX_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_SELECTION_LIST_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_SELECTION_RESULTS_FIELD_NUMBER: _ClassVar[int]
    provisioning_model_mix: InstanceFlexibilityPolicy.ProvisioningModelMix
    instance_selection_list: _containers.RepeatedCompositeFieldContainer[InstanceFlexibilityPolicy.InstanceSelection]
    instance_selection_results: _containers.RepeatedCompositeFieldContainer[InstanceFlexibilityPolicy.InstanceSelectionResult]
    def __init__(self, provisioning_model_mix: _Optional[_Union[InstanceFlexibilityPolicy.ProvisioningModelMix, _Mapping]] = ..., instance_selection_list: _Optional[_Iterable[_Union[InstanceFlexibilityPolicy.InstanceSelection, _Mapping]]] = ..., instance_selection_results: _Optional[_Iterable[_Union[InstanceFlexibilityPolicy.InstanceSelectionResult, _Mapping]]] = ...) -> None: ...

class AcceleratorConfig(_message.Message):
    __slots__ = ("accelerator_type_uri", "accelerator_count")
    ACCELERATOR_TYPE_URI_FIELD_NUMBER: _ClassVar[int]
    ACCELERATOR_COUNT_FIELD_NUMBER: _ClassVar[int]
    accelerator_type_uri: str
    accelerator_count: int
    def __init__(self, accelerator_type_uri: _Optional[str] = ..., accelerator_count: _Optional[int] = ...) -> None: ...

class DiskConfig(_message.Message):
    __slots__ = ("boot_disk_type", "boot_disk_size_gb", "num_local_ssds", "local_ssd_interface", "boot_disk_provisioned_iops", "boot_disk_provisioned_throughput")
    BOOT_DISK_TYPE_FIELD_NUMBER: _ClassVar[int]
    BOOT_DISK_SIZE_GB_FIELD_NUMBER: _ClassVar[int]
    NUM_LOCAL_SSDS_FIELD_NUMBER: _ClassVar[int]
    LOCAL_SSD_INTERFACE_FIELD_NUMBER: _ClassVar[int]
    BOOT_DISK_PROVISIONED_IOPS_FIELD_NUMBER: _ClassVar[int]
    BOOT_DISK_PROVISIONED_THROUGHPUT_FIELD_NUMBER: _ClassVar[int]
    boot_disk_type: str
    boot_disk_size_gb: int
    num_local_ssds: int
    local_ssd_interface: str
    boot_disk_provisioned_iops: int
    boot_disk_provisioned_throughput: int
    def __init__(self, boot_disk_type: _Optional[str] = ..., boot_disk_size_gb: _Optional[int] = ..., num_local_ssds: _Optional[int] = ..., local_ssd_interface: _Optional[str] = ..., boot_disk_provisioned_iops: _Optional[int] = ..., boot_disk_provisioned_throughput: _Optional[int] = ...) -> None: ...

class AuxiliaryNodeGroup(_message.Message):
    __slots__ = ("node_group", "node_group_id")
    NODE_GROUP_FIELD_NUMBER: _ClassVar[int]
    NODE_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    node_group: NodeGroup
    node_group_id: str
    def __init__(self, node_group: _Optional[_Union[NodeGroup, _Mapping]] = ..., node_group_id: _Optional[str] = ...) -> None: ...

class NodeGroup(_message.Message):
    __slots__ = ("name", "roles", "node_group_config", "labels")
    class Role(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ROLE_UNSPECIFIED: _ClassVar[NodeGroup.Role]
        DRIVER: _ClassVar[NodeGroup.Role]
    ROLE_UNSPECIFIED: NodeGroup.Role
    DRIVER: NodeGroup.Role
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    ROLES_FIELD_NUMBER: _ClassVar[int]
    NODE_GROUP_CONFIG_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    name: str
    roles: _containers.RepeatedScalarFieldContainer[NodeGroup.Role]
    node_group_config: InstanceGroupConfig
    labels: _containers.ScalarMap[str, str]
    def __init__(self, name: _Optional[str] = ..., roles: _Optional[_Iterable[_Union[NodeGroup.Role, str]]] = ..., node_group_config: _Optional[_Union[InstanceGroupConfig, _Mapping]] = ..., labels: _Optional[_Mapping[str, str]] = ...) -> None: ...

class NodeInitializationAction(_message.Message):
    __slots__ = ("executable_file", "execution_timeout")
    EXECUTABLE_FILE_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    executable_file: str
    execution_timeout: _duration_pb2.Duration
    def __init__(self, executable_file: _Optional[str] = ..., execution_timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...

class ClusterStatus(_message.Message):
    __slots__ = ("state", "detail", "state_start_time", "substate")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[ClusterStatus.State]
        CREATING: _ClassVar[ClusterStatus.State]
        RUNNING: _ClassVar[ClusterStatus.State]
        ERROR: _ClassVar[ClusterStatus.State]
        ERROR_DUE_TO_UPDATE: _ClassVar[ClusterStatus.State]
        DELETING: _ClassVar[ClusterStatus.State]
        UPDATING: _ClassVar[ClusterStatus.State]
        STOPPING: _ClassVar[ClusterStatus.State]
        STOPPED: _ClassVar[ClusterStatus.State]
        STARTING: _ClassVar[ClusterStatus.State]
        REPAIRING: _ClassVar[ClusterStatus.State]
    UNKNOWN: ClusterStatus.State
    CREATING: ClusterStatus.State
    RUNNING: ClusterStatus.State
    ERROR: ClusterStatus.State
    ERROR_DUE_TO_UPDATE: ClusterStatus.State
    DELETING: ClusterStatus.State
    UPDATING: ClusterStatus.State
    STOPPING: ClusterStatus.State
    STOPPED: ClusterStatus.State
    STARTING: ClusterStatus.State
    REPAIRING: ClusterStatus.State
    class Substate(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ClusterStatus.Substate]
        UNHEALTHY: _ClassVar[ClusterStatus.Substate]
        STALE_STATUS: _ClassVar[ClusterStatus.Substate]
    UNSPECIFIED: ClusterStatus.Substate
    UNHEALTHY: ClusterStatus.Substate
    STALE_STATUS: ClusterStatus.Substate
    STATE_FIELD_NUMBER: _ClassVar[int]
    DETAIL_FIELD_NUMBER: _ClassVar[int]
    STATE_START_TIME_FIELD_NUMBER: _ClassVar[int]
    SUBSTATE_FIELD_NUMBER: _ClassVar[int]
    state: ClusterStatus.State
    detail: str
    state_start_time: _timestamp_pb2.Timestamp
    substate: ClusterStatus.Substate
    def __init__(self, state: _Optional[_Union[ClusterStatus.State, str]] = ..., detail: _Optional[str] = ..., state_start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., substate: _Optional[_Union[ClusterStatus.Substate, str]] = ...) -> None: ...

class SecurityConfig(_message.Message):
    __slots__ = ("kerberos_config", "identity_config")
    KERBEROS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_CONFIG_FIELD_NUMBER: _ClassVar[int]
    kerberos_config: KerberosConfig
    identity_config: IdentityConfig
    def __init__(self, kerberos_config: _Optional[_Union[KerberosConfig, _Mapping]] = ..., identity_config: _Optional[_Union[IdentityConfig, _Mapping]] = ...) -> None: ...

class KerberosConfig(_message.Message):
    __slots__ = ("enable_kerberos", "root_principal_password_uri", "kms_key_uri", "keystore_uri", "truststore_uri", "keystore_password_uri", "key_password_uri", "truststore_password_uri", "cross_realm_trust_realm", "cross_realm_trust_kdc", "cross_realm_trust_admin_server", "cross_realm_trust_shared_password_uri", "kdc_db_key_uri", "tgt_lifetime_hours", "realm")
    ENABLE_KERBEROS_FIELD_NUMBER: _ClassVar[int]
    ROOT_PRINCIPAL_PASSWORD_URI_FIELD_NUMBER: _ClassVar[int]
    KMS_KEY_URI_FIELD_NUMBER: _ClassVar[int]
    KEYSTORE_URI_FIELD_NUMBER: _ClassVar[int]
    TRUSTSTORE_URI_FIELD_NUMBER: _ClassVar[int]
    KEYSTORE_PASSWORD_URI_FIELD_NUMBER: _ClassVar[int]
    KEY_PASSWORD_URI_FIELD_NUMBER: _ClassVar[int]
    TRUSTSTORE_PASSWORD_URI_FIELD_NUMBER: _ClassVar[int]
    CROSS_REALM_TRUST_REALM_FIELD_NUMBER: _ClassVar[int]
    CROSS_REALM_TRUST_KDC_FIELD_NUMBER: _ClassVar[int]
    CROSS_REALM_TRUST_ADMIN_SERVER_FIELD_NUMBER: _ClassVar[int]
    CROSS_REALM_TRUST_SHARED_PASSWORD_URI_FIELD_NUMBER: _ClassVar[int]
    KDC_DB_KEY_URI_FIELD_NUMBER: _ClassVar[int]
    TGT_LIFETIME_HOURS_FIELD_NUMBER: _ClassVar[int]
    REALM_FIELD_NUMBER: _ClassVar[int]
    enable_kerberos: bool
    root_principal_password_uri: str
    kms_key_uri: str
    keystore_uri: str
    truststore_uri: str
    keystore_password_uri: str
    key_password_uri: str
    truststore_password_uri: str
    cross_realm_trust_realm: str
    cross_realm_trust_kdc: str
    cross_realm_trust_admin_server: str
    cross_realm_trust_shared_password_uri: str
    kdc_db_key_uri: str
    tgt_lifetime_hours: int
    realm: str
    def __init__(self, enable_kerberos: bool = ..., root_principal_password_uri: _Optional[str] = ..., kms_key_uri: _Optional[str] = ..., keystore_uri: _Optional[str] = ..., truststore_uri: _Optional[str] = ..., keystore_password_uri: _Optional[str] = ..., key_password_uri: _Optional[str] = ..., truststore_password_uri: _Optional[str] = ..., cross_realm_trust_realm: _Optional[str] = ..., cross_realm_trust_kdc: _Optional[str] = ..., cross_realm_trust_admin_server: _Optional[str] = ..., cross_realm_trust_shared_password_uri: _Optional[str] = ..., kdc_db_key_uri: _Optional[str] = ..., tgt_lifetime_hours: _Optional[int] = ..., realm: _Optional[str] = ...) -> None: ...

class IdentityConfig(_message.Message):
    __slots__ = ("user_service_account_mapping",)
    class UserServiceAccountMappingEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    USER_SERVICE_ACCOUNT_MAPPING_FIELD_NUMBER: _ClassVar[int]
    user_service_account_mapping: _containers.ScalarMap[str, str]
    def __init__(self, user_service_account_mapping: _Optional[_Mapping[str, str]] = ...) -> None: ...

class SoftwareConfig(_message.Message):
    __slots__ = ("image_version", "properties", "optional_components")
    class PropertiesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    IMAGE_VERSION_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_COMPONENTS_FIELD_NUMBER: _ClassVar[int]
    image_version: str
    properties: _containers.ScalarMap[str, str]
    optional_components: _containers.RepeatedScalarFieldContainer[_shared_pb2.Component]
    def __init__(self, image_version: _Optional[str] = ..., properties: _Optional[_Mapping[str, str]] = ..., optional_components: _Optional[_Iterable[_Union[_shared_pb2.Component, str]]] = ...) -> None: ...

class LifecycleConfig(_message.Message):
    __slots__ = ("idle_delete_ttl", "auto_delete_time", "auto_delete_ttl", "idle_start_time")
    IDLE_DELETE_TTL_FIELD_NUMBER: _ClassVar[int]
    AUTO_DELETE_TIME_FIELD_NUMBER: _ClassVar[int]
    AUTO_DELETE_TTL_FIELD_NUMBER: _ClassVar[int]
    IDLE_START_TIME_FIELD_NUMBER: _ClassVar[int]
    idle_delete_ttl: _duration_pb2.Duration
    auto_delete_time: _timestamp_pb2.Timestamp
    auto_delete_ttl: _duration_pb2.Duration
    idle_start_time: _timestamp_pb2.Timestamp
    def __init__(self, idle_delete_ttl: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., auto_delete_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., auto_delete_ttl: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., idle_start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class MetastoreConfig(_message.Message):
    __slots__ = ("dataproc_metastore_service",)
    DATAPROC_METASTORE_SERVICE_FIELD_NUMBER: _ClassVar[int]
    dataproc_metastore_service: str
    def __init__(self, dataproc_metastore_service: _Optional[str] = ...) -> None: ...

class ClusterMetrics(_message.Message):
    __slots__ = ("hdfs_metrics", "yarn_metrics")
    class HdfsMetricsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    class YarnMetricsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    HDFS_METRICS_FIELD_NUMBER: _ClassVar[int]
    YARN_METRICS_FIELD_NUMBER: _ClassVar[int]
    hdfs_metrics: _containers.ScalarMap[str, int]
    yarn_metrics: _containers.ScalarMap[str, int]
    def __init__(self, hdfs_metrics: _Optional[_Mapping[str, int]] = ..., yarn_metrics: _Optional[_Mapping[str, int]] = ...) -> None: ...

class DataprocMetricConfig(_message.Message):
    __slots__ = ("metrics",)
    class MetricSource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        METRIC_SOURCE_UNSPECIFIED: _ClassVar[DataprocMetricConfig.MetricSource]
        MONITORING_AGENT_DEFAULTS: _ClassVar[DataprocMetricConfig.MetricSource]
        HDFS: _ClassVar[DataprocMetricConfig.MetricSource]
        SPARK: _ClassVar[DataprocMetricConfig.MetricSource]
        YARN: _ClassVar[DataprocMetricConfig.MetricSource]
        SPARK_HISTORY_SERVER: _ClassVar[DataprocMetricConfig.MetricSource]
        HIVESERVER2: _ClassVar[DataprocMetricConfig.MetricSource]
        HIVEMETASTORE: _ClassVar[DataprocMetricConfig.MetricSource]
        FLINK: _ClassVar[DataprocMetricConfig.MetricSource]
    METRIC_SOURCE_UNSPECIFIED: DataprocMetricConfig.MetricSource
    MONITORING_AGENT_DEFAULTS: DataprocMetricConfig.MetricSource
    HDFS: DataprocMetricConfig.MetricSource
    SPARK: DataprocMetricConfig.MetricSource
    YARN: DataprocMetricConfig.MetricSource
    SPARK_HISTORY_SERVER: DataprocMetricConfig.MetricSource
    HIVESERVER2: DataprocMetricConfig.MetricSource
    HIVEMETASTORE: DataprocMetricConfig.MetricSource
    FLINK: DataprocMetricConfig.MetricSource
    class Metric(_message.Message):
        __slots__ = ("metric_source", "metric_overrides")
        METRIC_SOURCE_FIELD_NUMBER: _ClassVar[int]
        METRIC_OVERRIDES_FIELD_NUMBER: _ClassVar[int]
        metric_source: DataprocMetricConfig.MetricSource
        metric_overrides: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, metric_source: _Optional[_Union[DataprocMetricConfig.MetricSource, str]] = ..., metric_overrides: _Optional[_Iterable[str]] = ...) -> None: ...
    METRICS_FIELD_NUMBER: _ClassVar[int]
    metrics: _containers.RepeatedCompositeFieldContainer[DataprocMetricConfig.Metric]
    def __init__(self, metrics: _Optional[_Iterable[_Union[DataprocMetricConfig.Metric, _Mapping]]] = ...) -> None: ...

class CreateClusterRequest(_message.Message):
    __slots__ = ("project_id", "region", "cluster", "request_id", "action_on_failed_primary_workers")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    ACTION_ON_FAILED_PRIMARY_WORKERS_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    region: str
    cluster: Cluster
    request_id: str
    action_on_failed_primary_workers: _shared_pb2.FailureAction
    def __init__(self, project_id: _Optional[str] = ..., region: _Optional[str] = ..., cluster: _Optional[_Union[Cluster, _Mapping]] = ..., request_id: _Optional[str] = ..., action_on_failed_primary_workers: _Optional[_Union[_shared_pb2.FailureAction, str]] = ...) -> None: ...

class UpdateClusterRequest(_message.Message):
    __slots__ = ("project_id", "region", "cluster_name", "cluster", "graceful_decommission_timeout", "update_mask", "request_id")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_NAME_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_FIELD_NUMBER: _ClassVar[int]
    GRACEFUL_DECOMMISSION_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    region: str
    cluster_name: str
    cluster: Cluster
    graceful_decommission_timeout: _duration_pb2.Duration
    update_mask: _field_mask_pb2.FieldMask
    request_id: str
    def __init__(self, project_id: _Optional[str] = ..., region: _Optional[str] = ..., cluster_name: _Optional[str] = ..., cluster: _Optional[_Union[Cluster, _Mapping]] = ..., graceful_decommission_timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., request_id: _Optional[str] = ...) -> None: ...

class StopClusterRequest(_message.Message):
    __slots__ = ("project_id", "region", "cluster_name", "cluster_uuid", "request_id")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_NAME_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_UUID_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    region: str
    cluster_name: str
    cluster_uuid: str
    request_id: str
    def __init__(self, project_id: _Optional[str] = ..., region: _Optional[str] = ..., cluster_name: _Optional[str] = ..., cluster_uuid: _Optional[str] = ..., request_id: _Optional[str] = ...) -> None: ...

class StartClusterRequest(_message.Message):
    __slots__ = ("project_id", "region", "cluster_name", "cluster_uuid", "request_id")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_NAME_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_UUID_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    region: str
    cluster_name: str
    cluster_uuid: str
    request_id: str
    def __init__(self, project_id: _Optional[str] = ..., region: _Optional[str] = ..., cluster_name: _Optional[str] = ..., cluster_uuid: _Optional[str] = ..., request_id: _Optional[str] = ...) -> None: ...

class DeleteClusterRequest(_message.Message):
    __slots__ = ("project_id", "region", "cluster_name", "cluster_uuid", "request_id")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_NAME_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_UUID_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    region: str
    cluster_name: str
    cluster_uuid: str
    request_id: str
    def __init__(self, project_id: _Optional[str] = ..., region: _Optional[str] = ..., cluster_name: _Optional[str] = ..., cluster_uuid: _Optional[str] = ..., request_id: _Optional[str] = ...) -> None: ...

class GetClusterRequest(_message.Message):
    __slots__ = ("project_id", "region", "cluster_name")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_NAME_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    region: str
    cluster_name: str
    def __init__(self, project_id: _Optional[str] = ..., region: _Optional[str] = ..., cluster_name: _Optional[str] = ...) -> None: ...

class ListClustersRequest(_message.Message):
    __slots__ = ("project_id", "region", "filter", "page_size", "page_token")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    region: str
    filter: str
    page_size: int
    page_token: str
    def __init__(self, project_id: _Optional[str] = ..., region: _Optional[str] = ..., filter: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListClustersResponse(_message.Message):
    __slots__ = ("clusters", "next_page_token")
    CLUSTERS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    clusters: _containers.RepeatedCompositeFieldContainer[Cluster]
    next_page_token: str
    def __init__(self, clusters: _Optional[_Iterable[_Union[Cluster, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class DiagnoseClusterRequest(_message.Message):
    __slots__ = ("project_id", "region", "cluster_name", "tarball_gcs_dir", "tarball_access", "diagnosis_interval", "jobs", "yarn_application_ids")
    class TarballAccess(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TARBALL_ACCESS_UNSPECIFIED: _ClassVar[DiagnoseClusterRequest.TarballAccess]
        GOOGLE_CLOUD_SUPPORT: _ClassVar[DiagnoseClusterRequest.TarballAccess]
        GOOGLE_DATAPROC_DIAGNOSE: _ClassVar[DiagnoseClusterRequest.TarballAccess]
    TARBALL_ACCESS_UNSPECIFIED: DiagnoseClusterRequest.TarballAccess
    GOOGLE_CLOUD_SUPPORT: DiagnoseClusterRequest.TarballAccess
    GOOGLE_DATAPROC_DIAGNOSE: DiagnoseClusterRequest.TarballAccess
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_NAME_FIELD_NUMBER: _ClassVar[int]
    TARBALL_GCS_DIR_FIELD_NUMBER: _ClassVar[int]
    TARBALL_ACCESS_FIELD_NUMBER: _ClassVar[int]
    DIAGNOSIS_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    JOBS_FIELD_NUMBER: _ClassVar[int]
    YARN_APPLICATION_IDS_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    region: str
    cluster_name: str
    tarball_gcs_dir: str
    tarball_access: DiagnoseClusterRequest.TarballAccess
    diagnosis_interval: _interval_pb2.Interval
    jobs: _containers.RepeatedScalarFieldContainer[str]
    yarn_application_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, project_id: _Optional[str] = ..., region: _Optional[str] = ..., cluster_name: _Optional[str] = ..., tarball_gcs_dir: _Optional[str] = ..., tarball_access: _Optional[_Union[DiagnoseClusterRequest.TarballAccess, str]] = ..., diagnosis_interval: _Optional[_Union[_interval_pb2.Interval, _Mapping]] = ..., jobs: _Optional[_Iterable[str]] = ..., yarn_application_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class DiagnoseClusterResults(_message.Message):
    __slots__ = ("output_uri",)
    OUTPUT_URI_FIELD_NUMBER: _ClassVar[int]
    output_uri: str
    def __init__(self, output_uri: _Optional[str] = ...) -> None: ...

class ReservationAffinity(_message.Message):
    __slots__ = ("consume_reservation_type", "key", "values")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[ReservationAffinity.Type]
        NO_RESERVATION: _ClassVar[ReservationAffinity.Type]
        ANY_RESERVATION: _ClassVar[ReservationAffinity.Type]
        SPECIFIC_RESERVATION: _ClassVar[ReservationAffinity.Type]
    TYPE_UNSPECIFIED: ReservationAffinity.Type
    NO_RESERVATION: ReservationAffinity.Type
    ANY_RESERVATION: ReservationAffinity.Type
    SPECIFIC_RESERVATION: ReservationAffinity.Type
    CONSUME_RESERVATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    consume_reservation_type: ReservationAffinity.Type
    key: str
    values: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, consume_reservation_type: _Optional[_Union[ReservationAffinity.Type, str]] = ..., key: _Optional[str] = ..., values: _Optional[_Iterable[str]] = ...) -> None: ...
