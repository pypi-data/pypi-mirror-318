from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Membership(_message.Message):
    __slots__ = ('endpoint', 'name', 'labels', 'description', 'state', 'create_time', 'update_time', 'delete_time', 'external_id', 'last_connection_time', 'unique_id', 'authority', 'monitoring_config')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DELETE_TIME_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ID_FIELD_NUMBER: _ClassVar[int]
    LAST_CONNECTION_TIME_FIELD_NUMBER: _ClassVar[int]
    UNIQUE_ID_FIELD_NUMBER: _ClassVar[int]
    AUTHORITY_FIELD_NUMBER: _ClassVar[int]
    MONITORING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    endpoint: MembershipEndpoint
    name: str
    labels: _containers.ScalarMap[str, str]
    description: str
    state: MembershipState
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    delete_time: _timestamp_pb2.Timestamp
    external_id: str
    last_connection_time: _timestamp_pb2.Timestamp
    unique_id: str
    authority: Authority
    monitoring_config: MonitoringConfig

    def __init__(self, endpoint: _Optional[_Union[MembershipEndpoint, _Mapping]]=..., name: _Optional[str]=..., labels: _Optional[_Mapping[str, str]]=..., description: _Optional[str]=..., state: _Optional[_Union[MembershipState, _Mapping]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., delete_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., external_id: _Optional[str]=..., last_connection_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., unique_id: _Optional[str]=..., authority: _Optional[_Union[Authority, _Mapping]]=..., monitoring_config: _Optional[_Union[MonitoringConfig, _Mapping]]=...) -> None:
        ...

class MembershipEndpoint(_message.Message):
    __slots__ = ('gke_cluster', 'kubernetes_metadata', 'kubernetes_resource', 'google_managed')
    GKE_CLUSTER_FIELD_NUMBER: _ClassVar[int]
    KUBERNETES_METADATA_FIELD_NUMBER: _ClassVar[int]
    KUBERNETES_RESOURCE_FIELD_NUMBER: _ClassVar[int]
    GOOGLE_MANAGED_FIELD_NUMBER: _ClassVar[int]
    gke_cluster: GkeCluster
    kubernetes_metadata: KubernetesMetadata
    kubernetes_resource: KubernetesResource
    google_managed: bool

    def __init__(self, gke_cluster: _Optional[_Union[GkeCluster, _Mapping]]=..., kubernetes_metadata: _Optional[_Union[KubernetesMetadata, _Mapping]]=..., kubernetes_resource: _Optional[_Union[KubernetesResource, _Mapping]]=..., google_managed: bool=...) -> None:
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
    __slots__ = ('code',)

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
    code: MembershipState.Code

    def __init__(self, code: _Optional[_Union[MembershipState.Code, str]]=...) -> None:
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