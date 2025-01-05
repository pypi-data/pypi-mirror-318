from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Version(_message.Message):
    __slots__ = ('name', 'description', 'version_number', 'create_time', 'status')

    class VersionStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        VERSION_STATUS_UNSPECIFIED: _ClassVar[Version.VersionStatus]
        IN_PROGRESS: _ClassVar[Version.VersionStatus]
        READY: _ClassVar[Version.VersionStatus]
        FAILED: _ClassVar[Version.VersionStatus]
    VERSION_STATUS_UNSPECIFIED: Version.VersionStatus
    IN_PROGRESS: Version.VersionStatus
    READY: Version.VersionStatus
    FAILED: Version.VersionStatus
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    VERSION_NUMBER_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    version_number: int
    create_time: _timestamp_pb2.Timestamp
    status: Version.VersionStatus

    def __init__(self, name: _Optional[str]=..., description: _Optional[str]=..., version_number: _Optional[int]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., status: _Optional[_Union[Version.VersionStatus, str]]=...) -> None:
        ...

class ListVersionsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
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
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateVersionRequest(_message.Message):
    __slots__ = ('parent', 'version')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    parent: str
    version: Version

    def __init__(self, parent: _Optional[str]=..., version: _Optional[_Union[Version, _Mapping]]=...) -> None:
        ...

class UpdateVersionRequest(_message.Message):
    __slots__ = ('version', 'update_mask')
    VERSION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    version: Version
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, version: _Optional[_Union[Version, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteVersionRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...