from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.api import routing_pb2 as _routing_pb2
from google.bigtable.v2 import data_pb2 as _data_pb2
from google.bigtable.v2 import request_stats_pb2 as _request_stats_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ReadRowsRequest(_message.Message):
    __slots__ = ("table_name", "authorized_view_name", "app_profile_id", "rows", "filter", "rows_limit", "request_stats_view", "reversed")
    class RequestStatsView(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        REQUEST_STATS_VIEW_UNSPECIFIED: _ClassVar[ReadRowsRequest.RequestStatsView]
        REQUEST_STATS_NONE: _ClassVar[ReadRowsRequest.RequestStatsView]
        REQUEST_STATS_FULL: _ClassVar[ReadRowsRequest.RequestStatsView]
    REQUEST_STATS_VIEW_UNSPECIFIED: ReadRowsRequest.RequestStatsView
    REQUEST_STATS_NONE: ReadRowsRequest.RequestStatsView
    REQUEST_STATS_FULL: ReadRowsRequest.RequestStatsView
    TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZED_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    APP_PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    ROWS_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ROWS_LIMIT_FIELD_NUMBER: _ClassVar[int]
    REQUEST_STATS_VIEW_FIELD_NUMBER: _ClassVar[int]
    REVERSED_FIELD_NUMBER: _ClassVar[int]
    table_name: str
    authorized_view_name: str
    app_profile_id: str
    rows: _data_pb2.RowSet
    filter: _data_pb2.RowFilter
    rows_limit: int
    request_stats_view: ReadRowsRequest.RequestStatsView
    reversed: bool
    def __init__(self, table_name: _Optional[str] = ..., authorized_view_name: _Optional[str] = ..., app_profile_id: _Optional[str] = ..., rows: _Optional[_Union[_data_pb2.RowSet, _Mapping]] = ..., filter: _Optional[_Union[_data_pb2.RowFilter, _Mapping]] = ..., rows_limit: _Optional[int] = ..., request_stats_view: _Optional[_Union[ReadRowsRequest.RequestStatsView, str]] = ..., reversed: bool = ...) -> None: ...

class ReadRowsResponse(_message.Message):
    __slots__ = ("chunks", "last_scanned_row_key", "request_stats")
    class CellChunk(_message.Message):
        __slots__ = ("row_key", "family_name", "qualifier", "timestamp_micros", "labels", "value", "value_size", "reset_row", "commit_row")
        ROW_KEY_FIELD_NUMBER: _ClassVar[int]
        FAMILY_NAME_FIELD_NUMBER: _ClassVar[int]
        QUALIFIER_FIELD_NUMBER: _ClassVar[int]
        TIMESTAMP_MICROS_FIELD_NUMBER: _ClassVar[int]
        LABELS_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        VALUE_SIZE_FIELD_NUMBER: _ClassVar[int]
        RESET_ROW_FIELD_NUMBER: _ClassVar[int]
        COMMIT_ROW_FIELD_NUMBER: _ClassVar[int]
        row_key: bytes
        family_name: _wrappers_pb2.StringValue
        qualifier: _wrappers_pb2.BytesValue
        timestamp_micros: int
        labels: _containers.RepeatedScalarFieldContainer[str]
        value: bytes
        value_size: int
        reset_row: bool
        commit_row: bool
        def __init__(self, row_key: _Optional[bytes] = ..., family_name: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., qualifier: _Optional[_Union[_wrappers_pb2.BytesValue, _Mapping]] = ..., timestamp_micros: _Optional[int] = ..., labels: _Optional[_Iterable[str]] = ..., value: _Optional[bytes] = ..., value_size: _Optional[int] = ..., reset_row: bool = ..., commit_row: bool = ...) -> None: ...
    CHUNKS_FIELD_NUMBER: _ClassVar[int]
    LAST_SCANNED_ROW_KEY_FIELD_NUMBER: _ClassVar[int]
    REQUEST_STATS_FIELD_NUMBER: _ClassVar[int]
    chunks: _containers.RepeatedCompositeFieldContainer[ReadRowsResponse.CellChunk]
    last_scanned_row_key: bytes
    request_stats: _request_stats_pb2.RequestStats
    def __init__(self, chunks: _Optional[_Iterable[_Union[ReadRowsResponse.CellChunk, _Mapping]]] = ..., last_scanned_row_key: _Optional[bytes] = ..., request_stats: _Optional[_Union[_request_stats_pb2.RequestStats, _Mapping]] = ...) -> None: ...

class SampleRowKeysRequest(_message.Message):
    __slots__ = ("table_name", "authorized_view_name", "app_profile_id")
    TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZED_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    APP_PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    table_name: str
    authorized_view_name: str
    app_profile_id: str
    def __init__(self, table_name: _Optional[str] = ..., authorized_view_name: _Optional[str] = ..., app_profile_id: _Optional[str] = ...) -> None: ...

class SampleRowKeysResponse(_message.Message):
    __slots__ = ("row_key", "offset_bytes")
    ROW_KEY_FIELD_NUMBER: _ClassVar[int]
    OFFSET_BYTES_FIELD_NUMBER: _ClassVar[int]
    row_key: bytes
    offset_bytes: int
    def __init__(self, row_key: _Optional[bytes] = ..., offset_bytes: _Optional[int] = ...) -> None: ...

class MutateRowRequest(_message.Message):
    __slots__ = ("table_name", "authorized_view_name", "app_profile_id", "row_key", "mutations")
    TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZED_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    APP_PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    ROW_KEY_FIELD_NUMBER: _ClassVar[int]
    MUTATIONS_FIELD_NUMBER: _ClassVar[int]
    table_name: str
    authorized_view_name: str
    app_profile_id: str
    row_key: bytes
    mutations: _containers.RepeatedCompositeFieldContainer[_data_pb2.Mutation]
    def __init__(self, table_name: _Optional[str] = ..., authorized_view_name: _Optional[str] = ..., app_profile_id: _Optional[str] = ..., row_key: _Optional[bytes] = ..., mutations: _Optional[_Iterable[_Union[_data_pb2.Mutation, _Mapping]]] = ...) -> None: ...

class MutateRowResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MutateRowsRequest(_message.Message):
    __slots__ = ("table_name", "authorized_view_name", "app_profile_id", "entries")
    class Entry(_message.Message):
        __slots__ = ("row_key", "mutations")
        ROW_KEY_FIELD_NUMBER: _ClassVar[int]
        MUTATIONS_FIELD_NUMBER: _ClassVar[int]
        row_key: bytes
        mutations: _containers.RepeatedCompositeFieldContainer[_data_pb2.Mutation]
        def __init__(self, row_key: _Optional[bytes] = ..., mutations: _Optional[_Iterable[_Union[_data_pb2.Mutation, _Mapping]]] = ...) -> None: ...
    TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZED_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    APP_PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    table_name: str
    authorized_view_name: str
    app_profile_id: str
    entries: _containers.RepeatedCompositeFieldContainer[MutateRowsRequest.Entry]
    def __init__(self, table_name: _Optional[str] = ..., authorized_view_name: _Optional[str] = ..., app_profile_id: _Optional[str] = ..., entries: _Optional[_Iterable[_Union[MutateRowsRequest.Entry, _Mapping]]] = ...) -> None: ...

class MutateRowsResponse(_message.Message):
    __slots__ = ("entries", "rate_limit_info")
    class Entry(_message.Message):
        __slots__ = ("index", "status")
        INDEX_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        index: int
        status: _status_pb2.Status
        def __init__(self, index: _Optional[int] = ..., status: _Optional[_Union[_status_pb2.Status, _Mapping]] = ...) -> None: ...
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    RATE_LIMIT_INFO_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.RepeatedCompositeFieldContainer[MutateRowsResponse.Entry]
    rate_limit_info: RateLimitInfo
    def __init__(self, entries: _Optional[_Iterable[_Union[MutateRowsResponse.Entry, _Mapping]]] = ..., rate_limit_info: _Optional[_Union[RateLimitInfo, _Mapping]] = ...) -> None: ...

class RateLimitInfo(_message.Message):
    __slots__ = ("period", "factor")
    PERIOD_FIELD_NUMBER: _ClassVar[int]
    FACTOR_FIELD_NUMBER: _ClassVar[int]
    period: _duration_pb2.Duration
    factor: float
    def __init__(self, period: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., factor: _Optional[float] = ...) -> None: ...

class CheckAndMutateRowRequest(_message.Message):
    __slots__ = ("table_name", "authorized_view_name", "app_profile_id", "row_key", "predicate_filter", "true_mutations", "false_mutations")
    TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZED_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    APP_PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    ROW_KEY_FIELD_NUMBER: _ClassVar[int]
    PREDICATE_FILTER_FIELD_NUMBER: _ClassVar[int]
    TRUE_MUTATIONS_FIELD_NUMBER: _ClassVar[int]
    FALSE_MUTATIONS_FIELD_NUMBER: _ClassVar[int]
    table_name: str
    authorized_view_name: str
    app_profile_id: str
    row_key: bytes
    predicate_filter: _data_pb2.RowFilter
    true_mutations: _containers.RepeatedCompositeFieldContainer[_data_pb2.Mutation]
    false_mutations: _containers.RepeatedCompositeFieldContainer[_data_pb2.Mutation]
    def __init__(self, table_name: _Optional[str] = ..., authorized_view_name: _Optional[str] = ..., app_profile_id: _Optional[str] = ..., row_key: _Optional[bytes] = ..., predicate_filter: _Optional[_Union[_data_pb2.RowFilter, _Mapping]] = ..., true_mutations: _Optional[_Iterable[_Union[_data_pb2.Mutation, _Mapping]]] = ..., false_mutations: _Optional[_Iterable[_Union[_data_pb2.Mutation, _Mapping]]] = ...) -> None: ...

class CheckAndMutateRowResponse(_message.Message):
    __slots__ = ("predicate_matched",)
    PREDICATE_MATCHED_FIELD_NUMBER: _ClassVar[int]
    predicate_matched: bool
    def __init__(self, predicate_matched: bool = ...) -> None: ...

class PingAndWarmRequest(_message.Message):
    __slots__ = ("name", "app_profile_id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    APP_PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    app_profile_id: str
    def __init__(self, name: _Optional[str] = ..., app_profile_id: _Optional[str] = ...) -> None: ...

class PingAndWarmResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ReadModifyWriteRowRequest(_message.Message):
    __slots__ = ("table_name", "authorized_view_name", "app_profile_id", "row_key", "rules")
    TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZED_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    APP_PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    ROW_KEY_FIELD_NUMBER: _ClassVar[int]
    RULES_FIELD_NUMBER: _ClassVar[int]
    table_name: str
    authorized_view_name: str
    app_profile_id: str
    row_key: bytes
    rules: _containers.RepeatedCompositeFieldContainer[_data_pb2.ReadModifyWriteRule]
    def __init__(self, table_name: _Optional[str] = ..., authorized_view_name: _Optional[str] = ..., app_profile_id: _Optional[str] = ..., row_key: _Optional[bytes] = ..., rules: _Optional[_Iterable[_Union[_data_pb2.ReadModifyWriteRule, _Mapping]]] = ...) -> None: ...

class ReadModifyWriteRowResponse(_message.Message):
    __slots__ = ("row",)
    ROW_FIELD_NUMBER: _ClassVar[int]
    row: _data_pb2.Row
    def __init__(self, row: _Optional[_Union[_data_pb2.Row, _Mapping]] = ...) -> None: ...

class GenerateInitialChangeStreamPartitionsRequest(_message.Message):
    __slots__ = ("table_name", "app_profile_id")
    TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    APP_PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    table_name: str
    app_profile_id: str
    def __init__(self, table_name: _Optional[str] = ..., app_profile_id: _Optional[str] = ...) -> None: ...

class GenerateInitialChangeStreamPartitionsResponse(_message.Message):
    __slots__ = ("partition",)
    PARTITION_FIELD_NUMBER: _ClassVar[int]
    partition: _data_pb2.StreamPartition
    def __init__(self, partition: _Optional[_Union[_data_pb2.StreamPartition, _Mapping]] = ...) -> None: ...

class ReadChangeStreamRequest(_message.Message):
    __slots__ = ("table_name", "app_profile_id", "partition", "start_time", "continuation_tokens", "end_time", "heartbeat_duration")
    TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    APP_PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    PARTITION_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    CONTINUATION_TOKENS_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    HEARTBEAT_DURATION_FIELD_NUMBER: _ClassVar[int]
    table_name: str
    app_profile_id: str
    partition: _data_pb2.StreamPartition
    start_time: _timestamp_pb2.Timestamp
    continuation_tokens: _data_pb2.StreamContinuationTokens
    end_time: _timestamp_pb2.Timestamp
    heartbeat_duration: _duration_pb2.Duration
    def __init__(self, table_name: _Optional[str] = ..., app_profile_id: _Optional[str] = ..., partition: _Optional[_Union[_data_pb2.StreamPartition, _Mapping]] = ..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., continuation_tokens: _Optional[_Union[_data_pb2.StreamContinuationTokens, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., heartbeat_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...

class ReadChangeStreamResponse(_message.Message):
    __slots__ = ("data_change", "heartbeat", "close_stream")
    class MutationChunk(_message.Message):
        __slots__ = ("chunk_info", "mutation")
        class ChunkInfo(_message.Message):
            __slots__ = ("chunked_value_size", "chunked_value_offset", "last_chunk")
            CHUNKED_VALUE_SIZE_FIELD_NUMBER: _ClassVar[int]
            CHUNKED_VALUE_OFFSET_FIELD_NUMBER: _ClassVar[int]
            LAST_CHUNK_FIELD_NUMBER: _ClassVar[int]
            chunked_value_size: int
            chunked_value_offset: int
            last_chunk: bool
            def __init__(self, chunked_value_size: _Optional[int] = ..., chunked_value_offset: _Optional[int] = ..., last_chunk: bool = ...) -> None: ...
        CHUNK_INFO_FIELD_NUMBER: _ClassVar[int]
        MUTATION_FIELD_NUMBER: _ClassVar[int]
        chunk_info: ReadChangeStreamResponse.MutationChunk.ChunkInfo
        mutation: _data_pb2.Mutation
        def __init__(self, chunk_info: _Optional[_Union[ReadChangeStreamResponse.MutationChunk.ChunkInfo, _Mapping]] = ..., mutation: _Optional[_Union[_data_pb2.Mutation, _Mapping]] = ...) -> None: ...
    class DataChange(_message.Message):
        __slots__ = ("type", "source_cluster_id", "row_key", "commit_timestamp", "tiebreaker", "chunks", "done", "token", "estimated_low_watermark")
        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            TYPE_UNSPECIFIED: _ClassVar[ReadChangeStreamResponse.DataChange.Type]
            USER: _ClassVar[ReadChangeStreamResponse.DataChange.Type]
            GARBAGE_COLLECTION: _ClassVar[ReadChangeStreamResponse.DataChange.Type]
            CONTINUATION: _ClassVar[ReadChangeStreamResponse.DataChange.Type]
        TYPE_UNSPECIFIED: ReadChangeStreamResponse.DataChange.Type
        USER: ReadChangeStreamResponse.DataChange.Type
        GARBAGE_COLLECTION: ReadChangeStreamResponse.DataChange.Type
        CONTINUATION: ReadChangeStreamResponse.DataChange.Type
        TYPE_FIELD_NUMBER: _ClassVar[int]
        SOURCE_CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
        ROW_KEY_FIELD_NUMBER: _ClassVar[int]
        COMMIT_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        TIEBREAKER_FIELD_NUMBER: _ClassVar[int]
        CHUNKS_FIELD_NUMBER: _ClassVar[int]
        DONE_FIELD_NUMBER: _ClassVar[int]
        TOKEN_FIELD_NUMBER: _ClassVar[int]
        ESTIMATED_LOW_WATERMARK_FIELD_NUMBER: _ClassVar[int]
        type: ReadChangeStreamResponse.DataChange.Type
        source_cluster_id: str
        row_key: bytes
        commit_timestamp: _timestamp_pb2.Timestamp
        tiebreaker: int
        chunks: _containers.RepeatedCompositeFieldContainer[ReadChangeStreamResponse.MutationChunk]
        done: bool
        token: str
        estimated_low_watermark: _timestamp_pb2.Timestamp
        def __init__(self, type: _Optional[_Union[ReadChangeStreamResponse.DataChange.Type, str]] = ..., source_cluster_id: _Optional[str] = ..., row_key: _Optional[bytes] = ..., commit_timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., tiebreaker: _Optional[int] = ..., chunks: _Optional[_Iterable[_Union[ReadChangeStreamResponse.MutationChunk, _Mapping]]] = ..., done: bool = ..., token: _Optional[str] = ..., estimated_low_watermark: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    class Heartbeat(_message.Message):
        __slots__ = ("continuation_token", "estimated_low_watermark")
        CONTINUATION_TOKEN_FIELD_NUMBER: _ClassVar[int]
        ESTIMATED_LOW_WATERMARK_FIELD_NUMBER: _ClassVar[int]
        continuation_token: _data_pb2.StreamContinuationToken
        estimated_low_watermark: _timestamp_pb2.Timestamp
        def __init__(self, continuation_token: _Optional[_Union[_data_pb2.StreamContinuationToken, _Mapping]] = ..., estimated_low_watermark: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    class CloseStream(_message.Message):
        __slots__ = ("status", "continuation_tokens", "new_partitions")
        STATUS_FIELD_NUMBER: _ClassVar[int]
        CONTINUATION_TOKENS_FIELD_NUMBER: _ClassVar[int]
        NEW_PARTITIONS_FIELD_NUMBER: _ClassVar[int]
        status: _status_pb2.Status
        continuation_tokens: _containers.RepeatedCompositeFieldContainer[_data_pb2.StreamContinuationToken]
        new_partitions: _containers.RepeatedCompositeFieldContainer[_data_pb2.StreamPartition]
        def __init__(self, status: _Optional[_Union[_status_pb2.Status, _Mapping]] = ..., continuation_tokens: _Optional[_Iterable[_Union[_data_pb2.StreamContinuationToken, _Mapping]]] = ..., new_partitions: _Optional[_Iterable[_Union[_data_pb2.StreamPartition, _Mapping]]] = ...) -> None: ...
    DATA_CHANGE_FIELD_NUMBER: _ClassVar[int]
    HEARTBEAT_FIELD_NUMBER: _ClassVar[int]
    CLOSE_STREAM_FIELD_NUMBER: _ClassVar[int]
    data_change: ReadChangeStreamResponse.DataChange
    heartbeat: ReadChangeStreamResponse.Heartbeat
    close_stream: ReadChangeStreamResponse.CloseStream
    def __init__(self, data_change: _Optional[_Union[ReadChangeStreamResponse.DataChange, _Mapping]] = ..., heartbeat: _Optional[_Union[ReadChangeStreamResponse.Heartbeat, _Mapping]] = ..., close_stream: _Optional[_Union[ReadChangeStreamResponse.CloseStream, _Mapping]] = ...) -> None: ...

class ExecuteQueryRequest(_message.Message):
    __slots__ = ("instance_name", "app_profile_id", "query", "proto_format", "resume_token", "params")
    class ParamsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _data_pb2.Value
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_data_pb2.Value, _Mapping]] = ...) -> None: ...
    INSTANCE_NAME_FIELD_NUMBER: _ClassVar[int]
    APP_PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    PROTO_FORMAT_FIELD_NUMBER: _ClassVar[int]
    RESUME_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    instance_name: str
    app_profile_id: str
    query: str
    proto_format: _data_pb2.ProtoFormat
    resume_token: bytes
    params: _containers.MessageMap[str, _data_pb2.Value]
    def __init__(self, instance_name: _Optional[str] = ..., app_profile_id: _Optional[str] = ..., query: _Optional[str] = ..., proto_format: _Optional[_Union[_data_pb2.ProtoFormat, _Mapping]] = ..., resume_token: _Optional[bytes] = ..., params: _Optional[_Mapping[str, _data_pb2.Value]] = ...) -> None: ...

class ExecuteQueryResponse(_message.Message):
    __slots__ = ("metadata", "results")
    METADATA_FIELD_NUMBER: _ClassVar[int]
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    metadata: _data_pb2.ResultSetMetadata
    results: _data_pb2.PartialResultSet
    def __init__(self, metadata: _Optional[_Union[_data_pb2.ResultSetMetadata, _Mapping]] = ..., results: _Optional[_Union[_data_pb2.PartialResultSet, _Mapping]] = ...) -> None: ...
