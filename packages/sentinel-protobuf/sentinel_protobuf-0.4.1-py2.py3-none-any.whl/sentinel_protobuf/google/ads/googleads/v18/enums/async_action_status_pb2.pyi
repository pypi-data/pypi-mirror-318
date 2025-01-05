from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class AsyncActionStatusEnum(_message.Message):
    __slots__ = ()

    class AsyncActionStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[AsyncActionStatusEnum.AsyncActionStatus]
        UNKNOWN: _ClassVar[AsyncActionStatusEnum.AsyncActionStatus]
        NOT_STARTED: _ClassVar[AsyncActionStatusEnum.AsyncActionStatus]
        IN_PROGRESS: _ClassVar[AsyncActionStatusEnum.AsyncActionStatus]
        COMPLETED: _ClassVar[AsyncActionStatusEnum.AsyncActionStatus]
        FAILED: _ClassVar[AsyncActionStatusEnum.AsyncActionStatus]
        COMPLETED_WITH_WARNING: _ClassVar[AsyncActionStatusEnum.AsyncActionStatus]
    UNSPECIFIED: AsyncActionStatusEnum.AsyncActionStatus
    UNKNOWN: AsyncActionStatusEnum.AsyncActionStatus
    NOT_STARTED: AsyncActionStatusEnum.AsyncActionStatus
    IN_PROGRESS: AsyncActionStatusEnum.AsyncActionStatus
    COMPLETED: AsyncActionStatusEnum.AsyncActionStatus
    FAILED: AsyncActionStatusEnum.AsyncActionStatus
    COMPLETED_WITH_WARNING: AsyncActionStatusEnum.AsyncActionStatus

    def __init__(self) -> None:
        ...