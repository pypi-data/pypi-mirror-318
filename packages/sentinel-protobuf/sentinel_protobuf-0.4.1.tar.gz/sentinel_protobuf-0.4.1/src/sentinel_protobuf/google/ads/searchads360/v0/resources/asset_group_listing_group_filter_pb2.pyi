from google.ads.searchads360.v0.enums import listing_group_filter_bidding_category_level_pb2 as _listing_group_filter_bidding_category_level_pb2
from google.ads.searchads360.v0.enums import listing_group_filter_custom_attribute_index_pb2 as _listing_group_filter_custom_attribute_index_pb2
from google.ads.searchads360.v0.enums import listing_group_filter_product_channel_pb2 as _listing_group_filter_product_channel_pb2
from google.ads.searchads360.v0.enums import listing_group_filter_product_condition_pb2 as _listing_group_filter_product_condition_pb2
from google.ads.searchads360.v0.enums import listing_group_filter_product_type_level_pb2 as _listing_group_filter_product_type_level_pb2
from google.ads.searchads360.v0.enums import listing_group_filter_type_enum_pb2 as _listing_group_filter_type_enum_pb2
from google.ads.searchads360.v0.enums import listing_group_filter_vertical_pb2 as _listing_group_filter_vertical_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AssetGroupListingGroupFilter(_message.Message):
    __slots__ = ("resource_name", "asset_group", "id", "type", "vertical", "case_value", "parent_listing_group_filter", "path")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    ASSET_GROUP_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VERTICAL_FIELD_NUMBER: _ClassVar[int]
    CASE_VALUE_FIELD_NUMBER: _ClassVar[int]
    PARENT_LISTING_GROUP_FILTER_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    asset_group: str
    id: int
    type: _listing_group_filter_type_enum_pb2.ListingGroupFilterTypeEnum.ListingGroupFilterType
    vertical: _listing_group_filter_vertical_pb2.ListingGroupFilterVerticalEnum.ListingGroupFilterVertical
    case_value: ListingGroupFilterDimension
    parent_listing_group_filter: str
    path: ListingGroupFilterDimensionPath
    def __init__(self, resource_name: _Optional[str] = ..., asset_group: _Optional[str] = ..., id: _Optional[int] = ..., type: _Optional[_Union[_listing_group_filter_type_enum_pb2.ListingGroupFilterTypeEnum.ListingGroupFilterType, str]] = ..., vertical: _Optional[_Union[_listing_group_filter_vertical_pb2.ListingGroupFilterVerticalEnum.ListingGroupFilterVertical, str]] = ..., case_value: _Optional[_Union[ListingGroupFilterDimension, _Mapping]] = ..., parent_listing_group_filter: _Optional[str] = ..., path: _Optional[_Union[ListingGroupFilterDimensionPath, _Mapping]] = ...) -> None: ...

class ListingGroupFilterDimensionPath(_message.Message):
    __slots__ = ("dimensions",)
    DIMENSIONS_FIELD_NUMBER: _ClassVar[int]
    dimensions: _containers.RepeatedCompositeFieldContainer[ListingGroupFilterDimension]
    def __init__(self, dimensions: _Optional[_Iterable[_Union[ListingGroupFilterDimension, _Mapping]]] = ...) -> None: ...

class ListingGroupFilterDimension(_message.Message):
    __slots__ = ("product_bidding_category", "product_brand", "product_channel", "product_condition", "product_custom_attribute", "product_item_id", "product_type")
    class ProductBiddingCategory(_message.Message):
        __slots__ = ("id", "level")
        ID_FIELD_NUMBER: _ClassVar[int]
        LEVEL_FIELD_NUMBER: _ClassVar[int]
        id: int
        level: _listing_group_filter_bidding_category_level_pb2.ListingGroupFilterBiddingCategoryLevelEnum.ListingGroupFilterBiddingCategoryLevel
        def __init__(self, id: _Optional[int] = ..., level: _Optional[_Union[_listing_group_filter_bidding_category_level_pb2.ListingGroupFilterBiddingCategoryLevelEnum.ListingGroupFilterBiddingCategoryLevel, str]] = ...) -> None: ...
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
    PRODUCT_BIDDING_CATEGORY_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_BRAND_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_CHANNEL_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_CONDITION_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_CUSTOM_ATTRIBUTE_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_TYPE_FIELD_NUMBER: _ClassVar[int]
    product_bidding_category: ListingGroupFilterDimension.ProductBiddingCategory
    product_brand: ListingGroupFilterDimension.ProductBrand
    product_channel: ListingGroupFilterDimension.ProductChannel
    product_condition: ListingGroupFilterDimension.ProductCondition
    product_custom_attribute: ListingGroupFilterDimension.ProductCustomAttribute
    product_item_id: ListingGroupFilterDimension.ProductItemId
    product_type: ListingGroupFilterDimension.ProductType
    def __init__(self, product_bidding_category: _Optional[_Union[ListingGroupFilterDimension.ProductBiddingCategory, _Mapping]] = ..., product_brand: _Optional[_Union[ListingGroupFilterDimension.ProductBrand, _Mapping]] = ..., product_channel: _Optional[_Union[ListingGroupFilterDimension.ProductChannel, _Mapping]] = ..., product_condition: _Optional[_Union[ListingGroupFilterDimension.ProductCondition, _Mapping]] = ..., product_custom_attribute: _Optional[_Union[ListingGroupFilterDimension.ProductCustomAttribute, _Mapping]] = ..., product_item_id: _Optional[_Union[ListingGroupFilterDimension.ProductItemId, _Mapping]] = ..., product_type: _Optional[_Union[ListingGroupFilterDimension.ProductType, _Mapping]] = ...) -> None: ...
