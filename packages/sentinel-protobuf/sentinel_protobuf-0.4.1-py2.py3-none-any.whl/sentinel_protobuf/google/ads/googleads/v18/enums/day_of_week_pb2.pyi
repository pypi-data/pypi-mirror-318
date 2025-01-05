from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class DayOfWeekEnum(_message.Message):
    __slots__ = ()

    class DayOfWeek(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[DayOfWeekEnum.DayOfWeek]
        UNKNOWN: _ClassVar[DayOfWeekEnum.DayOfWeek]
        MONDAY: _ClassVar[DayOfWeekEnum.DayOfWeek]
        TUESDAY: _ClassVar[DayOfWeekEnum.DayOfWeek]
        WEDNESDAY: _ClassVar[DayOfWeekEnum.DayOfWeek]
        THURSDAY: _ClassVar[DayOfWeekEnum.DayOfWeek]
        FRIDAY: _ClassVar[DayOfWeekEnum.DayOfWeek]
        SATURDAY: _ClassVar[DayOfWeekEnum.DayOfWeek]
        SUNDAY: _ClassVar[DayOfWeekEnum.DayOfWeek]
    UNSPECIFIED: DayOfWeekEnum.DayOfWeek
    UNKNOWN: DayOfWeekEnum.DayOfWeek
    MONDAY: DayOfWeekEnum.DayOfWeek
    TUESDAY: DayOfWeekEnum.DayOfWeek
    WEDNESDAY: DayOfWeekEnum.DayOfWeek
    THURSDAY: DayOfWeekEnum.DayOfWeek
    FRIDAY: DayOfWeekEnum.DayOfWeek
    SATURDAY: DayOfWeekEnum.DayOfWeek
    SUNDAY: DayOfWeekEnum.DayOfWeek

    def __init__(self) -> None:
        ...