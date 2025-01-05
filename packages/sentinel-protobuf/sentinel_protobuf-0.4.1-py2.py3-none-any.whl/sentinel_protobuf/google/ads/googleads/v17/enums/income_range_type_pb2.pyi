from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class IncomeRangeTypeEnum(_message.Message):
    __slots__ = ()

    class IncomeRangeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[IncomeRangeTypeEnum.IncomeRangeType]
        UNKNOWN: _ClassVar[IncomeRangeTypeEnum.IncomeRangeType]
        INCOME_RANGE_0_50: _ClassVar[IncomeRangeTypeEnum.IncomeRangeType]
        INCOME_RANGE_50_60: _ClassVar[IncomeRangeTypeEnum.IncomeRangeType]
        INCOME_RANGE_60_70: _ClassVar[IncomeRangeTypeEnum.IncomeRangeType]
        INCOME_RANGE_70_80: _ClassVar[IncomeRangeTypeEnum.IncomeRangeType]
        INCOME_RANGE_80_90: _ClassVar[IncomeRangeTypeEnum.IncomeRangeType]
        INCOME_RANGE_90_UP: _ClassVar[IncomeRangeTypeEnum.IncomeRangeType]
        INCOME_RANGE_UNDETERMINED: _ClassVar[IncomeRangeTypeEnum.IncomeRangeType]
    UNSPECIFIED: IncomeRangeTypeEnum.IncomeRangeType
    UNKNOWN: IncomeRangeTypeEnum.IncomeRangeType
    INCOME_RANGE_0_50: IncomeRangeTypeEnum.IncomeRangeType
    INCOME_RANGE_50_60: IncomeRangeTypeEnum.IncomeRangeType
    INCOME_RANGE_60_70: IncomeRangeTypeEnum.IncomeRangeType
    INCOME_RANGE_70_80: IncomeRangeTypeEnum.IncomeRangeType
    INCOME_RANGE_80_90: IncomeRangeTypeEnum.IncomeRangeType
    INCOME_RANGE_90_UP: IncomeRangeTypeEnum.IncomeRangeType
    INCOME_RANGE_UNDETERMINED: IncomeRangeTypeEnum.IncomeRangeType

    def __init__(self) -> None:
        ...