from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class TargetingDimensionEnum(_message.Message):
    __slots__ = ()

    class TargetingDimension(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[TargetingDimensionEnum.TargetingDimension]
        UNKNOWN: _ClassVar[TargetingDimensionEnum.TargetingDimension]
        KEYWORD: _ClassVar[TargetingDimensionEnum.TargetingDimension]
        AUDIENCE: _ClassVar[TargetingDimensionEnum.TargetingDimension]
        TOPIC: _ClassVar[TargetingDimensionEnum.TargetingDimension]
        GENDER: _ClassVar[TargetingDimensionEnum.TargetingDimension]
        AGE_RANGE: _ClassVar[TargetingDimensionEnum.TargetingDimension]
        PLACEMENT: _ClassVar[TargetingDimensionEnum.TargetingDimension]
        PARENTAL_STATUS: _ClassVar[TargetingDimensionEnum.TargetingDimension]
        INCOME_RANGE: _ClassVar[TargetingDimensionEnum.TargetingDimension]
    UNSPECIFIED: TargetingDimensionEnum.TargetingDimension
    UNKNOWN: TargetingDimensionEnum.TargetingDimension
    KEYWORD: TargetingDimensionEnum.TargetingDimension
    AUDIENCE: TargetingDimensionEnum.TargetingDimension
    TOPIC: TargetingDimensionEnum.TargetingDimension
    GENDER: TargetingDimensionEnum.TargetingDimension
    AGE_RANGE: TargetingDimensionEnum.TargetingDimension
    PLACEMENT: TargetingDimensionEnum.TargetingDimension
    PARENTAL_STATUS: TargetingDimensionEnum.TargetingDimension
    INCOME_RANGE: TargetingDimensionEnum.TargetingDimension

    def __init__(self) -> None:
        ...