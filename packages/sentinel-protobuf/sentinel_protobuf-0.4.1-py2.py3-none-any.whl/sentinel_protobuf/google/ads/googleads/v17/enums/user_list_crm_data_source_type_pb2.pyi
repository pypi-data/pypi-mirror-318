from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class UserListCrmDataSourceTypeEnum(_message.Message):
    __slots__ = ()

    class UserListCrmDataSourceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[UserListCrmDataSourceTypeEnum.UserListCrmDataSourceType]
        UNKNOWN: _ClassVar[UserListCrmDataSourceTypeEnum.UserListCrmDataSourceType]
        FIRST_PARTY: _ClassVar[UserListCrmDataSourceTypeEnum.UserListCrmDataSourceType]
        THIRD_PARTY_CREDIT_BUREAU: _ClassVar[UserListCrmDataSourceTypeEnum.UserListCrmDataSourceType]
        THIRD_PARTY_VOTER_FILE: _ClassVar[UserListCrmDataSourceTypeEnum.UserListCrmDataSourceType]
    UNSPECIFIED: UserListCrmDataSourceTypeEnum.UserListCrmDataSourceType
    UNKNOWN: UserListCrmDataSourceTypeEnum.UserListCrmDataSourceType
    FIRST_PARTY: UserListCrmDataSourceTypeEnum.UserListCrmDataSourceType
    THIRD_PARTY_CREDIT_BUREAU: UserListCrmDataSourceTypeEnum.UserListCrmDataSourceType
    THIRD_PARTY_VOTER_FILE: UserListCrmDataSourceTypeEnum.UserListCrmDataSourceType

    def __init__(self) -> None:
        ...