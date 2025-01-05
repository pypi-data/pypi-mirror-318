from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class LocalServicesVerificationStatusEnum(_message.Message):
    __slots__ = ()

    class LocalServicesVerificationStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[LocalServicesVerificationStatusEnum.LocalServicesVerificationStatus]
        UNKNOWN: _ClassVar[LocalServicesVerificationStatusEnum.LocalServicesVerificationStatus]
        NEEDS_REVIEW: _ClassVar[LocalServicesVerificationStatusEnum.LocalServicesVerificationStatus]
        FAILED: _ClassVar[LocalServicesVerificationStatusEnum.LocalServicesVerificationStatus]
        PASSED: _ClassVar[LocalServicesVerificationStatusEnum.LocalServicesVerificationStatus]
        NOT_APPLICABLE: _ClassVar[LocalServicesVerificationStatusEnum.LocalServicesVerificationStatus]
        NO_SUBMISSION: _ClassVar[LocalServicesVerificationStatusEnum.LocalServicesVerificationStatus]
        PARTIAL_SUBMISSION: _ClassVar[LocalServicesVerificationStatusEnum.LocalServicesVerificationStatus]
        PENDING_ESCALATION: _ClassVar[LocalServicesVerificationStatusEnum.LocalServicesVerificationStatus]
    UNSPECIFIED: LocalServicesVerificationStatusEnum.LocalServicesVerificationStatus
    UNKNOWN: LocalServicesVerificationStatusEnum.LocalServicesVerificationStatus
    NEEDS_REVIEW: LocalServicesVerificationStatusEnum.LocalServicesVerificationStatus
    FAILED: LocalServicesVerificationStatusEnum.LocalServicesVerificationStatus
    PASSED: LocalServicesVerificationStatusEnum.LocalServicesVerificationStatus
    NOT_APPLICABLE: LocalServicesVerificationStatusEnum.LocalServicesVerificationStatus
    NO_SUBMISSION: LocalServicesVerificationStatusEnum.LocalServicesVerificationStatus
    PARTIAL_SUBMISSION: LocalServicesVerificationStatusEnum.LocalServicesVerificationStatus
    PENDING_ESCALATION: LocalServicesVerificationStatusEnum.LocalServicesVerificationStatus

    def __init__(self) -> None:
        ...