from google.protobuf import duration_pb2 as _duration_pb2
from google.rpc import status_pb2 as _status_pb2
from google.api import client_pb2 as _client_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Action(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ACTION_UNSPECIFIED: _ClassVar[Action]
    OPEN_NEW_STREAM: _ClassVar[Action]

class TetherEndpoint(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TETHER_ENDPOINT_UNSPECIFIED: _ClassVar[TetherEndpoint]
    APIGEE_MART: _ClassVar[TetherEndpoint]
    APIGEE_RUNTIME: _ClassVar[TetherEndpoint]
    APIGEE_MINT_RATING: _ClassVar[TetherEndpoint]

class Scheme(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SCHEME_UNSPECIFIED: _ClassVar[Scheme]
    HTTPS: _ClassVar[Scheme]
ACTION_UNSPECIFIED: Action
OPEN_NEW_STREAM: Action
TETHER_ENDPOINT_UNSPECIFIED: TetherEndpoint
APIGEE_MART: TetherEndpoint
APIGEE_RUNTIME: TetherEndpoint
APIGEE_MINT_RATING: TetherEndpoint
SCHEME_UNSPECIFIED: Scheme
HTTPS: Scheme

class EgressRequest(_message.Message):
    __slots__ = ('id', 'payload', 'endpoint', 'project', 'trace_id', 'timeout')
    ID_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    id: str
    payload: Payload
    endpoint: TetherEndpoint
    project: str
    trace_id: str
    timeout: _duration_pb2.Duration

    def __init__(self, id: _Optional[str]=..., payload: _Optional[_Union[Payload, _Mapping]]=..., endpoint: _Optional[_Union[TetherEndpoint, str]]=..., project: _Optional[str]=..., trace_id: _Optional[str]=..., timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=...) -> None:
        ...

class Payload(_message.Message):
    __slots__ = ('http_request', 'stream_info', 'action')
    HTTP_REQUEST_FIELD_NUMBER: _ClassVar[int]
    STREAM_INFO_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    http_request: HttpRequest
    stream_info: StreamInfo
    action: Action

    def __init__(self, http_request: _Optional[_Union[HttpRequest, _Mapping]]=..., stream_info: _Optional[_Union[StreamInfo, _Mapping]]=..., action: _Optional[_Union[Action, str]]=...) -> None:
        ...

class StreamInfo(_message.Message):
    __slots__ = ('id',)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str

    def __init__(self, id: _Optional[str]=...) -> None:
        ...

class EgressResponse(_message.Message):
    __slots__ = ('id', 'http_response', 'status', 'project', 'trace_id', 'endpoint', 'name')
    ID_FIELD_NUMBER: _ClassVar[int]
    HTTP_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    http_response: HttpResponse
    status: _status_pb2.Status
    project: str
    trace_id: str
    endpoint: TetherEndpoint
    name: str

    def __init__(self, id: _Optional[str]=..., http_response: _Optional[_Union[HttpResponse, _Mapping]]=..., status: _Optional[_Union[_status_pb2.Status, _Mapping]]=..., project: _Optional[str]=..., trace_id: _Optional[str]=..., endpoint: _Optional[_Union[TetherEndpoint, str]]=..., name: _Optional[str]=...) -> None:
        ...

class HttpRequest(_message.Message):
    __slots__ = ('id', 'method', 'url', 'headers', 'body')
    ID_FIELD_NUMBER: _ClassVar[int]
    METHOD_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    HEADERS_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    id: str
    method: str
    url: Url
    headers: _containers.RepeatedCompositeFieldContainer[Header]
    body: bytes

    def __init__(self, id: _Optional[str]=..., method: _Optional[str]=..., url: _Optional[_Union[Url, _Mapping]]=..., headers: _Optional[_Iterable[_Union[Header, _Mapping]]]=..., body: _Optional[bytes]=...) -> None:
        ...

class Url(_message.Message):
    __slots__ = ('scheme', 'host', 'path')
    SCHEME_FIELD_NUMBER: _ClassVar[int]
    HOST_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    scheme: Scheme
    host: str
    path: str

    def __init__(self, scheme: _Optional[_Union[Scheme, str]]=..., host: _Optional[str]=..., path: _Optional[str]=...) -> None:
        ...

class Header(_message.Message):
    __slots__ = ('key', 'values')
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    key: str
    values: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, key: _Optional[str]=..., values: _Optional[_Iterable[str]]=...) -> None:
        ...

class HttpResponse(_message.Message):
    __slots__ = ('id', 'status', 'status_code', 'body', 'headers', 'content_length')
    ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    STATUS_CODE_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    HEADERS_FIELD_NUMBER: _ClassVar[int]
    CONTENT_LENGTH_FIELD_NUMBER: _ClassVar[int]
    id: str
    status: str
    status_code: int
    body: bytes
    headers: _containers.RepeatedCompositeFieldContainer[Header]
    content_length: int

    def __init__(self, id: _Optional[str]=..., status: _Optional[str]=..., status_code: _Optional[int]=..., body: _Optional[bytes]=..., headers: _Optional[_Iterable[_Union[Header, _Mapping]]]=..., content_length: _Optional[int]=...) -> None:
        ...