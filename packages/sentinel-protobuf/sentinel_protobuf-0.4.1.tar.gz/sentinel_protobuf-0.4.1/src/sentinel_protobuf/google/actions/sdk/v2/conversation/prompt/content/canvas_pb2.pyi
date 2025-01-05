from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Canvas(_message.Message):
    __slots__ = ('url', 'data', 'suppress_mic', 'enable_full_screen')
    URL_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    SUPPRESS_MIC_FIELD_NUMBER: _ClassVar[int]
    ENABLE_FULL_SCREEN_FIELD_NUMBER: _ClassVar[int]
    url: str
    data: _containers.RepeatedCompositeFieldContainer[_struct_pb2.Value]
    suppress_mic: bool
    enable_full_screen: bool

    def __init__(self, url: _Optional[str]=..., data: _Optional[_Iterable[_Union[_struct_pb2.Value, _Mapping]]]=..., suppress_mic: bool=..., enable_full_screen: bool=...) -> None:
        ...