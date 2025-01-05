from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class PolicyViolationErrorEnum(_message.Message):
    __slots__ = ()

    class PolicyViolationError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[PolicyViolationErrorEnum.PolicyViolationError]
        UNKNOWN: _ClassVar[PolicyViolationErrorEnum.PolicyViolationError]
        POLICY_ERROR: _ClassVar[PolicyViolationErrorEnum.PolicyViolationError]
    UNSPECIFIED: PolicyViolationErrorEnum.PolicyViolationError
    UNKNOWN: PolicyViolationErrorEnum.PolicyViolationError
    POLICY_ERROR: PolicyViolationErrorEnum.PolicyViolationError

    def __init__(self) -> None:
        ...