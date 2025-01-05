from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.asset.v1p5beta1 import assets_pb2 as _assets_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ContentType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CONTENT_TYPE_UNSPECIFIED: _ClassVar[ContentType]
    RESOURCE: _ClassVar[ContentType]
    IAM_POLICY: _ClassVar[ContentType]
    ORG_POLICY: _ClassVar[ContentType]
    ACCESS_POLICY: _ClassVar[ContentType]
CONTENT_TYPE_UNSPECIFIED: ContentType
RESOURCE: ContentType
IAM_POLICY: ContentType
ORG_POLICY: ContentType
ACCESS_POLICY: ContentType

class ListAssetsRequest(_message.Message):
    __slots__ = ('parent', 'read_time', 'asset_types', 'content_type', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    READ_TIME_FIELD_NUMBER: _ClassVar[int]
    ASSET_TYPES_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    read_time: _timestamp_pb2.Timestamp
    asset_types: _containers.RepeatedScalarFieldContainer[str]
    content_type: ContentType
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., read_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., asset_types: _Optional[_Iterable[str]]=..., content_type: _Optional[_Union[ContentType, str]]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListAssetsResponse(_message.Message):
    __slots__ = ('read_time', 'assets', 'next_page_token')
    READ_TIME_FIELD_NUMBER: _ClassVar[int]
    ASSETS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    read_time: _timestamp_pb2.Timestamp
    assets: _containers.RepeatedCompositeFieldContainer[_assets_pb2.Asset]
    next_page_token: str

    def __init__(self, read_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., assets: _Optional[_Iterable[_Union[_assets_pb2.Asset, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...