from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class FunctionParsingErrorEnum(_message.Message):
    __slots__ = ()

    class FunctionParsingError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[FunctionParsingErrorEnum.FunctionParsingError]
        UNKNOWN: _ClassVar[FunctionParsingErrorEnum.FunctionParsingError]
        NO_MORE_INPUT: _ClassVar[FunctionParsingErrorEnum.FunctionParsingError]
        EXPECTED_CHARACTER: _ClassVar[FunctionParsingErrorEnum.FunctionParsingError]
        UNEXPECTED_SEPARATOR: _ClassVar[FunctionParsingErrorEnum.FunctionParsingError]
        UNMATCHED_LEFT_BRACKET: _ClassVar[FunctionParsingErrorEnum.FunctionParsingError]
        UNMATCHED_RIGHT_BRACKET: _ClassVar[FunctionParsingErrorEnum.FunctionParsingError]
        TOO_MANY_NESTED_FUNCTIONS: _ClassVar[FunctionParsingErrorEnum.FunctionParsingError]
        MISSING_RIGHT_HAND_OPERAND: _ClassVar[FunctionParsingErrorEnum.FunctionParsingError]
        INVALID_OPERATOR_NAME: _ClassVar[FunctionParsingErrorEnum.FunctionParsingError]
        FEED_ATTRIBUTE_OPERAND_ARGUMENT_NOT_INTEGER: _ClassVar[FunctionParsingErrorEnum.FunctionParsingError]
        NO_OPERANDS: _ClassVar[FunctionParsingErrorEnum.FunctionParsingError]
        TOO_MANY_OPERANDS: _ClassVar[FunctionParsingErrorEnum.FunctionParsingError]
    UNSPECIFIED: FunctionParsingErrorEnum.FunctionParsingError
    UNKNOWN: FunctionParsingErrorEnum.FunctionParsingError
    NO_MORE_INPUT: FunctionParsingErrorEnum.FunctionParsingError
    EXPECTED_CHARACTER: FunctionParsingErrorEnum.FunctionParsingError
    UNEXPECTED_SEPARATOR: FunctionParsingErrorEnum.FunctionParsingError
    UNMATCHED_LEFT_BRACKET: FunctionParsingErrorEnum.FunctionParsingError
    UNMATCHED_RIGHT_BRACKET: FunctionParsingErrorEnum.FunctionParsingError
    TOO_MANY_NESTED_FUNCTIONS: FunctionParsingErrorEnum.FunctionParsingError
    MISSING_RIGHT_HAND_OPERAND: FunctionParsingErrorEnum.FunctionParsingError
    INVALID_OPERATOR_NAME: FunctionParsingErrorEnum.FunctionParsingError
    FEED_ATTRIBUTE_OPERAND_ARGUMENT_NOT_INTEGER: FunctionParsingErrorEnum.FunctionParsingError
    NO_OPERANDS: FunctionParsingErrorEnum.FunctionParsingError
    TOO_MANY_OPERANDS: FunctionParsingErrorEnum.FunctionParsingError

    def __init__(self) -> None:
        ...