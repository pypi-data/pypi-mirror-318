from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class LanguageCodeErrorEnum(_message.Message):
    __slots__ = ()

    class LanguageCodeError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[LanguageCodeErrorEnum.LanguageCodeError]
        UNKNOWN: _ClassVar[LanguageCodeErrorEnum.LanguageCodeError]
        LANGUAGE_CODE_NOT_FOUND: _ClassVar[LanguageCodeErrorEnum.LanguageCodeError]
        INVALID_LANGUAGE_CODE: _ClassVar[LanguageCodeErrorEnum.LanguageCodeError]
    UNSPECIFIED: LanguageCodeErrorEnum.LanguageCodeError
    UNKNOWN: LanguageCodeErrorEnum.LanguageCodeError
    LANGUAGE_CODE_NOT_FOUND: LanguageCodeErrorEnum.LanguageCodeError
    INVALID_LANGUAGE_CODE: LanguageCodeErrorEnum.LanguageCodeError

    def __init__(self) -> None:
        ...