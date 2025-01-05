from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class FieldErrorEnum(_message.Message):
    __slots__ = ()

    class FieldError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[FieldErrorEnum.FieldError]
        UNKNOWN: _ClassVar[FieldErrorEnum.FieldError]
        REQUIRED: _ClassVar[FieldErrorEnum.FieldError]
        IMMUTABLE_FIELD: _ClassVar[FieldErrorEnum.FieldError]
        INVALID_VALUE: _ClassVar[FieldErrorEnum.FieldError]
        VALUE_MUST_BE_UNSET: _ClassVar[FieldErrorEnum.FieldError]
        REQUIRED_NONEMPTY_LIST: _ClassVar[FieldErrorEnum.FieldError]
        FIELD_CANNOT_BE_CLEARED: _ClassVar[FieldErrorEnum.FieldError]
        BLOCKED_VALUE: _ClassVar[FieldErrorEnum.FieldError]
        FIELD_CAN_ONLY_BE_CLEARED: _ClassVar[FieldErrorEnum.FieldError]
    UNSPECIFIED: FieldErrorEnum.FieldError
    UNKNOWN: FieldErrorEnum.FieldError
    REQUIRED: FieldErrorEnum.FieldError
    IMMUTABLE_FIELD: FieldErrorEnum.FieldError
    INVALID_VALUE: FieldErrorEnum.FieldError
    VALUE_MUST_BE_UNSET: FieldErrorEnum.FieldError
    REQUIRED_NONEMPTY_LIST: FieldErrorEnum.FieldError
    FIELD_CANNOT_BE_CLEARED: FieldErrorEnum.FieldError
    BLOCKED_VALUE: FieldErrorEnum.FieldError
    FIELD_CAN_ONLY_BE_CLEARED: FieldErrorEnum.FieldError

    def __init__(self) -> None:
        ...