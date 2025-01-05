from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class DataLinkStatusEnum(_message.Message):
    __slots__ = ()

    class DataLinkStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[DataLinkStatusEnum.DataLinkStatus]
        UNKNOWN: _ClassVar[DataLinkStatusEnum.DataLinkStatus]
        REQUESTED: _ClassVar[DataLinkStatusEnum.DataLinkStatus]
        PENDING_APPROVAL: _ClassVar[DataLinkStatusEnum.DataLinkStatus]
        ENABLED: _ClassVar[DataLinkStatusEnum.DataLinkStatus]
        DISABLED: _ClassVar[DataLinkStatusEnum.DataLinkStatus]
        REVOKED: _ClassVar[DataLinkStatusEnum.DataLinkStatus]
        REJECTED: _ClassVar[DataLinkStatusEnum.DataLinkStatus]
    UNSPECIFIED: DataLinkStatusEnum.DataLinkStatus
    UNKNOWN: DataLinkStatusEnum.DataLinkStatus
    REQUESTED: DataLinkStatusEnum.DataLinkStatus
    PENDING_APPROVAL: DataLinkStatusEnum.DataLinkStatus
    ENABLED: DataLinkStatusEnum.DataLinkStatus
    DISABLED: DataLinkStatusEnum.DataLinkStatus
    REVOKED: DataLinkStatusEnum.DataLinkStatus
    REJECTED: DataLinkStatusEnum.DataLinkStatus

    def __init__(self) -> None:
        ...