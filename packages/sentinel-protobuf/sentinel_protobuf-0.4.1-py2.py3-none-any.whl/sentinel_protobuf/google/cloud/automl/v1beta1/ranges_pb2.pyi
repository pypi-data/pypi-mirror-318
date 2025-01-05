from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class DoubleRange(_message.Message):
    __slots__ = ('start', 'end')
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    start: float
    end: float

    def __init__(self, start: _Optional[float]=..., end: _Optional[float]=...) -> None:
        ...