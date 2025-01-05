from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class VolumeSnapshot(_message.Message):
    __slots__ = ('name', 'id', 'description', 'create_time', 'storage_volume', 'type')

    class SnapshotType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SNAPSHOT_TYPE_UNSPECIFIED: _ClassVar[VolumeSnapshot.SnapshotType]
        AD_HOC: _ClassVar[VolumeSnapshot.SnapshotType]
        SCHEDULED: _ClassVar[VolumeSnapshot.SnapshotType]
    SNAPSHOT_TYPE_UNSPECIFIED: VolumeSnapshot.SnapshotType
    AD_HOC: VolumeSnapshot.SnapshotType
    SCHEDULED: VolumeSnapshot.SnapshotType
    NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    STORAGE_VOLUME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    name: str
    id: str
    description: str
    create_time: _timestamp_pb2.Timestamp
    storage_volume: str
    type: VolumeSnapshot.SnapshotType

    def __init__(self, name: _Optional[str]=..., id: _Optional[str]=..., description: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., storage_volume: _Optional[str]=..., type: _Optional[_Union[VolumeSnapshot.SnapshotType, str]]=...) -> None:
        ...

class GetVolumeSnapshotRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListVolumeSnapshotsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListVolumeSnapshotsResponse(_message.Message):
    __slots__ = ('volume_snapshots', 'next_page_token', 'unreachable')
    VOLUME_SNAPSHOTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    volume_snapshots: _containers.RepeatedCompositeFieldContainer[VolumeSnapshot]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, volume_snapshots: _Optional[_Iterable[_Union[VolumeSnapshot, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class DeleteVolumeSnapshotRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateVolumeSnapshotRequest(_message.Message):
    __slots__ = ('parent', 'volume_snapshot')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    VOLUME_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    parent: str
    volume_snapshot: VolumeSnapshot

    def __init__(self, parent: _Optional[str]=..., volume_snapshot: _Optional[_Union[VolumeSnapshot, _Mapping]]=...) -> None:
        ...

class RestoreVolumeSnapshotRequest(_message.Message):
    __slots__ = ('volume_snapshot',)
    VOLUME_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    volume_snapshot: str

    def __init__(self, volume_snapshot: _Optional[str]=...) -> None:
        ...