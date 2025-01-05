from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class UserListTypeEnum(_message.Message):
    __slots__ = ()

    class UserListType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[UserListTypeEnum.UserListType]
        UNKNOWN: _ClassVar[UserListTypeEnum.UserListType]
        REMARKETING: _ClassVar[UserListTypeEnum.UserListType]
        LOGICAL: _ClassVar[UserListTypeEnum.UserListType]
        EXTERNAL_REMARKETING: _ClassVar[UserListTypeEnum.UserListType]
        RULE_BASED: _ClassVar[UserListTypeEnum.UserListType]
        SIMILAR: _ClassVar[UserListTypeEnum.UserListType]
        CRM_BASED: _ClassVar[UserListTypeEnum.UserListType]
        LOOKALIKE: _ClassVar[UserListTypeEnum.UserListType]
    UNSPECIFIED: UserListTypeEnum.UserListType
    UNKNOWN: UserListTypeEnum.UserListType
    REMARKETING: UserListTypeEnum.UserListType
    LOGICAL: UserListTypeEnum.UserListType
    EXTERNAL_REMARKETING: UserListTypeEnum.UserListType
    RULE_BASED: UserListTypeEnum.UserListType
    SIMILAR: UserListTypeEnum.UserListType
    CRM_BASED: UserListTypeEnum.UserListType
    LOOKALIKE: UserListTypeEnum.UserListType

    def __init__(self) -> None:
        ...