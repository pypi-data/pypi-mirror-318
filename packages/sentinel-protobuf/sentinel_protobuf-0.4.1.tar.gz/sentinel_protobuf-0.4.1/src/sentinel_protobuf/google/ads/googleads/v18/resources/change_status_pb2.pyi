from google.ads.googleads.v18.enums import change_status_operation_pb2 as _change_status_operation_pb2
from google.ads.googleads.v18.enums import change_status_resource_type_pb2 as _change_status_resource_type_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ChangeStatus(_message.Message):
    __slots__ = ("resource_name", "last_change_date_time", "resource_type", "campaign", "ad_group", "resource_status", "ad_group_ad", "ad_group_criterion", "campaign_criterion", "feed", "feed_item", "ad_group_feed", "campaign_feed", "ad_group_bid_modifier", "shared_set", "campaign_shared_set", "asset", "customer_asset", "campaign_asset", "ad_group_asset", "combined_audience", "asset_group")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_CHANGE_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_FIELD_NUMBER: _ClassVar[int]
    AD_GROUP_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_STATUS_FIELD_NUMBER: _ClassVar[int]
    AD_GROUP_AD_FIELD_NUMBER: _ClassVar[int]
    AD_GROUP_CRITERION_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_CRITERION_FIELD_NUMBER: _ClassVar[int]
    FEED_FIELD_NUMBER: _ClassVar[int]
    FEED_ITEM_FIELD_NUMBER: _ClassVar[int]
    AD_GROUP_FEED_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_FEED_FIELD_NUMBER: _ClassVar[int]
    AD_GROUP_BID_MODIFIER_FIELD_NUMBER: _ClassVar[int]
    SHARED_SET_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_SHARED_SET_FIELD_NUMBER: _ClassVar[int]
    ASSET_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_ASSET_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_ASSET_FIELD_NUMBER: _ClassVar[int]
    AD_GROUP_ASSET_FIELD_NUMBER: _ClassVar[int]
    COMBINED_AUDIENCE_FIELD_NUMBER: _ClassVar[int]
    ASSET_GROUP_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    last_change_date_time: str
    resource_type: _change_status_resource_type_pb2.ChangeStatusResourceTypeEnum.ChangeStatusResourceType
    campaign: str
    ad_group: str
    resource_status: _change_status_operation_pb2.ChangeStatusOperationEnum.ChangeStatusOperation
    ad_group_ad: str
    ad_group_criterion: str
    campaign_criterion: str
    feed: str
    feed_item: str
    ad_group_feed: str
    campaign_feed: str
    ad_group_bid_modifier: str
    shared_set: str
    campaign_shared_set: str
    asset: str
    customer_asset: str
    campaign_asset: str
    ad_group_asset: str
    combined_audience: str
    asset_group: str
    def __init__(self, resource_name: _Optional[str] = ..., last_change_date_time: _Optional[str] = ..., resource_type: _Optional[_Union[_change_status_resource_type_pb2.ChangeStatusResourceTypeEnum.ChangeStatusResourceType, str]] = ..., campaign: _Optional[str] = ..., ad_group: _Optional[str] = ..., resource_status: _Optional[_Union[_change_status_operation_pb2.ChangeStatusOperationEnum.ChangeStatusOperation, str]] = ..., ad_group_ad: _Optional[str] = ..., ad_group_criterion: _Optional[str] = ..., campaign_criterion: _Optional[str] = ..., feed: _Optional[str] = ..., feed_item: _Optional[str] = ..., ad_group_feed: _Optional[str] = ..., campaign_feed: _Optional[str] = ..., ad_group_bid_modifier: _Optional[str] = ..., shared_set: _Optional[str] = ..., campaign_shared_set: _Optional[str] = ..., asset: _Optional[str] = ..., customer_asset: _Optional[str] = ..., campaign_asset: _Optional[str] = ..., ad_group_asset: _Optional[str] = ..., combined_audience: _Optional[str] = ..., asset_group: _Optional[str] = ...) -> None: ...
