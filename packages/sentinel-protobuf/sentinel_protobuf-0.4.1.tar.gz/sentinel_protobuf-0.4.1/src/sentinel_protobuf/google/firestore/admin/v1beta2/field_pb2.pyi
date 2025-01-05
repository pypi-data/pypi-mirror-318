from google.firestore.admin.v1beta2 import index_pb2 as _index_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Field(_message.Message):
    __slots__ = ('name', 'index_config')

    class IndexConfig(_message.Message):
        __slots__ = ('indexes', 'uses_ancestor_config', 'ancestor_field', 'reverting')
        INDEXES_FIELD_NUMBER: _ClassVar[int]
        USES_ANCESTOR_CONFIG_FIELD_NUMBER: _ClassVar[int]
        ANCESTOR_FIELD_FIELD_NUMBER: _ClassVar[int]
        REVERTING_FIELD_NUMBER: _ClassVar[int]
        indexes: _containers.RepeatedCompositeFieldContainer[_index_pb2.Index]
        uses_ancestor_config: bool
        ancestor_field: str
        reverting: bool

        def __init__(self, indexes: _Optional[_Iterable[_Union[_index_pb2.Index, _Mapping]]]=..., uses_ancestor_config: bool=..., ancestor_field: _Optional[str]=..., reverting: bool=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    INDEX_CONFIG_FIELD_NUMBER: _ClassVar[int]
    name: str
    index_config: Field.IndexConfig

    def __init__(self, name: _Optional[str]=..., index_config: _Optional[_Union[Field.IndexConfig, _Mapping]]=...) -> None:
        ...