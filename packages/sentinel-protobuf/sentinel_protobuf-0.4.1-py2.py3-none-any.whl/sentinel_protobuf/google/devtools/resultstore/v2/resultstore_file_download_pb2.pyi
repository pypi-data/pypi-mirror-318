from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class GetFileRequest(_message.Message):
    __slots__ = ('uri', 'read_offset', 'read_limit', 'archive_entry')
    URI_FIELD_NUMBER: _ClassVar[int]
    READ_OFFSET_FIELD_NUMBER: _ClassVar[int]
    READ_LIMIT_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_ENTRY_FIELD_NUMBER: _ClassVar[int]
    uri: str
    read_offset: int
    read_limit: int
    archive_entry: str

    def __init__(self, uri: _Optional[str]=..., read_offset: _Optional[int]=..., read_limit: _Optional[int]=..., archive_entry: _Optional[str]=...) -> None:
        ...

class GetFileResponse(_message.Message):
    __slots__ = ('data',)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: bytes

    def __init__(self, data: _Optional[bytes]=...) -> None:
        ...

class GetFileTailRequest(_message.Message):
    __slots__ = ('uri', 'read_offset', 'read_limit', 'archive_entry')
    URI_FIELD_NUMBER: _ClassVar[int]
    READ_OFFSET_FIELD_NUMBER: _ClassVar[int]
    READ_LIMIT_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_ENTRY_FIELD_NUMBER: _ClassVar[int]
    uri: str
    read_offset: int
    read_limit: int
    archive_entry: str

    def __init__(self, uri: _Optional[str]=..., read_offset: _Optional[int]=..., read_limit: _Optional[int]=..., archive_entry: _Optional[str]=...) -> None:
        ...

class GetFileTailResponse(_message.Message):
    __slots__ = ('data',)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: bytes

    def __init__(self, data: _Optional[bytes]=...) -> None:
        ...