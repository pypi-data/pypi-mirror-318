from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class ExtensionFeedItemErrorEnum(_message.Message):
    __slots__ = ()

    class ExtensionFeedItemError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ExtensionFeedItemErrorEnum.ExtensionFeedItemError]
        UNKNOWN: _ClassVar[ExtensionFeedItemErrorEnum.ExtensionFeedItemError]
        VALUE_OUT_OF_RANGE: _ClassVar[ExtensionFeedItemErrorEnum.ExtensionFeedItemError]
        URL_LIST_TOO_LONG: _ClassVar[ExtensionFeedItemErrorEnum.ExtensionFeedItemError]
        CANNOT_HAVE_RESTRICTION_ON_EMPTY_GEO_TARGETING: _ClassVar[ExtensionFeedItemErrorEnum.ExtensionFeedItemError]
        CANNOT_SET_WITH_FINAL_URLS: _ClassVar[ExtensionFeedItemErrorEnum.ExtensionFeedItemError]
        CANNOT_SET_WITHOUT_FINAL_URLS: _ClassVar[ExtensionFeedItemErrorEnum.ExtensionFeedItemError]
        INVALID_PHONE_NUMBER: _ClassVar[ExtensionFeedItemErrorEnum.ExtensionFeedItemError]
        PHONE_NUMBER_NOT_SUPPORTED_FOR_COUNTRY: _ClassVar[ExtensionFeedItemErrorEnum.ExtensionFeedItemError]
        CARRIER_SPECIFIC_SHORT_NUMBER_NOT_ALLOWED: _ClassVar[ExtensionFeedItemErrorEnum.ExtensionFeedItemError]
        PREMIUM_RATE_NUMBER_NOT_ALLOWED: _ClassVar[ExtensionFeedItemErrorEnum.ExtensionFeedItemError]
        DISALLOWED_NUMBER_TYPE: _ClassVar[ExtensionFeedItemErrorEnum.ExtensionFeedItemError]
        INVALID_DOMESTIC_PHONE_NUMBER_FORMAT: _ClassVar[ExtensionFeedItemErrorEnum.ExtensionFeedItemError]
        VANITY_PHONE_NUMBER_NOT_ALLOWED: _ClassVar[ExtensionFeedItemErrorEnum.ExtensionFeedItemError]
        INVALID_CALL_CONVERSION_ACTION: _ClassVar[ExtensionFeedItemErrorEnum.ExtensionFeedItemError]
        CUSTOMER_NOT_ON_ALLOWLIST_FOR_CALLTRACKING: _ClassVar[ExtensionFeedItemErrorEnum.ExtensionFeedItemError]
        CALLTRACKING_NOT_SUPPORTED_FOR_COUNTRY: _ClassVar[ExtensionFeedItemErrorEnum.ExtensionFeedItemError]
        CUSTOMER_CONSENT_FOR_CALL_RECORDING_REQUIRED: _ClassVar[ExtensionFeedItemErrorEnum.ExtensionFeedItemError]
        INVALID_APP_ID: _ClassVar[ExtensionFeedItemErrorEnum.ExtensionFeedItemError]
        QUOTES_IN_REVIEW_EXTENSION_SNIPPET: _ClassVar[ExtensionFeedItemErrorEnum.ExtensionFeedItemError]
        HYPHENS_IN_REVIEW_EXTENSION_SNIPPET: _ClassVar[ExtensionFeedItemErrorEnum.ExtensionFeedItemError]
        REVIEW_EXTENSION_SOURCE_INELIGIBLE: _ClassVar[ExtensionFeedItemErrorEnum.ExtensionFeedItemError]
        SOURCE_NAME_IN_REVIEW_EXTENSION_TEXT: _ClassVar[ExtensionFeedItemErrorEnum.ExtensionFeedItemError]
        INCONSISTENT_CURRENCY_CODES: _ClassVar[ExtensionFeedItemErrorEnum.ExtensionFeedItemError]
        PRICE_EXTENSION_HAS_DUPLICATED_HEADERS: _ClassVar[ExtensionFeedItemErrorEnum.ExtensionFeedItemError]
        PRICE_ITEM_HAS_DUPLICATED_HEADER_AND_DESCRIPTION: _ClassVar[ExtensionFeedItemErrorEnum.ExtensionFeedItemError]
        PRICE_EXTENSION_HAS_TOO_FEW_ITEMS: _ClassVar[ExtensionFeedItemErrorEnum.ExtensionFeedItemError]
        PRICE_EXTENSION_HAS_TOO_MANY_ITEMS: _ClassVar[ExtensionFeedItemErrorEnum.ExtensionFeedItemError]
        UNSUPPORTED_VALUE: _ClassVar[ExtensionFeedItemErrorEnum.ExtensionFeedItemError]
        UNSUPPORTED_VALUE_IN_SELECTED_LANGUAGE: _ClassVar[ExtensionFeedItemErrorEnum.ExtensionFeedItemError]
        INVALID_DEVICE_PREFERENCE: _ClassVar[ExtensionFeedItemErrorEnum.ExtensionFeedItemError]
        INVALID_SCHEDULE_END: _ClassVar[ExtensionFeedItemErrorEnum.ExtensionFeedItemError]
        DATE_TIME_MUST_BE_IN_ACCOUNT_TIME_ZONE: _ClassVar[ExtensionFeedItemErrorEnum.ExtensionFeedItemError]
        INVALID_SNIPPETS_HEADER: _ClassVar[ExtensionFeedItemErrorEnum.ExtensionFeedItemError]
        CANNOT_OPERATE_ON_REMOVED_FEED_ITEM: _ClassVar[ExtensionFeedItemErrorEnum.ExtensionFeedItemError]
        PHONE_NUMBER_NOT_SUPPORTED_WITH_CALLTRACKING_FOR_COUNTRY: _ClassVar[ExtensionFeedItemErrorEnum.ExtensionFeedItemError]
        CONFLICTING_CALL_CONVERSION_SETTINGS: _ClassVar[ExtensionFeedItemErrorEnum.ExtensionFeedItemError]
        EXTENSION_TYPE_MISMATCH: _ClassVar[ExtensionFeedItemErrorEnum.ExtensionFeedItemError]
        EXTENSION_SUBTYPE_REQUIRED: _ClassVar[ExtensionFeedItemErrorEnum.ExtensionFeedItemError]
        EXTENSION_TYPE_UNSUPPORTED: _ClassVar[ExtensionFeedItemErrorEnum.ExtensionFeedItemError]
        CANNOT_OPERATE_ON_FEED_WITH_MULTIPLE_MAPPINGS: _ClassVar[ExtensionFeedItemErrorEnum.ExtensionFeedItemError]
        CANNOT_OPERATE_ON_FEED_WITH_KEY_ATTRIBUTES: _ClassVar[ExtensionFeedItemErrorEnum.ExtensionFeedItemError]
        INVALID_PRICE_FORMAT: _ClassVar[ExtensionFeedItemErrorEnum.ExtensionFeedItemError]
        PROMOTION_INVALID_TIME: _ClassVar[ExtensionFeedItemErrorEnum.ExtensionFeedItemError]
        TOO_MANY_DECIMAL_PLACES_SPECIFIED: _ClassVar[ExtensionFeedItemErrorEnum.ExtensionFeedItemError]
        CONCRETE_EXTENSION_TYPE_REQUIRED: _ClassVar[ExtensionFeedItemErrorEnum.ExtensionFeedItemError]
        SCHEDULE_END_NOT_AFTER_START: _ClassVar[ExtensionFeedItemErrorEnum.ExtensionFeedItemError]
    UNSPECIFIED: ExtensionFeedItemErrorEnum.ExtensionFeedItemError
    UNKNOWN: ExtensionFeedItemErrorEnum.ExtensionFeedItemError
    VALUE_OUT_OF_RANGE: ExtensionFeedItemErrorEnum.ExtensionFeedItemError
    URL_LIST_TOO_LONG: ExtensionFeedItemErrorEnum.ExtensionFeedItemError
    CANNOT_HAVE_RESTRICTION_ON_EMPTY_GEO_TARGETING: ExtensionFeedItemErrorEnum.ExtensionFeedItemError
    CANNOT_SET_WITH_FINAL_URLS: ExtensionFeedItemErrorEnum.ExtensionFeedItemError
    CANNOT_SET_WITHOUT_FINAL_URLS: ExtensionFeedItemErrorEnum.ExtensionFeedItemError
    INVALID_PHONE_NUMBER: ExtensionFeedItemErrorEnum.ExtensionFeedItemError
    PHONE_NUMBER_NOT_SUPPORTED_FOR_COUNTRY: ExtensionFeedItemErrorEnum.ExtensionFeedItemError
    CARRIER_SPECIFIC_SHORT_NUMBER_NOT_ALLOWED: ExtensionFeedItemErrorEnum.ExtensionFeedItemError
    PREMIUM_RATE_NUMBER_NOT_ALLOWED: ExtensionFeedItemErrorEnum.ExtensionFeedItemError
    DISALLOWED_NUMBER_TYPE: ExtensionFeedItemErrorEnum.ExtensionFeedItemError
    INVALID_DOMESTIC_PHONE_NUMBER_FORMAT: ExtensionFeedItemErrorEnum.ExtensionFeedItemError
    VANITY_PHONE_NUMBER_NOT_ALLOWED: ExtensionFeedItemErrorEnum.ExtensionFeedItemError
    INVALID_CALL_CONVERSION_ACTION: ExtensionFeedItemErrorEnum.ExtensionFeedItemError
    CUSTOMER_NOT_ON_ALLOWLIST_FOR_CALLTRACKING: ExtensionFeedItemErrorEnum.ExtensionFeedItemError
    CALLTRACKING_NOT_SUPPORTED_FOR_COUNTRY: ExtensionFeedItemErrorEnum.ExtensionFeedItemError
    CUSTOMER_CONSENT_FOR_CALL_RECORDING_REQUIRED: ExtensionFeedItemErrorEnum.ExtensionFeedItemError
    INVALID_APP_ID: ExtensionFeedItemErrorEnum.ExtensionFeedItemError
    QUOTES_IN_REVIEW_EXTENSION_SNIPPET: ExtensionFeedItemErrorEnum.ExtensionFeedItemError
    HYPHENS_IN_REVIEW_EXTENSION_SNIPPET: ExtensionFeedItemErrorEnum.ExtensionFeedItemError
    REVIEW_EXTENSION_SOURCE_INELIGIBLE: ExtensionFeedItemErrorEnum.ExtensionFeedItemError
    SOURCE_NAME_IN_REVIEW_EXTENSION_TEXT: ExtensionFeedItemErrorEnum.ExtensionFeedItemError
    INCONSISTENT_CURRENCY_CODES: ExtensionFeedItemErrorEnum.ExtensionFeedItemError
    PRICE_EXTENSION_HAS_DUPLICATED_HEADERS: ExtensionFeedItemErrorEnum.ExtensionFeedItemError
    PRICE_ITEM_HAS_DUPLICATED_HEADER_AND_DESCRIPTION: ExtensionFeedItemErrorEnum.ExtensionFeedItemError
    PRICE_EXTENSION_HAS_TOO_FEW_ITEMS: ExtensionFeedItemErrorEnum.ExtensionFeedItemError
    PRICE_EXTENSION_HAS_TOO_MANY_ITEMS: ExtensionFeedItemErrorEnum.ExtensionFeedItemError
    UNSUPPORTED_VALUE: ExtensionFeedItemErrorEnum.ExtensionFeedItemError
    UNSUPPORTED_VALUE_IN_SELECTED_LANGUAGE: ExtensionFeedItemErrorEnum.ExtensionFeedItemError
    INVALID_DEVICE_PREFERENCE: ExtensionFeedItemErrorEnum.ExtensionFeedItemError
    INVALID_SCHEDULE_END: ExtensionFeedItemErrorEnum.ExtensionFeedItemError
    DATE_TIME_MUST_BE_IN_ACCOUNT_TIME_ZONE: ExtensionFeedItemErrorEnum.ExtensionFeedItemError
    INVALID_SNIPPETS_HEADER: ExtensionFeedItemErrorEnum.ExtensionFeedItemError
    CANNOT_OPERATE_ON_REMOVED_FEED_ITEM: ExtensionFeedItemErrorEnum.ExtensionFeedItemError
    PHONE_NUMBER_NOT_SUPPORTED_WITH_CALLTRACKING_FOR_COUNTRY: ExtensionFeedItemErrorEnum.ExtensionFeedItemError
    CONFLICTING_CALL_CONVERSION_SETTINGS: ExtensionFeedItemErrorEnum.ExtensionFeedItemError
    EXTENSION_TYPE_MISMATCH: ExtensionFeedItemErrorEnum.ExtensionFeedItemError
    EXTENSION_SUBTYPE_REQUIRED: ExtensionFeedItemErrorEnum.ExtensionFeedItemError
    EXTENSION_TYPE_UNSUPPORTED: ExtensionFeedItemErrorEnum.ExtensionFeedItemError
    CANNOT_OPERATE_ON_FEED_WITH_MULTIPLE_MAPPINGS: ExtensionFeedItemErrorEnum.ExtensionFeedItemError
    CANNOT_OPERATE_ON_FEED_WITH_KEY_ATTRIBUTES: ExtensionFeedItemErrorEnum.ExtensionFeedItemError
    INVALID_PRICE_FORMAT: ExtensionFeedItemErrorEnum.ExtensionFeedItemError
    PROMOTION_INVALID_TIME: ExtensionFeedItemErrorEnum.ExtensionFeedItemError
    TOO_MANY_DECIMAL_PLACES_SPECIFIED: ExtensionFeedItemErrorEnum.ExtensionFeedItemError
    CONCRETE_EXTENSION_TYPE_REQUIRED: ExtensionFeedItemErrorEnum.ExtensionFeedItemError
    SCHEDULE_END_NOT_AFTER_START: ExtensionFeedItemErrorEnum.ExtensionFeedItemError

    def __init__(self) -> None:
        ...