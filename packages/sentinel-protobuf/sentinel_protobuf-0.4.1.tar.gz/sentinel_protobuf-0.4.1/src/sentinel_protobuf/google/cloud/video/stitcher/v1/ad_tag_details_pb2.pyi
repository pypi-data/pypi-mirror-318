from google.api import resource_pb2 as _resource_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class LiveAdTagDetail(_message.Message):
    __slots__ = ('name', 'ad_requests')
    NAME_FIELD_NUMBER: _ClassVar[int]
    AD_REQUESTS_FIELD_NUMBER: _ClassVar[int]
    name: str
    ad_requests: _containers.RepeatedCompositeFieldContainer[AdRequest]

    def __init__(self, name: _Optional[str]=..., ad_requests: _Optional[_Iterable[_Union[AdRequest, _Mapping]]]=...) -> None:
        ...

class VodAdTagDetail(_message.Message):
    __slots__ = ('name', 'ad_requests')
    NAME_FIELD_NUMBER: _ClassVar[int]
    AD_REQUESTS_FIELD_NUMBER: _ClassVar[int]
    name: str
    ad_requests: _containers.RepeatedCompositeFieldContainer[AdRequest]

    def __init__(self, name: _Optional[str]=..., ad_requests: _Optional[_Iterable[_Union[AdRequest, _Mapping]]]=...) -> None:
        ...

class AdRequest(_message.Message):
    __slots__ = ('uri', 'request_metadata', 'response_metadata')
    URI_FIELD_NUMBER: _ClassVar[int]
    REQUEST_METADATA_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_METADATA_FIELD_NUMBER: _ClassVar[int]
    uri: str
    request_metadata: RequestMetadata
    response_metadata: ResponseMetadata

    def __init__(self, uri: _Optional[str]=..., request_metadata: _Optional[_Union[RequestMetadata, _Mapping]]=..., response_metadata: _Optional[_Union[ResponseMetadata, _Mapping]]=...) -> None:
        ...

class RequestMetadata(_message.Message):
    __slots__ = ('headers',)
    HEADERS_FIELD_NUMBER: _ClassVar[int]
    headers: _struct_pb2.Struct

    def __init__(self, headers: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=...) -> None:
        ...

class ResponseMetadata(_message.Message):
    __slots__ = ('error', 'headers', 'status_code', 'size_bytes', 'duration', 'body')
    ERROR_FIELD_NUMBER: _ClassVar[int]
    HEADERS_FIELD_NUMBER: _ClassVar[int]
    STATUS_CODE_FIELD_NUMBER: _ClassVar[int]
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    error: str
    headers: _struct_pb2.Struct
    status_code: str
    size_bytes: int
    duration: _duration_pb2.Duration
    body: str

    def __init__(self, error: _Optional[str]=..., headers: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=..., status_code: _Optional[str]=..., size_bytes: _Optional[int]=..., duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., body: _Optional[str]=...) -> None:
        ...