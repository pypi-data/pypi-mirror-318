from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class CustomerClientLinkErrorEnum(_message.Message):
    __slots__ = ()

    class CustomerClientLinkError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[CustomerClientLinkErrorEnum.CustomerClientLinkError]
        UNKNOWN: _ClassVar[CustomerClientLinkErrorEnum.CustomerClientLinkError]
        CLIENT_ALREADY_INVITED_BY_THIS_MANAGER: _ClassVar[CustomerClientLinkErrorEnum.CustomerClientLinkError]
        CLIENT_ALREADY_MANAGED_IN_HIERARCHY: _ClassVar[CustomerClientLinkErrorEnum.CustomerClientLinkError]
        CYCLIC_LINK_NOT_ALLOWED: _ClassVar[CustomerClientLinkErrorEnum.CustomerClientLinkError]
        CUSTOMER_HAS_TOO_MANY_ACCOUNTS: _ClassVar[CustomerClientLinkErrorEnum.CustomerClientLinkError]
        CLIENT_HAS_TOO_MANY_INVITATIONS: _ClassVar[CustomerClientLinkErrorEnum.CustomerClientLinkError]
        CANNOT_HIDE_OR_UNHIDE_MANAGER_ACCOUNTS: _ClassVar[CustomerClientLinkErrorEnum.CustomerClientLinkError]
        CUSTOMER_HAS_TOO_MANY_ACCOUNTS_AT_MANAGER: _ClassVar[CustomerClientLinkErrorEnum.CustomerClientLinkError]
        CLIENT_HAS_TOO_MANY_MANAGERS: _ClassVar[CustomerClientLinkErrorEnum.CustomerClientLinkError]
    UNSPECIFIED: CustomerClientLinkErrorEnum.CustomerClientLinkError
    UNKNOWN: CustomerClientLinkErrorEnum.CustomerClientLinkError
    CLIENT_ALREADY_INVITED_BY_THIS_MANAGER: CustomerClientLinkErrorEnum.CustomerClientLinkError
    CLIENT_ALREADY_MANAGED_IN_HIERARCHY: CustomerClientLinkErrorEnum.CustomerClientLinkError
    CYCLIC_LINK_NOT_ALLOWED: CustomerClientLinkErrorEnum.CustomerClientLinkError
    CUSTOMER_HAS_TOO_MANY_ACCOUNTS: CustomerClientLinkErrorEnum.CustomerClientLinkError
    CLIENT_HAS_TOO_MANY_INVITATIONS: CustomerClientLinkErrorEnum.CustomerClientLinkError
    CANNOT_HIDE_OR_UNHIDE_MANAGER_ACCOUNTS: CustomerClientLinkErrorEnum.CustomerClientLinkError
    CUSTOMER_HAS_TOO_MANY_ACCOUNTS_AT_MANAGER: CustomerClientLinkErrorEnum.CustomerClientLinkError
    CLIENT_HAS_TOO_MANY_MANAGERS: CustomerClientLinkErrorEnum.CustomerClientLinkError

    def __init__(self) -> None:
        ...