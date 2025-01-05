from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class RangeErrorEnum(_message.Message):
    __slots__ = ()

    class RangeError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[RangeErrorEnum.RangeError]
        UNKNOWN: _ClassVar[RangeErrorEnum.RangeError]
        TOO_LOW: _ClassVar[RangeErrorEnum.RangeError]
        TOO_HIGH: _ClassVar[RangeErrorEnum.RangeError]
    UNSPECIFIED: RangeErrorEnum.RangeError
    UNKNOWN: RangeErrorEnum.RangeError
    TOO_LOW: RangeErrorEnum.RangeError
    TOO_HIGH: RangeErrorEnum.RangeError

    def __init__(self) -> None:
        ...