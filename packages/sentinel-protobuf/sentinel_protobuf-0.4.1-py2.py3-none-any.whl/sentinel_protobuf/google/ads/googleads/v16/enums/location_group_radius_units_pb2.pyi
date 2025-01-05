from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class LocationGroupRadiusUnitsEnum(_message.Message):
    __slots__ = ()

    class LocationGroupRadiusUnits(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[LocationGroupRadiusUnitsEnum.LocationGroupRadiusUnits]
        UNKNOWN: _ClassVar[LocationGroupRadiusUnitsEnum.LocationGroupRadiusUnits]
        METERS: _ClassVar[LocationGroupRadiusUnitsEnum.LocationGroupRadiusUnits]
        MILES: _ClassVar[LocationGroupRadiusUnitsEnum.LocationGroupRadiusUnits]
        MILLI_MILES: _ClassVar[LocationGroupRadiusUnitsEnum.LocationGroupRadiusUnits]
    UNSPECIFIED: LocationGroupRadiusUnitsEnum.LocationGroupRadiusUnits
    UNKNOWN: LocationGroupRadiusUnitsEnum.LocationGroupRadiusUnits
    METERS: LocationGroupRadiusUnitsEnum.LocationGroupRadiusUnits
    MILES: LocationGroupRadiusUnitsEnum.LocationGroupRadiusUnits
    MILLI_MILES: LocationGroupRadiusUnitsEnum.LocationGroupRadiusUnits

    def __init__(self) -> None:
        ...