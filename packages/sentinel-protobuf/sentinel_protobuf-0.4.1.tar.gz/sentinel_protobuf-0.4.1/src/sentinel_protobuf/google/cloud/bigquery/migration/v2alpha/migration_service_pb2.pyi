from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.bigquery.migration.v2alpha import migration_entities_pb2 as _migration_entities_pb2
from google.cloud.bigquery.migration.v2alpha import migration_error_details_pb2 as _migration_error_details_pb2
from google.cloud.bigquery.migration.v2alpha import migration_metrics_pb2 as _migration_metrics_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CreateMigrationWorkflowRequest(_message.Message):
    __slots__ = ('parent', 'migration_workflow')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    MIGRATION_WORKFLOW_FIELD_NUMBER: _ClassVar[int]
    parent: str
    migration_workflow: _migration_entities_pb2.MigrationWorkflow

    def __init__(self, parent: _Optional[str]=..., migration_workflow: _Optional[_Union[_migration_entities_pb2.MigrationWorkflow, _Mapping]]=...) -> None:
        ...

class GetMigrationWorkflowRequest(_message.Message):
    __slots__ = ('name', 'read_mask')
    NAME_FIELD_NUMBER: _ClassVar[int]
    READ_MASK_FIELD_NUMBER: _ClassVar[int]
    name: str
    read_mask: _field_mask_pb2.FieldMask

    def __init__(self, name: _Optional[str]=..., read_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class ListMigrationWorkflowsRequest(_message.Message):
    __slots__ = ('parent', 'read_mask', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    READ_MASK_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    read_mask: _field_mask_pb2.FieldMask
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., read_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListMigrationWorkflowsResponse(_message.Message):
    __slots__ = ('migration_workflows', 'next_page_token')
    MIGRATION_WORKFLOWS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    migration_workflows: _containers.RepeatedCompositeFieldContainer[_migration_entities_pb2.MigrationWorkflow]
    next_page_token: str

    def __init__(self, migration_workflows: _Optional[_Iterable[_Union[_migration_entities_pb2.MigrationWorkflow, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class DeleteMigrationWorkflowRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class StartMigrationWorkflowRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class GetMigrationSubtaskRequest(_message.Message):
    __slots__ = ('name', 'read_mask')
    NAME_FIELD_NUMBER: _ClassVar[int]
    READ_MASK_FIELD_NUMBER: _ClassVar[int]
    name: str
    read_mask: _field_mask_pb2.FieldMask

    def __init__(self, name: _Optional[str]=..., read_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class ListMigrationSubtasksRequest(_message.Message):
    __slots__ = ('parent', 'read_mask', 'page_size', 'page_token', 'filter')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    READ_MASK_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    read_mask: _field_mask_pb2.FieldMask
    page_size: int
    page_token: str
    filter: str

    def __init__(self, parent: _Optional[str]=..., read_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=...) -> None:
        ...

class ListMigrationSubtasksResponse(_message.Message):
    __slots__ = ('migration_subtasks', 'next_page_token')
    MIGRATION_SUBTASKS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    migration_subtasks: _containers.RepeatedCompositeFieldContainer[_migration_entities_pb2.MigrationSubtask]
    next_page_token: str

    def __init__(self, migration_subtasks: _Optional[_Iterable[_Union[_migration_entities_pb2.MigrationSubtask, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...