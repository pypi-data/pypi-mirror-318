from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class TagHold(_message.Message):
    __slots__ = ('name', 'holder', 'origin', 'help_link', 'create_time')
    NAME_FIELD_NUMBER: _ClassVar[int]
    HOLDER_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    HELP_LINK_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    holder: str
    origin: str
    help_link: str
    create_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., holder: _Optional[str]=..., origin: _Optional[str]=..., help_link: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class CreateTagHoldRequest(_message.Message):
    __slots__ = ('parent', 'tag_hold', 'validate_only')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TAG_HOLD_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    tag_hold: TagHold
    validate_only: bool

    def __init__(self, parent: _Optional[str]=..., tag_hold: _Optional[_Union[TagHold, _Mapping]]=..., validate_only: bool=...) -> None:
        ...

class CreateTagHoldMetadata(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class DeleteTagHoldRequest(_message.Message):
    __slots__ = ('name', 'validate_only')
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    name: str
    validate_only: bool

    def __init__(self, name: _Optional[str]=..., validate_only: bool=...) -> None:
        ...

class DeleteTagHoldMetadata(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class ListTagHoldsRequest(_message.Message):
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

class ListTagHoldsResponse(_message.Message):
    __slots__ = ('tag_holds', 'next_page_token')
    TAG_HOLDS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    tag_holds: _containers.RepeatedCompositeFieldContainer[TagHold]
    next_page_token: str

    def __init__(self, tag_holds: _Optional[_Iterable[_Union[TagHold, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...