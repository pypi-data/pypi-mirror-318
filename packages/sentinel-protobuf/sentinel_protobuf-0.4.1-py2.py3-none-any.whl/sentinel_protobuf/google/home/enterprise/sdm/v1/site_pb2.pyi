from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Structure(_message.Message):
    __slots__ = ('name', 'traits')
    NAME_FIELD_NUMBER: _ClassVar[int]
    TRAITS_FIELD_NUMBER: _ClassVar[int]
    name: str
    traits: _struct_pb2.Struct

    def __init__(self, name: _Optional[str]=..., traits: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=...) -> None:
        ...

class Room(_message.Message):
    __slots__ = ('name', 'traits')
    NAME_FIELD_NUMBER: _ClassVar[int]
    TRAITS_FIELD_NUMBER: _ClassVar[int]
    name: str
    traits: _struct_pb2.Struct

    def __init__(self, name: _Optional[str]=..., traits: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=...) -> None:
        ...