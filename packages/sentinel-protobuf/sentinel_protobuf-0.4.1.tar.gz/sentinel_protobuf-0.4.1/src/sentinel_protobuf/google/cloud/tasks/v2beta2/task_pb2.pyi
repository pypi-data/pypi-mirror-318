from google.api import resource_pb2 as _resource_pb2
from google.cloud.tasks.v2beta2 import target_pb2 as _target_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Task(_message.Message):
    __slots__ = ("name", "app_engine_http_request", "pull_message", "http_request", "schedule_time", "create_time", "status", "view")
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
    PULL_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    HTTP_REQUEST_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_TIME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    name: str
    app_engine_http_request: _target_pb2.AppEngineHttpRequest
    pull_message: _target_pb2.PullMessage
    http_request: _target_pb2.HttpRequest
    schedule_time: _timestamp_pb2.Timestamp
    create_time: _timestamp_pb2.Timestamp
    status: TaskStatus
    view: Task.View
    def __init__(self, name: _Optional[str] = ..., app_engine_http_request: _Optional[_Union[_target_pb2.AppEngineHttpRequest, _Mapping]] = ..., pull_message: _Optional[_Union[_target_pb2.PullMessage, _Mapping]] = ..., http_request: _Optional[_Union[_target_pb2.HttpRequest, _Mapping]] = ..., schedule_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., status: _Optional[_Union[TaskStatus, _Mapping]] = ..., view: _Optional[_Union[Task.View, str]] = ...) -> None: ...

class TaskStatus(_message.Message):
    __slots__ = ("attempt_dispatch_count", "attempt_response_count", "first_attempt_status", "last_attempt_status")
    ATTEMPT_DISPATCH_COUNT_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_RESPONSE_COUNT_FIELD_NUMBER: _ClassVar[int]
    FIRST_ATTEMPT_STATUS_FIELD_NUMBER: _ClassVar[int]
    LAST_ATTEMPT_STATUS_FIELD_NUMBER: _ClassVar[int]
    attempt_dispatch_count: int
    attempt_response_count: int
    first_attempt_status: AttemptStatus
    last_attempt_status: AttemptStatus
    def __init__(self, attempt_dispatch_count: _Optional[int] = ..., attempt_response_count: _Optional[int] = ..., first_attempt_status: _Optional[_Union[AttemptStatus, _Mapping]] = ..., last_attempt_status: _Optional[_Union[AttemptStatus, _Mapping]] = ...) -> None: ...

class AttemptStatus(_message.Message):
    __slots__ = ("schedule_time", "dispatch_time", "response_time", "response_status")
    SCHEDULE_TIME_FIELD_NUMBER: _ClassVar[int]
    DISPATCH_TIME_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_TIME_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STATUS_FIELD_NUMBER: _ClassVar[int]
    schedule_time: _timestamp_pb2.Timestamp
    dispatch_time: _timestamp_pb2.Timestamp
    response_time: _timestamp_pb2.Timestamp
    response_status: _status_pb2.Status
    def __init__(self, schedule_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., dispatch_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., response_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., response_status: _Optional[_Union[_status_pb2.Status, _Mapping]] = ...) -> None: ...
