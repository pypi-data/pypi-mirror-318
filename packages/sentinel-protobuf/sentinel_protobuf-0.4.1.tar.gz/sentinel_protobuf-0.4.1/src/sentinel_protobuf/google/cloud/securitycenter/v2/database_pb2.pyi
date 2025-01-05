from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class Database(_message.Message):
    __slots__ = ('name', 'display_name', 'user_name', 'query', 'grantees', 'version')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    GRANTEES_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    user_name: str
    query: str
    grantees: _containers.RepeatedScalarFieldContainer[str]
    version: str

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., user_name: _Optional[str]=..., query: _Optional[str]=..., grantees: _Optional[_Iterable[str]]=..., version: _Optional[str]=...) -> None:
        ...