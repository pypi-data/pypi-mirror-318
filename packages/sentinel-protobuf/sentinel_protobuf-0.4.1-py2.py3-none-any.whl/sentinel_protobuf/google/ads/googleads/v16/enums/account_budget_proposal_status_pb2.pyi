from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class AccountBudgetProposalStatusEnum(_message.Message):
    __slots__ = ()

    class AccountBudgetProposalStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[AccountBudgetProposalStatusEnum.AccountBudgetProposalStatus]
        UNKNOWN: _ClassVar[AccountBudgetProposalStatusEnum.AccountBudgetProposalStatus]
        PENDING: _ClassVar[AccountBudgetProposalStatusEnum.AccountBudgetProposalStatus]
        APPROVED_HELD: _ClassVar[AccountBudgetProposalStatusEnum.AccountBudgetProposalStatus]
        APPROVED: _ClassVar[AccountBudgetProposalStatusEnum.AccountBudgetProposalStatus]
        CANCELLED: _ClassVar[AccountBudgetProposalStatusEnum.AccountBudgetProposalStatus]
        REJECTED: _ClassVar[AccountBudgetProposalStatusEnum.AccountBudgetProposalStatus]
    UNSPECIFIED: AccountBudgetProposalStatusEnum.AccountBudgetProposalStatus
    UNKNOWN: AccountBudgetProposalStatusEnum.AccountBudgetProposalStatus
    PENDING: AccountBudgetProposalStatusEnum.AccountBudgetProposalStatus
    APPROVED_HELD: AccountBudgetProposalStatusEnum.AccountBudgetProposalStatus
    APPROVED: AccountBudgetProposalStatusEnum.AccountBudgetProposalStatus
    CANCELLED: AccountBudgetProposalStatusEnum.AccountBudgetProposalStatus
    REJECTED: AccountBudgetProposalStatusEnum.AccountBudgetProposalStatus

    def __init__(self) -> None:
        ...