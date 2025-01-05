from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class RegionCodeErrorEnum(_message.Message):
    __slots__ = ()

    class RegionCodeError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[RegionCodeErrorEnum.RegionCodeError]
        UNKNOWN: _ClassVar[RegionCodeErrorEnum.RegionCodeError]
        INVALID_REGION_CODE: _ClassVar[RegionCodeErrorEnum.RegionCodeError]
    UNSPECIFIED: RegionCodeErrorEnum.RegionCodeError
    UNKNOWN: RegionCodeErrorEnum.RegionCodeError
    INVALID_REGION_CODE: RegionCodeErrorEnum.RegionCodeError

    def __init__(self) -> None:
        ...