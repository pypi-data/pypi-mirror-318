from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class IdentityVerificationErrorEnum(_message.Message):
    __slots__ = ()

    class IdentityVerificationError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[IdentityVerificationErrorEnum.IdentityVerificationError]
        UNKNOWN: _ClassVar[IdentityVerificationErrorEnum.IdentityVerificationError]
        NO_EFFECTIVE_BILLING: _ClassVar[IdentityVerificationErrorEnum.IdentityVerificationError]
        BILLING_NOT_ON_MONTHLY_INVOICING: _ClassVar[IdentityVerificationErrorEnum.IdentityVerificationError]
        VERIFICATION_ALREADY_STARTED: _ClassVar[IdentityVerificationErrorEnum.IdentityVerificationError]
    UNSPECIFIED: IdentityVerificationErrorEnum.IdentityVerificationError
    UNKNOWN: IdentityVerificationErrorEnum.IdentityVerificationError
    NO_EFFECTIVE_BILLING: IdentityVerificationErrorEnum.IdentityVerificationError
    BILLING_NOT_ON_MONTHLY_INVOICING: IdentityVerificationErrorEnum.IdentityVerificationError
    VERIFICATION_ALREADY_STARTED: IdentityVerificationErrorEnum.IdentityVerificationError

    def __init__(self) -> None:
        ...