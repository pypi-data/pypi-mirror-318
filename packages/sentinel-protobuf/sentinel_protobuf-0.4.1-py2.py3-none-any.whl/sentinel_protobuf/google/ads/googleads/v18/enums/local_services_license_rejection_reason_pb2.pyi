from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class LocalServicesLicenseRejectionReasonEnum(_message.Message):
    __slots__ = ()

    class LocalServicesLicenseRejectionReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[LocalServicesLicenseRejectionReasonEnum.LocalServicesLicenseRejectionReason]
        UNKNOWN: _ClassVar[LocalServicesLicenseRejectionReasonEnum.LocalServicesLicenseRejectionReason]
        BUSINESS_NAME_MISMATCH: _ClassVar[LocalServicesLicenseRejectionReasonEnum.LocalServicesLicenseRejectionReason]
        UNAUTHORIZED: _ClassVar[LocalServicesLicenseRejectionReasonEnum.LocalServicesLicenseRejectionReason]
        EXPIRED: _ClassVar[LocalServicesLicenseRejectionReasonEnum.LocalServicesLicenseRejectionReason]
        POOR_QUALITY: _ClassVar[LocalServicesLicenseRejectionReasonEnum.LocalServicesLicenseRejectionReason]
        UNVERIFIABLE: _ClassVar[LocalServicesLicenseRejectionReasonEnum.LocalServicesLicenseRejectionReason]
        WRONG_DOCUMENT_OR_ID: _ClassVar[LocalServicesLicenseRejectionReasonEnum.LocalServicesLicenseRejectionReason]
        OTHER: _ClassVar[LocalServicesLicenseRejectionReasonEnum.LocalServicesLicenseRejectionReason]
    UNSPECIFIED: LocalServicesLicenseRejectionReasonEnum.LocalServicesLicenseRejectionReason
    UNKNOWN: LocalServicesLicenseRejectionReasonEnum.LocalServicesLicenseRejectionReason
    BUSINESS_NAME_MISMATCH: LocalServicesLicenseRejectionReasonEnum.LocalServicesLicenseRejectionReason
    UNAUTHORIZED: LocalServicesLicenseRejectionReasonEnum.LocalServicesLicenseRejectionReason
    EXPIRED: LocalServicesLicenseRejectionReasonEnum.LocalServicesLicenseRejectionReason
    POOR_QUALITY: LocalServicesLicenseRejectionReasonEnum.LocalServicesLicenseRejectionReason
    UNVERIFIABLE: LocalServicesLicenseRejectionReasonEnum.LocalServicesLicenseRejectionReason
    WRONG_DOCUMENT_OR_ID: LocalServicesLicenseRejectionReasonEnum.LocalServicesLicenseRejectionReason
    OTHER: LocalServicesLicenseRejectionReasonEnum.LocalServicesLicenseRejectionReason

    def __init__(self) -> None:
        ...