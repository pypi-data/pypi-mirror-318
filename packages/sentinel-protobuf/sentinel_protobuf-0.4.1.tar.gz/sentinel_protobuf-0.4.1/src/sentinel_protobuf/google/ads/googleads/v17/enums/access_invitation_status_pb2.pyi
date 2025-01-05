from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class AccessInvitationStatusEnum(_message.Message):
    __slots__ = ()

    class AccessInvitationStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[AccessInvitationStatusEnum.AccessInvitationStatus]
        UNKNOWN: _ClassVar[AccessInvitationStatusEnum.AccessInvitationStatus]
        PENDING: _ClassVar[AccessInvitationStatusEnum.AccessInvitationStatus]
        DECLINED: _ClassVar[AccessInvitationStatusEnum.AccessInvitationStatus]
        EXPIRED: _ClassVar[AccessInvitationStatusEnum.AccessInvitationStatus]
    UNSPECIFIED: AccessInvitationStatusEnum.AccessInvitationStatus
    UNKNOWN: AccessInvitationStatusEnum.AccessInvitationStatus
    PENDING: AccessInvitationStatusEnum.AccessInvitationStatus
    DECLINED: AccessInvitationStatusEnum.AccessInvitationStatus
    EXPIRED: AccessInvitationStatusEnum.AccessInvitationStatus

    def __init__(self) -> None:
        ...