from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class UserListStringRuleItemOperatorEnum(_message.Message):
    __slots__ = ()

    class UserListStringRuleItemOperator(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[UserListStringRuleItemOperatorEnum.UserListStringRuleItemOperator]
        UNKNOWN: _ClassVar[UserListStringRuleItemOperatorEnum.UserListStringRuleItemOperator]
        CONTAINS: _ClassVar[UserListStringRuleItemOperatorEnum.UserListStringRuleItemOperator]
        EQUALS: _ClassVar[UserListStringRuleItemOperatorEnum.UserListStringRuleItemOperator]
        STARTS_WITH: _ClassVar[UserListStringRuleItemOperatorEnum.UserListStringRuleItemOperator]
        ENDS_WITH: _ClassVar[UserListStringRuleItemOperatorEnum.UserListStringRuleItemOperator]
        NOT_EQUALS: _ClassVar[UserListStringRuleItemOperatorEnum.UserListStringRuleItemOperator]
        NOT_CONTAINS: _ClassVar[UserListStringRuleItemOperatorEnum.UserListStringRuleItemOperator]
        NOT_STARTS_WITH: _ClassVar[UserListStringRuleItemOperatorEnum.UserListStringRuleItemOperator]
        NOT_ENDS_WITH: _ClassVar[UserListStringRuleItemOperatorEnum.UserListStringRuleItemOperator]
    UNSPECIFIED: UserListStringRuleItemOperatorEnum.UserListStringRuleItemOperator
    UNKNOWN: UserListStringRuleItemOperatorEnum.UserListStringRuleItemOperator
    CONTAINS: UserListStringRuleItemOperatorEnum.UserListStringRuleItemOperator
    EQUALS: UserListStringRuleItemOperatorEnum.UserListStringRuleItemOperator
    STARTS_WITH: UserListStringRuleItemOperatorEnum.UserListStringRuleItemOperator
    ENDS_WITH: UserListStringRuleItemOperatorEnum.UserListStringRuleItemOperator
    NOT_EQUALS: UserListStringRuleItemOperatorEnum.UserListStringRuleItemOperator
    NOT_CONTAINS: UserListStringRuleItemOperatorEnum.UserListStringRuleItemOperator
    NOT_STARTS_WITH: UserListStringRuleItemOperatorEnum.UserListStringRuleItemOperator
    NOT_ENDS_WITH: UserListStringRuleItemOperatorEnum.UserListStringRuleItemOperator

    def __init__(self) -> None:
        ...