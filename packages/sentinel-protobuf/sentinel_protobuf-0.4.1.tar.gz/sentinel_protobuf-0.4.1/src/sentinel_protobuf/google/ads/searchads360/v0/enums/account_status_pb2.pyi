from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class AccountStatusEnum(_message.Message):
    __slots__ = ()

    class AccountStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[AccountStatusEnum.AccountStatus]
        UNKNOWN: _ClassVar[AccountStatusEnum.AccountStatus]
        ENABLED: _ClassVar[AccountStatusEnum.AccountStatus]
        PAUSED: _ClassVar[AccountStatusEnum.AccountStatus]
        SUSPENDED: _ClassVar[AccountStatusEnum.AccountStatus]
        REMOVED: _ClassVar[AccountStatusEnum.AccountStatus]
        DRAFT: _ClassVar[AccountStatusEnum.AccountStatus]
    UNSPECIFIED: AccountStatusEnum.AccountStatus
    UNKNOWN: AccountStatusEnum.AccountStatus
    ENABLED: AccountStatusEnum.AccountStatus
    PAUSED: AccountStatusEnum.AccountStatus
    SUSPENDED: AccountStatusEnum.AccountStatus
    REMOVED: AccountStatusEnum.AccountStatus
    DRAFT: AccountStatusEnum.AccountStatus

    def __init__(self) -> None:
        ...