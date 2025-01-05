from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class CustomerPayPerConversionEligibilityFailureReasonEnum(_message.Message):
    __slots__ = ()

    class CustomerPayPerConversionEligibilityFailureReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[CustomerPayPerConversionEligibilityFailureReasonEnum.CustomerPayPerConversionEligibilityFailureReason]
        UNKNOWN: _ClassVar[CustomerPayPerConversionEligibilityFailureReasonEnum.CustomerPayPerConversionEligibilityFailureReason]
        NOT_ENOUGH_CONVERSIONS: _ClassVar[CustomerPayPerConversionEligibilityFailureReasonEnum.CustomerPayPerConversionEligibilityFailureReason]
        CONVERSION_LAG_TOO_HIGH: _ClassVar[CustomerPayPerConversionEligibilityFailureReasonEnum.CustomerPayPerConversionEligibilityFailureReason]
        HAS_CAMPAIGN_WITH_SHARED_BUDGET: _ClassVar[CustomerPayPerConversionEligibilityFailureReasonEnum.CustomerPayPerConversionEligibilityFailureReason]
        HAS_UPLOAD_CLICKS_CONVERSION: _ClassVar[CustomerPayPerConversionEligibilityFailureReasonEnum.CustomerPayPerConversionEligibilityFailureReason]
        AVERAGE_DAILY_SPEND_TOO_HIGH: _ClassVar[CustomerPayPerConversionEligibilityFailureReasonEnum.CustomerPayPerConversionEligibilityFailureReason]
        ANALYSIS_NOT_COMPLETE: _ClassVar[CustomerPayPerConversionEligibilityFailureReasonEnum.CustomerPayPerConversionEligibilityFailureReason]
        OTHER: _ClassVar[CustomerPayPerConversionEligibilityFailureReasonEnum.CustomerPayPerConversionEligibilityFailureReason]
    UNSPECIFIED: CustomerPayPerConversionEligibilityFailureReasonEnum.CustomerPayPerConversionEligibilityFailureReason
    UNKNOWN: CustomerPayPerConversionEligibilityFailureReasonEnum.CustomerPayPerConversionEligibilityFailureReason
    NOT_ENOUGH_CONVERSIONS: CustomerPayPerConversionEligibilityFailureReasonEnum.CustomerPayPerConversionEligibilityFailureReason
    CONVERSION_LAG_TOO_HIGH: CustomerPayPerConversionEligibilityFailureReasonEnum.CustomerPayPerConversionEligibilityFailureReason
    HAS_CAMPAIGN_WITH_SHARED_BUDGET: CustomerPayPerConversionEligibilityFailureReasonEnum.CustomerPayPerConversionEligibilityFailureReason
    HAS_UPLOAD_CLICKS_CONVERSION: CustomerPayPerConversionEligibilityFailureReasonEnum.CustomerPayPerConversionEligibilityFailureReason
    AVERAGE_DAILY_SPEND_TOO_HIGH: CustomerPayPerConversionEligibilityFailureReasonEnum.CustomerPayPerConversionEligibilityFailureReason
    ANALYSIS_NOT_COMPLETE: CustomerPayPerConversionEligibilityFailureReasonEnum.CustomerPayPerConversionEligibilityFailureReason
    OTHER: CustomerPayPerConversionEligibilityFailureReasonEnum.CustomerPayPerConversionEligibilityFailureReason

    def __init__(self) -> None:
        ...