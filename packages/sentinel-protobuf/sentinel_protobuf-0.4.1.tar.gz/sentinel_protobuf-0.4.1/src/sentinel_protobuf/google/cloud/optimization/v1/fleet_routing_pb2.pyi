from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.cloud.optimization.v1 import async_model_pb2 as _async_model_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.type import latlng_pb2 as _latlng_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OptimizeToursRequest(_message.Message):
    __slots__ = ("parent", "timeout", "model", "solving_mode", "search_mode", "injected_first_solution_routes", "injected_solution_constraint", "refresh_details_routes", "interpret_injected_solutions_using_labels", "consider_road_traffic", "populate_polylines", "populate_transition_polylines", "allow_large_deadline_despite_interruption_risk", "use_geodesic_distances", "geodesic_meters_per_second", "max_validation_errors", "label", "populate_travel_step_polylines")
    class SolvingMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEFAULT_SOLVE: _ClassVar[OptimizeToursRequest.SolvingMode]
        VALIDATE_ONLY: _ClassVar[OptimizeToursRequest.SolvingMode]
        DETECT_SOME_INFEASIBLE_SHIPMENTS: _ClassVar[OptimizeToursRequest.SolvingMode]
    DEFAULT_SOLVE: OptimizeToursRequest.SolvingMode
    VALIDATE_ONLY: OptimizeToursRequest.SolvingMode
    DETECT_SOME_INFEASIBLE_SHIPMENTS: OptimizeToursRequest.SolvingMode
    class SearchMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SEARCH_MODE_UNSPECIFIED: _ClassVar[OptimizeToursRequest.SearchMode]
        RETURN_FAST: _ClassVar[OptimizeToursRequest.SearchMode]
        CONSUME_ALL_AVAILABLE_TIME: _ClassVar[OptimizeToursRequest.SearchMode]
    SEARCH_MODE_UNSPECIFIED: OptimizeToursRequest.SearchMode
    RETURN_FAST: OptimizeToursRequest.SearchMode
    CONSUME_ALL_AVAILABLE_TIME: OptimizeToursRequest.SearchMode
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    SOLVING_MODE_FIELD_NUMBER: _ClassVar[int]
    SEARCH_MODE_FIELD_NUMBER: _ClassVar[int]
    INJECTED_FIRST_SOLUTION_ROUTES_FIELD_NUMBER: _ClassVar[int]
    INJECTED_SOLUTION_CONSTRAINT_FIELD_NUMBER: _ClassVar[int]
    REFRESH_DETAILS_ROUTES_FIELD_NUMBER: _ClassVar[int]
    INTERPRET_INJECTED_SOLUTIONS_USING_LABELS_FIELD_NUMBER: _ClassVar[int]
    CONSIDER_ROAD_TRAFFIC_FIELD_NUMBER: _ClassVar[int]
    POPULATE_POLYLINES_FIELD_NUMBER: _ClassVar[int]
    POPULATE_TRANSITION_POLYLINES_FIELD_NUMBER: _ClassVar[int]
    ALLOW_LARGE_DEADLINE_DESPITE_INTERRUPTION_RISK_FIELD_NUMBER: _ClassVar[int]
    USE_GEODESIC_DISTANCES_FIELD_NUMBER: _ClassVar[int]
    GEODESIC_METERS_PER_SECOND_FIELD_NUMBER: _ClassVar[int]
    MAX_VALIDATION_ERRORS_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    POPULATE_TRAVEL_STEP_POLYLINES_FIELD_NUMBER: _ClassVar[int]
    parent: str
    timeout: _duration_pb2.Duration
    model: ShipmentModel
    solving_mode: OptimizeToursRequest.SolvingMode
    search_mode: OptimizeToursRequest.SearchMode
    injected_first_solution_routes: _containers.RepeatedCompositeFieldContainer[ShipmentRoute]
    injected_solution_constraint: InjectedSolutionConstraint
    refresh_details_routes: _containers.RepeatedCompositeFieldContainer[ShipmentRoute]
    interpret_injected_solutions_using_labels: bool
    consider_road_traffic: bool
    populate_polylines: bool
    populate_transition_polylines: bool
    allow_large_deadline_despite_interruption_risk: bool
    use_geodesic_distances: bool
    geodesic_meters_per_second: float
    max_validation_errors: int
    label: str
    populate_travel_step_polylines: bool
    def __init__(self, parent: _Optional[str] = ..., timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., model: _Optional[_Union[ShipmentModel, _Mapping]] = ..., solving_mode: _Optional[_Union[OptimizeToursRequest.SolvingMode, str]] = ..., search_mode: _Optional[_Union[OptimizeToursRequest.SearchMode, str]] = ..., injected_first_solution_routes: _Optional[_Iterable[_Union[ShipmentRoute, _Mapping]]] = ..., injected_solution_constraint: _Optional[_Union[InjectedSolutionConstraint, _Mapping]] = ..., refresh_details_routes: _Optional[_Iterable[_Union[ShipmentRoute, _Mapping]]] = ..., interpret_injected_solutions_using_labels: bool = ..., consider_road_traffic: bool = ..., populate_polylines: bool = ..., populate_transition_polylines: bool = ..., allow_large_deadline_despite_interruption_risk: bool = ..., use_geodesic_distances: bool = ..., geodesic_meters_per_second: _Optional[float] = ..., max_validation_errors: _Optional[int] = ..., label: _Optional[str] = ..., populate_travel_step_polylines: bool = ...) -> None: ...

class OptimizeToursResponse(_message.Message):
    __slots__ = ("routes", "request_label", "skipped_shipments", "validation_errors", "metrics", "total_cost")
    class Metrics(_message.Message):
        __slots__ = ("aggregated_route_metrics", "skipped_mandatory_shipment_count", "used_vehicle_count", "earliest_vehicle_start_time", "latest_vehicle_end_time", "costs", "total_cost")
        class CostsEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: float
            def __init__(self, key: _Optional[str] = ..., value: _Optional[float] = ...) -> None: ...
        AGGREGATED_ROUTE_METRICS_FIELD_NUMBER: _ClassVar[int]
        SKIPPED_MANDATORY_SHIPMENT_COUNT_FIELD_NUMBER: _ClassVar[int]
        USED_VEHICLE_COUNT_FIELD_NUMBER: _ClassVar[int]
        EARLIEST_VEHICLE_START_TIME_FIELD_NUMBER: _ClassVar[int]
        LATEST_VEHICLE_END_TIME_FIELD_NUMBER: _ClassVar[int]
        COSTS_FIELD_NUMBER: _ClassVar[int]
        TOTAL_COST_FIELD_NUMBER: _ClassVar[int]
        aggregated_route_metrics: AggregatedMetrics
        skipped_mandatory_shipment_count: int
        used_vehicle_count: int
        earliest_vehicle_start_time: _timestamp_pb2.Timestamp
        latest_vehicle_end_time: _timestamp_pb2.Timestamp
        costs: _containers.ScalarMap[str, float]
        total_cost: float
        def __init__(self, aggregated_route_metrics: _Optional[_Union[AggregatedMetrics, _Mapping]] = ..., skipped_mandatory_shipment_count: _Optional[int] = ..., used_vehicle_count: _Optional[int] = ..., earliest_vehicle_start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., latest_vehicle_end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., costs: _Optional[_Mapping[str, float]] = ..., total_cost: _Optional[float] = ...) -> None: ...
    ROUTES_FIELD_NUMBER: _ClassVar[int]
    REQUEST_LABEL_FIELD_NUMBER: _ClassVar[int]
    SKIPPED_SHIPMENTS_FIELD_NUMBER: _ClassVar[int]
    VALIDATION_ERRORS_FIELD_NUMBER: _ClassVar[int]
    METRICS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COST_FIELD_NUMBER: _ClassVar[int]
    routes: _containers.RepeatedCompositeFieldContainer[ShipmentRoute]
    request_label: str
    skipped_shipments: _containers.RepeatedCompositeFieldContainer[SkippedShipment]
    validation_errors: _containers.RepeatedCompositeFieldContainer[OptimizeToursValidationError]
    metrics: OptimizeToursResponse.Metrics
    total_cost: float
    def __init__(self, routes: _Optional[_Iterable[_Union[ShipmentRoute, _Mapping]]] = ..., request_label: _Optional[str] = ..., skipped_shipments: _Optional[_Iterable[_Union[SkippedShipment, _Mapping]]] = ..., validation_errors: _Optional[_Iterable[_Union[OptimizeToursValidationError, _Mapping]]] = ..., metrics: _Optional[_Union[OptimizeToursResponse.Metrics, _Mapping]] = ..., total_cost: _Optional[float] = ...) -> None: ...

class BatchOptimizeToursRequest(_message.Message):
    __slots__ = ("parent", "model_configs")
    class AsyncModelConfig(_message.Message):
        __slots__ = ("display_name", "input_config", "output_config", "enable_checkpoints")
        DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
        INPUT_CONFIG_FIELD_NUMBER: _ClassVar[int]
        OUTPUT_CONFIG_FIELD_NUMBER: _ClassVar[int]
        ENABLE_CHECKPOINTS_FIELD_NUMBER: _ClassVar[int]
        display_name: str
        input_config: _async_model_pb2.InputConfig
        output_config: _async_model_pb2.OutputConfig
        enable_checkpoints: bool
        def __init__(self, display_name: _Optional[str] = ..., input_config: _Optional[_Union[_async_model_pb2.InputConfig, _Mapping]] = ..., output_config: _Optional[_Union[_async_model_pb2.OutputConfig, _Mapping]] = ..., enable_checkpoints: bool = ...) -> None: ...
    PARENT_FIELD_NUMBER: _ClassVar[int]
    MODEL_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    parent: str
    model_configs: _containers.RepeatedCompositeFieldContainer[BatchOptimizeToursRequest.AsyncModelConfig]
    def __init__(self, parent: _Optional[str] = ..., model_configs: _Optional[_Iterable[_Union[BatchOptimizeToursRequest.AsyncModelConfig, _Mapping]]] = ...) -> None: ...

class BatchOptimizeToursResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ShipmentModel(_message.Message):
    __slots__ = ("shipments", "vehicles", "max_active_vehicles", "global_start_time", "global_end_time", "global_duration_cost_per_hour", "duration_distance_matrices", "duration_distance_matrix_src_tags", "duration_distance_matrix_dst_tags", "transition_attributes", "shipment_type_incompatibilities", "shipment_type_requirements", "precedence_rules", "break_rules")
    class DurationDistanceMatrix(_message.Message):
        __slots__ = ("rows", "vehicle_start_tag")
        class Row(_message.Message):
            __slots__ = ("durations", "meters")
            DURATIONS_FIELD_NUMBER: _ClassVar[int]
            METERS_FIELD_NUMBER: _ClassVar[int]
            durations: _containers.RepeatedCompositeFieldContainer[_duration_pb2.Duration]
            meters: _containers.RepeatedScalarFieldContainer[float]
            def __init__(self, durations: _Optional[_Iterable[_Union[_duration_pb2.Duration, _Mapping]]] = ..., meters: _Optional[_Iterable[float]] = ...) -> None: ...
        ROWS_FIELD_NUMBER: _ClassVar[int]
        VEHICLE_START_TAG_FIELD_NUMBER: _ClassVar[int]
        rows: _containers.RepeatedCompositeFieldContainer[ShipmentModel.DurationDistanceMatrix.Row]
        vehicle_start_tag: str
        def __init__(self, rows: _Optional[_Iterable[_Union[ShipmentModel.DurationDistanceMatrix.Row, _Mapping]]] = ..., vehicle_start_tag: _Optional[str] = ...) -> None: ...
    class PrecedenceRule(_message.Message):
        __slots__ = ("first_index", "first_is_delivery", "second_index", "second_is_delivery", "offset_duration")
        FIRST_INDEX_FIELD_NUMBER: _ClassVar[int]
        FIRST_IS_DELIVERY_FIELD_NUMBER: _ClassVar[int]
        SECOND_INDEX_FIELD_NUMBER: _ClassVar[int]
        SECOND_IS_DELIVERY_FIELD_NUMBER: _ClassVar[int]
        OFFSET_DURATION_FIELD_NUMBER: _ClassVar[int]
        first_index: int
        first_is_delivery: bool
        second_index: int
        second_is_delivery: bool
        offset_duration: _duration_pb2.Duration
        def __init__(self, first_index: _Optional[int] = ..., first_is_delivery: bool = ..., second_index: _Optional[int] = ..., second_is_delivery: bool = ..., offset_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...
    class BreakRule(_message.Message):
        __slots__ = ("break_requests", "frequency_constraints")
        class BreakRequest(_message.Message):
            __slots__ = ("earliest_start_time", "latest_start_time", "min_duration")
            EARLIEST_START_TIME_FIELD_NUMBER: _ClassVar[int]
            LATEST_START_TIME_FIELD_NUMBER: _ClassVar[int]
            MIN_DURATION_FIELD_NUMBER: _ClassVar[int]
            earliest_start_time: _timestamp_pb2.Timestamp
            latest_start_time: _timestamp_pb2.Timestamp
            min_duration: _duration_pb2.Duration
            def __init__(self, earliest_start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., latest_start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., min_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...
        class FrequencyConstraint(_message.Message):
            __slots__ = ("min_break_duration", "max_inter_break_duration")
            MIN_BREAK_DURATION_FIELD_NUMBER: _ClassVar[int]
            MAX_INTER_BREAK_DURATION_FIELD_NUMBER: _ClassVar[int]
            min_break_duration: _duration_pb2.Duration
            max_inter_break_duration: _duration_pb2.Duration
            def __init__(self, min_break_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., max_inter_break_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...
        BREAK_REQUESTS_FIELD_NUMBER: _ClassVar[int]
        FREQUENCY_CONSTRAINTS_FIELD_NUMBER: _ClassVar[int]
        break_requests: _containers.RepeatedCompositeFieldContainer[ShipmentModel.BreakRule.BreakRequest]
        frequency_constraints: _containers.RepeatedCompositeFieldContainer[ShipmentModel.BreakRule.FrequencyConstraint]
        def __init__(self, break_requests: _Optional[_Iterable[_Union[ShipmentModel.BreakRule.BreakRequest, _Mapping]]] = ..., frequency_constraints: _Optional[_Iterable[_Union[ShipmentModel.BreakRule.FrequencyConstraint, _Mapping]]] = ...) -> None: ...
    SHIPMENTS_FIELD_NUMBER: _ClassVar[int]
    VEHICLES_FIELD_NUMBER: _ClassVar[int]
    MAX_ACTIVE_VEHICLES_FIELD_NUMBER: _ClassVar[int]
    GLOBAL_START_TIME_FIELD_NUMBER: _ClassVar[int]
    GLOBAL_END_TIME_FIELD_NUMBER: _ClassVar[int]
    GLOBAL_DURATION_COST_PER_HOUR_FIELD_NUMBER: _ClassVar[int]
    DURATION_DISTANCE_MATRICES_FIELD_NUMBER: _ClassVar[int]
    DURATION_DISTANCE_MATRIX_SRC_TAGS_FIELD_NUMBER: _ClassVar[int]
    DURATION_DISTANCE_MATRIX_DST_TAGS_FIELD_NUMBER: _ClassVar[int]
    TRANSITION_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    SHIPMENT_TYPE_INCOMPATIBILITIES_FIELD_NUMBER: _ClassVar[int]
    SHIPMENT_TYPE_REQUIREMENTS_FIELD_NUMBER: _ClassVar[int]
    PRECEDENCE_RULES_FIELD_NUMBER: _ClassVar[int]
    BREAK_RULES_FIELD_NUMBER: _ClassVar[int]
    shipments: _containers.RepeatedCompositeFieldContainer[Shipment]
    vehicles: _containers.RepeatedCompositeFieldContainer[Vehicle]
    max_active_vehicles: int
    global_start_time: _timestamp_pb2.Timestamp
    global_end_time: _timestamp_pb2.Timestamp
    global_duration_cost_per_hour: float
    duration_distance_matrices: _containers.RepeatedCompositeFieldContainer[ShipmentModel.DurationDistanceMatrix]
    duration_distance_matrix_src_tags: _containers.RepeatedScalarFieldContainer[str]
    duration_distance_matrix_dst_tags: _containers.RepeatedScalarFieldContainer[str]
    transition_attributes: _containers.RepeatedCompositeFieldContainer[TransitionAttributes]
    shipment_type_incompatibilities: _containers.RepeatedCompositeFieldContainer[ShipmentTypeIncompatibility]
    shipment_type_requirements: _containers.RepeatedCompositeFieldContainer[ShipmentTypeRequirement]
    precedence_rules: _containers.RepeatedCompositeFieldContainer[ShipmentModel.PrecedenceRule]
    break_rules: _containers.RepeatedCompositeFieldContainer[ShipmentModel.BreakRule]
    def __init__(self, shipments: _Optional[_Iterable[_Union[Shipment, _Mapping]]] = ..., vehicles: _Optional[_Iterable[_Union[Vehicle, _Mapping]]] = ..., max_active_vehicles: _Optional[int] = ..., global_start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., global_end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., global_duration_cost_per_hour: _Optional[float] = ..., duration_distance_matrices: _Optional[_Iterable[_Union[ShipmentModel.DurationDistanceMatrix, _Mapping]]] = ..., duration_distance_matrix_src_tags: _Optional[_Iterable[str]] = ..., duration_distance_matrix_dst_tags: _Optional[_Iterable[str]] = ..., transition_attributes: _Optional[_Iterable[_Union[TransitionAttributes, _Mapping]]] = ..., shipment_type_incompatibilities: _Optional[_Iterable[_Union[ShipmentTypeIncompatibility, _Mapping]]] = ..., shipment_type_requirements: _Optional[_Iterable[_Union[ShipmentTypeRequirement, _Mapping]]] = ..., precedence_rules: _Optional[_Iterable[_Union[ShipmentModel.PrecedenceRule, _Mapping]]] = ..., break_rules: _Optional[_Iterable[_Union[ShipmentModel.BreakRule, _Mapping]]] = ...) -> None: ...

class Shipment(_message.Message):
    __slots__ = ("pickups", "deliveries", "load_demands", "penalty_cost", "allowed_vehicle_indices", "costs_per_vehicle", "costs_per_vehicle_indices", "pickup_to_delivery_relative_detour_limit", "pickup_to_delivery_absolute_detour_limit", "pickup_to_delivery_time_limit", "shipment_type", "label", "ignore", "demands")
    class VisitRequest(_message.Message):
        __slots__ = ("arrival_location", "arrival_waypoint", "departure_location", "departure_waypoint", "tags", "time_windows", "duration", "cost", "load_demands", "visit_types", "label", "demands")
        class LoadDemandsEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: Shipment.Load
            def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Shipment.Load, _Mapping]] = ...) -> None: ...
        ARRIVAL_LOCATION_FIELD_NUMBER: _ClassVar[int]
        ARRIVAL_WAYPOINT_FIELD_NUMBER: _ClassVar[int]
        DEPARTURE_LOCATION_FIELD_NUMBER: _ClassVar[int]
        DEPARTURE_WAYPOINT_FIELD_NUMBER: _ClassVar[int]
        TAGS_FIELD_NUMBER: _ClassVar[int]
        TIME_WINDOWS_FIELD_NUMBER: _ClassVar[int]
        DURATION_FIELD_NUMBER: _ClassVar[int]
        COST_FIELD_NUMBER: _ClassVar[int]
        LOAD_DEMANDS_FIELD_NUMBER: _ClassVar[int]
        VISIT_TYPES_FIELD_NUMBER: _ClassVar[int]
        LABEL_FIELD_NUMBER: _ClassVar[int]
        DEMANDS_FIELD_NUMBER: _ClassVar[int]
        arrival_location: _latlng_pb2.LatLng
        arrival_waypoint: Waypoint
        departure_location: _latlng_pb2.LatLng
        departure_waypoint: Waypoint
        tags: _containers.RepeatedScalarFieldContainer[str]
        time_windows: _containers.RepeatedCompositeFieldContainer[TimeWindow]
        duration: _duration_pb2.Duration
        cost: float
        load_demands: _containers.MessageMap[str, Shipment.Load]
        visit_types: _containers.RepeatedScalarFieldContainer[str]
        label: str
        demands: _containers.RepeatedCompositeFieldContainer[CapacityQuantity]
        def __init__(self, arrival_location: _Optional[_Union[_latlng_pb2.LatLng, _Mapping]] = ..., arrival_waypoint: _Optional[_Union[Waypoint, _Mapping]] = ..., departure_location: _Optional[_Union[_latlng_pb2.LatLng, _Mapping]] = ..., departure_waypoint: _Optional[_Union[Waypoint, _Mapping]] = ..., tags: _Optional[_Iterable[str]] = ..., time_windows: _Optional[_Iterable[_Union[TimeWindow, _Mapping]]] = ..., duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., cost: _Optional[float] = ..., load_demands: _Optional[_Mapping[str, Shipment.Load]] = ..., visit_types: _Optional[_Iterable[str]] = ..., label: _Optional[str] = ..., demands: _Optional[_Iterable[_Union[CapacityQuantity, _Mapping]]] = ...) -> None: ...
    class Load(_message.Message):
        __slots__ = ("amount",)
        AMOUNT_FIELD_NUMBER: _ClassVar[int]
        amount: int
        def __init__(self, amount: _Optional[int] = ...) -> None: ...
    class LoadDemandsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Shipment.Load
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Shipment.Load, _Mapping]] = ...) -> None: ...
    PICKUPS_FIELD_NUMBER: _ClassVar[int]
    DELIVERIES_FIELD_NUMBER: _ClassVar[int]
    LOAD_DEMANDS_FIELD_NUMBER: _ClassVar[int]
    PENALTY_COST_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_VEHICLE_INDICES_FIELD_NUMBER: _ClassVar[int]
    COSTS_PER_VEHICLE_FIELD_NUMBER: _ClassVar[int]
    COSTS_PER_VEHICLE_INDICES_FIELD_NUMBER: _ClassVar[int]
    PICKUP_TO_DELIVERY_RELATIVE_DETOUR_LIMIT_FIELD_NUMBER: _ClassVar[int]
    PICKUP_TO_DELIVERY_ABSOLUTE_DETOUR_LIMIT_FIELD_NUMBER: _ClassVar[int]
    PICKUP_TO_DELIVERY_TIME_LIMIT_FIELD_NUMBER: _ClassVar[int]
    SHIPMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    IGNORE_FIELD_NUMBER: _ClassVar[int]
    DEMANDS_FIELD_NUMBER: _ClassVar[int]
    pickups: _containers.RepeatedCompositeFieldContainer[Shipment.VisitRequest]
    deliveries: _containers.RepeatedCompositeFieldContainer[Shipment.VisitRequest]
    load_demands: _containers.MessageMap[str, Shipment.Load]
    penalty_cost: float
    allowed_vehicle_indices: _containers.RepeatedScalarFieldContainer[int]
    costs_per_vehicle: _containers.RepeatedScalarFieldContainer[float]
    costs_per_vehicle_indices: _containers.RepeatedScalarFieldContainer[int]
    pickup_to_delivery_relative_detour_limit: float
    pickup_to_delivery_absolute_detour_limit: _duration_pb2.Duration
    pickup_to_delivery_time_limit: _duration_pb2.Duration
    shipment_type: str
    label: str
    ignore: bool
    demands: _containers.RepeatedCompositeFieldContainer[CapacityQuantity]
    def __init__(self, pickups: _Optional[_Iterable[_Union[Shipment.VisitRequest, _Mapping]]] = ..., deliveries: _Optional[_Iterable[_Union[Shipment.VisitRequest, _Mapping]]] = ..., load_demands: _Optional[_Mapping[str, Shipment.Load]] = ..., penalty_cost: _Optional[float] = ..., allowed_vehicle_indices: _Optional[_Iterable[int]] = ..., costs_per_vehicle: _Optional[_Iterable[float]] = ..., costs_per_vehicle_indices: _Optional[_Iterable[int]] = ..., pickup_to_delivery_relative_detour_limit: _Optional[float] = ..., pickup_to_delivery_absolute_detour_limit: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., pickup_to_delivery_time_limit: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., shipment_type: _Optional[str] = ..., label: _Optional[str] = ..., ignore: bool = ..., demands: _Optional[_Iterable[_Union[CapacityQuantity, _Mapping]]] = ...) -> None: ...

class ShipmentTypeIncompatibility(_message.Message):
    __slots__ = ("types", "incompatibility_mode")
    class IncompatibilityMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        INCOMPATIBILITY_MODE_UNSPECIFIED: _ClassVar[ShipmentTypeIncompatibility.IncompatibilityMode]
        NOT_PERFORMED_BY_SAME_VEHICLE: _ClassVar[ShipmentTypeIncompatibility.IncompatibilityMode]
        NOT_IN_SAME_VEHICLE_SIMULTANEOUSLY: _ClassVar[ShipmentTypeIncompatibility.IncompatibilityMode]
    INCOMPATIBILITY_MODE_UNSPECIFIED: ShipmentTypeIncompatibility.IncompatibilityMode
    NOT_PERFORMED_BY_SAME_VEHICLE: ShipmentTypeIncompatibility.IncompatibilityMode
    NOT_IN_SAME_VEHICLE_SIMULTANEOUSLY: ShipmentTypeIncompatibility.IncompatibilityMode
    TYPES_FIELD_NUMBER: _ClassVar[int]
    INCOMPATIBILITY_MODE_FIELD_NUMBER: _ClassVar[int]
    types: _containers.RepeatedScalarFieldContainer[str]
    incompatibility_mode: ShipmentTypeIncompatibility.IncompatibilityMode
    def __init__(self, types: _Optional[_Iterable[str]] = ..., incompatibility_mode: _Optional[_Union[ShipmentTypeIncompatibility.IncompatibilityMode, str]] = ...) -> None: ...

class ShipmentTypeRequirement(_message.Message):
    __slots__ = ("required_shipment_type_alternatives", "dependent_shipment_types", "requirement_mode")
    class RequirementMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        REQUIREMENT_MODE_UNSPECIFIED: _ClassVar[ShipmentTypeRequirement.RequirementMode]
        PERFORMED_BY_SAME_VEHICLE: _ClassVar[ShipmentTypeRequirement.RequirementMode]
        IN_SAME_VEHICLE_AT_PICKUP_TIME: _ClassVar[ShipmentTypeRequirement.RequirementMode]
        IN_SAME_VEHICLE_AT_DELIVERY_TIME: _ClassVar[ShipmentTypeRequirement.RequirementMode]
    REQUIREMENT_MODE_UNSPECIFIED: ShipmentTypeRequirement.RequirementMode
    PERFORMED_BY_SAME_VEHICLE: ShipmentTypeRequirement.RequirementMode
    IN_SAME_VEHICLE_AT_PICKUP_TIME: ShipmentTypeRequirement.RequirementMode
    IN_SAME_VEHICLE_AT_DELIVERY_TIME: ShipmentTypeRequirement.RequirementMode
    REQUIRED_SHIPMENT_TYPE_ALTERNATIVES_FIELD_NUMBER: _ClassVar[int]
    DEPENDENT_SHIPMENT_TYPES_FIELD_NUMBER: _ClassVar[int]
    REQUIREMENT_MODE_FIELD_NUMBER: _ClassVar[int]
    required_shipment_type_alternatives: _containers.RepeatedScalarFieldContainer[str]
    dependent_shipment_types: _containers.RepeatedScalarFieldContainer[str]
    requirement_mode: ShipmentTypeRequirement.RequirementMode
    def __init__(self, required_shipment_type_alternatives: _Optional[_Iterable[str]] = ..., dependent_shipment_types: _Optional[_Iterable[str]] = ..., requirement_mode: _Optional[_Union[ShipmentTypeRequirement.RequirementMode, str]] = ...) -> None: ...

class RouteModifiers(_message.Message):
    __slots__ = ("avoid_tolls", "avoid_highways", "avoid_ferries", "avoid_indoor")
    AVOID_TOLLS_FIELD_NUMBER: _ClassVar[int]
    AVOID_HIGHWAYS_FIELD_NUMBER: _ClassVar[int]
    AVOID_FERRIES_FIELD_NUMBER: _ClassVar[int]
    AVOID_INDOOR_FIELD_NUMBER: _ClassVar[int]
    avoid_tolls: bool
    avoid_highways: bool
    avoid_ferries: bool
    avoid_indoor: bool
    def __init__(self, avoid_tolls: bool = ..., avoid_highways: bool = ..., avoid_ferries: bool = ..., avoid_indoor: bool = ...) -> None: ...

class Vehicle(_message.Message):
    __slots__ = ("travel_mode", "route_modifiers", "start_location", "start_waypoint", "end_location", "end_waypoint", "start_tags", "end_tags", "start_time_windows", "end_time_windows", "travel_duration_multiple", "unloading_policy", "load_limits", "cost_per_hour", "cost_per_traveled_hour", "cost_per_kilometer", "fixed_cost", "used_if_route_is_empty", "route_duration_limit", "travel_duration_limit", "route_distance_limit", "extra_visit_duration_for_visit_type", "break_rule", "label", "ignore", "break_rule_indices", "capacities", "start_load_intervals", "end_load_intervals")
    class TravelMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TRAVEL_MODE_UNSPECIFIED: _ClassVar[Vehicle.TravelMode]
        DRIVING: _ClassVar[Vehicle.TravelMode]
        WALKING: _ClassVar[Vehicle.TravelMode]
    TRAVEL_MODE_UNSPECIFIED: Vehicle.TravelMode
    DRIVING: Vehicle.TravelMode
    WALKING: Vehicle.TravelMode
    class UnloadingPolicy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNLOADING_POLICY_UNSPECIFIED: _ClassVar[Vehicle.UnloadingPolicy]
        LAST_IN_FIRST_OUT: _ClassVar[Vehicle.UnloadingPolicy]
        FIRST_IN_FIRST_OUT: _ClassVar[Vehicle.UnloadingPolicy]
    UNLOADING_POLICY_UNSPECIFIED: Vehicle.UnloadingPolicy
    LAST_IN_FIRST_OUT: Vehicle.UnloadingPolicy
    FIRST_IN_FIRST_OUT: Vehicle.UnloadingPolicy
    class LoadLimit(_message.Message):
        __slots__ = ("max_load", "soft_max_load", "cost_per_unit_above_soft_max", "start_load_interval", "end_load_interval")
        class Interval(_message.Message):
            __slots__ = ("min", "max")
            MIN_FIELD_NUMBER: _ClassVar[int]
            MAX_FIELD_NUMBER: _ClassVar[int]
            min: int
            max: int
            def __init__(self, min: _Optional[int] = ..., max: _Optional[int] = ...) -> None: ...
        MAX_LOAD_FIELD_NUMBER: _ClassVar[int]
        SOFT_MAX_LOAD_FIELD_NUMBER: _ClassVar[int]
        COST_PER_UNIT_ABOVE_SOFT_MAX_FIELD_NUMBER: _ClassVar[int]
        START_LOAD_INTERVAL_FIELD_NUMBER: _ClassVar[int]
        END_LOAD_INTERVAL_FIELD_NUMBER: _ClassVar[int]
        max_load: int
        soft_max_load: int
        cost_per_unit_above_soft_max: float
        start_load_interval: Vehicle.LoadLimit.Interval
        end_load_interval: Vehicle.LoadLimit.Interval
        def __init__(self, max_load: _Optional[int] = ..., soft_max_load: _Optional[int] = ..., cost_per_unit_above_soft_max: _Optional[float] = ..., start_load_interval: _Optional[_Union[Vehicle.LoadLimit.Interval, _Mapping]] = ..., end_load_interval: _Optional[_Union[Vehicle.LoadLimit.Interval, _Mapping]] = ...) -> None: ...
    class DurationLimit(_message.Message):
        __slots__ = ("max_duration", "soft_max_duration", "cost_per_hour_after_soft_max", "quadratic_soft_max_duration", "cost_per_square_hour_after_quadratic_soft_max")
        MAX_DURATION_FIELD_NUMBER: _ClassVar[int]
        SOFT_MAX_DURATION_FIELD_NUMBER: _ClassVar[int]
        COST_PER_HOUR_AFTER_SOFT_MAX_FIELD_NUMBER: _ClassVar[int]
        QUADRATIC_SOFT_MAX_DURATION_FIELD_NUMBER: _ClassVar[int]
        COST_PER_SQUARE_HOUR_AFTER_QUADRATIC_SOFT_MAX_FIELD_NUMBER: _ClassVar[int]
        max_duration: _duration_pb2.Duration
        soft_max_duration: _duration_pb2.Duration
        cost_per_hour_after_soft_max: float
        quadratic_soft_max_duration: _duration_pb2.Duration
        cost_per_square_hour_after_quadratic_soft_max: float
        def __init__(self, max_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., soft_max_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., cost_per_hour_after_soft_max: _Optional[float] = ..., quadratic_soft_max_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., cost_per_square_hour_after_quadratic_soft_max: _Optional[float] = ...) -> None: ...
    class LoadLimitsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Vehicle.LoadLimit
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Vehicle.LoadLimit, _Mapping]] = ...) -> None: ...
    class ExtraVisitDurationForVisitTypeEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _duration_pb2.Duration
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...
    TRAVEL_MODE_FIELD_NUMBER: _ClassVar[int]
    ROUTE_MODIFIERS_FIELD_NUMBER: _ClassVar[int]
    START_LOCATION_FIELD_NUMBER: _ClassVar[int]
    START_WAYPOINT_FIELD_NUMBER: _ClassVar[int]
    END_LOCATION_FIELD_NUMBER: _ClassVar[int]
    END_WAYPOINT_FIELD_NUMBER: _ClassVar[int]
    START_TAGS_FIELD_NUMBER: _ClassVar[int]
    END_TAGS_FIELD_NUMBER: _ClassVar[int]
    START_TIME_WINDOWS_FIELD_NUMBER: _ClassVar[int]
    END_TIME_WINDOWS_FIELD_NUMBER: _ClassVar[int]
    TRAVEL_DURATION_MULTIPLE_FIELD_NUMBER: _ClassVar[int]
    UNLOADING_POLICY_FIELD_NUMBER: _ClassVar[int]
    LOAD_LIMITS_FIELD_NUMBER: _ClassVar[int]
    COST_PER_HOUR_FIELD_NUMBER: _ClassVar[int]
    COST_PER_TRAVELED_HOUR_FIELD_NUMBER: _ClassVar[int]
    COST_PER_KILOMETER_FIELD_NUMBER: _ClassVar[int]
    FIXED_COST_FIELD_NUMBER: _ClassVar[int]
    USED_IF_ROUTE_IS_EMPTY_FIELD_NUMBER: _ClassVar[int]
    ROUTE_DURATION_LIMIT_FIELD_NUMBER: _ClassVar[int]
    TRAVEL_DURATION_LIMIT_FIELD_NUMBER: _ClassVar[int]
    ROUTE_DISTANCE_LIMIT_FIELD_NUMBER: _ClassVar[int]
    EXTRA_VISIT_DURATION_FOR_VISIT_TYPE_FIELD_NUMBER: _ClassVar[int]
    BREAK_RULE_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    IGNORE_FIELD_NUMBER: _ClassVar[int]
    BREAK_RULE_INDICES_FIELD_NUMBER: _ClassVar[int]
    CAPACITIES_FIELD_NUMBER: _ClassVar[int]
    START_LOAD_INTERVALS_FIELD_NUMBER: _ClassVar[int]
    END_LOAD_INTERVALS_FIELD_NUMBER: _ClassVar[int]
    travel_mode: Vehicle.TravelMode
    route_modifiers: RouteModifiers
    start_location: _latlng_pb2.LatLng
    start_waypoint: Waypoint
    end_location: _latlng_pb2.LatLng
    end_waypoint: Waypoint
    start_tags: _containers.RepeatedScalarFieldContainer[str]
    end_tags: _containers.RepeatedScalarFieldContainer[str]
    start_time_windows: _containers.RepeatedCompositeFieldContainer[TimeWindow]
    end_time_windows: _containers.RepeatedCompositeFieldContainer[TimeWindow]
    travel_duration_multiple: float
    unloading_policy: Vehicle.UnloadingPolicy
    load_limits: _containers.MessageMap[str, Vehicle.LoadLimit]
    cost_per_hour: float
    cost_per_traveled_hour: float
    cost_per_kilometer: float
    fixed_cost: float
    used_if_route_is_empty: bool
    route_duration_limit: Vehicle.DurationLimit
    travel_duration_limit: Vehicle.DurationLimit
    route_distance_limit: DistanceLimit
    extra_visit_duration_for_visit_type: _containers.MessageMap[str, _duration_pb2.Duration]
    break_rule: BreakRule
    label: str
    ignore: bool
    break_rule_indices: _containers.RepeatedScalarFieldContainer[int]
    capacities: _containers.RepeatedCompositeFieldContainer[CapacityQuantity]
    start_load_intervals: _containers.RepeatedCompositeFieldContainer[CapacityQuantityInterval]
    end_load_intervals: _containers.RepeatedCompositeFieldContainer[CapacityQuantityInterval]
    def __init__(self, travel_mode: _Optional[_Union[Vehicle.TravelMode, str]] = ..., route_modifiers: _Optional[_Union[RouteModifiers, _Mapping]] = ..., start_location: _Optional[_Union[_latlng_pb2.LatLng, _Mapping]] = ..., start_waypoint: _Optional[_Union[Waypoint, _Mapping]] = ..., end_location: _Optional[_Union[_latlng_pb2.LatLng, _Mapping]] = ..., end_waypoint: _Optional[_Union[Waypoint, _Mapping]] = ..., start_tags: _Optional[_Iterable[str]] = ..., end_tags: _Optional[_Iterable[str]] = ..., start_time_windows: _Optional[_Iterable[_Union[TimeWindow, _Mapping]]] = ..., end_time_windows: _Optional[_Iterable[_Union[TimeWindow, _Mapping]]] = ..., travel_duration_multiple: _Optional[float] = ..., unloading_policy: _Optional[_Union[Vehicle.UnloadingPolicy, str]] = ..., load_limits: _Optional[_Mapping[str, Vehicle.LoadLimit]] = ..., cost_per_hour: _Optional[float] = ..., cost_per_traveled_hour: _Optional[float] = ..., cost_per_kilometer: _Optional[float] = ..., fixed_cost: _Optional[float] = ..., used_if_route_is_empty: bool = ..., route_duration_limit: _Optional[_Union[Vehicle.DurationLimit, _Mapping]] = ..., travel_duration_limit: _Optional[_Union[Vehicle.DurationLimit, _Mapping]] = ..., route_distance_limit: _Optional[_Union[DistanceLimit, _Mapping]] = ..., extra_visit_duration_for_visit_type: _Optional[_Mapping[str, _duration_pb2.Duration]] = ..., break_rule: _Optional[_Union[BreakRule, _Mapping]] = ..., label: _Optional[str] = ..., ignore: bool = ..., break_rule_indices: _Optional[_Iterable[int]] = ..., capacities: _Optional[_Iterable[_Union[CapacityQuantity, _Mapping]]] = ..., start_load_intervals: _Optional[_Iterable[_Union[CapacityQuantityInterval, _Mapping]]] = ..., end_load_intervals: _Optional[_Iterable[_Union[CapacityQuantityInterval, _Mapping]]] = ...) -> None: ...

class TimeWindow(_message.Message):
    __slots__ = ("start_time", "end_time", "soft_start_time", "soft_end_time", "cost_per_hour_before_soft_start_time", "cost_per_hour_after_soft_end_time")
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    SOFT_START_TIME_FIELD_NUMBER: _ClassVar[int]
    SOFT_END_TIME_FIELD_NUMBER: _ClassVar[int]
    COST_PER_HOUR_BEFORE_SOFT_START_TIME_FIELD_NUMBER: _ClassVar[int]
    COST_PER_HOUR_AFTER_SOFT_END_TIME_FIELD_NUMBER: _ClassVar[int]
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    soft_start_time: _timestamp_pb2.Timestamp
    soft_end_time: _timestamp_pb2.Timestamp
    cost_per_hour_before_soft_start_time: float
    cost_per_hour_after_soft_end_time: float
    def __init__(self, start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., soft_start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., soft_end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., cost_per_hour_before_soft_start_time: _Optional[float] = ..., cost_per_hour_after_soft_end_time: _Optional[float] = ...) -> None: ...

class CapacityQuantity(_message.Message):
    __slots__ = ("type", "value")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    type: str
    value: int
    def __init__(self, type: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...

class CapacityQuantityInterval(_message.Message):
    __slots__ = ("type", "min_value", "max_value")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    MIN_VALUE_FIELD_NUMBER: _ClassVar[int]
    MAX_VALUE_FIELD_NUMBER: _ClassVar[int]
    type: str
    min_value: int
    max_value: int
    def __init__(self, type: _Optional[str] = ..., min_value: _Optional[int] = ..., max_value: _Optional[int] = ...) -> None: ...

class DistanceLimit(_message.Message):
    __slots__ = ("max_meters", "soft_max_meters", "cost_per_kilometer_below_soft_max", "cost_per_kilometer_above_soft_max")
    MAX_METERS_FIELD_NUMBER: _ClassVar[int]
    SOFT_MAX_METERS_FIELD_NUMBER: _ClassVar[int]
    COST_PER_KILOMETER_BELOW_SOFT_MAX_FIELD_NUMBER: _ClassVar[int]
    COST_PER_KILOMETER_ABOVE_SOFT_MAX_FIELD_NUMBER: _ClassVar[int]
    max_meters: int
    soft_max_meters: int
    cost_per_kilometer_below_soft_max: float
    cost_per_kilometer_above_soft_max: float
    def __init__(self, max_meters: _Optional[int] = ..., soft_max_meters: _Optional[int] = ..., cost_per_kilometer_below_soft_max: _Optional[float] = ..., cost_per_kilometer_above_soft_max: _Optional[float] = ...) -> None: ...

class TransitionAttributes(_message.Message):
    __slots__ = ("src_tag", "excluded_src_tag", "dst_tag", "excluded_dst_tag", "cost", "cost_per_kilometer", "distance_limit", "delay")
    SRC_TAG_FIELD_NUMBER: _ClassVar[int]
    EXCLUDED_SRC_TAG_FIELD_NUMBER: _ClassVar[int]
    DST_TAG_FIELD_NUMBER: _ClassVar[int]
    EXCLUDED_DST_TAG_FIELD_NUMBER: _ClassVar[int]
    COST_FIELD_NUMBER: _ClassVar[int]
    COST_PER_KILOMETER_FIELD_NUMBER: _ClassVar[int]
    DISTANCE_LIMIT_FIELD_NUMBER: _ClassVar[int]
    DELAY_FIELD_NUMBER: _ClassVar[int]
    src_tag: str
    excluded_src_tag: str
    dst_tag: str
    excluded_dst_tag: str
    cost: float
    cost_per_kilometer: float
    distance_limit: DistanceLimit
    delay: _duration_pb2.Duration
    def __init__(self, src_tag: _Optional[str] = ..., excluded_src_tag: _Optional[str] = ..., dst_tag: _Optional[str] = ..., excluded_dst_tag: _Optional[str] = ..., cost: _Optional[float] = ..., cost_per_kilometer: _Optional[float] = ..., distance_limit: _Optional[_Union[DistanceLimit, _Mapping]] = ..., delay: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...

class Waypoint(_message.Message):
    __slots__ = ("location", "place_id", "side_of_road")
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    PLACE_ID_FIELD_NUMBER: _ClassVar[int]
    SIDE_OF_ROAD_FIELD_NUMBER: _ClassVar[int]
    location: Location
    place_id: str
    side_of_road: bool
    def __init__(self, location: _Optional[_Union[Location, _Mapping]] = ..., place_id: _Optional[str] = ..., side_of_road: bool = ...) -> None: ...

class Location(_message.Message):
    __slots__ = ("lat_lng", "heading")
    LAT_LNG_FIELD_NUMBER: _ClassVar[int]
    HEADING_FIELD_NUMBER: _ClassVar[int]
    lat_lng: _latlng_pb2.LatLng
    heading: int
    def __init__(self, lat_lng: _Optional[_Union[_latlng_pb2.LatLng, _Mapping]] = ..., heading: _Optional[int] = ...) -> None: ...

class BreakRule(_message.Message):
    __slots__ = ("break_requests", "frequency_constraints")
    class BreakRequest(_message.Message):
        __slots__ = ("earliest_start_time", "latest_start_time", "min_duration")
        EARLIEST_START_TIME_FIELD_NUMBER: _ClassVar[int]
        LATEST_START_TIME_FIELD_NUMBER: _ClassVar[int]
        MIN_DURATION_FIELD_NUMBER: _ClassVar[int]
        earliest_start_time: _timestamp_pb2.Timestamp
        latest_start_time: _timestamp_pb2.Timestamp
        min_duration: _duration_pb2.Duration
        def __init__(self, earliest_start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., latest_start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., min_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...
    class FrequencyConstraint(_message.Message):
        __slots__ = ("min_break_duration", "max_inter_break_duration")
        MIN_BREAK_DURATION_FIELD_NUMBER: _ClassVar[int]
        MAX_INTER_BREAK_DURATION_FIELD_NUMBER: _ClassVar[int]
        min_break_duration: _duration_pb2.Duration
        max_inter_break_duration: _duration_pb2.Duration
        def __init__(self, min_break_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., max_inter_break_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...
    BREAK_REQUESTS_FIELD_NUMBER: _ClassVar[int]
    FREQUENCY_CONSTRAINTS_FIELD_NUMBER: _ClassVar[int]
    break_requests: _containers.RepeatedCompositeFieldContainer[BreakRule.BreakRequest]
    frequency_constraints: _containers.RepeatedCompositeFieldContainer[BreakRule.FrequencyConstraint]
    def __init__(self, break_requests: _Optional[_Iterable[_Union[BreakRule.BreakRequest, _Mapping]]] = ..., frequency_constraints: _Optional[_Iterable[_Union[BreakRule.FrequencyConstraint, _Mapping]]] = ...) -> None: ...

class ShipmentRoute(_message.Message):
    __slots__ = ("vehicle_index", "vehicle_label", "vehicle_start_time", "vehicle_end_time", "visits", "transitions", "has_traffic_infeasibilities", "route_polyline", "breaks", "metrics", "route_costs", "route_total_cost", "end_loads", "travel_steps", "vehicle_detour", "delay_before_vehicle_end")
    class Delay(_message.Message):
        __slots__ = ("start_time", "duration")
        START_TIME_FIELD_NUMBER: _ClassVar[int]
        DURATION_FIELD_NUMBER: _ClassVar[int]
        start_time: _timestamp_pb2.Timestamp
        duration: _duration_pb2.Duration
        def __init__(self, start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...
    class Visit(_message.Message):
        __slots__ = ("shipment_index", "is_pickup", "visit_request_index", "start_time", "load_demands", "detour", "shipment_label", "visit_label", "arrival_loads", "delay_before_start", "demands")
        class LoadDemandsEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: Shipment.Load
            def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Shipment.Load, _Mapping]] = ...) -> None: ...
        SHIPMENT_INDEX_FIELD_NUMBER: _ClassVar[int]
        IS_PICKUP_FIELD_NUMBER: _ClassVar[int]
        VISIT_REQUEST_INDEX_FIELD_NUMBER: _ClassVar[int]
        START_TIME_FIELD_NUMBER: _ClassVar[int]
        LOAD_DEMANDS_FIELD_NUMBER: _ClassVar[int]
        DETOUR_FIELD_NUMBER: _ClassVar[int]
        SHIPMENT_LABEL_FIELD_NUMBER: _ClassVar[int]
        VISIT_LABEL_FIELD_NUMBER: _ClassVar[int]
        ARRIVAL_LOADS_FIELD_NUMBER: _ClassVar[int]
        DELAY_BEFORE_START_FIELD_NUMBER: _ClassVar[int]
        DEMANDS_FIELD_NUMBER: _ClassVar[int]
        shipment_index: int
        is_pickup: bool
        visit_request_index: int
        start_time: _timestamp_pb2.Timestamp
        load_demands: _containers.MessageMap[str, Shipment.Load]
        detour: _duration_pb2.Duration
        shipment_label: str
        visit_label: str
        arrival_loads: _containers.RepeatedCompositeFieldContainer[CapacityQuantity]
        delay_before_start: ShipmentRoute.Delay
        demands: _containers.RepeatedCompositeFieldContainer[CapacityQuantity]
        def __init__(self, shipment_index: _Optional[int] = ..., is_pickup: bool = ..., visit_request_index: _Optional[int] = ..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., load_demands: _Optional[_Mapping[str, Shipment.Load]] = ..., detour: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., shipment_label: _Optional[str] = ..., visit_label: _Optional[str] = ..., arrival_loads: _Optional[_Iterable[_Union[CapacityQuantity, _Mapping]]] = ..., delay_before_start: _Optional[_Union[ShipmentRoute.Delay, _Mapping]] = ..., demands: _Optional[_Iterable[_Union[CapacityQuantity, _Mapping]]] = ...) -> None: ...
    class Transition(_message.Message):
        __slots__ = ("travel_duration", "travel_distance_meters", "traffic_info_unavailable", "delay_duration", "break_duration", "wait_duration", "total_duration", "start_time", "route_polyline", "vehicle_loads", "loads")
        class VehicleLoadsEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: ShipmentRoute.VehicleLoad
            def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ShipmentRoute.VehicleLoad, _Mapping]] = ...) -> None: ...
        TRAVEL_DURATION_FIELD_NUMBER: _ClassVar[int]
        TRAVEL_DISTANCE_METERS_FIELD_NUMBER: _ClassVar[int]
        TRAFFIC_INFO_UNAVAILABLE_FIELD_NUMBER: _ClassVar[int]
        DELAY_DURATION_FIELD_NUMBER: _ClassVar[int]
        BREAK_DURATION_FIELD_NUMBER: _ClassVar[int]
        WAIT_DURATION_FIELD_NUMBER: _ClassVar[int]
        TOTAL_DURATION_FIELD_NUMBER: _ClassVar[int]
        START_TIME_FIELD_NUMBER: _ClassVar[int]
        ROUTE_POLYLINE_FIELD_NUMBER: _ClassVar[int]
        VEHICLE_LOADS_FIELD_NUMBER: _ClassVar[int]
        LOADS_FIELD_NUMBER: _ClassVar[int]
        travel_duration: _duration_pb2.Duration
        travel_distance_meters: float
        traffic_info_unavailable: bool
        delay_duration: _duration_pb2.Duration
        break_duration: _duration_pb2.Duration
        wait_duration: _duration_pb2.Duration
        total_duration: _duration_pb2.Duration
        start_time: _timestamp_pb2.Timestamp
        route_polyline: ShipmentRoute.EncodedPolyline
        vehicle_loads: _containers.MessageMap[str, ShipmentRoute.VehicleLoad]
        loads: _containers.RepeatedCompositeFieldContainer[CapacityQuantity]
        def __init__(self, travel_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., travel_distance_meters: _Optional[float] = ..., traffic_info_unavailable: bool = ..., delay_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., break_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., wait_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., total_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., route_polyline: _Optional[_Union[ShipmentRoute.EncodedPolyline, _Mapping]] = ..., vehicle_loads: _Optional[_Mapping[str, ShipmentRoute.VehicleLoad]] = ..., loads: _Optional[_Iterable[_Union[CapacityQuantity, _Mapping]]] = ...) -> None: ...
    class VehicleLoad(_message.Message):
        __slots__ = ("amount",)
        AMOUNT_FIELD_NUMBER: _ClassVar[int]
        amount: int
        def __init__(self, amount: _Optional[int] = ...) -> None: ...
    class EncodedPolyline(_message.Message):
        __slots__ = ("points",)
        POINTS_FIELD_NUMBER: _ClassVar[int]
        points: str
        def __init__(self, points: _Optional[str] = ...) -> None: ...
    class Break(_message.Message):
        __slots__ = ("start_time", "duration")
        START_TIME_FIELD_NUMBER: _ClassVar[int]
        DURATION_FIELD_NUMBER: _ClassVar[int]
        start_time: _timestamp_pb2.Timestamp
        duration: _duration_pb2.Duration
        def __init__(self, start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...
    class TravelStep(_message.Message):
        __slots__ = ("duration", "distance_meters", "traffic_info_unavailable", "route_polyline")
        DURATION_FIELD_NUMBER: _ClassVar[int]
        DISTANCE_METERS_FIELD_NUMBER: _ClassVar[int]
        TRAFFIC_INFO_UNAVAILABLE_FIELD_NUMBER: _ClassVar[int]
        ROUTE_POLYLINE_FIELD_NUMBER: _ClassVar[int]
        duration: _duration_pb2.Duration
        distance_meters: float
        traffic_info_unavailable: bool
        route_polyline: ShipmentRoute.EncodedPolyline
        def __init__(self, duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., distance_meters: _Optional[float] = ..., traffic_info_unavailable: bool = ..., route_polyline: _Optional[_Union[ShipmentRoute.EncodedPolyline, _Mapping]] = ...) -> None: ...
    class RouteCostsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: float
        def __init__(self, key: _Optional[str] = ..., value: _Optional[float] = ...) -> None: ...
    VEHICLE_INDEX_FIELD_NUMBER: _ClassVar[int]
    VEHICLE_LABEL_FIELD_NUMBER: _ClassVar[int]
    VEHICLE_START_TIME_FIELD_NUMBER: _ClassVar[int]
    VEHICLE_END_TIME_FIELD_NUMBER: _ClassVar[int]
    VISITS_FIELD_NUMBER: _ClassVar[int]
    TRANSITIONS_FIELD_NUMBER: _ClassVar[int]
    HAS_TRAFFIC_INFEASIBILITIES_FIELD_NUMBER: _ClassVar[int]
    ROUTE_POLYLINE_FIELD_NUMBER: _ClassVar[int]
    BREAKS_FIELD_NUMBER: _ClassVar[int]
    METRICS_FIELD_NUMBER: _ClassVar[int]
    ROUTE_COSTS_FIELD_NUMBER: _ClassVar[int]
    ROUTE_TOTAL_COST_FIELD_NUMBER: _ClassVar[int]
    END_LOADS_FIELD_NUMBER: _ClassVar[int]
    TRAVEL_STEPS_FIELD_NUMBER: _ClassVar[int]
    VEHICLE_DETOUR_FIELD_NUMBER: _ClassVar[int]
    DELAY_BEFORE_VEHICLE_END_FIELD_NUMBER: _ClassVar[int]
    vehicle_index: int
    vehicle_label: str
    vehicle_start_time: _timestamp_pb2.Timestamp
    vehicle_end_time: _timestamp_pb2.Timestamp
    visits: _containers.RepeatedCompositeFieldContainer[ShipmentRoute.Visit]
    transitions: _containers.RepeatedCompositeFieldContainer[ShipmentRoute.Transition]
    has_traffic_infeasibilities: bool
    route_polyline: ShipmentRoute.EncodedPolyline
    breaks: _containers.RepeatedCompositeFieldContainer[ShipmentRoute.Break]
    metrics: AggregatedMetrics
    route_costs: _containers.ScalarMap[str, float]
    route_total_cost: float
    end_loads: _containers.RepeatedCompositeFieldContainer[CapacityQuantity]
    travel_steps: _containers.RepeatedCompositeFieldContainer[ShipmentRoute.TravelStep]
    vehicle_detour: _duration_pb2.Duration
    delay_before_vehicle_end: ShipmentRoute.Delay
    def __init__(self, vehicle_index: _Optional[int] = ..., vehicle_label: _Optional[str] = ..., vehicle_start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., vehicle_end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., visits: _Optional[_Iterable[_Union[ShipmentRoute.Visit, _Mapping]]] = ..., transitions: _Optional[_Iterable[_Union[ShipmentRoute.Transition, _Mapping]]] = ..., has_traffic_infeasibilities: bool = ..., route_polyline: _Optional[_Union[ShipmentRoute.EncodedPolyline, _Mapping]] = ..., breaks: _Optional[_Iterable[_Union[ShipmentRoute.Break, _Mapping]]] = ..., metrics: _Optional[_Union[AggregatedMetrics, _Mapping]] = ..., route_costs: _Optional[_Mapping[str, float]] = ..., route_total_cost: _Optional[float] = ..., end_loads: _Optional[_Iterable[_Union[CapacityQuantity, _Mapping]]] = ..., travel_steps: _Optional[_Iterable[_Union[ShipmentRoute.TravelStep, _Mapping]]] = ..., vehicle_detour: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., delay_before_vehicle_end: _Optional[_Union[ShipmentRoute.Delay, _Mapping]] = ...) -> None: ...

class SkippedShipment(_message.Message):
    __slots__ = ("index", "label", "reasons")
    class Reason(_message.Message):
        __slots__ = ("code", "example_vehicle_index", "example_exceeded_capacity_type")
        class Code(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            CODE_UNSPECIFIED: _ClassVar[SkippedShipment.Reason.Code]
            NO_VEHICLE: _ClassVar[SkippedShipment.Reason.Code]
            DEMAND_EXCEEDS_VEHICLE_CAPACITY: _ClassVar[SkippedShipment.Reason.Code]
            CANNOT_BE_PERFORMED_WITHIN_VEHICLE_DISTANCE_LIMIT: _ClassVar[SkippedShipment.Reason.Code]
            CANNOT_BE_PERFORMED_WITHIN_VEHICLE_DURATION_LIMIT: _ClassVar[SkippedShipment.Reason.Code]
            CANNOT_BE_PERFORMED_WITHIN_VEHICLE_TRAVEL_DURATION_LIMIT: _ClassVar[SkippedShipment.Reason.Code]
            CANNOT_BE_PERFORMED_WITHIN_VEHICLE_TIME_WINDOWS: _ClassVar[SkippedShipment.Reason.Code]
            VEHICLE_NOT_ALLOWED: _ClassVar[SkippedShipment.Reason.Code]
        CODE_UNSPECIFIED: SkippedShipment.Reason.Code
        NO_VEHICLE: SkippedShipment.Reason.Code
        DEMAND_EXCEEDS_VEHICLE_CAPACITY: SkippedShipment.Reason.Code
        CANNOT_BE_PERFORMED_WITHIN_VEHICLE_DISTANCE_LIMIT: SkippedShipment.Reason.Code
        CANNOT_BE_PERFORMED_WITHIN_VEHICLE_DURATION_LIMIT: SkippedShipment.Reason.Code
        CANNOT_BE_PERFORMED_WITHIN_VEHICLE_TRAVEL_DURATION_LIMIT: SkippedShipment.Reason.Code
        CANNOT_BE_PERFORMED_WITHIN_VEHICLE_TIME_WINDOWS: SkippedShipment.Reason.Code
        VEHICLE_NOT_ALLOWED: SkippedShipment.Reason.Code
        CODE_FIELD_NUMBER: _ClassVar[int]
        EXAMPLE_VEHICLE_INDEX_FIELD_NUMBER: _ClassVar[int]
        EXAMPLE_EXCEEDED_CAPACITY_TYPE_FIELD_NUMBER: _ClassVar[int]
        code: SkippedShipment.Reason.Code
        example_vehicle_index: int
        example_exceeded_capacity_type: str
        def __init__(self, code: _Optional[_Union[SkippedShipment.Reason.Code, str]] = ..., example_vehicle_index: _Optional[int] = ..., example_exceeded_capacity_type: _Optional[str] = ...) -> None: ...
    INDEX_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    REASONS_FIELD_NUMBER: _ClassVar[int]
    index: int
    label: str
    reasons: _containers.RepeatedCompositeFieldContainer[SkippedShipment.Reason]
    def __init__(self, index: _Optional[int] = ..., label: _Optional[str] = ..., reasons: _Optional[_Iterable[_Union[SkippedShipment.Reason, _Mapping]]] = ...) -> None: ...

class AggregatedMetrics(_message.Message):
    __slots__ = ("performed_shipment_count", "travel_duration", "wait_duration", "delay_duration", "break_duration", "visit_duration", "total_duration", "travel_distance_meters", "max_loads", "costs", "total_cost")
    class MaxLoadsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ShipmentRoute.VehicleLoad
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ShipmentRoute.VehicleLoad, _Mapping]] = ...) -> None: ...
    class CostsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: float
        def __init__(self, key: _Optional[str] = ..., value: _Optional[float] = ...) -> None: ...
    PERFORMED_SHIPMENT_COUNT_FIELD_NUMBER: _ClassVar[int]
    TRAVEL_DURATION_FIELD_NUMBER: _ClassVar[int]
    WAIT_DURATION_FIELD_NUMBER: _ClassVar[int]
    DELAY_DURATION_FIELD_NUMBER: _ClassVar[int]
    BREAK_DURATION_FIELD_NUMBER: _ClassVar[int]
    VISIT_DURATION_FIELD_NUMBER: _ClassVar[int]
    TOTAL_DURATION_FIELD_NUMBER: _ClassVar[int]
    TRAVEL_DISTANCE_METERS_FIELD_NUMBER: _ClassVar[int]
    MAX_LOADS_FIELD_NUMBER: _ClassVar[int]
    COSTS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COST_FIELD_NUMBER: _ClassVar[int]
    performed_shipment_count: int
    travel_duration: _duration_pb2.Duration
    wait_duration: _duration_pb2.Duration
    delay_duration: _duration_pb2.Duration
    break_duration: _duration_pb2.Duration
    visit_duration: _duration_pb2.Duration
    total_duration: _duration_pb2.Duration
    travel_distance_meters: float
    max_loads: _containers.MessageMap[str, ShipmentRoute.VehicleLoad]
    costs: _containers.ScalarMap[str, float]
    total_cost: float
    def __init__(self, performed_shipment_count: _Optional[int] = ..., travel_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., wait_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., delay_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., break_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., visit_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., total_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., travel_distance_meters: _Optional[float] = ..., max_loads: _Optional[_Mapping[str, ShipmentRoute.VehicleLoad]] = ..., costs: _Optional[_Mapping[str, float]] = ..., total_cost: _Optional[float] = ...) -> None: ...

class InjectedSolutionConstraint(_message.Message):
    __slots__ = ("routes", "skipped_shipments", "constraint_relaxations")
    class ConstraintRelaxation(_message.Message):
        __slots__ = ("relaxations", "vehicle_indices")
        class Relaxation(_message.Message):
            __slots__ = ("level", "threshold_time", "threshold_visit_count")
            class Level(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                LEVEL_UNSPECIFIED: _ClassVar[InjectedSolutionConstraint.ConstraintRelaxation.Relaxation.Level]
                RELAX_VISIT_TIMES_AFTER_THRESHOLD: _ClassVar[InjectedSolutionConstraint.ConstraintRelaxation.Relaxation.Level]
                RELAX_VISIT_TIMES_AND_SEQUENCE_AFTER_THRESHOLD: _ClassVar[InjectedSolutionConstraint.ConstraintRelaxation.Relaxation.Level]
                RELAX_ALL_AFTER_THRESHOLD: _ClassVar[InjectedSolutionConstraint.ConstraintRelaxation.Relaxation.Level]
            LEVEL_UNSPECIFIED: InjectedSolutionConstraint.ConstraintRelaxation.Relaxation.Level
            RELAX_VISIT_TIMES_AFTER_THRESHOLD: InjectedSolutionConstraint.ConstraintRelaxation.Relaxation.Level
            RELAX_VISIT_TIMES_AND_SEQUENCE_AFTER_THRESHOLD: InjectedSolutionConstraint.ConstraintRelaxation.Relaxation.Level
            RELAX_ALL_AFTER_THRESHOLD: InjectedSolutionConstraint.ConstraintRelaxation.Relaxation.Level
            LEVEL_FIELD_NUMBER: _ClassVar[int]
            THRESHOLD_TIME_FIELD_NUMBER: _ClassVar[int]
            THRESHOLD_VISIT_COUNT_FIELD_NUMBER: _ClassVar[int]
            level: InjectedSolutionConstraint.ConstraintRelaxation.Relaxation.Level
            threshold_time: _timestamp_pb2.Timestamp
            threshold_visit_count: int
            def __init__(self, level: _Optional[_Union[InjectedSolutionConstraint.ConstraintRelaxation.Relaxation.Level, str]] = ..., threshold_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., threshold_visit_count: _Optional[int] = ...) -> None: ...
        RELAXATIONS_FIELD_NUMBER: _ClassVar[int]
        VEHICLE_INDICES_FIELD_NUMBER: _ClassVar[int]
        relaxations: _containers.RepeatedCompositeFieldContainer[InjectedSolutionConstraint.ConstraintRelaxation.Relaxation]
        vehicle_indices: _containers.RepeatedScalarFieldContainer[int]
        def __init__(self, relaxations: _Optional[_Iterable[_Union[InjectedSolutionConstraint.ConstraintRelaxation.Relaxation, _Mapping]]] = ..., vehicle_indices: _Optional[_Iterable[int]] = ...) -> None: ...
    ROUTES_FIELD_NUMBER: _ClassVar[int]
    SKIPPED_SHIPMENTS_FIELD_NUMBER: _ClassVar[int]
    CONSTRAINT_RELAXATIONS_FIELD_NUMBER: _ClassVar[int]
    routes: _containers.RepeatedCompositeFieldContainer[ShipmentRoute]
    skipped_shipments: _containers.RepeatedCompositeFieldContainer[SkippedShipment]
    constraint_relaxations: _containers.RepeatedCompositeFieldContainer[InjectedSolutionConstraint.ConstraintRelaxation]
    def __init__(self, routes: _Optional[_Iterable[_Union[ShipmentRoute, _Mapping]]] = ..., skipped_shipments: _Optional[_Iterable[_Union[SkippedShipment, _Mapping]]] = ..., constraint_relaxations: _Optional[_Iterable[_Union[InjectedSolutionConstraint.ConstraintRelaxation, _Mapping]]] = ...) -> None: ...

class OptimizeToursValidationError(_message.Message):
    __slots__ = ("code", "display_name", "fields", "error_message", "offending_values")
    class FieldReference(_message.Message):
        __slots__ = ("name", "index", "key", "sub_field")
        NAME_FIELD_NUMBER: _ClassVar[int]
        INDEX_FIELD_NUMBER: _ClassVar[int]
        KEY_FIELD_NUMBER: _ClassVar[int]
        SUB_FIELD_FIELD_NUMBER: _ClassVar[int]
        name: str
        index: int
        key: str
        sub_field: OptimizeToursValidationError.FieldReference
        def __init__(self, name: _Optional[str] = ..., index: _Optional[int] = ..., key: _Optional[str] = ..., sub_field: _Optional[_Union[OptimizeToursValidationError.FieldReference, _Mapping]] = ...) -> None: ...
    CODE_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    OFFENDING_VALUES_FIELD_NUMBER: _ClassVar[int]
    code: int
    display_name: str
    fields: _containers.RepeatedCompositeFieldContainer[OptimizeToursValidationError.FieldReference]
    error_message: str
    offending_values: str
    def __init__(self, code: _Optional[int] = ..., display_name: _Optional[str] = ..., fields: _Optional[_Iterable[_Union[OptimizeToursValidationError.FieldReference, _Mapping]]] = ..., error_message: _Optional[str] = ..., offending_values: _Optional[str] = ...) -> None: ...
