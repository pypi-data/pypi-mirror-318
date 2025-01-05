from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class UserListMembershipStatusEnum(_message.Message):
    __slots__ = ()

    class UserListMembershipStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[UserListMembershipStatusEnum.UserListMembershipStatus]
        UNKNOWN: _ClassVar[UserListMembershipStatusEnum.UserListMembershipStatus]
        OPEN: _ClassVar[UserListMembershipStatusEnum.UserListMembershipStatus]
        CLOSED: _ClassVar[UserListMembershipStatusEnum.UserListMembershipStatus]
    UNSPECIFIED: UserListMembershipStatusEnum.UserListMembershipStatus
    UNKNOWN: UserListMembershipStatusEnum.UserListMembershipStatus
    OPEN: UserListMembershipStatusEnum.UserListMembershipStatus
    CLOSED: UserListMembershipStatusEnum.UserListMembershipStatus

    def __init__(self) -> None:
        ...