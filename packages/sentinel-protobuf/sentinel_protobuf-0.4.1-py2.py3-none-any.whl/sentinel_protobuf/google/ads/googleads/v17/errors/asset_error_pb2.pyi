from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class AssetErrorEnum(_message.Message):
    __slots__ = ()

    class AssetError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[AssetErrorEnum.AssetError]
        UNKNOWN: _ClassVar[AssetErrorEnum.AssetError]
        CUSTOMER_NOT_ON_ALLOWLIST_FOR_ASSET_TYPE: _ClassVar[AssetErrorEnum.AssetError]
        DUPLICATE_ASSET: _ClassVar[AssetErrorEnum.AssetError]
        DUPLICATE_ASSET_NAME: _ClassVar[AssetErrorEnum.AssetError]
        ASSET_DATA_IS_MISSING: _ClassVar[AssetErrorEnum.AssetError]
        CANNOT_MODIFY_ASSET_NAME: _ClassVar[AssetErrorEnum.AssetError]
        FIELD_INCOMPATIBLE_WITH_ASSET_TYPE: _ClassVar[AssetErrorEnum.AssetError]
        INVALID_CALL_TO_ACTION_TEXT: _ClassVar[AssetErrorEnum.AssetError]
        LEAD_FORM_INVALID_FIELDS_COMBINATION: _ClassVar[AssetErrorEnum.AssetError]
        LEAD_FORM_MISSING_AGREEMENT: _ClassVar[AssetErrorEnum.AssetError]
        INVALID_ASSET_STATUS: _ClassVar[AssetErrorEnum.AssetError]
        FIELD_CANNOT_BE_MODIFIED_FOR_ASSET_TYPE: _ClassVar[AssetErrorEnum.AssetError]
        SCHEDULES_CANNOT_OVERLAP: _ClassVar[AssetErrorEnum.AssetError]
        PROMOTION_CANNOT_SET_PERCENT_OFF_AND_MONEY_AMOUNT_OFF: _ClassVar[AssetErrorEnum.AssetError]
        PROMOTION_CANNOT_SET_PROMOTION_CODE_AND_ORDERS_OVER_AMOUNT: _ClassVar[AssetErrorEnum.AssetError]
        TOO_MANY_DECIMAL_PLACES_SPECIFIED: _ClassVar[AssetErrorEnum.AssetError]
        DUPLICATE_ASSETS_WITH_DIFFERENT_FIELD_VALUE: _ClassVar[AssetErrorEnum.AssetError]
        CALL_CARRIER_SPECIFIC_SHORT_NUMBER_NOT_ALLOWED: _ClassVar[AssetErrorEnum.AssetError]
        CALL_CUSTOMER_CONSENT_FOR_CALL_RECORDING_REQUIRED: _ClassVar[AssetErrorEnum.AssetError]
        CALL_DISALLOWED_NUMBER_TYPE: _ClassVar[AssetErrorEnum.AssetError]
        CALL_INVALID_CONVERSION_ACTION: _ClassVar[AssetErrorEnum.AssetError]
        CALL_INVALID_COUNTRY_CODE: _ClassVar[AssetErrorEnum.AssetError]
        CALL_INVALID_DOMESTIC_PHONE_NUMBER_FORMAT: _ClassVar[AssetErrorEnum.AssetError]
        CALL_INVALID_PHONE_NUMBER: _ClassVar[AssetErrorEnum.AssetError]
        CALL_PHONE_NUMBER_NOT_SUPPORTED_FOR_COUNTRY: _ClassVar[AssetErrorEnum.AssetError]
        CALL_PREMIUM_RATE_NUMBER_NOT_ALLOWED: _ClassVar[AssetErrorEnum.AssetError]
        CALL_VANITY_PHONE_NUMBER_NOT_ALLOWED: _ClassVar[AssetErrorEnum.AssetError]
        PRICE_HEADER_SAME_AS_DESCRIPTION: _ClassVar[AssetErrorEnum.AssetError]
        MOBILE_APP_INVALID_APP_ID: _ClassVar[AssetErrorEnum.AssetError]
        MOBILE_APP_INVALID_FINAL_URL_FOR_APP_DOWNLOAD_URL: _ClassVar[AssetErrorEnum.AssetError]
        NAME_REQUIRED_FOR_ASSET_TYPE: _ClassVar[AssetErrorEnum.AssetError]
        LEAD_FORM_LEGACY_QUALIFYING_QUESTIONS_DISALLOWED: _ClassVar[AssetErrorEnum.AssetError]
        NAME_CONFLICT_FOR_ASSET_TYPE: _ClassVar[AssetErrorEnum.AssetError]
        CANNOT_MODIFY_ASSET_SOURCE: _ClassVar[AssetErrorEnum.AssetError]
        CANNOT_MODIFY_AUTOMATICALLY_CREATED_ASSET: _ClassVar[AssetErrorEnum.AssetError]
        LEAD_FORM_LOCATION_ANSWER_TYPE_DISALLOWED: _ClassVar[AssetErrorEnum.AssetError]
        PAGE_FEED_INVALID_LABEL_TEXT: _ClassVar[AssetErrorEnum.AssetError]
    UNSPECIFIED: AssetErrorEnum.AssetError
    UNKNOWN: AssetErrorEnum.AssetError
    CUSTOMER_NOT_ON_ALLOWLIST_FOR_ASSET_TYPE: AssetErrorEnum.AssetError
    DUPLICATE_ASSET: AssetErrorEnum.AssetError
    DUPLICATE_ASSET_NAME: AssetErrorEnum.AssetError
    ASSET_DATA_IS_MISSING: AssetErrorEnum.AssetError
    CANNOT_MODIFY_ASSET_NAME: AssetErrorEnum.AssetError
    FIELD_INCOMPATIBLE_WITH_ASSET_TYPE: AssetErrorEnum.AssetError
    INVALID_CALL_TO_ACTION_TEXT: AssetErrorEnum.AssetError
    LEAD_FORM_INVALID_FIELDS_COMBINATION: AssetErrorEnum.AssetError
    LEAD_FORM_MISSING_AGREEMENT: AssetErrorEnum.AssetError
    INVALID_ASSET_STATUS: AssetErrorEnum.AssetError
    FIELD_CANNOT_BE_MODIFIED_FOR_ASSET_TYPE: AssetErrorEnum.AssetError
    SCHEDULES_CANNOT_OVERLAP: AssetErrorEnum.AssetError
    PROMOTION_CANNOT_SET_PERCENT_OFF_AND_MONEY_AMOUNT_OFF: AssetErrorEnum.AssetError
    PROMOTION_CANNOT_SET_PROMOTION_CODE_AND_ORDERS_OVER_AMOUNT: AssetErrorEnum.AssetError
    TOO_MANY_DECIMAL_PLACES_SPECIFIED: AssetErrorEnum.AssetError
    DUPLICATE_ASSETS_WITH_DIFFERENT_FIELD_VALUE: AssetErrorEnum.AssetError
    CALL_CARRIER_SPECIFIC_SHORT_NUMBER_NOT_ALLOWED: AssetErrorEnum.AssetError
    CALL_CUSTOMER_CONSENT_FOR_CALL_RECORDING_REQUIRED: AssetErrorEnum.AssetError
    CALL_DISALLOWED_NUMBER_TYPE: AssetErrorEnum.AssetError
    CALL_INVALID_CONVERSION_ACTION: AssetErrorEnum.AssetError
    CALL_INVALID_COUNTRY_CODE: AssetErrorEnum.AssetError
    CALL_INVALID_DOMESTIC_PHONE_NUMBER_FORMAT: AssetErrorEnum.AssetError
    CALL_INVALID_PHONE_NUMBER: AssetErrorEnum.AssetError
    CALL_PHONE_NUMBER_NOT_SUPPORTED_FOR_COUNTRY: AssetErrorEnum.AssetError
    CALL_PREMIUM_RATE_NUMBER_NOT_ALLOWED: AssetErrorEnum.AssetError
    CALL_VANITY_PHONE_NUMBER_NOT_ALLOWED: AssetErrorEnum.AssetError
    PRICE_HEADER_SAME_AS_DESCRIPTION: AssetErrorEnum.AssetError
    MOBILE_APP_INVALID_APP_ID: AssetErrorEnum.AssetError
    MOBILE_APP_INVALID_FINAL_URL_FOR_APP_DOWNLOAD_URL: AssetErrorEnum.AssetError
    NAME_REQUIRED_FOR_ASSET_TYPE: AssetErrorEnum.AssetError
    LEAD_FORM_LEGACY_QUALIFYING_QUESTIONS_DISALLOWED: AssetErrorEnum.AssetError
    NAME_CONFLICT_FOR_ASSET_TYPE: AssetErrorEnum.AssetError
    CANNOT_MODIFY_ASSET_SOURCE: AssetErrorEnum.AssetError
    CANNOT_MODIFY_AUTOMATICALLY_CREATED_ASSET: AssetErrorEnum.AssetError
    LEAD_FORM_LOCATION_ANSWER_TYPE_DISALLOWED: AssetErrorEnum.AssetError
    PAGE_FEED_INVALID_LABEL_TEXT: AssetErrorEnum.AssetError

    def __init__(self) -> None:
        ...