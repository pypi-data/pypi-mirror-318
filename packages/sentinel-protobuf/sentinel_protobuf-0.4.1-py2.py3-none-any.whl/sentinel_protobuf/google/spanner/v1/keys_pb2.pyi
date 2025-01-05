from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class KeyRange(_message.Message):
    __slots__ = ('start_closed', 'start_open', 'end_closed', 'end_open')
    START_CLOSED_FIELD_NUMBER: _ClassVar[int]
    START_OPEN_FIELD_NUMBER: _ClassVar[int]
    END_CLOSED_FIELD_NUMBER: _ClassVar[int]
    END_OPEN_FIELD_NUMBER: _ClassVar[int]
    start_closed: _struct_pb2.ListValue
    start_open: _struct_pb2.ListValue
    end_closed: _struct_pb2.ListValue
    end_open: _struct_pb2.ListValue

    def __init__(self, start_closed: _Optional[_Union[_struct_pb2.ListValue, _Mapping]]=..., start_open: _Optional[_Union[_struct_pb2.ListValue, _Mapping]]=..., end_closed: _Optional[_Union[_struct_pb2.ListValue, _Mapping]]=..., end_open: _Optional[_Union[_struct_pb2.ListValue, _Mapping]]=...) -> None:
        ...

class KeySet(_message.Message):
    __slots__ = ('keys', 'ranges', 'all')
    KEYS_FIELD_NUMBER: _ClassVar[int]
    RANGES_FIELD_NUMBER: _ClassVar[int]
    ALL_FIELD_NUMBER: _ClassVar[int]
    keys: _containers.RepeatedCompositeFieldContainer[_struct_pb2.ListValue]
    ranges: _containers.RepeatedCompositeFieldContainer[KeyRange]
    all: bool

    def __init__(self, keys: _Optional[_Iterable[_Union[_struct_pb2.ListValue, _Mapping]]]=..., ranges: _Optional[_Iterable[_Union[KeyRange, _Mapping]]]=..., all: bool=...) -> None:
        ...