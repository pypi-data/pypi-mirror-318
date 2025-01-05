from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class KnowledgeBase(_message.Message):
    __slots__ = ('name', 'display_name', 'language_code')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    language_code: str

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., language_code: _Optional[str]=...) -> None:
        ...

class ListKnowledgeBasesRequest(_message.Message):
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

class ListKnowledgeBasesResponse(_message.Message):
    __slots__ = ('knowledge_bases', 'next_page_token')
    KNOWLEDGE_BASES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    knowledge_bases: _containers.RepeatedCompositeFieldContainer[KnowledgeBase]
    next_page_token: str

    def __init__(self, knowledge_bases: _Optional[_Iterable[_Union[KnowledgeBase, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetKnowledgeBaseRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateKnowledgeBaseRequest(_message.Message):
    __slots__ = ('parent', 'knowledge_base')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    KNOWLEDGE_BASE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    knowledge_base: KnowledgeBase

    def __init__(self, parent: _Optional[str]=..., knowledge_base: _Optional[_Union[KnowledgeBase, _Mapping]]=...) -> None:
        ...

class DeleteKnowledgeBaseRequest(_message.Message):
    __slots__ = ('name', 'force')
    NAME_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    force: bool

    def __init__(self, name: _Optional[str]=..., force: bool=...) -> None:
        ...

class UpdateKnowledgeBaseRequest(_message.Message):
    __slots__ = ('knowledge_base', 'update_mask')
    KNOWLEDGE_BASE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    knowledge_base: KnowledgeBase
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, knowledge_base: _Optional[_Union[KnowledgeBase, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...