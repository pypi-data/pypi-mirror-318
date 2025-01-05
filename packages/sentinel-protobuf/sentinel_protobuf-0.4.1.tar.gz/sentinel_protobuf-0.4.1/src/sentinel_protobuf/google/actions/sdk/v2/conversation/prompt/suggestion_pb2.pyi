from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class Suggestion(_message.Message):
    __slots__ = ('title',)
    TITLE_FIELD_NUMBER: _ClassVar[int]
    title: str

    def __init__(self, title: _Optional[str]=...) -> None:
        ...