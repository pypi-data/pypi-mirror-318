from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class AdGroupCriterionErrorEnum(_message.Message):
    __slots__ = ()

    class AdGroupCriterionError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[AdGroupCriterionErrorEnum.AdGroupCriterionError]
        UNKNOWN: _ClassVar[AdGroupCriterionErrorEnum.AdGroupCriterionError]
        AD_GROUP_CRITERION_LABEL_DOES_NOT_EXIST: _ClassVar[AdGroupCriterionErrorEnum.AdGroupCriterionError]
        AD_GROUP_CRITERION_LABEL_ALREADY_EXISTS: _ClassVar[AdGroupCriterionErrorEnum.AdGroupCriterionError]
        CANNOT_ADD_LABEL_TO_NEGATIVE_CRITERION: _ClassVar[AdGroupCriterionErrorEnum.AdGroupCriterionError]
        TOO_MANY_OPERATIONS: _ClassVar[AdGroupCriterionErrorEnum.AdGroupCriterionError]
        CANT_UPDATE_NEGATIVE: _ClassVar[AdGroupCriterionErrorEnum.AdGroupCriterionError]
        CONCRETE_TYPE_REQUIRED: _ClassVar[AdGroupCriterionErrorEnum.AdGroupCriterionError]
        BID_INCOMPATIBLE_WITH_ADGROUP: _ClassVar[AdGroupCriterionErrorEnum.AdGroupCriterionError]
        CANNOT_TARGET_AND_EXCLUDE: _ClassVar[AdGroupCriterionErrorEnum.AdGroupCriterionError]
        ILLEGAL_URL: _ClassVar[AdGroupCriterionErrorEnum.AdGroupCriterionError]
        INVALID_KEYWORD_TEXT: _ClassVar[AdGroupCriterionErrorEnum.AdGroupCriterionError]
        INVALID_DESTINATION_URL: _ClassVar[AdGroupCriterionErrorEnum.AdGroupCriterionError]
        MISSING_DESTINATION_URL_TAG: _ClassVar[AdGroupCriterionErrorEnum.AdGroupCriterionError]
        KEYWORD_LEVEL_BID_NOT_SUPPORTED_FOR_MANUALCPM: _ClassVar[AdGroupCriterionErrorEnum.AdGroupCriterionError]
        INVALID_USER_STATUS: _ClassVar[AdGroupCriterionErrorEnum.AdGroupCriterionError]
        CANNOT_ADD_CRITERIA_TYPE: _ClassVar[AdGroupCriterionErrorEnum.AdGroupCriterionError]
        CANNOT_EXCLUDE_CRITERIA_TYPE: _ClassVar[AdGroupCriterionErrorEnum.AdGroupCriterionError]
        CAMPAIGN_TYPE_NOT_COMPATIBLE_WITH_PARTIAL_FAILURE: _ClassVar[AdGroupCriterionErrorEnum.AdGroupCriterionError]
        OPERATIONS_FOR_TOO_MANY_SHOPPING_ADGROUPS: _ClassVar[AdGroupCriterionErrorEnum.AdGroupCriterionError]
        CANNOT_MODIFY_URL_FIELDS_WITH_DUPLICATE_ELEMENTS: _ClassVar[AdGroupCriterionErrorEnum.AdGroupCriterionError]
        CANNOT_SET_WITHOUT_FINAL_URLS: _ClassVar[AdGroupCriterionErrorEnum.AdGroupCriterionError]
        CANNOT_CLEAR_FINAL_URLS_IF_FINAL_MOBILE_URLS_EXIST: _ClassVar[AdGroupCriterionErrorEnum.AdGroupCriterionError]
        CANNOT_CLEAR_FINAL_URLS_IF_FINAL_APP_URLS_EXIST: _ClassVar[AdGroupCriterionErrorEnum.AdGroupCriterionError]
        CANNOT_CLEAR_FINAL_URLS_IF_TRACKING_URL_TEMPLATE_EXISTS: _ClassVar[AdGroupCriterionErrorEnum.AdGroupCriterionError]
        CANNOT_CLEAR_FINAL_URLS_IF_URL_CUSTOM_PARAMETERS_EXIST: _ClassVar[AdGroupCriterionErrorEnum.AdGroupCriterionError]
        CANNOT_SET_BOTH_DESTINATION_URL_AND_FINAL_URLS: _ClassVar[AdGroupCriterionErrorEnum.AdGroupCriterionError]
        CANNOT_SET_BOTH_DESTINATION_URL_AND_TRACKING_URL_TEMPLATE: _ClassVar[AdGroupCriterionErrorEnum.AdGroupCriterionError]
        FINAL_URLS_NOT_SUPPORTED_FOR_CRITERION_TYPE: _ClassVar[AdGroupCriterionErrorEnum.AdGroupCriterionError]
        FINAL_MOBILE_URLS_NOT_SUPPORTED_FOR_CRITERION_TYPE: _ClassVar[AdGroupCriterionErrorEnum.AdGroupCriterionError]
    UNSPECIFIED: AdGroupCriterionErrorEnum.AdGroupCriterionError
    UNKNOWN: AdGroupCriterionErrorEnum.AdGroupCriterionError
    AD_GROUP_CRITERION_LABEL_DOES_NOT_EXIST: AdGroupCriterionErrorEnum.AdGroupCriterionError
    AD_GROUP_CRITERION_LABEL_ALREADY_EXISTS: AdGroupCriterionErrorEnum.AdGroupCriterionError
    CANNOT_ADD_LABEL_TO_NEGATIVE_CRITERION: AdGroupCriterionErrorEnum.AdGroupCriterionError
    TOO_MANY_OPERATIONS: AdGroupCriterionErrorEnum.AdGroupCriterionError
    CANT_UPDATE_NEGATIVE: AdGroupCriterionErrorEnum.AdGroupCriterionError
    CONCRETE_TYPE_REQUIRED: AdGroupCriterionErrorEnum.AdGroupCriterionError
    BID_INCOMPATIBLE_WITH_ADGROUP: AdGroupCriterionErrorEnum.AdGroupCriterionError
    CANNOT_TARGET_AND_EXCLUDE: AdGroupCriterionErrorEnum.AdGroupCriterionError
    ILLEGAL_URL: AdGroupCriterionErrorEnum.AdGroupCriterionError
    INVALID_KEYWORD_TEXT: AdGroupCriterionErrorEnum.AdGroupCriterionError
    INVALID_DESTINATION_URL: AdGroupCriterionErrorEnum.AdGroupCriterionError
    MISSING_DESTINATION_URL_TAG: AdGroupCriterionErrorEnum.AdGroupCriterionError
    KEYWORD_LEVEL_BID_NOT_SUPPORTED_FOR_MANUALCPM: AdGroupCriterionErrorEnum.AdGroupCriterionError
    INVALID_USER_STATUS: AdGroupCriterionErrorEnum.AdGroupCriterionError
    CANNOT_ADD_CRITERIA_TYPE: AdGroupCriterionErrorEnum.AdGroupCriterionError
    CANNOT_EXCLUDE_CRITERIA_TYPE: AdGroupCriterionErrorEnum.AdGroupCriterionError
    CAMPAIGN_TYPE_NOT_COMPATIBLE_WITH_PARTIAL_FAILURE: AdGroupCriterionErrorEnum.AdGroupCriterionError
    OPERATIONS_FOR_TOO_MANY_SHOPPING_ADGROUPS: AdGroupCriterionErrorEnum.AdGroupCriterionError
    CANNOT_MODIFY_URL_FIELDS_WITH_DUPLICATE_ELEMENTS: AdGroupCriterionErrorEnum.AdGroupCriterionError
    CANNOT_SET_WITHOUT_FINAL_URLS: AdGroupCriterionErrorEnum.AdGroupCriterionError
    CANNOT_CLEAR_FINAL_URLS_IF_FINAL_MOBILE_URLS_EXIST: AdGroupCriterionErrorEnum.AdGroupCriterionError
    CANNOT_CLEAR_FINAL_URLS_IF_FINAL_APP_URLS_EXIST: AdGroupCriterionErrorEnum.AdGroupCriterionError
    CANNOT_CLEAR_FINAL_URLS_IF_TRACKING_URL_TEMPLATE_EXISTS: AdGroupCriterionErrorEnum.AdGroupCriterionError
    CANNOT_CLEAR_FINAL_URLS_IF_URL_CUSTOM_PARAMETERS_EXIST: AdGroupCriterionErrorEnum.AdGroupCriterionError
    CANNOT_SET_BOTH_DESTINATION_URL_AND_FINAL_URLS: AdGroupCriterionErrorEnum.AdGroupCriterionError
    CANNOT_SET_BOTH_DESTINATION_URL_AND_TRACKING_URL_TEMPLATE: AdGroupCriterionErrorEnum.AdGroupCriterionError
    FINAL_URLS_NOT_SUPPORTED_FOR_CRITERION_TYPE: AdGroupCriterionErrorEnum.AdGroupCriterionError
    FINAL_MOBILE_URLS_NOT_SUPPORTED_FOR_CRITERION_TYPE: AdGroupCriterionErrorEnum.AdGroupCriterionError

    def __init__(self) -> None:
        ...