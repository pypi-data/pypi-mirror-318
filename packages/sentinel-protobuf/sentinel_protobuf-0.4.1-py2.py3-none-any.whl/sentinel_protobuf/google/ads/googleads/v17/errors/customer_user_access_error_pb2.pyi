from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class CustomerUserAccessErrorEnum(_message.Message):
    __slots__ = ()

    class CustomerUserAccessError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[CustomerUserAccessErrorEnum.CustomerUserAccessError]
        UNKNOWN: _ClassVar[CustomerUserAccessErrorEnum.CustomerUserAccessError]
        INVALID_USER_ID: _ClassVar[CustomerUserAccessErrorEnum.CustomerUserAccessError]
        REMOVAL_DISALLOWED: _ClassVar[CustomerUserAccessErrorEnum.CustomerUserAccessError]
        DISALLOWED_ACCESS_ROLE: _ClassVar[CustomerUserAccessErrorEnum.CustomerUserAccessError]
        LAST_ADMIN_USER_OF_SERVING_CUSTOMER: _ClassVar[CustomerUserAccessErrorEnum.CustomerUserAccessError]
        LAST_ADMIN_USER_OF_MANAGER: _ClassVar[CustomerUserAccessErrorEnum.CustomerUserAccessError]
    UNSPECIFIED: CustomerUserAccessErrorEnum.CustomerUserAccessError
    UNKNOWN: CustomerUserAccessErrorEnum.CustomerUserAccessError
    INVALID_USER_ID: CustomerUserAccessErrorEnum.CustomerUserAccessError
    REMOVAL_DISALLOWED: CustomerUserAccessErrorEnum.CustomerUserAccessError
    DISALLOWED_ACCESS_ROLE: CustomerUserAccessErrorEnum.CustomerUserAccessError
    LAST_ADMIN_USER_OF_SERVING_CUSTOMER: CustomerUserAccessErrorEnum.CustomerUserAccessError
    LAST_ADMIN_USER_OF_MANAGER: CustomerUserAccessErrorEnum.CustomerUserAccessError

    def __init__(self) -> None:
        ...