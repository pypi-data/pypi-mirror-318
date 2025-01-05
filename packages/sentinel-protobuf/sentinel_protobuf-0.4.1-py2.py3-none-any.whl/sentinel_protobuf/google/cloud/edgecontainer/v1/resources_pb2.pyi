from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class KmsKeyState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    KMS_KEY_STATE_UNSPECIFIED: _ClassVar[KmsKeyState]
    KMS_KEY_STATE_KEY_AVAILABLE: _ClassVar[KmsKeyState]
    KMS_KEY_STATE_KEY_UNAVAILABLE: _ClassVar[KmsKeyState]

class ResourceState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RESOURCE_STATE_UNSPECIFIED: _ClassVar[ResourceState]
    RESOURCE_STATE_LOCK_DOWN: _ClassVar[ResourceState]
    RESOURCE_STATE_LOCK_DOWN_PENDING: _ClassVar[ResourceState]
KMS_KEY_STATE_UNSPECIFIED: KmsKeyState
KMS_KEY_STATE_KEY_AVAILABLE: KmsKeyState
KMS_KEY_STATE_KEY_UNAVAILABLE: KmsKeyState
RESOURCE_STATE_UNSPECIFIED: ResourceState
RESOURCE_STATE_LOCK_DOWN: ResourceState
RESOURCE_STATE_LOCK_DOWN_PENDING: ResourceState

class Cluster(_message.Message):
    __slots__ = ('name', 'create_time', 'update_time', 'labels', 'fleet', 'networking', 'authorization', 'default_max_pods_per_node', 'endpoint', 'port', 'cluster_ca_certificate', 'maintenance_policy', 'control_plane_version', 'node_version', 'control_plane', 'system_addons_config', 'external_load_balancer_ipv4_address_pools', 'control_plane_encryption', 'status', 'maintenance_events', 'target_version', 'release_channel', 'survivability_config', 'external_load_balancer_ipv6_address_pools', 'connection_state')

    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATUS_UNSPECIFIED: _ClassVar[Cluster.Status]
        PROVISIONING: _ClassVar[Cluster.Status]
        RUNNING: _ClassVar[Cluster.Status]
        DELETING: _ClassVar[Cluster.Status]
        ERROR: _ClassVar[Cluster.Status]
        RECONCILING: _ClassVar[Cluster.Status]
    STATUS_UNSPECIFIED: Cluster.Status
    PROVISIONING: Cluster.Status
    RUNNING: Cluster.Status
    DELETING: Cluster.Status
    ERROR: Cluster.Status
    RECONCILING: Cluster.Status

    class ReleaseChannel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RELEASE_CHANNEL_UNSPECIFIED: _ClassVar[Cluster.ReleaseChannel]
        NONE: _ClassVar[Cluster.ReleaseChannel]
        REGULAR: _ClassVar[Cluster.ReleaseChannel]
    RELEASE_CHANNEL_UNSPECIFIED: Cluster.ReleaseChannel
    NONE: Cluster.ReleaseChannel
    REGULAR: Cluster.ReleaseChannel

    class ControlPlane(_message.Message):
        __slots__ = ('remote', 'local')

        class SharedDeploymentPolicy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            SHARED_DEPLOYMENT_POLICY_UNSPECIFIED: _ClassVar[Cluster.ControlPlane.SharedDeploymentPolicy]
            ALLOWED: _ClassVar[Cluster.ControlPlane.SharedDeploymentPolicy]
            DISALLOWED: _ClassVar[Cluster.ControlPlane.SharedDeploymentPolicy]
        SHARED_DEPLOYMENT_POLICY_UNSPECIFIED: Cluster.ControlPlane.SharedDeploymentPolicy
        ALLOWED: Cluster.ControlPlane.SharedDeploymentPolicy
        DISALLOWED: Cluster.ControlPlane.SharedDeploymentPolicy

        class Remote(_message.Message):
            __slots__ = ()

            def __init__(self) -> None:
                ...

        class Local(_message.Message):
            __slots__ = ('node_location', 'node_count', 'machine_filter', 'shared_deployment_policy', 'control_plane_node_storage_schema')
            NODE_LOCATION_FIELD_NUMBER: _ClassVar[int]
            NODE_COUNT_FIELD_NUMBER: _ClassVar[int]
            MACHINE_FILTER_FIELD_NUMBER: _ClassVar[int]
            SHARED_DEPLOYMENT_POLICY_FIELD_NUMBER: _ClassVar[int]
            CONTROL_PLANE_NODE_STORAGE_SCHEMA_FIELD_NUMBER: _ClassVar[int]
            node_location: str
            node_count: int
            machine_filter: str
            shared_deployment_policy: Cluster.ControlPlane.SharedDeploymentPolicy
            control_plane_node_storage_schema: str

            def __init__(self, node_location: _Optional[str]=..., node_count: _Optional[int]=..., machine_filter: _Optional[str]=..., shared_deployment_policy: _Optional[_Union[Cluster.ControlPlane.SharedDeploymentPolicy, str]]=..., control_plane_node_storage_schema: _Optional[str]=...) -> None:
                ...
        REMOTE_FIELD_NUMBER: _ClassVar[int]
        LOCAL_FIELD_NUMBER: _ClassVar[int]
        remote: Cluster.ControlPlane.Remote
        local: Cluster.ControlPlane.Local

        def __init__(self, remote: _Optional[_Union[Cluster.ControlPlane.Remote, _Mapping]]=..., local: _Optional[_Union[Cluster.ControlPlane.Local, _Mapping]]=...) -> None:
            ...

    class SystemAddonsConfig(_message.Message):
        __slots__ = ('ingress', 'vm_service_config')

        class Ingress(_message.Message):
            __slots__ = ('disabled', 'ipv4_vip')
            DISABLED_FIELD_NUMBER: _ClassVar[int]
            IPV4_VIP_FIELD_NUMBER: _ClassVar[int]
            disabled: bool
            ipv4_vip: str

            def __init__(self, disabled: bool=..., ipv4_vip: _Optional[str]=...) -> None:
                ...

        class VMServiceConfig(_message.Message):
            __slots__ = ('vmm_enabled',)
            VMM_ENABLED_FIELD_NUMBER: _ClassVar[int]
            vmm_enabled: bool

            def __init__(self, vmm_enabled: bool=...) -> None:
                ...
        INGRESS_FIELD_NUMBER: _ClassVar[int]
        VM_SERVICE_CONFIG_FIELD_NUMBER: _ClassVar[int]
        ingress: Cluster.SystemAddonsConfig.Ingress
        vm_service_config: Cluster.SystemAddonsConfig.VMServiceConfig

        def __init__(self, ingress: _Optional[_Union[Cluster.SystemAddonsConfig.Ingress, _Mapping]]=..., vm_service_config: _Optional[_Union[Cluster.SystemAddonsConfig.VMServiceConfig, _Mapping]]=...) -> None:
            ...

    class ControlPlaneEncryption(_message.Message):
        __slots__ = ('kms_key', 'kms_key_active_version', 'kms_key_state', 'kms_status', 'resource_state')
        KMS_KEY_FIELD_NUMBER: _ClassVar[int]
        KMS_KEY_ACTIVE_VERSION_FIELD_NUMBER: _ClassVar[int]
        KMS_KEY_STATE_FIELD_NUMBER: _ClassVar[int]
        KMS_STATUS_FIELD_NUMBER: _ClassVar[int]
        RESOURCE_STATE_FIELD_NUMBER: _ClassVar[int]
        kms_key: str
        kms_key_active_version: str
        kms_key_state: KmsKeyState
        kms_status: _status_pb2.Status
        resource_state: ResourceState

        def __init__(self, kms_key: _Optional[str]=..., kms_key_active_version: _Optional[str]=..., kms_key_state: _Optional[_Union[KmsKeyState, str]]=..., kms_status: _Optional[_Union[_status_pb2.Status, _Mapping]]=..., resource_state: _Optional[_Union[ResourceState, str]]=...) -> None:
            ...

    class MaintenanceEvent(_message.Message):
        __slots__ = ('uuid', 'target_version', 'operation', 'type', 'schedule', 'state', 'create_time', 'start_time', 'end_time', 'update_time')

        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            TYPE_UNSPECIFIED: _ClassVar[Cluster.MaintenanceEvent.Type]
            USER_INITIATED_UPGRADE: _ClassVar[Cluster.MaintenanceEvent.Type]
            GOOGLE_DRIVEN_UPGRADE: _ClassVar[Cluster.MaintenanceEvent.Type]
        TYPE_UNSPECIFIED: Cluster.MaintenanceEvent.Type
        USER_INITIATED_UPGRADE: Cluster.MaintenanceEvent.Type
        GOOGLE_DRIVEN_UPGRADE: Cluster.MaintenanceEvent.Type

        class Schedule(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            SCHEDULE_UNSPECIFIED: _ClassVar[Cluster.MaintenanceEvent.Schedule]
            IMMEDIATELY: _ClassVar[Cluster.MaintenanceEvent.Schedule]
        SCHEDULE_UNSPECIFIED: Cluster.MaintenanceEvent.Schedule
        IMMEDIATELY: Cluster.MaintenanceEvent.Schedule

        class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            STATE_UNSPECIFIED: _ClassVar[Cluster.MaintenanceEvent.State]
            RECONCILING: _ClassVar[Cluster.MaintenanceEvent.State]
            SUCCEEDED: _ClassVar[Cluster.MaintenanceEvent.State]
            FAILED: _ClassVar[Cluster.MaintenanceEvent.State]
        STATE_UNSPECIFIED: Cluster.MaintenanceEvent.State
        RECONCILING: Cluster.MaintenanceEvent.State
        SUCCEEDED: Cluster.MaintenanceEvent.State
        FAILED: Cluster.MaintenanceEvent.State
        UUID_FIELD_NUMBER: _ClassVar[int]
        TARGET_VERSION_FIELD_NUMBER: _ClassVar[int]
        OPERATION_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        SCHEDULE_FIELD_NUMBER: _ClassVar[int]
        STATE_FIELD_NUMBER: _ClassVar[int]
        CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
        START_TIME_FIELD_NUMBER: _ClassVar[int]
        END_TIME_FIELD_NUMBER: _ClassVar[int]
        UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
        uuid: str
        target_version: str
        operation: str
        type: Cluster.MaintenanceEvent.Type
        schedule: Cluster.MaintenanceEvent.Schedule
        state: Cluster.MaintenanceEvent.State
        create_time: _timestamp_pb2.Timestamp
        start_time: _timestamp_pb2.Timestamp
        end_time: _timestamp_pb2.Timestamp
        update_time: _timestamp_pb2.Timestamp

        def __init__(self, uuid: _Optional[str]=..., target_version: _Optional[str]=..., operation: _Optional[str]=..., type: _Optional[_Union[Cluster.MaintenanceEvent.Type, str]]=..., schedule: _Optional[_Union[Cluster.MaintenanceEvent.Schedule, str]]=..., state: _Optional[_Union[Cluster.MaintenanceEvent.State, str]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
            ...

    class SurvivabilityConfig(_message.Message):
        __slots__ = ('offline_reboot_ttl',)
        OFFLINE_REBOOT_TTL_FIELD_NUMBER: _ClassVar[int]
        offline_reboot_ttl: _duration_pb2.Duration

        def __init__(self, offline_reboot_ttl: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=...) -> None:
            ...

    class ConnectionState(_message.Message):
        __slots__ = ('state', 'update_time')

        class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            STATE_UNSPECIFIED: _ClassVar[Cluster.ConnectionState.State]
            DISCONNECTED: _ClassVar[Cluster.ConnectionState.State]
            CONNECTED: _ClassVar[Cluster.ConnectionState.State]
            CONNECTED_AND_SYNCING: _ClassVar[Cluster.ConnectionState.State]
        STATE_UNSPECIFIED: Cluster.ConnectionState.State
        DISCONNECTED: Cluster.ConnectionState.State
        CONNECTED: Cluster.ConnectionState.State
        CONNECTED_AND_SYNCING: Cluster.ConnectionState.State
        STATE_FIELD_NUMBER: _ClassVar[int]
        UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
        state: Cluster.ConnectionState.State
        update_time: _timestamp_pb2.Timestamp

        def __init__(self, state: _Optional[_Union[Cluster.ConnectionState.State, str]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
            ...

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    FLEET_FIELD_NUMBER: _ClassVar[int]
    NETWORKING_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZATION_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_MAX_PODS_PER_NODE_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_CA_CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    MAINTENANCE_POLICY_FIELD_NUMBER: _ClassVar[int]
    CONTROL_PLANE_VERSION_FIELD_NUMBER: _ClassVar[int]
    NODE_VERSION_FIELD_NUMBER: _ClassVar[int]
    CONTROL_PLANE_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_ADDONS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_LOAD_BALANCER_IPV4_ADDRESS_POOLS_FIELD_NUMBER: _ClassVar[int]
    CONTROL_PLANE_ENCRYPTION_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MAINTENANCE_EVENTS_FIELD_NUMBER: _ClassVar[int]
    TARGET_VERSION_FIELD_NUMBER: _ClassVar[int]
    RELEASE_CHANNEL_FIELD_NUMBER: _ClassVar[int]
    SURVIVABILITY_CONFIG_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_LOAD_BALANCER_IPV6_ADDRESS_POOLS_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_STATE_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    fleet: Fleet
    networking: ClusterNetworking
    authorization: Authorization
    default_max_pods_per_node: int
    endpoint: str
    port: int
    cluster_ca_certificate: str
    maintenance_policy: MaintenancePolicy
    control_plane_version: str
    node_version: str
    control_plane: Cluster.ControlPlane
    system_addons_config: Cluster.SystemAddonsConfig
    external_load_balancer_ipv4_address_pools: _containers.RepeatedScalarFieldContainer[str]
    control_plane_encryption: Cluster.ControlPlaneEncryption
    status: Cluster.Status
    maintenance_events: _containers.RepeatedCompositeFieldContainer[Cluster.MaintenanceEvent]
    target_version: str
    release_channel: Cluster.ReleaseChannel
    survivability_config: Cluster.SurvivabilityConfig
    external_load_balancer_ipv6_address_pools: _containers.RepeatedScalarFieldContainer[str]
    connection_state: Cluster.ConnectionState

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., fleet: _Optional[_Union[Fleet, _Mapping]]=..., networking: _Optional[_Union[ClusterNetworking, _Mapping]]=..., authorization: _Optional[_Union[Authorization, _Mapping]]=..., default_max_pods_per_node: _Optional[int]=..., endpoint: _Optional[str]=..., port: _Optional[int]=..., cluster_ca_certificate: _Optional[str]=..., maintenance_policy: _Optional[_Union[MaintenancePolicy, _Mapping]]=..., control_plane_version: _Optional[str]=..., node_version: _Optional[str]=..., control_plane: _Optional[_Union[Cluster.ControlPlane, _Mapping]]=..., system_addons_config: _Optional[_Union[Cluster.SystemAddonsConfig, _Mapping]]=..., external_load_balancer_ipv4_address_pools: _Optional[_Iterable[str]]=..., control_plane_encryption: _Optional[_Union[Cluster.ControlPlaneEncryption, _Mapping]]=..., status: _Optional[_Union[Cluster.Status, str]]=..., maintenance_events: _Optional[_Iterable[_Union[Cluster.MaintenanceEvent, _Mapping]]]=..., target_version: _Optional[str]=..., release_channel: _Optional[_Union[Cluster.ReleaseChannel, str]]=..., survivability_config: _Optional[_Union[Cluster.SurvivabilityConfig, _Mapping]]=..., external_load_balancer_ipv6_address_pools: _Optional[_Iterable[str]]=..., connection_state: _Optional[_Union[Cluster.ConnectionState, _Mapping]]=...) -> None:
        ...

class ClusterNetworking(_message.Message):
    __slots__ = ('cluster_ipv4_cidr_blocks', 'services_ipv4_cidr_blocks')
    CLUSTER_IPV4_CIDR_BLOCKS_FIELD_NUMBER: _ClassVar[int]
    SERVICES_IPV4_CIDR_BLOCKS_FIELD_NUMBER: _ClassVar[int]
    cluster_ipv4_cidr_blocks: _containers.RepeatedScalarFieldContainer[str]
    services_ipv4_cidr_blocks: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, cluster_ipv4_cidr_blocks: _Optional[_Iterable[str]]=..., services_ipv4_cidr_blocks: _Optional[_Iterable[str]]=...) -> None:
        ...

class Fleet(_message.Message):
    __slots__ = ('project', 'membership')
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    MEMBERSHIP_FIELD_NUMBER: _ClassVar[int]
    project: str
    membership: str

    def __init__(self, project: _Optional[str]=..., membership: _Optional[str]=...) -> None:
        ...

class ClusterUser(_message.Message):
    __slots__ = ('username',)
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    username: str

    def __init__(self, username: _Optional[str]=...) -> None:
        ...

class Authorization(_message.Message):
    __slots__ = ('admin_users',)
    ADMIN_USERS_FIELD_NUMBER: _ClassVar[int]
    admin_users: ClusterUser

    def __init__(self, admin_users: _Optional[_Union[ClusterUser, _Mapping]]=...) -> None:
        ...

class NodePool(_message.Message):
    __slots__ = ('name', 'create_time', 'update_time', 'labels', 'node_location', 'node_count', 'machine_filter', 'local_disk_encryption', 'node_version', 'node_config')

    class LocalDiskEncryption(_message.Message):
        __slots__ = ('kms_key', 'kms_key_active_version', 'kms_key_state', 'kms_status', 'resource_state')
        KMS_KEY_FIELD_NUMBER: _ClassVar[int]
        KMS_KEY_ACTIVE_VERSION_FIELD_NUMBER: _ClassVar[int]
        KMS_KEY_STATE_FIELD_NUMBER: _ClassVar[int]
        KMS_STATUS_FIELD_NUMBER: _ClassVar[int]
        RESOURCE_STATE_FIELD_NUMBER: _ClassVar[int]
        kms_key: str
        kms_key_active_version: str
        kms_key_state: KmsKeyState
        kms_status: _status_pb2.Status
        resource_state: ResourceState

        def __init__(self, kms_key: _Optional[str]=..., kms_key_active_version: _Optional[str]=..., kms_key_state: _Optional[_Union[KmsKeyState, str]]=..., kms_status: _Optional[_Union[_status_pb2.Status, _Mapping]]=..., resource_state: _Optional[_Union[ResourceState, str]]=...) -> None:
            ...

    class NodeConfig(_message.Message):
        __slots__ = ('labels', 'node_storage_schema')

        class LabelsEntry(_message.Message):
            __slots__ = ('key', 'value')
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str

            def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
                ...
        LABELS_FIELD_NUMBER: _ClassVar[int]
        NODE_STORAGE_SCHEMA_FIELD_NUMBER: _ClassVar[int]
        labels: _containers.ScalarMap[str, str]
        node_storage_schema: str

        def __init__(self, labels: _Optional[_Mapping[str, str]]=..., node_storage_schema: _Optional[str]=...) -> None:
            ...

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    NODE_LOCATION_FIELD_NUMBER: _ClassVar[int]
    NODE_COUNT_FIELD_NUMBER: _ClassVar[int]
    MACHINE_FILTER_FIELD_NUMBER: _ClassVar[int]
    LOCAL_DISK_ENCRYPTION_FIELD_NUMBER: _ClassVar[int]
    NODE_VERSION_FIELD_NUMBER: _ClassVar[int]
    NODE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    node_location: str
    node_count: int
    machine_filter: str
    local_disk_encryption: NodePool.LocalDiskEncryption
    node_version: str
    node_config: NodePool.NodeConfig

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., node_location: _Optional[str]=..., node_count: _Optional[int]=..., machine_filter: _Optional[str]=..., local_disk_encryption: _Optional[_Union[NodePool.LocalDiskEncryption, _Mapping]]=..., node_version: _Optional[str]=..., node_config: _Optional[_Union[NodePool.NodeConfig, _Mapping]]=...) -> None:
        ...

class Machine(_message.Message):
    __slots__ = ('name', 'create_time', 'update_time', 'labels', 'hosted_node', 'zone', 'version', 'disabled')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    HOSTED_NODE_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    DISABLED_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    hosted_node: str
    zone: str
    version: str
    disabled: bool

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., hosted_node: _Optional[str]=..., zone: _Optional[str]=..., version: _Optional[str]=..., disabled: bool=...) -> None:
        ...

class VpnConnection(_message.Message):
    __slots__ = ('name', 'create_time', 'update_time', 'labels', 'nat_gateway_ip', 'bgp_routing_mode', 'cluster', 'vpc', 'vpc_project', 'enable_high_availability', 'router', 'details')

    class BgpRoutingMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        BGP_ROUTING_MODE_UNSPECIFIED: _ClassVar[VpnConnection.BgpRoutingMode]
        REGIONAL: _ClassVar[VpnConnection.BgpRoutingMode]
        GLOBAL: _ClassVar[VpnConnection.BgpRoutingMode]
    BGP_ROUTING_MODE_UNSPECIFIED: VpnConnection.BgpRoutingMode
    REGIONAL: VpnConnection.BgpRoutingMode
    GLOBAL: VpnConnection.BgpRoutingMode

    class VpcProject(_message.Message):
        __slots__ = ('project_id', 'service_account')
        PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
        SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
        project_id: str
        service_account: str

        def __init__(self, project_id: _Optional[str]=..., service_account: _Optional[str]=...) -> None:
            ...

    class Details(_message.Message):
        __slots__ = ('state', 'error', 'cloud_router', 'cloud_vpns')

        class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            STATE_UNSPECIFIED: _ClassVar[VpnConnection.Details.State]
            STATE_CONNECTED: _ClassVar[VpnConnection.Details.State]
            STATE_CONNECTING: _ClassVar[VpnConnection.Details.State]
            STATE_ERROR: _ClassVar[VpnConnection.Details.State]
        STATE_UNSPECIFIED: VpnConnection.Details.State
        STATE_CONNECTED: VpnConnection.Details.State
        STATE_CONNECTING: VpnConnection.Details.State
        STATE_ERROR: VpnConnection.Details.State

        class CloudRouter(_message.Message):
            __slots__ = ('name',)
            NAME_FIELD_NUMBER: _ClassVar[int]
            name: str

            def __init__(self, name: _Optional[str]=...) -> None:
                ...

        class CloudVpn(_message.Message):
            __slots__ = ('gateway',)
            GATEWAY_FIELD_NUMBER: _ClassVar[int]
            gateway: str

            def __init__(self, gateway: _Optional[str]=...) -> None:
                ...
        STATE_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        CLOUD_ROUTER_FIELD_NUMBER: _ClassVar[int]
        CLOUD_VPNS_FIELD_NUMBER: _ClassVar[int]
        state: VpnConnection.Details.State
        error: str
        cloud_router: VpnConnection.Details.CloudRouter
        cloud_vpns: _containers.RepeatedCompositeFieldContainer[VpnConnection.Details.CloudVpn]

        def __init__(self, state: _Optional[_Union[VpnConnection.Details.State, str]]=..., error: _Optional[str]=..., cloud_router: _Optional[_Union[VpnConnection.Details.CloudRouter, _Mapping]]=..., cloud_vpns: _Optional[_Iterable[_Union[VpnConnection.Details.CloudVpn, _Mapping]]]=...) -> None:
            ...

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    NAT_GATEWAY_IP_FIELD_NUMBER: _ClassVar[int]
    BGP_ROUTING_MODE_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_FIELD_NUMBER: _ClassVar[int]
    VPC_FIELD_NUMBER: _ClassVar[int]
    VPC_PROJECT_FIELD_NUMBER: _ClassVar[int]
    ENABLE_HIGH_AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    ROUTER_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    nat_gateway_ip: str
    bgp_routing_mode: VpnConnection.BgpRoutingMode
    cluster: str
    vpc: str
    vpc_project: VpnConnection.VpcProject
    enable_high_availability: bool
    router: str
    details: VpnConnection.Details

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., nat_gateway_ip: _Optional[str]=..., bgp_routing_mode: _Optional[_Union[VpnConnection.BgpRoutingMode, str]]=..., cluster: _Optional[str]=..., vpc: _Optional[str]=..., vpc_project: _Optional[_Union[VpnConnection.VpcProject, _Mapping]]=..., enable_high_availability: bool=..., router: _Optional[str]=..., details: _Optional[_Union[VpnConnection.Details, _Mapping]]=...) -> None:
        ...

class LocationMetadata(_message.Message):
    __slots__ = ('available_zones',)

    class AvailableZonesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ZoneMetadata

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[ZoneMetadata, _Mapping]]=...) -> None:
            ...
    AVAILABLE_ZONES_FIELD_NUMBER: _ClassVar[int]
    available_zones: _containers.MessageMap[str, ZoneMetadata]

    def __init__(self, available_zones: _Optional[_Mapping[str, ZoneMetadata]]=...) -> None:
        ...

class ZoneMetadata(_message.Message):
    __slots__ = ('quota', 'rack_types', 'config_data')

    class RackType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RACK_TYPE_UNSPECIFIED: _ClassVar[ZoneMetadata.RackType]
        BASE: _ClassVar[ZoneMetadata.RackType]
        EXPANSION: _ClassVar[ZoneMetadata.RackType]
    RACK_TYPE_UNSPECIFIED: ZoneMetadata.RackType
    BASE: ZoneMetadata.RackType
    EXPANSION: ZoneMetadata.RackType

    class RackTypesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ZoneMetadata.RackType

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[ZoneMetadata.RackType, str]]=...) -> None:
            ...
    QUOTA_FIELD_NUMBER: _ClassVar[int]
    RACK_TYPES_FIELD_NUMBER: _ClassVar[int]
    CONFIG_DATA_FIELD_NUMBER: _ClassVar[int]
    quota: _containers.RepeatedCompositeFieldContainer[Quota]
    rack_types: _containers.ScalarMap[str, ZoneMetadata.RackType]
    config_data: ConfigData

    def __init__(self, quota: _Optional[_Iterable[_Union[Quota, _Mapping]]]=..., rack_types: _Optional[_Mapping[str, ZoneMetadata.RackType]]=..., config_data: _Optional[_Union[ConfigData, _Mapping]]=...) -> None:
        ...

class ConfigData(_message.Message):
    __slots__ = ('available_external_lb_pools_ipv4', 'available_external_lb_pools_ipv6')
    AVAILABLE_EXTERNAL_LB_POOLS_IPV4_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_EXTERNAL_LB_POOLS_IPV6_FIELD_NUMBER: _ClassVar[int]
    available_external_lb_pools_ipv4: _containers.RepeatedScalarFieldContainer[str]
    available_external_lb_pools_ipv6: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, available_external_lb_pools_ipv4: _Optional[_Iterable[str]]=..., available_external_lb_pools_ipv6: _Optional[_Iterable[str]]=...) -> None:
        ...

class Quota(_message.Message):
    __slots__ = ('metric', 'limit', 'usage')
    METRIC_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    USAGE_FIELD_NUMBER: _ClassVar[int]
    metric: str
    limit: float
    usage: float

    def __init__(self, metric: _Optional[str]=..., limit: _Optional[float]=..., usage: _Optional[float]=...) -> None:
        ...

class MaintenancePolicy(_message.Message):
    __slots__ = ('window', 'maintenance_exclusions')
    WINDOW_FIELD_NUMBER: _ClassVar[int]
    MAINTENANCE_EXCLUSIONS_FIELD_NUMBER: _ClassVar[int]
    window: MaintenanceWindow
    maintenance_exclusions: _containers.RepeatedCompositeFieldContainer[MaintenanceExclusionWindow]

    def __init__(self, window: _Optional[_Union[MaintenanceWindow, _Mapping]]=..., maintenance_exclusions: _Optional[_Iterable[_Union[MaintenanceExclusionWindow, _Mapping]]]=...) -> None:
        ...

class MaintenanceWindow(_message.Message):
    __slots__ = ('recurring_window',)
    RECURRING_WINDOW_FIELD_NUMBER: _ClassVar[int]
    recurring_window: RecurringTimeWindow

    def __init__(self, recurring_window: _Optional[_Union[RecurringTimeWindow, _Mapping]]=...) -> None:
        ...

class RecurringTimeWindow(_message.Message):
    __slots__ = ('window', 'recurrence')
    WINDOW_FIELD_NUMBER: _ClassVar[int]
    RECURRENCE_FIELD_NUMBER: _ClassVar[int]
    window: TimeWindow
    recurrence: str

    def __init__(self, window: _Optional[_Union[TimeWindow, _Mapping]]=..., recurrence: _Optional[str]=...) -> None:
        ...

class MaintenanceExclusionWindow(_message.Message):
    __slots__ = ('window', 'id')
    WINDOW_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    window: TimeWindow
    id: str

    def __init__(self, window: _Optional[_Union[TimeWindow, _Mapping]]=..., id: _Optional[str]=...) -> None:
        ...

class TimeWindow(_message.Message):
    __slots__ = ('start_time', 'end_time')
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp

    def __init__(self, start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class ServerConfig(_message.Message):
    __slots__ = ('channels', 'versions', 'default_version')

    class ChannelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ChannelConfig

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[ChannelConfig, _Mapping]]=...) -> None:
            ...
    CHANNELS_FIELD_NUMBER: _ClassVar[int]
    VERSIONS_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_VERSION_FIELD_NUMBER: _ClassVar[int]
    channels: _containers.MessageMap[str, ChannelConfig]
    versions: _containers.RepeatedCompositeFieldContainer[Version]
    default_version: str

    def __init__(self, channels: _Optional[_Mapping[str, ChannelConfig]]=..., versions: _Optional[_Iterable[_Union[Version, _Mapping]]]=..., default_version: _Optional[str]=...) -> None:
        ...

class ChannelConfig(_message.Message):
    __slots__ = ('default_version',)
    DEFAULT_VERSION_FIELD_NUMBER: _ClassVar[int]
    default_version: str

    def __init__(self, default_version: _Optional[str]=...) -> None:
        ...

class Version(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...