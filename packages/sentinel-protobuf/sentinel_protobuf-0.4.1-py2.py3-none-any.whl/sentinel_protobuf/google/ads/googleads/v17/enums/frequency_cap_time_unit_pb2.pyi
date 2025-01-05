from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class FrequencyCapTimeUnitEnum(_message.Message):
    __slots__ = ()

    class FrequencyCapTimeUnit(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[FrequencyCapTimeUnitEnum.FrequencyCapTimeUnit]
        UNKNOWN: _ClassVar[FrequencyCapTimeUnitEnum.FrequencyCapTimeUnit]
        DAY: _ClassVar[FrequencyCapTimeUnitEnum.FrequencyCapTimeUnit]
        WEEK: _ClassVar[FrequencyCapTimeUnitEnum.FrequencyCapTimeUnit]
        MONTH: _ClassVar[FrequencyCapTimeUnitEnum.FrequencyCapTimeUnit]
    UNSPECIFIED: FrequencyCapTimeUnitEnum.FrequencyCapTimeUnit
    UNKNOWN: FrequencyCapTimeUnitEnum.FrequencyCapTimeUnit
    DAY: FrequencyCapTimeUnitEnum.FrequencyCapTimeUnit
    WEEK: FrequencyCapTimeUnitEnum.FrequencyCapTimeUnit
    MONTH: FrequencyCapTimeUnitEnum.FrequencyCapTimeUnit

    def __init__(self) -> None:
        ...