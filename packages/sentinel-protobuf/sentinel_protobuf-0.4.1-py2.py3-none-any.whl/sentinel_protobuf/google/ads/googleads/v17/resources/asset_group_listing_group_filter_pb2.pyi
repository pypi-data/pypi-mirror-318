from google.ads.googleads.v17.enums import listing_group_filter_custom_attribute_index_pb2 as _listing_group_filter_custom_attribute_index_pb2
from google.ads.googleads.v17.enums import listing_group_filter_listing_source_pb2 as _listing_group_filter_listing_source_pb2
from google.ads.googleads.v17.enums import listing_group_filter_product_category_level_pb2 as _listing_group_filter_product_category_level_pb2
from google.ads.googleads.v17.enums import listing_group_filter_product_channel_pb2 as _listing_group_filter_product_channel_pb2
from google.ads.googleads.v17.enums import listing_group_filter_product_condition_pb2 as _listing_group_filter_product_condition_pb2
from google.ads.googleads.v17.enums import listing_group_filter_product_type_level_pb2 as _listing_group_filter_product_type_level_pb2
from google.ads.googleads.v17.enums import listing_group_filter_type_enum_pb2 as _listing_group_filter_type_enum_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AssetGroupListingGroupFilter(_message.Message):
    __slots__ = ("resource_name", "asset_group", "id", "type", "listing_source", "case_value", "parent_listing_group_filter", "path")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    ASSET_GROUP_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    LISTING_SOURCE_FIELD_NUMBER: _ClassVar[int]
    CASE_VALUE_FIELD_NUMBER: _ClassVar[int]
    PARENT_LISTING_GROUP_FILTER_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    asset_group: str
    id: int
    type: _listing_group_filter_type_enum_pb2.ListingGroupFilterTypeEnum.ListingGroupFilterType
    listing_source: _listing_group_filter_listing_source_pb2.ListingGroupFilterListingSourceEnum.ListingGroupFilterListingSource
    case_value: ListingGroupFilterDimension
    parent_listing_group_filter: str
    path: ListingGroupFilterDimensionPath
    def __init__(self, resource_name: _Optional[str] = ..., asset_group: _Optional[str] = ..., id: _Optional[int] = ..., type: _Optional[_Union[_listing_group_filter_type_enum_pb2.ListingGroupFilterTypeEnum.ListingGroupFilterType, str]] = ..., listing_source: _Optional[_Union[_listing_group_filter_listing_source_pb2.ListingGroupFilterListingSourceEnum.ListingGroupFilterListingSource, str]] = ..., case_value: _Optional[_Union[ListingGroupFilterDimension, _Mapping]] = ..., parent_listing_group_filter: _Optional[str] = ..., path: _Optional[_Union[ListingGroupFilterDimensionPath, _Mapping]] = ...) -> None: ...

class ListingGroupFilterDimensionPath(_message.Message):
    __slots__ = ("dimensions",)
    DIMENSIONS_FIELD_NUMBER: _ClassVar[int]
    dimensions: _containers.RepeatedCompositeFieldContainer[ListingGroupFilterDimension]
    def __init__(self, dimensions: _Optional[_Iterable[_Union[ListingGroupFilterDimension, _Mapping]]] = ...) -> None: ...

class ListingGroupFilterDimension(_message.Message):
    __slots__ = ("product_category", "product_brand", "product_channel", "product_condition", "product_custom_attribute", "product_item_id", "product_type", "webpage")
    class ProductCategory(_message.Message):
        __slots__ = ("category_id", "level")
        CATEGORY_ID_FIELD_NUMBER: _ClassVar[int]
        LEVEL_FIELD_NUMBER: _ClassVar[int]
        category_id: int
        level: _listing_group_filter_product_category_level_pb2.ListingGroupFilterProductCategoryLevelEnum.ListingGroupFilterProductCategoryLevel
        def __init__(self, category_id: _Optional[int] = ..., level: _Optional[_Union[_listing_group_filter_product_category_level_pb2.ListingGroupFilterProductCategoryLevelEnum.ListingGroupFilterProductCategoryLevel, str]] = ...) -> None: ...
    class ProductBrand(_message.Message):
        __slots__ = ("value",)
        VALUE_FIELD_NUMBER: _ClassVar[int]
        value: str
        def __init__(self, value: _Optional[str] = ...) -> None: ...
    class ProductChannel(_message.Message):
        __slots__ = ("channel",)
        CHANNEL_FIELD_NUMBER: _ClassVar[int]
        channel: _listing_group_filter_product_channel_pb2.ListingGroupFilterProductChannelEnum.ListingGroupFilterProductChannel
        def __init__(self, channel: _Optional[_Union[_listing_group_filter_product_channel_pb2.ListingGroupFilterProductChannelEnum.ListingGroupFilterProductChannel, str]] = ...) -> None: ...
    class ProductCondition(_message.Message):
        __slots__ = ("condition",)
        CONDITION_FIELD_NUMBER: _ClassVar[int]
        condition: _listing_group_filter_product_condition_pb2.ListingGroupFilterProductConditionEnum.ListingGroupFilterProductCondition
        def __init__(self, condition: _Optional[_Union[_listing_group_filter_product_condition_pb2.ListingGroupFilterProductConditionEnum.ListingGroupFilterProductCondition, str]] = ...) -> None: ...
    class ProductCustomAttribute(_message.Message):
        __slots__ = ("value", "index")
        VALUE_FIELD_NUMBER: _ClassVar[int]
        INDEX_FIELD_NUMBER: _ClassVar[int]
        value: str
        index: _listing_group_filter_custom_attribute_index_pb2.ListingGroupFilterCustomAttributeIndexEnum.ListingGroupFilterCustomAttributeIndex
        def __init__(self, value: _Optional[str] = ..., index: _Optional[_Union[_listing_group_filter_custom_attribute_index_pb2.ListingGroupFilterCustomAttributeIndexEnum.ListingGroupFilterCustomAttributeIndex, str]] = ...) -> None: ...
    class ProductItemId(_message.Message):
        __slots__ = ("value",)
        VALUE_FIELD_NUMBER: _ClassVar[int]
        value: str
        def __init__(self, value: _Optional[str] = ...) -> None: ...
    class ProductType(_message.Message):
        __slots__ = ("value", "level")
        VALUE_FIELD_NUMBER: _ClassVar[int]
        LEVEL_FIELD_NUMBER: _ClassVar[int]
        value: str
        level: _listing_group_filter_product_type_level_pb2.ListingGroupFilterProductTypeLevelEnum.ListingGroupFilterProductTypeLevel
        def __init__(self, value: _Optional[str] = ..., level: _Optional[_Union[_listing_group_filter_product_type_level_pb2.ListingGroupFilterProductTypeLevelEnum.ListingGroupFilterProductTypeLevel, str]] = ...) -> None: ...
    class Webpage(_message.Message):
        __slots__ = ("conditions",)
        CONDITIONS_FIELD_NUMBER: _ClassVar[int]
        conditions: _containers.RepeatedCompositeFieldContainer[ListingGroupFilterDimension.WebpageCondition]
        def __init__(self, conditions: _Optional[_Iterable[_Union[ListingGroupFilterDimension.WebpageCondition, _Mapping]]] = ...) -> None: ...
    class WebpageCondition(_message.Message):
        __slots__ = ("custom_label", "url_contains")
        CUSTOM_LABEL_FIELD_NUMBER: _ClassVar[int]
        URL_CONTAINS_FIELD_NUMBER: _ClassVar[int]
        custom_label: str
        url_contains: str
        def __init__(self, custom_label: _Optional[str] = ..., url_contains: _Optional[str] = ...) -> None: ...
    PRODUCT_CATEGORY_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_BRAND_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_CHANNEL_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_CONDITION_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_CUSTOM_ATTRIBUTE_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_TYPE_FIELD_NUMBER: _ClassVar[int]
    WEBPAGE_FIELD_NUMBER: _ClassVar[int]
    product_category: ListingGroupFilterDimension.ProductCategory
    product_brand: ListingGroupFilterDimension.ProductBrand
    product_channel: ListingGroupFilterDimension.ProductChannel
    product_condition: ListingGroupFilterDimension.ProductCondition
    product_custom_attribute: ListingGroupFilterDimension.ProductCustomAttribute
    product_item_id: ListingGroupFilterDimension.ProductItemId
    product_type: ListingGroupFilterDimension.ProductType
    webpage: ListingGroupFilterDimension.Webpage
    def __init__(self, product_category: _Optional[_Union[ListingGroupFilterDimension.ProductCategory, _Mapping]] = ..., product_brand: _Optional[_Union[ListingGroupFilterDimension.ProductBrand, _Mapping]] = ..., product_channel: _Optional[_Union[ListingGroupFilterDimension.ProductChannel, _Mapping]] = ..., product_condition: _Optional[_Union[ListingGroupFilterDimension.ProductCondition, _Mapping]] = ..., product_custom_attribute: _Optional[_Union[ListingGroupFilterDimension.ProductCustomAttribute, _Mapping]] = ..., product_item_id: _Optional[_Union[ListingGroupFilterDimension.ProductItemId, _Mapping]] = ..., product_type: _Optional[_Union[ListingGroupFilterDimension.ProductType, _Mapping]] = ..., webpage: _Optional[_Union[ListingGroupFilterDimension.Webpage, _Mapping]] = ...) -> None: ...
