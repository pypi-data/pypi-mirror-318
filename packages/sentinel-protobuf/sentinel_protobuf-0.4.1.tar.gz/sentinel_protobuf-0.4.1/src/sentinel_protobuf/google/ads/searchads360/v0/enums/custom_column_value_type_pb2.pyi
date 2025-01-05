from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class CustomColumnValueTypeEnum(_message.Message):
    __slots__ = ()

    class CustomColumnValueType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[CustomColumnValueTypeEnum.CustomColumnValueType]
        UNKNOWN: _ClassVar[CustomColumnValueTypeEnum.CustomColumnValueType]
        STRING: _ClassVar[CustomColumnValueTypeEnum.CustomColumnValueType]
        INT64: _ClassVar[CustomColumnValueTypeEnum.CustomColumnValueType]
        DOUBLE: _ClassVar[CustomColumnValueTypeEnum.CustomColumnValueType]
        BOOLEAN: _ClassVar[CustomColumnValueTypeEnum.CustomColumnValueType]
        DATE: _ClassVar[CustomColumnValueTypeEnum.CustomColumnValueType]
    UNSPECIFIED: CustomColumnValueTypeEnum.CustomColumnValueType
    UNKNOWN: CustomColumnValueTypeEnum.CustomColumnValueType
    STRING: CustomColumnValueTypeEnum.CustomColumnValueType
    INT64: CustomColumnValueTypeEnum.CustomColumnValueType
    DOUBLE: CustomColumnValueTypeEnum.CustomColumnValueType
    BOOLEAN: CustomColumnValueTypeEnum.CustomColumnValueType
    DATE: CustomColumnValueTypeEnum.CustomColumnValueType

    def __init__(self) -> None:
        ...