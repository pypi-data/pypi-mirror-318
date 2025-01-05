from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.bigquery.storage.v1beta2 import arrow_pb2 as _arrow_pb2
from google.cloud.bigquery.storage.v1beta2 import avro_pb2 as _avro_pb2
from google.cloud.bigquery.storage.v1beta2 import protobuf_pb2 as _protobuf_pb2
from google.cloud.bigquery.storage.v1beta2 import stream_pb2 as _stream_pb2
from google.cloud.bigquery.storage.v1beta2 import table_pb2 as _table_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CreateReadSessionRequest(_message.Message):
    __slots__ = ('parent', 'read_session', 'max_stream_count')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    READ_SESSION_FIELD_NUMBER: _ClassVar[int]
    MAX_STREAM_COUNT_FIELD_NUMBER: _ClassVar[int]
    parent: str
    read_session: _stream_pb2.ReadSession
    max_stream_count: int

    def __init__(self, parent: _Optional[str]=..., read_session: _Optional[_Union[_stream_pb2.ReadSession, _Mapping]]=..., max_stream_count: _Optional[int]=...) -> None:
        ...

class ReadRowsRequest(_message.Message):
    __slots__ = ('read_stream', 'offset')
    READ_STREAM_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    read_stream: str
    offset: int

    def __init__(self, read_stream: _Optional[str]=..., offset: _Optional[int]=...) -> None:
        ...

class ThrottleState(_message.Message):
    __slots__ = ('throttle_percent',)
    THROTTLE_PERCENT_FIELD_NUMBER: _ClassVar[int]
    throttle_percent: int

    def __init__(self, throttle_percent: _Optional[int]=...) -> None:
        ...

class StreamStats(_message.Message):
    __slots__ = ('progress',)

    class Progress(_message.Message):
        __slots__ = ('at_response_start', 'at_response_end')
        AT_RESPONSE_START_FIELD_NUMBER: _ClassVar[int]
        AT_RESPONSE_END_FIELD_NUMBER: _ClassVar[int]
        at_response_start: float
        at_response_end: float

        def __init__(self, at_response_start: _Optional[float]=..., at_response_end: _Optional[float]=...) -> None:
            ...
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    progress: StreamStats.Progress

    def __init__(self, progress: _Optional[_Union[StreamStats.Progress, _Mapping]]=...) -> None:
        ...

class ReadRowsResponse(_message.Message):
    __slots__ = ('avro_rows', 'arrow_record_batch', 'row_count', 'stats', 'throttle_state', 'avro_schema', 'arrow_schema')
    AVRO_ROWS_FIELD_NUMBER: _ClassVar[int]
    ARROW_RECORD_BATCH_FIELD_NUMBER: _ClassVar[int]
    ROW_COUNT_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    THROTTLE_STATE_FIELD_NUMBER: _ClassVar[int]
    AVRO_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    ARROW_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    avro_rows: _avro_pb2.AvroRows
    arrow_record_batch: _arrow_pb2.ArrowRecordBatch
    row_count: int
    stats: StreamStats
    throttle_state: ThrottleState
    avro_schema: _avro_pb2.AvroSchema
    arrow_schema: _arrow_pb2.ArrowSchema

    def __init__(self, avro_rows: _Optional[_Union[_avro_pb2.AvroRows, _Mapping]]=..., arrow_record_batch: _Optional[_Union[_arrow_pb2.ArrowRecordBatch, _Mapping]]=..., row_count: _Optional[int]=..., stats: _Optional[_Union[StreamStats, _Mapping]]=..., throttle_state: _Optional[_Union[ThrottleState, _Mapping]]=..., avro_schema: _Optional[_Union[_avro_pb2.AvroSchema, _Mapping]]=..., arrow_schema: _Optional[_Union[_arrow_pb2.ArrowSchema, _Mapping]]=...) -> None:
        ...

class SplitReadStreamRequest(_message.Message):
    __slots__ = ('name', 'fraction')
    NAME_FIELD_NUMBER: _ClassVar[int]
    FRACTION_FIELD_NUMBER: _ClassVar[int]
    name: str
    fraction: float

    def __init__(self, name: _Optional[str]=..., fraction: _Optional[float]=...) -> None:
        ...

class SplitReadStreamResponse(_message.Message):
    __slots__ = ('primary_stream', 'remainder_stream')
    PRIMARY_STREAM_FIELD_NUMBER: _ClassVar[int]
    REMAINDER_STREAM_FIELD_NUMBER: _ClassVar[int]
    primary_stream: _stream_pb2.ReadStream
    remainder_stream: _stream_pb2.ReadStream

    def __init__(self, primary_stream: _Optional[_Union[_stream_pb2.ReadStream, _Mapping]]=..., remainder_stream: _Optional[_Union[_stream_pb2.ReadStream, _Mapping]]=...) -> None:
        ...

class CreateWriteStreamRequest(_message.Message):
    __slots__ = ('parent', 'write_stream')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    WRITE_STREAM_FIELD_NUMBER: _ClassVar[int]
    parent: str
    write_stream: _stream_pb2.WriteStream

    def __init__(self, parent: _Optional[str]=..., write_stream: _Optional[_Union[_stream_pb2.WriteStream, _Mapping]]=...) -> None:
        ...

class AppendRowsRequest(_message.Message):
    __slots__ = ('write_stream', 'offset', 'proto_rows', 'trace_id')

    class ProtoData(_message.Message):
        __slots__ = ('writer_schema', 'rows')
        WRITER_SCHEMA_FIELD_NUMBER: _ClassVar[int]
        ROWS_FIELD_NUMBER: _ClassVar[int]
        writer_schema: _protobuf_pb2.ProtoSchema
        rows: _protobuf_pb2.ProtoRows

        def __init__(self, writer_schema: _Optional[_Union[_protobuf_pb2.ProtoSchema, _Mapping]]=..., rows: _Optional[_Union[_protobuf_pb2.ProtoRows, _Mapping]]=...) -> None:
            ...
    WRITE_STREAM_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    PROTO_ROWS_FIELD_NUMBER: _ClassVar[int]
    TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    write_stream: str
    offset: _wrappers_pb2.Int64Value
    proto_rows: AppendRowsRequest.ProtoData
    trace_id: str

    def __init__(self, write_stream: _Optional[str]=..., offset: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]]=..., proto_rows: _Optional[_Union[AppendRowsRequest.ProtoData, _Mapping]]=..., trace_id: _Optional[str]=...) -> None:
        ...

class AppendRowsResponse(_message.Message):
    __slots__ = ('append_result', 'error', 'updated_schema')

    class AppendResult(_message.Message):
        __slots__ = ('offset',)
        OFFSET_FIELD_NUMBER: _ClassVar[int]
        offset: _wrappers_pb2.Int64Value

        def __init__(self, offset: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]]=...) -> None:
            ...
    APPEND_RESULT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    UPDATED_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    append_result: AppendRowsResponse.AppendResult
    error: _status_pb2.Status
    updated_schema: _table_pb2.TableSchema

    def __init__(self, append_result: _Optional[_Union[AppendRowsResponse.AppendResult, _Mapping]]=..., error: _Optional[_Union[_status_pb2.Status, _Mapping]]=..., updated_schema: _Optional[_Union[_table_pb2.TableSchema, _Mapping]]=...) -> None:
        ...

class GetWriteStreamRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class BatchCommitWriteStreamsRequest(_message.Message):
    __slots__ = ('parent', 'write_streams')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    WRITE_STREAMS_FIELD_NUMBER: _ClassVar[int]
    parent: str
    write_streams: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, parent: _Optional[str]=..., write_streams: _Optional[_Iterable[str]]=...) -> None:
        ...

class BatchCommitWriteStreamsResponse(_message.Message):
    __slots__ = ('commit_time', 'stream_errors')
    COMMIT_TIME_FIELD_NUMBER: _ClassVar[int]
    STREAM_ERRORS_FIELD_NUMBER: _ClassVar[int]
    commit_time: _timestamp_pb2.Timestamp
    stream_errors: _containers.RepeatedCompositeFieldContainer[StorageError]

    def __init__(self, commit_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., stream_errors: _Optional[_Iterable[_Union[StorageError, _Mapping]]]=...) -> None:
        ...

class FinalizeWriteStreamRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class FinalizeWriteStreamResponse(_message.Message):
    __slots__ = ('row_count',)
    ROW_COUNT_FIELD_NUMBER: _ClassVar[int]
    row_count: int

    def __init__(self, row_count: _Optional[int]=...) -> None:
        ...

class FlushRowsRequest(_message.Message):
    __slots__ = ('write_stream', 'offset')
    WRITE_STREAM_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    write_stream: str
    offset: _wrappers_pb2.Int64Value

    def __init__(self, write_stream: _Optional[str]=..., offset: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]]=...) -> None:
        ...

class FlushRowsResponse(_message.Message):
    __slots__ = ('offset',)
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    offset: int

    def __init__(self, offset: _Optional[int]=...) -> None:
        ...

class StorageError(_message.Message):
    __slots__ = ('code', 'entity', 'error_message')

    class StorageErrorCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STORAGE_ERROR_CODE_UNSPECIFIED: _ClassVar[StorageError.StorageErrorCode]
        TABLE_NOT_FOUND: _ClassVar[StorageError.StorageErrorCode]
        STREAM_ALREADY_COMMITTED: _ClassVar[StorageError.StorageErrorCode]
        STREAM_NOT_FOUND: _ClassVar[StorageError.StorageErrorCode]
        INVALID_STREAM_TYPE: _ClassVar[StorageError.StorageErrorCode]
        INVALID_STREAM_STATE: _ClassVar[StorageError.StorageErrorCode]
        STREAM_FINALIZED: _ClassVar[StorageError.StorageErrorCode]
    STORAGE_ERROR_CODE_UNSPECIFIED: StorageError.StorageErrorCode
    TABLE_NOT_FOUND: StorageError.StorageErrorCode
    STREAM_ALREADY_COMMITTED: StorageError.StorageErrorCode
    STREAM_NOT_FOUND: StorageError.StorageErrorCode
    INVALID_STREAM_TYPE: StorageError.StorageErrorCode
    INVALID_STREAM_STATE: StorageError.StorageErrorCode
    STREAM_FINALIZED: StorageError.StorageErrorCode
    CODE_FIELD_NUMBER: _ClassVar[int]
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    code: StorageError.StorageErrorCode
    entity: str
    error_message: str

    def __init__(self, code: _Optional[_Union[StorageError.StorageErrorCode, str]]=..., entity: _Optional[str]=..., error_message: _Optional[str]=...) -> None:
        ...