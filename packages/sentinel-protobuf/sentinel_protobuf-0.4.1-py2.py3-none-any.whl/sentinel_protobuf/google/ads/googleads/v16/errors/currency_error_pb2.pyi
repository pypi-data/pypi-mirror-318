from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class CurrencyErrorEnum(_message.Message):
    __slots__ = ()

    class CurrencyError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[CurrencyErrorEnum.CurrencyError]
        UNKNOWN: _ClassVar[CurrencyErrorEnum.CurrencyError]
        VALUE_NOT_MULTIPLE_OF_BILLABLE_UNIT: _ClassVar[CurrencyErrorEnum.CurrencyError]
    UNSPECIFIED: CurrencyErrorEnum.CurrencyError
    UNKNOWN: CurrencyErrorEnum.CurrencyError
    VALUE_NOT_MULTIPLE_OF_BILLABLE_UNIT: CurrencyErrorEnum.CurrencyError

    def __init__(self) -> None:
        ...