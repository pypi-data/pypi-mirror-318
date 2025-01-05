from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class AuthorizedDomain(_message.Message):
    __slots__ = ('name', 'id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    id: str

    def __init__(self, name: _Optional[str]=..., id: _Optional[str]=...) -> None:
        ...