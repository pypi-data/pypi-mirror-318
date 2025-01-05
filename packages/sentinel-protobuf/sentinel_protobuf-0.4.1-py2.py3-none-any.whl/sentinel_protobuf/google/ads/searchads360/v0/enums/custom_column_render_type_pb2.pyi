from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class CustomColumnRenderTypeEnum(_message.Message):
    __slots__ = ()

    class CustomColumnRenderType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[CustomColumnRenderTypeEnum.CustomColumnRenderType]
        UNKNOWN: _ClassVar[CustomColumnRenderTypeEnum.CustomColumnRenderType]
        NUMBER: _ClassVar[CustomColumnRenderTypeEnum.CustomColumnRenderType]
        PERCENT: _ClassVar[CustomColumnRenderTypeEnum.CustomColumnRenderType]
        MONEY: _ClassVar[CustomColumnRenderTypeEnum.CustomColumnRenderType]
        STRING: _ClassVar[CustomColumnRenderTypeEnum.CustomColumnRenderType]
        BOOLEAN: _ClassVar[CustomColumnRenderTypeEnum.CustomColumnRenderType]
        DATE: _ClassVar[CustomColumnRenderTypeEnum.CustomColumnRenderType]
    UNSPECIFIED: CustomColumnRenderTypeEnum.CustomColumnRenderType
    UNKNOWN: CustomColumnRenderTypeEnum.CustomColumnRenderType
    NUMBER: CustomColumnRenderTypeEnum.CustomColumnRenderType
    PERCENT: CustomColumnRenderTypeEnum.CustomColumnRenderType
    MONEY: CustomColumnRenderTypeEnum.CustomColumnRenderType
    STRING: CustomColumnRenderTypeEnum.CustomColumnRenderType
    BOOLEAN: CustomColumnRenderTypeEnum.CustomColumnRenderType
    DATE: CustomColumnRenderTypeEnum.CustomColumnRenderType

    def __init__(self) -> None:
        ...