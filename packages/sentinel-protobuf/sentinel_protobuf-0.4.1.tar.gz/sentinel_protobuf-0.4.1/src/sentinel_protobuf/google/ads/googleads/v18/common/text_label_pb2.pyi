from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TextLabel(_message.Message):
    __slots__ = ("background_color", "description")
    BACKGROUND_COLOR_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    background_color: str
    description: str
    def __init__(self, background_color: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...
