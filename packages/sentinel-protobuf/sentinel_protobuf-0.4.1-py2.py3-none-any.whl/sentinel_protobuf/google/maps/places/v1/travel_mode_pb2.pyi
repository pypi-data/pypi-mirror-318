from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class TravelMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TRAVEL_MODE_UNSPECIFIED: _ClassVar[TravelMode]
    DRIVE: _ClassVar[TravelMode]
    BICYCLE: _ClassVar[TravelMode]
    WALK: _ClassVar[TravelMode]
    TWO_WHEELER: _ClassVar[TravelMode]
TRAVEL_MODE_UNSPECIFIED: TravelMode
DRIVE: TravelMode
BICYCLE: TravelMode
WALK: TravelMode
TWO_WHEELER: TravelMode