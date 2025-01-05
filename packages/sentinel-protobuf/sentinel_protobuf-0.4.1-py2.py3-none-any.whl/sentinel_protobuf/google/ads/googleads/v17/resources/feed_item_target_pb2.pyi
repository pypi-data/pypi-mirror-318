from google.ads.googleads.v17.common import criteria_pb2 as _criteria_pb2
from google.ads.googleads.v17.enums import feed_item_target_device_pb2 as _feed_item_target_device_pb2
from google.ads.googleads.v17.enums import feed_item_target_status_pb2 as _feed_item_target_status_pb2
from google.ads.googleads.v17.enums import feed_item_target_type_pb2 as _feed_item_target_type_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FeedItemTarget(_message.Message):
    __slots__ = ("resource_name", "feed_item", "feed_item_target_type", "feed_item_target_id", "status", "campaign", "ad_group", "keyword", "geo_target_constant", "device", "ad_schedule")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    FEED_ITEM_FIELD_NUMBER: _ClassVar[int]
    FEED_ITEM_TARGET_TYPE_FIELD_NUMBER: _ClassVar[int]
    FEED_ITEM_TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_FIELD_NUMBER: _ClassVar[int]
    AD_GROUP_FIELD_NUMBER: _ClassVar[int]
    KEYWORD_FIELD_NUMBER: _ClassVar[int]
    GEO_TARGET_CONSTANT_FIELD_NUMBER: _ClassVar[int]
    DEVICE_FIELD_NUMBER: _ClassVar[int]
    AD_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    feed_item: str
    feed_item_target_type: _feed_item_target_type_pb2.FeedItemTargetTypeEnum.FeedItemTargetType
    feed_item_target_id: int
    status: _feed_item_target_status_pb2.FeedItemTargetStatusEnum.FeedItemTargetStatus
    campaign: str
    ad_group: str
    keyword: _criteria_pb2.KeywordInfo
    geo_target_constant: str
    device: _feed_item_target_device_pb2.FeedItemTargetDeviceEnum.FeedItemTargetDevice
    ad_schedule: _criteria_pb2.AdScheduleInfo
    def __init__(self, resource_name: _Optional[str] = ..., feed_item: _Optional[str] = ..., feed_item_target_type: _Optional[_Union[_feed_item_target_type_pb2.FeedItemTargetTypeEnum.FeedItemTargetType, str]] = ..., feed_item_target_id: _Optional[int] = ..., status: _Optional[_Union[_feed_item_target_status_pb2.FeedItemTargetStatusEnum.FeedItemTargetStatus, str]] = ..., campaign: _Optional[str] = ..., ad_group: _Optional[str] = ..., keyword: _Optional[_Union[_criteria_pb2.KeywordInfo, _Mapping]] = ..., geo_target_constant: _Optional[str] = ..., device: _Optional[_Union[_feed_item_target_device_pb2.FeedItemTargetDeviceEnum.FeedItemTargetDevice, str]] = ..., ad_schedule: _Optional[_Union[_criteria_pb2.AdScheduleInfo, _Mapping]] = ...) -> None: ...
