from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.type import date_pb2 as _date_pb2
from google.type import dayofweek_pb2 as _dayofweek_pb2
from google.type import timeofday_pb2 as _timeofday_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class SkaffoldSupportState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SKAFFOLD_SUPPORT_STATE_UNSPECIFIED: _ClassVar[SkaffoldSupportState]
    SKAFFOLD_SUPPORT_STATE_SUPPORTED: _ClassVar[SkaffoldSupportState]
    SKAFFOLD_SUPPORT_STATE_MAINTENANCE_MODE: _ClassVar[SkaffoldSupportState]
    SKAFFOLD_SUPPORT_STATE_UNSUPPORTED: _ClassVar[SkaffoldSupportState]

class BackoffMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BACKOFF_MODE_UNSPECIFIED: _ClassVar[BackoffMode]
    BACKOFF_MODE_LINEAR: _ClassVar[BackoffMode]
    BACKOFF_MODE_EXPONENTIAL: _ClassVar[BackoffMode]

class RepairState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    REPAIR_STATE_UNSPECIFIED: _ClassVar[RepairState]
    REPAIR_STATE_SUCCEEDED: _ClassVar[RepairState]
    REPAIR_STATE_CANCELLED: _ClassVar[RepairState]
    REPAIR_STATE_FAILED: _ClassVar[RepairState]
    REPAIR_STATE_IN_PROGRESS: _ClassVar[RepairState]
    REPAIR_STATE_PENDING: _ClassVar[RepairState]
    REPAIR_STATE_ABORTED: _ClassVar[RepairState]
SKAFFOLD_SUPPORT_STATE_UNSPECIFIED: SkaffoldSupportState
SKAFFOLD_SUPPORT_STATE_SUPPORTED: SkaffoldSupportState
SKAFFOLD_SUPPORT_STATE_MAINTENANCE_MODE: SkaffoldSupportState
SKAFFOLD_SUPPORT_STATE_UNSUPPORTED: SkaffoldSupportState
BACKOFF_MODE_UNSPECIFIED: BackoffMode
BACKOFF_MODE_LINEAR: BackoffMode
BACKOFF_MODE_EXPONENTIAL: BackoffMode
REPAIR_STATE_UNSPECIFIED: RepairState
REPAIR_STATE_SUCCEEDED: RepairState
REPAIR_STATE_CANCELLED: RepairState
REPAIR_STATE_FAILED: RepairState
REPAIR_STATE_IN_PROGRESS: RepairState
REPAIR_STATE_PENDING: RepairState
REPAIR_STATE_ABORTED: RepairState

class DeliveryPipeline(_message.Message):
    __slots__ = ('name', 'uid', 'description', 'annotations', 'labels', 'create_time', 'update_time', 'serial_pipeline', 'condition', 'etag', 'suspended')

    class AnnotationsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    SERIAL_PIPELINE_FIELD_NUMBER: _ClassVar[int]
    CONDITION_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    SUSPENDED_FIELD_NUMBER: _ClassVar[int]
    name: str
    uid: str
    description: str
    annotations: _containers.ScalarMap[str, str]
    labels: _containers.ScalarMap[str, str]
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    serial_pipeline: SerialPipeline
    condition: PipelineCondition
    etag: str
    suspended: bool

    def __init__(self, name: _Optional[str]=..., uid: _Optional[str]=..., description: _Optional[str]=..., annotations: _Optional[_Mapping[str, str]]=..., labels: _Optional[_Mapping[str, str]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., serial_pipeline: _Optional[_Union[SerialPipeline, _Mapping]]=..., condition: _Optional[_Union[PipelineCondition, _Mapping]]=..., etag: _Optional[str]=..., suspended: bool=...) -> None:
        ...

class SerialPipeline(_message.Message):
    __slots__ = ('stages',)
    STAGES_FIELD_NUMBER: _ClassVar[int]
    stages: _containers.RepeatedCompositeFieldContainer[Stage]

    def __init__(self, stages: _Optional[_Iterable[_Union[Stage, _Mapping]]]=...) -> None:
        ...

class Stage(_message.Message):
    __slots__ = ('target_id', 'profiles', 'strategy', 'deploy_parameters')
    TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    PROFILES_FIELD_NUMBER: _ClassVar[int]
    STRATEGY_FIELD_NUMBER: _ClassVar[int]
    DEPLOY_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    target_id: str
    profiles: _containers.RepeatedScalarFieldContainer[str]
    strategy: Strategy
    deploy_parameters: _containers.RepeatedCompositeFieldContainer[DeployParameters]

    def __init__(self, target_id: _Optional[str]=..., profiles: _Optional[_Iterable[str]]=..., strategy: _Optional[_Union[Strategy, _Mapping]]=..., deploy_parameters: _Optional[_Iterable[_Union[DeployParameters, _Mapping]]]=...) -> None:
        ...

class DeployParameters(_message.Message):
    __slots__ = ('values', 'match_target_labels')

    class ValuesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...

    class MatchTargetLabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    VALUES_FIELD_NUMBER: _ClassVar[int]
    MATCH_TARGET_LABELS_FIELD_NUMBER: _ClassVar[int]
    values: _containers.ScalarMap[str, str]
    match_target_labels: _containers.ScalarMap[str, str]

    def __init__(self, values: _Optional[_Mapping[str, str]]=..., match_target_labels: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class Strategy(_message.Message):
    __slots__ = ('standard', 'canary')
    STANDARD_FIELD_NUMBER: _ClassVar[int]
    CANARY_FIELD_NUMBER: _ClassVar[int]
    standard: Standard
    canary: Canary

    def __init__(self, standard: _Optional[_Union[Standard, _Mapping]]=..., canary: _Optional[_Union[Canary, _Mapping]]=...) -> None:
        ...

class Predeploy(_message.Message):
    __slots__ = ('actions',)
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    actions: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, actions: _Optional[_Iterable[str]]=...) -> None:
        ...

class Postdeploy(_message.Message):
    __slots__ = ('actions',)
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    actions: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, actions: _Optional[_Iterable[str]]=...) -> None:
        ...

class Standard(_message.Message):
    __slots__ = ('verify', 'predeploy', 'postdeploy')
    VERIFY_FIELD_NUMBER: _ClassVar[int]
    PREDEPLOY_FIELD_NUMBER: _ClassVar[int]
    POSTDEPLOY_FIELD_NUMBER: _ClassVar[int]
    verify: bool
    predeploy: Predeploy
    postdeploy: Postdeploy

    def __init__(self, verify: bool=..., predeploy: _Optional[_Union[Predeploy, _Mapping]]=..., postdeploy: _Optional[_Union[Postdeploy, _Mapping]]=...) -> None:
        ...

class Canary(_message.Message):
    __slots__ = ('runtime_config', 'canary_deployment', 'custom_canary_deployment')
    RUNTIME_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CANARY_DEPLOYMENT_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_CANARY_DEPLOYMENT_FIELD_NUMBER: _ClassVar[int]
    runtime_config: RuntimeConfig
    canary_deployment: CanaryDeployment
    custom_canary_deployment: CustomCanaryDeployment

    def __init__(self, runtime_config: _Optional[_Union[RuntimeConfig, _Mapping]]=..., canary_deployment: _Optional[_Union[CanaryDeployment, _Mapping]]=..., custom_canary_deployment: _Optional[_Union[CustomCanaryDeployment, _Mapping]]=...) -> None:
        ...

class CanaryDeployment(_message.Message):
    __slots__ = ('percentages', 'verify', 'predeploy', 'postdeploy')
    PERCENTAGES_FIELD_NUMBER: _ClassVar[int]
    VERIFY_FIELD_NUMBER: _ClassVar[int]
    PREDEPLOY_FIELD_NUMBER: _ClassVar[int]
    POSTDEPLOY_FIELD_NUMBER: _ClassVar[int]
    percentages: _containers.RepeatedScalarFieldContainer[int]
    verify: bool
    predeploy: Predeploy
    postdeploy: Postdeploy

    def __init__(self, percentages: _Optional[_Iterable[int]]=..., verify: bool=..., predeploy: _Optional[_Union[Predeploy, _Mapping]]=..., postdeploy: _Optional[_Union[Postdeploy, _Mapping]]=...) -> None:
        ...

class CustomCanaryDeployment(_message.Message):
    __slots__ = ('phase_configs',)

    class PhaseConfig(_message.Message):
        __slots__ = ('phase_id', 'percentage', 'profiles', 'verify', 'predeploy', 'postdeploy')
        PHASE_ID_FIELD_NUMBER: _ClassVar[int]
        PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
        PROFILES_FIELD_NUMBER: _ClassVar[int]
        VERIFY_FIELD_NUMBER: _ClassVar[int]
        PREDEPLOY_FIELD_NUMBER: _ClassVar[int]
        POSTDEPLOY_FIELD_NUMBER: _ClassVar[int]
        phase_id: str
        percentage: int
        profiles: _containers.RepeatedScalarFieldContainer[str]
        verify: bool
        predeploy: Predeploy
        postdeploy: Postdeploy

        def __init__(self, phase_id: _Optional[str]=..., percentage: _Optional[int]=..., profiles: _Optional[_Iterable[str]]=..., verify: bool=..., predeploy: _Optional[_Union[Predeploy, _Mapping]]=..., postdeploy: _Optional[_Union[Postdeploy, _Mapping]]=...) -> None:
            ...
    PHASE_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    phase_configs: _containers.RepeatedCompositeFieldContainer[CustomCanaryDeployment.PhaseConfig]

    def __init__(self, phase_configs: _Optional[_Iterable[_Union[CustomCanaryDeployment.PhaseConfig, _Mapping]]]=...) -> None:
        ...

class KubernetesConfig(_message.Message):
    __slots__ = ('gateway_service_mesh', 'service_networking')

    class GatewayServiceMesh(_message.Message):
        __slots__ = ('http_route', 'service', 'deployment', 'route_update_wait_time', 'stable_cutback_duration', 'pod_selector_label', 'route_destinations')

        class RouteDestinations(_message.Message):
            __slots__ = ('destination_ids', 'propagate_service')
            DESTINATION_IDS_FIELD_NUMBER: _ClassVar[int]
            PROPAGATE_SERVICE_FIELD_NUMBER: _ClassVar[int]
            destination_ids: _containers.RepeatedScalarFieldContainer[str]
            propagate_service: bool

            def __init__(self, destination_ids: _Optional[_Iterable[str]]=..., propagate_service: bool=...) -> None:
                ...
        HTTP_ROUTE_FIELD_NUMBER: _ClassVar[int]
        SERVICE_FIELD_NUMBER: _ClassVar[int]
        DEPLOYMENT_FIELD_NUMBER: _ClassVar[int]
        ROUTE_UPDATE_WAIT_TIME_FIELD_NUMBER: _ClassVar[int]
        STABLE_CUTBACK_DURATION_FIELD_NUMBER: _ClassVar[int]
        POD_SELECTOR_LABEL_FIELD_NUMBER: _ClassVar[int]
        ROUTE_DESTINATIONS_FIELD_NUMBER: _ClassVar[int]
        http_route: str
        service: str
        deployment: str
        route_update_wait_time: _duration_pb2.Duration
        stable_cutback_duration: _duration_pb2.Duration
        pod_selector_label: str
        route_destinations: KubernetesConfig.GatewayServiceMesh.RouteDestinations

        def __init__(self, http_route: _Optional[str]=..., service: _Optional[str]=..., deployment: _Optional[str]=..., route_update_wait_time: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., stable_cutback_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., pod_selector_label: _Optional[str]=..., route_destinations: _Optional[_Union[KubernetesConfig.GatewayServiceMesh.RouteDestinations, _Mapping]]=...) -> None:
            ...

    class ServiceNetworking(_message.Message):
        __slots__ = ('service', 'deployment', 'disable_pod_overprovisioning', 'pod_selector_label')
        SERVICE_FIELD_NUMBER: _ClassVar[int]
        DEPLOYMENT_FIELD_NUMBER: _ClassVar[int]
        DISABLE_POD_OVERPROVISIONING_FIELD_NUMBER: _ClassVar[int]
        POD_SELECTOR_LABEL_FIELD_NUMBER: _ClassVar[int]
        service: str
        deployment: str
        disable_pod_overprovisioning: bool
        pod_selector_label: str

        def __init__(self, service: _Optional[str]=..., deployment: _Optional[str]=..., disable_pod_overprovisioning: bool=..., pod_selector_label: _Optional[str]=...) -> None:
            ...
    GATEWAY_SERVICE_MESH_FIELD_NUMBER: _ClassVar[int]
    SERVICE_NETWORKING_FIELD_NUMBER: _ClassVar[int]
    gateway_service_mesh: KubernetesConfig.GatewayServiceMesh
    service_networking: KubernetesConfig.ServiceNetworking

    def __init__(self, gateway_service_mesh: _Optional[_Union[KubernetesConfig.GatewayServiceMesh, _Mapping]]=..., service_networking: _Optional[_Union[KubernetesConfig.ServiceNetworking, _Mapping]]=...) -> None:
        ...

class CloudRunConfig(_message.Message):
    __slots__ = ('automatic_traffic_control', 'canary_revision_tags', 'prior_revision_tags', 'stable_revision_tags')
    AUTOMATIC_TRAFFIC_CONTROL_FIELD_NUMBER: _ClassVar[int]
    CANARY_REVISION_TAGS_FIELD_NUMBER: _ClassVar[int]
    PRIOR_REVISION_TAGS_FIELD_NUMBER: _ClassVar[int]
    STABLE_REVISION_TAGS_FIELD_NUMBER: _ClassVar[int]
    automatic_traffic_control: bool
    canary_revision_tags: _containers.RepeatedScalarFieldContainer[str]
    prior_revision_tags: _containers.RepeatedScalarFieldContainer[str]
    stable_revision_tags: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, automatic_traffic_control: bool=..., canary_revision_tags: _Optional[_Iterable[str]]=..., prior_revision_tags: _Optional[_Iterable[str]]=..., stable_revision_tags: _Optional[_Iterable[str]]=...) -> None:
        ...

class RuntimeConfig(_message.Message):
    __slots__ = ('kubernetes', 'cloud_run')
    KUBERNETES_FIELD_NUMBER: _ClassVar[int]
    CLOUD_RUN_FIELD_NUMBER: _ClassVar[int]
    kubernetes: KubernetesConfig
    cloud_run: CloudRunConfig

    def __init__(self, kubernetes: _Optional[_Union[KubernetesConfig, _Mapping]]=..., cloud_run: _Optional[_Union[CloudRunConfig, _Mapping]]=...) -> None:
        ...

class PipelineReadyCondition(_message.Message):
    __slots__ = ('status', 'update_time')
    STATUS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    status: bool
    update_time: _timestamp_pb2.Timestamp

    def __init__(self, status: bool=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class TargetsPresentCondition(_message.Message):
    __slots__ = ('status', 'missing_targets', 'update_time')
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MISSING_TARGETS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    status: bool
    missing_targets: _containers.RepeatedScalarFieldContainer[str]
    update_time: _timestamp_pb2.Timestamp

    def __init__(self, status: bool=..., missing_targets: _Optional[_Iterable[str]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class TargetsTypeCondition(_message.Message):
    __slots__ = ('status', 'error_details')
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_DETAILS_FIELD_NUMBER: _ClassVar[int]
    status: bool
    error_details: str

    def __init__(self, status: bool=..., error_details: _Optional[str]=...) -> None:
        ...

class PipelineCondition(_message.Message):
    __slots__ = ('pipeline_ready_condition', 'targets_present_condition', 'targets_type_condition')
    PIPELINE_READY_CONDITION_FIELD_NUMBER: _ClassVar[int]
    TARGETS_PRESENT_CONDITION_FIELD_NUMBER: _ClassVar[int]
    TARGETS_TYPE_CONDITION_FIELD_NUMBER: _ClassVar[int]
    pipeline_ready_condition: PipelineReadyCondition
    targets_present_condition: TargetsPresentCondition
    targets_type_condition: TargetsTypeCondition

    def __init__(self, pipeline_ready_condition: _Optional[_Union[PipelineReadyCondition, _Mapping]]=..., targets_present_condition: _Optional[_Union[TargetsPresentCondition, _Mapping]]=..., targets_type_condition: _Optional[_Union[TargetsTypeCondition, _Mapping]]=...) -> None:
        ...

class ListDeliveryPipelinesRequest(_message.Message):
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

class ListDeliveryPipelinesResponse(_message.Message):
    __slots__ = ('delivery_pipelines', 'next_page_token', 'unreachable')
    DELIVERY_PIPELINES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    delivery_pipelines: _containers.RepeatedCompositeFieldContainer[DeliveryPipeline]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, delivery_pipelines: _Optional[_Iterable[_Union[DeliveryPipeline, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetDeliveryPipelineRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateDeliveryPipelineRequest(_message.Message):
    __slots__ = ('parent', 'delivery_pipeline_id', 'delivery_pipeline', 'request_id', 'validate_only')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_PIPELINE_ID_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_PIPELINE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    delivery_pipeline_id: str
    delivery_pipeline: DeliveryPipeline
    request_id: str
    validate_only: bool

    def __init__(self, parent: _Optional[str]=..., delivery_pipeline_id: _Optional[str]=..., delivery_pipeline: _Optional[_Union[DeliveryPipeline, _Mapping]]=..., request_id: _Optional[str]=..., validate_only: bool=...) -> None:
        ...

class UpdateDeliveryPipelineRequest(_message.Message):
    __slots__ = ('update_mask', 'delivery_pipeline', 'request_id', 'allow_missing', 'validate_only')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_PIPELINE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MISSING_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    delivery_pipeline: DeliveryPipeline
    request_id: str
    allow_missing: bool
    validate_only: bool

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., delivery_pipeline: _Optional[_Union[DeliveryPipeline, _Mapping]]=..., request_id: _Optional[str]=..., allow_missing: bool=..., validate_only: bool=...) -> None:
        ...

class DeleteDeliveryPipelineRequest(_message.Message):
    __slots__ = ('name', 'request_id', 'allow_missing', 'validate_only', 'force', 'etag')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MISSING_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str
    allow_missing: bool
    validate_only: bool
    force: bool
    etag: str

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=..., allow_missing: bool=..., validate_only: bool=..., force: bool=..., etag: _Optional[str]=...) -> None:
        ...

class RollbackTargetConfig(_message.Message):
    __slots__ = ('rollout', 'starting_phase_id')
    ROLLOUT_FIELD_NUMBER: _ClassVar[int]
    STARTING_PHASE_ID_FIELD_NUMBER: _ClassVar[int]
    rollout: Rollout
    starting_phase_id: str

    def __init__(self, rollout: _Optional[_Union[Rollout, _Mapping]]=..., starting_phase_id: _Optional[str]=...) -> None:
        ...

class RollbackTargetRequest(_message.Message):
    __slots__ = ('name', 'target_id', 'rollout_id', 'release_id', 'rollout_to_roll_back', 'rollback_config', 'validate_only', 'override_deploy_policy')
    NAME_FIELD_NUMBER: _ClassVar[int]
    TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    ROLLOUT_ID_FIELD_NUMBER: _ClassVar[int]
    RELEASE_ID_FIELD_NUMBER: _ClassVar[int]
    ROLLOUT_TO_ROLL_BACK_FIELD_NUMBER: _ClassVar[int]
    ROLLBACK_CONFIG_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    OVERRIDE_DEPLOY_POLICY_FIELD_NUMBER: _ClassVar[int]
    name: str
    target_id: str
    rollout_id: str
    release_id: str
    rollout_to_roll_back: str
    rollback_config: RollbackTargetConfig
    validate_only: bool
    override_deploy_policy: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, name: _Optional[str]=..., target_id: _Optional[str]=..., rollout_id: _Optional[str]=..., release_id: _Optional[str]=..., rollout_to_roll_back: _Optional[str]=..., rollback_config: _Optional[_Union[RollbackTargetConfig, _Mapping]]=..., validate_only: bool=..., override_deploy_policy: _Optional[_Iterable[str]]=...) -> None:
        ...

class RollbackTargetResponse(_message.Message):
    __slots__ = ('rollback_config',)
    ROLLBACK_CONFIG_FIELD_NUMBER: _ClassVar[int]
    rollback_config: RollbackTargetConfig

    def __init__(self, rollback_config: _Optional[_Union[RollbackTargetConfig, _Mapping]]=...) -> None:
        ...

class Target(_message.Message):
    __slots__ = ('name', 'target_id', 'uid', 'description', 'annotations', 'labels', 'require_approval', 'create_time', 'update_time', 'gke', 'anthos_cluster', 'run', 'multi_target', 'custom_target', 'associated_entities', 'etag', 'execution_configs', 'deploy_parameters')

    class AnnotationsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...

    class AssociatedEntitiesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: AssociatedEntities

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[AssociatedEntities, _Mapping]]=...) -> None:
            ...

    class DeployParametersEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    REQUIRE_APPROVAL_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    GKE_FIELD_NUMBER: _ClassVar[int]
    ANTHOS_CLUSTER_FIELD_NUMBER: _ClassVar[int]
    RUN_FIELD_NUMBER: _ClassVar[int]
    MULTI_TARGET_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_TARGET_FIELD_NUMBER: _ClassVar[int]
    ASSOCIATED_ENTITIES_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    DEPLOY_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    name: str
    target_id: str
    uid: str
    description: str
    annotations: _containers.ScalarMap[str, str]
    labels: _containers.ScalarMap[str, str]
    require_approval: bool
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    gke: GkeCluster
    anthos_cluster: AnthosCluster
    run: CloudRunLocation
    multi_target: MultiTarget
    custom_target: CustomTarget
    associated_entities: _containers.MessageMap[str, AssociatedEntities]
    etag: str
    execution_configs: _containers.RepeatedCompositeFieldContainer[ExecutionConfig]
    deploy_parameters: _containers.ScalarMap[str, str]

    def __init__(self, name: _Optional[str]=..., target_id: _Optional[str]=..., uid: _Optional[str]=..., description: _Optional[str]=..., annotations: _Optional[_Mapping[str, str]]=..., labels: _Optional[_Mapping[str, str]]=..., require_approval: bool=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., gke: _Optional[_Union[GkeCluster, _Mapping]]=..., anthos_cluster: _Optional[_Union[AnthosCluster, _Mapping]]=..., run: _Optional[_Union[CloudRunLocation, _Mapping]]=..., multi_target: _Optional[_Union[MultiTarget, _Mapping]]=..., custom_target: _Optional[_Union[CustomTarget, _Mapping]]=..., associated_entities: _Optional[_Mapping[str, AssociatedEntities]]=..., etag: _Optional[str]=..., execution_configs: _Optional[_Iterable[_Union[ExecutionConfig, _Mapping]]]=..., deploy_parameters: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class ExecutionConfig(_message.Message):
    __slots__ = ('usages', 'default_pool', 'private_pool', 'worker_pool', 'service_account', 'artifact_storage', 'execution_timeout', 'verbose')

    class ExecutionEnvironmentUsage(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        EXECUTION_ENVIRONMENT_USAGE_UNSPECIFIED: _ClassVar[ExecutionConfig.ExecutionEnvironmentUsage]
        RENDER: _ClassVar[ExecutionConfig.ExecutionEnvironmentUsage]
        DEPLOY: _ClassVar[ExecutionConfig.ExecutionEnvironmentUsage]
        VERIFY: _ClassVar[ExecutionConfig.ExecutionEnvironmentUsage]
        PREDEPLOY: _ClassVar[ExecutionConfig.ExecutionEnvironmentUsage]
        POSTDEPLOY: _ClassVar[ExecutionConfig.ExecutionEnvironmentUsage]
    EXECUTION_ENVIRONMENT_USAGE_UNSPECIFIED: ExecutionConfig.ExecutionEnvironmentUsage
    RENDER: ExecutionConfig.ExecutionEnvironmentUsage
    DEPLOY: ExecutionConfig.ExecutionEnvironmentUsage
    VERIFY: ExecutionConfig.ExecutionEnvironmentUsage
    PREDEPLOY: ExecutionConfig.ExecutionEnvironmentUsage
    POSTDEPLOY: ExecutionConfig.ExecutionEnvironmentUsage
    USAGES_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_POOL_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_POOL_FIELD_NUMBER: _ClassVar[int]
    WORKER_POOL_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    ARTIFACT_STORAGE_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    VERBOSE_FIELD_NUMBER: _ClassVar[int]
    usages: _containers.RepeatedScalarFieldContainer[ExecutionConfig.ExecutionEnvironmentUsage]
    default_pool: DefaultPool
    private_pool: PrivatePool
    worker_pool: str
    service_account: str
    artifact_storage: str
    execution_timeout: _duration_pb2.Duration
    verbose: bool

    def __init__(self, usages: _Optional[_Iterable[_Union[ExecutionConfig.ExecutionEnvironmentUsage, str]]]=..., default_pool: _Optional[_Union[DefaultPool, _Mapping]]=..., private_pool: _Optional[_Union[PrivatePool, _Mapping]]=..., worker_pool: _Optional[str]=..., service_account: _Optional[str]=..., artifact_storage: _Optional[str]=..., execution_timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., verbose: bool=...) -> None:
        ...

class DefaultPool(_message.Message):
    __slots__ = ('service_account', 'artifact_storage')
    SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    ARTIFACT_STORAGE_FIELD_NUMBER: _ClassVar[int]
    service_account: str
    artifact_storage: str

    def __init__(self, service_account: _Optional[str]=..., artifact_storage: _Optional[str]=...) -> None:
        ...

class PrivatePool(_message.Message):
    __slots__ = ('worker_pool', 'service_account', 'artifact_storage')
    WORKER_POOL_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    ARTIFACT_STORAGE_FIELD_NUMBER: _ClassVar[int]
    worker_pool: str
    service_account: str
    artifact_storage: str

    def __init__(self, worker_pool: _Optional[str]=..., service_account: _Optional[str]=..., artifact_storage: _Optional[str]=...) -> None:
        ...

class GkeCluster(_message.Message):
    __slots__ = ('cluster', 'internal_ip', 'proxy_url', 'dns_endpoint')
    CLUSTER_FIELD_NUMBER: _ClassVar[int]
    INTERNAL_IP_FIELD_NUMBER: _ClassVar[int]
    PROXY_URL_FIELD_NUMBER: _ClassVar[int]
    DNS_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    cluster: str
    internal_ip: bool
    proxy_url: str
    dns_endpoint: bool

    def __init__(self, cluster: _Optional[str]=..., internal_ip: bool=..., proxy_url: _Optional[str]=..., dns_endpoint: bool=...) -> None:
        ...

class AnthosCluster(_message.Message):
    __slots__ = ('membership',)
    MEMBERSHIP_FIELD_NUMBER: _ClassVar[int]
    membership: str

    def __init__(self, membership: _Optional[str]=...) -> None:
        ...

class CloudRunLocation(_message.Message):
    __slots__ = ('location',)
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    location: str

    def __init__(self, location: _Optional[str]=...) -> None:
        ...

class MultiTarget(_message.Message):
    __slots__ = ('target_ids',)
    TARGET_IDS_FIELD_NUMBER: _ClassVar[int]
    target_ids: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, target_ids: _Optional[_Iterable[str]]=...) -> None:
        ...

class CustomTarget(_message.Message):
    __slots__ = ('custom_target_type',)
    CUSTOM_TARGET_TYPE_FIELD_NUMBER: _ClassVar[int]
    custom_target_type: str

    def __init__(self, custom_target_type: _Optional[str]=...) -> None:
        ...

class AssociatedEntities(_message.Message):
    __slots__ = ('gke_clusters', 'anthos_clusters')
    GKE_CLUSTERS_FIELD_NUMBER: _ClassVar[int]
    ANTHOS_CLUSTERS_FIELD_NUMBER: _ClassVar[int]
    gke_clusters: _containers.RepeatedCompositeFieldContainer[GkeCluster]
    anthos_clusters: _containers.RepeatedCompositeFieldContainer[AnthosCluster]

    def __init__(self, gke_clusters: _Optional[_Iterable[_Union[GkeCluster, _Mapping]]]=..., anthos_clusters: _Optional[_Iterable[_Union[AnthosCluster, _Mapping]]]=...) -> None:
        ...

class ListTargetsRequest(_message.Message):
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

class ListTargetsResponse(_message.Message):
    __slots__ = ('targets', 'next_page_token', 'unreachable')
    TARGETS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    targets: _containers.RepeatedCompositeFieldContainer[Target]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, targets: _Optional[_Iterable[_Union[Target, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetTargetRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateTargetRequest(_message.Message):
    __slots__ = ('parent', 'target_id', 'target', 'request_id', 'validate_only')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    target_id: str
    target: Target
    request_id: str
    validate_only: bool

    def __init__(self, parent: _Optional[str]=..., target_id: _Optional[str]=..., target: _Optional[_Union[Target, _Mapping]]=..., request_id: _Optional[str]=..., validate_only: bool=...) -> None:
        ...

class UpdateTargetRequest(_message.Message):
    __slots__ = ('update_mask', 'target', 'request_id', 'allow_missing', 'validate_only')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MISSING_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    target: Target
    request_id: str
    allow_missing: bool
    validate_only: bool

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., target: _Optional[_Union[Target, _Mapping]]=..., request_id: _Optional[str]=..., allow_missing: bool=..., validate_only: bool=...) -> None:
        ...

class DeleteTargetRequest(_message.Message):
    __slots__ = ('name', 'request_id', 'allow_missing', 'validate_only', 'etag')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MISSING_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str
    allow_missing: bool
    validate_only: bool
    etag: str

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=..., allow_missing: bool=..., validate_only: bool=..., etag: _Optional[str]=...) -> None:
        ...

class CustomTargetType(_message.Message):
    __slots__ = ('name', 'custom_target_type_id', 'uid', 'description', 'annotations', 'labels', 'create_time', 'update_time', 'etag', 'custom_actions')

    class AnnotationsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_TARGET_TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_ACTIONS_FIELD_NUMBER: _ClassVar[int]
    name: str
    custom_target_type_id: str
    uid: str
    description: str
    annotations: _containers.ScalarMap[str, str]
    labels: _containers.ScalarMap[str, str]
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    etag: str
    custom_actions: CustomTargetSkaffoldActions

    def __init__(self, name: _Optional[str]=..., custom_target_type_id: _Optional[str]=..., uid: _Optional[str]=..., description: _Optional[str]=..., annotations: _Optional[_Mapping[str, str]]=..., labels: _Optional[_Mapping[str, str]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., etag: _Optional[str]=..., custom_actions: _Optional[_Union[CustomTargetSkaffoldActions, _Mapping]]=...) -> None:
        ...

class CustomTargetSkaffoldActions(_message.Message):
    __slots__ = ('render_action', 'deploy_action', 'include_skaffold_modules')
    RENDER_ACTION_FIELD_NUMBER: _ClassVar[int]
    DEPLOY_ACTION_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_SKAFFOLD_MODULES_FIELD_NUMBER: _ClassVar[int]
    render_action: str
    deploy_action: str
    include_skaffold_modules: _containers.RepeatedCompositeFieldContainer[SkaffoldModules]

    def __init__(self, render_action: _Optional[str]=..., deploy_action: _Optional[str]=..., include_skaffold_modules: _Optional[_Iterable[_Union[SkaffoldModules, _Mapping]]]=...) -> None:
        ...

class SkaffoldModules(_message.Message):
    __slots__ = ('configs', 'git', 'google_cloud_storage', 'google_cloud_build_repo')

    class SkaffoldGitSource(_message.Message):
        __slots__ = ('repo', 'path', 'ref')
        REPO_FIELD_NUMBER: _ClassVar[int]
        PATH_FIELD_NUMBER: _ClassVar[int]
        REF_FIELD_NUMBER: _ClassVar[int]
        repo: str
        path: str
        ref: str

        def __init__(self, repo: _Optional[str]=..., path: _Optional[str]=..., ref: _Optional[str]=...) -> None:
            ...

    class SkaffoldGCSSource(_message.Message):
        __slots__ = ('source', 'path')
        SOURCE_FIELD_NUMBER: _ClassVar[int]
        PATH_FIELD_NUMBER: _ClassVar[int]
        source: str
        path: str

        def __init__(self, source: _Optional[str]=..., path: _Optional[str]=...) -> None:
            ...

    class SkaffoldGCBRepoSource(_message.Message):
        __slots__ = ('repository', 'path', 'ref')
        REPOSITORY_FIELD_NUMBER: _ClassVar[int]
        PATH_FIELD_NUMBER: _ClassVar[int]
        REF_FIELD_NUMBER: _ClassVar[int]
        repository: str
        path: str
        ref: str

        def __init__(self, repository: _Optional[str]=..., path: _Optional[str]=..., ref: _Optional[str]=...) -> None:
            ...
    CONFIGS_FIELD_NUMBER: _ClassVar[int]
    GIT_FIELD_NUMBER: _ClassVar[int]
    GOOGLE_CLOUD_STORAGE_FIELD_NUMBER: _ClassVar[int]
    GOOGLE_CLOUD_BUILD_REPO_FIELD_NUMBER: _ClassVar[int]
    configs: _containers.RepeatedScalarFieldContainer[str]
    git: SkaffoldModules.SkaffoldGitSource
    google_cloud_storage: SkaffoldModules.SkaffoldGCSSource
    google_cloud_build_repo: SkaffoldModules.SkaffoldGCBRepoSource

    def __init__(self, configs: _Optional[_Iterable[str]]=..., git: _Optional[_Union[SkaffoldModules.SkaffoldGitSource, _Mapping]]=..., google_cloud_storage: _Optional[_Union[SkaffoldModules.SkaffoldGCSSource, _Mapping]]=..., google_cloud_build_repo: _Optional[_Union[SkaffoldModules.SkaffoldGCBRepoSource, _Mapping]]=...) -> None:
        ...

class ListCustomTargetTypesRequest(_message.Message):
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

class ListCustomTargetTypesResponse(_message.Message):
    __slots__ = ('custom_target_types', 'next_page_token', 'unreachable')
    CUSTOM_TARGET_TYPES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    custom_target_types: _containers.RepeatedCompositeFieldContainer[CustomTargetType]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, custom_target_types: _Optional[_Iterable[_Union[CustomTargetType, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetCustomTargetTypeRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateCustomTargetTypeRequest(_message.Message):
    __slots__ = ('parent', 'custom_target_type_id', 'custom_target_type', 'request_id', 'validate_only')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_TARGET_TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_TARGET_TYPE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    custom_target_type_id: str
    custom_target_type: CustomTargetType
    request_id: str
    validate_only: bool

    def __init__(self, parent: _Optional[str]=..., custom_target_type_id: _Optional[str]=..., custom_target_type: _Optional[_Union[CustomTargetType, _Mapping]]=..., request_id: _Optional[str]=..., validate_only: bool=...) -> None:
        ...

class UpdateCustomTargetTypeRequest(_message.Message):
    __slots__ = ('update_mask', 'custom_target_type', 'request_id', 'allow_missing', 'validate_only')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_TARGET_TYPE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MISSING_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    custom_target_type: CustomTargetType
    request_id: str
    allow_missing: bool
    validate_only: bool

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., custom_target_type: _Optional[_Union[CustomTargetType, _Mapping]]=..., request_id: _Optional[str]=..., allow_missing: bool=..., validate_only: bool=...) -> None:
        ...

class DeleteCustomTargetTypeRequest(_message.Message):
    __slots__ = ('name', 'request_id', 'allow_missing', 'validate_only', 'etag')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MISSING_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str
    allow_missing: bool
    validate_only: bool
    etag: str

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=..., allow_missing: bool=..., validate_only: bool=..., etag: _Optional[str]=...) -> None:
        ...

class DeployPolicy(_message.Message):
    __slots__ = ('name', 'uid', 'description', 'annotations', 'labels', 'create_time', 'update_time', 'suspended', 'selectors', 'rules', 'etag')

    class Invoker(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        INVOKER_UNSPECIFIED: _ClassVar[DeployPolicy.Invoker]
        USER: _ClassVar[DeployPolicy.Invoker]
        DEPLOY_AUTOMATION: _ClassVar[DeployPolicy.Invoker]
    INVOKER_UNSPECIFIED: DeployPolicy.Invoker
    USER: DeployPolicy.Invoker
    DEPLOY_AUTOMATION: DeployPolicy.Invoker

    class AnnotationsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    SUSPENDED_FIELD_NUMBER: _ClassVar[int]
    SELECTORS_FIELD_NUMBER: _ClassVar[int]
    RULES_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    uid: str
    description: str
    annotations: _containers.ScalarMap[str, str]
    labels: _containers.ScalarMap[str, str]
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    suspended: bool
    selectors: _containers.RepeatedCompositeFieldContainer[DeployPolicyResourceSelector]
    rules: _containers.RepeatedCompositeFieldContainer[PolicyRule]
    etag: str

    def __init__(self, name: _Optional[str]=..., uid: _Optional[str]=..., description: _Optional[str]=..., annotations: _Optional[_Mapping[str, str]]=..., labels: _Optional[_Mapping[str, str]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., suspended: bool=..., selectors: _Optional[_Iterable[_Union[DeployPolicyResourceSelector, _Mapping]]]=..., rules: _Optional[_Iterable[_Union[PolicyRule, _Mapping]]]=..., etag: _Optional[str]=...) -> None:
        ...

class DeployPolicyResourceSelector(_message.Message):
    __slots__ = ('delivery_pipeline', 'target')
    DELIVERY_PIPELINE_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    delivery_pipeline: DeliveryPipelineAttribute
    target: TargetAttribute

    def __init__(self, delivery_pipeline: _Optional[_Union[DeliveryPipelineAttribute, _Mapping]]=..., target: _Optional[_Union[TargetAttribute, _Mapping]]=...) -> None:
        ...

class DeliveryPipelineAttribute(_message.Message):
    __slots__ = ('id', 'labels')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    ID_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    id: str
    labels: _containers.ScalarMap[str, str]

    def __init__(self, id: _Optional[str]=..., labels: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class TargetAttribute(_message.Message):
    __slots__ = ('id', 'labels')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    ID_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    id: str
    labels: _containers.ScalarMap[str, str]

    def __init__(self, id: _Optional[str]=..., labels: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class PolicyRule(_message.Message):
    __slots__ = ('rollout_restriction',)
    ROLLOUT_RESTRICTION_FIELD_NUMBER: _ClassVar[int]
    rollout_restriction: RolloutRestriction

    def __init__(self, rollout_restriction: _Optional[_Union[RolloutRestriction, _Mapping]]=...) -> None:
        ...

class RolloutRestriction(_message.Message):
    __slots__ = ('id', 'invokers', 'actions', 'time_windows')

    class RolloutActions(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ROLLOUT_ACTIONS_UNSPECIFIED: _ClassVar[RolloutRestriction.RolloutActions]
        ADVANCE: _ClassVar[RolloutRestriction.RolloutActions]
        APPROVE: _ClassVar[RolloutRestriction.RolloutActions]
        CANCEL: _ClassVar[RolloutRestriction.RolloutActions]
        CREATE: _ClassVar[RolloutRestriction.RolloutActions]
        IGNORE_JOB: _ClassVar[RolloutRestriction.RolloutActions]
        RETRY_JOB: _ClassVar[RolloutRestriction.RolloutActions]
        ROLLBACK: _ClassVar[RolloutRestriction.RolloutActions]
        TERMINATE_JOBRUN: _ClassVar[RolloutRestriction.RolloutActions]
    ROLLOUT_ACTIONS_UNSPECIFIED: RolloutRestriction.RolloutActions
    ADVANCE: RolloutRestriction.RolloutActions
    APPROVE: RolloutRestriction.RolloutActions
    CANCEL: RolloutRestriction.RolloutActions
    CREATE: RolloutRestriction.RolloutActions
    IGNORE_JOB: RolloutRestriction.RolloutActions
    RETRY_JOB: RolloutRestriction.RolloutActions
    ROLLBACK: RolloutRestriction.RolloutActions
    TERMINATE_JOBRUN: RolloutRestriction.RolloutActions
    ID_FIELD_NUMBER: _ClassVar[int]
    INVOKERS_FIELD_NUMBER: _ClassVar[int]
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    TIME_WINDOWS_FIELD_NUMBER: _ClassVar[int]
    id: str
    invokers: _containers.RepeatedScalarFieldContainer[DeployPolicy.Invoker]
    actions: _containers.RepeatedScalarFieldContainer[RolloutRestriction.RolloutActions]
    time_windows: TimeWindows

    def __init__(self, id: _Optional[str]=..., invokers: _Optional[_Iterable[_Union[DeployPolicy.Invoker, str]]]=..., actions: _Optional[_Iterable[_Union[RolloutRestriction.RolloutActions, str]]]=..., time_windows: _Optional[_Union[TimeWindows, _Mapping]]=...) -> None:
        ...

class TimeWindows(_message.Message):
    __slots__ = ('time_zone', 'one_time_windows', 'weekly_windows')
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    ONE_TIME_WINDOWS_FIELD_NUMBER: _ClassVar[int]
    WEEKLY_WINDOWS_FIELD_NUMBER: _ClassVar[int]
    time_zone: str
    one_time_windows: _containers.RepeatedCompositeFieldContainer[OneTimeWindow]
    weekly_windows: _containers.RepeatedCompositeFieldContainer[WeeklyWindow]

    def __init__(self, time_zone: _Optional[str]=..., one_time_windows: _Optional[_Iterable[_Union[OneTimeWindow, _Mapping]]]=..., weekly_windows: _Optional[_Iterable[_Union[WeeklyWindow, _Mapping]]]=...) -> None:
        ...

class OneTimeWindow(_message.Message):
    __slots__ = ('start_date', 'start_time', 'end_date', 'end_time')
    START_DATE_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_DATE_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    start_date: _date_pb2.Date
    start_time: _timeofday_pb2.TimeOfDay
    end_date: _date_pb2.Date
    end_time: _timeofday_pb2.TimeOfDay

    def __init__(self, start_date: _Optional[_Union[_date_pb2.Date, _Mapping]]=..., start_time: _Optional[_Union[_timeofday_pb2.TimeOfDay, _Mapping]]=..., end_date: _Optional[_Union[_date_pb2.Date, _Mapping]]=..., end_time: _Optional[_Union[_timeofday_pb2.TimeOfDay, _Mapping]]=...) -> None:
        ...

class WeeklyWindow(_message.Message):
    __slots__ = ('days_of_week', 'start_time', 'end_time')
    DAYS_OF_WEEK_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    days_of_week: _containers.RepeatedScalarFieldContainer[_dayofweek_pb2.DayOfWeek]
    start_time: _timeofday_pb2.TimeOfDay
    end_time: _timeofday_pb2.TimeOfDay

    def __init__(self, days_of_week: _Optional[_Iterable[_Union[_dayofweek_pb2.DayOfWeek, str]]]=..., start_time: _Optional[_Union[_timeofday_pb2.TimeOfDay, _Mapping]]=..., end_time: _Optional[_Union[_timeofday_pb2.TimeOfDay, _Mapping]]=...) -> None:
        ...

class PolicyViolation(_message.Message):
    __slots__ = ('policy_violation_details',)
    POLICY_VIOLATION_DETAILS_FIELD_NUMBER: _ClassVar[int]
    policy_violation_details: _containers.RepeatedCompositeFieldContainer[PolicyViolationDetails]

    def __init__(self, policy_violation_details: _Optional[_Iterable[_Union[PolicyViolationDetails, _Mapping]]]=...) -> None:
        ...

class PolicyViolationDetails(_message.Message):
    __slots__ = ('policy', 'rule_id', 'failure_message')
    POLICY_FIELD_NUMBER: _ClassVar[int]
    RULE_ID_FIELD_NUMBER: _ClassVar[int]
    FAILURE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    policy: str
    rule_id: str
    failure_message: str

    def __init__(self, policy: _Optional[str]=..., rule_id: _Optional[str]=..., failure_message: _Optional[str]=...) -> None:
        ...

class Release(_message.Message):
    __slots__ = ('name', 'uid', 'description', 'annotations', 'labels', 'abandoned', 'create_time', 'render_start_time', 'render_end_time', 'skaffold_config_uri', 'skaffold_config_path', 'build_artifacts', 'delivery_pipeline_snapshot', 'target_snapshots', 'custom_target_type_snapshots', 'render_state', 'etag', 'skaffold_version', 'target_artifacts', 'target_renders', 'condition', 'deploy_parameters')

    class RenderState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RENDER_STATE_UNSPECIFIED: _ClassVar[Release.RenderState]
        SUCCEEDED: _ClassVar[Release.RenderState]
        FAILED: _ClassVar[Release.RenderState]
        IN_PROGRESS: _ClassVar[Release.RenderState]
    RENDER_STATE_UNSPECIFIED: Release.RenderState
    SUCCEEDED: Release.RenderState
    FAILED: Release.RenderState
    IN_PROGRESS: Release.RenderState

    class TargetRender(_message.Message):
        __slots__ = ('rendering_build', 'rendering_state', 'metadata', 'failure_cause', 'failure_message')

        class TargetRenderState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            TARGET_RENDER_STATE_UNSPECIFIED: _ClassVar[Release.TargetRender.TargetRenderState]
            SUCCEEDED: _ClassVar[Release.TargetRender.TargetRenderState]
            FAILED: _ClassVar[Release.TargetRender.TargetRenderState]
            IN_PROGRESS: _ClassVar[Release.TargetRender.TargetRenderState]
        TARGET_RENDER_STATE_UNSPECIFIED: Release.TargetRender.TargetRenderState
        SUCCEEDED: Release.TargetRender.TargetRenderState
        FAILED: Release.TargetRender.TargetRenderState
        IN_PROGRESS: Release.TargetRender.TargetRenderState

        class FailureCause(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            FAILURE_CAUSE_UNSPECIFIED: _ClassVar[Release.TargetRender.FailureCause]
            CLOUD_BUILD_UNAVAILABLE: _ClassVar[Release.TargetRender.FailureCause]
            EXECUTION_FAILED: _ClassVar[Release.TargetRender.FailureCause]
            CLOUD_BUILD_REQUEST_FAILED: _ClassVar[Release.TargetRender.FailureCause]
            VERIFICATION_CONFIG_NOT_FOUND: _ClassVar[Release.TargetRender.FailureCause]
            CUSTOM_ACTION_NOT_FOUND: _ClassVar[Release.TargetRender.FailureCause]
            DEPLOYMENT_STRATEGY_NOT_SUPPORTED: _ClassVar[Release.TargetRender.FailureCause]
            RENDER_FEATURE_NOT_SUPPORTED: _ClassVar[Release.TargetRender.FailureCause]
        FAILURE_CAUSE_UNSPECIFIED: Release.TargetRender.FailureCause
        CLOUD_BUILD_UNAVAILABLE: Release.TargetRender.FailureCause
        EXECUTION_FAILED: Release.TargetRender.FailureCause
        CLOUD_BUILD_REQUEST_FAILED: Release.TargetRender.FailureCause
        VERIFICATION_CONFIG_NOT_FOUND: Release.TargetRender.FailureCause
        CUSTOM_ACTION_NOT_FOUND: Release.TargetRender.FailureCause
        DEPLOYMENT_STRATEGY_NOT_SUPPORTED: Release.TargetRender.FailureCause
        RENDER_FEATURE_NOT_SUPPORTED: Release.TargetRender.FailureCause
        RENDERING_BUILD_FIELD_NUMBER: _ClassVar[int]
        RENDERING_STATE_FIELD_NUMBER: _ClassVar[int]
        METADATA_FIELD_NUMBER: _ClassVar[int]
        FAILURE_CAUSE_FIELD_NUMBER: _ClassVar[int]
        FAILURE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        rendering_build: str
        rendering_state: Release.TargetRender.TargetRenderState
        metadata: RenderMetadata
        failure_cause: Release.TargetRender.FailureCause
        failure_message: str

        def __init__(self, rendering_build: _Optional[str]=..., rendering_state: _Optional[_Union[Release.TargetRender.TargetRenderState, str]]=..., metadata: _Optional[_Union[RenderMetadata, _Mapping]]=..., failure_cause: _Optional[_Union[Release.TargetRender.FailureCause, str]]=..., failure_message: _Optional[str]=...) -> None:
            ...

    class ReleaseReadyCondition(_message.Message):
        __slots__ = ('status',)
        STATUS_FIELD_NUMBER: _ClassVar[int]
        status: bool

        def __init__(self, status: bool=...) -> None:
            ...

    class SkaffoldSupportedCondition(_message.Message):
        __slots__ = ('status', 'skaffold_support_state', 'maintenance_mode_time', 'support_expiration_time')
        STATUS_FIELD_NUMBER: _ClassVar[int]
        SKAFFOLD_SUPPORT_STATE_FIELD_NUMBER: _ClassVar[int]
        MAINTENANCE_MODE_TIME_FIELD_NUMBER: _ClassVar[int]
        SUPPORT_EXPIRATION_TIME_FIELD_NUMBER: _ClassVar[int]
        status: bool
        skaffold_support_state: SkaffoldSupportState
        maintenance_mode_time: _timestamp_pb2.Timestamp
        support_expiration_time: _timestamp_pb2.Timestamp

        def __init__(self, status: bool=..., skaffold_support_state: _Optional[_Union[SkaffoldSupportState, str]]=..., maintenance_mode_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., support_expiration_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
            ...

    class ReleaseCondition(_message.Message):
        __slots__ = ('release_ready_condition', 'skaffold_supported_condition')
        RELEASE_READY_CONDITION_FIELD_NUMBER: _ClassVar[int]
        SKAFFOLD_SUPPORTED_CONDITION_FIELD_NUMBER: _ClassVar[int]
        release_ready_condition: Release.ReleaseReadyCondition
        skaffold_supported_condition: Release.SkaffoldSupportedCondition

        def __init__(self, release_ready_condition: _Optional[_Union[Release.ReleaseReadyCondition, _Mapping]]=..., skaffold_supported_condition: _Optional[_Union[Release.SkaffoldSupportedCondition, _Mapping]]=...) -> None:
            ...

    class AnnotationsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...

    class TargetArtifactsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: TargetArtifact

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[TargetArtifact, _Mapping]]=...) -> None:
            ...

    class TargetRendersEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Release.TargetRender

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[Release.TargetRender, _Mapping]]=...) -> None:
            ...

    class DeployParametersEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    ABANDONED_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    RENDER_START_TIME_FIELD_NUMBER: _ClassVar[int]
    RENDER_END_TIME_FIELD_NUMBER: _ClassVar[int]
    SKAFFOLD_CONFIG_URI_FIELD_NUMBER: _ClassVar[int]
    SKAFFOLD_CONFIG_PATH_FIELD_NUMBER: _ClassVar[int]
    BUILD_ARTIFACTS_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_PIPELINE_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    TARGET_SNAPSHOTS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_TARGET_TYPE_SNAPSHOTS_FIELD_NUMBER: _ClassVar[int]
    RENDER_STATE_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    SKAFFOLD_VERSION_FIELD_NUMBER: _ClassVar[int]
    TARGET_ARTIFACTS_FIELD_NUMBER: _ClassVar[int]
    TARGET_RENDERS_FIELD_NUMBER: _ClassVar[int]
    CONDITION_FIELD_NUMBER: _ClassVar[int]
    DEPLOY_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    name: str
    uid: str
    description: str
    annotations: _containers.ScalarMap[str, str]
    labels: _containers.ScalarMap[str, str]
    abandoned: bool
    create_time: _timestamp_pb2.Timestamp
    render_start_time: _timestamp_pb2.Timestamp
    render_end_time: _timestamp_pb2.Timestamp
    skaffold_config_uri: str
    skaffold_config_path: str
    build_artifacts: _containers.RepeatedCompositeFieldContainer[BuildArtifact]
    delivery_pipeline_snapshot: DeliveryPipeline
    target_snapshots: _containers.RepeatedCompositeFieldContainer[Target]
    custom_target_type_snapshots: _containers.RepeatedCompositeFieldContainer[CustomTargetType]
    render_state: Release.RenderState
    etag: str
    skaffold_version: str
    target_artifacts: _containers.MessageMap[str, TargetArtifact]
    target_renders: _containers.MessageMap[str, Release.TargetRender]
    condition: Release.ReleaseCondition
    deploy_parameters: _containers.ScalarMap[str, str]

    def __init__(self, name: _Optional[str]=..., uid: _Optional[str]=..., description: _Optional[str]=..., annotations: _Optional[_Mapping[str, str]]=..., labels: _Optional[_Mapping[str, str]]=..., abandoned: bool=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., render_start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., render_end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., skaffold_config_uri: _Optional[str]=..., skaffold_config_path: _Optional[str]=..., build_artifacts: _Optional[_Iterable[_Union[BuildArtifact, _Mapping]]]=..., delivery_pipeline_snapshot: _Optional[_Union[DeliveryPipeline, _Mapping]]=..., target_snapshots: _Optional[_Iterable[_Union[Target, _Mapping]]]=..., custom_target_type_snapshots: _Optional[_Iterable[_Union[CustomTargetType, _Mapping]]]=..., render_state: _Optional[_Union[Release.RenderState, str]]=..., etag: _Optional[str]=..., skaffold_version: _Optional[str]=..., target_artifacts: _Optional[_Mapping[str, TargetArtifact]]=..., target_renders: _Optional[_Mapping[str, Release.TargetRender]]=..., condition: _Optional[_Union[Release.ReleaseCondition, _Mapping]]=..., deploy_parameters: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class CreateDeployPolicyRequest(_message.Message):
    __slots__ = ('parent', 'deploy_policy_id', 'deploy_policy', 'request_id', 'validate_only')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    DEPLOY_POLICY_ID_FIELD_NUMBER: _ClassVar[int]
    DEPLOY_POLICY_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    deploy_policy_id: str
    deploy_policy: DeployPolicy
    request_id: str
    validate_only: bool

    def __init__(self, parent: _Optional[str]=..., deploy_policy_id: _Optional[str]=..., deploy_policy: _Optional[_Union[DeployPolicy, _Mapping]]=..., request_id: _Optional[str]=..., validate_only: bool=...) -> None:
        ...

class UpdateDeployPolicyRequest(_message.Message):
    __slots__ = ('update_mask', 'deploy_policy', 'request_id', 'allow_missing', 'validate_only')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    DEPLOY_POLICY_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MISSING_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    deploy_policy: DeployPolicy
    request_id: str
    allow_missing: bool
    validate_only: bool

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., deploy_policy: _Optional[_Union[DeployPolicy, _Mapping]]=..., request_id: _Optional[str]=..., allow_missing: bool=..., validate_only: bool=...) -> None:
        ...

class DeleteDeployPolicyRequest(_message.Message):
    __slots__ = ('name', 'request_id', 'allow_missing', 'validate_only', 'etag')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MISSING_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str
    allow_missing: bool
    validate_only: bool
    etag: str

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=..., allow_missing: bool=..., validate_only: bool=..., etag: _Optional[str]=...) -> None:
        ...

class ListDeployPoliciesRequest(_message.Message):
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

class ListDeployPoliciesResponse(_message.Message):
    __slots__ = ('deploy_policies', 'next_page_token', 'unreachable')
    DEPLOY_POLICIES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    deploy_policies: _containers.RepeatedCompositeFieldContainer[DeployPolicy]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, deploy_policies: _Optional[_Iterable[_Union[DeployPolicy, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetDeployPolicyRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class BuildArtifact(_message.Message):
    __slots__ = ('image', 'tag')
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    image: str
    tag: str

    def __init__(self, image: _Optional[str]=..., tag: _Optional[str]=...) -> None:
        ...

class TargetArtifact(_message.Message):
    __slots__ = ('artifact_uri', 'skaffold_config_path', 'manifest_path', 'phase_artifacts')

    class PhaseArtifact(_message.Message):
        __slots__ = ('skaffold_config_path', 'manifest_path', 'job_manifests_path')
        SKAFFOLD_CONFIG_PATH_FIELD_NUMBER: _ClassVar[int]
        MANIFEST_PATH_FIELD_NUMBER: _ClassVar[int]
        JOB_MANIFESTS_PATH_FIELD_NUMBER: _ClassVar[int]
        skaffold_config_path: str
        manifest_path: str
        job_manifests_path: str

        def __init__(self, skaffold_config_path: _Optional[str]=..., manifest_path: _Optional[str]=..., job_manifests_path: _Optional[str]=...) -> None:
            ...

    class PhaseArtifactsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: TargetArtifact.PhaseArtifact

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[TargetArtifact.PhaseArtifact, _Mapping]]=...) -> None:
            ...
    ARTIFACT_URI_FIELD_NUMBER: _ClassVar[int]
    SKAFFOLD_CONFIG_PATH_FIELD_NUMBER: _ClassVar[int]
    MANIFEST_PATH_FIELD_NUMBER: _ClassVar[int]
    PHASE_ARTIFACTS_FIELD_NUMBER: _ClassVar[int]
    artifact_uri: str
    skaffold_config_path: str
    manifest_path: str
    phase_artifacts: _containers.MessageMap[str, TargetArtifact.PhaseArtifact]

    def __init__(self, artifact_uri: _Optional[str]=..., skaffold_config_path: _Optional[str]=..., manifest_path: _Optional[str]=..., phase_artifacts: _Optional[_Mapping[str, TargetArtifact.PhaseArtifact]]=...) -> None:
        ...

class DeployArtifact(_message.Message):
    __slots__ = ('artifact_uri', 'manifest_paths')
    ARTIFACT_URI_FIELD_NUMBER: _ClassVar[int]
    MANIFEST_PATHS_FIELD_NUMBER: _ClassVar[int]
    artifact_uri: str
    manifest_paths: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, artifact_uri: _Optional[str]=..., manifest_paths: _Optional[_Iterable[str]]=...) -> None:
        ...

class CloudRunRenderMetadata(_message.Message):
    __slots__ = ('service',)
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    service: str

    def __init__(self, service: _Optional[str]=...) -> None:
        ...

class RenderMetadata(_message.Message):
    __slots__ = ('cloud_run', 'custom')
    CLOUD_RUN_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELD_NUMBER: _ClassVar[int]
    cloud_run: CloudRunRenderMetadata
    custom: CustomMetadata

    def __init__(self, cloud_run: _Optional[_Union[CloudRunRenderMetadata, _Mapping]]=..., custom: _Optional[_Union[CustomMetadata, _Mapping]]=...) -> None:
        ...

class ListReleasesRequest(_message.Message):
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

class ListReleasesResponse(_message.Message):
    __slots__ = ('releases', 'next_page_token', 'unreachable')
    RELEASES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    releases: _containers.RepeatedCompositeFieldContainer[Release]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, releases: _Optional[_Iterable[_Union[Release, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetReleaseRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateReleaseRequest(_message.Message):
    __slots__ = ('parent', 'release_id', 'release', 'request_id', 'validate_only', 'override_deploy_policy')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    RELEASE_ID_FIELD_NUMBER: _ClassVar[int]
    RELEASE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    OVERRIDE_DEPLOY_POLICY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    release_id: str
    release: Release
    request_id: str
    validate_only: bool
    override_deploy_policy: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, parent: _Optional[str]=..., release_id: _Optional[str]=..., release: _Optional[_Union[Release, _Mapping]]=..., request_id: _Optional[str]=..., validate_only: bool=..., override_deploy_policy: _Optional[_Iterable[str]]=...) -> None:
        ...

class Rollout(_message.Message):
    __slots__ = ('name', 'uid', 'description', 'annotations', 'labels', 'create_time', 'approve_time', 'enqueue_time', 'deploy_start_time', 'deploy_end_time', 'target_id', 'approval_state', 'state', 'failure_reason', 'deploying_build', 'etag', 'deploy_failure_cause', 'phases', 'metadata', 'controller_rollout', 'rollback_of_rollout', 'rolled_back_by_rollouts', 'active_repair_automation_run')

    class ApprovalState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        APPROVAL_STATE_UNSPECIFIED: _ClassVar[Rollout.ApprovalState]
        NEEDS_APPROVAL: _ClassVar[Rollout.ApprovalState]
        DOES_NOT_NEED_APPROVAL: _ClassVar[Rollout.ApprovalState]
        APPROVED: _ClassVar[Rollout.ApprovalState]
        REJECTED: _ClassVar[Rollout.ApprovalState]
    APPROVAL_STATE_UNSPECIFIED: Rollout.ApprovalState
    NEEDS_APPROVAL: Rollout.ApprovalState
    DOES_NOT_NEED_APPROVAL: Rollout.ApprovalState
    APPROVED: Rollout.ApprovalState
    REJECTED: Rollout.ApprovalState

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Rollout.State]
        SUCCEEDED: _ClassVar[Rollout.State]
        FAILED: _ClassVar[Rollout.State]
        IN_PROGRESS: _ClassVar[Rollout.State]
        PENDING_APPROVAL: _ClassVar[Rollout.State]
        APPROVAL_REJECTED: _ClassVar[Rollout.State]
        PENDING: _ClassVar[Rollout.State]
        PENDING_RELEASE: _ClassVar[Rollout.State]
        CANCELLING: _ClassVar[Rollout.State]
        CANCELLED: _ClassVar[Rollout.State]
        HALTED: _ClassVar[Rollout.State]
    STATE_UNSPECIFIED: Rollout.State
    SUCCEEDED: Rollout.State
    FAILED: Rollout.State
    IN_PROGRESS: Rollout.State
    PENDING_APPROVAL: Rollout.State
    APPROVAL_REJECTED: Rollout.State
    PENDING: Rollout.State
    PENDING_RELEASE: Rollout.State
    CANCELLING: Rollout.State
    CANCELLED: Rollout.State
    HALTED: Rollout.State

    class FailureCause(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FAILURE_CAUSE_UNSPECIFIED: _ClassVar[Rollout.FailureCause]
        CLOUD_BUILD_UNAVAILABLE: _ClassVar[Rollout.FailureCause]
        EXECUTION_FAILED: _ClassVar[Rollout.FailureCause]
        DEADLINE_EXCEEDED: _ClassVar[Rollout.FailureCause]
        RELEASE_FAILED: _ClassVar[Rollout.FailureCause]
        RELEASE_ABANDONED: _ClassVar[Rollout.FailureCause]
        VERIFICATION_CONFIG_NOT_FOUND: _ClassVar[Rollout.FailureCause]
        CLOUD_BUILD_REQUEST_FAILED: _ClassVar[Rollout.FailureCause]
        OPERATION_FEATURE_NOT_SUPPORTED: _ClassVar[Rollout.FailureCause]
    FAILURE_CAUSE_UNSPECIFIED: Rollout.FailureCause
    CLOUD_BUILD_UNAVAILABLE: Rollout.FailureCause
    EXECUTION_FAILED: Rollout.FailureCause
    DEADLINE_EXCEEDED: Rollout.FailureCause
    RELEASE_FAILED: Rollout.FailureCause
    RELEASE_ABANDONED: Rollout.FailureCause
    VERIFICATION_CONFIG_NOT_FOUND: Rollout.FailureCause
    CLOUD_BUILD_REQUEST_FAILED: Rollout.FailureCause
    OPERATION_FEATURE_NOT_SUPPORTED: Rollout.FailureCause

    class AnnotationsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    APPROVE_TIME_FIELD_NUMBER: _ClassVar[int]
    ENQUEUE_TIME_FIELD_NUMBER: _ClassVar[int]
    DEPLOY_START_TIME_FIELD_NUMBER: _ClassVar[int]
    DEPLOY_END_TIME_FIELD_NUMBER: _ClassVar[int]
    TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    APPROVAL_STATE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    FAILURE_REASON_FIELD_NUMBER: _ClassVar[int]
    DEPLOYING_BUILD_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    DEPLOY_FAILURE_CAUSE_FIELD_NUMBER: _ClassVar[int]
    PHASES_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    CONTROLLER_ROLLOUT_FIELD_NUMBER: _ClassVar[int]
    ROLLBACK_OF_ROLLOUT_FIELD_NUMBER: _ClassVar[int]
    ROLLED_BACK_BY_ROLLOUTS_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_REPAIR_AUTOMATION_RUN_FIELD_NUMBER: _ClassVar[int]
    name: str
    uid: str
    description: str
    annotations: _containers.ScalarMap[str, str]
    labels: _containers.ScalarMap[str, str]
    create_time: _timestamp_pb2.Timestamp
    approve_time: _timestamp_pb2.Timestamp
    enqueue_time: _timestamp_pb2.Timestamp
    deploy_start_time: _timestamp_pb2.Timestamp
    deploy_end_time: _timestamp_pb2.Timestamp
    target_id: str
    approval_state: Rollout.ApprovalState
    state: Rollout.State
    failure_reason: str
    deploying_build: str
    etag: str
    deploy_failure_cause: Rollout.FailureCause
    phases: _containers.RepeatedCompositeFieldContainer[Phase]
    metadata: Metadata
    controller_rollout: str
    rollback_of_rollout: str
    rolled_back_by_rollouts: _containers.RepeatedScalarFieldContainer[str]
    active_repair_automation_run: str

    def __init__(self, name: _Optional[str]=..., uid: _Optional[str]=..., description: _Optional[str]=..., annotations: _Optional[_Mapping[str, str]]=..., labels: _Optional[_Mapping[str, str]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., approve_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., enqueue_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., deploy_start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., deploy_end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., target_id: _Optional[str]=..., approval_state: _Optional[_Union[Rollout.ApprovalState, str]]=..., state: _Optional[_Union[Rollout.State, str]]=..., failure_reason: _Optional[str]=..., deploying_build: _Optional[str]=..., etag: _Optional[str]=..., deploy_failure_cause: _Optional[_Union[Rollout.FailureCause, str]]=..., phases: _Optional[_Iterable[_Union[Phase, _Mapping]]]=..., metadata: _Optional[_Union[Metadata, _Mapping]]=..., controller_rollout: _Optional[str]=..., rollback_of_rollout: _Optional[str]=..., rolled_back_by_rollouts: _Optional[_Iterable[str]]=..., active_repair_automation_run: _Optional[str]=...) -> None:
        ...

class Metadata(_message.Message):
    __slots__ = ('cloud_run', 'automation', 'custom')
    CLOUD_RUN_FIELD_NUMBER: _ClassVar[int]
    AUTOMATION_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELD_NUMBER: _ClassVar[int]
    cloud_run: CloudRunMetadata
    automation: AutomationRolloutMetadata
    custom: CustomMetadata

    def __init__(self, cloud_run: _Optional[_Union[CloudRunMetadata, _Mapping]]=..., automation: _Optional[_Union[AutomationRolloutMetadata, _Mapping]]=..., custom: _Optional[_Union[CustomMetadata, _Mapping]]=...) -> None:
        ...

class DeployJobRunMetadata(_message.Message):
    __slots__ = ('cloud_run', 'custom_target', 'custom')
    CLOUD_RUN_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_TARGET_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELD_NUMBER: _ClassVar[int]
    cloud_run: CloudRunMetadata
    custom_target: CustomTargetDeployMetadata
    custom: CustomMetadata

    def __init__(self, cloud_run: _Optional[_Union[CloudRunMetadata, _Mapping]]=..., custom_target: _Optional[_Union[CustomTargetDeployMetadata, _Mapping]]=..., custom: _Optional[_Union[CustomMetadata, _Mapping]]=...) -> None:
        ...

class CloudRunMetadata(_message.Message):
    __slots__ = ('service', 'service_urls', 'revision', 'job')
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    SERVICE_URLS_FIELD_NUMBER: _ClassVar[int]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    JOB_FIELD_NUMBER: _ClassVar[int]
    service: str
    service_urls: _containers.RepeatedScalarFieldContainer[str]
    revision: str
    job: str

    def __init__(self, service: _Optional[str]=..., service_urls: _Optional[_Iterable[str]]=..., revision: _Optional[str]=..., job: _Optional[str]=...) -> None:
        ...

class CustomTargetDeployMetadata(_message.Message):
    __slots__ = ('skip_message',)
    SKIP_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    skip_message: str

    def __init__(self, skip_message: _Optional[str]=...) -> None:
        ...

class AutomationRolloutMetadata(_message.Message):
    __slots__ = ('promote_automation_run', 'advance_automation_runs', 'repair_automation_runs')
    PROMOTE_AUTOMATION_RUN_FIELD_NUMBER: _ClassVar[int]
    ADVANCE_AUTOMATION_RUNS_FIELD_NUMBER: _ClassVar[int]
    REPAIR_AUTOMATION_RUNS_FIELD_NUMBER: _ClassVar[int]
    promote_automation_run: str
    advance_automation_runs: _containers.RepeatedScalarFieldContainer[str]
    repair_automation_runs: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, promote_automation_run: _Optional[str]=..., advance_automation_runs: _Optional[_Iterable[str]]=..., repair_automation_runs: _Optional[_Iterable[str]]=...) -> None:
        ...

class CustomMetadata(_message.Message):
    __slots__ = ('values',)

    class ValuesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.ScalarMap[str, str]

    def __init__(self, values: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class Phase(_message.Message):
    __slots__ = ('id', 'state', 'skip_message', 'deployment_jobs', 'child_rollout_jobs')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Phase.State]
        PENDING: _ClassVar[Phase.State]
        IN_PROGRESS: _ClassVar[Phase.State]
        SUCCEEDED: _ClassVar[Phase.State]
        FAILED: _ClassVar[Phase.State]
        ABORTED: _ClassVar[Phase.State]
        SKIPPED: _ClassVar[Phase.State]
    STATE_UNSPECIFIED: Phase.State
    PENDING: Phase.State
    IN_PROGRESS: Phase.State
    SUCCEEDED: Phase.State
    FAILED: Phase.State
    ABORTED: Phase.State
    SKIPPED: Phase.State
    ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    SKIP_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_JOBS_FIELD_NUMBER: _ClassVar[int]
    CHILD_ROLLOUT_JOBS_FIELD_NUMBER: _ClassVar[int]
    id: str
    state: Phase.State
    skip_message: str
    deployment_jobs: DeploymentJobs
    child_rollout_jobs: ChildRolloutJobs

    def __init__(self, id: _Optional[str]=..., state: _Optional[_Union[Phase.State, str]]=..., skip_message: _Optional[str]=..., deployment_jobs: _Optional[_Union[DeploymentJobs, _Mapping]]=..., child_rollout_jobs: _Optional[_Union[ChildRolloutJobs, _Mapping]]=...) -> None:
        ...

class DeploymentJobs(_message.Message):
    __slots__ = ('deploy_job', 'verify_job', 'predeploy_job', 'postdeploy_job')
    DEPLOY_JOB_FIELD_NUMBER: _ClassVar[int]
    VERIFY_JOB_FIELD_NUMBER: _ClassVar[int]
    PREDEPLOY_JOB_FIELD_NUMBER: _ClassVar[int]
    POSTDEPLOY_JOB_FIELD_NUMBER: _ClassVar[int]
    deploy_job: Job
    verify_job: Job
    predeploy_job: Job
    postdeploy_job: Job

    def __init__(self, deploy_job: _Optional[_Union[Job, _Mapping]]=..., verify_job: _Optional[_Union[Job, _Mapping]]=..., predeploy_job: _Optional[_Union[Job, _Mapping]]=..., postdeploy_job: _Optional[_Union[Job, _Mapping]]=...) -> None:
        ...

class ChildRolloutJobs(_message.Message):
    __slots__ = ('create_rollout_jobs', 'advance_rollout_jobs')
    CREATE_ROLLOUT_JOBS_FIELD_NUMBER: _ClassVar[int]
    ADVANCE_ROLLOUT_JOBS_FIELD_NUMBER: _ClassVar[int]
    create_rollout_jobs: _containers.RepeatedCompositeFieldContainer[Job]
    advance_rollout_jobs: _containers.RepeatedCompositeFieldContainer[Job]

    def __init__(self, create_rollout_jobs: _Optional[_Iterable[_Union[Job, _Mapping]]]=..., advance_rollout_jobs: _Optional[_Iterable[_Union[Job, _Mapping]]]=...) -> None:
        ...

class Job(_message.Message):
    __slots__ = ('id', 'state', 'skip_message', 'job_run', 'deploy_job', 'verify_job', 'predeploy_job', 'postdeploy_job', 'create_child_rollout_job', 'advance_child_rollout_job')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Job.State]
        PENDING: _ClassVar[Job.State]
        DISABLED: _ClassVar[Job.State]
        IN_PROGRESS: _ClassVar[Job.State]
        SUCCEEDED: _ClassVar[Job.State]
        FAILED: _ClassVar[Job.State]
        ABORTED: _ClassVar[Job.State]
        SKIPPED: _ClassVar[Job.State]
        IGNORED: _ClassVar[Job.State]
    STATE_UNSPECIFIED: Job.State
    PENDING: Job.State
    DISABLED: Job.State
    IN_PROGRESS: Job.State
    SUCCEEDED: Job.State
    FAILED: Job.State
    ABORTED: Job.State
    SKIPPED: Job.State
    IGNORED: Job.State
    ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    SKIP_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    JOB_RUN_FIELD_NUMBER: _ClassVar[int]
    DEPLOY_JOB_FIELD_NUMBER: _ClassVar[int]
    VERIFY_JOB_FIELD_NUMBER: _ClassVar[int]
    PREDEPLOY_JOB_FIELD_NUMBER: _ClassVar[int]
    POSTDEPLOY_JOB_FIELD_NUMBER: _ClassVar[int]
    CREATE_CHILD_ROLLOUT_JOB_FIELD_NUMBER: _ClassVar[int]
    ADVANCE_CHILD_ROLLOUT_JOB_FIELD_NUMBER: _ClassVar[int]
    id: str
    state: Job.State
    skip_message: str
    job_run: str
    deploy_job: DeployJob
    verify_job: VerifyJob
    predeploy_job: PredeployJob
    postdeploy_job: PostdeployJob
    create_child_rollout_job: CreateChildRolloutJob
    advance_child_rollout_job: AdvanceChildRolloutJob

    def __init__(self, id: _Optional[str]=..., state: _Optional[_Union[Job.State, str]]=..., skip_message: _Optional[str]=..., job_run: _Optional[str]=..., deploy_job: _Optional[_Union[DeployJob, _Mapping]]=..., verify_job: _Optional[_Union[VerifyJob, _Mapping]]=..., predeploy_job: _Optional[_Union[PredeployJob, _Mapping]]=..., postdeploy_job: _Optional[_Union[PostdeployJob, _Mapping]]=..., create_child_rollout_job: _Optional[_Union[CreateChildRolloutJob, _Mapping]]=..., advance_child_rollout_job: _Optional[_Union[AdvanceChildRolloutJob, _Mapping]]=...) -> None:
        ...

class DeployJob(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class VerifyJob(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class PredeployJob(_message.Message):
    __slots__ = ('actions',)
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    actions: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, actions: _Optional[_Iterable[str]]=...) -> None:
        ...

class PostdeployJob(_message.Message):
    __slots__ = ('actions',)
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    actions: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, actions: _Optional[_Iterable[str]]=...) -> None:
        ...

class CreateChildRolloutJob(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class AdvanceChildRolloutJob(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class ListRolloutsRequest(_message.Message):
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

class ListRolloutsResponse(_message.Message):
    __slots__ = ('rollouts', 'next_page_token', 'unreachable')
    ROLLOUTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    rollouts: _containers.RepeatedCompositeFieldContainer[Rollout]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, rollouts: _Optional[_Iterable[_Union[Rollout, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetRolloutRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateRolloutRequest(_message.Message):
    __slots__ = ('parent', 'rollout_id', 'rollout', 'request_id', 'validate_only', 'override_deploy_policy', 'starting_phase_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ROLLOUT_ID_FIELD_NUMBER: _ClassVar[int]
    ROLLOUT_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    OVERRIDE_DEPLOY_POLICY_FIELD_NUMBER: _ClassVar[int]
    STARTING_PHASE_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    rollout_id: str
    rollout: Rollout
    request_id: str
    validate_only: bool
    override_deploy_policy: _containers.RepeatedScalarFieldContainer[str]
    starting_phase_id: str

    def __init__(self, parent: _Optional[str]=..., rollout_id: _Optional[str]=..., rollout: _Optional[_Union[Rollout, _Mapping]]=..., request_id: _Optional[str]=..., validate_only: bool=..., override_deploy_policy: _Optional[_Iterable[str]]=..., starting_phase_id: _Optional[str]=...) -> None:
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

class ApproveRolloutRequest(_message.Message):
    __slots__ = ('name', 'approved', 'override_deploy_policy')
    NAME_FIELD_NUMBER: _ClassVar[int]
    APPROVED_FIELD_NUMBER: _ClassVar[int]
    OVERRIDE_DEPLOY_POLICY_FIELD_NUMBER: _ClassVar[int]
    name: str
    approved: bool
    override_deploy_policy: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, name: _Optional[str]=..., approved: bool=..., override_deploy_policy: _Optional[_Iterable[str]]=...) -> None:
        ...

class ApproveRolloutResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class AdvanceRolloutRequest(_message.Message):
    __slots__ = ('name', 'phase_id', 'override_deploy_policy')
    NAME_FIELD_NUMBER: _ClassVar[int]
    PHASE_ID_FIELD_NUMBER: _ClassVar[int]
    OVERRIDE_DEPLOY_POLICY_FIELD_NUMBER: _ClassVar[int]
    name: str
    phase_id: str
    override_deploy_policy: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, name: _Optional[str]=..., phase_id: _Optional[str]=..., override_deploy_policy: _Optional[_Iterable[str]]=...) -> None:
        ...

class AdvanceRolloutResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class CancelRolloutRequest(_message.Message):
    __slots__ = ('name', 'override_deploy_policy')
    NAME_FIELD_NUMBER: _ClassVar[int]
    OVERRIDE_DEPLOY_POLICY_FIELD_NUMBER: _ClassVar[int]
    name: str
    override_deploy_policy: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, name: _Optional[str]=..., override_deploy_policy: _Optional[_Iterable[str]]=...) -> None:
        ...

class CancelRolloutResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class IgnoreJobRequest(_message.Message):
    __slots__ = ('rollout', 'phase_id', 'job_id', 'override_deploy_policy')
    ROLLOUT_FIELD_NUMBER: _ClassVar[int]
    PHASE_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    OVERRIDE_DEPLOY_POLICY_FIELD_NUMBER: _ClassVar[int]
    rollout: str
    phase_id: str
    job_id: str
    override_deploy_policy: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, rollout: _Optional[str]=..., phase_id: _Optional[str]=..., job_id: _Optional[str]=..., override_deploy_policy: _Optional[_Iterable[str]]=...) -> None:
        ...

class IgnoreJobResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class RetryJobRequest(_message.Message):
    __slots__ = ('rollout', 'phase_id', 'job_id', 'override_deploy_policy')
    ROLLOUT_FIELD_NUMBER: _ClassVar[int]
    PHASE_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    OVERRIDE_DEPLOY_POLICY_FIELD_NUMBER: _ClassVar[int]
    rollout: str
    phase_id: str
    job_id: str
    override_deploy_policy: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, rollout: _Optional[str]=..., phase_id: _Optional[str]=..., job_id: _Optional[str]=..., override_deploy_policy: _Optional[_Iterable[str]]=...) -> None:
        ...

class RetryJobResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class AbandonReleaseRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class AbandonReleaseResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class JobRun(_message.Message):
    __slots__ = ('name', 'uid', 'phase_id', 'job_id', 'create_time', 'start_time', 'end_time', 'state', 'deploy_job_run', 'verify_job_run', 'predeploy_job_run', 'postdeploy_job_run', 'create_child_rollout_job_run', 'advance_child_rollout_job_run', 'etag')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[JobRun.State]
        IN_PROGRESS: _ClassVar[JobRun.State]
        SUCCEEDED: _ClassVar[JobRun.State]
        FAILED: _ClassVar[JobRun.State]
        TERMINATING: _ClassVar[JobRun.State]
        TERMINATED: _ClassVar[JobRun.State]
    STATE_UNSPECIFIED: JobRun.State
    IN_PROGRESS: JobRun.State
    SUCCEEDED: JobRun.State
    FAILED: JobRun.State
    TERMINATING: JobRun.State
    TERMINATED: JobRun.State
    NAME_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    PHASE_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    DEPLOY_JOB_RUN_FIELD_NUMBER: _ClassVar[int]
    VERIFY_JOB_RUN_FIELD_NUMBER: _ClassVar[int]
    PREDEPLOY_JOB_RUN_FIELD_NUMBER: _ClassVar[int]
    POSTDEPLOY_JOB_RUN_FIELD_NUMBER: _ClassVar[int]
    CREATE_CHILD_ROLLOUT_JOB_RUN_FIELD_NUMBER: _ClassVar[int]
    ADVANCE_CHILD_ROLLOUT_JOB_RUN_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    uid: str
    phase_id: str
    job_id: str
    create_time: _timestamp_pb2.Timestamp
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    state: JobRun.State
    deploy_job_run: DeployJobRun
    verify_job_run: VerifyJobRun
    predeploy_job_run: PredeployJobRun
    postdeploy_job_run: PostdeployJobRun
    create_child_rollout_job_run: CreateChildRolloutJobRun
    advance_child_rollout_job_run: AdvanceChildRolloutJobRun
    etag: str

    def __init__(self, name: _Optional[str]=..., uid: _Optional[str]=..., phase_id: _Optional[str]=..., job_id: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., state: _Optional[_Union[JobRun.State, str]]=..., deploy_job_run: _Optional[_Union[DeployJobRun, _Mapping]]=..., verify_job_run: _Optional[_Union[VerifyJobRun, _Mapping]]=..., predeploy_job_run: _Optional[_Union[PredeployJobRun, _Mapping]]=..., postdeploy_job_run: _Optional[_Union[PostdeployJobRun, _Mapping]]=..., create_child_rollout_job_run: _Optional[_Union[CreateChildRolloutJobRun, _Mapping]]=..., advance_child_rollout_job_run: _Optional[_Union[AdvanceChildRolloutJobRun, _Mapping]]=..., etag: _Optional[str]=...) -> None:
        ...

class DeployJobRun(_message.Message):
    __slots__ = ('build', 'failure_cause', 'failure_message', 'metadata', 'artifact')

    class FailureCause(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FAILURE_CAUSE_UNSPECIFIED: _ClassVar[DeployJobRun.FailureCause]
        CLOUD_BUILD_UNAVAILABLE: _ClassVar[DeployJobRun.FailureCause]
        EXECUTION_FAILED: _ClassVar[DeployJobRun.FailureCause]
        DEADLINE_EXCEEDED: _ClassVar[DeployJobRun.FailureCause]
        MISSING_RESOURCES_FOR_CANARY: _ClassVar[DeployJobRun.FailureCause]
        CLOUD_BUILD_REQUEST_FAILED: _ClassVar[DeployJobRun.FailureCause]
        DEPLOY_FEATURE_NOT_SUPPORTED: _ClassVar[DeployJobRun.FailureCause]
    FAILURE_CAUSE_UNSPECIFIED: DeployJobRun.FailureCause
    CLOUD_BUILD_UNAVAILABLE: DeployJobRun.FailureCause
    EXECUTION_FAILED: DeployJobRun.FailureCause
    DEADLINE_EXCEEDED: DeployJobRun.FailureCause
    MISSING_RESOURCES_FOR_CANARY: DeployJobRun.FailureCause
    CLOUD_BUILD_REQUEST_FAILED: DeployJobRun.FailureCause
    DEPLOY_FEATURE_NOT_SUPPORTED: DeployJobRun.FailureCause
    BUILD_FIELD_NUMBER: _ClassVar[int]
    FAILURE_CAUSE_FIELD_NUMBER: _ClassVar[int]
    FAILURE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    ARTIFACT_FIELD_NUMBER: _ClassVar[int]
    build: str
    failure_cause: DeployJobRun.FailureCause
    failure_message: str
    metadata: DeployJobRunMetadata
    artifact: DeployArtifact

    def __init__(self, build: _Optional[str]=..., failure_cause: _Optional[_Union[DeployJobRun.FailureCause, str]]=..., failure_message: _Optional[str]=..., metadata: _Optional[_Union[DeployJobRunMetadata, _Mapping]]=..., artifact: _Optional[_Union[DeployArtifact, _Mapping]]=...) -> None:
        ...

class VerifyJobRun(_message.Message):
    __slots__ = ('build', 'artifact_uri', 'event_log_path', 'failure_cause', 'failure_message')

    class FailureCause(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FAILURE_CAUSE_UNSPECIFIED: _ClassVar[VerifyJobRun.FailureCause]
        CLOUD_BUILD_UNAVAILABLE: _ClassVar[VerifyJobRun.FailureCause]
        EXECUTION_FAILED: _ClassVar[VerifyJobRun.FailureCause]
        DEADLINE_EXCEEDED: _ClassVar[VerifyJobRun.FailureCause]
        VERIFICATION_CONFIG_NOT_FOUND: _ClassVar[VerifyJobRun.FailureCause]
        CLOUD_BUILD_REQUEST_FAILED: _ClassVar[VerifyJobRun.FailureCause]
    FAILURE_CAUSE_UNSPECIFIED: VerifyJobRun.FailureCause
    CLOUD_BUILD_UNAVAILABLE: VerifyJobRun.FailureCause
    EXECUTION_FAILED: VerifyJobRun.FailureCause
    DEADLINE_EXCEEDED: VerifyJobRun.FailureCause
    VERIFICATION_CONFIG_NOT_FOUND: VerifyJobRun.FailureCause
    CLOUD_BUILD_REQUEST_FAILED: VerifyJobRun.FailureCause
    BUILD_FIELD_NUMBER: _ClassVar[int]
    ARTIFACT_URI_FIELD_NUMBER: _ClassVar[int]
    EVENT_LOG_PATH_FIELD_NUMBER: _ClassVar[int]
    FAILURE_CAUSE_FIELD_NUMBER: _ClassVar[int]
    FAILURE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    build: str
    artifact_uri: str
    event_log_path: str
    failure_cause: VerifyJobRun.FailureCause
    failure_message: str

    def __init__(self, build: _Optional[str]=..., artifact_uri: _Optional[str]=..., event_log_path: _Optional[str]=..., failure_cause: _Optional[_Union[VerifyJobRun.FailureCause, str]]=..., failure_message: _Optional[str]=...) -> None:
        ...

class PredeployJobRun(_message.Message):
    __slots__ = ('build', 'failure_cause', 'failure_message')

    class FailureCause(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FAILURE_CAUSE_UNSPECIFIED: _ClassVar[PredeployJobRun.FailureCause]
        CLOUD_BUILD_UNAVAILABLE: _ClassVar[PredeployJobRun.FailureCause]
        EXECUTION_FAILED: _ClassVar[PredeployJobRun.FailureCause]
        DEADLINE_EXCEEDED: _ClassVar[PredeployJobRun.FailureCause]
        CLOUD_BUILD_REQUEST_FAILED: _ClassVar[PredeployJobRun.FailureCause]
    FAILURE_CAUSE_UNSPECIFIED: PredeployJobRun.FailureCause
    CLOUD_BUILD_UNAVAILABLE: PredeployJobRun.FailureCause
    EXECUTION_FAILED: PredeployJobRun.FailureCause
    DEADLINE_EXCEEDED: PredeployJobRun.FailureCause
    CLOUD_BUILD_REQUEST_FAILED: PredeployJobRun.FailureCause
    BUILD_FIELD_NUMBER: _ClassVar[int]
    FAILURE_CAUSE_FIELD_NUMBER: _ClassVar[int]
    FAILURE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    build: str
    failure_cause: PredeployJobRun.FailureCause
    failure_message: str

    def __init__(self, build: _Optional[str]=..., failure_cause: _Optional[_Union[PredeployJobRun.FailureCause, str]]=..., failure_message: _Optional[str]=...) -> None:
        ...

class PostdeployJobRun(_message.Message):
    __slots__ = ('build', 'failure_cause', 'failure_message')

    class FailureCause(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FAILURE_CAUSE_UNSPECIFIED: _ClassVar[PostdeployJobRun.FailureCause]
        CLOUD_BUILD_UNAVAILABLE: _ClassVar[PostdeployJobRun.FailureCause]
        EXECUTION_FAILED: _ClassVar[PostdeployJobRun.FailureCause]
        DEADLINE_EXCEEDED: _ClassVar[PostdeployJobRun.FailureCause]
        CLOUD_BUILD_REQUEST_FAILED: _ClassVar[PostdeployJobRun.FailureCause]
    FAILURE_CAUSE_UNSPECIFIED: PostdeployJobRun.FailureCause
    CLOUD_BUILD_UNAVAILABLE: PostdeployJobRun.FailureCause
    EXECUTION_FAILED: PostdeployJobRun.FailureCause
    DEADLINE_EXCEEDED: PostdeployJobRun.FailureCause
    CLOUD_BUILD_REQUEST_FAILED: PostdeployJobRun.FailureCause
    BUILD_FIELD_NUMBER: _ClassVar[int]
    FAILURE_CAUSE_FIELD_NUMBER: _ClassVar[int]
    FAILURE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    build: str
    failure_cause: PostdeployJobRun.FailureCause
    failure_message: str

    def __init__(self, build: _Optional[str]=..., failure_cause: _Optional[_Union[PostdeployJobRun.FailureCause, str]]=..., failure_message: _Optional[str]=...) -> None:
        ...

class CreateChildRolloutJobRun(_message.Message):
    __slots__ = ('rollout', 'rollout_phase_id')
    ROLLOUT_FIELD_NUMBER: _ClassVar[int]
    ROLLOUT_PHASE_ID_FIELD_NUMBER: _ClassVar[int]
    rollout: str
    rollout_phase_id: str

    def __init__(self, rollout: _Optional[str]=..., rollout_phase_id: _Optional[str]=...) -> None:
        ...

class AdvanceChildRolloutJobRun(_message.Message):
    __slots__ = ('rollout', 'rollout_phase_id')
    ROLLOUT_FIELD_NUMBER: _ClassVar[int]
    ROLLOUT_PHASE_ID_FIELD_NUMBER: _ClassVar[int]
    rollout: str
    rollout_phase_id: str

    def __init__(self, rollout: _Optional[str]=..., rollout_phase_id: _Optional[str]=...) -> None:
        ...

class ListJobRunsRequest(_message.Message):
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

class ListJobRunsResponse(_message.Message):
    __slots__ = ('job_runs', 'next_page_token', 'unreachable')
    JOB_RUNS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    job_runs: _containers.RepeatedCompositeFieldContainer[JobRun]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, job_runs: _Optional[_Iterable[_Union[JobRun, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetJobRunRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class TerminateJobRunRequest(_message.Message):
    __slots__ = ('name', 'override_deploy_policy')
    NAME_FIELD_NUMBER: _ClassVar[int]
    OVERRIDE_DEPLOY_POLICY_FIELD_NUMBER: _ClassVar[int]
    name: str
    override_deploy_policy: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, name: _Optional[str]=..., override_deploy_policy: _Optional[_Iterable[str]]=...) -> None:
        ...

class TerminateJobRunResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class Config(_message.Message):
    __slots__ = ('name', 'supported_versions', 'default_skaffold_version')
    NAME_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_VERSIONS_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_SKAFFOLD_VERSION_FIELD_NUMBER: _ClassVar[int]
    name: str
    supported_versions: _containers.RepeatedCompositeFieldContainer[SkaffoldVersion]
    default_skaffold_version: str

    def __init__(self, name: _Optional[str]=..., supported_versions: _Optional[_Iterable[_Union[SkaffoldVersion, _Mapping]]]=..., default_skaffold_version: _Optional[str]=...) -> None:
        ...

class SkaffoldVersion(_message.Message):
    __slots__ = ('version', 'maintenance_mode_time', 'support_expiration_time', 'support_end_date')
    VERSION_FIELD_NUMBER: _ClassVar[int]
    MAINTENANCE_MODE_TIME_FIELD_NUMBER: _ClassVar[int]
    SUPPORT_EXPIRATION_TIME_FIELD_NUMBER: _ClassVar[int]
    SUPPORT_END_DATE_FIELD_NUMBER: _ClassVar[int]
    version: str
    maintenance_mode_time: _timestamp_pb2.Timestamp
    support_expiration_time: _timestamp_pb2.Timestamp
    support_end_date: _date_pb2.Date

    def __init__(self, version: _Optional[str]=..., maintenance_mode_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., support_expiration_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., support_end_date: _Optional[_Union[_date_pb2.Date, _Mapping]]=...) -> None:
        ...

class GetConfigRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class Automation(_message.Message):
    __slots__ = ('name', 'uid', 'description', 'create_time', 'update_time', 'annotations', 'labels', 'etag', 'suspended', 'service_account', 'selector', 'rules')

    class AnnotationsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    SUSPENDED_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    SELECTOR_FIELD_NUMBER: _ClassVar[int]
    RULES_FIELD_NUMBER: _ClassVar[int]
    name: str
    uid: str
    description: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    annotations: _containers.ScalarMap[str, str]
    labels: _containers.ScalarMap[str, str]
    etag: str
    suspended: bool
    service_account: str
    selector: AutomationResourceSelector
    rules: _containers.RepeatedCompositeFieldContainer[AutomationRule]

    def __init__(self, name: _Optional[str]=..., uid: _Optional[str]=..., description: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., annotations: _Optional[_Mapping[str, str]]=..., labels: _Optional[_Mapping[str, str]]=..., etag: _Optional[str]=..., suspended: bool=..., service_account: _Optional[str]=..., selector: _Optional[_Union[AutomationResourceSelector, _Mapping]]=..., rules: _Optional[_Iterable[_Union[AutomationRule, _Mapping]]]=...) -> None:
        ...

class AutomationResourceSelector(_message.Message):
    __slots__ = ('targets',)
    TARGETS_FIELD_NUMBER: _ClassVar[int]
    targets: _containers.RepeatedCompositeFieldContainer[TargetAttribute]

    def __init__(self, targets: _Optional[_Iterable[_Union[TargetAttribute, _Mapping]]]=...) -> None:
        ...

class AutomationRule(_message.Message):
    __slots__ = ('promote_release_rule', 'advance_rollout_rule', 'repair_rollout_rule', 'timed_promote_release_rule')
    PROMOTE_RELEASE_RULE_FIELD_NUMBER: _ClassVar[int]
    ADVANCE_ROLLOUT_RULE_FIELD_NUMBER: _ClassVar[int]
    REPAIR_ROLLOUT_RULE_FIELD_NUMBER: _ClassVar[int]
    TIMED_PROMOTE_RELEASE_RULE_FIELD_NUMBER: _ClassVar[int]
    promote_release_rule: PromoteReleaseRule
    advance_rollout_rule: AdvanceRolloutRule
    repair_rollout_rule: RepairRolloutRule
    timed_promote_release_rule: TimedPromoteReleaseRule

    def __init__(self, promote_release_rule: _Optional[_Union[PromoteReleaseRule, _Mapping]]=..., advance_rollout_rule: _Optional[_Union[AdvanceRolloutRule, _Mapping]]=..., repair_rollout_rule: _Optional[_Union[RepairRolloutRule, _Mapping]]=..., timed_promote_release_rule: _Optional[_Union[TimedPromoteReleaseRule, _Mapping]]=...) -> None:
        ...

class TimedPromoteReleaseRule(_message.Message):
    __slots__ = ('id', 'destination_target_id', 'schedule', 'time_zone', 'condition', 'destination_phase')
    ID_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    CONDITION_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_PHASE_FIELD_NUMBER: _ClassVar[int]
    id: str
    destination_target_id: str
    schedule: str
    time_zone: str
    condition: AutomationRuleCondition
    destination_phase: str

    def __init__(self, id: _Optional[str]=..., destination_target_id: _Optional[str]=..., schedule: _Optional[str]=..., time_zone: _Optional[str]=..., condition: _Optional[_Union[AutomationRuleCondition, _Mapping]]=..., destination_phase: _Optional[str]=...) -> None:
        ...

class PromoteReleaseRule(_message.Message):
    __slots__ = ('id', 'wait', 'destination_target_id', 'condition', 'destination_phase')
    ID_FIELD_NUMBER: _ClassVar[int]
    WAIT_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    CONDITION_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_PHASE_FIELD_NUMBER: _ClassVar[int]
    id: str
    wait: _duration_pb2.Duration
    destination_target_id: str
    condition: AutomationRuleCondition
    destination_phase: str

    def __init__(self, id: _Optional[str]=..., wait: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., destination_target_id: _Optional[str]=..., condition: _Optional[_Union[AutomationRuleCondition, _Mapping]]=..., destination_phase: _Optional[str]=...) -> None:
        ...

class AdvanceRolloutRule(_message.Message):
    __slots__ = ('id', 'source_phases', 'wait', 'condition')
    ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_PHASES_FIELD_NUMBER: _ClassVar[int]
    WAIT_FIELD_NUMBER: _ClassVar[int]
    CONDITION_FIELD_NUMBER: _ClassVar[int]
    id: str
    source_phases: _containers.RepeatedScalarFieldContainer[str]
    wait: _duration_pb2.Duration
    condition: AutomationRuleCondition

    def __init__(self, id: _Optional[str]=..., source_phases: _Optional[_Iterable[str]]=..., wait: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., condition: _Optional[_Union[AutomationRuleCondition, _Mapping]]=...) -> None:
        ...

class RepairRolloutRule(_message.Message):
    __slots__ = ('id', 'phases', 'jobs', 'condition', 'repair_phases')
    ID_FIELD_NUMBER: _ClassVar[int]
    PHASES_FIELD_NUMBER: _ClassVar[int]
    JOBS_FIELD_NUMBER: _ClassVar[int]
    CONDITION_FIELD_NUMBER: _ClassVar[int]
    REPAIR_PHASES_FIELD_NUMBER: _ClassVar[int]
    id: str
    phases: _containers.RepeatedScalarFieldContainer[str]
    jobs: _containers.RepeatedScalarFieldContainer[str]
    condition: AutomationRuleCondition
    repair_phases: _containers.RepeatedCompositeFieldContainer[RepairPhaseConfig]

    def __init__(self, id: _Optional[str]=..., phases: _Optional[_Iterable[str]]=..., jobs: _Optional[_Iterable[str]]=..., condition: _Optional[_Union[AutomationRuleCondition, _Mapping]]=..., repair_phases: _Optional[_Iterable[_Union[RepairPhaseConfig, _Mapping]]]=...) -> None:
        ...

class RepairPhaseConfig(_message.Message):
    __slots__ = ('retry', 'rollback')
    RETRY_FIELD_NUMBER: _ClassVar[int]
    ROLLBACK_FIELD_NUMBER: _ClassVar[int]
    retry: Retry
    rollback: Rollback

    def __init__(self, retry: _Optional[_Union[Retry, _Mapping]]=..., rollback: _Optional[_Union[Rollback, _Mapping]]=...) -> None:
        ...

class Retry(_message.Message):
    __slots__ = ('attempts', 'wait', 'backoff_mode')
    ATTEMPTS_FIELD_NUMBER: _ClassVar[int]
    WAIT_FIELD_NUMBER: _ClassVar[int]
    BACKOFF_MODE_FIELD_NUMBER: _ClassVar[int]
    attempts: int
    wait: _duration_pb2.Duration
    backoff_mode: BackoffMode

    def __init__(self, attempts: _Optional[int]=..., wait: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., backoff_mode: _Optional[_Union[BackoffMode, str]]=...) -> None:
        ...

class Rollback(_message.Message):
    __slots__ = ('destination_phase', 'disable_rollback_if_rollout_pending')
    DESTINATION_PHASE_FIELD_NUMBER: _ClassVar[int]
    DISABLE_ROLLBACK_IF_ROLLOUT_PENDING_FIELD_NUMBER: _ClassVar[int]
    destination_phase: str
    disable_rollback_if_rollout_pending: bool

    def __init__(self, destination_phase: _Optional[str]=..., disable_rollback_if_rollout_pending: bool=...) -> None:
        ...

class AutomationRuleCondition(_message.Message):
    __slots__ = ('targets_present_condition', 'timed_promote_release_condition')
    TARGETS_PRESENT_CONDITION_FIELD_NUMBER: _ClassVar[int]
    TIMED_PROMOTE_RELEASE_CONDITION_FIELD_NUMBER: _ClassVar[int]
    targets_present_condition: TargetsPresentCondition
    timed_promote_release_condition: TimedPromoteReleaseCondition

    def __init__(self, targets_present_condition: _Optional[_Union[TargetsPresentCondition, _Mapping]]=..., timed_promote_release_condition: _Optional[_Union[TimedPromoteReleaseCondition, _Mapping]]=...) -> None:
        ...

class TimedPromoteReleaseCondition(_message.Message):
    __slots__ = ('next_promotion_time', 'targets_list')

    class Targets(_message.Message):
        __slots__ = ('source_target_id', 'destination_target_id')
        SOURCE_TARGET_ID_FIELD_NUMBER: _ClassVar[int]
        DESTINATION_TARGET_ID_FIELD_NUMBER: _ClassVar[int]
        source_target_id: str
        destination_target_id: str

        def __init__(self, source_target_id: _Optional[str]=..., destination_target_id: _Optional[str]=...) -> None:
            ...
    NEXT_PROMOTION_TIME_FIELD_NUMBER: _ClassVar[int]
    TARGETS_LIST_FIELD_NUMBER: _ClassVar[int]
    next_promotion_time: _timestamp_pb2.Timestamp
    targets_list: _containers.RepeatedCompositeFieldContainer[TimedPromoteReleaseCondition.Targets]

    def __init__(self, next_promotion_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., targets_list: _Optional[_Iterable[_Union[TimedPromoteReleaseCondition.Targets, _Mapping]]]=...) -> None:
        ...

class CreateAutomationRequest(_message.Message):
    __slots__ = ('parent', 'automation_id', 'automation', 'request_id', 'validate_only')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    AUTOMATION_ID_FIELD_NUMBER: _ClassVar[int]
    AUTOMATION_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    automation_id: str
    automation: Automation
    request_id: str
    validate_only: bool

    def __init__(self, parent: _Optional[str]=..., automation_id: _Optional[str]=..., automation: _Optional[_Union[Automation, _Mapping]]=..., request_id: _Optional[str]=..., validate_only: bool=...) -> None:
        ...

class UpdateAutomationRequest(_message.Message):
    __slots__ = ('update_mask', 'automation', 'request_id', 'allow_missing', 'validate_only')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    AUTOMATION_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MISSING_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    automation: Automation
    request_id: str
    allow_missing: bool
    validate_only: bool

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., automation: _Optional[_Union[Automation, _Mapping]]=..., request_id: _Optional[str]=..., allow_missing: bool=..., validate_only: bool=...) -> None:
        ...

class DeleteAutomationRequest(_message.Message):
    __slots__ = ('name', 'request_id', 'allow_missing', 'validate_only', 'etag')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MISSING_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str
    allow_missing: bool
    validate_only: bool
    etag: str

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=..., allow_missing: bool=..., validate_only: bool=..., etag: _Optional[str]=...) -> None:
        ...

class ListAutomationsRequest(_message.Message):
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

class ListAutomationsResponse(_message.Message):
    __slots__ = ('automations', 'next_page_token', 'unreachable')
    AUTOMATIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    automations: _containers.RepeatedCompositeFieldContainer[Automation]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, automations: _Optional[_Iterable[_Union[Automation, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetAutomationRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class AutomationRun(_message.Message):
    __slots__ = ('name', 'create_time', 'update_time', 'etag', 'service_account', 'automation_snapshot', 'target_id', 'state', 'state_description', 'policy_violation', 'expire_time', 'rule_id', 'automation_id', 'promote_release_operation', 'advance_rollout_operation', 'repair_rollout_operation', 'timed_promote_release_operation', 'wait_until_time')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[AutomationRun.State]
        SUCCEEDED: _ClassVar[AutomationRun.State]
        CANCELLED: _ClassVar[AutomationRun.State]
        FAILED: _ClassVar[AutomationRun.State]
        IN_PROGRESS: _ClassVar[AutomationRun.State]
        PENDING: _ClassVar[AutomationRun.State]
        ABORTED: _ClassVar[AutomationRun.State]
    STATE_UNSPECIFIED: AutomationRun.State
    SUCCEEDED: AutomationRun.State
    CANCELLED: AutomationRun.State
    FAILED: AutomationRun.State
    IN_PROGRESS: AutomationRun.State
    PENDING: AutomationRun.State
    ABORTED: AutomationRun.State
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    AUTOMATION_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATE_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    POLICY_VIOLATION_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
    RULE_ID_FIELD_NUMBER: _ClassVar[int]
    AUTOMATION_ID_FIELD_NUMBER: _ClassVar[int]
    PROMOTE_RELEASE_OPERATION_FIELD_NUMBER: _ClassVar[int]
    ADVANCE_ROLLOUT_OPERATION_FIELD_NUMBER: _ClassVar[int]
    REPAIR_ROLLOUT_OPERATION_FIELD_NUMBER: _ClassVar[int]
    TIMED_PROMOTE_RELEASE_OPERATION_FIELD_NUMBER: _ClassVar[int]
    WAIT_UNTIL_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    etag: str
    service_account: str
    automation_snapshot: Automation
    target_id: str
    state: AutomationRun.State
    state_description: str
    policy_violation: PolicyViolation
    expire_time: _timestamp_pb2.Timestamp
    rule_id: str
    automation_id: str
    promote_release_operation: PromoteReleaseOperation
    advance_rollout_operation: AdvanceRolloutOperation
    repair_rollout_operation: RepairRolloutOperation
    timed_promote_release_operation: TimedPromoteReleaseOperation
    wait_until_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., etag: _Optional[str]=..., service_account: _Optional[str]=..., automation_snapshot: _Optional[_Union[Automation, _Mapping]]=..., target_id: _Optional[str]=..., state: _Optional[_Union[AutomationRun.State, str]]=..., state_description: _Optional[str]=..., policy_violation: _Optional[_Union[PolicyViolation, _Mapping]]=..., expire_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., rule_id: _Optional[str]=..., automation_id: _Optional[str]=..., promote_release_operation: _Optional[_Union[PromoteReleaseOperation, _Mapping]]=..., advance_rollout_operation: _Optional[_Union[AdvanceRolloutOperation, _Mapping]]=..., repair_rollout_operation: _Optional[_Union[RepairRolloutOperation, _Mapping]]=..., timed_promote_release_operation: _Optional[_Union[TimedPromoteReleaseOperation, _Mapping]]=..., wait_until_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class PromoteReleaseOperation(_message.Message):
    __slots__ = ('target_id', 'wait', 'rollout', 'phase')
    TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    WAIT_FIELD_NUMBER: _ClassVar[int]
    ROLLOUT_FIELD_NUMBER: _ClassVar[int]
    PHASE_FIELD_NUMBER: _ClassVar[int]
    target_id: str
    wait: _duration_pb2.Duration
    rollout: str
    phase: str

    def __init__(self, target_id: _Optional[str]=..., wait: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., rollout: _Optional[str]=..., phase: _Optional[str]=...) -> None:
        ...

class AdvanceRolloutOperation(_message.Message):
    __slots__ = ('source_phase', 'wait', 'rollout', 'destination_phase')
    SOURCE_PHASE_FIELD_NUMBER: _ClassVar[int]
    WAIT_FIELD_NUMBER: _ClassVar[int]
    ROLLOUT_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_PHASE_FIELD_NUMBER: _ClassVar[int]
    source_phase: str
    wait: _duration_pb2.Duration
    rollout: str
    destination_phase: str

    def __init__(self, source_phase: _Optional[str]=..., wait: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., rollout: _Optional[str]=..., destination_phase: _Optional[str]=...) -> None:
        ...

class RepairRolloutOperation(_message.Message):
    __slots__ = ('rollout', 'current_repair_phase_index', 'repair_phases', 'phase_id', 'job_id')
    ROLLOUT_FIELD_NUMBER: _ClassVar[int]
    CURRENT_REPAIR_PHASE_INDEX_FIELD_NUMBER: _ClassVar[int]
    REPAIR_PHASES_FIELD_NUMBER: _ClassVar[int]
    PHASE_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    rollout: str
    current_repair_phase_index: int
    repair_phases: _containers.RepeatedCompositeFieldContainer[RepairPhase]
    phase_id: str
    job_id: str

    def __init__(self, rollout: _Optional[str]=..., current_repair_phase_index: _Optional[int]=..., repair_phases: _Optional[_Iterable[_Union[RepairPhase, _Mapping]]]=..., phase_id: _Optional[str]=..., job_id: _Optional[str]=...) -> None:
        ...

class TimedPromoteReleaseOperation(_message.Message):
    __slots__ = ('target_id', 'release', 'phase')
    TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    RELEASE_FIELD_NUMBER: _ClassVar[int]
    PHASE_FIELD_NUMBER: _ClassVar[int]
    target_id: str
    release: str
    phase: str

    def __init__(self, target_id: _Optional[str]=..., release: _Optional[str]=..., phase: _Optional[str]=...) -> None:
        ...

class RepairPhase(_message.Message):
    __slots__ = ('retry', 'rollback')
    RETRY_FIELD_NUMBER: _ClassVar[int]
    ROLLBACK_FIELD_NUMBER: _ClassVar[int]
    retry: RetryPhase
    rollback: RollbackAttempt

    def __init__(self, retry: _Optional[_Union[RetryPhase, _Mapping]]=..., rollback: _Optional[_Union[RollbackAttempt, _Mapping]]=...) -> None:
        ...

class RetryPhase(_message.Message):
    __slots__ = ('total_attempts', 'backoff_mode', 'attempts')
    TOTAL_ATTEMPTS_FIELD_NUMBER: _ClassVar[int]
    BACKOFF_MODE_FIELD_NUMBER: _ClassVar[int]
    ATTEMPTS_FIELD_NUMBER: _ClassVar[int]
    total_attempts: int
    backoff_mode: BackoffMode
    attempts: _containers.RepeatedCompositeFieldContainer[RetryAttempt]

    def __init__(self, total_attempts: _Optional[int]=..., backoff_mode: _Optional[_Union[BackoffMode, str]]=..., attempts: _Optional[_Iterable[_Union[RetryAttempt, _Mapping]]]=...) -> None:
        ...

class RetryAttempt(_message.Message):
    __slots__ = ('attempt', 'wait', 'state', 'state_desc')
    ATTEMPT_FIELD_NUMBER: _ClassVar[int]
    WAIT_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATE_DESC_FIELD_NUMBER: _ClassVar[int]
    attempt: int
    wait: _duration_pb2.Duration
    state: RepairState
    state_desc: str

    def __init__(self, attempt: _Optional[int]=..., wait: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., state: _Optional[_Union[RepairState, str]]=..., state_desc: _Optional[str]=...) -> None:
        ...

class RollbackAttempt(_message.Message):
    __slots__ = ('destination_phase', 'rollout_id', 'state', 'state_desc', 'disable_rollback_if_rollout_pending')
    DESTINATION_PHASE_FIELD_NUMBER: _ClassVar[int]
    ROLLOUT_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATE_DESC_FIELD_NUMBER: _ClassVar[int]
    DISABLE_ROLLBACK_IF_ROLLOUT_PENDING_FIELD_NUMBER: _ClassVar[int]
    destination_phase: str
    rollout_id: str
    state: RepairState
    state_desc: str
    disable_rollback_if_rollout_pending: bool

    def __init__(self, destination_phase: _Optional[str]=..., rollout_id: _Optional[str]=..., state: _Optional[_Union[RepairState, str]]=..., state_desc: _Optional[str]=..., disable_rollback_if_rollout_pending: bool=...) -> None:
        ...

class ListAutomationRunsRequest(_message.Message):
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

class ListAutomationRunsResponse(_message.Message):
    __slots__ = ('automation_runs', 'next_page_token', 'unreachable')
    AUTOMATION_RUNS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    automation_runs: _containers.RepeatedCompositeFieldContainer[AutomationRun]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, automation_runs: _Optional[_Iterable[_Union[AutomationRun, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetAutomationRunRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CancelAutomationRunRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CancelAutomationRunResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...