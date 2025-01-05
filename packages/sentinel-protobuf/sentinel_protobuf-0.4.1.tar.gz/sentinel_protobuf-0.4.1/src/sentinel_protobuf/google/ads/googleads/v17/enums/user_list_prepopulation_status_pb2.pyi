from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class UserListPrepopulationStatusEnum(_message.Message):
    __slots__ = ()

    class UserListPrepopulationStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[UserListPrepopulationStatusEnum.UserListPrepopulationStatus]
        UNKNOWN: _ClassVar[UserListPrepopulationStatusEnum.UserListPrepopulationStatus]
        REQUESTED: _ClassVar[UserListPrepopulationStatusEnum.UserListPrepopulationStatus]
        FINISHED: _ClassVar[UserListPrepopulationStatusEnum.UserListPrepopulationStatus]
        FAILED: _ClassVar[UserListPrepopulationStatusEnum.UserListPrepopulationStatus]
    UNSPECIFIED: UserListPrepopulationStatusEnum.UserListPrepopulationStatus
    UNKNOWN: UserListPrepopulationStatusEnum.UserListPrepopulationStatus
    REQUESTED: UserListPrepopulationStatusEnum.UserListPrepopulationStatus
    FINISHED: UserListPrepopulationStatusEnum.UserListPrepopulationStatus
    FAILED: UserListPrepopulationStatusEnum.UserListPrepopulationStatus

    def __init__(self) -> None:
        ...