from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.type import calendar_period_pb2 as _calendar_period_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Service(_message.Message):
    __slots__ = ('name', 'display_name', 'custom', 'app_engine', 'cloud_endpoints', 'cluster_istio', 'mesh_istio', 'istio_canonical_service', 'cloud_run', 'gke_namespace', 'gke_workload', 'gke_service', 'basic_service', 'telemetry', 'user_labels')

    class Custom(_message.Message):
        __slots__ = ()

        def __init__(self) -> None:
            ...

    class AppEngine(_message.Message):
        __slots__ = ('module_id',)
        MODULE_ID_FIELD_NUMBER: _ClassVar[int]
        module_id: str

        def __init__(self, module_id: _Optional[str]=...) -> None:
            ...

    class CloudEndpoints(_message.Message):
        __slots__ = ('service',)
        SERVICE_FIELD_NUMBER: _ClassVar[int]
        service: str

        def __init__(self, service: _Optional[str]=...) -> None:
            ...

    class ClusterIstio(_message.Message):
        __slots__ = ('location', 'cluster_name', 'service_namespace', 'service_name')
        LOCATION_FIELD_NUMBER: _ClassVar[int]
        CLUSTER_NAME_FIELD_NUMBER: _ClassVar[int]
        SERVICE_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
        SERVICE_NAME_FIELD_NUMBER: _ClassVar[int]
        location: str
        cluster_name: str
        service_namespace: str
        service_name: str

        def __init__(self, location: _Optional[str]=..., cluster_name: _Optional[str]=..., service_namespace: _Optional[str]=..., service_name: _Optional[str]=...) -> None:
            ...

    class MeshIstio(_message.Message):
        __slots__ = ('mesh_uid', 'service_namespace', 'service_name')
        MESH_UID_FIELD_NUMBER: _ClassVar[int]
        SERVICE_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
        SERVICE_NAME_FIELD_NUMBER: _ClassVar[int]
        mesh_uid: str
        service_namespace: str
        service_name: str

        def __init__(self, mesh_uid: _Optional[str]=..., service_namespace: _Optional[str]=..., service_name: _Optional[str]=...) -> None:
            ...

    class IstioCanonicalService(_message.Message):
        __slots__ = ('mesh_uid', 'canonical_service_namespace', 'canonical_service')
        MESH_UID_FIELD_NUMBER: _ClassVar[int]
        CANONICAL_SERVICE_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
        CANONICAL_SERVICE_FIELD_NUMBER: _ClassVar[int]
        mesh_uid: str
        canonical_service_namespace: str
        canonical_service: str

        def __init__(self, mesh_uid: _Optional[str]=..., canonical_service_namespace: _Optional[str]=..., canonical_service: _Optional[str]=...) -> None:
            ...

    class CloudRun(_message.Message):
        __slots__ = ('service_name', 'location')
        SERVICE_NAME_FIELD_NUMBER: _ClassVar[int]
        LOCATION_FIELD_NUMBER: _ClassVar[int]
        service_name: str
        location: str

        def __init__(self, service_name: _Optional[str]=..., location: _Optional[str]=...) -> None:
            ...

    class GkeNamespace(_message.Message):
        __slots__ = ('project_id', 'location', 'cluster_name', 'namespace_name')
        PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
        LOCATION_FIELD_NUMBER: _ClassVar[int]
        CLUSTER_NAME_FIELD_NUMBER: _ClassVar[int]
        NAMESPACE_NAME_FIELD_NUMBER: _ClassVar[int]
        project_id: str
        location: str
        cluster_name: str
        namespace_name: str

        def __init__(self, project_id: _Optional[str]=..., location: _Optional[str]=..., cluster_name: _Optional[str]=..., namespace_name: _Optional[str]=...) -> None:
            ...

    class GkeWorkload(_message.Message):
        __slots__ = ('project_id', 'location', 'cluster_name', 'namespace_name', 'top_level_controller_type', 'top_level_controller_name')
        PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
        LOCATION_FIELD_NUMBER: _ClassVar[int]
        CLUSTER_NAME_FIELD_NUMBER: _ClassVar[int]
        NAMESPACE_NAME_FIELD_NUMBER: _ClassVar[int]
        TOP_LEVEL_CONTROLLER_TYPE_FIELD_NUMBER: _ClassVar[int]
        TOP_LEVEL_CONTROLLER_NAME_FIELD_NUMBER: _ClassVar[int]
        project_id: str
        location: str
        cluster_name: str
        namespace_name: str
        top_level_controller_type: str
        top_level_controller_name: str

        def __init__(self, project_id: _Optional[str]=..., location: _Optional[str]=..., cluster_name: _Optional[str]=..., namespace_name: _Optional[str]=..., top_level_controller_type: _Optional[str]=..., top_level_controller_name: _Optional[str]=...) -> None:
            ...

    class GkeService(_message.Message):
        __slots__ = ('project_id', 'location', 'cluster_name', 'namespace_name', 'service_name')
        PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
        LOCATION_FIELD_NUMBER: _ClassVar[int]
        CLUSTER_NAME_FIELD_NUMBER: _ClassVar[int]
        NAMESPACE_NAME_FIELD_NUMBER: _ClassVar[int]
        SERVICE_NAME_FIELD_NUMBER: _ClassVar[int]
        project_id: str
        location: str
        cluster_name: str
        namespace_name: str
        service_name: str

        def __init__(self, project_id: _Optional[str]=..., location: _Optional[str]=..., cluster_name: _Optional[str]=..., namespace_name: _Optional[str]=..., service_name: _Optional[str]=...) -> None:
            ...

    class BasicService(_message.Message):
        __slots__ = ('service_type', 'service_labels')

        class ServiceLabelsEntry(_message.Message):
            __slots__ = ('key', 'value')
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str

            def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
                ...
        SERVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
        SERVICE_LABELS_FIELD_NUMBER: _ClassVar[int]
        service_type: str
        service_labels: _containers.ScalarMap[str, str]

        def __init__(self, service_type: _Optional[str]=..., service_labels: _Optional[_Mapping[str, str]]=...) -> None:
            ...

    class Telemetry(_message.Message):
        __slots__ = ('resource_name',)
        RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
        resource_name: str

        def __init__(self, resource_name: _Optional[str]=...) -> None:
            ...

    class UserLabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELD_NUMBER: _ClassVar[int]
    APP_ENGINE_FIELD_NUMBER: _ClassVar[int]
    CLOUD_ENDPOINTS_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ISTIO_FIELD_NUMBER: _ClassVar[int]
    MESH_ISTIO_FIELD_NUMBER: _ClassVar[int]
    ISTIO_CANONICAL_SERVICE_FIELD_NUMBER: _ClassVar[int]
    CLOUD_RUN_FIELD_NUMBER: _ClassVar[int]
    GKE_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    GKE_WORKLOAD_FIELD_NUMBER: _ClassVar[int]
    GKE_SERVICE_FIELD_NUMBER: _ClassVar[int]
    BASIC_SERVICE_FIELD_NUMBER: _ClassVar[int]
    TELEMETRY_FIELD_NUMBER: _ClassVar[int]
    USER_LABELS_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    custom: Service.Custom
    app_engine: Service.AppEngine
    cloud_endpoints: Service.CloudEndpoints
    cluster_istio: Service.ClusterIstio
    mesh_istio: Service.MeshIstio
    istio_canonical_service: Service.IstioCanonicalService
    cloud_run: Service.CloudRun
    gke_namespace: Service.GkeNamespace
    gke_workload: Service.GkeWorkload
    gke_service: Service.GkeService
    basic_service: Service.BasicService
    telemetry: Service.Telemetry
    user_labels: _containers.ScalarMap[str, str]

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., custom: _Optional[_Union[Service.Custom, _Mapping]]=..., app_engine: _Optional[_Union[Service.AppEngine, _Mapping]]=..., cloud_endpoints: _Optional[_Union[Service.CloudEndpoints, _Mapping]]=..., cluster_istio: _Optional[_Union[Service.ClusterIstio, _Mapping]]=..., mesh_istio: _Optional[_Union[Service.MeshIstio, _Mapping]]=..., istio_canonical_service: _Optional[_Union[Service.IstioCanonicalService, _Mapping]]=..., cloud_run: _Optional[_Union[Service.CloudRun, _Mapping]]=..., gke_namespace: _Optional[_Union[Service.GkeNamespace, _Mapping]]=..., gke_workload: _Optional[_Union[Service.GkeWorkload, _Mapping]]=..., gke_service: _Optional[_Union[Service.GkeService, _Mapping]]=..., basic_service: _Optional[_Union[Service.BasicService, _Mapping]]=..., telemetry: _Optional[_Union[Service.Telemetry, _Mapping]]=..., user_labels: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class ServiceLevelObjective(_message.Message):
    __slots__ = ('name', 'display_name', 'service_level_indicator', 'goal', 'rolling_period', 'calendar_period', 'user_labels')

    class View(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        VIEW_UNSPECIFIED: _ClassVar[ServiceLevelObjective.View]
        FULL: _ClassVar[ServiceLevelObjective.View]
        EXPLICIT: _ClassVar[ServiceLevelObjective.View]
    VIEW_UNSPECIFIED: ServiceLevelObjective.View
    FULL: ServiceLevelObjective.View
    EXPLICIT: ServiceLevelObjective.View

    class UserLabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    SERVICE_LEVEL_INDICATOR_FIELD_NUMBER: _ClassVar[int]
    GOAL_FIELD_NUMBER: _ClassVar[int]
    ROLLING_PERIOD_FIELD_NUMBER: _ClassVar[int]
    CALENDAR_PERIOD_FIELD_NUMBER: _ClassVar[int]
    USER_LABELS_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    service_level_indicator: ServiceLevelIndicator
    goal: float
    rolling_period: _duration_pb2.Duration
    calendar_period: _calendar_period_pb2.CalendarPeriod
    user_labels: _containers.ScalarMap[str, str]

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., service_level_indicator: _Optional[_Union[ServiceLevelIndicator, _Mapping]]=..., goal: _Optional[float]=..., rolling_period: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., calendar_period: _Optional[_Union[_calendar_period_pb2.CalendarPeriod, str]]=..., user_labels: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class ServiceLevelIndicator(_message.Message):
    __slots__ = ('basic_sli', 'request_based', 'windows_based')
    BASIC_SLI_FIELD_NUMBER: _ClassVar[int]
    REQUEST_BASED_FIELD_NUMBER: _ClassVar[int]
    WINDOWS_BASED_FIELD_NUMBER: _ClassVar[int]
    basic_sli: BasicSli
    request_based: RequestBasedSli
    windows_based: WindowsBasedSli

    def __init__(self, basic_sli: _Optional[_Union[BasicSli, _Mapping]]=..., request_based: _Optional[_Union[RequestBasedSli, _Mapping]]=..., windows_based: _Optional[_Union[WindowsBasedSli, _Mapping]]=...) -> None:
        ...

class BasicSli(_message.Message):
    __slots__ = ('method', 'location', 'version', 'availability', 'latency')

    class AvailabilityCriteria(_message.Message):
        __slots__ = ()

        def __init__(self) -> None:
            ...

    class LatencyCriteria(_message.Message):
        __slots__ = ('threshold',)
        THRESHOLD_FIELD_NUMBER: _ClassVar[int]
        threshold: _duration_pb2.Duration

        def __init__(self, threshold: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=...) -> None:
            ...
    METHOD_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    LATENCY_FIELD_NUMBER: _ClassVar[int]
    method: _containers.RepeatedScalarFieldContainer[str]
    location: _containers.RepeatedScalarFieldContainer[str]
    version: _containers.RepeatedScalarFieldContainer[str]
    availability: BasicSli.AvailabilityCriteria
    latency: BasicSli.LatencyCriteria

    def __init__(self, method: _Optional[_Iterable[str]]=..., location: _Optional[_Iterable[str]]=..., version: _Optional[_Iterable[str]]=..., availability: _Optional[_Union[BasicSli.AvailabilityCriteria, _Mapping]]=..., latency: _Optional[_Union[BasicSli.LatencyCriteria, _Mapping]]=...) -> None:
        ...

class Range(_message.Message):
    __slots__ = ('min', 'max')
    MIN_FIELD_NUMBER: _ClassVar[int]
    MAX_FIELD_NUMBER: _ClassVar[int]
    min: float
    max: float

    def __init__(self, min: _Optional[float]=..., max: _Optional[float]=...) -> None:
        ...

class RequestBasedSli(_message.Message):
    __slots__ = ('good_total_ratio', 'distribution_cut')
    GOOD_TOTAL_RATIO_FIELD_NUMBER: _ClassVar[int]
    DISTRIBUTION_CUT_FIELD_NUMBER: _ClassVar[int]
    good_total_ratio: TimeSeriesRatio
    distribution_cut: DistributionCut

    def __init__(self, good_total_ratio: _Optional[_Union[TimeSeriesRatio, _Mapping]]=..., distribution_cut: _Optional[_Union[DistributionCut, _Mapping]]=...) -> None:
        ...

class TimeSeriesRatio(_message.Message):
    __slots__ = ('good_service_filter', 'bad_service_filter', 'total_service_filter')
    GOOD_SERVICE_FILTER_FIELD_NUMBER: _ClassVar[int]
    BAD_SERVICE_FILTER_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SERVICE_FILTER_FIELD_NUMBER: _ClassVar[int]
    good_service_filter: str
    bad_service_filter: str
    total_service_filter: str

    def __init__(self, good_service_filter: _Optional[str]=..., bad_service_filter: _Optional[str]=..., total_service_filter: _Optional[str]=...) -> None:
        ...

class DistributionCut(_message.Message):
    __slots__ = ('distribution_filter', 'range')
    DISTRIBUTION_FILTER_FIELD_NUMBER: _ClassVar[int]
    RANGE_FIELD_NUMBER: _ClassVar[int]
    distribution_filter: str
    range: Range

    def __init__(self, distribution_filter: _Optional[str]=..., range: _Optional[_Union[Range, _Mapping]]=...) -> None:
        ...

class WindowsBasedSli(_message.Message):
    __slots__ = ('good_bad_metric_filter', 'good_total_ratio_threshold', 'metric_mean_in_range', 'metric_sum_in_range', 'window_period')

    class PerformanceThreshold(_message.Message):
        __slots__ = ('performance', 'basic_sli_performance', 'threshold')
        PERFORMANCE_FIELD_NUMBER: _ClassVar[int]
        BASIC_SLI_PERFORMANCE_FIELD_NUMBER: _ClassVar[int]
        THRESHOLD_FIELD_NUMBER: _ClassVar[int]
        performance: RequestBasedSli
        basic_sli_performance: BasicSli
        threshold: float

        def __init__(self, performance: _Optional[_Union[RequestBasedSli, _Mapping]]=..., basic_sli_performance: _Optional[_Union[BasicSli, _Mapping]]=..., threshold: _Optional[float]=...) -> None:
            ...

    class MetricRange(_message.Message):
        __slots__ = ('time_series', 'range')
        TIME_SERIES_FIELD_NUMBER: _ClassVar[int]
        RANGE_FIELD_NUMBER: _ClassVar[int]
        time_series: str
        range: Range

        def __init__(self, time_series: _Optional[str]=..., range: _Optional[_Union[Range, _Mapping]]=...) -> None:
            ...
    GOOD_BAD_METRIC_FILTER_FIELD_NUMBER: _ClassVar[int]
    GOOD_TOTAL_RATIO_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    METRIC_MEAN_IN_RANGE_FIELD_NUMBER: _ClassVar[int]
    METRIC_SUM_IN_RANGE_FIELD_NUMBER: _ClassVar[int]
    WINDOW_PERIOD_FIELD_NUMBER: _ClassVar[int]
    good_bad_metric_filter: str
    good_total_ratio_threshold: WindowsBasedSli.PerformanceThreshold
    metric_mean_in_range: WindowsBasedSli.MetricRange
    metric_sum_in_range: WindowsBasedSli.MetricRange
    window_period: _duration_pb2.Duration

    def __init__(self, good_bad_metric_filter: _Optional[str]=..., good_total_ratio_threshold: _Optional[_Union[WindowsBasedSli.PerformanceThreshold, _Mapping]]=..., metric_mean_in_range: _Optional[_Union[WindowsBasedSli.MetricRange, _Mapping]]=..., metric_sum_in_range: _Optional[_Union[WindowsBasedSli.MetricRange, _Mapping]]=..., window_period: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=...) -> None:
        ...