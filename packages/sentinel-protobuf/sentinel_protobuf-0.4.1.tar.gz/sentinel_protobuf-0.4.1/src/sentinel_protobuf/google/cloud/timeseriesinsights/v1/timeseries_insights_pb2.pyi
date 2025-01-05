from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BigqueryMapping(_message.Message):
    __slots__ = ("timestamp_column", "group_id_column", "dimension_column")
    TIMESTAMP_COLUMN_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_COLUMN_FIELD_NUMBER: _ClassVar[int]
    DIMENSION_COLUMN_FIELD_NUMBER: _ClassVar[int]
    timestamp_column: str
    group_id_column: str
    dimension_column: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, timestamp_column: _Optional[str] = ..., group_id_column: _Optional[str] = ..., dimension_column: _Optional[_Iterable[str]] = ...) -> None: ...

class DataSource(_message.Message):
    __slots__ = ("uri", "bq_mapping")
    URI_FIELD_NUMBER: _ClassVar[int]
    BQ_MAPPING_FIELD_NUMBER: _ClassVar[int]
    uri: str
    bq_mapping: BigqueryMapping
    def __init__(self, uri: _Optional[str] = ..., bq_mapping: _Optional[_Union[BigqueryMapping, _Mapping]] = ...) -> None: ...

class DataSet(_message.Message):
    __slots__ = ("name", "data_names", "data_sources", "state", "status", "ttl")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[DataSet.State]
        UNKNOWN: _ClassVar[DataSet.State]
        PENDING: _ClassVar[DataSet.State]
        LOADING: _ClassVar[DataSet.State]
        LOADED: _ClassVar[DataSet.State]
        UNLOADING: _ClassVar[DataSet.State]
        UNLOADED: _ClassVar[DataSet.State]
        FAILED: _ClassVar[DataSet.State]
    STATE_UNSPECIFIED: DataSet.State
    UNKNOWN: DataSet.State
    PENDING: DataSet.State
    LOADING: DataSet.State
    LOADED: DataSet.State
    UNLOADING: DataSet.State
    UNLOADED: DataSet.State
    FAILED: DataSet.State
    NAME_FIELD_NUMBER: _ClassVar[int]
    DATA_NAMES_FIELD_NUMBER: _ClassVar[int]
    DATA_SOURCES_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TTL_FIELD_NUMBER: _ClassVar[int]
    name: str
    data_names: _containers.RepeatedScalarFieldContainer[str]
    data_sources: _containers.RepeatedCompositeFieldContainer[DataSource]
    state: DataSet.State
    status: _status_pb2.Status
    ttl: _duration_pb2.Duration
    def __init__(self, name: _Optional[str] = ..., data_names: _Optional[_Iterable[str]] = ..., data_sources: _Optional[_Iterable[_Union[DataSource, _Mapping]]] = ..., state: _Optional[_Union[DataSet.State, str]] = ..., status: _Optional[_Union[_status_pb2.Status, _Mapping]] = ..., ttl: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...

class EventDimension(_message.Message):
    __slots__ = ("name", "string_val", "long_val", "bool_val", "double_val")
    NAME_FIELD_NUMBER: _ClassVar[int]
    STRING_VAL_FIELD_NUMBER: _ClassVar[int]
    LONG_VAL_FIELD_NUMBER: _ClassVar[int]
    BOOL_VAL_FIELD_NUMBER: _ClassVar[int]
    DOUBLE_VAL_FIELD_NUMBER: _ClassVar[int]
    name: str
    string_val: str
    long_val: int
    bool_val: bool
    double_val: float
    def __init__(self, name: _Optional[str] = ..., string_val: _Optional[str] = ..., long_val: _Optional[int] = ..., bool_val: bool = ..., double_val: _Optional[float] = ...) -> None: ...

class Event(_message.Message):
    __slots__ = ("dimensions", "group_id", "event_time")
    DIMENSIONS_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    EVENT_TIME_FIELD_NUMBER: _ClassVar[int]
    dimensions: _containers.RepeatedCompositeFieldContainer[EventDimension]
    group_id: int
    event_time: _timestamp_pb2.Timestamp
    def __init__(self, dimensions: _Optional[_Iterable[_Union[EventDimension, _Mapping]]] = ..., group_id: _Optional[int] = ..., event_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class AppendEventsRequest(_message.Message):
    __slots__ = ("events", "dataset")
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    DATASET_FIELD_NUMBER: _ClassVar[int]
    events: _containers.RepeatedCompositeFieldContainer[Event]
    dataset: str
    def __init__(self, events: _Optional[_Iterable[_Union[Event, _Mapping]]] = ..., dataset: _Optional[str] = ...) -> None: ...

class AppendEventsResponse(_message.Message):
    __slots__ = ("dropped_events",)
    DROPPED_EVENTS_FIELD_NUMBER: _ClassVar[int]
    dropped_events: _containers.RepeatedCompositeFieldContainer[Event]
    def __init__(self, dropped_events: _Optional[_Iterable[_Union[Event, _Mapping]]] = ...) -> None: ...

class CreateDataSetRequest(_message.Message):
    __slots__ = ("parent", "dataset")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    DATASET_FIELD_NUMBER: _ClassVar[int]
    parent: str
    dataset: DataSet
    def __init__(self, parent: _Optional[str] = ..., dataset: _Optional[_Union[DataSet, _Mapping]] = ...) -> None: ...

class DeleteDataSetRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListDataSetsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListDataSetsResponse(_message.Message):
    __slots__ = ("datasets", "next_page_token")
    DATASETS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    datasets: _containers.RepeatedCompositeFieldContainer[DataSet]
    next_page_token: str
    def __init__(self, datasets: _Optional[_Iterable[_Union[DataSet, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class PinnedDimension(_message.Message):
    __slots__ = ("name", "string_val", "bool_val")
    NAME_FIELD_NUMBER: _ClassVar[int]
    STRING_VAL_FIELD_NUMBER: _ClassVar[int]
    BOOL_VAL_FIELD_NUMBER: _ClassVar[int]
    name: str
    string_val: str
    bool_val: bool
    def __init__(self, name: _Optional[str] = ..., string_val: _Optional[str] = ..., bool_val: bool = ...) -> None: ...

class ForecastParams(_message.Message):
    __slots__ = ("noise_threshold", "seasonality_hint", "horizon_duration")
    class Period(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PERIOD_UNSPECIFIED: _ClassVar[ForecastParams.Period]
        HOURLY: _ClassVar[ForecastParams.Period]
        DAILY: _ClassVar[ForecastParams.Period]
        WEEKLY: _ClassVar[ForecastParams.Period]
        MONTHLY: _ClassVar[ForecastParams.Period]
        YEARLY: _ClassVar[ForecastParams.Period]
    PERIOD_UNSPECIFIED: ForecastParams.Period
    HOURLY: ForecastParams.Period
    DAILY: ForecastParams.Period
    WEEKLY: ForecastParams.Period
    MONTHLY: ForecastParams.Period
    YEARLY: ForecastParams.Period
    NOISE_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    SEASONALITY_HINT_FIELD_NUMBER: _ClassVar[int]
    HORIZON_DURATION_FIELD_NUMBER: _ClassVar[int]
    noise_threshold: float
    seasonality_hint: ForecastParams.Period
    horizon_duration: _duration_pb2.Duration
    def __init__(self, noise_threshold: _Optional[float] = ..., seasonality_hint: _Optional[_Union[ForecastParams.Period, str]] = ..., horizon_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...

class TimeseriesPoint(_message.Message):
    __slots__ = ("time", "value")
    TIME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    time: _timestamp_pb2.Timestamp
    value: float
    def __init__(self, time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., value: _Optional[float] = ...) -> None: ...

class Timeseries(_message.Message):
    __slots__ = ("point",)
    POINT_FIELD_NUMBER: _ClassVar[int]
    point: _containers.RepeatedCompositeFieldContainer[TimeseriesPoint]
    def __init__(self, point: _Optional[_Iterable[_Union[TimeseriesPoint, _Mapping]]] = ...) -> None: ...

class EvaluatedSlice(_message.Message):
    __slots__ = ("dimensions", "detection_point_actual", "detection_point_forecast", "expected_deviation", "anomaly_score", "history", "forecast", "status")
    DIMENSIONS_FIELD_NUMBER: _ClassVar[int]
    DETECTION_POINT_ACTUAL_FIELD_NUMBER: _ClassVar[int]
    DETECTION_POINT_FORECAST_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_DEVIATION_FIELD_NUMBER: _ClassVar[int]
    ANOMALY_SCORE_FIELD_NUMBER: _ClassVar[int]
    HISTORY_FIELD_NUMBER: _ClassVar[int]
    FORECAST_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    dimensions: _containers.RepeatedCompositeFieldContainer[PinnedDimension]
    detection_point_actual: float
    detection_point_forecast: float
    expected_deviation: float
    anomaly_score: float
    history: Timeseries
    forecast: Timeseries
    status: _status_pb2.Status
    def __init__(self, dimensions: _Optional[_Iterable[_Union[PinnedDimension, _Mapping]]] = ..., detection_point_actual: _Optional[float] = ..., detection_point_forecast: _Optional[float] = ..., expected_deviation: _Optional[float] = ..., anomaly_score: _Optional[float] = ..., history: _Optional[_Union[Timeseries, _Mapping]] = ..., forecast: _Optional[_Union[Timeseries, _Mapping]] = ..., status: _Optional[_Union[_status_pb2.Status, _Mapping]] = ...) -> None: ...

class SlicingParams(_message.Message):
    __slots__ = ("dimension_names", "pinned_dimensions")
    DIMENSION_NAMES_FIELD_NUMBER: _ClassVar[int]
    PINNED_DIMENSIONS_FIELD_NUMBER: _ClassVar[int]
    dimension_names: _containers.RepeatedScalarFieldContainer[str]
    pinned_dimensions: _containers.RepeatedCompositeFieldContainer[PinnedDimension]
    def __init__(self, dimension_names: _Optional[_Iterable[str]] = ..., pinned_dimensions: _Optional[_Iterable[_Union[PinnedDimension, _Mapping]]] = ...) -> None: ...

class TimeseriesParams(_message.Message):
    __slots__ = ("forecast_history", "granularity", "metric", "metric_aggregation_method")
    class AggregationMethod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        AGGREGATION_METHOD_UNSPECIFIED: _ClassVar[TimeseriesParams.AggregationMethod]
        SUM: _ClassVar[TimeseriesParams.AggregationMethod]
        AVERAGE: _ClassVar[TimeseriesParams.AggregationMethod]
    AGGREGATION_METHOD_UNSPECIFIED: TimeseriesParams.AggregationMethod
    SUM: TimeseriesParams.AggregationMethod
    AVERAGE: TimeseriesParams.AggregationMethod
    FORECAST_HISTORY_FIELD_NUMBER: _ClassVar[int]
    GRANULARITY_FIELD_NUMBER: _ClassVar[int]
    METRIC_FIELD_NUMBER: _ClassVar[int]
    METRIC_AGGREGATION_METHOD_FIELD_NUMBER: _ClassVar[int]
    forecast_history: _duration_pb2.Duration
    granularity: _duration_pb2.Duration
    metric: str
    metric_aggregation_method: TimeseriesParams.AggregationMethod
    def __init__(self, forecast_history: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., granularity: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., metric: _Optional[str] = ..., metric_aggregation_method: _Optional[_Union[TimeseriesParams.AggregationMethod, str]] = ...) -> None: ...

class QueryDataSetRequest(_message.Message):
    __slots__ = ("name", "detection_time", "num_returned_slices", "slicing_params", "timeseries_params", "forecast_params", "return_timeseries")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DETECTION_TIME_FIELD_NUMBER: _ClassVar[int]
    NUM_RETURNED_SLICES_FIELD_NUMBER: _ClassVar[int]
    SLICING_PARAMS_FIELD_NUMBER: _ClassVar[int]
    TIMESERIES_PARAMS_FIELD_NUMBER: _ClassVar[int]
    FORECAST_PARAMS_FIELD_NUMBER: _ClassVar[int]
    RETURN_TIMESERIES_FIELD_NUMBER: _ClassVar[int]
    name: str
    detection_time: _timestamp_pb2.Timestamp
    num_returned_slices: int
    slicing_params: SlicingParams
    timeseries_params: TimeseriesParams
    forecast_params: ForecastParams
    return_timeseries: bool
    def __init__(self, name: _Optional[str] = ..., detection_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., num_returned_slices: _Optional[int] = ..., slicing_params: _Optional[_Union[SlicingParams, _Mapping]] = ..., timeseries_params: _Optional[_Union[TimeseriesParams, _Mapping]] = ..., forecast_params: _Optional[_Union[ForecastParams, _Mapping]] = ..., return_timeseries: bool = ...) -> None: ...

class QueryDataSetResponse(_message.Message):
    __slots__ = ("name", "slices")
    NAME_FIELD_NUMBER: _ClassVar[int]
    SLICES_FIELD_NUMBER: _ClassVar[int]
    name: str
    slices: _containers.RepeatedCompositeFieldContainer[EvaluatedSlice]
    def __init__(self, name: _Optional[str] = ..., slices: _Optional[_Iterable[_Union[EvaluatedSlice, _Mapping]]] = ...) -> None: ...

class EvaluateSliceRequest(_message.Message):
    __slots__ = ("dataset", "pinned_dimensions", "detection_time", "timeseries_params", "forecast_params")
    DATASET_FIELD_NUMBER: _ClassVar[int]
    PINNED_DIMENSIONS_FIELD_NUMBER: _ClassVar[int]
    DETECTION_TIME_FIELD_NUMBER: _ClassVar[int]
    TIMESERIES_PARAMS_FIELD_NUMBER: _ClassVar[int]
    FORECAST_PARAMS_FIELD_NUMBER: _ClassVar[int]
    dataset: str
    pinned_dimensions: _containers.RepeatedCompositeFieldContainer[PinnedDimension]
    detection_time: _timestamp_pb2.Timestamp
    timeseries_params: TimeseriesParams
    forecast_params: ForecastParams
    def __init__(self, dataset: _Optional[str] = ..., pinned_dimensions: _Optional[_Iterable[_Union[PinnedDimension, _Mapping]]] = ..., detection_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., timeseries_params: _Optional[_Union[TimeseriesParams, _Mapping]] = ..., forecast_params: _Optional[_Union[ForecastParams, _Mapping]] = ...) -> None: ...

class EvaluateTimeseriesRequest(_message.Message):
    __slots__ = ("parent", "timeseries", "granularity", "forecast_params")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TIMESERIES_FIELD_NUMBER: _ClassVar[int]
    GRANULARITY_FIELD_NUMBER: _ClassVar[int]
    FORECAST_PARAMS_FIELD_NUMBER: _ClassVar[int]
    parent: str
    timeseries: Timeseries
    granularity: _duration_pb2.Duration
    forecast_params: ForecastParams
    def __init__(self, parent: _Optional[str] = ..., timeseries: _Optional[_Union[Timeseries, _Mapping]] = ..., granularity: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., forecast_params: _Optional[_Union[ForecastParams, _Mapping]] = ...) -> None: ...
