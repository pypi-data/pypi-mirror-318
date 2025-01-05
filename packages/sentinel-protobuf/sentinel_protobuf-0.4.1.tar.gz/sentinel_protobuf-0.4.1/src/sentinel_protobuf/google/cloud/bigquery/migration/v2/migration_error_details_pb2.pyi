from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.rpc import error_details_pb2 as _error_details_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ResourceErrorDetail(_message.Message):
    __slots__ = ('resource_info', 'error_details', 'error_count')
    RESOURCE_INFO_FIELD_NUMBER: _ClassVar[int]
    ERROR_DETAILS_FIELD_NUMBER: _ClassVar[int]
    ERROR_COUNT_FIELD_NUMBER: _ClassVar[int]
    resource_info: _error_details_pb2.ResourceInfo
    error_details: _containers.RepeatedCompositeFieldContainer[ErrorDetail]
    error_count: int

    def __init__(self, resource_info: _Optional[_Union[_error_details_pb2.ResourceInfo, _Mapping]]=..., error_details: _Optional[_Iterable[_Union[ErrorDetail, _Mapping]]]=..., error_count: _Optional[int]=...) -> None:
        ...

class ErrorDetail(_message.Message):
    __slots__ = ('location', 'error_info')
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    ERROR_INFO_FIELD_NUMBER: _ClassVar[int]
    location: ErrorLocation
    error_info: _error_details_pb2.ErrorInfo

    def __init__(self, location: _Optional[_Union[ErrorLocation, _Mapping]]=..., error_info: _Optional[_Union[_error_details_pb2.ErrorInfo, _Mapping]]=...) -> None:
        ...

class ErrorLocation(_message.Message):
    __slots__ = ('line', 'column')
    LINE_FIELD_NUMBER: _ClassVar[int]
    COLUMN_FIELD_NUMBER: _ClassVar[int]
    line: int
    column: int

    def __init__(self, line: _Optional[int]=..., column: _Optional[int]=...) -> None:
        ...