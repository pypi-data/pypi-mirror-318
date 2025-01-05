from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class Compliance(_message.Message):
    __slots__ = ('standard', 'version', 'ids')
    STANDARD_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    IDS_FIELD_NUMBER: _ClassVar[int]
    standard: str
    version: str
    ids: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, standard: _Optional[str]=..., version: _Optional[str]=..., ids: _Optional[_Iterable[str]]=...) -> None:
        ...