from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class BudgetStatusEnum(_message.Message):
    __slots__ = ()

    class BudgetStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[BudgetStatusEnum.BudgetStatus]
        UNKNOWN: _ClassVar[BudgetStatusEnum.BudgetStatus]
        ENABLED: _ClassVar[BudgetStatusEnum.BudgetStatus]
        REMOVED: _ClassVar[BudgetStatusEnum.BudgetStatus]
    UNSPECIFIED: BudgetStatusEnum.BudgetStatus
    UNKNOWN: BudgetStatusEnum.BudgetStatus
    ENABLED: BudgetStatusEnum.BudgetStatus
    REMOVED: BudgetStatusEnum.BudgetStatus

    def __init__(self) -> None:
        ...