from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class UserListFlexibleRuleOperatorEnum(_message.Message):
    __slots__ = ()

    class UserListFlexibleRuleOperator(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[UserListFlexibleRuleOperatorEnum.UserListFlexibleRuleOperator]
        UNKNOWN: _ClassVar[UserListFlexibleRuleOperatorEnum.UserListFlexibleRuleOperator]
        AND: _ClassVar[UserListFlexibleRuleOperatorEnum.UserListFlexibleRuleOperator]
        OR: _ClassVar[UserListFlexibleRuleOperatorEnum.UserListFlexibleRuleOperator]
    UNSPECIFIED: UserListFlexibleRuleOperatorEnum.UserListFlexibleRuleOperator
    UNKNOWN: UserListFlexibleRuleOperatorEnum.UserListFlexibleRuleOperator
    AND: UserListFlexibleRuleOperatorEnum.UserListFlexibleRuleOperator
    OR: UserListFlexibleRuleOperatorEnum.UserListFlexibleRuleOperator

    def __init__(self) -> None:
        ...