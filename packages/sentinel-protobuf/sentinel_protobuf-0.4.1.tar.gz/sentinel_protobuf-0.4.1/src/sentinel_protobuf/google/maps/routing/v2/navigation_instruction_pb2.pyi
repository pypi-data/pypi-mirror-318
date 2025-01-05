from google.maps.routing.v2 import maneuver_pb2 as _maneuver_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class NavigationInstruction(_message.Message):
    __slots__ = ('maneuver', 'instructions')
    MANEUVER_FIELD_NUMBER: _ClassVar[int]
    INSTRUCTIONS_FIELD_NUMBER: _ClassVar[int]
    maneuver: _maneuver_pb2.Maneuver
    instructions: str

    def __init__(self, maneuver: _Optional[_Union[_maneuver_pb2.Maneuver, str]]=..., instructions: _Optional[str]=...) -> None:
        ...