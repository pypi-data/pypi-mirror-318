from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class RecommendationErrorEnum(_message.Message):
    __slots__ = ()

    class RecommendationError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[RecommendationErrorEnum.RecommendationError]
        UNKNOWN: _ClassVar[RecommendationErrorEnum.RecommendationError]
        BUDGET_AMOUNT_TOO_SMALL: _ClassVar[RecommendationErrorEnum.RecommendationError]
        BUDGET_AMOUNT_TOO_LARGE: _ClassVar[RecommendationErrorEnum.RecommendationError]
        INVALID_BUDGET_AMOUNT: _ClassVar[RecommendationErrorEnum.RecommendationError]
        POLICY_ERROR: _ClassVar[RecommendationErrorEnum.RecommendationError]
        INVALID_BID_AMOUNT: _ClassVar[RecommendationErrorEnum.RecommendationError]
        ADGROUP_KEYWORD_LIMIT: _ClassVar[RecommendationErrorEnum.RecommendationError]
        RECOMMENDATION_ALREADY_APPLIED: _ClassVar[RecommendationErrorEnum.RecommendationError]
        RECOMMENDATION_INVALIDATED: _ClassVar[RecommendationErrorEnum.RecommendationError]
        TOO_MANY_OPERATIONS: _ClassVar[RecommendationErrorEnum.RecommendationError]
        NO_OPERATIONS: _ClassVar[RecommendationErrorEnum.RecommendationError]
        DIFFERENT_TYPES_NOT_SUPPORTED: _ClassVar[RecommendationErrorEnum.RecommendationError]
        DUPLICATE_RESOURCE_NAME: _ClassVar[RecommendationErrorEnum.RecommendationError]
        RECOMMENDATION_ALREADY_DISMISSED: _ClassVar[RecommendationErrorEnum.RecommendationError]
        INVALID_APPLY_REQUEST: _ClassVar[RecommendationErrorEnum.RecommendationError]
        RECOMMENDATION_TYPE_APPLY_NOT_SUPPORTED: _ClassVar[RecommendationErrorEnum.RecommendationError]
        INVALID_MULTIPLIER: _ClassVar[RecommendationErrorEnum.RecommendationError]
        ADVERTISING_CHANNEL_TYPE_GENERATE_NOT_SUPPORTED: _ClassVar[RecommendationErrorEnum.RecommendationError]
        RECOMMENDATION_TYPE_GENERATE_NOT_SUPPORTED: _ClassVar[RecommendationErrorEnum.RecommendationError]
        RECOMMENDATION_TYPES_CANNOT_BE_EMPTY: _ClassVar[RecommendationErrorEnum.RecommendationError]
        CAMPAIGN_BUDGET_RECOMMENDATION_TYPE_REQUIRES_BIDDING_INFO: _ClassVar[RecommendationErrorEnum.RecommendationError]
        CAMPAIGN_BUDGET_RECOMMENDATION_TYPE_REQUIRES_BIDDING_STRATEGY_TYPE: _ClassVar[RecommendationErrorEnum.RecommendationError]
        CAMPAIGN_BUDGET_RECOMMENDATION_TYPE_REQUIRES_ASSET_GROUP_INFO: _ClassVar[RecommendationErrorEnum.RecommendationError]
        CAMPAIGN_BUDGET_RECOMMENDATION_TYPE_REQUIRES_ASSET_GROUP_INFO_WITH_FINAL_URL: _ClassVar[RecommendationErrorEnum.RecommendationError]
        CAMPAIGN_BUDGET_RECOMMENDATION_TYPE_REQUIRES_COUNTRY_CODES_FOR_SEARCH_CHANNEL: _ClassVar[RecommendationErrorEnum.RecommendationError]
        CAMPAIGN_BUDGET_RECOMMENDATION_TYPE_INVALID_COUNTRY_CODE_FOR_SEARCH_CHANNEL: _ClassVar[RecommendationErrorEnum.RecommendationError]
        CAMPAIGN_BUDGET_RECOMMENDATION_TYPE_REQUIRES_LANGUAGE_CODES_FOR_SEARCH_CHANNEL: _ClassVar[RecommendationErrorEnum.RecommendationError]
        CAMPAIGN_BUDGET_RECOMMENDATION_TYPE_REQUIRES_EITHER_POSITIVE_OR_NEGATIVE_LOCATION_IDS_FOR_SEARCH_CHANNEL: _ClassVar[RecommendationErrorEnum.RecommendationError]
        CAMPAIGN_BUDGET_RECOMMENDATION_TYPE_REQUIRES_AD_GROUP_INFO_FOR_SEARCH_CHANNEL: _ClassVar[RecommendationErrorEnum.RecommendationError]
        CAMPAIGN_BUDGET_RECOMMENDATION_TYPE_REQUIRES_KEYWORDS_FOR_SEARCH_CHANNEL: _ClassVar[RecommendationErrorEnum.RecommendationError]
        CAMPAIGN_BUDGET_RECOMMENDATION_TYPE_WITH_CHANNEL_TYPE_SEARCH_AND_BIDDING_STRATEGY_TYPE_TARGET_IMPRESSION_SHARE_REQUIRES_LOCATION: _ClassVar[RecommendationErrorEnum.RecommendationError]
        CAMPAIGN_BUDGET_RECOMMENDATION_TYPE_WITH_CHANNEL_TYPE_SEARCH_AND_BIDDING_STRATEGY_TYPE_TARGET_IMPRESSION_SHARE_REQUIRES_TARGET_IMPRESSION_SHARE_MICROS: _ClassVar[RecommendationErrorEnum.RecommendationError]
        CAMPAIGN_BUDGET_RECOMMENDATION_TYPE_TARGET_IMPRESSION_SHARE_MICROS_BETWEEN_1_AND_1000000: _ClassVar[RecommendationErrorEnum.RecommendationError]
        CAMPAIGN_BUDGET_RECOMMENDATION_TYPE_WITH_CHANNEL_TYPE_SEARCH_AND_BIDDING_STRATEGY_TYPE_TARGET_IMPRESSION_SHARE_REQUIRES_TARGET_IMPRESSION_SHARE_INFO: _ClassVar[RecommendationErrorEnum.RecommendationError]
    UNSPECIFIED: RecommendationErrorEnum.RecommendationError
    UNKNOWN: RecommendationErrorEnum.RecommendationError
    BUDGET_AMOUNT_TOO_SMALL: RecommendationErrorEnum.RecommendationError
    BUDGET_AMOUNT_TOO_LARGE: RecommendationErrorEnum.RecommendationError
    INVALID_BUDGET_AMOUNT: RecommendationErrorEnum.RecommendationError
    POLICY_ERROR: RecommendationErrorEnum.RecommendationError
    INVALID_BID_AMOUNT: RecommendationErrorEnum.RecommendationError
    ADGROUP_KEYWORD_LIMIT: RecommendationErrorEnum.RecommendationError
    RECOMMENDATION_ALREADY_APPLIED: RecommendationErrorEnum.RecommendationError
    RECOMMENDATION_INVALIDATED: RecommendationErrorEnum.RecommendationError
    TOO_MANY_OPERATIONS: RecommendationErrorEnum.RecommendationError
    NO_OPERATIONS: RecommendationErrorEnum.RecommendationError
    DIFFERENT_TYPES_NOT_SUPPORTED: RecommendationErrorEnum.RecommendationError
    DUPLICATE_RESOURCE_NAME: RecommendationErrorEnum.RecommendationError
    RECOMMENDATION_ALREADY_DISMISSED: RecommendationErrorEnum.RecommendationError
    INVALID_APPLY_REQUEST: RecommendationErrorEnum.RecommendationError
    RECOMMENDATION_TYPE_APPLY_NOT_SUPPORTED: RecommendationErrorEnum.RecommendationError
    INVALID_MULTIPLIER: RecommendationErrorEnum.RecommendationError
    ADVERTISING_CHANNEL_TYPE_GENERATE_NOT_SUPPORTED: RecommendationErrorEnum.RecommendationError
    RECOMMENDATION_TYPE_GENERATE_NOT_SUPPORTED: RecommendationErrorEnum.RecommendationError
    RECOMMENDATION_TYPES_CANNOT_BE_EMPTY: RecommendationErrorEnum.RecommendationError
    CAMPAIGN_BUDGET_RECOMMENDATION_TYPE_REQUIRES_BIDDING_INFO: RecommendationErrorEnum.RecommendationError
    CAMPAIGN_BUDGET_RECOMMENDATION_TYPE_REQUIRES_BIDDING_STRATEGY_TYPE: RecommendationErrorEnum.RecommendationError
    CAMPAIGN_BUDGET_RECOMMENDATION_TYPE_REQUIRES_ASSET_GROUP_INFO: RecommendationErrorEnum.RecommendationError
    CAMPAIGN_BUDGET_RECOMMENDATION_TYPE_REQUIRES_ASSET_GROUP_INFO_WITH_FINAL_URL: RecommendationErrorEnum.RecommendationError
    CAMPAIGN_BUDGET_RECOMMENDATION_TYPE_REQUIRES_COUNTRY_CODES_FOR_SEARCH_CHANNEL: RecommendationErrorEnum.RecommendationError
    CAMPAIGN_BUDGET_RECOMMENDATION_TYPE_INVALID_COUNTRY_CODE_FOR_SEARCH_CHANNEL: RecommendationErrorEnum.RecommendationError
    CAMPAIGN_BUDGET_RECOMMENDATION_TYPE_REQUIRES_LANGUAGE_CODES_FOR_SEARCH_CHANNEL: RecommendationErrorEnum.RecommendationError
    CAMPAIGN_BUDGET_RECOMMENDATION_TYPE_REQUIRES_EITHER_POSITIVE_OR_NEGATIVE_LOCATION_IDS_FOR_SEARCH_CHANNEL: RecommendationErrorEnum.RecommendationError
    CAMPAIGN_BUDGET_RECOMMENDATION_TYPE_REQUIRES_AD_GROUP_INFO_FOR_SEARCH_CHANNEL: RecommendationErrorEnum.RecommendationError
    CAMPAIGN_BUDGET_RECOMMENDATION_TYPE_REQUIRES_KEYWORDS_FOR_SEARCH_CHANNEL: RecommendationErrorEnum.RecommendationError
    CAMPAIGN_BUDGET_RECOMMENDATION_TYPE_WITH_CHANNEL_TYPE_SEARCH_AND_BIDDING_STRATEGY_TYPE_TARGET_IMPRESSION_SHARE_REQUIRES_LOCATION: RecommendationErrorEnum.RecommendationError
    CAMPAIGN_BUDGET_RECOMMENDATION_TYPE_WITH_CHANNEL_TYPE_SEARCH_AND_BIDDING_STRATEGY_TYPE_TARGET_IMPRESSION_SHARE_REQUIRES_TARGET_IMPRESSION_SHARE_MICROS: RecommendationErrorEnum.RecommendationError
    CAMPAIGN_BUDGET_RECOMMENDATION_TYPE_TARGET_IMPRESSION_SHARE_MICROS_BETWEEN_1_AND_1000000: RecommendationErrorEnum.RecommendationError
    CAMPAIGN_BUDGET_RECOMMENDATION_TYPE_WITH_CHANNEL_TYPE_SEARCH_AND_BIDDING_STRATEGY_TYPE_TARGET_IMPRESSION_SHARE_REQUIRES_TARGET_IMPRESSION_SHARE_INFO: RecommendationErrorEnum.RecommendationError

    def __init__(self) -> None:
        ...