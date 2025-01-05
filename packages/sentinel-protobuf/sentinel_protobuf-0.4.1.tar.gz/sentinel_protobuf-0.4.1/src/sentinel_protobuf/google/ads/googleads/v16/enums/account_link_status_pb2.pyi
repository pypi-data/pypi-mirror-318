from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class AccountLinkStatusEnum(_message.Message):
    __slots__ = ()

    class AccountLinkStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[AccountLinkStatusEnum.AccountLinkStatus]
        UNKNOWN: _ClassVar[AccountLinkStatusEnum.AccountLinkStatus]
        ENABLED: _ClassVar[AccountLinkStatusEnum.AccountLinkStatus]
        REMOVED: _ClassVar[AccountLinkStatusEnum.AccountLinkStatus]
        REQUESTED: _ClassVar[AccountLinkStatusEnum.AccountLinkStatus]
        PENDING_APPROVAL: _ClassVar[AccountLinkStatusEnum.AccountLinkStatus]
        REJECTED: _ClassVar[AccountLinkStatusEnum.AccountLinkStatus]
        REVOKED: _ClassVar[AccountLinkStatusEnum.AccountLinkStatus]
    UNSPECIFIED: AccountLinkStatusEnum.AccountLinkStatus
    UNKNOWN: AccountLinkStatusEnum.AccountLinkStatus
    ENABLED: AccountLinkStatusEnum.AccountLinkStatus
    REMOVED: AccountLinkStatusEnum.AccountLinkStatus
    REQUESTED: AccountLinkStatusEnum.AccountLinkStatus
    PENDING_APPROVAL: AccountLinkStatusEnum.AccountLinkStatus
    REJECTED: AccountLinkStatusEnum.AccountLinkStatus
    REVOKED: AccountLinkStatusEnum.AccountLinkStatus

    def __init__(self) -> None:
        ...