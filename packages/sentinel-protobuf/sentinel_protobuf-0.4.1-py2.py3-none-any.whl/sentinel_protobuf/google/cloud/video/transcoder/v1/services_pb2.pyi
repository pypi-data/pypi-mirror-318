from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.video.transcoder.v1 import resources_pb2 as _resources_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CreateJobRequest(_message.Message):
    __slots__ = ('parent', 'job')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    JOB_FIELD_NUMBER: _ClassVar[int]
    parent: str
    job: _resources_pb2.Job

    def __init__(self, parent: _Optional[str]=..., job: _Optional[_Union[_resources_pb2.Job, _Mapping]]=...) -> None:
        ...

class ListJobsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'order_by')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=...) -> None:
        ...

class GetJobRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class DeleteJobRequest(_message.Message):
    __slots__ = ('name', 'allow_missing')
    NAME_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MISSING_FIELD_NUMBER: _ClassVar[int]
    name: str
    allow_missing: bool

    def __init__(self, name: _Optional[str]=..., allow_missing: bool=...) -> None:
        ...

class ListJobsResponse(_message.Message):
    __slots__ = ('jobs', 'next_page_token', 'unreachable')
    JOBS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    jobs: _containers.RepeatedCompositeFieldContainer[_resources_pb2.Job]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, jobs: _Optional[_Iterable[_Union[_resources_pb2.Job, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class CreateJobTemplateRequest(_message.Message):
    __slots__ = ('parent', 'job_template', 'job_template_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    JOB_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    JOB_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    job_template: _resources_pb2.JobTemplate
    job_template_id: str

    def __init__(self, parent: _Optional[str]=..., job_template: _Optional[_Union[_resources_pb2.JobTemplate, _Mapping]]=..., job_template_id: _Optional[str]=...) -> None:
        ...

class ListJobTemplatesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'order_by')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=...) -> None:
        ...

class GetJobTemplateRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class DeleteJobTemplateRequest(_message.Message):
    __slots__ = ('name', 'allow_missing')
    NAME_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MISSING_FIELD_NUMBER: _ClassVar[int]
    name: str
    allow_missing: bool

    def __init__(self, name: _Optional[str]=..., allow_missing: bool=...) -> None:
        ...

class ListJobTemplatesResponse(_message.Message):
    __slots__ = ('job_templates', 'next_page_token', 'unreachable')
    JOB_TEMPLATES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    job_templates: _containers.RepeatedCompositeFieldContainer[_resources_pb2.JobTemplate]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, job_templates: _Optional[_Iterable[_Union[_resources_pb2.JobTemplate, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...