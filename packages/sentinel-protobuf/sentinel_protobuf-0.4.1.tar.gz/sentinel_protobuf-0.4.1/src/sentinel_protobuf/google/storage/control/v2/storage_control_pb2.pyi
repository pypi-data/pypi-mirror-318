from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import field_info_pb2 as _field_info_pb2
from google.api import resource_pb2 as _resource_pb2
from google.api import routing_pb2 as _routing_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PendingRenameInfo(_message.Message):
    __slots__ = ("operation",)
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    operation: str
    def __init__(self, operation: _Optional[str] = ...) -> None: ...

class Folder(_message.Message):
    __slots__ = ("name", "metageneration", "create_time", "update_time", "pending_rename_info")
    NAME_FIELD_NUMBER: _ClassVar[int]
    METAGENERATION_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    PENDING_RENAME_INFO_FIELD_NUMBER: _ClassVar[int]
    name: str
    metageneration: int
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    pending_rename_info: PendingRenameInfo
    def __init__(self, name: _Optional[str] = ..., metageneration: _Optional[int] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., pending_rename_info: _Optional[_Union[PendingRenameInfo, _Mapping]] = ...) -> None: ...

class GetFolderRequest(_message.Message):
    __slots__ = ("name", "if_metageneration_match", "if_metageneration_not_match", "request_id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    IF_METAGENERATION_MATCH_FIELD_NUMBER: _ClassVar[int]
    IF_METAGENERATION_NOT_MATCH_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    if_metageneration_match: int
    if_metageneration_not_match: int
    request_id: str
    def __init__(self, name: _Optional[str] = ..., if_metageneration_match: _Optional[int] = ..., if_metageneration_not_match: _Optional[int] = ..., request_id: _Optional[str] = ...) -> None: ...

class CreateFolderRequest(_message.Message):
    __slots__ = ("parent", "folder", "folder_id", "recursive", "request_id")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FOLDER_FIELD_NUMBER: _ClassVar[int]
    FOLDER_ID_FIELD_NUMBER: _ClassVar[int]
    RECURSIVE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    folder: Folder
    folder_id: str
    recursive: bool
    request_id: str
    def __init__(self, parent: _Optional[str] = ..., folder: _Optional[_Union[Folder, _Mapping]] = ..., folder_id: _Optional[str] = ..., recursive: bool = ..., request_id: _Optional[str] = ...) -> None: ...

class DeleteFolderRequest(_message.Message):
    __slots__ = ("name", "if_metageneration_match", "if_metageneration_not_match", "request_id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    IF_METAGENERATION_MATCH_FIELD_NUMBER: _ClassVar[int]
    IF_METAGENERATION_NOT_MATCH_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    if_metageneration_match: int
    if_metageneration_not_match: int
    request_id: str
    def __init__(self, name: _Optional[str] = ..., if_metageneration_match: _Optional[int] = ..., if_metageneration_not_match: _Optional[int] = ..., request_id: _Optional[str] = ...) -> None: ...

class ListFoldersRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token", "prefix", "delimiter", "lexicographic_start", "lexicographic_end", "request_id")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PREFIX_FIELD_NUMBER: _ClassVar[int]
    DELIMITER_FIELD_NUMBER: _ClassVar[int]
    LEXICOGRAPHIC_START_FIELD_NUMBER: _ClassVar[int]
    LEXICOGRAPHIC_END_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    prefix: str
    delimiter: str
    lexicographic_start: str
    lexicographic_end: str
    request_id: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., prefix: _Optional[str] = ..., delimiter: _Optional[str] = ..., lexicographic_start: _Optional[str] = ..., lexicographic_end: _Optional[str] = ..., request_id: _Optional[str] = ...) -> None: ...

class ListFoldersResponse(_message.Message):
    __slots__ = ("folders", "next_page_token")
    FOLDERS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    folders: _containers.RepeatedCompositeFieldContainer[Folder]
    next_page_token: str
    def __init__(self, folders: _Optional[_Iterable[_Union[Folder, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class RenameFolderRequest(_message.Message):
    __slots__ = ("name", "destination_folder_id", "if_metageneration_match", "if_metageneration_not_match", "request_id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_FOLDER_ID_FIELD_NUMBER: _ClassVar[int]
    IF_METAGENERATION_MATCH_FIELD_NUMBER: _ClassVar[int]
    IF_METAGENERATION_NOT_MATCH_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    destination_folder_id: str
    if_metageneration_match: int
    if_metageneration_not_match: int
    request_id: str
    def __init__(self, name: _Optional[str] = ..., destination_folder_id: _Optional[str] = ..., if_metageneration_match: _Optional[int] = ..., if_metageneration_not_match: _Optional[int] = ..., request_id: _Optional[str] = ...) -> None: ...

class CommonLongRunningOperationMetadata(_message.Message):
    __slots__ = ("create_time", "end_time", "update_time", "type", "requested_cancellation", "progress_percent")
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_CANCELLATION_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_PERCENT_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    type: str
    requested_cancellation: bool
    progress_percent: int
    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., type: _Optional[str] = ..., requested_cancellation: bool = ..., progress_percent: _Optional[int] = ...) -> None: ...

class RenameFolderMetadata(_message.Message):
    __slots__ = ("common_metadata", "source_folder_id", "destination_folder_id")
    COMMON_METADATA_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FOLDER_ID_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_FOLDER_ID_FIELD_NUMBER: _ClassVar[int]
    common_metadata: CommonLongRunningOperationMetadata
    source_folder_id: str
    destination_folder_id: str
    def __init__(self, common_metadata: _Optional[_Union[CommonLongRunningOperationMetadata, _Mapping]] = ..., source_folder_id: _Optional[str] = ..., destination_folder_id: _Optional[str] = ...) -> None: ...

class StorageLayout(_message.Message):
    __slots__ = ("name", "location", "location_type", "custom_placement_config", "hierarchical_namespace")
    class CustomPlacementConfig(_message.Message):
        __slots__ = ("data_locations",)
        DATA_LOCATIONS_FIELD_NUMBER: _ClassVar[int]
        data_locations: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, data_locations: _Optional[_Iterable[str]] = ...) -> None: ...
    class HierarchicalNamespace(_message.Message):
        __slots__ = ("enabled",)
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        enabled: bool
        def __init__(self, enabled: bool = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    LOCATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_PLACEMENT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    HIERARCHICAL_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    name: str
    location: str
    location_type: str
    custom_placement_config: StorageLayout.CustomPlacementConfig
    hierarchical_namespace: StorageLayout.HierarchicalNamespace
    def __init__(self, name: _Optional[str] = ..., location: _Optional[str] = ..., location_type: _Optional[str] = ..., custom_placement_config: _Optional[_Union[StorageLayout.CustomPlacementConfig, _Mapping]] = ..., hierarchical_namespace: _Optional[_Union[StorageLayout.HierarchicalNamespace, _Mapping]] = ...) -> None: ...

class GetStorageLayoutRequest(_message.Message):
    __slots__ = ("name", "prefix", "request_id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PREFIX_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    prefix: str
    request_id: str
    def __init__(self, name: _Optional[str] = ..., prefix: _Optional[str] = ..., request_id: _Optional[str] = ...) -> None: ...

class ManagedFolder(_message.Message):
    __slots__ = ("name", "metageneration", "create_time", "update_time")
    NAME_FIELD_NUMBER: _ClassVar[int]
    METAGENERATION_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    metageneration: int
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    def __init__(self, name: _Optional[str] = ..., metageneration: _Optional[int] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class GetManagedFolderRequest(_message.Message):
    __slots__ = ("name", "if_metageneration_match", "if_metageneration_not_match", "request_id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    IF_METAGENERATION_MATCH_FIELD_NUMBER: _ClassVar[int]
    IF_METAGENERATION_NOT_MATCH_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    if_metageneration_match: int
    if_metageneration_not_match: int
    request_id: str
    def __init__(self, name: _Optional[str] = ..., if_metageneration_match: _Optional[int] = ..., if_metageneration_not_match: _Optional[int] = ..., request_id: _Optional[str] = ...) -> None: ...

class CreateManagedFolderRequest(_message.Message):
    __slots__ = ("parent", "managed_folder", "managed_folder_id", "request_id")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    MANAGED_FOLDER_FIELD_NUMBER: _ClassVar[int]
    MANAGED_FOLDER_ID_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    managed_folder: ManagedFolder
    managed_folder_id: str
    request_id: str
    def __init__(self, parent: _Optional[str] = ..., managed_folder: _Optional[_Union[ManagedFolder, _Mapping]] = ..., managed_folder_id: _Optional[str] = ..., request_id: _Optional[str] = ...) -> None: ...

class DeleteManagedFolderRequest(_message.Message):
    __slots__ = ("name", "if_metageneration_match", "if_metageneration_not_match", "allow_non_empty", "request_id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    IF_METAGENERATION_MATCH_FIELD_NUMBER: _ClassVar[int]
    IF_METAGENERATION_NOT_MATCH_FIELD_NUMBER: _ClassVar[int]
    ALLOW_NON_EMPTY_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    if_metageneration_match: int
    if_metageneration_not_match: int
    allow_non_empty: bool
    request_id: str
    def __init__(self, name: _Optional[str] = ..., if_metageneration_match: _Optional[int] = ..., if_metageneration_not_match: _Optional[int] = ..., allow_non_empty: bool = ..., request_id: _Optional[str] = ...) -> None: ...

class ListManagedFoldersRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token", "prefix", "request_id")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PREFIX_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    prefix: str
    request_id: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., prefix: _Optional[str] = ..., request_id: _Optional[str] = ...) -> None: ...

class ListManagedFoldersResponse(_message.Message):
    __slots__ = ("managed_folders", "next_page_token")
    MANAGED_FOLDERS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    managed_folders: _containers.RepeatedCompositeFieldContainer[ManagedFolder]
    next_page_token: str
    def __init__(self, managed_folders: _Optional[_Iterable[_Union[ManagedFolder, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...
