from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class CustomerStatusEnum(_message.Message):
    __slots__ = ()

    class CustomerStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[CustomerStatusEnum.CustomerStatus]
        UNKNOWN: _ClassVar[CustomerStatusEnum.CustomerStatus]
        ENABLED: _ClassVar[CustomerStatusEnum.CustomerStatus]
        CANCELED: _ClassVar[CustomerStatusEnum.CustomerStatus]
        SUSPENDED: _ClassVar[CustomerStatusEnum.CustomerStatus]
        CLOSED: _ClassVar[CustomerStatusEnum.CustomerStatus]
    UNSPECIFIED: CustomerStatusEnum.CustomerStatus
    UNKNOWN: CustomerStatusEnum.CustomerStatus
    ENABLED: CustomerStatusEnum.CustomerStatus
    CANCELED: CustomerStatusEnum.CustomerStatus
    SUSPENDED: CustomerStatusEnum.CustomerStatus
    CLOSED: CustomerStatusEnum.CustomerStatus

    def __init__(self) -> None:
        ...