from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class PurgeMetadata(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class PurgeProductsMetadata(_message.Message):
    __slots__ = ('create_time', 'update_time', 'success_count', 'failure_count')
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_COUNT_FIELD_NUMBER: _ClassVar[int]
    FAILURE_COUNT_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    success_count: int
    failure_count: int

    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., success_count: _Optional[int]=..., failure_count: _Optional[int]=...) -> None:
        ...

class PurgeProductsRequest(_message.Message):
    __slots__ = ('parent', 'filter', 'force')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    force: bool

    def __init__(self, parent: _Optional[str]=..., filter: _Optional[str]=..., force: bool=...) -> None:
        ...

class PurgeProductsResponse(_message.Message):
    __slots__ = ('purge_count', 'purge_sample')
    PURGE_COUNT_FIELD_NUMBER: _ClassVar[int]
    PURGE_SAMPLE_FIELD_NUMBER: _ClassVar[int]
    purge_count: int
    purge_sample: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, purge_count: _Optional[int]=..., purge_sample: _Optional[_Iterable[str]]=...) -> None:
        ...

class PurgeUserEventsRequest(_message.Message):
    __slots__ = ('parent', 'filter', 'force')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    force: bool

    def __init__(self, parent: _Optional[str]=..., filter: _Optional[str]=..., force: bool=...) -> None:
        ...

class PurgeUserEventsResponse(_message.Message):
    __slots__ = ('purged_events_count',)
    PURGED_EVENTS_COUNT_FIELD_NUMBER: _ClassVar[int]
    purged_events_count: int

    def __init__(self, purged_events_count: _Optional[int]=...) -> None:
        ...