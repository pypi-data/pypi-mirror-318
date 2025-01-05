from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.shopping.css.v1 import css_product_common_pb2 as _css_product_common_pb2
from google.shopping.type import types_pb2 as _types_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetCssProductRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CssProduct(_message.Message):
    __slots__ = ("name", "raw_provided_id", "content_language", "feed_label", "attributes", "custom_attributes", "css_product_status")
    NAME_FIELD_NUMBER: _ClassVar[int]
    RAW_PROVIDED_ID_FIELD_NUMBER: _ClassVar[int]
    CONTENT_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    FEED_LABEL_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    CSS_PRODUCT_STATUS_FIELD_NUMBER: _ClassVar[int]
    name: str
    raw_provided_id: str
    content_language: str
    feed_label: str
    attributes: _css_product_common_pb2.Attributes
    custom_attributes: _containers.RepeatedCompositeFieldContainer[_types_pb2.CustomAttribute]
    css_product_status: _css_product_common_pb2.CssProductStatus
    def __init__(self, name: _Optional[str] = ..., raw_provided_id: _Optional[str] = ..., content_language: _Optional[str] = ..., feed_label: _Optional[str] = ..., attributes: _Optional[_Union[_css_product_common_pb2.Attributes, _Mapping]] = ..., custom_attributes: _Optional[_Iterable[_Union[_types_pb2.CustomAttribute, _Mapping]]] = ..., css_product_status: _Optional[_Union[_css_product_common_pb2.CssProductStatus, _Mapping]] = ...) -> None: ...

class ListCssProductsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListCssProductsResponse(_message.Message):
    __slots__ = ("css_products", "next_page_token")
    CSS_PRODUCTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    css_products: _containers.RepeatedCompositeFieldContainer[CssProduct]
    next_page_token: str
    def __init__(self, css_products: _Optional[_Iterable[_Union[CssProduct, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...
