from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class CustomizerAttributeTypeEnum(_message.Message):
    __slots__ = ()

    class CustomizerAttributeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[CustomizerAttributeTypeEnum.CustomizerAttributeType]
        UNKNOWN: _ClassVar[CustomizerAttributeTypeEnum.CustomizerAttributeType]
        TEXT: _ClassVar[CustomizerAttributeTypeEnum.CustomizerAttributeType]
        NUMBER: _ClassVar[CustomizerAttributeTypeEnum.CustomizerAttributeType]
        PRICE: _ClassVar[CustomizerAttributeTypeEnum.CustomizerAttributeType]
        PERCENT: _ClassVar[CustomizerAttributeTypeEnum.CustomizerAttributeType]
    UNSPECIFIED: CustomizerAttributeTypeEnum.CustomizerAttributeType
    UNKNOWN: CustomizerAttributeTypeEnum.CustomizerAttributeType
    TEXT: CustomizerAttributeTypeEnum.CustomizerAttributeType
    NUMBER: CustomizerAttributeTypeEnum.CustomizerAttributeType
    PRICE: CustomizerAttributeTypeEnum.CustomizerAttributeType
    PERCENT: CustomizerAttributeTypeEnum.CustomizerAttributeType

    def __init__(self) -> None:
        ...