from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class CampaignConversionGoalErrorEnum(_message.Message):
    __slots__ = ()

    class CampaignConversionGoalError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[CampaignConversionGoalErrorEnum.CampaignConversionGoalError]
        UNKNOWN: _ClassVar[CampaignConversionGoalErrorEnum.CampaignConversionGoalError]
        CANNOT_USE_CAMPAIGN_GOAL_FOR_SEARCH_ADS_360_MANAGED_CAMPAIGN: _ClassVar[CampaignConversionGoalErrorEnum.CampaignConversionGoalError]
        CANNOT_USE_STORE_SALE_GOAL_FOR_PERFORMANCE_MAX_CAMPAIGN: _ClassVar[CampaignConversionGoalErrorEnum.CampaignConversionGoalError]
    UNSPECIFIED: CampaignConversionGoalErrorEnum.CampaignConversionGoalError
    UNKNOWN: CampaignConversionGoalErrorEnum.CampaignConversionGoalError
    CANNOT_USE_CAMPAIGN_GOAL_FOR_SEARCH_ADS_360_MANAGED_CAMPAIGN: CampaignConversionGoalErrorEnum.CampaignConversionGoalError
    CANNOT_USE_STORE_SALE_GOAL_FOR_PERFORMANCE_MAX_CAMPAIGN: CampaignConversionGoalErrorEnum.CampaignConversionGoalError

    def __init__(self) -> None:
        ...