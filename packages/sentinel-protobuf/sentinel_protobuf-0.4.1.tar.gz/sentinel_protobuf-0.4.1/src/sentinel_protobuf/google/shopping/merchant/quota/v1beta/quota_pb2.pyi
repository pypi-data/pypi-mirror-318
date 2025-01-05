from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class QuotaGroup(_message.Message):
    __slots__ = ('name', 'quota_usage', 'quota_limit', 'quota_minute_limit', 'method_details')
    NAME_FIELD_NUMBER: _ClassVar[int]
    QUOTA_USAGE_FIELD_NUMBER: _ClassVar[int]
    QUOTA_LIMIT_FIELD_NUMBER: _ClassVar[int]
    QUOTA_MINUTE_LIMIT_FIELD_NUMBER: _ClassVar[int]
    METHOD_DETAILS_FIELD_NUMBER: _ClassVar[int]
    name: str
    quota_usage: int
    quota_limit: int
    quota_minute_limit: int
    method_details: _containers.RepeatedCompositeFieldContainer[MethodDetails]

    def __init__(self, name: _Optional[str]=..., quota_usage: _Optional[int]=..., quota_limit: _Optional[int]=..., quota_minute_limit: _Optional[int]=..., method_details: _Optional[_Iterable[_Union[MethodDetails, _Mapping]]]=...) -> None:
        ...

class MethodDetails(_message.Message):
    __slots__ = ('method', 'version', 'subapi', 'path')
    METHOD_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    SUBAPI_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    method: str
    version: str
    subapi: str
    path: str

    def __init__(self, method: _Optional[str]=..., version: _Optional[str]=..., subapi: _Optional[str]=..., path: _Optional[str]=...) -> None:
        ...

class ListQuotaGroupsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListQuotaGroupsResponse(_message.Message):
    __slots__ = ('quota_groups', 'next_page_token')
    QUOTA_GROUPS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    quota_groups: _containers.RepeatedCompositeFieldContainer[QuotaGroup]
    next_page_token: str

    def __init__(self, quota_groups: _Optional[_Iterable[_Union[QuotaGroup, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...