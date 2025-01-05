from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class CustomerLifecycleGoalErrorEnum(_message.Message):
    __slots__ = ()

    class CustomerLifecycleGoalError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[CustomerLifecycleGoalErrorEnum.CustomerLifecycleGoalError]
        UNKNOWN: _ClassVar[CustomerLifecycleGoalErrorEnum.CustomerLifecycleGoalError]
        CUSTOMER_ACQUISITION_VALUE_MISSING: _ClassVar[CustomerLifecycleGoalErrorEnum.CustomerLifecycleGoalError]
        CUSTOMER_ACQUISITION_INVALID_VALUE: _ClassVar[CustomerLifecycleGoalErrorEnum.CustomerLifecycleGoalError]
        CUSTOMER_ACQUISITION_INVALID_HIGH_LIFETIME_VALUE: _ClassVar[CustomerLifecycleGoalErrorEnum.CustomerLifecycleGoalError]
        CUSTOMER_ACQUISITION_VALUE_CANNOT_BE_CLEARED: _ClassVar[CustomerLifecycleGoalErrorEnum.CustomerLifecycleGoalError]
        CUSTOMER_ACQUISITION_HIGH_LIFETIME_VALUE_CANNOT_BE_CLEARED: _ClassVar[CustomerLifecycleGoalErrorEnum.CustomerLifecycleGoalError]
        INVALID_EXISTING_USER_LIST: _ClassVar[CustomerLifecycleGoalErrorEnum.CustomerLifecycleGoalError]
        INVALID_HIGH_LIFETIME_VALUE_USER_LIST: _ClassVar[CustomerLifecycleGoalErrorEnum.CustomerLifecycleGoalError]
    UNSPECIFIED: CustomerLifecycleGoalErrorEnum.CustomerLifecycleGoalError
    UNKNOWN: CustomerLifecycleGoalErrorEnum.CustomerLifecycleGoalError
    CUSTOMER_ACQUISITION_VALUE_MISSING: CustomerLifecycleGoalErrorEnum.CustomerLifecycleGoalError
    CUSTOMER_ACQUISITION_INVALID_VALUE: CustomerLifecycleGoalErrorEnum.CustomerLifecycleGoalError
    CUSTOMER_ACQUISITION_INVALID_HIGH_LIFETIME_VALUE: CustomerLifecycleGoalErrorEnum.CustomerLifecycleGoalError
    CUSTOMER_ACQUISITION_VALUE_CANNOT_BE_CLEARED: CustomerLifecycleGoalErrorEnum.CustomerLifecycleGoalError
    CUSTOMER_ACQUISITION_HIGH_LIFETIME_VALUE_CANNOT_BE_CLEARED: CustomerLifecycleGoalErrorEnum.CustomerLifecycleGoalError
    INVALID_EXISTING_USER_LIST: CustomerLifecycleGoalErrorEnum.CustomerLifecycleGoalError
    INVALID_HIGH_LIFETIME_VALUE_USER_LIST: CustomerLifecycleGoalErrorEnum.CustomerLifecycleGoalError

    def __init__(self) -> None:
        ...