from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class SpendingLimitTypeEnum(_message.Message):
    __slots__ = ()

    class SpendingLimitType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[SpendingLimitTypeEnum.SpendingLimitType]
        UNKNOWN: _ClassVar[SpendingLimitTypeEnum.SpendingLimitType]
        INFINITE: _ClassVar[SpendingLimitTypeEnum.SpendingLimitType]
    UNSPECIFIED: SpendingLimitTypeEnum.SpendingLimitType
    UNKNOWN: SpendingLimitTypeEnum.SpendingLimitType
    INFINITE: SpendingLimitTypeEnum.SpendingLimitType

    def __init__(self) -> None:
        ...