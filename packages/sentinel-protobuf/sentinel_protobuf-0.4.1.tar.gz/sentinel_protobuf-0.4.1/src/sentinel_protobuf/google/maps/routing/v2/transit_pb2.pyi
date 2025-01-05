from google.maps.routing.v2 import location_pb2 as _location_pb2
from google.type import localized_text_pb2 as _localized_text_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class TransitAgency(_message.Message):
    __slots__ = ('name', 'phone_number', 'uri')
    NAME_FIELD_NUMBER: _ClassVar[int]
    PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    URI_FIELD_NUMBER: _ClassVar[int]
    name: str
    phone_number: str
    uri: str

    def __init__(self, name: _Optional[str]=..., phone_number: _Optional[str]=..., uri: _Optional[str]=...) -> None:
        ...

class TransitLine(_message.Message):
    __slots__ = ('agencies', 'name', 'uri', 'color', 'icon_uri', 'name_short', 'text_color', 'vehicle')
    AGENCIES_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    URI_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    ICON_URI_FIELD_NUMBER: _ClassVar[int]
    NAME_SHORT_FIELD_NUMBER: _ClassVar[int]
    TEXT_COLOR_FIELD_NUMBER: _ClassVar[int]
    VEHICLE_FIELD_NUMBER: _ClassVar[int]
    agencies: _containers.RepeatedCompositeFieldContainer[TransitAgency]
    name: str
    uri: str
    color: str
    icon_uri: str
    name_short: str
    text_color: str
    vehicle: TransitVehicle

    def __init__(self, agencies: _Optional[_Iterable[_Union[TransitAgency, _Mapping]]]=..., name: _Optional[str]=..., uri: _Optional[str]=..., color: _Optional[str]=..., icon_uri: _Optional[str]=..., name_short: _Optional[str]=..., text_color: _Optional[str]=..., vehicle: _Optional[_Union[TransitVehicle, _Mapping]]=...) -> None:
        ...

class TransitStop(_message.Message):
    __slots__ = ('name', 'location')
    NAME_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    name: str
    location: _location_pb2.Location

    def __init__(self, name: _Optional[str]=..., location: _Optional[_Union[_location_pb2.Location, _Mapping]]=...) -> None:
        ...

class TransitVehicle(_message.Message):
    __slots__ = ('name', 'type', 'icon_uri', 'local_icon_uri')

    class TransitVehicleType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TRANSIT_VEHICLE_TYPE_UNSPECIFIED: _ClassVar[TransitVehicle.TransitVehicleType]
        BUS: _ClassVar[TransitVehicle.TransitVehicleType]
        CABLE_CAR: _ClassVar[TransitVehicle.TransitVehicleType]
        COMMUTER_TRAIN: _ClassVar[TransitVehicle.TransitVehicleType]
        FERRY: _ClassVar[TransitVehicle.TransitVehicleType]
        FUNICULAR: _ClassVar[TransitVehicle.TransitVehicleType]
        GONDOLA_LIFT: _ClassVar[TransitVehicle.TransitVehicleType]
        HEAVY_RAIL: _ClassVar[TransitVehicle.TransitVehicleType]
        HIGH_SPEED_TRAIN: _ClassVar[TransitVehicle.TransitVehicleType]
        INTERCITY_BUS: _ClassVar[TransitVehicle.TransitVehicleType]
        LONG_DISTANCE_TRAIN: _ClassVar[TransitVehicle.TransitVehicleType]
        METRO_RAIL: _ClassVar[TransitVehicle.TransitVehicleType]
        MONORAIL: _ClassVar[TransitVehicle.TransitVehicleType]
        OTHER: _ClassVar[TransitVehicle.TransitVehicleType]
        RAIL: _ClassVar[TransitVehicle.TransitVehicleType]
        SHARE_TAXI: _ClassVar[TransitVehicle.TransitVehicleType]
        SUBWAY: _ClassVar[TransitVehicle.TransitVehicleType]
        TRAM: _ClassVar[TransitVehicle.TransitVehicleType]
        TROLLEYBUS: _ClassVar[TransitVehicle.TransitVehicleType]
    TRANSIT_VEHICLE_TYPE_UNSPECIFIED: TransitVehicle.TransitVehicleType
    BUS: TransitVehicle.TransitVehicleType
    CABLE_CAR: TransitVehicle.TransitVehicleType
    COMMUTER_TRAIN: TransitVehicle.TransitVehicleType
    FERRY: TransitVehicle.TransitVehicleType
    FUNICULAR: TransitVehicle.TransitVehicleType
    GONDOLA_LIFT: TransitVehicle.TransitVehicleType
    HEAVY_RAIL: TransitVehicle.TransitVehicleType
    HIGH_SPEED_TRAIN: TransitVehicle.TransitVehicleType
    INTERCITY_BUS: TransitVehicle.TransitVehicleType
    LONG_DISTANCE_TRAIN: TransitVehicle.TransitVehicleType
    METRO_RAIL: TransitVehicle.TransitVehicleType
    MONORAIL: TransitVehicle.TransitVehicleType
    OTHER: TransitVehicle.TransitVehicleType
    RAIL: TransitVehicle.TransitVehicleType
    SHARE_TAXI: TransitVehicle.TransitVehicleType
    SUBWAY: TransitVehicle.TransitVehicleType
    TRAM: TransitVehicle.TransitVehicleType
    TROLLEYBUS: TransitVehicle.TransitVehicleType
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ICON_URI_FIELD_NUMBER: _ClassVar[int]
    LOCAL_ICON_URI_FIELD_NUMBER: _ClassVar[int]
    name: _localized_text_pb2.LocalizedText
    type: TransitVehicle.TransitVehicleType
    icon_uri: str
    local_icon_uri: str

    def __init__(self, name: _Optional[_Union[_localized_text_pb2.LocalizedText, _Mapping]]=..., type: _Optional[_Union[TransitVehicle.TransitVehicleType, str]]=..., icon_uri: _Optional[str]=..., local_icon_uri: _Optional[str]=...) -> None:
        ...