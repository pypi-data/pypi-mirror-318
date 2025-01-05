from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.aiplatform.v1beta1 import job_state_pb2 as _job_state_pb2
from google.cloud.aiplatform.v1beta1 import model_monitoring_spec_pb2 as _model_monitoring_spec_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.rpc import status_pb2 as _status_pb2
from google.type import interval_pb2 as _interval_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ModelMonitoringJob(_message.Message):
    __slots__ = ("name", "display_name", "model_monitoring_spec", "create_time", "update_time", "state", "schedule", "job_execution_detail", "schedule_time")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    MODEL_MONITORING_SPEC_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    JOB_EXECUTION_DETAIL_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    model_monitoring_spec: _model_monitoring_spec_pb2.ModelMonitoringSpec
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    state: _job_state_pb2.JobState
    schedule: str
    job_execution_detail: ModelMonitoringJobExecutionDetail
    schedule_time: _timestamp_pb2.Timestamp
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., model_monitoring_spec: _Optional[_Union[_model_monitoring_spec_pb2.ModelMonitoringSpec, _Mapping]] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., state: _Optional[_Union[_job_state_pb2.JobState, str]] = ..., schedule: _Optional[str] = ..., job_execution_detail: _Optional[_Union[ModelMonitoringJobExecutionDetail, _Mapping]] = ..., schedule_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ModelMonitoringJobExecutionDetail(_message.Message):
    __slots__ = ("baseline_datasets", "target_datasets", "objective_status", "error")
    class ProcessedDataset(_message.Message):
        __slots__ = ("location", "time_range")
        LOCATION_FIELD_NUMBER: _ClassVar[int]
        TIME_RANGE_FIELD_NUMBER: _ClassVar[int]
        location: str
        time_range: _interval_pb2.Interval
        def __init__(self, location: _Optional[str] = ..., time_range: _Optional[_Union[_interval_pb2.Interval, _Mapping]] = ...) -> None: ...
    class ObjectiveStatusEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _status_pb2.Status
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_status_pb2.Status, _Mapping]] = ...) -> None: ...
    BASELINE_DATASETS_FIELD_NUMBER: _ClassVar[int]
    TARGET_DATASETS_FIELD_NUMBER: _ClassVar[int]
    OBJECTIVE_STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    baseline_datasets: _containers.RepeatedCompositeFieldContainer[ModelMonitoringJobExecutionDetail.ProcessedDataset]
    target_datasets: _containers.RepeatedCompositeFieldContainer[ModelMonitoringJobExecutionDetail.ProcessedDataset]
    objective_status: _containers.MessageMap[str, _status_pb2.Status]
    error: _status_pb2.Status
    def __init__(self, baseline_datasets: _Optional[_Iterable[_Union[ModelMonitoringJobExecutionDetail.ProcessedDataset, _Mapping]]] = ..., target_datasets: _Optional[_Iterable[_Union[ModelMonitoringJobExecutionDetail.ProcessedDataset, _Mapping]]] = ..., objective_status: _Optional[_Mapping[str, _status_pb2.Status]] = ..., error: _Optional[_Union[_status_pb2.Status, _Mapping]] = ...) -> None: ...
