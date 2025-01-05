from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class UserListNumberRuleItemOperatorEnum(_message.Message):
    __slots__ = ()

    class UserListNumberRuleItemOperator(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[UserListNumberRuleItemOperatorEnum.UserListNumberRuleItemOperator]
        UNKNOWN: _ClassVar[UserListNumberRuleItemOperatorEnum.UserListNumberRuleItemOperator]
        GREATER_THAN: _ClassVar[UserListNumberRuleItemOperatorEnum.UserListNumberRuleItemOperator]
        GREATER_THAN_OR_EQUAL: _ClassVar[UserListNumberRuleItemOperatorEnum.UserListNumberRuleItemOperator]
        EQUALS: _ClassVar[UserListNumberRuleItemOperatorEnum.UserListNumberRuleItemOperator]
        NOT_EQUALS: _ClassVar[UserListNumberRuleItemOperatorEnum.UserListNumberRuleItemOperator]
        LESS_THAN: _ClassVar[UserListNumberRuleItemOperatorEnum.UserListNumberRuleItemOperator]
        LESS_THAN_OR_EQUAL: _ClassVar[UserListNumberRuleItemOperatorEnum.UserListNumberRuleItemOperator]
    UNSPECIFIED: UserListNumberRuleItemOperatorEnum.UserListNumberRuleItemOperator
    UNKNOWN: UserListNumberRuleItemOperatorEnum.UserListNumberRuleItemOperator
    GREATER_THAN: UserListNumberRuleItemOperatorEnum.UserListNumberRuleItemOperator
    GREATER_THAN_OR_EQUAL: UserListNumberRuleItemOperatorEnum.UserListNumberRuleItemOperator
    EQUALS: UserListNumberRuleItemOperatorEnum.UserListNumberRuleItemOperator
    NOT_EQUALS: UserListNumberRuleItemOperatorEnum.UserListNumberRuleItemOperator
    LESS_THAN: UserListNumberRuleItemOperatorEnum.UserListNumberRuleItemOperator
    LESS_THAN_OR_EQUAL: UserListNumberRuleItemOperatorEnum.UserListNumberRuleItemOperator

    def __init__(self) -> None:
        ...