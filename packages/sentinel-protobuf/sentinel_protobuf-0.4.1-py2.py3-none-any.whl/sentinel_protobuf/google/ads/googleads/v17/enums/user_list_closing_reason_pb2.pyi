from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class UserListClosingReasonEnum(_message.Message):
    __slots__ = ()

    class UserListClosingReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[UserListClosingReasonEnum.UserListClosingReason]
        UNKNOWN: _ClassVar[UserListClosingReasonEnum.UserListClosingReason]
        UNUSED: _ClassVar[UserListClosingReasonEnum.UserListClosingReason]
    UNSPECIFIED: UserListClosingReasonEnum.UserListClosingReason
    UNKNOWN: UserListClosingReasonEnum.UserListClosingReason
    UNUSED: UserListClosingReasonEnum.UserListClosingReason

    def __init__(self) -> None:
        ...