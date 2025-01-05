from google.ads.googleads.v16.enums import change_client_type_pb2 as _change_client_type_pb2
from google.ads.googleads.v16.enums import change_event_resource_type_pb2 as _change_event_resource_type_pb2
from google.ads.googleads.v16.enums import resource_change_operation_pb2 as _resource_change_operation_pb2
from google.ads.googleads.v16.resources import ad_pb2 as _ad_pb2
from google.ads.googleads.v16.resources import ad_group_pb2 as _ad_group_pb2
from google.ads.googleads.v16.resources import ad_group_ad_pb2 as _ad_group_ad_pb2
from google.ads.googleads.v16.resources import ad_group_asset_pb2 as _ad_group_asset_pb2
from google.ads.googleads.v16.resources import ad_group_bid_modifier_pb2 as _ad_group_bid_modifier_pb2
from google.ads.googleads.v16.resources import ad_group_criterion_pb2 as _ad_group_criterion_pb2
from google.ads.googleads.v16.resources import ad_group_feed_pb2 as _ad_group_feed_pb2
from google.ads.googleads.v16.resources import asset_pb2 as _asset_pb2
from google.ads.googleads.v16.resources import asset_set_pb2 as _asset_set_pb2
from google.ads.googleads.v16.resources import asset_set_asset_pb2 as _asset_set_asset_pb2
from google.ads.googleads.v16.resources import campaign_pb2 as _campaign_pb2
from google.ads.googleads.v16.resources import campaign_asset_pb2 as _campaign_asset_pb2
from google.ads.googleads.v16.resources import campaign_asset_set_pb2 as _campaign_asset_set_pb2
from google.ads.googleads.v16.resources import campaign_budget_pb2 as _campaign_budget_pb2
from google.ads.googleads.v16.resources import campaign_criterion_pb2 as _campaign_criterion_pb2
from google.ads.googleads.v16.resources import campaign_feed_pb2 as _campaign_feed_pb2
from google.ads.googleads.v16.resources import customer_asset_pb2 as _customer_asset_pb2
from google.ads.googleads.v16.resources import feed_pb2 as _feed_pb2
from google.ads.googleads.v16.resources import feed_item_pb2 as _feed_item_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ChangeEvent(_message.Message):
    __slots__ = ("resource_name", "change_date_time", "change_resource_type", "change_resource_name", "client_type", "user_email", "old_resource", "new_resource", "resource_change_operation", "changed_fields", "campaign", "ad_group", "feed", "feed_item", "asset")
    class ChangedResource(_message.Message):
        __slots__ = ("ad", "ad_group", "ad_group_criterion", "campaign", "campaign_budget", "ad_group_bid_modifier", "campaign_criterion", "feed", "feed_item", "campaign_feed", "ad_group_feed", "ad_group_ad", "asset", "customer_asset", "campaign_asset", "ad_group_asset", "asset_set", "asset_set_asset", "campaign_asset_set")
        AD_FIELD_NUMBER: _ClassVar[int]
        AD_GROUP_FIELD_NUMBER: _ClassVar[int]
        AD_GROUP_CRITERION_FIELD_NUMBER: _ClassVar[int]
        CAMPAIGN_FIELD_NUMBER: _ClassVar[int]
        CAMPAIGN_BUDGET_FIELD_NUMBER: _ClassVar[int]
        AD_GROUP_BID_MODIFIER_FIELD_NUMBER: _ClassVar[int]
        CAMPAIGN_CRITERION_FIELD_NUMBER: _ClassVar[int]
        FEED_FIELD_NUMBER: _ClassVar[int]
        FEED_ITEM_FIELD_NUMBER: _ClassVar[int]
        CAMPAIGN_FEED_FIELD_NUMBER: _ClassVar[int]
        AD_GROUP_FEED_FIELD_NUMBER: _ClassVar[int]
        AD_GROUP_AD_FIELD_NUMBER: _ClassVar[int]
        ASSET_FIELD_NUMBER: _ClassVar[int]
        CUSTOMER_ASSET_FIELD_NUMBER: _ClassVar[int]
        CAMPAIGN_ASSET_FIELD_NUMBER: _ClassVar[int]
        AD_GROUP_ASSET_FIELD_NUMBER: _ClassVar[int]
        ASSET_SET_FIELD_NUMBER: _ClassVar[int]
        ASSET_SET_ASSET_FIELD_NUMBER: _ClassVar[int]
        CAMPAIGN_ASSET_SET_FIELD_NUMBER: _ClassVar[int]
        ad: _ad_pb2.Ad
        ad_group: _ad_group_pb2.AdGroup
        ad_group_criterion: _ad_group_criterion_pb2.AdGroupCriterion
        campaign: _campaign_pb2.Campaign
        campaign_budget: _campaign_budget_pb2.CampaignBudget
        ad_group_bid_modifier: _ad_group_bid_modifier_pb2.AdGroupBidModifier
        campaign_criterion: _campaign_criterion_pb2.CampaignCriterion
        feed: _feed_pb2.Feed
        feed_item: _feed_item_pb2.FeedItem
        campaign_feed: _campaign_feed_pb2.CampaignFeed
        ad_group_feed: _ad_group_feed_pb2.AdGroupFeed
        ad_group_ad: _ad_group_ad_pb2.AdGroupAd
        asset: _asset_pb2.Asset
        customer_asset: _customer_asset_pb2.CustomerAsset
        campaign_asset: _campaign_asset_pb2.CampaignAsset
        ad_group_asset: _ad_group_asset_pb2.AdGroupAsset
        asset_set: _asset_set_pb2.AssetSet
        asset_set_asset: _asset_set_asset_pb2.AssetSetAsset
        campaign_asset_set: _campaign_asset_set_pb2.CampaignAssetSet
        def __init__(self, ad: _Optional[_Union[_ad_pb2.Ad, _Mapping]] = ..., ad_group: _Optional[_Union[_ad_group_pb2.AdGroup, _Mapping]] = ..., ad_group_criterion: _Optional[_Union[_ad_group_criterion_pb2.AdGroupCriterion, _Mapping]] = ..., campaign: _Optional[_Union[_campaign_pb2.Campaign, _Mapping]] = ..., campaign_budget: _Optional[_Union[_campaign_budget_pb2.CampaignBudget, _Mapping]] = ..., ad_group_bid_modifier: _Optional[_Union[_ad_group_bid_modifier_pb2.AdGroupBidModifier, _Mapping]] = ..., campaign_criterion: _Optional[_Union[_campaign_criterion_pb2.CampaignCriterion, _Mapping]] = ..., feed: _Optional[_Union[_feed_pb2.Feed, _Mapping]] = ..., feed_item: _Optional[_Union[_feed_item_pb2.FeedItem, _Mapping]] = ..., campaign_feed: _Optional[_Union[_campaign_feed_pb2.CampaignFeed, _Mapping]] = ..., ad_group_feed: _Optional[_Union[_ad_group_feed_pb2.AdGroupFeed, _Mapping]] = ..., ad_group_ad: _Optional[_Union[_ad_group_ad_pb2.AdGroupAd, _Mapping]] = ..., asset: _Optional[_Union[_asset_pb2.Asset, _Mapping]] = ..., customer_asset: _Optional[_Union[_customer_asset_pb2.CustomerAsset, _Mapping]] = ..., campaign_asset: _Optional[_Union[_campaign_asset_pb2.CampaignAsset, _Mapping]] = ..., ad_group_asset: _Optional[_Union[_ad_group_asset_pb2.AdGroupAsset, _Mapping]] = ..., asset_set: _Optional[_Union[_asset_set_pb2.AssetSet, _Mapping]] = ..., asset_set_asset: _Optional[_Union[_asset_set_asset_pb2.AssetSetAsset, _Mapping]] = ..., campaign_asset_set: _Optional[_Union[_campaign_asset_set_pb2.CampaignAssetSet, _Mapping]] = ...) -> None: ...
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    CHANGE_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    CHANGE_RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    CHANGE_RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    CLIENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    USER_EMAIL_FIELD_NUMBER: _ClassVar[int]
    OLD_RESOURCE_FIELD_NUMBER: _ClassVar[int]
    NEW_RESOURCE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_CHANGE_OPERATION_FIELD_NUMBER: _ClassVar[int]
    CHANGED_FIELDS_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_FIELD_NUMBER: _ClassVar[int]
    AD_GROUP_FIELD_NUMBER: _ClassVar[int]
    FEED_FIELD_NUMBER: _ClassVar[int]
    FEED_ITEM_FIELD_NUMBER: _ClassVar[int]
    ASSET_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    change_date_time: str
    change_resource_type: _change_event_resource_type_pb2.ChangeEventResourceTypeEnum.ChangeEventResourceType
    change_resource_name: str
    client_type: _change_client_type_pb2.ChangeClientTypeEnum.ChangeClientType
    user_email: str
    old_resource: ChangeEvent.ChangedResource
    new_resource: ChangeEvent.ChangedResource
    resource_change_operation: _resource_change_operation_pb2.ResourceChangeOperationEnum.ResourceChangeOperation
    changed_fields: _field_mask_pb2.FieldMask
    campaign: str
    ad_group: str
    feed: str
    feed_item: str
    asset: str
    def __init__(self, resource_name: _Optional[str] = ..., change_date_time: _Optional[str] = ..., change_resource_type: _Optional[_Union[_change_event_resource_type_pb2.ChangeEventResourceTypeEnum.ChangeEventResourceType, str]] = ..., change_resource_name: _Optional[str] = ..., client_type: _Optional[_Union[_change_client_type_pb2.ChangeClientTypeEnum.ChangeClientType, str]] = ..., user_email: _Optional[str] = ..., old_resource: _Optional[_Union[ChangeEvent.ChangedResource, _Mapping]] = ..., new_resource: _Optional[_Union[ChangeEvent.ChangedResource, _Mapping]] = ..., resource_change_operation: _Optional[_Union[_resource_change_operation_pb2.ResourceChangeOperationEnum.ResourceChangeOperation, str]] = ..., changed_fields: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., campaign: _Optional[str] = ..., ad_group: _Optional[str] = ..., feed: _Optional[str] = ..., feed_item: _Optional[str] = ..., asset: _Optional[str] = ...) -> None: ...
