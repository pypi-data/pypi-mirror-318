from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class Application(_message.Message):
    __slots__ = ('base_uri', 'full_uri')
    BASE_URI_FIELD_NUMBER: _ClassVar[int]
    FULL_URI_FIELD_NUMBER: _ClassVar[int]
    base_uri: str
    full_uri: str

    def __init__(self, base_uri: _Optional[str]=..., full_uri: _Optional[str]=...) -> None:
        ...