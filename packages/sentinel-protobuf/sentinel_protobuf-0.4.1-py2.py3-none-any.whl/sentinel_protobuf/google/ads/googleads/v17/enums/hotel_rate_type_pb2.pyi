from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class HotelRateTypeEnum(_message.Message):
    __slots__ = ()

    class HotelRateType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[HotelRateTypeEnum.HotelRateType]
        UNKNOWN: _ClassVar[HotelRateTypeEnum.HotelRateType]
        UNAVAILABLE: _ClassVar[HotelRateTypeEnum.HotelRateType]
        PUBLIC_RATE: _ClassVar[HotelRateTypeEnum.HotelRateType]
        QUALIFIED_RATE: _ClassVar[HotelRateTypeEnum.HotelRateType]
        PRIVATE_RATE: _ClassVar[HotelRateTypeEnum.HotelRateType]
    UNSPECIFIED: HotelRateTypeEnum.HotelRateType
    UNKNOWN: HotelRateTypeEnum.HotelRateType
    UNAVAILABLE: HotelRateTypeEnum.HotelRateType
    PUBLIC_RATE: HotelRateTypeEnum.HotelRateType
    QUALIFIED_RATE: HotelRateTypeEnum.HotelRateType
    PRIVATE_RATE: HotelRateTypeEnum.HotelRateType

    def __init__(self) -> None:
        ...