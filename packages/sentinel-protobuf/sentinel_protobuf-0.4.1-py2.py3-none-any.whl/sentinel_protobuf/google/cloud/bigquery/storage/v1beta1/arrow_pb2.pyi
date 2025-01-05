from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class ArrowSchema(_message.Message):
    __slots__ = ('serialized_schema',)
    SERIALIZED_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    serialized_schema: bytes

    def __init__(self, serialized_schema: _Optional[bytes]=...) -> None:
        ...

class ArrowRecordBatch(_message.Message):
    __slots__ = ('serialized_record_batch', 'row_count')
    SERIALIZED_RECORD_BATCH_FIELD_NUMBER: _ClassVar[int]
    ROW_COUNT_FIELD_NUMBER: _ClassVar[int]
    serialized_record_batch: bytes
    row_count: int

    def __init__(self, serialized_record_batch: _Optional[bytes]=..., row_count: _Optional[int]=...) -> None:
        ...