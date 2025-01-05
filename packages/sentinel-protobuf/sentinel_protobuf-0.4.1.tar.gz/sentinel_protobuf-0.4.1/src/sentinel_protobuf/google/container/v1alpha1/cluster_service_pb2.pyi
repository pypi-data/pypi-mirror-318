from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class NodeConfig(_message.Message):
    __slots__ = ('machine_type', 'disk_size_gb', 'oauth_scopes', 'service_account', 'metadata', 'image_type', 'labels', 'local_ssd_count', 'tags', 'preemptible', 'accelerators', 'min_cpu_platform', 'taints')

    class MetadataEntry(_message.Message):
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
    MIN_CPU_PLATFORM_FIELD_NUMBER: _ClassVar[int]
    TAINTS_FIELD_NUMBER: _ClassVar[int]
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
    min_cpu_platform: str
    taints: _containers.RepeatedCompositeFieldContainer[NodeTaint]

    def __init__(self, machine_type: _Optional[str]=..., disk_size_gb: _Optional[int]=..., oauth_scopes: _Optional[_Iterable[str]]=..., service_account: _Optional[str]=..., metadata: _Optional[_Mapping[str, str]]=..., image_type: _Optional[str]=..., labels: _Optional[_Mapping[str, str]]=..., local_ssd_count: _Optional[int]=..., tags: _Optional[_Iterable[str]]=..., preemptible: bool=..., accelerators: _Optional[_Iterable[_Union[AcceleratorConfig, _Mapping]]]=..., min_cpu_platform: _Optional[str]=..., taints: _Optional[_Iterable[_Union[NodeTaint, _Mapping]]]=...) -> None:
        ...

class NodeTaint(_message.Message):
    __slots__ = ('key', 'value', 'effect')

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

    def __init__(self, key: _Optional[str]=..., value: _Optional[str]=..., effect: _Optional[_Union[NodeTaint.Effect, str]]=...) -> None:
        ...

class MasterAuth(_message.Message):
    __slots__ = ('username', 'password', 'client_certificate_config', 'cluster_ca_certificate', 'client_certificate', 'client_key')
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

    def __init__(self, username: _Optional[str]=..., password: _Optional[str]=..., client_certificate_config: _Optional[_Union[ClientCertificateConfig, _Mapping]]=..., cluster_ca_certificate: _Optional[str]=..., client_certificate: _Optional[str]=..., client_key: _Optional[str]=...) -> None:
        ...

class ClientCertificateConfig(_message.Message):
    __slots__ = ('issue_client_certificate',)
    ISSUE_CLIENT_CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    issue_client_certificate: bool

    def __init__(self, issue_client_certificate: bool=...) -> None:
        ...

class AddonsConfig(_message.Message):
    __slots__ = ('http_load_balancing', 'horizontal_pod_autoscaling', 'kubernetes_dashboard', 'network_policy_config')
    HTTP_LOAD_BALANCING_FIELD_NUMBER: _ClassVar[int]
    HORIZONTAL_POD_AUTOSCALING_FIELD_NUMBER: _ClassVar[int]
    KUBERNETES_DASHBOARD_FIELD_NUMBER: _ClassVar[int]
    NETWORK_POLICY_CONFIG_FIELD_NUMBER: _ClassVar[int]
    http_load_balancing: HttpLoadBalancing
    horizontal_pod_autoscaling: HorizontalPodAutoscaling
    kubernetes_dashboard: KubernetesDashboard
    network_policy_config: NetworkPolicyConfig

    def __init__(self, http_load_balancing: _Optional[_Union[HttpLoadBalancing, _Mapping]]=..., horizontal_pod_autoscaling: _Optional[_Union[HorizontalPodAutoscaling, _Mapping]]=..., kubernetes_dashboard: _Optional[_Union[KubernetesDashboard, _Mapping]]=..., network_policy_config: _Optional[_Union[NetworkPolicyConfig, _Mapping]]=...) -> None:
        ...

class HttpLoadBalancing(_message.Message):
    __slots__ = ('disabled',)
    DISABLED_FIELD_NUMBER: _ClassVar[int]
    disabled: bool

    def __init__(self, disabled: bool=...) -> None:
        ...

class HorizontalPodAutoscaling(_message.Message):
    __slots__ = ('disabled',)
    DISABLED_FIELD_NUMBER: _ClassVar[int]
    disabled: bool

    def __init__(self, disabled: bool=...) -> None:
        ...

class KubernetesDashboard(_message.Message):
    __slots__ = ('disabled',)
    DISABLED_FIELD_NUMBER: _ClassVar[int]
    disabled: bool

    def __init__(self, disabled: bool=...) -> None:
        ...

class NetworkPolicyConfig(_message.Message):
    __slots__ = ('disabled',)
    DISABLED_FIELD_NUMBER: _ClassVar[int]
    disabled: bool

    def __init__(self, disabled: bool=...) -> None:
        ...

class MasterAuthorizedNetworksConfig(_message.Message):
    __slots__ = ('enabled', 'cidr_blocks')

    class CidrBlock(_message.Message):
        __slots__ = ('display_name', 'cidr_block')
        DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
        CIDR_BLOCK_FIELD_NUMBER: _ClassVar[int]
        display_name: str
        cidr_block: str

        def __init__(self, display_name: _Optional[str]=..., cidr_block: _Optional[str]=...) -> None:
            ...
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    CIDR_BLOCKS_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    cidr_blocks: _containers.RepeatedCompositeFieldContainer[MasterAuthorizedNetworksConfig.CidrBlock]

    def __init__(self, enabled: bool=..., cidr_blocks: _Optional[_Iterable[_Union[MasterAuthorizedNetworksConfig.CidrBlock, _Mapping]]]=...) -> None:
        ...

class NetworkPolicy(_message.Message):
    __slots__ = ('provider', 'enabled')

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

    def __init__(self, provider: _Optional[_Union[NetworkPolicy.Provider, str]]=..., enabled: bool=...) -> None:
        ...

class IPAllocationPolicy(_message.Message):
    __slots__ = ('use_ip_aliases', 'create_subnetwork', 'subnetwork_name', 'cluster_ipv4_cidr', 'node_ipv4_cidr', 'services_ipv4_cidr', 'cluster_secondary_range_name', 'services_secondary_range_name', 'cluster_ipv4_cidr_block', 'node_ipv4_cidr_block', 'services_ipv4_cidr_block')
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

    def __init__(self, use_ip_aliases: bool=..., create_subnetwork: bool=..., subnetwork_name: _Optional[str]=..., cluster_ipv4_cidr: _Optional[str]=..., node_ipv4_cidr: _Optional[str]=..., services_ipv4_cidr: _Optional[str]=..., cluster_secondary_range_name: _Optional[str]=..., services_secondary_range_name: _Optional[str]=..., cluster_ipv4_cidr_block: _Optional[str]=..., node_ipv4_cidr_block: _Optional[str]=..., services_ipv4_cidr_block: _Optional[str]=...) -> None:
        ...

class PodSecurityPolicyConfig(_message.Message):
    __slots__ = ('enabled',)
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    enabled: bool

    def __init__(self, enabled: bool=...) -> None:
        ...

class Cluster(_message.Message):
    __slots__ = ('name', 'description', 'initial_node_count', 'node_config', 'master_auth', 'logging_service', 'monitoring_service', 'network', 'cluster_ipv4_cidr', 'addons_config', 'subnetwork', 'node_pools', 'locations', 'enable_kubernetes_alpha', 'network_policy', 'ip_allocation_policy', 'master_authorized_networks_config', 'maintenance_policy', 'pod_security_policy_config', 'self_link', 'zone', 'endpoint', 'initial_cluster_version', 'current_master_version', 'current_node_version', 'create_time', 'status', 'status_message', 'node_ipv4_cidr_size', 'services_ipv4_cidr', 'instance_group_urls', 'current_node_count', 'expire_time', 'location')

    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATUS_UNSPECIFIED: _ClassVar[Cluster.Status]
        PROVISIONING: _ClassVar[Cluster.Status]
        RUNNING: _ClassVar[Cluster.Status]
        RECONCILING: _ClassVar[Cluster.Status]
        STOPPING: _ClassVar[Cluster.Status]
        ERROR: _ClassVar[Cluster.Status]
    STATUS_UNSPECIFIED: Cluster.Status
    PROVISIONING: Cluster.Status
    RUNNING: Cluster.Status
    RECONCILING: Cluster.Status
    STOPPING: Cluster.Status
    ERROR: Cluster.Status
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
    NETWORK_POLICY_FIELD_NUMBER: _ClassVar[int]
    IP_ALLOCATION_POLICY_FIELD_NUMBER: _ClassVar[int]
    MASTER_AUTHORIZED_NETWORKS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    MAINTENANCE_POLICY_FIELD_NUMBER: _ClassVar[int]
    POD_SECURITY_POLICY_CONFIG_FIELD_NUMBER: _ClassVar[int]
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
    network_policy: NetworkPolicy
    ip_allocation_policy: IPAllocationPolicy
    master_authorized_networks_config: MasterAuthorizedNetworksConfig
    maintenance_policy: MaintenancePolicy
    pod_security_policy_config: PodSecurityPolicyConfig
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

    def __init__(self, name: _Optional[str]=..., description: _Optional[str]=..., initial_node_count: _Optional[int]=..., node_config: _Optional[_Union[NodeConfig, _Mapping]]=..., master_auth: _Optional[_Union[MasterAuth, _Mapping]]=..., logging_service: _Optional[str]=..., monitoring_service: _Optional[str]=..., network: _Optional[str]=..., cluster_ipv4_cidr: _Optional[str]=..., addons_config: _Optional[_Union[AddonsConfig, _Mapping]]=..., subnetwork: _Optional[str]=..., node_pools: _Optional[_Iterable[_Union[NodePool, _Mapping]]]=..., locations: _Optional[_Iterable[str]]=..., enable_kubernetes_alpha: bool=..., network_policy: _Optional[_Union[NetworkPolicy, _Mapping]]=..., ip_allocation_policy: _Optional[_Union[IPAllocationPolicy, _Mapping]]=..., master_authorized_networks_config: _Optional[_Union[MasterAuthorizedNetworksConfig, _Mapping]]=..., maintenance_policy: _Optional[_Union[MaintenancePolicy, _Mapping]]=..., pod_security_policy_config: _Optional[_Union[PodSecurityPolicyConfig, _Mapping]]=..., self_link: _Optional[str]=..., zone: _Optional[str]=..., endpoint: _Optional[str]=..., initial_cluster_version: _Optional[str]=..., current_master_version: _Optional[str]=..., current_node_version: _Optional[str]=..., create_time: _Optional[str]=..., status: _Optional[_Union[Cluster.Status, str]]=..., status_message: _Optional[str]=..., node_ipv4_cidr_size: _Optional[int]=..., services_ipv4_cidr: _Optional[str]=..., instance_group_urls: _Optional[_Iterable[str]]=..., current_node_count: _Optional[int]=..., expire_time: _Optional[str]=..., location: _Optional[str]=...) -> None:
        ...

class ClusterUpdate(_message.Message):
    __slots__ = ('desired_node_version', 'desired_monitoring_service', 'desired_addons_config', 'desired_node_pool_id', 'desired_image_type', 'desired_node_pool_autoscaling', 'desired_locations', 'desired_master_authorized_networks_config', 'desired_pod_security_policy_config', 'desired_master_version')
    DESIRED_NODE_VERSION_FIELD_NUMBER: _ClassVar[int]
    DESIRED_MONITORING_SERVICE_FIELD_NUMBER: _ClassVar[int]
    DESIRED_ADDONS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DESIRED_NODE_POOL_ID_FIELD_NUMBER: _ClassVar[int]
    DESIRED_IMAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    DESIRED_NODE_POOL_AUTOSCALING_FIELD_NUMBER: _ClassVar[int]
    DESIRED_LOCATIONS_FIELD_NUMBER: _ClassVar[int]
    DESIRED_MASTER_AUTHORIZED_NETWORKS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DESIRED_POD_SECURITY_POLICY_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DESIRED_MASTER_VERSION_FIELD_NUMBER: _ClassVar[int]
    desired_node_version: str
    desired_monitoring_service: str
    desired_addons_config: AddonsConfig
    desired_node_pool_id: str
    desired_image_type: str
    desired_node_pool_autoscaling: NodePoolAutoscaling
    desired_locations: _containers.RepeatedScalarFieldContainer[str]
    desired_master_authorized_networks_config: MasterAuthorizedNetworksConfig
    desired_pod_security_policy_config: PodSecurityPolicyConfig
    desired_master_version: str

    def __init__(self, desired_node_version: _Optional[str]=..., desired_monitoring_service: _Optional[str]=..., desired_addons_config: _Optional[_Union[AddonsConfig, _Mapping]]=..., desired_node_pool_id: _Optional[str]=..., desired_image_type: _Optional[str]=..., desired_node_pool_autoscaling: _Optional[_Union[NodePoolAutoscaling, _Mapping]]=..., desired_locations: _Optional[_Iterable[str]]=..., desired_master_authorized_networks_config: _Optional[_Union[MasterAuthorizedNetworksConfig, _Mapping]]=..., desired_pod_security_policy_config: _Optional[_Union[PodSecurityPolicyConfig, _Mapping]]=..., desired_master_version: _Optional[str]=...) -> None:
        ...

class Operation(_message.Message):
    __slots__ = ('name', 'zone', 'operation_type', 'status', 'detail', 'status_message', 'self_link', 'target_link', 'location', 'start_time', 'end_time')

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

    def __init__(self, name: _Optional[str]=..., zone: _Optional[str]=..., operation_type: _Optional[_Union[Operation.Type, str]]=..., status: _Optional[_Union[Operation.Status, str]]=..., detail: _Optional[str]=..., status_message: _Optional[str]=..., self_link: _Optional[str]=..., target_link: _Optional[str]=..., location: _Optional[str]=..., start_time: _Optional[str]=..., end_time: _Optional[str]=...) -> None:
        ...

class CreateClusterRequest(_message.Message):
    __slots__ = ('project_id', 'zone', 'cluster', 'parent')
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    zone: str
    cluster: Cluster
    parent: str

    def __init__(self, project_id: _Optional[str]=..., zone: _Optional[str]=..., cluster: _Optional[_Union[Cluster, _Mapping]]=..., parent: _Optional[str]=...) -> None:
        ...

class GetClusterRequest(_message.Message):
    __slots__ = ('project_id', 'zone', 'cluster_id', 'name')
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    zone: str
    cluster_id: str
    name: str

    def __init__(self, project_id: _Optional[str]=..., zone: _Optional[str]=..., cluster_id: _Optional[str]=..., name: _Optional[str]=...) -> None:
        ...

class UpdateClusterRequest(_message.Message):
    __slots__ = ('project_id', 'zone', 'cluster_id', 'update', 'name')
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

    def __init__(self, project_id: _Optional[str]=..., zone: _Optional[str]=..., cluster_id: _Optional[str]=..., update: _Optional[_Union[ClusterUpdate, _Mapping]]=..., name: _Optional[str]=...) -> None:
        ...

class UpdateNodePoolRequest(_message.Message):
    __slots__ = ('project_id', 'zone', 'cluster_id', 'node_pool_id', 'node_version', 'image_type', 'name')
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_POOL_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_VERSION_FIELD_NUMBER: _ClassVar[int]
    IMAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    zone: str
    cluster_id: str
    node_pool_id: str
    node_version: str
    image_type: str
    name: str

    def __init__(self, project_id: _Optional[str]=..., zone: _Optional[str]=..., cluster_id: _Optional[str]=..., node_pool_id: _Optional[str]=..., node_version: _Optional[str]=..., image_type: _Optional[str]=..., name: _Optional[str]=...) -> None:
        ...

class SetNodePoolAutoscalingRequest(_message.Message):
    __slots__ = ('project_id', 'zone', 'cluster_id', 'node_pool_id', 'autoscaling', 'name')
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

    def __init__(self, project_id: _Optional[str]=..., zone: _Optional[str]=..., cluster_id: _Optional[str]=..., node_pool_id: _Optional[str]=..., autoscaling: _Optional[_Union[NodePoolAutoscaling, _Mapping]]=..., name: _Optional[str]=...) -> None:
        ...

class SetLoggingServiceRequest(_message.Message):
    __slots__ = ('project_id', 'zone', 'cluster_id', 'logging_service', 'name')
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

    def __init__(self, project_id: _Optional[str]=..., zone: _Optional[str]=..., cluster_id: _Optional[str]=..., logging_service: _Optional[str]=..., name: _Optional[str]=...) -> None:
        ...

class SetMonitoringServiceRequest(_message.Message):
    __slots__ = ('project_id', 'zone', 'cluster_id', 'monitoring_service', 'name')
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

    def __init__(self, project_id: _Optional[str]=..., zone: _Optional[str]=..., cluster_id: _Optional[str]=..., monitoring_service: _Optional[str]=..., name: _Optional[str]=...) -> None:
        ...

class SetAddonsConfigRequest(_message.Message):
    __slots__ = ('project_id', 'zone', 'cluster_id', 'addons_config', 'name')
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

    def __init__(self, project_id: _Optional[str]=..., zone: _Optional[str]=..., cluster_id: _Optional[str]=..., addons_config: _Optional[_Union[AddonsConfig, _Mapping]]=..., name: _Optional[str]=...) -> None:
        ...

class SetLocationsRequest(_message.Message):
    __slots__ = ('project_id', 'zone', 'cluster_id', 'locations', 'name')
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

    def __init__(self, project_id: _Optional[str]=..., zone: _Optional[str]=..., cluster_id: _Optional[str]=..., locations: _Optional[_Iterable[str]]=..., name: _Optional[str]=...) -> None:
        ...

class UpdateMasterRequest(_message.Message):
    __slots__ = ('project_id', 'zone', 'cluster_id', 'master_version', 'name')
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

    def __init__(self, project_id: _Optional[str]=..., zone: _Optional[str]=..., cluster_id: _Optional[str]=..., master_version: _Optional[str]=..., name: _Optional[str]=...) -> None:
        ...

class SetMasterAuthRequest(_message.Message):
    __slots__ = ('project_id', 'zone', 'cluster_id', 'action', 'update', 'name')

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

    def __init__(self, project_id: _Optional[str]=..., zone: _Optional[str]=..., cluster_id: _Optional[str]=..., action: _Optional[_Union[SetMasterAuthRequest.Action, str]]=..., update: _Optional[_Union[MasterAuth, _Mapping]]=..., name: _Optional[str]=...) -> None:
        ...

class DeleteClusterRequest(_message.Message):
    __slots__ = ('project_id', 'zone', 'cluster_id', 'name')
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    zone: str
    cluster_id: str
    name: str

    def __init__(self, project_id: _Optional[str]=..., zone: _Optional[str]=..., cluster_id: _Optional[str]=..., name: _Optional[str]=...) -> None:
        ...

class ListClustersRequest(_message.Message):
    __slots__ = ('project_id', 'zone', 'parent')
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    zone: str
    parent: str

    def __init__(self, project_id: _Optional[str]=..., zone: _Optional[str]=..., parent: _Optional[str]=...) -> None:
        ...

class ListClustersResponse(_message.Message):
    __slots__ = ('clusters', 'missing_zones')
    CLUSTERS_FIELD_NUMBER: _ClassVar[int]
    MISSING_ZONES_FIELD_NUMBER: _ClassVar[int]
    clusters: _containers.RepeatedCompositeFieldContainer[Cluster]
    missing_zones: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, clusters: _Optional[_Iterable[_Union[Cluster, _Mapping]]]=..., missing_zones: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetOperationRequest(_message.Message):
    __slots__ = ('project_id', 'zone', 'operation_id', 'name')
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    zone: str
    operation_id: str
    name: str

    def __init__(self, project_id: _Optional[str]=..., zone: _Optional[str]=..., operation_id: _Optional[str]=..., name: _Optional[str]=...) -> None:
        ...

class ListOperationsRequest(_message.Message):
    __slots__ = ('project_id', 'zone', 'parent')
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    zone: str
    parent: str

    def __init__(self, project_id: _Optional[str]=..., zone: _Optional[str]=..., parent: _Optional[str]=...) -> None:
        ...

class CancelOperationRequest(_message.Message):
    __slots__ = ('project_id', 'zone', 'operation_id', 'name')
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    zone: str
    operation_id: str
    name: str

    def __init__(self, project_id: _Optional[str]=..., zone: _Optional[str]=..., operation_id: _Optional[str]=..., name: _Optional[str]=...) -> None:
        ...

class ListOperationsResponse(_message.Message):
    __slots__ = ('operations', 'missing_zones')
    OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    MISSING_ZONES_FIELD_NUMBER: _ClassVar[int]
    operations: _containers.RepeatedCompositeFieldContainer[Operation]
    missing_zones: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, operations: _Optional[_Iterable[_Union[Operation, _Mapping]]]=..., missing_zones: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetServerConfigRequest(_message.Message):
    __slots__ = ('project_id', 'zone', 'name')
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    zone: str
    name: str

    def __init__(self, project_id: _Optional[str]=..., zone: _Optional[str]=..., name: _Optional[str]=...) -> None:
        ...

class ServerConfig(_message.Message):
    __slots__ = ('default_cluster_version', 'valid_node_versions', 'default_image_type', 'valid_image_types', 'valid_master_versions')
    DEFAULT_CLUSTER_VERSION_FIELD_NUMBER: _ClassVar[int]
    VALID_NODE_VERSIONS_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_IMAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    VALID_IMAGE_TYPES_FIELD_NUMBER: _ClassVar[int]
    VALID_MASTER_VERSIONS_FIELD_NUMBER: _ClassVar[int]
    default_cluster_version: str
    valid_node_versions: _containers.RepeatedScalarFieldContainer[str]
    default_image_type: str
    valid_image_types: _containers.RepeatedScalarFieldContainer[str]
    valid_master_versions: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, default_cluster_version: _Optional[str]=..., valid_node_versions: _Optional[_Iterable[str]]=..., default_image_type: _Optional[str]=..., valid_image_types: _Optional[_Iterable[str]]=..., valid_master_versions: _Optional[_Iterable[str]]=...) -> None:
        ...

class CreateNodePoolRequest(_message.Message):
    __slots__ = ('project_id', 'zone', 'cluster_id', 'node_pool', 'parent')
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

    def __init__(self, project_id: _Optional[str]=..., zone: _Optional[str]=..., cluster_id: _Optional[str]=..., node_pool: _Optional[_Union[NodePool, _Mapping]]=..., parent: _Optional[str]=...) -> None:
        ...

class DeleteNodePoolRequest(_message.Message):
    __slots__ = ('project_id', 'zone', 'cluster_id', 'node_pool_id', 'name')
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

    def __init__(self, project_id: _Optional[str]=..., zone: _Optional[str]=..., cluster_id: _Optional[str]=..., node_pool_id: _Optional[str]=..., name: _Optional[str]=...) -> None:
        ...

class ListNodePoolsRequest(_message.Message):
    __slots__ = ('project_id', 'zone', 'cluster_id', 'parent')
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    zone: str
    cluster_id: str
    parent: str

    def __init__(self, project_id: _Optional[str]=..., zone: _Optional[str]=..., cluster_id: _Optional[str]=..., parent: _Optional[str]=...) -> None:
        ...

class GetNodePoolRequest(_message.Message):
    __slots__ = ('project_id', 'zone', 'cluster_id', 'node_pool_id', 'name')
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

    def __init__(self, project_id: _Optional[str]=..., zone: _Optional[str]=..., cluster_id: _Optional[str]=..., node_pool_id: _Optional[str]=..., name: _Optional[str]=...) -> None:
        ...

class NodePool(_message.Message):
    __slots__ = ('name', 'config', 'initial_node_count', 'autoscaling', 'management', 'self_link', 'version', 'instance_group_urls', 'status', 'status_message')

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
    NAME_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    INITIAL_NODE_COUNT_FIELD_NUMBER: _ClassVar[int]
    AUTOSCALING_FIELD_NUMBER: _ClassVar[int]
    MANAGEMENT_FIELD_NUMBER: _ClassVar[int]
    SELF_LINK_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_GROUP_URLS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    STATUS_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    name: str
    config: NodeConfig
    initial_node_count: int
    autoscaling: NodePoolAutoscaling
    management: NodeManagement
    self_link: str
    version: str
    instance_group_urls: _containers.RepeatedScalarFieldContainer[str]
    status: NodePool.Status
    status_message: str

    def __init__(self, name: _Optional[str]=..., config: _Optional[_Union[NodeConfig, _Mapping]]=..., initial_node_count: _Optional[int]=..., autoscaling: _Optional[_Union[NodePoolAutoscaling, _Mapping]]=..., management: _Optional[_Union[NodeManagement, _Mapping]]=..., self_link: _Optional[str]=..., version: _Optional[str]=..., instance_group_urls: _Optional[_Iterable[str]]=..., status: _Optional[_Union[NodePool.Status, str]]=..., status_message: _Optional[str]=...) -> None:
        ...

class NodeManagement(_message.Message):
    __slots__ = ('auto_upgrade', 'auto_repair', 'upgrade_options')
    AUTO_UPGRADE_FIELD_NUMBER: _ClassVar[int]
    AUTO_REPAIR_FIELD_NUMBER: _ClassVar[int]
    UPGRADE_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    auto_upgrade: bool
    auto_repair: bool
    upgrade_options: AutoUpgradeOptions

    def __init__(self, auto_upgrade: bool=..., auto_repair: bool=..., upgrade_options: _Optional[_Union[AutoUpgradeOptions, _Mapping]]=...) -> None:
        ...

class AutoUpgradeOptions(_message.Message):
    __slots__ = ('auto_upgrade_start_time', 'description')
    AUTO_UPGRADE_START_TIME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    auto_upgrade_start_time: str
    description: str

    def __init__(self, auto_upgrade_start_time: _Optional[str]=..., description: _Optional[str]=...) -> None:
        ...

class MaintenancePolicy(_message.Message):
    __slots__ = ('window',)
    WINDOW_FIELD_NUMBER: _ClassVar[int]
    window: MaintenanceWindow

    def __init__(self, window: _Optional[_Union[MaintenanceWindow, _Mapping]]=...) -> None:
        ...

class MaintenanceWindow(_message.Message):
    __slots__ = ('daily_maintenance_window',)
    DAILY_MAINTENANCE_WINDOW_FIELD_NUMBER: _ClassVar[int]
    daily_maintenance_window: DailyMaintenanceWindow

    def __init__(self, daily_maintenance_window: _Optional[_Union[DailyMaintenanceWindow, _Mapping]]=...) -> None:
        ...

class DailyMaintenanceWindow(_message.Message):
    __slots__ = ('start_time', 'duration')
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    start_time: str
    duration: str

    def __init__(self, start_time: _Optional[str]=..., duration: _Optional[str]=...) -> None:
        ...

class SetNodePoolManagementRequest(_message.Message):
    __slots__ = ('project_id', 'zone', 'cluster_id', 'node_pool_id', 'management', 'name')
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

    def __init__(self, project_id: _Optional[str]=..., zone: _Optional[str]=..., cluster_id: _Optional[str]=..., node_pool_id: _Optional[str]=..., management: _Optional[_Union[NodeManagement, _Mapping]]=..., name: _Optional[str]=...) -> None:
        ...

class SetNodePoolSizeRequest(_message.Message):
    __slots__ = ('project_id', 'zone', 'cluster_id', 'node_pool_id', 'node_count', 'name')
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

    def __init__(self, project_id: _Optional[str]=..., zone: _Optional[str]=..., cluster_id: _Optional[str]=..., node_pool_id: _Optional[str]=..., node_count: _Optional[int]=..., name: _Optional[str]=...) -> None:
        ...

class RollbackNodePoolUpgradeRequest(_message.Message):
    __slots__ = ('project_id', 'zone', 'cluster_id', 'node_pool_id', 'name')
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

    def __init__(self, project_id: _Optional[str]=..., zone: _Optional[str]=..., cluster_id: _Optional[str]=..., node_pool_id: _Optional[str]=..., name: _Optional[str]=...) -> None:
        ...

class ListNodePoolsResponse(_message.Message):
    __slots__ = ('node_pools',)
    NODE_POOLS_FIELD_NUMBER: _ClassVar[int]
    node_pools: _containers.RepeatedCompositeFieldContainer[NodePool]

    def __init__(self, node_pools: _Optional[_Iterable[_Union[NodePool, _Mapping]]]=...) -> None:
        ...

class NodePoolAutoscaling(_message.Message):
    __slots__ = ('enabled', 'min_node_count', 'max_node_count')
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    MIN_NODE_COUNT_FIELD_NUMBER: _ClassVar[int]
    MAX_NODE_COUNT_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    min_node_count: int
    max_node_count: int

    def __init__(self, enabled: bool=..., min_node_count: _Optional[int]=..., max_node_count: _Optional[int]=...) -> None:
        ...

class SetLabelsRequest(_message.Message):
    __slots__ = ('project_id', 'zone', 'cluster_id', 'resource_labels', 'label_fingerprint', 'name')

    class ResourceLabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
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

    def __init__(self, project_id: _Optional[str]=..., zone: _Optional[str]=..., cluster_id: _Optional[str]=..., resource_labels: _Optional[_Mapping[str, str]]=..., label_fingerprint: _Optional[str]=..., name: _Optional[str]=...) -> None:
        ...

class SetLegacyAbacRequest(_message.Message):
    __slots__ = ('project_id', 'zone', 'cluster_id', 'enabled', 'name')
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

    def __init__(self, project_id: _Optional[str]=..., zone: _Optional[str]=..., cluster_id: _Optional[str]=..., enabled: bool=..., name: _Optional[str]=...) -> None:
        ...

class StartIPRotationRequest(_message.Message):
    __slots__ = ('project_id', 'zone', 'cluster_id', 'name')
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    zone: str
    cluster_id: str
    name: str

    def __init__(self, project_id: _Optional[str]=..., zone: _Optional[str]=..., cluster_id: _Optional[str]=..., name: _Optional[str]=...) -> None:
        ...

class CompleteIPRotationRequest(_message.Message):
    __slots__ = ('project_id', 'zone', 'cluster_id', 'name')
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    zone: str
    cluster_id: str
    name: str

    def __init__(self, project_id: _Optional[str]=..., zone: _Optional[str]=..., cluster_id: _Optional[str]=..., name: _Optional[str]=...) -> None:
        ...

class AcceleratorConfig(_message.Message):
    __slots__ = ('accelerator_count', 'accelerator_type')
    ACCELERATOR_COUNT_FIELD_NUMBER: _ClassVar[int]
    ACCELERATOR_TYPE_FIELD_NUMBER: _ClassVar[int]
    accelerator_count: int
    accelerator_type: str

    def __init__(self, accelerator_count: _Optional[int]=..., accelerator_type: _Optional[str]=...) -> None:
        ...

class SetNetworkPolicyRequest(_message.Message):
    __slots__ = ('project_id', 'zone', 'cluster_id', 'network_policy', 'name')
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

    def __init__(self, project_id: _Optional[str]=..., zone: _Optional[str]=..., cluster_id: _Optional[str]=..., network_policy: _Optional[_Union[NetworkPolicy, _Mapping]]=..., name: _Optional[str]=...) -> None:
        ...

class SetMaintenancePolicyRequest(_message.Message):
    __slots__ = ('project_id', 'zone', 'cluster_id', 'maintenance_policy', 'name')
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

    def __init__(self, project_id: _Optional[str]=..., zone: _Optional[str]=..., cluster_id: _Optional[str]=..., maintenance_policy: _Optional[_Union[MaintenancePolicy, _Mapping]]=..., name: _Optional[str]=...) -> None:
        ...