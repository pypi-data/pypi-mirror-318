from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.devtools.artifactregistry.v1 import tag_pb2 as _tag_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class VersionView(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    VERSION_VIEW_UNSPECIFIED: _ClassVar[VersionView]
    BASIC: _ClassVar[VersionView]
    FULL: _ClassVar[VersionView]
VERSION_VIEW_UNSPECIFIED: VersionView
BASIC: VersionView
FULL: VersionView

class Version(_message.Message):
    __slots__ = ('name', 'description', 'create_time', 'update_time', 'related_tags', 'metadata', 'annotations')

    class AnnotationsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    RELATED_TAGS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    related_tags: _containers.RepeatedCompositeFieldContainer[_tag_pb2.Tag]
    metadata: _struct_pb2.Struct
    annotations: _containers.ScalarMap[str, str]

    def __init__(self, name: _Optional[str]=..., description: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., related_tags: _Optional[_Iterable[_Union[_tag_pb2.Tag, _Mapping]]]=..., metadata: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=..., annotations: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class ListVersionsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'view', 'order_by', 'filter')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    view: VersionView
    order_by: str
    filter: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., view: _Optional[_Union[VersionView, str]]=..., order_by: _Optional[str]=..., filter: _Optional[str]=...) -> None:
        ...

class ListVersionsResponse(_message.Message):
    __slots__ = ('versions', 'next_page_token')
    VERSIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    versions: _containers.RepeatedCompositeFieldContainer[Version]
    next_page_token: str

    def __init__(self, versions: _Optional[_Iterable[_Union[Version, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetVersionRequest(_message.Message):
    __slots__ = ('name', 'view')
    NAME_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    name: str
    view: VersionView

    def __init__(self, name: _Optional[str]=..., view: _Optional[_Union[VersionView, str]]=...) -> None:
        ...

class DeleteVersionRequest(_message.Message):
    __slots__ = ('name', 'force')
    NAME_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    force: bool

    def __init__(self, name: _Optional[str]=..., force: bool=...) -> None:
        ...

class BatchDeleteVersionsRequest(_message.Message):
    __slots__ = ('parent', 'names', 'validate_only')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NAMES_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    names: _containers.RepeatedScalarFieldContainer[str]
    validate_only: bool

    def __init__(self, parent: _Optional[str]=..., names: _Optional[_Iterable[str]]=..., validate_only: bool=...) -> None:
        ...

class BatchDeleteVersionsMetadata(_message.Message):
    __slots__ = ('failed_versions',)
    FAILED_VERSIONS_FIELD_NUMBER: _ClassVar[int]
    failed_versions: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, failed_versions: _Optional[_Iterable[str]]=...) -> None:
        ...

class UpdateVersionRequest(_message.Message):
    __slots__ = ('version', 'update_mask')
    VERSION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    version: Version
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, version: _Optional[_Union[Version, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...