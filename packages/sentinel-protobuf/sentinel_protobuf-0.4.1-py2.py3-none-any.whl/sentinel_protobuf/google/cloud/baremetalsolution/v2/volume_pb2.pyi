from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.baremetalsolution.v2 import common_pb2 as _common_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Volume(_message.Message):
    __slots__ = ('name', 'id', 'storage_type', 'state', 'requested_size_gib', 'originally_requested_size_gib', 'current_size_gib', 'emergency_size_gib', 'max_size_gib', 'auto_grown_size_gib', 'remaining_space_gib', 'snapshot_reservation_detail', 'snapshot_auto_delete_behavior', 'labels', 'snapshot_enabled', 'pod', 'protocol', 'boot_volume', 'performance_tier', 'notes', 'workload_profile', 'expire_time', 'instances', 'attached')

    class StorageType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STORAGE_TYPE_UNSPECIFIED: _ClassVar[Volume.StorageType]
        SSD: _ClassVar[Volume.StorageType]
        HDD: _ClassVar[Volume.StorageType]
    STORAGE_TYPE_UNSPECIFIED: Volume.StorageType
    SSD: Volume.StorageType
    HDD: Volume.StorageType

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Volume.State]
        CREATING: _ClassVar[Volume.State]
        READY: _ClassVar[Volume.State]
        DELETING: _ClassVar[Volume.State]
        UPDATING: _ClassVar[Volume.State]
        COOL_OFF: _ClassVar[Volume.State]
    STATE_UNSPECIFIED: Volume.State
    CREATING: Volume.State
    READY: Volume.State
    DELETING: Volume.State
    UPDATING: Volume.State
    COOL_OFF: Volume.State

    class SnapshotAutoDeleteBehavior(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SNAPSHOT_AUTO_DELETE_BEHAVIOR_UNSPECIFIED: _ClassVar[Volume.SnapshotAutoDeleteBehavior]
        DISABLED: _ClassVar[Volume.SnapshotAutoDeleteBehavior]
        OLDEST_FIRST: _ClassVar[Volume.SnapshotAutoDeleteBehavior]
        NEWEST_FIRST: _ClassVar[Volume.SnapshotAutoDeleteBehavior]
    SNAPSHOT_AUTO_DELETE_BEHAVIOR_UNSPECIFIED: Volume.SnapshotAutoDeleteBehavior
    DISABLED: Volume.SnapshotAutoDeleteBehavior
    OLDEST_FIRST: Volume.SnapshotAutoDeleteBehavior
    NEWEST_FIRST: Volume.SnapshotAutoDeleteBehavior

    class Protocol(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PROTOCOL_UNSPECIFIED: _ClassVar[Volume.Protocol]
        FIBRE_CHANNEL: _ClassVar[Volume.Protocol]
        NFS: _ClassVar[Volume.Protocol]
    PROTOCOL_UNSPECIFIED: Volume.Protocol
    FIBRE_CHANNEL: Volume.Protocol
    NFS: Volume.Protocol

    class WorkloadProfile(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        WORKLOAD_PROFILE_UNSPECIFIED: _ClassVar[Volume.WorkloadProfile]
        GENERIC: _ClassVar[Volume.WorkloadProfile]
        HANA: _ClassVar[Volume.WorkloadProfile]
    WORKLOAD_PROFILE_UNSPECIFIED: Volume.WorkloadProfile
    GENERIC: Volume.WorkloadProfile
    HANA: Volume.WorkloadProfile

    class SnapshotReservationDetail(_message.Message):
        __slots__ = ('reserved_space_gib', 'reserved_space_used_percent', 'reserved_space_remaining_gib', 'reserved_space_percent')
        RESERVED_SPACE_GIB_FIELD_NUMBER: _ClassVar[int]
        RESERVED_SPACE_USED_PERCENT_FIELD_NUMBER: _ClassVar[int]
        RESERVED_SPACE_REMAINING_GIB_FIELD_NUMBER: _ClassVar[int]
        RESERVED_SPACE_PERCENT_FIELD_NUMBER: _ClassVar[int]
        reserved_space_gib: int
        reserved_space_used_percent: int
        reserved_space_remaining_gib: int
        reserved_space_percent: int

        def __init__(self, reserved_space_gib: _Optional[int]=..., reserved_space_used_percent: _Optional[int]=..., reserved_space_remaining_gib: _Optional[int]=..., reserved_space_percent: _Optional[int]=...) -> None:
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
    ID_FIELD_NUMBER: _ClassVar[int]
    STORAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_SIZE_GIB_FIELD_NUMBER: _ClassVar[int]
    ORIGINALLY_REQUESTED_SIZE_GIB_FIELD_NUMBER: _ClassVar[int]
    CURRENT_SIZE_GIB_FIELD_NUMBER: _ClassVar[int]
    EMERGENCY_SIZE_GIB_FIELD_NUMBER: _ClassVar[int]
    MAX_SIZE_GIB_FIELD_NUMBER: _ClassVar[int]
    AUTO_GROWN_SIZE_GIB_FIELD_NUMBER: _ClassVar[int]
    REMAINING_SPACE_GIB_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_RESERVATION_DETAIL_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_AUTO_DELETE_BEHAVIOR_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_ENABLED_FIELD_NUMBER: _ClassVar[int]
    POD_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    BOOT_VOLUME_FIELD_NUMBER: _ClassVar[int]
    PERFORMANCE_TIER_FIELD_NUMBER: _ClassVar[int]
    NOTES_FIELD_NUMBER: _ClassVar[int]
    WORKLOAD_PROFILE_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
    INSTANCES_FIELD_NUMBER: _ClassVar[int]
    ATTACHED_FIELD_NUMBER: _ClassVar[int]
    name: str
    id: str
    storage_type: Volume.StorageType
    state: Volume.State
    requested_size_gib: int
    originally_requested_size_gib: int
    current_size_gib: int
    emergency_size_gib: int
    max_size_gib: int
    auto_grown_size_gib: int
    remaining_space_gib: int
    snapshot_reservation_detail: Volume.SnapshotReservationDetail
    snapshot_auto_delete_behavior: Volume.SnapshotAutoDeleteBehavior
    labels: _containers.ScalarMap[str, str]
    snapshot_enabled: bool
    pod: str
    protocol: Volume.Protocol
    boot_volume: bool
    performance_tier: _common_pb2.VolumePerformanceTier
    notes: str
    workload_profile: Volume.WorkloadProfile
    expire_time: _timestamp_pb2.Timestamp
    instances: _containers.RepeatedScalarFieldContainer[str]
    attached: bool

    def __init__(self, name: _Optional[str]=..., id: _Optional[str]=..., storage_type: _Optional[_Union[Volume.StorageType, str]]=..., state: _Optional[_Union[Volume.State, str]]=..., requested_size_gib: _Optional[int]=..., originally_requested_size_gib: _Optional[int]=..., current_size_gib: _Optional[int]=..., emergency_size_gib: _Optional[int]=..., max_size_gib: _Optional[int]=..., auto_grown_size_gib: _Optional[int]=..., remaining_space_gib: _Optional[int]=..., snapshot_reservation_detail: _Optional[_Union[Volume.SnapshotReservationDetail, _Mapping]]=..., snapshot_auto_delete_behavior: _Optional[_Union[Volume.SnapshotAutoDeleteBehavior, str]]=..., labels: _Optional[_Mapping[str, str]]=..., snapshot_enabled: bool=..., pod: _Optional[str]=..., protocol: _Optional[_Union[Volume.Protocol, str]]=..., boot_volume: bool=..., performance_tier: _Optional[_Union[_common_pb2.VolumePerformanceTier, str]]=..., notes: _Optional[str]=..., workload_profile: _Optional[_Union[Volume.WorkloadProfile, str]]=..., expire_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., instances: _Optional[_Iterable[str]]=..., attached: bool=...) -> None:
        ...

class GetVolumeRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListVolumesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=...) -> None:
        ...

class ListVolumesResponse(_message.Message):
    __slots__ = ('volumes', 'next_page_token', 'unreachable')
    VOLUMES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    volumes: _containers.RepeatedCompositeFieldContainer[Volume]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, volumes: _Optional[_Iterable[_Union[Volume, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class UpdateVolumeRequest(_message.Message):
    __slots__ = ('volume', 'update_mask')
    VOLUME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    volume: Volume
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, volume: _Optional[_Union[Volume, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class RenameVolumeRequest(_message.Message):
    __slots__ = ('name', 'new_volume_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    NEW_VOLUME_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    new_volume_id: str

    def __init__(self, name: _Optional[str]=..., new_volume_id: _Optional[str]=...) -> None:
        ...

class EvictVolumeRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ResizeVolumeRequest(_message.Message):
    __slots__ = ('volume', 'size_gib')
    VOLUME_FIELD_NUMBER: _ClassVar[int]
    SIZE_GIB_FIELD_NUMBER: _ClassVar[int]
    volume: str
    size_gib: int

    def __init__(self, volume: _Optional[str]=..., size_gib: _Optional[int]=...) -> None:
        ...