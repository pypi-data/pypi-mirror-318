from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class SearchCatalogsRequest(_message.Message):
    __slots__ = ('resource', 'query', 'page_size', 'page_token')
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    resource: str
    query: str
    page_size: int
    page_token: str

    def __init__(self, resource: _Optional[str]=..., query: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class SearchCatalogsResponse(_message.Message):
    __slots__ = ('catalogs', 'next_page_token')
    CATALOGS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    catalogs: _containers.RepeatedCompositeFieldContainer[Catalog]
    next_page_token: str

    def __init__(self, catalogs: _Optional[_Iterable[_Union[Catalog, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class SearchProductsRequest(_message.Message):
    __slots__ = ('resource', 'query', 'page_size', 'page_token')
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    resource: str
    query: str
    page_size: int
    page_token: str

    def __init__(self, resource: _Optional[str]=..., query: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class SearchProductsResponse(_message.Message):
    __slots__ = ('products', 'next_page_token')
    PRODUCTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    products: _containers.RepeatedCompositeFieldContainer[Product]
    next_page_token: str

    def __init__(self, products: _Optional[_Iterable[_Union[Product, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class SearchVersionsRequest(_message.Message):
    __slots__ = ('resource', 'query', 'page_size', 'page_token')
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    resource: str
    query: str
    page_size: int
    page_token: str

    def __init__(self, resource: _Optional[str]=..., query: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class SearchVersionsResponse(_message.Message):
    __slots__ = ('versions', 'next_page_token')
    VERSIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    versions: _containers.RepeatedCompositeFieldContainer[Version]
    next_page_token: str

    def __init__(self, versions: _Optional[_Iterable[_Union[Version, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class Catalog(_message.Message):
    __slots__ = ('name', 'display_name', 'description', 'create_time', 'update_time')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    description: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., description: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class Product(_message.Message):
    __slots__ = ('name', 'asset_type', 'display_metadata', 'icon_uri', 'asset_references', 'create_time', 'update_time')
    NAME_FIELD_NUMBER: _ClassVar[int]
    ASSET_TYPE_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_METADATA_FIELD_NUMBER: _ClassVar[int]
    ICON_URI_FIELD_NUMBER: _ClassVar[int]
    ASSET_REFERENCES_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    asset_type: str
    display_metadata: _struct_pb2.Struct
    icon_uri: str
    asset_references: _containers.RepeatedCompositeFieldContainer[AssetReference]
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., asset_type: _Optional[str]=..., display_metadata: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=..., icon_uri: _Optional[str]=..., asset_references: _Optional[_Iterable[_Union[AssetReference, _Mapping]]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class AssetReference(_message.Message):
    __slots__ = ('id', 'description', 'inputs', 'validation_status', 'validation_operation', 'asset', 'gcs_path', 'git_source', 'gcs_source', 'create_time', 'update_time', 'version')

    class AssetValidationState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ASSET_VALIDATION_STATE_UNSPECIFIED: _ClassVar[AssetReference.AssetValidationState]
        PENDING: _ClassVar[AssetReference.AssetValidationState]
        VALID: _ClassVar[AssetReference.AssetValidationState]
        INVALID: _ClassVar[AssetReference.AssetValidationState]
    ASSET_VALIDATION_STATE_UNSPECIFIED: AssetReference.AssetValidationState
    PENDING: AssetReference.AssetValidationState
    VALID: AssetReference.AssetValidationState
    INVALID: AssetReference.AssetValidationState
    ID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    INPUTS_FIELD_NUMBER: _ClassVar[int]
    VALIDATION_STATUS_FIELD_NUMBER: _ClassVar[int]
    VALIDATION_OPERATION_FIELD_NUMBER: _ClassVar[int]
    ASSET_FIELD_NUMBER: _ClassVar[int]
    GCS_PATH_FIELD_NUMBER: _ClassVar[int]
    GIT_SOURCE_FIELD_NUMBER: _ClassVar[int]
    GCS_SOURCE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    id: str
    description: str
    inputs: Inputs
    validation_status: AssetReference.AssetValidationState
    validation_operation: _operations_pb2.Operation
    asset: str
    gcs_path: str
    git_source: GitSource
    gcs_source: GcsSource
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    version: str

    def __init__(self, id: _Optional[str]=..., description: _Optional[str]=..., inputs: _Optional[_Union[Inputs, _Mapping]]=..., validation_status: _Optional[_Union[AssetReference.AssetValidationState, str]]=..., validation_operation: _Optional[_Union[_operations_pb2.Operation, _Mapping]]=..., asset: _Optional[str]=..., gcs_path: _Optional[str]=..., git_source: _Optional[_Union[GitSource, _Mapping]]=..., gcs_source: _Optional[_Union[GcsSource, _Mapping]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., version: _Optional[str]=...) -> None:
        ...

class Inputs(_message.Message):
    __slots__ = ('parameters',)
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    parameters: _struct_pb2.Struct

    def __init__(self, parameters: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=...) -> None:
        ...

class GcsSource(_message.Message):
    __slots__ = ('gcs_path', 'generation', 'update_time')
    GCS_PATH_FIELD_NUMBER: _ClassVar[int]
    GENERATION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    gcs_path: str
    generation: int
    update_time: _timestamp_pb2.Timestamp

    def __init__(self, gcs_path: _Optional[str]=..., generation: _Optional[int]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class GitSource(_message.Message):
    __slots__ = ('repo', 'dir', 'commit', 'branch', 'tag')
    REPO_FIELD_NUMBER: _ClassVar[int]
    DIR_FIELD_NUMBER: _ClassVar[int]
    COMMIT_FIELD_NUMBER: _ClassVar[int]
    BRANCH_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    repo: str
    dir: str
    commit: str
    branch: str
    tag: str

    def __init__(self, repo: _Optional[str]=..., dir: _Optional[str]=..., commit: _Optional[str]=..., branch: _Optional[str]=..., tag: _Optional[str]=...) -> None:
        ...

class Version(_message.Message):
    __slots__ = ('name', 'description', 'asset', 'create_time', 'update_time')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ASSET_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    asset: _struct_pb2.Struct
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., description: _Optional[str]=..., asset: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...