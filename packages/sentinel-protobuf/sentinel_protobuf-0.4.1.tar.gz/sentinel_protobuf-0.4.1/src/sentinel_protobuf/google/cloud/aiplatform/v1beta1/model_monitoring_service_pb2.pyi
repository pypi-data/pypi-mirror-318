from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.aiplatform.v1beta1 import model_monitor_pb2 as _model_monitor_pb2
from google.cloud.aiplatform.v1beta1 import model_monitoring_alert_pb2 as _model_monitoring_alert_pb2
from google.cloud.aiplatform.v1beta1 import model_monitoring_job_pb2 as _model_monitoring_job_pb2
from google.cloud.aiplatform.v1beta1 import model_monitoring_stats_pb2 as _model_monitoring_stats_pb2
from google.cloud.aiplatform.v1beta1 import operation_pb2 as _operation_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.type import interval_pb2 as _interval_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateModelMonitorRequest(_message.Message):
    __slots__ = ("parent", "model_monitor", "model_monitor_id")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    MODEL_MONITOR_FIELD_NUMBER: _ClassVar[int]
    MODEL_MONITOR_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    model_monitor: _model_monitor_pb2.ModelMonitor
    model_monitor_id: str
    def __init__(self, parent: _Optional[str] = ..., model_monitor: _Optional[_Union[_model_monitor_pb2.ModelMonitor, _Mapping]] = ..., model_monitor_id: _Optional[str] = ...) -> None: ...

class CreateModelMonitorOperationMetadata(_message.Message):
    __slots__ = ("generic_metadata",)
    GENERIC_METADATA_FIELD_NUMBER: _ClassVar[int]
    generic_metadata: _operation_pb2.GenericOperationMetadata
    def __init__(self, generic_metadata: _Optional[_Union[_operation_pb2.GenericOperationMetadata, _Mapping]] = ...) -> None: ...

class UpdateModelMonitorRequest(_message.Message):
    __slots__ = ("model_monitor", "update_mask")
    MODEL_MONITOR_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    model_monitor: _model_monitor_pb2.ModelMonitor
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, model_monitor: _Optional[_Union[_model_monitor_pb2.ModelMonitor, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateModelMonitorOperationMetadata(_message.Message):
    __slots__ = ("generic_metadata",)
    GENERIC_METADATA_FIELD_NUMBER: _ClassVar[int]
    generic_metadata: _operation_pb2.GenericOperationMetadata
    def __init__(self, generic_metadata: _Optional[_Union[_operation_pb2.GenericOperationMetadata, _Mapping]] = ...) -> None: ...

class GetModelMonitorRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListModelMonitorsRequest(_message.Message):
    __slots__ = ("parent", "filter", "page_size", "page_token", "read_mask")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    READ_MASK_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    page_size: int
    page_token: str
    read_mask: _field_mask_pb2.FieldMask
    def __init__(self, parent: _Optional[str] = ..., filter: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., read_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class ListModelMonitorsResponse(_message.Message):
    __slots__ = ("model_monitors", "next_page_token")
    MODEL_MONITORS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    model_monitors: _containers.RepeatedCompositeFieldContainer[_model_monitor_pb2.ModelMonitor]
    next_page_token: str
    def __init__(self, model_monitors: _Optional[_Iterable[_Union[_model_monitor_pb2.ModelMonitor, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class DeleteModelMonitorRequest(_message.Message):
    __slots__ = ("name", "force")
    NAME_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    force: bool
    def __init__(self, name: _Optional[str] = ..., force: bool = ...) -> None: ...

class CreateModelMonitoringJobRequest(_message.Message):
    __slots__ = ("parent", "model_monitoring_job", "model_monitoring_job_id")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    MODEL_MONITORING_JOB_FIELD_NUMBER: _ClassVar[int]
    MODEL_MONITORING_JOB_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    model_monitoring_job: _model_monitoring_job_pb2.ModelMonitoringJob
    model_monitoring_job_id: str
    def __init__(self, parent: _Optional[str] = ..., model_monitoring_job: _Optional[_Union[_model_monitoring_job_pb2.ModelMonitoringJob, _Mapping]] = ..., model_monitoring_job_id: _Optional[str] = ...) -> None: ...

class GetModelMonitoringJobRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListModelMonitoringJobsRequest(_message.Message):
    __slots__ = ("parent", "filter", "page_size", "page_token", "read_mask")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    READ_MASK_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    page_size: int
    page_token: str
    read_mask: _field_mask_pb2.FieldMask
    def __init__(self, parent: _Optional[str] = ..., filter: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., read_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class ListModelMonitoringJobsResponse(_message.Message):
    __slots__ = ("model_monitoring_jobs", "next_page_token")
    MODEL_MONITORING_JOBS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    model_monitoring_jobs: _containers.RepeatedCompositeFieldContainer[_model_monitoring_job_pb2.ModelMonitoringJob]
    next_page_token: str
    def __init__(self, model_monitoring_jobs: _Optional[_Iterable[_Union[_model_monitoring_job_pb2.ModelMonitoringJob, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class DeleteModelMonitoringJobRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class SearchModelMonitoringStatsRequest(_message.Message):
    __slots__ = ("model_monitor", "stats_filter", "time_interval", "page_size", "page_token")
    MODEL_MONITOR_FIELD_NUMBER: _ClassVar[int]
    STATS_FILTER_FIELD_NUMBER: _ClassVar[int]
    TIME_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    model_monitor: str
    stats_filter: _model_monitoring_stats_pb2.SearchModelMonitoringStatsFilter
    time_interval: _interval_pb2.Interval
    page_size: int
    page_token: str
    def __init__(self, model_monitor: _Optional[str] = ..., stats_filter: _Optional[_Union[_model_monitoring_stats_pb2.SearchModelMonitoringStatsFilter, _Mapping]] = ..., time_interval: _Optional[_Union[_interval_pb2.Interval, _Mapping]] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class SearchModelMonitoringStatsResponse(_message.Message):
    __slots__ = ("monitoring_stats", "next_page_token")
    MONITORING_STATS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    monitoring_stats: _containers.RepeatedCompositeFieldContainer[_model_monitoring_stats_pb2.ModelMonitoringStats]
    next_page_token: str
    def __init__(self, monitoring_stats: _Optional[_Iterable[_Union[_model_monitoring_stats_pb2.ModelMonitoringStats, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class SearchModelMonitoringAlertsRequest(_message.Message):
    __slots__ = ("model_monitor", "model_monitoring_job", "alert_time_interval", "stats_name", "objective_type", "page_size", "page_token")
    MODEL_MONITOR_FIELD_NUMBER: _ClassVar[int]
    MODEL_MONITORING_JOB_FIELD_NUMBER: _ClassVar[int]
    ALERT_TIME_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    STATS_NAME_FIELD_NUMBER: _ClassVar[int]
    OBJECTIVE_TYPE_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    model_monitor: str
    model_monitoring_job: str
    alert_time_interval: _interval_pb2.Interval
    stats_name: str
    objective_type: str
    page_size: int
    page_token: str
    def __init__(self, model_monitor: _Optional[str] = ..., model_monitoring_job: _Optional[str] = ..., alert_time_interval: _Optional[_Union[_interval_pb2.Interval, _Mapping]] = ..., stats_name: _Optional[str] = ..., objective_type: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class SearchModelMonitoringAlertsResponse(_message.Message):
    __slots__ = ("model_monitoring_alerts", "total_number_alerts", "next_page_token")
    MODEL_MONITORING_ALERTS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_NUMBER_ALERTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    model_monitoring_alerts: _containers.RepeatedCompositeFieldContainer[_model_monitoring_alert_pb2.ModelMonitoringAlert]
    total_number_alerts: int
    next_page_token: str
    def __init__(self, model_monitoring_alerts: _Optional[_Iterable[_Union[_model_monitoring_alert_pb2.ModelMonitoringAlert, _Mapping]]] = ..., total_number_alerts: _Optional[int] = ..., next_page_token: _Optional[str] = ...) -> None: ...
