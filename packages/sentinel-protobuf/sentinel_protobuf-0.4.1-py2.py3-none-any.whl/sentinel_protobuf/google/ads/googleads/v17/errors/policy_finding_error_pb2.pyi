from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class PolicyFindingErrorEnum(_message.Message):
    __slots__ = ()

    class PolicyFindingError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[PolicyFindingErrorEnum.PolicyFindingError]
        UNKNOWN: _ClassVar[PolicyFindingErrorEnum.PolicyFindingError]
        POLICY_FINDING: _ClassVar[PolicyFindingErrorEnum.PolicyFindingError]
        POLICY_TOPIC_NOT_FOUND: _ClassVar[PolicyFindingErrorEnum.PolicyFindingError]
    UNSPECIFIED: PolicyFindingErrorEnum.PolicyFindingError
    UNKNOWN: PolicyFindingErrorEnum.PolicyFindingError
    POLICY_FINDING: PolicyFindingErrorEnum.PolicyFindingError
    POLICY_TOPIC_NOT_FOUND: PolicyFindingErrorEnum.PolicyFindingError

    def __init__(self) -> None:
        ...