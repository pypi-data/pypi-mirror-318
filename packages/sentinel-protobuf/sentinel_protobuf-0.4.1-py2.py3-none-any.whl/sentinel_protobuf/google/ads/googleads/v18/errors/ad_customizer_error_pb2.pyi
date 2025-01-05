from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class AdCustomizerErrorEnum(_message.Message):
    __slots__ = ()

    class AdCustomizerError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[AdCustomizerErrorEnum.AdCustomizerError]
        UNKNOWN: _ClassVar[AdCustomizerErrorEnum.AdCustomizerError]
        COUNTDOWN_INVALID_DATE_FORMAT: _ClassVar[AdCustomizerErrorEnum.AdCustomizerError]
        COUNTDOWN_DATE_IN_PAST: _ClassVar[AdCustomizerErrorEnum.AdCustomizerError]
        COUNTDOWN_INVALID_LOCALE: _ClassVar[AdCustomizerErrorEnum.AdCustomizerError]
        COUNTDOWN_INVALID_START_DAYS_BEFORE: _ClassVar[AdCustomizerErrorEnum.AdCustomizerError]
        UNKNOWN_USER_LIST: _ClassVar[AdCustomizerErrorEnum.AdCustomizerError]
    UNSPECIFIED: AdCustomizerErrorEnum.AdCustomizerError
    UNKNOWN: AdCustomizerErrorEnum.AdCustomizerError
    COUNTDOWN_INVALID_DATE_FORMAT: AdCustomizerErrorEnum.AdCustomizerError
    COUNTDOWN_DATE_IN_PAST: AdCustomizerErrorEnum.AdCustomizerError
    COUNTDOWN_INVALID_LOCALE: AdCustomizerErrorEnum.AdCustomizerError
    COUNTDOWN_INVALID_START_DAYS_BEFORE: AdCustomizerErrorEnum.AdCustomizerError
    UNKNOWN_USER_LIST: AdCustomizerErrorEnum.AdCustomizerError

    def __init__(self) -> None:
        ...