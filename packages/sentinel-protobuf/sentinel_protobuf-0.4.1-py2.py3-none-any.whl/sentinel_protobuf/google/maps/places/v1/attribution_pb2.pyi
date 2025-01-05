from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class AuthorAttribution(_message.Message):
    __slots__ = ('display_name', 'uri', 'photo_uri')
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    URI_FIELD_NUMBER: _ClassVar[int]
    PHOTO_URI_FIELD_NUMBER: _ClassVar[int]
    display_name: str
    uri: str
    photo_uri: str

    def __init__(self, display_name: _Optional[str]=..., uri: _Optional[str]=..., photo_uri: _Optional[str]=...) -> None:
        ...