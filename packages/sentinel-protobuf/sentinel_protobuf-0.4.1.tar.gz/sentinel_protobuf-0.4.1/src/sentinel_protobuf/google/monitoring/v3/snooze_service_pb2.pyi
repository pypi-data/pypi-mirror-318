from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.monitoring.v3 import snooze_pb2 as _snooze_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CreateSnoozeRequest(_message.Message):
    __slots__ = ('parent', 'snooze')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SNOOZE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    snooze: _snooze_pb2.Snooze

    def __init__(self, parent: _Optional[str]=..., snooze: _Optional[_Union[_snooze_pb2.Snooze, _Mapping]]=...) -> None:
        ...

class ListSnoozesRequest(_message.Message):
    __slots__ = ('parent', 'filter', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., filter: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListSnoozesResponse(_message.Message):
    __slots__ = ('snoozes', 'next_page_token')
    SNOOZES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    snoozes: _containers.RepeatedCompositeFieldContainer[_snooze_pb2.Snooze]
    next_page_token: str

    def __init__(self, snoozes: _Optional[_Iterable[_Union[_snooze_pb2.Snooze, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetSnoozeRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateSnoozeRequest(_message.Message):
    __slots__ = ('snooze', 'update_mask')
    SNOOZE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    snooze: _snooze_pb2.Snooze
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, snooze: _Optional[_Union[_snooze_pb2.Snooze, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...