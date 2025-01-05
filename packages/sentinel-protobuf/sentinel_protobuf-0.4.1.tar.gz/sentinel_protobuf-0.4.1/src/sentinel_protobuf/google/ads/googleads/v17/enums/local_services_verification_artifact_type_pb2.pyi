from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class LocalServicesVerificationArtifactTypeEnum(_message.Message):
    __slots__ = ()

    class LocalServicesVerificationArtifactType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[LocalServicesVerificationArtifactTypeEnum.LocalServicesVerificationArtifactType]
        UNKNOWN: _ClassVar[LocalServicesVerificationArtifactTypeEnum.LocalServicesVerificationArtifactType]
        BACKGROUND_CHECK: _ClassVar[LocalServicesVerificationArtifactTypeEnum.LocalServicesVerificationArtifactType]
        INSURANCE: _ClassVar[LocalServicesVerificationArtifactTypeEnum.LocalServicesVerificationArtifactType]
        LICENSE: _ClassVar[LocalServicesVerificationArtifactTypeEnum.LocalServicesVerificationArtifactType]
        BUSINESS_REGISTRATION_CHECK: _ClassVar[LocalServicesVerificationArtifactTypeEnum.LocalServicesVerificationArtifactType]
    UNSPECIFIED: LocalServicesVerificationArtifactTypeEnum.LocalServicesVerificationArtifactType
    UNKNOWN: LocalServicesVerificationArtifactTypeEnum.LocalServicesVerificationArtifactType
    BACKGROUND_CHECK: LocalServicesVerificationArtifactTypeEnum.LocalServicesVerificationArtifactType
    INSURANCE: LocalServicesVerificationArtifactTypeEnum.LocalServicesVerificationArtifactType
    LICENSE: LocalServicesVerificationArtifactTypeEnum.LocalServicesVerificationArtifactType
    BUSINESS_REGISTRATION_CHECK: LocalServicesVerificationArtifactTypeEnum.LocalServicesVerificationArtifactType

    def __init__(self) -> None:
        ...