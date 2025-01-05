from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Device(_message.Message):
    __slots__ = ('name', 'type', 'traits', 'parent_relations')
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    TRAITS_FIELD_NUMBER: _ClassVar[int]
    PARENT_RELATIONS_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: str
    traits: _struct_pb2.Struct
    parent_relations: _containers.RepeatedCompositeFieldContainer[ParentRelation]

    def __init__(self, name: _Optional[str]=..., type: _Optional[str]=..., traits: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=..., parent_relations: _Optional[_Iterable[_Union[ParentRelation, _Mapping]]]=...) -> None:
        ...

class ParentRelation(_message.Message):
    __slots__ = ('parent', 'display_name')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    parent: str
    display_name: str

    def __init__(self, parent: _Optional[str]=..., display_name: _Optional[str]=...) -> None:
        ...