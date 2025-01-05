from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class ConversionAdjustmentUploadErrorEnum(_message.Message):
    __slots__ = ()

    class ConversionAdjustmentUploadError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadError]
        UNKNOWN: _ClassVar[ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadError]
        TOO_RECENT_CONVERSION_ACTION: _ClassVar[ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadError]
        CONVERSION_ALREADY_RETRACTED: _ClassVar[ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadError]
        CONVERSION_NOT_FOUND: _ClassVar[ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadError]
        CONVERSION_EXPIRED: _ClassVar[ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadError]
        ADJUSTMENT_PRECEDES_CONVERSION: _ClassVar[ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadError]
        MORE_RECENT_RESTATEMENT_FOUND: _ClassVar[ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadError]
        TOO_RECENT_CONVERSION: _ClassVar[ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadError]
        CANNOT_RESTATE_CONVERSION_ACTION_THAT_ALWAYS_USES_DEFAULT_CONVERSION_VALUE: _ClassVar[ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadError]
        TOO_MANY_ADJUSTMENTS_IN_REQUEST: _ClassVar[ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadError]
        TOO_MANY_ADJUSTMENTS: _ClassVar[ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadError]
        RESTATEMENT_ALREADY_EXISTS: _ClassVar[ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadError]
        DUPLICATE_ADJUSTMENT_IN_REQUEST: _ClassVar[ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadError]
        CUSTOMER_NOT_ACCEPTED_CUSTOMER_DATA_TERMS: _ClassVar[ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadError]
        CONVERSION_ACTION_NOT_ELIGIBLE_FOR_ENHANCEMENT: _ClassVar[ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadError]
        INVALID_USER_IDENTIFIER: _ClassVar[ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadError]
        UNSUPPORTED_USER_IDENTIFIER: _ClassVar[ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadError]
        GCLID_DATE_TIME_PAIR_AND_ORDER_ID_BOTH_SET: _ClassVar[ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadError]
        CONVERSION_ALREADY_ENHANCED: _ClassVar[ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadError]
        DUPLICATE_ENHANCEMENT_IN_REQUEST: _ClassVar[ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadError]
        CUSTOMER_DATA_POLICY_PROHIBITS_ENHANCEMENT: _ClassVar[ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadError]
        MISSING_ORDER_ID_FOR_WEBPAGE: _ClassVar[ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadError]
        ORDER_ID_CONTAINS_PII: _ClassVar[ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadError]
        INVALID_JOB_ID: _ClassVar[ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadError]
        NO_CONVERSION_ACTION_FOUND: _ClassVar[ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadError]
        INVALID_CONVERSION_ACTION_TYPE: _ClassVar[ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadError]
    UNSPECIFIED: ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadError
    UNKNOWN: ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadError
    TOO_RECENT_CONVERSION_ACTION: ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadError
    CONVERSION_ALREADY_RETRACTED: ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadError
    CONVERSION_NOT_FOUND: ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadError
    CONVERSION_EXPIRED: ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadError
    ADJUSTMENT_PRECEDES_CONVERSION: ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadError
    MORE_RECENT_RESTATEMENT_FOUND: ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadError
    TOO_RECENT_CONVERSION: ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadError
    CANNOT_RESTATE_CONVERSION_ACTION_THAT_ALWAYS_USES_DEFAULT_CONVERSION_VALUE: ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadError
    TOO_MANY_ADJUSTMENTS_IN_REQUEST: ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadError
    TOO_MANY_ADJUSTMENTS: ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadError
    RESTATEMENT_ALREADY_EXISTS: ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadError
    DUPLICATE_ADJUSTMENT_IN_REQUEST: ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadError
    CUSTOMER_NOT_ACCEPTED_CUSTOMER_DATA_TERMS: ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadError
    CONVERSION_ACTION_NOT_ELIGIBLE_FOR_ENHANCEMENT: ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadError
    INVALID_USER_IDENTIFIER: ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadError
    UNSUPPORTED_USER_IDENTIFIER: ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadError
    GCLID_DATE_TIME_PAIR_AND_ORDER_ID_BOTH_SET: ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadError
    CONVERSION_ALREADY_ENHANCED: ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadError
    DUPLICATE_ENHANCEMENT_IN_REQUEST: ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadError
    CUSTOMER_DATA_POLICY_PROHIBITS_ENHANCEMENT: ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadError
    MISSING_ORDER_ID_FOR_WEBPAGE: ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadError
    ORDER_ID_CONTAINS_PII: ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadError
    INVALID_JOB_ID: ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadError
    NO_CONVERSION_ACTION_FOUND: ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadError
    INVALID_CONVERSION_ACTION_TYPE: ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadError

    def __init__(self) -> None:
        ...