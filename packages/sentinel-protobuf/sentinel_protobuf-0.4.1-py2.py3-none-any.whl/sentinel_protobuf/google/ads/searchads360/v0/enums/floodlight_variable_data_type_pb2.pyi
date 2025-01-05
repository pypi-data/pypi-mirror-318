from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class FloodlightVariableDataTypeEnum(_message.Message):
    __slots__ = ()

    class FloodlightVariableDataType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[FloodlightVariableDataTypeEnum.FloodlightVariableDataType]
        UNKNOWN: _ClassVar[FloodlightVariableDataTypeEnum.FloodlightVariableDataType]
        NUMBER: _ClassVar[FloodlightVariableDataTypeEnum.FloodlightVariableDataType]
        STRING: _ClassVar[FloodlightVariableDataTypeEnum.FloodlightVariableDataType]
    UNSPECIFIED: FloodlightVariableDataTypeEnum.FloodlightVariableDataType
    UNKNOWN: FloodlightVariableDataTypeEnum.FloodlightVariableDataType
    NUMBER: FloodlightVariableDataTypeEnum.FloodlightVariableDataType
    STRING: FloodlightVariableDataTypeEnum.FloodlightVariableDataType

    def __init__(self) -> None:
        ...