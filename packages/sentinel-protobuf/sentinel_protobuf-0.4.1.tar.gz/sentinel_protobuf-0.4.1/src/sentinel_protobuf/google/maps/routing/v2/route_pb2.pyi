from google.geo.type import viewport_pb2 as _viewport_pb2
from google.maps.routing.v2 import localized_time_pb2 as _localized_time_pb2
from google.maps.routing.v2 import location_pb2 as _location_pb2
from google.maps.routing.v2 import navigation_instruction_pb2 as _navigation_instruction_pb2
from google.maps.routing.v2 import polyline_pb2 as _polyline_pb2
from google.maps.routing.v2 import polyline_details_pb2 as _polyline_details_pb2
from google.maps.routing.v2 import route_label_pb2 as _route_label_pb2
from google.maps.routing.v2 import route_travel_mode_pb2 as _route_travel_mode_pb2
from google.maps.routing.v2 import speed_reading_interval_pb2 as _speed_reading_interval_pb2
from google.maps.routing.v2 import toll_info_pb2 as _toll_info_pb2
from google.maps.routing.v2 import transit_pb2 as _transit_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.type import localized_text_pb2 as _localized_text_pb2
from google.type import money_pb2 as _money_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Route(_message.Message):
    __slots__ = ("route_labels", "legs", "distance_meters", "duration", "static_duration", "polyline", "description", "warnings", "viewport", "travel_advisory", "optimized_intermediate_waypoint_index", "localized_values", "route_token", "polyline_details")
    class RouteLocalizedValues(_message.Message):
        __slots__ = ("distance", "duration", "static_duration", "transit_fare")
        DISTANCE_FIELD_NUMBER: _ClassVar[int]
        DURATION_FIELD_NUMBER: _ClassVar[int]
        STATIC_DURATION_FIELD_NUMBER: _ClassVar[int]
        TRANSIT_FARE_FIELD_NUMBER: _ClassVar[int]
        distance: _localized_text_pb2.LocalizedText
        duration: _localized_text_pb2.LocalizedText
        static_duration: _localized_text_pb2.LocalizedText
        transit_fare: _localized_text_pb2.LocalizedText
        def __init__(self, distance: _Optional[_Union[_localized_text_pb2.LocalizedText, _Mapping]] = ..., duration: _Optional[_Union[_localized_text_pb2.LocalizedText, _Mapping]] = ..., static_duration: _Optional[_Union[_localized_text_pb2.LocalizedText, _Mapping]] = ..., transit_fare: _Optional[_Union[_localized_text_pb2.LocalizedText, _Mapping]] = ...) -> None: ...
    ROUTE_LABELS_FIELD_NUMBER: _ClassVar[int]
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
    LOCALIZED_VALUES_FIELD_NUMBER: _ClassVar[int]
    ROUTE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    POLYLINE_DETAILS_FIELD_NUMBER: _ClassVar[int]
    route_labels: _containers.RepeatedScalarFieldContainer[_route_label_pb2.RouteLabel]
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
    localized_values: Route.RouteLocalizedValues
    route_token: str
    polyline_details: _polyline_details_pb2.PolylineDetails
    def __init__(self, route_labels: _Optional[_Iterable[_Union[_route_label_pb2.RouteLabel, str]]] = ..., legs: _Optional[_Iterable[_Union[RouteLeg, _Mapping]]] = ..., distance_meters: _Optional[int] = ..., duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., static_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., polyline: _Optional[_Union[_polyline_pb2.Polyline, _Mapping]] = ..., description: _Optional[str] = ..., warnings: _Optional[_Iterable[str]] = ..., viewport: _Optional[_Union[_viewport_pb2.Viewport, _Mapping]] = ..., travel_advisory: _Optional[_Union[RouteTravelAdvisory, _Mapping]] = ..., optimized_intermediate_waypoint_index: _Optional[_Iterable[int]] = ..., localized_values: _Optional[_Union[Route.RouteLocalizedValues, _Mapping]] = ..., route_token: _Optional[str] = ..., polyline_details: _Optional[_Union[_polyline_details_pb2.PolylineDetails, _Mapping]] = ...) -> None: ...

class RouteTravelAdvisory(_message.Message):
    __slots__ = ("toll_info", "speed_reading_intervals", "fuel_consumption_microliters", "route_restrictions_partially_ignored", "transit_fare")
    TOLL_INFO_FIELD_NUMBER: _ClassVar[int]
    SPEED_READING_INTERVALS_FIELD_NUMBER: _ClassVar[int]
    FUEL_CONSUMPTION_MICROLITERS_FIELD_NUMBER: _ClassVar[int]
    ROUTE_RESTRICTIONS_PARTIALLY_IGNORED_FIELD_NUMBER: _ClassVar[int]
    TRANSIT_FARE_FIELD_NUMBER: _ClassVar[int]
    toll_info: _toll_info_pb2.TollInfo
    speed_reading_intervals: _containers.RepeatedCompositeFieldContainer[_speed_reading_interval_pb2.SpeedReadingInterval]
    fuel_consumption_microliters: int
    route_restrictions_partially_ignored: bool
    transit_fare: _money_pb2.Money
    def __init__(self, toll_info: _Optional[_Union[_toll_info_pb2.TollInfo, _Mapping]] = ..., speed_reading_intervals: _Optional[_Iterable[_Union[_speed_reading_interval_pb2.SpeedReadingInterval, _Mapping]]] = ..., fuel_consumption_microliters: _Optional[int] = ..., route_restrictions_partially_ignored: bool = ..., transit_fare: _Optional[_Union[_money_pb2.Money, _Mapping]] = ...) -> None: ...

class RouteLegTravelAdvisory(_message.Message):
    __slots__ = ("toll_info", "speed_reading_intervals")
    TOLL_INFO_FIELD_NUMBER: _ClassVar[int]
    SPEED_READING_INTERVALS_FIELD_NUMBER: _ClassVar[int]
    toll_info: _toll_info_pb2.TollInfo
    speed_reading_intervals: _containers.RepeatedCompositeFieldContainer[_speed_reading_interval_pb2.SpeedReadingInterval]
    def __init__(self, toll_info: _Optional[_Union[_toll_info_pb2.TollInfo, _Mapping]] = ..., speed_reading_intervals: _Optional[_Iterable[_Union[_speed_reading_interval_pb2.SpeedReadingInterval, _Mapping]]] = ...) -> None: ...

class RouteLegStepTravelAdvisory(_message.Message):
    __slots__ = ("speed_reading_intervals",)
    SPEED_READING_INTERVALS_FIELD_NUMBER: _ClassVar[int]
    speed_reading_intervals: _containers.RepeatedCompositeFieldContainer[_speed_reading_interval_pb2.SpeedReadingInterval]
    def __init__(self, speed_reading_intervals: _Optional[_Iterable[_Union[_speed_reading_interval_pb2.SpeedReadingInterval, _Mapping]]] = ...) -> None: ...

class RouteLeg(_message.Message):
    __slots__ = ("distance_meters", "duration", "static_duration", "polyline", "start_location", "end_location", "steps", "travel_advisory", "localized_values", "steps_overview")
    class RouteLegLocalizedValues(_message.Message):
        __slots__ = ("distance", "duration", "static_duration")
        DISTANCE_FIELD_NUMBER: _ClassVar[int]
        DURATION_FIELD_NUMBER: _ClassVar[int]
        STATIC_DURATION_FIELD_NUMBER: _ClassVar[int]
        distance: _localized_text_pb2.LocalizedText
        duration: _localized_text_pb2.LocalizedText
        static_duration: _localized_text_pb2.LocalizedText
        def __init__(self, distance: _Optional[_Union[_localized_text_pb2.LocalizedText, _Mapping]] = ..., duration: _Optional[_Union[_localized_text_pb2.LocalizedText, _Mapping]] = ..., static_duration: _Optional[_Union[_localized_text_pb2.LocalizedText, _Mapping]] = ...) -> None: ...
    class StepsOverview(_message.Message):
        __slots__ = ("multi_modal_segments",)
        class MultiModalSegment(_message.Message):
            __slots__ = ("step_start_index", "step_end_index", "navigation_instruction", "travel_mode")
            STEP_START_INDEX_FIELD_NUMBER: _ClassVar[int]
            STEP_END_INDEX_FIELD_NUMBER: _ClassVar[int]
            NAVIGATION_INSTRUCTION_FIELD_NUMBER: _ClassVar[int]
            TRAVEL_MODE_FIELD_NUMBER: _ClassVar[int]
            step_start_index: int
            step_end_index: int
            navigation_instruction: _navigation_instruction_pb2.NavigationInstruction
            travel_mode: _route_travel_mode_pb2.RouteTravelMode
            def __init__(self, step_start_index: _Optional[int] = ..., step_end_index: _Optional[int] = ..., navigation_instruction: _Optional[_Union[_navigation_instruction_pb2.NavigationInstruction, _Mapping]] = ..., travel_mode: _Optional[_Union[_route_travel_mode_pb2.RouteTravelMode, str]] = ...) -> None: ...
        MULTI_MODAL_SEGMENTS_FIELD_NUMBER: _ClassVar[int]
        multi_modal_segments: _containers.RepeatedCompositeFieldContainer[RouteLeg.StepsOverview.MultiModalSegment]
        def __init__(self, multi_modal_segments: _Optional[_Iterable[_Union[RouteLeg.StepsOverview.MultiModalSegment, _Mapping]]] = ...) -> None: ...
    DISTANCE_METERS_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    STATIC_DURATION_FIELD_NUMBER: _ClassVar[int]
    POLYLINE_FIELD_NUMBER: _ClassVar[int]
    START_LOCATION_FIELD_NUMBER: _ClassVar[int]
    END_LOCATION_FIELD_NUMBER: _ClassVar[int]
    STEPS_FIELD_NUMBER: _ClassVar[int]
    TRAVEL_ADVISORY_FIELD_NUMBER: _ClassVar[int]
    LOCALIZED_VALUES_FIELD_NUMBER: _ClassVar[int]
    STEPS_OVERVIEW_FIELD_NUMBER: _ClassVar[int]
    distance_meters: int
    duration: _duration_pb2.Duration
    static_duration: _duration_pb2.Duration
    polyline: _polyline_pb2.Polyline
    start_location: _location_pb2.Location
    end_location: _location_pb2.Location
    steps: _containers.RepeatedCompositeFieldContainer[RouteLegStep]
    travel_advisory: RouteLegTravelAdvisory
    localized_values: RouteLeg.RouteLegLocalizedValues
    steps_overview: RouteLeg.StepsOverview
    def __init__(self, distance_meters: _Optional[int] = ..., duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., static_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., polyline: _Optional[_Union[_polyline_pb2.Polyline, _Mapping]] = ..., start_location: _Optional[_Union[_location_pb2.Location, _Mapping]] = ..., end_location: _Optional[_Union[_location_pb2.Location, _Mapping]] = ..., steps: _Optional[_Iterable[_Union[RouteLegStep, _Mapping]]] = ..., travel_advisory: _Optional[_Union[RouteLegTravelAdvisory, _Mapping]] = ..., localized_values: _Optional[_Union[RouteLeg.RouteLegLocalizedValues, _Mapping]] = ..., steps_overview: _Optional[_Union[RouteLeg.StepsOverview, _Mapping]] = ...) -> None: ...

class RouteLegStep(_message.Message):
    __slots__ = ("distance_meters", "static_duration", "polyline", "start_location", "end_location", "navigation_instruction", "travel_advisory", "localized_values", "transit_details", "travel_mode")
    class RouteLegStepLocalizedValues(_message.Message):
        __slots__ = ("distance", "static_duration")
        DISTANCE_FIELD_NUMBER: _ClassVar[int]
        STATIC_DURATION_FIELD_NUMBER: _ClassVar[int]
        distance: _localized_text_pb2.LocalizedText
        static_duration: _localized_text_pb2.LocalizedText
        def __init__(self, distance: _Optional[_Union[_localized_text_pb2.LocalizedText, _Mapping]] = ..., static_duration: _Optional[_Union[_localized_text_pb2.LocalizedText, _Mapping]] = ...) -> None: ...
    DISTANCE_METERS_FIELD_NUMBER: _ClassVar[int]
    STATIC_DURATION_FIELD_NUMBER: _ClassVar[int]
    POLYLINE_FIELD_NUMBER: _ClassVar[int]
    START_LOCATION_FIELD_NUMBER: _ClassVar[int]
    END_LOCATION_FIELD_NUMBER: _ClassVar[int]
    NAVIGATION_INSTRUCTION_FIELD_NUMBER: _ClassVar[int]
    TRAVEL_ADVISORY_FIELD_NUMBER: _ClassVar[int]
    LOCALIZED_VALUES_FIELD_NUMBER: _ClassVar[int]
    TRANSIT_DETAILS_FIELD_NUMBER: _ClassVar[int]
    TRAVEL_MODE_FIELD_NUMBER: _ClassVar[int]
    distance_meters: int
    static_duration: _duration_pb2.Duration
    polyline: _polyline_pb2.Polyline
    start_location: _location_pb2.Location
    end_location: _location_pb2.Location
    navigation_instruction: _navigation_instruction_pb2.NavigationInstruction
    travel_advisory: RouteLegStepTravelAdvisory
    localized_values: RouteLegStep.RouteLegStepLocalizedValues
    transit_details: RouteLegStepTransitDetails
    travel_mode: _route_travel_mode_pb2.RouteTravelMode
    def __init__(self, distance_meters: _Optional[int] = ..., static_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., polyline: _Optional[_Union[_polyline_pb2.Polyline, _Mapping]] = ..., start_location: _Optional[_Union[_location_pb2.Location, _Mapping]] = ..., end_location: _Optional[_Union[_location_pb2.Location, _Mapping]] = ..., navigation_instruction: _Optional[_Union[_navigation_instruction_pb2.NavigationInstruction, _Mapping]] = ..., travel_advisory: _Optional[_Union[RouteLegStepTravelAdvisory, _Mapping]] = ..., localized_values: _Optional[_Union[RouteLegStep.RouteLegStepLocalizedValues, _Mapping]] = ..., transit_details: _Optional[_Union[RouteLegStepTransitDetails, _Mapping]] = ..., travel_mode: _Optional[_Union[_route_travel_mode_pb2.RouteTravelMode, str]] = ...) -> None: ...

class RouteLegStepTransitDetails(_message.Message):
    __slots__ = ("stop_details", "localized_values", "headsign", "headway", "transit_line", "stop_count", "trip_short_text")
    class TransitStopDetails(_message.Message):
        __slots__ = ("arrival_stop", "arrival_time", "departure_stop", "departure_time")
        ARRIVAL_STOP_FIELD_NUMBER: _ClassVar[int]
        ARRIVAL_TIME_FIELD_NUMBER: _ClassVar[int]
        DEPARTURE_STOP_FIELD_NUMBER: _ClassVar[int]
        DEPARTURE_TIME_FIELD_NUMBER: _ClassVar[int]
        arrival_stop: _transit_pb2.TransitStop
        arrival_time: _timestamp_pb2.Timestamp
        departure_stop: _transit_pb2.TransitStop
        departure_time: _timestamp_pb2.Timestamp
        def __init__(self, arrival_stop: _Optional[_Union[_transit_pb2.TransitStop, _Mapping]] = ..., arrival_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., departure_stop: _Optional[_Union[_transit_pb2.TransitStop, _Mapping]] = ..., departure_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    class TransitDetailsLocalizedValues(_message.Message):
        __slots__ = ("arrival_time", "departure_time")
        ARRIVAL_TIME_FIELD_NUMBER: _ClassVar[int]
        DEPARTURE_TIME_FIELD_NUMBER: _ClassVar[int]
        arrival_time: _localized_time_pb2.LocalizedTime
        departure_time: _localized_time_pb2.LocalizedTime
        def __init__(self, arrival_time: _Optional[_Union[_localized_time_pb2.LocalizedTime, _Mapping]] = ..., departure_time: _Optional[_Union[_localized_time_pb2.LocalizedTime, _Mapping]] = ...) -> None: ...
    STOP_DETAILS_FIELD_NUMBER: _ClassVar[int]
    LOCALIZED_VALUES_FIELD_NUMBER: _ClassVar[int]
    HEADSIGN_FIELD_NUMBER: _ClassVar[int]
    HEADWAY_FIELD_NUMBER: _ClassVar[int]
    TRANSIT_LINE_FIELD_NUMBER: _ClassVar[int]
    STOP_COUNT_FIELD_NUMBER: _ClassVar[int]
    TRIP_SHORT_TEXT_FIELD_NUMBER: _ClassVar[int]
    stop_details: RouteLegStepTransitDetails.TransitStopDetails
    localized_values: RouteLegStepTransitDetails.TransitDetailsLocalizedValues
    headsign: str
    headway: _duration_pb2.Duration
    transit_line: _transit_pb2.TransitLine
    stop_count: int
    trip_short_text: str
    def __init__(self, stop_details: _Optional[_Union[RouteLegStepTransitDetails.TransitStopDetails, _Mapping]] = ..., localized_values: _Optional[_Union[RouteLegStepTransitDetails.TransitDetailsLocalizedValues, _Mapping]] = ..., headsign: _Optional[str] = ..., headway: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., transit_line: _Optional[_Union[_transit_pb2.TransitLine, _Mapping]] = ..., stop_count: _Optional[int] = ..., trip_short_text: _Optional[str] = ...) -> None: ...
