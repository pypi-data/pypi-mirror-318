from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class Simple(_message.Message):
    __slots__ = ('speech', 'text')
    SPEECH_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    speech: str
    text: str

    def __init__(self, speech: _Optional[str]=..., text: _Optional[str]=...) -> None:
        ...