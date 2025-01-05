from google.ads.googleads.v18.common import criteria_pb2 as _criteria_pb2
from google.ads.googleads.v18.common import extensions_pb2 as _extensions_pb2
from google.ads.googleads.v18.enums import extension_type_pb2 as _extension_type_pb2
from google.ads.googleads.v18.enums import feed_item_status_pb2 as _feed_item_status_pb2
from google.ads.googleads.v18.enums import feed_item_target_device_pb2 as _feed_item_target_device_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ExtensionFeedItem(_message.Message):
    __slots__ = ("resource_name", "id", "extension_type", "start_date_time", "end_date_time", "ad_schedules", "device", "targeted_geo_target_constant", "targeted_keyword", "status", "sitelink_feed_item", "structured_snippet_feed_item", "app_feed_item", "call_feed_item", "callout_feed_item", "text_message_feed_item", "price_feed_item", "promotion_feed_item", "location_feed_item", "affiliate_location_feed_item", "hotel_callout_feed_item", "image_feed_item", "targeted_campaign", "targeted_ad_group")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    EXTENSION_TYPE_FIELD_NUMBER: _ClassVar[int]
    START_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    END_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    AD_SCHEDULES_FIELD_NUMBER: _ClassVar[int]
    DEVICE_FIELD_NUMBER: _ClassVar[int]
    TARGETED_GEO_TARGET_CONSTANT_FIELD_NUMBER: _ClassVar[int]
    TARGETED_KEYWORD_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SITELINK_FEED_ITEM_FIELD_NUMBER: _ClassVar[int]
    STRUCTURED_SNIPPET_FEED_ITEM_FIELD_NUMBER: _ClassVar[int]
    APP_FEED_ITEM_FIELD_NUMBER: _ClassVar[int]
    CALL_FEED_ITEM_FIELD_NUMBER: _ClassVar[int]
    CALLOUT_FEED_ITEM_FIELD_NUMBER: _ClassVar[int]
    TEXT_MESSAGE_FEED_ITEM_FIELD_NUMBER: _ClassVar[int]
    PRICE_FEED_ITEM_FIELD_NUMBER: _ClassVar[int]
    PROMOTION_FEED_ITEM_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FEED_ITEM_FIELD_NUMBER: _ClassVar[int]
    AFFILIATE_LOCATION_FEED_ITEM_FIELD_NUMBER: _ClassVar[int]
    HOTEL_CALLOUT_FEED_ITEM_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FEED_ITEM_FIELD_NUMBER: _ClassVar[int]
    TARGETED_CAMPAIGN_FIELD_NUMBER: _ClassVar[int]
    TARGETED_AD_GROUP_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    id: int
    extension_type: _extension_type_pb2.ExtensionTypeEnum.ExtensionType
    start_date_time: str
    end_date_time: str
    ad_schedules: _containers.RepeatedCompositeFieldContainer[_criteria_pb2.AdScheduleInfo]
    device: _feed_item_target_device_pb2.FeedItemTargetDeviceEnum.FeedItemTargetDevice
    targeted_geo_target_constant: str
    targeted_keyword: _criteria_pb2.KeywordInfo
    status: _feed_item_status_pb2.FeedItemStatusEnum.FeedItemStatus
    sitelink_feed_item: _extensions_pb2.SitelinkFeedItem
    structured_snippet_feed_item: _extensions_pb2.StructuredSnippetFeedItem
    app_feed_item: _extensions_pb2.AppFeedItem
    call_feed_item: _extensions_pb2.CallFeedItem
    callout_feed_item: _extensions_pb2.CalloutFeedItem
    text_message_feed_item: _extensions_pb2.TextMessageFeedItem
    price_feed_item: _extensions_pb2.PriceFeedItem
    promotion_feed_item: _extensions_pb2.PromotionFeedItem
    location_feed_item: _extensions_pb2.LocationFeedItem
    affiliate_location_feed_item: _extensions_pb2.AffiliateLocationFeedItem
    hotel_callout_feed_item: _extensions_pb2.HotelCalloutFeedItem
    image_feed_item: _extensions_pb2.ImageFeedItem
    targeted_campaign: str
    targeted_ad_group: str
    def __init__(self, resource_name: _Optional[str] = ..., id: _Optional[int] = ..., extension_type: _Optional[_Union[_extension_type_pb2.ExtensionTypeEnum.ExtensionType, str]] = ..., start_date_time: _Optional[str] = ..., end_date_time: _Optional[str] = ..., ad_schedules: _Optional[_Iterable[_Union[_criteria_pb2.AdScheduleInfo, _Mapping]]] = ..., device: _Optional[_Union[_feed_item_target_device_pb2.FeedItemTargetDeviceEnum.FeedItemTargetDevice, str]] = ..., targeted_geo_target_constant: _Optional[str] = ..., targeted_keyword: _Optional[_Union[_criteria_pb2.KeywordInfo, _Mapping]] = ..., status: _Optional[_Union[_feed_item_status_pb2.FeedItemStatusEnum.FeedItemStatus, str]] = ..., sitelink_feed_item: _Optional[_Union[_extensions_pb2.SitelinkFeedItem, _Mapping]] = ..., structured_snippet_feed_item: _Optional[_Union[_extensions_pb2.StructuredSnippetFeedItem, _Mapping]] = ..., app_feed_item: _Optional[_Union[_extensions_pb2.AppFeedItem, _Mapping]] = ..., call_feed_item: _Optional[_Union[_extensions_pb2.CallFeedItem, _Mapping]] = ..., callout_feed_item: _Optional[_Union[_extensions_pb2.CalloutFeedItem, _Mapping]] = ..., text_message_feed_item: _Optional[_Union[_extensions_pb2.TextMessageFeedItem, _Mapping]] = ..., price_feed_item: _Optional[_Union[_extensions_pb2.PriceFeedItem, _Mapping]] = ..., promotion_feed_item: _Optional[_Union[_extensions_pb2.PromotionFeedItem, _Mapping]] = ..., location_feed_item: _Optional[_Union[_extensions_pb2.LocationFeedItem, _Mapping]] = ..., affiliate_location_feed_item: _Optional[_Union[_extensions_pb2.AffiliateLocationFeedItem, _Mapping]] = ..., hotel_callout_feed_item: _Optional[_Union[_extensions_pb2.HotelCalloutFeedItem, _Mapping]] = ..., image_feed_item: _Optional[_Union[_extensions_pb2.ImageFeedItem, _Mapping]] = ..., targeted_campaign: _Optional[str] = ..., targeted_ad_group: _Optional[str] = ...) -> None: ...
