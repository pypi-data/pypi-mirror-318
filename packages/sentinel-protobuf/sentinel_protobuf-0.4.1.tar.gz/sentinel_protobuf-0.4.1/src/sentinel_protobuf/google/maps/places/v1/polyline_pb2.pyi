from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class Polyline(_message.Message):
    __slots__ = ('encoded_polyline',)
    ENCODED_POLYLINE_FIELD_NUMBER: _ClassVar[int]
    encoded_polyline: str

    def __init__(self, encoded_polyline: _Optional[str]=...) -> None:
        ...