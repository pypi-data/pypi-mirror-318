from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class AdGroupTypeEnum(_message.Message):
    __slots__ = ()

    class AdGroupType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[AdGroupTypeEnum.AdGroupType]
        UNKNOWN: _ClassVar[AdGroupTypeEnum.AdGroupType]
        SEARCH_STANDARD: _ClassVar[AdGroupTypeEnum.AdGroupType]
        DISPLAY_STANDARD: _ClassVar[AdGroupTypeEnum.AdGroupType]
        SHOPPING_PRODUCT_ADS: _ClassVar[AdGroupTypeEnum.AdGroupType]
        SHOPPING_SHOWCASE_ADS: _ClassVar[AdGroupTypeEnum.AdGroupType]
        HOTEL_ADS: _ClassVar[AdGroupTypeEnum.AdGroupType]
        SHOPPING_SMART_ADS: _ClassVar[AdGroupTypeEnum.AdGroupType]
        VIDEO_BUMPER: _ClassVar[AdGroupTypeEnum.AdGroupType]
        VIDEO_TRUE_VIEW_IN_STREAM: _ClassVar[AdGroupTypeEnum.AdGroupType]
        VIDEO_TRUE_VIEW_IN_DISPLAY: _ClassVar[AdGroupTypeEnum.AdGroupType]
        VIDEO_NON_SKIPPABLE_IN_STREAM: _ClassVar[AdGroupTypeEnum.AdGroupType]
        VIDEO_OUTSTREAM: _ClassVar[AdGroupTypeEnum.AdGroupType]
        SEARCH_DYNAMIC_ADS: _ClassVar[AdGroupTypeEnum.AdGroupType]
        SHOPPING_COMPARISON_LISTING_ADS: _ClassVar[AdGroupTypeEnum.AdGroupType]
        PROMOTED_HOTEL_ADS: _ClassVar[AdGroupTypeEnum.AdGroupType]
        VIDEO_RESPONSIVE: _ClassVar[AdGroupTypeEnum.AdGroupType]
        VIDEO_EFFICIENT_REACH: _ClassVar[AdGroupTypeEnum.AdGroupType]
        SMART_CAMPAIGN_ADS: _ClassVar[AdGroupTypeEnum.AdGroupType]
        TRAVEL_ADS: _ClassVar[AdGroupTypeEnum.AdGroupType]
    UNSPECIFIED: AdGroupTypeEnum.AdGroupType
    UNKNOWN: AdGroupTypeEnum.AdGroupType
    SEARCH_STANDARD: AdGroupTypeEnum.AdGroupType
    DISPLAY_STANDARD: AdGroupTypeEnum.AdGroupType
    SHOPPING_PRODUCT_ADS: AdGroupTypeEnum.AdGroupType
    SHOPPING_SHOWCASE_ADS: AdGroupTypeEnum.AdGroupType
    HOTEL_ADS: AdGroupTypeEnum.AdGroupType
    SHOPPING_SMART_ADS: AdGroupTypeEnum.AdGroupType
    VIDEO_BUMPER: AdGroupTypeEnum.AdGroupType
    VIDEO_TRUE_VIEW_IN_STREAM: AdGroupTypeEnum.AdGroupType
    VIDEO_TRUE_VIEW_IN_DISPLAY: AdGroupTypeEnum.AdGroupType
    VIDEO_NON_SKIPPABLE_IN_STREAM: AdGroupTypeEnum.AdGroupType
    VIDEO_OUTSTREAM: AdGroupTypeEnum.AdGroupType
    SEARCH_DYNAMIC_ADS: AdGroupTypeEnum.AdGroupType
    SHOPPING_COMPARISON_LISTING_ADS: AdGroupTypeEnum.AdGroupType
    PROMOTED_HOTEL_ADS: AdGroupTypeEnum.AdGroupType
    VIDEO_RESPONSIVE: AdGroupTypeEnum.AdGroupType
    VIDEO_EFFICIENT_REACH: AdGroupTypeEnum.AdGroupType
    SMART_CAMPAIGN_ADS: AdGroupTypeEnum.AdGroupType
    TRAVEL_ADS: AdGroupTypeEnum.AdGroupType

    def __init__(self) -> None:
        ...