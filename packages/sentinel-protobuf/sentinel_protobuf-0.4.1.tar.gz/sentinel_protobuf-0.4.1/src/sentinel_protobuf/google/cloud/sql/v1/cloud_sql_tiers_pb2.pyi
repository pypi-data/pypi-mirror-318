from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class SqlTiersListRequest(_message.Message):
    __slots__ = ('project',)
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    project: str

    def __init__(self, project: _Optional[str]=...) -> None:
        ...

class TiersListResponse(_message.Message):
    __slots__ = ('kind', 'items')
    KIND_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    kind: str
    items: _containers.RepeatedCompositeFieldContainer[Tier]

    def __init__(self, kind: _Optional[str]=..., items: _Optional[_Iterable[_Union[Tier, _Mapping]]]=...) -> None:
        ...

class Tier(_message.Message):
    __slots__ = ('tier', 'RAM', 'kind', 'Disk_Quota', 'region')
    TIER_FIELD_NUMBER: _ClassVar[int]
    RAM_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    DISK_QUOTA_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    tier: str
    RAM: int
    kind: str
    Disk_Quota: int
    region: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, tier: _Optional[str]=..., RAM: _Optional[int]=..., kind: _Optional[str]=..., Disk_Quota: _Optional[int]=..., region: _Optional[_Iterable[str]]=...) -> None:
        ...