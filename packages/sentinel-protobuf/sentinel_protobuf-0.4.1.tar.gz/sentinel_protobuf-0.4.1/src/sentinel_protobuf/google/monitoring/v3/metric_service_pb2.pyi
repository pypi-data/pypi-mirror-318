from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import metric_pb2 as _metric_pb2
from google.api import monitored_resource_pb2 as _monitored_resource_pb2
from google.api import resource_pb2 as _resource_pb2
from google.monitoring.v3 import common_pb2 as _common_pb2
from google.monitoring.v3 import metric_pb2 as _metric_pb2_1
from google.protobuf import empty_pb2 as _empty_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ListMonitoredResourceDescriptorsRequest(_message.Message):
    __slots__ = ('name', 'filter', 'page_size', 'page_token')
    NAME_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    name: str
    filter: str
    page_size: int
    page_token: str

    def __init__(self, name: _Optional[str]=..., filter: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListMonitoredResourceDescriptorsResponse(_message.Message):
    __slots__ = ('resource_descriptors', 'next_page_token')
    RESOURCE_DESCRIPTORS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    resource_descriptors: _containers.RepeatedCompositeFieldContainer[_monitored_resource_pb2.MonitoredResourceDescriptor]
    next_page_token: str

    def __init__(self, resource_descriptors: _Optional[_Iterable[_Union[_monitored_resource_pb2.MonitoredResourceDescriptor, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetMonitoredResourceDescriptorRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListMetricDescriptorsRequest(_message.Message):
    __slots__ = ('name', 'filter', 'page_size', 'page_token')
    NAME_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    name: str
    filter: str
    page_size: int
    page_token: str

    def __init__(self, name: _Optional[str]=..., filter: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListMetricDescriptorsResponse(_message.Message):
    __slots__ = ('metric_descriptors', 'next_page_token')
    METRIC_DESCRIPTORS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    metric_descriptors: _containers.RepeatedCompositeFieldContainer[_metric_pb2.MetricDescriptor]
    next_page_token: str

    def __init__(self, metric_descriptors: _Optional[_Iterable[_Union[_metric_pb2.MetricDescriptor, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetMetricDescriptorRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateMetricDescriptorRequest(_message.Message):
    __slots__ = ('name', 'metric_descriptor')
    NAME_FIELD_NUMBER: _ClassVar[int]
    METRIC_DESCRIPTOR_FIELD_NUMBER: _ClassVar[int]
    name: str
    metric_descriptor: _metric_pb2.MetricDescriptor

    def __init__(self, name: _Optional[str]=..., metric_descriptor: _Optional[_Union[_metric_pb2.MetricDescriptor, _Mapping]]=...) -> None:
        ...

class DeleteMetricDescriptorRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListTimeSeriesRequest(_message.Message):
    __slots__ = ('name', 'filter', 'interval', 'aggregation', 'secondary_aggregation', 'order_by', 'view', 'page_size', 'page_token')

    class TimeSeriesView(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FULL: _ClassVar[ListTimeSeriesRequest.TimeSeriesView]
        HEADERS: _ClassVar[ListTimeSeriesRequest.TimeSeriesView]
    FULL: ListTimeSeriesRequest.TimeSeriesView
    HEADERS: ListTimeSeriesRequest.TimeSeriesView
    NAME_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    INTERVAL_FIELD_NUMBER: _ClassVar[int]
    AGGREGATION_FIELD_NUMBER: _ClassVar[int]
    SECONDARY_AGGREGATION_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    name: str
    filter: str
    interval: _common_pb2.TimeInterval
    aggregation: _common_pb2.Aggregation
    secondary_aggregation: _common_pb2.Aggregation
    order_by: str
    view: ListTimeSeriesRequest.TimeSeriesView
    page_size: int
    page_token: str

    def __init__(self, name: _Optional[str]=..., filter: _Optional[str]=..., interval: _Optional[_Union[_common_pb2.TimeInterval, _Mapping]]=..., aggregation: _Optional[_Union[_common_pb2.Aggregation, _Mapping]]=..., secondary_aggregation: _Optional[_Union[_common_pb2.Aggregation, _Mapping]]=..., order_by: _Optional[str]=..., view: _Optional[_Union[ListTimeSeriesRequest.TimeSeriesView, str]]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListTimeSeriesResponse(_message.Message):
    __slots__ = ('time_series', 'next_page_token', 'execution_errors', 'unit')
    TIME_SERIES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_ERRORS_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    time_series: _containers.RepeatedCompositeFieldContainer[_metric_pb2_1.TimeSeries]
    next_page_token: str
    execution_errors: _containers.RepeatedCompositeFieldContainer[_status_pb2.Status]
    unit: str

    def __init__(self, time_series: _Optional[_Iterable[_Union[_metric_pb2_1.TimeSeries, _Mapping]]]=..., next_page_token: _Optional[str]=..., execution_errors: _Optional[_Iterable[_Union[_status_pb2.Status, _Mapping]]]=..., unit: _Optional[str]=...) -> None:
        ...

class CreateTimeSeriesRequest(_message.Message):
    __slots__ = ('name', 'time_series')
    NAME_FIELD_NUMBER: _ClassVar[int]
    TIME_SERIES_FIELD_NUMBER: _ClassVar[int]
    name: str
    time_series: _containers.RepeatedCompositeFieldContainer[_metric_pb2_1.TimeSeries]

    def __init__(self, name: _Optional[str]=..., time_series: _Optional[_Iterable[_Union[_metric_pb2_1.TimeSeries, _Mapping]]]=...) -> None:
        ...

class CreateTimeSeriesError(_message.Message):
    __slots__ = ('time_series', 'status')
    TIME_SERIES_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    time_series: _metric_pb2_1.TimeSeries
    status: _status_pb2.Status

    def __init__(self, time_series: _Optional[_Union[_metric_pb2_1.TimeSeries, _Mapping]]=..., status: _Optional[_Union[_status_pb2.Status, _Mapping]]=...) -> None:
        ...

class CreateTimeSeriesSummary(_message.Message):
    __slots__ = ('total_point_count', 'success_point_count', 'errors')

    class Error(_message.Message):
        __slots__ = ('status', 'point_count')
        STATUS_FIELD_NUMBER: _ClassVar[int]
        POINT_COUNT_FIELD_NUMBER: _ClassVar[int]
        status: _status_pb2.Status
        point_count: int

        def __init__(self, status: _Optional[_Union[_status_pb2.Status, _Mapping]]=..., point_count: _Optional[int]=...) -> None:
            ...
    TOTAL_POINT_COUNT_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_POINT_COUNT_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    total_point_count: int
    success_point_count: int
    errors: _containers.RepeatedCompositeFieldContainer[CreateTimeSeriesSummary.Error]

    def __init__(self, total_point_count: _Optional[int]=..., success_point_count: _Optional[int]=..., errors: _Optional[_Iterable[_Union[CreateTimeSeriesSummary.Error, _Mapping]]]=...) -> None:
        ...

class QueryTimeSeriesRequest(_message.Message):
    __slots__ = ('name', 'query', 'page_size', 'page_token')
    NAME_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    name: str
    query: str
    page_size: int
    page_token: str

    def __init__(self, name: _Optional[str]=..., query: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class QueryTimeSeriesResponse(_message.Message):
    __slots__ = ('time_series_descriptor', 'time_series_data', 'next_page_token', 'partial_errors')
    TIME_SERIES_DESCRIPTOR_FIELD_NUMBER: _ClassVar[int]
    TIME_SERIES_DATA_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PARTIAL_ERRORS_FIELD_NUMBER: _ClassVar[int]
    time_series_descriptor: _metric_pb2_1.TimeSeriesDescriptor
    time_series_data: _containers.RepeatedCompositeFieldContainer[_metric_pb2_1.TimeSeriesData]
    next_page_token: str
    partial_errors: _containers.RepeatedCompositeFieldContainer[_status_pb2.Status]

    def __init__(self, time_series_descriptor: _Optional[_Union[_metric_pb2_1.TimeSeriesDescriptor, _Mapping]]=..., time_series_data: _Optional[_Iterable[_Union[_metric_pb2_1.TimeSeriesData, _Mapping]]]=..., next_page_token: _Optional[str]=..., partial_errors: _Optional[_Iterable[_Union[_status_pb2.Status, _Mapping]]]=...) -> None:
        ...

class QueryErrorList(_message.Message):
    __slots__ = ('errors', 'error_summary')
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    ERROR_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    errors: _containers.RepeatedCompositeFieldContainer[_metric_pb2_1.QueryError]
    error_summary: str

    def __init__(self, errors: _Optional[_Iterable[_Union[_metric_pb2_1.QueryError, _Mapping]]]=..., error_summary: _Optional[str]=...) -> None:
        ...