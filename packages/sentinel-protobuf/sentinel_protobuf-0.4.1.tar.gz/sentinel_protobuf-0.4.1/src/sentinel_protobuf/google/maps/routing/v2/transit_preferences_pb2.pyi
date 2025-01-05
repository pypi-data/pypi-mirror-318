from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class TransitPreferences(_message.Message):
    __slots__ = ('allowed_travel_modes', 'routing_preference')

    class TransitTravelMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TRANSIT_TRAVEL_MODE_UNSPECIFIED: _ClassVar[TransitPreferences.TransitTravelMode]
        BUS: _ClassVar[TransitPreferences.TransitTravelMode]
        SUBWAY: _ClassVar[TransitPreferences.TransitTravelMode]
        TRAIN: _ClassVar[TransitPreferences.TransitTravelMode]
        LIGHT_RAIL: _ClassVar[TransitPreferences.TransitTravelMode]
        RAIL: _ClassVar[TransitPreferences.TransitTravelMode]
    TRANSIT_TRAVEL_MODE_UNSPECIFIED: TransitPreferences.TransitTravelMode
    BUS: TransitPreferences.TransitTravelMode
    SUBWAY: TransitPreferences.TransitTravelMode
    TRAIN: TransitPreferences.TransitTravelMode
    LIGHT_RAIL: TransitPreferences.TransitTravelMode
    RAIL: TransitPreferences.TransitTravelMode

    class TransitRoutingPreference(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TRANSIT_ROUTING_PREFERENCE_UNSPECIFIED: _ClassVar[TransitPreferences.TransitRoutingPreference]
        LESS_WALKING: _ClassVar[TransitPreferences.TransitRoutingPreference]
        FEWER_TRANSFERS: _ClassVar[TransitPreferences.TransitRoutingPreference]
    TRANSIT_ROUTING_PREFERENCE_UNSPECIFIED: TransitPreferences.TransitRoutingPreference
    LESS_WALKING: TransitPreferences.TransitRoutingPreference
    FEWER_TRANSFERS: TransitPreferences.TransitRoutingPreference
    ALLOWED_TRAVEL_MODES_FIELD_NUMBER: _ClassVar[int]
    ROUTING_PREFERENCE_FIELD_NUMBER: _ClassVar[int]
    allowed_travel_modes: _containers.RepeatedScalarFieldContainer[TransitPreferences.TransitTravelMode]
    routing_preference: TransitPreferences.TransitRoutingPreference

    def __init__(self, allowed_travel_modes: _Optional[_Iterable[_Union[TransitPreferences.TransitTravelMode, str]]]=..., routing_preference: _Optional[_Union[TransitPreferences.TransitRoutingPreference, str]]=...) -> None:
        ...