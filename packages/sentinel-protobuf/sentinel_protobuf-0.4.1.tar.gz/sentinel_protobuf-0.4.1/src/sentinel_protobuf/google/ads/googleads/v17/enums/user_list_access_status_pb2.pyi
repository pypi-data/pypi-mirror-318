from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class UserListAccessStatusEnum(_message.Message):
    __slots__ = ()

    class UserListAccessStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[UserListAccessStatusEnum.UserListAccessStatus]
        UNKNOWN: _ClassVar[UserListAccessStatusEnum.UserListAccessStatus]
        ENABLED: _ClassVar[UserListAccessStatusEnum.UserListAccessStatus]
        DISABLED: _ClassVar[UserListAccessStatusEnum.UserListAccessStatus]
    UNSPECIFIED: UserListAccessStatusEnum.UserListAccessStatus
    UNKNOWN: UserListAccessStatusEnum.UserListAccessStatus
    ENABLED: UserListAccessStatusEnum.UserListAccessStatus
    DISABLED: UserListAccessStatusEnum.UserListAccessStatus

    def __init__(self) -> None:
        ...