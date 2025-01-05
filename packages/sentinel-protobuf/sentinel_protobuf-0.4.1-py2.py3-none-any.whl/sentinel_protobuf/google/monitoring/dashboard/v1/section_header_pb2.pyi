from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class SectionHeader(_message.Message):
    __slots__ = ('subtitle', 'divider_below')
    SUBTITLE_FIELD_NUMBER: _ClassVar[int]
    DIVIDER_BELOW_FIELD_NUMBER: _ClassVar[int]
    subtitle: str
    divider_below: bool

    def __init__(self, subtitle: _Optional[str]=..., divider_below: bool=...) -> None:
        ...