from google.maps.routing.v2 import toll_passes_pb2 as _toll_passes_pb2
from google.maps.routing.v2 import vehicle_info_pb2 as _vehicle_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class RouteModifiers(_message.Message):
    __slots__ = ('avoid_tolls', 'avoid_highways', 'avoid_ferries', 'avoid_indoor', 'vehicle_info', 'toll_passes')
    AVOID_TOLLS_FIELD_NUMBER: _ClassVar[int]
    AVOID_HIGHWAYS_FIELD_NUMBER: _ClassVar[int]
    AVOID_FERRIES_FIELD_NUMBER: _ClassVar[int]
    AVOID_INDOOR_FIELD_NUMBER: _ClassVar[int]
    VEHICLE_INFO_FIELD_NUMBER: _ClassVar[int]
    TOLL_PASSES_FIELD_NUMBER: _ClassVar[int]
    avoid_tolls: bool
    avoid_highways: bool
    avoid_ferries: bool
    avoid_indoor: bool
    vehicle_info: _vehicle_info_pb2.VehicleInfo
    toll_passes: _containers.RepeatedScalarFieldContainer[_toll_passes_pb2.TollPass]

    def __init__(self, avoid_tolls: bool=..., avoid_highways: bool=..., avoid_ferries: bool=..., avoid_indoor: bool=..., vehicle_info: _Optional[_Union[_vehicle_info_pb2.VehicleInfo, _Mapping]]=..., toll_passes: _Optional[_Iterable[_Union[_toll_passes_pb2.TollPass, str]]]=...) -> None:
        ...