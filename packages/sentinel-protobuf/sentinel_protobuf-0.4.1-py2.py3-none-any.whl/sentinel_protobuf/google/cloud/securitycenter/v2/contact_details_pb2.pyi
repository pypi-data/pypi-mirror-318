from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ContactDetails(_message.Message):
    __slots__ = ('contacts',)
    CONTACTS_FIELD_NUMBER: _ClassVar[int]
    contacts: _containers.RepeatedCompositeFieldContainer[Contact]

    def __init__(self, contacts: _Optional[_Iterable[_Union[Contact, _Mapping]]]=...) -> None:
        ...

class Contact(_message.Message):
    __slots__ = ('email',)
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    email: str

    def __init__(self, email: _Optional[str]=...) -> None:
        ...