from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.shopping.merchant.products.v1beta import products_common_pb2 as _products_common_pb2
from google.shopping.type import types_pb2 as _types_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Product(_message.Message):
    __slots__ = ("name", "channel", "offer_id", "content_language", "feed_label", "data_source", "version_number", "attributes", "custom_attributes", "product_status")
    NAME_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    OFFER_ID_FIELD_NUMBER: _ClassVar[int]
    CONTENT_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    FEED_LABEL_FIELD_NUMBER: _ClassVar[int]
    DATA_SOURCE_FIELD_NUMBER: _ClassVar[int]
    VERSION_NUMBER_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_STATUS_FIELD_NUMBER: _ClassVar[int]
    name: str
    channel: _types_pb2.Channel.ChannelEnum
    offer_id: str
    content_language: str
    feed_label: str
    data_source: str
    version_number: int
    attributes: _products_common_pb2.Attributes
    custom_attributes: _containers.RepeatedCompositeFieldContainer[_types_pb2.CustomAttribute]
    product_status: _products_common_pb2.ProductStatus
    def __init__(self, name: _Optional[str] = ..., channel: _Optional[_Union[_types_pb2.Channel.ChannelEnum, str]] = ..., offer_id: _Optional[str] = ..., content_language: _Optional[str] = ..., feed_label: _Optional[str] = ..., data_source: _Optional[str] = ..., version_number: _Optional[int] = ..., attributes: _Optional[_Union[_products_common_pb2.Attributes, _Mapping]] = ..., custom_attributes: _Optional[_Iterable[_Union[_types_pb2.CustomAttribute, _Mapping]]] = ..., product_status: _Optional[_Union[_products_common_pb2.ProductStatus, _Mapping]] = ...) -> None: ...

class GetProductRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListProductsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListProductsResponse(_message.Message):
    __slots__ = ("products", "next_page_token")
    PRODUCTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    products: _containers.RepeatedCompositeFieldContainer[Product]
    next_page_token: str
    def __init__(self, products: _Optional[_Iterable[_Union[Product, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...
