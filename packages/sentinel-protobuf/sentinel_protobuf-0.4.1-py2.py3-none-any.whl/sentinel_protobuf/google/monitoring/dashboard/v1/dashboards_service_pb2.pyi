from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.monitoring.dashboard.v1 import dashboard_pb2 as _dashboard_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CreateDashboardRequest(_message.Message):
    __slots__ = ('parent', 'dashboard', 'validate_only')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    DASHBOARD_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    dashboard: _dashboard_pb2.Dashboard
    validate_only: bool

    def __init__(self, parent: _Optional[str]=..., dashboard: _Optional[_Union[_dashboard_pb2.Dashboard, _Mapping]]=..., validate_only: bool=...) -> None:
        ...

class ListDashboardsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListDashboardsResponse(_message.Message):
    __slots__ = ('dashboards', 'next_page_token')
    DASHBOARDS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    dashboards: _containers.RepeatedCompositeFieldContainer[_dashboard_pb2.Dashboard]
    next_page_token: str

    def __init__(self, dashboards: _Optional[_Iterable[_Union[_dashboard_pb2.Dashboard, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetDashboardRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class DeleteDashboardRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateDashboardRequest(_message.Message):
    __slots__ = ('dashboard', 'validate_only')
    DASHBOARD_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    dashboard: _dashboard_pb2.Dashboard
    validate_only: bool

    def __init__(self, dashboard: _Optional[_Union[_dashboard_pb2.Dashboard, _Mapping]]=..., validate_only: bool=...) -> None:
        ...