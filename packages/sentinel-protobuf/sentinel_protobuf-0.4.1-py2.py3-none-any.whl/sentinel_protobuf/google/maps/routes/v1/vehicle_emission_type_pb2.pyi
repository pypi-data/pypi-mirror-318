from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class VehicleEmissionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    VEHICLE_EMISSION_TYPE_UNSPECIFIED: _ClassVar[VehicleEmissionType]
    GASOLINE: _ClassVar[VehicleEmissionType]
    ELECTRIC: _ClassVar[VehicleEmissionType]
    HYBRID: _ClassVar[VehicleEmissionType]
VEHICLE_EMISSION_TYPE_UNSPECIFIED: VehicleEmissionType
GASOLINE: VehicleEmissionType
ELECTRIC: VehicleEmissionType
HYBRID: VehicleEmissionType