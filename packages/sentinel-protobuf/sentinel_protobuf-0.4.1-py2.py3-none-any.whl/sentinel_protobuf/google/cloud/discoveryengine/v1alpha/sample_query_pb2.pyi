from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SampleQuery(_message.Message):
    __slots__ = ("query_entry", "name", "create_time")
    class QueryEntry(_message.Message):
        __slots__ = ("query", "targets")
        class Target(_message.Message):
            __slots__ = ("uri", "page_numbers", "score")
            URI_FIELD_NUMBER: _ClassVar[int]
            PAGE_NUMBERS_FIELD_NUMBER: _ClassVar[int]
            SCORE_FIELD_NUMBER: _ClassVar[int]
            uri: str
            page_numbers: _containers.RepeatedScalarFieldContainer[int]
            score: float
            def __init__(self, uri: _Optional[str] = ..., page_numbers: _Optional[_Iterable[int]] = ..., score: _Optional[float] = ...) -> None: ...
        QUERY_FIELD_NUMBER: _ClassVar[int]
        TARGETS_FIELD_NUMBER: _ClassVar[int]
        query: str
        targets: _containers.RepeatedCompositeFieldContainer[SampleQuery.QueryEntry.Target]
        def __init__(self, query: _Optional[str] = ..., targets: _Optional[_Iterable[_Union[SampleQuery.QueryEntry.Target, _Mapping]]] = ...) -> None: ...
    QUERY_ENTRY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    query_entry: SampleQuery.QueryEntry
    name: str
    create_time: _timestamp_pb2.Timestamp
    def __init__(self, query_entry: _Optional[_Union[SampleQuery.QueryEntry, _Mapping]] = ..., name: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
