from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class ConversionValueRuleSetErrorEnum(_message.Message):
    __slots__ = ()

    class ConversionValueRuleSetError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ConversionValueRuleSetErrorEnum.ConversionValueRuleSetError]
        UNKNOWN: _ClassVar[ConversionValueRuleSetErrorEnum.ConversionValueRuleSetError]
        CONFLICTING_VALUE_RULE_CONDITIONS: _ClassVar[ConversionValueRuleSetErrorEnum.ConversionValueRuleSetError]
        INVALID_VALUE_RULE: _ClassVar[ConversionValueRuleSetErrorEnum.ConversionValueRuleSetError]
        DIMENSIONS_UPDATE_ONLY_ALLOW_APPEND: _ClassVar[ConversionValueRuleSetErrorEnum.ConversionValueRuleSetError]
        CONDITION_TYPE_NOT_ALLOWED: _ClassVar[ConversionValueRuleSetErrorEnum.ConversionValueRuleSetError]
        DUPLICATE_DIMENSIONS: _ClassVar[ConversionValueRuleSetErrorEnum.ConversionValueRuleSetError]
        INVALID_CAMPAIGN_ID: _ClassVar[ConversionValueRuleSetErrorEnum.ConversionValueRuleSetError]
        CANNOT_PAUSE_UNLESS_ALL_VALUE_RULES_ARE_PAUSED: _ClassVar[ConversionValueRuleSetErrorEnum.ConversionValueRuleSetError]
        SHOULD_PAUSE_WHEN_ALL_VALUE_RULES_ARE_PAUSED: _ClassVar[ConversionValueRuleSetErrorEnum.ConversionValueRuleSetError]
        VALUE_RULES_NOT_SUPPORTED_FOR_CAMPAIGN_TYPE: _ClassVar[ConversionValueRuleSetErrorEnum.ConversionValueRuleSetError]
        INELIGIBLE_CONVERSION_ACTION_CATEGORIES: _ClassVar[ConversionValueRuleSetErrorEnum.ConversionValueRuleSetError]
        DIMENSION_NO_CONDITION_USED_WITH_OTHER_DIMENSIONS: _ClassVar[ConversionValueRuleSetErrorEnum.ConversionValueRuleSetError]
        DIMENSION_NO_CONDITION_NOT_ALLOWED: _ClassVar[ConversionValueRuleSetErrorEnum.ConversionValueRuleSetError]
        UNSUPPORTED_CONVERSION_ACTION_CATEGORIES: _ClassVar[ConversionValueRuleSetErrorEnum.ConversionValueRuleSetError]
        DIMENSION_NOT_SUPPORTED_FOR_CAMPAIGN_TYPE: _ClassVar[ConversionValueRuleSetErrorEnum.ConversionValueRuleSetError]
    UNSPECIFIED: ConversionValueRuleSetErrorEnum.ConversionValueRuleSetError
    UNKNOWN: ConversionValueRuleSetErrorEnum.ConversionValueRuleSetError
    CONFLICTING_VALUE_RULE_CONDITIONS: ConversionValueRuleSetErrorEnum.ConversionValueRuleSetError
    INVALID_VALUE_RULE: ConversionValueRuleSetErrorEnum.ConversionValueRuleSetError
    DIMENSIONS_UPDATE_ONLY_ALLOW_APPEND: ConversionValueRuleSetErrorEnum.ConversionValueRuleSetError
    CONDITION_TYPE_NOT_ALLOWED: ConversionValueRuleSetErrorEnum.ConversionValueRuleSetError
    DUPLICATE_DIMENSIONS: ConversionValueRuleSetErrorEnum.ConversionValueRuleSetError
    INVALID_CAMPAIGN_ID: ConversionValueRuleSetErrorEnum.ConversionValueRuleSetError
    CANNOT_PAUSE_UNLESS_ALL_VALUE_RULES_ARE_PAUSED: ConversionValueRuleSetErrorEnum.ConversionValueRuleSetError
    SHOULD_PAUSE_WHEN_ALL_VALUE_RULES_ARE_PAUSED: ConversionValueRuleSetErrorEnum.ConversionValueRuleSetError
    VALUE_RULES_NOT_SUPPORTED_FOR_CAMPAIGN_TYPE: ConversionValueRuleSetErrorEnum.ConversionValueRuleSetError
    INELIGIBLE_CONVERSION_ACTION_CATEGORIES: ConversionValueRuleSetErrorEnum.ConversionValueRuleSetError
    DIMENSION_NO_CONDITION_USED_WITH_OTHER_DIMENSIONS: ConversionValueRuleSetErrorEnum.ConversionValueRuleSetError
    DIMENSION_NO_CONDITION_NOT_ALLOWED: ConversionValueRuleSetErrorEnum.ConversionValueRuleSetError
    UNSUPPORTED_CONVERSION_ACTION_CATEGORIES: ConversionValueRuleSetErrorEnum.ConversionValueRuleSetError
    DIMENSION_NOT_SUPPORTED_FOR_CAMPAIGN_TYPE: ConversionValueRuleSetErrorEnum.ConversionValueRuleSetError

    def __init__(self) -> None:
        ...