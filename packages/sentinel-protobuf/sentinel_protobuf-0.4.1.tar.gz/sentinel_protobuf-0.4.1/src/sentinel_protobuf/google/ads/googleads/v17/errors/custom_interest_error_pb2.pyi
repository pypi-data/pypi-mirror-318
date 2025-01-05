from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class CustomInterestErrorEnum(_message.Message):
    __slots__ = ()

    class CustomInterestError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[CustomInterestErrorEnum.CustomInterestError]
        UNKNOWN: _ClassVar[CustomInterestErrorEnum.CustomInterestError]
        NAME_ALREADY_USED: _ClassVar[CustomInterestErrorEnum.CustomInterestError]
        CUSTOM_INTEREST_MEMBER_ID_AND_TYPE_PARAMETER_NOT_PRESENT_IN_REMOVE: _ClassVar[CustomInterestErrorEnum.CustomInterestError]
        TYPE_AND_PARAMETER_NOT_FOUND: _ClassVar[CustomInterestErrorEnum.CustomInterestError]
        TYPE_AND_PARAMETER_ALREADY_EXISTED: _ClassVar[CustomInterestErrorEnum.CustomInterestError]
        INVALID_CUSTOM_INTEREST_MEMBER_TYPE: _ClassVar[CustomInterestErrorEnum.CustomInterestError]
        CANNOT_REMOVE_WHILE_IN_USE: _ClassVar[CustomInterestErrorEnum.CustomInterestError]
        CANNOT_CHANGE_TYPE: _ClassVar[CustomInterestErrorEnum.CustomInterestError]
    UNSPECIFIED: CustomInterestErrorEnum.CustomInterestError
    UNKNOWN: CustomInterestErrorEnum.CustomInterestError
    NAME_ALREADY_USED: CustomInterestErrorEnum.CustomInterestError
    CUSTOM_INTEREST_MEMBER_ID_AND_TYPE_PARAMETER_NOT_PRESENT_IN_REMOVE: CustomInterestErrorEnum.CustomInterestError
    TYPE_AND_PARAMETER_NOT_FOUND: CustomInterestErrorEnum.CustomInterestError
    TYPE_AND_PARAMETER_ALREADY_EXISTED: CustomInterestErrorEnum.CustomInterestError
    INVALID_CUSTOM_INTEREST_MEMBER_TYPE: CustomInterestErrorEnum.CustomInterestError
    CANNOT_REMOVE_WHILE_IN_USE: CustomInterestErrorEnum.CustomInterestError
    CANNOT_CHANGE_TYPE: CustomInterestErrorEnum.CustomInterestError

    def __init__(self) -> None:
        ...