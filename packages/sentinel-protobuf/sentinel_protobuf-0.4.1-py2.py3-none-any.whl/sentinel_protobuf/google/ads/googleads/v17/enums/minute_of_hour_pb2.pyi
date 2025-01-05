from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class MinuteOfHourEnum(_message.Message):
    __slots__ = ()

    class MinuteOfHour(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[MinuteOfHourEnum.MinuteOfHour]
        UNKNOWN: _ClassVar[MinuteOfHourEnum.MinuteOfHour]
        ZERO: _ClassVar[MinuteOfHourEnum.MinuteOfHour]
        FIFTEEN: _ClassVar[MinuteOfHourEnum.MinuteOfHour]
        THIRTY: _ClassVar[MinuteOfHourEnum.MinuteOfHour]
        FORTY_FIVE: _ClassVar[MinuteOfHourEnum.MinuteOfHour]
    UNSPECIFIED: MinuteOfHourEnum.MinuteOfHour
    UNKNOWN: MinuteOfHourEnum.MinuteOfHour
    ZERO: MinuteOfHourEnum.MinuteOfHour
    FIFTEEN: MinuteOfHourEnum.MinuteOfHour
    THIRTY: MinuteOfHourEnum.MinuteOfHour
    FORTY_FIVE: MinuteOfHourEnum.MinuteOfHour

    def __init__(self) -> None:
        ...