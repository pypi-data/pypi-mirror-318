from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class HotelPriceBucketEnum(_message.Message):
    __slots__ = ()

    class HotelPriceBucket(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[HotelPriceBucketEnum.HotelPriceBucket]
        UNKNOWN: _ClassVar[HotelPriceBucketEnum.HotelPriceBucket]
        LOWEST_UNIQUE: _ClassVar[HotelPriceBucketEnum.HotelPriceBucket]
        LOWEST_TIED: _ClassVar[HotelPriceBucketEnum.HotelPriceBucket]
        NOT_LOWEST: _ClassVar[HotelPriceBucketEnum.HotelPriceBucket]
        ONLY_PARTNER_SHOWN: _ClassVar[HotelPriceBucketEnum.HotelPriceBucket]
    UNSPECIFIED: HotelPriceBucketEnum.HotelPriceBucket
    UNKNOWN: HotelPriceBucketEnum.HotelPriceBucket
    LOWEST_UNIQUE: HotelPriceBucketEnum.HotelPriceBucket
    LOWEST_TIED: HotelPriceBucketEnum.HotelPriceBucket
    NOT_LOWEST: HotelPriceBucketEnum.HotelPriceBucket
    ONLY_PARTNER_SHOWN: HotelPriceBucketEnum.HotelPriceBucket

    def __init__(self) -> None:
        ...