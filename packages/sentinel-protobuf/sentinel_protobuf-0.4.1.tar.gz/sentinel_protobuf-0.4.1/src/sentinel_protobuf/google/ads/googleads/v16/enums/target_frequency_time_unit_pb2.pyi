from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class TargetFrequencyTimeUnitEnum(_message.Message):
    __slots__ = ()

    class TargetFrequencyTimeUnit(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[TargetFrequencyTimeUnitEnum.TargetFrequencyTimeUnit]
        UNKNOWN: _ClassVar[TargetFrequencyTimeUnitEnum.TargetFrequencyTimeUnit]
        WEEKLY: _ClassVar[TargetFrequencyTimeUnitEnum.TargetFrequencyTimeUnit]
    UNSPECIFIED: TargetFrequencyTimeUnitEnum.TargetFrequencyTimeUnit
    UNKNOWN: TargetFrequencyTimeUnitEnum.TargetFrequencyTimeUnit
    WEEKLY: TargetFrequencyTimeUnitEnum.TargetFrequencyTimeUnit

    def __init__(self) -> None:
        ...