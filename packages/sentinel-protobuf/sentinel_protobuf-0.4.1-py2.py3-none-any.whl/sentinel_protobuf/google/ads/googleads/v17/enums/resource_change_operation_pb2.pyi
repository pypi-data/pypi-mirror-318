from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class ResourceChangeOperationEnum(_message.Message):
    __slots__ = ()

    class ResourceChangeOperation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ResourceChangeOperationEnum.ResourceChangeOperation]
        UNKNOWN: _ClassVar[ResourceChangeOperationEnum.ResourceChangeOperation]
        CREATE: _ClassVar[ResourceChangeOperationEnum.ResourceChangeOperation]
        UPDATE: _ClassVar[ResourceChangeOperationEnum.ResourceChangeOperation]
        REMOVE: _ClassVar[ResourceChangeOperationEnum.ResourceChangeOperation]
    UNSPECIFIED: ResourceChangeOperationEnum.ResourceChangeOperation
    UNKNOWN: ResourceChangeOperationEnum.ResourceChangeOperation
    CREATE: ResourceChangeOperationEnum.ResourceChangeOperation
    UPDATE: ResourceChangeOperationEnum.ResourceChangeOperation
    REMOVE: ResourceChangeOperationEnum.ResourceChangeOperation

    def __init__(self) -> None:
        ...