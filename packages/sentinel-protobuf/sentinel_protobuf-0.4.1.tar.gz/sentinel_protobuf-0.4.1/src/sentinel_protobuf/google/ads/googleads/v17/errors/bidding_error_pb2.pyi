from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class BiddingErrorEnum(_message.Message):
    __slots__ = ()

    class BiddingError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[BiddingErrorEnum.BiddingError]
        UNKNOWN: _ClassVar[BiddingErrorEnum.BiddingError]
        BIDDING_STRATEGY_TRANSITION_NOT_ALLOWED: _ClassVar[BiddingErrorEnum.BiddingError]
        CANNOT_ATTACH_BIDDING_STRATEGY_TO_CAMPAIGN: _ClassVar[BiddingErrorEnum.BiddingError]
        INVALID_ANONYMOUS_BIDDING_STRATEGY_TYPE: _ClassVar[BiddingErrorEnum.BiddingError]
        INVALID_BIDDING_STRATEGY_TYPE: _ClassVar[BiddingErrorEnum.BiddingError]
        INVALID_BID: _ClassVar[BiddingErrorEnum.BiddingError]
        BIDDING_STRATEGY_NOT_AVAILABLE_FOR_ACCOUNT_TYPE: _ClassVar[BiddingErrorEnum.BiddingError]
        CANNOT_CREATE_CAMPAIGN_WITH_BIDDING_STRATEGY: _ClassVar[BiddingErrorEnum.BiddingError]
        CANNOT_TARGET_CONTENT_NETWORK_ONLY_WITH_CAMPAIGN_LEVEL_POP_BIDDING_STRATEGY: _ClassVar[BiddingErrorEnum.BiddingError]
        BIDDING_STRATEGY_NOT_SUPPORTED_WITH_AD_SCHEDULE: _ClassVar[BiddingErrorEnum.BiddingError]
        PAY_PER_CONVERSION_NOT_AVAILABLE_FOR_CUSTOMER: _ClassVar[BiddingErrorEnum.BiddingError]
        PAY_PER_CONVERSION_NOT_ALLOWED_WITH_TARGET_CPA: _ClassVar[BiddingErrorEnum.BiddingError]
        BIDDING_STRATEGY_NOT_ALLOWED_FOR_SEARCH_ONLY_CAMPAIGNS: _ClassVar[BiddingErrorEnum.BiddingError]
        BIDDING_STRATEGY_NOT_SUPPORTED_IN_DRAFTS_OR_EXPERIMENTS: _ClassVar[BiddingErrorEnum.BiddingError]
        BIDDING_STRATEGY_TYPE_DOES_NOT_SUPPORT_PRODUCT_TYPE_ADGROUP_CRITERION: _ClassVar[BiddingErrorEnum.BiddingError]
        BID_TOO_SMALL: _ClassVar[BiddingErrorEnum.BiddingError]
        BID_TOO_BIG: _ClassVar[BiddingErrorEnum.BiddingError]
        BID_TOO_MANY_FRACTIONAL_DIGITS: _ClassVar[BiddingErrorEnum.BiddingError]
        INVALID_DOMAIN_NAME: _ClassVar[BiddingErrorEnum.BiddingError]
        NOT_COMPATIBLE_WITH_PAYMENT_MODE: _ClassVar[BiddingErrorEnum.BiddingError]
        BIDDING_STRATEGY_TYPE_INCOMPATIBLE_WITH_SHARED_BUDGET: _ClassVar[BiddingErrorEnum.BiddingError]
        BIDDING_STRATEGY_AND_BUDGET_MUST_BE_ALIGNED: _ClassVar[BiddingErrorEnum.BiddingError]
        BIDDING_STRATEGY_AND_BUDGET_MUST_BE_ATTACHED_TO_THE_SAME_CAMPAIGNS_TO_ALIGN: _ClassVar[BiddingErrorEnum.BiddingError]
        BIDDING_STRATEGY_AND_BUDGET_MUST_BE_REMOVED_TOGETHER: _ClassVar[BiddingErrorEnum.BiddingError]
        CPC_BID_FLOOR_MICROS_GREATER_THAN_CPC_BID_CEILING_MICROS: _ClassVar[BiddingErrorEnum.BiddingError]
    UNSPECIFIED: BiddingErrorEnum.BiddingError
    UNKNOWN: BiddingErrorEnum.BiddingError
    BIDDING_STRATEGY_TRANSITION_NOT_ALLOWED: BiddingErrorEnum.BiddingError
    CANNOT_ATTACH_BIDDING_STRATEGY_TO_CAMPAIGN: BiddingErrorEnum.BiddingError
    INVALID_ANONYMOUS_BIDDING_STRATEGY_TYPE: BiddingErrorEnum.BiddingError
    INVALID_BIDDING_STRATEGY_TYPE: BiddingErrorEnum.BiddingError
    INVALID_BID: BiddingErrorEnum.BiddingError
    BIDDING_STRATEGY_NOT_AVAILABLE_FOR_ACCOUNT_TYPE: BiddingErrorEnum.BiddingError
    CANNOT_CREATE_CAMPAIGN_WITH_BIDDING_STRATEGY: BiddingErrorEnum.BiddingError
    CANNOT_TARGET_CONTENT_NETWORK_ONLY_WITH_CAMPAIGN_LEVEL_POP_BIDDING_STRATEGY: BiddingErrorEnum.BiddingError
    BIDDING_STRATEGY_NOT_SUPPORTED_WITH_AD_SCHEDULE: BiddingErrorEnum.BiddingError
    PAY_PER_CONVERSION_NOT_AVAILABLE_FOR_CUSTOMER: BiddingErrorEnum.BiddingError
    PAY_PER_CONVERSION_NOT_ALLOWED_WITH_TARGET_CPA: BiddingErrorEnum.BiddingError
    BIDDING_STRATEGY_NOT_ALLOWED_FOR_SEARCH_ONLY_CAMPAIGNS: BiddingErrorEnum.BiddingError
    BIDDING_STRATEGY_NOT_SUPPORTED_IN_DRAFTS_OR_EXPERIMENTS: BiddingErrorEnum.BiddingError
    BIDDING_STRATEGY_TYPE_DOES_NOT_SUPPORT_PRODUCT_TYPE_ADGROUP_CRITERION: BiddingErrorEnum.BiddingError
    BID_TOO_SMALL: BiddingErrorEnum.BiddingError
    BID_TOO_BIG: BiddingErrorEnum.BiddingError
    BID_TOO_MANY_FRACTIONAL_DIGITS: BiddingErrorEnum.BiddingError
    INVALID_DOMAIN_NAME: BiddingErrorEnum.BiddingError
    NOT_COMPATIBLE_WITH_PAYMENT_MODE: BiddingErrorEnum.BiddingError
    BIDDING_STRATEGY_TYPE_INCOMPATIBLE_WITH_SHARED_BUDGET: BiddingErrorEnum.BiddingError
    BIDDING_STRATEGY_AND_BUDGET_MUST_BE_ALIGNED: BiddingErrorEnum.BiddingError
    BIDDING_STRATEGY_AND_BUDGET_MUST_BE_ATTACHED_TO_THE_SAME_CAMPAIGNS_TO_ALIGN: BiddingErrorEnum.BiddingError
    BIDDING_STRATEGY_AND_BUDGET_MUST_BE_REMOVED_TOGETHER: BiddingErrorEnum.BiddingError
    CPC_BID_FLOOR_MICROS_GREATER_THAN_CPC_BID_CEILING_MICROS: BiddingErrorEnum.BiddingError

    def __init__(self) -> None:
        ...