from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class BatchJobStatusEnum(_message.Message):
    __slots__ = ()

    class BatchJobStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[BatchJobStatusEnum.BatchJobStatus]
        UNKNOWN: _ClassVar[BatchJobStatusEnum.BatchJobStatus]
        PENDING: _ClassVar[BatchJobStatusEnum.BatchJobStatus]
        RUNNING: _ClassVar[BatchJobStatusEnum.BatchJobStatus]
        DONE: _ClassVar[BatchJobStatusEnum.BatchJobStatus]
    UNSPECIFIED: BatchJobStatusEnum.BatchJobStatus
    UNKNOWN: BatchJobStatusEnum.BatchJobStatus
    PENDING: BatchJobStatusEnum.BatchJobStatus
    RUNNING: BatchJobStatusEnum.BatchJobStatus
    DONE: BatchJobStatusEnum.BatchJobStatus

    def __init__(self) -> None:
        ...