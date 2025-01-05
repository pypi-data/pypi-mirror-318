from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class SystemManagedResourceSourceEnum(_message.Message):
    __slots__ = ()

    class SystemManagedResourceSource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[SystemManagedResourceSourceEnum.SystemManagedResourceSource]
        UNKNOWN: _ClassVar[SystemManagedResourceSourceEnum.SystemManagedResourceSource]
        AD_VARIATIONS: _ClassVar[SystemManagedResourceSourceEnum.SystemManagedResourceSource]
    UNSPECIFIED: SystemManagedResourceSourceEnum.SystemManagedResourceSource
    UNKNOWN: SystemManagedResourceSourceEnum.SystemManagedResourceSource
    AD_VARIATIONS: SystemManagedResourceSourceEnum.SystemManagedResourceSource

    def __init__(self) -> None:
        ...