from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.type import date_pb2 as _date_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ListImageVersionsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'include_past_releases')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_PAST_RELEASES_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    include_past_releases: bool

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., include_past_releases: bool=...) -> None:
        ...

class ListImageVersionsResponse(_message.Message):
    __slots__ = ('image_versions', 'next_page_token')
    IMAGE_VERSIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    image_versions: _containers.RepeatedCompositeFieldContainer[ImageVersion]
    next_page_token: str

    def __init__(self, image_versions: _Optional[_Iterable[_Union[ImageVersion, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class ImageVersion(_message.Message):
    __slots__ = ('image_version_id', 'is_default', 'supported_python_versions', 'release_date', 'creation_disabled', 'upgrade_disabled')
    IMAGE_VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    IS_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_PYTHON_VERSIONS_FIELD_NUMBER: _ClassVar[int]
    RELEASE_DATE_FIELD_NUMBER: _ClassVar[int]
    CREATION_DISABLED_FIELD_NUMBER: _ClassVar[int]
    UPGRADE_DISABLED_FIELD_NUMBER: _ClassVar[int]
    image_version_id: str
    is_default: bool
    supported_python_versions: _containers.RepeatedScalarFieldContainer[str]
    release_date: _date_pb2.Date
    creation_disabled: bool
    upgrade_disabled: bool

    def __init__(self, image_version_id: _Optional[str]=..., is_default: bool=..., supported_python_versions: _Optional[_Iterable[str]]=..., release_date: _Optional[_Union[_date_pb2.Date, _Mapping]]=..., creation_disabled: bool=..., upgrade_disabled: bool=...) -> None:
        ...