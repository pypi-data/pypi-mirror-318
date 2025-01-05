from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class ConversionUploadErrorEnum(_message.Message):
    __slots__ = ()

    class ConversionUploadError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ConversionUploadErrorEnum.ConversionUploadError]
        UNKNOWN: _ClassVar[ConversionUploadErrorEnum.ConversionUploadError]
        TOO_MANY_CONVERSIONS_IN_REQUEST: _ClassVar[ConversionUploadErrorEnum.ConversionUploadError]
        UNPARSEABLE_GCLID: _ClassVar[ConversionUploadErrorEnum.ConversionUploadError]
        CONVERSION_PRECEDES_EVENT: _ClassVar[ConversionUploadErrorEnum.ConversionUploadError]
        EXPIRED_EVENT: _ClassVar[ConversionUploadErrorEnum.ConversionUploadError]
        TOO_RECENT_EVENT: _ClassVar[ConversionUploadErrorEnum.ConversionUploadError]
        EVENT_NOT_FOUND: _ClassVar[ConversionUploadErrorEnum.ConversionUploadError]
        UNAUTHORIZED_CUSTOMER: _ClassVar[ConversionUploadErrorEnum.ConversionUploadError]
        TOO_RECENT_CONVERSION_ACTION: _ClassVar[ConversionUploadErrorEnum.ConversionUploadError]
        CONVERSION_TRACKING_NOT_ENABLED_AT_IMPRESSION_TIME: _ClassVar[ConversionUploadErrorEnum.ConversionUploadError]
        EXTERNAL_ATTRIBUTION_DATA_SET_FOR_NON_EXTERNALLY_ATTRIBUTED_CONVERSION_ACTION: _ClassVar[ConversionUploadErrorEnum.ConversionUploadError]
        EXTERNAL_ATTRIBUTION_DATA_NOT_SET_FOR_EXTERNALLY_ATTRIBUTED_CONVERSION_ACTION: _ClassVar[ConversionUploadErrorEnum.ConversionUploadError]
        ORDER_ID_NOT_PERMITTED_FOR_EXTERNALLY_ATTRIBUTED_CONVERSION_ACTION: _ClassVar[ConversionUploadErrorEnum.ConversionUploadError]
        ORDER_ID_ALREADY_IN_USE: _ClassVar[ConversionUploadErrorEnum.ConversionUploadError]
        DUPLICATE_ORDER_ID: _ClassVar[ConversionUploadErrorEnum.ConversionUploadError]
        TOO_RECENT_CALL: _ClassVar[ConversionUploadErrorEnum.ConversionUploadError]
        EXPIRED_CALL: _ClassVar[ConversionUploadErrorEnum.ConversionUploadError]
        CALL_NOT_FOUND: _ClassVar[ConversionUploadErrorEnum.ConversionUploadError]
        CONVERSION_PRECEDES_CALL: _ClassVar[ConversionUploadErrorEnum.ConversionUploadError]
        CONVERSION_TRACKING_NOT_ENABLED_AT_CALL_TIME: _ClassVar[ConversionUploadErrorEnum.ConversionUploadError]
        UNPARSEABLE_CALLERS_PHONE_NUMBER: _ClassVar[ConversionUploadErrorEnum.ConversionUploadError]
        CLICK_CONVERSION_ALREADY_EXISTS: _ClassVar[ConversionUploadErrorEnum.ConversionUploadError]
        CALL_CONVERSION_ALREADY_EXISTS: _ClassVar[ConversionUploadErrorEnum.ConversionUploadError]
        DUPLICATE_CLICK_CONVERSION_IN_REQUEST: _ClassVar[ConversionUploadErrorEnum.ConversionUploadError]
        DUPLICATE_CALL_CONVERSION_IN_REQUEST: _ClassVar[ConversionUploadErrorEnum.ConversionUploadError]
        CUSTOM_VARIABLE_NOT_ENABLED: _ClassVar[ConversionUploadErrorEnum.ConversionUploadError]
        CUSTOM_VARIABLE_VALUE_CONTAINS_PII: _ClassVar[ConversionUploadErrorEnum.ConversionUploadError]
        INVALID_CUSTOMER_FOR_CLICK: _ClassVar[ConversionUploadErrorEnum.ConversionUploadError]
        INVALID_CUSTOMER_FOR_CALL: _ClassVar[ConversionUploadErrorEnum.ConversionUploadError]
        CONVERSION_NOT_COMPLIANT_WITH_ATT_POLICY: _ClassVar[ConversionUploadErrorEnum.ConversionUploadError]
        CLICK_NOT_FOUND: _ClassVar[ConversionUploadErrorEnum.ConversionUploadError]
        INVALID_USER_IDENTIFIER: _ClassVar[ConversionUploadErrorEnum.ConversionUploadError]
        EXTERNALLY_ATTRIBUTED_CONVERSION_ACTION_NOT_PERMITTED_WITH_USER_IDENTIFIER: _ClassVar[ConversionUploadErrorEnum.ConversionUploadError]
        UNSUPPORTED_USER_IDENTIFIER: _ClassVar[ConversionUploadErrorEnum.ConversionUploadError]
        GBRAID_WBRAID_BOTH_SET: _ClassVar[ConversionUploadErrorEnum.ConversionUploadError]
        UNPARSEABLE_WBRAID: _ClassVar[ConversionUploadErrorEnum.ConversionUploadError]
        UNPARSEABLE_GBRAID: _ClassVar[ConversionUploadErrorEnum.ConversionUploadError]
        ONE_PER_CLICK_CONVERSION_ACTION_NOT_PERMITTED_WITH_BRAID: _ClassVar[ConversionUploadErrorEnum.ConversionUploadError]
        CUSTOMER_DATA_POLICY_PROHIBITS_ENHANCED_CONVERSIONS: _ClassVar[ConversionUploadErrorEnum.ConversionUploadError]
        CUSTOMER_NOT_ACCEPTED_CUSTOMER_DATA_TERMS: _ClassVar[ConversionUploadErrorEnum.ConversionUploadError]
        ORDER_ID_CONTAINS_PII: _ClassVar[ConversionUploadErrorEnum.ConversionUploadError]
        CUSTOMER_NOT_ENABLED_ENHANCED_CONVERSIONS_FOR_LEADS: _ClassVar[ConversionUploadErrorEnum.ConversionUploadError]
        INVALID_JOB_ID: _ClassVar[ConversionUploadErrorEnum.ConversionUploadError]
        NO_CONVERSION_ACTION_FOUND: _ClassVar[ConversionUploadErrorEnum.ConversionUploadError]
        INVALID_CONVERSION_ACTION_TYPE: _ClassVar[ConversionUploadErrorEnum.ConversionUploadError]
    UNSPECIFIED: ConversionUploadErrorEnum.ConversionUploadError
    UNKNOWN: ConversionUploadErrorEnum.ConversionUploadError
    TOO_MANY_CONVERSIONS_IN_REQUEST: ConversionUploadErrorEnum.ConversionUploadError
    UNPARSEABLE_GCLID: ConversionUploadErrorEnum.ConversionUploadError
    CONVERSION_PRECEDES_EVENT: ConversionUploadErrorEnum.ConversionUploadError
    EXPIRED_EVENT: ConversionUploadErrorEnum.ConversionUploadError
    TOO_RECENT_EVENT: ConversionUploadErrorEnum.ConversionUploadError
    EVENT_NOT_FOUND: ConversionUploadErrorEnum.ConversionUploadError
    UNAUTHORIZED_CUSTOMER: ConversionUploadErrorEnum.ConversionUploadError
    TOO_RECENT_CONVERSION_ACTION: ConversionUploadErrorEnum.ConversionUploadError
    CONVERSION_TRACKING_NOT_ENABLED_AT_IMPRESSION_TIME: ConversionUploadErrorEnum.ConversionUploadError
    EXTERNAL_ATTRIBUTION_DATA_SET_FOR_NON_EXTERNALLY_ATTRIBUTED_CONVERSION_ACTION: ConversionUploadErrorEnum.ConversionUploadError
    EXTERNAL_ATTRIBUTION_DATA_NOT_SET_FOR_EXTERNALLY_ATTRIBUTED_CONVERSION_ACTION: ConversionUploadErrorEnum.ConversionUploadError
    ORDER_ID_NOT_PERMITTED_FOR_EXTERNALLY_ATTRIBUTED_CONVERSION_ACTION: ConversionUploadErrorEnum.ConversionUploadError
    ORDER_ID_ALREADY_IN_USE: ConversionUploadErrorEnum.ConversionUploadError
    DUPLICATE_ORDER_ID: ConversionUploadErrorEnum.ConversionUploadError
    TOO_RECENT_CALL: ConversionUploadErrorEnum.ConversionUploadError
    EXPIRED_CALL: ConversionUploadErrorEnum.ConversionUploadError
    CALL_NOT_FOUND: ConversionUploadErrorEnum.ConversionUploadError
    CONVERSION_PRECEDES_CALL: ConversionUploadErrorEnum.ConversionUploadError
    CONVERSION_TRACKING_NOT_ENABLED_AT_CALL_TIME: ConversionUploadErrorEnum.ConversionUploadError
    UNPARSEABLE_CALLERS_PHONE_NUMBER: ConversionUploadErrorEnum.ConversionUploadError
    CLICK_CONVERSION_ALREADY_EXISTS: ConversionUploadErrorEnum.ConversionUploadError
    CALL_CONVERSION_ALREADY_EXISTS: ConversionUploadErrorEnum.ConversionUploadError
    DUPLICATE_CLICK_CONVERSION_IN_REQUEST: ConversionUploadErrorEnum.ConversionUploadError
    DUPLICATE_CALL_CONVERSION_IN_REQUEST: ConversionUploadErrorEnum.ConversionUploadError
    CUSTOM_VARIABLE_NOT_ENABLED: ConversionUploadErrorEnum.ConversionUploadError
    CUSTOM_VARIABLE_VALUE_CONTAINS_PII: ConversionUploadErrorEnum.ConversionUploadError
    INVALID_CUSTOMER_FOR_CLICK: ConversionUploadErrorEnum.ConversionUploadError
    INVALID_CUSTOMER_FOR_CALL: ConversionUploadErrorEnum.ConversionUploadError
    CONVERSION_NOT_COMPLIANT_WITH_ATT_POLICY: ConversionUploadErrorEnum.ConversionUploadError
    CLICK_NOT_FOUND: ConversionUploadErrorEnum.ConversionUploadError
    INVALID_USER_IDENTIFIER: ConversionUploadErrorEnum.ConversionUploadError
    EXTERNALLY_ATTRIBUTED_CONVERSION_ACTION_NOT_PERMITTED_WITH_USER_IDENTIFIER: ConversionUploadErrorEnum.ConversionUploadError
    UNSUPPORTED_USER_IDENTIFIER: ConversionUploadErrorEnum.ConversionUploadError
    GBRAID_WBRAID_BOTH_SET: ConversionUploadErrorEnum.ConversionUploadError
    UNPARSEABLE_WBRAID: ConversionUploadErrorEnum.ConversionUploadError
    UNPARSEABLE_GBRAID: ConversionUploadErrorEnum.ConversionUploadError
    ONE_PER_CLICK_CONVERSION_ACTION_NOT_PERMITTED_WITH_BRAID: ConversionUploadErrorEnum.ConversionUploadError
    CUSTOMER_DATA_POLICY_PROHIBITS_ENHANCED_CONVERSIONS: ConversionUploadErrorEnum.ConversionUploadError
    CUSTOMER_NOT_ACCEPTED_CUSTOMER_DATA_TERMS: ConversionUploadErrorEnum.ConversionUploadError
    ORDER_ID_CONTAINS_PII: ConversionUploadErrorEnum.ConversionUploadError
    CUSTOMER_NOT_ENABLED_ENHANCED_CONVERSIONS_FOR_LEADS: ConversionUploadErrorEnum.ConversionUploadError
    INVALID_JOB_ID: ConversionUploadErrorEnum.ConversionUploadError
    NO_CONVERSION_ACTION_FOUND: ConversionUploadErrorEnum.ConversionUploadError
    INVALID_CONVERSION_ACTION_TYPE: ConversionUploadErrorEnum.ConversionUploadError

    def __init__(self) -> None:
        ...