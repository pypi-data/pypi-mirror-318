from google.ads.admanager.v1 import time_unit_enum_pb2 as _time_unit_enum_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FrequencyCap(_message.Message):
    __slots__ = ("max_impressions", "time_amount", "time_unit")
    MAX_IMPRESSIONS_FIELD_NUMBER: _ClassVar[int]
    TIME_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    TIME_UNIT_FIELD_NUMBER: _ClassVar[int]
    max_impressions: int
    time_amount: int
    time_unit: _time_unit_enum_pb2.TimeUnitEnum.TimeUnit
    def __init__(self, max_impressions: _Optional[int] = ..., time_amount: _Optional[int] = ..., time_unit: _Optional[_Union[_time_unit_enum_pb2.TimeUnitEnum.TimeUnit, str]] = ...) -> None: ...
