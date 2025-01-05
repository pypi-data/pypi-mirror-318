from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class SharedSetStatusEnum(_message.Message):
    __slots__ = ()

    class SharedSetStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[SharedSetStatusEnum.SharedSetStatus]
        UNKNOWN: _ClassVar[SharedSetStatusEnum.SharedSetStatus]
        ENABLED: _ClassVar[SharedSetStatusEnum.SharedSetStatus]
        REMOVED: _ClassVar[SharedSetStatusEnum.SharedSetStatus]
    UNSPECIFIED: SharedSetStatusEnum.SharedSetStatus
    UNKNOWN: SharedSetStatusEnum.SharedSetStatus
    ENABLED: SharedSetStatusEnum.SharedSetStatus
    REMOVED: SharedSetStatusEnum.SharedSetStatus

    def __init__(self) -> None:
        ...