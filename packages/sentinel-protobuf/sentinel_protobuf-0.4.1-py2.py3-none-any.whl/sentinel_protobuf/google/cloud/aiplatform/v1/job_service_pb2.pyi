from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.aiplatform.v1 import batch_prediction_job_pb2 as _batch_prediction_job_pb2
from google.cloud.aiplatform.v1 import custom_job_pb2 as _custom_job_pb2
from google.cloud.aiplatform.v1 import data_labeling_job_pb2 as _data_labeling_job_pb2
from google.cloud.aiplatform.v1 import hyperparameter_tuning_job_pb2 as _hyperparameter_tuning_job_pb2
from google.cloud.aiplatform.v1 import model_deployment_monitoring_job_pb2 as _model_deployment_monitoring_job_pb2
from google.cloud.aiplatform.v1 import nas_job_pb2 as _nas_job_pb2
from google.cloud.aiplatform.v1 import operation_pb2 as _operation_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateCustomJobRequest(_message.Message):
    __slots__ = ("parent", "custom_job")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_JOB_FIELD_NUMBER: _ClassVar[int]
    parent: str
    custom_job: _custom_job_pb2.CustomJob
    def __init__(self, parent: _Optional[str] = ..., custom_job: _Optional[_Union[_custom_job_pb2.CustomJob, _Mapping]] = ...) -> None: ...

class GetCustomJobRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListCustomJobsRequest(_message.Message):
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

class ListCustomJobsResponse(_message.Message):
    __slots__ = ("custom_jobs", "next_page_token")
    CUSTOM_JOBS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    custom_jobs: _containers.RepeatedCompositeFieldContainer[_custom_job_pb2.CustomJob]
    next_page_token: str
    def __init__(self, custom_jobs: _Optional[_Iterable[_Union[_custom_job_pb2.CustomJob, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class DeleteCustomJobRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CancelCustomJobRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CreateDataLabelingJobRequest(_message.Message):
    __slots__ = ("parent", "data_labeling_job")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    DATA_LABELING_JOB_FIELD_NUMBER: _ClassVar[int]
    parent: str
    data_labeling_job: _data_labeling_job_pb2.DataLabelingJob
    def __init__(self, parent: _Optional[str] = ..., data_labeling_job: _Optional[_Union[_data_labeling_job_pb2.DataLabelingJob, _Mapping]] = ...) -> None: ...

class GetDataLabelingJobRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListDataLabelingJobsRequest(_message.Message):
    __slots__ = ("parent", "filter", "page_size", "page_token", "read_mask", "order_by")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    READ_MASK_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    page_size: int
    page_token: str
    read_mask: _field_mask_pb2.FieldMask
    order_by: str
    def __init__(self, parent: _Optional[str] = ..., filter: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., read_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., order_by: _Optional[str] = ...) -> None: ...

class ListDataLabelingJobsResponse(_message.Message):
    __slots__ = ("data_labeling_jobs", "next_page_token")
    DATA_LABELING_JOBS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    data_labeling_jobs: _containers.RepeatedCompositeFieldContainer[_data_labeling_job_pb2.DataLabelingJob]
    next_page_token: str
    def __init__(self, data_labeling_jobs: _Optional[_Iterable[_Union[_data_labeling_job_pb2.DataLabelingJob, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class DeleteDataLabelingJobRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CancelDataLabelingJobRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CreateHyperparameterTuningJobRequest(_message.Message):
    __slots__ = ("parent", "hyperparameter_tuning_job")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    HYPERPARAMETER_TUNING_JOB_FIELD_NUMBER: _ClassVar[int]
    parent: str
    hyperparameter_tuning_job: _hyperparameter_tuning_job_pb2.HyperparameterTuningJob
    def __init__(self, parent: _Optional[str] = ..., hyperparameter_tuning_job: _Optional[_Union[_hyperparameter_tuning_job_pb2.HyperparameterTuningJob, _Mapping]] = ...) -> None: ...

class GetHyperparameterTuningJobRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListHyperparameterTuningJobsRequest(_message.Message):
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

class ListHyperparameterTuningJobsResponse(_message.Message):
    __slots__ = ("hyperparameter_tuning_jobs", "next_page_token")
    HYPERPARAMETER_TUNING_JOBS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    hyperparameter_tuning_jobs: _containers.RepeatedCompositeFieldContainer[_hyperparameter_tuning_job_pb2.HyperparameterTuningJob]
    next_page_token: str
    def __init__(self, hyperparameter_tuning_jobs: _Optional[_Iterable[_Union[_hyperparameter_tuning_job_pb2.HyperparameterTuningJob, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class DeleteHyperparameterTuningJobRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CancelHyperparameterTuningJobRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CreateNasJobRequest(_message.Message):
    __slots__ = ("parent", "nas_job")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NAS_JOB_FIELD_NUMBER: _ClassVar[int]
    parent: str
    nas_job: _nas_job_pb2.NasJob
    def __init__(self, parent: _Optional[str] = ..., nas_job: _Optional[_Union[_nas_job_pb2.NasJob, _Mapping]] = ...) -> None: ...

class GetNasJobRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListNasJobsRequest(_message.Message):
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

class ListNasJobsResponse(_message.Message):
    __slots__ = ("nas_jobs", "next_page_token")
    NAS_JOBS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    nas_jobs: _containers.RepeatedCompositeFieldContainer[_nas_job_pb2.NasJob]
    next_page_token: str
    def __init__(self, nas_jobs: _Optional[_Iterable[_Union[_nas_job_pb2.NasJob, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class DeleteNasJobRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CancelNasJobRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class GetNasTrialDetailRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListNasTrialDetailsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListNasTrialDetailsResponse(_message.Message):
    __slots__ = ("nas_trial_details", "next_page_token")
    NAS_TRIAL_DETAILS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    nas_trial_details: _containers.RepeatedCompositeFieldContainer[_nas_job_pb2.NasTrialDetail]
    next_page_token: str
    def __init__(self, nas_trial_details: _Optional[_Iterable[_Union[_nas_job_pb2.NasTrialDetail, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class CreateBatchPredictionJobRequest(_message.Message):
    __slots__ = ("parent", "batch_prediction_job")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    BATCH_PREDICTION_JOB_FIELD_NUMBER: _ClassVar[int]
    parent: str
    batch_prediction_job: _batch_prediction_job_pb2.BatchPredictionJob
    def __init__(self, parent: _Optional[str] = ..., batch_prediction_job: _Optional[_Union[_batch_prediction_job_pb2.BatchPredictionJob, _Mapping]] = ...) -> None: ...

class GetBatchPredictionJobRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListBatchPredictionJobsRequest(_message.Message):
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

class ListBatchPredictionJobsResponse(_message.Message):
    __slots__ = ("batch_prediction_jobs", "next_page_token")
    BATCH_PREDICTION_JOBS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    batch_prediction_jobs: _containers.RepeatedCompositeFieldContainer[_batch_prediction_job_pb2.BatchPredictionJob]
    next_page_token: str
    def __init__(self, batch_prediction_jobs: _Optional[_Iterable[_Union[_batch_prediction_job_pb2.BatchPredictionJob, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class DeleteBatchPredictionJobRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CancelBatchPredictionJobRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CreateModelDeploymentMonitoringJobRequest(_message.Message):
    __slots__ = ("parent", "model_deployment_monitoring_job")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    MODEL_DEPLOYMENT_MONITORING_JOB_FIELD_NUMBER: _ClassVar[int]
    parent: str
    model_deployment_monitoring_job: _model_deployment_monitoring_job_pb2.ModelDeploymentMonitoringJob
    def __init__(self, parent: _Optional[str] = ..., model_deployment_monitoring_job: _Optional[_Union[_model_deployment_monitoring_job_pb2.ModelDeploymentMonitoringJob, _Mapping]] = ...) -> None: ...

class SearchModelDeploymentMonitoringStatsAnomaliesRequest(_message.Message):
    __slots__ = ("model_deployment_monitoring_job", "deployed_model_id", "feature_display_name", "objectives", "page_size", "page_token", "start_time", "end_time")
    class StatsAnomaliesObjective(_message.Message):
        __slots__ = ("type", "top_feature_count")
        TYPE_FIELD_NUMBER: _ClassVar[int]
        TOP_FEATURE_COUNT_FIELD_NUMBER: _ClassVar[int]
        type: _model_deployment_monitoring_job_pb2.ModelDeploymentMonitoringObjectiveType
        top_feature_count: int
        def __init__(self, type: _Optional[_Union[_model_deployment_monitoring_job_pb2.ModelDeploymentMonitoringObjectiveType, str]] = ..., top_feature_count: _Optional[int] = ...) -> None: ...
    MODEL_DEPLOYMENT_MONITORING_JOB_FIELD_NUMBER: _ClassVar[int]
    DEPLOYED_MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    FEATURE_DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    OBJECTIVES_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    model_deployment_monitoring_job: str
    deployed_model_id: str
    feature_display_name: str
    objectives: _containers.RepeatedCompositeFieldContainer[SearchModelDeploymentMonitoringStatsAnomaliesRequest.StatsAnomaliesObjective]
    page_size: int
    page_token: str
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    def __init__(self, model_deployment_monitoring_job: _Optional[str] = ..., deployed_model_id: _Optional[str] = ..., feature_display_name: _Optional[str] = ..., objectives: _Optional[_Iterable[_Union[SearchModelDeploymentMonitoringStatsAnomaliesRequest.StatsAnomaliesObjective, _Mapping]]] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class SearchModelDeploymentMonitoringStatsAnomaliesResponse(_message.Message):
    __slots__ = ("monitoring_stats", "next_page_token")
    MONITORING_STATS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    monitoring_stats: _containers.RepeatedCompositeFieldContainer[_model_deployment_monitoring_job_pb2.ModelMonitoringStatsAnomalies]
    next_page_token: str
    def __init__(self, monitoring_stats: _Optional[_Iterable[_Union[_model_deployment_monitoring_job_pb2.ModelMonitoringStatsAnomalies, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class GetModelDeploymentMonitoringJobRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListModelDeploymentMonitoringJobsRequest(_message.Message):
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

class ListModelDeploymentMonitoringJobsResponse(_message.Message):
    __slots__ = ("model_deployment_monitoring_jobs", "next_page_token")
    MODEL_DEPLOYMENT_MONITORING_JOBS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    model_deployment_monitoring_jobs: _containers.RepeatedCompositeFieldContainer[_model_deployment_monitoring_job_pb2.ModelDeploymentMonitoringJob]
    next_page_token: str
    def __init__(self, model_deployment_monitoring_jobs: _Optional[_Iterable[_Union[_model_deployment_monitoring_job_pb2.ModelDeploymentMonitoringJob, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class UpdateModelDeploymentMonitoringJobRequest(_message.Message):
    __slots__ = ("model_deployment_monitoring_job", "update_mask")
    MODEL_DEPLOYMENT_MONITORING_JOB_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    model_deployment_monitoring_job: _model_deployment_monitoring_job_pb2.ModelDeploymentMonitoringJob
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, model_deployment_monitoring_job: _Optional[_Union[_model_deployment_monitoring_job_pb2.ModelDeploymentMonitoringJob, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeleteModelDeploymentMonitoringJobRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class PauseModelDeploymentMonitoringJobRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ResumeModelDeploymentMonitoringJobRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class UpdateModelDeploymentMonitoringJobOperationMetadata(_message.Message):
    __slots__ = ("generic_metadata",)
    GENERIC_METADATA_FIELD_NUMBER: _ClassVar[int]
    generic_metadata: _operation_pb2.GenericOperationMetadata
    def __init__(self, generic_metadata: _Optional[_Union[_operation_pb2.GenericOperationMetadata, _Mapping]] = ...) -> None: ...
