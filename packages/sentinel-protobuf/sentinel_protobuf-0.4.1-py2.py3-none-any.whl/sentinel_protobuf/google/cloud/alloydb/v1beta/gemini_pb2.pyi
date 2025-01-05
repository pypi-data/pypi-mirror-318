from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class GeminiClusterConfig(_message.Message):
    __slots__ = ('entitled',)
    ENTITLED_FIELD_NUMBER: _ClassVar[int]
    entitled: bool

    def __init__(self, entitled: bool=...) -> None:
        ...

class GeminiInstanceConfig(_message.Message):
    __slots__ = ('entitled',)
    ENTITLED_FIELD_NUMBER: _ClassVar[int]
    entitled: bool

    def __init__(self, entitled: bool=...) -> None:
        ...