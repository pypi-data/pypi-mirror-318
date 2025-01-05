from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class ProximityRadiusUnitsEnum(_message.Message):
    __slots__ = ()

    class ProximityRadiusUnits(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ProximityRadiusUnitsEnum.ProximityRadiusUnits]
        UNKNOWN: _ClassVar[ProximityRadiusUnitsEnum.ProximityRadiusUnits]
        MILES: _ClassVar[ProximityRadiusUnitsEnum.ProximityRadiusUnits]
        KILOMETERS: _ClassVar[ProximityRadiusUnitsEnum.ProximityRadiusUnits]
    UNSPECIFIED: ProximityRadiusUnitsEnum.ProximityRadiusUnits
    UNKNOWN: ProximityRadiusUnitsEnum.ProximityRadiusUnits
    MILES: ProximityRadiusUnitsEnum.ProximityRadiusUnits
    KILOMETERS: ProximityRadiusUnitsEnum.ProximityRadiusUnits

    def __init__(self) -> None:
        ...