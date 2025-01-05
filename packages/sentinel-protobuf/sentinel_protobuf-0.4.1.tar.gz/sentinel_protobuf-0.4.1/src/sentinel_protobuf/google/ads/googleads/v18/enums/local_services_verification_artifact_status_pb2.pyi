from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class LocalServicesVerificationArtifactStatusEnum(_message.Message):
    __slots__ = ()

    class LocalServicesVerificationArtifactStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[LocalServicesVerificationArtifactStatusEnum.LocalServicesVerificationArtifactStatus]
        UNKNOWN: _ClassVar[LocalServicesVerificationArtifactStatusEnum.LocalServicesVerificationArtifactStatus]
        PASSED: _ClassVar[LocalServicesVerificationArtifactStatusEnum.LocalServicesVerificationArtifactStatus]
        FAILED: _ClassVar[LocalServicesVerificationArtifactStatusEnum.LocalServicesVerificationArtifactStatus]
        PENDING: _ClassVar[LocalServicesVerificationArtifactStatusEnum.LocalServicesVerificationArtifactStatus]
        NO_SUBMISSION: _ClassVar[LocalServicesVerificationArtifactStatusEnum.LocalServicesVerificationArtifactStatus]
        CANCELLED: _ClassVar[LocalServicesVerificationArtifactStatusEnum.LocalServicesVerificationArtifactStatus]
    UNSPECIFIED: LocalServicesVerificationArtifactStatusEnum.LocalServicesVerificationArtifactStatus
    UNKNOWN: LocalServicesVerificationArtifactStatusEnum.LocalServicesVerificationArtifactStatus
    PASSED: LocalServicesVerificationArtifactStatusEnum.LocalServicesVerificationArtifactStatus
    FAILED: LocalServicesVerificationArtifactStatusEnum.LocalServicesVerificationArtifactStatus
    PENDING: LocalServicesVerificationArtifactStatusEnum.LocalServicesVerificationArtifactStatus
    NO_SUBMISSION: LocalServicesVerificationArtifactStatusEnum.LocalServicesVerificationArtifactStatus
    CANCELLED: LocalServicesVerificationArtifactStatusEnum.LocalServicesVerificationArtifactStatus

    def __init__(self) -> None:
        ...