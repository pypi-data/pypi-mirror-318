from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AuthorizationMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AUTH_MODE_UNSPECIFIED: _ClassVar[AuthorizationMode]
    AUTH_MODE_IAM_AUTH: _ClassVar[AuthorizationMode]
    AUTH_MODE_DISABLED: _ClassVar[AuthorizationMode]

class NodeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NODE_TYPE_UNSPECIFIED: _ClassVar[NodeType]
    REDIS_SHARED_CORE_NANO: _ClassVar[NodeType]
    REDIS_HIGHMEM_MEDIUM: _ClassVar[NodeType]
    REDIS_HIGHMEM_XLARGE: _ClassVar[NodeType]
    REDIS_STANDARD_SMALL: _ClassVar[NodeType]

class TransitEncryptionMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TRANSIT_ENCRYPTION_MODE_UNSPECIFIED: _ClassVar[TransitEncryptionMode]
    TRANSIT_ENCRYPTION_MODE_DISABLED: _ClassVar[TransitEncryptionMode]
    TRANSIT_ENCRYPTION_MODE_SERVER_AUTHENTICATION: _ClassVar[TransitEncryptionMode]
AUTH_MODE_UNSPECIFIED: AuthorizationMode
AUTH_MODE_IAM_AUTH: AuthorizationMode
AUTH_MODE_DISABLED: AuthorizationMode
NODE_TYPE_UNSPECIFIED: NodeType
REDIS_SHARED_CORE_NANO: NodeType
REDIS_HIGHMEM_MEDIUM: NodeType
REDIS_HIGHMEM_XLARGE: NodeType
REDIS_STANDARD_SMALL: NodeType
TRANSIT_ENCRYPTION_MODE_UNSPECIFIED: TransitEncryptionMode
TRANSIT_ENCRYPTION_MODE_DISABLED: TransitEncryptionMode
TRANSIT_ENCRYPTION_MODE_SERVER_AUTHENTICATION: TransitEncryptionMode

class CreateClusterRequest(_message.Message):
    __slots__ = ("parent", "cluster_id", "cluster", "request_id")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    cluster_id: str
    cluster: Cluster
    request_id: str
    def __init__(self, parent: _Optional[str] = ..., cluster_id: _Optional[str] = ..., cluster: _Optional[_Union[Cluster, _Mapping]] = ..., request_id: _Optional[str] = ...) -> None: ...

class ListClustersRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListClustersResponse(_message.Message):
    __slots__ = ("clusters", "next_page_token", "unreachable")
    CLUSTERS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    clusters: _containers.RepeatedCompositeFieldContainer[Cluster]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, clusters: _Optional[_Iterable[_Union[Cluster, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., unreachable: _Optional[_Iterable[str]] = ...) -> None: ...

class UpdateClusterRequest(_message.Message):
    __slots__ = ("update_mask", "cluster", "request_id")
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    cluster: Cluster
    request_id: str
    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., cluster: _Optional[_Union[Cluster, _Mapping]] = ..., request_id: _Optional[str] = ...) -> None: ...

class GetClusterRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class DeleteClusterRequest(_message.Message):
    __slots__ = ("name", "request_id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str
    def __init__(self, name: _Optional[str] = ..., request_id: _Optional[str] = ...) -> None: ...

class GetClusterCertificateAuthorityRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class Cluster(_message.Message):
    __slots__ = ("name", "create_time", "state", "uid", "replica_count", "authorization_mode", "transit_encryption_mode", "size_gb", "shard_count", "psc_configs", "discovery_endpoints", "psc_connections", "state_info", "node_type", "persistence_config", "redis_configs", "precise_size_gb", "zone_distribution_config", "deletion_protection_enabled")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Cluster.State]
        CREATING: _ClassVar[Cluster.State]
        ACTIVE: _ClassVar[Cluster.State]
        UPDATING: _ClassVar[Cluster.State]
        DELETING: _ClassVar[Cluster.State]
    STATE_UNSPECIFIED: Cluster.State
    CREATING: Cluster.State
    ACTIVE: Cluster.State
    UPDATING: Cluster.State
    DELETING: Cluster.State
    class StateInfo(_message.Message):
        __slots__ = ("update_info",)
        class UpdateInfo(_message.Message):
            __slots__ = ("target_shard_count", "target_replica_count")
            TARGET_SHARD_COUNT_FIELD_NUMBER: _ClassVar[int]
            TARGET_REPLICA_COUNT_FIELD_NUMBER: _ClassVar[int]
            target_shard_count: int
            target_replica_count: int
            def __init__(self, target_shard_count: _Optional[int] = ..., target_replica_count: _Optional[int] = ...) -> None: ...
        UPDATE_INFO_FIELD_NUMBER: _ClassVar[int]
        update_info: Cluster.StateInfo.UpdateInfo
        def __init__(self, update_info: _Optional[_Union[Cluster.StateInfo.UpdateInfo, _Mapping]] = ...) -> None: ...
    class RedisConfigsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    REPLICA_COUNT_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZATION_MODE_FIELD_NUMBER: _ClassVar[int]
    TRANSIT_ENCRYPTION_MODE_FIELD_NUMBER: _ClassVar[int]
    SIZE_GB_FIELD_NUMBER: _ClassVar[int]
    SHARD_COUNT_FIELD_NUMBER: _ClassVar[int]
    PSC_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    DISCOVERY_ENDPOINTS_FIELD_NUMBER: _ClassVar[int]
    PSC_CONNECTIONS_FIELD_NUMBER: _ClassVar[int]
    STATE_INFO_FIELD_NUMBER: _ClassVar[int]
    NODE_TYPE_FIELD_NUMBER: _ClassVar[int]
    PERSISTENCE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    REDIS_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    PRECISE_SIZE_GB_FIELD_NUMBER: _ClassVar[int]
    ZONE_DISTRIBUTION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DELETION_PROTECTION_ENABLED_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    state: Cluster.State
    uid: str
    replica_count: int
    authorization_mode: AuthorizationMode
    transit_encryption_mode: TransitEncryptionMode
    size_gb: int
    shard_count: int
    psc_configs: _containers.RepeatedCompositeFieldContainer[PscConfig]
    discovery_endpoints: _containers.RepeatedCompositeFieldContainer[DiscoveryEndpoint]
    psc_connections: _containers.RepeatedCompositeFieldContainer[PscConnection]
    state_info: Cluster.StateInfo
    node_type: NodeType
    persistence_config: ClusterPersistenceConfig
    redis_configs: _containers.ScalarMap[str, str]
    precise_size_gb: float
    zone_distribution_config: ZoneDistributionConfig
    deletion_protection_enabled: bool
    def __init__(self, name: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., state: _Optional[_Union[Cluster.State, str]] = ..., uid: _Optional[str] = ..., replica_count: _Optional[int] = ..., authorization_mode: _Optional[_Union[AuthorizationMode, str]] = ..., transit_encryption_mode: _Optional[_Union[TransitEncryptionMode, str]] = ..., size_gb: _Optional[int] = ..., shard_count: _Optional[int] = ..., psc_configs: _Optional[_Iterable[_Union[PscConfig, _Mapping]]] = ..., discovery_endpoints: _Optional[_Iterable[_Union[DiscoveryEndpoint, _Mapping]]] = ..., psc_connections: _Optional[_Iterable[_Union[PscConnection, _Mapping]]] = ..., state_info: _Optional[_Union[Cluster.StateInfo, _Mapping]] = ..., node_type: _Optional[_Union[NodeType, str]] = ..., persistence_config: _Optional[_Union[ClusterPersistenceConfig, _Mapping]] = ..., redis_configs: _Optional[_Mapping[str, str]] = ..., precise_size_gb: _Optional[float] = ..., zone_distribution_config: _Optional[_Union[ZoneDistributionConfig, _Mapping]] = ..., deletion_protection_enabled: bool = ...) -> None: ...

class PscConfig(_message.Message):
    __slots__ = ("network",)
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    network: str
    def __init__(self, network: _Optional[str] = ...) -> None: ...

class DiscoveryEndpoint(_message.Message):
    __slots__ = ("address", "port", "psc_config")
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    PSC_CONFIG_FIELD_NUMBER: _ClassVar[int]
    address: str
    port: int
    psc_config: PscConfig
    def __init__(self, address: _Optional[str] = ..., port: _Optional[int] = ..., psc_config: _Optional[_Union[PscConfig, _Mapping]] = ...) -> None: ...

class PscConnection(_message.Message):
    __slots__ = ("psc_connection_id", "address", "forwarding_rule", "project_id", "network")
    PSC_CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    FORWARDING_RULE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    psc_connection_id: str
    address: str
    forwarding_rule: str
    project_id: str
    network: str
    def __init__(self, psc_connection_id: _Optional[str] = ..., address: _Optional[str] = ..., forwarding_rule: _Optional[str] = ..., project_id: _Optional[str] = ..., network: _Optional[str] = ...) -> None: ...

class OperationMetadata(_message.Message):
    __slots__ = ("create_time", "end_time", "target", "verb", "status_message", "requested_cancellation", "api_version")
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    VERB_FIELD_NUMBER: _ClassVar[int]
    STATUS_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_CANCELLATION_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    target: str
    verb: str
    status_message: str
    requested_cancellation: bool
    api_version: str
    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., target: _Optional[str] = ..., verb: _Optional[str] = ..., status_message: _Optional[str] = ..., requested_cancellation: bool = ..., api_version: _Optional[str] = ...) -> None: ...

class CertificateAuthority(_message.Message):
    __slots__ = ("managed_server_ca", "name")
    class ManagedCertificateAuthority(_message.Message):
        __slots__ = ("ca_certs",)
        class CertChain(_message.Message):
            __slots__ = ("certificates",)
            CERTIFICATES_FIELD_NUMBER: _ClassVar[int]
            certificates: _containers.RepeatedScalarFieldContainer[str]
            def __init__(self, certificates: _Optional[_Iterable[str]] = ...) -> None: ...
        CA_CERTS_FIELD_NUMBER: _ClassVar[int]
        ca_certs: _containers.RepeatedCompositeFieldContainer[CertificateAuthority.ManagedCertificateAuthority.CertChain]
        def __init__(self, ca_certs: _Optional[_Iterable[_Union[CertificateAuthority.ManagedCertificateAuthority.CertChain, _Mapping]]] = ...) -> None: ...
    MANAGED_SERVER_CA_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    managed_server_ca: CertificateAuthority.ManagedCertificateAuthority
    name: str
    def __init__(self, managed_server_ca: _Optional[_Union[CertificateAuthority.ManagedCertificateAuthority, _Mapping]] = ..., name: _Optional[str] = ...) -> None: ...

class ClusterPersistenceConfig(_message.Message):
    __slots__ = ("mode", "rdb_config", "aof_config")
    class PersistenceMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PERSISTENCE_MODE_UNSPECIFIED: _ClassVar[ClusterPersistenceConfig.PersistenceMode]
        DISABLED: _ClassVar[ClusterPersistenceConfig.PersistenceMode]
        RDB: _ClassVar[ClusterPersistenceConfig.PersistenceMode]
        AOF: _ClassVar[ClusterPersistenceConfig.PersistenceMode]
    PERSISTENCE_MODE_UNSPECIFIED: ClusterPersistenceConfig.PersistenceMode
    DISABLED: ClusterPersistenceConfig.PersistenceMode
    RDB: ClusterPersistenceConfig.PersistenceMode
    AOF: ClusterPersistenceConfig.PersistenceMode
    class RDBConfig(_message.Message):
        __slots__ = ("rdb_snapshot_period", "rdb_snapshot_start_time")
        class SnapshotPeriod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            SNAPSHOT_PERIOD_UNSPECIFIED: _ClassVar[ClusterPersistenceConfig.RDBConfig.SnapshotPeriod]
            ONE_HOUR: _ClassVar[ClusterPersistenceConfig.RDBConfig.SnapshotPeriod]
            SIX_HOURS: _ClassVar[ClusterPersistenceConfig.RDBConfig.SnapshotPeriod]
            TWELVE_HOURS: _ClassVar[ClusterPersistenceConfig.RDBConfig.SnapshotPeriod]
            TWENTY_FOUR_HOURS: _ClassVar[ClusterPersistenceConfig.RDBConfig.SnapshotPeriod]
        SNAPSHOT_PERIOD_UNSPECIFIED: ClusterPersistenceConfig.RDBConfig.SnapshotPeriod
        ONE_HOUR: ClusterPersistenceConfig.RDBConfig.SnapshotPeriod
        SIX_HOURS: ClusterPersistenceConfig.RDBConfig.SnapshotPeriod
        TWELVE_HOURS: ClusterPersistenceConfig.RDBConfig.SnapshotPeriod
        TWENTY_FOUR_HOURS: ClusterPersistenceConfig.RDBConfig.SnapshotPeriod
        RDB_SNAPSHOT_PERIOD_FIELD_NUMBER: _ClassVar[int]
        RDB_SNAPSHOT_START_TIME_FIELD_NUMBER: _ClassVar[int]
        rdb_snapshot_period: ClusterPersistenceConfig.RDBConfig.SnapshotPeriod
        rdb_snapshot_start_time: _timestamp_pb2.Timestamp
        def __init__(self, rdb_snapshot_period: _Optional[_Union[ClusterPersistenceConfig.RDBConfig.SnapshotPeriod, str]] = ..., rdb_snapshot_start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    class AOFConfig(_message.Message):
        __slots__ = ("append_fsync",)
        class AppendFsync(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            APPEND_FSYNC_UNSPECIFIED: _ClassVar[ClusterPersistenceConfig.AOFConfig.AppendFsync]
            NO: _ClassVar[ClusterPersistenceConfig.AOFConfig.AppendFsync]
            EVERYSEC: _ClassVar[ClusterPersistenceConfig.AOFConfig.AppendFsync]
            ALWAYS: _ClassVar[ClusterPersistenceConfig.AOFConfig.AppendFsync]
        APPEND_FSYNC_UNSPECIFIED: ClusterPersistenceConfig.AOFConfig.AppendFsync
        NO: ClusterPersistenceConfig.AOFConfig.AppendFsync
        EVERYSEC: ClusterPersistenceConfig.AOFConfig.AppendFsync
        ALWAYS: ClusterPersistenceConfig.AOFConfig.AppendFsync
        APPEND_FSYNC_FIELD_NUMBER: _ClassVar[int]
        append_fsync: ClusterPersistenceConfig.AOFConfig.AppendFsync
        def __init__(self, append_fsync: _Optional[_Union[ClusterPersistenceConfig.AOFConfig.AppendFsync, str]] = ...) -> None: ...
    MODE_FIELD_NUMBER: _ClassVar[int]
    RDB_CONFIG_FIELD_NUMBER: _ClassVar[int]
    AOF_CONFIG_FIELD_NUMBER: _ClassVar[int]
    mode: ClusterPersistenceConfig.PersistenceMode
    rdb_config: ClusterPersistenceConfig.RDBConfig
    aof_config: ClusterPersistenceConfig.AOFConfig
    def __init__(self, mode: _Optional[_Union[ClusterPersistenceConfig.PersistenceMode, str]] = ..., rdb_config: _Optional[_Union[ClusterPersistenceConfig.RDBConfig, _Mapping]] = ..., aof_config: _Optional[_Union[ClusterPersistenceConfig.AOFConfig, _Mapping]] = ...) -> None: ...

class ZoneDistributionConfig(_message.Message):
    __slots__ = ("mode", "zone")
    class ZoneDistributionMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ZONE_DISTRIBUTION_MODE_UNSPECIFIED: _ClassVar[ZoneDistributionConfig.ZoneDistributionMode]
        MULTI_ZONE: _ClassVar[ZoneDistributionConfig.ZoneDistributionMode]
        SINGLE_ZONE: _ClassVar[ZoneDistributionConfig.ZoneDistributionMode]
    ZONE_DISTRIBUTION_MODE_UNSPECIFIED: ZoneDistributionConfig.ZoneDistributionMode
    MULTI_ZONE: ZoneDistributionConfig.ZoneDistributionMode
    SINGLE_ZONE: ZoneDistributionConfig.ZoneDistributionMode
    MODE_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    mode: ZoneDistributionConfig.ZoneDistributionMode
    zone: str
    def __init__(self, mode: _Optional[_Union[ZoneDistributionConfig.ZoneDistributionMode, str]] = ..., zone: _Optional[str] = ...) -> None: ...
