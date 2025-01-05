from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.bigquery.storage.v1 import arrow_pb2 as _arrow_pb2
from google.cloud.bigquery.storage.v1 import avro_pb2 as _avro_pb2
from google.cloud.bigquery.storage.v1 import table_pb2 as _table_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DataFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DATA_FORMAT_UNSPECIFIED: _ClassVar[DataFormat]
    AVRO: _ClassVar[DataFormat]
    ARROW: _ClassVar[DataFormat]

class WriteStreamView(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    WRITE_STREAM_VIEW_UNSPECIFIED: _ClassVar[WriteStreamView]
    BASIC: _ClassVar[WriteStreamView]
    FULL: _ClassVar[WriteStreamView]
DATA_FORMAT_UNSPECIFIED: DataFormat
AVRO: DataFormat
ARROW: DataFormat
WRITE_STREAM_VIEW_UNSPECIFIED: WriteStreamView
BASIC: WriteStreamView
FULL: WriteStreamView

class ReadSession(_message.Message):
    __slots__ = ("name", "expire_time", "data_format", "avro_schema", "arrow_schema", "table", "table_modifiers", "read_options", "streams", "estimated_total_bytes_scanned", "estimated_total_physical_file_size", "estimated_row_count", "trace_id")
    class TableModifiers(_message.Message):
        __slots__ = ("snapshot_time",)
        SNAPSHOT_TIME_FIELD_NUMBER: _ClassVar[int]
        snapshot_time: _timestamp_pb2.Timestamp
        def __init__(self, snapshot_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    class TableReadOptions(_message.Message):
        __slots__ = ("selected_fields", "row_restriction", "arrow_serialization_options", "avro_serialization_options", "sample_percentage", "response_compression_codec")
        class ResponseCompressionCodec(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            RESPONSE_COMPRESSION_CODEC_UNSPECIFIED: _ClassVar[ReadSession.TableReadOptions.ResponseCompressionCodec]
            RESPONSE_COMPRESSION_CODEC_LZ4: _ClassVar[ReadSession.TableReadOptions.ResponseCompressionCodec]
        RESPONSE_COMPRESSION_CODEC_UNSPECIFIED: ReadSession.TableReadOptions.ResponseCompressionCodec
        RESPONSE_COMPRESSION_CODEC_LZ4: ReadSession.TableReadOptions.ResponseCompressionCodec
        SELECTED_FIELDS_FIELD_NUMBER: _ClassVar[int]
        ROW_RESTRICTION_FIELD_NUMBER: _ClassVar[int]
        ARROW_SERIALIZATION_OPTIONS_FIELD_NUMBER: _ClassVar[int]
        AVRO_SERIALIZATION_OPTIONS_FIELD_NUMBER: _ClassVar[int]
        SAMPLE_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
        RESPONSE_COMPRESSION_CODEC_FIELD_NUMBER: _ClassVar[int]
        selected_fields: _containers.RepeatedScalarFieldContainer[str]
        row_restriction: str
        arrow_serialization_options: _arrow_pb2.ArrowSerializationOptions
        avro_serialization_options: _avro_pb2.AvroSerializationOptions
        sample_percentage: float
        response_compression_codec: ReadSession.TableReadOptions.ResponseCompressionCodec
        def __init__(self, selected_fields: _Optional[_Iterable[str]] = ..., row_restriction: _Optional[str] = ..., arrow_serialization_options: _Optional[_Union[_arrow_pb2.ArrowSerializationOptions, _Mapping]] = ..., avro_serialization_options: _Optional[_Union[_avro_pb2.AvroSerializationOptions, _Mapping]] = ..., sample_percentage: _Optional[float] = ..., response_compression_codec: _Optional[_Union[ReadSession.TableReadOptions.ResponseCompressionCodec, str]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
    DATA_FORMAT_FIELD_NUMBER: _ClassVar[int]
    AVRO_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    ARROW_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    TABLE_FIELD_NUMBER: _ClassVar[int]
    TABLE_MODIFIERS_FIELD_NUMBER: _ClassVar[int]
    READ_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    STREAMS_FIELD_NUMBER: _ClassVar[int]
    ESTIMATED_TOTAL_BYTES_SCANNED_FIELD_NUMBER: _ClassVar[int]
    ESTIMATED_TOTAL_PHYSICAL_FILE_SIZE_FIELD_NUMBER: _ClassVar[int]
    ESTIMATED_ROW_COUNT_FIELD_NUMBER: _ClassVar[int]
    TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    expire_time: _timestamp_pb2.Timestamp
    data_format: DataFormat
    avro_schema: _avro_pb2.AvroSchema
    arrow_schema: _arrow_pb2.ArrowSchema
    table: str
    table_modifiers: ReadSession.TableModifiers
    read_options: ReadSession.TableReadOptions
    streams: _containers.RepeatedCompositeFieldContainer[ReadStream]
    estimated_total_bytes_scanned: int
    estimated_total_physical_file_size: int
    estimated_row_count: int
    trace_id: str
    def __init__(self, name: _Optional[str] = ..., expire_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., data_format: _Optional[_Union[DataFormat, str]] = ..., avro_schema: _Optional[_Union[_avro_pb2.AvroSchema, _Mapping]] = ..., arrow_schema: _Optional[_Union[_arrow_pb2.ArrowSchema, _Mapping]] = ..., table: _Optional[str] = ..., table_modifiers: _Optional[_Union[ReadSession.TableModifiers, _Mapping]] = ..., read_options: _Optional[_Union[ReadSession.TableReadOptions, _Mapping]] = ..., streams: _Optional[_Iterable[_Union[ReadStream, _Mapping]]] = ..., estimated_total_bytes_scanned: _Optional[int] = ..., estimated_total_physical_file_size: _Optional[int] = ..., estimated_row_count: _Optional[int] = ..., trace_id: _Optional[str] = ...) -> None: ...

class ReadStream(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class WriteStream(_message.Message):
    __slots__ = ("name", "type", "create_time", "commit_time", "table_schema", "write_mode", "location")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[WriteStream.Type]
        COMMITTED: _ClassVar[WriteStream.Type]
        PENDING: _ClassVar[WriteStream.Type]
        BUFFERED: _ClassVar[WriteStream.Type]
    TYPE_UNSPECIFIED: WriteStream.Type
    COMMITTED: WriteStream.Type
    PENDING: WriteStream.Type
    BUFFERED: WriteStream.Type
    class WriteMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        WRITE_MODE_UNSPECIFIED: _ClassVar[WriteStream.WriteMode]
        INSERT: _ClassVar[WriteStream.WriteMode]
    WRITE_MODE_UNSPECIFIED: WriteStream.WriteMode
    INSERT: WriteStream.WriteMode
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    COMMIT_TIME_FIELD_NUMBER: _ClassVar[int]
    TABLE_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    WRITE_MODE_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: WriteStream.Type
    create_time: _timestamp_pb2.Timestamp
    commit_time: _timestamp_pb2.Timestamp
    table_schema: _table_pb2.TableSchema
    write_mode: WriteStream.WriteMode
    location: str
    def __init__(self, name: _Optional[str] = ..., type: _Optional[_Union[WriteStream.Type, str]] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., commit_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., table_schema: _Optional[_Union[_table_pb2.TableSchema, _Mapping]] = ..., write_mode: _Optional[_Union[WriteStream.WriteMode, str]] = ..., location: _Optional[str] = ...) -> None: ...
