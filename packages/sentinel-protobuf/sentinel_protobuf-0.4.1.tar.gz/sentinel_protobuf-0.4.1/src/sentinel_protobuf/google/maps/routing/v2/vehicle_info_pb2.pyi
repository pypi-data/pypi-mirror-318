from google.maps.routing.v2 import vehicle_emission_type_pb2 as _vehicle_emission_type_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class VehicleInfo(_message.Message):
    __slots__ = ('emission_type',)
    EMISSION_TYPE_FIELD_NUMBER: _ClassVar[int]
    emission_type: _vehicle_emission_type_pb2.VehicleEmissionType

    def __init__(self, emission_type: _Optional[_Union[_vehicle_emission_type_pb2.VehicleEmissionType, str]]=...) -> None:
        ...