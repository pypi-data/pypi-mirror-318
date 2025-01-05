from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Vertex(_message.Message):
    __slots__ = ('x', 'y')
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    x: int
    y: int

    def __init__(self, x: _Optional[int]=..., y: _Optional[int]=...) -> None:
        ...

class BoundingPoly(_message.Message):
    __slots__ = ('vertices',)
    VERTICES_FIELD_NUMBER: _ClassVar[int]
    vertices: _containers.RepeatedCompositeFieldContainer[Vertex]

    def __init__(self, vertices: _Optional[_Iterable[_Union[Vertex, _Mapping]]]=...) -> None:
        ...

class Position(_message.Message):
    __slots__ = ('x', 'y', 'z')
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    Z_FIELD_NUMBER: _ClassVar[int]
    x: float
    y: float
    z: float

    def __init__(self, x: _Optional[float]=..., y: _Optional[float]=..., z: _Optional[float]=...) -> None:
        ...