from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import field_info_pb2 as _field_info_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NetworkConfig(_message.Message):
    __slots__ = ("management_cidr", "vmware_engine_network", "vmware_engine_network_canonical", "management_ip_address_layout_version", "dns_server_ip")
    MANAGEMENT_CIDR_FIELD_NUMBER: _ClassVar[int]
    VMWARE_ENGINE_NETWORK_FIELD_NUMBER: _ClassVar[int]
    VMWARE_ENGINE_NETWORK_CANONICAL_FIELD_NUMBER: _ClassVar[int]
    MANAGEMENT_IP_ADDRESS_LAYOUT_VERSION_FIELD_NUMBER: _ClassVar[int]
    DNS_SERVER_IP_FIELD_NUMBER: _ClassVar[int]
    management_cidr: str
    vmware_engine_network: str
    vmware_engine_network_canonical: str
    management_ip_address_layout_version: int
    dns_server_ip: str
    def __init__(self, management_cidr: _Optional[str] = ..., vmware_engine_network: _Optional[str] = ..., vmware_engine_network_canonical: _Optional[str] = ..., management_ip_address_layout_version: _Optional[int] = ..., dns_server_ip: _Optional[str] = ...) -> None: ...

class NodeTypeConfig(_message.Message):
    __slots__ = ("node_count", "custom_core_count")
    NODE_COUNT_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_CORE_COUNT_FIELD_NUMBER: _ClassVar[int]
    node_count: int
    custom_core_count: int
    def __init__(self, node_count: _Optional[int] = ..., custom_core_count: _Optional[int] = ...) -> None: ...

class StretchedClusterConfig(_message.Message):
    __slots__ = ("preferred_location", "secondary_location")
    PREFERRED_LOCATION_FIELD_NUMBER: _ClassVar[int]
    SECONDARY_LOCATION_FIELD_NUMBER: _ClassVar[int]
    preferred_location: str
    secondary_location: str
    def __init__(self, preferred_location: _Optional[str] = ..., secondary_location: _Optional[str] = ...) -> None: ...

class PrivateCloud(_message.Message):
    __slots__ = ("name", "create_time", "update_time", "delete_time", "expire_time", "state", "network_config", "management_cluster", "description", "hcx", "nsx", "vcenter", "uid", "type")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[PrivateCloud.State]
        ACTIVE: _ClassVar[PrivateCloud.State]
        CREATING: _ClassVar[PrivateCloud.State]
        UPDATING: _ClassVar[PrivateCloud.State]
        FAILED: _ClassVar[PrivateCloud.State]
        DELETED: _ClassVar[PrivateCloud.State]
        PURGING: _ClassVar[PrivateCloud.State]
    STATE_UNSPECIFIED: PrivateCloud.State
    ACTIVE: PrivateCloud.State
    CREATING: PrivateCloud.State
    UPDATING: PrivateCloud.State
    FAILED: PrivateCloud.State
    DELETED: PrivateCloud.State
    PURGING: PrivateCloud.State
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STANDARD: _ClassVar[PrivateCloud.Type]
        TIME_LIMITED: _ClassVar[PrivateCloud.Type]
        STRETCHED: _ClassVar[PrivateCloud.Type]
    STANDARD: PrivateCloud.Type
    TIME_LIMITED: PrivateCloud.Type
    STRETCHED: PrivateCloud.Type
    class ManagementCluster(_message.Message):
        __slots__ = ("cluster_id", "node_type_configs", "stretched_cluster_config")
        class NodeTypeConfigsEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: NodeTypeConfig
            def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[NodeTypeConfig, _Mapping]] = ...) -> None: ...
        CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
        NODE_TYPE_CONFIGS_FIELD_NUMBER: _ClassVar[int]
        STRETCHED_CLUSTER_CONFIG_FIELD_NUMBER: _ClassVar[int]
        cluster_id: str
        node_type_configs: _containers.MessageMap[str, NodeTypeConfig]
        stretched_cluster_config: StretchedClusterConfig
        def __init__(self, cluster_id: _Optional[str] = ..., node_type_configs: _Optional[_Mapping[str, NodeTypeConfig]] = ..., stretched_cluster_config: _Optional[_Union[StretchedClusterConfig, _Mapping]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DELETE_TIME_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    NETWORK_CONFIG_FIELD_NUMBER: _ClassVar[int]
    MANAGEMENT_CLUSTER_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    HCX_FIELD_NUMBER: _ClassVar[int]
    NSX_FIELD_NUMBER: _ClassVar[int]
    VCENTER_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    delete_time: _timestamp_pb2.Timestamp
    expire_time: _timestamp_pb2.Timestamp
    state: PrivateCloud.State
    network_config: NetworkConfig
    management_cluster: PrivateCloud.ManagementCluster
    description: str
    hcx: Hcx
    nsx: Nsx
    vcenter: Vcenter
    uid: str
    type: PrivateCloud.Type
    def __init__(self, name: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., delete_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., expire_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., state: _Optional[_Union[PrivateCloud.State, str]] = ..., network_config: _Optional[_Union[NetworkConfig, _Mapping]] = ..., management_cluster: _Optional[_Union[PrivateCloud.ManagementCluster, _Mapping]] = ..., description: _Optional[str] = ..., hcx: _Optional[_Union[Hcx, _Mapping]] = ..., nsx: _Optional[_Union[Nsx, _Mapping]] = ..., vcenter: _Optional[_Union[Vcenter, _Mapping]] = ..., uid: _Optional[str] = ..., type: _Optional[_Union[PrivateCloud.Type, str]] = ...) -> None: ...

class Cluster(_message.Message):
    __slots__ = ("name", "create_time", "update_time", "state", "management", "autoscaling_settings", "uid", "node_type_configs", "stretched_cluster_config")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Cluster.State]
        ACTIVE: _ClassVar[Cluster.State]
        CREATING: _ClassVar[Cluster.State]
        UPDATING: _ClassVar[Cluster.State]
        DELETING: _ClassVar[Cluster.State]
        REPAIRING: _ClassVar[Cluster.State]
    STATE_UNSPECIFIED: Cluster.State
    ACTIVE: Cluster.State
    CREATING: Cluster.State
    UPDATING: Cluster.State
    DELETING: Cluster.State
    REPAIRING: Cluster.State
    class NodeTypeConfigsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: NodeTypeConfig
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[NodeTypeConfig, _Mapping]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    MANAGEMENT_FIELD_NUMBER: _ClassVar[int]
    AUTOSCALING_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    NODE_TYPE_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    STRETCHED_CLUSTER_CONFIG_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    state: Cluster.State
    management: bool
    autoscaling_settings: AutoscalingSettings
    uid: str
    node_type_configs: _containers.MessageMap[str, NodeTypeConfig]
    stretched_cluster_config: StretchedClusterConfig
    def __init__(self, name: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., state: _Optional[_Union[Cluster.State, str]] = ..., management: bool = ..., autoscaling_settings: _Optional[_Union[AutoscalingSettings, _Mapping]] = ..., uid: _Optional[str] = ..., node_type_configs: _Optional[_Mapping[str, NodeTypeConfig]] = ..., stretched_cluster_config: _Optional[_Union[StretchedClusterConfig, _Mapping]] = ...) -> None: ...

class Node(_message.Message):
    __slots__ = ("name", "fqdn", "internal_ip", "node_type_id", "version", "custom_core_count", "state")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Node.State]
        ACTIVE: _ClassVar[Node.State]
        CREATING: _ClassVar[Node.State]
        FAILED: _ClassVar[Node.State]
        UPGRADING: _ClassVar[Node.State]
    STATE_UNSPECIFIED: Node.State
    ACTIVE: Node.State
    CREATING: Node.State
    FAILED: Node.State
    UPGRADING: Node.State
    NAME_FIELD_NUMBER: _ClassVar[int]
    FQDN_FIELD_NUMBER: _ClassVar[int]
    INTERNAL_IP_FIELD_NUMBER: _ClassVar[int]
    NODE_TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_CORE_COUNT_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    name: str
    fqdn: str
    internal_ip: str
    node_type_id: str
    version: str
    custom_core_count: int
    state: Node.State
    def __init__(self, name: _Optional[str] = ..., fqdn: _Optional[str] = ..., internal_ip: _Optional[str] = ..., node_type_id: _Optional[str] = ..., version: _Optional[str] = ..., custom_core_count: _Optional[int] = ..., state: _Optional[_Union[Node.State, str]] = ...) -> None: ...

class ExternalAddress(_message.Message):
    __slots__ = ("name", "create_time", "update_time", "internal_ip", "external_ip", "state", "uid", "description")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[ExternalAddress.State]
        ACTIVE: _ClassVar[ExternalAddress.State]
        CREATING: _ClassVar[ExternalAddress.State]
        UPDATING: _ClassVar[ExternalAddress.State]
        DELETING: _ClassVar[ExternalAddress.State]
    STATE_UNSPECIFIED: ExternalAddress.State
    ACTIVE: ExternalAddress.State
    CREATING: ExternalAddress.State
    UPDATING: ExternalAddress.State
    DELETING: ExternalAddress.State
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    INTERNAL_IP_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_IP_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    internal_ip: str
    external_ip: str
    state: ExternalAddress.State
    uid: str
    description: str
    def __init__(self, name: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., internal_ip: _Optional[str] = ..., external_ip: _Optional[str] = ..., state: _Optional[_Union[ExternalAddress.State, str]] = ..., uid: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class Subnet(_message.Message):
    __slots__ = ("name", "ip_cidr_range", "gateway_ip", "type", "state", "vlan_id")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Subnet.State]
        ACTIVE: _ClassVar[Subnet.State]
        CREATING: _ClassVar[Subnet.State]
        UPDATING: _ClassVar[Subnet.State]
        DELETING: _ClassVar[Subnet.State]
        RECONCILING: _ClassVar[Subnet.State]
        FAILED: _ClassVar[Subnet.State]
    STATE_UNSPECIFIED: Subnet.State
    ACTIVE: Subnet.State
    CREATING: Subnet.State
    UPDATING: Subnet.State
    DELETING: Subnet.State
    RECONCILING: Subnet.State
    FAILED: Subnet.State
    NAME_FIELD_NUMBER: _ClassVar[int]
    IP_CIDR_RANGE_FIELD_NUMBER: _ClassVar[int]
    GATEWAY_IP_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    VLAN_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    ip_cidr_range: str
    gateway_ip: str
    type: str
    state: Subnet.State
    vlan_id: int
    def __init__(self, name: _Optional[str] = ..., ip_cidr_range: _Optional[str] = ..., gateway_ip: _Optional[str] = ..., type: _Optional[str] = ..., state: _Optional[_Union[Subnet.State, str]] = ..., vlan_id: _Optional[int] = ...) -> None: ...

class ExternalAccessRule(_message.Message):
    __slots__ = ("name", "create_time", "update_time", "description", "priority", "action", "ip_protocol", "source_ip_ranges", "source_ports", "destination_ip_ranges", "destination_ports", "state", "uid")
    class Action(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ACTION_UNSPECIFIED: _ClassVar[ExternalAccessRule.Action]
        ALLOW: _ClassVar[ExternalAccessRule.Action]
        DENY: _ClassVar[ExternalAccessRule.Action]
    ACTION_UNSPECIFIED: ExternalAccessRule.Action
    ALLOW: ExternalAccessRule.Action
    DENY: ExternalAccessRule.Action
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[ExternalAccessRule.State]
        ACTIVE: _ClassVar[ExternalAccessRule.State]
        CREATING: _ClassVar[ExternalAccessRule.State]
        UPDATING: _ClassVar[ExternalAccessRule.State]
        DELETING: _ClassVar[ExternalAccessRule.State]
    STATE_UNSPECIFIED: ExternalAccessRule.State
    ACTIVE: ExternalAccessRule.State
    CREATING: ExternalAccessRule.State
    UPDATING: ExternalAccessRule.State
    DELETING: ExternalAccessRule.State
    class IpRange(_message.Message):
        __slots__ = ("ip_address", "ip_address_range", "external_address")
        IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
        IP_ADDRESS_RANGE_FIELD_NUMBER: _ClassVar[int]
        EXTERNAL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
        ip_address: str
        ip_address_range: str
        external_address: str
        def __init__(self, ip_address: _Optional[str] = ..., ip_address_range: _Optional[str] = ..., external_address: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    IP_PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    SOURCE_IP_RANGES_FIELD_NUMBER: _ClassVar[int]
    SOURCE_PORTS_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_IP_RANGES_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_PORTS_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    description: str
    priority: int
    action: ExternalAccessRule.Action
    ip_protocol: str
    source_ip_ranges: _containers.RepeatedCompositeFieldContainer[ExternalAccessRule.IpRange]
    source_ports: _containers.RepeatedScalarFieldContainer[str]
    destination_ip_ranges: _containers.RepeatedCompositeFieldContainer[ExternalAccessRule.IpRange]
    destination_ports: _containers.RepeatedScalarFieldContainer[str]
    state: ExternalAccessRule.State
    uid: str
    def __init__(self, name: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., description: _Optional[str] = ..., priority: _Optional[int] = ..., action: _Optional[_Union[ExternalAccessRule.Action, str]] = ..., ip_protocol: _Optional[str] = ..., source_ip_ranges: _Optional[_Iterable[_Union[ExternalAccessRule.IpRange, _Mapping]]] = ..., source_ports: _Optional[_Iterable[str]] = ..., destination_ip_ranges: _Optional[_Iterable[_Union[ExternalAccessRule.IpRange, _Mapping]]] = ..., destination_ports: _Optional[_Iterable[str]] = ..., state: _Optional[_Union[ExternalAccessRule.State, str]] = ..., uid: _Optional[str] = ...) -> None: ...

class LoggingServer(_message.Message):
    __slots__ = ("name", "create_time", "update_time", "hostname", "port", "protocol", "source_type", "uid")
    class Protocol(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PROTOCOL_UNSPECIFIED: _ClassVar[LoggingServer.Protocol]
        UDP: _ClassVar[LoggingServer.Protocol]
        TCP: _ClassVar[LoggingServer.Protocol]
        TLS: _ClassVar[LoggingServer.Protocol]
        SSL: _ClassVar[LoggingServer.Protocol]
        RELP: _ClassVar[LoggingServer.Protocol]
    PROTOCOL_UNSPECIFIED: LoggingServer.Protocol
    UDP: LoggingServer.Protocol
    TCP: LoggingServer.Protocol
    TLS: LoggingServer.Protocol
    SSL: LoggingServer.Protocol
    RELP: LoggingServer.Protocol
    class SourceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SOURCE_TYPE_UNSPECIFIED: _ClassVar[LoggingServer.SourceType]
        ESXI: _ClassVar[LoggingServer.SourceType]
        VCSA: _ClassVar[LoggingServer.SourceType]
    SOURCE_TYPE_UNSPECIFIED: LoggingServer.SourceType
    ESXI: LoggingServer.SourceType
    VCSA: LoggingServer.SourceType
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    SOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    hostname: str
    port: int
    protocol: LoggingServer.Protocol
    source_type: LoggingServer.SourceType
    uid: str
    def __init__(self, name: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., hostname: _Optional[str] = ..., port: _Optional[int] = ..., protocol: _Optional[_Union[LoggingServer.Protocol, str]] = ..., source_type: _Optional[_Union[LoggingServer.SourceType, str]] = ..., uid: _Optional[str] = ...) -> None: ...

class NodeType(_message.Message):
    __slots__ = ("name", "node_type_id", "display_name", "virtual_cpu_count", "total_core_count", "memory_gb", "disk_size_gb", "available_custom_core_counts", "kind", "families", "capabilities")
    class Kind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        KIND_UNSPECIFIED: _ClassVar[NodeType.Kind]
        STANDARD: _ClassVar[NodeType.Kind]
        STORAGE_ONLY: _ClassVar[NodeType.Kind]
    KIND_UNSPECIFIED: NodeType.Kind
    STANDARD: NodeType.Kind
    STORAGE_ONLY: NodeType.Kind
    class Capability(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CAPABILITY_UNSPECIFIED: _ClassVar[NodeType.Capability]
        STRETCHED_CLUSTERS: _ClassVar[NodeType.Capability]
    CAPABILITY_UNSPECIFIED: NodeType.Capability
    STRETCHED_CLUSTERS: NodeType.Capability
    NAME_FIELD_NUMBER: _ClassVar[int]
    NODE_TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    VIRTUAL_CPU_COUNT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_CORE_COUNT_FIELD_NUMBER: _ClassVar[int]
    MEMORY_GB_FIELD_NUMBER: _ClassVar[int]
    DISK_SIZE_GB_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_CUSTOM_CORE_COUNTS_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    FAMILIES_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    name: str
    node_type_id: str
    display_name: str
    virtual_cpu_count: int
    total_core_count: int
    memory_gb: int
    disk_size_gb: int
    available_custom_core_counts: _containers.RepeatedScalarFieldContainer[int]
    kind: NodeType.Kind
    families: _containers.RepeatedScalarFieldContainer[str]
    capabilities: _containers.RepeatedScalarFieldContainer[NodeType.Capability]
    def __init__(self, name: _Optional[str] = ..., node_type_id: _Optional[str] = ..., display_name: _Optional[str] = ..., virtual_cpu_count: _Optional[int] = ..., total_core_count: _Optional[int] = ..., memory_gb: _Optional[int] = ..., disk_size_gb: _Optional[int] = ..., available_custom_core_counts: _Optional[_Iterable[int]] = ..., kind: _Optional[_Union[NodeType.Kind, str]] = ..., families: _Optional[_Iterable[str]] = ..., capabilities: _Optional[_Iterable[_Union[NodeType.Capability, str]]] = ...) -> None: ...

class Credentials(_message.Message):
    __slots__ = ("username", "password")
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    username: str
    password: str
    def __init__(self, username: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class HcxActivationKey(_message.Message):
    __slots__ = ("name", "create_time", "state", "activation_key", "uid")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[HcxActivationKey.State]
        AVAILABLE: _ClassVar[HcxActivationKey.State]
        CONSUMED: _ClassVar[HcxActivationKey.State]
        CREATING: _ClassVar[HcxActivationKey.State]
    STATE_UNSPECIFIED: HcxActivationKey.State
    AVAILABLE: HcxActivationKey.State
    CONSUMED: HcxActivationKey.State
    CREATING: HcxActivationKey.State
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ACTIVATION_KEY_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    state: HcxActivationKey.State
    activation_key: str
    uid: str
    def __init__(self, name: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., state: _Optional[_Union[HcxActivationKey.State, str]] = ..., activation_key: _Optional[str] = ..., uid: _Optional[str] = ...) -> None: ...

class Hcx(_message.Message):
    __slots__ = ("internal_ip", "version", "state", "fqdn")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Hcx.State]
        ACTIVE: _ClassVar[Hcx.State]
        CREATING: _ClassVar[Hcx.State]
        ACTIVATING: _ClassVar[Hcx.State]
    STATE_UNSPECIFIED: Hcx.State
    ACTIVE: Hcx.State
    CREATING: Hcx.State
    ACTIVATING: Hcx.State
    INTERNAL_IP_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    FQDN_FIELD_NUMBER: _ClassVar[int]
    internal_ip: str
    version: str
    state: Hcx.State
    fqdn: str
    def __init__(self, internal_ip: _Optional[str] = ..., version: _Optional[str] = ..., state: _Optional[_Union[Hcx.State, str]] = ..., fqdn: _Optional[str] = ...) -> None: ...

class Nsx(_message.Message):
    __slots__ = ("internal_ip", "version", "state", "fqdn")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Nsx.State]
        ACTIVE: _ClassVar[Nsx.State]
        CREATING: _ClassVar[Nsx.State]
    STATE_UNSPECIFIED: Nsx.State
    ACTIVE: Nsx.State
    CREATING: Nsx.State
    INTERNAL_IP_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    FQDN_FIELD_NUMBER: _ClassVar[int]
    internal_ip: str
    version: str
    state: Nsx.State
    fqdn: str
    def __init__(self, internal_ip: _Optional[str] = ..., version: _Optional[str] = ..., state: _Optional[_Union[Nsx.State, str]] = ..., fqdn: _Optional[str] = ...) -> None: ...

class Vcenter(_message.Message):
    __slots__ = ("internal_ip", "version", "state", "fqdn")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Vcenter.State]
        ACTIVE: _ClassVar[Vcenter.State]
        CREATING: _ClassVar[Vcenter.State]
    STATE_UNSPECIFIED: Vcenter.State
    ACTIVE: Vcenter.State
    CREATING: Vcenter.State
    INTERNAL_IP_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    FQDN_FIELD_NUMBER: _ClassVar[int]
    internal_ip: str
    version: str
    state: Vcenter.State
    fqdn: str
    def __init__(self, internal_ip: _Optional[str] = ..., version: _Optional[str] = ..., state: _Optional[_Union[Vcenter.State, str]] = ..., fqdn: _Optional[str] = ...) -> None: ...

class AutoscalingSettings(_message.Message):
    __slots__ = ("autoscaling_policies", "min_cluster_node_count", "max_cluster_node_count", "cool_down_period")
    class Thresholds(_message.Message):
        __slots__ = ("scale_out", "scale_in")
        SCALE_OUT_FIELD_NUMBER: _ClassVar[int]
        SCALE_IN_FIELD_NUMBER: _ClassVar[int]
        scale_out: int
        scale_in: int
        def __init__(self, scale_out: _Optional[int] = ..., scale_in: _Optional[int] = ...) -> None: ...
    class AutoscalingPolicy(_message.Message):
        __slots__ = ("node_type_id", "scale_out_size", "cpu_thresholds", "granted_memory_thresholds", "consumed_memory_thresholds", "storage_thresholds")
        NODE_TYPE_ID_FIELD_NUMBER: _ClassVar[int]
        SCALE_OUT_SIZE_FIELD_NUMBER: _ClassVar[int]
        CPU_THRESHOLDS_FIELD_NUMBER: _ClassVar[int]
        GRANTED_MEMORY_THRESHOLDS_FIELD_NUMBER: _ClassVar[int]
        CONSUMED_MEMORY_THRESHOLDS_FIELD_NUMBER: _ClassVar[int]
        STORAGE_THRESHOLDS_FIELD_NUMBER: _ClassVar[int]
        node_type_id: str
        scale_out_size: int
        cpu_thresholds: AutoscalingSettings.Thresholds
        granted_memory_thresholds: AutoscalingSettings.Thresholds
        consumed_memory_thresholds: AutoscalingSettings.Thresholds
        storage_thresholds: AutoscalingSettings.Thresholds
        def __init__(self, node_type_id: _Optional[str] = ..., scale_out_size: _Optional[int] = ..., cpu_thresholds: _Optional[_Union[AutoscalingSettings.Thresholds, _Mapping]] = ..., granted_memory_thresholds: _Optional[_Union[AutoscalingSettings.Thresholds, _Mapping]] = ..., consumed_memory_thresholds: _Optional[_Union[AutoscalingSettings.Thresholds, _Mapping]] = ..., storage_thresholds: _Optional[_Union[AutoscalingSettings.Thresholds, _Mapping]] = ...) -> None: ...
    class AutoscalingPoliciesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: AutoscalingSettings.AutoscalingPolicy
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[AutoscalingSettings.AutoscalingPolicy, _Mapping]] = ...) -> None: ...
    AUTOSCALING_POLICIES_FIELD_NUMBER: _ClassVar[int]
    MIN_CLUSTER_NODE_COUNT_FIELD_NUMBER: _ClassVar[int]
    MAX_CLUSTER_NODE_COUNT_FIELD_NUMBER: _ClassVar[int]
    COOL_DOWN_PERIOD_FIELD_NUMBER: _ClassVar[int]
    autoscaling_policies: _containers.MessageMap[str, AutoscalingSettings.AutoscalingPolicy]
    min_cluster_node_count: int
    max_cluster_node_count: int
    cool_down_period: _duration_pb2.Duration
    def __init__(self, autoscaling_policies: _Optional[_Mapping[str, AutoscalingSettings.AutoscalingPolicy]] = ..., min_cluster_node_count: _Optional[int] = ..., max_cluster_node_count: _Optional[int] = ..., cool_down_period: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...

class DnsForwarding(_message.Message):
    __slots__ = ("name", "create_time", "update_time", "forwarding_rules")
    class ForwardingRule(_message.Message):
        __slots__ = ("domain", "name_servers")
        DOMAIN_FIELD_NUMBER: _ClassVar[int]
        NAME_SERVERS_FIELD_NUMBER: _ClassVar[int]
        domain: str
        name_servers: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, domain: _Optional[str] = ..., name_servers: _Optional[_Iterable[str]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    FORWARDING_RULES_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    forwarding_rules: _containers.RepeatedCompositeFieldContainer[DnsForwarding.ForwardingRule]
    def __init__(self, name: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., forwarding_rules: _Optional[_Iterable[_Union[DnsForwarding.ForwardingRule, _Mapping]]] = ...) -> None: ...

class NetworkPeering(_message.Message):
    __slots__ = ("name", "create_time", "update_time", "peer_network", "export_custom_routes", "import_custom_routes", "exchange_subnet_routes", "export_custom_routes_with_public_ip", "import_custom_routes_with_public_ip", "state", "state_details", "peer_mtu", "peer_network_type", "uid", "vmware_engine_network", "description")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[NetworkPeering.State]
        INACTIVE: _ClassVar[NetworkPeering.State]
        ACTIVE: _ClassVar[NetworkPeering.State]
        CREATING: _ClassVar[NetworkPeering.State]
        DELETING: _ClassVar[NetworkPeering.State]
    STATE_UNSPECIFIED: NetworkPeering.State
    INACTIVE: NetworkPeering.State
    ACTIVE: NetworkPeering.State
    CREATING: NetworkPeering.State
    DELETING: NetworkPeering.State
    class PeerNetworkType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PEER_NETWORK_TYPE_UNSPECIFIED: _ClassVar[NetworkPeering.PeerNetworkType]
        STANDARD: _ClassVar[NetworkPeering.PeerNetworkType]
        VMWARE_ENGINE_NETWORK: _ClassVar[NetworkPeering.PeerNetworkType]
        PRIVATE_SERVICES_ACCESS: _ClassVar[NetworkPeering.PeerNetworkType]
        NETAPP_CLOUD_VOLUMES: _ClassVar[NetworkPeering.PeerNetworkType]
        THIRD_PARTY_SERVICE: _ClassVar[NetworkPeering.PeerNetworkType]
        DELL_POWERSCALE: _ClassVar[NetworkPeering.PeerNetworkType]
        GOOGLE_CLOUD_NETAPP_VOLUMES: _ClassVar[NetworkPeering.PeerNetworkType]
    PEER_NETWORK_TYPE_UNSPECIFIED: NetworkPeering.PeerNetworkType
    STANDARD: NetworkPeering.PeerNetworkType
    VMWARE_ENGINE_NETWORK: NetworkPeering.PeerNetworkType
    PRIVATE_SERVICES_ACCESS: NetworkPeering.PeerNetworkType
    NETAPP_CLOUD_VOLUMES: NetworkPeering.PeerNetworkType
    THIRD_PARTY_SERVICE: NetworkPeering.PeerNetworkType
    DELL_POWERSCALE: NetworkPeering.PeerNetworkType
    GOOGLE_CLOUD_NETAPP_VOLUMES: NetworkPeering.PeerNetworkType
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    PEER_NETWORK_FIELD_NUMBER: _ClassVar[int]
    EXPORT_CUSTOM_ROUTES_FIELD_NUMBER: _ClassVar[int]
    IMPORT_CUSTOM_ROUTES_FIELD_NUMBER: _ClassVar[int]
    EXCHANGE_SUBNET_ROUTES_FIELD_NUMBER: _ClassVar[int]
    EXPORT_CUSTOM_ROUTES_WITH_PUBLIC_IP_FIELD_NUMBER: _ClassVar[int]
    IMPORT_CUSTOM_ROUTES_WITH_PUBLIC_IP_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATE_DETAILS_FIELD_NUMBER: _ClassVar[int]
    PEER_MTU_FIELD_NUMBER: _ClassVar[int]
    PEER_NETWORK_TYPE_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    VMWARE_ENGINE_NETWORK_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    peer_network: str
    export_custom_routes: bool
    import_custom_routes: bool
    exchange_subnet_routes: bool
    export_custom_routes_with_public_ip: bool
    import_custom_routes_with_public_ip: bool
    state: NetworkPeering.State
    state_details: str
    peer_mtu: int
    peer_network_type: NetworkPeering.PeerNetworkType
    uid: str
    vmware_engine_network: str
    description: str
    def __init__(self, name: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., peer_network: _Optional[str] = ..., export_custom_routes: bool = ..., import_custom_routes: bool = ..., exchange_subnet_routes: bool = ..., export_custom_routes_with_public_ip: bool = ..., import_custom_routes_with_public_ip: bool = ..., state: _Optional[_Union[NetworkPeering.State, str]] = ..., state_details: _Optional[str] = ..., peer_mtu: _Optional[int] = ..., peer_network_type: _Optional[_Union[NetworkPeering.PeerNetworkType, str]] = ..., uid: _Optional[str] = ..., vmware_engine_network: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class PeeringRoute(_message.Message):
    __slots__ = ("dest_range", "type", "next_hop_region", "priority", "imported", "direction")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[PeeringRoute.Type]
        DYNAMIC_PEERING_ROUTE: _ClassVar[PeeringRoute.Type]
        STATIC_PEERING_ROUTE: _ClassVar[PeeringRoute.Type]
        SUBNET_PEERING_ROUTE: _ClassVar[PeeringRoute.Type]
    TYPE_UNSPECIFIED: PeeringRoute.Type
    DYNAMIC_PEERING_ROUTE: PeeringRoute.Type
    STATIC_PEERING_ROUTE: PeeringRoute.Type
    SUBNET_PEERING_ROUTE: PeeringRoute.Type
    class Direction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DIRECTION_UNSPECIFIED: _ClassVar[PeeringRoute.Direction]
        INCOMING: _ClassVar[PeeringRoute.Direction]
        OUTGOING: _ClassVar[PeeringRoute.Direction]
    DIRECTION_UNSPECIFIED: PeeringRoute.Direction
    INCOMING: PeeringRoute.Direction
    OUTGOING: PeeringRoute.Direction
    DEST_RANGE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NEXT_HOP_REGION_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    IMPORTED_FIELD_NUMBER: _ClassVar[int]
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    dest_range: str
    type: PeeringRoute.Type
    next_hop_region: str
    priority: int
    imported: bool
    direction: PeeringRoute.Direction
    def __init__(self, dest_range: _Optional[str] = ..., type: _Optional[_Union[PeeringRoute.Type, str]] = ..., next_hop_region: _Optional[str] = ..., priority: _Optional[int] = ..., imported: bool = ..., direction: _Optional[_Union[PeeringRoute.Direction, str]] = ...) -> None: ...

class NetworkPolicy(_message.Message):
    __slots__ = ("name", "create_time", "update_time", "internet_access", "external_ip", "edge_services_cidr", "uid", "vmware_engine_network", "description", "vmware_engine_network_canonical")
    class NetworkService(_message.Message):
        __slots__ = ("enabled", "state")
        class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            STATE_UNSPECIFIED: _ClassVar[NetworkPolicy.NetworkService.State]
            UNPROVISIONED: _ClassVar[NetworkPolicy.NetworkService.State]
            RECONCILING: _ClassVar[NetworkPolicy.NetworkService.State]
            ACTIVE: _ClassVar[NetworkPolicy.NetworkService.State]
        STATE_UNSPECIFIED: NetworkPolicy.NetworkService.State
        UNPROVISIONED: NetworkPolicy.NetworkService.State
        RECONCILING: NetworkPolicy.NetworkService.State
        ACTIVE: NetworkPolicy.NetworkService.State
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        STATE_FIELD_NUMBER: _ClassVar[int]
        enabled: bool
        state: NetworkPolicy.NetworkService.State
        def __init__(self, enabled: bool = ..., state: _Optional[_Union[NetworkPolicy.NetworkService.State, str]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    INTERNET_ACCESS_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_IP_FIELD_NUMBER: _ClassVar[int]
    EDGE_SERVICES_CIDR_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    VMWARE_ENGINE_NETWORK_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    VMWARE_ENGINE_NETWORK_CANONICAL_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    internet_access: NetworkPolicy.NetworkService
    external_ip: NetworkPolicy.NetworkService
    edge_services_cidr: str
    uid: str
    vmware_engine_network: str
    description: str
    vmware_engine_network_canonical: str
    def __init__(self, name: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., internet_access: _Optional[_Union[NetworkPolicy.NetworkService, _Mapping]] = ..., external_ip: _Optional[_Union[NetworkPolicy.NetworkService, _Mapping]] = ..., edge_services_cidr: _Optional[str] = ..., uid: _Optional[str] = ..., vmware_engine_network: _Optional[str] = ..., description: _Optional[str] = ..., vmware_engine_network_canonical: _Optional[str] = ...) -> None: ...

class ManagementDnsZoneBinding(_message.Message):
    __slots__ = ("name", "create_time", "update_time", "state", "description", "vpc_network", "vmware_engine_network", "uid")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[ManagementDnsZoneBinding.State]
        ACTIVE: _ClassVar[ManagementDnsZoneBinding.State]
        CREATING: _ClassVar[ManagementDnsZoneBinding.State]
        UPDATING: _ClassVar[ManagementDnsZoneBinding.State]
        DELETING: _ClassVar[ManagementDnsZoneBinding.State]
        FAILED: _ClassVar[ManagementDnsZoneBinding.State]
    STATE_UNSPECIFIED: ManagementDnsZoneBinding.State
    ACTIVE: ManagementDnsZoneBinding.State
    CREATING: ManagementDnsZoneBinding.State
    UPDATING: ManagementDnsZoneBinding.State
    DELETING: ManagementDnsZoneBinding.State
    FAILED: ManagementDnsZoneBinding.State
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    VPC_NETWORK_FIELD_NUMBER: _ClassVar[int]
    VMWARE_ENGINE_NETWORK_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    state: ManagementDnsZoneBinding.State
    description: str
    vpc_network: str
    vmware_engine_network: str
    uid: str
    def __init__(self, name: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., state: _Optional[_Union[ManagementDnsZoneBinding.State, str]] = ..., description: _Optional[str] = ..., vpc_network: _Optional[str] = ..., vmware_engine_network: _Optional[str] = ..., uid: _Optional[str] = ...) -> None: ...

class VmwareEngineNetwork(_message.Message):
    __slots__ = ("name", "create_time", "update_time", "description", "vpc_networks", "state", "type", "uid", "etag")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[VmwareEngineNetwork.State]
        CREATING: _ClassVar[VmwareEngineNetwork.State]
        ACTIVE: _ClassVar[VmwareEngineNetwork.State]
        UPDATING: _ClassVar[VmwareEngineNetwork.State]
        DELETING: _ClassVar[VmwareEngineNetwork.State]
    STATE_UNSPECIFIED: VmwareEngineNetwork.State
    CREATING: VmwareEngineNetwork.State
    ACTIVE: VmwareEngineNetwork.State
    UPDATING: VmwareEngineNetwork.State
    DELETING: VmwareEngineNetwork.State
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[VmwareEngineNetwork.Type]
        LEGACY: _ClassVar[VmwareEngineNetwork.Type]
        STANDARD: _ClassVar[VmwareEngineNetwork.Type]
    TYPE_UNSPECIFIED: VmwareEngineNetwork.Type
    LEGACY: VmwareEngineNetwork.Type
    STANDARD: VmwareEngineNetwork.Type
    class VpcNetwork(_message.Message):
        __slots__ = ("type", "network")
        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            TYPE_UNSPECIFIED: _ClassVar[VmwareEngineNetwork.VpcNetwork.Type]
            INTRANET: _ClassVar[VmwareEngineNetwork.VpcNetwork.Type]
            INTERNET: _ClassVar[VmwareEngineNetwork.VpcNetwork.Type]
            GOOGLE_CLOUD: _ClassVar[VmwareEngineNetwork.VpcNetwork.Type]
        TYPE_UNSPECIFIED: VmwareEngineNetwork.VpcNetwork.Type
        INTRANET: VmwareEngineNetwork.VpcNetwork.Type
        INTERNET: VmwareEngineNetwork.VpcNetwork.Type
        GOOGLE_CLOUD: VmwareEngineNetwork.VpcNetwork.Type
        TYPE_FIELD_NUMBER: _ClassVar[int]
        NETWORK_FIELD_NUMBER: _ClassVar[int]
        type: VmwareEngineNetwork.VpcNetwork.Type
        network: str
        def __init__(self, type: _Optional[_Union[VmwareEngineNetwork.VpcNetwork.Type, str]] = ..., network: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    VPC_NETWORKS_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    description: str
    vpc_networks: _containers.RepeatedCompositeFieldContainer[VmwareEngineNetwork.VpcNetwork]
    state: VmwareEngineNetwork.State
    type: VmwareEngineNetwork.Type
    uid: str
    etag: str
    def __init__(self, name: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., description: _Optional[str] = ..., vpc_networks: _Optional[_Iterable[_Union[VmwareEngineNetwork.VpcNetwork, _Mapping]]] = ..., state: _Optional[_Union[VmwareEngineNetwork.State, str]] = ..., type: _Optional[_Union[VmwareEngineNetwork.Type, str]] = ..., uid: _Optional[str] = ..., etag: _Optional[str] = ...) -> None: ...

class PrivateConnection(_message.Message):
    __slots__ = ("name", "create_time", "update_time", "description", "state", "vmware_engine_network", "vmware_engine_network_canonical", "type", "peering_id", "routing_mode", "uid", "service_network", "peering_state")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[PrivateConnection.State]
        CREATING: _ClassVar[PrivateConnection.State]
        ACTIVE: _ClassVar[PrivateConnection.State]
        UPDATING: _ClassVar[PrivateConnection.State]
        DELETING: _ClassVar[PrivateConnection.State]
        UNPROVISIONED: _ClassVar[PrivateConnection.State]
        FAILED: _ClassVar[PrivateConnection.State]
    STATE_UNSPECIFIED: PrivateConnection.State
    CREATING: PrivateConnection.State
    ACTIVE: PrivateConnection.State
    UPDATING: PrivateConnection.State
    DELETING: PrivateConnection.State
    UNPROVISIONED: PrivateConnection.State
    FAILED: PrivateConnection.State
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[PrivateConnection.Type]
        PRIVATE_SERVICE_ACCESS: _ClassVar[PrivateConnection.Type]
        NETAPP_CLOUD_VOLUMES: _ClassVar[PrivateConnection.Type]
        DELL_POWERSCALE: _ClassVar[PrivateConnection.Type]
        THIRD_PARTY_SERVICE: _ClassVar[PrivateConnection.Type]
    TYPE_UNSPECIFIED: PrivateConnection.Type
    PRIVATE_SERVICE_ACCESS: PrivateConnection.Type
    NETAPP_CLOUD_VOLUMES: PrivateConnection.Type
    DELL_POWERSCALE: PrivateConnection.Type
    THIRD_PARTY_SERVICE: PrivateConnection.Type
    class RoutingMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ROUTING_MODE_UNSPECIFIED: _ClassVar[PrivateConnection.RoutingMode]
        GLOBAL: _ClassVar[PrivateConnection.RoutingMode]
        REGIONAL: _ClassVar[PrivateConnection.RoutingMode]
    ROUTING_MODE_UNSPECIFIED: PrivateConnection.RoutingMode
    GLOBAL: PrivateConnection.RoutingMode
    REGIONAL: PrivateConnection.RoutingMode
    class PeeringState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PEERING_STATE_UNSPECIFIED: _ClassVar[PrivateConnection.PeeringState]
        PEERING_ACTIVE: _ClassVar[PrivateConnection.PeeringState]
        PEERING_INACTIVE: _ClassVar[PrivateConnection.PeeringState]
    PEERING_STATE_UNSPECIFIED: PrivateConnection.PeeringState
    PEERING_ACTIVE: PrivateConnection.PeeringState
    PEERING_INACTIVE: PrivateConnection.PeeringState
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    VMWARE_ENGINE_NETWORK_FIELD_NUMBER: _ClassVar[int]
    VMWARE_ENGINE_NETWORK_CANONICAL_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PEERING_ID_FIELD_NUMBER: _ClassVar[int]
    ROUTING_MODE_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    SERVICE_NETWORK_FIELD_NUMBER: _ClassVar[int]
    PEERING_STATE_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    description: str
    state: PrivateConnection.State
    vmware_engine_network: str
    vmware_engine_network_canonical: str
    type: PrivateConnection.Type
    peering_id: str
    routing_mode: PrivateConnection.RoutingMode
    uid: str
    service_network: str
    peering_state: PrivateConnection.PeeringState
    def __init__(self, name: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., description: _Optional[str] = ..., state: _Optional[_Union[PrivateConnection.State, str]] = ..., vmware_engine_network: _Optional[str] = ..., vmware_engine_network_canonical: _Optional[str] = ..., type: _Optional[_Union[PrivateConnection.Type, str]] = ..., peering_id: _Optional[str] = ..., routing_mode: _Optional[_Union[PrivateConnection.RoutingMode, str]] = ..., uid: _Optional[str] = ..., service_network: _Optional[str] = ..., peering_state: _Optional[_Union[PrivateConnection.PeeringState, str]] = ...) -> None: ...

class LocationMetadata(_message.Message):
    __slots__ = ("capabilities",)
    class Capability(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CAPABILITY_UNSPECIFIED: _ClassVar[LocationMetadata.Capability]
        STRETCHED_CLUSTERS: _ClassVar[LocationMetadata.Capability]
    CAPABILITY_UNSPECIFIED: LocationMetadata.Capability
    STRETCHED_CLUSTERS: LocationMetadata.Capability
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    capabilities: _containers.RepeatedScalarFieldContainer[LocationMetadata.Capability]
    def __init__(self, capabilities: _Optional[_Iterable[_Union[LocationMetadata.Capability, str]]] = ...) -> None: ...

class DnsBindPermission(_message.Message):
    __slots__ = ("name", "principals")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PRINCIPALS_FIELD_NUMBER: _ClassVar[int]
    name: str
    principals: _containers.RepeatedCompositeFieldContainer[Principal]
    def __init__(self, name: _Optional[str] = ..., principals: _Optional[_Iterable[_Union[Principal, _Mapping]]] = ...) -> None: ...

class Principal(_message.Message):
    __slots__ = ("user", "service_account")
    USER_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    user: str
    service_account: str
    def __init__(self, user: _Optional[str] = ..., service_account: _Optional[str] = ...) -> None: ...
