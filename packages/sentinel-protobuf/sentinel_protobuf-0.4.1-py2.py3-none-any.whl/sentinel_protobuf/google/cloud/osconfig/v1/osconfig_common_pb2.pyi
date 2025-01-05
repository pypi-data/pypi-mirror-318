from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class FixedOrPercent(_message.Message):
    __slots__ = ('fixed', 'percent')
    FIXED_FIELD_NUMBER: _ClassVar[int]
    PERCENT_FIELD_NUMBER: _ClassVar[int]
    fixed: int
    percent: int

    def __init__(self, fixed: _Optional[int]=..., percent: _Optional[int]=...) -> None:
        ...