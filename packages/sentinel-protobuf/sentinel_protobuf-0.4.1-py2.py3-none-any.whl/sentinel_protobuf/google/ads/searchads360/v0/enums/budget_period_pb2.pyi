from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class BudgetPeriodEnum(_message.Message):
    __slots__ = ()

    class BudgetPeriod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[BudgetPeriodEnum.BudgetPeriod]
        UNKNOWN: _ClassVar[BudgetPeriodEnum.BudgetPeriod]
        DAILY: _ClassVar[BudgetPeriodEnum.BudgetPeriod]
        FIXED_DAILY: _ClassVar[BudgetPeriodEnum.BudgetPeriod]
        CUSTOM_PERIOD: _ClassVar[BudgetPeriodEnum.BudgetPeriod]
    UNSPECIFIED: BudgetPeriodEnum.BudgetPeriod
    UNKNOWN: BudgetPeriodEnum.BudgetPeriod
    DAILY: BudgetPeriodEnum.BudgetPeriod
    FIXED_DAILY: BudgetPeriodEnum.BudgetPeriod
    CUSTOM_PERIOD: BudgetPeriodEnum.BudgetPeriod

    def __init__(self) -> None:
        ...