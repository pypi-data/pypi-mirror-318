from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class PolicyValidationParameterErrorEnum(_message.Message):
    __slots__ = ()

    class PolicyValidationParameterError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[PolicyValidationParameterErrorEnum.PolicyValidationParameterError]
        UNKNOWN: _ClassVar[PolicyValidationParameterErrorEnum.PolicyValidationParameterError]
        UNSUPPORTED_AD_TYPE_FOR_IGNORABLE_POLICY_TOPICS: _ClassVar[PolicyValidationParameterErrorEnum.PolicyValidationParameterError]
        UNSUPPORTED_AD_TYPE_FOR_EXEMPT_POLICY_VIOLATION_KEYS: _ClassVar[PolicyValidationParameterErrorEnum.PolicyValidationParameterError]
        CANNOT_SET_BOTH_IGNORABLE_POLICY_TOPICS_AND_EXEMPT_POLICY_VIOLATION_KEYS: _ClassVar[PolicyValidationParameterErrorEnum.PolicyValidationParameterError]
    UNSPECIFIED: PolicyValidationParameterErrorEnum.PolicyValidationParameterError
    UNKNOWN: PolicyValidationParameterErrorEnum.PolicyValidationParameterError
    UNSUPPORTED_AD_TYPE_FOR_IGNORABLE_POLICY_TOPICS: PolicyValidationParameterErrorEnum.PolicyValidationParameterError
    UNSUPPORTED_AD_TYPE_FOR_EXEMPT_POLICY_VIOLATION_KEYS: PolicyValidationParameterErrorEnum.PolicyValidationParameterError
    CANNOT_SET_BOTH_IGNORABLE_POLICY_TOPICS_AND_EXEMPT_POLICY_VIOLATION_KEYS: PolicyValidationParameterErrorEnum.PolicyValidationParameterError

    def __init__(self) -> None:
        ...