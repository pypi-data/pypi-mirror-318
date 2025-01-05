from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.geo.type import viewport_pb2 as _viewport_pb2
from google.maps.routes.v1 import polyline_pb2 as _polyline_pb2
from google.maps.routes.v1 import waypoint_pb2 as _waypoint_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.type import money_pb2 as _money_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Maneuver(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MANEUVER_UNSPECIFIED: _ClassVar[Maneuver]
    TURN_SLIGHT_LEFT: _ClassVar[Maneuver]
    TURN_SHARP_LEFT: _ClassVar[Maneuver]
    UTURN_LEFT: _ClassVar[Maneuver]
    TURN_LEFT: _ClassVar[Maneuver]
    TURN_SLIGHT_RIGHT: _ClassVar[Maneuver]
    TURN_SHARP_RIGHT: _ClassVar[Maneuver]
    UTURN_RIGHT: _ClassVar[Maneuver]
    TURN_RIGHT: _ClassVar[Maneuver]
    STRAIGHT: _ClassVar[Maneuver]
    RAMP_LEFT: _ClassVar[Maneuver]
    RAMP_RIGHT: _ClassVar[Maneuver]
    MERGE: _ClassVar[Maneuver]
    FORK_LEFT: _ClassVar[Maneuver]
    FORK_RIGHT: _ClassVar[Maneuver]
    FERRY: _ClassVar[Maneuver]
    FERRY_TRAIN: _ClassVar[Maneuver]
    ROUNDABOUT_LEFT: _ClassVar[Maneuver]
    ROUNDABOUT_RIGHT: _ClassVar[Maneuver]
    DEPART: _ClassVar[Maneuver]
    NAME_CHANGE: _ClassVar[Maneuver]
MANEUVER_UNSPECIFIED: Maneuver
TURN_SLIGHT_LEFT: Maneuver
TURN_SHARP_LEFT: Maneuver
UTURN_LEFT: Maneuver
TURN_LEFT: Maneuver
TURN_SLIGHT_RIGHT: Maneuver
TURN_SHARP_RIGHT: Maneuver
UTURN_RIGHT: Maneuver
TURN_RIGHT: Maneuver
STRAIGHT: Maneuver
RAMP_LEFT: Maneuver
RAMP_RIGHT: Maneuver
MERGE: Maneuver
FORK_LEFT: Maneuver
FORK_RIGHT: Maneuver
FERRY: Maneuver
FERRY_TRAIN: Maneuver
ROUNDABOUT_LEFT: Maneuver
ROUNDABOUT_RIGHT: Maneuver
DEPART: Maneuver
NAME_CHANGE: Maneuver

class Route(_message.Message):
    __slots__ = ('legs', 'distance_meters', 'duration', 'static_duration', 'polyline', 'description', 'warnings', 'viewport', 'travel_advisory', 'optimized_intermediate_waypoint_index')
    LEGS_FIELD_NUMBER: _ClassVar[int]
    DISTANCE_METERS_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    STATIC_DURATION_FIELD_NUMBER: _ClassVar[int]
    POLYLINE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    VIEWPORT_FIELD_NUMBER: _ClassVar[int]
    TRAVEL_ADVISORY_FIELD_NUMBER: _ClassVar[int]
    OPTIMIZED_INTERMEDIATE_WAYPOINT_INDEX_FIELD_NUMBER: _ClassVar[int]
    legs: _containers.RepeatedCompositeFieldContainer[RouteLeg]
    distance_meters: int
    duration: _duration_pb2.Duration
    static_duration: _duration_pb2.Duration
    polyline: _polyline_pb2.Polyline
    description: str
    warnings: _containers.RepeatedScalarFieldContainer[str]
    viewport: _viewport_pb2.Viewport
    travel_advisory: RouteTravelAdvisory
    optimized_intermediate_waypoint_index: _containers.RepeatedScalarFieldContainer[int]

    def __init__(self, legs: _Optional[_Iterable[_Union[RouteLeg, _Mapping]]]=..., distance_meters: _Optional[int]=..., duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., static_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., polyline: _Optional[_Union[_polyline_pb2.Polyline, _Mapping]]=..., description: _Optional[str]=..., warnings: _Optional[_Iterable[str]]=..., viewport: _Optional[_Union[_viewport_pb2.Viewport, _Mapping]]=..., travel_advisory: _Optional[_Union[RouteTravelAdvisory, _Mapping]]=..., optimized_intermediate_waypoint_index: _Optional[_Iterable[int]]=...) -> None:
        ...

class RouteTravelAdvisory(_message.Message):
    __slots__ = ('traffic_restriction', 'toll_info', 'speed_reading_intervals', 'custom_layer_info')
    TRAFFIC_RESTRICTION_FIELD_NUMBER: _ClassVar[int]
    TOLL_INFO_FIELD_NUMBER: _ClassVar[int]
    SPEED_READING_INTERVALS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_LAYER_INFO_FIELD_NUMBER: _ClassVar[int]
    traffic_restriction: TrafficRestriction
    toll_info: TollInfo
    speed_reading_intervals: _containers.RepeatedCompositeFieldContainer[SpeedReadingInterval]
    custom_layer_info: CustomLayerInfo

    def __init__(self, traffic_restriction: _Optional[_Union[TrafficRestriction, _Mapping]]=..., toll_info: _Optional[_Union[TollInfo, _Mapping]]=..., speed_reading_intervals: _Optional[_Iterable[_Union[SpeedReadingInterval, _Mapping]]]=..., custom_layer_info: _Optional[_Union[CustomLayerInfo, _Mapping]]=...) -> None:
        ...

class RouteLegTravelAdvisory(_message.Message):
    __slots__ = ('toll_info', 'speed_reading_intervals', 'custom_layer_info')
    TOLL_INFO_FIELD_NUMBER: _ClassVar[int]
    SPEED_READING_INTERVALS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_LAYER_INFO_FIELD_NUMBER: _ClassVar[int]
    toll_info: TollInfo
    speed_reading_intervals: _containers.RepeatedCompositeFieldContainer[SpeedReadingInterval]
    custom_layer_info: CustomLayerInfo

    def __init__(self, toll_info: _Optional[_Union[TollInfo, _Mapping]]=..., speed_reading_intervals: _Optional[_Iterable[_Union[SpeedReadingInterval, _Mapping]]]=..., custom_layer_info: _Optional[_Union[CustomLayerInfo, _Mapping]]=...) -> None:
        ...

class RouteLegStepTravelAdvisory(_message.Message):
    __slots__ = ('speed_reading_intervals',)
    SPEED_READING_INTERVALS_FIELD_NUMBER: _ClassVar[int]
    speed_reading_intervals: _containers.RepeatedCompositeFieldContainer[SpeedReadingInterval]

    def __init__(self, speed_reading_intervals: _Optional[_Iterable[_Union[SpeedReadingInterval, _Mapping]]]=...) -> None:
        ...

class TrafficRestriction(_message.Message):
    __slots__ = ('license_plate_last_character_restriction',)
    LICENSE_PLATE_LAST_CHARACTER_RESTRICTION_FIELD_NUMBER: _ClassVar[int]
    license_plate_last_character_restriction: LicensePlateLastCharacterRestriction

    def __init__(self, license_plate_last_character_restriction: _Optional[_Union[LicensePlateLastCharacterRestriction, _Mapping]]=...) -> None:
        ...

class LicensePlateLastCharacterRestriction(_message.Message):
    __slots__ = ('allowed_last_characters',)
    ALLOWED_LAST_CHARACTERS_FIELD_NUMBER: _ClassVar[int]
    allowed_last_characters: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, allowed_last_characters: _Optional[_Iterable[str]]=...) -> None:
        ...

class RouteLeg(_message.Message):
    __slots__ = ('distance_meters', 'duration', 'static_duration', 'polyline', 'start_location', 'end_location', 'steps', 'travel_advisory')
    DISTANCE_METERS_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    STATIC_DURATION_FIELD_NUMBER: _ClassVar[int]
    POLYLINE_FIELD_NUMBER: _ClassVar[int]
    START_LOCATION_FIELD_NUMBER: _ClassVar[int]
    END_LOCATION_FIELD_NUMBER: _ClassVar[int]
    STEPS_FIELD_NUMBER: _ClassVar[int]
    TRAVEL_ADVISORY_FIELD_NUMBER: _ClassVar[int]
    distance_meters: int
    duration: _duration_pb2.Duration
    static_duration: _duration_pb2.Duration
    polyline: _polyline_pb2.Polyline
    start_location: _waypoint_pb2.Location
    end_location: _waypoint_pb2.Location
    steps: _containers.RepeatedCompositeFieldContainer[RouteLegStep]
    travel_advisory: RouteLegTravelAdvisory

    def __init__(self, distance_meters: _Optional[int]=..., duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., static_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., polyline: _Optional[_Union[_polyline_pb2.Polyline, _Mapping]]=..., start_location: _Optional[_Union[_waypoint_pb2.Location, _Mapping]]=..., end_location: _Optional[_Union[_waypoint_pb2.Location, _Mapping]]=..., steps: _Optional[_Iterable[_Union[RouteLegStep, _Mapping]]]=..., travel_advisory: _Optional[_Union[RouteLegTravelAdvisory, _Mapping]]=...) -> None:
        ...

class TollInfo(_message.Message):
    __slots__ = ('estimated_price',)
    ESTIMATED_PRICE_FIELD_NUMBER: _ClassVar[int]
    estimated_price: _containers.RepeatedCompositeFieldContainer[_money_pb2.Money]

    def __init__(self, estimated_price: _Optional[_Iterable[_Union[_money_pb2.Money, _Mapping]]]=...) -> None:
        ...

class RouteLegStep(_message.Message):
    __slots__ = ('distance_meters', 'static_duration', 'polyline', 'start_location', 'end_location', 'navigation_instruction', 'travel_advisory')
    DISTANCE_METERS_FIELD_NUMBER: _ClassVar[int]
    STATIC_DURATION_FIELD_NUMBER: _ClassVar[int]
    POLYLINE_FIELD_NUMBER: _ClassVar[int]
    START_LOCATION_FIELD_NUMBER: _ClassVar[int]
    END_LOCATION_FIELD_NUMBER: _ClassVar[int]
    NAVIGATION_INSTRUCTION_FIELD_NUMBER: _ClassVar[int]
    TRAVEL_ADVISORY_FIELD_NUMBER: _ClassVar[int]
    distance_meters: int
    static_duration: _duration_pb2.Duration
    polyline: _polyline_pb2.Polyline
    start_location: _waypoint_pb2.Location
    end_location: _waypoint_pb2.Location
    navigation_instruction: NavigationInstruction
    travel_advisory: RouteLegStepTravelAdvisory

    def __init__(self, distance_meters: _Optional[int]=..., static_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., polyline: _Optional[_Union[_polyline_pb2.Polyline, _Mapping]]=..., start_location: _Optional[_Union[_waypoint_pb2.Location, _Mapping]]=..., end_location: _Optional[_Union[_waypoint_pb2.Location, _Mapping]]=..., navigation_instruction: _Optional[_Union[NavigationInstruction, _Mapping]]=..., travel_advisory: _Optional[_Union[RouteLegStepTravelAdvisory, _Mapping]]=...) -> None:
        ...

class NavigationInstruction(_message.Message):
    __slots__ = ('maneuver', 'instructions')
    MANEUVER_FIELD_NUMBER: _ClassVar[int]
    INSTRUCTIONS_FIELD_NUMBER: _ClassVar[int]
    maneuver: Maneuver
    instructions: str

    def __init__(self, maneuver: _Optional[_Union[Maneuver, str]]=..., instructions: _Optional[str]=...) -> None:
        ...

class SpeedReadingInterval(_message.Message):
    __slots__ = ('start_polyline_point_index', 'end_polyline_point_index', 'speed')

    class Speed(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SPEED_UNSPECIFIED: _ClassVar[SpeedReadingInterval.Speed]
        NORMAL: _ClassVar[SpeedReadingInterval.Speed]
        SLOW: _ClassVar[SpeedReadingInterval.Speed]
        TRAFFIC_JAM: _ClassVar[SpeedReadingInterval.Speed]
    SPEED_UNSPECIFIED: SpeedReadingInterval.Speed
    NORMAL: SpeedReadingInterval.Speed
    SLOW: SpeedReadingInterval.Speed
    TRAFFIC_JAM: SpeedReadingInterval.Speed
    START_POLYLINE_POINT_INDEX_FIELD_NUMBER: _ClassVar[int]
    END_POLYLINE_POINT_INDEX_FIELD_NUMBER: _ClassVar[int]
    SPEED_FIELD_NUMBER: _ClassVar[int]
    start_polyline_point_index: int
    end_polyline_point_index: int
    speed: SpeedReadingInterval.Speed

    def __init__(self, start_polyline_point_index: _Optional[int]=..., end_polyline_point_index: _Optional[int]=..., speed: _Optional[_Union[SpeedReadingInterval.Speed, str]]=...) -> None:
        ...

class CustomLayerInfo(_message.Message):
    __slots__ = ('area_info', 'total_distance_in_areas_meters', 'total_duration_in_areas')

    class AreaInfo(_message.Message):
        __slots__ = ('area_id', 'distance_in_area_meters', 'duration_in_area')
        AREA_ID_FIELD_NUMBER: _ClassVar[int]
        DISTANCE_IN_AREA_METERS_FIELD_NUMBER: _ClassVar[int]
        DURATION_IN_AREA_FIELD_NUMBER: _ClassVar[int]
        area_id: str
        distance_in_area_meters: float
        duration_in_area: _duration_pb2.Duration

        def __init__(self, area_id: _Optional[str]=..., distance_in_area_meters: _Optional[float]=..., duration_in_area: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=...) -> None:
            ...
    AREA_INFO_FIELD_NUMBER: _ClassVar[int]
    TOTAL_DISTANCE_IN_AREAS_METERS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_DURATION_IN_AREAS_FIELD_NUMBER: _ClassVar[int]
    area_info: _containers.RepeatedCompositeFieldContainer[CustomLayerInfo.AreaInfo]
    total_distance_in_areas_meters: float
    total_duration_in_areas: _duration_pb2.Duration

    def __init__(self, area_info: _Optional[_Iterable[_Union[CustomLayerInfo.AreaInfo, _Mapping]]]=..., total_distance_in_areas_meters: _Optional[float]=..., total_duration_in_areas: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=...) -> None:
        ...