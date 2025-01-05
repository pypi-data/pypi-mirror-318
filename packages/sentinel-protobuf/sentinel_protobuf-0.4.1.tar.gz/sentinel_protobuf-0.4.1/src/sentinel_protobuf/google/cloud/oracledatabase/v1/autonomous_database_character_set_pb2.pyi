from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class AutonomousDatabaseCharacterSet(_message.Message):
    __slots__ = ('name', 'character_set_type', 'character_set')

    class CharacterSetType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CHARACTER_SET_TYPE_UNSPECIFIED: _ClassVar[AutonomousDatabaseCharacterSet.CharacterSetType]
        DATABASE: _ClassVar[AutonomousDatabaseCharacterSet.CharacterSetType]
        NATIONAL: _ClassVar[AutonomousDatabaseCharacterSet.CharacterSetType]
    CHARACTER_SET_TYPE_UNSPECIFIED: AutonomousDatabaseCharacterSet.CharacterSetType
    DATABASE: AutonomousDatabaseCharacterSet.CharacterSetType
    NATIONAL: AutonomousDatabaseCharacterSet.CharacterSetType
    NAME_FIELD_NUMBER: _ClassVar[int]
    CHARACTER_SET_TYPE_FIELD_NUMBER: _ClassVar[int]
    CHARACTER_SET_FIELD_NUMBER: _ClassVar[int]
    name: str
    character_set_type: AutonomousDatabaseCharacterSet.CharacterSetType
    character_set: str

    def __init__(self, name: _Optional[str]=..., character_set_type: _Optional[_Union[AutonomousDatabaseCharacterSet.CharacterSetType, str]]=..., character_set: _Optional[str]=...) -> None:
        ...