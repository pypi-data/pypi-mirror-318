from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class TimeUnitEnum(_message.Message):
    __slots__ = ()

    class TimeUnit(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TIME_UNIT_UNSPECIFIED: _ClassVar[TimeUnitEnum.TimeUnit]
        MINUTE: _ClassVar[TimeUnitEnum.TimeUnit]
        HOUR: _ClassVar[TimeUnitEnum.TimeUnit]
        DAY: _ClassVar[TimeUnitEnum.TimeUnit]
        WEEK: _ClassVar[TimeUnitEnum.TimeUnit]
        MONTH: _ClassVar[TimeUnitEnum.TimeUnit]
        LIFETIME: _ClassVar[TimeUnitEnum.TimeUnit]
        POD: _ClassVar[TimeUnitEnum.TimeUnit]
        STREAM: _ClassVar[TimeUnitEnum.TimeUnit]
    TIME_UNIT_UNSPECIFIED: TimeUnitEnum.TimeUnit
    MINUTE: TimeUnitEnum.TimeUnit
    HOUR: TimeUnitEnum.TimeUnit
    DAY: TimeUnitEnum.TimeUnit
    WEEK: TimeUnitEnum.TimeUnit
    MONTH: TimeUnitEnum.TimeUnit
    LIFETIME: TimeUnitEnum.TimeUnit
    POD: TimeUnitEnum.TimeUnit
    STREAM: TimeUnitEnum.TimeUnit

    def __init__(self) -> None:
        ...