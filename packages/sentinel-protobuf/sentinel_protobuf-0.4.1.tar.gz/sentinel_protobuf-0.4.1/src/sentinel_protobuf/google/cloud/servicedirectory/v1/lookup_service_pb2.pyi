from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.servicedirectory.v1 import service_pb2 as _service_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ResolveServiceRequest(_message.Message):
    __slots__ = ('name', 'max_endpoints', 'endpoint_filter')
    NAME_FIELD_NUMBER: _ClassVar[int]
    MAX_ENDPOINTS_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_FILTER_FIELD_NUMBER: _ClassVar[int]
    name: str
    max_endpoints: int
    endpoint_filter: str

    def __init__(self, name: _Optional[str]=..., max_endpoints: _Optional[int]=..., endpoint_filter: _Optional[str]=...) -> None:
        ...

class ResolveServiceResponse(_message.Message):
    __slots__ = ('service',)
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    service: _service_pb2.Service

    def __init__(self, service: _Optional[_Union[_service_pb2.Service, _Mapping]]=...) -> None:
        ...