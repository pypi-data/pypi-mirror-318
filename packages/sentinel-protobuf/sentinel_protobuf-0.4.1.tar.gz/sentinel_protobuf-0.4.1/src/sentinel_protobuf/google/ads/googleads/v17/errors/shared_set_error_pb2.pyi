from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class SharedSetErrorEnum(_message.Message):
    __slots__ = ()

    class SharedSetError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[SharedSetErrorEnum.SharedSetError]
        UNKNOWN: _ClassVar[SharedSetErrorEnum.SharedSetError]
        CUSTOMER_CANNOT_CREATE_SHARED_SET_OF_THIS_TYPE: _ClassVar[SharedSetErrorEnum.SharedSetError]
        DUPLICATE_NAME: _ClassVar[SharedSetErrorEnum.SharedSetError]
        SHARED_SET_REMOVED: _ClassVar[SharedSetErrorEnum.SharedSetError]
        SHARED_SET_IN_USE: _ClassVar[SharedSetErrorEnum.SharedSetError]
    UNSPECIFIED: SharedSetErrorEnum.SharedSetError
    UNKNOWN: SharedSetErrorEnum.SharedSetError
    CUSTOMER_CANNOT_CREATE_SHARED_SET_OF_THIS_TYPE: SharedSetErrorEnum.SharedSetError
    DUPLICATE_NAME: SharedSetErrorEnum.SharedSetError
    SHARED_SET_REMOVED: SharedSetErrorEnum.SharedSetError
    SHARED_SET_IN_USE: SharedSetErrorEnum.SharedSetError

    def __init__(self) -> None:
        ...