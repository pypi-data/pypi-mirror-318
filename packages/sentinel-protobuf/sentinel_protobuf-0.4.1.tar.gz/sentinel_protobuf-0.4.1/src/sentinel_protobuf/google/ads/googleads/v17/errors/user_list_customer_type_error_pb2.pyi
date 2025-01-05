from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class UserListCustomerTypeErrorEnum(_message.Message):
    __slots__ = ()

    class UserListCustomerTypeError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[UserListCustomerTypeErrorEnum.UserListCustomerTypeError]
        UNKNOWN: _ClassVar[UserListCustomerTypeErrorEnum.UserListCustomerTypeError]
        CONFLICTING_CUSTOMER_TYPES: _ClassVar[UserListCustomerTypeErrorEnum.UserListCustomerTypeError]
        NO_ACCESS_TO_USER_LIST: _ClassVar[UserListCustomerTypeErrorEnum.UserListCustomerTypeError]
        USERLIST_NOT_ELIGIBLE: _ClassVar[UserListCustomerTypeErrorEnum.UserListCustomerTypeError]
        CONVERSION_TRACKING_NOT_ENABLED_OR_NOT_MCC_MANAGER_ACCOUNT: _ClassVar[UserListCustomerTypeErrorEnum.UserListCustomerTypeError]
        TOO_MANY_USER_LISTS_FOR_THE_CUSTOMER_TYPE: _ClassVar[UserListCustomerTypeErrorEnum.UserListCustomerTypeError]
    UNSPECIFIED: UserListCustomerTypeErrorEnum.UserListCustomerTypeError
    UNKNOWN: UserListCustomerTypeErrorEnum.UserListCustomerTypeError
    CONFLICTING_CUSTOMER_TYPES: UserListCustomerTypeErrorEnum.UserListCustomerTypeError
    NO_ACCESS_TO_USER_LIST: UserListCustomerTypeErrorEnum.UserListCustomerTypeError
    USERLIST_NOT_ELIGIBLE: UserListCustomerTypeErrorEnum.UserListCustomerTypeError
    CONVERSION_TRACKING_NOT_ENABLED_OR_NOT_MCC_MANAGER_ACCOUNT: UserListCustomerTypeErrorEnum.UserListCustomerTypeError
    TOO_MANY_USER_LISTS_FOR_THE_CUSTOMER_TYPE: UserListCustomerTypeErrorEnum.UserListCustomerTypeError

    def __init__(self) -> None:
        ...