from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class LocalServicesCreditStateEnum(_message.Message):
    __slots__ = ()

    class CreditState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[LocalServicesCreditStateEnum.CreditState]
        UNKNOWN: _ClassVar[LocalServicesCreditStateEnum.CreditState]
        PENDING: _ClassVar[LocalServicesCreditStateEnum.CreditState]
        CREDITED: _ClassVar[LocalServicesCreditStateEnum.CreditState]
    UNSPECIFIED: LocalServicesCreditStateEnum.CreditState
    UNKNOWN: LocalServicesCreditStateEnum.CreditState
    PENDING: LocalServicesCreditStateEnum.CreditState
    CREDITED: LocalServicesCreditStateEnum.CreditState

    def __init__(self) -> None:
        ...