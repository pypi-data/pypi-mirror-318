from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class CompletionStats(_message.Message):
    __slots__ = ('successful_count', 'failed_count', 'incomplete_count', 'successful_forecast_point_count')
    SUCCESSFUL_COUNT_FIELD_NUMBER: _ClassVar[int]
    FAILED_COUNT_FIELD_NUMBER: _ClassVar[int]
    INCOMPLETE_COUNT_FIELD_NUMBER: _ClassVar[int]
    SUCCESSFUL_FORECAST_POINT_COUNT_FIELD_NUMBER: _ClassVar[int]
    successful_count: int
    failed_count: int
    incomplete_count: int
    successful_forecast_point_count: int

    def __init__(self, successful_count: _Optional[int]=..., failed_count: _Optional[int]=..., incomplete_count: _Optional[int]=..., successful_forecast_point_count: _Optional[int]=...) -> None:
        ...