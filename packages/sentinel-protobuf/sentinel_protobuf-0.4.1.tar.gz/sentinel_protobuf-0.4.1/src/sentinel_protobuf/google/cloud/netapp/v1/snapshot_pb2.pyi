from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ListSnapshotsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'order_by', 'filter')
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

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., order_by: _Optional[str]=..., filter: _Optional[str]=...) -> None:
        ...

class ListSnapshotsResponse(_message.Message):
    __slots__ = ('snapshots', 'next_page_token', 'unreachable')
    SNAPSHOTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    snapshots: _containers.RepeatedCompositeFieldContainer[Snapshot]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, snapshots: _Optional[_Iterable[_Union[Snapshot, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetSnapshotRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateSnapshotRequest(_message.Message):
    __slots__ = ('parent', 'snapshot', 'snapshot_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    snapshot: Snapshot
    snapshot_id: str

    def __init__(self, parent: _Optional[str]=..., snapshot: _Optional[_Union[Snapshot, _Mapping]]=..., snapshot_id: _Optional[str]=...) -> None:
        ...

class DeleteSnapshotRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateSnapshotRequest(_message.Message):
    __slots__ = ('update_mask', 'snapshot')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    snapshot: Snapshot

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., snapshot: _Optional[_Union[Snapshot, _Mapping]]=...) -> None:
        ...

class Snapshot(_message.Message):
    __slots__ = ('name', 'state', 'state_details', 'description', 'used_bytes', 'create_time', 'labels')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Snapshot.State]
        READY: _ClassVar[Snapshot.State]
        CREATING: _ClassVar[Snapshot.State]
        DELETING: _ClassVar[Snapshot.State]
        UPDATING: _ClassVar[Snapshot.State]
        DISABLED: _ClassVar[Snapshot.State]
        ERROR: _ClassVar[Snapshot.State]
    STATE_UNSPECIFIED: Snapshot.State
    READY: Snapshot.State
    CREATING: Snapshot.State
    DELETING: Snapshot.State
    UPDATING: Snapshot.State
    DISABLED: Snapshot.State
    ERROR: Snapshot.State

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATE_DETAILS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    USED_BYTES_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    name: str
    state: Snapshot.State
    state_details: str
    description: str
    used_bytes: float
    create_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]

    def __init__(self, name: _Optional[str]=..., state: _Optional[_Union[Snapshot.State, str]]=..., state_details: _Optional[str]=..., description: _Optional[str]=..., used_bytes: _Optional[float]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=...) -> None:
        ...