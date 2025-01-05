from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class NotAllowlistedErrorEnum(_message.Message):
    __slots__ = ()

    class NotAllowlistedError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[NotAllowlistedErrorEnum.NotAllowlistedError]
        UNKNOWN: _ClassVar[NotAllowlistedErrorEnum.NotAllowlistedError]
        CUSTOMER_NOT_ALLOWLISTED_FOR_THIS_FEATURE: _ClassVar[NotAllowlistedErrorEnum.NotAllowlistedError]
    UNSPECIFIED: NotAllowlistedErrorEnum.NotAllowlistedError
    UNKNOWN: NotAllowlistedErrorEnum.NotAllowlistedError
    CUSTOMER_NOT_ALLOWLISTED_FOR_THIS_FEATURE: NotAllowlistedErrorEnum.NotAllowlistedError

    def __init__(self) -> None:
        ...