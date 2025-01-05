from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.contentwarehouse.v1 import synonymset_pb2 as _synonymset_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CreateSynonymSetRequest(_message.Message):
    __slots__ = ('parent', 'synonym_set')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SYNONYM_SET_FIELD_NUMBER: _ClassVar[int]
    parent: str
    synonym_set: _synonymset_pb2.SynonymSet

    def __init__(self, parent: _Optional[str]=..., synonym_set: _Optional[_Union[_synonymset_pb2.SynonymSet, _Mapping]]=...) -> None:
        ...

class GetSynonymSetRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListSynonymSetsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListSynonymSetsResponse(_message.Message):
    __slots__ = ('synonym_sets', 'next_page_token')
    SYNONYM_SETS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    synonym_sets: _containers.RepeatedCompositeFieldContainer[_synonymset_pb2.SynonymSet]
    next_page_token: str

    def __init__(self, synonym_sets: _Optional[_Iterable[_Union[_synonymset_pb2.SynonymSet, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class UpdateSynonymSetRequest(_message.Message):
    __slots__ = ('name', 'synonym_set')
    NAME_FIELD_NUMBER: _ClassVar[int]
    SYNONYM_SET_FIELD_NUMBER: _ClassVar[int]
    name: str
    synonym_set: _synonymset_pb2.SynonymSet

    def __init__(self, name: _Optional[str]=..., synonym_set: _Optional[_Union[_synonymset_pb2.SynonymSet, _Mapping]]=...) -> None:
        ...

class DeleteSynonymSetRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...