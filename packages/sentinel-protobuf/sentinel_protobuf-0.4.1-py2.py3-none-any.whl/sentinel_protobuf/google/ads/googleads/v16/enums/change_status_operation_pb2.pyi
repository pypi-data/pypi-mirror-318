from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class ChangeStatusOperationEnum(_message.Message):
    __slots__ = ()

    class ChangeStatusOperation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ChangeStatusOperationEnum.ChangeStatusOperation]
        UNKNOWN: _ClassVar[ChangeStatusOperationEnum.ChangeStatusOperation]
        ADDED: _ClassVar[ChangeStatusOperationEnum.ChangeStatusOperation]
        CHANGED: _ClassVar[ChangeStatusOperationEnum.ChangeStatusOperation]
        REMOVED: _ClassVar[ChangeStatusOperationEnum.ChangeStatusOperation]
    UNSPECIFIED: ChangeStatusOperationEnum.ChangeStatusOperation
    UNKNOWN: ChangeStatusOperationEnum.ChangeStatusOperation
    ADDED: ChangeStatusOperationEnum.ChangeStatusOperation
    CHANGED: ChangeStatusOperationEnum.ChangeStatusOperation
    REMOVED: ChangeStatusOperationEnum.ChangeStatusOperation

    def __init__(self) -> None:
        ...