from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class UserListLogicalRuleOperatorEnum(_message.Message):
    __slots__ = ()

    class UserListLogicalRuleOperator(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[UserListLogicalRuleOperatorEnum.UserListLogicalRuleOperator]
        UNKNOWN: _ClassVar[UserListLogicalRuleOperatorEnum.UserListLogicalRuleOperator]
        ALL: _ClassVar[UserListLogicalRuleOperatorEnum.UserListLogicalRuleOperator]
        ANY: _ClassVar[UserListLogicalRuleOperatorEnum.UserListLogicalRuleOperator]
        NONE: _ClassVar[UserListLogicalRuleOperatorEnum.UserListLogicalRuleOperator]
    UNSPECIFIED: UserListLogicalRuleOperatorEnum.UserListLogicalRuleOperator
    UNKNOWN: UserListLogicalRuleOperatorEnum.UserListLogicalRuleOperator
    ALL: UserListLogicalRuleOperatorEnum.UserListLogicalRuleOperator
    ANY: UserListLogicalRuleOperatorEnum.UserListLogicalRuleOperator
    NONE: UserListLogicalRuleOperatorEnum.UserListLogicalRuleOperator

    def __init__(self) -> None:
        ...