from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.devtools.clouderrorreporting.v1beta1 import common_pb2 as _common_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ReportErrorEventRequest(_message.Message):
    __slots__ = ('project_name', 'event')
    PROJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    EVENT_FIELD_NUMBER: _ClassVar[int]
    project_name: str
    event: ReportedErrorEvent

    def __init__(self, project_name: _Optional[str]=..., event: _Optional[_Union[ReportedErrorEvent, _Mapping]]=...) -> None:
        ...

class ReportErrorEventResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class ReportedErrorEvent(_message.Message):
    __slots__ = ('event_time', 'service_context', 'message', 'context')
    EVENT_TIME_FIELD_NUMBER: _ClassVar[int]
    SERVICE_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    event_time: _timestamp_pb2.Timestamp
    service_context: _common_pb2.ServiceContext
    message: str
    context: _common_pb2.ErrorContext

    def __init__(self, event_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., service_context: _Optional[_Union[_common_pb2.ServiceContext, _Mapping]]=..., message: _Optional[str]=..., context: _Optional[_Union[_common_pb2.ErrorContext, _Mapping]]=...) -> None:
        ...