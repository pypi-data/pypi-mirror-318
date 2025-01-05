from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.dataplex.v1 import analyze_pb2 as _analyze_pb2
from google.cloud.dataplex.v1 import resources_pb2 as _resources_pb2
from google.cloud.dataplex.v1 import tasks_pb2 as _tasks_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CreateLakeRequest(_message.Message):
    __slots__ = ('parent', 'lake_id', 'lake', 'validate_only')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    LAKE_ID_FIELD_NUMBER: _ClassVar[int]
    LAKE_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    lake_id: str
    lake: _resources_pb2.Lake
    validate_only: bool

    def __init__(self, parent: _Optional[str]=..., lake_id: _Optional[str]=..., lake: _Optional[_Union[_resources_pb2.Lake, _Mapping]]=..., validate_only: bool=...) -> None:
        ...

class UpdateLakeRequest(_message.Message):
    __slots__ = ('update_mask', 'lake', 'validate_only')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    LAKE_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    lake: _resources_pb2.Lake
    validate_only: bool

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., lake: _Optional[_Union[_resources_pb2.Lake, _Mapping]]=..., validate_only: bool=...) -> None:
        ...

class DeleteLakeRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListLakesRequest(_message.Message):
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

class ListLakesResponse(_message.Message):
    __slots__ = ('lakes', 'next_page_token', 'unreachable_locations')
    LAKES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_LOCATIONS_FIELD_NUMBER: _ClassVar[int]
    lakes: _containers.RepeatedCompositeFieldContainer[_resources_pb2.Lake]
    next_page_token: str
    unreachable_locations: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, lakes: _Optional[_Iterable[_Union[_resources_pb2.Lake, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable_locations: _Optional[_Iterable[str]]=...) -> None:
        ...

class ListLakeActionsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListActionsResponse(_message.Message):
    __slots__ = ('actions', 'next_page_token')
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    actions: _containers.RepeatedCompositeFieldContainer[_resources_pb2.Action]
    next_page_token: str

    def __init__(self, actions: _Optional[_Iterable[_Union[_resources_pb2.Action, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetLakeRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateZoneRequest(_message.Message):
    __slots__ = ('parent', 'zone_id', 'zone', 'validate_only')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ZONE_ID_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    zone_id: str
    zone: _resources_pb2.Zone
    validate_only: bool

    def __init__(self, parent: _Optional[str]=..., zone_id: _Optional[str]=..., zone: _Optional[_Union[_resources_pb2.Zone, _Mapping]]=..., validate_only: bool=...) -> None:
        ...

class UpdateZoneRequest(_message.Message):
    __slots__ = ('update_mask', 'zone', 'validate_only')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    zone: _resources_pb2.Zone
    validate_only: bool

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., zone: _Optional[_Union[_resources_pb2.Zone, _Mapping]]=..., validate_only: bool=...) -> None:
        ...

class DeleteZoneRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListZonesRequest(_message.Message):
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

class ListZonesResponse(_message.Message):
    __slots__ = ('zones', 'next_page_token')
    ZONES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    zones: _containers.RepeatedCompositeFieldContainer[_resources_pb2.Zone]
    next_page_token: str

    def __init__(self, zones: _Optional[_Iterable[_Union[_resources_pb2.Zone, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class ListZoneActionsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class GetZoneRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateAssetRequest(_message.Message):
    __slots__ = ('parent', 'asset_id', 'asset', 'validate_only')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ASSET_ID_FIELD_NUMBER: _ClassVar[int]
    ASSET_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    asset_id: str
    asset: _resources_pb2.Asset
    validate_only: bool

    def __init__(self, parent: _Optional[str]=..., asset_id: _Optional[str]=..., asset: _Optional[_Union[_resources_pb2.Asset, _Mapping]]=..., validate_only: bool=...) -> None:
        ...

class UpdateAssetRequest(_message.Message):
    __slots__ = ('update_mask', 'asset', 'validate_only')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    ASSET_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    asset: _resources_pb2.Asset
    validate_only: bool

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., asset: _Optional[_Union[_resources_pb2.Asset, _Mapping]]=..., validate_only: bool=...) -> None:
        ...

class DeleteAssetRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListAssetsRequest(_message.Message):
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

class ListAssetsResponse(_message.Message):
    __slots__ = ('assets', 'next_page_token')
    ASSETS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    assets: _containers.RepeatedCompositeFieldContainer[_resources_pb2.Asset]
    next_page_token: str

    def __init__(self, assets: _Optional[_Iterable[_Union[_resources_pb2.Asset, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class ListAssetActionsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class GetAssetRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class OperationMetadata(_message.Message):
    __slots__ = ('create_time', 'end_time', 'target', 'verb', 'status_message', 'requested_cancellation', 'api_version')
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    VERB_FIELD_NUMBER: _ClassVar[int]
    STATUS_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_CANCELLATION_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    target: str
    verb: str
    status_message: str
    requested_cancellation: bool
    api_version: str

    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., target: _Optional[str]=..., verb: _Optional[str]=..., status_message: _Optional[str]=..., requested_cancellation: bool=..., api_version: _Optional[str]=...) -> None:
        ...

class CreateTaskRequest(_message.Message):
    __slots__ = ('parent', 'task_id', 'task', 'validate_only')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    TASK_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    task_id: str
    task: _tasks_pb2.Task
    validate_only: bool

    def __init__(self, parent: _Optional[str]=..., task_id: _Optional[str]=..., task: _Optional[_Union[_tasks_pb2.Task, _Mapping]]=..., validate_only: bool=...) -> None:
        ...

class UpdateTaskRequest(_message.Message):
    __slots__ = ('update_mask', 'task', 'validate_only')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    TASK_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    task: _tasks_pb2.Task
    validate_only: bool

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., task: _Optional[_Union[_tasks_pb2.Task, _Mapping]]=..., validate_only: bool=...) -> None:
        ...

class DeleteTaskRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListTasksRequest(_message.Message):
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

class ListTasksResponse(_message.Message):
    __slots__ = ('tasks', 'next_page_token', 'unreachable_locations')
    TASKS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_LOCATIONS_FIELD_NUMBER: _ClassVar[int]
    tasks: _containers.RepeatedCompositeFieldContainer[_tasks_pb2.Task]
    next_page_token: str
    unreachable_locations: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, tasks: _Optional[_Iterable[_Union[_tasks_pb2.Task, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable_locations: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetTaskRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class GetJobRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class RunTaskRequest(_message.Message):
    __slots__ = ('name', 'labels', 'args')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...

    class ArgsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    ARGS_FIELD_NUMBER: _ClassVar[int]
    name: str
    labels: _containers.ScalarMap[str, str]
    args: _containers.ScalarMap[str, str]

    def __init__(self, name: _Optional[str]=..., labels: _Optional[_Mapping[str, str]]=..., args: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class RunTaskResponse(_message.Message):
    __slots__ = ('job',)
    JOB_FIELD_NUMBER: _ClassVar[int]
    job: _tasks_pb2.Job

    def __init__(self, job: _Optional[_Union[_tasks_pb2.Job, _Mapping]]=...) -> None:
        ...

class ListJobsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListJobsResponse(_message.Message):
    __slots__ = ('jobs', 'next_page_token')
    JOBS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    jobs: _containers.RepeatedCompositeFieldContainer[_tasks_pb2.Job]
    next_page_token: str

    def __init__(self, jobs: _Optional[_Iterable[_Union[_tasks_pb2.Job, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class CancelJobRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateEnvironmentRequest(_message.Message):
    __slots__ = ('parent', 'environment_id', 'environment', 'validate_only')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_ID_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    environment_id: str
    environment: _analyze_pb2.Environment
    validate_only: bool

    def __init__(self, parent: _Optional[str]=..., environment_id: _Optional[str]=..., environment: _Optional[_Union[_analyze_pb2.Environment, _Mapping]]=..., validate_only: bool=...) -> None:
        ...

class UpdateEnvironmentRequest(_message.Message):
    __slots__ = ('update_mask', 'environment', 'validate_only')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    environment: _analyze_pb2.Environment
    validate_only: bool

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., environment: _Optional[_Union[_analyze_pb2.Environment, _Mapping]]=..., validate_only: bool=...) -> None:
        ...

class DeleteEnvironmentRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListEnvironmentsRequest(_message.Message):
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

class ListEnvironmentsResponse(_message.Message):
    __slots__ = ('environments', 'next_page_token')
    ENVIRONMENTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    environments: _containers.RepeatedCompositeFieldContainer[_analyze_pb2.Environment]
    next_page_token: str

    def __init__(self, environments: _Optional[_Iterable[_Union[_analyze_pb2.Environment, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetEnvironmentRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListSessionsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=...) -> None:
        ...

class ListSessionsResponse(_message.Message):
    __slots__ = ('sessions', 'next_page_token')
    SESSIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    sessions: _containers.RepeatedCompositeFieldContainer[_analyze_pb2.Session]
    next_page_token: str

    def __init__(self, sessions: _Optional[_Iterable[_Union[_analyze_pb2.Session, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...