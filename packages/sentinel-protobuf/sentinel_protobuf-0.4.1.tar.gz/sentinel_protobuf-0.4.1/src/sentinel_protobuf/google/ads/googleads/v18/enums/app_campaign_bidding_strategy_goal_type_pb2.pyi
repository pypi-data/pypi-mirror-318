from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class AppCampaignBiddingStrategyGoalTypeEnum(_message.Message):
    __slots__ = ()

    class AppCampaignBiddingStrategyGoalType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[AppCampaignBiddingStrategyGoalTypeEnum.AppCampaignBiddingStrategyGoalType]
        UNKNOWN: _ClassVar[AppCampaignBiddingStrategyGoalTypeEnum.AppCampaignBiddingStrategyGoalType]
        OPTIMIZE_INSTALLS_TARGET_INSTALL_COST: _ClassVar[AppCampaignBiddingStrategyGoalTypeEnum.AppCampaignBiddingStrategyGoalType]
        OPTIMIZE_IN_APP_CONVERSIONS_TARGET_INSTALL_COST: _ClassVar[AppCampaignBiddingStrategyGoalTypeEnum.AppCampaignBiddingStrategyGoalType]
        OPTIMIZE_IN_APP_CONVERSIONS_TARGET_CONVERSION_COST: _ClassVar[AppCampaignBiddingStrategyGoalTypeEnum.AppCampaignBiddingStrategyGoalType]
        OPTIMIZE_RETURN_ON_ADVERTISING_SPEND: _ClassVar[AppCampaignBiddingStrategyGoalTypeEnum.AppCampaignBiddingStrategyGoalType]
        OPTIMIZE_PRE_REGISTRATION_CONVERSION_VOLUME: _ClassVar[AppCampaignBiddingStrategyGoalTypeEnum.AppCampaignBiddingStrategyGoalType]
        OPTIMIZE_INSTALLS_WITHOUT_TARGET_INSTALL_COST: _ClassVar[AppCampaignBiddingStrategyGoalTypeEnum.AppCampaignBiddingStrategyGoalType]
    UNSPECIFIED: AppCampaignBiddingStrategyGoalTypeEnum.AppCampaignBiddingStrategyGoalType
    UNKNOWN: AppCampaignBiddingStrategyGoalTypeEnum.AppCampaignBiddingStrategyGoalType
    OPTIMIZE_INSTALLS_TARGET_INSTALL_COST: AppCampaignBiddingStrategyGoalTypeEnum.AppCampaignBiddingStrategyGoalType
    OPTIMIZE_IN_APP_CONVERSIONS_TARGET_INSTALL_COST: AppCampaignBiddingStrategyGoalTypeEnum.AppCampaignBiddingStrategyGoalType
    OPTIMIZE_IN_APP_CONVERSIONS_TARGET_CONVERSION_COST: AppCampaignBiddingStrategyGoalTypeEnum.AppCampaignBiddingStrategyGoalType
    OPTIMIZE_RETURN_ON_ADVERTISING_SPEND: AppCampaignBiddingStrategyGoalTypeEnum.AppCampaignBiddingStrategyGoalType
    OPTIMIZE_PRE_REGISTRATION_CONVERSION_VOLUME: AppCampaignBiddingStrategyGoalTypeEnum.AppCampaignBiddingStrategyGoalType
    OPTIMIZE_INSTALLS_WITHOUT_TARGET_INSTALL_COST: AppCampaignBiddingStrategyGoalTypeEnum.AppCampaignBiddingStrategyGoalType

    def __init__(self) -> None:
        ...