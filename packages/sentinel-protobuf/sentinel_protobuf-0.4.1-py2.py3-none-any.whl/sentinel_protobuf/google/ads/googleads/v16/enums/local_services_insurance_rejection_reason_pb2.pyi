from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class LocalServicesInsuranceRejectionReasonEnum(_message.Message):
    __slots__ = ()

    class LocalServicesInsuranceRejectionReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[LocalServicesInsuranceRejectionReasonEnum.LocalServicesInsuranceRejectionReason]
        UNKNOWN: _ClassVar[LocalServicesInsuranceRejectionReasonEnum.LocalServicesInsuranceRejectionReason]
        BUSINESS_NAME_MISMATCH: _ClassVar[LocalServicesInsuranceRejectionReasonEnum.LocalServicesInsuranceRejectionReason]
        INSURANCE_AMOUNT_INSUFFICIENT: _ClassVar[LocalServicesInsuranceRejectionReasonEnum.LocalServicesInsuranceRejectionReason]
        EXPIRED: _ClassVar[LocalServicesInsuranceRejectionReasonEnum.LocalServicesInsuranceRejectionReason]
        NO_SIGNATURE: _ClassVar[LocalServicesInsuranceRejectionReasonEnum.LocalServicesInsuranceRejectionReason]
        NO_POLICY_NUMBER: _ClassVar[LocalServicesInsuranceRejectionReasonEnum.LocalServicesInsuranceRejectionReason]
        NO_COMMERCIAL_GENERAL_LIABILITY: _ClassVar[LocalServicesInsuranceRejectionReasonEnum.LocalServicesInsuranceRejectionReason]
        EDITABLE_FORMAT: _ClassVar[LocalServicesInsuranceRejectionReasonEnum.LocalServicesInsuranceRejectionReason]
        CATEGORY_MISMATCH: _ClassVar[LocalServicesInsuranceRejectionReasonEnum.LocalServicesInsuranceRejectionReason]
        MISSING_EXPIRATION_DATE: _ClassVar[LocalServicesInsuranceRejectionReasonEnum.LocalServicesInsuranceRejectionReason]
        POOR_QUALITY: _ClassVar[LocalServicesInsuranceRejectionReasonEnum.LocalServicesInsuranceRejectionReason]
        POTENTIALLY_EDITED: _ClassVar[LocalServicesInsuranceRejectionReasonEnum.LocalServicesInsuranceRejectionReason]
        WRONG_DOCUMENT_TYPE: _ClassVar[LocalServicesInsuranceRejectionReasonEnum.LocalServicesInsuranceRejectionReason]
        NON_FINAL: _ClassVar[LocalServicesInsuranceRejectionReasonEnum.LocalServicesInsuranceRejectionReason]
        OTHER: _ClassVar[LocalServicesInsuranceRejectionReasonEnum.LocalServicesInsuranceRejectionReason]
    UNSPECIFIED: LocalServicesInsuranceRejectionReasonEnum.LocalServicesInsuranceRejectionReason
    UNKNOWN: LocalServicesInsuranceRejectionReasonEnum.LocalServicesInsuranceRejectionReason
    BUSINESS_NAME_MISMATCH: LocalServicesInsuranceRejectionReasonEnum.LocalServicesInsuranceRejectionReason
    INSURANCE_AMOUNT_INSUFFICIENT: LocalServicesInsuranceRejectionReasonEnum.LocalServicesInsuranceRejectionReason
    EXPIRED: LocalServicesInsuranceRejectionReasonEnum.LocalServicesInsuranceRejectionReason
    NO_SIGNATURE: LocalServicesInsuranceRejectionReasonEnum.LocalServicesInsuranceRejectionReason
    NO_POLICY_NUMBER: LocalServicesInsuranceRejectionReasonEnum.LocalServicesInsuranceRejectionReason
    NO_COMMERCIAL_GENERAL_LIABILITY: LocalServicesInsuranceRejectionReasonEnum.LocalServicesInsuranceRejectionReason
    EDITABLE_FORMAT: LocalServicesInsuranceRejectionReasonEnum.LocalServicesInsuranceRejectionReason
    CATEGORY_MISMATCH: LocalServicesInsuranceRejectionReasonEnum.LocalServicesInsuranceRejectionReason
    MISSING_EXPIRATION_DATE: LocalServicesInsuranceRejectionReasonEnum.LocalServicesInsuranceRejectionReason
    POOR_QUALITY: LocalServicesInsuranceRejectionReasonEnum.LocalServicesInsuranceRejectionReason
    POTENTIALLY_EDITED: LocalServicesInsuranceRejectionReasonEnum.LocalServicesInsuranceRejectionReason
    WRONG_DOCUMENT_TYPE: LocalServicesInsuranceRejectionReasonEnum.LocalServicesInsuranceRejectionReason
    NON_FINAL: LocalServicesInsuranceRejectionReasonEnum.LocalServicesInsuranceRejectionReason
    OTHER: LocalServicesInsuranceRejectionReasonEnum.LocalServicesInsuranceRejectionReason

    def __init__(self) -> None:
        ...