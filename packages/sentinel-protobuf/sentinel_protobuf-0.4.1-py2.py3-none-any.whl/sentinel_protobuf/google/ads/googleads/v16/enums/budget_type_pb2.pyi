from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class BudgetTypeEnum(_message.Message):
    __slots__ = ()

    class BudgetType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[BudgetTypeEnum.BudgetType]
        UNKNOWN: _ClassVar[BudgetTypeEnum.BudgetType]
        STANDARD: _ClassVar[BudgetTypeEnum.BudgetType]
        FIXED_CPA: _ClassVar[BudgetTypeEnum.BudgetType]
        SMART_CAMPAIGN: _ClassVar[BudgetTypeEnum.BudgetType]
        LOCAL_SERVICES: _ClassVar[BudgetTypeEnum.BudgetType]
    UNSPECIFIED: BudgetTypeEnum.BudgetType
    UNKNOWN: BudgetTypeEnum.BudgetType
    STANDARD: BudgetTypeEnum.BudgetType
    FIXED_CPA: BudgetTypeEnum.BudgetType
    SMART_CAMPAIGN: BudgetTypeEnum.BudgetType
    LOCAL_SERVICES: BudgetTypeEnum.BudgetType

    def __init__(self) -> None:
        ...