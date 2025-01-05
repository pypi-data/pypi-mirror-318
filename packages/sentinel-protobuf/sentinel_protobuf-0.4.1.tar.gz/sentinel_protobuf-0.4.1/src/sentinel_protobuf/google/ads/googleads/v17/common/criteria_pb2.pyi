from google.ads.googleads.v17.enums import age_range_type_pb2 as _age_range_type_pb2
from google.ads.googleads.v17.enums import app_payment_model_type_pb2 as _app_payment_model_type_pb2
from google.ads.googleads.v17.enums import brand_request_rejection_reason_pb2 as _brand_request_rejection_reason_pb2
from google.ads.googleads.v17.enums import brand_state_pb2 as _brand_state_pb2
from google.ads.googleads.v17.enums import content_label_type_pb2 as _content_label_type_pb2
from google.ads.googleads.v17.enums import day_of_week_pb2 as _day_of_week_pb2
from google.ads.googleads.v17.enums import device_pb2 as _device_pb2
from google.ads.googleads.v17.enums import gender_type_pb2 as _gender_type_pb2
from google.ads.googleads.v17.enums import hotel_date_selection_type_pb2 as _hotel_date_selection_type_pb2
from google.ads.googleads.v17.enums import income_range_type_pb2 as _income_range_type_pb2
from google.ads.googleads.v17.enums import interaction_type_pb2 as _interaction_type_pb2
from google.ads.googleads.v17.enums import keyword_match_type_pb2 as _keyword_match_type_pb2
from google.ads.googleads.v17.enums import listing_group_type_pb2 as _listing_group_type_pb2
from google.ads.googleads.v17.enums import location_group_radius_units_pb2 as _location_group_radius_units_pb2
from google.ads.googleads.v17.enums import minute_of_hour_pb2 as _minute_of_hour_pb2
from google.ads.googleads.v17.enums import parental_status_type_pb2 as _parental_status_type_pb2
from google.ads.googleads.v17.enums import product_category_level_pb2 as _product_category_level_pb2
from google.ads.googleads.v17.enums import product_channel_pb2 as _product_channel_pb2
from google.ads.googleads.v17.enums import product_channel_exclusivity_pb2 as _product_channel_exclusivity_pb2
from google.ads.googleads.v17.enums import product_condition_pb2 as _product_condition_pb2
from google.ads.googleads.v17.enums import product_custom_attribute_index_pb2 as _product_custom_attribute_index_pb2
from google.ads.googleads.v17.enums import product_type_level_pb2 as _product_type_level_pb2
from google.ads.googleads.v17.enums import proximity_radius_units_pb2 as _proximity_radius_units_pb2
from google.ads.googleads.v17.enums import webpage_condition_operand_pb2 as _webpage_condition_operand_pb2
from google.ads.googleads.v17.enums import webpage_condition_operator_pb2 as _webpage_condition_operator_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class KeywordInfo(_message.Message):
    __slots__ = ("text", "match_type")
    TEXT_FIELD_NUMBER: _ClassVar[int]
    MATCH_TYPE_FIELD_NUMBER: _ClassVar[int]
    text: str
    match_type: _keyword_match_type_pb2.KeywordMatchTypeEnum.KeywordMatchType
    def __init__(self, text: _Optional[str] = ..., match_type: _Optional[_Union[_keyword_match_type_pb2.KeywordMatchTypeEnum.KeywordMatchType, str]] = ...) -> None: ...

class PlacementInfo(_message.Message):
    __slots__ = ("url",)
    URL_FIELD_NUMBER: _ClassVar[int]
    url: str
    def __init__(self, url: _Optional[str] = ...) -> None: ...

class NegativeKeywordListInfo(_message.Message):
    __slots__ = ("shared_set",)
    SHARED_SET_FIELD_NUMBER: _ClassVar[int]
    shared_set: str
    def __init__(self, shared_set: _Optional[str] = ...) -> None: ...

class MobileAppCategoryInfo(_message.Message):
    __slots__ = ("mobile_app_category_constant",)
    MOBILE_APP_CATEGORY_CONSTANT_FIELD_NUMBER: _ClassVar[int]
    mobile_app_category_constant: str
    def __init__(self, mobile_app_category_constant: _Optional[str] = ...) -> None: ...

class MobileApplicationInfo(_message.Message):
    __slots__ = ("app_id", "name")
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    app_id: str
    name: str
    def __init__(self, app_id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class LocationInfo(_message.Message):
    __slots__ = ("geo_target_constant",)
    GEO_TARGET_CONSTANT_FIELD_NUMBER: _ClassVar[int]
    geo_target_constant: str
    def __init__(self, geo_target_constant: _Optional[str] = ...) -> None: ...

class DeviceInfo(_message.Message):
    __slots__ = ("type",)
    TYPE_FIELD_NUMBER: _ClassVar[int]
    type: _device_pb2.DeviceEnum.Device
    def __init__(self, type: _Optional[_Union[_device_pb2.DeviceEnum.Device, str]] = ...) -> None: ...

class ListingGroupInfo(_message.Message):
    __slots__ = ("type", "case_value", "parent_ad_group_criterion", "path")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CASE_VALUE_FIELD_NUMBER: _ClassVar[int]
    PARENT_AD_GROUP_CRITERION_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    type: _listing_group_type_pb2.ListingGroupTypeEnum.ListingGroupType
    case_value: ListingDimensionInfo
    parent_ad_group_criterion: str
    path: ListingDimensionPath
    def __init__(self, type: _Optional[_Union[_listing_group_type_pb2.ListingGroupTypeEnum.ListingGroupType, str]] = ..., case_value: _Optional[_Union[ListingDimensionInfo, _Mapping]] = ..., parent_ad_group_criterion: _Optional[str] = ..., path: _Optional[_Union[ListingDimensionPath, _Mapping]] = ...) -> None: ...

class ListingDimensionPath(_message.Message):
    __slots__ = ("dimensions",)
    DIMENSIONS_FIELD_NUMBER: _ClassVar[int]
    dimensions: _containers.RepeatedCompositeFieldContainer[ListingDimensionInfo]
    def __init__(self, dimensions: _Optional[_Iterable[_Union[ListingDimensionInfo, _Mapping]]] = ...) -> None: ...

class ListingScopeInfo(_message.Message):
    __slots__ = ("dimensions",)
    DIMENSIONS_FIELD_NUMBER: _ClassVar[int]
    dimensions: _containers.RepeatedCompositeFieldContainer[ListingDimensionInfo]
    def __init__(self, dimensions: _Optional[_Iterable[_Union[ListingDimensionInfo, _Mapping]]] = ...) -> None: ...

class ListingDimensionInfo(_message.Message):
    __slots__ = ("hotel_id", "hotel_class", "hotel_country_region", "hotel_state", "hotel_city", "product_category", "product_brand", "product_channel", "product_channel_exclusivity", "product_condition", "product_custom_attribute", "product_item_id", "product_type", "product_grouping", "product_labels", "product_legacy_condition", "product_type_full", "activity_id", "activity_rating", "activity_country", "activity_state", "activity_city", "unknown_listing_dimension")
    HOTEL_ID_FIELD_NUMBER: _ClassVar[int]
    HOTEL_CLASS_FIELD_NUMBER: _ClassVar[int]
    HOTEL_COUNTRY_REGION_FIELD_NUMBER: _ClassVar[int]
    HOTEL_STATE_FIELD_NUMBER: _ClassVar[int]
    HOTEL_CITY_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_CATEGORY_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_BRAND_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_CHANNEL_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_CHANNEL_EXCLUSIVITY_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_CONDITION_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_CUSTOM_ATTRIBUTE_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_TYPE_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_GROUPING_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_LABELS_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_LEGACY_CONDITION_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_TYPE_FULL_FIELD_NUMBER: _ClassVar[int]
    ACTIVITY_ID_FIELD_NUMBER: _ClassVar[int]
    ACTIVITY_RATING_FIELD_NUMBER: _ClassVar[int]
    ACTIVITY_COUNTRY_FIELD_NUMBER: _ClassVar[int]
    ACTIVITY_STATE_FIELD_NUMBER: _ClassVar[int]
    ACTIVITY_CITY_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_LISTING_DIMENSION_FIELD_NUMBER: _ClassVar[int]
    hotel_id: HotelIdInfo
    hotel_class: HotelClassInfo
    hotel_country_region: HotelCountryRegionInfo
    hotel_state: HotelStateInfo
    hotel_city: HotelCityInfo
    product_category: ProductCategoryInfo
    product_brand: ProductBrandInfo
    product_channel: ProductChannelInfo
    product_channel_exclusivity: ProductChannelExclusivityInfo
    product_condition: ProductConditionInfo
    product_custom_attribute: ProductCustomAttributeInfo
    product_item_id: ProductItemIdInfo
    product_type: ProductTypeInfo
    product_grouping: ProductGroupingInfo
    product_labels: ProductLabelsInfo
    product_legacy_condition: ProductLegacyConditionInfo
    product_type_full: ProductTypeFullInfo
    activity_id: ActivityIdInfo
    activity_rating: ActivityRatingInfo
    activity_country: ActivityCountryInfo
    activity_state: ActivityStateInfo
    activity_city: ActivityCityInfo
    unknown_listing_dimension: UnknownListingDimensionInfo
    def __init__(self, hotel_id: _Optional[_Union[HotelIdInfo, _Mapping]] = ..., hotel_class: _Optional[_Union[HotelClassInfo, _Mapping]] = ..., hotel_country_region: _Optional[_Union[HotelCountryRegionInfo, _Mapping]] = ..., hotel_state: _Optional[_Union[HotelStateInfo, _Mapping]] = ..., hotel_city: _Optional[_Union[HotelCityInfo, _Mapping]] = ..., product_category: _Optional[_Union[ProductCategoryInfo, _Mapping]] = ..., product_brand: _Optional[_Union[ProductBrandInfo, _Mapping]] = ..., product_channel: _Optional[_Union[ProductChannelInfo, _Mapping]] = ..., product_channel_exclusivity: _Optional[_Union[ProductChannelExclusivityInfo, _Mapping]] = ..., product_condition: _Optional[_Union[ProductConditionInfo, _Mapping]] = ..., product_custom_attribute: _Optional[_Union[ProductCustomAttributeInfo, _Mapping]] = ..., product_item_id: _Optional[_Union[ProductItemIdInfo, _Mapping]] = ..., product_type: _Optional[_Union[ProductTypeInfo, _Mapping]] = ..., product_grouping: _Optional[_Union[ProductGroupingInfo, _Mapping]] = ..., product_labels: _Optional[_Union[ProductLabelsInfo, _Mapping]] = ..., product_legacy_condition: _Optional[_Union[ProductLegacyConditionInfo, _Mapping]] = ..., product_type_full: _Optional[_Union[ProductTypeFullInfo, _Mapping]] = ..., activity_id: _Optional[_Union[ActivityIdInfo, _Mapping]] = ..., activity_rating: _Optional[_Union[ActivityRatingInfo, _Mapping]] = ..., activity_country: _Optional[_Union[ActivityCountryInfo, _Mapping]] = ..., activity_state: _Optional[_Union[ActivityStateInfo, _Mapping]] = ..., activity_city: _Optional[_Union[ActivityCityInfo, _Mapping]] = ..., unknown_listing_dimension: _Optional[_Union[UnknownListingDimensionInfo, _Mapping]] = ...) -> None: ...

class HotelIdInfo(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: str
    def __init__(self, value: _Optional[str] = ...) -> None: ...

class HotelClassInfo(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: int
    def __init__(self, value: _Optional[int] = ...) -> None: ...

class HotelCountryRegionInfo(_message.Message):
    __slots__ = ("country_region_criterion",)
    COUNTRY_REGION_CRITERION_FIELD_NUMBER: _ClassVar[int]
    country_region_criterion: str
    def __init__(self, country_region_criterion: _Optional[str] = ...) -> None: ...

class HotelStateInfo(_message.Message):
    __slots__ = ("state_criterion",)
    STATE_CRITERION_FIELD_NUMBER: _ClassVar[int]
    state_criterion: str
    def __init__(self, state_criterion: _Optional[str] = ...) -> None: ...

class HotelCityInfo(_message.Message):
    __slots__ = ("city_criterion",)
    CITY_CRITERION_FIELD_NUMBER: _ClassVar[int]
    city_criterion: str
    def __init__(self, city_criterion: _Optional[str] = ...) -> None: ...

class ProductCategoryInfo(_message.Message):
    __slots__ = ("category_id", "level")
    CATEGORY_ID_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    category_id: int
    level: _product_category_level_pb2.ProductCategoryLevelEnum.ProductCategoryLevel
    def __init__(self, category_id: _Optional[int] = ..., level: _Optional[_Union[_product_category_level_pb2.ProductCategoryLevelEnum.ProductCategoryLevel, str]] = ...) -> None: ...

class ProductBrandInfo(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: str
    def __init__(self, value: _Optional[str] = ...) -> None: ...

class ProductChannelInfo(_message.Message):
    __slots__ = ("channel",)
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    channel: _product_channel_pb2.ProductChannelEnum.ProductChannel
    def __init__(self, channel: _Optional[_Union[_product_channel_pb2.ProductChannelEnum.ProductChannel, str]] = ...) -> None: ...

class ProductChannelExclusivityInfo(_message.Message):
    __slots__ = ("channel_exclusivity",)
    CHANNEL_EXCLUSIVITY_FIELD_NUMBER: _ClassVar[int]
    channel_exclusivity: _product_channel_exclusivity_pb2.ProductChannelExclusivityEnum.ProductChannelExclusivity
    def __init__(self, channel_exclusivity: _Optional[_Union[_product_channel_exclusivity_pb2.ProductChannelExclusivityEnum.ProductChannelExclusivity, str]] = ...) -> None: ...

class ProductConditionInfo(_message.Message):
    __slots__ = ("condition",)
    CONDITION_FIELD_NUMBER: _ClassVar[int]
    condition: _product_condition_pb2.ProductConditionEnum.ProductCondition
    def __init__(self, condition: _Optional[_Union[_product_condition_pb2.ProductConditionEnum.ProductCondition, str]] = ...) -> None: ...

class ProductCustomAttributeInfo(_message.Message):
    __slots__ = ("value", "index")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    value: str
    index: _product_custom_attribute_index_pb2.ProductCustomAttributeIndexEnum.ProductCustomAttributeIndex
    def __init__(self, value: _Optional[str] = ..., index: _Optional[_Union[_product_custom_attribute_index_pb2.ProductCustomAttributeIndexEnum.ProductCustomAttributeIndex, str]] = ...) -> None: ...

class ProductItemIdInfo(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: str
    def __init__(self, value: _Optional[str] = ...) -> None: ...

class ProductTypeInfo(_message.Message):
    __slots__ = ("value", "level")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    value: str
    level: _product_type_level_pb2.ProductTypeLevelEnum.ProductTypeLevel
    def __init__(self, value: _Optional[str] = ..., level: _Optional[_Union[_product_type_level_pb2.ProductTypeLevelEnum.ProductTypeLevel, str]] = ...) -> None: ...

class ProductGroupingInfo(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: str
    def __init__(self, value: _Optional[str] = ...) -> None: ...

class ProductLabelsInfo(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: str
    def __init__(self, value: _Optional[str] = ...) -> None: ...

class ProductLegacyConditionInfo(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: str
    def __init__(self, value: _Optional[str] = ...) -> None: ...

class ProductTypeFullInfo(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: str
    def __init__(self, value: _Optional[str] = ...) -> None: ...

class UnknownListingDimensionInfo(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class HotelDateSelectionTypeInfo(_message.Message):
    __slots__ = ("type",)
    TYPE_FIELD_NUMBER: _ClassVar[int]
    type: _hotel_date_selection_type_pb2.HotelDateSelectionTypeEnum.HotelDateSelectionType
    def __init__(self, type: _Optional[_Union[_hotel_date_selection_type_pb2.HotelDateSelectionTypeEnum.HotelDateSelectionType, str]] = ...) -> None: ...

class HotelAdvanceBookingWindowInfo(_message.Message):
    __slots__ = ("min_days", "max_days")
    MIN_DAYS_FIELD_NUMBER: _ClassVar[int]
    MAX_DAYS_FIELD_NUMBER: _ClassVar[int]
    min_days: int
    max_days: int
    def __init__(self, min_days: _Optional[int] = ..., max_days: _Optional[int] = ...) -> None: ...

class HotelLengthOfStayInfo(_message.Message):
    __slots__ = ("min_nights", "max_nights")
    MIN_NIGHTS_FIELD_NUMBER: _ClassVar[int]
    MAX_NIGHTS_FIELD_NUMBER: _ClassVar[int]
    min_nights: int
    max_nights: int
    def __init__(self, min_nights: _Optional[int] = ..., max_nights: _Optional[int] = ...) -> None: ...

class HotelCheckInDateRangeInfo(_message.Message):
    __slots__ = ("start_date", "end_date")
    START_DATE_FIELD_NUMBER: _ClassVar[int]
    END_DATE_FIELD_NUMBER: _ClassVar[int]
    start_date: str
    end_date: str
    def __init__(self, start_date: _Optional[str] = ..., end_date: _Optional[str] = ...) -> None: ...

class HotelCheckInDayInfo(_message.Message):
    __slots__ = ("day_of_week",)
    DAY_OF_WEEK_FIELD_NUMBER: _ClassVar[int]
    day_of_week: _day_of_week_pb2.DayOfWeekEnum.DayOfWeek
    def __init__(self, day_of_week: _Optional[_Union[_day_of_week_pb2.DayOfWeekEnum.DayOfWeek, str]] = ...) -> None: ...

class ActivityIdInfo(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: str
    def __init__(self, value: _Optional[str] = ...) -> None: ...

class ActivityRatingInfo(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: int
    def __init__(self, value: _Optional[int] = ...) -> None: ...

class ActivityCountryInfo(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: str
    def __init__(self, value: _Optional[str] = ...) -> None: ...

class ActivityStateInfo(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: str
    def __init__(self, value: _Optional[str] = ...) -> None: ...

class ActivityCityInfo(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: str
    def __init__(self, value: _Optional[str] = ...) -> None: ...

class InteractionTypeInfo(_message.Message):
    __slots__ = ("type",)
    TYPE_FIELD_NUMBER: _ClassVar[int]
    type: _interaction_type_pb2.InteractionTypeEnum.InteractionType
    def __init__(self, type: _Optional[_Union[_interaction_type_pb2.InteractionTypeEnum.InteractionType, str]] = ...) -> None: ...

class AdScheduleInfo(_message.Message):
    __slots__ = ("start_minute", "end_minute", "start_hour", "end_hour", "day_of_week")
    START_MINUTE_FIELD_NUMBER: _ClassVar[int]
    END_MINUTE_FIELD_NUMBER: _ClassVar[int]
    START_HOUR_FIELD_NUMBER: _ClassVar[int]
    END_HOUR_FIELD_NUMBER: _ClassVar[int]
    DAY_OF_WEEK_FIELD_NUMBER: _ClassVar[int]
    start_minute: _minute_of_hour_pb2.MinuteOfHourEnum.MinuteOfHour
    end_minute: _minute_of_hour_pb2.MinuteOfHourEnum.MinuteOfHour
    start_hour: int
    end_hour: int
    day_of_week: _day_of_week_pb2.DayOfWeekEnum.DayOfWeek
    def __init__(self, start_minute: _Optional[_Union[_minute_of_hour_pb2.MinuteOfHourEnum.MinuteOfHour, str]] = ..., end_minute: _Optional[_Union[_minute_of_hour_pb2.MinuteOfHourEnum.MinuteOfHour, str]] = ..., start_hour: _Optional[int] = ..., end_hour: _Optional[int] = ..., day_of_week: _Optional[_Union[_day_of_week_pb2.DayOfWeekEnum.DayOfWeek, str]] = ...) -> None: ...

class AgeRangeInfo(_message.Message):
    __slots__ = ("type",)
    TYPE_FIELD_NUMBER: _ClassVar[int]
    type: _age_range_type_pb2.AgeRangeTypeEnum.AgeRangeType
    def __init__(self, type: _Optional[_Union[_age_range_type_pb2.AgeRangeTypeEnum.AgeRangeType, str]] = ...) -> None: ...

class GenderInfo(_message.Message):
    __slots__ = ("type",)
    TYPE_FIELD_NUMBER: _ClassVar[int]
    type: _gender_type_pb2.GenderTypeEnum.GenderType
    def __init__(self, type: _Optional[_Union[_gender_type_pb2.GenderTypeEnum.GenderType, str]] = ...) -> None: ...

class IncomeRangeInfo(_message.Message):
    __slots__ = ("type",)
    TYPE_FIELD_NUMBER: _ClassVar[int]
    type: _income_range_type_pb2.IncomeRangeTypeEnum.IncomeRangeType
    def __init__(self, type: _Optional[_Union[_income_range_type_pb2.IncomeRangeTypeEnum.IncomeRangeType, str]] = ...) -> None: ...

class ParentalStatusInfo(_message.Message):
    __slots__ = ("type",)
    TYPE_FIELD_NUMBER: _ClassVar[int]
    type: _parental_status_type_pb2.ParentalStatusTypeEnum.ParentalStatusType
    def __init__(self, type: _Optional[_Union[_parental_status_type_pb2.ParentalStatusTypeEnum.ParentalStatusType, str]] = ...) -> None: ...

class YouTubeVideoInfo(_message.Message):
    __slots__ = ("video_id",)
    VIDEO_ID_FIELD_NUMBER: _ClassVar[int]
    video_id: str
    def __init__(self, video_id: _Optional[str] = ...) -> None: ...

class YouTubeChannelInfo(_message.Message):
    __slots__ = ("channel_id",)
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    def __init__(self, channel_id: _Optional[str] = ...) -> None: ...

class UserListInfo(_message.Message):
    __slots__ = ("user_list",)
    USER_LIST_FIELD_NUMBER: _ClassVar[int]
    user_list: str
    def __init__(self, user_list: _Optional[str] = ...) -> None: ...

class ProximityInfo(_message.Message):
    __slots__ = ("geo_point", "radius", "radius_units", "address")
    GEO_POINT_FIELD_NUMBER: _ClassVar[int]
    RADIUS_FIELD_NUMBER: _ClassVar[int]
    RADIUS_UNITS_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    geo_point: GeoPointInfo
    radius: float
    radius_units: _proximity_radius_units_pb2.ProximityRadiusUnitsEnum.ProximityRadiusUnits
    address: AddressInfo
    def __init__(self, geo_point: _Optional[_Union[GeoPointInfo, _Mapping]] = ..., radius: _Optional[float] = ..., radius_units: _Optional[_Union[_proximity_radius_units_pb2.ProximityRadiusUnitsEnum.ProximityRadiusUnits, str]] = ..., address: _Optional[_Union[AddressInfo, _Mapping]] = ...) -> None: ...

class GeoPointInfo(_message.Message):
    __slots__ = ("longitude_in_micro_degrees", "latitude_in_micro_degrees")
    LONGITUDE_IN_MICRO_DEGREES_FIELD_NUMBER: _ClassVar[int]
    LATITUDE_IN_MICRO_DEGREES_FIELD_NUMBER: _ClassVar[int]
    longitude_in_micro_degrees: int
    latitude_in_micro_degrees: int
    def __init__(self, longitude_in_micro_degrees: _Optional[int] = ..., latitude_in_micro_degrees: _Optional[int] = ...) -> None: ...

class AddressInfo(_message.Message):
    __slots__ = ("postal_code", "province_code", "country_code", "province_name", "street_address", "street_address2", "city_name")
    POSTAL_CODE_FIELD_NUMBER: _ClassVar[int]
    PROVINCE_CODE_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    PROVINCE_NAME_FIELD_NUMBER: _ClassVar[int]
    STREET_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    STREET_ADDRESS2_FIELD_NUMBER: _ClassVar[int]
    CITY_NAME_FIELD_NUMBER: _ClassVar[int]
    postal_code: str
    province_code: str
    country_code: str
    province_name: str
    street_address: str
    street_address2: str
    city_name: str
    def __init__(self, postal_code: _Optional[str] = ..., province_code: _Optional[str] = ..., country_code: _Optional[str] = ..., province_name: _Optional[str] = ..., street_address: _Optional[str] = ..., street_address2: _Optional[str] = ..., city_name: _Optional[str] = ...) -> None: ...

class TopicInfo(_message.Message):
    __slots__ = ("topic_constant", "path")
    TOPIC_CONSTANT_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    topic_constant: str
    path: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, topic_constant: _Optional[str] = ..., path: _Optional[_Iterable[str]] = ...) -> None: ...

class LanguageInfo(_message.Message):
    __slots__ = ("language_constant",)
    LANGUAGE_CONSTANT_FIELD_NUMBER: _ClassVar[int]
    language_constant: str
    def __init__(self, language_constant: _Optional[str] = ...) -> None: ...

class IpBlockInfo(_message.Message):
    __slots__ = ("ip_address",)
    IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    ip_address: str
    def __init__(self, ip_address: _Optional[str] = ...) -> None: ...

class ContentLabelInfo(_message.Message):
    __slots__ = ("type",)
    TYPE_FIELD_NUMBER: _ClassVar[int]
    type: _content_label_type_pb2.ContentLabelTypeEnum.ContentLabelType
    def __init__(self, type: _Optional[_Union[_content_label_type_pb2.ContentLabelTypeEnum.ContentLabelType, str]] = ...) -> None: ...

class CarrierInfo(_message.Message):
    __slots__ = ("carrier_constant",)
    CARRIER_CONSTANT_FIELD_NUMBER: _ClassVar[int]
    carrier_constant: str
    def __init__(self, carrier_constant: _Optional[str] = ...) -> None: ...

class UserInterestInfo(_message.Message):
    __slots__ = ("user_interest_category",)
    USER_INTEREST_CATEGORY_FIELD_NUMBER: _ClassVar[int]
    user_interest_category: str
    def __init__(self, user_interest_category: _Optional[str] = ...) -> None: ...

class WebpageInfo(_message.Message):
    __slots__ = ("criterion_name", "conditions", "coverage_percentage", "sample")
    CRITERION_NAME_FIELD_NUMBER: _ClassVar[int]
    CONDITIONS_FIELD_NUMBER: _ClassVar[int]
    COVERAGE_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_FIELD_NUMBER: _ClassVar[int]
    criterion_name: str
    conditions: _containers.RepeatedCompositeFieldContainer[WebpageConditionInfo]
    coverage_percentage: float
    sample: WebpageSampleInfo
    def __init__(self, criterion_name: _Optional[str] = ..., conditions: _Optional[_Iterable[_Union[WebpageConditionInfo, _Mapping]]] = ..., coverage_percentage: _Optional[float] = ..., sample: _Optional[_Union[WebpageSampleInfo, _Mapping]] = ...) -> None: ...

class WebpageConditionInfo(_message.Message):
    __slots__ = ("operand", "operator", "argument")
    OPERAND_FIELD_NUMBER: _ClassVar[int]
    OPERATOR_FIELD_NUMBER: _ClassVar[int]
    ARGUMENT_FIELD_NUMBER: _ClassVar[int]
    operand: _webpage_condition_operand_pb2.WebpageConditionOperandEnum.WebpageConditionOperand
    operator: _webpage_condition_operator_pb2.WebpageConditionOperatorEnum.WebpageConditionOperator
    argument: str
    def __init__(self, operand: _Optional[_Union[_webpage_condition_operand_pb2.WebpageConditionOperandEnum.WebpageConditionOperand, str]] = ..., operator: _Optional[_Union[_webpage_condition_operator_pb2.WebpageConditionOperatorEnum.WebpageConditionOperator, str]] = ..., argument: _Optional[str] = ...) -> None: ...

class WebpageSampleInfo(_message.Message):
    __slots__ = ("sample_urls",)
    SAMPLE_URLS_FIELD_NUMBER: _ClassVar[int]
    sample_urls: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, sample_urls: _Optional[_Iterable[str]] = ...) -> None: ...

class OperatingSystemVersionInfo(_message.Message):
    __slots__ = ("operating_system_version_constant",)
    OPERATING_SYSTEM_VERSION_CONSTANT_FIELD_NUMBER: _ClassVar[int]
    operating_system_version_constant: str
    def __init__(self, operating_system_version_constant: _Optional[str] = ...) -> None: ...

class AppPaymentModelInfo(_message.Message):
    __slots__ = ("type",)
    TYPE_FIELD_NUMBER: _ClassVar[int]
    type: _app_payment_model_type_pb2.AppPaymentModelTypeEnum.AppPaymentModelType
    def __init__(self, type: _Optional[_Union[_app_payment_model_type_pb2.AppPaymentModelTypeEnum.AppPaymentModelType, str]] = ...) -> None: ...

class MobileDeviceInfo(_message.Message):
    __slots__ = ("mobile_device_constant",)
    MOBILE_DEVICE_CONSTANT_FIELD_NUMBER: _ClassVar[int]
    mobile_device_constant: str
    def __init__(self, mobile_device_constant: _Optional[str] = ...) -> None: ...

class CustomAffinityInfo(_message.Message):
    __slots__ = ("custom_affinity",)
    CUSTOM_AFFINITY_FIELD_NUMBER: _ClassVar[int]
    custom_affinity: str
    def __init__(self, custom_affinity: _Optional[str] = ...) -> None: ...

class CustomIntentInfo(_message.Message):
    __slots__ = ("custom_intent",)
    CUSTOM_INTENT_FIELD_NUMBER: _ClassVar[int]
    custom_intent: str
    def __init__(self, custom_intent: _Optional[str] = ...) -> None: ...

class LocationGroupInfo(_message.Message):
    __slots__ = ("feed", "geo_target_constants", "radius", "radius_units", "feed_item_sets", "enable_customer_level_location_asset_set", "location_group_asset_sets")
    FEED_FIELD_NUMBER: _ClassVar[int]
    GEO_TARGET_CONSTANTS_FIELD_NUMBER: _ClassVar[int]
    RADIUS_FIELD_NUMBER: _ClassVar[int]
    RADIUS_UNITS_FIELD_NUMBER: _ClassVar[int]
    FEED_ITEM_SETS_FIELD_NUMBER: _ClassVar[int]
    ENABLE_CUSTOMER_LEVEL_LOCATION_ASSET_SET_FIELD_NUMBER: _ClassVar[int]
    LOCATION_GROUP_ASSET_SETS_FIELD_NUMBER: _ClassVar[int]
    feed: str
    geo_target_constants: _containers.RepeatedScalarFieldContainer[str]
    radius: int
    radius_units: _location_group_radius_units_pb2.LocationGroupRadiusUnitsEnum.LocationGroupRadiusUnits
    feed_item_sets: _containers.RepeatedScalarFieldContainer[str]
    enable_customer_level_location_asset_set: bool
    location_group_asset_sets: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, feed: _Optional[str] = ..., geo_target_constants: _Optional[_Iterable[str]] = ..., radius: _Optional[int] = ..., radius_units: _Optional[_Union[_location_group_radius_units_pb2.LocationGroupRadiusUnitsEnum.LocationGroupRadiusUnits, str]] = ..., feed_item_sets: _Optional[_Iterable[str]] = ..., enable_customer_level_location_asset_set: bool = ..., location_group_asset_sets: _Optional[_Iterable[str]] = ...) -> None: ...

class CustomAudienceInfo(_message.Message):
    __slots__ = ("custom_audience",)
    CUSTOM_AUDIENCE_FIELD_NUMBER: _ClassVar[int]
    custom_audience: str
    def __init__(self, custom_audience: _Optional[str] = ...) -> None: ...

class CombinedAudienceInfo(_message.Message):
    __slots__ = ("combined_audience",)
    COMBINED_AUDIENCE_FIELD_NUMBER: _ClassVar[int]
    combined_audience: str
    def __init__(self, combined_audience: _Optional[str] = ...) -> None: ...

class AudienceInfo(_message.Message):
    __slots__ = ("audience",)
    AUDIENCE_FIELD_NUMBER: _ClassVar[int]
    audience: str
    def __init__(self, audience: _Optional[str] = ...) -> None: ...

class KeywordThemeInfo(_message.Message):
    __slots__ = ("keyword_theme_constant", "free_form_keyword_theme")
    KEYWORD_THEME_CONSTANT_FIELD_NUMBER: _ClassVar[int]
    FREE_FORM_KEYWORD_THEME_FIELD_NUMBER: _ClassVar[int]
    keyword_theme_constant: str
    free_form_keyword_theme: str
    def __init__(self, keyword_theme_constant: _Optional[str] = ..., free_form_keyword_theme: _Optional[str] = ...) -> None: ...

class LocalServiceIdInfo(_message.Message):
    __slots__ = ("service_id",)
    SERVICE_ID_FIELD_NUMBER: _ClassVar[int]
    service_id: str
    def __init__(self, service_id: _Optional[str] = ...) -> None: ...

class SearchThemeInfo(_message.Message):
    __slots__ = ("text",)
    TEXT_FIELD_NUMBER: _ClassVar[int]
    text: str
    def __init__(self, text: _Optional[str] = ...) -> None: ...

class BrandInfo(_message.Message):
    __slots__ = ("display_name", "entity_id", "primary_url", "rejection_reason", "status")
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_URL_FIELD_NUMBER: _ClassVar[int]
    REJECTION_REASON_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    display_name: str
    entity_id: str
    primary_url: str
    rejection_reason: _brand_request_rejection_reason_pb2.BrandRequestRejectionReasonEnum.BrandRequestRejectionReason
    status: _brand_state_pb2.BrandStateEnum.BrandState
    def __init__(self, display_name: _Optional[str] = ..., entity_id: _Optional[str] = ..., primary_url: _Optional[str] = ..., rejection_reason: _Optional[_Union[_brand_request_rejection_reason_pb2.BrandRequestRejectionReasonEnum.BrandRequestRejectionReason, str]] = ..., status: _Optional[_Union[_brand_state_pb2.BrandStateEnum.BrandState, str]] = ...) -> None: ...

class BrandListInfo(_message.Message):
    __slots__ = ("shared_set",)
    SHARED_SET_FIELD_NUMBER: _ClassVar[int]
    shared_set: str
    def __init__(self, shared_set: _Optional[str] = ...) -> None: ...
