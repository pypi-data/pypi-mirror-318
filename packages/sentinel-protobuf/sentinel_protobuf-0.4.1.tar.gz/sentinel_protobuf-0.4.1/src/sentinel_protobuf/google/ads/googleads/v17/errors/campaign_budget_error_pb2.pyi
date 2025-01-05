from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class CampaignBudgetErrorEnum(_message.Message):
    __slots__ = ()

    class CampaignBudgetError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[CampaignBudgetErrorEnum.CampaignBudgetError]
        UNKNOWN: _ClassVar[CampaignBudgetErrorEnum.CampaignBudgetError]
        CAMPAIGN_BUDGET_CANNOT_BE_SHARED: _ClassVar[CampaignBudgetErrorEnum.CampaignBudgetError]
        CAMPAIGN_BUDGET_REMOVED: _ClassVar[CampaignBudgetErrorEnum.CampaignBudgetError]
        CAMPAIGN_BUDGET_IN_USE: _ClassVar[CampaignBudgetErrorEnum.CampaignBudgetError]
        CAMPAIGN_BUDGET_PERIOD_NOT_AVAILABLE: _ClassVar[CampaignBudgetErrorEnum.CampaignBudgetError]
        CANNOT_MODIFY_FIELD_OF_IMPLICITLY_SHARED_CAMPAIGN_BUDGET: _ClassVar[CampaignBudgetErrorEnum.CampaignBudgetError]
        CANNOT_UPDATE_CAMPAIGN_BUDGET_TO_IMPLICITLY_SHARED: _ClassVar[CampaignBudgetErrorEnum.CampaignBudgetError]
        CANNOT_UPDATE_CAMPAIGN_BUDGET_TO_EXPLICITLY_SHARED_WITHOUT_NAME: _ClassVar[CampaignBudgetErrorEnum.CampaignBudgetError]
        CANNOT_UPDATE_CAMPAIGN_BUDGET_TO_EXPLICITLY_SHARED: _ClassVar[CampaignBudgetErrorEnum.CampaignBudgetError]
        CANNOT_USE_IMPLICITLY_SHARED_CAMPAIGN_BUDGET_WITH_MULTIPLE_CAMPAIGNS: _ClassVar[CampaignBudgetErrorEnum.CampaignBudgetError]
        DUPLICATE_NAME: _ClassVar[CampaignBudgetErrorEnum.CampaignBudgetError]
        MONEY_AMOUNT_IN_WRONG_CURRENCY: _ClassVar[CampaignBudgetErrorEnum.CampaignBudgetError]
        MONEY_AMOUNT_LESS_THAN_CURRENCY_MINIMUM_CPC: _ClassVar[CampaignBudgetErrorEnum.CampaignBudgetError]
        MONEY_AMOUNT_TOO_LARGE: _ClassVar[CampaignBudgetErrorEnum.CampaignBudgetError]
        NEGATIVE_MONEY_AMOUNT: _ClassVar[CampaignBudgetErrorEnum.CampaignBudgetError]
        NON_MULTIPLE_OF_MINIMUM_CURRENCY_UNIT: _ClassVar[CampaignBudgetErrorEnum.CampaignBudgetError]
        TOTAL_BUDGET_AMOUNT_MUST_BE_UNSET_FOR_BUDGET_PERIOD_DAILY: _ClassVar[CampaignBudgetErrorEnum.CampaignBudgetError]
        INVALID_PERIOD: _ClassVar[CampaignBudgetErrorEnum.CampaignBudgetError]
        CANNOT_USE_ACCELERATED_DELIVERY_MODE: _ClassVar[CampaignBudgetErrorEnum.CampaignBudgetError]
        BUDGET_AMOUNT_MUST_BE_UNSET_FOR_CUSTOM_BUDGET_PERIOD: _ClassVar[CampaignBudgetErrorEnum.CampaignBudgetError]
    UNSPECIFIED: CampaignBudgetErrorEnum.CampaignBudgetError
    UNKNOWN: CampaignBudgetErrorEnum.CampaignBudgetError
    CAMPAIGN_BUDGET_CANNOT_BE_SHARED: CampaignBudgetErrorEnum.CampaignBudgetError
    CAMPAIGN_BUDGET_REMOVED: CampaignBudgetErrorEnum.CampaignBudgetError
    CAMPAIGN_BUDGET_IN_USE: CampaignBudgetErrorEnum.CampaignBudgetError
    CAMPAIGN_BUDGET_PERIOD_NOT_AVAILABLE: CampaignBudgetErrorEnum.CampaignBudgetError
    CANNOT_MODIFY_FIELD_OF_IMPLICITLY_SHARED_CAMPAIGN_BUDGET: CampaignBudgetErrorEnum.CampaignBudgetError
    CANNOT_UPDATE_CAMPAIGN_BUDGET_TO_IMPLICITLY_SHARED: CampaignBudgetErrorEnum.CampaignBudgetError
    CANNOT_UPDATE_CAMPAIGN_BUDGET_TO_EXPLICITLY_SHARED_WITHOUT_NAME: CampaignBudgetErrorEnum.CampaignBudgetError
    CANNOT_UPDATE_CAMPAIGN_BUDGET_TO_EXPLICITLY_SHARED: CampaignBudgetErrorEnum.CampaignBudgetError
    CANNOT_USE_IMPLICITLY_SHARED_CAMPAIGN_BUDGET_WITH_MULTIPLE_CAMPAIGNS: CampaignBudgetErrorEnum.CampaignBudgetError
    DUPLICATE_NAME: CampaignBudgetErrorEnum.CampaignBudgetError
    MONEY_AMOUNT_IN_WRONG_CURRENCY: CampaignBudgetErrorEnum.CampaignBudgetError
    MONEY_AMOUNT_LESS_THAN_CURRENCY_MINIMUM_CPC: CampaignBudgetErrorEnum.CampaignBudgetError
    MONEY_AMOUNT_TOO_LARGE: CampaignBudgetErrorEnum.CampaignBudgetError
    NEGATIVE_MONEY_AMOUNT: CampaignBudgetErrorEnum.CampaignBudgetError
    NON_MULTIPLE_OF_MINIMUM_CURRENCY_UNIT: CampaignBudgetErrorEnum.CampaignBudgetError
    TOTAL_BUDGET_AMOUNT_MUST_BE_UNSET_FOR_BUDGET_PERIOD_DAILY: CampaignBudgetErrorEnum.CampaignBudgetError
    INVALID_PERIOD: CampaignBudgetErrorEnum.CampaignBudgetError
    CANNOT_USE_ACCELERATED_DELIVERY_MODE: CampaignBudgetErrorEnum.CampaignBudgetError
    BUDGET_AMOUNT_MUST_BE_UNSET_FOR_CUSTOM_BUDGET_PERIOD: CampaignBudgetErrorEnum.CampaignBudgetError

    def __init__(self) -> None:
        ...