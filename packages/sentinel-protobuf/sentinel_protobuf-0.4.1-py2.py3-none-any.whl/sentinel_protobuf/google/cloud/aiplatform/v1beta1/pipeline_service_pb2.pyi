from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.aiplatform.v1beta1 import operation_pb2 as _operation_pb2
from google.cloud.aiplatform.v1beta1 import pipeline_job_pb2 as _pipeline_job_pb2
from google.cloud.aiplatform.v1beta1 import training_pipeline_pb2 as _training_pipeline_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BatchCancelPipelineJobsOperationMetadata(_message.Message):
    __slots__ = ("generic_metadata",)
    GENERIC_METADATA_FIELD_NUMBER: _ClassVar[int]
    generic_metadata: _operation_pb2.GenericOperationMetadata
    def __init__(self, generic_metadata: _Optional[_Union[_operation_pb2.GenericOperationMetadata, _Mapping]] = ...) -> None: ...

class CreateTrainingPipelineRequest(_message.Message):
    __slots__ = ("parent", "training_pipeline")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TRAINING_PIPELINE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    training_pipeline: _training_pipeline_pb2.TrainingPipeline
    def __init__(self, parent: _Optional[str] = ..., training_pipeline: _Optional[_Union[_training_pipeline_pb2.TrainingPipeline, _Mapping]] = ...) -> None: ...

class GetTrainingPipelineRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListTrainingPipelinesRequest(_message.Message):
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

class ListTrainingPipelinesResponse(_message.Message):
    __slots__ = ("training_pipelines", "next_page_token")
    TRAINING_PIPELINES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    training_pipelines: _containers.RepeatedCompositeFieldContainer[_training_pipeline_pb2.TrainingPipeline]
    next_page_token: str
    def __init__(self, training_pipelines: _Optional[_Iterable[_Union[_training_pipeline_pb2.TrainingPipeline, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class DeleteTrainingPipelineRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CancelTrainingPipelineRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CreatePipelineJobRequest(_message.Message):
    __slots__ = ("parent", "pipeline_job", "pipeline_job_id")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PIPELINE_JOB_FIELD_NUMBER: _ClassVar[int]
    PIPELINE_JOB_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    pipeline_job: _pipeline_job_pb2.PipelineJob
    pipeline_job_id: str
    def __init__(self, parent: _Optional[str] = ..., pipeline_job: _Optional[_Union[_pipeline_job_pb2.PipelineJob, _Mapping]] = ..., pipeline_job_id: _Optional[str] = ...) -> None: ...

class GetPipelineJobRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListPipelineJobsRequest(_message.Message):
    __slots__ = ("parent", "filter", "page_size", "page_token", "order_by", "read_mask")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    READ_MASK_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    page_size: int
    page_token: str
    order_by: str
    read_mask: _field_mask_pb2.FieldMask
    def __init__(self, parent: _Optional[str] = ..., filter: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., order_by: _Optional[str] = ..., read_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class ListPipelineJobsResponse(_message.Message):
    __slots__ = ("pipeline_jobs", "next_page_token")
    PIPELINE_JOBS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    pipeline_jobs: _containers.RepeatedCompositeFieldContainer[_pipeline_job_pb2.PipelineJob]
    next_page_token: str
    def __init__(self, pipeline_jobs: _Optional[_Iterable[_Union[_pipeline_job_pb2.PipelineJob, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class DeletePipelineJobRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class BatchDeletePipelineJobsRequest(_message.Message):
    __slots__ = ("parent", "names")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NAMES_FIELD_NUMBER: _ClassVar[int]
    parent: str
    names: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, parent: _Optional[str] = ..., names: _Optional[_Iterable[str]] = ...) -> None: ...

class BatchDeletePipelineJobsResponse(_message.Message):
    __slots__ = ("pipeline_jobs",)
    PIPELINE_JOBS_FIELD_NUMBER: _ClassVar[int]
    pipeline_jobs: _containers.RepeatedCompositeFieldContainer[_pipeline_job_pb2.PipelineJob]
    def __init__(self, pipeline_jobs: _Optional[_Iterable[_Union[_pipeline_job_pb2.PipelineJob, _Mapping]]] = ...) -> None: ...

class CancelPipelineJobRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class BatchCancelPipelineJobsRequest(_message.Message):
    __slots__ = ("parent", "names")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NAMES_FIELD_NUMBER: _ClassVar[int]
    parent: str
    names: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, parent: _Optional[str] = ..., names: _Optional[_Iterable[str]] = ...) -> None: ...

class BatchCancelPipelineJobsResponse(_message.Message):
    __slots__ = ("pipeline_jobs",)
    PIPELINE_JOBS_FIELD_NUMBER: _ClassVar[int]
    pipeline_jobs: _containers.RepeatedCompositeFieldContainer[_pipeline_job_pb2.PipelineJob]
    def __init__(self, pipeline_jobs: _Optional[_Iterable[_Union[_pipeline_job_pb2.PipelineJob, _Mapping]]] = ...) -> None: ...
