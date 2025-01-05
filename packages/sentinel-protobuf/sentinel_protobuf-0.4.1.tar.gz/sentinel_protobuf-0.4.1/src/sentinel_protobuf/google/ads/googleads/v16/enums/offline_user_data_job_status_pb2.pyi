from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class OfflineUserDataJobStatusEnum(_message.Message):
    __slots__ = ()

    class OfflineUserDataJobStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[OfflineUserDataJobStatusEnum.OfflineUserDataJobStatus]
        UNKNOWN: _ClassVar[OfflineUserDataJobStatusEnum.OfflineUserDataJobStatus]
        PENDING: _ClassVar[OfflineUserDataJobStatusEnum.OfflineUserDataJobStatus]
        RUNNING: _ClassVar[OfflineUserDataJobStatusEnum.OfflineUserDataJobStatus]
        SUCCESS: _ClassVar[OfflineUserDataJobStatusEnum.OfflineUserDataJobStatus]
        FAILED: _ClassVar[OfflineUserDataJobStatusEnum.OfflineUserDataJobStatus]
    UNSPECIFIED: OfflineUserDataJobStatusEnum.OfflineUserDataJobStatus
    UNKNOWN: OfflineUserDataJobStatusEnum.OfflineUserDataJobStatus
    PENDING: OfflineUserDataJobStatusEnum.OfflineUserDataJobStatus
    RUNNING: OfflineUserDataJobStatusEnum.OfflineUserDataJobStatus
    SUCCESS: OfflineUserDataJobStatusEnum.OfflineUserDataJobStatus
    FAILED: OfflineUserDataJobStatusEnum.OfflineUserDataJobStatus

    def __init__(self) -> None:
        ...