from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class TimeTypeEnum(_message.Message):
    __slots__ = ()

    class TimeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[TimeTypeEnum.TimeType]
        UNKNOWN: _ClassVar[TimeTypeEnum.TimeType]
        NOW: _ClassVar[TimeTypeEnum.TimeType]
        FOREVER: _ClassVar[TimeTypeEnum.TimeType]
    UNSPECIFIED: TimeTypeEnum.TimeType
    UNKNOWN: TimeTypeEnum.TimeType
    NOW: TimeTypeEnum.TimeType
    FOREVER: TimeTypeEnum.TimeType

    def __init__(self) -> None:
        ...