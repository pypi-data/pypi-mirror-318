from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class AccountTypeEnum(_message.Message):
    __slots__ = ()

    class AccountType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[AccountTypeEnum.AccountType]
        UNKNOWN: _ClassVar[AccountTypeEnum.AccountType]
        BAIDU: _ClassVar[AccountTypeEnum.AccountType]
        ENGINE_TRACK: _ClassVar[AccountTypeEnum.AccountType]
        FACEBOOK: _ClassVar[AccountTypeEnum.AccountType]
        FACEBOOK_GATEWAY: _ClassVar[AccountTypeEnum.AccountType]
        GOOGLE_ADS: _ClassVar[AccountTypeEnum.AccountType]
        MICROSOFT: _ClassVar[AccountTypeEnum.AccountType]
        SEARCH_ADS_360: _ClassVar[AccountTypeEnum.AccountType]
        YAHOO_JAPAN: _ClassVar[AccountTypeEnum.AccountType]
    UNSPECIFIED: AccountTypeEnum.AccountType
    UNKNOWN: AccountTypeEnum.AccountType
    BAIDU: AccountTypeEnum.AccountType
    ENGINE_TRACK: AccountTypeEnum.AccountType
    FACEBOOK: AccountTypeEnum.AccountType
    FACEBOOK_GATEWAY: AccountTypeEnum.AccountType
    GOOGLE_ADS: AccountTypeEnum.AccountType
    MICROSOFT: AccountTypeEnum.AccountType
    SEARCH_ADS_360: AccountTypeEnum.AccountType
    YAHOO_JAPAN: AccountTypeEnum.AccountType

    def __init__(self) -> None:
        ...