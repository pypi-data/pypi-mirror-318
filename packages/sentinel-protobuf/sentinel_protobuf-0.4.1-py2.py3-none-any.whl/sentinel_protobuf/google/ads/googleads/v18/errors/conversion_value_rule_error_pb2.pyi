from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class ConversionValueRuleErrorEnum(_message.Message):
    __slots__ = ()

    class ConversionValueRuleError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ConversionValueRuleErrorEnum.ConversionValueRuleError]
        UNKNOWN: _ClassVar[ConversionValueRuleErrorEnum.ConversionValueRuleError]
        INVALID_GEO_TARGET_CONSTANT: _ClassVar[ConversionValueRuleErrorEnum.ConversionValueRuleError]
        CONFLICTING_INCLUDED_AND_EXCLUDED_GEO_TARGET: _ClassVar[ConversionValueRuleErrorEnum.ConversionValueRuleError]
        CONFLICTING_CONDITIONS: _ClassVar[ConversionValueRuleErrorEnum.ConversionValueRuleError]
        CANNOT_REMOVE_IF_INCLUDED_IN_VALUE_RULE_SET: _ClassVar[ConversionValueRuleErrorEnum.ConversionValueRuleError]
        CONDITION_NOT_ALLOWED: _ClassVar[ConversionValueRuleErrorEnum.ConversionValueRuleError]
        FIELD_MUST_BE_UNSET: _ClassVar[ConversionValueRuleErrorEnum.ConversionValueRuleError]
        CANNOT_PAUSE_UNLESS_VALUE_RULE_SET_IS_PAUSED: _ClassVar[ConversionValueRuleErrorEnum.ConversionValueRuleError]
        UNTARGETABLE_GEO_TARGET: _ClassVar[ConversionValueRuleErrorEnum.ConversionValueRuleError]
        INVALID_AUDIENCE_USER_LIST: _ClassVar[ConversionValueRuleErrorEnum.ConversionValueRuleError]
        INACCESSIBLE_USER_LIST: _ClassVar[ConversionValueRuleErrorEnum.ConversionValueRuleError]
        INVALID_AUDIENCE_USER_INTEREST: _ClassVar[ConversionValueRuleErrorEnum.ConversionValueRuleError]
        CANNOT_ADD_RULE_WITH_STATUS_REMOVED: _ClassVar[ConversionValueRuleErrorEnum.ConversionValueRuleError]
        NO_DAY_OF_WEEK_SELECTED: _ClassVar[ConversionValueRuleErrorEnum.ConversionValueRuleError]
    UNSPECIFIED: ConversionValueRuleErrorEnum.ConversionValueRuleError
    UNKNOWN: ConversionValueRuleErrorEnum.ConversionValueRuleError
    INVALID_GEO_TARGET_CONSTANT: ConversionValueRuleErrorEnum.ConversionValueRuleError
    CONFLICTING_INCLUDED_AND_EXCLUDED_GEO_TARGET: ConversionValueRuleErrorEnum.ConversionValueRuleError
    CONFLICTING_CONDITIONS: ConversionValueRuleErrorEnum.ConversionValueRuleError
    CANNOT_REMOVE_IF_INCLUDED_IN_VALUE_RULE_SET: ConversionValueRuleErrorEnum.ConversionValueRuleError
    CONDITION_NOT_ALLOWED: ConversionValueRuleErrorEnum.ConversionValueRuleError
    FIELD_MUST_BE_UNSET: ConversionValueRuleErrorEnum.ConversionValueRuleError
    CANNOT_PAUSE_UNLESS_VALUE_RULE_SET_IS_PAUSED: ConversionValueRuleErrorEnum.ConversionValueRuleError
    UNTARGETABLE_GEO_TARGET: ConversionValueRuleErrorEnum.ConversionValueRuleError
    INVALID_AUDIENCE_USER_LIST: ConversionValueRuleErrorEnum.ConversionValueRuleError
    INACCESSIBLE_USER_LIST: ConversionValueRuleErrorEnum.ConversionValueRuleError
    INVALID_AUDIENCE_USER_INTEREST: ConversionValueRuleErrorEnum.ConversionValueRuleError
    CANNOT_ADD_RULE_WITH_STATUS_REMOVED: ConversionValueRuleErrorEnum.ConversionValueRuleError
    NO_DAY_OF_WEEK_SELECTED: ConversionValueRuleErrorEnum.ConversionValueRuleError

    def __init__(self) -> None:
        ...