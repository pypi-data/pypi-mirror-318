from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class NoteKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NOTE_KIND_UNSPECIFIED: _ClassVar[NoteKind]
    VULNERABILITY: _ClassVar[NoteKind]
    BUILD: _ClassVar[NoteKind]
    IMAGE: _ClassVar[NoteKind]
    PACKAGE: _ClassVar[NoteKind]
    DEPLOYMENT: _ClassVar[NoteKind]
    DISCOVERY: _ClassVar[NoteKind]
    ATTESTATION: _ClassVar[NoteKind]
NOTE_KIND_UNSPECIFIED: NoteKind
VULNERABILITY: NoteKind
BUILD: NoteKind
IMAGE: NoteKind
PACKAGE: NoteKind
DEPLOYMENT: NoteKind
DISCOVERY: NoteKind
ATTESTATION: NoteKind

class RelatedUrl(_message.Message):
    __slots__ = ('url', 'label')
    URL_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    url: str
    label: str

    def __init__(self, url: _Optional[str]=..., label: _Optional[str]=...) -> None:
        ...

class Signature(_message.Message):
    __slots__ = ('signature', 'public_key_id')
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    signature: bytes
    public_key_id: str

    def __init__(self, signature: _Optional[bytes]=..., public_key_id: _Optional[str]=...) -> None:
        ...