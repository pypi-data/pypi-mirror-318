from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class UserListRuleTypeEnum(_message.Message):
    __slots__ = ()

    class UserListRuleType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[UserListRuleTypeEnum.UserListRuleType]
        UNKNOWN: _ClassVar[UserListRuleTypeEnum.UserListRuleType]
        AND_OF_ORS: _ClassVar[UserListRuleTypeEnum.UserListRuleType]
        OR_OF_ANDS: _ClassVar[UserListRuleTypeEnum.UserListRuleType]
    UNSPECIFIED: UserListRuleTypeEnum.UserListRuleType
    UNKNOWN: UserListRuleTypeEnum.UserListRuleType
    AND_OF_ORS: UserListRuleTypeEnum.UserListRuleType
    OR_OF_ANDS: UserListRuleTypeEnum.UserListRuleType

    def __init__(self) -> None:
        ...