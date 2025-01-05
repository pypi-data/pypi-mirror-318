from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class GetGlobalSettingsRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class Settings(_message.Message):
    __slots__ = ('name', 'vpcsc', 'payg')
    NAME_FIELD_NUMBER: _ClassVar[int]
    VPCSC_FIELD_NUMBER: _ClassVar[int]
    PAYG_FIELD_NUMBER: _ClassVar[int]
    name: str
    vpcsc: bool
    payg: bool

    def __init__(self, name: _Optional[str]=..., vpcsc: bool=..., payg: bool=...) -> None:
        ...