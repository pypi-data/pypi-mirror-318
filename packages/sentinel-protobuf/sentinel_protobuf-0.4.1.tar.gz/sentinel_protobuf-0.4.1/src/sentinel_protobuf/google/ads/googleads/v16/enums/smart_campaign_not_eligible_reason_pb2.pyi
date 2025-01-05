from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class SmartCampaignNotEligibleReasonEnum(_message.Message):
    __slots__ = ()

    class SmartCampaignNotEligibleReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[SmartCampaignNotEligibleReasonEnum.SmartCampaignNotEligibleReason]
        UNKNOWN: _ClassVar[SmartCampaignNotEligibleReasonEnum.SmartCampaignNotEligibleReason]
        ACCOUNT_ISSUE: _ClassVar[SmartCampaignNotEligibleReasonEnum.SmartCampaignNotEligibleReason]
        BILLING_ISSUE: _ClassVar[SmartCampaignNotEligibleReasonEnum.SmartCampaignNotEligibleReason]
        BUSINESS_PROFILE_LOCATION_REMOVED: _ClassVar[SmartCampaignNotEligibleReasonEnum.SmartCampaignNotEligibleReason]
        ALL_ADS_DISAPPROVED: _ClassVar[SmartCampaignNotEligibleReasonEnum.SmartCampaignNotEligibleReason]
    UNSPECIFIED: SmartCampaignNotEligibleReasonEnum.SmartCampaignNotEligibleReason
    UNKNOWN: SmartCampaignNotEligibleReasonEnum.SmartCampaignNotEligibleReason
    ACCOUNT_ISSUE: SmartCampaignNotEligibleReasonEnum.SmartCampaignNotEligibleReason
    BILLING_ISSUE: SmartCampaignNotEligibleReasonEnum.SmartCampaignNotEligibleReason
    BUSINESS_PROFILE_LOCATION_REMOVED: SmartCampaignNotEligibleReasonEnum.SmartCampaignNotEligibleReason
    ALL_ADS_DISAPPROVED: SmartCampaignNotEligibleReasonEnum.SmartCampaignNotEligibleReason

    def __init__(self) -> None:
        ...