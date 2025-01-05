from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.cloud.recommendationengine.v1beta1 import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CatalogItem(_message.Message):
    __slots__ = ('id', 'category_hierarchies', 'title', 'description', 'item_attributes', 'language_code', 'tags', 'item_group_id', 'product_metadata')

    class CategoryHierarchy(_message.Message):
        __slots__ = ('categories',)
        CATEGORIES_FIELD_NUMBER: _ClassVar[int]
        categories: _containers.RepeatedScalarFieldContainer[str]

        def __init__(self, categories: _Optional[_Iterable[str]]=...) -> None:
            ...
    ID_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_HIERARCHIES_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ITEM_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    ITEM_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_METADATA_FIELD_NUMBER: _ClassVar[int]
    id: str
    category_hierarchies: _containers.RepeatedCompositeFieldContainer[CatalogItem.CategoryHierarchy]
    title: str
    description: str
    item_attributes: _common_pb2.FeatureMap
    language_code: str
    tags: _containers.RepeatedScalarFieldContainer[str]
    item_group_id: str
    product_metadata: ProductCatalogItem

    def __init__(self, id: _Optional[str]=..., category_hierarchies: _Optional[_Iterable[_Union[CatalogItem.CategoryHierarchy, _Mapping]]]=..., title: _Optional[str]=..., description: _Optional[str]=..., item_attributes: _Optional[_Union[_common_pb2.FeatureMap, _Mapping]]=..., language_code: _Optional[str]=..., tags: _Optional[_Iterable[str]]=..., item_group_id: _Optional[str]=..., product_metadata: _Optional[_Union[ProductCatalogItem, _Mapping]]=...) -> None:
        ...

class ProductCatalogItem(_message.Message):
    __slots__ = ('exact_price', 'price_range', 'costs', 'currency_code', 'stock_state', 'available_quantity', 'canonical_product_uri', 'images')

    class StockState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STOCK_STATE_UNSPECIFIED: _ClassVar[ProductCatalogItem.StockState]
        IN_STOCK: _ClassVar[ProductCatalogItem.StockState]
        OUT_OF_STOCK: _ClassVar[ProductCatalogItem.StockState]
        PREORDER: _ClassVar[ProductCatalogItem.StockState]
        BACKORDER: _ClassVar[ProductCatalogItem.StockState]
    STOCK_STATE_UNSPECIFIED: ProductCatalogItem.StockState
    IN_STOCK: ProductCatalogItem.StockState
    OUT_OF_STOCK: ProductCatalogItem.StockState
    PREORDER: ProductCatalogItem.StockState
    BACKORDER: ProductCatalogItem.StockState

    class ExactPrice(_message.Message):
        __slots__ = ('display_price', 'original_price')
        DISPLAY_PRICE_FIELD_NUMBER: _ClassVar[int]
        ORIGINAL_PRICE_FIELD_NUMBER: _ClassVar[int]
        display_price: float
        original_price: float

        def __init__(self, display_price: _Optional[float]=..., original_price: _Optional[float]=...) -> None:
            ...

    class PriceRange(_message.Message):
        __slots__ = ('min', 'max')
        MIN_FIELD_NUMBER: _ClassVar[int]
        MAX_FIELD_NUMBER: _ClassVar[int]
        min: float
        max: float

        def __init__(self, min: _Optional[float]=..., max: _Optional[float]=...) -> None:
            ...

    class CostsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: float

        def __init__(self, key: _Optional[str]=..., value: _Optional[float]=...) -> None:
            ...
    EXACT_PRICE_FIELD_NUMBER: _ClassVar[int]
    PRICE_RANGE_FIELD_NUMBER: _ClassVar[int]
    COSTS_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_CODE_FIELD_NUMBER: _ClassVar[int]
    STOCK_STATE_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    CANONICAL_PRODUCT_URI_FIELD_NUMBER: _ClassVar[int]
    IMAGES_FIELD_NUMBER: _ClassVar[int]
    exact_price: ProductCatalogItem.ExactPrice
    price_range: ProductCatalogItem.PriceRange
    costs: _containers.ScalarMap[str, float]
    currency_code: str
    stock_state: ProductCatalogItem.StockState
    available_quantity: int
    canonical_product_uri: str
    images: _containers.RepeatedCompositeFieldContainer[Image]

    def __init__(self, exact_price: _Optional[_Union[ProductCatalogItem.ExactPrice, _Mapping]]=..., price_range: _Optional[_Union[ProductCatalogItem.PriceRange, _Mapping]]=..., costs: _Optional[_Mapping[str, float]]=..., currency_code: _Optional[str]=..., stock_state: _Optional[_Union[ProductCatalogItem.StockState, str]]=..., available_quantity: _Optional[int]=..., canonical_product_uri: _Optional[str]=..., images: _Optional[_Iterable[_Union[Image, _Mapping]]]=...) -> None:
        ...

class Image(_message.Message):
    __slots__ = ('uri', 'height', 'width')
    URI_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    uri: str
    height: int
    width: int

    def __init__(self, uri: _Optional[str]=..., height: _Optional[int]=..., width: _Optional[int]=...) -> None:
        ...