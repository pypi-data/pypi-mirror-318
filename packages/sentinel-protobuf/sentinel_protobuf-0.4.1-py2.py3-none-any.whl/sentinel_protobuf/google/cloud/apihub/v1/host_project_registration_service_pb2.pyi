from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CreateHostProjectRegistrationRequest(_message.Message):
    __slots__ = ('parent', 'host_project_registration_id', 'host_project_registration')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    HOST_PROJECT_REGISTRATION_ID_FIELD_NUMBER: _ClassVar[int]
    HOST_PROJECT_REGISTRATION_FIELD_NUMBER: _ClassVar[int]
    parent: str
    host_project_registration_id: str
    host_project_registration: HostProjectRegistration

    def __init__(self, parent: _Optional[str]=..., host_project_registration_id: _Optional[str]=..., host_project_registration: _Optional[_Union[HostProjectRegistration, _Mapping]]=...) -> None:
        ...

class GetHostProjectRegistrationRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListHostProjectRegistrationsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'order_by')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=...) -> None:
        ...

class ListHostProjectRegistrationsResponse(_message.Message):
    __slots__ = ('host_project_registrations', 'next_page_token')
    HOST_PROJECT_REGISTRATIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    host_project_registrations: _containers.RepeatedCompositeFieldContainer[HostProjectRegistration]
    next_page_token: str

    def __init__(self, host_project_registrations: _Optional[_Iterable[_Union[HostProjectRegistration, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class HostProjectRegistration(_message.Message):
    __slots__ = ('name', 'gcp_project', 'create_time')
    NAME_FIELD_NUMBER: _ClassVar[int]
    GCP_PROJECT_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    gcp_project: str
    create_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., gcp_project: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...