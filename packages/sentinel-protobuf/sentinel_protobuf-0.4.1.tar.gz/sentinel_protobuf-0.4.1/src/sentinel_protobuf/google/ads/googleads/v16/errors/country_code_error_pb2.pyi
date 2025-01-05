from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class CountryCodeErrorEnum(_message.Message):
    __slots__ = ()

    class CountryCodeError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[CountryCodeErrorEnum.CountryCodeError]
        UNKNOWN: _ClassVar[CountryCodeErrorEnum.CountryCodeError]
        INVALID_COUNTRY_CODE: _ClassVar[CountryCodeErrorEnum.CountryCodeError]
    UNSPECIFIED: CountryCodeErrorEnum.CountryCodeError
    UNKNOWN: CountryCodeErrorEnum.CountryCodeError
    INVALID_COUNTRY_CODE: CountryCodeErrorEnum.CountryCodeError

    def __init__(self) -> None:
        ...