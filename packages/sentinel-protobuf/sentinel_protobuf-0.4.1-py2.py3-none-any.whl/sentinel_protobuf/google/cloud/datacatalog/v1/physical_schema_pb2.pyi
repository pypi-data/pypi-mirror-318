from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class PhysicalSchema(_message.Message):
    __slots__ = ('avro', 'thrift', 'protobuf', 'parquet', 'orc', 'csv')

    class AvroSchema(_message.Message):
        __slots__ = ('text',)
        TEXT_FIELD_NUMBER: _ClassVar[int]
        text: str

        def __init__(self, text: _Optional[str]=...) -> None:
            ...

    class ThriftSchema(_message.Message):
        __slots__ = ('text',)
        TEXT_FIELD_NUMBER: _ClassVar[int]
        text: str

        def __init__(self, text: _Optional[str]=...) -> None:
            ...

    class ProtobufSchema(_message.Message):
        __slots__ = ('text',)
        TEXT_FIELD_NUMBER: _ClassVar[int]
        text: str

        def __init__(self, text: _Optional[str]=...) -> None:
            ...

    class ParquetSchema(_message.Message):
        __slots__ = ()

        def __init__(self) -> None:
            ...

    class OrcSchema(_message.Message):
        __slots__ = ()

        def __init__(self) -> None:
            ...

    class CsvSchema(_message.Message):
        __slots__ = ()

        def __init__(self) -> None:
            ...
    AVRO_FIELD_NUMBER: _ClassVar[int]
    THRIFT_FIELD_NUMBER: _ClassVar[int]
    PROTOBUF_FIELD_NUMBER: _ClassVar[int]
    PARQUET_FIELD_NUMBER: _ClassVar[int]
    ORC_FIELD_NUMBER: _ClassVar[int]
    CSV_FIELD_NUMBER: _ClassVar[int]
    avro: PhysicalSchema.AvroSchema
    thrift: PhysicalSchema.ThriftSchema
    protobuf: PhysicalSchema.ProtobufSchema
    parquet: PhysicalSchema.ParquetSchema
    orc: PhysicalSchema.OrcSchema
    csv: PhysicalSchema.CsvSchema

    def __init__(self, avro: _Optional[_Union[PhysicalSchema.AvroSchema, _Mapping]]=..., thrift: _Optional[_Union[PhysicalSchema.ThriftSchema, _Mapping]]=..., protobuf: _Optional[_Union[PhysicalSchema.ProtobufSchema, _Mapping]]=..., parquet: _Optional[_Union[PhysicalSchema.ParquetSchema, _Mapping]]=..., orc: _Optional[_Union[PhysicalSchema.OrcSchema, _Mapping]]=..., csv: _Optional[_Union[PhysicalSchema.CsvSchema, _Mapping]]=...) -> None:
        ...