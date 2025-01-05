from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class CustomerManagerLinkErrorEnum(_message.Message):
    __slots__ = ()

    class CustomerManagerLinkError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[CustomerManagerLinkErrorEnum.CustomerManagerLinkError]
        UNKNOWN: _ClassVar[CustomerManagerLinkErrorEnum.CustomerManagerLinkError]
        NO_PENDING_INVITE: _ClassVar[CustomerManagerLinkErrorEnum.CustomerManagerLinkError]
        SAME_CLIENT_MORE_THAN_ONCE_PER_CALL: _ClassVar[CustomerManagerLinkErrorEnum.CustomerManagerLinkError]
        MANAGER_HAS_MAX_NUMBER_OF_LINKED_ACCOUNTS: _ClassVar[CustomerManagerLinkErrorEnum.CustomerManagerLinkError]
        CANNOT_UNLINK_ACCOUNT_WITHOUT_ACTIVE_USER: _ClassVar[CustomerManagerLinkErrorEnum.CustomerManagerLinkError]
        CANNOT_REMOVE_LAST_CLIENT_ACCOUNT_OWNER: _ClassVar[CustomerManagerLinkErrorEnum.CustomerManagerLinkError]
        CANNOT_CHANGE_ROLE_BY_NON_ACCOUNT_OWNER: _ClassVar[CustomerManagerLinkErrorEnum.CustomerManagerLinkError]
        CANNOT_CHANGE_ROLE_FOR_NON_ACTIVE_LINK_ACCOUNT: _ClassVar[CustomerManagerLinkErrorEnum.CustomerManagerLinkError]
        DUPLICATE_CHILD_FOUND: _ClassVar[CustomerManagerLinkErrorEnum.CustomerManagerLinkError]
        TEST_ACCOUNT_LINKS_TOO_MANY_CHILD_ACCOUNTS: _ClassVar[CustomerManagerLinkErrorEnum.CustomerManagerLinkError]
    UNSPECIFIED: CustomerManagerLinkErrorEnum.CustomerManagerLinkError
    UNKNOWN: CustomerManagerLinkErrorEnum.CustomerManagerLinkError
    NO_PENDING_INVITE: CustomerManagerLinkErrorEnum.CustomerManagerLinkError
    SAME_CLIENT_MORE_THAN_ONCE_PER_CALL: CustomerManagerLinkErrorEnum.CustomerManagerLinkError
    MANAGER_HAS_MAX_NUMBER_OF_LINKED_ACCOUNTS: CustomerManagerLinkErrorEnum.CustomerManagerLinkError
    CANNOT_UNLINK_ACCOUNT_WITHOUT_ACTIVE_USER: CustomerManagerLinkErrorEnum.CustomerManagerLinkError
    CANNOT_REMOVE_LAST_CLIENT_ACCOUNT_OWNER: CustomerManagerLinkErrorEnum.CustomerManagerLinkError
    CANNOT_CHANGE_ROLE_BY_NON_ACCOUNT_OWNER: CustomerManagerLinkErrorEnum.CustomerManagerLinkError
    CANNOT_CHANGE_ROLE_FOR_NON_ACTIVE_LINK_ACCOUNT: CustomerManagerLinkErrorEnum.CustomerManagerLinkError
    DUPLICATE_CHILD_FOUND: CustomerManagerLinkErrorEnum.CustomerManagerLinkError
    TEST_ACCOUNT_LINKS_TOO_MANY_CHILD_ACCOUNTS: CustomerManagerLinkErrorEnum.CustomerManagerLinkError

    def __init__(self) -> None:
        ...