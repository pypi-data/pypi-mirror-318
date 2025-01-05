from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class EntitySet(_message.Message):
    __slots__ = ('entities',)

    class Entity(_message.Message):
        __slots__ = ('id',)
        ID_FIELD_NUMBER: _ClassVar[int]
        id: str

        def __init__(self, id: _Optional[str]=...) -> None:
            ...
    ENTITIES_FIELD_NUMBER: _ClassVar[int]
    entities: _containers.RepeatedCompositeFieldContainer[EntitySet.Entity]

    def __init__(self, entities: _Optional[_Iterable[_Union[EntitySet.Entity, _Mapping]]]=...) -> None:
        ...