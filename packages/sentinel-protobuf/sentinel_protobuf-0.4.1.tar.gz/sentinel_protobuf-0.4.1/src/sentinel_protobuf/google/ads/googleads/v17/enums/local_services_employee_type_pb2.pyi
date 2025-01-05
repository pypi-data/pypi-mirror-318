from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class LocalServicesEmployeeTypeEnum(_message.Message):
    __slots__ = ()

    class LocalServicesEmployeeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[LocalServicesEmployeeTypeEnum.LocalServicesEmployeeType]
        UNKNOWN: _ClassVar[LocalServicesEmployeeTypeEnum.LocalServicesEmployeeType]
        BUSINESS_OWNER: _ClassVar[LocalServicesEmployeeTypeEnum.LocalServicesEmployeeType]
        EMPLOYEE: _ClassVar[LocalServicesEmployeeTypeEnum.LocalServicesEmployeeType]
    UNSPECIFIED: LocalServicesEmployeeTypeEnum.LocalServicesEmployeeType
    UNKNOWN: LocalServicesEmployeeTypeEnum.LocalServicesEmployeeType
    BUSINESS_OWNER: LocalServicesEmployeeTypeEnum.LocalServicesEmployeeType
    EMPLOYEE: LocalServicesEmployeeTypeEnum.LocalServicesEmployeeType

    def __init__(self) -> None:
        ...