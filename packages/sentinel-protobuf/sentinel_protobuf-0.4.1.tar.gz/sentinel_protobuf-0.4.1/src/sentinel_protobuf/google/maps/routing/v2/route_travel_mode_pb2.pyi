from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class RouteTravelMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TRAVEL_MODE_UNSPECIFIED: _ClassVar[RouteTravelMode]
    DRIVE: _ClassVar[RouteTravelMode]
    BICYCLE: _ClassVar[RouteTravelMode]
    WALK: _ClassVar[RouteTravelMode]
    TWO_WHEELER: _ClassVar[RouteTravelMode]
    TRANSIT: _ClassVar[RouteTravelMode]
TRAVEL_MODE_UNSPECIFIED: RouteTravelMode
DRIVE: RouteTravelMode
BICYCLE: RouteTravelMode
WALK: RouteTravelMode
TWO_WHEELER: RouteTravelMode
TRANSIT: RouteTravelMode