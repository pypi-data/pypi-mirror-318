from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.netapp.v1 import volume_pb2 as _volume_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TransferStats(_message.Message):
    __slots__ = ("transfer_bytes", "total_transfer_duration", "last_transfer_bytes", "last_transfer_duration", "lag_duration", "update_time", "last_transfer_end_time", "last_transfer_error")
    TRANSFER_BYTES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_TRANSFER_DURATION_FIELD_NUMBER: _ClassVar[int]
    LAST_TRANSFER_BYTES_FIELD_NUMBER: _ClassVar[int]
    LAST_TRANSFER_DURATION_FIELD_NUMBER: _ClassVar[int]
    LAG_DURATION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LAST_TRANSFER_END_TIME_FIELD_NUMBER: _ClassVar[int]
    LAST_TRANSFER_ERROR_FIELD_NUMBER: _ClassVar[int]
    transfer_bytes: int
    total_transfer_duration: _duration_pb2.Duration
    last_transfer_bytes: int
    last_transfer_duration: _duration_pb2.Duration
    lag_duration: _duration_pb2.Duration
    update_time: _timestamp_pb2.Timestamp
    last_transfer_end_time: _timestamp_pb2.Timestamp
    last_transfer_error: str
    def __init__(self, transfer_bytes: _Optional[int] = ..., total_transfer_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., last_transfer_bytes: _Optional[int] = ..., last_transfer_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., lag_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_transfer_end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_transfer_error: _Optional[str] = ...) -> None: ...

class Replication(_message.Message):
    __slots__ = ("name", "state", "state_details", "role", "replication_schedule", "mirror_state", "healthy", "create_time", "destination_volume", "transfer_stats", "labels", "description", "destination_volume_parameters", "source_volume", "hybrid_peering_details", "cluster_location", "hybrid_replication_type")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Replication.State]
        CREATING: _ClassVar[Replication.State]
        READY: _ClassVar[Replication.State]
        UPDATING: _ClassVar[Replication.State]
        DELETING: _ClassVar[Replication.State]
        ERROR: _ClassVar[Replication.State]
        PENDING_CLUSTER_PEERING: _ClassVar[Replication.State]
        PENDING_SVM_PEERING: _ClassVar[Replication.State]
    STATE_UNSPECIFIED: Replication.State
    CREATING: Replication.State
    READY: Replication.State
    UPDATING: Replication.State
    DELETING: Replication.State
    ERROR: Replication.State
    PENDING_CLUSTER_PEERING: Replication.State
    PENDING_SVM_PEERING: Replication.State
    class ReplicationRole(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        REPLICATION_ROLE_UNSPECIFIED: _ClassVar[Replication.ReplicationRole]
        SOURCE: _ClassVar[Replication.ReplicationRole]
        DESTINATION: _ClassVar[Replication.ReplicationRole]
    REPLICATION_ROLE_UNSPECIFIED: Replication.ReplicationRole
    SOURCE: Replication.ReplicationRole
    DESTINATION: Replication.ReplicationRole
    class ReplicationSchedule(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        REPLICATION_SCHEDULE_UNSPECIFIED: _ClassVar[Replication.ReplicationSchedule]
        EVERY_10_MINUTES: _ClassVar[Replication.ReplicationSchedule]
        HOURLY: _ClassVar[Replication.ReplicationSchedule]
        DAILY: _ClassVar[Replication.ReplicationSchedule]
    REPLICATION_SCHEDULE_UNSPECIFIED: Replication.ReplicationSchedule
    EVERY_10_MINUTES: Replication.ReplicationSchedule
    HOURLY: Replication.ReplicationSchedule
    DAILY: Replication.ReplicationSchedule
    class MirrorState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MIRROR_STATE_UNSPECIFIED: _ClassVar[Replication.MirrorState]
        PREPARING: _ClassVar[Replication.MirrorState]
        MIRRORED: _ClassVar[Replication.MirrorState]
        STOPPED: _ClassVar[Replication.MirrorState]
        TRANSFERRING: _ClassVar[Replication.MirrorState]
        BASELINE_TRANSFERRING: _ClassVar[Replication.MirrorState]
        ABORTED: _ClassVar[Replication.MirrorState]
    MIRROR_STATE_UNSPECIFIED: Replication.MirrorState
    PREPARING: Replication.MirrorState
    MIRRORED: Replication.MirrorState
    STOPPED: Replication.MirrorState
    TRANSFERRING: Replication.MirrorState
    BASELINE_TRANSFERRING: Replication.MirrorState
    ABORTED: Replication.MirrorState
    class HybridReplicationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        HYBRID_REPLICATION_TYPE_UNSPECIFIED: _ClassVar[Replication.HybridReplicationType]
        MIGRATION: _ClassVar[Replication.HybridReplicationType]
        CONTINUOUS_REPLICATION: _ClassVar[Replication.HybridReplicationType]
    HYBRID_REPLICATION_TYPE_UNSPECIFIED: Replication.HybridReplicationType
    MIGRATION: Replication.HybridReplicationType
    CONTINUOUS_REPLICATION: Replication.HybridReplicationType
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATE_DETAILS_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    REPLICATION_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    MIRROR_STATE_FIELD_NUMBER: _ClassVar[int]
    HEALTHY_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_VOLUME_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_STATS_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_VOLUME_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_VOLUME_FIELD_NUMBER: _ClassVar[int]
    HYBRID_PEERING_DETAILS_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_LOCATION_FIELD_NUMBER: _ClassVar[int]
    HYBRID_REPLICATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    name: str
    state: Replication.State
    state_details: str
    role: Replication.ReplicationRole
    replication_schedule: Replication.ReplicationSchedule
    mirror_state: Replication.MirrorState
    healthy: bool
    create_time: _timestamp_pb2.Timestamp
    destination_volume: str
    transfer_stats: TransferStats
    labels: _containers.ScalarMap[str, str]
    description: str
    destination_volume_parameters: DestinationVolumeParameters
    source_volume: str
    hybrid_peering_details: HybridPeeringDetails
    cluster_location: str
    hybrid_replication_type: Replication.HybridReplicationType
    def __init__(self, name: _Optional[str] = ..., state: _Optional[_Union[Replication.State, str]] = ..., state_details: _Optional[str] = ..., role: _Optional[_Union[Replication.ReplicationRole, str]] = ..., replication_schedule: _Optional[_Union[Replication.ReplicationSchedule, str]] = ..., mirror_state: _Optional[_Union[Replication.MirrorState, str]] = ..., healthy: bool = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., destination_volume: _Optional[str] = ..., transfer_stats: _Optional[_Union[TransferStats, _Mapping]] = ..., labels: _Optional[_Mapping[str, str]] = ..., description: _Optional[str] = ..., destination_volume_parameters: _Optional[_Union[DestinationVolumeParameters, _Mapping]] = ..., source_volume: _Optional[str] = ..., hybrid_peering_details: _Optional[_Union[HybridPeeringDetails, _Mapping]] = ..., cluster_location: _Optional[str] = ..., hybrid_replication_type: _Optional[_Union[Replication.HybridReplicationType, str]] = ...) -> None: ...

class HybridPeeringDetails(_message.Message):
    __slots__ = ("subnet_ip", "command", "command_expiry_time", "passphrase")
    SUBNET_IP_FIELD_NUMBER: _ClassVar[int]
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    COMMAND_EXPIRY_TIME_FIELD_NUMBER: _ClassVar[int]
    PASSPHRASE_FIELD_NUMBER: _ClassVar[int]
    subnet_ip: str
    command: str
    command_expiry_time: _timestamp_pb2.Timestamp
    passphrase: str
    def __init__(self, subnet_ip: _Optional[str] = ..., command: _Optional[str] = ..., command_expiry_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., passphrase: _Optional[str] = ...) -> None: ...

class ListReplicationsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token", "order_by", "filter")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    order_by: str
    filter: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., order_by: _Optional[str] = ..., filter: _Optional[str] = ...) -> None: ...

class ListReplicationsResponse(_message.Message):
    __slots__ = ("replications", "next_page_token", "unreachable")
    REPLICATIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    replications: _containers.RepeatedCompositeFieldContainer[Replication]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, replications: _Optional[_Iterable[_Union[Replication, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., unreachable: _Optional[_Iterable[str]] = ...) -> None: ...

class GetReplicationRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class DestinationVolumeParameters(_message.Message):
    __slots__ = ("storage_pool", "volume_id", "share_name", "description", "tiering_policy")
    STORAGE_POOL_FIELD_NUMBER: _ClassVar[int]
    VOLUME_ID_FIELD_NUMBER: _ClassVar[int]
    SHARE_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TIERING_POLICY_FIELD_NUMBER: _ClassVar[int]
    storage_pool: str
    volume_id: str
    share_name: str
    description: str
    tiering_policy: _volume_pb2.TieringPolicy
    def __init__(self, storage_pool: _Optional[str] = ..., volume_id: _Optional[str] = ..., share_name: _Optional[str] = ..., description: _Optional[str] = ..., tiering_policy: _Optional[_Union[_volume_pb2.TieringPolicy, _Mapping]] = ...) -> None: ...

class CreateReplicationRequest(_message.Message):
    __slots__ = ("parent", "replication", "replication_id")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    REPLICATION_FIELD_NUMBER: _ClassVar[int]
    REPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    replication: Replication
    replication_id: str
    def __init__(self, parent: _Optional[str] = ..., replication: _Optional[_Union[Replication, _Mapping]] = ..., replication_id: _Optional[str] = ...) -> None: ...

class DeleteReplicationRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class UpdateReplicationRequest(_message.Message):
    __slots__ = ("update_mask", "replication")
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    REPLICATION_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    replication: Replication
    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., replication: _Optional[_Union[Replication, _Mapping]] = ...) -> None: ...

class StopReplicationRequest(_message.Message):
    __slots__ = ("name", "force")
    NAME_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    force: bool
    def __init__(self, name: _Optional[str] = ..., force: bool = ...) -> None: ...

class ResumeReplicationRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ReverseReplicationDirectionRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class EstablishPeeringRequest(_message.Message):
    __slots__ = ("name", "peer_cluster_name", "peer_svm_name", "peer_ip_addresses", "peer_volume_name")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PEER_CLUSTER_NAME_FIELD_NUMBER: _ClassVar[int]
    PEER_SVM_NAME_FIELD_NUMBER: _ClassVar[int]
    PEER_IP_ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    PEER_VOLUME_NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    peer_cluster_name: str
    peer_svm_name: str
    peer_ip_addresses: _containers.RepeatedScalarFieldContainer[str]
    peer_volume_name: str
    def __init__(self, name: _Optional[str] = ..., peer_cluster_name: _Optional[str] = ..., peer_svm_name: _Optional[str] = ..., peer_ip_addresses: _Optional[_Iterable[str]] = ..., peer_volume_name: _Optional[str] = ...) -> None: ...

class SyncReplicationRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...
