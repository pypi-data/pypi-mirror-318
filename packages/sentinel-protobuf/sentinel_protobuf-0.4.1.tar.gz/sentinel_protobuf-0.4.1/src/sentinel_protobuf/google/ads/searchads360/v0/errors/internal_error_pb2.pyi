from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class InternalErrorEnum(_message.Message):
    __slots__ = ()

    class InternalError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[InternalErrorEnum.InternalError]
        UNKNOWN: _ClassVar[InternalErrorEnum.InternalError]
        INTERNAL_ERROR: _ClassVar[InternalErrorEnum.InternalError]
        ERROR_CODE_NOT_PUBLISHED: _ClassVar[InternalErrorEnum.InternalError]
        TRANSIENT_ERROR: _ClassVar[InternalErrorEnum.InternalError]
        DEADLINE_EXCEEDED: _ClassVar[InternalErrorEnum.InternalError]
    UNSPECIFIED: InternalErrorEnum.InternalError
    UNKNOWN: InternalErrorEnum.InternalError
    INTERNAL_ERROR: InternalErrorEnum.InternalError
    ERROR_CODE_NOT_PUBLISHED: InternalErrorEnum.InternalError
    TRANSIENT_ERROR: InternalErrorEnum.InternalError
    DEADLINE_EXCEEDED: InternalErrorEnum.InternalError

    def __init__(self) -> None:
        ...