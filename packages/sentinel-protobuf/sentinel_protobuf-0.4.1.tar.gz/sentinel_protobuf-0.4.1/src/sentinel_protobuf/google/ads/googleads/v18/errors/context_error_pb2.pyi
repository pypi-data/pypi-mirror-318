from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class ContextErrorEnum(_message.Message):
    __slots__ = ()

    class ContextError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ContextErrorEnum.ContextError]
        UNKNOWN: _ClassVar[ContextErrorEnum.ContextError]
        OPERATION_NOT_PERMITTED_FOR_CONTEXT: _ClassVar[ContextErrorEnum.ContextError]
        OPERATION_NOT_PERMITTED_FOR_REMOVED_RESOURCE: _ClassVar[ContextErrorEnum.ContextError]
    UNSPECIFIED: ContextErrorEnum.ContextError
    UNKNOWN: ContextErrorEnum.ContextError
    OPERATION_NOT_PERMITTED_FOR_CONTEXT: ContextErrorEnum.ContextError
    OPERATION_NOT_PERMITTED_FOR_REMOVED_RESOURCE: ContextErrorEnum.ContextError

    def __init__(self) -> None:
        ...