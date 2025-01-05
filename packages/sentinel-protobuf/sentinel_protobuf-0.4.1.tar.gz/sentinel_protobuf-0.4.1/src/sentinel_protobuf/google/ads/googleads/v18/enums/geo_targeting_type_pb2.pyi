from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class GeoTargetingTypeEnum(_message.Message):
    __slots__ = ()

    class GeoTargetingType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[GeoTargetingTypeEnum.GeoTargetingType]
        UNKNOWN: _ClassVar[GeoTargetingTypeEnum.GeoTargetingType]
        AREA_OF_INTEREST: _ClassVar[GeoTargetingTypeEnum.GeoTargetingType]
        LOCATION_OF_PRESENCE: _ClassVar[GeoTargetingTypeEnum.GeoTargetingType]
    UNSPECIFIED: GeoTargetingTypeEnum.GeoTargetingType
    UNKNOWN: GeoTargetingTypeEnum.GeoTargetingType
    AREA_OF_INTEREST: GeoTargetingTypeEnum.GeoTargetingType
    LOCATION_OF_PRESENCE: GeoTargetingTypeEnum.GeoTargetingType

    def __init__(self) -> None:
        ...