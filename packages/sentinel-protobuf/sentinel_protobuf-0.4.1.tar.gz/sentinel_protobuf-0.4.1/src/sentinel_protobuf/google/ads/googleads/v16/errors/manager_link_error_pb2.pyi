from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class ManagerLinkErrorEnum(_message.Message):
    __slots__ = ()

    class ManagerLinkError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ManagerLinkErrorEnum.ManagerLinkError]
        UNKNOWN: _ClassVar[ManagerLinkErrorEnum.ManagerLinkError]
        ACCOUNTS_NOT_COMPATIBLE_FOR_LINKING: _ClassVar[ManagerLinkErrorEnum.ManagerLinkError]
        TOO_MANY_MANAGERS: _ClassVar[ManagerLinkErrorEnum.ManagerLinkError]
        TOO_MANY_INVITES: _ClassVar[ManagerLinkErrorEnum.ManagerLinkError]
        ALREADY_INVITED_BY_THIS_MANAGER: _ClassVar[ManagerLinkErrorEnum.ManagerLinkError]
        ALREADY_MANAGED_BY_THIS_MANAGER: _ClassVar[ManagerLinkErrorEnum.ManagerLinkError]
        ALREADY_MANAGED_IN_HIERARCHY: _ClassVar[ManagerLinkErrorEnum.ManagerLinkError]
        DUPLICATE_CHILD_FOUND: _ClassVar[ManagerLinkErrorEnum.ManagerLinkError]
        CLIENT_HAS_NO_ADMIN_USER: _ClassVar[ManagerLinkErrorEnum.ManagerLinkError]
        MAX_DEPTH_EXCEEDED: _ClassVar[ManagerLinkErrorEnum.ManagerLinkError]
        CYCLE_NOT_ALLOWED: _ClassVar[ManagerLinkErrorEnum.ManagerLinkError]
        TOO_MANY_ACCOUNTS: _ClassVar[ManagerLinkErrorEnum.ManagerLinkError]
        TOO_MANY_ACCOUNTS_AT_MANAGER: _ClassVar[ManagerLinkErrorEnum.ManagerLinkError]
        NON_OWNER_USER_CANNOT_MODIFY_LINK: _ClassVar[ManagerLinkErrorEnum.ManagerLinkError]
        SUSPENDED_ACCOUNT_CANNOT_ADD_CLIENTS: _ClassVar[ManagerLinkErrorEnum.ManagerLinkError]
        CLIENT_OUTSIDE_TREE: _ClassVar[ManagerLinkErrorEnum.ManagerLinkError]
        INVALID_STATUS_CHANGE: _ClassVar[ManagerLinkErrorEnum.ManagerLinkError]
        INVALID_CHANGE: _ClassVar[ManagerLinkErrorEnum.ManagerLinkError]
        CUSTOMER_CANNOT_MANAGE_SELF: _ClassVar[ManagerLinkErrorEnum.ManagerLinkError]
        CREATING_ENABLED_LINK_NOT_ALLOWED: _ClassVar[ManagerLinkErrorEnum.ManagerLinkError]
    UNSPECIFIED: ManagerLinkErrorEnum.ManagerLinkError
    UNKNOWN: ManagerLinkErrorEnum.ManagerLinkError
    ACCOUNTS_NOT_COMPATIBLE_FOR_LINKING: ManagerLinkErrorEnum.ManagerLinkError
    TOO_MANY_MANAGERS: ManagerLinkErrorEnum.ManagerLinkError
    TOO_MANY_INVITES: ManagerLinkErrorEnum.ManagerLinkError
    ALREADY_INVITED_BY_THIS_MANAGER: ManagerLinkErrorEnum.ManagerLinkError
    ALREADY_MANAGED_BY_THIS_MANAGER: ManagerLinkErrorEnum.ManagerLinkError
    ALREADY_MANAGED_IN_HIERARCHY: ManagerLinkErrorEnum.ManagerLinkError
    DUPLICATE_CHILD_FOUND: ManagerLinkErrorEnum.ManagerLinkError
    CLIENT_HAS_NO_ADMIN_USER: ManagerLinkErrorEnum.ManagerLinkError
    MAX_DEPTH_EXCEEDED: ManagerLinkErrorEnum.ManagerLinkError
    CYCLE_NOT_ALLOWED: ManagerLinkErrorEnum.ManagerLinkError
    TOO_MANY_ACCOUNTS: ManagerLinkErrorEnum.ManagerLinkError
    TOO_MANY_ACCOUNTS_AT_MANAGER: ManagerLinkErrorEnum.ManagerLinkError
    NON_OWNER_USER_CANNOT_MODIFY_LINK: ManagerLinkErrorEnum.ManagerLinkError
    SUSPENDED_ACCOUNT_CANNOT_ADD_CLIENTS: ManagerLinkErrorEnum.ManagerLinkError
    CLIENT_OUTSIDE_TREE: ManagerLinkErrorEnum.ManagerLinkError
    INVALID_STATUS_CHANGE: ManagerLinkErrorEnum.ManagerLinkError
    INVALID_CHANGE: ManagerLinkErrorEnum.ManagerLinkError
    CUSTOMER_CANNOT_MANAGE_SELF: ManagerLinkErrorEnum.ManagerLinkError
    CREATING_ENABLED_LINK_NOT_ALLOWED: ManagerLinkErrorEnum.ManagerLinkError

    def __init__(self) -> None:
        ...