from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class ListOperationErrorEnum(_message.Message):
    __slots__ = ()

    class ListOperationError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ListOperationErrorEnum.ListOperationError]
        UNKNOWN: _ClassVar[ListOperationErrorEnum.ListOperationError]
        REQUIRED_FIELD_MISSING: _ClassVar[ListOperationErrorEnum.ListOperationError]
        DUPLICATE_VALUES: _ClassVar[ListOperationErrorEnum.ListOperationError]
    UNSPECIFIED: ListOperationErrorEnum.ListOperationError
    UNKNOWN: ListOperationErrorEnum.ListOperationError
    REQUIRED_FIELD_MISSING: ListOperationErrorEnum.ListOperationError
    DUPLICATE_VALUES: ListOperationErrorEnum.ListOperationError

    def __init__(self) -> None:
        ...