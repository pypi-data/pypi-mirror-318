from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class IdentityVerificationProgramEnum(_message.Message):
    __slots__ = ()

    class IdentityVerificationProgram(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[IdentityVerificationProgramEnum.IdentityVerificationProgram]
        UNKNOWN: _ClassVar[IdentityVerificationProgramEnum.IdentityVerificationProgram]
        ADVERTISER_IDENTITY_VERIFICATION: _ClassVar[IdentityVerificationProgramEnum.IdentityVerificationProgram]
    UNSPECIFIED: IdentityVerificationProgramEnum.IdentityVerificationProgram
    UNKNOWN: IdentityVerificationProgramEnum.IdentityVerificationProgram
    ADVERTISER_IDENTITY_VERIFICATION: IdentityVerificationProgramEnum.IdentityVerificationProgram

    def __init__(self) -> None:
        ...