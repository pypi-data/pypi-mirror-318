from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class AvroSchema(_message.Message):
    __slots__ = ('schema',)
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    schema: str

    def __init__(self, schema: _Optional[str]=...) -> None:
        ...

class AvroRows(_message.Message):
    __slots__ = ('serialized_binary_rows', 'row_count')
    SERIALIZED_BINARY_ROWS_FIELD_NUMBER: _ClassVar[int]
    ROW_COUNT_FIELD_NUMBER: _ClassVar[int]
    serialized_binary_rows: bytes
    row_count: int

    def __init__(self, serialized_binary_rows: _Optional[bytes]=..., row_count: _Optional[int]=...) -> None:
        ...