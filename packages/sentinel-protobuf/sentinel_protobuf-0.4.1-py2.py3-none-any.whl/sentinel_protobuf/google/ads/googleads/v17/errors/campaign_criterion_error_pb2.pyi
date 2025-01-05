from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class CampaignCriterionErrorEnum(_message.Message):
    __slots__ = ()

    class CampaignCriterionError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[CampaignCriterionErrorEnum.CampaignCriterionError]
        UNKNOWN: _ClassVar[CampaignCriterionErrorEnum.CampaignCriterionError]
        CONCRETE_TYPE_REQUIRED: _ClassVar[CampaignCriterionErrorEnum.CampaignCriterionError]
        INVALID_PLACEMENT_URL: _ClassVar[CampaignCriterionErrorEnum.CampaignCriterionError]
        CANNOT_EXCLUDE_CRITERIA_TYPE: _ClassVar[CampaignCriterionErrorEnum.CampaignCriterionError]
        CANNOT_SET_STATUS_FOR_CRITERIA_TYPE: _ClassVar[CampaignCriterionErrorEnum.CampaignCriterionError]
        CANNOT_SET_STATUS_FOR_EXCLUDED_CRITERIA: _ClassVar[CampaignCriterionErrorEnum.CampaignCriterionError]
        CANNOT_TARGET_AND_EXCLUDE: _ClassVar[CampaignCriterionErrorEnum.CampaignCriterionError]
        TOO_MANY_OPERATIONS: _ClassVar[CampaignCriterionErrorEnum.CampaignCriterionError]
        OPERATOR_NOT_SUPPORTED_FOR_CRITERION_TYPE: _ClassVar[CampaignCriterionErrorEnum.CampaignCriterionError]
        SHOPPING_CAMPAIGN_SALES_COUNTRY_NOT_SUPPORTED_FOR_SALES_CHANNEL: _ClassVar[CampaignCriterionErrorEnum.CampaignCriterionError]
        CANNOT_ADD_EXISTING_FIELD: _ClassVar[CampaignCriterionErrorEnum.CampaignCriterionError]
        CANNOT_UPDATE_NEGATIVE_CRITERION: _ClassVar[CampaignCriterionErrorEnum.CampaignCriterionError]
        CANNOT_SET_NEGATIVE_KEYWORD_THEME_CONSTANT_CRITERION: _ClassVar[CampaignCriterionErrorEnum.CampaignCriterionError]
        INVALID_KEYWORD_THEME_CONSTANT: _ClassVar[CampaignCriterionErrorEnum.CampaignCriterionError]
        MISSING_KEYWORD_THEME_CONSTANT_OR_FREE_FORM_KEYWORD_THEME: _ClassVar[CampaignCriterionErrorEnum.CampaignCriterionError]
        CANNOT_TARGET_BOTH_PROXIMITY_AND_LOCATION_CRITERIA_FOR_SMART_CAMPAIGN: _ClassVar[CampaignCriterionErrorEnum.CampaignCriterionError]
        CANNOT_TARGET_MULTIPLE_PROXIMITY_CRITERIA_FOR_SMART_CAMPAIGN: _ClassVar[CampaignCriterionErrorEnum.CampaignCriterionError]
        LOCATION_NOT_LAUNCHED_FOR_LOCAL_SERVICES_CAMPAIGN: _ClassVar[CampaignCriterionErrorEnum.CampaignCriterionError]
        LOCATION_INVALID_FOR_LOCAL_SERVICES_CAMPAIGN: _ClassVar[CampaignCriterionErrorEnum.CampaignCriterionError]
        CANNOT_TARGET_COUNTRY_FOR_LOCAL_SERVICES_CAMPAIGN: _ClassVar[CampaignCriterionErrorEnum.CampaignCriterionError]
        LOCATION_NOT_IN_HOME_COUNTRY_FOR_LOCAL_SERVICES_CAMPAIGN: _ClassVar[CampaignCriterionErrorEnum.CampaignCriterionError]
        CANNOT_ADD_OR_REMOVE_LOCATION_FOR_LOCAL_SERVICES_CAMPAIGN: _ClassVar[CampaignCriterionErrorEnum.CampaignCriterionError]
        AT_LEAST_ONE_POSITIVE_LOCATION_REQUIRED_FOR_LOCAL_SERVICES_CAMPAIGN: _ClassVar[CampaignCriterionErrorEnum.CampaignCriterionError]
        AT_LEAST_ONE_LOCAL_SERVICE_ID_CRITERION_REQUIRED_FOR_LOCAL_SERVICES_CAMPAIGN: _ClassVar[CampaignCriterionErrorEnum.CampaignCriterionError]
        LOCAL_SERVICE_ID_NOT_FOUND_FOR_CATEGORY: _ClassVar[CampaignCriterionErrorEnum.CampaignCriterionError]
        CANNOT_ATTACH_BRAND_LIST_TO_NON_QUALIFIED_SEARCH_CAMPAIGN: _ClassVar[CampaignCriterionErrorEnum.CampaignCriterionError]
        CANNOT_REMOVE_ALL_LOCATIONS_DUE_TO_TOO_MANY_COUNTRY_EXCLUSIONS: _ClassVar[CampaignCriterionErrorEnum.CampaignCriterionError]
    UNSPECIFIED: CampaignCriterionErrorEnum.CampaignCriterionError
    UNKNOWN: CampaignCriterionErrorEnum.CampaignCriterionError
    CONCRETE_TYPE_REQUIRED: CampaignCriterionErrorEnum.CampaignCriterionError
    INVALID_PLACEMENT_URL: CampaignCriterionErrorEnum.CampaignCriterionError
    CANNOT_EXCLUDE_CRITERIA_TYPE: CampaignCriterionErrorEnum.CampaignCriterionError
    CANNOT_SET_STATUS_FOR_CRITERIA_TYPE: CampaignCriterionErrorEnum.CampaignCriterionError
    CANNOT_SET_STATUS_FOR_EXCLUDED_CRITERIA: CampaignCriterionErrorEnum.CampaignCriterionError
    CANNOT_TARGET_AND_EXCLUDE: CampaignCriterionErrorEnum.CampaignCriterionError
    TOO_MANY_OPERATIONS: CampaignCriterionErrorEnum.CampaignCriterionError
    OPERATOR_NOT_SUPPORTED_FOR_CRITERION_TYPE: CampaignCriterionErrorEnum.CampaignCriterionError
    SHOPPING_CAMPAIGN_SALES_COUNTRY_NOT_SUPPORTED_FOR_SALES_CHANNEL: CampaignCriterionErrorEnum.CampaignCriterionError
    CANNOT_ADD_EXISTING_FIELD: CampaignCriterionErrorEnum.CampaignCriterionError
    CANNOT_UPDATE_NEGATIVE_CRITERION: CampaignCriterionErrorEnum.CampaignCriterionError
    CANNOT_SET_NEGATIVE_KEYWORD_THEME_CONSTANT_CRITERION: CampaignCriterionErrorEnum.CampaignCriterionError
    INVALID_KEYWORD_THEME_CONSTANT: CampaignCriterionErrorEnum.CampaignCriterionError
    MISSING_KEYWORD_THEME_CONSTANT_OR_FREE_FORM_KEYWORD_THEME: CampaignCriterionErrorEnum.CampaignCriterionError
    CANNOT_TARGET_BOTH_PROXIMITY_AND_LOCATION_CRITERIA_FOR_SMART_CAMPAIGN: CampaignCriterionErrorEnum.CampaignCriterionError
    CANNOT_TARGET_MULTIPLE_PROXIMITY_CRITERIA_FOR_SMART_CAMPAIGN: CampaignCriterionErrorEnum.CampaignCriterionError
    LOCATION_NOT_LAUNCHED_FOR_LOCAL_SERVICES_CAMPAIGN: CampaignCriterionErrorEnum.CampaignCriterionError
    LOCATION_INVALID_FOR_LOCAL_SERVICES_CAMPAIGN: CampaignCriterionErrorEnum.CampaignCriterionError
    CANNOT_TARGET_COUNTRY_FOR_LOCAL_SERVICES_CAMPAIGN: CampaignCriterionErrorEnum.CampaignCriterionError
    LOCATION_NOT_IN_HOME_COUNTRY_FOR_LOCAL_SERVICES_CAMPAIGN: CampaignCriterionErrorEnum.CampaignCriterionError
    CANNOT_ADD_OR_REMOVE_LOCATION_FOR_LOCAL_SERVICES_CAMPAIGN: CampaignCriterionErrorEnum.CampaignCriterionError
    AT_LEAST_ONE_POSITIVE_LOCATION_REQUIRED_FOR_LOCAL_SERVICES_CAMPAIGN: CampaignCriterionErrorEnum.CampaignCriterionError
    AT_LEAST_ONE_LOCAL_SERVICE_ID_CRITERION_REQUIRED_FOR_LOCAL_SERVICES_CAMPAIGN: CampaignCriterionErrorEnum.CampaignCriterionError
    LOCAL_SERVICE_ID_NOT_FOUND_FOR_CATEGORY: CampaignCriterionErrorEnum.CampaignCriterionError
    CANNOT_ATTACH_BRAND_LIST_TO_NON_QUALIFIED_SEARCH_CAMPAIGN: CampaignCriterionErrorEnum.CampaignCriterionError
    CANNOT_REMOVE_ALL_LOCATIONS_DUE_TO_TOO_MANY_COUNTRY_EXCLUSIONS: CampaignCriterionErrorEnum.CampaignCriterionError

    def __init__(self) -> None:
        ...