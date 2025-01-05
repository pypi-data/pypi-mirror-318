from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Membership(_message.Message):
    __slots__ = ('name', 'labels', 'description', 'endpoint', 'state', 'authority', 'create_time', 'update_time', 'delete_time', 'external_id', 'last_connection_time', 'unique_id', 'infrastructure_type', 'monitoring_config')

    class InfrastructureType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        INFRASTRUCTURE_TYPE_UNSPECIFIED: _ClassVar[Membership.InfrastructureType]
        ON_PREM: _ClassVar[Membership.InfrastructureType]
        MULTI_CLOUD: _ClassVar[Membership.InfrastructureType]
    INFRASTRUCTURE_TYPE_UNSPECIFIED: Membership.InfrastructureType
    ON_PREM: Membership.InfrastructureType
    MULTI_CLOUD: Membership.InfrastructureType

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    AUTHORITY_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DELETE_TIME_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ID_FIELD_NUMBER: _ClassVar[int]
    LAST_CONNECTION_TIME_FIELD_NUMBER: _ClassVar[int]
    UNIQUE_ID_FIELD_NUMBER: _ClassVar[int]
    INFRASTRUCTURE_TYPE_FIELD_NUMBER: _ClassVar[int]
    MONITORING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    name: str
    labels: _containers.ScalarMap[str, str]
    description: str
    endpoint: MembershipEndpoint
    state: MembershipState
    authority: Authority
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    delete_time: _timestamp_pb2.Timestamp
    external_id: str
    last_connection_time: _timestamp_pb2.Timestamp
    unique_id: str
    infrastructure_type: Membership.InfrastructureType
    monitoring_config: MonitoringConfig

    def __init__(self, name: _Optional[str]=..., labels: _Optional[_Mapping[str, str]]=..., description: _Optional[str]=..., endpoint: _Optional[_Union[MembershipEndpoint, _Mapping]]=..., state: _Optional[_Union[MembershipState, _Mapping]]=..., authority: _Optional[_Union[Authority, _Mapping]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., delete_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., external_id: _Optional[str]=..., last_connection_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., unique_id: _Optional[str]=..., infrastructure_type: _Optional[_Union[Membership.InfrastructureType, str]]=..., monitoring_config: _Optional[_Union[MonitoringConfig, _Mapping]]=...) -> None:
        ...

class MembershipEndpoint(_message.Message):
    __slots__ = ('gke_cluster', 'on_prem_cluster', 'multi_cloud_cluster', 'edge_cluster', 'appliance_cluster', 'kubernetes_metadata', 'kubernetes_resource')
    GKE_CLUSTER_FIELD_NUMBER: _ClassVar[int]
    ON_PREM_CLUSTER_FIELD_NUMBER: _ClassVar[int]
    MULTI_CLOUD_CLUSTER_FIELD_NUMBER: _ClassVar[int]
    EDGE_CLUSTER_FIELD_NUMBER: _ClassVar[int]
    APPLIANCE_CLUSTER_FIELD_NUMBER: _ClassVar[int]
    KUBERNETES_METADATA_FIELD_NUMBER: _ClassVar[int]
    KUBERNETES_RESOURCE_FIELD_NUMBER: _ClassVar[int]
    gke_cluster: GkeCluster
    on_prem_cluster: OnPremCluster
    multi_cloud_cluster: MultiCloudCluster
    edge_cluster: EdgeCluster
    appliance_cluster: ApplianceCluster
    kubernetes_metadata: KubernetesMetadata
    kubernetes_resource: KubernetesResource

    def __init__(self, gke_cluster: _Optional[_Union[GkeCluster, _Mapping]]=..., on_prem_cluster: _Optional[_Union[OnPremCluster, _Mapping]]=..., multi_cloud_cluster: _Optional[_Union[MultiCloudCluster, _Mapping]]=..., edge_cluster: _Optional[_Union[EdgeCluster, _Mapping]]=..., appliance_cluster: _Optional[_Union[ApplianceCluster, _Mapping]]=..., kubernetes_metadata: _Optional[_Union[KubernetesMetadata, _Mapping]]=..., kubernetes_resource: _Optional[_Union[KubernetesResource, _Mapping]]=...) -> None:
        ...

class KubernetesResource(_message.Message):
    __slots__ = ('membership_cr_manifest', 'membership_resources', 'connect_resources', 'resource_options')
    MEMBERSHIP_CR_MANIFEST_FIELD_NUMBER: _ClassVar[int]
    MEMBERSHIP_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    CONNECT_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    membership_cr_manifest: str
    membership_resources: _containers.RepeatedCompositeFieldContainer[ResourceManifest]
    connect_resources: _containers.RepeatedCompositeFieldContainer[ResourceManifest]
    resource_options: ResourceOptions

    def __init__(self, membership_cr_manifest: _Optional[str]=..., membership_resources: _Optional[_Iterable[_Union[ResourceManifest, _Mapping]]]=..., connect_resources: _Optional[_Iterable[_Union[ResourceManifest, _Mapping]]]=..., resource_options: _Optional[_Union[ResourceOptions, _Mapping]]=...) -> None:
        ...

class ResourceOptions(_message.Message):
    __slots__ = ('connect_version', 'v1beta1_crd', 'k8s_version')
    CONNECT_VERSION_FIELD_NUMBER: _ClassVar[int]
    V1BETA1_CRD_FIELD_NUMBER: _ClassVar[int]
    K8S_VERSION_FIELD_NUMBER: _ClassVar[int]
    connect_version: str
    v1beta1_crd: bool
    k8s_version: str

    def __init__(self, connect_version: _Optional[str]=..., v1beta1_crd: bool=..., k8s_version: _Optional[str]=...) -> None:
        ...

class ResourceManifest(_message.Message):
    __slots__ = ('manifest', 'cluster_scoped')
    MANIFEST_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_SCOPED_FIELD_NUMBER: _ClassVar[int]
    manifest: str
    cluster_scoped: bool

    def __init__(self, manifest: _Optional[str]=..., cluster_scoped: bool=...) -> None:
        ...

class GkeCluster(_message.Message):
    __slots__ = ('resource_link', 'cluster_missing')
    RESOURCE_LINK_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_MISSING_FIELD_NUMBER: _ClassVar[int]
    resource_link: str
    cluster_missing: bool

    def __init__(self, resource_link: _Optional[str]=..., cluster_missing: bool=...) -> None:
        ...

class OnPremCluster(_message.Message):
    __slots__ = ('resource_link', 'cluster_missing', 'admin_cluster', 'cluster_type')

    class ClusterType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CLUSTERTYPE_UNSPECIFIED: _ClassVar[OnPremCluster.ClusterType]
        BOOTSTRAP: _ClassVar[OnPremCluster.ClusterType]
        HYBRID: _ClassVar[OnPremCluster.ClusterType]
        STANDALONE: _ClassVar[OnPremCluster.ClusterType]
        USER: _ClassVar[OnPremCluster.ClusterType]
    CLUSTERTYPE_UNSPECIFIED: OnPremCluster.ClusterType
    BOOTSTRAP: OnPremCluster.ClusterType
    HYBRID: OnPremCluster.ClusterType
    STANDALONE: OnPremCluster.ClusterType
    USER: OnPremCluster.ClusterType
    RESOURCE_LINK_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_MISSING_FIELD_NUMBER: _ClassVar[int]
    ADMIN_CLUSTER_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_TYPE_FIELD_NUMBER: _ClassVar[int]
    resource_link: str
    cluster_missing: bool
    admin_cluster: bool
    cluster_type: OnPremCluster.ClusterType

    def __init__(self, resource_link: _Optional[str]=..., cluster_missing: bool=..., admin_cluster: bool=..., cluster_type: _Optional[_Union[OnPremCluster.ClusterType, str]]=...) -> None:
        ...

class MultiCloudCluster(_message.Message):
    __slots__ = ('resource_link', 'cluster_missing')
    RESOURCE_LINK_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_MISSING_FIELD_NUMBER: _ClassVar[int]
    resource_link: str
    cluster_missing: bool

    def __init__(self, resource_link: _Optional[str]=..., cluster_missing: bool=...) -> None:
        ...

class EdgeCluster(_message.Message):
    __slots__ = ('resource_link',)
    RESOURCE_LINK_FIELD_NUMBER: _ClassVar[int]
    resource_link: str

    def __init__(self, resource_link: _Optional[str]=...) -> None:
        ...

class ApplianceCluster(_message.Message):
    __slots__ = ('resource_link',)
    RESOURCE_LINK_FIELD_NUMBER: _ClassVar[int]
    resource_link: str

    def __init__(self, resource_link: _Optional[str]=...) -> None:
        ...

class KubernetesMetadata(_message.Message):
    __slots__ = ('kubernetes_api_server_version', 'node_provider_id', 'node_count', 'vcpu_count', 'memory_mb', 'update_time')
    KUBERNETES_API_SERVER_VERSION_FIELD_NUMBER: _ClassVar[int]
    NODE_PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_COUNT_FIELD_NUMBER: _ClassVar[int]
    VCPU_COUNT_FIELD_NUMBER: _ClassVar[int]
    MEMORY_MB_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    kubernetes_api_server_version: str
    node_provider_id: str
    node_count: int
    vcpu_count: int
    memory_mb: int
    update_time: _timestamp_pb2.Timestamp

    def __init__(self, kubernetes_api_server_version: _Optional[str]=..., node_provider_id: _Optional[str]=..., node_count: _Optional[int]=..., vcpu_count: _Optional[int]=..., memory_mb: _Optional[int]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class Authority(_message.Message):
    __slots__ = ('issuer', 'workload_identity_pool', 'identity_provider', 'oidc_jwks')
    ISSUER_FIELD_NUMBER: _ClassVar[int]
    WORKLOAD_IDENTITY_POOL_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_PROVIDER_FIELD_NUMBER: _ClassVar[int]
    OIDC_JWKS_FIELD_NUMBER: _ClassVar[int]
    issuer: str
    workload_identity_pool: str
    identity_provider: str
    oidc_jwks: bytes

    def __init__(self, issuer: _Optional[str]=..., workload_identity_pool: _Optional[str]=..., identity_provider: _Optional[str]=..., oidc_jwks: _Optional[bytes]=...) -> None:
        ...

class MonitoringConfig(_message.Message):
    __slots__ = ('project_id', 'location', 'cluster', 'kubernetes_metrics_prefix', 'cluster_hash')
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_FIELD_NUMBER: _ClassVar[int]
    KUBERNETES_METRICS_PREFIX_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_HASH_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    location: str
    cluster: str
    kubernetes_metrics_prefix: str
    cluster_hash: str

    def __init__(self, project_id: _Optional[str]=..., location: _Optional[str]=..., cluster: _Optional[str]=..., kubernetes_metrics_prefix: _Optional[str]=..., cluster_hash: _Optional[str]=...) -> None:
        ...

class MembershipState(_message.Message):
    __slots__ = ('code', 'description', 'update_time')

    class Code(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CODE_UNSPECIFIED: _ClassVar[MembershipState.Code]
        CREATING: _ClassVar[MembershipState.Code]
        READY: _ClassVar[MembershipState.Code]
        DELETING: _ClassVar[MembershipState.Code]
        UPDATING: _ClassVar[MembershipState.Code]
        SERVICE_UPDATING: _ClassVar[MembershipState.Code]
    CODE_UNSPECIFIED: MembershipState.Code
    CREATING: MembershipState.Code
    READY: MembershipState.Code
    DELETING: MembershipState.Code
    UPDATING: MembershipState.Code
    SERVICE_UPDATING: MembershipState.Code
    CODE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    code: MembershipState.Code
    description: str
    update_time: _timestamp_pb2.Timestamp

    def __init__(self, code: _Optional[_Union[MembershipState.Code, str]]=..., description: _Optional[str]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class ListMembershipsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'order_by')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=...) -> None:
        ...

class ListMembershipsResponse(_message.Message):
    __slots__ = ('resources', 'next_page_token', 'unreachable')
    RESOURCES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    resources: _containers.RepeatedCompositeFieldContainer[Membership]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, resources: _Optional[_Iterable[_Union[Membership, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetMembershipRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateMembershipRequest(_message.Message):
    __slots__ = ('parent', 'membership_id', 'resource', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    MEMBERSHIP_ID_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    membership_id: str
    resource: Membership
    request_id: str

    def __init__(self, parent: _Optional[str]=..., membership_id: _Optional[str]=..., resource: _Optional[_Union[Membership, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class DeleteMembershipRequest(_message.Message):
    __slots__ = ('name', 'request_id', 'force')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str
    force: bool

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=..., force: bool=...) -> None:
        ...

class UpdateMembershipRequest(_message.Message):
    __slots__ = ('name', 'update_mask', 'resource', 'request_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    update_mask: _field_mask_pb2.FieldMask
    resource: Membership
    request_id: str

    def __init__(self, name: _Optional[str]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., resource: _Optional[_Union[Membership, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class GenerateConnectManifestRequest(_message.Message):
    __slots__ = ('name', 'connect_agent', 'version', 'is_upgrade', 'registry', 'image_pull_secret_content')
    NAME_FIELD_NUMBER: _ClassVar[int]
    CONNECT_AGENT_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    IS_UPGRADE_FIELD_NUMBER: _ClassVar[int]
    REGISTRY_FIELD_NUMBER: _ClassVar[int]
    IMAGE_PULL_SECRET_CONTENT_FIELD_NUMBER: _ClassVar[int]
    name: str
    connect_agent: ConnectAgent
    version: str
    is_upgrade: bool
    registry: str
    image_pull_secret_content: bytes

    def __init__(self, name: _Optional[str]=..., connect_agent: _Optional[_Union[ConnectAgent, _Mapping]]=..., version: _Optional[str]=..., is_upgrade: bool=..., registry: _Optional[str]=..., image_pull_secret_content: _Optional[bytes]=...) -> None:
        ...

class GenerateConnectManifestResponse(_message.Message):
    __slots__ = ('manifest',)
    MANIFEST_FIELD_NUMBER: _ClassVar[int]
    manifest: _containers.RepeatedCompositeFieldContainer[ConnectAgentResource]

    def __init__(self, manifest: _Optional[_Iterable[_Union[ConnectAgentResource, _Mapping]]]=...) -> None:
        ...

class ConnectAgentResource(_message.Message):
    __slots__ = ('type', 'manifest')
    TYPE_FIELD_NUMBER: _ClassVar[int]
    MANIFEST_FIELD_NUMBER: _ClassVar[int]
    type: TypeMeta
    manifest: str

    def __init__(self, type: _Optional[_Union[TypeMeta, _Mapping]]=..., manifest: _Optional[str]=...) -> None:
        ...

class TypeMeta(_message.Message):
    __slots__ = ('kind', 'api_version')
    KIND_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    kind: str
    api_version: str

    def __init__(self, kind: _Optional[str]=..., api_version: _Optional[str]=...) -> None:
        ...

class ConnectAgent(_message.Message):
    __slots__ = ('name', 'proxy', 'namespace')
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROXY_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    name: str
    proxy: bytes
    namespace: str

    def __init__(self, name: _Optional[str]=..., proxy: _Optional[bytes]=..., namespace: _Optional[str]=...) -> None:
        ...

class ValidateExclusivityRequest(_message.Message):
    __slots__ = ('parent', 'cr_manifest', 'intended_membership')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CR_MANIFEST_FIELD_NUMBER: _ClassVar[int]
    INTENDED_MEMBERSHIP_FIELD_NUMBER: _ClassVar[int]
    parent: str
    cr_manifest: str
    intended_membership: str

    def __init__(self, parent: _Optional[str]=..., cr_manifest: _Optional[str]=..., intended_membership: _Optional[str]=...) -> None:
        ...

class ValidateExclusivityResponse(_message.Message):
    __slots__ = ('status',)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: _status_pb2.Status

    def __init__(self, status: _Optional[_Union[_status_pb2.Status, _Mapping]]=...) -> None:
        ...

class GenerateExclusivityManifestRequest(_message.Message):
    __slots__ = ('name', 'crd_manifest', 'cr_manifest')
    NAME_FIELD_NUMBER: _ClassVar[int]
    CRD_MANIFEST_FIELD_NUMBER: _ClassVar[int]
    CR_MANIFEST_FIELD_NUMBER: _ClassVar[int]
    name: str
    crd_manifest: str
    cr_manifest: str

    def __init__(self, name: _Optional[str]=..., crd_manifest: _Optional[str]=..., cr_manifest: _Optional[str]=...) -> None:
        ...

class GenerateExclusivityManifestResponse(_message.Message):
    __slots__ = ('crd_manifest', 'cr_manifest')
    CRD_MANIFEST_FIELD_NUMBER: _ClassVar[int]
    CR_MANIFEST_FIELD_NUMBER: _ClassVar[int]
    crd_manifest: str
    cr_manifest: str

    def __init__(self, crd_manifest: _Optional[str]=..., cr_manifest: _Optional[str]=...) -> None:
        ...

class OperationMetadata(_message.Message):
    __slots__ = ('create_time', 'end_time', 'target', 'verb', 'status_detail', 'cancel_requested', 'api_version')
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    VERB_FIELD_NUMBER: _ClassVar[int]
    STATUS_DETAIL_FIELD_NUMBER: _ClassVar[int]
    CANCEL_REQUESTED_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    target: str
    verb: str
    status_detail: str
    cancel_requested: bool
    api_version: str

    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., target: _Optional[str]=..., verb: _Optional[str]=..., status_detail: _Optional[str]=..., cancel_requested: bool=..., api_version: _Optional[str]=...) -> None:
        ...