from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class FunctionErrorEnum(_message.Message):
    __slots__ = ()

    class FunctionError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[FunctionErrorEnum.FunctionError]
        UNKNOWN: _ClassVar[FunctionErrorEnum.FunctionError]
        INVALID_FUNCTION_FORMAT: _ClassVar[FunctionErrorEnum.FunctionError]
        DATA_TYPE_MISMATCH: _ClassVar[FunctionErrorEnum.FunctionError]
        INVALID_CONJUNCTION_OPERANDS: _ClassVar[FunctionErrorEnum.FunctionError]
        INVALID_NUMBER_OF_OPERANDS: _ClassVar[FunctionErrorEnum.FunctionError]
        INVALID_OPERAND_TYPE: _ClassVar[FunctionErrorEnum.FunctionError]
        INVALID_OPERATOR: _ClassVar[FunctionErrorEnum.FunctionError]
        INVALID_REQUEST_CONTEXT_TYPE: _ClassVar[FunctionErrorEnum.FunctionError]
        INVALID_FUNCTION_FOR_CALL_PLACEHOLDER: _ClassVar[FunctionErrorEnum.FunctionError]
        INVALID_FUNCTION_FOR_PLACEHOLDER: _ClassVar[FunctionErrorEnum.FunctionError]
        INVALID_OPERAND: _ClassVar[FunctionErrorEnum.FunctionError]
        MISSING_CONSTANT_OPERAND_VALUE: _ClassVar[FunctionErrorEnum.FunctionError]
        INVALID_CONSTANT_OPERAND_VALUE: _ClassVar[FunctionErrorEnum.FunctionError]
        INVALID_NESTING: _ClassVar[FunctionErrorEnum.FunctionError]
        MULTIPLE_FEED_IDS_NOT_SUPPORTED: _ClassVar[FunctionErrorEnum.FunctionError]
        INVALID_FUNCTION_FOR_FEED_WITH_FIXED_SCHEMA: _ClassVar[FunctionErrorEnum.FunctionError]
        INVALID_ATTRIBUTE_NAME: _ClassVar[FunctionErrorEnum.FunctionError]
    UNSPECIFIED: FunctionErrorEnum.FunctionError
    UNKNOWN: FunctionErrorEnum.FunctionError
    INVALID_FUNCTION_FORMAT: FunctionErrorEnum.FunctionError
    DATA_TYPE_MISMATCH: FunctionErrorEnum.FunctionError
    INVALID_CONJUNCTION_OPERANDS: FunctionErrorEnum.FunctionError
    INVALID_NUMBER_OF_OPERANDS: FunctionErrorEnum.FunctionError
    INVALID_OPERAND_TYPE: FunctionErrorEnum.FunctionError
    INVALID_OPERATOR: FunctionErrorEnum.FunctionError
    INVALID_REQUEST_CONTEXT_TYPE: FunctionErrorEnum.FunctionError
    INVALID_FUNCTION_FOR_CALL_PLACEHOLDER: FunctionErrorEnum.FunctionError
    INVALID_FUNCTION_FOR_PLACEHOLDER: FunctionErrorEnum.FunctionError
    INVALID_OPERAND: FunctionErrorEnum.FunctionError
    MISSING_CONSTANT_OPERAND_VALUE: FunctionErrorEnum.FunctionError
    INVALID_CONSTANT_OPERAND_VALUE: FunctionErrorEnum.FunctionError
    INVALID_NESTING: FunctionErrorEnum.FunctionError
    MULTIPLE_FEED_IDS_NOT_SUPPORTED: FunctionErrorEnum.FunctionError
    INVALID_FUNCTION_FOR_FEED_WITH_FIXED_SCHEMA: FunctionErrorEnum.FunctionError
    INVALID_ATTRIBUTE_NAME: FunctionErrorEnum.FunctionError

    def __init__(self) -> None:
        ...