from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
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

class ArrowSerializationOptions(_message.Message):
    __slots__ = ('buffer_compression',)

    class CompressionCodec(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        COMPRESSION_UNSPECIFIED: _ClassVar[ArrowSerializationOptions.CompressionCodec]
        LZ4_FRAME: _ClassVar[ArrowSerializationOptions.CompressionCodec]
        ZSTD: _ClassVar[ArrowSerializationOptions.CompressionCodec]
    COMPRESSION_UNSPECIFIED: ArrowSerializationOptions.CompressionCodec
    LZ4_FRAME: ArrowSerializationOptions.CompressionCodec
    ZSTD: ArrowSerializationOptions.CompressionCodec
    BUFFER_COMPRESSION_FIELD_NUMBER: _ClassVar[int]
    buffer_compression: ArrowSerializationOptions.CompressionCodec

    def __init__(self, buffer_compression: _Optional[_Union[ArrowSerializationOptions.CompressionCodec, str]]=...) -> None:
        ...