from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ResolutionStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RESOLUTION_STATUS_UNSPECIFIED: _ClassVar[ResolutionStatus]
    OPEN: _ClassVar[ResolutionStatus]
    ACKNOWLEDGED: _ClassVar[ResolutionStatus]
    RESOLVED: _ClassVar[ResolutionStatus]
    MUTED: _ClassVar[ResolutionStatus]
RESOLUTION_STATUS_UNSPECIFIED: ResolutionStatus
OPEN: ResolutionStatus
ACKNOWLEDGED: ResolutionStatus
RESOLVED: ResolutionStatus
MUTED: ResolutionStatus

class ErrorGroup(_message.Message):
    __slots__ = ('name', 'group_id', 'tracking_issues', 'resolution_status')
    NAME_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    TRACKING_ISSUES_FIELD_NUMBER: _ClassVar[int]
    RESOLUTION_STATUS_FIELD_NUMBER: _ClassVar[int]
    name: str
    group_id: str
    tracking_issues: _containers.RepeatedCompositeFieldContainer[TrackingIssue]
    resolution_status: ResolutionStatus

    def __init__(self, name: _Optional[str]=..., group_id: _Optional[str]=..., tracking_issues: _Optional[_Iterable[_Union[TrackingIssue, _Mapping]]]=..., resolution_status: _Optional[_Union[ResolutionStatus, str]]=...) -> None:
        ...

class TrackingIssue(_message.Message):
    __slots__ = ('url',)
    URL_FIELD_NUMBER: _ClassVar[int]
    url: str

    def __init__(self, url: _Optional[str]=...) -> None:
        ...

class ErrorEvent(_message.Message):
    __slots__ = ('event_time', 'service_context', 'message', 'context')
    EVENT_TIME_FIELD_NUMBER: _ClassVar[int]
    SERVICE_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    event_time: _timestamp_pb2.Timestamp
    service_context: ServiceContext
    message: str
    context: ErrorContext

    def __init__(self, event_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., service_context: _Optional[_Union[ServiceContext, _Mapping]]=..., message: _Optional[str]=..., context: _Optional[_Union[ErrorContext, _Mapping]]=...) -> None:
        ...

class ServiceContext(_message.Message):
    __slots__ = ('service', 'version', 'resource_type')
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    service: str
    version: str
    resource_type: str

    def __init__(self, service: _Optional[str]=..., version: _Optional[str]=..., resource_type: _Optional[str]=...) -> None:
        ...

class ErrorContext(_message.Message):
    __slots__ = ('http_request', 'user', 'report_location')
    HTTP_REQUEST_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    REPORT_LOCATION_FIELD_NUMBER: _ClassVar[int]
    http_request: HttpRequestContext
    user: str
    report_location: SourceLocation

    def __init__(self, http_request: _Optional[_Union[HttpRequestContext, _Mapping]]=..., user: _Optional[str]=..., report_location: _Optional[_Union[SourceLocation, _Mapping]]=...) -> None:
        ...

class HttpRequestContext(_message.Message):
    __slots__ = ('method', 'url', 'user_agent', 'referrer', 'response_status_code', 'remote_ip')
    METHOD_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    USER_AGENT_FIELD_NUMBER: _ClassVar[int]
    REFERRER_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STATUS_CODE_FIELD_NUMBER: _ClassVar[int]
    REMOTE_IP_FIELD_NUMBER: _ClassVar[int]
    method: str
    url: str
    user_agent: str
    referrer: str
    response_status_code: int
    remote_ip: str

    def __init__(self, method: _Optional[str]=..., url: _Optional[str]=..., user_agent: _Optional[str]=..., referrer: _Optional[str]=..., response_status_code: _Optional[int]=..., remote_ip: _Optional[str]=...) -> None:
        ...

class SourceLocation(_message.Message):
    __slots__ = ('file_path', 'line_number', 'function_name')
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    LINE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    FUNCTION_NAME_FIELD_NUMBER: _ClassVar[int]
    file_path: str
    line_number: int
    function_name: str

    def __init__(self, file_path: _Optional[str]=..., line_number: _Optional[int]=..., function_name: _Optional[str]=...) -> None:
        ...