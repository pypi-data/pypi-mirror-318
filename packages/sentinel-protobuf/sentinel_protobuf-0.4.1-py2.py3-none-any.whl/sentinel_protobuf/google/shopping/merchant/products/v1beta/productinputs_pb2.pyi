from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.shopping.merchant.products.v1beta import products_common_pb2 as _products_common_pb2
from google.shopping.type import types_pb2 as _types_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProductInput(_message.Message):
    __slots__ = ("name", "product", "channel", "offer_id", "content_language", "feed_label", "version_number", "attributes", "custom_attributes")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    OFFER_ID_FIELD_NUMBER: _ClassVar[int]
    CONTENT_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    FEED_LABEL_FIELD_NUMBER: _ClassVar[int]
    VERSION_NUMBER_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    name: str
    product: str
    channel: _types_pb2.Channel.ChannelEnum
    offer_id: str
    content_language: str
    feed_label: str
    version_number: int
    attributes: _products_common_pb2.Attributes
    custom_attributes: _containers.RepeatedCompositeFieldContainer[_types_pb2.CustomAttribute]
    def __init__(self, name: _Optional[str] = ..., product: _Optional[str] = ..., channel: _Optional[_Union[_types_pb2.Channel.ChannelEnum, str]] = ..., offer_id: _Optional[str] = ..., content_language: _Optional[str] = ..., feed_label: _Optional[str] = ..., version_number: _Optional[int] = ..., attributes: _Optional[_Union[_products_common_pb2.Attributes, _Mapping]] = ..., custom_attributes: _Optional[_Iterable[_Union[_types_pb2.CustomAttribute, _Mapping]]] = ...) -> None: ...

class InsertProductInputRequest(_message.Message):
    __slots__ = ("parent", "product_input", "data_source")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_INPUT_FIELD_NUMBER: _ClassVar[int]
    DATA_SOURCE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    product_input: ProductInput
    data_source: str
    def __init__(self, parent: _Optional[str] = ..., product_input: _Optional[_Union[ProductInput, _Mapping]] = ..., data_source: _Optional[str] = ...) -> None: ...

class DeleteProductInputRequest(_message.Message):
    __slots__ = ("name", "data_source")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DATA_SOURCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    data_source: str
    def __init__(self, name: _Optional[str] = ..., data_source: _Optional[str] = ...) -> None: ...
