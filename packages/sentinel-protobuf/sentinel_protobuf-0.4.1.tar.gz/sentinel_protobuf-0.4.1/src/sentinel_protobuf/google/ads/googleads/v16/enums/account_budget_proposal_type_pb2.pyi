from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class AccountBudgetProposalTypeEnum(_message.Message):
    __slots__ = ()

    class AccountBudgetProposalType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[AccountBudgetProposalTypeEnum.AccountBudgetProposalType]
        UNKNOWN: _ClassVar[AccountBudgetProposalTypeEnum.AccountBudgetProposalType]
        CREATE: _ClassVar[AccountBudgetProposalTypeEnum.AccountBudgetProposalType]
        UPDATE: _ClassVar[AccountBudgetProposalTypeEnum.AccountBudgetProposalType]
        END: _ClassVar[AccountBudgetProposalTypeEnum.AccountBudgetProposalType]
        REMOVE: _ClassVar[AccountBudgetProposalTypeEnum.AccountBudgetProposalType]
    UNSPECIFIED: AccountBudgetProposalTypeEnum.AccountBudgetProposalType
    UNKNOWN: AccountBudgetProposalTypeEnum.AccountBudgetProposalType
    CREATE: AccountBudgetProposalTypeEnum.AccountBudgetProposalType
    UPDATE: AccountBudgetProposalTypeEnum.AccountBudgetProposalType
    END: AccountBudgetProposalTypeEnum.AccountBudgetProposalType
    REMOVE: AccountBudgetProposalTypeEnum.AccountBudgetProposalType

    def __init__(self) -> None:
        ...