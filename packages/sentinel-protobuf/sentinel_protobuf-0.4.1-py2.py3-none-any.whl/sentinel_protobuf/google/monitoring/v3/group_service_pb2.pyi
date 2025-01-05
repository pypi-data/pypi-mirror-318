from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import monitored_resource_pb2 as _monitored_resource_pb2
from google.api import resource_pb2 as _resource_pb2
from google.monitoring.v3 import common_pb2 as _common_pb2
from google.monitoring.v3 import group_pb2 as _group_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ListGroupsRequest(_message.Message):
    __slots__ = ('name', 'children_of_group', 'ancestors_of_group', 'descendants_of_group', 'page_size', 'page_token')
    NAME_FIELD_NUMBER: _ClassVar[int]
    CHILDREN_OF_GROUP_FIELD_NUMBER: _ClassVar[int]
    ANCESTORS_OF_GROUP_FIELD_NUMBER: _ClassVar[int]
    DESCENDANTS_OF_GROUP_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    name: str
    children_of_group: str
    ancestors_of_group: str
    descendants_of_group: str
    page_size: int
    page_token: str

    def __init__(self, name: _Optional[str]=..., children_of_group: _Optional[str]=..., ancestors_of_group: _Optional[str]=..., descendants_of_group: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListGroupsResponse(_message.Message):
    __slots__ = ('group', 'next_page_token')
    GROUP_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    group: _containers.RepeatedCompositeFieldContainer[_group_pb2.Group]
    next_page_token: str

    def __init__(self, group: _Optional[_Iterable[_Union[_group_pb2.Group, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetGroupRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateGroupRequest(_message.Message):
    __slots__ = ('name', 'group', 'validate_only')
    NAME_FIELD_NUMBER: _ClassVar[int]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    name: str
    group: _group_pb2.Group
    validate_only: bool

    def __init__(self, name: _Optional[str]=..., group: _Optional[_Union[_group_pb2.Group, _Mapping]]=..., validate_only: bool=...) -> None:
        ...

class UpdateGroupRequest(_message.Message):
    __slots__ = ('group', 'validate_only')
    GROUP_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    group: _group_pb2.Group
    validate_only: bool

    def __init__(self, group: _Optional[_Union[_group_pb2.Group, _Mapping]]=..., validate_only: bool=...) -> None:
        ...

class DeleteGroupRequest(_message.Message):
    __slots__ = ('name', 'recursive')
    NAME_FIELD_NUMBER: _ClassVar[int]
    RECURSIVE_FIELD_NUMBER: _ClassVar[int]
    name: str
    recursive: bool

    def __init__(self, name: _Optional[str]=..., recursive: bool=...) -> None:
        ...

class ListGroupMembersRequest(_message.Message):
    __slots__ = ('name', 'page_size', 'page_token', 'filter', 'interval')
    NAME_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    INTERVAL_FIELD_NUMBER: _ClassVar[int]
    name: str
    page_size: int
    page_token: str
    filter: str
    interval: _common_pb2.TimeInterval

    def __init__(self, name: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., interval: _Optional[_Union[_common_pb2.TimeInterval, _Mapping]]=...) -> None:
        ...

class ListGroupMembersResponse(_message.Message):
    __slots__ = ('members', 'next_page_token', 'total_size')
    MEMBERS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    members: _containers.RepeatedCompositeFieldContainer[_monitored_resource_pb2.MonitoredResource]
    next_page_token: str
    total_size: int

    def __init__(self, members: _Optional[_Iterable[_Union[_monitored_resource_pb2.MonitoredResource, _Mapping]]]=..., next_page_token: _Optional[str]=..., total_size: _Optional[int]=...) -> None:
        ...