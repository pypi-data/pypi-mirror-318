from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class CurrencyCodeErrorEnum(_message.Message):
    __slots__ = ()

    class CurrencyCodeError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[CurrencyCodeErrorEnum.CurrencyCodeError]
        UNKNOWN: _ClassVar[CurrencyCodeErrorEnum.CurrencyCodeError]
        UNSUPPORTED: _ClassVar[CurrencyCodeErrorEnum.CurrencyCodeError]
    UNSPECIFIED: CurrencyCodeErrorEnum.CurrencyCodeError
    UNKNOWN: CurrencyCodeErrorEnum.CurrencyCodeError
    UNSUPPORTED: CurrencyCodeErrorEnum.CurrencyCodeError

    def __init__(self) -> None:
        ...