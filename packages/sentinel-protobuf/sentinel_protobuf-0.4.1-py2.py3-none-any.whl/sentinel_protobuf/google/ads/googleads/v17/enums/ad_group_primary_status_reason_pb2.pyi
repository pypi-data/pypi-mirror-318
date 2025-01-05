from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class AdGroupPrimaryStatusReasonEnum(_message.Message):
    __slots__ = ()

    class AdGroupPrimaryStatusReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[AdGroupPrimaryStatusReasonEnum.AdGroupPrimaryStatusReason]
        UNKNOWN: _ClassVar[AdGroupPrimaryStatusReasonEnum.AdGroupPrimaryStatusReason]
        CAMPAIGN_REMOVED: _ClassVar[AdGroupPrimaryStatusReasonEnum.AdGroupPrimaryStatusReason]
        CAMPAIGN_PAUSED: _ClassVar[AdGroupPrimaryStatusReasonEnum.AdGroupPrimaryStatusReason]
        CAMPAIGN_PENDING: _ClassVar[AdGroupPrimaryStatusReasonEnum.AdGroupPrimaryStatusReason]
        CAMPAIGN_ENDED: _ClassVar[AdGroupPrimaryStatusReasonEnum.AdGroupPrimaryStatusReason]
        AD_GROUP_PAUSED: _ClassVar[AdGroupPrimaryStatusReasonEnum.AdGroupPrimaryStatusReason]
        AD_GROUP_REMOVED: _ClassVar[AdGroupPrimaryStatusReasonEnum.AdGroupPrimaryStatusReason]
        AD_GROUP_INCOMPLETE: _ClassVar[AdGroupPrimaryStatusReasonEnum.AdGroupPrimaryStatusReason]
        KEYWORDS_PAUSED: _ClassVar[AdGroupPrimaryStatusReasonEnum.AdGroupPrimaryStatusReason]
        NO_KEYWORDS: _ClassVar[AdGroupPrimaryStatusReasonEnum.AdGroupPrimaryStatusReason]
        AD_GROUP_ADS_PAUSED: _ClassVar[AdGroupPrimaryStatusReasonEnum.AdGroupPrimaryStatusReason]
        NO_AD_GROUP_ADS: _ClassVar[AdGroupPrimaryStatusReasonEnum.AdGroupPrimaryStatusReason]
        HAS_ADS_DISAPPROVED: _ClassVar[AdGroupPrimaryStatusReasonEnum.AdGroupPrimaryStatusReason]
        HAS_ADS_LIMITED_BY_POLICY: _ClassVar[AdGroupPrimaryStatusReasonEnum.AdGroupPrimaryStatusReason]
        MOST_ADS_UNDER_REVIEW: _ClassVar[AdGroupPrimaryStatusReasonEnum.AdGroupPrimaryStatusReason]
        CAMPAIGN_DRAFT: _ClassVar[AdGroupPrimaryStatusReasonEnum.AdGroupPrimaryStatusReason]
        AD_GROUP_PAUSED_DUE_TO_LOW_ACTIVITY: _ClassVar[AdGroupPrimaryStatusReasonEnum.AdGroupPrimaryStatusReason]
    UNSPECIFIED: AdGroupPrimaryStatusReasonEnum.AdGroupPrimaryStatusReason
    UNKNOWN: AdGroupPrimaryStatusReasonEnum.AdGroupPrimaryStatusReason
    CAMPAIGN_REMOVED: AdGroupPrimaryStatusReasonEnum.AdGroupPrimaryStatusReason
    CAMPAIGN_PAUSED: AdGroupPrimaryStatusReasonEnum.AdGroupPrimaryStatusReason
    CAMPAIGN_PENDING: AdGroupPrimaryStatusReasonEnum.AdGroupPrimaryStatusReason
    CAMPAIGN_ENDED: AdGroupPrimaryStatusReasonEnum.AdGroupPrimaryStatusReason
    AD_GROUP_PAUSED: AdGroupPrimaryStatusReasonEnum.AdGroupPrimaryStatusReason
    AD_GROUP_REMOVED: AdGroupPrimaryStatusReasonEnum.AdGroupPrimaryStatusReason
    AD_GROUP_INCOMPLETE: AdGroupPrimaryStatusReasonEnum.AdGroupPrimaryStatusReason
    KEYWORDS_PAUSED: AdGroupPrimaryStatusReasonEnum.AdGroupPrimaryStatusReason
    NO_KEYWORDS: AdGroupPrimaryStatusReasonEnum.AdGroupPrimaryStatusReason
    AD_GROUP_ADS_PAUSED: AdGroupPrimaryStatusReasonEnum.AdGroupPrimaryStatusReason
    NO_AD_GROUP_ADS: AdGroupPrimaryStatusReasonEnum.AdGroupPrimaryStatusReason
    HAS_ADS_DISAPPROVED: AdGroupPrimaryStatusReasonEnum.AdGroupPrimaryStatusReason
    HAS_ADS_LIMITED_BY_POLICY: AdGroupPrimaryStatusReasonEnum.AdGroupPrimaryStatusReason
    MOST_ADS_UNDER_REVIEW: AdGroupPrimaryStatusReasonEnum.AdGroupPrimaryStatusReason
    CAMPAIGN_DRAFT: AdGroupPrimaryStatusReasonEnum.AdGroupPrimaryStatusReason
    AD_GROUP_PAUSED_DUE_TO_LOW_ACTIVITY: AdGroupPrimaryStatusReasonEnum.AdGroupPrimaryStatusReason

    def __init__(self) -> None:
        ...