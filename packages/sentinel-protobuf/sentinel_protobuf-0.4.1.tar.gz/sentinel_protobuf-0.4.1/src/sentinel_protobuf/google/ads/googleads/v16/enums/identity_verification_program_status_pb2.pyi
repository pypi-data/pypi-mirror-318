from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class IdentityVerificationProgramStatusEnum(_message.Message):
    __slots__ = ()

    class IdentityVerificationProgramStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[IdentityVerificationProgramStatusEnum.IdentityVerificationProgramStatus]
        UNKNOWN: _ClassVar[IdentityVerificationProgramStatusEnum.IdentityVerificationProgramStatus]
        PENDING_USER_ACTION: _ClassVar[IdentityVerificationProgramStatusEnum.IdentityVerificationProgramStatus]
        PENDING_REVIEW: _ClassVar[IdentityVerificationProgramStatusEnum.IdentityVerificationProgramStatus]
        SUCCESS: _ClassVar[IdentityVerificationProgramStatusEnum.IdentityVerificationProgramStatus]
        FAILURE: _ClassVar[IdentityVerificationProgramStatusEnum.IdentityVerificationProgramStatus]
    UNSPECIFIED: IdentityVerificationProgramStatusEnum.IdentityVerificationProgramStatus
    UNKNOWN: IdentityVerificationProgramStatusEnum.IdentityVerificationProgramStatus
    PENDING_USER_ACTION: IdentityVerificationProgramStatusEnum.IdentityVerificationProgramStatus
    PENDING_REVIEW: IdentityVerificationProgramStatusEnum.IdentityVerificationProgramStatus
    SUCCESS: IdentityVerificationProgramStatusEnum.IdentityVerificationProgramStatus
    FAILURE: IdentityVerificationProgramStatusEnum.IdentityVerificationProgramStatus

    def __init__(self) -> None:
        ...