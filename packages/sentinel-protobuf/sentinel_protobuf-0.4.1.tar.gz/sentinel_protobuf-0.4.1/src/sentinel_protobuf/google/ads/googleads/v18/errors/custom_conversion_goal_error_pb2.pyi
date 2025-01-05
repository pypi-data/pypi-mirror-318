from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class CustomConversionGoalErrorEnum(_message.Message):
    __slots__ = ()

    class CustomConversionGoalError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[CustomConversionGoalErrorEnum.CustomConversionGoalError]
        UNKNOWN: _ClassVar[CustomConversionGoalErrorEnum.CustomConversionGoalError]
        INVALID_CONVERSION_ACTION: _ClassVar[CustomConversionGoalErrorEnum.CustomConversionGoalError]
        CONVERSION_ACTION_NOT_ENABLED: _ClassVar[CustomConversionGoalErrorEnum.CustomConversionGoalError]
        CANNOT_REMOVE_LINKED_CUSTOM_CONVERSION_GOAL: _ClassVar[CustomConversionGoalErrorEnum.CustomConversionGoalError]
        CUSTOM_GOAL_DUPLICATE_NAME: _ClassVar[CustomConversionGoalErrorEnum.CustomConversionGoalError]
        DUPLICATE_CONVERSION_ACTION_LIST: _ClassVar[CustomConversionGoalErrorEnum.CustomConversionGoalError]
        NON_BIDDABLE_CONVERSION_ACTION_NOT_ELIGIBLE_FOR_CUSTOM_GOAL: _ClassVar[CustomConversionGoalErrorEnum.CustomConversionGoalError]
    UNSPECIFIED: CustomConversionGoalErrorEnum.CustomConversionGoalError
    UNKNOWN: CustomConversionGoalErrorEnum.CustomConversionGoalError
    INVALID_CONVERSION_ACTION: CustomConversionGoalErrorEnum.CustomConversionGoalError
    CONVERSION_ACTION_NOT_ENABLED: CustomConversionGoalErrorEnum.CustomConversionGoalError
    CANNOT_REMOVE_LINKED_CUSTOM_CONVERSION_GOAL: CustomConversionGoalErrorEnum.CustomConversionGoalError
    CUSTOM_GOAL_DUPLICATE_NAME: CustomConversionGoalErrorEnum.CustomConversionGoalError
    DUPLICATE_CONVERSION_ACTION_LIST: CustomConversionGoalErrorEnum.CustomConversionGoalError
    NON_BIDDABLE_CONVERSION_ACTION_NOT_ELIGIBLE_FOR_CUSTOM_GOAL: CustomConversionGoalErrorEnum.CustomConversionGoalError

    def __init__(self) -> None:
        ...