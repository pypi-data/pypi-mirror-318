from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.storagetransfer.v1 import transfer_types_pb2 as _transfer_types_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class GetGoogleServiceAccountRequest(_message.Message):
    __slots__ = ('project_id',)
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    project_id: str

    def __init__(self, project_id: _Optional[str]=...) -> None:
        ...

class CreateTransferJobRequest(_message.Message):
    __slots__ = ('transfer_job',)
    TRANSFER_JOB_FIELD_NUMBER: _ClassVar[int]
    transfer_job: _transfer_types_pb2.TransferJob

    def __init__(self, transfer_job: _Optional[_Union[_transfer_types_pb2.TransferJob, _Mapping]]=...) -> None:
        ...

class UpdateTransferJobRequest(_message.Message):
    __slots__ = ('job_name', 'project_id', 'transfer_job', 'update_transfer_job_field_mask')
    JOB_NAME_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_JOB_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TRANSFER_JOB_FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    job_name: str
    project_id: str
    transfer_job: _transfer_types_pb2.TransferJob
    update_transfer_job_field_mask: _field_mask_pb2.FieldMask

    def __init__(self, job_name: _Optional[str]=..., project_id: _Optional[str]=..., transfer_job: _Optional[_Union[_transfer_types_pb2.TransferJob, _Mapping]]=..., update_transfer_job_field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class GetTransferJobRequest(_message.Message):
    __slots__ = ('job_name', 'project_id')
    JOB_NAME_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    job_name: str
    project_id: str

    def __init__(self, job_name: _Optional[str]=..., project_id: _Optional[str]=...) -> None:
        ...

class DeleteTransferJobRequest(_message.Message):
    __slots__ = ('job_name', 'project_id')
    JOB_NAME_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    job_name: str
    project_id: str

    def __init__(self, job_name: _Optional[str]=..., project_id: _Optional[str]=...) -> None:
        ...

class ListTransferJobsRequest(_message.Message):
    __slots__ = ('filter', 'page_size', 'page_token')
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    filter: str
    page_size: int
    page_token: str

    def __init__(self, filter: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListTransferJobsResponse(_message.Message):
    __slots__ = ('transfer_jobs', 'next_page_token')
    TRANSFER_JOBS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    transfer_jobs: _containers.RepeatedCompositeFieldContainer[_transfer_types_pb2.TransferJob]
    next_page_token: str

    def __init__(self, transfer_jobs: _Optional[_Iterable[_Union[_transfer_types_pb2.TransferJob, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class PauseTransferOperationRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ResumeTransferOperationRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class RunTransferJobRequest(_message.Message):
    __slots__ = ('job_name', 'project_id')
    JOB_NAME_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    job_name: str
    project_id: str

    def __init__(self, job_name: _Optional[str]=..., project_id: _Optional[str]=...) -> None:
        ...

class CreateAgentPoolRequest(_message.Message):
    __slots__ = ('project_id', 'agent_pool', 'agent_pool_id')
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    AGENT_POOL_FIELD_NUMBER: _ClassVar[int]
    AGENT_POOL_ID_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    agent_pool: _transfer_types_pb2.AgentPool
    agent_pool_id: str

    def __init__(self, project_id: _Optional[str]=..., agent_pool: _Optional[_Union[_transfer_types_pb2.AgentPool, _Mapping]]=..., agent_pool_id: _Optional[str]=...) -> None:
        ...

class UpdateAgentPoolRequest(_message.Message):
    __slots__ = ('agent_pool', 'update_mask')
    AGENT_POOL_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    agent_pool: _transfer_types_pb2.AgentPool
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, agent_pool: _Optional[_Union[_transfer_types_pb2.AgentPool, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class GetAgentPoolRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class DeleteAgentPoolRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListAgentPoolsRequest(_message.Message):
    __slots__ = ('project_id', 'filter', 'page_size', 'page_token')
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    filter: str
    page_size: int
    page_token: str

    def __init__(self, project_id: _Optional[str]=..., filter: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListAgentPoolsResponse(_message.Message):
    __slots__ = ('agent_pools', 'next_page_token')
    AGENT_POOLS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    agent_pools: _containers.RepeatedCompositeFieldContainer[_transfer_types_pb2.AgentPool]
    next_page_token: str

    def __init__(self, agent_pools: _Optional[_Iterable[_Union[_transfer_types_pb2.AgentPool, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...