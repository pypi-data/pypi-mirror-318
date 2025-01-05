from google.type import date_pb2 as _date_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class DateRange(_message.Message):
    __slots__ = ('start', 'end')
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    start: _date_pb2.Date
    end: _date_pb2.Date

    def __init__(self, start: _Optional[_Union[_date_pb2.Date, _Mapping]]=..., end: _Optional[_Union[_date_pb2.Date, _Mapping]]=...) -> None:
        ...