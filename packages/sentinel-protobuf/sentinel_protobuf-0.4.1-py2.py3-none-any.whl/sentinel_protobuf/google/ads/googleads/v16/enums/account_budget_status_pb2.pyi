from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class AccountBudgetStatusEnum(_message.Message):
    __slots__ = ()

    class AccountBudgetStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[AccountBudgetStatusEnum.AccountBudgetStatus]
        UNKNOWN: _ClassVar[AccountBudgetStatusEnum.AccountBudgetStatus]
        PENDING: _ClassVar[AccountBudgetStatusEnum.AccountBudgetStatus]
        APPROVED: _ClassVar[AccountBudgetStatusEnum.AccountBudgetStatus]
        CANCELLED: _ClassVar[AccountBudgetStatusEnum.AccountBudgetStatus]
    UNSPECIFIED: AccountBudgetStatusEnum.AccountBudgetStatus
    UNKNOWN: AccountBudgetStatusEnum.AccountBudgetStatus
    PENDING: AccountBudgetStatusEnum.AccountBudgetStatus
    APPROVED: AccountBudgetStatusEnum.AccountBudgetStatus
    CANCELLED: AccountBudgetStatusEnum.AccountBudgetStatus

    def __init__(self) -> None:
        ...