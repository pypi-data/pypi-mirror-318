from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.aiplatform.v1beta1 import io_pb2 as _io_pb2
from google.cloud.aiplatform.v1beta1 import operation_pb2 as _operation_pb2
from google.cloud.aiplatform.v1beta1 import tuning_job_pb2 as _tuning_job_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateTuningJobRequest(_message.Message):
    __slots__ = ("parent", "tuning_job")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TUNING_JOB_FIELD_NUMBER: _ClassVar[int]
    parent: str
    tuning_job: _tuning_job_pb2.TuningJob
    def __init__(self, parent: _Optional[str] = ..., tuning_job: _Optional[_Union[_tuning_job_pb2.TuningJob, _Mapping]] = ...) -> None: ...

class GetTuningJobRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListTuningJobsRequest(_message.Message):
    __slots__ = ("parent", "filter", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., filter: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListTuningJobsResponse(_message.Message):
    __slots__ = ("tuning_jobs", "next_page_token")
    TUNING_JOBS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    tuning_jobs: _containers.RepeatedCompositeFieldContainer[_tuning_job_pb2.TuningJob]
    next_page_token: str
    def __init__(self, tuning_jobs: _Optional[_Iterable[_Union[_tuning_job_pb2.TuningJob, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class CancelTuningJobRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class RebaseTunedModelRequest(_message.Message):
    __slots__ = ("parent", "tuned_model_ref", "tuning_job", "artifact_destination", "deploy_to_same_endpoint")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TUNED_MODEL_REF_FIELD_NUMBER: _ClassVar[int]
    TUNING_JOB_FIELD_NUMBER: _ClassVar[int]
    ARTIFACT_DESTINATION_FIELD_NUMBER: _ClassVar[int]
    DEPLOY_TO_SAME_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    parent: str
    tuned_model_ref: _tuning_job_pb2.TunedModelRef
    tuning_job: _tuning_job_pb2.TuningJob
    artifact_destination: _io_pb2.GcsDestination
    deploy_to_same_endpoint: bool
    def __init__(self, parent: _Optional[str] = ..., tuned_model_ref: _Optional[_Union[_tuning_job_pb2.TunedModelRef, _Mapping]] = ..., tuning_job: _Optional[_Union[_tuning_job_pb2.TuningJob, _Mapping]] = ..., artifact_destination: _Optional[_Union[_io_pb2.GcsDestination, _Mapping]] = ..., deploy_to_same_endpoint: bool = ...) -> None: ...

class RebaseTunedModelOperationMetadata(_message.Message):
    __slots__ = ("generic_metadata",)
    GENERIC_METADATA_FIELD_NUMBER: _ClassVar[int]
    generic_metadata: _operation_pb2.GenericOperationMetadata
    def __init__(self, generic_metadata: _Optional[_Union[_operation_pb2.GenericOperationMetadata, _Mapping]] = ...) -> None: ...
