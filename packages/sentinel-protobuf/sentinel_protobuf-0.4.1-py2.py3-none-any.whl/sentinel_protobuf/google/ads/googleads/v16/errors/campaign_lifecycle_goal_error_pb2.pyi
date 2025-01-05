from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class CampaignLifecycleGoalErrorEnum(_message.Message):
    __slots__ = ()

    class CampaignLifecycleGoalError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[CampaignLifecycleGoalErrorEnum.CampaignLifecycleGoalError]
        UNKNOWN: _ClassVar[CampaignLifecycleGoalErrorEnum.CampaignLifecycleGoalError]
        CAMPAIGN_MISSING: _ClassVar[CampaignLifecycleGoalErrorEnum.CampaignLifecycleGoalError]
        INVALID_CAMPAIGN: _ClassVar[CampaignLifecycleGoalErrorEnum.CampaignLifecycleGoalError]
        CUSTOMER_ACQUISITION_INVALID_OPTIMIZATION_MODE: _ClassVar[CampaignLifecycleGoalErrorEnum.CampaignLifecycleGoalError]
        INCOMPATIBLE_BIDDING_STRATEGY: _ClassVar[CampaignLifecycleGoalErrorEnum.CampaignLifecycleGoalError]
        MISSING_PURCHASE_GOAL: _ClassVar[CampaignLifecycleGoalErrorEnum.CampaignLifecycleGoalError]
        CUSTOMER_ACQUISITION_INVALID_HIGH_LIFETIME_VALUE: _ClassVar[CampaignLifecycleGoalErrorEnum.CampaignLifecycleGoalError]
        CUSTOMER_ACQUISITION_UNSUPPORTED_CAMPAIGN_TYPE: _ClassVar[CampaignLifecycleGoalErrorEnum.CampaignLifecycleGoalError]
        CUSTOMER_ACQUISITION_INVALID_VALUE: _ClassVar[CampaignLifecycleGoalErrorEnum.CampaignLifecycleGoalError]
        CUSTOMER_ACQUISITION_VALUE_MISSING: _ClassVar[CampaignLifecycleGoalErrorEnum.CampaignLifecycleGoalError]
        CUSTOMER_ACQUISITION_MISSING_EXISTING_CUSTOMER_DEFINITION: _ClassVar[CampaignLifecycleGoalErrorEnum.CampaignLifecycleGoalError]
        CUSTOMER_ACQUISITION_MISSING_HIGH_VALUE_CUSTOMER_DEFINITION: _ClassVar[CampaignLifecycleGoalErrorEnum.CampaignLifecycleGoalError]
    UNSPECIFIED: CampaignLifecycleGoalErrorEnum.CampaignLifecycleGoalError
    UNKNOWN: CampaignLifecycleGoalErrorEnum.CampaignLifecycleGoalError
    CAMPAIGN_MISSING: CampaignLifecycleGoalErrorEnum.CampaignLifecycleGoalError
    INVALID_CAMPAIGN: CampaignLifecycleGoalErrorEnum.CampaignLifecycleGoalError
    CUSTOMER_ACQUISITION_INVALID_OPTIMIZATION_MODE: CampaignLifecycleGoalErrorEnum.CampaignLifecycleGoalError
    INCOMPATIBLE_BIDDING_STRATEGY: CampaignLifecycleGoalErrorEnum.CampaignLifecycleGoalError
    MISSING_PURCHASE_GOAL: CampaignLifecycleGoalErrorEnum.CampaignLifecycleGoalError
    CUSTOMER_ACQUISITION_INVALID_HIGH_LIFETIME_VALUE: CampaignLifecycleGoalErrorEnum.CampaignLifecycleGoalError
    CUSTOMER_ACQUISITION_UNSUPPORTED_CAMPAIGN_TYPE: CampaignLifecycleGoalErrorEnum.CampaignLifecycleGoalError
    CUSTOMER_ACQUISITION_INVALID_VALUE: CampaignLifecycleGoalErrorEnum.CampaignLifecycleGoalError
    CUSTOMER_ACQUISITION_VALUE_MISSING: CampaignLifecycleGoalErrorEnum.CampaignLifecycleGoalError
    CUSTOMER_ACQUISITION_MISSING_EXISTING_CUSTOMER_DEFINITION: CampaignLifecycleGoalErrorEnum.CampaignLifecycleGoalError
    CUSTOMER_ACQUISITION_MISSING_HIGH_VALUE_CUSTOMER_DEFINITION: CampaignLifecycleGoalErrorEnum.CampaignLifecycleGoalError

    def __init__(self) -> None:
        ...