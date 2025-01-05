from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class OfflineUserDataJobErrorEnum(_message.Message):
    __slots__ = ()

    class OfflineUserDataJobError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[OfflineUserDataJobErrorEnum.OfflineUserDataJobError]
        UNKNOWN: _ClassVar[OfflineUserDataJobErrorEnum.OfflineUserDataJobError]
        INVALID_USER_LIST_ID: _ClassVar[OfflineUserDataJobErrorEnum.OfflineUserDataJobError]
        INVALID_USER_LIST_TYPE: _ClassVar[OfflineUserDataJobErrorEnum.OfflineUserDataJobError]
        NOT_ON_ALLOWLIST_FOR_USER_ID: _ClassVar[OfflineUserDataJobErrorEnum.OfflineUserDataJobError]
        INCOMPATIBLE_UPLOAD_KEY_TYPE: _ClassVar[OfflineUserDataJobErrorEnum.OfflineUserDataJobError]
        MISSING_USER_IDENTIFIER: _ClassVar[OfflineUserDataJobErrorEnum.OfflineUserDataJobError]
        INVALID_MOBILE_ID_FORMAT: _ClassVar[OfflineUserDataJobErrorEnum.OfflineUserDataJobError]
        TOO_MANY_USER_IDENTIFIERS: _ClassVar[OfflineUserDataJobErrorEnum.OfflineUserDataJobError]
        NOT_ON_ALLOWLIST_FOR_STORE_SALES_DIRECT: _ClassVar[OfflineUserDataJobErrorEnum.OfflineUserDataJobError]
        NOT_ON_ALLOWLIST_FOR_UNIFIED_STORE_SALES: _ClassVar[OfflineUserDataJobErrorEnum.OfflineUserDataJobError]
        INVALID_PARTNER_ID: _ClassVar[OfflineUserDataJobErrorEnum.OfflineUserDataJobError]
        INVALID_ENCODING: _ClassVar[OfflineUserDataJobErrorEnum.OfflineUserDataJobError]
        INVALID_COUNTRY_CODE: _ClassVar[OfflineUserDataJobErrorEnum.OfflineUserDataJobError]
        INCOMPATIBLE_USER_IDENTIFIER: _ClassVar[OfflineUserDataJobErrorEnum.OfflineUserDataJobError]
        FUTURE_TRANSACTION_TIME: _ClassVar[OfflineUserDataJobErrorEnum.OfflineUserDataJobError]
        INVALID_CONVERSION_ACTION: _ClassVar[OfflineUserDataJobErrorEnum.OfflineUserDataJobError]
        MOBILE_ID_NOT_SUPPORTED: _ClassVar[OfflineUserDataJobErrorEnum.OfflineUserDataJobError]
        INVALID_OPERATION_ORDER: _ClassVar[OfflineUserDataJobErrorEnum.OfflineUserDataJobError]
        CONFLICTING_OPERATION: _ClassVar[OfflineUserDataJobErrorEnum.OfflineUserDataJobError]
        EXTERNAL_UPDATE_ID_ALREADY_EXISTS: _ClassVar[OfflineUserDataJobErrorEnum.OfflineUserDataJobError]
        JOB_ALREADY_STARTED: _ClassVar[OfflineUserDataJobErrorEnum.OfflineUserDataJobError]
        REMOVE_NOT_SUPPORTED: _ClassVar[OfflineUserDataJobErrorEnum.OfflineUserDataJobError]
        REMOVE_ALL_NOT_SUPPORTED: _ClassVar[OfflineUserDataJobErrorEnum.OfflineUserDataJobError]
        INVALID_SHA256_FORMAT: _ClassVar[OfflineUserDataJobErrorEnum.OfflineUserDataJobError]
        CUSTOM_KEY_DISABLED: _ClassVar[OfflineUserDataJobErrorEnum.OfflineUserDataJobError]
        CUSTOM_KEY_NOT_PREDEFINED: _ClassVar[OfflineUserDataJobErrorEnum.OfflineUserDataJobError]
        CUSTOM_KEY_NOT_SET: _ClassVar[OfflineUserDataJobErrorEnum.OfflineUserDataJobError]
        CUSTOMER_NOT_ACCEPTED_CUSTOMER_DATA_TERMS: _ClassVar[OfflineUserDataJobErrorEnum.OfflineUserDataJobError]
        ATTRIBUTES_NOT_APPLICABLE_FOR_CUSTOMER_MATCH_USER_LIST: _ClassVar[OfflineUserDataJobErrorEnum.OfflineUserDataJobError]
        LIFETIME_VALUE_BUCKET_NOT_IN_RANGE: _ClassVar[OfflineUserDataJobErrorEnum.OfflineUserDataJobError]
        INCOMPATIBLE_USER_IDENTIFIER_FOR_ATTRIBUTES: _ClassVar[OfflineUserDataJobErrorEnum.OfflineUserDataJobError]
        FUTURE_TIME_NOT_ALLOWED: _ClassVar[OfflineUserDataJobErrorEnum.OfflineUserDataJobError]
        LAST_PURCHASE_TIME_LESS_THAN_ACQUISITION_TIME: _ClassVar[OfflineUserDataJobErrorEnum.OfflineUserDataJobError]
        CUSTOMER_IDENTIFIER_NOT_ALLOWED: _ClassVar[OfflineUserDataJobErrorEnum.OfflineUserDataJobError]
        INVALID_ITEM_ID: _ClassVar[OfflineUserDataJobErrorEnum.OfflineUserDataJobError]
        FIRST_PURCHASE_TIME_GREATER_THAN_LAST_PURCHASE_TIME: _ClassVar[OfflineUserDataJobErrorEnum.OfflineUserDataJobError]
        INVALID_LIFECYCLE_STAGE: _ClassVar[OfflineUserDataJobErrorEnum.OfflineUserDataJobError]
        INVALID_EVENT_VALUE: _ClassVar[OfflineUserDataJobErrorEnum.OfflineUserDataJobError]
        EVENT_ATTRIBUTE_ALL_FIELDS_ARE_REQUIRED: _ClassVar[OfflineUserDataJobErrorEnum.OfflineUserDataJobError]
        OPERATION_LEVEL_CONSENT_PROVIDED: _ClassVar[OfflineUserDataJobErrorEnum.OfflineUserDataJobError]
    UNSPECIFIED: OfflineUserDataJobErrorEnum.OfflineUserDataJobError
    UNKNOWN: OfflineUserDataJobErrorEnum.OfflineUserDataJobError
    INVALID_USER_LIST_ID: OfflineUserDataJobErrorEnum.OfflineUserDataJobError
    INVALID_USER_LIST_TYPE: OfflineUserDataJobErrorEnum.OfflineUserDataJobError
    NOT_ON_ALLOWLIST_FOR_USER_ID: OfflineUserDataJobErrorEnum.OfflineUserDataJobError
    INCOMPATIBLE_UPLOAD_KEY_TYPE: OfflineUserDataJobErrorEnum.OfflineUserDataJobError
    MISSING_USER_IDENTIFIER: OfflineUserDataJobErrorEnum.OfflineUserDataJobError
    INVALID_MOBILE_ID_FORMAT: OfflineUserDataJobErrorEnum.OfflineUserDataJobError
    TOO_MANY_USER_IDENTIFIERS: OfflineUserDataJobErrorEnum.OfflineUserDataJobError
    NOT_ON_ALLOWLIST_FOR_STORE_SALES_DIRECT: OfflineUserDataJobErrorEnum.OfflineUserDataJobError
    NOT_ON_ALLOWLIST_FOR_UNIFIED_STORE_SALES: OfflineUserDataJobErrorEnum.OfflineUserDataJobError
    INVALID_PARTNER_ID: OfflineUserDataJobErrorEnum.OfflineUserDataJobError
    INVALID_ENCODING: OfflineUserDataJobErrorEnum.OfflineUserDataJobError
    INVALID_COUNTRY_CODE: OfflineUserDataJobErrorEnum.OfflineUserDataJobError
    INCOMPATIBLE_USER_IDENTIFIER: OfflineUserDataJobErrorEnum.OfflineUserDataJobError
    FUTURE_TRANSACTION_TIME: OfflineUserDataJobErrorEnum.OfflineUserDataJobError
    INVALID_CONVERSION_ACTION: OfflineUserDataJobErrorEnum.OfflineUserDataJobError
    MOBILE_ID_NOT_SUPPORTED: OfflineUserDataJobErrorEnum.OfflineUserDataJobError
    INVALID_OPERATION_ORDER: OfflineUserDataJobErrorEnum.OfflineUserDataJobError
    CONFLICTING_OPERATION: OfflineUserDataJobErrorEnum.OfflineUserDataJobError
    EXTERNAL_UPDATE_ID_ALREADY_EXISTS: OfflineUserDataJobErrorEnum.OfflineUserDataJobError
    JOB_ALREADY_STARTED: OfflineUserDataJobErrorEnum.OfflineUserDataJobError
    REMOVE_NOT_SUPPORTED: OfflineUserDataJobErrorEnum.OfflineUserDataJobError
    REMOVE_ALL_NOT_SUPPORTED: OfflineUserDataJobErrorEnum.OfflineUserDataJobError
    INVALID_SHA256_FORMAT: OfflineUserDataJobErrorEnum.OfflineUserDataJobError
    CUSTOM_KEY_DISABLED: OfflineUserDataJobErrorEnum.OfflineUserDataJobError
    CUSTOM_KEY_NOT_PREDEFINED: OfflineUserDataJobErrorEnum.OfflineUserDataJobError
    CUSTOM_KEY_NOT_SET: OfflineUserDataJobErrorEnum.OfflineUserDataJobError
    CUSTOMER_NOT_ACCEPTED_CUSTOMER_DATA_TERMS: OfflineUserDataJobErrorEnum.OfflineUserDataJobError
    ATTRIBUTES_NOT_APPLICABLE_FOR_CUSTOMER_MATCH_USER_LIST: OfflineUserDataJobErrorEnum.OfflineUserDataJobError
    LIFETIME_VALUE_BUCKET_NOT_IN_RANGE: OfflineUserDataJobErrorEnum.OfflineUserDataJobError
    INCOMPATIBLE_USER_IDENTIFIER_FOR_ATTRIBUTES: OfflineUserDataJobErrorEnum.OfflineUserDataJobError
    FUTURE_TIME_NOT_ALLOWED: OfflineUserDataJobErrorEnum.OfflineUserDataJobError
    LAST_PURCHASE_TIME_LESS_THAN_ACQUISITION_TIME: OfflineUserDataJobErrorEnum.OfflineUserDataJobError
    CUSTOMER_IDENTIFIER_NOT_ALLOWED: OfflineUserDataJobErrorEnum.OfflineUserDataJobError
    INVALID_ITEM_ID: OfflineUserDataJobErrorEnum.OfflineUserDataJobError
    FIRST_PURCHASE_TIME_GREATER_THAN_LAST_PURCHASE_TIME: OfflineUserDataJobErrorEnum.OfflineUserDataJobError
    INVALID_LIFECYCLE_STAGE: OfflineUserDataJobErrorEnum.OfflineUserDataJobError
    INVALID_EVENT_VALUE: OfflineUserDataJobErrorEnum.OfflineUserDataJobError
    EVENT_ATTRIBUTE_ALL_FIELDS_ARE_REQUIRED: OfflineUserDataJobErrorEnum.OfflineUserDataJobError
    OPERATION_LEVEL_CONSENT_PROVIDED: OfflineUserDataJobErrorEnum.OfflineUserDataJobError

    def __init__(self) -> None:
        ...