from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.bigtable.admin.v2 import common_pb2 as _common_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Instance(_message.Message):
    __slots__ = ("name", "display_name", "state", "type", "labels", "create_time", "satisfies_pzs")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_NOT_KNOWN: _ClassVar[Instance.State]
        READY: _ClassVar[Instance.State]
        CREATING: _ClassVar[Instance.State]
    STATE_NOT_KNOWN: Instance.State
    READY: Instance.State
    CREATING: Instance.State
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[Instance.Type]
        PRODUCTION: _ClassVar[Instance.Type]
        DEVELOPMENT: _ClassVar[Instance.Type]
    TYPE_UNSPECIFIED: Instance.Type
    PRODUCTION: Instance.Type
    DEVELOPMENT: Instance.Type
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    SATISFIES_PZS_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    state: Instance.State
    type: Instance.Type
    labels: _containers.ScalarMap[str, str]
    create_time: _timestamp_pb2.Timestamp
    satisfies_pzs: bool
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., state: _Optional[_Union[Instance.State, str]] = ..., type: _Optional[_Union[Instance.Type, str]] = ..., labels: _Optional[_Mapping[str, str]] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., satisfies_pzs: bool = ...) -> None: ...

class AutoscalingTargets(_message.Message):
    __slots__ = ("cpu_utilization_percent", "storage_utilization_gib_per_node")
    CPU_UTILIZATION_PERCENT_FIELD_NUMBER: _ClassVar[int]
    STORAGE_UTILIZATION_GIB_PER_NODE_FIELD_NUMBER: _ClassVar[int]
    cpu_utilization_percent: int
    storage_utilization_gib_per_node: int
    def __init__(self, cpu_utilization_percent: _Optional[int] = ..., storage_utilization_gib_per_node: _Optional[int] = ...) -> None: ...

class AutoscalingLimits(_message.Message):
    __slots__ = ("min_serve_nodes", "max_serve_nodes")
    MIN_SERVE_NODES_FIELD_NUMBER: _ClassVar[int]
    MAX_SERVE_NODES_FIELD_NUMBER: _ClassVar[int]
    min_serve_nodes: int
    max_serve_nodes: int
    def __init__(self, min_serve_nodes: _Optional[int] = ..., max_serve_nodes: _Optional[int] = ...) -> None: ...

class Cluster(_message.Message):
    __slots__ = ("name", "location", "state", "serve_nodes", "node_scaling_factor", "cluster_config", "default_storage_type", "encryption_config")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_NOT_KNOWN: _ClassVar[Cluster.State]
        READY: _ClassVar[Cluster.State]
        CREATING: _ClassVar[Cluster.State]
        RESIZING: _ClassVar[Cluster.State]
        DISABLED: _ClassVar[Cluster.State]
    STATE_NOT_KNOWN: Cluster.State
    READY: Cluster.State
    CREATING: Cluster.State
    RESIZING: Cluster.State
    DISABLED: Cluster.State
    class NodeScalingFactor(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NODE_SCALING_FACTOR_UNSPECIFIED: _ClassVar[Cluster.NodeScalingFactor]
        NODE_SCALING_FACTOR_1X: _ClassVar[Cluster.NodeScalingFactor]
        NODE_SCALING_FACTOR_2X: _ClassVar[Cluster.NodeScalingFactor]
    NODE_SCALING_FACTOR_UNSPECIFIED: Cluster.NodeScalingFactor
    NODE_SCALING_FACTOR_1X: Cluster.NodeScalingFactor
    NODE_SCALING_FACTOR_2X: Cluster.NodeScalingFactor
    class ClusterAutoscalingConfig(_message.Message):
        __slots__ = ("autoscaling_limits", "autoscaling_targets")
        AUTOSCALING_LIMITS_FIELD_NUMBER: _ClassVar[int]
        AUTOSCALING_TARGETS_FIELD_NUMBER: _ClassVar[int]
        autoscaling_limits: AutoscalingLimits
        autoscaling_targets: AutoscalingTargets
        def __init__(self, autoscaling_limits: _Optional[_Union[AutoscalingLimits, _Mapping]] = ..., autoscaling_targets: _Optional[_Union[AutoscalingTargets, _Mapping]] = ...) -> None: ...
    class ClusterConfig(_message.Message):
        __slots__ = ("cluster_autoscaling_config",)
        CLUSTER_AUTOSCALING_CONFIG_FIELD_NUMBER: _ClassVar[int]
        cluster_autoscaling_config: Cluster.ClusterAutoscalingConfig
        def __init__(self, cluster_autoscaling_config: _Optional[_Union[Cluster.ClusterAutoscalingConfig, _Mapping]] = ...) -> None: ...
    class EncryptionConfig(_message.Message):
        __slots__ = ("kms_key_name",)
        KMS_KEY_NAME_FIELD_NUMBER: _ClassVar[int]
        kms_key_name: str
        def __init__(self, kms_key_name: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    SERVE_NODES_FIELD_NUMBER: _ClassVar[int]
    NODE_SCALING_FACTOR_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_STORAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    name: str
    location: str
    state: Cluster.State
    serve_nodes: int
    node_scaling_factor: Cluster.NodeScalingFactor
    cluster_config: Cluster.ClusterConfig
    default_storage_type: _common_pb2.StorageType
    encryption_config: Cluster.EncryptionConfig
    def __init__(self, name: _Optional[str] = ..., location: _Optional[str] = ..., state: _Optional[_Union[Cluster.State, str]] = ..., serve_nodes: _Optional[int] = ..., node_scaling_factor: _Optional[_Union[Cluster.NodeScalingFactor, str]] = ..., cluster_config: _Optional[_Union[Cluster.ClusterConfig, _Mapping]] = ..., default_storage_type: _Optional[_Union[_common_pb2.StorageType, str]] = ..., encryption_config: _Optional[_Union[Cluster.EncryptionConfig, _Mapping]] = ...) -> None: ...

class AppProfile(_message.Message):
    __slots__ = ("name", "etag", "description", "multi_cluster_routing_use_any", "single_cluster_routing", "priority", "standard_isolation", "data_boost_isolation_read_only")
    class Priority(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PRIORITY_UNSPECIFIED: _ClassVar[AppProfile.Priority]
        PRIORITY_LOW: _ClassVar[AppProfile.Priority]
        PRIORITY_MEDIUM: _ClassVar[AppProfile.Priority]
        PRIORITY_HIGH: _ClassVar[AppProfile.Priority]
    PRIORITY_UNSPECIFIED: AppProfile.Priority
    PRIORITY_LOW: AppProfile.Priority
    PRIORITY_MEDIUM: AppProfile.Priority
    PRIORITY_HIGH: AppProfile.Priority
    class MultiClusterRoutingUseAny(_message.Message):
        __slots__ = ("cluster_ids", "row_affinity")
        class RowAffinity(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        CLUSTER_IDS_FIELD_NUMBER: _ClassVar[int]
        ROW_AFFINITY_FIELD_NUMBER: _ClassVar[int]
        cluster_ids: _containers.RepeatedScalarFieldContainer[str]
        row_affinity: AppProfile.MultiClusterRoutingUseAny.RowAffinity
        def __init__(self, cluster_ids: _Optional[_Iterable[str]] = ..., row_affinity: _Optional[_Union[AppProfile.MultiClusterRoutingUseAny.RowAffinity, _Mapping]] = ...) -> None: ...
    class SingleClusterRouting(_message.Message):
        __slots__ = ("cluster_id", "allow_transactional_writes")
        CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
        ALLOW_TRANSACTIONAL_WRITES_FIELD_NUMBER: _ClassVar[int]
        cluster_id: str
        allow_transactional_writes: bool
        def __init__(self, cluster_id: _Optional[str] = ..., allow_transactional_writes: bool = ...) -> None: ...
    class StandardIsolation(_message.Message):
        __slots__ = ("priority",)
        PRIORITY_FIELD_NUMBER: _ClassVar[int]
        priority: AppProfile.Priority
        def __init__(self, priority: _Optional[_Union[AppProfile.Priority, str]] = ...) -> None: ...
    class DataBoostIsolationReadOnly(_message.Message):
        __slots__ = ("compute_billing_owner",)
        class ComputeBillingOwner(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            COMPUTE_BILLING_OWNER_UNSPECIFIED: _ClassVar[AppProfile.DataBoostIsolationReadOnly.ComputeBillingOwner]
            HOST_PAYS: _ClassVar[AppProfile.DataBoostIsolationReadOnly.ComputeBillingOwner]
        COMPUTE_BILLING_OWNER_UNSPECIFIED: AppProfile.DataBoostIsolationReadOnly.ComputeBillingOwner
        HOST_PAYS: AppProfile.DataBoostIsolationReadOnly.ComputeBillingOwner
        COMPUTE_BILLING_OWNER_FIELD_NUMBER: _ClassVar[int]
        compute_billing_owner: AppProfile.DataBoostIsolationReadOnly.ComputeBillingOwner
        def __init__(self, compute_billing_owner: _Optional[_Union[AppProfile.DataBoostIsolationReadOnly.ComputeBillingOwner, str]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    MULTI_CLUSTER_ROUTING_USE_ANY_FIELD_NUMBER: _ClassVar[int]
    SINGLE_CLUSTER_ROUTING_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    STANDARD_ISOLATION_FIELD_NUMBER: _ClassVar[int]
    DATA_BOOST_ISOLATION_READ_ONLY_FIELD_NUMBER: _ClassVar[int]
    name: str
    etag: str
    description: str
    multi_cluster_routing_use_any: AppProfile.MultiClusterRoutingUseAny
    single_cluster_routing: AppProfile.SingleClusterRouting
    priority: AppProfile.Priority
    standard_isolation: AppProfile.StandardIsolation
    data_boost_isolation_read_only: AppProfile.DataBoostIsolationReadOnly
    def __init__(self, name: _Optional[str] = ..., etag: _Optional[str] = ..., description: _Optional[str] = ..., multi_cluster_routing_use_any: _Optional[_Union[AppProfile.MultiClusterRoutingUseAny, _Mapping]] = ..., single_cluster_routing: _Optional[_Union[AppProfile.SingleClusterRouting, _Mapping]] = ..., priority: _Optional[_Union[AppProfile.Priority, str]] = ..., standard_isolation: _Optional[_Union[AppProfile.StandardIsolation, _Mapping]] = ..., data_boost_isolation_read_only: _Optional[_Union[AppProfile.DataBoostIsolationReadOnly, _Mapping]] = ...) -> None: ...

class HotTablet(_message.Message):
    __slots__ = ("name", "table_name", "start_time", "end_time", "start_key", "end_key", "node_cpu_usage_percent")
    NAME_FIELD_NUMBER: _ClassVar[int]
    TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    START_KEY_FIELD_NUMBER: _ClassVar[int]
    END_KEY_FIELD_NUMBER: _ClassVar[int]
    NODE_CPU_USAGE_PERCENT_FIELD_NUMBER: _ClassVar[int]
    name: str
    table_name: str
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    start_key: str
    end_key: str
    node_cpu_usage_percent: float
    def __init__(self, name: _Optional[str] = ..., table_name: _Optional[str] = ..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., start_key: _Optional[str] = ..., end_key: _Optional[str] = ..., node_cpu_usage_percent: _Optional[float] = ...) -> None: ...
