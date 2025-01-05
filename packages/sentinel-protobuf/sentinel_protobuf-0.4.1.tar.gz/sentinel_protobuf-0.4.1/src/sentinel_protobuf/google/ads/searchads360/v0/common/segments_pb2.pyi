from google.ads.searchads360.v0.common import criteria_pb2 as _criteria_pb2
from google.ads.searchads360.v0.common import value_pb2 as _value_pb2
from google.ads.searchads360.v0.enums import ad_network_type_pb2 as _ad_network_type_pb2
from google.ads.searchads360.v0.enums import conversion_action_category_pb2 as _conversion_action_category_pb2
from google.ads.searchads360.v0.enums import day_of_week_pb2 as _day_of_week_pb2
from google.ads.searchads360.v0.enums import device_pb2 as _device_pb2
from google.ads.searchads360.v0.enums import product_channel_pb2 as _product_channel_pb2
from google.ads.searchads360.v0.enums import product_channel_exclusivity_pb2 as _product_channel_exclusivity_pb2
from google.ads.searchads360.v0.enums import product_condition_pb2 as _product_condition_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Segments(_message.Message):
    __slots__ = ("ad_network_type", "conversion_action", "conversion_action_category", "conversion_action_name", "conversion_custom_dimensions", "date", "day_of_week", "device", "geo_target_city", "geo_target_country", "geo_target_metro", "geo_target_region", "hour", "keyword", "month", "product_bidding_category_level1", "product_bidding_category_level2", "product_bidding_category_level3", "product_bidding_category_level4", "product_bidding_category_level5", "product_brand", "product_channel", "product_channel_exclusivity", "product_condition", "product_country", "product_custom_attribute0", "product_custom_attribute1", "product_custom_attribute2", "product_custom_attribute3", "product_custom_attribute4", "product_item_id", "product_language", "product_sold_bidding_category_level1", "product_sold_bidding_category_level2", "product_sold_bidding_category_level3", "product_sold_bidding_category_level4", "product_sold_bidding_category_level5", "product_sold_brand", "product_sold_condition", "product_sold_custom_attribute0", "product_sold_custom_attribute1", "product_sold_custom_attribute2", "product_sold_custom_attribute3", "product_sold_custom_attribute4", "product_sold_item_id", "product_sold_title", "product_sold_type_l1", "product_sold_type_l2", "product_sold_type_l3", "product_sold_type_l4", "product_sold_type_l5", "product_store_id", "product_title", "product_type_l1", "product_type_l2", "product_type_l3", "product_type_l4", "product_type_l5", "quarter", "raw_event_conversion_dimensions", "week", "year", "asset_interaction_target")
    AD_NETWORK_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONVERSION_ACTION_FIELD_NUMBER: _ClassVar[int]
    CONVERSION_ACTION_CATEGORY_FIELD_NUMBER: _ClassVar[int]
    CONVERSION_ACTION_NAME_FIELD_NUMBER: _ClassVar[int]
    CONVERSION_CUSTOM_DIMENSIONS_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    DAY_OF_WEEK_FIELD_NUMBER: _ClassVar[int]
    DEVICE_FIELD_NUMBER: _ClassVar[int]
    GEO_TARGET_CITY_FIELD_NUMBER: _ClassVar[int]
    GEO_TARGET_COUNTRY_FIELD_NUMBER: _ClassVar[int]
    GEO_TARGET_METRO_FIELD_NUMBER: _ClassVar[int]
    GEO_TARGET_REGION_FIELD_NUMBER: _ClassVar[int]
    HOUR_FIELD_NUMBER: _ClassVar[int]
    KEYWORD_FIELD_NUMBER: _ClassVar[int]
    MONTH_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_BIDDING_CATEGORY_LEVEL1_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_BIDDING_CATEGORY_LEVEL2_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_BIDDING_CATEGORY_LEVEL3_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_BIDDING_CATEGORY_LEVEL4_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_BIDDING_CATEGORY_LEVEL5_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_BRAND_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_CHANNEL_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_CHANNEL_EXCLUSIVITY_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_CONDITION_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_COUNTRY_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_CUSTOM_ATTRIBUTE0_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_CUSTOM_ATTRIBUTE1_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_CUSTOM_ATTRIBUTE2_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_CUSTOM_ATTRIBUTE3_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_CUSTOM_ATTRIBUTE4_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_SOLD_BIDDING_CATEGORY_LEVEL1_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_SOLD_BIDDING_CATEGORY_LEVEL2_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_SOLD_BIDDING_CATEGORY_LEVEL3_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_SOLD_BIDDING_CATEGORY_LEVEL4_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_SOLD_BIDDING_CATEGORY_LEVEL5_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_SOLD_BRAND_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_SOLD_CONDITION_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_SOLD_CUSTOM_ATTRIBUTE0_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_SOLD_CUSTOM_ATTRIBUTE1_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_SOLD_CUSTOM_ATTRIBUTE2_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_SOLD_CUSTOM_ATTRIBUTE3_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_SOLD_CUSTOM_ATTRIBUTE4_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_SOLD_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_SOLD_TITLE_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_SOLD_TYPE_L1_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_SOLD_TYPE_L2_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_SOLD_TYPE_L3_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_SOLD_TYPE_L4_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_SOLD_TYPE_L5_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_STORE_ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_TITLE_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_TYPE_L1_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_TYPE_L2_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_TYPE_L3_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_TYPE_L4_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_TYPE_L5_FIELD_NUMBER: _ClassVar[int]
    QUARTER_FIELD_NUMBER: _ClassVar[int]
    RAW_EVENT_CONVERSION_DIMENSIONS_FIELD_NUMBER: _ClassVar[int]
    WEEK_FIELD_NUMBER: _ClassVar[int]
    YEAR_FIELD_NUMBER: _ClassVar[int]
    ASSET_INTERACTION_TARGET_FIELD_NUMBER: _ClassVar[int]
    ad_network_type: _ad_network_type_pb2.AdNetworkTypeEnum.AdNetworkType
    conversion_action: str
    conversion_action_category: _conversion_action_category_pb2.ConversionActionCategoryEnum.ConversionActionCategory
    conversion_action_name: str
    conversion_custom_dimensions: _containers.RepeatedCompositeFieldContainer[_value_pb2.Value]
    date: str
    day_of_week: _day_of_week_pb2.DayOfWeekEnum.DayOfWeek
    device: _device_pb2.DeviceEnum.Device
    geo_target_city: str
    geo_target_country: str
    geo_target_metro: str
    geo_target_region: str
    hour: int
    keyword: Keyword
    month: str
    product_bidding_category_level1: str
    product_bidding_category_level2: str
    product_bidding_category_level3: str
    product_bidding_category_level4: str
    product_bidding_category_level5: str
    product_brand: str
    product_channel: _product_channel_pb2.ProductChannelEnum.ProductChannel
    product_channel_exclusivity: _product_channel_exclusivity_pb2.ProductChannelExclusivityEnum.ProductChannelExclusivity
    product_condition: _product_condition_pb2.ProductConditionEnum.ProductCondition
    product_country: str
    product_custom_attribute0: str
    product_custom_attribute1: str
    product_custom_attribute2: str
    product_custom_attribute3: str
    product_custom_attribute4: str
    product_item_id: str
    product_language: str
    product_sold_bidding_category_level1: str
    product_sold_bidding_category_level2: str
    product_sold_bidding_category_level3: str
    product_sold_bidding_category_level4: str
    product_sold_bidding_category_level5: str
    product_sold_brand: str
    product_sold_condition: _product_condition_pb2.ProductConditionEnum.ProductCondition
    product_sold_custom_attribute0: str
    product_sold_custom_attribute1: str
    product_sold_custom_attribute2: str
    product_sold_custom_attribute3: str
    product_sold_custom_attribute4: str
    product_sold_item_id: str
    product_sold_title: str
    product_sold_type_l1: str
    product_sold_type_l2: str
    product_sold_type_l3: str
    product_sold_type_l4: str
    product_sold_type_l5: str
    product_store_id: str
    product_title: str
    product_type_l1: str
    product_type_l2: str
    product_type_l3: str
    product_type_l4: str
    product_type_l5: str
    quarter: str
    raw_event_conversion_dimensions: _containers.RepeatedCompositeFieldContainer[_value_pb2.Value]
    week: str
    year: int
    asset_interaction_target: AssetInteractionTarget
    def __init__(self, ad_network_type: _Optional[_Union[_ad_network_type_pb2.AdNetworkTypeEnum.AdNetworkType, str]] = ..., conversion_action: _Optional[str] = ..., conversion_action_category: _Optional[_Union[_conversion_action_category_pb2.ConversionActionCategoryEnum.ConversionActionCategory, str]] = ..., conversion_action_name: _Optional[str] = ..., conversion_custom_dimensions: _Optional[_Iterable[_Union[_value_pb2.Value, _Mapping]]] = ..., date: _Optional[str] = ..., day_of_week: _Optional[_Union[_day_of_week_pb2.DayOfWeekEnum.DayOfWeek, str]] = ..., device: _Optional[_Union[_device_pb2.DeviceEnum.Device, str]] = ..., geo_target_city: _Optional[str] = ..., geo_target_country: _Optional[str] = ..., geo_target_metro: _Optional[str] = ..., geo_target_region: _Optional[str] = ..., hour: _Optional[int] = ..., keyword: _Optional[_Union[Keyword, _Mapping]] = ..., month: _Optional[str] = ..., product_bidding_category_level1: _Optional[str] = ..., product_bidding_category_level2: _Optional[str] = ..., product_bidding_category_level3: _Optional[str] = ..., product_bidding_category_level4: _Optional[str] = ..., product_bidding_category_level5: _Optional[str] = ..., product_brand: _Optional[str] = ..., product_channel: _Optional[_Union[_product_channel_pb2.ProductChannelEnum.ProductChannel, str]] = ..., product_channel_exclusivity: _Optional[_Union[_product_channel_exclusivity_pb2.ProductChannelExclusivityEnum.ProductChannelExclusivity, str]] = ..., product_condition: _Optional[_Union[_product_condition_pb2.ProductConditionEnum.ProductCondition, str]] = ..., product_country: _Optional[str] = ..., product_custom_attribute0: _Optional[str] = ..., product_custom_attribute1: _Optional[str] = ..., product_custom_attribute2: _Optional[str] = ..., product_custom_attribute3: _Optional[str] = ..., product_custom_attribute4: _Optional[str] = ..., product_item_id: _Optional[str] = ..., product_language: _Optional[str] = ..., product_sold_bidding_category_level1: _Optional[str] = ..., product_sold_bidding_category_level2: _Optional[str] = ..., product_sold_bidding_category_level3: _Optional[str] = ..., product_sold_bidding_category_level4: _Optional[str] = ..., product_sold_bidding_category_level5: _Optional[str] = ..., product_sold_brand: _Optional[str] = ..., product_sold_condition: _Optional[_Union[_product_condition_pb2.ProductConditionEnum.ProductCondition, str]] = ..., product_sold_custom_attribute0: _Optional[str] = ..., product_sold_custom_attribute1: _Optional[str] = ..., product_sold_custom_attribute2: _Optional[str] = ..., product_sold_custom_attribute3: _Optional[str] = ..., product_sold_custom_attribute4: _Optional[str] = ..., product_sold_item_id: _Optional[str] = ..., product_sold_title: _Optional[str] = ..., product_sold_type_l1: _Optional[str] = ..., product_sold_type_l2: _Optional[str] = ..., product_sold_type_l3: _Optional[str] = ..., product_sold_type_l4: _Optional[str] = ..., product_sold_type_l5: _Optional[str] = ..., product_store_id: _Optional[str] = ..., product_title: _Optional[str] = ..., product_type_l1: _Optional[str] = ..., product_type_l2: _Optional[str] = ..., product_type_l3: _Optional[str] = ..., product_type_l4: _Optional[str] = ..., product_type_l5: _Optional[str] = ..., quarter: _Optional[str] = ..., raw_event_conversion_dimensions: _Optional[_Iterable[_Union[_value_pb2.Value, _Mapping]]] = ..., week: _Optional[str] = ..., year: _Optional[int] = ..., asset_interaction_target: _Optional[_Union[AssetInteractionTarget, _Mapping]] = ...) -> None: ...

class Keyword(_message.Message):
    __slots__ = ("ad_group_criterion", "info")
    AD_GROUP_CRITERION_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    ad_group_criterion: str
    info: _criteria_pb2.KeywordInfo
    def __init__(self, ad_group_criterion: _Optional[str] = ..., info: _Optional[_Union[_criteria_pb2.KeywordInfo, _Mapping]] = ...) -> None: ...

class AssetInteractionTarget(_message.Message):
    __slots__ = ("asset", "interaction_on_this_asset")
    ASSET_FIELD_NUMBER: _ClassVar[int]
    INTERACTION_ON_THIS_ASSET_FIELD_NUMBER: _ClassVar[int]
    asset: str
    interaction_on_this_asset: bool
    def __init__(self, asset: _Optional[str] = ..., interaction_on_this_asset: bool = ...) -> None: ...
