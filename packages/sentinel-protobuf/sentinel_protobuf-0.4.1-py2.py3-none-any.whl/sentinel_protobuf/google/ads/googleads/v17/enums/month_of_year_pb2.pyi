from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class MonthOfYearEnum(_message.Message):
    __slots__ = ()

    class MonthOfYear(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[MonthOfYearEnum.MonthOfYear]
        UNKNOWN: _ClassVar[MonthOfYearEnum.MonthOfYear]
        JANUARY: _ClassVar[MonthOfYearEnum.MonthOfYear]
        FEBRUARY: _ClassVar[MonthOfYearEnum.MonthOfYear]
        MARCH: _ClassVar[MonthOfYearEnum.MonthOfYear]
        APRIL: _ClassVar[MonthOfYearEnum.MonthOfYear]
        MAY: _ClassVar[MonthOfYearEnum.MonthOfYear]
        JUNE: _ClassVar[MonthOfYearEnum.MonthOfYear]
        JULY: _ClassVar[MonthOfYearEnum.MonthOfYear]
        AUGUST: _ClassVar[MonthOfYearEnum.MonthOfYear]
        SEPTEMBER: _ClassVar[MonthOfYearEnum.MonthOfYear]
        OCTOBER: _ClassVar[MonthOfYearEnum.MonthOfYear]
        NOVEMBER: _ClassVar[MonthOfYearEnum.MonthOfYear]
        DECEMBER: _ClassVar[MonthOfYearEnum.MonthOfYear]
    UNSPECIFIED: MonthOfYearEnum.MonthOfYear
    UNKNOWN: MonthOfYearEnum.MonthOfYear
    JANUARY: MonthOfYearEnum.MonthOfYear
    FEBRUARY: MonthOfYearEnum.MonthOfYear
    MARCH: MonthOfYearEnum.MonthOfYear
    APRIL: MonthOfYearEnum.MonthOfYear
    MAY: MonthOfYearEnum.MonthOfYear
    JUNE: MonthOfYearEnum.MonthOfYear
    JULY: MonthOfYearEnum.MonthOfYear
    AUGUST: MonthOfYearEnum.MonthOfYear
    SEPTEMBER: MonthOfYearEnum.MonthOfYear
    OCTOBER: MonthOfYearEnum.MonthOfYear
    NOVEMBER: MonthOfYearEnum.MonthOfYear
    DECEMBER: MonthOfYearEnum.MonthOfYear

    def __init__(self) -> None:
        ...