from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class CampaignPrimaryStatusReasonEnum(_message.Message):
    __slots__ = ()

    class CampaignPrimaryStatusReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[CampaignPrimaryStatusReasonEnum.CampaignPrimaryStatusReason]
        UNKNOWN: _ClassVar[CampaignPrimaryStatusReasonEnum.CampaignPrimaryStatusReason]
        CAMPAIGN_REMOVED: _ClassVar[CampaignPrimaryStatusReasonEnum.CampaignPrimaryStatusReason]
        CAMPAIGN_PAUSED: _ClassVar[CampaignPrimaryStatusReasonEnum.CampaignPrimaryStatusReason]
        CAMPAIGN_PENDING: _ClassVar[CampaignPrimaryStatusReasonEnum.CampaignPrimaryStatusReason]
        CAMPAIGN_ENDED: _ClassVar[CampaignPrimaryStatusReasonEnum.CampaignPrimaryStatusReason]
        CAMPAIGN_DRAFT: _ClassVar[CampaignPrimaryStatusReasonEnum.CampaignPrimaryStatusReason]
        BIDDING_STRATEGY_MISCONFIGURED: _ClassVar[CampaignPrimaryStatusReasonEnum.CampaignPrimaryStatusReason]
        BIDDING_STRATEGY_LIMITED: _ClassVar[CampaignPrimaryStatusReasonEnum.CampaignPrimaryStatusReason]
        BIDDING_STRATEGY_LEARNING: _ClassVar[CampaignPrimaryStatusReasonEnum.CampaignPrimaryStatusReason]
        BIDDING_STRATEGY_CONSTRAINED: _ClassVar[CampaignPrimaryStatusReasonEnum.CampaignPrimaryStatusReason]
        BUDGET_CONSTRAINED: _ClassVar[CampaignPrimaryStatusReasonEnum.CampaignPrimaryStatusReason]
        BUDGET_MISCONFIGURED: _ClassVar[CampaignPrimaryStatusReasonEnum.CampaignPrimaryStatusReason]
        SEARCH_VOLUME_LIMITED: _ClassVar[CampaignPrimaryStatusReasonEnum.CampaignPrimaryStatusReason]
        AD_GROUPS_PAUSED: _ClassVar[CampaignPrimaryStatusReasonEnum.CampaignPrimaryStatusReason]
        NO_AD_GROUPS: _ClassVar[CampaignPrimaryStatusReasonEnum.CampaignPrimaryStatusReason]
        KEYWORDS_PAUSED: _ClassVar[CampaignPrimaryStatusReasonEnum.CampaignPrimaryStatusReason]
        NO_KEYWORDS: _ClassVar[CampaignPrimaryStatusReasonEnum.CampaignPrimaryStatusReason]
        AD_GROUP_ADS_PAUSED: _ClassVar[CampaignPrimaryStatusReasonEnum.CampaignPrimaryStatusReason]
        NO_AD_GROUP_ADS: _ClassVar[CampaignPrimaryStatusReasonEnum.CampaignPrimaryStatusReason]
        HAS_ADS_LIMITED_BY_POLICY: _ClassVar[CampaignPrimaryStatusReasonEnum.CampaignPrimaryStatusReason]
        HAS_ADS_DISAPPROVED: _ClassVar[CampaignPrimaryStatusReasonEnum.CampaignPrimaryStatusReason]
        MOST_ADS_UNDER_REVIEW: _ClassVar[CampaignPrimaryStatusReasonEnum.CampaignPrimaryStatusReason]
        MISSING_LEAD_FORM_EXTENSION: _ClassVar[CampaignPrimaryStatusReasonEnum.CampaignPrimaryStatusReason]
        MISSING_CALL_EXTENSION: _ClassVar[CampaignPrimaryStatusReasonEnum.CampaignPrimaryStatusReason]
        LEAD_FORM_EXTENSION_UNDER_REVIEW: _ClassVar[CampaignPrimaryStatusReasonEnum.CampaignPrimaryStatusReason]
        LEAD_FORM_EXTENSION_DISAPPROVED: _ClassVar[CampaignPrimaryStatusReasonEnum.CampaignPrimaryStatusReason]
        CALL_EXTENSION_UNDER_REVIEW: _ClassVar[CampaignPrimaryStatusReasonEnum.CampaignPrimaryStatusReason]
        CALL_EXTENSION_DISAPPROVED: _ClassVar[CampaignPrimaryStatusReasonEnum.CampaignPrimaryStatusReason]
        NO_MOBILE_APPLICATION_AD_GROUP_CRITERIA: _ClassVar[CampaignPrimaryStatusReasonEnum.CampaignPrimaryStatusReason]
        CAMPAIGN_GROUP_PAUSED: _ClassVar[CampaignPrimaryStatusReasonEnum.CampaignPrimaryStatusReason]
        CAMPAIGN_GROUP_ALL_GROUP_BUDGETS_ENDED: _ClassVar[CampaignPrimaryStatusReasonEnum.CampaignPrimaryStatusReason]
        APP_NOT_RELEASED: _ClassVar[CampaignPrimaryStatusReasonEnum.CampaignPrimaryStatusReason]
        APP_PARTIALLY_RELEASED: _ClassVar[CampaignPrimaryStatusReasonEnum.CampaignPrimaryStatusReason]
        HAS_ASSET_GROUPS_DISAPPROVED: _ClassVar[CampaignPrimaryStatusReasonEnum.CampaignPrimaryStatusReason]
        HAS_ASSET_GROUPS_LIMITED_BY_POLICY: _ClassVar[CampaignPrimaryStatusReasonEnum.CampaignPrimaryStatusReason]
        MOST_ASSET_GROUPS_UNDER_REVIEW: _ClassVar[CampaignPrimaryStatusReasonEnum.CampaignPrimaryStatusReason]
        NO_ASSET_GROUPS: _ClassVar[CampaignPrimaryStatusReasonEnum.CampaignPrimaryStatusReason]
        ASSET_GROUPS_PAUSED: _ClassVar[CampaignPrimaryStatusReasonEnum.CampaignPrimaryStatusReason]
    UNSPECIFIED: CampaignPrimaryStatusReasonEnum.CampaignPrimaryStatusReason
    UNKNOWN: CampaignPrimaryStatusReasonEnum.CampaignPrimaryStatusReason
    CAMPAIGN_REMOVED: CampaignPrimaryStatusReasonEnum.CampaignPrimaryStatusReason
    CAMPAIGN_PAUSED: CampaignPrimaryStatusReasonEnum.CampaignPrimaryStatusReason
    CAMPAIGN_PENDING: CampaignPrimaryStatusReasonEnum.CampaignPrimaryStatusReason
    CAMPAIGN_ENDED: CampaignPrimaryStatusReasonEnum.CampaignPrimaryStatusReason
    CAMPAIGN_DRAFT: CampaignPrimaryStatusReasonEnum.CampaignPrimaryStatusReason
    BIDDING_STRATEGY_MISCONFIGURED: CampaignPrimaryStatusReasonEnum.CampaignPrimaryStatusReason
    BIDDING_STRATEGY_LIMITED: CampaignPrimaryStatusReasonEnum.CampaignPrimaryStatusReason
    BIDDING_STRATEGY_LEARNING: CampaignPrimaryStatusReasonEnum.CampaignPrimaryStatusReason
    BIDDING_STRATEGY_CONSTRAINED: CampaignPrimaryStatusReasonEnum.CampaignPrimaryStatusReason
    BUDGET_CONSTRAINED: CampaignPrimaryStatusReasonEnum.CampaignPrimaryStatusReason
    BUDGET_MISCONFIGURED: CampaignPrimaryStatusReasonEnum.CampaignPrimaryStatusReason
    SEARCH_VOLUME_LIMITED: CampaignPrimaryStatusReasonEnum.CampaignPrimaryStatusReason
    AD_GROUPS_PAUSED: CampaignPrimaryStatusReasonEnum.CampaignPrimaryStatusReason
    NO_AD_GROUPS: CampaignPrimaryStatusReasonEnum.CampaignPrimaryStatusReason
    KEYWORDS_PAUSED: CampaignPrimaryStatusReasonEnum.CampaignPrimaryStatusReason
    NO_KEYWORDS: CampaignPrimaryStatusReasonEnum.CampaignPrimaryStatusReason
    AD_GROUP_ADS_PAUSED: CampaignPrimaryStatusReasonEnum.CampaignPrimaryStatusReason
    NO_AD_GROUP_ADS: CampaignPrimaryStatusReasonEnum.CampaignPrimaryStatusReason
    HAS_ADS_LIMITED_BY_POLICY: CampaignPrimaryStatusReasonEnum.CampaignPrimaryStatusReason
    HAS_ADS_DISAPPROVED: CampaignPrimaryStatusReasonEnum.CampaignPrimaryStatusReason
    MOST_ADS_UNDER_REVIEW: CampaignPrimaryStatusReasonEnum.CampaignPrimaryStatusReason
    MISSING_LEAD_FORM_EXTENSION: CampaignPrimaryStatusReasonEnum.CampaignPrimaryStatusReason
    MISSING_CALL_EXTENSION: CampaignPrimaryStatusReasonEnum.CampaignPrimaryStatusReason
    LEAD_FORM_EXTENSION_UNDER_REVIEW: CampaignPrimaryStatusReasonEnum.CampaignPrimaryStatusReason
    LEAD_FORM_EXTENSION_DISAPPROVED: CampaignPrimaryStatusReasonEnum.CampaignPrimaryStatusReason
    CALL_EXTENSION_UNDER_REVIEW: CampaignPrimaryStatusReasonEnum.CampaignPrimaryStatusReason
    CALL_EXTENSION_DISAPPROVED: CampaignPrimaryStatusReasonEnum.CampaignPrimaryStatusReason
    NO_MOBILE_APPLICATION_AD_GROUP_CRITERIA: CampaignPrimaryStatusReasonEnum.CampaignPrimaryStatusReason
    CAMPAIGN_GROUP_PAUSED: CampaignPrimaryStatusReasonEnum.CampaignPrimaryStatusReason
    CAMPAIGN_GROUP_ALL_GROUP_BUDGETS_ENDED: CampaignPrimaryStatusReasonEnum.CampaignPrimaryStatusReason
    APP_NOT_RELEASED: CampaignPrimaryStatusReasonEnum.CampaignPrimaryStatusReason
    APP_PARTIALLY_RELEASED: CampaignPrimaryStatusReasonEnum.CampaignPrimaryStatusReason
    HAS_ASSET_GROUPS_DISAPPROVED: CampaignPrimaryStatusReasonEnum.CampaignPrimaryStatusReason
    HAS_ASSET_GROUPS_LIMITED_BY_POLICY: CampaignPrimaryStatusReasonEnum.CampaignPrimaryStatusReason
    MOST_ASSET_GROUPS_UNDER_REVIEW: CampaignPrimaryStatusReasonEnum.CampaignPrimaryStatusReason
    NO_ASSET_GROUPS: CampaignPrimaryStatusReasonEnum.CampaignPrimaryStatusReason
    ASSET_GROUPS_PAUSED: CampaignPrimaryStatusReasonEnum.CampaignPrimaryStatusReason

    def __init__(self) -> None:
        ...