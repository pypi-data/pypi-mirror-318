from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.bigquery.storage.v1beta1 import arrow_pb2 as _arrow_pb2
from google.cloud.bigquery.storage.v1beta1 import avro_pb2 as _avro_pb2
from google.cloud.bigquery.storage.v1beta1 import read_options_pb2 as _read_options_pb2
from google.cloud.bigquery.storage.v1beta1 import table_reference_pb2 as _table_reference_pb2
from google.protobuf import empty_pb2 as _empty_pb2
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

class ShardingStrategy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SHARDING_STRATEGY_UNSPECIFIED: _ClassVar[ShardingStrategy]
    LIQUID: _ClassVar[ShardingStrategy]
    BALANCED: _ClassVar[ShardingStrategy]
DATA_FORMAT_UNSPECIFIED: DataFormat
AVRO: DataFormat
ARROW: DataFormat
SHARDING_STRATEGY_UNSPECIFIED: ShardingStrategy
LIQUID: ShardingStrategy
BALANCED: ShardingStrategy

class Stream(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class StreamPosition(_message.Message):
    __slots__ = ('stream', 'offset')
    STREAM_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    stream: Stream
    offset: int

    def __init__(self, stream: _Optional[_Union[Stream, _Mapping]]=..., offset: _Optional[int]=...) -> None:
        ...

class ReadSession(_message.Message):
    __slots__ = ('name', 'expire_time', 'avro_schema', 'arrow_schema', 'streams', 'table_reference', 'table_modifiers', 'sharding_strategy')
    NAME_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
    AVRO_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    ARROW_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    STREAMS_FIELD_NUMBER: _ClassVar[int]
    TABLE_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    TABLE_MODIFIERS_FIELD_NUMBER: _ClassVar[int]
    SHARDING_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    name: str
    expire_time: _timestamp_pb2.Timestamp
    avro_schema: _avro_pb2.AvroSchema
    arrow_schema: _arrow_pb2.ArrowSchema
    streams: _containers.RepeatedCompositeFieldContainer[Stream]
    table_reference: _table_reference_pb2.TableReference
    table_modifiers: _table_reference_pb2.TableModifiers
    sharding_strategy: ShardingStrategy

    def __init__(self, name: _Optional[str]=..., expire_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., avro_schema: _Optional[_Union[_avro_pb2.AvroSchema, _Mapping]]=..., arrow_schema: _Optional[_Union[_arrow_pb2.ArrowSchema, _Mapping]]=..., streams: _Optional[_Iterable[_Union[Stream, _Mapping]]]=..., table_reference: _Optional[_Union[_table_reference_pb2.TableReference, _Mapping]]=..., table_modifiers: _Optional[_Union[_table_reference_pb2.TableModifiers, _Mapping]]=..., sharding_strategy: _Optional[_Union[ShardingStrategy, str]]=...) -> None:
        ...

class CreateReadSessionRequest(_message.Message):
    __slots__ = ('table_reference', 'parent', 'table_modifiers', 'requested_streams', 'read_options', 'format', 'sharding_strategy')
    TABLE_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TABLE_MODIFIERS_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_STREAMS_FIELD_NUMBER: _ClassVar[int]
    READ_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    SHARDING_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    table_reference: _table_reference_pb2.TableReference
    parent: str
    table_modifiers: _table_reference_pb2.TableModifiers
    requested_streams: int
    read_options: _read_options_pb2.TableReadOptions
    format: DataFormat
    sharding_strategy: ShardingStrategy

    def __init__(self, table_reference: _Optional[_Union[_table_reference_pb2.TableReference, _Mapping]]=..., parent: _Optional[str]=..., table_modifiers: _Optional[_Union[_table_reference_pb2.TableModifiers, _Mapping]]=..., requested_streams: _Optional[int]=..., read_options: _Optional[_Union[_read_options_pb2.TableReadOptions, _Mapping]]=..., format: _Optional[_Union[DataFormat, str]]=..., sharding_strategy: _Optional[_Union[ShardingStrategy, str]]=...) -> None:
        ...

class ReadRowsRequest(_message.Message):
    __slots__ = ('read_position',)
    READ_POSITION_FIELD_NUMBER: _ClassVar[int]
    read_position: StreamPosition

    def __init__(self, read_position: _Optional[_Union[StreamPosition, _Mapping]]=...) -> None:
        ...

class StreamStatus(_message.Message):
    __slots__ = ('estimated_row_count', 'fraction_consumed', 'progress', 'is_splittable')
    ESTIMATED_ROW_COUNT_FIELD_NUMBER: _ClassVar[int]
    FRACTION_CONSUMED_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    IS_SPLITTABLE_FIELD_NUMBER: _ClassVar[int]
    estimated_row_count: int
    fraction_consumed: float
    progress: Progress
    is_splittable: bool

    def __init__(self, estimated_row_count: _Optional[int]=..., fraction_consumed: _Optional[float]=..., progress: _Optional[_Union[Progress, _Mapping]]=..., is_splittable: bool=...) -> None:
        ...

class Progress(_message.Message):
    __slots__ = ('at_response_start', 'at_response_end')
    AT_RESPONSE_START_FIELD_NUMBER: _ClassVar[int]
    AT_RESPONSE_END_FIELD_NUMBER: _ClassVar[int]
    at_response_start: float
    at_response_end: float

    def __init__(self, at_response_start: _Optional[float]=..., at_response_end: _Optional[float]=...) -> None:
        ...

class ThrottleStatus(_message.Message):
    __slots__ = ('throttle_percent',)
    THROTTLE_PERCENT_FIELD_NUMBER: _ClassVar[int]
    throttle_percent: int

    def __init__(self, throttle_percent: _Optional[int]=...) -> None:
        ...

class ReadRowsResponse(_message.Message):
    __slots__ = ('avro_rows', 'arrow_record_batch', 'row_count', 'status', 'throttle_status', 'avro_schema', 'arrow_schema')
    AVRO_ROWS_FIELD_NUMBER: _ClassVar[int]
    ARROW_RECORD_BATCH_FIELD_NUMBER: _ClassVar[int]
    ROW_COUNT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    THROTTLE_STATUS_FIELD_NUMBER: _ClassVar[int]
    AVRO_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    ARROW_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    avro_rows: _avro_pb2.AvroRows
    arrow_record_batch: _arrow_pb2.ArrowRecordBatch
    row_count: int
    status: StreamStatus
    throttle_status: ThrottleStatus
    avro_schema: _avro_pb2.AvroSchema
    arrow_schema: _arrow_pb2.ArrowSchema

    def __init__(self, avro_rows: _Optional[_Union[_avro_pb2.AvroRows, _Mapping]]=..., arrow_record_batch: _Optional[_Union[_arrow_pb2.ArrowRecordBatch, _Mapping]]=..., row_count: _Optional[int]=..., status: _Optional[_Union[StreamStatus, _Mapping]]=..., throttle_status: _Optional[_Union[ThrottleStatus, _Mapping]]=..., avro_schema: _Optional[_Union[_avro_pb2.AvroSchema, _Mapping]]=..., arrow_schema: _Optional[_Union[_arrow_pb2.ArrowSchema, _Mapping]]=...) -> None:
        ...

class BatchCreateReadSessionStreamsRequest(_message.Message):
    __slots__ = ('session', 'requested_streams')
    SESSION_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_STREAMS_FIELD_NUMBER: _ClassVar[int]
    session: ReadSession
    requested_streams: int

    def __init__(self, session: _Optional[_Union[ReadSession, _Mapping]]=..., requested_streams: _Optional[int]=...) -> None:
        ...

class BatchCreateReadSessionStreamsResponse(_message.Message):
    __slots__ = ('streams',)
    STREAMS_FIELD_NUMBER: _ClassVar[int]
    streams: _containers.RepeatedCompositeFieldContainer[Stream]

    def __init__(self, streams: _Optional[_Iterable[_Union[Stream, _Mapping]]]=...) -> None:
        ...

class FinalizeStreamRequest(_message.Message):
    __slots__ = ('stream',)
    STREAM_FIELD_NUMBER: _ClassVar[int]
    stream: Stream

    def __init__(self, stream: _Optional[_Union[Stream, _Mapping]]=...) -> None:
        ...

class SplitReadStreamRequest(_message.Message):
    __slots__ = ('original_stream', 'fraction')
    ORIGINAL_STREAM_FIELD_NUMBER: _ClassVar[int]
    FRACTION_FIELD_NUMBER: _ClassVar[int]
    original_stream: Stream
    fraction: float

    def __init__(self, original_stream: _Optional[_Union[Stream, _Mapping]]=..., fraction: _Optional[float]=...) -> None:
        ...

class SplitReadStreamResponse(_message.Message):
    __slots__ = ('primary_stream', 'remainder_stream')
    PRIMARY_STREAM_FIELD_NUMBER: _ClassVar[int]
    REMAINDER_STREAM_FIELD_NUMBER: _ClassVar[int]
    primary_stream: Stream
    remainder_stream: Stream

    def __init__(self, primary_stream: _Optional[_Union[Stream, _Mapping]]=..., remainder_stream: _Optional[_Union[Stream, _Mapping]]=...) -> None:
        ...