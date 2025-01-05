from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class UserListDateRuleItemOperatorEnum(_message.Message):
    __slots__ = ()

    class UserListDateRuleItemOperator(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[UserListDateRuleItemOperatorEnum.UserListDateRuleItemOperator]
        UNKNOWN: _ClassVar[UserListDateRuleItemOperatorEnum.UserListDateRuleItemOperator]
        EQUALS: _ClassVar[UserListDateRuleItemOperatorEnum.UserListDateRuleItemOperator]
        NOT_EQUALS: _ClassVar[UserListDateRuleItemOperatorEnum.UserListDateRuleItemOperator]
        BEFORE: _ClassVar[UserListDateRuleItemOperatorEnum.UserListDateRuleItemOperator]
        AFTER: _ClassVar[UserListDateRuleItemOperatorEnum.UserListDateRuleItemOperator]
    UNSPECIFIED: UserListDateRuleItemOperatorEnum.UserListDateRuleItemOperator
    UNKNOWN: UserListDateRuleItemOperatorEnum.UserListDateRuleItemOperator
    EQUALS: UserListDateRuleItemOperatorEnum.UserListDateRuleItemOperator
    NOT_EQUALS: UserListDateRuleItemOperatorEnum.UserListDateRuleItemOperator
    BEFORE: UserListDateRuleItemOperatorEnum.UserListDateRuleItemOperator
    AFTER: UserListDateRuleItemOperatorEnum.UserListDateRuleItemOperator

    def __init__(self) -> None:
        ...