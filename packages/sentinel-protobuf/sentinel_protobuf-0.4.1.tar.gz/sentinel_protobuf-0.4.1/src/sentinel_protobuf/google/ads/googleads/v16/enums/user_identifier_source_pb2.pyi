from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class UserIdentifierSourceEnum(_message.Message):
    __slots__ = ()

    class UserIdentifierSource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[UserIdentifierSourceEnum.UserIdentifierSource]
        UNKNOWN: _ClassVar[UserIdentifierSourceEnum.UserIdentifierSource]
        FIRST_PARTY: _ClassVar[UserIdentifierSourceEnum.UserIdentifierSource]
        THIRD_PARTY: _ClassVar[UserIdentifierSourceEnum.UserIdentifierSource]
    UNSPECIFIED: UserIdentifierSourceEnum.UserIdentifierSource
    UNKNOWN: UserIdentifierSourceEnum.UserIdentifierSource
    FIRST_PARTY: UserIdentifierSourceEnum.UserIdentifierSource
    THIRD_PARTY: UserIdentifierSourceEnum.UserIdentifierSource

    def __init__(self) -> None:
        ...