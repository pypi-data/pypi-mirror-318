from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class CustomerErrorEnum(_message.Message):
    __slots__ = ()

    class CustomerError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[CustomerErrorEnum.CustomerError]
        UNKNOWN: _ClassVar[CustomerErrorEnum.CustomerError]
        STATUS_CHANGE_DISALLOWED: _ClassVar[CustomerErrorEnum.CustomerError]
        ACCOUNT_NOT_SET_UP: _ClassVar[CustomerErrorEnum.CustomerError]
    UNSPECIFIED: CustomerErrorEnum.CustomerError
    UNKNOWN: CustomerErrorEnum.CustomerError
    STATUS_CHANGE_DISALLOWED: CustomerErrorEnum.CustomerError
    ACCOUNT_NOT_SET_UP: CustomerErrorEnum.CustomerError

    def __init__(self) -> None:
        ...