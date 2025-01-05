from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class AdParameterErrorEnum(_message.Message):
    __slots__ = ()

    class AdParameterError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[AdParameterErrorEnum.AdParameterError]
        UNKNOWN: _ClassVar[AdParameterErrorEnum.AdParameterError]
        AD_GROUP_CRITERION_MUST_BE_KEYWORD: _ClassVar[AdParameterErrorEnum.AdParameterError]
        INVALID_INSERTION_TEXT_FORMAT: _ClassVar[AdParameterErrorEnum.AdParameterError]
    UNSPECIFIED: AdParameterErrorEnum.AdParameterError
    UNKNOWN: AdParameterErrorEnum.AdParameterError
    AD_GROUP_CRITERION_MUST_BE_KEYWORD: AdParameterErrorEnum.AdParameterError
    INVALID_INSERTION_TEXT_FORMAT: AdParameterErrorEnum.AdParameterError

    def __init__(self) -> None:
        ...