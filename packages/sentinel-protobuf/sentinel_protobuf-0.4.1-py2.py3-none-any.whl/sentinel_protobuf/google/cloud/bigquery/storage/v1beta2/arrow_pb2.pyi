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
    __slots__ = ('serialized_record_batch',)
    SERIALIZED_RECORD_BATCH_FIELD_NUMBER: _ClassVar[int]
    serialized_record_batch: bytes

    def __init__(self, serialized_record_batch: _Optional[bytes]=...) -> None:
        ...

class ArrowSerializationOptions(_message.Message):
    __slots__ = ('format',)

    class Format(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FORMAT_UNSPECIFIED: _ClassVar[ArrowSerializationOptions.Format]
        ARROW_0_14: _ClassVar[ArrowSerializationOptions.Format]
        ARROW_0_15: _ClassVar[ArrowSerializationOptions.Format]
    FORMAT_UNSPECIFIED: ArrowSerializationOptions.Format
    ARROW_0_14: ArrowSerializationOptions.Format
    ARROW_0_15: ArrowSerializationOptions.Format
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    format: ArrowSerializationOptions.Format

    def __init__(self, format: _Optional[_Union[ArrowSerializationOptions.Format, str]]=...) -> None:
        ...