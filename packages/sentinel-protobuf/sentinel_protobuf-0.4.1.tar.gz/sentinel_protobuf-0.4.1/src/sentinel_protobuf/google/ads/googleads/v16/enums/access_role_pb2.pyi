from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class AccessRoleEnum(_message.Message):
    __slots__ = ()

    class AccessRole(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[AccessRoleEnum.AccessRole]
        UNKNOWN: _ClassVar[AccessRoleEnum.AccessRole]
        ADMIN: _ClassVar[AccessRoleEnum.AccessRole]
        STANDARD: _ClassVar[AccessRoleEnum.AccessRole]
        READ_ONLY: _ClassVar[AccessRoleEnum.AccessRole]
        EMAIL_ONLY: _ClassVar[AccessRoleEnum.AccessRole]
    UNSPECIFIED: AccessRoleEnum.AccessRole
    UNKNOWN: AccessRoleEnum.AccessRole
    ADMIN: AccessRoleEnum.AccessRole
    STANDARD: AccessRoleEnum.AccessRole
    READ_ONLY: AccessRoleEnum.AccessRole
    EMAIL_ONLY: AccessRoleEnum.AccessRole

    def __init__(self) -> None:
        ...