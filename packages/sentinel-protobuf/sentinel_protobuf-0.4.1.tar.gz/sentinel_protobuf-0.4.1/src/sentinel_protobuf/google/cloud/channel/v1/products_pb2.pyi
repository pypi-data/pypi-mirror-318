from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class MediaType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MEDIA_TYPE_UNSPECIFIED: _ClassVar[MediaType]
    MEDIA_TYPE_IMAGE: _ClassVar[MediaType]
MEDIA_TYPE_UNSPECIFIED: MediaType
MEDIA_TYPE_IMAGE: MediaType

class Product(_message.Message):
    __slots__ = ('name', 'marketing_info')
    NAME_FIELD_NUMBER: _ClassVar[int]
    MARKETING_INFO_FIELD_NUMBER: _ClassVar[int]
    name: str
    marketing_info: MarketingInfo

    def __init__(self, name: _Optional[str]=..., marketing_info: _Optional[_Union[MarketingInfo, _Mapping]]=...) -> None:
        ...

class Sku(_message.Message):
    __slots__ = ('name', 'marketing_info', 'product')
    NAME_FIELD_NUMBER: _ClassVar[int]
    MARKETING_INFO_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_FIELD_NUMBER: _ClassVar[int]
    name: str
    marketing_info: MarketingInfo
    product: Product

    def __init__(self, name: _Optional[str]=..., marketing_info: _Optional[_Union[MarketingInfo, _Mapping]]=..., product: _Optional[_Union[Product, _Mapping]]=...) -> None:
        ...

class MarketingInfo(_message.Message):
    __slots__ = ('display_name', 'description', 'default_logo')
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_LOGO_FIELD_NUMBER: _ClassVar[int]
    display_name: str
    description: str
    default_logo: Media

    def __init__(self, display_name: _Optional[str]=..., description: _Optional[str]=..., default_logo: _Optional[_Union[Media, _Mapping]]=...) -> None:
        ...

class Media(_message.Message):
    __slots__ = ('title', 'content', 'type')
    TITLE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    title: str
    content: str
    type: MediaType

    def __init__(self, title: _Optional[str]=..., content: _Optional[str]=..., type: _Optional[_Union[MediaType, str]]=...) -> None:
        ...