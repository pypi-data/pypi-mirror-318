from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.gkemulticloud.v1 import common_resources_pb2 as _common_resources_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AttachedCluster(_message.Message):
    __slots__ = ("name", "description", "oidc_config", "platform_version", "distribution", "cluster_region", "fleet", "state", "uid", "reconciling", "create_time", "update_time", "etag", "kubernetes_version", "annotations", "workload_identity_config", "logging_config", "errors", "authorization", "monitoring_config", "proxy_config", "binary_authorization", "security_posture_config", "tags")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[AttachedCluster.State]
        PROVISIONING: _ClassVar[AttachedCluster.State]
        RUNNING: _ClassVar[AttachedCluster.State]
        RECONCILING: _ClassVar[AttachedCluster.State]
        STOPPING: _ClassVar[AttachedCluster.State]
        ERROR: _ClassVar[AttachedCluster.State]
        DEGRADED: _ClassVar[AttachedCluster.State]
    STATE_UNSPECIFIED: AttachedCluster.State
    PROVISIONING: AttachedCluster.State
    RUNNING: AttachedCluster.State
    RECONCILING: AttachedCluster.State
    STOPPING: AttachedCluster.State
    ERROR: AttachedCluster.State
    DEGRADED: AttachedCluster.State
    class AnnotationsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class TagsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    OIDC_CONFIG_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_VERSION_FIELD_NUMBER: _ClassVar[int]
    DISTRIBUTION_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_REGION_FIELD_NUMBER: _ClassVar[int]
    FLEET_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    RECONCILING_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    KUBERNETES_VERSION_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    WORKLOAD_IDENTITY_CONFIG_FIELD_NUMBER: _ClassVar[int]
    LOGGING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZATION_FIELD_NUMBER: _ClassVar[int]
    MONITORING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    PROXY_CONFIG_FIELD_NUMBER: _ClassVar[int]
    BINARY_AUTHORIZATION_FIELD_NUMBER: _ClassVar[int]
    SECURITY_POSTURE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    oidc_config: AttachedOidcConfig
    platform_version: str
    distribution: str
    cluster_region: str
    fleet: _common_resources_pb2.Fleet
    state: AttachedCluster.State
    uid: str
    reconciling: bool
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    etag: str
    kubernetes_version: str
    annotations: _containers.ScalarMap[str, str]
    workload_identity_config: _common_resources_pb2.WorkloadIdentityConfig
    logging_config: _common_resources_pb2.LoggingConfig
    errors: _containers.RepeatedCompositeFieldContainer[AttachedClusterError]
    authorization: AttachedClustersAuthorization
    monitoring_config: _common_resources_pb2.MonitoringConfig
    proxy_config: AttachedProxyConfig
    binary_authorization: _common_resources_pb2.BinaryAuthorization
    security_posture_config: _common_resources_pb2.SecurityPostureConfig
    tags: _containers.ScalarMap[str, str]
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., oidc_config: _Optional[_Union[AttachedOidcConfig, _Mapping]] = ..., platform_version: _Optional[str] = ..., distribution: _Optional[str] = ..., cluster_region: _Optional[str] = ..., fleet: _Optional[_Union[_common_resources_pb2.Fleet, _Mapping]] = ..., state: _Optional[_Union[AttachedCluster.State, str]] = ..., uid: _Optional[str] = ..., reconciling: bool = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., etag: _Optional[str] = ..., kubernetes_version: _Optional[str] = ..., annotations: _Optional[_Mapping[str, str]] = ..., workload_identity_config: _Optional[_Union[_common_resources_pb2.WorkloadIdentityConfig, _Mapping]] = ..., logging_config: _Optional[_Union[_common_resources_pb2.LoggingConfig, _Mapping]] = ..., errors: _Optional[_Iterable[_Union[AttachedClusterError, _Mapping]]] = ..., authorization: _Optional[_Union[AttachedClustersAuthorization, _Mapping]] = ..., monitoring_config: _Optional[_Union[_common_resources_pb2.MonitoringConfig, _Mapping]] = ..., proxy_config: _Optional[_Union[AttachedProxyConfig, _Mapping]] = ..., binary_authorization: _Optional[_Union[_common_resources_pb2.BinaryAuthorization, _Mapping]] = ..., security_posture_config: _Optional[_Union[_common_resources_pb2.SecurityPostureConfig, _Mapping]] = ..., tags: _Optional[_Mapping[str, str]] = ...) -> None: ...

class AttachedClustersAuthorization(_message.Message):
    __slots__ = ("admin_users", "admin_groups")
    ADMIN_USERS_FIELD_NUMBER: _ClassVar[int]
    ADMIN_GROUPS_FIELD_NUMBER: _ClassVar[int]
    admin_users: _containers.RepeatedCompositeFieldContainer[AttachedClusterUser]
    admin_groups: _containers.RepeatedCompositeFieldContainer[AttachedClusterGroup]
    def __init__(self, admin_users: _Optional[_Iterable[_Union[AttachedClusterUser, _Mapping]]] = ..., admin_groups: _Optional[_Iterable[_Union[AttachedClusterGroup, _Mapping]]] = ...) -> None: ...

class AttachedClusterUser(_message.Message):
    __slots__ = ("username",)
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    username: str
    def __init__(self, username: _Optional[str] = ...) -> None: ...

class AttachedClusterGroup(_message.Message):
    __slots__ = ("group",)
    GROUP_FIELD_NUMBER: _ClassVar[int]
    group: str
    def __init__(self, group: _Optional[str] = ...) -> None: ...

class AttachedOidcConfig(_message.Message):
    __slots__ = ("issuer_url", "jwks")
    ISSUER_URL_FIELD_NUMBER: _ClassVar[int]
    JWKS_FIELD_NUMBER: _ClassVar[int]
    issuer_url: str
    jwks: bytes
    def __init__(self, issuer_url: _Optional[str] = ..., jwks: _Optional[bytes] = ...) -> None: ...

class AttachedServerConfig(_message.Message):
    __slots__ = ("name", "valid_versions")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALID_VERSIONS_FIELD_NUMBER: _ClassVar[int]
    name: str
    valid_versions: _containers.RepeatedCompositeFieldContainer[AttachedPlatformVersionInfo]
    def __init__(self, name: _Optional[str] = ..., valid_versions: _Optional[_Iterable[_Union[AttachedPlatformVersionInfo, _Mapping]]] = ...) -> None: ...

class AttachedPlatformVersionInfo(_message.Message):
    __slots__ = ("version",)
    VERSION_FIELD_NUMBER: _ClassVar[int]
    version: str
    def __init__(self, version: _Optional[str] = ...) -> None: ...

class AttachedClusterError(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class AttachedProxyConfig(_message.Message):
    __slots__ = ("kubernetes_secret",)
    KUBERNETES_SECRET_FIELD_NUMBER: _ClassVar[int]
    kubernetes_secret: KubernetesSecret
    def __init__(self, kubernetes_secret: _Optional[_Union[KubernetesSecret, _Mapping]] = ...) -> None: ...

class KubernetesSecret(_message.Message):
    __slots__ = ("name", "namespace")
    NAME_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    name: str
    namespace: str
    def __init__(self, name: _Optional[str] = ..., namespace: _Optional[str] = ...) -> None: ...
