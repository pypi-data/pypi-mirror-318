from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.dialogflow.cx.v3 import page_pb2 as _page_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class TransitionRouteGroup(_message.Message):
    __slots__ = ('name', 'display_name', 'transition_routes')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    TRANSITION_ROUTES_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    transition_routes: _containers.RepeatedCompositeFieldContainer[_page_pb2.TransitionRoute]

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., transition_routes: _Optional[_Iterable[_Union[_page_pb2.TransitionRoute, _Mapping]]]=...) -> None:
        ...

class ListTransitionRouteGroupsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'language_code')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    language_code: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., language_code: _Optional[str]=...) -> None:
        ...

class ListTransitionRouteGroupsResponse(_message.Message):
    __slots__ = ('transition_route_groups', 'next_page_token')
    TRANSITION_ROUTE_GROUPS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    transition_route_groups: _containers.RepeatedCompositeFieldContainer[TransitionRouteGroup]
    next_page_token: str

    def __init__(self, transition_route_groups: _Optional[_Iterable[_Union[TransitionRouteGroup, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetTransitionRouteGroupRequest(_message.Message):
    __slots__ = ('name', 'language_code')
    NAME_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    name: str
    language_code: str

    def __init__(self, name: _Optional[str]=..., language_code: _Optional[str]=...) -> None:
        ...

class CreateTransitionRouteGroupRequest(_message.Message):
    __slots__ = ('parent', 'transition_route_group', 'language_code')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TRANSITION_ROUTE_GROUP_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    transition_route_group: TransitionRouteGroup
    language_code: str

    def __init__(self, parent: _Optional[str]=..., transition_route_group: _Optional[_Union[TransitionRouteGroup, _Mapping]]=..., language_code: _Optional[str]=...) -> None:
        ...

class UpdateTransitionRouteGroupRequest(_message.Message):
    __slots__ = ('transition_route_group', 'update_mask', 'language_code')
    TRANSITION_ROUTE_GROUP_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    transition_route_group: TransitionRouteGroup
    update_mask: _field_mask_pb2.FieldMask
    language_code: str

    def __init__(self, transition_route_group: _Optional[_Union[TransitionRouteGroup, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., language_code: _Optional[str]=...) -> None:
        ...

class DeleteTransitionRouteGroupRequest(_message.Message):
    __slots__ = ('name', 'force')
    NAME_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    force: bool

    def __init__(self, name: _Optional[str]=..., force: bool=...) -> None:
        ...