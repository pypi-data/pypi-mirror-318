from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.iam.v1 import iam_policy_pb2 as _iam_policy_pb2
from google.iam.v1 import policy_pb2 as _policy_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Project(_message.Message):
    __slots__ = ('name', 'parent', 'project_id', 'state', 'display_name', 'create_time', 'update_time', 'delete_time', 'etag', 'labels')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Project.State]
        ACTIVE: _ClassVar[Project.State]
        DELETE_REQUESTED: _ClassVar[Project.State]
    STATE_UNSPECIFIED: Project.State
    ACTIVE: Project.State
    DELETE_REQUESTED: Project.State

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DELETE_TIME_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    name: str
    parent: str
    project_id: str
    state: Project.State
    display_name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    delete_time: _timestamp_pb2.Timestamp
    etag: str
    labels: _containers.ScalarMap[str, str]

    def __init__(self, name: _Optional[str]=..., parent: _Optional[str]=..., project_id: _Optional[str]=..., state: _Optional[_Union[Project.State, str]]=..., display_name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., delete_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., etag: _Optional[str]=..., labels: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class GetProjectRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListProjectsRequest(_message.Message):
    __slots__ = ('parent', 'page_token', 'page_size', 'show_deleted')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    SHOW_DELETED_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_token: str
    page_size: int
    show_deleted: bool

    def __init__(self, parent: _Optional[str]=..., page_token: _Optional[str]=..., page_size: _Optional[int]=..., show_deleted: bool=...) -> None:
        ...

class ListProjectsResponse(_message.Message):
    __slots__ = ('projects', 'next_page_token')
    PROJECTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    projects: _containers.RepeatedCompositeFieldContainer[Project]
    next_page_token: str

    def __init__(self, projects: _Optional[_Iterable[_Union[Project, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class SearchProjectsRequest(_message.Message):
    __slots__ = ('query', 'page_token', 'page_size')
    QUERY_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    query: str
    page_token: str
    page_size: int

    def __init__(self, query: _Optional[str]=..., page_token: _Optional[str]=..., page_size: _Optional[int]=...) -> None:
        ...

class SearchProjectsResponse(_message.Message):
    __slots__ = ('projects', 'next_page_token')
    PROJECTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    projects: _containers.RepeatedCompositeFieldContainer[Project]
    next_page_token: str

    def __init__(self, projects: _Optional[_Iterable[_Union[Project, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class CreateProjectRequest(_message.Message):
    __slots__ = ('project',)
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    project: Project

    def __init__(self, project: _Optional[_Union[Project, _Mapping]]=...) -> None:
        ...

class CreateProjectMetadata(_message.Message):
    __slots__ = ('create_time', 'gettable', 'ready')
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    GETTABLE_FIELD_NUMBER: _ClassVar[int]
    READY_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    gettable: bool
    ready: bool

    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., gettable: bool=..., ready: bool=...) -> None:
        ...

class UpdateProjectRequest(_message.Message):
    __slots__ = ('project', 'update_mask')
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    project: Project
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, project: _Optional[_Union[Project, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class UpdateProjectMetadata(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class MoveProjectRequest(_message.Message):
    __slots__ = ('name', 'destination_parent')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_PARENT_FIELD_NUMBER: _ClassVar[int]
    name: str
    destination_parent: str

    def __init__(self, name: _Optional[str]=..., destination_parent: _Optional[str]=...) -> None:
        ...

class MoveProjectMetadata(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class DeleteProjectRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class DeleteProjectMetadata(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class UndeleteProjectRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UndeleteProjectMetadata(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...