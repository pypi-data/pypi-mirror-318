from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Cluster(_message.Message):
    __slots__ = ("gcp_config", "name", "create_time", "update_time", "labels", "capacity_config", "rebalance_config", "state", "satisfies_pzi", "satisfies_pzs")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Cluster.State]
        CREATING: _ClassVar[Cluster.State]
        ACTIVE: _ClassVar[Cluster.State]
        DELETING: _ClassVar[Cluster.State]
    STATE_UNSPECIFIED: Cluster.State
    CREATING: Cluster.State
    ACTIVE: Cluster.State
    DELETING: Cluster.State
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    GCP_CONFIG_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    CAPACITY_CONFIG_FIELD_NUMBER: _ClassVar[int]
    REBALANCE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    SATISFIES_PZI_FIELD_NUMBER: _ClassVar[int]
    SATISFIES_PZS_FIELD_NUMBER: _ClassVar[int]
    gcp_config: GcpConfig
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    capacity_config: CapacityConfig
    rebalance_config: RebalanceConfig
    state: Cluster.State
    satisfies_pzi: bool
    satisfies_pzs: bool
    def __init__(self, gcp_config: _Optional[_Union[GcpConfig, _Mapping]] = ..., name: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., labels: _Optional[_Mapping[str, str]] = ..., capacity_config: _Optional[_Union[CapacityConfig, _Mapping]] = ..., rebalance_config: _Optional[_Union[RebalanceConfig, _Mapping]] = ..., state: _Optional[_Union[Cluster.State, str]] = ..., satisfies_pzi: bool = ..., satisfies_pzs: bool = ...) -> None: ...

class CapacityConfig(_message.Message):
    __slots__ = ("vcpu_count", "memory_bytes")
    VCPU_COUNT_FIELD_NUMBER: _ClassVar[int]
    MEMORY_BYTES_FIELD_NUMBER: _ClassVar[int]
    vcpu_count: int
    memory_bytes: int
    def __init__(self, vcpu_count: _Optional[int] = ..., memory_bytes: _Optional[int] = ...) -> None: ...

class RebalanceConfig(_message.Message):
    __slots__ = ("mode",)
    class Mode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MODE_UNSPECIFIED: _ClassVar[RebalanceConfig.Mode]
        NO_REBALANCE: _ClassVar[RebalanceConfig.Mode]
        AUTO_REBALANCE_ON_SCALE_UP: _ClassVar[RebalanceConfig.Mode]
    MODE_UNSPECIFIED: RebalanceConfig.Mode
    NO_REBALANCE: RebalanceConfig.Mode
    AUTO_REBALANCE_ON_SCALE_UP: RebalanceConfig.Mode
    MODE_FIELD_NUMBER: _ClassVar[int]
    mode: RebalanceConfig.Mode
    def __init__(self, mode: _Optional[_Union[RebalanceConfig.Mode, str]] = ...) -> None: ...

class NetworkConfig(_message.Message):
    __slots__ = ("subnet",)
    SUBNET_FIELD_NUMBER: _ClassVar[int]
    subnet: str
    def __init__(self, subnet: _Optional[str] = ...) -> None: ...

class AccessConfig(_message.Message):
    __slots__ = ("network_configs",)
    NETWORK_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    network_configs: _containers.RepeatedCompositeFieldContainer[NetworkConfig]
    def __init__(self, network_configs: _Optional[_Iterable[_Union[NetworkConfig, _Mapping]]] = ...) -> None: ...

class GcpConfig(_message.Message):
    __slots__ = ("access_config", "kms_key")
    ACCESS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    KMS_KEY_FIELD_NUMBER: _ClassVar[int]
    access_config: AccessConfig
    kms_key: str
    def __init__(self, access_config: _Optional[_Union[AccessConfig, _Mapping]] = ..., kms_key: _Optional[str] = ...) -> None: ...

class Topic(_message.Message):
    __slots__ = ("name", "partition_count", "replication_factor", "configs")
    class ConfigsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    PARTITION_COUNT_FIELD_NUMBER: _ClassVar[int]
    REPLICATION_FACTOR_FIELD_NUMBER: _ClassVar[int]
    CONFIGS_FIELD_NUMBER: _ClassVar[int]
    name: str
    partition_count: int
    replication_factor: int
    configs: _containers.ScalarMap[str, str]
    def __init__(self, name: _Optional[str] = ..., partition_count: _Optional[int] = ..., replication_factor: _Optional[int] = ..., configs: _Optional[_Mapping[str, str]] = ...) -> None: ...

class ConsumerTopicMetadata(_message.Message):
    __slots__ = ("partitions",)
    class PartitionsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: ConsumerPartitionMetadata
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[ConsumerPartitionMetadata, _Mapping]] = ...) -> None: ...
    PARTITIONS_FIELD_NUMBER: _ClassVar[int]
    partitions: _containers.MessageMap[int, ConsumerPartitionMetadata]
    def __init__(self, partitions: _Optional[_Mapping[int, ConsumerPartitionMetadata]] = ...) -> None: ...

class ConsumerPartitionMetadata(_message.Message):
    __slots__ = ("offset", "metadata")
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    offset: int
    metadata: str
    def __init__(self, offset: _Optional[int] = ..., metadata: _Optional[str] = ...) -> None: ...

class ConsumerGroup(_message.Message):
    __slots__ = ("name", "topics")
    class TopicsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ConsumerTopicMetadata
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ConsumerTopicMetadata, _Mapping]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    TOPICS_FIELD_NUMBER: _ClassVar[int]
    name: str
    topics: _containers.MessageMap[str, ConsumerTopicMetadata]
    def __init__(self, name: _Optional[str] = ..., topics: _Optional[_Mapping[str, ConsumerTopicMetadata]] = ...) -> None: ...

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
