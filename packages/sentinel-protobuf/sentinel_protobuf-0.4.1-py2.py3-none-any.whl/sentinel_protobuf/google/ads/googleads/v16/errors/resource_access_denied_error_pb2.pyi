from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class ResourceAccessDeniedErrorEnum(_message.Message):
    __slots__ = ()

    class ResourceAccessDeniedError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ResourceAccessDeniedErrorEnum.ResourceAccessDeniedError]
        UNKNOWN: _ClassVar[ResourceAccessDeniedErrorEnum.ResourceAccessDeniedError]
        WRITE_ACCESS_DENIED: _ClassVar[ResourceAccessDeniedErrorEnum.ResourceAccessDeniedError]
    UNSPECIFIED: ResourceAccessDeniedErrorEnum.ResourceAccessDeniedError
    UNKNOWN: ResourceAccessDeniedErrorEnum.ResourceAccessDeniedError
    WRITE_ACCESS_DENIED: ResourceAccessDeniedErrorEnum.ResourceAccessDeniedError

    def __init__(self) -> None:
        ...