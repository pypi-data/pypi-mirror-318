from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class SnapshotState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNKNOWN_SNAPSHOT_STATE: _ClassVar[SnapshotState]
    PENDING: _ClassVar[SnapshotState]
    RUNNING: _ClassVar[SnapshotState]
    READY: _ClassVar[SnapshotState]
    FAILED: _ClassVar[SnapshotState]
    DELETED: _ClassVar[SnapshotState]
UNKNOWN_SNAPSHOT_STATE: SnapshotState
PENDING: SnapshotState
RUNNING: SnapshotState
READY: SnapshotState
FAILED: SnapshotState
DELETED: SnapshotState

class PubsubSnapshotMetadata(_message.Message):
    __slots__ = ('topic_name', 'snapshot_name', 'expire_time')
    TOPIC_NAME_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_NAME_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
    topic_name: str
    snapshot_name: str
    expire_time: _timestamp_pb2.Timestamp

    def __init__(self, topic_name: _Optional[str]=..., snapshot_name: _Optional[str]=..., expire_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class Snapshot(_message.Message):
    __slots__ = ('id', 'project_id', 'source_job_id', 'creation_time', 'ttl', 'state', 'pubsub_metadata', 'description', 'disk_size_bytes', 'region')
    ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_JOB_ID_FIELD_NUMBER: _ClassVar[int]
    CREATION_TIME_FIELD_NUMBER: _ClassVar[int]
    TTL_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    PUBSUB_METADATA_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DISK_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    id: str
    project_id: str
    source_job_id: str
    creation_time: _timestamp_pb2.Timestamp
    ttl: _duration_pb2.Duration
    state: SnapshotState
    pubsub_metadata: _containers.RepeatedCompositeFieldContainer[PubsubSnapshotMetadata]
    description: str
    disk_size_bytes: int
    region: str

    def __init__(self, id: _Optional[str]=..., project_id: _Optional[str]=..., source_job_id: _Optional[str]=..., creation_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., ttl: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., state: _Optional[_Union[SnapshotState, str]]=..., pubsub_metadata: _Optional[_Iterable[_Union[PubsubSnapshotMetadata, _Mapping]]]=..., description: _Optional[str]=..., disk_size_bytes: _Optional[int]=..., region: _Optional[str]=...) -> None:
        ...

class GetSnapshotRequest(_message.Message):
    __slots__ = ('project_id', 'snapshot_id', 'location')
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_ID_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    snapshot_id: str
    location: str

    def __init__(self, project_id: _Optional[str]=..., snapshot_id: _Optional[str]=..., location: _Optional[str]=...) -> None:
        ...

class DeleteSnapshotRequest(_message.Message):
    __slots__ = ('project_id', 'snapshot_id', 'location')
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_ID_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    snapshot_id: str
    location: str

    def __init__(self, project_id: _Optional[str]=..., snapshot_id: _Optional[str]=..., location: _Optional[str]=...) -> None:
        ...

class DeleteSnapshotResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class ListSnapshotsRequest(_message.Message):
    __slots__ = ('project_id', 'job_id', 'location')
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    job_id: str
    location: str

    def __init__(self, project_id: _Optional[str]=..., job_id: _Optional[str]=..., location: _Optional[str]=...) -> None:
        ...

class ListSnapshotsResponse(_message.Message):
    __slots__ = ('snapshots',)
    SNAPSHOTS_FIELD_NUMBER: _ClassVar[int]
    snapshots: _containers.RepeatedCompositeFieldContainer[Snapshot]

    def __init__(self, snapshots: _Optional[_Iterable[_Union[Snapshot, _Mapping]]]=...) -> None:
        ...