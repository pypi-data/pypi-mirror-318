from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Context(_message.Message):
    __slots__ = ('name', 'lifespan_count', 'parameters')
    NAME_FIELD_NUMBER: _ClassVar[int]
    LIFESPAN_COUNT_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    name: str
    lifespan_count: int
    parameters: _struct_pb2.Struct

    def __init__(self, name: _Optional[str]=..., lifespan_count: _Optional[int]=..., parameters: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=...) -> None:
        ...

class ListContextsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListContextsResponse(_message.Message):
    __slots__ = ('contexts', 'next_page_token')
    CONTEXTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    contexts: _containers.RepeatedCompositeFieldContainer[Context]
    next_page_token: str

    def __init__(self, contexts: _Optional[_Iterable[_Union[Context, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetContextRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateContextRequest(_message.Message):
    __slots__ = ('parent', 'context')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    parent: str
    context: Context

    def __init__(self, parent: _Optional[str]=..., context: _Optional[_Union[Context, _Mapping]]=...) -> None:
        ...

class UpdateContextRequest(_message.Message):
    __slots__ = ('context', 'update_mask')
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    context: Context
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, context: _Optional[_Union[Context, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteContextRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class DeleteAllContextsRequest(_message.Message):
    __slots__ = ('parent',)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: str

    def __init__(self, parent: _Optional[str]=...) -> None:
        ...