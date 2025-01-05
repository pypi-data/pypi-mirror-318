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

class Folder(_message.Message):
    __slots__ = ('name', 'parent', 'display_name', 'lifecycle_state', 'create_time', 'update_time')

    class LifecycleState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        LIFECYCLE_STATE_UNSPECIFIED: _ClassVar[Folder.LifecycleState]
        ACTIVE: _ClassVar[Folder.LifecycleState]
        DELETE_REQUESTED: _ClassVar[Folder.LifecycleState]
    LIFECYCLE_STATE_UNSPECIFIED: Folder.LifecycleState
    ACTIVE: Folder.LifecycleState
    DELETE_REQUESTED: Folder.LifecycleState
    NAME_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    LIFECYCLE_STATE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    parent: str
    display_name: str
    lifecycle_state: Folder.LifecycleState
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., parent: _Optional[str]=..., display_name: _Optional[str]=..., lifecycle_state: _Optional[_Union[Folder.LifecycleState, str]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class ListFoldersRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'show_deleted')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    SHOW_DELETED_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    show_deleted: bool

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., show_deleted: bool=...) -> None:
        ...

class ListFoldersResponse(_message.Message):
    __slots__ = ('folders', 'next_page_token')
    FOLDERS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    folders: _containers.RepeatedCompositeFieldContainer[Folder]
    next_page_token: str

    def __init__(self, folders: _Optional[_Iterable[_Union[Folder, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class SearchFoldersRequest(_message.Message):
    __slots__ = ('page_size', 'page_token', 'query')
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    page_size: int
    page_token: str
    query: str

    def __init__(self, page_size: _Optional[int]=..., page_token: _Optional[str]=..., query: _Optional[str]=...) -> None:
        ...

class SearchFoldersResponse(_message.Message):
    __slots__ = ('folders', 'next_page_token')
    FOLDERS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    folders: _containers.RepeatedCompositeFieldContainer[Folder]
    next_page_token: str

    def __init__(self, folders: _Optional[_Iterable[_Union[Folder, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetFolderRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateFolderRequest(_message.Message):
    __slots__ = ('parent', 'folder')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FOLDER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    folder: Folder

    def __init__(self, parent: _Optional[str]=..., folder: _Optional[_Union[Folder, _Mapping]]=...) -> None:
        ...

class MoveFolderRequest(_message.Message):
    __slots__ = ('name', 'destination_parent')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_PARENT_FIELD_NUMBER: _ClassVar[int]
    name: str
    destination_parent: str

    def __init__(self, name: _Optional[str]=..., destination_parent: _Optional[str]=...) -> None:
        ...

class UpdateFolderRequest(_message.Message):
    __slots__ = ('folder', 'update_mask')
    FOLDER_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    folder: Folder
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, folder: _Optional[_Union[Folder, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteFolderRequest(_message.Message):
    __slots__ = ('name', 'recursive_delete')
    NAME_FIELD_NUMBER: _ClassVar[int]
    RECURSIVE_DELETE_FIELD_NUMBER: _ClassVar[int]
    name: str
    recursive_delete: bool

    def __init__(self, name: _Optional[str]=..., recursive_delete: bool=...) -> None:
        ...

class UndeleteFolderRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class FolderOperation(_message.Message):
    __slots__ = ('display_name', 'operation_type', 'source_parent', 'destination_parent')

    class OperationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        OPERATION_TYPE_UNSPECIFIED: _ClassVar[FolderOperation.OperationType]
        CREATE: _ClassVar[FolderOperation.OperationType]
        MOVE: _ClassVar[FolderOperation.OperationType]
    OPERATION_TYPE_UNSPECIFIED: FolderOperation.OperationType
    CREATE: FolderOperation.OperationType
    MOVE: FolderOperation.OperationType
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    OPERATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_PARENT_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_PARENT_FIELD_NUMBER: _ClassVar[int]
    display_name: str
    operation_type: FolderOperation.OperationType
    source_parent: str
    destination_parent: str

    def __init__(self, display_name: _Optional[str]=..., operation_type: _Optional[_Union[FolderOperation.OperationType, str]]=..., source_parent: _Optional[str]=..., destination_parent: _Optional[str]=...) -> None:
        ...