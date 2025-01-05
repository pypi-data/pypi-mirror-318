from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class PhoneVerificationState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PHONE_VERIFICATION_STATE_UNSPECIFIED: _ClassVar[PhoneVerificationState]
    PHONE_VERIFICATION_STATE_VERIFIED: _ClassVar[PhoneVerificationState]
    PHONE_VERIFICATION_STATE_UNVERIFIED: _ClassVar[PhoneVerificationState]
PHONE_VERIFICATION_STATE_UNSPECIFIED: PhoneVerificationState
PHONE_VERIFICATION_STATE_VERIFIED: PhoneVerificationState
PHONE_VERIFICATION_STATE_UNVERIFIED: PhoneVerificationState