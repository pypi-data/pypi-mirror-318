from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class UserDataErrorEnum(_message.Message):
    __slots__ = ()

    class UserDataError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[UserDataErrorEnum.UserDataError]
        UNKNOWN: _ClassVar[UserDataErrorEnum.UserDataError]
        OPERATIONS_FOR_CUSTOMER_MATCH_NOT_ALLOWED: _ClassVar[UserDataErrorEnum.UserDataError]
        TOO_MANY_USER_IDENTIFIERS: _ClassVar[UserDataErrorEnum.UserDataError]
        USER_LIST_NOT_APPLICABLE: _ClassVar[UserDataErrorEnum.UserDataError]
    UNSPECIFIED: UserDataErrorEnum.UserDataError
    UNKNOWN: UserDataErrorEnum.UserDataError
    OPERATIONS_FOR_CUSTOMER_MATCH_NOT_ALLOWED: UserDataErrorEnum.UserDataError
    TOO_MANY_USER_IDENTIFIERS: UserDataErrorEnum.UserDataError
    USER_LIST_NOT_APPLICABLE: UserDataErrorEnum.UserDataError

    def __init__(self) -> None:
        ...