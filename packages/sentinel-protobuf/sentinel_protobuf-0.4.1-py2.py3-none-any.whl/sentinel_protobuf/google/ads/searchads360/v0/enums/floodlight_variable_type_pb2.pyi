from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class FloodlightVariableTypeEnum(_message.Message):
    __slots__ = ()

    class FloodlightVariableType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[FloodlightVariableTypeEnum.FloodlightVariableType]
        UNKNOWN: _ClassVar[FloodlightVariableTypeEnum.FloodlightVariableType]
        DIMENSION: _ClassVar[FloodlightVariableTypeEnum.FloodlightVariableType]
        METRIC: _ClassVar[FloodlightVariableTypeEnum.FloodlightVariableType]
        UNSET: _ClassVar[FloodlightVariableTypeEnum.FloodlightVariableType]
    UNSPECIFIED: FloodlightVariableTypeEnum.FloodlightVariableType
    UNKNOWN: FloodlightVariableTypeEnum.FloodlightVariableType
    DIMENSION: FloodlightVariableTypeEnum.FloodlightVariableType
    METRIC: FloodlightVariableTypeEnum.FloodlightVariableType
    UNSET: FloodlightVariableTypeEnum.FloodlightVariableType

    def __init__(self) -> None:
        ...