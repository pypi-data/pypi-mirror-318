from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class BrandRequestRejectionReasonEnum(_message.Message):
    __slots__ = ()

    class BrandRequestRejectionReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[BrandRequestRejectionReasonEnum.BrandRequestRejectionReason]
        UNKNOWN: _ClassVar[BrandRequestRejectionReasonEnum.BrandRequestRejectionReason]
        EXISTING_BRAND: _ClassVar[BrandRequestRejectionReasonEnum.BrandRequestRejectionReason]
        EXISTING_BRAND_VARIANT: _ClassVar[BrandRequestRejectionReasonEnum.BrandRequestRejectionReason]
        INCORRECT_INFORMATION: _ClassVar[BrandRequestRejectionReasonEnum.BrandRequestRejectionReason]
        NOT_A_BRAND: _ClassVar[BrandRequestRejectionReasonEnum.BrandRequestRejectionReason]
    UNSPECIFIED: BrandRequestRejectionReasonEnum.BrandRequestRejectionReason
    UNKNOWN: BrandRequestRejectionReasonEnum.BrandRequestRejectionReason
    EXISTING_BRAND: BrandRequestRejectionReasonEnum.BrandRequestRejectionReason
    EXISTING_BRAND_VARIANT: BrandRequestRejectionReasonEnum.BrandRequestRejectionReason
    INCORRECT_INFORMATION: BrandRequestRejectionReasonEnum.BrandRequestRejectionReason
    NOT_A_BRAND: BrandRequestRejectionReasonEnum.BrandRequestRejectionReason

    def __init__(self) -> None:
        ...