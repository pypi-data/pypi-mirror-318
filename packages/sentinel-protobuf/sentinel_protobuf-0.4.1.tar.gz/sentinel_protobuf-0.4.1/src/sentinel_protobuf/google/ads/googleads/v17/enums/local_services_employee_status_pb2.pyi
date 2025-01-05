from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class LocalServicesEmployeeStatusEnum(_message.Message):
    __slots__ = ()

    class LocalServicesEmployeeStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[LocalServicesEmployeeStatusEnum.LocalServicesEmployeeStatus]
        UNKNOWN: _ClassVar[LocalServicesEmployeeStatusEnum.LocalServicesEmployeeStatus]
        ENABLED: _ClassVar[LocalServicesEmployeeStatusEnum.LocalServicesEmployeeStatus]
        REMOVED: _ClassVar[LocalServicesEmployeeStatusEnum.LocalServicesEmployeeStatus]
    UNSPECIFIED: LocalServicesEmployeeStatusEnum.LocalServicesEmployeeStatus
    UNKNOWN: LocalServicesEmployeeStatusEnum.LocalServicesEmployeeStatus
    ENABLED: LocalServicesEmployeeStatusEnum.LocalServicesEmployeeStatus
    REMOVED: LocalServicesEmployeeStatusEnum.LocalServicesEmployeeStatus

    def __init__(self) -> None:
        ...