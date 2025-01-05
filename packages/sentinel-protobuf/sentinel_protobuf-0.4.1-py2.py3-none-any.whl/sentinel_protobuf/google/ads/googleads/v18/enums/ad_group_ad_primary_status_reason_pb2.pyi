from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class AdGroupAdPrimaryStatusReasonEnum(_message.Message):
    __slots__ = ()

    class AdGroupAdPrimaryStatusReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[AdGroupAdPrimaryStatusReasonEnum.AdGroupAdPrimaryStatusReason]
        UNKNOWN: _ClassVar[AdGroupAdPrimaryStatusReasonEnum.AdGroupAdPrimaryStatusReason]
        CAMPAIGN_REMOVED: _ClassVar[AdGroupAdPrimaryStatusReasonEnum.AdGroupAdPrimaryStatusReason]
        CAMPAIGN_PAUSED: _ClassVar[AdGroupAdPrimaryStatusReasonEnum.AdGroupAdPrimaryStatusReason]
        CAMPAIGN_PENDING: _ClassVar[AdGroupAdPrimaryStatusReasonEnum.AdGroupAdPrimaryStatusReason]
        CAMPAIGN_ENDED: _ClassVar[AdGroupAdPrimaryStatusReasonEnum.AdGroupAdPrimaryStatusReason]
        AD_GROUP_PAUSED: _ClassVar[AdGroupAdPrimaryStatusReasonEnum.AdGroupAdPrimaryStatusReason]
        AD_GROUP_REMOVED: _ClassVar[AdGroupAdPrimaryStatusReasonEnum.AdGroupAdPrimaryStatusReason]
        AD_GROUP_AD_PAUSED: _ClassVar[AdGroupAdPrimaryStatusReasonEnum.AdGroupAdPrimaryStatusReason]
        AD_GROUP_AD_REMOVED: _ClassVar[AdGroupAdPrimaryStatusReasonEnum.AdGroupAdPrimaryStatusReason]
        AD_GROUP_AD_DISAPPROVED: _ClassVar[AdGroupAdPrimaryStatusReasonEnum.AdGroupAdPrimaryStatusReason]
        AD_GROUP_AD_UNDER_REVIEW: _ClassVar[AdGroupAdPrimaryStatusReasonEnum.AdGroupAdPrimaryStatusReason]
        AD_GROUP_AD_POOR_QUALITY: _ClassVar[AdGroupAdPrimaryStatusReasonEnum.AdGroupAdPrimaryStatusReason]
        AD_GROUP_AD_NO_ADS: _ClassVar[AdGroupAdPrimaryStatusReasonEnum.AdGroupAdPrimaryStatusReason]
        AD_GROUP_AD_APPROVED_LABELED: _ClassVar[AdGroupAdPrimaryStatusReasonEnum.AdGroupAdPrimaryStatusReason]
        AD_GROUP_AD_AREA_OF_INTEREST_ONLY: _ClassVar[AdGroupAdPrimaryStatusReasonEnum.AdGroupAdPrimaryStatusReason]
        AD_GROUP_AD_UNDER_APPEAL: _ClassVar[AdGroupAdPrimaryStatusReasonEnum.AdGroupAdPrimaryStatusReason]
    UNSPECIFIED: AdGroupAdPrimaryStatusReasonEnum.AdGroupAdPrimaryStatusReason
    UNKNOWN: AdGroupAdPrimaryStatusReasonEnum.AdGroupAdPrimaryStatusReason
    CAMPAIGN_REMOVED: AdGroupAdPrimaryStatusReasonEnum.AdGroupAdPrimaryStatusReason
    CAMPAIGN_PAUSED: AdGroupAdPrimaryStatusReasonEnum.AdGroupAdPrimaryStatusReason
    CAMPAIGN_PENDING: AdGroupAdPrimaryStatusReasonEnum.AdGroupAdPrimaryStatusReason
    CAMPAIGN_ENDED: AdGroupAdPrimaryStatusReasonEnum.AdGroupAdPrimaryStatusReason
    AD_GROUP_PAUSED: AdGroupAdPrimaryStatusReasonEnum.AdGroupAdPrimaryStatusReason
    AD_GROUP_REMOVED: AdGroupAdPrimaryStatusReasonEnum.AdGroupAdPrimaryStatusReason
    AD_GROUP_AD_PAUSED: AdGroupAdPrimaryStatusReasonEnum.AdGroupAdPrimaryStatusReason
    AD_GROUP_AD_REMOVED: AdGroupAdPrimaryStatusReasonEnum.AdGroupAdPrimaryStatusReason
    AD_GROUP_AD_DISAPPROVED: AdGroupAdPrimaryStatusReasonEnum.AdGroupAdPrimaryStatusReason
    AD_GROUP_AD_UNDER_REVIEW: AdGroupAdPrimaryStatusReasonEnum.AdGroupAdPrimaryStatusReason
    AD_GROUP_AD_POOR_QUALITY: AdGroupAdPrimaryStatusReasonEnum.AdGroupAdPrimaryStatusReason
    AD_GROUP_AD_NO_ADS: AdGroupAdPrimaryStatusReasonEnum.AdGroupAdPrimaryStatusReason
    AD_GROUP_AD_APPROVED_LABELED: AdGroupAdPrimaryStatusReasonEnum.AdGroupAdPrimaryStatusReason
    AD_GROUP_AD_AREA_OF_INTEREST_ONLY: AdGroupAdPrimaryStatusReasonEnum.AdGroupAdPrimaryStatusReason
    AD_GROUP_AD_UNDER_APPEAL: AdGroupAdPrimaryStatusReasonEnum.AdGroupAdPrimaryStatusReason

    def __init__(self) -> None:
        ...