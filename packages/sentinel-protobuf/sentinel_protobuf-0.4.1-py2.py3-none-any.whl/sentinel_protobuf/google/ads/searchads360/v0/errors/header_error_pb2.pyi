from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class HeaderErrorEnum(_message.Message):
    __slots__ = ()

    class HeaderError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[HeaderErrorEnum.HeaderError]
        UNKNOWN: _ClassVar[HeaderErrorEnum.HeaderError]
        INVALID_USER_SELECTED_CUSTOMER_ID: _ClassVar[HeaderErrorEnum.HeaderError]
        INVALID_LOGIN_CUSTOMER_ID: _ClassVar[HeaderErrorEnum.HeaderError]
    UNSPECIFIED: HeaderErrorEnum.HeaderError
    UNKNOWN: HeaderErrorEnum.HeaderError
    INVALID_USER_SELECTED_CUSTOMER_ID: HeaderErrorEnum.HeaderError
    INVALID_LOGIN_CUSTOMER_ID: HeaderErrorEnum.HeaderError

    def __init__(self) -> None:
        ...