from google.api import resource_pb2 as _resource_pb2
from google.cloud.tasks.v2 import target_pb2 as _target_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Task(_message.Message):
    __slots__ = ('name', 'app_engine_http_request', 'http_request', 'schedule_time', 'create_time', 'dispatch_deadline', 'dispatch_count', 'response_count', 'first_attempt', 'last_attempt', 'view')

    class View(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        VIEW_UNSPECIFIED: _ClassVar[Task.View]
        BASIC: _ClassVar[Task.View]
        FULL: _ClassVar[Task.View]
    VIEW_UNSPECIFIED: Task.View
    BASIC: Task.View
    FULL: Task.View
    NAME_FIELD_NUMBER: _ClassVar[int]
    APP_ENGINE_HTTP_REQUEST_FIELD_NUMBER: _ClassVar[int]
    HTTP_REQUEST_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_TIME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DISPATCH_DEADLINE_FIELD_NUMBER: _ClassVar[int]
    DISPATCH_COUNT_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_COUNT_FIELD_NUMBER: _ClassVar[int]
    FIRST_ATTEMPT_FIELD_NUMBER: _ClassVar[int]
    LAST_ATTEMPT_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    name: str
    app_engine_http_request: _target_pb2.AppEngineHttpRequest
    http_request: _target_pb2.HttpRequest
    schedule_time: _timestamp_pb2.Timestamp
    create_time: _timestamp_pb2.Timestamp
    dispatch_deadline: _duration_pb2.Duration
    dispatch_count: int
    response_count: int
    first_attempt: Attempt
    last_attempt: Attempt
    view: Task.View

    def __init__(self, name: _Optional[str]=..., app_engine_http_request: _Optional[_Union[_target_pb2.AppEngineHttpRequest, _Mapping]]=..., http_request: _Optional[_Union[_target_pb2.HttpRequest, _Mapping]]=..., schedule_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., dispatch_deadline: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., dispatch_count: _Optional[int]=..., response_count: _Optional[int]=..., first_attempt: _Optional[_Union[Attempt, _Mapping]]=..., last_attempt: _Optional[_Union[Attempt, _Mapping]]=..., view: _Optional[_Union[Task.View, str]]=...) -> None:
        ...

class Attempt(_message.Message):
    __slots__ = ('schedule_time', 'dispatch_time', 'response_time', 'response_status')
    SCHEDULE_TIME_FIELD_NUMBER: _ClassVar[int]
    DISPATCH_TIME_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_TIME_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STATUS_FIELD_NUMBER: _ClassVar[int]
    schedule_time: _timestamp_pb2.Timestamp
    dispatch_time: _timestamp_pb2.Timestamp
    response_time: _timestamp_pb2.Timestamp
    response_status: _status_pb2.Status

    def __init__(self, schedule_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., dispatch_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., response_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., response_status: _Optional[_Union[_status_pb2.Status, _Mapping]]=...) -> None:
        ...