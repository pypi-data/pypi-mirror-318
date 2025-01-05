from google.ads.googleads.v18.enums import month_of_year_pb2 as _month_of_year_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DateRange(_message.Message):
    __slots__ = ("start_date", "end_date")
    START_DATE_FIELD_NUMBER: _ClassVar[int]
    END_DATE_FIELD_NUMBER: _ClassVar[int]
    start_date: str
    end_date: str
    def __init__(self, start_date: _Optional[str] = ..., end_date: _Optional[str] = ...) -> None: ...

class YearMonthRange(_message.Message):
    __slots__ = ("start", "end")
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    start: YearMonth
    end: YearMonth
    def __init__(self, start: _Optional[_Union[YearMonth, _Mapping]] = ..., end: _Optional[_Union[YearMonth, _Mapping]] = ...) -> None: ...

class YearMonth(_message.Message):
    __slots__ = ("year", "month")
    YEAR_FIELD_NUMBER: _ClassVar[int]
    MONTH_FIELD_NUMBER: _ClassVar[int]
    year: int
    month: _month_of_year_pb2.MonthOfYearEnum.MonthOfYear
    def __init__(self, year: _Optional[int] = ..., month: _Optional[_Union[_month_of_year_pb2.MonthOfYearEnum.MonthOfYear, str]] = ...) -> None: ...
