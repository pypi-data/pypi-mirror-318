from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class AccountLinkErrorEnum(_message.Message):
    __slots__ = ()

    class AccountLinkError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[AccountLinkErrorEnum.AccountLinkError]
        UNKNOWN: _ClassVar[AccountLinkErrorEnum.AccountLinkError]
        INVALID_STATUS: _ClassVar[AccountLinkErrorEnum.AccountLinkError]
        PERMISSION_DENIED: _ClassVar[AccountLinkErrorEnum.AccountLinkError]
    UNSPECIFIED: AccountLinkErrorEnum.AccountLinkError
    UNKNOWN: AccountLinkErrorEnum.AccountLinkError
    INVALID_STATUS: AccountLinkErrorEnum.AccountLinkError
    PERMISSION_DENIED: AccountLinkErrorEnum.AccountLinkError

    def __init__(self) -> None:
        ...