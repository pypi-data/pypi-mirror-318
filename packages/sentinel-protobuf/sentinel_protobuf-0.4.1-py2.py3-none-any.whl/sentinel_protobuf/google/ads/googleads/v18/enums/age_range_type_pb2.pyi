from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class AgeRangeTypeEnum(_message.Message):
    __slots__ = ()

    class AgeRangeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[AgeRangeTypeEnum.AgeRangeType]
        UNKNOWN: _ClassVar[AgeRangeTypeEnum.AgeRangeType]
        AGE_RANGE_18_24: _ClassVar[AgeRangeTypeEnum.AgeRangeType]
        AGE_RANGE_25_34: _ClassVar[AgeRangeTypeEnum.AgeRangeType]
        AGE_RANGE_35_44: _ClassVar[AgeRangeTypeEnum.AgeRangeType]
        AGE_RANGE_45_54: _ClassVar[AgeRangeTypeEnum.AgeRangeType]
        AGE_RANGE_55_64: _ClassVar[AgeRangeTypeEnum.AgeRangeType]
        AGE_RANGE_65_UP: _ClassVar[AgeRangeTypeEnum.AgeRangeType]
        AGE_RANGE_UNDETERMINED: _ClassVar[AgeRangeTypeEnum.AgeRangeType]
    UNSPECIFIED: AgeRangeTypeEnum.AgeRangeType
    UNKNOWN: AgeRangeTypeEnum.AgeRangeType
    AGE_RANGE_18_24: AgeRangeTypeEnum.AgeRangeType
    AGE_RANGE_25_34: AgeRangeTypeEnum.AgeRangeType
    AGE_RANGE_35_44: AgeRangeTypeEnum.AgeRangeType
    AGE_RANGE_45_54: AgeRangeTypeEnum.AgeRangeType
    AGE_RANGE_55_64: AgeRangeTypeEnum.AgeRangeType
    AGE_RANGE_65_UP: AgeRangeTypeEnum.AgeRangeType
    AGE_RANGE_UNDETERMINED: AgeRangeTypeEnum.AgeRangeType

    def __init__(self) -> None:
        ...