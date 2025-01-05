from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class RoleStatusEnum(_message.Message):
    __slots__ = ()

    class RoleStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ROLE_STATUS_UNSPECIFIED: _ClassVar[RoleStatusEnum.RoleStatus]
        ACTIVE: _ClassVar[RoleStatusEnum.RoleStatus]
        INACTIVE: _ClassVar[RoleStatusEnum.RoleStatus]
    ROLE_STATUS_UNSPECIFIED: RoleStatusEnum.RoleStatus
    ACTIVE: RoleStatusEnum.RoleStatus
    INACTIVE: RoleStatusEnum.RoleStatus

    def __init__(self) -> None:
        ...