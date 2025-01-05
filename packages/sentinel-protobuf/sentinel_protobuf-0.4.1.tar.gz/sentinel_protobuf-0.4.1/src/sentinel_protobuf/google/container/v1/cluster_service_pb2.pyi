from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.rpc import code_pb2 as _code_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PrivateIPv6GoogleAccess(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PRIVATE_IPV6_GOOGLE_ACCESS_UNSPECIFIED: _ClassVar[PrivateIPv6GoogleAccess]
    PRIVATE_IPV6_GOOGLE_ACCESS_DISABLED: _ClassVar[PrivateIPv6GoogleAccess]
    PRIVATE_IPV6_GOOGLE_ACCESS_TO_GOOGLE: _ClassVar[PrivateIPv6GoogleAccess]
    PRIVATE_IPV6_GOOGLE_ACCESS_BIDIRECTIONAL: _ClassVar[PrivateIPv6GoogleAccess]

class UpgradeResourceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UPGRADE_RESOURCE_TYPE_UNSPECIFIED: _ClassVar[UpgradeResourceType]
    MASTER: _ClassVar[UpgradeResourceType]
    NODE_POOL: _ClassVar[UpgradeResourceType]

class DatapathProvider(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DATAPATH_PROVIDER_UNSPECIFIED: _ClassVar[DatapathProvider]
    LEGACY_DATAPATH: _ClassVar[DatapathProvider]
    ADVANCED_DATAPATH: _ClassVar[DatapathProvider]

class NodePoolUpdateStrategy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NODE_POOL_UPDATE_STRATEGY_UNSPECIFIED: _ClassVar[NodePoolUpdateStrategy]
    BLUE_GREEN: _ClassVar[NodePoolUpdateStrategy]
    SURGE: _ClassVar[NodePoolUpdateStrategy]

class StackType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STACK_TYPE_UNSPECIFIED: _ClassVar[StackType]
    IPV4: _ClassVar[StackType]
    IPV4_IPV6: _ClassVar[StackType]

class IPv6AccessType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    IPV6_ACCESS_TYPE_UNSPECIFIED: _ClassVar[IPv6AccessType]
    INTERNAL: _ClassVar[IPv6AccessType]
    EXTERNAL: _ClassVar[IPv6AccessType]

class InTransitEncryptionConfig(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    IN_TRANSIT_ENCRYPTION_CONFIG_UNSPECIFIED: _ClassVar[InTransitEncryptionConfig]
    IN_TRANSIT_ENCRYPTION_DISABLED: _ClassVar[InTransitEncryptionConfig]
    IN_TRANSIT_ENCRYPTION_INTER_NODE_TRANSPARENT: _ClassVar[InTransitEncryptionConfig]
PRIVATE_IPV6_GOOGLE_ACCESS_UNSPECIFIED: PrivateIPv6GoogleAccess
PRIVATE_IPV6_GOOGLE_ACCESS_DISABLED: PrivateIPv6GoogleAccess
PRIVATE_IPV6_GOOGLE_ACCESS_TO_GOOGLE: PrivateIPv6GoogleAccess
PRIVATE_IPV6_GOOGLE_ACCESS_BIDIRECTIONAL: PrivateIPv6GoogleAccess
UPGRADE_RESOURCE_TYPE_UNSPECIFIED: UpgradeResourceType
MASTER: UpgradeResourceType
NODE_POOL: UpgradeResourceType
DATAPATH_PROVIDER_UNSPECIFIED: DatapathProvider
LEGACY_DATAPATH: DatapathProvider
ADVANCED_DATAPATH: DatapathProvider
NODE_POOL_UPDATE_STRATEGY_UNSPECIFIED: NodePoolUpdateStrategy
BLUE_GREEN: NodePoolUpdateStrategy
SURGE: NodePoolUpdateStrategy
STACK_TYPE_UNSPECIFIED: StackType
IPV4: StackType
IPV4_IPV6: StackType
IPV6_ACCESS_TYPE_UNSPECIFIED: IPv6AccessType
INTERNAL: IPv6AccessType
EXTERNAL: IPv6AccessType
IN_TRANSIT_ENCRYPTION_CONFIG_UNSPECIFIED: InTransitEncryptionConfig
IN_TRANSIT_ENCRYPTION_DISABLED: InTransitEncryptionConfig
IN_TRANSIT_ENCRYPTION_INTER_NODE_TRANSPARENT: InTransitEncryptionConfig

class LinuxNodeConfig(_message.Message):
    __slots__ = ("sysctls", "cgroup_mode", "hugepages")
    class CgroupMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CGROUP_MODE_UNSPECIFIED: _ClassVar[LinuxNodeConfig.CgroupMode]
        CGROUP_MODE_V1: _ClassVar[LinuxNodeConfig.CgroupMode]
        CGROUP_MODE_V2: _ClassVar[LinuxNodeConfig.CgroupMode]
    CGROUP_MODE_UNSPECIFIED: LinuxNodeConfig.CgroupMode
    CGROUP_MODE_V1: LinuxNodeConfig.CgroupMode
    CGROUP_MODE_V2: LinuxNodeConfig.CgroupMode
    class HugepagesConfig(_message.Message):
        __slots__ = ("hugepage_size2m", "hugepage_size1g")
        HUGEPAGE_SIZE2M_FIELD_NUMBER: _ClassVar[int]
        HUGEPAGE_SIZE1G_FIELD_NUMBER: _ClassVar[int]
        hugepage_size2m: int
        hugepage_size1g: int
        def __init__(self, hugepage_size2m: _Optional[int] = ..., hugepage_size1g: _Optional[int] = ...) -> None: ...
    class SysctlsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    SYSCTLS_FIELD_NUMBER: _ClassVar[int]
    CGROUP_MODE_FIELD_NUMBER: _ClassVar[int]
    HUGEPAGES_FIELD_NUMBER: _ClassVar[int]
    sysctls: _containers.ScalarMap[str, str]
    cgroup_mode: LinuxNodeConfig.CgroupMode
    hugepages: LinuxNodeConfig.HugepagesConfig
    def __init__(self, sysctls: _Optional[_Mapping[str, str]] = ..., cgroup_mode: _Optional[_Union[LinuxNodeConfig.CgroupMode, str]] = ..., hugepages: _Optional[_Union[LinuxNodeConfig.HugepagesConfig, _Mapping]] = ...) -> None: ...

class WindowsNodeConfig(_message.Message):
    __slots__ = ("os_version",)
    class OSVersion(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        OS_VERSION_UNSPECIFIED: _ClassVar[WindowsNodeConfig.OSVersion]
        OS_VERSION_LTSC2019: _ClassVar[WindowsNodeConfig.OSVersion]
        OS_VERSION_LTSC2022: _ClassVar[WindowsNodeConfig.OSVersion]
    OS_VERSION_UNSPECIFIED: WindowsNodeConfig.OSVersion
    OS_VERSION_LTSC2019: WindowsNodeConfig.OSVersion
    OS_VERSION_LTSC2022: WindowsNodeConfig.OSVersion
    OS_VERSION_FIELD_NUMBER: _ClassVar[int]
    os_version: WindowsNodeConfig.OSVersion
    def __init__(self, os_version: _Optional[_Union[WindowsNodeConfig.OSVersion, str]] = ...) -> None: ...

class NodeKubeletConfig(_message.Message):
    __slots__ = ("cpu_manager_policy", "cpu_cfs_quota", "cpu_cfs_quota_period", "pod_pids_limit", "insecure_kubelet_readonly_port_enabled")
    CPU_MANAGER_POLICY_FIELD_NUMBER: _ClassVar[int]
    CPU_CFS_QUOTA_FIELD_NUMBER: _ClassVar[int]
    CPU_CFS_QUOTA_PERIOD_FIELD_NUMBER: _ClassVar[int]
    POD_PIDS_LIMIT_FIELD_NUMBER: _ClassVar[int]
    INSECURE_KUBELET_READONLY_PORT_ENABLED_FIELD_NUMBER: _ClassVar[int]
    cpu_manager_policy: str
    cpu_cfs_quota: _wrappers_pb2.BoolValue
    cpu_cfs_quota_period: str
    pod_pids_limit: int
    insecure_kubelet_readonly_port_enabled: bool
    def __init__(self, cpu_manager_policy: _Optional[str] = ..., cpu_cfs_quota: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., cpu_cfs_quota_period: _Optional[str] = ..., pod_pids_limit: _Optional[int] = ..., insecure_kubelet_readonly_port_enabled: bool = ...) -> None: ...

class NodeConfig(_message.Message):
    __slots__ = ("machine_type", "disk_size_gb", "oauth_scopes", "service_account", "metadata", "image_type", "labels", "local_ssd_count", "tags", "preemptible", "accelerators", "disk_type", "min_cpu_platform", "workload_metadata_config", "taints", "sandbox_config", "node_group", "reservation_affinity", "shielded_instance_config", "linux_node_config", "kubelet_config", "boot_disk_kms_key", "gcfs_config", "advanced_machine_features", "gvnic", "spot", "confidential_nodes", "fast_socket", "resource_labels", "logging_config", "windows_node_config", "local_nvme_ssd_block_config", "ephemeral_storage_local_ssd_config", "sole_tenant_config", "containerd_config", "resource_manager_tags", "enable_confidential_storage", "secondary_boot_disks", "storage_pools", "secondary_boot_disk_update_strategy", "local_ssd_encryption_mode", "effective_cgroup_mode")
    class LocalSsdEncryptionMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        LOCAL_SSD_ENCRYPTION_MODE_UNSPECIFIED: _ClassVar[NodeConfig.LocalSsdEncryptionMode]
        STANDARD_ENCRYPTION: _ClassVar[NodeConfig.LocalSsdEncryptionMode]
        EPHEMERAL_KEY_ENCRYPTION: _ClassVar[NodeConfig.LocalSsdEncryptionMode]
    LOCAL_SSD_ENCRYPTION_MODE_UNSPECIFIED: NodeConfig.LocalSsdEncryptionMode
    STANDARD_ENCRYPTION: NodeConfig.LocalSsdEncryptionMode
    EPHEMERAL_KEY_ENCRYPTION: NodeConfig.LocalSsdEncryptionMode
    class EffectiveCgroupMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        EFFECTIVE_CGROUP_MODE_UNSPECIFIED: _ClassVar[NodeConfig.EffectiveCgroupMode]
        EFFECTIVE_CGROUP_MODE_V1: _ClassVar[NodeConfig.EffectiveCgroupMode]
        EFFECTIVE_CGROUP_MODE_V2: _ClassVar[NodeConfig.EffectiveCgroupMode]
    EFFECTIVE_CGROUP_MODE_UNSPECIFIED: NodeConfig.EffectiveCgroupMode
    EFFECTIVE_CGROUP_MODE_V1: NodeConfig.EffectiveCgroupMode
    EFFECTIVE_CGROUP_MODE_V2: NodeConfig.EffectiveCgroupMode
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class ResourceLabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    MACHINE_TYPE_FIELD_NUMBER: _ClassVar[int]
    DISK_SIZE_GB_FIELD_NUMBER: _ClassVar[int]
    OAUTH_SCOPES_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    IMAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    LOCAL_SSD_COUNT_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    PREEMPTIBLE_FIELD_NUMBER: _ClassVar[int]
    ACCELERATORS_FIELD_NUMBER: _ClassVar[int]
    DISK_TYPE_FIELD_NUMBER: _ClassVar[int]
    MIN_CPU_PLATFORM_FIELD_NUMBER: _ClassVar[int]
    WORKLOAD_METADATA_CONFIG_FIELD_NUMBER: _ClassVar[int]
    TAINTS_FIELD_NUMBER: _ClassVar[int]
    SANDBOX_CONFIG_FIELD_NUMBER: _ClassVar[int]
    NODE_GROUP_FIELD_NUMBER: _ClassVar[int]
    RESERVATION_AFFINITY_FIELD_NUMBER: _ClassVar[int]
    SHIELDED_INSTANCE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    LINUX_NODE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    KUBELET_CONFIG_FIELD_NUMBER: _ClassVar[int]
    BOOT_DISK_KMS_KEY_FIELD_NUMBER: _ClassVar[int]
    GCFS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ADVANCED_MACHINE_FEATURES_FIELD_NUMBER: _ClassVar[int]
    GVNIC_FIELD_NUMBER: _ClassVar[int]
    SPOT_FIELD_NUMBER: _ClassVar[int]
    CONFIDENTIAL_NODES_FIELD_NUMBER: _ClassVar[int]
    FAST_SOCKET_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_LABELS_FIELD_NUMBER: _ClassVar[int]
    LOGGING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    WINDOWS_NODE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    LOCAL_NVME_SSD_BLOCK_CONFIG_FIELD_NUMBER: _ClassVar[int]
    EPHEMERAL_STORAGE_LOCAL_SSD_CONFIG_FIELD_NUMBER: _ClassVar[int]
    SOLE_TENANT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CONTAINERD_CONFIG_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_MANAGER_TAGS_FIELD_NUMBER: _ClassVar[int]
    ENABLE_CONFIDENTIAL_STORAGE_FIELD_NUMBER: _ClassVar[int]
    SECONDARY_BOOT_DISKS_FIELD_NUMBER: _ClassVar[int]
    STORAGE_POOLS_FIELD_NUMBER: _ClassVar[int]
    SECONDARY_BOOT_DISK_UPDATE_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    LOCAL_SSD_ENCRYPTION_MODE_FIELD_NUMBER: _ClassVar[int]
    EFFECTIVE_CGROUP_MODE_FIELD_NUMBER: _ClassVar[int]
    machine_type: str
    disk_size_gb: int
    oauth_scopes: _containers.RepeatedScalarFieldContainer[str]
    service_account: str
    metadata: _containers.ScalarMap[str, str]
    image_type: str
    labels: _containers.ScalarMap[str, str]
    local_ssd_count: int
    tags: _containers.RepeatedScalarFieldContainer[str]
    preemptible: bool
    accelerators: _containers.RepeatedCompositeFieldContainer[AcceleratorConfig]
    disk_type: str
    min_cpu_platform: str
    workload_metadata_config: WorkloadMetadataConfig
    taints: _containers.RepeatedCompositeFieldContainer[NodeTaint]
    sandbox_config: SandboxConfig
    node_group: str
    reservation_affinity: ReservationAffinity
    shielded_instance_config: ShieldedInstanceConfig
    linux_node_config: LinuxNodeConfig
    kubelet_config: NodeKubeletConfig
    boot_disk_kms_key: str
    gcfs_config: GcfsConfig
    advanced_machine_features: AdvancedMachineFeatures
    gvnic: VirtualNIC
    spot: bool
    confidential_nodes: ConfidentialNodes
    fast_socket: FastSocket
    resource_labels: _containers.ScalarMap[str, str]
    logging_config: NodePoolLoggingConfig
    windows_node_config: WindowsNodeConfig
    local_nvme_ssd_block_config: LocalNvmeSsdBlockConfig
    ephemeral_storage_local_ssd_config: EphemeralStorageLocalSsdConfig
    sole_tenant_config: SoleTenantConfig
    containerd_config: ContainerdConfig
    resource_manager_tags: ResourceManagerTags
    enable_confidential_storage: bool
    secondary_boot_disks: _containers.RepeatedCompositeFieldContainer[SecondaryBootDisk]
    storage_pools: _containers.RepeatedScalarFieldContainer[str]
    secondary_boot_disk_update_strategy: SecondaryBootDiskUpdateStrategy
    local_ssd_encryption_mode: NodeConfig.LocalSsdEncryptionMode
    effective_cgroup_mode: NodeConfig.EffectiveCgroupMode
    def __init__(self, machine_type: _Optional[str] = ..., disk_size_gb: _Optional[int] = ..., oauth_scopes: _Optional[_Iterable[str]] = ..., service_account: _Optional[str] = ..., metadata: _Optional[_Mapping[str, str]] = ..., image_type: _Optional[str] = ..., labels: _Optional[_Mapping[str, str]] = ..., local_ssd_count: _Optional[int] = ..., tags: _Optional[_Iterable[str]] = ..., preemptible: bool = ..., accelerators: _Optional[_Iterable[_Union[AcceleratorConfig, _Mapping]]] = ..., disk_type: _Optional[str] = ..., min_cpu_platform: _Optional[str] = ..., workload_metadata_config: _Optional[_Union[WorkloadMetadataConfig, _Mapping]] = ..., taints: _Optional[_Iterable[_Union[NodeTaint, _Mapping]]] = ..., sandbox_config: _Optional[_Union[SandboxConfig, _Mapping]] = ..., node_group: _Optional[str] = ..., reservation_affinity: _Optional[_Union[ReservationAffinity, _Mapping]] = ..., shielded_instance_config: _Optional[_Union[ShieldedInstanceConfig, _Mapping]] = ..., linux_node_config: _Optional[_Union[LinuxNodeConfig, _Mapping]] = ..., kubelet_config: _Optional[_Union[NodeKubeletConfig, _Mapping]] = ..., boot_disk_kms_key: _Optional[str] = ..., gcfs_config: _Optional[_Union[GcfsConfig, _Mapping]] = ..., advanced_machine_features: _Optional[_Union[AdvancedMachineFeatures, _Mapping]] = ..., gvnic: _Optional[_Union[VirtualNIC, _Mapping]] = ..., spot: bool = ..., confidential_nodes: _Optional[_Union[ConfidentialNodes, _Mapping]] = ..., fast_socket: _Optional[_Union[FastSocket, _Mapping]] = ..., resource_labels: _Optional[_Mapping[str, str]] = ..., logging_config: _Optional[_Union[NodePoolLoggingConfig, _Mapping]] = ..., windows_node_config: _Optional[_Union[WindowsNodeConfig, _Mapping]] = ..., local_nvme_ssd_block_config: _Optional[_Union[LocalNvmeSsdBlockConfig, _Mapping]] = ..., ephemeral_storage_local_ssd_config: _Optional[_Union[EphemeralStorageLocalSsdConfig, _Mapping]] = ..., sole_tenant_config: _Optional[_Union[SoleTenantConfig, _Mapping]] = ..., containerd_config: _Optional[_Union[ContainerdConfig, _Mapping]] = ..., resource_manager_tags: _Optional[_Union[ResourceManagerTags, _Mapping]] = ..., enable_confidential_storage: bool = ..., secondary_boot_disks: _Optional[_Iterable[_Union[SecondaryBootDisk, _Mapping]]] = ..., storage_pools: _Optional[_Iterable[str]] = ..., secondary_boot_disk_update_strategy: _Optional[_Union[SecondaryBootDiskUpdateStrategy, _Mapping]] = ..., local_ssd_encryption_mode: _Optional[_Union[NodeConfig.LocalSsdEncryptionMode, str]] = ..., effective_cgroup_mode: _Optional[_Union[NodeConfig.EffectiveCgroupMode, str]] = ...) -> None: ...

class AdvancedMachineFeatures(_message.Message):
    __slots__ = ("threads_per_core", "enable_nested_virtualization")
    THREADS_PER_CORE_FIELD_NUMBER: _ClassVar[int]
    ENABLE_NESTED_VIRTUALIZATION_FIELD_NUMBER: _ClassVar[int]
    threads_per_core: int
    enable_nested_virtualization: bool
    def __init__(self, threads_per_core: _Optional[int] = ..., enable_nested_virtualization: bool = ...) -> None: ...

class NodeNetworkConfig(_message.Message):
    __slots__ = ("create_pod_range", "pod_range", "pod_ipv4_cidr_block", "enable_private_nodes", "network_performance_config", "pod_cidr_overprovision_config", "additional_node_network_configs", "additional_pod_network_configs", "pod_ipv4_range_utilization")
    class NetworkPerformanceConfig(_message.Message):
        __slots__ = ("total_egress_bandwidth_tier",)
        class Tier(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            TIER_UNSPECIFIED: _ClassVar[NodeNetworkConfig.NetworkPerformanceConfig.Tier]
            TIER_1: _ClassVar[NodeNetworkConfig.NetworkPerformanceConfig.Tier]
        TIER_UNSPECIFIED: NodeNetworkConfig.NetworkPerformanceConfig.Tier
        TIER_1: NodeNetworkConfig.NetworkPerformanceConfig.Tier
        TOTAL_EGRESS_BANDWIDTH_TIER_FIELD_NUMBER: _ClassVar[int]
        total_egress_bandwidth_tier: NodeNetworkConfig.NetworkPerformanceConfig.Tier
        def __init__(self, total_egress_bandwidth_tier: _Optional[_Union[NodeNetworkConfig.NetworkPerformanceConfig.Tier, str]] = ...) -> None: ...
    CREATE_POD_RANGE_FIELD_NUMBER: _ClassVar[int]
    POD_RANGE_FIELD_NUMBER: _ClassVar[int]
    POD_IPV4_CIDR_BLOCK_FIELD_NUMBER: _ClassVar[int]
    ENABLE_PRIVATE_NODES_FIELD_NUMBER: _ClassVar[int]
    NETWORK_PERFORMANCE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    POD_CIDR_OVERPROVISION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_NODE_NETWORK_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_POD_NETWORK_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    POD_IPV4_RANGE_UTILIZATION_FIELD_NUMBER: _ClassVar[int]
    create_pod_range: bool
    pod_range: str
    pod_ipv4_cidr_block: str
    enable_private_nodes: bool
    network_performance_config: NodeNetworkConfig.NetworkPerformanceConfig
    pod_cidr_overprovision_config: PodCIDROverprovisionConfig
    additional_node_network_configs: _containers.RepeatedCompositeFieldContainer[AdditionalNodeNetworkConfig]
    additional_pod_network_configs: _containers.RepeatedCompositeFieldContainer[AdditionalPodNetworkConfig]
    pod_ipv4_range_utilization: float
    def __init__(self, create_pod_range: bool = ..., pod_range: _Optional[str] = ..., pod_ipv4_cidr_block: _Optional[str] = ..., enable_private_nodes: bool = ..., network_performance_config: _Optional[_Union[NodeNetworkConfig.NetworkPerformanceConfig, _Mapping]] = ..., pod_cidr_overprovision_config: _Optional[_Union[PodCIDROverprovisionConfig, _Mapping]] = ..., additional_node_network_configs: _Optional[_Iterable[_Union[AdditionalNodeNetworkConfig, _Mapping]]] = ..., additional_pod_network_configs: _Optional[_Iterable[_Union[AdditionalPodNetworkConfig, _Mapping]]] = ..., pod_ipv4_range_utilization: _Optional[float] = ...) -> None: ...

class AdditionalNodeNetworkConfig(_message.Message):
    __slots__ = ("network", "subnetwork")
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    SUBNETWORK_FIELD_NUMBER: _ClassVar[int]
    network: str
    subnetwork: str
    def __init__(self, network: _Optional[str] = ..., subnetwork: _Optional[str] = ...) -> None: ...

class AdditionalPodNetworkConfig(_message.Message):
    __slots__ = ("subnetwork", "secondary_pod_range", "max_pods_per_node")
    SUBNETWORK_FIELD_NUMBER: _ClassVar[int]
    SECONDARY_POD_RANGE_FIELD_NUMBER: _ClassVar[int]
    MAX_PODS_PER_NODE_FIELD_NUMBER: _ClassVar[int]
    subnetwork: str
    secondary_pod_range: str
    max_pods_per_node: MaxPodsConstraint
    def __init__(self, subnetwork: _Optional[str] = ..., secondary_pod_range: _Optional[str] = ..., max_pods_per_node: _Optional[_Union[MaxPodsConstraint, _Mapping]] = ...) -> None: ...

class ShieldedInstanceConfig(_message.Message):
    __slots__ = ("enable_secure_boot", "enable_integrity_monitoring")
    ENABLE_SECURE_BOOT_FIELD_NUMBER: _ClassVar[int]
    ENABLE_INTEGRITY_MONITORING_FIELD_NUMBER: _ClassVar[int]
    enable_secure_boot: bool
    enable_integrity_monitoring: bool
    def __init__(self, enable_secure_boot: bool = ..., enable_integrity_monitoring: bool = ...) -> None: ...

class SandboxConfig(_message.Message):
    __slots__ = ("type",)
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[SandboxConfig.Type]
        GVISOR: _ClassVar[SandboxConfig.Type]
    UNSPECIFIED: SandboxConfig.Type
    GVISOR: SandboxConfig.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    type: SandboxConfig.Type
    def __init__(self, type: _Optional[_Union[SandboxConfig.Type, str]] = ...) -> None: ...

class GcfsConfig(_message.Message):
    __slots__ = ("enabled",)
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    def __init__(self, enabled: bool = ...) -> None: ...

class ReservationAffinity(_message.Message):
    __slots__ = ("consume_reservation_type", "key", "values")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ReservationAffinity.Type]
        NO_RESERVATION: _ClassVar[ReservationAffinity.Type]
        ANY_RESERVATION: _ClassVar[ReservationAffinity.Type]
        SPECIFIC_RESERVATION: _ClassVar[ReservationAffinity.Type]
    UNSPECIFIED: ReservationAffinity.Type
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

class SoleTenantConfig(_message.Message):
    __slots__ = ("node_affinities",)
    class NodeAffinity(_message.Message):
        __slots__ = ("key", "operator", "values")
        class Operator(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            OPERATOR_UNSPECIFIED: _ClassVar[SoleTenantConfig.NodeAffinity.Operator]
            IN: _ClassVar[SoleTenantConfig.NodeAffinity.Operator]
            NOT_IN: _ClassVar[SoleTenantConfig.NodeAffinity.Operator]
        OPERATOR_UNSPECIFIED: SoleTenantConfig.NodeAffinity.Operator
        IN: SoleTenantConfig.NodeAffinity.Operator
        NOT_IN: SoleTenantConfig.NodeAffinity.Operator
        KEY_FIELD_NUMBER: _ClassVar[int]
        OPERATOR_FIELD_NUMBER: _ClassVar[int]
        VALUES_FIELD_NUMBER: _ClassVar[int]
        key: str
        operator: SoleTenantConfig.NodeAffinity.Operator
        values: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, key: _Optional[str] = ..., operator: _Optional[_Union[SoleTenantConfig.NodeAffinity.Operator, str]] = ..., values: _Optional[_Iterable[str]] = ...) -> None: ...
    NODE_AFFINITIES_FIELD_NUMBER: _ClassVar[int]
    node_affinities: _containers.RepeatedCompositeFieldContainer[SoleTenantConfig.NodeAffinity]
    def __init__(self, node_affinities: _Optional[_Iterable[_Union[SoleTenantConfig.NodeAffinity, _Mapping]]] = ...) -> None: ...

class ContainerdConfig(_message.Message):
    __slots__ = ("private_registry_access_config",)
    class PrivateRegistryAccessConfig(_message.Message):
        __slots__ = ("enabled", "certificate_authority_domain_config")
        class CertificateAuthorityDomainConfig(_message.Message):
            __slots__ = ("fqdns", "gcp_secret_manager_certificate_config")
            class GCPSecretManagerCertificateConfig(_message.Message):
                __slots__ = ("secret_uri",)
                SECRET_URI_FIELD_NUMBER: _ClassVar[int]
                secret_uri: str
                def __init__(self, secret_uri: _Optional[str] = ...) -> None: ...
            FQDNS_FIELD_NUMBER: _ClassVar[int]
            GCP_SECRET_MANAGER_CERTIFICATE_CONFIG_FIELD_NUMBER: _ClassVar[int]
            fqdns: _containers.RepeatedScalarFieldContainer[str]
            gcp_secret_manager_certificate_config: ContainerdConfig.PrivateRegistryAccessConfig.CertificateAuthorityDomainConfig.GCPSecretManagerCertificateConfig
            def __init__(self, fqdns: _Optional[_Iterable[str]] = ..., gcp_secret_manager_certificate_config: _Optional[_Union[ContainerdConfig.PrivateRegistryAccessConfig.CertificateAuthorityDomainConfig.GCPSecretManagerCertificateConfig, _Mapping]] = ...) -> None: ...
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        CERTIFICATE_AUTHORITY_DOMAIN_CONFIG_FIELD_NUMBER: _ClassVar[int]
        enabled: bool
        certificate_authority_domain_config: _containers.RepeatedCompositeFieldContainer[ContainerdConfig.PrivateRegistryAccessConfig.CertificateAuthorityDomainConfig]
        def __init__(self, enabled: bool = ..., certificate_authority_domain_config: _Optional[_Iterable[_Union[ContainerdConfig.PrivateRegistryAccessConfig.CertificateAuthorityDomainConfig, _Mapping]]] = ...) -> None: ...
    PRIVATE_REGISTRY_ACCESS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    private_registry_access_config: ContainerdConfig.PrivateRegistryAccessConfig
    def __init__(self, private_registry_access_config: _Optional[_Union[ContainerdConfig.PrivateRegistryAccessConfig, _Mapping]] = ...) -> None: ...

class NodeTaint(_message.Message):
    __slots__ = ("key", "value", "effect")
    class Effect(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        EFFECT_UNSPECIFIED: _ClassVar[NodeTaint.Effect]
        NO_SCHEDULE: _ClassVar[NodeTaint.Effect]
        PREFER_NO_SCHEDULE: _ClassVar[NodeTaint.Effect]
        NO_EXECUTE: _ClassVar[NodeTaint.Effect]
    EFFECT_UNSPECIFIED: NodeTaint.Effect
    NO_SCHEDULE: NodeTaint.Effect
    PREFER_NO_SCHEDULE: NodeTaint.Effect
    NO_EXECUTE: NodeTaint.Effect
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    EFFECT_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: str
    effect: NodeTaint.Effect
    def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ..., effect: _Optional[_Union[NodeTaint.Effect, str]] = ...) -> None: ...

class NodeTaints(_message.Message):
    __slots__ = ("taints",)
    TAINTS_FIELD_NUMBER: _ClassVar[int]
    taints: _containers.RepeatedCompositeFieldContainer[NodeTaint]
    def __init__(self, taints: _Optional[_Iterable[_Union[NodeTaint, _Mapping]]] = ...) -> None: ...

class NodeLabels(_message.Message):
    __slots__ = ("labels",)
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    LABELS_FIELD_NUMBER: _ClassVar[int]
    labels: _containers.ScalarMap[str, str]
    def __init__(self, labels: _Optional[_Mapping[str, str]] = ...) -> None: ...

class ResourceLabels(_message.Message):
    __slots__ = ("labels",)
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    LABELS_FIELD_NUMBER: _ClassVar[int]
    labels: _containers.ScalarMap[str, str]
    def __init__(self, labels: _Optional[_Mapping[str, str]] = ...) -> None: ...

class NetworkTags(_message.Message):
    __slots__ = ("tags",)
    TAGS_FIELD_NUMBER: _ClassVar[int]
    tags: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, tags: _Optional[_Iterable[str]] = ...) -> None: ...

class MasterAuth(_message.Message):
    __slots__ = ("username", "password", "client_certificate_config", "cluster_ca_certificate", "client_certificate", "client_key")
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    CLIENT_CERTIFICATE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_CA_CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    CLIENT_CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    CLIENT_KEY_FIELD_NUMBER: _ClassVar[int]
    username: str
    password: str
    client_certificate_config: ClientCertificateConfig
    cluster_ca_certificate: str
    client_certificate: str
    client_key: str
    def __init__(self, username: _Optional[str] = ..., password: _Optional[str] = ..., client_certificate_config: _Optional[_Union[ClientCertificateConfig, _Mapping]] = ..., cluster_ca_certificate: _Optional[str] = ..., client_certificate: _Optional[str] = ..., client_key: _Optional[str] = ...) -> None: ...

class ClientCertificateConfig(_message.Message):
    __slots__ = ("issue_client_certificate",)
    ISSUE_CLIENT_CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    issue_client_certificate: bool
    def __init__(self, issue_client_certificate: bool = ...) -> None: ...

class AddonsConfig(_message.Message):
    __slots__ = ("http_load_balancing", "horizontal_pod_autoscaling", "kubernetes_dashboard", "network_policy_config", "cloud_run_config", "dns_cache_config", "config_connector_config", "gce_persistent_disk_csi_driver_config", "gcp_filestore_csi_driver_config", "gke_backup_agent_config", "gcs_fuse_csi_driver_config", "stateful_ha_config", "parallelstore_csi_driver_config", "ray_operator_config")
    HTTP_LOAD_BALANCING_FIELD_NUMBER: _ClassVar[int]
    HORIZONTAL_POD_AUTOSCALING_FIELD_NUMBER: _ClassVar[int]
    KUBERNETES_DASHBOARD_FIELD_NUMBER: _ClassVar[int]
    NETWORK_POLICY_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CLOUD_RUN_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DNS_CACHE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CONFIG_CONNECTOR_CONFIG_FIELD_NUMBER: _ClassVar[int]
    GCE_PERSISTENT_DISK_CSI_DRIVER_CONFIG_FIELD_NUMBER: _ClassVar[int]
    GCP_FILESTORE_CSI_DRIVER_CONFIG_FIELD_NUMBER: _ClassVar[int]
    GKE_BACKUP_AGENT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    GCS_FUSE_CSI_DRIVER_CONFIG_FIELD_NUMBER: _ClassVar[int]
    STATEFUL_HA_CONFIG_FIELD_NUMBER: _ClassVar[int]
    PARALLELSTORE_CSI_DRIVER_CONFIG_FIELD_NUMBER: _ClassVar[int]
    RAY_OPERATOR_CONFIG_FIELD_NUMBER: _ClassVar[int]
    http_load_balancing: HttpLoadBalancing
    horizontal_pod_autoscaling: HorizontalPodAutoscaling
    kubernetes_dashboard: KubernetesDashboard
    network_policy_config: NetworkPolicyConfig
    cloud_run_config: CloudRunConfig
    dns_cache_config: DnsCacheConfig
    config_connector_config: ConfigConnectorConfig
    gce_persistent_disk_csi_driver_config: GcePersistentDiskCsiDriverConfig
    gcp_filestore_csi_driver_config: GcpFilestoreCsiDriverConfig
    gke_backup_agent_config: GkeBackupAgentConfig
    gcs_fuse_csi_driver_config: GcsFuseCsiDriverConfig
    stateful_ha_config: StatefulHAConfig
    parallelstore_csi_driver_config: ParallelstoreCsiDriverConfig
    ray_operator_config: RayOperatorConfig
    def __init__(self, http_load_balancing: _Optional[_Union[HttpLoadBalancing, _Mapping]] = ..., horizontal_pod_autoscaling: _Optional[_Union[HorizontalPodAutoscaling, _Mapping]] = ..., kubernetes_dashboard: _Optional[_Union[KubernetesDashboard, _Mapping]] = ..., network_policy_config: _Optional[_Union[NetworkPolicyConfig, _Mapping]] = ..., cloud_run_config: _Optional[_Union[CloudRunConfig, _Mapping]] = ..., dns_cache_config: _Optional[_Union[DnsCacheConfig, _Mapping]] = ..., config_connector_config: _Optional[_Union[ConfigConnectorConfig, _Mapping]] = ..., gce_persistent_disk_csi_driver_config: _Optional[_Union[GcePersistentDiskCsiDriverConfig, _Mapping]] = ..., gcp_filestore_csi_driver_config: _Optional[_Union[GcpFilestoreCsiDriverConfig, _Mapping]] = ..., gke_backup_agent_config: _Optional[_Union[GkeBackupAgentConfig, _Mapping]] = ..., gcs_fuse_csi_driver_config: _Optional[_Union[GcsFuseCsiDriverConfig, _Mapping]] = ..., stateful_ha_config: _Optional[_Union[StatefulHAConfig, _Mapping]] = ..., parallelstore_csi_driver_config: _Optional[_Union[ParallelstoreCsiDriverConfig, _Mapping]] = ..., ray_operator_config: _Optional[_Union[RayOperatorConfig, _Mapping]] = ...) -> None: ...

class HttpLoadBalancing(_message.Message):
    __slots__ = ("disabled",)
    DISABLED_FIELD_NUMBER: _ClassVar[int]
    disabled: bool
    def __init__(self, disabled: bool = ...) -> None: ...

class HorizontalPodAutoscaling(_message.Message):
    __slots__ = ("disabled",)
    DISABLED_FIELD_NUMBER: _ClassVar[int]
    disabled: bool
    def __init__(self, disabled: bool = ...) -> None: ...

class KubernetesDashboard(_message.Message):
    __slots__ = ("disabled",)
    DISABLED_FIELD_NUMBER: _ClassVar[int]
    disabled: bool
    def __init__(self, disabled: bool = ...) -> None: ...

class NetworkPolicyConfig(_message.Message):
    __slots__ = ("disabled",)
    DISABLED_FIELD_NUMBER: _ClassVar[int]
    disabled: bool
    def __init__(self, disabled: bool = ...) -> None: ...

class DnsCacheConfig(_message.Message):
    __slots__ = ("enabled",)
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    def __init__(self, enabled: bool = ...) -> None: ...

class PrivateClusterMasterGlobalAccessConfig(_message.Message):
    __slots__ = ("enabled",)
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    def __init__(self, enabled: bool = ...) -> None: ...

class PrivateClusterConfig(_message.Message):
    __slots__ = ("enable_private_nodes", "enable_private_endpoint", "master_ipv4_cidr_block", "private_endpoint", "public_endpoint", "peering_name", "master_global_access_config", "private_endpoint_subnetwork")
    ENABLE_PRIVATE_NODES_FIELD_NUMBER: _ClassVar[int]
    ENABLE_PRIVATE_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    MASTER_IPV4_CIDR_BLOCK_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    PEERING_NAME_FIELD_NUMBER: _ClassVar[int]
    MASTER_GLOBAL_ACCESS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_ENDPOINT_SUBNETWORK_FIELD_NUMBER: _ClassVar[int]
    enable_private_nodes: bool
    enable_private_endpoint: bool
    master_ipv4_cidr_block: str
    private_endpoint: str
    public_endpoint: str
    peering_name: str
    master_global_access_config: PrivateClusterMasterGlobalAccessConfig
    private_endpoint_subnetwork: str
    def __init__(self, enable_private_nodes: bool = ..., enable_private_endpoint: bool = ..., master_ipv4_cidr_block: _Optional[str] = ..., private_endpoint: _Optional[str] = ..., public_endpoint: _Optional[str] = ..., peering_name: _Optional[str] = ..., master_global_access_config: _Optional[_Union[PrivateClusterMasterGlobalAccessConfig, _Mapping]] = ..., private_endpoint_subnetwork: _Optional[str] = ...) -> None: ...

class AuthenticatorGroupsConfig(_message.Message):
    __slots__ = ("enabled", "security_group")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    SECURITY_GROUP_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    security_group: str
    def __init__(self, enabled: bool = ..., security_group: _Optional[str] = ...) -> None: ...

class CloudRunConfig(_message.Message):
    __slots__ = ("disabled", "load_balancer_type")
    class LoadBalancerType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        LOAD_BALANCER_TYPE_UNSPECIFIED: _ClassVar[CloudRunConfig.LoadBalancerType]
        LOAD_BALANCER_TYPE_EXTERNAL: _ClassVar[CloudRunConfig.LoadBalancerType]
        LOAD_BALANCER_TYPE_INTERNAL: _ClassVar[CloudRunConfig.LoadBalancerType]
    LOAD_BALANCER_TYPE_UNSPECIFIED: CloudRunConfig.LoadBalancerType
    LOAD_BALANCER_TYPE_EXTERNAL: CloudRunConfig.LoadBalancerType
    LOAD_BALANCER_TYPE_INTERNAL: CloudRunConfig.LoadBalancerType
    DISABLED_FIELD_NUMBER: _ClassVar[int]
    LOAD_BALANCER_TYPE_FIELD_NUMBER: _ClassVar[int]
    disabled: bool
    load_balancer_type: CloudRunConfig.LoadBalancerType
    def __init__(self, disabled: bool = ..., load_balancer_type: _Optional[_Union[CloudRunConfig.LoadBalancerType, str]] = ...) -> None: ...

class ConfigConnectorConfig(_message.Message):
    __slots__ = ("enabled",)
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    def __init__(self, enabled: bool = ...) -> None: ...

class GcePersistentDiskCsiDriverConfig(_message.Message):
    __slots__ = ("enabled",)
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    def __init__(self, enabled: bool = ...) -> None: ...

class GcpFilestoreCsiDriverConfig(_message.Message):
    __slots__ = ("enabled",)
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    def __init__(self, enabled: bool = ...) -> None: ...

class GcsFuseCsiDriverConfig(_message.Message):
    __slots__ = ("enabled",)
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    def __init__(self, enabled: bool = ...) -> None: ...

class ParallelstoreCsiDriverConfig(_message.Message):
    __slots__ = ("enabled",)
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    def __init__(self, enabled: bool = ...) -> None: ...

class RayOperatorConfig(_message.Message):
    __slots__ = ("enabled", "ray_cluster_logging_config", "ray_cluster_monitoring_config")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    RAY_CLUSTER_LOGGING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    RAY_CLUSTER_MONITORING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    ray_cluster_logging_config: RayClusterLoggingConfig
    ray_cluster_monitoring_config: RayClusterMonitoringConfig
    def __init__(self, enabled: bool = ..., ray_cluster_logging_config: _Optional[_Union[RayClusterLoggingConfig, _Mapping]] = ..., ray_cluster_monitoring_config: _Optional[_Union[RayClusterMonitoringConfig, _Mapping]] = ...) -> None: ...

class GkeBackupAgentConfig(_message.Message):
    __slots__ = ("enabled",)
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    def __init__(self, enabled: bool = ...) -> None: ...

class StatefulHAConfig(_message.Message):
    __slots__ = ("enabled",)
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    def __init__(self, enabled: bool = ...) -> None: ...

class MasterAuthorizedNetworksConfig(_message.Message):
    __slots__ = ("enabled", "cidr_blocks", "gcp_public_cidrs_access_enabled", "private_endpoint_enforcement_enabled")
    class CidrBlock(_message.Message):
        __slots__ = ("display_name", "cidr_block")
        DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
        CIDR_BLOCK_FIELD_NUMBER: _ClassVar[int]
        display_name: str
        cidr_block: str
        def __init__(self, display_name: _Optional[str] = ..., cidr_block: _Optional[str] = ...) -> None: ...
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    CIDR_BLOCKS_FIELD_NUMBER: _ClassVar[int]
    GCP_PUBLIC_CIDRS_ACCESS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_ENDPOINT_ENFORCEMENT_ENABLED_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    cidr_blocks: _containers.RepeatedCompositeFieldContainer[MasterAuthorizedNetworksConfig.CidrBlock]
    gcp_public_cidrs_access_enabled: bool
    private_endpoint_enforcement_enabled: bool
    def __init__(self, enabled: bool = ..., cidr_blocks: _Optional[_Iterable[_Union[MasterAuthorizedNetworksConfig.CidrBlock, _Mapping]]] = ..., gcp_public_cidrs_access_enabled: bool = ..., private_endpoint_enforcement_enabled: bool = ...) -> None: ...

class LegacyAbac(_message.Message):
    __slots__ = ("enabled",)
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    def __init__(self, enabled: bool = ...) -> None: ...

class NetworkPolicy(_message.Message):
    __slots__ = ("provider", "enabled")
    class Provider(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PROVIDER_UNSPECIFIED: _ClassVar[NetworkPolicy.Provider]
        CALICO: _ClassVar[NetworkPolicy.Provider]
    PROVIDER_UNSPECIFIED: NetworkPolicy.Provider
    CALICO: NetworkPolicy.Provider
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    provider: NetworkPolicy.Provider
    enabled: bool
    def __init__(self, provider: _Optional[_Union[NetworkPolicy.Provider, str]] = ..., enabled: bool = ...) -> None: ...

class BinaryAuthorization(_message.Message):
    __slots__ = ("enabled", "evaluation_mode")
    class EvaluationMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        EVALUATION_MODE_UNSPECIFIED: _ClassVar[BinaryAuthorization.EvaluationMode]
        DISABLED: _ClassVar[BinaryAuthorization.EvaluationMode]
        PROJECT_SINGLETON_POLICY_ENFORCE: _ClassVar[BinaryAuthorization.EvaluationMode]
    EVALUATION_MODE_UNSPECIFIED: BinaryAuthorization.EvaluationMode
    DISABLED: BinaryAuthorization.EvaluationMode
    PROJECT_SINGLETON_POLICY_ENFORCE: BinaryAuthorization.EvaluationMode
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    EVALUATION_MODE_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    evaluation_mode: BinaryAuthorization.EvaluationMode
    def __init__(self, enabled: bool = ..., evaluation_mode: _Optional[_Union[BinaryAuthorization.EvaluationMode, str]] = ...) -> None: ...

class PodCIDROverprovisionConfig(_message.Message):
    __slots__ = ("disable",)
    DISABLE_FIELD_NUMBER: _ClassVar[int]
    disable: bool
    def __init__(self, disable: bool = ...) -> None: ...

class IPAllocationPolicy(_message.Message):
    __slots__ = ("use_ip_aliases", "create_subnetwork", "subnetwork_name", "cluster_ipv4_cidr", "node_ipv4_cidr", "services_ipv4_cidr", "cluster_secondary_range_name", "services_secondary_range_name", "cluster_ipv4_cidr_block", "node_ipv4_cidr_block", "services_ipv4_cidr_block", "tpu_ipv4_cidr_block", "use_routes", "stack_type", "ipv6_access_type", "pod_cidr_overprovision_config", "subnet_ipv6_cidr_block", "services_ipv6_cidr_block", "additional_pod_ranges_config", "default_pod_ipv4_range_utilization")
    USE_IP_ALIASES_FIELD_NUMBER: _ClassVar[int]
    CREATE_SUBNETWORK_FIELD_NUMBER: _ClassVar[int]
    SUBNETWORK_NAME_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_IPV4_CIDR_FIELD_NUMBER: _ClassVar[int]
    NODE_IPV4_CIDR_FIELD_NUMBER: _ClassVar[int]
    SERVICES_IPV4_CIDR_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_SECONDARY_RANGE_NAME_FIELD_NUMBER: _ClassVar[int]
    SERVICES_SECONDARY_RANGE_NAME_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_IPV4_CIDR_BLOCK_FIELD_NUMBER: _ClassVar[int]
    NODE_IPV4_CIDR_BLOCK_FIELD_NUMBER: _ClassVar[int]
    SERVICES_IPV4_CIDR_BLOCK_FIELD_NUMBER: _ClassVar[int]
    TPU_IPV4_CIDR_BLOCK_FIELD_NUMBER: _ClassVar[int]
    USE_ROUTES_FIELD_NUMBER: _ClassVar[int]
    STACK_TYPE_FIELD_NUMBER: _ClassVar[int]
    IPV6_ACCESS_TYPE_FIELD_NUMBER: _ClassVar[int]
    POD_CIDR_OVERPROVISION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    SUBNET_IPV6_CIDR_BLOCK_FIELD_NUMBER: _ClassVar[int]
    SERVICES_IPV6_CIDR_BLOCK_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_POD_RANGES_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_POD_IPV4_RANGE_UTILIZATION_FIELD_NUMBER: _ClassVar[int]
    use_ip_aliases: bool
    create_subnetwork: bool
    subnetwork_name: str
    cluster_ipv4_cidr: str
    node_ipv4_cidr: str
    services_ipv4_cidr: str
    cluster_secondary_range_name: str
    services_secondary_range_name: str
    cluster_ipv4_cidr_block: str
    node_ipv4_cidr_block: str
    services_ipv4_cidr_block: str
    tpu_ipv4_cidr_block: str
    use_routes: bool
    stack_type: StackType
    ipv6_access_type: IPv6AccessType
    pod_cidr_overprovision_config: PodCIDROverprovisionConfig
    subnet_ipv6_cidr_block: str
    services_ipv6_cidr_block: str
    additional_pod_ranges_config: AdditionalPodRangesConfig
    default_pod_ipv4_range_utilization: float
    def __init__(self, use_ip_aliases: bool = ..., create_subnetwork: bool = ..., subnetwork_name: _Optional[str] = ..., cluster_ipv4_cidr: _Optional[str] = ..., node_ipv4_cidr: _Optional[str] = ..., services_ipv4_cidr: _Optional[str] = ..., cluster_secondary_range_name: _Optional[str] = ..., services_secondary_range_name: _Optional[str] = ..., cluster_ipv4_cidr_block: _Optional[str] = ..., node_ipv4_cidr_block: _Optional[str] = ..., services_ipv4_cidr_block: _Optional[str] = ..., tpu_ipv4_cidr_block: _Optional[str] = ..., use_routes: bool = ..., stack_type: _Optional[_Union[StackType, str]] = ..., ipv6_access_type: _Optional[_Union[IPv6AccessType, str]] = ..., pod_cidr_overprovision_config: _Optional[_Union[PodCIDROverprovisionConfig, _Mapping]] = ..., subnet_ipv6_cidr_block: _Optional[str] = ..., services_ipv6_cidr_block: _Optional[str] = ..., additional_pod_ranges_config: _Optional[_Union[AdditionalPodRangesConfig, _Mapping]] = ..., default_pod_ipv4_range_utilization: _Optional[float] = ...) -> None: ...

class Cluster(_message.Message):
    __slots__ = ("name", "description", "initial_node_count", "node_config", "master_auth", "logging_service", "monitoring_service", "network", "cluster_ipv4_cidr", "addons_config", "subnetwork", "node_pools", "locations", "enable_kubernetes_alpha", "resource_labels", "label_fingerprint", "legacy_abac", "network_policy", "ip_allocation_policy", "master_authorized_networks_config", "maintenance_policy", "binary_authorization", "autoscaling", "network_config", "default_max_pods_constraint", "resource_usage_export_config", "authenticator_groups_config", "private_cluster_config", "database_encryption", "vertical_pod_autoscaling", "shielded_nodes", "release_channel", "workload_identity_config", "mesh_certificates", "cost_management_config", "notification_config", "confidential_nodes", "identity_service_config", "self_link", "zone", "endpoint", "initial_cluster_version", "current_master_version", "current_node_version", "create_time", "status", "status_message", "node_ipv4_cidr_size", "services_ipv4_cidr", "instance_group_urls", "current_node_count", "expire_time", "location", "enable_tpu", "tpu_ipv4_cidr_block", "conditions", "autopilot", "id", "node_pool_defaults", "logging_config", "monitoring_config", "node_pool_auto_config", "etag", "fleet", "security_posture_config", "control_plane_endpoints_config", "enable_k8s_beta_apis", "enterprise_config", "secret_manager_config", "compliance_posture_config", "satisfies_pzs", "satisfies_pzi", "user_managed_keys_config", "rbac_binding_config")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATUS_UNSPECIFIED: _ClassVar[Cluster.Status]
        PROVISIONING: _ClassVar[Cluster.Status]
        RUNNING: _ClassVar[Cluster.Status]
        RECONCILING: _ClassVar[Cluster.Status]
        STOPPING: _ClassVar[Cluster.Status]
        ERROR: _ClassVar[Cluster.Status]
        DEGRADED: _ClassVar[Cluster.Status]
    STATUS_UNSPECIFIED: Cluster.Status
    PROVISIONING: Cluster.Status
    RUNNING: Cluster.Status
    RECONCILING: Cluster.Status
    STOPPING: Cluster.Status
    ERROR: Cluster.Status
    DEGRADED: Cluster.Status
    class ResourceLabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    INITIAL_NODE_COUNT_FIELD_NUMBER: _ClassVar[int]
    NODE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    MASTER_AUTH_FIELD_NUMBER: _ClassVar[int]
    LOGGING_SERVICE_FIELD_NUMBER: _ClassVar[int]
    MONITORING_SERVICE_FIELD_NUMBER: _ClassVar[int]
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_IPV4_CIDR_FIELD_NUMBER: _ClassVar[int]
    ADDONS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    SUBNETWORK_FIELD_NUMBER: _ClassVar[int]
    NODE_POOLS_FIELD_NUMBER: _ClassVar[int]
    LOCATIONS_FIELD_NUMBER: _ClassVar[int]
    ENABLE_KUBERNETES_ALPHA_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_LABELS_FIELD_NUMBER: _ClassVar[int]
    LABEL_FINGERPRINT_FIELD_NUMBER: _ClassVar[int]
    LEGACY_ABAC_FIELD_NUMBER: _ClassVar[int]
    NETWORK_POLICY_FIELD_NUMBER: _ClassVar[int]
    IP_ALLOCATION_POLICY_FIELD_NUMBER: _ClassVar[int]
    MASTER_AUTHORIZED_NETWORKS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    MAINTENANCE_POLICY_FIELD_NUMBER: _ClassVar[int]
    BINARY_AUTHORIZATION_FIELD_NUMBER: _ClassVar[int]
    AUTOSCALING_FIELD_NUMBER: _ClassVar[int]
    NETWORK_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_MAX_PODS_CONSTRAINT_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_USAGE_EXPORT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    AUTHENTICATOR_GROUPS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_CLUSTER_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DATABASE_ENCRYPTION_FIELD_NUMBER: _ClassVar[int]
    VERTICAL_POD_AUTOSCALING_FIELD_NUMBER: _ClassVar[int]
    SHIELDED_NODES_FIELD_NUMBER: _ClassVar[int]
    RELEASE_CHANNEL_FIELD_NUMBER: _ClassVar[int]
    WORKLOAD_IDENTITY_CONFIG_FIELD_NUMBER: _ClassVar[int]
    MESH_CERTIFICATES_FIELD_NUMBER: _ClassVar[int]
    COST_MANAGEMENT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CONFIDENTIAL_NODES_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_SERVICE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    SELF_LINK_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    INITIAL_CLUSTER_VERSION_FIELD_NUMBER: _ClassVar[int]
    CURRENT_MASTER_VERSION_FIELD_NUMBER: _ClassVar[int]
    CURRENT_NODE_VERSION_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    STATUS_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    NODE_IPV4_CIDR_SIZE_FIELD_NUMBER: _ClassVar[int]
    SERVICES_IPV4_CIDR_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_GROUP_URLS_FIELD_NUMBER: _ClassVar[int]
    CURRENT_NODE_COUNT_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    ENABLE_TPU_FIELD_NUMBER: _ClassVar[int]
    TPU_IPV4_CIDR_BLOCK_FIELD_NUMBER: _ClassVar[int]
    CONDITIONS_FIELD_NUMBER: _ClassVar[int]
    AUTOPILOT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NODE_POOL_DEFAULTS_FIELD_NUMBER: _ClassVar[int]
    LOGGING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    MONITORING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    NODE_POOL_AUTO_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    FLEET_FIELD_NUMBER: _ClassVar[int]
    SECURITY_POSTURE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CONTROL_PLANE_ENDPOINTS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ENABLE_K8S_BETA_APIS_FIELD_NUMBER: _ClassVar[int]
    ENTERPRISE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    SECRET_MANAGER_CONFIG_FIELD_NUMBER: _ClassVar[int]
    COMPLIANCE_POSTURE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    SATISFIES_PZS_FIELD_NUMBER: _ClassVar[int]
    SATISFIES_PZI_FIELD_NUMBER: _ClassVar[int]
    USER_MANAGED_KEYS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    RBAC_BINDING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    initial_node_count: int
    node_config: NodeConfig
    master_auth: MasterAuth
    logging_service: str
    monitoring_service: str
    network: str
    cluster_ipv4_cidr: str
    addons_config: AddonsConfig
    subnetwork: str
    node_pools: _containers.RepeatedCompositeFieldContainer[NodePool]
    locations: _containers.RepeatedScalarFieldContainer[str]
    enable_kubernetes_alpha: bool
    resource_labels: _containers.ScalarMap[str, str]
    label_fingerprint: str
    legacy_abac: LegacyAbac
    network_policy: NetworkPolicy
    ip_allocation_policy: IPAllocationPolicy
    master_authorized_networks_config: MasterAuthorizedNetworksConfig
    maintenance_policy: MaintenancePolicy
    binary_authorization: BinaryAuthorization
    autoscaling: ClusterAutoscaling
    network_config: NetworkConfig
    default_max_pods_constraint: MaxPodsConstraint
    resource_usage_export_config: ResourceUsageExportConfig
    authenticator_groups_config: AuthenticatorGroupsConfig
    private_cluster_config: PrivateClusterConfig
    database_encryption: DatabaseEncryption
    vertical_pod_autoscaling: VerticalPodAutoscaling
    shielded_nodes: ShieldedNodes
    release_channel: ReleaseChannel
    workload_identity_config: WorkloadIdentityConfig
    mesh_certificates: MeshCertificates
    cost_management_config: CostManagementConfig
    notification_config: NotificationConfig
    confidential_nodes: ConfidentialNodes
    identity_service_config: IdentityServiceConfig
    self_link: str
    zone: str
    endpoint: str
    initial_cluster_version: str
    current_master_version: str
    current_node_version: str
    create_time: str
    status: Cluster.Status
    status_message: str
    node_ipv4_cidr_size: int
    services_ipv4_cidr: str
    instance_group_urls: _containers.RepeatedScalarFieldContainer[str]
    current_node_count: int
    expire_time: str
    location: str
    enable_tpu: bool
    tpu_ipv4_cidr_block: str
    conditions: _containers.RepeatedCompositeFieldContainer[StatusCondition]
    autopilot: Autopilot
    id: str
    node_pool_defaults: NodePoolDefaults
    logging_config: LoggingConfig
    monitoring_config: MonitoringConfig
    node_pool_auto_config: NodePoolAutoConfig
    etag: str
    fleet: Fleet
    security_posture_config: SecurityPostureConfig
    control_plane_endpoints_config: ControlPlaneEndpointsConfig
    enable_k8s_beta_apis: K8sBetaAPIConfig
    enterprise_config: EnterpriseConfig
    secret_manager_config: SecretManagerConfig
    compliance_posture_config: CompliancePostureConfig
    satisfies_pzs: bool
    satisfies_pzi: bool
    user_managed_keys_config: UserManagedKeysConfig
    rbac_binding_config: RBACBindingConfig
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., initial_node_count: _Optional[int] = ..., node_config: _Optional[_Union[NodeConfig, _Mapping]] = ..., master_auth: _Optional[_Union[MasterAuth, _Mapping]] = ..., logging_service: _Optional[str] = ..., monitoring_service: _Optional[str] = ..., network: _Optional[str] = ..., cluster_ipv4_cidr: _Optional[str] = ..., addons_config: _Optional[_Union[AddonsConfig, _Mapping]] = ..., subnetwork: _Optional[str] = ..., node_pools: _Optional[_Iterable[_Union[NodePool, _Mapping]]] = ..., locations: _Optional[_Iterable[str]] = ..., enable_kubernetes_alpha: bool = ..., resource_labels: _Optional[_Mapping[str, str]] = ..., label_fingerprint: _Optional[str] = ..., legacy_abac: _Optional[_Union[LegacyAbac, _Mapping]] = ..., network_policy: _Optional[_Union[NetworkPolicy, _Mapping]] = ..., ip_allocation_policy: _Optional[_Union[IPAllocationPolicy, _Mapping]] = ..., master_authorized_networks_config: _Optional[_Union[MasterAuthorizedNetworksConfig, _Mapping]] = ..., maintenance_policy: _Optional[_Union[MaintenancePolicy, _Mapping]] = ..., binary_authorization: _Optional[_Union[BinaryAuthorization, _Mapping]] = ..., autoscaling: _Optional[_Union[ClusterAutoscaling, _Mapping]] = ..., network_config: _Optional[_Union[NetworkConfig, _Mapping]] = ..., default_max_pods_constraint: _Optional[_Union[MaxPodsConstraint, _Mapping]] = ..., resource_usage_export_config: _Optional[_Union[ResourceUsageExportConfig, _Mapping]] = ..., authenticator_groups_config: _Optional[_Union[AuthenticatorGroupsConfig, _Mapping]] = ..., private_cluster_config: _Optional[_Union[PrivateClusterConfig, _Mapping]] = ..., database_encryption: _Optional[_Union[DatabaseEncryption, _Mapping]] = ..., vertical_pod_autoscaling: _Optional[_Union[VerticalPodAutoscaling, _Mapping]] = ..., shielded_nodes: _Optional[_Union[ShieldedNodes, _Mapping]] = ..., release_channel: _Optional[_Union[ReleaseChannel, _Mapping]] = ..., workload_identity_config: _Optional[_Union[WorkloadIdentityConfig, _Mapping]] = ..., mesh_certificates: _Optional[_Union[MeshCertificates, _Mapping]] = ..., cost_management_config: _Optional[_Union[CostManagementConfig, _Mapping]] = ..., notification_config: _Optional[_Union[NotificationConfig, _Mapping]] = ..., confidential_nodes: _Optional[_Union[ConfidentialNodes, _Mapping]] = ..., identity_service_config: _Optional[_Union[IdentityServiceConfig, _Mapping]] = ..., self_link: _Optional[str] = ..., zone: _Optional[str] = ..., endpoint: _Optional[str] = ..., initial_cluster_version: _Optional[str] = ..., current_master_version: _Optional[str] = ..., current_node_version: _Optional[str] = ..., create_time: _Optional[str] = ..., status: _Optional[_Union[Cluster.Status, str]] = ..., status_message: _Optional[str] = ..., node_ipv4_cidr_size: _Optional[int] = ..., services_ipv4_cidr: _Optional[str] = ..., instance_group_urls: _Optional[_Iterable[str]] = ..., current_node_count: _Optional[int] = ..., expire_time: _Optional[str] = ..., location: _Optional[str] = ..., enable_tpu: bool = ..., tpu_ipv4_cidr_block: _Optional[str] = ..., conditions: _Optional[_Iterable[_Union[StatusCondition, _Mapping]]] = ..., autopilot: _Optional[_Union[Autopilot, _Mapping]] = ..., id: _Optional[str] = ..., node_pool_defaults: _Optional[_Union[NodePoolDefaults, _Mapping]] = ..., logging_config: _Optional[_Union[LoggingConfig, _Mapping]] = ..., monitoring_config: _Optional[_Union[MonitoringConfig, _Mapping]] = ..., node_pool_auto_config: _Optional[_Union[NodePoolAutoConfig, _Mapping]] = ..., etag: _Optional[str] = ..., fleet: _Optional[_Union[Fleet, _Mapping]] = ..., security_posture_config: _Optional[_Union[SecurityPostureConfig, _Mapping]] = ..., control_plane_endpoints_config: _Optional[_Union[ControlPlaneEndpointsConfig, _Mapping]] = ..., enable_k8s_beta_apis: _Optional[_Union[K8sBetaAPIConfig, _Mapping]] = ..., enterprise_config: _Optional[_Union[EnterpriseConfig, _Mapping]] = ..., secret_manager_config: _Optional[_Union[SecretManagerConfig, _Mapping]] = ..., compliance_posture_config: _Optional[_Union[CompliancePostureConfig, _Mapping]] = ..., satisfies_pzs: bool = ..., satisfies_pzi: bool = ..., user_managed_keys_config: _Optional[_Union[UserManagedKeysConfig, _Mapping]] = ..., rbac_binding_config: _Optional[_Union[RBACBindingConfig, _Mapping]] = ...) -> None: ...

class RBACBindingConfig(_message.Message):
    __slots__ = ("enable_insecure_binding_system_unauthenticated", "enable_insecure_binding_system_authenticated")
    ENABLE_INSECURE_BINDING_SYSTEM_UNAUTHENTICATED_FIELD_NUMBER: _ClassVar[int]
    ENABLE_INSECURE_BINDING_SYSTEM_AUTHENTICATED_FIELD_NUMBER: _ClassVar[int]
    enable_insecure_binding_system_unauthenticated: bool
    enable_insecure_binding_system_authenticated: bool
    def __init__(self, enable_insecure_binding_system_unauthenticated: bool = ..., enable_insecure_binding_system_authenticated: bool = ...) -> None: ...

class UserManagedKeysConfig(_message.Message):
    __slots__ = ("cluster_ca", "etcd_api_ca", "etcd_peer_ca", "service_account_signing_keys", "service_account_verification_keys", "aggregation_ca", "control_plane_disk_encryption_key", "gkeops_etcd_backup_encryption_key")
    CLUSTER_CA_FIELD_NUMBER: _ClassVar[int]
    ETCD_API_CA_FIELD_NUMBER: _ClassVar[int]
    ETCD_PEER_CA_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_SIGNING_KEYS_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_VERIFICATION_KEYS_FIELD_NUMBER: _ClassVar[int]
    AGGREGATION_CA_FIELD_NUMBER: _ClassVar[int]
    CONTROL_PLANE_DISK_ENCRYPTION_KEY_FIELD_NUMBER: _ClassVar[int]
    GKEOPS_ETCD_BACKUP_ENCRYPTION_KEY_FIELD_NUMBER: _ClassVar[int]
    cluster_ca: str
    etcd_api_ca: str
    etcd_peer_ca: str
    service_account_signing_keys: _containers.RepeatedScalarFieldContainer[str]
    service_account_verification_keys: _containers.RepeatedScalarFieldContainer[str]
    aggregation_ca: str
    control_plane_disk_encryption_key: str
    gkeops_etcd_backup_encryption_key: str
    def __init__(self, cluster_ca: _Optional[str] = ..., etcd_api_ca: _Optional[str] = ..., etcd_peer_ca: _Optional[str] = ..., service_account_signing_keys: _Optional[_Iterable[str]] = ..., service_account_verification_keys: _Optional[_Iterable[str]] = ..., aggregation_ca: _Optional[str] = ..., control_plane_disk_encryption_key: _Optional[str] = ..., gkeops_etcd_backup_encryption_key: _Optional[str] = ...) -> None: ...

class CompliancePostureConfig(_message.Message):
    __slots__ = ("mode", "compliance_standards")
    class Mode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MODE_UNSPECIFIED: _ClassVar[CompliancePostureConfig.Mode]
        DISABLED: _ClassVar[CompliancePostureConfig.Mode]
        ENABLED: _ClassVar[CompliancePostureConfig.Mode]
    MODE_UNSPECIFIED: CompliancePostureConfig.Mode
    DISABLED: CompliancePostureConfig.Mode
    ENABLED: CompliancePostureConfig.Mode
    class ComplianceStandard(_message.Message):
        __slots__ = ("standard",)
        STANDARD_FIELD_NUMBER: _ClassVar[int]
        standard: str
        def __init__(self, standard: _Optional[str] = ...) -> None: ...
    MODE_FIELD_NUMBER: _ClassVar[int]
    COMPLIANCE_STANDARDS_FIELD_NUMBER: _ClassVar[int]
    mode: CompliancePostureConfig.Mode
    compliance_standards: _containers.RepeatedCompositeFieldContainer[CompliancePostureConfig.ComplianceStandard]
    def __init__(self, mode: _Optional[_Union[CompliancePostureConfig.Mode, str]] = ..., compliance_standards: _Optional[_Iterable[_Union[CompliancePostureConfig.ComplianceStandard, _Mapping]]] = ...) -> None: ...

class K8sBetaAPIConfig(_message.Message):
    __slots__ = ("enabled_apis",)
    ENABLED_APIS_FIELD_NUMBER: _ClassVar[int]
    enabled_apis: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, enabled_apis: _Optional[_Iterable[str]] = ...) -> None: ...

class SecurityPostureConfig(_message.Message):
    __slots__ = ("mode", "vulnerability_mode")
    class Mode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MODE_UNSPECIFIED: _ClassVar[SecurityPostureConfig.Mode]
        DISABLED: _ClassVar[SecurityPostureConfig.Mode]
        BASIC: _ClassVar[SecurityPostureConfig.Mode]
        ENTERPRISE: _ClassVar[SecurityPostureConfig.Mode]
    MODE_UNSPECIFIED: SecurityPostureConfig.Mode
    DISABLED: SecurityPostureConfig.Mode
    BASIC: SecurityPostureConfig.Mode
    ENTERPRISE: SecurityPostureConfig.Mode
    class VulnerabilityMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        VULNERABILITY_MODE_UNSPECIFIED: _ClassVar[SecurityPostureConfig.VulnerabilityMode]
        VULNERABILITY_DISABLED: _ClassVar[SecurityPostureConfig.VulnerabilityMode]
        VULNERABILITY_BASIC: _ClassVar[SecurityPostureConfig.VulnerabilityMode]
        VULNERABILITY_ENTERPRISE: _ClassVar[SecurityPostureConfig.VulnerabilityMode]
    VULNERABILITY_MODE_UNSPECIFIED: SecurityPostureConfig.VulnerabilityMode
    VULNERABILITY_DISABLED: SecurityPostureConfig.VulnerabilityMode
    VULNERABILITY_BASIC: SecurityPostureConfig.VulnerabilityMode
    VULNERABILITY_ENTERPRISE: SecurityPostureConfig.VulnerabilityMode
    MODE_FIELD_NUMBER: _ClassVar[int]
    VULNERABILITY_MODE_FIELD_NUMBER: _ClassVar[int]
    mode: SecurityPostureConfig.Mode
    vulnerability_mode: SecurityPostureConfig.VulnerabilityMode
    def __init__(self, mode: _Optional[_Union[SecurityPostureConfig.Mode, str]] = ..., vulnerability_mode: _Optional[_Union[SecurityPostureConfig.VulnerabilityMode, str]] = ...) -> None: ...

class NodePoolAutoConfig(_message.Message):
    __slots__ = ("network_tags", "resource_manager_tags", "node_kubelet_config", "linux_node_config")
    NETWORK_TAGS_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_MANAGER_TAGS_FIELD_NUMBER: _ClassVar[int]
    NODE_KUBELET_CONFIG_FIELD_NUMBER: _ClassVar[int]
    LINUX_NODE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    network_tags: NetworkTags
    resource_manager_tags: ResourceManagerTags
    node_kubelet_config: NodeKubeletConfig
    linux_node_config: LinuxNodeConfig
    def __init__(self, network_tags: _Optional[_Union[NetworkTags, _Mapping]] = ..., resource_manager_tags: _Optional[_Union[ResourceManagerTags, _Mapping]] = ..., node_kubelet_config: _Optional[_Union[NodeKubeletConfig, _Mapping]] = ..., linux_node_config: _Optional[_Union[LinuxNodeConfig, _Mapping]] = ...) -> None: ...

class NodePoolDefaults(_message.Message):
    __slots__ = ("node_config_defaults",)
    NODE_CONFIG_DEFAULTS_FIELD_NUMBER: _ClassVar[int]
    node_config_defaults: NodeConfigDefaults
    def __init__(self, node_config_defaults: _Optional[_Union[NodeConfigDefaults, _Mapping]] = ...) -> None: ...

class NodeConfigDefaults(_message.Message):
    __slots__ = ("gcfs_config", "logging_config", "containerd_config", "node_kubelet_config")
    GCFS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    LOGGING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CONTAINERD_CONFIG_FIELD_NUMBER: _ClassVar[int]
    NODE_KUBELET_CONFIG_FIELD_NUMBER: _ClassVar[int]
    gcfs_config: GcfsConfig
    logging_config: NodePoolLoggingConfig
    containerd_config: ContainerdConfig
    node_kubelet_config: NodeKubeletConfig
    def __init__(self, gcfs_config: _Optional[_Union[GcfsConfig, _Mapping]] = ..., logging_config: _Optional[_Union[NodePoolLoggingConfig, _Mapping]] = ..., containerd_config: _Optional[_Union[ContainerdConfig, _Mapping]] = ..., node_kubelet_config: _Optional[_Union[NodeKubeletConfig, _Mapping]] = ...) -> None: ...

class ClusterUpdate(_message.Message):
    __slots__ = ("desired_node_version", "desired_monitoring_service", "desired_addons_config", "desired_node_pool_id", "desired_image_type", "desired_database_encryption", "desired_workload_identity_config", "desired_mesh_certificates", "desired_shielded_nodes", "desired_cost_management_config", "desired_dns_config", "desired_node_pool_autoscaling", "desired_locations", "desired_master_authorized_networks_config", "desired_cluster_autoscaling", "desired_binary_authorization", "desired_logging_service", "desired_resource_usage_export_config", "desired_vertical_pod_autoscaling", "desired_private_cluster_config", "desired_intra_node_visibility_config", "desired_default_snat_status", "desired_release_channel", "desired_l4ilb_subsetting_config", "desired_datapath_provider", "desired_private_ipv6_google_access", "desired_notification_config", "desired_authenticator_groups_config", "desired_logging_config", "desired_monitoring_config", "desired_identity_service_config", "desired_service_external_ips_config", "desired_enable_private_endpoint", "desired_default_enable_private_nodes", "desired_control_plane_endpoints_config", "desired_master_version", "desired_gcfs_config", "desired_node_pool_auto_config_network_tags", "desired_gateway_api_config", "etag", "desired_node_pool_logging_config", "desired_fleet", "desired_stack_type", "additional_pod_ranges_config", "removed_additional_pod_ranges_config", "enable_k8s_beta_apis", "desired_security_posture_config", "desired_network_performance_config", "desired_enable_fqdn_network_policy", "desired_autopilot_workload_policy_config", "desired_k8s_beta_apis", "desired_containerd_config", "desired_enable_multi_networking", "desired_node_pool_auto_config_resource_manager_tags", "desired_in_transit_encryption_config", "desired_enable_cilium_clusterwide_network_policy", "desired_secret_manager_config", "desired_compliance_posture_config", "desired_node_kubelet_config", "desired_node_pool_auto_config_kubelet_config", "user_managed_keys_config", "desired_rbac_binding_config", "desired_enterprise_config", "desired_node_pool_auto_config_linux_node_config")
    DESIRED_NODE_VERSION_FIELD_NUMBER: _ClassVar[int]
    DESIRED_MONITORING_SERVICE_FIELD_NUMBER: _ClassVar[int]
    DESIRED_ADDONS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DESIRED_NODE_POOL_ID_FIELD_NUMBER: _ClassVar[int]
    DESIRED_IMAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    DESIRED_DATABASE_ENCRYPTION_FIELD_NUMBER: _ClassVar[int]
    DESIRED_WORKLOAD_IDENTITY_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DESIRED_MESH_CERTIFICATES_FIELD_NUMBER: _ClassVar[int]
    DESIRED_SHIELDED_NODES_FIELD_NUMBER: _ClassVar[int]
    DESIRED_COST_MANAGEMENT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DESIRED_DNS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DESIRED_NODE_POOL_AUTOSCALING_FIELD_NUMBER: _ClassVar[int]
    DESIRED_LOCATIONS_FIELD_NUMBER: _ClassVar[int]
    DESIRED_MASTER_AUTHORIZED_NETWORKS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DESIRED_CLUSTER_AUTOSCALING_FIELD_NUMBER: _ClassVar[int]
    DESIRED_BINARY_AUTHORIZATION_FIELD_NUMBER: _ClassVar[int]
    DESIRED_LOGGING_SERVICE_FIELD_NUMBER: _ClassVar[int]
    DESIRED_RESOURCE_USAGE_EXPORT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DESIRED_VERTICAL_POD_AUTOSCALING_FIELD_NUMBER: _ClassVar[int]
    DESIRED_PRIVATE_CLUSTER_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DESIRED_INTRA_NODE_VISIBILITY_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DESIRED_DEFAULT_SNAT_STATUS_FIELD_NUMBER: _ClassVar[int]
    DESIRED_RELEASE_CHANNEL_FIELD_NUMBER: _ClassVar[int]
    DESIRED_L4ILB_SUBSETTING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DESIRED_DATAPATH_PROVIDER_FIELD_NUMBER: _ClassVar[int]
    DESIRED_PRIVATE_IPV6_GOOGLE_ACCESS_FIELD_NUMBER: _ClassVar[int]
    DESIRED_NOTIFICATION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DESIRED_AUTHENTICATOR_GROUPS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DESIRED_LOGGING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DESIRED_MONITORING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DESIRED_IDENTITY_SERVICE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DESIRED_SERVICE_EXTERNAL_IPS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DESIRED_ENABLE_PRIVATE_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    DESIRED_DEFAULT_ENABLE_PRIVATE_NODES_FIELD_NUMBER: _ClassVar[int]
    DESIRED_CONTROL_PLANE_ENDPOINTS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DESIRED_MASTER_VERSION_FIELD_NUMBER: _ClassVar[int]
    DESIRED_GCFS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DESIRED_NODE_POOL_AUTO_CONFIG_NETWORK_TAGS_FIELD_NUMBER: _ClassVar[int]
    DESIRED_GATEWAY_API_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    DESIRED_NODE_POOL_LOGGING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DESIRED_FLEET_FIELD_NUMBER: _ClassVar[int]
    DESIRED_STACK_TYPE_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_POD_RANGES_CONFIG_FIELD_NUMBER: _ClassVar[int]
    REMOVED_ADDITIONAL_POD_RANGES_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ENABLE_K8S_BETA_APIS_FIELD_NUMBER: _ClassVar[int]
    DESIRED_SECURITY_POSTURE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DESIRED_NETWORK_PERFORMANCE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DESIRED_ENABLE_FQDN_NETWORK_POLICY_FIELD_NUMBER: _ClassVar[int]
    DESIRED_AUTOPILOT_WORKLOAD_POLICY_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DESIRED_K8S_BETA_APIS_FIELD_NUMBER: _ClassVar[int]
    DESIRED_CONTAINERD_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DESIRED_ENABLE_MULTI_NETWORKING_FIELD_NUMBER: _ClassVar[int]
    DESIRED_NODE_POOL_AUTO_CONFIG_RESOURCE_MANAGER_TAGS_FIELD_NUMBER: _ClassVar[int]
    DESIRED_IN_TRANSIT_ENCRYPTION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DESIRED_ENABLE_CILIUM_CLUSTERWIDE_NETWORK_POLICY_FIELD_NUMBER: _ClassVar[int]
    DESIRED_SECRET_MANAGER_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DESIRED_COMPLIANCE_POSTURE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DESIRED_NODE_KUBELET_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DESIRED_NODE_POOL_AUTO_CONFIG_KUBELET_CONFIG_FIELD_NUMBER: _ClassVar[int]
    USER_MANAGED_KEYS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DESIRED_RBAC_BINDING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DESIRED_ENTERPRISE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DESIRED_NODE_POOL_AUTO_CONFIG_LINUX_NODE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    desired_node_version: str
    desired_monitoring_service: str
    desired_addons_config: AddonsConfig
    desired_node_pool_id: str
    desired_image_type: str
    desired_database_encryption: DatabaseEncryption
    desired_workload_identity_config: WorkloadIdentityConfig
    desired_mesh_certificates: MeshCertificates
    desired_shielded_nodes: ShieldedNodes
    desired_cost_management_config: CostManagementConfig
    desired_dns_config: DNSConfig
    desired_node_pool_autoscaling: NodePoolAutoscaling
    desired_locations: _containers.RepeatedScalarFieldContainer[str]
    desired_master_authorized_networks_config: MasterAuthorizedNetworksConfig
    desired_cluster_autoscaling: ClusterAutoscaling
    desired_binary_authorization: BinaryAuthorization
    desired_logging_service: str
    desired_resource_usage_export_config: ResourceUsageExportConfig
    desired_vertical_pod_autoscaling: VerticalPodAutoscaling
    desired_private_cluster_config: PrivateClusterConfig
    desired_intra_node_visibility_config: IntraNodeVisibilityConfig
    desired_default_snat_status: DefaultSnatStatus
    desired_release_channel: ReleaseChannel
    desired_l4ilb_subsetting_config: ILBSubsettingConfig
    desired_datapath_provider: DatapathProvider
    desired_private_ipv6_google_access: PrivateIPv6GoogleAccess
    desired_notification_config: NotificationConfig
    desired_authenticator_groups_config: AuthenticatorGroupsConfig
    desired_logging_config: LoggingConfig
    desired_monitoring_config: MonitoringConfig
    desired_identity_service_config: IdentityServiceConfig
    desired_service_external_ips_config: ServiceExternalIPsConfig
    desired_enable_private_endpoint: bool
    desired_default_enable_private_nodes: bool
    desired_control_plane_endpoints_config: ControlPlaneEndpointsConfig
    desired_master_version: str
    desired_gcfs_config: GcfsConfig
    desired_node_pool_auto_config_network_tags: NetworkTags
    desired_gateway_api_config: GatewayAPIConfig
    etag: str
    desired_node_pool_logging_config: NodePoolLoggingConfig
    desired_fleet: Fleet
    desired_stack_type: StackType
    additional_pod_ranges_config: AdditionalPodRangesConfig
    removed_additional_pod_ranges_config: AdditionalPodRangesConfig
    enable_k8s_beta_apis: K8sBetaAPIConfig
    desired_security_posture_config: SecurityPostureConfig
    desired_network_performance_config: NetworkConfig.ClusterNetworkPerformanceConfig
    desired_enable_fqdn_network_policy: bool
    desired_autopilot_workload_policy_config: WorkloadPolicyConfig
    desired_k8s_beta_apis: K8sBetaAPIConfig
    desired_containerd_config: ContainerdConfig
    desired_enable_multi_networking: bool
    desired_node_pool_auto_config_resource_manager_tags: ResourceManagerTags
    desired_in_transit_encryption_config: InTransitEncryptionConfig
    desired_enable_cilium_clusterwide_network_policy: bool
    desired_secret_manager_config: SecretManagerConfig
    desired_compliance_posture_config: CompliancePostureConfig
    desired_node_kubelet_config: NodeKubeletConfig
    desired_node_pool_auto_config_kubelet_config: NodeKubeletConfig
    user_managed_keys_config: UserManagedKeysConfig
    desired_rbac_binding_config: RBACBindingConfig
    desired_enterprise_config: DesiredEnterpriseConfig
    desired_node_pool_auto_config_linux_node_config: LinuxNodeConfig
    def __init__(self, desired_node_version: _Optional[str] = ..., desired_monitoring_service: _Optional[str] = ..., desired_addons_config: _Optional[_Union[AddonsConfig, _Mapping]] = ..., desired_node_pool_id: _Optional[str] = ..., desired_image_type: _Optional[str] = ..., desired_database_encryption: _Optional[_Union[DatabaseEncryption, _Mapping]] = ..., desired_workload_identity_config: _Optional[_Union[WorkloadIdentityConfig, _Mapping]] = ..., desired_mesh_certificates: _Optional[_Union[MeshCertificates, _Mapping]] = ..., desired_shielded_nodes: _Optional[_Union[ShieldedNodes, _Mapping]] = ..., desired_cost_management_config: _Optional[_Union[CostManagementConfig, _Mapping]] = ..., desired_dns_config: _Optional[_Union[DNSConfig, _Mapping]] = ..., desired_node_pool_autoscaling: _Optional[_Union[NodePoolAutoscaling, _Mapping]] = ..., desired_locations: _Optional[_Iterable[str]] = ..., desired_master_authorized_networks_config: _Optional[_Union[MasterAuthorizedNetworksConfig, _Mapping]] = ..., desired_cluster_autoscaling: _Optional[_Union[ClusterAutoscaling, _Mapping]] = ..., desired_binary_authorization: _Optional[_Union[BinaryAuthorization, _Mapping]] = ..., desired_logging_service: _Optional[str] = ..., desired_resource_usage_export_config: _Optional[_Union[ResourceUsageExportConfig, _Mapping]] = ..., desired_vertical_pod_autoscaling: _Optional[_Union[VerticalPodAutoscaling, _Mapping]] = ..., desired_private_cluster_config: _Optional[_Union[PrivateClusterConfig, _Mapping]] = ..., desired_intra_node_visibility_config: _Optional[_Union[IntraNodeVisibilityConfig, _Mapping]] = ..., desired_default_snat_status: _Optional[_Union[DefaultSnatStatus, _Mapping]] = ..., desired_release_channel: _Optional[_Union[ReleaseChannel, _Mapping]] = ..., desired_l4ilb_subsetting_config: _Optional[_Union[ILBSubsettingConfig, _Mapping]] = ..., desired_datapath_provider: _Optional[_Union[DatapathProvider, str]] = ..., desired_private_ipv6_google_access: _Optional[_Union[PrivateIPv6GoogleAccess, str]] = ..., desired_notification_config: _Optional[_Union[NotificationConfig, _Mapping]] = ..., desired_authenticator_groups_config: _Optional[_Union[AuthenticatorGroupsConfig, _Mapping]] = ..., desired_logging_config: _Optional[_Union[LoggingConfig, _Mapping]] = ..., desired_monitoring_config: _Optional[_Union[MonitoringConfig, _Mapping]] = ..., desired_identity_service_config: _Optional[_Union[IdentityServiceConfig, _Mapping]] = ..., desired_service_external_ips_config: _Optional[_Union[ServiceExternalIPsConfig, _Mapping]] = ..., desired_enable_private_endpoint: bool = ..., desired_default_enable_private_nodes: bool = ..., desired_control_plane_endpoints_config: _Optional[_Union[ControlPlaneEndpointsConfig, _Mapping]] = ..., desired_master_version: _Optional[str] = ..., desired_gcfs_config: _Optional[_Union[GcfsConfig, _Mapping]] = ..., desired_node_pool_auto_config_network_tags: _Optional[_Union[NetworkTags, _Mapping]] = ..., desired_gateway_api_config: _Optional[_Union[GatewayAPIConfig, _Mapping]] = ..., etag: _Optional[str] = ..., desired_node_pool_logging_config: _Optional[_Union[NodePoolLoggingConfig, _Mapping]] = ..., desired_fleet: _Optional[_Union[Fleet, _Mapping]] = ..., desired_stack_type: _Optional[_Union[StackType, str]] = ..., additional_pod_ranges_config: _Optional[_Union[AdditionalPodRangesConfig, _Mapping]] = ..., removed_additional_pod_ranges_config: _Optional[_Union[AdditionalPodRangesConfig, _Mapping]] = ..., enable_k8s_beta_apis: _Optional[_Union[K8sBetaAPIConfig, _Mapping]] = ..., desired_security_posture_config: _Optional[_Union[SecurityPostureConfig, _Mapping]] = ..., desired_network_performance_config: _Optional[_Union[NetworkConfig.ClusterNetworkPerformanceConfig, _Mapping]] = ..., desired_enable_fqdn_network_policy: bool = ..., desired_autopilot_workload_policy_config: _Optional[_Union[WorkloadPolicyConfig, _Mapping]] = ..., desired_k8s_beta_apis: _Optional[_Union[K8sBetaAPIConfig, _Mapping]] = ..., desired_containerd_config: _Optional[_Union[ContainerdConfig, _Mapping]] = ..., desired_enable_multi_networking: bool = ..., desired_node_pool_auto_config_resource_manager_tags: _Optional[_Union[ResourceManagerTags, _Mapping]] = ..., desired_in_transit_encryption_config: _Optional[_Union[InTransitEncryptionConfig, str]] = ..., desired_enable_cilium_clusterwide_network_policy: bool = ..., desired_secret_manager_config: _Optional[_Union[SecretManagerConfig, _Mapping]] = ..., desired_compliance_posture_config: _Optional[_Union[CompliancePostureConfig, _Mapping]] = ..., desired_node_kubelet_config: _Optional[_Union[NodeKubeletConfig, _Mapping]] = ..., desired_node_pool_auto_config_kubelet_config: _Optional[_Union[NodeKubeletConfig, _Mapping]] = ..., user_managed_keys_config: _Optional[_Union[UserManagedKeysConfig, _Mapping]] = ..., desired_rbac_binding_config: _Optional[_Union[RBACBindingConfig, _Mapping]] = ..., desired_enterprise_config: _Optional[_Union[DesiredEnterpriseConfig, _Mapping]] = ..., desired_node_pool_auto_config_linux_node_config: _Optional[_Union[LinuxNodeConfig, _Mapping]] = ...) -> None: ...

class AdditionalPodRangesConfig(_message.Message):
    __slots__ = ("pod_range_names", "pod_range_info")
    POD_RANGE_NAMES_FIELD_NUMBER: _ClassVar[int]
    POD_RANGE_INFO_FIELD_NUMBER: _ClassVar[int]
    pod_range_names: _containers.RepeatedScalarFieldContainer[str]
    pod_range_info: _containers.RepeatedCompositeFieldContainer[RangeInfo]
    def __init__(self, pod_range_names: _Optional[_Iterable[str]] = ..., pod_range_info: _Optional[_Iterable[_Union[RangeInfo, _Mapping]]] = ...) -> None: ...

class RangeInfo(_message.Message):
    __slots__ = ("range_name", "utilization")
    RANGE_NAME_FIELD_NUMBER: _ClassVar[int]
    UTILIZATION_FIELD_NUMBER: _ClassVar[int]
    range_name: str
    utilization: float
    def __init__(self, range_name: _Optional[str] = ..., utilization: _Optional[float] = ...) -> None: ...

class DesiredEnterpriseConfig(_message.Message):
    __slots__ = ("desired_tier",)
    DESIRED_TIER_FIELD_NUMBER: _ClassVar[int]
    desired_tier: EnterpriseConfig.ClusterTier
    def __init__(self, desired_tier: _Optional[_Union[EnterpriseConfig.ClusterTier, str]] = ...) -> None: ...

class Operation(_message.Message):
    __slots__ = ("name", "zone", "operation_type", "status", "detail", "status_message", "self_link", "target_link", "location", "start_time", "end_time", "progress", "cluster_conditions", "nodepool_conditions", "error")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATUS_UNSPECIFIED: _ClassVar[Operation.Status]
        PENDING: _ClassVar[Operation.Status]
        RUNNING: _ClassVar[Operation.Status]
        DONE: _ClassVar[Operation.Status]
        ABORTING: _ClassVar[Operation.Status]
    STATUS_UNSPECIFIED: Operation.Status
    PENDING: Operation.Status
    RUNNING: Operation.Status
    DONE: Operation.Status
    ABORTING: Operation.Status
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[Operation.Type]
        CREATE_CLUSTER: _ClassVar[Operation.Type]
        DELETE_CLUSTER: _ClassVar[Operation.Type]
        UPGRADE_MASTER: _ClassVar[Operation.Type]
        UPGRADE_NODES: _ClassVar[Operation.Type]
        REPAIR_CLUSTER: _ClassVar[Operation.Type]
        UPDATE_CLUSTER: _ClassVar[Operation.Type]
        CREATE_NODE_POOL: _ClassVar[Operation.Type]
        DELETE_NODE_POOL: _ClassVar[Operation.Type]
        SET_NODE_POOL_MANAGEMENT: _ClassVar[Operation.Type]
        AUTO_REPAIR_NODES: _ClassVar[Operation.Type]
        AUTO_UPGRADE_NODES: _ClassVar[Operation.Type]
        SET_LABELS: _ClassVar[Operation.Type]
        SET_MASTER_AUTH: _ClassVar[Operation.Type]
        SET_NODE_POOL_SIZE: _ClassVar[Operation.Type]
        SET_NETWORK_POLICY: _ClassVar[Operation.Type]
        SET_MAINTENANCE_POLICY: _ClassVar[Operation.Type]
        RESIZE_CLUSTER: _ClassVar[Operation.Type]
        FLEET_FEATURE_UPGRADE: _ClassVar[Operation.Type]
    TYPE_UNSPECIFIED: Operation.Type
    CREATE_CLUSTER: Operation.Type
    DELETE_CLUSTER: Operation.Type
    UPGRADE_MASTER: Operation.Type
    UPGRADE_NODES: Operation.Type
    REPAIR_CLUSTER: Operation.Type
    UPDATE_CLUSTER: Operation.Type
    CREATE_NODE_POOL: Operation.Type
    DELETE_NODE_POOL: Operation.Type
    SET_NODE_POOL_MANAGEMENT: Operation.Type
    AUTO_REPAIR_NODES: Operation.Type
    AUTO_UPGRADE_NODES: Operation.Type
    SET_LABELS: Operation.Type
    SET_MASTER_AUTH: Operation.Type
    SET_NODE_POOL_SIZE: Operation.Type
    SET_NETWORK_POLICY: Operation.Type
    SET_MAINTENANCE_POLICY: Operation.Type
    RESIZE_CLUSTER: Operation.Type
    FLEET_FEATURE_UPGRADE: Operation.Type
    NAME_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    OPERATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DETAIL_FIELD_NUMBER: _ClassVar[int]
    STATUS_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SELF_LINK_FIELD_NUMBER: _ClassVar[int]
    TARGET_LINK_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_CONDITIONS_FIELD_NUMBER: _ClassVar[int]
    NODEPOOL_CONDITIONS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    name: str
    zone: str
    operation_type: Operation.Type
    status: Operation.Status
    detail: str
    status_message: str
    self_link: str
    target_link: str
    location: str
    start_time: str
    end_time: str
    progress: OperationProgress
    cluster_conditions: _containers.RepeatedCompositeFieldContainer[StatusCondition]
    nodepool_conditions: _containers.RepeatedCompositeFieldContainer[StatusCondition]
    error: _status_pb2.Status
    def __init__(self, name: _Optional[str] = ..., zone: _Optional[str] = ..., operation_type: _Optional[_Union[Operation.Type, str]] = ..., status: _Optional[_Union[Operation.Status, str]] = ..., detail: _Optional[str] = ..., status_message: _Optional[str] = ..., self_link: _Optional[str] = ..., target_link: _Optional[str] = ..., location: _Optional[str] = ..., start_time: _Optional[str] = ..., end_time: _Optional[str] = ..., progress: _Optional[_Union[OperationProgress, _Mapping]] = ..., cluster_conditions: _Optional[_Iterable[_Union[StatusCondition, _Mapping]]] = ..., nodepool_conditions: _Optional[_Iterable[_Union[StatusCondition, _Mapping]]] = ..., error: _Optional[_Union[_status_pb2.Status, _Mapping]] = ...) -> None: ...

class OperationProgress(_message.Message):
    __slots__ = ("name", "status", "metrics", "stages")
    class Metric(_message.Message):
        __slots__ = ("name", "int_value", "double_value", "string_value")
        NAME_FIELD_NUMBER: _ClassVar[int]
        INT_VALUE_FIELD_NUMBER: _ClassVar[int]
        DOUBLE_VALUE_FIELD_NUMBER: _ClassVar[int]
        STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
        name: str
        int_value: int
        double_value: float
        string_value: str
        def __init__(self, name: _Optional[str] = ..., int_value: _Optional[int] = ..., double_value: _Optional[float] = ..., string_value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    METRICS_FIELD_NUMBER: _ClassVar[int]
    STAGES_FIELD_NUMBER: _ClassVar[int]
    name: str
    status: Operation.Status
    metrics: _containers.RepeatedCompositeFieldContainer[OperationProgress.Metric]
    stages: _containers.RepeatedCompositeFieldContainer[OperationProgress]
    def __init__(self, name: _Optional[str] = ..., status: _Optional[_Union[Operation.Status, str]] = ..., metrics: _Optional[_Iterable[_Union[OperationProgress.Metric, _Mapping]]] = ..., stages: _Optional[_Iterable[_Union[OperationProgress, _Mapping]]] = ...) -> None: ...

class CreateClusterRequest(_message.Message):
    __slots__ = ("project_id", "zone", "cluster", "parent")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    zone: str
    cluster: Cluster
    parent: str
    def __init__(self, project_id: _Optional[str] = ..., zone: _Optional[str] = ..., cluster: _Optional[_Union[Cluster, _Mapping]] = ..., parent: _Optional[str] = ...) -> None: ...

class GetClusterRequest(_message.Message):
    __slots__ = ("project_id", "zone", "cluster_id", "name")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    zone: str
    cluster_id: str
    name: str
    def __init__(self, project_id: _Optional[str] = ..., zone: _Optional[str] = ..., cluster_id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class UpdateClusterRequest(_message.Message):
    __slots__ = ("project_id", "zone", "cluster_id", "update", "name")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    UPDATE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    zone: str
    cluster_id: str
    update: ClusterUpdate
    name: str
    def __init__(self, project_id: _Optional[str] = ..., zone: _Optional[str] = ..., cluster_id: _Optional[str] = ..., update: _Optional[_Union[ClusterUpdate, _Mapping]] = ..., name: _Optional[str] = ...) -> None: ...

class UpdateNodePoolRequest(_message.Message):
    __slots__ = ("project_id", "zone", "cluster_id", "node_pool_id", "node_version", "image_type", "name", "locations", "workload_metadata_config", "upgrade_settings", "tags", "taints", "labels", "linux_node_config", "kubelet_config", "node_network_config", "gcfs_config", "confidential_nodes", "gvnic", "etag", "fast_socket", "logging_config", "resource_labels", "windows_node_config", "accelerators", "machine_type", "disk_type", "disk_size_gb", "resource_manager_tags", "containerd_config", "queued_provisioning", "storage_pools")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_POOL_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_VERSION_FIELD_NUMBER: _ClassVar[int]
    IMAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    LOCATIONS_FIELD_NUMBER: _ClassVar[int]
    WORKLOAD_METADATA_CONFIG_FIELD_NUMBER: _ClassVar[int]
    UPGRADE_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    TAINTS_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    LINUX_NODE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    KUBELET_CONFIG_FIELD_NUMBER: _ClassVar[int]
    NODE_NETWORK_CONFIG_FIELD_NUMBER: _ClassVar[int]
    GCFS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CONFIDENTIAL_NODES_FIELD_NUMBER: _ClassVar[int]
    GVNIC_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    FAST_SOCKET_FIELD_NUMBER: _ClassVar[int]
    LOGGING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_LABELS_FIELD_NUMBER: _ClassVar[int]
    WINDOWS_NODE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ACCELERATORS_FIELD_NUMBER: _ClassVar[int]
    MACHINE_TYPE_FIELD_NUMBER: _ClassVar[int]
    DISK_TYPE_FIELD_NUMBER: _ClassVar[int]
    DISK_SIZE_GB_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_MANAGER_TAGS_FIELD_NUMBER: _ClassVar[int]
    CONTAINERD_CONFIG_FIELD_NUMBER: _ClassVar[int]
    QUEUED_PROVISIONING_FIELD_NUMBER: _ClassVar[int]
    STORAGE_POOLS_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    zone: str
    cluster_id: str
    node_pool_id: str
    node_version: str
    image_type: str
    name: str
    locations: _containers.RepeatedScalarFieldContainer[str]
    workload_metadata_config: WorkloadMetadataConfig
    upgrade_settings: NodePool.UpgradeSettings
    tags: NetworkTags
    taints: NodeTaints
    labels: NodeLabels
    linux_node_config: LinuxNodeConfig
    kubelet_config: NodeKubeletConfig
    node_network_config: NodeNetworkConfig
    gcfs_config: GcfsConfig
    confidential_nodes: ConfidentialNodes
    gvnic: VirtualNIC
    etag: str
    fast_socket: FastSocket
    logging_config: NodePoolLoggingConfig
    resource_labels: ResourceLabels
    windows_node_config: WindowsNodeConfig
    accelerators: _containers.RepeatedCompositeFieldContainer[AcceleratorConfig]
    machine_type: str
    disk_type: str
    disk_size_gb: int
    resource_manager_tags: ResourceManagerTags
    containerd_config: ContainerdConfig
    queued_provisioning: NodePool.QueuedProvisioning
    storage_pools: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, project_id: _Optional[str] = ..., zone: _Optional[str] = ..., cluster_id: _Optional[str] = ..., node_pool_id: _Optional[str] = ..., node_version: _Optional[str] = ..., image_type: _Optional[str] = ..., name: _Optional[str] = ..., locations: _Optional[_Iterable[str]] = ..., workload_metadata_config: _Optional[_Union[WorkloadMetadataConfig, _Mapping]] = ..., upgrade_settings: _Optional[_Union[NodePool.UpgradeSettings, _Mapping]] = ..., tags: _Optional[_Union[NetworkTags, _Mapping]] = ..., taints: _Optional[_Union[NodeTaints, _Mapping]] = ..., labels: _Optional[_Union[NodeLabels, _Mapping]] = ..., linux_node_config: _Optional[_Union[LinuxNodeConfig, _Mapping]] = ..., kubelet_config: _Optional[_Union[NodeKubeletConfig, _Mapping]] = ..., node_network_config: _Optional[_Union[NodeNetworkConfig, _Mapping]] = ..., gcfs_config: _Optional[_Union[GcfsConfig, _Mapping]] = ..., confidential_nodes: _Optional[_Union[ConfidentialNodes, _Mapping]] = ..., gvnic: _Optional[_Union[VirtualNIC, _Mapping]] = ..., etag: _Optional[str] = ..., fast_socket: _Optional[_Union[FastSocket, _Mapping]] = ..., logging_config: _Optional[_Union[NodePoolLoggingConfig, _Mapping]] = ..., resource_labels: _Optional[_Union[ResourceLabels, _Mapping]] = ..., windows_node_config: _Optional[_Union[WindowsNodeConfig, _Mapping]] = ..., accelerators: _Optional[_Iterable[_Union[AcceleratorConfig, _Mapping]]] = ..., machine_type: _Optional[str] = ..., disk_type: _Optional[str] = ..., disk_size_gb: _Optional[int] = ..., resource_manager_tags: _Optional[_Union[ResourceManagerTags, _Mapping]] = ..., containerd_config: _Optional[_Union[ContainerdConfig, _Mapping]] = ..., queued_provisioning: _Optional[_Union[NodePool.QueuedProvisioning, _Mapping]] = ..., storage_pools: _Optional[_Iterable[str]] = ...) -> None: ...

class SetNodePoolAutoscalingRequest(_message.Message):
    __slots__ = ("project_id", "zone", "cluster_id", "node_pool_id", "autoscaling", "name")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_POOL_ID_FIELD_NUMBER: _ClassVar[int]
    AUTOSCALING_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    zone: str
    cluster_id: str
    node_pool_id: str
    autoscaling: NodePoolAutoscaling
    name: str
    def __init__(self, project_id: _Optional[str] = ..., zone: _Optional[str] = ..., cluster_id: _Optional[str] = ..., node_pool_id: _Optional[str] = ..., autoscaling: _Optional[_Union[NodePoolAutoscaling, _Mapping]] = ..., name: _Optional[str] = ...) -> None: ...

class SetLoggingServiceRequest(_message.Message):
    __slots__ = ("project_id", "zone", "cluster_id", "logging_service", "name")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    LOGGING_SERVICE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    zone: str
    cluster_id: str
    logging_service: str
    name: str
    def __init__(self, project_id: _Optional[str] = ..., zone: _Optional[str] = ..., cluster_id: _Optional[str] = ..., logging_service: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class SetMonitoringServiceRequest(_message.Message):
    __slots__ = ("project_id", "zone", "cluster_id", "monitoring_service", "name")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    MONITORING_SERVICE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    zone: str
    cluster_id: str
    monitoring_service: str
    name: str
    def __init__(self, project_id: _Optional[str] = ..., zone: _Optional[str] = ..., cluster_id: _Optional[str] = ..., monitoring_service: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class SetAddonsConfigRequest(_message.Message):
    __slots__ = ("project_id", "zone", "cluster_id", "addons_config", "name")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    ADDONS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    zone: str
    cluster_id: str
    addons_config: AddonsConfig
    name: str
    def __init__(self, project_id: _Optional[str] = ..., zone: _Optional[str] = ..., cluster_id: _Optional[str] = ..., addons_config: _Optional[_Union[AddonsConfig, _Mapping]] = ..., name: _Optional[str] = ...) -> None: ...

class SetLocationsRequest(_message.Message):
    __slots__ = ("project_id", "zone", "cluster_id", "locations", "name")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    LOCATIONS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    zone: str
    cluster_id: str
    locations: _containers.RepeatedScalarFieldContainer[str]
    name: str
    def __init__(self, project_id: _Optional[str] = ..., zone: _Optional[str] = ..., cluster_id: _Optional[str] = ..., locations: _Optional[_Iterable[str]] = ..., name: _Optional[str] = ...) -> None: ...

class UpdateMasterRequest(_message.Message):
    __slots__ = ("project_id", "zone", "cluster_id", "master_version", "name")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    MASTER_VERSION_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    zone: str
    cluster_id: str
    master_version: str
    name: str
    def __init__(self, project_id: _Optional[str] = ..., zone: _Optional[str] = ..., cluster_id: _Optional[str] = ..., master_version: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class SetMasterAuthRequest(_message.Message):
    __slots__ = ("project_id", "zone", "cluster_id", "action", "update", "name")
    class Action(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[SetMasterAuthRequest.Action]
        SET_PASSWORD: _ClassVar[SetMasterAuthRequest.Action]
        GENERATE_PASSWORD: _ClassVar[SetMasterAuthRequest.Action]
        SET_USERNAME: _ClassVar[SetMasterAuthRequest.Action]
    UNKNOWN: SetMasterAuthRequest.Action
    SET_PASSWORD: SetMasterAuthRequest.Action
    GENERATE_PASSWORD: SetMasterAuthRequest.Action
    SET_USERNAME: SetMasterAuthRequest.Action
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    zone: str
    cluster_id: str
    action: SetMasterAuthRequest.Action
    update: MasterAuth
    name: str
    def __init__(self, project_id: _Optional[str] = ..., zone: _Optional[str] = ..., cluster_id: _Optional[str] = ..., action: _Optional[_Union[SetMasterAuthRequest.Action, str]] = ..., update: _Optional[_Union[MasterAuth, _Mapping]] = ..., name: _Optional[str] = ...) -> None: ...

class DeleteClusterRequest(_message.Message):
    __slots__ = ("project_id", "zone", "cluster_id", "name")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    zone: str
    cluster_id: str
    name: str
    def __init__(self, project_id: _Optional[str] = ..., zone: _Optional[str] = ..., cluster_id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class ListClustersRequest(_message.Message):
    __slots__ = ("project_id", "zone", "parent")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    zone: str
    parent: str
    def __init__(self, project_id: _Optional[str] = ..., zone: _Optional[str] = ..., parent: _Optional[str] = ...) -> None: ...

class ListClustersResponse(_message.Message):
    __slots__ = ("clusters", "missing_zones")
    CLUSTERS_FIELD_NUMBER: _ClassVar[int]
    MISSING_ZONES_FIELD_NUMBER: _ClassVar[int]
    clusters: _containers.RepeatedCompositeFieldContainer[Cluster]
    missing_zones: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, clusters: _Optional[_Iterable[_Union[Cluster, _Mapping]]] = ..., missing_zones: _Optional[_Iterable[str]] = ...) -> None: ...

class GetOperationRequest(_message.Message):
    __slots__ = ("project_id", "zone", "operation_id", "name")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    zone: str
    operation_id: str
    name: str
    def __init__(self, project_id: _Optional[str] = ..., zone: _Optional[str] = ..., operation_id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class ListOperationsRequest(_message.Message):
    __slots__ = ("project_id", "zone", "parent")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    zone: str
    parent: str
    def __init__(self, project_id: _Optional[str] = ..., zone: _Optional[str] = ..., parent: _Optional[str] = ...) -> None: ...

class CancelOperationRequest(_message.Message):
    __slots__ = ("project_id", "zone", "operation_id", "name")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    zone: str
    operation_id: str
    name: str
    def __init__(self, project_id: _Optional[str] = ..., zone: _Optional[str] = ..., operation_id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class ListOperationsResponse(_message.Message):
    __slots__ = ("operations", "missing_zones")
    OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    MISSING_ZONES_FIELD_NUMBER: _ClassVar[int]
    operations: _containers.RepeatedCompositeFieldContainer[Operation]
    missing_zones: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, operations: _Optional[_Iterable[_Union[Operation, _Mapping]]] = ..., missing_zones: _Optional[_Iterable[str]] = ...) -> None: ...

class GetServerConfigRequest(_message.Message):
    __slots__ = ("project_id", "zone", "name")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    zone: str
    name: str
    def __init__(self, project_id: _Optional[str] = ..., zone: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class ServerConfig(_message.Message):
    __slots__ = ("default_cluster_version", "valid_node_versions", "default_image_type", "valid_image_types", "valid_master_versions", "channels")
    class ReleaseChannelConfig(_message.Message):
        __slots__ = ("channel", "default_version", "valid_versions", "upgrade_target_version")
        CHANNEL_FIELD_NUMBER: _ClassVar[int]
        DEFAULT_VERSION_FIELD_NUMBER: _ClassVar[int]
        VALID_VERSIONS_FIELD_NUMBER: _ClassVar[int]
        UPGRADE_TARGET_VERSION_FIELD_NUMBER: _ClassVar[int]
        channel: ReleaseChannel.Channel
        default_version: str
        valid_versions: _containers.RepeatedScalarFieldContainer[str]
        upgrade_target_version: str
        def __init__(self, channel: _Optional[_Union[ReleaseChannel.Channel, str]] = ..., default_version: _Optional[str] = ..., valid_versions: _Optional[_Iterable[str]] = ..., upgrade_target_version: _Optional[str] = ...) -> None: ...
    DEFAULT_CLUSTER_VERSION_FIELD_NUMBER: _ClassVar[int]
    VALID_NODE_VERSIONS_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_IMAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    VALID_IMAGE_TYPES_FIELD_NUMBER: _ClassVar[int]
    VALID_MASTER_VERSIONS_FIELD_NUMBER: _ClassVar[int]
    CHANNELS_FIELD_NUMBER: _ClassVar[int]
    default_cluster_version: str
    valid_node_versions: _containers.RepeatedScalarFieldContainer[str]
    default_image_type: str
    valid_image_types: _containers.RepeatedScalarFieldContainer[str]
    valid_master_versions: _containers.RepeatedScalarFieldContainer[str]
    channels: _containers.RepeatedCompositeFieldContainer[ServerConfig.ReleaseChannelConfig]
    def __init__(self, default_cluster_version: _Optional[str] = ..., valid_node_versions: _Optional[_Iterable[str]] = ..., default_image_type: _Optional[str] = ..., valid_image_types: _Optional[_Iterable[str]] = ..., valid_master_versions: _Optional[_Iterable[str]] = ..., channels: _Optional[_Iterable[_Union[ServerConfig.ReleaseChannelConfig, _Mapping]]] = ...) -> None: ...

class CreateNodePoolRequest(_message.Message):
    __slots__ = ("project_id", "zone", "cluster_id", "node_pool", "parent")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_POOL_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    zone: str
    cluster_id: str
    node_pool: NodePool
    parent: str
    def __init__(self, project_id: _Optional[str] = ..., zone: _Optional[str] = ..., cluster_id: _Optional[str] = ..., node_pool: _Optional[_Union[NodePool, _Mapping]] = ..., parent: _Optional[str] = ...) -> None: ...

class DeleteNodePoolRequest(_message.Message):
    __slots__ = ("project_id", "zone", "cluster_id", "node_pool_id", "name")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_POOL_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    zone: str
    cluster_id: str
    node_pool_id: str
    name: str
    def __init__(self, project_id: _Optional[str] = ..., zone: _Optional[str] = ..., cluster_id: _Optional[str] = ..., node_pool_id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class ListNodePoolsRequest(_message.Message):
    __slots__ = ("project_id", "zone", "cluster_id", "parent")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    zone: str
    cluster_id: str
    parent: str
    def __init__(self, project_id: _Optional[str] = ..., zone: _Optional[str] = ..., cluster_id: _Optional[str] = ..., parent: _Optional[str] = ...) -> None: ...

class GetNodePoolRequest(_message.Message):
    __slots__ = ("project_id", "zone", "cluster_id", "node_pool_id", "name")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_POOL_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    zone: str
    cluster_id: str
    node_pool_id: str
    name: str
    def __init__(self, project_id: _Optional[str] = ..., zone: _Optional[str] = ..., cluster_id: _Optional[str] = ..., node_pool_id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class BlueGreenSettings(_message.Message):
    __slots__ = ("standard_rollout_policy", "node_pool_soak_duration")
    class StandardRolloutPolicy(_message.Message):
        __slots__ = ("batch_percentage", "batch_node_count", "batch_soak_duration")
        BATCH_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
        BATCH_NODE_COUNT_FIELD_NUMBER: _ClassVar[int]
        BATCH_SOAK_DURATION_FIELD_NUMBER: _ClassVar[int]
        batch_percentage: float
        batch_node_count: int
        batch_soak_duration: _duration_pb2.Duration
        def __init__(self, batch_percentage: _Optional[float] = ..., batch_node_count: _Optional[int] = ..., batch_soak_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...
    STANDARD_ROLLOUT_POLICY_FIELD_NUMBER: _ClassVar[int]
    NODE_POOL_SOAK_DURATION_FIELD_NUMBER: _ClassVar[int]
    standard_rollout_policy: BlueGreenSettings.StandardRolloutPolicy
    node_pool_soak_duration: _duration_pb2.Duration
    def __init__(self, standard_rollout_policy: _Optional[_Union[BlueGreenSettings.StandardRolloutPolicy, _Mapping]] = ..., node_pool_soak_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...

class NodePool(_message.Message):
    __slots__ = ("name", "config", "initial_node_count", "locations", "network_config", "self_link", "version", "instance_group_urls", "status", "status_message", "autoscaling", "management", "max_pods_constraint", "conditions", "pod_ipv4_cidr_size", "upgrade_settings", "placement_policy", "update_info", "etag", "queued_provisioning", "best_effort_provisioning")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATUS_UNSPECIFIED: _ClassVar[NodePool.Status]
        PROVISIONING: _ClassVar[NodePool.Status]
        RUNNING: _ClassVar[NodePool.Status]
        RUNNING_WITH_ERROR: _ClassVar[NodePool.Status]
        RECONCILING: _ClassVar[NodePool.Status]
        STOPPING: _ClassVar[NodePool.Status]
        ERROR: _ClassVar[NodePool.Status]
    STATUS_UNSPECIFIED: NodePool.Status
    PROVISIONING: NodePool.Status
    RUNNING: NodePool.Status
    RUNNING_WITH_ERROR: NodePool.Status
    RECONCILING: NodePool.Status
    STOPPING: NodePool.Status
    ERROR: NodePool.Status
    class UpgradeSettings(_message.Message):
        __slots__ = ("max_surge", "max_unavailable", "strategy", "blue_green_settings")
        MAX_SURGE_FIELD_NUMBER: _ClassVar[int]
        MAX_UNAVAILABLE_FIELD_NUMBER: _ClassVar[int]
        STRATEGY_FIELD_NUMBER: _ClassVar[int]
        BLUE_GREEN_SETTINGS_FIELD_NUMBER: _ClassVar[int]
        max_surge: int
        max_unavailable: int
        strategy: NodePoolUpdateStrategy
        blue_green_settings: BlueGreenSettings
        def __init__(self, max_surge: _Optional[int] = ..., max_unavailable: _Optional[int] = ..., strategy: _Optional[_Union[NodePoolUpdateStrategy, str]] = ..., blue_green_settings: _Optional[_Union[BlueGreenSettings, _Mapping]] = ...) -> None: ...
    class UpdateInfo(_message.Message):
        __slots__ = ("blue_green_info",)
        class BlueGreenInfo(_message.Message):
            __slots__ = ("phase", "blue_instance_group_urls", "green_instance_group_urls", "blue_pool_deletion_start_time", "green_pool_version")
            class Phase(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                PHASE_UNSPECIFIED: _ClassVar[NodePool.UpdateInfo.BlueGreenInfo.Phase]
                UPDATE_STARTED: _ClassVar[NodePool.UpdateInfo.BlueGreenInfo.Phase]
                CREATING_GREEN_POOL: _ClassVar[NodePool.UpdateInfo.BlueGreenInfo.Phase]
                CORDONING_BLUE_POOL: _ClassVar[NodePool.UpdateInfo.BlueGreenInfo.Phase]
                DRAINING_BLUE_POOL: _ClassVar[NodePool.UpdateInfo.BlueGreenInfo.Phase]
                NODE_POOL_SOAKING: _ClassVar[NodePool.UpdateInfo.BlueGreenInfo.Phase]
                DELETING_BLUE_POOL: _ClassVar[NodePool.UpdateInfo.BlueGreenInfo.Phase]
                ROLLBACK_STARTED: _ClassVar[NodePool.UpdateInfo.BlueGreenInfo.Phase]
            PHASE_UNSPECIFIED: NodePool.UpdateInfo.BlueGreenInfo.Phase
            UPDATE_STARTED: NodePool.UpdateInfo.BlueGreenInfo.Phase
            CREATING_GREEN_POOL: NodePool.UpdateInfo.BlueGreenInfo.Phase
            CORDONING_BLUE_POOL: NodePool.UpdateInfo.BlueGreenInfo.Phase
            DRAINING_BLUE_POOL: NodePool.UpdateInfo.BlueGreenInfo.Phase
            NODE_POOL_SOAKING: NodePool.UpdateInfo.BlueGreenInfo.Phase
            DELETING_BLUE_POOL: NodePool.UpdateInfo.BlueGreenInfo.Phase
            ROLLBACK_STARTED: NodePool.UpdateInfo.BlueGreenInfo.Phase
            PHASE_FIELD_NUMBER: _ClassVar[int]
            BLUE_INSTANCE_GROUP_URLS_FIELD_NUMBER: _ClassVar[int]
            GREEN_INSTANCE_GROUP_URLS_FIELD_NUMBER: _ClassVar[int]
            BLUE_POOL_DELETION_START_TIME_FIELD_NUMBER: _ClassVar[int]
            GREEN_POOL_VERSION_FIELD_NUMBER: _ClassVar[int]
            phase: NodePool.UpdateInfo.BlueGreenInfo.Phase
            blue_instance_group_urls: _containers.RepeatedScalarFieldContainer[str]
            green_instance_group_urls: _containers.RepeatedScalarFieldContainer[str]
            blue_pool_deletion_start_time: str
            green_pool_version: str
            def __init__(self, phase: _Optional[_Union[NodePool.UpdateInfo.BlueGreenInfo.Phase, str]] = ..., blue_instance_group_urls: _Optional[_Iterable[str]] = ..., green_instance_group_urls: _Optional[_Iterable[str]] = ..., blue_pool_deletion_start_time: _Optional[str] = ..., green_pool_version: _Optional[str] = ...) -> None: ...
        BLUE_GREEN_INFO_FIELD_NUMBER: _ClassVar[int]
        blue_green_info: NodePool.UpdateInfo.BlueGreenInfo
        def __init__(self, blue_green_info: _Optional[_Union[NodePool.UpdateInfo.BlueGreenInfo, _Mapping]] = ...) -> None: ...
    class PlacementPolicy(_message.Message):
        __slots__ = ("type", "tpu_topology", "policy_name")
        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            TYPE_UNSPECIFIED: _ClassVar[NodePool.PlacementPolicy.Type]
            COMPACT: _ClassVar[NodePool.PlacementPolicy.Type]
        TYPE_UNSPECIFIED: NodePool.PlacementPolicy.Type
        COMPACT: NodePool.PlacementPolicy.Type
        TYPE_FIELD_NUMBER: _ClassVar[int]
        TPU_TOPOLOGY_FIELD_NUMBER: _ClassVar[int]
        POLICY_NAME_FIELD_NUMBER: _ClassVar[int]
        type: NodePool.PlacementPolicy.Type
        tpu_topology: str
        policy_name: str
        def __init__(self, type: _Optional[_Union[NodePool.PlacementPolicy.Type, str]] = ..., tpu_topology: _Optional[str] = ..., policy_name: _Optional[str] = ...) -> None: ...
    class QueuedProvisioning(_message.Message):
        __slots__ = ("enabled",)
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        enabled: bool
        def __init__(self, enabled: bool = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    INITIAL_NODE_COUNT_FIELD_NUMBER: _ClassVar[int]
    LOCATIONS_FIELD_NUMBER: _ClassVar[int]
    NETWORK_CONFIG_FIELD_NUMBER: _ClassVar[int]
    SELF_LINK_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_GROUP_URLS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    STATUS_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    AUTOSCALING_FIELD_NUMBER: _ClassVar[int]
    MANAGEMENT_FIELD_NUMBER: _ClassVar[int]
    MAX_PODS_CONSTRAINT_FIELD_NUMBER: _ClassVar[int]
    CONDITIONS_FIELD_NUMBER: _ClassVar[int]
    POD_IPV4_CIDR_SIZE_FIELD_NUMBER: _ClassVar[int]
    UPGRADE_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    PLACEMENT_POLICY_FIELD_NUMBER: _ClassVar[int]
    UPDATE_INFO_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    QUEUED_PROVISIONING_FIELD_NUMBER: _ClassVar[int]
    BEST_EFFORT_PROVISIONING_FIELD_NUMBER: _ClassVar[int]
    name: str
    config: NodeConfig
    initial_node_count: int
    locations: _containers.RepeatedScalarFieldContainer[str]
    network_config: NodeNetworkConfig
    self_link: str
    version: str
    instance_group_urls: _containers.RepeatedScalarFieldContainer[str]
    status: NodePool.Status
    status_message: str
    autoscaling: NodePoolAutoscaling
    management: NodeManagement
    max_pods_constraint: MaxPodsConstraint
    conditions: _containers.RepeatedCompositeFieldContainer[StatusCondition]
    pod_ipv4_cidr_size: int
    upgrade_settings: NodePool.UpgradeSettings
    placement_policy: NodePool.PlacementPolicy
    update_info: NodePool.UpdateInfo
    etag: str
    queued_provisioning: NodePool.QueuedProvisioning
    best_effort_provisioning: BestEffortProvisioning
    def __init__(self, name: _Optional[str] = ..., config: _Optional[_Union[NodeConfig, _Mapping]] = ..., initial_node_count: _Optional[int] = ..., locations: _Optional[_Iterable[str]] = ..., network_config: _Optional[_Union[NodeNetworkConfig, _Mapping]] = ..., self_link: _Optional[str] = ..., version: _Optional[str] = ..., instance_group_urls: _Optional[_Iterable[str]] = ..., status: _Optional[_Union[NodePool.Status, str]] = ..., status_message: _Optional[str] = ..., autoscaling: _Optional[_Union[NodePoolAutoscaling, _Mapping]] = ..., management: _Optional[_Union[NodeManagement, _Mapping]] = ..., max_pods_constraint: _Optional[_Union[MaxPodsConstraint, _Mapping]] = ..., conditions: _Optional[_Iterable[_Union[StatusCondition, _Mapping]]] = ..., pod_ipv4_cidr_size: _Optional[int] = ..., upgrade_settings: _Optional[_Union[NodePool.UpgradeSettings, _Mapping]] = ..., placement_policy: _Optional[_Union[NodePool.PlacementPolicy, _Mapping]] = ..., update_info: _Optional[_Union[NodePool.UpdateInfo, _Mapping]] = ..., etag: _Optional[str] = ..., queued_provisioning: _Optional[_Union[NodePool.QueuedProvisioning, _Mapping]] = ..., best_effort_provisioning: _Optional[_Union[BestEffortProvisioning, _Mapping]] = ...) -> None: ...

class NodeManagement(_message.Message):
    __slots__ = ("auto_upgrade", "auto_repair", "upgrade_options")
    AUTO_UPGRADE_FIELD_NUMBER: _ClassVar[int]
    AUTO_REPAIR_FIELD_NUMBER: _ClassVar[int]
    UPGRADE_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    auto_upgrade: bool
    auto_repair: bool
    upgrade_options: AutoUpgradeOptions
    def __init__(self, auto_upgrade: bool = ..., auto_repair: bool = ..., upgrade_options: _Optional[_Union[AutoUpgradeOptions, _Mapping]] = ...) -> None: ...

class BestEffortProvisioning(_message.Message):
    __slots__ = ("enabled", "min_provision_nodes")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    MIN_PROVISION_NODES_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    min_provision_nodes: int
    def __init__(self, enabled: bool = ..., min_provision_nodes: _Optional[int] = ...) -> None: ...

class AutoUpgradeOptions(_message.Message):
    __slots__ = ("auto_upgrade_start_time", "description")
    AUTO_UPGRADE_START_TIME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    auto_upgrade_start_time: str
    description: str
    def __init__(self, auto_upgrade_start_time: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class MaintenancePolicy(_message.Message):
    __slots__ = ("window", "resource_version")
    WINDOW_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_VERSION_FIELD_NUMBER: _ClassVar[int]
    window: MaintenanceWindow
    resource_version: str
    def __init__(self, window: _Optional[_Union[MaintenanceWindow, _Mapping]] = ..., resource_version: _Optional[str] = ...) -> None: ...

class MaintenanceWindow(_message.Message):
    __slots__ = ("daily_maintenance_window", "recurring_window", "maintenance_exclusions")
    class MaintenanceExclusionsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: TimeWindow
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[TimeWindow, _Mapping]] = ...) -> None: ...
    DAILY_MAINTENANCE_WINDOW_FIELD_NUMBER: _ClassVar[int]
    RECURRING_WINDOW_FIELD_NUMBER: _ClassVar[int]
    MAINTENANCE_EXCLUSIONS_FIELD_NUMBER: _ClassVar[int]
    daily_maintenance_window: DailyMaintenanceWindow
    recurring_window: RecurringTimeWindow
    maintenance_exclusions: _containers.MessageMap[str, TimeWindow]
    def __init__(self, daily_maintenance_window: _Optional[_Union[DailyMaintenanceWindow, _Mapping]] = ..., recurring_window: _Optional[_Union[RecurringTimeWindow, _Mapping]] = ..., maintenance_exclusions: _Optional[_Mapping[str, TimeWindow]] = ...) -> None: ...

class TimeWindow(_message.Message):
    __slots__ = ("maintenance_exclusion_options", "start_time", "end_time")
    MAINTENANCE_EXCLUSION_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    maintenance_exclusion_options: MaintenanceExclusionOptions
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    def __init__(self, maintenance_exclusion_options: _Optional[_Union[MaintenanceExclusionOptions, _Mapping]] = ..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class MaintenanceExclusionOptions(_message.Message):
    __slots__ = ("scope",)
    class Scope(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_UPGRADES: _ClassVar[MaintenanceExclusionOptions.Scope]
        NO_MINOR_UPGRADES: _ClassVar[MaintenanceExclusionOptions.Scope]
        NO_MINOR_OR_NODE_UPGRADES: _ClassVar[MaintenanceExclusionOptions.Scope]
    NO_UPGRADES: MaintenanceExclusionOptions.Scope
    NO_MINOR_UPGRADES: MaintenanceExclusionOptions.Scope
    NO_MINOR_OR_NODE_UPGRADES: MaintenanceExclusionOptions.Scope
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    scope: MaintenanceExclusionOptions.Scope
    def __init__(self, scope: _Optional[_Union[MaintenanceExclusionOptions.Scope, str]] = ...) -> None: ...

class RecurringTimeWindow(_message.Message):
    __slots__ = ("window", "recurrence")
    WINDOW_FIELD_NUMBER: _ClassVar[int]
    RECURRENCE_FIELD_NUMBER: _ClassVar[int]
    window: TimeWindow
    recurrence: str
    def __init__(self, window: _Optional[_Union[TimeWindow, _Mapping]] = ..., recurrence: _Optional[str] = ...) -> None: ...

class DailyMaintenanceWindow(_message.Message):
    __slots__ = ("start_time", "duration")
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    start_time: str
    duration: str
    def __init__(self, start_time: _Optional[str] = ..., duration: _Optional[str] = ...) -> None: ...

class SetNodePoolManagementRequest(_message.Message):
    __slots__ = ("project_id", "zone", "cluster_id", "node_pool_id", "management", "name")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_POOL_ID_FIELD_NUMBER: _ClassVar[int]
    MANAGEMENT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    zone: str
    cluster_id: str
    node_pool_id: str
    management: NodeManagement
    name: str
    def __init__(self, project_id: _Optional[str] = ..., zone: _Optional[str] = ..., cluster_id: _Optional[str] = ..., node_pool_id: _Optional[str] = ..., management: _Optional[_Union[NodeManagement, _Mapping]] = ..., name: _Optional[str] = ...) -> None: ...

class SetNodePoolSizeRequest(_message.Message):
    __slots__ = ("project_id", "zone", "cluster_id", "node_pool_id", "node_count", "name")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_POOL_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_COUNT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    zone: str
    cluster_id: str
    node_pool_id: str
    node_count: int
    name: str
    def __init__(self, project_id: _Optional[str] = ..., zone: _Optional[str] = ..., cluster_id: _Optional[str] = ..., node_pool_id: _Optional[str] = ..., node_count: _Optional[int] = ..., name: _Optional[str] = ...) -> None: ...

class CompleteNodePoolUpgradeRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class RollbackNodePoolUpgradeRequest(_message.Message):
    __slots__ = ("project_id", "zone", "cluster_id", "node_pool_id", "name", "respect_pdb")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_POOL_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    RESPECT_PDB_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    zone: str
    cluster_id: str
    node_pool_id: str
    name: str
    respect_pdb: bool
    def __init__(self, project_id: _Optional[str] = ..., zone: _Optional[str] = ..., cluster_id: _Optional[str] = ..., node_pool_id: _Optional[str] = ..., name: _Optional[str] = ..., respect_pdb: bool = ...) -> None: ...

class ListNodePoolsResponse(_message.Message):
    __slots__ = ("node_pools",)
    NODE_POOLS_FIELD_NUMBER: _ClassVar[int]
    node_pools: _containers.RepeatedCompositeFieldContainer[NodePool]
    def __init__(self, node_pools: _Optional[_Iterable[_Union[NodePool, _Mapping]]] = ...) -> None: ...

class ClusterAutoscaling(_message.Message):
    __slots__ = ("enable_node_autoprovisioning", "resource_limits", "autoscaling_profile", "autoprovisioning_node_pool_defaults", "autoprovisioning_locations")
    class AutoscalingProfile(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PROFILE_UNSPECIFIED: _ClassVar[ClusterAutoscaling.AutoscalingProfile]
        OPTIMIZE_UTILIZATION: _ClassVar[ClusterAutoscaling.AutoscalingProfile]
        BALANCED: _ClassVar[ClusterAutoscaling.AutoscalingProfile]
    PROFILE_UNSPECIFIED: ClusterAutoscaling.AutoscalingProfile
    OPTIMIZE_UTILIZATION: ClusterAutoscaling.AutoscalingProfile
    BALANCED: ClusterAutoscaling.AutoscalingProfile
    ENABLE_NODE_AUTOPROVISIONING_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_LIMITS_FIELD_NUMBER: _ClassVar[int]
    AUTOSCALING_PROFILE_FIELD_NUMBER: _ClassVar[int]
    AUTOPROVISIONING_NODE_POOL_DEFAULTS_FIELD_NUMBER: _ClassVar[int]
    AUTOPROVISIONING_LOCATIONS_FIELD_NUMBER: _ClassVar[int]
    enable_node_autoprovisioning: bool
    resource_limits: _containers.RepeatedCompositeFieldContainer[ResourceLimit]
    autoscaling_profile: ClusterAutoscaling.AutoscalingProfile
    autoprovisioning_node_pool_defaults: AutoprovisioningNodePoolDefaults
    autoprovisioning_locations: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, enable_node_autoprovisioning: bool = ..., resource_limits: _Optional[_Iterable[_Union[ResourceLimit, _Mapping]]] = ..., autoscaling_profile: _Optional[_Union[ClusterAutoscaling.AutoscalingProfile, str]] = ..., autoprovisioning_node_pool_defaults: _Optional[_Union[AutoprovisioningNodePoolDefaults, _Mapping]] = ..., autoprovisioning_locations: _Optional[_Iterable[str]] = ...) -> None: ...

class AutoprovisioningNodePoolDefaults(_message.Message):
    __slots__ = ("oauth_scopes", "service_account", "upgrade_settings", "management", "min_cpu_platform", "disk_size_gb", "disk_type", "shielded_instance_config", "boot_disk_kms_key", "image_type", "insecure_kubelet_readonly_port_enabled")
    OAUTH_SCOPES_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    UPGRADE_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    MANAGEMENT_FIELD_NUMBER: _ClassVar[int]
    MIN_CPU_PLATFORM_FIELD_NUMBER: _ClassVar[int]
    DISK_SIZE_GB_FIELD_NUMBER: _ClassVar[int]
    DISK_TYPE_FIELD_NUMBER: _ClassVar[int]
    SHIELDED_INSTANCE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    BOOT_DISK_KMS_KEY_FIELD_NUMBER: _ClassVar[int]
    IMAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    INSECURE_KUBELET_READONLY_PORT_ENABLED_FIELD_NUMBER: _ClassVar[int]
    oauth_scopes: _containers.RepeatedScalarFieldContainer[str]
    service_account: str
    upgrade_settings: NodePool.UpgradeSettings
    management: NodeManagement
    min_cpu_platform: str
    disk_size_gb: int
    disk_type: str
    shielded_instance_config: ShieldedInstanceConfig
    boot_disk_kms_key: str
    image_type: str
    insecure_kubelet_readonly_port_enabled: bool
    def __init__(self, oauth_scopes: _Optional[_Iterable[str]] = ..., service_account: _Optional[str] = ..., upgrade_settings: _Optional[_Union[NodePool.UpgradeSettings, _Mapping]] = ..., management: _Optional[_Union[NodeManagement, _Mapping]] = ..., min_cpu_platform: _Optional[str] = ..., disk_size_gb: _Optional[int] = ..., disk_type: _Optional[str] = ..., shielded_instance_config: _Optional[_Union[ShieldedInstanceConfig, _Mapping]] = ..., boot_disk_kms_key: _Optional[str] = ..., image_type: _Optional[str] = ..., insecure_kubelet_readonly_port_enabled: bool = ...) -> None: ...

class ResourceLimit(_message.Message):
    __slots__ = ("resource_type", "minimum", "maximum")
    RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_FIELD_NUMBER: _ClassVar[int]
    resource_type: str
    minimum: int
    maximum: int
    def __init__(self, resource_type: _Optional[str] = ..., minimum: _Optional[int] = ..., maximum: _Optional[int] = ...) -> None: ...

class NodePoolAutoscaling(_message.Message):
    __slots__ = ("enabled", "min_node_count", "max_node_count", "autoprovisioned", "location_policy", "total_min_node_count", "total_max_node_count")
    class LocationPolicy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        LOCATION_POLICY_UNSPECIFIED: _ClassVar[NodePoolAutoscaling.LocationPolicy]
        BALANCED: _ClassVar[NodePoolAutoscaling.LocationPolicy]
        ANY: _ClassVar[NodePoolAutoscaling.LocationPolicy]
    LOCATION_POLICY_UNSPECIFIED: NodePoolAutoscaling.LocationPolicy
    BALANCED: NodePoolAutoscaling.LocationPolicy
    ANY: NodePoolAutoscaling.LocationPolicy
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    MIN_NODE_COUNT_FIELD_NUMBER: _ClassVar[int]
    MAX_NODE_COUNT_FIELD_NUMBER: _ClassVar[int]
    AUTOPROVISIONED_FIELD_NUMBER: _ClassVar[int]
    LOCATION_POLICY_FIELD_NUMBER: _ClassVar[int]
    TOTAL_MIN_NODE_COUNT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_MAX_NODE_COUNT_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    min_node_count: int
    max_node_count: int
    autoprovisioned: bool
    location_policy: NodePoolAutoscaling.LocationPolicy
    total_min_node_count: int
    total_max_node_count: int
    def __init__(self, enabled: bool = ..., min_node_count: _Optional[int] = ..., max_node_count: _Optional[int] = ..., autoprovisioned: bool = ..., location_policy: _Optional[_Union[NodePoolAutoscaling.LocationPolicy, str]] = ..., total_min_node_count: _Optional[int] = ..., total_max_node_count: _Optional[int] = ...) -> None: ...

class SetLabelsRequest(_message.Message):
    __slots__ = ("project_id", "zone", "cluster_id", "resource_labels", "label_fingerprint", "name")
    class ResourceLabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_LABELS_FIELD_NUMBER: _ClassVar[int]
    LABEL_FINGERPRINT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    zone: str
    cluster_id: str
    resource_labels: _containers.ScalarMap[str, str]
    label_fingerprint: str
    name: str
    def __init__(self, project_id: _Optional[str] = ..., zone: _Optional[str] = ..., cluster_id: _Optional[str] = ..., resource_labels: _Optional[_Mapping[str, str]] = ..., label_fingerprint: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class SetLegacyAbacRequest(_message.Message):
    __slots__ = ("project_id", "zone", "cluster_id", "enabled", "name")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    zone: str
    cluster_id: str
    enabled: bool
    name: str
    def __init__(self, project_id: _Optional[str] = ..., zone: _Optional[str] = ..., cluster_id: _Optional[str] = ..., enabled: bool = ..., name: _Optional[str] = ...) -> None: ...

class StartIPRotationRequest(_message.Message):
    __slots__ = ("project_id", "zone", "cluster_id", "name", "rotate_credentials")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ROTATE_CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    zone: str
    cluster_id: str
    name: str
    rotate_credentials: bool
    def __init__(self, project_id: _Optional[str] = ..., zone: _Optional[str] = ..., cluster_id: _Optional[str] = ..., name: _Optional[str] = ..., rotate_credentials: bool = ...) -> None: ...

class CompleteIPRotationRequest(_message.Message):
    __slots__ = ("project_id", "zone", "cluster_id", "name")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    zone: str
    cluster_id: str
    name: str
    def __init__(self, project_id: _Optional[str] = ..., zone: _Optional[str] = ..., cluster_id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class AcceleratorConfig(_message.Message):
    __slots__ = ("accelerator_count", "accelerator_type", "gpu_partition_size", "gpu_sharing_config", "gpu_driver_installation_config")
    ACCELERATOR_COUNT_FIELD_NUMBER: _ClassVar[int]
    ACCELERATOR_TYPE_FIELD_NUMBER: _ClassVar[int]
    GPU_PARTITION_SIZE_FIELD_NUMBER: _ClassVar[int]
    GPU_SHARING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    GPU_DRIVER_INSTALLATION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    accelerator_count: int
    accelerator_type: str
    gpu_partition_size: str
    gpu_sharing_config: GPUSharingConfig
    gpu_driver_installation_config: GPUDriverInstallationConfig
    def __init__(self, accelerator_count: _Optional[int] = ..., accelerator_type: _Optional[str] = ..., gpu_partition_size: _Optional[str] = ..., gpu_sharing_config: _Optional[_Union[GPUSharingConfig, _Mapping]] = ..., gpu_driver_installation_config: _Optional[_Union[GPUDriverInstallationConfig, _Mapping]] = ...) -> None: ...

class GPUSharingConfig(_message.Message):
    __slots__ = ("max_shared_clients_per_gpu", "gpu_sharing_strategy")
    class GPUSharingStrategy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        GPU_SHARING_STRATEGY_UNSPECIFIED: _ClassVar[GPUSharingConfig.GPUSharingStrategy]
        TIME_SHARING: _ClassVar[GPUSharingConfig.GPUSharingStrategy]
        MPS: _ClassVar[GPUSharingConfig.GPUSharingStrategy]
    GPU_SHARING_STRATEGY_UNSPECIFIED: GPUSharingConfig.GPUSharingStrategy
    TIME_SHARING: GPUSharingConfig.GPUSharingStrategy
    MPS: GPUSharingConfig.GPUSharingStrategy
    MAX_SHARED_CLIENTS_PER_GPU_FIELD_NUMBER: _ClassVar[int]
    GPU_SHARING_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    max_shared_clients_per_gpu: int
    gpu_sharing_strategy: GPUSharingConfig.GPUSharingStrategy
    def __init__(self, max_shared_clients_per_gpu: _Optional[int] = ..., gpu_sharing_strategy: _Optional[_Union[GPUSharingConfig.GPUSharingStrategy, str]] = ...) -> None: ...

class GPUDriverInstallationConfig(_message.Message):
    __slots__ = ("gpu_driver_version",)
    class GPUDriverVersion(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        GPU_DRIVER_VERSION_UNSPECIFIED: _ClassVar[GPUDriverInstallationConfig.GPUDriverVersion]
        INSTALLATION_DISABLED: _ClassVar[GPUDriverInstallationConfig.GPUDriverVersion]
        DEFAULT: _ClassVar[GPUDriverInstallationConfig.GPUDriverVersion]
        LATEST: _ClassVar[GPUDriverInstallationConfig.GPUDriverVersion]
    GPU_DRIVER_VERSION_UNSPECIFIED: GPUDriverInstallationConfig.GPUDriverVersion
    INSTALLATION_DISABLED: GPUDriverInstallationConfig.GPUDriverVersion
    DEFAULT: GPUDriverInstallationConfig.GPUDriverVersion
    LATEST: GPUDriverInstallationConfig.GPUDriverVersion
    GPU_DRIVER_VERSION_FIELD_NUMBER: _ClassVar[int]
    gpu_driver_version: GPUDriverInstallationConfig.GPUDriverVersion
    def __init__(self, gpu_driver_version: _Optional[_Union[GPUDriverInstallationConfig.GPUDriverVersion, str]] = ...) -> None: ...

class WorkloadMetadataConfig(_message.Message):
    __slots__ = ("mode",)
    class Mode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MODE_UNSPECIFIED: _ClassVar[WorkloadMetadataConfig.Mode]
        GCE_METADATA: _ClassVar[WorkloadMetadataConfig.Mode]
        GKE_METADATA: _ClassVar[WorkloadMetadataConfig.Mode]
    MODE_UNSPECIFIED: WorkloadMetadataConfig.Mode
    GCE_METADATA: WorkloadMetadataConfig.Mode
    GKE_METADATA: WorkloadMetadataConfig.Mode
    MODE_FIELD_NUMBER: _ClassVar[int]
    mode: WorkloadMetadataConfig.Mode
    def __init__(self, mode: _Optional[_Union[WorkloadMetadataConfig.Mode, str]] = ...) -> None: ...

class SetNetworkPolicyRequest(_message.Message):
    __slots__ = ("project_id", "zone", "cluster_id", "network_policy", "name")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    NETWORK_POLICY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    zone: str
    cluster_id: str
    network_policy: NetworkPolicy
    name: str
    def __init__(self, project_id: _Optional[str] = ..., zone: _Optional[str] = ..., cluster_id: _Optional[str] = ..., network_policy: _Optional[_Union[NetworkPolicy, _Mapping]] = ..., name: _Optional[str] = ...) -> None: ...

class SetMaintenancePolicyRequest(_message.Message):
    __slots__ = ("project_id", "zone", "cluster_id", "maintenance_policy", "name")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    MAINTENANCE_POLICY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    zone: str
    cluster_id: str
    maintenance_policy: MaintenancePolicy
    name: str
    def __init__(self, project_id: _Optional[str] = ..., zone: _Optional[str] = ..., cluster_id: _Optional[str] = ..., maintenance_policy: _Optional[_Union[MaintenancePolicy, _Mapping]] = ..., name: _Optional[str] = ...) -> None: ...

class StatusCondition(_message.Message):
    __slots__ = ("code", "message", "canonical_code")
    class Code(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[StatusCondition.Code]
        GCE_STOCKOUT: _ClassVar[StatusCondition.Code]
        GKE_SERVICE_ACCOUNT_DELETED: _ClassVar[StatusCondition.Code]
        GCE_QUOTA_EXCEEDED: _ClassVar[StatusCondition.Code]
        SET_BY_OPERATOR: _ClassVar[StatusCondition.Code]
        CLOUD_KMS_KEY_ERROR: _ClassVar[StatusCondition.Code]
        CA_EXPIRING: _ClassVar[StatusCondition.Code]
    UNKNOWN: StatusCondition.Code
    GCE_STOCKOUT: StatusCondition.Code
    GKE_SERVICE_ACCOUNT_DELETED: StatusCondition.Code
    GCE_QUOTA_EXCEEDED: StatusCondition.Code
    SET_BY_OPERATOR: StatusCondition.Code
    CLOUD_KMS_KEY_ERROR: StatusCondition.Code
    CA_EXPIRING: StatusCondition.Code
    CODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    CANONICAL_CODE_FIELD_NUMBER: _ClassVar[int]
    code: StatusCondition.Code
    message: str
    canonical_code: _code_pb2.Code
    def __init__(self, code: _Optional[_Union[StatusCondition.Code, str]] = ..., message: _Optional[str] = ..., canonical_code: _Optional[_Union[_code_pb2.Code, str]] = ...) -> None: ...

class NetworkConfig(_message.Message):
    __slots__ = ("network", "subnetwork", "enable_intra_node_visibility", "default_snat_status", "enable_l4ilb_subsetting", "datapath_provider", "private_ipv6_google_access", "dns_config", "service_external_ips_config", "gateway_api_config", "enable_multi_networking", "network_performance_config", "enable_fqdn_network_policy", "in_transit_encryption_config", "enable_cilium_clusterwide_network_policy", "default_enable_private_nodes")
    class ClusterNetworkPerformanceConfig(_message.Message):
        __slots__ = ("total_egress_bandwidth_tier",)
        class Tier(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            TIER_UNSPECIFIED: _ClassVar[NetworkConfig.ClusterNetworkPerformanceConfig.Tier]
            TIER_1: _ClassVar[NetworkConfig.ClusterNetworkPerformanceConfig.Tier]
        TIER_UNSPECIFIED: NetworkConfig.ClusterNetworkPerformanceConfig.Tier
        TIER_1: NetworkConfig.ClusterNetworkPerformanceConfig.Tier
        TOTAL_EGRESS_BANDWIDTH_TIER_FIELD_NUMBER: _ClassVar[int]
        total_egress_bandwidth_tier: NetworkConfig.ClusterNetworkPerformanceConfig.Tier
        def __init__(self, total_egress_bandwidth_tier: _Optional[_Union[NetworkConfig.ClusterNetworkPerformanceConfig.Tier, str]] = ...) -> None: ...
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    SUBNETWORK_FIELD_NUMBER: _ClassVar[int]
    ENABLE_INTRA_NODE_VISIBILITY_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_SNAT_STATUS_FIELD_NUMBER: _ClassVar[int]
    ENABLE_L4ILB_SUBSETTING_FIELD_NUMBER: _ClassVar[int]
    DATAPATH_PROVIDER_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_IPV6_GOOGLE_ACCESS_FIELD_NUMBER: _ClassVar[int]
    DNS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    SERVICE_EXTERNAL_IPS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    GATEWAY_API_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ENABLE_MULTI_NETWORKING_FIELD_NUMBER: _ClassVar[int]
    NETWORK_PERFORMANCE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ENABLE_FQDN_NETWORK_POLICY_FIELD_NUMBER: _ClassVar[int]
    IN_TRANSIT_ENCRYPTION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ENABLE_CILIUM_CLUSTERWIDE_NETWORK_POLICY_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_ENABLE_PRIVATE_NODES_FIELD_NUMBER: _ClassVar[int]
    network: str
    subnetwork: str
    enable_intra_node_visibility: bool
    default_snat_status: DefaultSnatStatus
    enable_l4ilb_subsetting: bool
    datapath_provider: DatapathProvider
    private_ipv6_google_access: PrivateIPv6GoogleAccess
    dns_config: DNSConfig
    service_external_ips_config: ServiceExternalIPsConfig
    gateway_api_config: GatewayAPIConfig
    enable_multi_networking: bool
    network_performance_config: NetworkConfig.ClusterNetworkPerformanceConfig
    enable_fqdn_network_policy: bool
    in_transit_encryption_config: InTransitEncryptionConfig
    enable_cilium_clusterwide_network_policy: bool
    default_enable_private_nodes: bool
    def __init__(self, network: _Optional[str] = ..., subnetwork: _Optional[str] = ..., enable_intra_node_visibility: bool = ..., default_snat_status: _Optional[_Union[DefaultSnatStatus, _Mapping]] = ..., enable_l4ilb_subsetting: bool = ..., datapath_provider: _Optional[_Union[DatapathProvider, str]] = ..., private_ipv6_google_access: _Optional[_Union[PrivateIPv6GoogleAccess, str]] = ..., dns_config: _Optional[_Union[DNSConfig, _Mapping]] = ..., service_external_ips_config: _Optional[_Union[ServiceExternalIPsConfig, _Mapping]] = ..., gateway_api_config: _Optional[_Union[GatewayAPIConfig, _Mapping]] = ..., enable_multi_networking: bool = ..., network_performance_config: _Optional[_Union[NetworkConfig.ClusterNetworkPerformanceConfig, _Mapping]] = ..., enable_fqdn_network_policy: bool = ..., in_transit_encryption_config: _Optional[_Union[InTransitEncryptionConfig, str]] = ..., enable_cilium_clusterwide_network_policy: bool = ..., default_enable_private_nodes: bool = ...) -> None: ...

class GatewayAPIConfig(_message.Message):
    __slots__ = ("channel",)
    class Channel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CHANNEL_UNSPECIFIED: _ClassVar[GatewayAPIConfig.Channel]
        CHANNEL_DISABLED: _ClassVar[GatewayAPIConfig.Channel]
        CHANNEL_EXPERIMENTAL: _ClassVar[GatewayAPIConfig.Channel]
        CHANNEL_STANDARD: _ClassVar[GatewayAPIConfig.Channel]
    CHANNEL_UNSPECIFIED: GatewayAPIConfig.Channel
    CHANNEL_DISABLED: GatewayAPIConfig.Channel
    CHANNEL_EXPERIMENTAL: GatewayAPIConfig.Channel
    CHANNEL_STANDARD: GatewayAPIConfig.Channel
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    channel: GatewayAPIConfig.Channel
    def __init__(self, channel: _Optional[_Union[GatewayAPIConfig.Channel, str]] = ...) -> None: ...

class ServiceExternalIPsConfig(_message.Message):
    __slots__ = ("enabled",)
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    def __init__(self, enabled: bool = ...) -> None: ...

class GetOpenIDConfigRequest(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: str
    def __init__(self, parent: _Optional[str] = ...) -> None: ...

class GetOpenIDConfigResponse(_message.Message):
    __slots__ = ("issuer", "jwks_uri", "response_types_supported", "subject_types_supported", "id_token_signing_alg_values_supported", "claims_supported", "grant_types")
    ISSUER_FIELD_NUMBER: _ClassVar[int]
    JWKS_URI_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_TYPES_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_TYPES_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    ID_TOKEN_SIGNING_ALG_VALUES_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    CLAIMS_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    GRANT_TYPES_FIELD_NUMBER: _ClassVar[int]
    issuer: str
    jwks_uri: str
    response_types_supported: _containers.RepeatedScalarFieldContainer[str]
    subject_types_supported: _containers.RepeatedScalarFieldContainer[str]
    id_token_signing_alg_values_supported: _containers.RepeatedScalarFieldContainer[str]
    claims_supported: _containers.RepeatedScalarFieldContainer[str]
    grant_types: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, issuer: _Optional[str] = ..., jwks_uri: _Optional[str] = ..., response_types_supported: _Optional[_Iterable[str]] = ..., subject_types_supported: _Optional[_Iterable[str]] = ..., id_token_signing_alg_values_supported: _Optional[_Iterable[str]] = ..., claims_supported: _Optional[_Iterable[str]] = ..., grant_types: _Optional[_Iterable[str]] = ...) -> None: ...

class GetJSONWebKeysRequest(_message.Message):
    __slots__ = ("parent",)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: str
    def __init__(self, parent: _Optional[str] = ...) -> None: ...

class Jwk(_message.Message):
    __slots__ = ("kty", "alg", "use", "kid", "n", "e", "x", "y", "crv")
    KTY_FIELD_NUMBER: _ClassVar[int]
    ALG_FIELD_NUMBER: _ClassVar[int]
    USE_FIELD_NUMBER: _ClassVar[int]
    KID_FIELD_NUMBER: _ClassVar[int]
    N_FIELD_NUMBER: _ClassVar[int]
    E_FIELD_NUMBER: _ClassVar[int]
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    CRV_FIELD_NUMBER: _ClassVar[int]
    kty: str
    alg: str
    use: str
    kid: str
    n: str
    e: str
    x: str
    y: str
    crv: str
    def __init__(self, kty: _Optional[str] = ..., alg: _Optional[str] = ..., use: _Optional[str] = ..., kid: _Optional[str] = ..., n: _Optional[str] = ..., e: _Optional[str] = ..., x: _Optional[str] = ..., y: _Optional[str] = ..., crv: _Optional[str] = ...) -> None: ...

class GetJSONWebKeysResponse(_message.Message):
    __slots__ = ("keys",)
    KEYS_FIELD_NUMBER: _ClassVar[int]
    keys: _containers.RepeatedCompositeFieldContainer[Jwk]
    def __init__(self, keys: _Optional[_Iterable[_Union[Jwk, _Mapping]]] = ...) -> None: ...

class CheckAutopilotCompatibilityRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class AutopilotCompatibilityIssue(_message.Message):
    __slots__ = ("last_observation", "constraint_type", "incompatibility_type", "subjects", "documentation_url", "description")
    class IssueType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[AutopilotCompatibilityIssue.IssueType]
        INCOMPATIBILITY: _ClassVar[AutopilotCompatibilityIssue.IssueType]
        ADDITIONAL_CONFIG_REQUIRED: _ClassVar[AutopilotCompatibilityIssue.IssueType]
        PASSED_WITH_OPTIONAL_CONFIG: _ClassVar[AutopilotCompatibilityIssue.IssueType]
    UNSPECIFIED: AutopilotCompatibilityIssue.IssueType
    INCOMPATIBILITY: AutopilotCompatibilityIssue.IssueType
    ADDITIONAL_CONFIG_REQUIRED: AutopilotCompatibilityIssue.IssueType
    PASSED_WITH_OPTIONAL_CONFIG: AutopilotCompatibilityIssue.IssueType
    LAST_OBSERVATION_FIELD_NUMBER: _ClassVar[int]
    CONSTRAINT_TYPE_FIELD_NUMBER: _ClassVar[int]
    INCOMPATIBILITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    SUBJECTS_FIELD_NUMBER: _ClassVar[int]
    DOCUMENTATION_URL_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    last_observation: _timestamp_pb2.Timestamp
    constraint_type: str
    incompatibility_type: AutopilotCompatibilityIssue.IssueType
    subjects: _containers.RepeatedScalarFieldContainer[str]
    documentation_url: str
    description: str
    def __init__(self, last_observation: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., constraint_type: _Optional[str] = ..., incompatibility_type: _Optional[_Union[AutopilotCompatibilityIssue.IssueType, str]] = ..., subjects: _Optional[_Iterable[str]] = ..., documentation_url: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class CheckAutopilotCompatibilityResponse(_message.Message):
    __slots__ = ("issues", "summary")
    ISSUES_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    issues: _containers.RepeatedCompositeFieldContainer[AutopilotCompatibilityIssue]
    summary: str
    def __init__(self, issues: _Optional[_Iterable[_Union[AutopilotCompatibilityIssue, _Mapping]]] = ..., summary: _Optional[str] = ...) -> None: ...

class ReleaseChannel(_message.Message):
    __slots__ = ("channel",)
    class Channel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ReleaseChannel.Channel]
        RAPID: _ClassVar[ReleaseChannel.Channel]
        REGULAR: _ClassVar[ReleaseChannel.Channel]
        STABLE: _ClassVar[ReleaseChannel.Channel]
        EXTENDED: _ClassVar[ReleaseChannel.Channel]
    UNSPECIFIED: ReleaseChannel.Channel
    RAPID: ReleaseChannel.Channel
    REGULAR: ReleaseChannel.Channel
    STABLE: ReleaseChannel.Channel
    EXTENDED: ReleaseChannel.Channel
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    channel: ReleaseChannel.Channel
    def __init__(self, channel: _Optional[_Union[ReleaseChannel.Channel, str]] = ...) -> None: ...

class CostManagementConfig(_message.Message):
    __slots__ = ("enabled",)
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    def __init__(self, enabled: bool = ...) -> None: ...

class IntraNodeVisibilityConfig(_message.Message):
    __slots__ = ("enabled",)
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    def __init__(self, enabled: bool = ...) -> None: ...

class ILBSubsettingConfig(_message.Message):
    __slots__ = ("enabled",)
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    def __init__(self, enabled: bool = ...) -> None: ...

class DNSConfig(_message.Message):
    __slots__ = ("cluster_dns", "cluster_dns_scope", "cluster_dns_domain", "additive_vpc_scope_dns_domain")
    class Provider(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PROVIDER_UNSPECIFIED: _ClassVar[DNSConfig.Provider]
        PLATFORM_DEFAULT: _ClassVar[DNSConfig.Provider]
        CLOUD_DNS: _ClassVar[DNSConfig.Provider]
        KUBE_DNS: _ClassVar[DNSConfig.Provider]
    PROVIDER_UNSPECIFIED: DNSConfig.Provider
    PLATFORM_DEFAULT: DNSConfig.Provider
    CLOUD_DNS: DNSConfig.Provider
    KUBE_DNS: DNSConfig.Provider
    class DNSScope(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DNS_SCOPE_UNSPECIFIED: _ClassVar[DNSConfig.DNSScope]
        CLUSTER_SCOPE: _ClassVar[DNSConfig.DNSScope]
        VPC_SCOPE: _ClassVar[DNSConfig.DNSScope]
    DNS_SCOPE_UNSPECIFIED: DNSConfig.DNSScope
    CLUSTER_SCOPE: DNSConfig.DNSScope
    VPC_SCOPE: DNSConfig.DNSScope
    CLUSTER_DNS_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_DNS_SCOPE_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_DNS_DOMAIN_FIELD_NUMBER: _ClassVar[int]
    ADDITIVE_VPC_SCOPE_DNS_DOMAIN_FIELD_NUMBER: _ClassVar[int]
    cluster_dns: DNSConfig.Provider
    cluster_dns_scope: DNSConfig.DNSScope
    cluster_dns_domain: str
    additive_vpc_scope_dns_domain: str
    def __init__(self, cluster_dns: _Optional[_Union[DNSConfig.Provider, str]] = ..., cluster_dns_scope: _Optional[_Union[DNSConfig.DNSScope, str]] = ..., cluster_dns_domain: _Optional[str] = ..., additive_vpc_scope_dns_domain: _Optional[str] = ...) -> None: ...

class MaxPodsConstraint(_message.Message):
    __slots__ = ("max_pods_per_node",)
    MAX_PODS_PER_NODE_FIELD_NUMBER: _ClassVar[int]
    max_pods_per_node: int
    def __init__(self, max_pods_per_node: _Optional[int] = ...) -> None: ...

class WorkloadIdentityConfig(_message.Message):
    __slots__ = ("workload_pool",)
    WORKLOAD_POOL_FIELD_NUMBER: _ClassVar[int]
    workload_pool: str
    def __init__(self, workload_pool: _Optional[str] = ...) -> None: ...

class IdentityServiceConfig(_message.Message):
    __slots__ = ("enabled",)
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    def __init__(self, enabled: bool = ...) -> None: ...

class MeshCertificates(_message.Message):
    __slots__ = ("enable_certificates",)
    ENABLE_CERTIFICATES_FIELD_NUMBER: _ClassVar[int]
    enable_certificates: _wrappers_pb2.BoolValue
    def __init__(self, enable_certificates: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...) -> None: ...

class DatabaseEncryption(_message.Message):
    __slots__ = ("key_name", "state", "current_state", "decryption_keys", "last_operation_errors")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[DatabaseEncryption.State]
        ENCRYPTED: _ClassVar[DatabaseEncryption.State]
        DECRYPTED: _ClassVar[DatabaseEncryption.State]
    UNKNOWN: DatabaseEncryption.State
    ENCRYPTED: DatabaseEncryption.State
    DECRYPTED: DatabaseEncryption.State
    class CurrentState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CURRENT_STATE_UNSPECIFIED: _ClassVar[DatabaseEncryption.CurrentState]
        CURRENT_STATE_ENCRYPTED: _ClassVar[DatabaseEncryption.CurrentState]
        CURRENT_STATE_DECRYPTED: _ClassVar[DatabaseEncryption.CurrentState]
        CURRENT_STATE_ENCRYPTION_PENDING: _ClassVar[DatabaseEncryption.CurrentState]
        CURRENT_STATE_ENCRYPTION_ERROR: _ClassVar[DatabaseEncryption.CurrentState]
        CURRENT_STATE_DECRYPTION_PENDING: _ClassVar[DatabaseEncryption.CurrentState]
        CURRENT_STATE_DECRYPTION_ERROR: _ClassVar[DatabaseEncryption.CurrentState]
    CURRENT_STATE_UNSPECIFIED: DatabaseEncryption.CurrentState
    CURRENT_STATE_ENCRYPTED: DatabaseEncryption.CurrentState
    CURRENT_STATE_DECRYPTED: DatabaseEncryption.CurrentState
    CURRENT_STATE_ENCRYPTION_PENDING: DatabaseEncryption.CurrentState
    CURRENT_STATE_ENCRYPTION_ERROR: DatabaseEncryption.CurrentState
    CURRENT_STATE_DECRYPTION_PENDING: DatabaseEncryption.CurrentState
    CURRENT_STATE_DECRYPTION_ERROR: DatabaseEncryption.CurrentState
    class OperationError(_message.Message):
        __slots__ = ("key_name", "error_message", "timestamp")
        KEY_NAME_FIELD_NUMBER: _ClassVar[int]
        ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        key_name: str
        error_message: str
        timestamp: _timestamp_pb2.Timestamp
        def __init__(self, key_name: _Optional[str] = ..., error_message: _Optional[str] = ..., timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CURRENT_STATE_FIELD_NUMBER: _ClassVar[int]
    DECRYPTION_KEYS_FIELD_NUMBER: _ClassVar[int]
    LAST_OPERATION_ERRORS_FIELD_NUMBER: _ClassVar[int]
    key_name: str
    state: DatabaseEncryption.State
    current_state: DatabaseEncryption.CurrentState
    decryption_keys: _containers.RepeatedScalarFieldContainer[str]
    last_operation_errors: _containers.RepeatedCompositeFieldContainer[DatabaseEncryption.OperationError]
    def __init__(self, key_name: _Optional[str] = ..., state: _Optional[_Union[DatabaseEncryption.State, str]] = ..., current_state: _Optional[_Union[DatabaseEncryption.CurrentState, str]] = ..., decryption_keys: _Optional[_Iterable[str]] = ..., last_operation_errors: _Optional[_Iterable[_Union[DatabaseEncryption.OperationError, _Mapping]]] = ...) -> None: ...

class ListUsableSubnetworksRequest(_message.Message):
    __slots__ = ("parent", "filter", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., filter: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListUsableSubnetworksResponse(_message.Message):
    __slots__ = ("subnetworks", "next_page_token")
    SUBNETWORKS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    subnetworks: _containers.RepeatedCompositeFieldContainer[UsableSubnetwork]
    next_page_token: str
    def __init__(self, subnetworks: _Optional[_Iterable[_Union[UsableSubnetwork, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class UsableSubnetworkSecondaryRange(_message.Message):
    __slots__ = ("range_name", "ip_cidr_range", "status")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[UsableSubnetworkSecondaryRange.Status]
        UNUSED: _ClassVar[UsableSubnetworkSecondaryRange.Status]
        IN_USE_SERVICE: _ClassVar[UsableSubnetworkSecondaryRange.Status]
        IN_USE_SHAREABLE_POD: _ClassVar[UsableSubnetworkSecondaryRange.Status]
        IN_USE_MANAGED_POD: _ClassVar[UsableSubnetworkSecondaryRange.Status]
    UNKNOWN: UsableSubnetworkSecondaryRange.Status
    UNUSED: UsableSubnetworkSecondaryRange.Status
    IN_USE_SERVICE: UsableSubnetworkSecondaryRange.Status
    IN_USE_SHAREABLE_POD: UsableSubnetworkSecondaryRange.Status
    IN_USE_MANAGED_POD: UsableSubnetworkSecondaryRange.Status
    RANGE_NAME_FIELD_NUMBER: _ClassVar[int]
    IP_CIDR_RANGE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    range_name: str
    ip_cidr_range: str
    status: UsableSubnetworkSecondaryRange.Status
    def __init__(self, range_name: _Optional[str] = ..., ip_cidr_range: _Optional[str] = ..., status: _Optional[_Union[UsableSubnetworkSecondaryRange.Status, str]] = ...) -> None: ...

class UsableSubnetwork(_message.Message):
    __slots__ = ("subnetwork", "network", "ip_cidr_range", "secondary_ip_ranges", "status_message")
    SUBNETWORK_FIELD_NUMBER: _ClassVar[int]
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    IP_CIDR_RANGE_FIELD_NUMBER: _ClassVar[int]
    SECONDARY_IP_RANGES_FIELD_NUMBER: _ClassVar[int]
    STATUS_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    subnetwork: str
    network: str
    ip_cidr_range: str
    secondary_ip_ranges: _containers.RepeatedCompositeFieldContainer[UsableSubnetworkSecondaryRange]
    status_message: str
    def __init__(self, subnetwork: _Optional[str] = ..., network: _Optional[str] = ..., ip_cidr_range: _Optional[str] = ..., secondary_ip_ranges: _Optional[_Iterable[_Union[UsableSubnetworkSecondaryRange, _Mapping]]] = ..., status_message: _Optional[str] = ...) -> None: ...

class ResourceUsageExportConfig(_message.Message):
    __slots__ = ("bigquery_destination", "enable_network_egress_metering", "consumption_metering_config")
    class BigQueryDestination(_message.Message):
        __slots__ = ("dataset_id",)
        DATASET_ID_FIELD_NUMBER: _ClassVar[int]
        dataset_id: str
        def __init__(self, dataset_id: _Optional[str] = ...) -> None: ...
    class ConsumptionMeteringConfig(_message.Message):
        __slots__ = ("enabled",)
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        enabled: bool
        def __init__(self, enabled: bool = ...) -> None: ...
    BIGQUERY_DESTINATION_FIELD_NUMBER: _ClassVar[int]
    ENABLE_NETWORK_EGRESS_METERING_FIELD_NUMBER: _ClassVar[int]
    CONSUMPTION_METERING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    bigquery_destination: ResourceUsageExportConfig.BigQueryDestination
    enable_network_egress_metering: bool
    consumption_metering_config: ResourceUsageExportConfig.ConsumptionMeteringConfig
    def __init__(self, bigquery_destination: _Optional[_Union[ResourceUsageExportConfig.BigQueryDestination, _Mapping]] = ..., enable_network_egress_metering: bool = ..., consumption_metering_config: _Optional[_Union[ResourceUsageExportConfig.ConsumptionMeteringConfig, _Mapping]] = ...) -> None: ...

class VerticalPodAutoscaling(_message.Message):
    __slots__ = ("enabled",)
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    def __init__(self, enabled: bool = ...) -> None: ...

class DefaultSnatStatus(_message.Message):
    __slots__ = ("disabled",)
    DISABLED_FIELD_NUMBER: _ClassVar[int]
    disabled: bool
    def __init__(self, disabled: bool = ...) -> None: ...

class ShieldedNodes(_message.Message):
    __slots__ = ("enabled",)
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    def __init__(self, enabled: bool = ...) -> None: ...

class VirtualNIC(_message.Message):
    __slots__ = ("enabled",)
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    def __init__(self, enabled: bool = ...) -> None: ...

class FastSocket(_message.Message):
    __slots__ = ("enabled",)
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    def __init__(self, enabled: bool = ...) -> None: ...

class NotificationConfig(_message.Message):
    __slots__ = ("pubsub",)
    class EventType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        EVENT_TYPE_UNSPECIFIED: _ClassVar[NotificationConfig.EventType]
        UPGRADE_AVAILABLE_EVENT: _ClassVar[NotificationConfig.EventType]
        UPGRADE_EVENT: _ClassVar[NotificationConfig.EventType]
        SECURITY_BULLETIN_EVENT: _ClassVar[NotificationConfig.EventType]
    EVENT_TYPE_UNSPECIFIED: NotificationConfig.EventType
    UPGRADE_AVAILABLE_EVENT: NotificationConfig.EventType
    UPGRADE_EVENT: NotificationConfig.EventType
    SECURITY_BULLETIN_EVENT: NotificationConfig.EventType
    class PubSub(_message.Message):
        __slots__ = ("enabled", "topic", "filter")
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        TOPIC_FIELD_NUMBER: _ClassVar[int]
        FILTER_FIELD_NUMBER: _ClassVar[int]
        enabled: bool
        topic: str
        filter: NotificationConfig.Filter
        def __init__(self, enabled: bool = ..., topic: _Optional[str] = ..., filter: _Optional[_Union[NotificationConfig.Filter, _Mapping]] = ...) -> None: ...
    class Filter(_message.Message):
        __slots__ = ("event_type",)
        EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
        event_type: _containers.RepeatedScalarFieldContainer[NotificationConfig.EventType]
        def __init__(self, event_type: _Optional[_Iterable[_Union[NotificationConfig.EventType, str]]] = ...) -> None: ...
    PUBSUB_FIELD_NUMBER: _ClassVar[int]
    pubsub: NotificationConfig.PubSub
    def __init__(self, pubsub: _Optional[_Union[NotificationConfig.PubSub, _Mapping]] = ...) -> None: ...

class ConfidentialNodes(_message.Message):
    __slots__ = ("enabled",)
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    def __init__(self, enabled: bool = ...) -> None: ...

class UpgradeEvent(_message.Message):
    __slots__ = ("resource_type", "operation", "operation_start_time", "current_version", "target_version", "resource")
    RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    OPERATION_START_TIME_FIELD_NUMBER: _ClassVar[int]
    CURRENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    TARGET_VERSION_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    resource_type: UpgradeResourceType
    operation: str
    operation_start_time: _timestamp_pb2.Timestamp
    current_version: str
    target_version: str
    resource: str
    def __init__(self, resource_type: _Optional[_Union[UpgradeResourceType, str]] = ..., operation: _Optional[str] = ..., operation_start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., current_version: _Optional[str] = ..., target_version: _Optional[str] = ..., resource: _Optional[str] = ...) -> None: ...

class UpgradeInfoEvent(_message.Message):
    __slots__ = ("resource_type", "operation", "start_time", "end_time", "current_version", "target_version", "resource", "state", "description")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[UpgradeInfoEvent.State]
        STARTED: _ClassVar[UpgradeInfoEvent.State]
        SUCCEEDED: _ClassVar[UpgradeInfoEvent.State]
        FAILED: _ClassVar[UpgradeInfoEvent.State]
        CANCELED: _ClassVar[UpgradeInfoEvent.State]
    STATE_UNSPECIFIED: UpgradeInfoEvent.State
    STARTED: UpgradeInfoEvent.State
    SUCCEEDED: UpgradeInfoEvent.State
    FAILED: UpgradeInfoEvent.State
    CANCELED: UpgradeInfoEvent.State
    RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    CURRENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    TARGET_VERSION_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    resource_type: UpgradeResourceType
    operation: str
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    current_version: str
    target_version: str
    resource: str
    state: UpgradeInfoEvent.State
    description: str
    def __init__(self, resource_type: _Optional[_Union[UpgradeResourceType, str]] = ..., operation: _Optional[str] = ..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., current_version: _Optional[str] = ..., target_version: _Optional[str] = ..., resource: _Optional[str] = ..., state: _Optional[_Union[UpgradeInfoEvent.State, str]] = ..., description: _Optional[str] = ...) -> None: ...

class UpgradeAvailableEvent(_message.Message):
    __slots__ = ("version", "resource_type", "release_channel", "resource")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    RELEASE_CHANNEL_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    version: str
    resource_type: UpgradeResourceType
    release_channel: ReleaseChannel
    resource: str
    def __init__(self, version: _Optional[str] = ..., resource_type: _Optional[_Union[UpgradeResourceType, str]] = ..., release_channel: _Optional[_Union[ReleaseChannel, _Mapping]] = ..., resource: _Optional[str] = ...) -> None: ...

class SecurityBulletinEvent(_message.Message):
    __slots__ = ("resource_type_affected", "bulletin_id", "cve_ids", "severity", "bulletin_uri", "brief_description", "affected_supported_minors", "patched_versions", "suggested_upgrade_target", "manual_steps_required")
    RESOURCE_TYPE_AFFECTED_FIELD_NUMBER: _ClassVar[int]
    BULLETIN_ID_FIELD_NUMBER: _ClassVar[int]
    CVE_IDS_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    BULLETIN_URI_FIELD_NUMBER: _ClassVar[int]
    BRIEF_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    AFFECTED_SUPPORTED_MINORS_FIELD_NUMBER: _ClassVar[int]
    PATCHED_VERSIONS_FIELD_NUMBER: _ClassVar[int]
    SUGGESTED_UPGRADE_TARGET_FIELD_NUMBER: _ClassVar[int]
    MANUAL_STEPS_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    resource_type_affected: str
    bulletin_id: str
    cve_ids: _containers.RepeatedScalarFieldContainer[str]
    severity: str
    bulletin_uri: str
    brief_description: str
    affected_supported_minors: _containers.RepeatedScalarFieldContainer[str]
    patched_versions: _containers.RepeatedScalarFieldContainer[str]
    suggested_upgrade_target: str
    manual_steps_required: bool
    def __init__(self, resource_type_affected: _Optional[str] = ..., bulletin_id: _Optional[str] = ..., cve_ids: _Optional[_Iterable[str]] = ..., severity: _Optional[str] = ..., bulletin_uri: _Optional[str] = ..., brief_description: _Optional[str] = ..., affected_supported_minors: _Optional[_Iterable[str]] = ..., patched_versions: _Optional[_Iterable[str]] = ..., suggested_upgrade_target: _Optional[str] = ..., manual_steps_required: bool = ...) -> None: ...

class Autopilot(_message.Message):
    __slots__ = ("enabled", "workload_policy_config")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    WORKLOAD_POLICY_CONFIG_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    workload_policy_config: WorkloadPolicyConfig
    def __init__(self, enabled: bool = ..., workload_policy_config: _Optional[_Union[WorkloadPolicyConfig, _Mapping]] = ...) -> None: ...

class WorkloadPolicyConfig(_message.Message):
    __slots__ = ("allow_net_admin",)
    ALLOW_NET_ADMIN_FIELD_NUMBER: _ClassVar[int]
    allow_net_admin: bool
    def __init__(self, allow_net_admin: bool = ...) -> None: ...

class LoggingConfig(_message.Message):
    __slots__ = ("component_config",)
    COMPONENT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    component_config: LoggingComponentConfig
    def __init__(self, component_config: _Optional[_Union[LoggingComponentConfig, _Mapping]] = ...) -> None: ...

class LoggingComponentConfig(_message.Message):
    __slots__ = ("enable_components",)
    class Component(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        COMPONENT_UNSPECIFIED: _ClassVar[LoggingComponentConfig.Component]
        SYSTEM_COMPONENTS: _ClassVar[LoggingComponentConfig.Component]
        WORKLOADS: _ClassVar[LoggingComponentConfig.Component]
        APISERVER: _ClassVar[LoggingComponentConfig.Component]
        SCHEDULER: _ClassVar[LoggingComponentConfig.Component]
        CONTROLLER_MANAGER: _ClassVar[LoggingComponentConfig.Component]
        KCP_SSHD: _ClassVar[LoggingComponentConfig.Component]
        KCP_CONNECTION: _ClassVar[LoggingComponentConfig.Component]
    COMPONENT_UNSPECIFIED: LoggingComponentConfig.Component
    SYSTEM_COMPONENTS: LoggingComponentConfig.Component
    WORKLOADS: LoggingComponentConfig.Component
    APISERVER: LoggingComponentConfig.Component
    SCHEDULER: LoggingComponentConfig.Component
    CONTROLLER_MANAGER: LoggingComponentConfig.Component
    KCP_SSHD: LoggingComponentConfig.Component
    KCP_CONNECTION: LoggingComponentConfig.Component
    ENABLE_COMPONENTS_FIELD_NUMBER: _ClassVar[int]
    enable_components: _containers.RepeatedScalarFieldContainer[LoggingComponentConfig.Component]
    def __init__(self, enable_components: _Optional[_Iterable[_Union[LoggingComponentConfig.Component, str]]] = ...) -> None: ...

class RayClusterLoggingConfig(_message.Message):
    __slots__ = ("enabled",)
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    def __init__(self, enabled: bool = ...) -> None: ...

class MonitoringConfig(_message.Message):
    __slots__ = ("component_config", "managed_prometheus_config", "advanced_datapath_observability_config")
    COMPONENT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    MANAGED_PROMETHEUS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ADVANCED_DATAPATH_OBSERVABILITY_CONFIG_FIELD_NUMBER: _ClassVar[int]
    component_config: MonitoringComponentConfig
    managed_prometheus_config: ManagedPrometheusConfig
    advanced_datapath_observability_config: AdvancedDatapathObservabilityConfig
    def __init__(self, component_config: _Optional[_Union[MonitoringComponentConfig, _Mapping]] = ..., managed_prometheus_config: _Optional[_Union[ManagedPrometheusConfig, _Mapping]] = ..., advanced_datapath_observability_config: _Optional[_Union[AdvancedDatapathObservabilityConfig, _Mapping]] = ...) -> None: ...

class AdvancedDatapathObservabilityConfig(_message.Message):
    __slots__ = ("enable_metrics", "relay_mode", "enable_relay")
    class RelayMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RELAY_MODE_UNSPECIFIED: _ClassVar[AdvancedDatapathObservabilityConfig.RelayMode]
        DISABLED: _ClassVar[AdvancedDatapathObservabilityConfig.RelayMode]
        INTERNAL_VPC_LB: _ClassVar[AdvancedDatapathObservabilityConfig.RelayMode]
        EXTERNAL_LB: _ClassVar[AdvancedDatapathObservabilityConfig.RelayMode]
    RELAY_MODE_UNSPECIFIED: AdvancedDatapathObservabilityConfig.RelayMode
    DISABLED: AdvancedDatapathObservabilityConfig.RelayMode
    INTERNAL_VPC_LB: AdvancedDatapathObservabilityConfig.RelayMode
    EXTERNAL_LB: AdvancedDatapathObservabilityConfig.RelayMode
    ENABLE_METRICS_FIELD_NUMBER: _ClassVar[int]
    RELAY_MODE_FIELD_NUMBER: _ClassVar[int]
    ENABLE_RELAY_FIELD_NUMBER: _ClassVar[int]
    enable_metrics: bool
    relay_mode: AdvancedDatapathObservabilityConfig.RelayMode
    enable_relay: bool
    def __init__(self, enable_metrics: bool = ..., relay_mode: _Optional[_Union[AdvancedDatapathObservabilityConfig.RelayMode, str]] = ..., enable_relay: bool = ...) -> None: ...

class RayClusterMonitoringConfig(_message.Message):
    __slots__ = ("enabled",)
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    def __init__(self, enabled: bool = ...) -> None: ...

class NodePoolLoggingConfig(_message.Message):
    __slots__ = ("variant_config",)
    VARIANT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    variant_config: LoggingVariantConfig
    def __init__(self, variant_config: _Optional[_Union[LoggingVariantConfig, _Mapping]] = ...) -> None: ...

class LoggingVariantConfig(_message.Message):
    __slots__ = ("variant",)
    class Variant(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        VARIANT_UNSPECIFIED: _ClassVar[LoggingVariantConfig.Variant]
        DEFAULT: _ClassVar[LoggingVariantConfig.Variant]
        MAX_THROUGHPUT: _ClassVar[LoggingVariantConfig.Variant]
    VARIANT_UNSPECIFIED: LoggingVariantConfig.Variant
    DEFAULT: LoggingVariantConfig.Variant
    MAX_THROUGHPUT: LoggingVariantConfig.Variant
    VARIANT_FIELD_NUMBER: _ClassVar[int]
    variant: LoggingVariantConfig.Variant
    def __init__(self, variant: _Optional[_Union[LoggingVariantConfig.Variant, str]] = ...) -> None: ...

class MonitoringComponentConfig(_message.Message):
    __slots__ = ("enable_components",)
    class Component(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        COMPONENT_UNSPECIFIED: _ClassVar[MonitoringComponentConfig.Component]
        SYSTEM_COMPONENTS: _ClassVar[MonitoringComponentConfig.Component]
        APISERVER: _ClassVar[MonitoringComponentConfig.Component]
        SCHEDULER: _ClassVar[MonitoringComponentConfig.Component]
        CONTROLLER_MANAGER: _ClassVar[MonitoringComponentConfig.Component]
        STORAGE: _ClassVar[MonitoringComponentConfig.Component]
        HPA: _ClassVar[MonitoringComponentConfig.Component]
        POD: _ClassVar[MonitoringComponentConfig.Component]
        DAEMONSET: _ClassVar[MonitoringComponentConfig.Component]
        DEPLOYMENT: _ClassVar[MonitoringComponentConfig.Component]
        STATEFULSET: _ClassVar[MonitoringComponentConfig.Component]
        CADVISOR: _ClassVar[MonitoringComponentConfig.Component]
        KUBELET: _ClassVar[MonitoringComponentConfig.Component]
        DCGM: _ClassVar[MonitoringComponentConfig.Component]
    COMPONENT_UNSPECIFIED: MonitoringComponentConfig.Component
    SYSTEM_COMPONENTS: MonitoringComponentConfig.Component
    APISERVER: MonitoringComponentConfig.Component
    SCHEDULER: MonitoringComponentConfig.Component
    CONTROLLER_MANAGER: MonitoringComponentConfig.Component
    STORAGE: MonitoringComponentConfig.Component
    HPA: MonitoringComponentConfig.Component
    POD: MonitoringComponentConfig.Component
    DAEMONSET: MonitoringComponentConfig.Component
    DEPLOYMENT: MonitoringComponentConfig.Component
    STATEFULSET: MonitoringComponentConfig.Component
    CADVISOR: MonitoringComponentConfig.Component
    KUBELET: MonitoringComponentConfig.Component
    DCGM: MonitoringComponentConfig.Component
    ENABLE_COMPONENTS_FIELD_NUMBER: _ClassVar[int]
    enable_components: _containers.RepeatedScalarFieldContainer[MonitoringComponentConfig.Component]
    def __init__(self, enable_components: _Optional[_Iterable[_Union[MonitoringComponentConfig.Component, str]]] = ...) -> None: ...

class ManagedPrometheusConfig(_message.Message):
    __slots__ = ("enabled",)
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    def __init__(self, enabled: bool = ...) -> None: ...

class Fleet(_message.Message):
    __slots__ = ("project", "membership", "pre_registered")
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    MEMBERSHIP_FIELD_NUMBER: _ClassVar[int]
    PRE_REGISTERED_FIELD_NUMBER: _ClassVar[int]
    project: str
    membership: str
    pre_registered: bool
    def __init__(self, project: _Optional[str] = ..., membership: _Optional[str] = ..., pre_registered: bool = ...) -> None: ...

class ControlPlaneEndpointsConfig(_message.Message):
    __slots__ = ("dns_endpoint_config", "ip_endpoints_config")
    class DNSEndpointConfig(_message.Message):
        __slots__ = ("endpoint", "allow_external_traffic")
        ENDPOINT_FIELD_NUMBER: _ClassVar[int]
        ALLOW_EXTERNAL_TRAFFIC_FIELD_NUMBER: _ClassVar[int]
        endpoint: str
        allow_external_traffic: bool
        def __init__(self, endpoint: _Optional[str] = ..., allow_external_traffic: bool = ...) -> None: ...
    class IPEndpointsConfig(_message.Message):
        __slots__ = ("enabled", "enable_public_endpoint", "global_access", "authorized_networks_config", "public_endpoint", "private_endpoint", "private_endpoint_subnetwork")
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        ENABLE_PUBLIC_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
        GLOBAL_ACCESS_FIELD_NUMBER: _ClassVar[int]
        AUTHORIZED_NETWORKS_CONFIG_FIELD_NUMBER: _ClassVar[int]
        PUBLIC_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
        PRIVATE_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
        PRIVATE_ENDPOINT_SUBNETWORK_FIELD_NUMBER: _ClassVar[int]
        enabled: bool
        enable_public_endpoint: bool
        global_access: bool
        authorized_networks_config: MasterAuthorizedNetworksConfig
        public_endpoint: str
        private_endpoint: str
        private_endpoint_subnetwork: str
        def __init__(self, enabled: bool = ..., enable_public_endpoint: bool = ..., global_access: bool = ..., authorized_networks_config: _Optional[_Union[MasterAuthorizedNetworksConfig, _Mapping]] = ..., public_endpoint: _Optional[str] = ..., private_endpoint: _Optional[str] = ..., private_endpoint_subnetwork: _Optional[str] = ...) -> None: ...
    DNS_ENDPOINT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    IP_ENDPOINTS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    dns_endpoint_config: ControlPlaneEndpointsConfig.DNSEndpointConfig
    ip_endpoints_config: ControlPlaneEndpointsConfig.IPEndpointsConfig
    def __init__(self, dns_endpoint_config: _Optional[_Union[ControlPlaneEndpointsConfig.DNSEndpointConfig, _Mapping]] = ..., ip_endpoints_config: _Optional[_Union[ControlPlaneEndpointsConfig.IPEndpointsConfig, _Mapping]] = ...) -> None: ...

class LocalNvmeSsdBlockConfig(_message.Message):
    __slots__ = ("local_ssd_count",)
    LOCAL_SSD_COUNT_FIELD_NUMBER: _ClassVar[int]
    local_ssd_count: int
    def __init__(self, local_ssd_count: _Optional[int] = ...) -> None: ...

class EphemeralStorageLocalSsdConfig(_message.Message):
    __slots__ = ("local_ssd_count",)
    LOCAL_SSD_COUNT_FIELD_NUMBER: _ClassVar[int]
    local_ssd_count: int
    def __init__(self, local_ssd_count: _Optional[int] = ...) -> None: ...

class ResourceManagerTags(_message.Message):
    __slots__ = ("tags",)
    class TagsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    TAGS_FIELD_NUMBER: _ClassVar[int]
    tags: _containers.ScalarMap[str, str]
    def __init__(self, tags: _Optional[_Mapping[str, str]] = ...) -> None: ...

class EnterpriseConfig(_message.Message):
    __slots__ = ("cluster_tier", "desired_tier")
    class ClusterTier(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CLUSTER_TIER_UNSPECIFIED: _ClassVar[EnterpriseConfig.ClusterTier]
        STANDARD: _ClassVar[EnterpriseConfig.ClusterTier]
        ENTERPRISE: _ClassVar[EnterpriseConfig.ClusterTier]
    CLUSTER_TIER_UNSPECIFIED: EnterpriseConfig.ClusterTier
    STANDARD: EnterpriseConfig.ClusterTier
    ENTERPRISE: EnterpriseConfig.ClusterTier
    CLUSTER_TIER_FIELD_NUMBER: _ClassVar[int]
    DESIRED_TIER_FIELD_NUMBER: _ClassVar[int]
    cluster_tier: EnterpriseConfig.ClusterTier
    desired_tier: EnterpriseConfig.ClusterTier
    def __init__(self, cluster_tier: _Optional[_Union[EnterpriseConfig.ClusterTier, str]] = ..., desired_tier: _Optional[_Union[EnterpriseConfig.ClusterTier, str]] = ...) -> None: ...

class SecretManagerConfig(_message.Message):
    __slots__ = ("enabled",)
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    def __init__(self, enabled: bool = ...) -> None: ...

class SecondaryBootDisk(_message.Message):
    __slots__ = ("mode", "disk_image")
    class Mode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MODE_UNSPECIFIED: _ClassVar[SecondaryBootDisk.Mode]
        CONTAINER_IMAGE_CACHE: _ClassVar[SecondaryBootDisk.Mode]
    MODE_UNSPECIFIED: SecondaryBootDisk.Mode
    CONTAINER_IMAGE_CACHE: SecondaryBootDisk.Mode
    MODE_FIELD_NUMBER: _ClassVar[int]
    DISK_IMAGE_FIELD_NUMBER: _ClassVar[int]
    mode: SecondaryBootDisk.Mode
    disk_image: str
    def __init__(self, mode: _Optional[_Union[SecondaryBootDisk.Mode, str]] = ..., disk_image: _Optional[str] = ...) -> None: ...

class SecondaryBootDiskUpdateStrategy(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
