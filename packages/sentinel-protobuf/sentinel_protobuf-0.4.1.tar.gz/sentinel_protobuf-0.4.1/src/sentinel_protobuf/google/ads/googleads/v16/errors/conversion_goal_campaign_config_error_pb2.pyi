from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class ConversionGoalCampaignConfigErrorEnum(_message.Message):
    __slots__ = ()

    class ConversionGoalCampaignConfigError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ConversionGoalCampaignConfigErrorEnum.ConversionGoalCampaignConfigError]
        UNKNOWN: _ClassVar[ConversionGoalCampaignConfigErrorEnum.ConversionGoalCampaignConfigError]
        CANNOT_USE_CAMPAIGN_GOAL_FOR_SEARCH_ADS_360_MANAGED_CAMPAIGN: _ClassVar[ConversionGoalCampaignConfigErrorEnum.ConversionGoalCampaignConfigError]
        CUSTOM_GOAL_DOES_NOT_BELONG_TO_GOOGLE_ADS_CONVERSION_CUSTOMER: _ClassVar[ConversionGoalCampaignConfigErrorEnum.ConversionGoalCampaignConfigError]
        CAMPAIGN_CANNOT_USE_UNIFIED_GOALS: _ClassVar[ConversionGoalCampaignConfigErrorEnum.ConversionGoalCampaignConfigError]
        EMPTY_CONVERSION_GOALS: _ClassVar[ConversionGoalCampaignConfigErrorEnum.ConversionGoalCampaignConfigError]
        STORE_SALE_STORE_VISIT_CANNOT_BE_BOTH_INCLUDED: _ClassVar[ConversionGoalCampaignConfigErrorEnum.ConversionGoalCampaignConfigError]
        PERFORMANCE_MAX_CAMPAIGN_CANNOT_USE_CUSTOM_GOAL_WITH_STORE_SALES: _ClassVar[ConversionGoalCampaignConfigErrorEnum.ConversionGoalCampaignConfigError]
    UNSPECIFIED: ConversionGoalCampaignConfigErrorEnum.ConversionGoalCampaignConfigError
    UNKNOWN: ConversionGoalCampaignConfigErrorEnum.ConversionGoalCampaignConfigError
    CANNOT_USE_CAMPAIGN_GOAL_FOR_SEARCH_ADS_360_MANAGED_CAMPAIGN: ConversionGoalCampaignConfigErrorEnum.ConversionGoalCampaignConfigError
    CUSTOM_GOAL_DOES_NOT_BELONG_TO_GOOGLE_ADS_CONVERSION_CUSTOMER: ConversionGoalCampaignConfigErrorEnum.ConversionGoalCampaignConfigError
    CAMPAIGN_CANNOT_USE_UNIFIED_GOALS: ConversionGoalCampaignConfigErrorEnum.ConversionGoalCampaignConfigError
    EMPTY_CONVERSION_GOALS: ConversionGoalCampaignConfigErrorEnum.ConversionGoalCampaignConfigError
    STORE_SALE_STORE_VISIT_CANNOT_BE_BOTH_INCLUDED: ConversionGoalCampaignConfigErrorEnum.ConversionGoalCampaignConfigError
    PERFORMANCE_MAX_CAMPAIGN_CANNOT_USE_CUSTOM_GOAL_WITH_STORE_SALES: ConversionGoalCampaignConfigErrorEnum.ConversionGoalCampaignConfigError

    def __init__(self) -> None:
        ...