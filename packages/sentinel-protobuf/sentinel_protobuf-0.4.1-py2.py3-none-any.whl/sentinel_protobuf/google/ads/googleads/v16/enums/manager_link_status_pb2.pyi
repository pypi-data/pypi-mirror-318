from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class ManagerLinkStatusEnum(_message.Message):
    __slots__ = ()

    class ManagerLinkStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ManagerLinkStatusEnum.ManagerLinkStatus]
        UNKNOWN: _ClassVar[ManagerLinkStatusEnum.ManagerLinkStatus]
        ACTIVE: _ClassVar[ManagerLinkStatusEnum.ManagerLinkStatus]
        INACTIVE: _ClassVar[ManagerLinkStatusEnum.ManagerLinkStatus]
        PENDING: _ClassVar[ManagerLinkStatusEnum.ManagerLinkStatus]
        REFUSED: _ClassVar[ManagerLinkStatusEnum.ManagerLinkStatus]
        CANCELED: _ClassVar[ManagerLinkStatusEnum.ManagerLinkStatus]
    UNSPECIFIED: ManagerLinkStatusEnum.ManagerLinkStatus
    UNKNOWN: ManagerLinkStatusEnum.ManagerLinkStatus
    ACTIVE: ManagerLinkStatusEnum.ManagerLinkStatus
    INACTIVE: ManagerLinkStatusEnum.ManagerLinkStatus
    PENDING: ManagerLinkStatusEnum.ManagerLinkStatus
    REFUSED: ManagerLinkStatusEnum.ManagerLinkStatus
    CANCELED: ManagerLinkStatusEnum.ManagerLinkStatus

    def __init__(self) -> None:
        ...