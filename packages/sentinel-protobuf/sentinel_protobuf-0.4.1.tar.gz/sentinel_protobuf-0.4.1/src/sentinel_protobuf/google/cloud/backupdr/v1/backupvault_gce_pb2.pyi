from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import field_info_pb2 as _field_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class KeyRevocationActionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    KEY_REVOCATION_ACTION_TYPE_UNSPECIFIED: _ClassVar[KeyRevocationActionType]
    NONE: _ClassVar[KeyRevocationActionType]
    STOP: _ClassVar[KeyRevocationActionType]
KEY_REVOCATION_ACTION_TYPE_UNSPECIFIED: KeyRevocationActionType
NONE: KeyRevocationActionType
STOP: KeyRevocationActionType

class ComputeInstanceBackupProperties(_message.Message):
    __slots__ = ("description", "tags", "machine_type", "can_ip_forward", "network_interface", "disk", "metadata", "service_account", "scheduling", "guest_accelerator", "min_cpu_platform", "key_revocation_action_type", "source_instance", "labels")
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    MACHINE_TYPE_FIELD_NUMBER: _ClassVar[int]
    CAN_IP_FORWARD_FIELD_NUMBER: _ClassVar[int]
    NETWORK_INTERFACE_FIELD_NUMBER: _ClassVar[int]
    DISK_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    SCHEDULING_FIELD_NUMBER: _ClassVar[int]
    GUEST_ACCELERATOR_FIELD_NUMBER: _ClassVar[int]
    MIN_CPU_PLATFORM_FIELD_NUMBER: _ClassVar[int]
    KEY_REVOCATION_ACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_INSTANCE_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    description: str
    tags: Tags
    machine_type: str
    can_ip_forward: bool
    network_interface: _containers.RepeatedCompositeFieldContainer[NetworkInterface]
    disk: _containers.RepeatedCompositeFieldContainer[AttachedDisk]
    metadata: Metadata
    service_account: _containers.RepeatedCompositeFieldContainer[ServiceAccount]
    scheduling: Scheduling
    guest_accelerator: _containers.RepeatedCompositeFieldContainer[AcceleratorConfig]
    min_cpu_platform: str
    key_revocation_action_type: KeyRevocationActionType
    source_instance: str
    labels: _containers.ScalarMap[str, str]
    def __init__(self, description: _Optional[str] = ..., tags: _Optional[_Union[Tags, _Mapping]] = ..., machine_type: _Optional[str] = ..., can_ip_forward: bool = ..., network_interface: _Optional[_Iterable[_Union[NetworkInterface, _Mapping]]] = ..., disk: _Optional[_Iterable[_Union[AttachedDisk, _Mapping]]] = ..., metadata: _Optional[_Union[Metadata, _Mapping]] = ..., service_account: _Optional[_Iterable[_Union[ServiceAccount, _Mapping]]] = ..., scheduling: _Optional[_Union[Scheduling, _Mapping]] = ..., guest_accelerator: _Optional[_Iterable[_Union[AcceleratorConfig, _Mapping]]] = ..., min_cpu_platform: _Optional[str] = ..., key_revocation_action_type: _Optional[_Union[KeyRevocationActionType, str]] = ..., source_instance: _Optional[str] = ..., labels: _Optional[_Mapping[str, str]] = ...) -> None: ...

class ComputeInstanceRestoreProperties(_message.Message):
    __slots__ = ("name", "advanced_machine_features", "can_ip_forward", "confidential_instance_config", "deletion_protection", "description", "disks", "display_device", "guest_accelerators", "hostname", "instance_encryption_key", "key_revocation_action_type", "labels", "machine_type", "metadata", "min_cpu_platform", "network_interfaces", "network_performance_config", "params", "private_ipv6_google_access", "allocation_affinity", "resource_policies", "scheduling", "service_accounts", "tags")
    class InstancePrivateIpv6GoogleAccess(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        INSTANCE_PRIVATE_IPV6_GOOGLE_ACCESS_UNSPECIFIED: _ClassVar[ComputeInstanceRestoreProperties.InstancePrivateIpv6GoogleAccess]
        INHERIT_FROM_SUBNETWORK: _ClassVar[ComputeInstanceRestoreProperties.InstancePrivateIpv6GoogleAccess]
        ENABLE_OUTBOUND_VM_ACCESS_TO_GOOGLE: _ClassVar[ComputeInstanceRestoreProperties.InstancePrivateIpv6GoogleAccess]
        ENABLE_BIDIRECTIONAL_ACCESS_TO_GOOGLE: _ClassVar[ComputeInstanceRestoreProperties.InstancePrivateIpv6GoogleAccess]
    INSTANCE_PRIVATE_IPV6_GOOGLE_ACCESS_UNSPECIFIED: ComputeInstanceRestoreProperties.InstancePrivateIpv6GoogleAccess
    INHERIT_FROM_SUBNETWORK: ComputeInstanceRestoreProperties.InstancePrivateIpv6GoogleAccess
    ENABLE_OUTBOUND_VM_ACCESS_TO_GOOGLE: ComputeInstanceRestoreProperties.InstancePrivateIpv6GoogleAccess
    ENABLE_BIDIRECTIONAL_ACCESS_TO_GOOGLE: ComputeInstanceRestoreProperties.InstancePrivateIpv6GoogleAccess
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    ADVANCED_MACHINE_FEATURES_FIELD_NUMBER: _ClassVar[int]
    CAN_IP_FORWARD_FIELD_NUMBER: _ClassVar[int]
    CONFIDENTIAL_INSTANCE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DELETION_PROTECTION_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DISKS_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_DEVICE_FIELD_NUMBER: _ClassVar[int]
    GUEST_ACCELERATORS_FIELD_NUMBER: _ClassVar[int]
    HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_ENCRYPTION_KEY_FIELD_NUMBER: _ClassVar[int]
    KEY_REVOCATION_ACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    MACHINE_TYPE_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    MIN_CPU_PLATFORM_FIELD_NUMBER: _ClassVar[int]
    NETWORK_INTERFACES_FIELD_NUMBER: _ClassVar[int]
    NETWORK_PERFORMANCE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_IPV6_GOOGLE_ACCESS_FIELD_NUMBER: _ClassVar[int]
    ALLOCATION_AFFINITY_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_POLICIES_FIELD_NUMBER: _ClassVar[int]
    SCHEDULING_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNTS_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    name: str
    advanced_machine_features: AdvancedMachineFeatures
    can_ip_forward: bool
    confidential_instance_config: ConfidentialInstanceConfig
    deletion_protection: bool
    description: str
    disks: _containers.RepeatedCompositeFieldContainer[AttachedDisk]
    display_device: DisplayDevice
    guest_accelerators: _containers.RepeatedCompositeFieldContainer[AcceleratorConfig]
    hostname: str
    instance_encryption_key: CustomerEncryptionKey
    key_revocation_action_type: KeyRevocationActionType
    labels: _containers.ScalarMap[str, str]
    machine_type: str
    metadata: Metadata
    min_cpu_platform: str
    network_interfaces: _containers.RepeatedCompositeFieldContainer[NetworkInterface]
    network_performance_config: NetworkPerformanceConfig
    params: InstanceParams
    private_ipv6_google_access: ComputeInstanceRestoreProperties.InstancePrivateIpv6GoogleAccess
    allocation_affinity: AllocationAffinity
    resource_policies: _containers.RepeatedScalarFieldContainer[str]
    scheduling: Scheduling
    service_accounts: _containers.RepeatedCompositeFieldContainer[ServiceAccount]
    tags: Tags
    def __init__(self, name: _Optional[str] = ..., advanced_machine_features: _Optional[_Union[AdvancedMachineFeatures, _Mapping]] = ..., can_ip_forward: bool = ..., confidential_instance_config: _Optional[_Union[ConfidentialInstanceConfig, _Mapping]] = ..., deletion_protection: bool = ..., description: _Optional[str] = ..., disks: _Optional[_Iterable[_Union[AttachedDisk, _Mapping]]] = ..., display_device: _Optional[_Union[DisplayDevice, _Mapping]] = ..., guest_accelerators: _Optional[_Iterable[_Union[AcceleratorConfig, _Mapping]]] = ..., hostname: _Optional[str] = ..., instance_encryption_key: _Optional[_Union[CustomerEncryptionKey, _Mapping]] = ..., key_revocation_action_type: _Optional[_Union[KeyRevocationActionType, str]] = ..., labels: _Optional[_Mapping[str, str]] = ..., machine_type: _Optional[str] = ..., metadata: _Optional[_Union[Metadata, _Mapping]] = ..., min_cpu_platform: _Optional[str] = ..., network_interfaces: _Optional[_Iterable[_Union[NetworkInterface, _Mapping]]] = ..., network_performance_config: _Optional[_Union[NetworkPerformanceConfig, _Mapping]] = ..., params: _Optional[_Union[InstanceParams, _Mapping]] = ..., private_ipv6_google_access: _Optional[_Union[ComputeInstanceRestoreProperties.InstancePrivateIpv6GoogleAccess, str]] = ..., allocation_affinity: _Optional[_Union[AllocationAffinity, _Mapping]] = ..., resource_policies: _Optional[_Iterable[str]] = ..., scheduling: _Optional[_Union[Scheduling, _Mapping]] = ..., service_accounts: _Optional[_Iterable[_Union[ServiceAccount, _Mapping]]] = ..., tags: _Optional[_Union[Tags, _Mapping]] = ...) -> None: ...

class ComputeInstanceTargetEnvironment(_message.Message):
    __slots__ = ("project", "zone")
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    project: str
    zone: str
    def __init__(self, project: _Optional[str] = ..., zone: _Optional[str] = ...) -> None: ...

class ComputeInstanceDataSourceProperties(_message.Message):
    __slots__ = ("name", "description", "machine_type", "total_disk_count", "total_disk_size_gb")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    MACHINE_TYPE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_DISK_COUNT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_DISK_SIZE_GB_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    machine_type: str
    total_disk_count: int
    total_disk_size_gb: int
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., machine_type: _Optional[str] = ..., total_disk_count: _Optional[int] = ..., total_disk_size_gb: _Optional[int] = ...) -> None: ...

class AdvancedMachineFeatures(_message.Message):
    __slots__ = ("enable_nested_virtualization", "threads_per_core", "visible_core_count", "enable_uefi_networking")
    ENABLE_NESTED_VIRTUALIZATION_FIELD_NUMBER: _ClassVar[int]
    THREADS_PER_CORE_FIELD_NUMBER: _ClassVar[int]
    VISIBLE_CORE_COUNT_FIELD_NUMBER: _ClassVar[int]
    ENABLE_UEFI_NETWORKING_FIELD_NUMBER: _ClassVar[int]
    enable_nested_virtualization: bool
    threads_per_core: int
    visible_core_count: int
    enable_uefi_networking: bool
    def __init__(self, enable_nested_virtualization: bool = ..., threads_per_core: _Optional[int] = ..., visible_core_count: _Optional[int] = ..., enable_uefi_networking: bool = ...) -> None: ...

class ConfidentialInstanceConfig(_message.Message):
    __slots__ = ("enable_confidential_compute",)
    ENABLE_CONFIDENTIAL_COMPUTE_FIELD_NUMBER: _ClassVar[int]
    enable_confidential_compute: bool
    def __init__(self, enable_confidential_compute: bool = ...) -> None: ...

class DisplayDevice(_message.Message):
    __slots__ = ("enable_display",)
    ENABLE_DISPLAY_FIELD_NUMBER: _ClassVar[int]
    enable_display: bool
    def __init__(self, enable_display: bool = ...) -> None: ...

class AcceleratorConfig(_message.Message):
    __slots__ = ("accelerator_type", "accelerator_count")
    ACCELERATOR_TYPE_FIELD_NUMBER: _ClassVar[int]
    ACCELERATOR_COUNT_FIELD_NUMBER: _ClassVar[int]
    accelerator_type: str
    accelerator_count: int
    def __init__(self, accelerator_type: _Optional[str] = ..., accelerator_count: _Optional[int] = ...) -> None: ...

class CustomerEncryptionKey(_message.Message):
    __slots__ = ("raw_key", "rsa_encrypted_key", "kms_key_name", "kms_key_service_account")
    RAW_KEY_FIELD_NUMBER: _ClassVar[int]
    RSA_ENCRYPTED_KEY_FIELD_NUMBER: _ClassVar[int]
    KMS_KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    KMS_KEY_SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    raw_key: str
    rsa_encrypted_key: str
    kms_key_name: str
    kms_key_service_account: str
    def __init__(self, raw_key: _Optional[str] = ..., rsa_encrypted_key: _Optional[str] = ..., kms_key_name: _Optional[str] = ..., kms_key_service_account: _Optional[str] = ...) -> None: ...

class Entry(_message.Message):
    __slots__ = ("key", "value")
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: str
    def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class Metadata(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[Entry]
    def __init__(self, items: _Optional[_Iterable[_Union[Entry, _Mapping]]] = ...) -> None: ...

class NetworkInterface(_message.Message):
    __slots__ = ("network", "subnetwork", "ip_address", "ipv6_address", "internal_ipv6_prefix_length", "name", "access_configs", "ipv6_access_configs", "alias_ip_ranges", "stack_type", "ipv6_access_type", "queue_count", "nic_type", "network_attachment")
    class StackType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STACK_TYPE_UNSPECIFIED: _ClassVar[NetworkInterface.StackType]
        IPV4_ONLY: _ClassVar[NetworkInterface.StackType]
        IPV4_IPV6: _ClassVar[NetworkInterface.StackType]
    STACK_TYPE_UNSPECIFIED: NetworkInterface.StackType
    IPV4_ONLY: NetworkInterface.StackType
    IPV4_IPV6: NetworkInterface.StackType
    class Ipv6AccessType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED_IPV6_ACCESS_TYPE: _ClassVar[NetworkInterface.Ipv6AccessType]
        INTERNAL: _ClassVar[NetworkInterface.Ipv6AccessType]
        EXTERNAL: _ClassVar[NetworkInterface.Ipv6AccessType]
    UNSPECIFIED_IPV6_ACCESS_TYPE: NetworkInterface.Ipv6AccessType
    INTERNAL: NetworkInterface.Ipv6AccessType
    EXTERNAL: NetworkInterface.Ipv6AccessType
    class NicType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NIC_TYPE_UNSPECIFIED: _ClassVar[NetworkInterface.NicType]
        VIRTIO_NET: _ClassVar[NetworkInterface.NicType]
        GVNIC: _ClassVar[NetworkInterface.NicType]
    NIC_TYPE_UNSPECIFIED: NetworkInterface.NicType
    VIRTIO_NET: NetworkInterface.NicType
    GVNIC: NetworkInterface.NicType
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    SUBNETWORK_FIELD_NUMBER: _ClassVar[int]
    IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    IPV6_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    INTERNAL_IPV6_PREFIX_LENGTH_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ACCESS_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    IPV6_ACCESS_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    ALIAS_IP_RANGES_FIELD_NUMBER: _ClassVar[int]
    STACK_TYPE_FIELD_NUMBER: _ClassVar[int]
    IPV6_ACCESS_TYPE_FIELD_NUMBER: _ClassVar[int]
    QUEUE_COUNT_FIELD_NUMBER: _ClassVar[int]
    NIC_TYPE_FIELD_NUMBER: _ClassVar[int]
    NETWORK_ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
    network: str
    subnetwork: str
    ip_address: str
    ipv6_address: str
    internal_ipv6_prefix_length: int
    name: str
    access_configs: _containers.RepeatedCompositeFieldContainer[AccessConfig]
    ipv6_access_configs: _containers.RepeatedCompositeFieldContainer[AccessConfig]
    alias_ip_ranges: _containers.RepeatedCompositeFieldContainer[AliasIpRange]
    stack_type: NetworkInterface.StackType
    ipv6_access_type: NetworkInterface.Ipv6AccessType
    queue_count: int
    nic_type: NetworkInterface.NicType
    network_attachment: str
    def __init__(self, network: _Optional[str] = ..., subnetwork: _Optional[str] = ..., ip_address: _Optional[str] = ..., ipv6_address: _Optional[str] = ..., internal_ipv6_prefix_length: _Optional[int] = ..., name: _Optional[str] = ..., access_configs: _Optional[_Iterable[_Union[AccessConfig, _Mapping]]] = ..., ipv6_access_configs: _Optional[_Iterable[_Union[AccessConfig, _Mapping]]] = ..., alias_ip_ranges: _Optional[_Iterable[_Union[AliasIpRange, _Mapping]]] = ..., stack_type: _Optional[_Union[NetworkInterface.StackType, str]] = ..., ipv6_access_type: _Optional[_Union[NetworkInterface.Ipv6AccessType, str]] = ..., queue_count: _Optional[int] = ..., nic_type: _Optional[_Union[NetworkInterface.NicType, str]] = ..., network_attachment: _Optional[str] = ...) -> None: ...

class NetworkPerformanceConfig(_message.Message):
    __slots__ = ("total_egress_bandwidth_tier",)
    class Tier(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TIER_UNSPECIFIED: _ClassVar[NetworkPerformanceConfig.Tier]
        DEFAULT: _ClassVar[NetworkPerformanceConfig.Tier]
        TIER_1: _ClassVar[NetworkPerformanceConfig.Tier]
    TIER_UNSPECIFIED: NetworkPerformanceConfig.Tier
    DEFAULT: NetworkPerformanceConfig.Tier
    TIER_1: NetworkPerformanceConfig.Tier
    TOTAL_EGRESS_BANDWIDTH_TIER_FIELD_NUMBER: _ClassVar[int]
    total_egress_bandwidth_tier: NetworkPerformanceConfig.Tier
    def __init__(self, total_egress_bandwidth_tier: _Optional[_Union[NetworkPerformanceConfig.Tier, str]] = ...) -> None: ...

class AccessConfig(_message.Message):
    __slots__ = ("type", "name", "external_ip", "external_ipv6", "external_ipv6_prefix_length", "set_public_ptr", "public_ptr_domain_name", "network_tier")
    class AccessType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ACCESS_TYPE_UNSPECIFIED: _ClassVar[AccessConfig.AccessType]
        ONE_TO_ONE_NAT: _ClassVar[AccessConfig.AccessType]
        DIRECT_IPV6: _ClassVar[AccessConfig.AccessType]
    ACCESS_TYPE_UNSPECIFIED: AccessConfig.AccessType
    ONE_TO_ONE_NAT: AccessConfig.AccessType
    DIRECT_IPV6: AccessConfig.AccessType
    class NetworkTier(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NETWORK_TIER_UNSPECIFIED: _ClassVar[AccessConfig.NetworkTier]
        PREMIUM: _ClassVar[AccessConfig.NetworkTier]
        STANDARD: _ClassVar[AccessConfig.NetworkTier]
    NETWORK_TIER_UNSPECIFIED: AccessConfig.NetworkTier
    PREMIUM: AccessConfig.NetworkTier
    STANDARD: AccessConfig.NetworkTier
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_IP_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_IPV6_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_IPV6_PREFIX_LENGTH_FIELD_NUMBER: _ClassVar[int]
    SET_PUBLIC_PTR_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_PTR_DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    NETWORK_TIER_FIELD_NUMBER: _ClassVar[int]
    type: AccessConfig.AccessType
    name: str
    external_ip: str
    external_ipv6: str
    external_ipv6_prefix_length: int
    set_public_ptr: bool
    public_ptr_domain_name: str
    network_tier: AccessConfig.NetworkTier
    def __init__(self, type: _Optional[_Union[AccessConfig.AccessType, str]] = ..., name: _Optional[str] = ..., external_ip: _Optional[str] = ..., external_ipv6: _Optional[str] = ..., external_ipv6_prefix_length: _Optional[int] = ..., set_public_ptr: bool = ..., public_ptr_domain_name: _Optional[str] = ..., network_tier: _Optional[_Union[AccessConfig.NetworkTier, str]] = ...) -> None: ...

class AliasIpRange(_message.Message):
    __slots__ = ("ip_cidr_range", "subnetwork_range_name")
    IP_CIDR_RANGE_FIELD_NUMBER: _ClassVar[int]
    SUBNETWORK_RANGE_NAME_FIELD_NUMBER: _ClassVar[int]
    ip_cidr_range: str
    subnetwork_range_name: str
    def __init__(self, ip_cidr_range: _Optional[str] = ..., subnetwork_range_name: _Optional[str] = ...) -> None: ...

class InstanceParams(_message.Message):
    __slots__ = ("resource_manager_tags",)
    class ResourceManagerTagsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    RESOURCE_MANAGER_TAGS_FIELD_NUMBER: _ClassVar[int]
    resource_manager_tags: _containers.ScalarMap[str, str]
    def __init__(self, resource_manager_tags: _Optional[_Mapping[str, str]] = ...) -> None: ...

class AllocationAffinity(_message.Message):
    __slots__ = ("consume_allocation_type", "key", "values")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[AllocationAffinity.Type]
        NO_RESERVATION: _ClassVar[AllocationAffinity.Type]
        ANY_RESERVATION: _ClassVar[AllocationAffinity.Type]
        SPECIFIC_RESERVATION: _ClassVar[AllocationAffinity.Type]
    TYPE_UNSPECIFIED: AllocationAffinity.Type
    NO_RESERVATION: AllocationAffinity.Type
    ANY_RESERVATION: AllocationAffinity.Type
    SPECIFIC_RESERVATION: AllocationAffinity.Type
    CONSUME_ALLOCATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    consume_allocation_type: AllocationAffinity.Type
    key: str
    values: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, consume_allocation_type: _Optional[_Union[AllocationAffinity.Type, str]] = ..., key: _Optional[str] = ..., values: _Optional[_Iterable[str]] = ...) -> None: ...

class Scheduling(_message.Message):
    __slots__ = ("on_host_maintenance", "automatic_restart", "preemptible", "node_affinities", "min_node_cpus", "provisioning_model", "instance_termination_action", "local_ssd_recovery_timeout")
    class OnHostMaintenance(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ON_HOST_MAINTENANCE_UNSPECIFIED: _ClassVar[Scheduling.OnHostMaintenance]
        TERMINATE: _ClassVar[Scheduling.OnHostMaintenance]
        MIGRATE: _ClassVar[Scheduling.OnHostMaintenance]
    ON_HOST_MAINTENANCE_UNSPECIFIED: Scheduling.OnHostMaintenance
    TERMINATE: Scheduling.OnHostMaintenance
    MIGRATE: Scheduling.OnHostMaintenance
    class ProvisioningModel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PROVISIONING_MODEL_UNSPECIFIED: _ClassVar[Scheduling.ProvisioningModel]
        STANDARD: _ClassVar[Scheduling.ProvisioningModel]
        SPOT: _ClassVar[Scheduling.ProvisioningModel]
    PROVISIONING_MODEL_UNSPECIFIED: Scheduling.ProvisioningModel
    STANDARD: Scheduling.ProvisioningModel
    SPOT: Scheduling.ProvisioningModel
    class InstanceTerminationAction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        INSTANCE_TERMINATION_ACTION_UNSPECIFIED: _ClassVar[Scheduling.InstanceTerminationAction]
        DELETE: _ClassVar[Scheduling.InstanceTerminationAction]
        STOP: _ClassVar[Scheduling.InstanceTerminationAction]
    INSTANCE_TERMINATION_ACTION_UNSPECIFIED: Scheduling.InstanceTerminationAction
    DELETE: Scheduling.InstanceTerminationAction
    STOP: Scheduling.InstanceTerminationAction
    class NodeAffinity(_message.Message):
        __slots__ = ("key", "operator", "values")
        class Operator(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            OPERATOR_UNSPECIFIED: _ClassVar[Scheduling.NodeAffinity.Operator]
            IN: _ClassVar[Scheduling.NodeAffinity.Operator]
            NOT_IN: _ClassVar[Scheduling.NodeAffinity.Operator]
        OPERATOR_UNSPECIFIED: Scheduling.NodeAffinity.Operator
        IN: Scheduling.NodeAffinity.Operator
        NOT_IN: Scheduling.NodeAffinity.Operator
        KEY_FIELD_NUMBER: _ClassVar[int]
        OPERATOR_FIELD_NUMBER: _ClassVar[int]
        VALUES_FIELD_NUMBER: _ClassVar[int]
        key: str
        operator: Scheduling.NodeAffinity.Operator
        values: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, key: _Optional[str] = ..., operator: _Optional[_Union[Scheduling.NodeAffinity.Operator, str]] = ..., values: _Optional[_Iterable[str]] = ...) -> None: ...
    ON_HOST_MAINTENANCE_FIELD_NUMBER: _ClassVar[int]
    AUTOMATIC_RESTART_FIELD_NUMBER: _ClassVar[int]
    PREEMPTIBLE_FIELD_NUMBER: _ClassVar[int]
    NODE_AFFINITIES_FIELD_NUMBER: _ClassVar[int]
    MIN_NODE_CPUS_FIELD_NUMBER: _ClassVar[int]
    PROVISIONING_MODEL_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_TERMINATION_ACTION_FIELD_NUMBER: _ClassVar[int]
    LOCAL_SSD_RECOVERY_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    on_host_maintenance: Scheduling.OnHostMaintenance
    automatic_restart: bool
    preemptible: bool
    node_affinities: _containers.RepeatedCompositeFieldContainer[Scheduling.NodeAffinity]
    min_node_cpus: int
    provisioning_model: Scheduling.ProvisioningModel
    instance_termination_action: Scheduling.InstanceTerminationAction
    local_ssd_recovery_timeout: SchedulingDuration
    def __init__(self, on_host_maintenance: _Optional[_Union[Scheduling.OnHostMaintenance, str]] = ..., automatic_restart: bool = ..., preemptible: bool = ..., node_affinities: _Optional[_Iterable[_Union[Scheduling.NodeAffinity, _Mapping]]] = ..., min_node_cpus: _Optional[int] = ..., provisioning_model: _Optional[_Union[Scheduling.ProvisioningModel, str]] = ..., instance_termination_action: _Optional[_Union[Scheduling.InstanceTerminationAction, str]] = ..., local_ssd_recovery_timeout: _Optional[_Union[SchedulingDuration, _Mapping]] = ...) -> None: ...

class SchedulingDuration(_message.Message):
    __slots__ = ("seconds", "nanos")
    SECONDS_FIELD_NUMBER: _ClassVar[int]
    NANOS_FIELD_NUMBER: _ClassVar[int]
    seconds: int
    nanos: int
    def __init__(self, seconds: _Optional[int] = ..., nanos: _Optional[int] = ...) -> None: ...

class ServiceAccount(_message.Message):
    __slots__ = ("email", "scopes")
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    SCOPES_FIELD_NUMBER: _ClassVar[int]
    email: str
    scopes: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, email: _Optional[str] = ..., scopes: _Optional[_Iterable[str]] = ...) -> None: ...

class Tags(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, items: _Optional[_Iterable[str]] = ...) -> None: ...

class AttachedDisk(_message.Message):
    __slots__ = ("initialize_params", "device_name", "kind", "disk_type_deprecated", "mode", "source", "index", "boot", "auto_delete", "license", "disk_interface", "guest_os_feature", "disk_encryption_key", "disk_size_gb", "saved_state", "disk_type", "type")
    class DiskType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DISK_TYPE_UNSPECIFIED: _ClassVar[AttachedDisk.DiskType]
        SCRATCH: _ClassVar[AttachedDisk.DiskType]
        PERSISTENT: _ClassVar[AttachedDisk.DiskType]
    DISK_TYPE_UNSPECIFIED: AttachedDisk.DiskType
    SCRATCH: AttachedDisk.DiskType
    PERSISTENT: AttachedDisk.DiskType
    class DiskMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DISK_MODE_UNSPECIFIED: _ClassVar[AttachedDisk.DiskMode]
        READ_WRITE: _ClassVar[AttachedDisk.DiskMode]
        READ_ONLY: _ClassVar[AttachedDisk.DiskMode]
        LOCKED: _ClassVar[AttachedDisk.DiskMode]
    DISK_MODE_UNSPECIFIED: AttachedDisk.DiskMode
    READ_WRITE: AttachedDisk.DiskMode
    READ_ONLY: AttachedDisk.DiskMode
    LOCKED: AttachedDisk.DiskMode
    class DiskInterface(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DISK_INTERFACE_UNSPECIFIED: _ClassVar[AttachedDisk.DiskInterface]
        SCSI: _ClassVar[AttachedDisk.DiskInterface]
        NVME: _ClassVar[AttachedDisk.DiskInterface]
        NVDIMM: _ClassVar[AttachedDisk.DiskInterface]
        ISCSI: _ClassVar[AttachedDisk.DiskInterface]
    DISK_INTERFACE_UNSPECIFIED: AttachedDisk.DiskInterface
    SCSI: AttachedDisk.DiskInterface
    NVME: AttachedDisk.DiskInterface
    NVDIMM: AttachedDisk.DiskInterface
    ISCSI: AttachedDisk.DiskInterface
    class DiskSavedState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DISK_SAVED_STATE_UNSPECIFIED: _ClassVar[AttachedDisk.DiskSavedState]
        PRESERVED: _ClassVar[AttachedDisk.DiskSavedState]
    DISK_SAVED_STATE_UNSPECIFIED: AttachedDisk.DiskSavedState
    PRESERVED: AttachedDisk.DiskSavedState
    class InitializeParams(_message.Message):
        __slots__ = ("disk_name", "replica_zones")
        DISK_NAME_FIELD_NUMBER: _ClassVar[int]
        REPLICA_ZONES_FIELD_NUMBER: _ClassVar[int]
        disk_name: str
        replica_zones: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, disk_name: _Optional[str] = ..., replica_zones: _Optional[_Iterable[str]] = ...) -> None: ...
    INITIALIZE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    DEVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    DISK_TYPE_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    BOOT_FIELD_NUMBER: _ClassVar[int]
    AUTO_DELETE_FIELD_NUMBER: _ClassVar[int]
    LICENSE_FIELD_NUMBER: _ClassVar[int]
    DISK_INTERFACE_FIELD_NUMBER: _ClassVar[int]
    GUEST_OS_FEATURE_FIELD_NUMBER: _ClassVar[int]
    DISK_ENCRYPTION_KEY_FIELD_NUMBER: _ClassVar[int]
    DISK_SIZE_GB_FIELD_NUMBER: _ClassVar[int]
    SAVED_STATE_FIELD_NUMBER: _ClassVar[int]
    DISK_TYPE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    initialize_params: AttachedDisk.InitializeParams
    device_name: str
    kind: str
    disk_type_deprecated: AttachedDisk.DiskType
    mode: AttachedDisk.DiskMode
    source: str
    index: int
    boot: bool
    auto_delete: bool
    license: _containers.RepeatedScalarFieldContainer[str]
    disk_interface: AttachedDisk.DiskInterface
    guest_os_feature: _containers.RepeatedCompositeFieldContainer[GuestOsFeature]
    disk_encryption_key: CustomerEncryptionKey
    disk_size_gb: int
    saved_state: AttachedDisk.DiskSavedState
    disk_type: str
    type: AttachedDisk.DiskType
    def __init__(self, initialize_params: _Optional[_Union[AttachedDisk.InitializeParams, _Mapping]] = ..., device_name: _Optional[str] = ..., kind: _Optional[str] = ..., disk_type_deprecated: _Optional[_Union[AttachedDisk.DiskType, str]] = ..., mode: _Optional[_Union[AttachedDisk.DiskMode, str]] = ..., source: _Optional[str] = ..., index: _Optional[int] = ..., boot: bool = ..., auto_delete: bool = ..., license: _Optional[_Iterable[str]] = ..., disk_interface: _Optional[_Union[AttachedDisk.DiskInterface, str]] = ..., guest_os_feature: _Optional[_Iterable[_Union[GuestOsFeature, _Mapping]]] = ..., disk_encryption_key: _Optional[_Union[CustomerEncryptionKey, _Mapping]] = ..., disk_size_gb: _Optional[int] = ..., saved_state: _Optional[_Union[AttachedDisk.DiskSavedState, str]] = ..., disk_type: _Optional[str] = ..., type: _Optional[_Union[AttachedDisk.DiskType, str]] = ...) -> None: ...

class GuestOsFeature(_message.Message):
    __slots__ = ("type",)
    class FeatureType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FEATURE_TYPE_UNSPECIFIED: _ClassVar[GuestOsFeature.FeatureType]
        VIRTIO_SCSI_MULTIQUEUE: _ClassVar[GuestOsFeature.FeatureType]
        WINDOWS: _ClassVar[GuestOsFeature.FeatureType]
        MULTI_IP_SUBNET: _ClassVar[GuestOsFeature.FeatureType]
        UEFI_COMPATIBLE: _ClassVar[GuestOsFeature.FeatureType]
        SECURE_BOOT: _ClassVar[GuestOsFeature.FeatureType]
        GVNIC: _ClassVar[GuestOsFeature.FeatureType]
        SEV_CAPABLE: _ClassVar[GuestOsFeature.FeatureType]
        BARE_METAL_LINUX_COMPATIBLE: _ClassVar[GuestOsFeature.FeatureType]
        SUSPEND_RESUME_COMPATIBLE: _ClassVar[GuestOsFeature.FeatureType]
        SEV_LIVE_MIGRATABLE: _ClassVar[GuestOsFeature.FeatureType]
        SEV_SNP_CAPABLE: _ClassVar[GuestOsFeature.FeatureType]
        TDX_CAPABLE: _ClassVar[GuestOsFeature.FeatureType]
        IDPF: _ClassVar[GuestOsFeature.FeatureType]
        SEV_LIVE_MIGRATABLE_V2: _ClassVar[GuestOsFeature.FeatureType]
    FEATURE_TYPE_UNSPECIFIED: GuestOsFeature.FeatureType
    VIRTIO_SCSI_MULTIQUEUE: GuestOsFeature.FeatureType
    WINDOWS: GuestOsFeature.FeatureType
    MULTI_IP_SUBNET: GuestOsFeature.FeatureType
    UEFI_COMPATIBLE: GuestOsFeature.FeatureType
    SECURE_BOOT: GuestOsFeature.FeatureType
    GVNIC: GuestOsFeature.FeatureType
    SEV_CAPABLE: GuestOsFeature.FeatureType
    BARE_METAL_LINUX_COMPATIBLE: GuestOsFeature.FeatureType
    SUSPEND_RESUME_COMPATIBLE: GuestOsFeature.FeatureType
    SEV_LIVE_MIGRATABLE: GuestOsFeature.FeatureType
    SEV_SNP_CAPABLE: GuestOsFeature.FeatureType
    TDX_CAPABLE: GuestOsFeature.FeatureType
    IDPF: GuestOsFeature.FeatureType
    SEV_LIVE_MIGRATABLE_V2: GuestOsFeature.FeatureType
    TYPE_FIELD_NUMBER: _ClassVar[int]
    type: GuestOsFeature.FeatureType
    def __init__(self, type: _Optional[_Union[GuestOsFeature.FeatureType, str]] = ...) -> None: ...
