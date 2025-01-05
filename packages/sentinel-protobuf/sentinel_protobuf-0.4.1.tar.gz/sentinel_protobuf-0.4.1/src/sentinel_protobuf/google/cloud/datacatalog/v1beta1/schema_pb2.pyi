from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Schema(_message.Message):
    __slots__ = ('columns',)
    COLUMNS_FIELD_NUMBER: _ClassVar[int]
    columns: _containers.RepeatedCompositeFieldContainer[ColumnSchema]

    def __init__(self, columns: _Optional[_Iterable[_Union[ColumnSchema, _Mapping]]]=...) -> None:
        ...

class ColumnSchema(_message.Message):
    __slots__ = ('column', 'type', 'description', 'mode', 'subcolumns')
    COLUMN_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    SUBCOLUMNS_FIELD_NUMBER: _ClassVar[int]
    column: str
    type: str
    description: str
    mode: str
    subcolumns: _containers.RepeatedCompositeFieldContainer[ColumnSchema]

    def __init__(self, column: _Optional[str]=..., type: _Optional[str]=..., description: _Optional[str]=..., mode: _Optional[str]=..., subcolumns: _Optional[_Iterable[_Union[ColumnSchema, _Mapping]]]=...) -> None:
        ...