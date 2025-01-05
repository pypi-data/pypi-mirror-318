from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class FixedCpmTargetFrequencyTimeUnitEnum(_message.Message):
    __slots__ = ()

    class FixedCpmTargetFrequencyTimeUnit(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[FixedCpmTargetFrequencyTimeUnitEnum.FixedCpmTargetFrequencyTimeUnit]
        UNKNOWN: _ClassVar[FixedCpmTargetFrequencyTimeUnitEnum.FixedCpmTargetFrequencyTimeUnit]
        MONTHLY: _ClassVar[FixedCpmTargetFrequencyTimeUnitEnum.FixedCpmTargetFrequencyTimeUnit]
    UNSPECIFIED: FixedCpmTargetFrequencyTimeUnitEnum.FixedCpmTargetFrequencyTimeUnit
    UNKNOWN: FixedCpmTargetFrequencyTimeUnitEnum.FixedCpmTargetFrequencyTimeUnit
    MONTHLY: FixedCpmTargetFrequencyTimeUnitEnum.FixedCpmTargetFrequencyTimeUnit

    def __init__(self) -> None:
        ...