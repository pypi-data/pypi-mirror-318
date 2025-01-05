from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class BlueprintView(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BLUEPRINT_VIEW_UNSPECIFIED: _ClassVar[BlueprintView]
    BLUEPRINT_VIEW_BASIC: _ClassVar[BlueprintView]
    BLUEPRINT_VIEW_FULL: _ClassVar[BlueprintView]

class DeploymentView(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DEPLOYMENT_VIEW_UNSPECIFIED: _ClassVar[DeploymentView]
    DEPLOYMENT_VIEW_BASIC: _ClassVar[DeploymentView]
    DEPLOYMENT_VIEW_FULL: _ClassVar[DeploymentView]

class ResourceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RESOURCE_TYPE_UNSPECIFIED: _ClassVar[ResourceType]
    NF_DEPLOY_RESOURCE: _ClassVar[ResourceType]
    DEPLOYMENT_RESOURCE: _ClassVar[ResourceType]

class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STATUS_UNSPECIFIED: _ClassVar[Status]
    STATUS_IN_PROGRESS: _ClassVar[Status]
    STATUS_ACTIVE: _ClassVar[Status]
    STATUS_FAILED: _ClassVar[Status]
    STATUS_DELETING: _ClassVar[Status]
    STATUS_DELETED: _ClassVar[Status]
    STATUS_PEERING: _ClassVar[Status]
    STATUS_NOT_APPLICABLE: _ClassVar[Status]

class DeploymentLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DEPLOYMENT_LEVEL_UNSPECIFIED: _ClassVar[DeploymentLevel]
    HYDRATION: _ClassVar[DeploymentLevel]
    SINGLE_DEPLOYMENT: _ClassVar[DeploymentLevel]
    MULTI_DEPLOYMENT: _ClassVar[DeploymentLevel]
    WORKLOAD_CLUSTER_DEPLOYMENT: _ClassVar[DeploymentLevel]
BLUEPRINT_VIEW_UNSPECIFIED: BlueprintView
BLUEPRINT_VIEW_BASIC: BlueprintView
BLUEPRINT_VIEW_FULL: BlueprintView
DEPLOYMENT_VIEW_UNSPECIFIED: DeploymentView
DEPLOYMENT_VIEW_BASIC: DeploymentView
DEPLOYMENT_VIEW_FULL: DeploymentView
RESOURCE_TYPE_UNSPECIFIED: ResourceType
NF_DEPLOY_RESOURCE: ResourceType
DEPLOYMENT_RESOURCE: ResourceType
STATUS_UNSPECIFIED: Status
STATUS_IN_PROGRESS: Status
STATUS_ACTIVE: Status
STATUS_FAILED: Status
STATUS_DELETING: Status
STATUS_DELETED: Status
STATUS_PEERING: Status
STATUS_NOT_APPLICABLE: Status
DEPLOYMENT_LEVEL_UNSPECIFIED: DeploymentLevel
HYDRATION: DeploymentLevel
SINGLE_DEPLOYMENT: DeploymentLevel
MULTI_DEPLOYMENT: DeploymentLevel
WORKLOAD_CLUSTER_DEPLOYMENT: DeploymentLevel

class OrchestrationCluster(_message.Message):
    __slots__ = ('name', 'management_config', 'create_time', 'update_time', 'labels', 'tna_version', 'state')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[OrchestrationCluster.State]
        CREATING: _ClassVar[OrchestrationCluster.State]
        ACTIVE: _ClassVar[OrchestrationCluster.State]
        DELETING: _ClassVar[OrchestrationCluster.State]
        FAILED: _ClassVar[OrchestrationCluster.State]
    STATE_UNSPECIFIED: OrchestrationCluster.State
    CREATING: OrchestrationCluster.State
    ACTIVE: OrchestrationCluster.State
    DELETING: OrchestrationCluster.State
    FAILED: OrchestrationCluster.State

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    MANAGEMENT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    TNA_VERSION_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    name: str
    management_config: ManagementConfig
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    tna_version: str
    state: OrchestrationCluster.State

    def __init__(self, name: _Optional[str]=..., management_config: _Optional[_Union[ManagementConfig, _Mapping]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., tna_version: _Optional[str]=..., state: _Optional[_Union[OrchestrationCluster.State, str]]=...) -> None:
        ...

class EdgeSlm(_message.Message):
    __slots__ = ('name', 'orchestration_cluster', 'create_time', 'update_time', 'labels', 'tna_version', 'state', 'workload_cluster_type')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[EdgeSlm.State]
        CREATING: _ClassVar[EdgeSlm.State]
        ACTIVE: _ClassVar[EdgeSlm.State]
        DELETING: _ClassVar[EdgeSlm.State]
        FAILED: _ClassVar[EdgeSlm.State]
    STATE_UNSPECIFIED: EdgeSlm.State
    CREATING: EdgeSlm.State
    ACTIVE: EdgeSlm.State
    DELETING: EdgeSlm.State
    FAILED: EdgeSlm.State

    class WorkloadClusterType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        WORKLOAD_CLUSTER_TYPE_UNSPECIFIED: _ClassVar[EdgeSlm.WorkloadClusterType]
        GDCE: _ClassVar[EdgeSlm.WorkloadClusterType]
        GKE: _ClassVar[EdgeSlm.WorkloadClusterType]
    WORKLOAD_CLUSTER_TYPE_UNSPECIFIED: EdgeSlm.WorkloadClusterType
    GDCE: EdgeSlm.WorkloadClusterType
    GKE: EdgeSlm.WorkloadClusterType

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    ORCHESTRATION_CLUSTER_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    TNA_VERSION_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    WORKLOAD_CLUSTER_TYPE_FIELD_NUMBER: _ClassVar[int]
    name: str
    orchestration_cluster: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    tna_version: str
    state: EdgeSlm.State
    workload_cluster_type: EdgeSlm.WorkloadClusterType

    def __init__(self, name: _Optional[str]=..., orchestration_cluster: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., tna_version: _Optional[str]=..., state: _Optional[_Union[EdgeSlm.State, str]]=..., workload_cluster_type: _Optional[_Union[EdgeSlm.WorkloadClusterType, str]]=...) -> None:
        ...

class Blueprint(_message.Message):
    __slots__ = ('name', 'revision_id', 'source_blueprint', 'revision_create_time', 'approval_state', 'display_name', 'repository', 'files', 'labels', 'create_time', 'update_time', 'source_provider', 'deployment_level', 'rollback_support')

    class ApprovalState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        APPROVAL_STATE_UNSPECIFIED: _ClassVar[Blueprint.ApprovalState]
        DRAFT: _ClassVar[Blueprint.ApprovalState]
        PROPOSED: _ClassVar[Blueprint.ApprovalState]
        APPROVED: _ClassVar[Blueprint.ApprovalState]
    APPROVAL_STATE_UNSPECIFIED: Blueprint.ApprovalState
    DRAFT: Blueprint.ApprovalState
    PROPOSED: Blueprint.ApprovalState
    APPROVED: Blueprint.ApprovalState

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_BLUEPRINT_FIELD_NUMBER: _ClassVar[int]
    REVISION_CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    APPROVAL_STATE_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    REPOSITORY_FIELD_NUMBER: _ClassVar[int]
    FILES_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_PROVIDER_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_LEVEL_FIELD_NUMBER: _ClassVar[int]
    ROLLBACK_SUPPORT_FIELD_NUMBER: _ClassVar[int]
    name: str
    revision_id: str
    source_blueprint: str
    revision_create_time: _timestamp_pb2.Timestamp
    approval_state: Blueprint.ApprovalState
    display_name: str
    repository: str
    files: _containers.RepeatedCompositeFieldContainer[File]
    labels: _containers.ScalarMap[str, str]
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    source_provider: str
    deployment_level: DeploymentLevel
    rollback_support: bool

    def __init__(self, name: _Optional[str]=..., revision_id: _Optional[str]=..., source_blueprint: _Optional[str]=..., revision_create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., approval_state: _Optional[_Union[Blueprint.ApprovalState, str]]=..., display_name: _Optional[str]=..., repository: _Optional[str]=..., files: _Optional[_Iterable[_Union[File, _Mapping]]]=..., labels: _Optional[_Mapping[str, str]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., source_provider: _Optional[str]=..., deployment_level: _Optional[_Union[DeploymentLevel, str]]=..., rollback_support: bool=...) -> None:
        ...

class PublicBlueprint(_message.Message):
    __slots__ = ('name', 'display_name', 'description', 'deployment_level', 'source_provider', 'rollback_support')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_LEVEL_FIELD_NUMBER: _ClassVar[int]
    SOURCE_PROVIDER_FIELD_NUMBER: _ClassVar[int]
    ROLLBACK_SUPPORT_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    description: str
    deployment_level: DeploymentLevel
    source_provider: str
    rollback_support: bool

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., description: _Optional[str]=..., deployment_level: _Optional[_Union[DeploymentLevel, str]]=..., source_provider: _Optional[str]=..., rollback_support: bool=...) -> None:
        ...

class Deployment(_message.Message):
    __slots__ = ('name', 'revision_id', 'source_blueprint_revision', 'revision_create_time', 'state', 'display_name', 'repository', 'files', 'labels', 'create_time', 'update_time', 'source_provider', 'workload_cluster', 'deployment_level', 'rollback_support')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Deployment.State]
        DRAFT: _ClassVar[Deployment.State]
        APPLIED: _ClassVar[Deployment.State]
        DELETING: _ClassVar[Deployment.State]
    STATE_UNSPECIFIED: Deployment.State
    DRAFT: Deployment.State
    APPLIED: Deployment.State
    DELETING: Deployment.State

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_BLUEPRINT_REVISION_FIELD_NUMBER: _ClassVar[int]
    REVISION_CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    REPOSITORY_FIELD_NUMBER: _ClassVar[int]
    FILES_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_PROVIDER_FIELD_NUMBER: _ClassVar[int]
    WORKLOAD_CLUSTER_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_LEVEL_FIELD_NUMBER: _ClassVar[int]
    ROLLBACK_SUPPORT_FIELD_NUMBER: _ClassVar[int]
    name: str
    revision_id: str
    source_blueprint_revision: str
    revision_create_time: _timestamp_pb2.Timestamp
    state: Deployment.State
    display_name: str
    repository: str
    files: _containers.RepeatedCompositeFieldContainer[File]
    labels: _containers.ScalarMap[str, str]
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    source_provider: str
    workload_cluster: str
    deployment_level: DeploymentLevel
    rollback_support: bool

    def __init__(self, name: _Optional[str]=..., revision_id: _Optional[str]=..., source_blueprint_revision: _Optional[str]=..., revision_create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., state: _Optional[_Union[Deployment.State, str]]=..., display_name: _Optional[str]=..., repository: _Optional[str]=..., files: _Optional[_Iterable[_Union[File, _Mapping]]]=..., labels: _Optional[_Mapping[str, str]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., source_provider: _Optional[str]=..., workload_cluster: _Optional[str]=..., deployment_level: _Optional[_Union[DeploymentLevel, str]]=..., rollback_support: bool=...) -> None:
        ...

class HydratedDeployment(_message.Message):
    __slots__ = ('name', 'state', 'files', 'workload_cluster')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[HydratedDeployment.State]
        DRAFT: _ClassVar[HydratedDeployment.State]
        APPLIED: _ClassVar[HydratedDeployment.State]
    STATE_UNSPECIFIED: HydratedDeployment.State
    DRAFT: HydratedDeployment.State
    APPLIED: HydratedDeployment.State
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    FILES_FIELD_NUMBER: _ClassVar[int]
    WORKLOAD_CLUSTER_FIELD_NUMBER: _ClassVar[int]
    name: str
    state: HydratedDeployment.State
    files: _containers.RepeatedCompositeFieldContainer[File]
    workload_cluster: str

    def __init__(self, name: _Optional[str]=..., state: _Optional[_Union[HydratedDeployment.State, str]]=..., files: _Optional[_Iterable[_Union[File, _Mapping]]]=..., workload_cluster: _Optional[str]=...) -> None:
        ...

class ListOrchestrationClustersRequest(_message.Message):
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

class ListOrchestrationClustersResponse(_message.Message):
    __slots__ = ('orchestration_clusters', 'next_page_token', 'unreachable')
    ORCHESTRATION_CLUSTERS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    orchestration_clusters: _containers.RepeatedCompositeFieldContainer[OrchestrationCluster]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, orchestration_clusters: _Optional[_Iterable[_Union[OrchestrationCluster, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetOrchestrationClusterRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateOrchestrationClusterRequest(_message.Message):
    __slots__ = ('parent', 'orchestration_cluster_id', 'orchestration_cluster', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ORCHESTRATION_CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    ORCHESTRATION_CLUSTER_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    orchestration_cluster_id: str
    orchestration_cluster: OrchestrationCluster
    request_id: str

    def __init__(self, parent: _Optional[str]=..., orchestration_cluster_id: _Optional[str]=..., orchestration_cluster: _Optional[_Union[OrchestrationCluster, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class DeleteOrchestrationClusterRequest(_message.Message):
    __slots__ = ('name', 'request_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=...) -> None:
        ...

class ListEdgeSlmsRequest(_message.Message):
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

class ListEdgeSlmsResponse(_message.Message):
    __slots__ = ('edge_slms', 'next_page_token', 'unreachable')
    EDGE_SLMS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    edge_slms: _containers.RepeatedCompositeFieldContainer[EdgeSlm]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, edge_slms: _Optional[_Iterable[_Union[EdgeSlm, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetEdgeSlmRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateEdgeSlmRequest(_message.Message):
    __slots__ = ('parent', 'edge_slm_id', 'edge_slm', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    EDGE_SLM_ID_FIELD_NUMBER: _ClassVar[int]
    EDGE_SLM_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    edge_slm_id: str
    edge_slm: EdgeSlm
    request_id: str

    def __init__(self, parent: _Optional[str]=..., edge_slm_id: _Optional[str]=..., edge_slm: _Optional[_Union[EdgeSlm, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class DeleteEdgeSlmRequest(_message.Message):
    __slots__ = ('name', 'request_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=...) -> None:
        ...

class CreateBlueprintRequest(_message.Message):
    __slots__ = ('parent', 'blueprint_id', 'blueprint')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    BLUEPRINT_ID_FIELD_NUMBER: _ClassVar[int]
    BLUEPRINT_FIELD_NUMBER: _ClassVar[int]
    parent: str
    blueprint_id: str
    blueprint: Blueprint

    def __init__(self, parent: _Optional[str]=..., blueprint_id: _Optional[str]=..., blueprint: _Optional[_Union[Blueprint, _Mapping]]=...) -> None:
        ...

class UpdateBlueprintRequest(_message.Message):
    __slots__ = ('blueprint', 'update_mask')
    BLUEPRINT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    blueprint: Blueprint
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, blueprint: _Optional[_Union[Blueprint, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class GetBlueprintRequest(_message.Message):
    __slots__ = ('name', 'view')
    NAME_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    name: str
    view: BlueprintView

    def __init__(self, name: _Optional[str]=..., view: _Optional[_Union[BlueprintView, str]]=...) -> None:
        ...

class DeleteBlueprintRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListBlueprintsRequest(_message.Message):
    __slots__ = ('parent', 'filter', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., filter: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListBlueprintsResponse(_message.Message):
    __slots__ = ('blueprints', 'next_page_token')
    BLUEPRINTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    blueprints: _containers.RepeatedCompositeFieldContainer[Blueprint]
    next_page_token: str

    def __init__(self, blueprints: _Optional[_Iterable[_Union[Blueprint, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class ApproveBlueprintRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ProposeBlueprintRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class RejectBlueprintRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListBlueprintRevisionsRequest(_message.Message):
    __slots__ = ('name', 'page_size', 'page_token')
    NAME_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    name: str
    page_size: int
    page_token: str

    def __init__(self, name: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListBlueprintRevisionsResponse(_message.Message):
    __slots__ = ('blueprints', 'next_page_token')
    BLUEPRINTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    blueprints: _containers.RepeatedCompositeFieldContainer[Blueprint]
    next_page_token: str

    def __init__(self, blueprints: _Optional[_Iterable[_Union[Blueprint, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class SearchBlueprintRevisionsRequest(_message.Message):
    __slots__ = ('parent', 'query', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    query: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., query: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class SearchBlueprintRevisionsResponse(_message.Message):
    __slots__ = ('blueprints', 'next_page_token')
    BLUEPRINTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    blueprints: _containers.RepeatedCompositeFieldContainer[Blueprint]
    next_page_token: str

    def __init__(self, blueprints: _Optional[_Iterable[_Union[Blueprint, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class DiscardBlueprintChangesRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class DiscardBlueprintChangesResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class ListPublicBlueprintsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListPublicBlueprintsResponse(_message.Message):
    __slots__ = ('public_blueprints', 'next_page_token')
    PUBLIC_BLUEPRINTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    public_blueprints: _containers.RepeatedCompositeFieldContainer[PublicBlueprint]
    next_page_token: str

    def __init__(self, public_blueprints: _Optional[_Iterable[_Union[PublicBlueprint, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetPublicBlueprintRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateDeploymentRequest(_message.Message):
    __slots__ = ('parent', 'deployment_id', 'deployment')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_FIELD_NUMBER: _ClassVar[int]
    parent: str
    deployment_id: str
    deployment: Deployment

    def __init__(self, parent: _Optional[str]=..., deployment_id: _Optional[str]=..., deployment: _Optional[_Union[Deployment, _Mapping]]=...) -> None:
        ...

class UpdateDeploymentRequest(_message.Message):
    __slots__ = ('deployment', 'update_mask')
    DEPLOYMENT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    deployment: Deployment
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, deployment: _Optional[_Union[Deployment, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class GetDeploymentRequest(_message.Message):
    __slots__ = ('name', 'view')
    NAME_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    name: str
    view: DeploymentView

    def __init__(self, name: _Optional[str]=..., view: _Optional[_Union[DeploymentView, str]]=...) -> None:
        ...

class RemoveDeploymentRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListDeploymentsRequest(_message.Message):
    __slots__ = ('parent', 'filter', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., filter: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListDeploymentsResponse(_message.Message):
    __slots__ = ('deployments', 'next_page_token')
    DEPLOYMENTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    deployments: _containers.RepeatedCompositeFieldContainer[Deployment]
    next_page_token: str

    def __init__(self, deployments: _Optional[_Iterable[_Union[Deployment, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class ListDeploymentRevisionsRequest(_message.Message):
    __slots__ = ('name', 'page_size', 'page_token')
    NAME_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    name: str
    page_size: int
    page_token: str

    def __init__(self, name: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListDeploymentRevisionsResponse(_message.Message):
    __slots__ = ('deployments', 'next_page_token')
    DEPLOYMENTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    deployments: _containers.RepeatedCompositeFieldContainer[Deployment]
    next_page_token: str

    def __init__(self, deployments: _Optional[_Iterable[_Union[Deployment, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class SearchDeploymentRevisionsRequest(_message.Message):
    __slots__ = ('parent', 'query', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    query: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., query: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class SearchDeploymentRevisionsResponse(_message.Message):
    __slots__ = ('deployments', 'next_page_token')
    DEPLOYMENTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    deployments: _containers.RepeatedCompositeFieldContainer[Deployment]
    next_page_token: str

    def __init__(self, deployments: _Optional[_Iterable[_Union[Deployment, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class DiscardDeploymentChangesRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class DiscardDeploymentChangesResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class ApplyDeploymentRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ComputeDeploymentStatusRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ComputeDeploymentStatusResponse(_message.Message):
    __slots__ = ('name', 'aggregated_status', 'resource_statuses')
    NAME_FIELD_NUMBER: _ClassVar[int]
    AGGREGATED_STATUS_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_STATUSES_FIELD_NUMBER: _ClassVar[int]
    name: str
    aggregated_status: Status
    resource_statuses: _containers.RepeatedCompositeFieldContainer[ResourceStatus]

    def __init__(self, name: _Optional[str]=..., aggregated_status: _Optional[_Union[Status, str]]=..., resource_statuses: _Optional[_Iterable[_Union[ResourceStatus, _Mapping]]]=...) -> None:
        ...

class RollbackDeploymentRequest(_message.Message):
    __slots__ = ('name', 'revision_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    revision_id: str

    def __init__(self, name: _Optional[str]=..., revision_id: _Optional[str]=...) -> None:
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

class GetHydratedDeploymentRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListHydratedDeploymentsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListHydratedDeploymentsResponse(_message.Message):
    __slots__ = ('hydrated_deployments', 'next_page_token')
    HYDRATED_DEPLOYMENTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    hydrated_deployments: _containers.RepeatedCompositeFieldContainer[HydratedDeployment]
    next_page_token: str

    def __init__(self, hydrated_deployments: _Optional[_Iterable[_Union[HydratedDeployment, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class UpdateHydratedDeploymentRequest(_message.Message):
    __slots__ = ('hydrated_deployment', 'update_mask')
    HYDRATED_DEPLOYMENT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    hydrated_deployment: HydratedDeployment
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, hydrated_deployment: _Optional[_Union[HydratedDeployment, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class ApplyHydratedDeploymentRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ManagementConfig(_message.Message):
    __slots__ = ('standard_management_config', 'full_management_config')
    STANDARD_MANAGEMENT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    FULL_MANAGEMENT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    standard_management_config: StandardManagementConfig
    full_management_config: FullManagementConfig

    def __init__(self, standard_management_config: _Optional[_Union[StandardManagementConfig, _Mapping]]=..., full_management_config: _Optional[_Union[FullManagementConfig, _Mapping]]=...) -> None:
        ...

class StandardManagementConfig(_message.Message):
    __slots__ = ('network', 'subnet', 'master_ipv4_cidr_block', 'cluster_cidr_block', 'services_cidr_block', 'cluster_named_range', 'services_named_range', 'master_authorized_networks_config')
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    SUBNET_FIELD_NUMBER: _ClassVar[int]
    MASTER_IPV4_CIDR_BLOCK_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_CIDR_BLOCK_FIELD_NUMBER: _ClassVar[int]
    SERVICES_CIDR_BLOCK_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_NAMED_RANGE_FIELD_NUMBER: _ClassVar[int]
    SERVICES_NAMED_RANGE_FIELD_NUMBER: _ClassVar[int]
    MASTER_AUTHORIZED_NETWORKS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    network: str
    subnet: str
    master_ipv4_cidr_block: str
    cluster_cidr_block: str
    services_cidr_block: str
    cluster_named_range: str
    services_named_range: str
    master_authorized_networks_config: MasterAuthorizedNetworksConfig

    def __init__(self, network: _Optional[str]=..., subnet: _Optional[str]=..., master_ipv4_cidr_block: _Optional[str]=..., cluster_cidr_block: _Optional[str]=..., services_cidr_block: _Optional[str]=..., cluster_named_range: _Optional[str]=..., services_named_range: _Optional[str]=..., master_authorized_networks_config: _Optional[_Union[MasterAuthorizedNetworksConfig, _Mapping]]=...) -> None:
        ...

class FullManagementConfig(_message.Message):
    __slots__ = ('network', 'subnet', 'master_ipv4_cidr_block', 'cluster_cidr_block', 'services_cidr_block', 'cluster_named_range', 'services_named_range', 'master_authorized_networks_config')
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    SUBNET_FIELD_NUMBER: _ClassVar[int]
    MASTER_IPV4_CIDR_BLOCK_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_CIDR_BLOCK_FIELD_NUMBER: _ClassVar[int]
    SERVICES_CIDR_BLOCK_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_NAMED_RANGE_FIELD_NUMBER: _ClassVar[int]
    SERVICES_NAMED_RANGE_FIELD_NUMBER: _ClassVar[int]
    MASTER_AUTHORIZED_NETWORKS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    network: str
    subnet: str
    master_ipv4_cidr_block: str
    cluster_cidr_block: str
    services_cidr_block: str
    cluster_named_range: str
    services_named_range: str
    master_authorized_networks_config: MasterAuthorizedNetworksConfig

    def __init__(self, network: _Optional[str]=..., subnet: _Optional[str]=..., master_ipv4_cidr_block: _Optional[str]=..., cluster_cidr_block: _Optional[str]=..., services_cidr_block: _Optional[str]=..., cluster_named_range: _Optional[str]=..., services_named_range: _Optional[str]=..., master_authorized_networks_config: _Optional[_Union[MasterAuthorizedNetworksConfig, _Mapping]]=...) -> None:
        ...

class MasterAuthorizedNetworksConfig(_message.Message):
    __slots__ = ('cidr_blocks',)

    class CidrBlock(_message.Message):
        __slots__ = ('display_name', 'cidr_block')
        DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
        CIDR_BLOCK_FIELD_NUMBER: _ClassVar[int]
        display_name: str
        cidr_block: str

        def __init__(self, display_name: _Optional[str]=..., cidr_block: _Optional[str]=...) -> None:
            ...
    CIDR_BLOCKS_FIELD_NUMBER: _ClassVar[int]
    cidr_blocks: _containers.RepeatedCompositeFieldContainer[MasterAuthorizedNetworksConfig.CidrBlock]

    def __init__(self, cidr_blocks: _Optional[_Iterable[_Union[MasterAuthorizedNetworksConfig.CidrBlock, _Mapping]]]=...) -> None:
        ...

class File(_message.Message):
    __slots__ = ('path', 'content', 'deleted', 'editable')
    PATH_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    DELETED_FIELD_NUMBER: _ClassVar[int]
    EDITABLE_FIELD_NUMBER: _ClassVar[int]
    path: str
    content: str
    deleted: bool
    editable: bool

    def __init__(self, path: _Optional[str]=..., content: _Optional[str]=..., deleted: bool=..., editable: bool=...) -> None:
        ...

class ResourceStatus(_message.Message):
    __slots__ = ('name', 'resource_namespace', 'group', 'version', 'kind', 'resource_type', 'status', 'nf_deploy_status')
    NAME_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    NF_DEPLOY_STATUS_FIELD_NUMBER: _ClassVar[int]
    name: str
    resource_namespace: str
    group: str
    version: str
    kind: str
    resource_type: ResourceType
    status: Status
    nf_deploy_status: NFDeployStatus

    def __init__(self, name: _Optional[str]=..., resource_namespace: _Optional[str]=..., group: _Optional[str]=..., version: _Optional[str]=..., kind: _Optional[str]=..., resource_type: _Optional[_Union[ResourceType, str]]=..., status: _Optional[_Union[Status, str]]=..., nf_deploy_status: _Optional[_Union[NFDeployStatus, _Mapping]]=...) -> None:
        ...

class NFDeployStatus(_message.Message):
    __slots__ = ('targeted_nfs', 'ready_nfs', 'sites')
    TARGETED_NFS_FIELD_NUMBER: _ClassVar[int]
    READY_NFS_FIELD_NUMBER: _ClassVar[int]
    SITES_FIELD_NUMBER: _ClassVar[int]
    targeted_nfs: int
    ready_nfs: int
    sites: _containers.RepeatedCompositeFieldContainer[NFDeploySiteStatus]

    def __init__(self, targeted_nfs: _Optional[int]=..., ready_nfs: _Optional[int]=..., sites: _Optional[_Iterable[_Union[NFDeploySiteStatus, _Mapping]]]=...) -> None:
        ...

class NFDeploySiteStatus(_message.Message):
    __slots__ = ('site', 'pending_deletion', 'hydration', 'workload')
    SITE_FIELD_NUMBER: _ClassVar[int]
    PENDING_DELETION_FIELD_NUMBER: _ClassVar[int]
    HYDRATION_FIELD_NUMBER: _ClassVar[int]
    WORKLOAD_FIELD_NUMBER: _ClassVar[int]
    site: str
    pending_deletion: bool
    hydration: HydrationStatus
    workload: WorkloadStatus

    def __init__(self, site: _Optional[str]=..., pending_deletion: bool=..., hydration: _Optional[_Union[HydrationStatus, _Mapping]]=..., workload: _Optional[_Union[WorkloadStatus, _Mapping]]=...) -> None:
        ...

class HydrationStatus(_message.Message):
    __slots__ = ('site_version', 'status')
    SITE_VERSION_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    site_version: SiteVersion
    status: str

    def __init__(self, site_version: _Optional[_Union[SiteVersion, _Mapping]]=..., status: _Optional[str]=...) -> None:
        ...

class SiteVersion(_message.Message):
    __slots__ = ('nf_vendor', 'nf_type', 'nf_version')
    NF_VENDOR_FIELD_NUMBER: _ClassVar[int]
    NF_TYPE_FIELD_NUMBER: _ClassVar[int]
    NF_VERSION_FIELD_NUMBER: _ClassVar[int]
    nf_vendor: str
    nf_type: str
    nf_version: str

    def __init__(self, nf_vendor: _Optional[str]=..., nf_type: _Optional[str]=..., nf_version: _Optional[str]=...) -> None:
        ...

class WorkloadStatus(_message.Message):
    __slots__ = ('site_version', 'status')
    SITE_VERSION_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    site_version: SiteVersion
    status: str

    def __init__(self, site_version: _Optional[_Union[SiteVersion, _Mapping]]=..., status: _Optional[str]=...) -> None:
        ...