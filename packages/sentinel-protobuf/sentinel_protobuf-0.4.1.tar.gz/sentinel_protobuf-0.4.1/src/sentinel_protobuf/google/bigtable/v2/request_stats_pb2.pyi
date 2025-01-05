from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ReadIterationStats(_message.Message):
    __slots__ = ('rows_seen_count', 'rows_returned_count', 'cells_seen_count', 'cells_returned_count')
    ROWS_SEEN_COUNT_FIELD_NUMBER: _ClassVar[int]
    ROWS_RETURNED_COUNT_FIELD_NUMBER: _ClassVar[int]
    CELLS_SEEN_COUNT_FIELD_NUMBER: _ClassVar[int]
    CELLS_RETURNED_COUNT_FIELD_NUMBER: _ClassVar[int]
    rows_seen_count: int
    rows_returned_count: int
    cells_seen_count: int
    cells_returned_count: int

    def __init__(self, rows_seen_count: _Optional[int]=..., rows_returned_count: _Optional[int]=..., cells_seen_count: _Optional[int]=..., cells_returned_count: _Optional[int]=...) -> None:
        ...

class RequestLatencyStats(_message.Message):
    __slots__ = ('frontend_server_latency',)
    FRONTEND_SERVER_LATENCY_FIELD_NUMBER: _ClassVar[int]
    frontend_server_latency: _duration_pb2.Duration

    def __init__(self, frontend_server_latency: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=...) -> None:
        ...

class FullReadStatsView(_message.Message):
    __slots__ = ('read_iteration_stats', 'request_latency_stats')
    READ_ITERATION_STATS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_LATENCY_STATS_FIELD_NUMBER: _ClassVar[int]
    read_iteration_stats: ReadIterationStats
    request_latency_stats: RequestLatencyStats

    def __init__(self, read_iteration_stats: _Optional[_Union[ReadIterationStats, _Mapping]]=..., request_latency_stats: _Optional[_Union[RequestLatencyStats, _Mapping]]=...) -> None:
        ...

class RequestStats(_message.Message):
    __slots__ = ('full_read_stats_view',)
    FULL_READ_STATS_VIEW_FIELD_NUMBER: _ClassVar[int]
    full_read_stats_view: FullReadStatsView

    def __init__(self, full_read_stats_view: _Optional[_Union[FullReadStatsView, _Mapping]]=...) -> None:
        ...