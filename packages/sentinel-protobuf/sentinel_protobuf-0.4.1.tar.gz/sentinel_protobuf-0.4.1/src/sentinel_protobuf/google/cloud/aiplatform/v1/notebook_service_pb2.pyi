from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.aiplatform.v1 import notebook_execution_job_pb2 as _notebook_execution_job_pb2
from google.cloud.aiplatform.v1 import notebook_runtime_pb2 as _notebook_runtime_pb2
from google.cloud.aiplatform.v1 import operation_pb2 as _operation_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class NotebookExecutionJobView(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NOTEBOOK_EXECUTION_JOB_VIEW_UNSPECIFIED: _ClassVar[NotebookExecutionJobView]
    NOTEBOOK_EXECUTION_JOB_VIEW_BASIC: _ClassVar[NotebookExecutionJobView]
    NOTEBOOK_EXECUTION_JOB_VIEW_FULL: _ClassVar[NotebookExecutionJobView]
NOTEBOOK_EXECUTION_JOB_VIEW_UNSPECIFIED: NotebookExecutionJobView
NOTEBOOK_EXECUTION_JOB_VIEW_BASIC: NotebookExecutionJobView
NOTEBOOK_EXECUTION_JOB_VIEW_FULL: NotebookExecutionJobView

class CreateNotebookRuntimeTemplateRequest(_message.Message):
    __slots__ = ('parent', 'notebook_runtime_template', 'notebook_runtime_template_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NOTEBOOK_RUNTIME_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    NOTEBOOK_RUNTIME_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    notebook_runtime_template: _notebook_runtime_pb2.NotebookRuntimeTemplate
    notebook_runtime_template_id: str

    def __init__(self, parent: _Optional[str]=..., notebook_runtime_template: _Optional[_Union[_notebook_runtime_pb2.NotebookRuntimeTemplate, _Mapping]]=..., notebook_runtime_template_id: _Optional[str]=...) -> None:
        ...

class CreateNotebookRuntimeTemplateOperationMetadata(_message.Message):
    __slots__ = ('generic_metadata',)
    GENERIC_METADATA_FIELD_NUMBER: _ClassVar[int]
    generic_metadata: _operation_pb2.GenericOperationMetadata

    def __init__(self, generic_metadata: _Optional[_Union[_operation_pb2.GenericOperationMetadata, _Mapping]]=...) -> None:
        ...

class GetNotebookRuntimeTemplateRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListNotebookRuntimeTemplatesRequest(_message.Message):
    __slots__ = ('parent', 'filter', 'page_size', 'page_token', 'read_mask', 'order_by')
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

    def __init__(self, parent: _Optional[str]=..., filter: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., read_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., order_by: _Optional[str]=...) -> None:
        ...

class ListNotebookRuntimeTemplatesResponse(_message.Message):
    __slots__ = ('notebook_runtime_templates', 'next_page_token')
    NOTEBOOK_RUNTIME_TEMPLATES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    notebook_runtime_templates: _containers.RepeatedCompositeFieldContainer[_notebook_runtime_pb2.NotebookRuntimeTemplate]
    next_page_token: str

    def __init__(self, notebook_runtime_templates: _Optional[_Iterable[_Union[_notebook_runtime_pb2.NotebookRuntimeTemplate, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class DeleteNotebookRuntimeTemplateRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateNotebookRuntimeTemplateRequest(_message.Message):
    __slots__ = ('notebook_runtime_template', 'update_mask')
    NOTEBOOK_RUNTIME_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    notebook_runtime_template: _notebook_runtime_pb2.NotebookRuntimeTemplate
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, notebook_runtime_template: _Optional[_Union[_notebook_runtime_pb2.NotebookRuntimeTemplate, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class AssignNotebookRuntimeRequest(_message.Message):
    __slots__ = ('parent', 'notebook_runtime_template', 'notebook_runtime', 'notebook_runtime_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NOTEBOOK_RUNTIME_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    NOTEBOOK_RUNTIME_FIELD_NUMBER: _ClassVar[int]
    NOTEBOOK_RUNTIME_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    notebook_runtime_template: str
    notebook_runtime: _notebook_runtime_pb2.NotebookRuntime
    notebook_runtime_id: str

    def __init__(self, parent: _Optional[str]=..., notebook_runtime_template: _Optional[str]=..., notebook_runtime: _Optional[_Union[_notebook_runtime_pb2.NotebookRuntime, _Mapping]]=..., notebook_runtime_id: _Optional[str]=...) -> None:
        ...

class AssignNotebookRuntimeOperationMetadata(_message.Message):
    __slots__ = ('generic_metadata', 'progress_message')
    GENERIC_METADATA_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    generic_metadata: _operation_pb2.GenericOperationMetadata
    progress_message: str

    def __init__(self, generic_metadata: _Optional[_Union[_operation_pb2.GenericOperationMetadata, _Mapping]]=..., progress_message: _Optional[str]=...) -> None:
        ...

class GetNotebookRuntimeRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListNotebookRuntimesRequest(_message.Message):
    __slots__ = ('parent', 'filter', 'page_size', 'page_token', 'read_mask', 'order_by')
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

    def __init__(self, parent: _Optional[str]=..., filter: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., read_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., order_by: _Optional[str]=...) -> None:
        ...

class ListNotebookRuntimesResponse(_message.Message):
    __slots__ = ('notebook_runtimes', 'next_page_token')
    NOTEBOOK_RUNTIMES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    notebook_runtimes: _containers.RepeatedCompositeFieldContainer[_notebook_runtime_pb2.NotebookRuntime]
    next_page_token: str

    def __init__(self, notebook_runtimes: _Optional[_Iterable[_Union[_notebook_runtime_pb2.NotebookRuntime, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class DeleteNotebookRuntimeRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpgradeNotebookRuntimeRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpgradeNotebookRuntimeOperationMetadata(_message.Message):
    __slots__ = ('generic_metadata', 'progress_message')
    GENERIC_METADATA_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    generic_metadata: _operation_pb2.GenericOperationMetadata
    progress_message: str

    def __init__(self, generic_metadata: _Optional[_Union[_operation_pb2.GenericOperationMetadata, _Mapping]]=..., progress_message: _Optional[str]=...) -> None:
        ...

class UpgradeNotebookRuntimeResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class StartNotebookRuntimeRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class StartNotebookRuntimeOperationMetadata(_message.Message):
    __slots__ = ('generic_metadata', 'progress_message')
    GENERIC_METADATA_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    generic_metadata: _operation_pb2.GenericOperationMetadata
    progress_message: str

    def __init__(self, generic_metadata: _Optional[_Union[_operation_pb2.GenericOperationMetadata, _Mapping]]=..., progress_message: _Optional[str]=...) -> None:
        ...

class StartNotebookRuntimeResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class StopNotebookRuntimeRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class StopNotebookRuntimeOperationMetadata(_message.Message):
    __slots__ = ('generic_metadata',)
    GENERIC_METADATA_FIELD_NUMBER: _ClassVar[int]
    generic_metadata: _operation_pb2.GenericOperationMetadata

    def __init__(self, generic_metadata: _Optional[_Union[_operation_pb2.GenericOperationMetadata, _Mapping]]=...) -> None:
        ...

class StopNotebookRuntimeResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class CreateNotebookExecutionJobRequest(_message.Message):
    __slots__ = ('parent', 'notebook_execution_job', 'notebook_execution_job_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NOTEBOOK_EXECUTION_JOB_FIELD_NUMBER: _ClassVar[int]
    NOTEBOOK_EXECUTION_JOB_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    notebook_execution_job: _notebook_execution_job_pb2.NotebookExecutionJob
    notebook_execution_job_id: str

    def __init__(self, parent: _Optional[str]=..., notebook_execution_job: _Optional[_Union[_notebook_execution_job_pb2.NotebookExecutionJob, _Mapping]]=..., notebook_execution_job_id: _Optional[str]=...) -> None:
        ...

class CreateNotebookExecutionJobOperationMetadata(_message.Message):
    __slots__ = ('generic_metadata', 'progress_message')
    GENERIC_METADATA_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    generic_metadata: _operation_pb2.GenericOperationMetadata
    progress_message: str

    def __init__(self, generic_metadata: _Optional[_Union[_operation_pb2.GenericOperationMetadata, _Mapping]]=..., progress_message: _Optional[str]=...) -> None:
        ...

class GetNotebookExecutionJobRequest(_message.Message):
    __slots__ = ('name', 'view')
    NAME_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    name: str
    view: NotebookExecutionJobView

    def __init__(self, name: _Optional[str]=..., view: _Optional[_Union[NotebookExecutionJobView, str]]=...) -> None:
        ...

class ListNotebookExecutionJobsRequest(_message.Message):
    __slots__ = ('parent', 'filter', 'page_size', 'page_token', 'order_by', 'view')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    page_size: int
    page_token: str
    order_by: str
    view: NotebookExecutionJobView

    def __init__(self, parent: _Optional[str]=..., filter: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., order_by: _Optional[str]=..., view: _Optional[_Union[NotebookExecutionJobView, str]]=...) -> None:
        ...

class ListNotebookExecutionJobsResponse(_message.Message):
    __slots__ = ('notebook_execution_jobs', 'next_page_token')
    NOTEBOOK_EXECUTION_JOBS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    notebook_execution_jobs: _containers.RepeatedCompositeFieldContainer[_notebook_execution_job_pb2.NotebookExecutionJob]
    next_page_token: str

    def __init__(self, notebook_execution_jobs: _Optional[_Iterable[_Union[_notebook_execution_job_pb2.NotebookExecutionJob, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class DeleteNotebookExecutionJobRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...