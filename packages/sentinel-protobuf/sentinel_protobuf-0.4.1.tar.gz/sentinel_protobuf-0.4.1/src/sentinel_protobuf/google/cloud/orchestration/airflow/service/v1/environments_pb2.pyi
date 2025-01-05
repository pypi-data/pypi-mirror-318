from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.orchestration.airflow.service.v1 import operations_pb2 as _operations_pb2
from google.longrunning import operations_pb2 as _operations_pb2_1
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CreateEnvironmentRequest(_message.Message):
    __slots__ = ('parent', 'environment')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    parent: str
    environment: Environment

    def __init__(self, parent: _Optional[str]=..., environment: _Optional[_Union[Environment, _Mapping]]=...) -> None:
        ...

class GetEnvironmentRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListEnvironmentsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListEnvironmentsResponse(_message.Message):
    __slots__ = ('environments', 'next_page_token')
    ENVIRONMENTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    environments: _containers.RepeatedCompositeFieldContainer[Environment]
    next_page_token: str

    def __init__(self, environments: _Optional[_Iterable[_Union[Environment, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class DeleteEnvironmentRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateEnvironmentRequest(_message.Message):
    __slots__ = ('name', 'environment', 'update_mask')
    NAME_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    name: str
    environment: Environment
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, name: _Optional[str]=..., environment: _Optional[_Union[Environment, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class ExecuteAirflowCommandRequest(_message.Message):
    __slots__ = ('environment', 'command', 'subcommand', 'parameters')
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    SUBCOMMAND_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    environment: str
    command: str
    subcommand: str
    parameters: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, environment: _Optional[str]=..., command: _Optional[str]=..., subcommand: _Optional[str]=..., parameters: _Optional[_Iterable[str]]=...) -> None:
        ...

class ExecuteAirflowCommandResponse(_message.Message):
    __slots__ = ('execution_id', 'pod', 'pod_namespace', 'error')
    EXECUTION_ID_FIELD_NUMBER: _ClassVar[int]
    POD_FIELD_NUMBER: _ClassVar[int]
    POD_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    execution_id: str
    pod: str
    pod_namespace: str
    error: str

    def __init__(self, execution_id: _Optional[str]=..., pod: _Optional[str]=..., pod_namespace: _Optional[str]=..., error: _Optional[str]=...) -> None:
        ...

class StopAirflowCommandRequest(_message.Message):
    __slots__ = ('environment', 'execution_id', 'pod', 'pod_namespace', 'force')
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_ID_FIELD_NUMBER: _ClassVar[int]
    POD_FIELD_NUMBER: _ClassVar[int]
    POD_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    environment: str
    execution_id: str
    pod: str
    pod_namespace: str
    force: bool

    def __init__(self, environment: _Optional[str]=..., execution_id: _Optional[str]=..., pod: _Optional[str]=..., pod_namespace: _Optional[str]=..., force: bool=...) -> None:
        ...

class StopAirflowCommandResponse(_message.Message):
    __slots__ = ('is_done', 'output')
    IS_DONE_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_FIELD_NUMBER: _ClassVar[int]
    is_done: bool
    output: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, is_done: bool=..., output: _Optional[_Iterable[str]]=...) -> None:
        ...

class PollAirflowCommandRequest(_message.Message):
    __slots__ = ('environment', 'execution_id', 'pod', 'pod_namespace', 'next_line_number')
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_ID_FIELD_NUMBER: _ClassVar[int]
    POD_FIELD_NUMBER: _ClassVar[int]
    POD_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    NEXT_LINE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    environment: str
    execution_id: str
    pod: str
    pod_namespace: str
    next_line_number: int

    def __init__(self, environment: _Optional[str]=..., execution_id: _Optional[str]=..., pod: _Optional[str]=..., pod_namespace: _Optional[str]=..., next_line_number: _Optional[int]=...) -> None:
        ...

class PollAirflowCommandResponse(_message.Message):
    __slots__ = ('output', 'output_end', 'exit_info')

    class Line(_message.Message):
        __slots__ = ('line_number', 'content')
        LINE_NUMBER_FIELD_NUMBER: _ClassVar[int]
        CONTENT_FIELD_NUMBER: _ClassVar[int]
        line_number: int
        content: str

        def __init__(self, line_number: _Optional[int]=..., content: _Optional[str]=...) -> None:
            ...

    class ExitInfo(_message.Message):
        __slots__ = ('exit_code', 'error')
        EXIT_CODE_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        exit_code: int
        error: str

        def __init__(self, exit_code: _Optional[int]=..., error: _Optional[str]=...) -> None:
            ...
    OUTPUT_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_END_FIELD_NUMBER: _ClassVar[int]
    EXIT_INFO_FIELD_NUMBER: _ClassVar[int]
    output: _containers.RepeatedCompositeFieldContainer[PollAirflowCommandResponse.Line]
    output_end: bool
    exit_info: PollAirflowCommandResponse.ExitInfo

    def __init__(self, output: _Optional[_Iterable[_Union[PollAirflowCommandResponse.Line, _Mapping]]]=..., output_end: bool=..., exit_info: _Optional[_Union[PollAirflowCommandResponse.ExitInfo, _Mapping]]=...) -> None:
        ...

class CreateUserWorkloadsSecretRequest(_message.Message):
    __slots__ = ('parent', 'user_workloads_secret')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    USER_WORKLOADS_SECRET_FIELD_NUMBER: _ClassVar[int]
    parent: str
    user_workloads_secret: UserWorkloadsSecret

    def __init__(self, parent: _Optional[str]=..., user_workloads_secret: _Optional[_Union[UserWorkloadsSecret, _Mapping]]=...) -> None:
        ...

class GetUserWorkloadsSecretRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListUserWorkloadsSecretsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class UpdateUserWorkloadsSecretRequest(_message.Message):
    __slots__ = ('user_workloads_secret',)
    USER_WORKLOADS_SECRET_FIELD_NUMBER: _ClassVar[int]
    user_workloads_secret: UserWorkloadsSecret

    def __init__(self, user_workloads_secret: _Optional[_Union[UserWorkloadsSecret, _Mapping]]=...) -> None:
        ...

class DeleteUserWorkloadsSecretRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateUserWorkloadsConfigMapRequest(_message.Message):
    __slots__ = ('parent', 'user_workloads_config_map')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    USER_WORKLOADS_CONFIG_MAP_FIELD_NUMBER: _ClassVar[int]
    parent: str
    user_workloads_config_map: UserWorkloadsConfigMap

    def __init__(self, parent: _Optional[str]=..., user_workloads_config_map: _Optional[_Union[UserWorkloadsConfigMap, _Mapping]]=...) -> None:
        ...

class GetUserWorkloadsConfigMapRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListUserWorkloadsConfigMapsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class UpdateUserWorkloadsConfigMapRequest(_message.Message):
    __slots__ = ('user_workloads_config_map',)
    USER_WORKLOADS_CONFIG_MAP_FIELD_NUMBER: _ClassVar[int]
    user_workloads_config_map: UserWorkloadsConfigMap

    def __init__(self, user_workloads_config_map: _Optional[_Union[UserWorkloadsConfigMap, _Mapping]]=...) -> None:
        ...

class DeleteUserWorkloadsConfigMapRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UserWorkloadsSecret(_message.Message):
    __slots__ = ('name', 'data')

    class DataEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    name: str
    data: _containers.ScalarMap[str, str]

    def __init__(self, name: _Optional[str]=..., data: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class ListUserWorkloadsSecretsResponse(_message.Message):
    __slots__ = ('user_workloads_secrets', 'next_page_token')
    USER_WORKLOADS_SECRETS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    user_workloads_secrets: _containers.RepeatedCompositeFieldContainer[UserWorkloadsSecret]
    next_page_token: str

    def __init__(self, user_workloads_secrets: _Optional[_Iterable[_Union[UserWorkloadsSecret, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class UserWorkloadsConfigMap(_message.Message):
    __slots__ = ('name', 'data')

    class DataEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    name: str
    data: _containers.ScalarMap[str, str]

    def __init__(self, name: _Optional[str]=..., data: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class ListUserWorkloadsConfigMapsResponse(_message.Message):
    __slots__ = ('user_workloads_config_maps', 'next_page_token')
    USER_WORKLOADS_CONFIG_MAPS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    user_workloads_config_maps: _containers.RepeatedCompositeFieldContainer[UserWorkloadsConfigMap]
    next_page_token: str

    def __init__(self, user_workloads_config_maps: _Optional[_Iterable[_Union[UserWorkloadsConfigMap, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class ListWorkloadsRequest(_message.Message):
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

class ListWorkloadsResponse(_message.Message):
    __slots__ = ('workloads', 'next_page_token')

    class ComposerWorkloadType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        COMPOSER_WORKLOAD_TYPE_UNSPECIFIED: _ClassVar[ListWorkloadsResponse.ComposerWorkloadType]
        CELERY_WORKER: _ClassVar[ListWorkloadsResponse.ComposerWorkloadType]
        KUBERNETES_WORKER: _ClassVar[ListWorkloadsResponse.ComposerWorkloadType]
        KUBERNETES_OPERATOR_POD: _ClassVar[ListWorkloadsResponse.ComposerWorkloadType]
        SCHEDULER: _ClassVar[ListWorkloadsResponse.ComposerWorkloadType]
        DAG_PROCESSOR: _ClassVar[ListWorkloadsResponse.ComposerWorkloadType]
        TRIGGERER: _ClassVar[ListWorkloadsResponse.ComposerWorkloadType]
        WEB_SERVER: _ClassVar[ListWorkloadsResponse.ComposerWorkloadType]
        REDIS: _ClassVar[ListWorkloadsResponse.ComposerWorkloadType]
    COMPOSER_WORKLOAD_TYPE_UNSPECIFIED: ListWorkloadsResponse.ComposerWorkloadType
    CELERY_WORKER: ListWorkloadsResponse.ComposerWorkloadType
    KUBERNETES_WORKER: ListWorkloadsResponse.ComposerWorkloadType
    KUBERNETES_OPERATOR_POD: ListWorkloadsResponse.ComposerWorkloadType
    SCHEDULER: ListWorkloadsResponse.ComposerWorkloadType
    DAG_PROCESSOR: ListWorkloadsResponse.ComposerWorkloadType
    TRIGGERER: ListWorkloadsResponse.ComposerWorkloadType
    WEB_SERVER: ListWorkloadsResponse.ComposerWorkloadType
    REDIS: ListWorkloadsResponse.ComposerWorkloadType

    class ComposerWorkloadState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        COMPOSER_WORKLOAD_STATE_UNSPECIFIED: _ClassVar[ListWorkloadsResponse.ComposerWorkloadState]
        PENDING: _ClassVar[ListWorkloadsResponse.ComposerWorkloadState]
        OK: _ClassVar[ListWorkloadsResponse.ComposerWorkloadState]
        WARNING: _ClassVar[ListWorkloadsResponse.ComposerWorkloadState]
        ERROR: _ClassVar[ListWorkloadsResponse.ComposerWorkloadState]
        SUCCEEDED: _ClassVar[ListWorkloadsResponse.ComposerWorkloadState]
        FAILED: _ClassVar[ListWorkloadsResponse.ComposerWorkloadState]
    COMPOSER_WORKLOAD_STATE_UNSPECIFIED: ListWorkloadsResponse.ComposerWorkloadState
    PENDING: ListWorkloadsResponse.ComposerWorkloadState
    OK: ListWorkloadsResponse.ComposerWorkloadState
    WARNING: ListWorkloadsResponse.ComposerWorkloadState
    ERROR: ListWorkloadsResponse.ComposerWorkloadState
    SUCCEEDED: ListWorkloadsResponse.ComposerWorkloadState
    FAILED: ListWorkloadsResponse.ComposerWorkloadState

    class ComposerWorkload(_message.Message):
        __slots__ = ('name', 'type', 'status')
        NAME_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        name: str
        type: ListWorkloadsResponse.ComposerWorkloadType
        status: ListWorkloadsResponse.ComposerWorkloadStatus

        def __init__(self, name: _Optional[str]=..., type: _Optional[_Union[ListWorkloadsResponse.ComposerWorkloadType, str]]=..., status: _Optional[_Union[ListWorkloadsResponse.ComposerWorkloadStatus, _Mapping]]=...) -> None:
            ...

    class ComposerWorkloadStatus(_message.Message):
        __slots__ = ('state', 'status_message', 'detailed_status_message')
        STATE_FIELD_NUMBER: _ClassVar[int]
        STATUS_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        DETAILED_STATUS_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        state: ListWorkloadsResponse.ComposerWorkloadState
        status_message: str
        detailed_status_message: str

        def __init__(self, state: _Optional[_Union[ListWorkloadsResponse.ComposerWorkloadState, str]]=..., status_message: _Optional[str]=..., detailed_status_message: _Optional[str]=...) -> None:
            ...
    WORKLOADS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    workloads: _containers.RepeatedCompositeFieldContainer[ListWorkloadsResponse.ComposerWorkload]
    next_page_token: str

    def __init__(self, workloads: _Optional[_Iterable[_Union[ListWorkloadsResponse.ComposerWorkload, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class SaveSnapshotRequest(_message.Message):
    __slots__ = ('environment', 'snapshot_location')
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_LOCATION_FIELD_NUMBER: _ClassVar[int]
    environment: str
    snapshot_location: str

    def __init__(self, environment: _Optional[str]=..., snapshot_location: _Optional[str]=...) -> None:
        ...

class SaveSnapshotResponse(_message.Message):
    __slots__ = ('snapshot_path',)
    SNAPSHOT_PATH_FIELD_NUMBER: _ClassVar[int]
    snapshot_path: str

    def __init__(self, snapshot_path: _Optional[str]=...) -> None:
        ...

class LoadSnapshotRequest(_message.Message):
    __slots__ = ('environment', 'snapshot_path', 'skip_pypi_packages_installation', 'skip_environment_variables_setting', 'skip_airflow_overrides_setting', 'skip_gcs_data_copying')
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_PATH_FIELD_NUMBER: _ClassVar[int]
    SKIP_PYPI_PACKAGES_INSTALLATION_FIELD_NUMBER: _ClassVar[int]
    SKIP_ENVIRONMENT_VARIABLES_SETTING_FIELD_NUMBER: _ClassVar[int]
    SKIP_AIRFLOW_OVERRIDES_SETTING_FIELD_NUMBER: _ClassVar[int]
    SKIP_GCS_DATA_COPYING_FIELD_NUMBER: _ClassVar[int]
    environment: str
    snapshot_path: str
    skip_pypi_packages_installation: bool
    skip_environment_variables_setting: bool
    skip_airflow_overrides_setting: bool
    skip_gcs_data_copying: bool

    def __init__(self, environment: _Optional[str]=..., snapshot_path: _Optional[str]=..., skip_pypi_packages_installation: bool=..., skip_environment_variables_setting: bool=..., skip_airflow_overrides_setting: bool=..., skip_gcs_data_copying: bool=...) -> None:
        ...

class LoadSnapshotResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class DatabaseFailoverRequest(_message.Message):
    __slots__ = ('environment',)
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    environment: str

    def __init__(self, environment: _Optional[str]=...) -> None:
        ...

class DatabaseFailoverResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class FetchDatabasePropertiesRequest(_message.Message):
    __slots__ = ('environment',)
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    environment: str

    def __init__(self, environment: _Optional[str]=...) -> None:
        ...

class FetchDatabasePropertiesResponse(_message.Message):
    __slots__ = ('primary_gce_zone', 'secondary_gce_zone', 'is_failover_replica_available')
    PRIMARY_GCE_ZONE_FIELD_NUMBER: _ClassVar[int]
    SECONDARY_GCE_ZONE_FIELD_NUMBER: _ClassVar[int]
    IS_FAILOVER_REPLICA_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    primary_gce_zone: str
    secondary_gce_zone: str
    is_failover_replica_available: bool

    def __init__(self, primary_gce_zone: _Optional[str]=..., secondary_gce_zone: _Optional[str]=..., is_failover_replica_available: bool=...) -> None:
        ...

class StorageConfig(_message.Message):
    __slots__ = ('bucket',)
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    bucket: str

    def __init__(self, bucket: _Optional[str]=...) -> None:
        ...

class EnvironmentConfig(_message.Message):
    __slots__ = ('gke_cluster', 'dag_gcs_prefix', 'node_count', 'software_config', 'node_config', 'private_environment_config', 'web_server_network_access_control', 'database_config', 'web_server_config', 'encryption_config', 'maintenance_window', 'workloads_config', 'environment_size', 'airflow_uri', 'airflow_byoid_uri', 'master_authorized_networks_config', 'recovery_config', 'resilience_mode', 'data_retention_config')

    class EnvironmentSize(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ENVIRONMENT_SIZE_UNSPECIFIED: _ClassVar[EnvironmentConfig.EnvironmentSize]
        ENVIRONMENT_SIZE_SMALL: _ClassVar[EnvironmentConfig.EnvironmentSize]
        ENVIRONMENT_SIZE_MEDIUM: _ClassVar[EnvironmentConfig.EnvironmentSize]
        ENVIRONMENT_SIZE_LARGE: _ClassVar[EnvironmentConfig.EnvironmentSize]
    ENVIRONMENT_SIZE_UNSPECIFIED: EnvironmentConfig.EnvironmentSize
    ENVIRONMENT_SIZE_SMALL: EnvironmentConfig.EnvironmentSize
    ENVIRONMENT_SIZE_MEDIUM: EnvironmentConfig.EnvironmentSize
    ENVIRONMENT_SIZE_LARGE: EnvironmentConfig.EnvironmentSize

    class ResilienceMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RESILIENCE_MODE_UNSPECIFIED: _ClassVar[EnvironmentConfig.ResilienceMode]
        HIGH_RESILIENCE: _ClassVar[EnvironmentConfig.ResilienceMode]
    RESILIENCE_MODE_UNSPECIFIED: EnvironmentConfig.ResilienceMode
    HIGH_RESILIENCE: EnvironmentConfig.ResilienceMode
    GKE_CLUSTER_FIELD_NUMBER: _ClassVar[int]
    DAG_GCS_PREFIX_FIELD_NUMBER: _ClassVar[int]
    NODE_COUNT_FIELD_NUMBER: _ClassVar[int]
    SOFTWARE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    NODE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_ENVIRONMENT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    WEB_SERVER_NETWORK_ACCESS_CONTROL_FIELD_NUMBER: _ClassVar[int]
    DATABASE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    WEB_SERVER_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    MAINTENANCE_WINDOW_FIELD_NUMBER: _ClassVar[int]
    WORKLOADS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_SIZE_FIELD_NUMBER: _ClassVar[int]
    AIRFLOW_URI_FIELD_NUMBER: _ClassVar[int]
    AIRFLOW_BYOID_URI_FIELD_NUMBER: _ClassVar[int]
    MASTER_AUTHORIZED_NETWORKS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    RECOVERY_CONFIG_FIELD_NUMBER: _ClassVar[int]
    RESILIENCE_MODE_FIELD_NUMBER: _ClassVar[int]
    DATA_RETENTION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    gke_cluster: str
    dag_gcs_prefix: str
    node_count: int
    software_config: SoftwareConfig
    node_config: NodeConfig
    private_environment_config: PrivateEnvironmentConfig
    web_server_network_access_control: WebServerNetworkAccessControl
    database_config: DatabaseConfig
    web_server_config: WebServerConfig
    encryption_config: EncryptionConfig
    maintenance_window: MaintenanceWindow
    workloads_config: WorkloadsConfig
    environment_size: EnvironmentConfig.EnvironmentSize
    airflow_uri: str
    airflow_byoid_uri: str
    master_authorized_networks_config: MasterAuthorizedNetworksConfig
    recovery_config: RecoveryConfig
    resilience_mode: EnvironmentConfig.ResilienceMode
    data_retention_config: DataRetentionConfig

    def __init__(self, gke_cluster: _Optional[str]=..., dag_gcs_prefix: _Optional[str]=..., node_count: _Optional[int]=..., software_config: _Optional[_Union[SoftwareConfig, _Mapping]]=..., node_config: _Optional[_Union[NodeConfig, _Mapping]]=..., private_environment_config: _Optional[_Union[PrivateEnvironmentConfig, _Mapping]]=..., web_server_network_access_control: _Optional[_Union[WebServerNetworkAccessControl, _Mapping]]=..., database_config: _Optional[_Union[DatabaseConfig, _Mapping]]=..., web_server_config: _Optional[_Union[WebServerConfig, _Mapping]]=..., encryption_config: _Optional[_Union[EncryptionConfig, _Mapping]]=..., maintenance_window: _Optional[_Union[MaintenanceWindow, _Mapping]]=..., workloads_config: _Optional[_Union[WorkloadsConfig, _Mapping]]=..., environment_size: _Optional[_Union[EnvironmentConfig.EnvironmentSize, str]]=..., airflow_uri: _Optional[str]=..., airflow_byoid_uri: _Optional[str]=..., master_authorized_networks_config: _Optional[_Union[MasterAuthorizedNetworksConfig, _Mapping]]=..., recovery_config: _Optional[_Union[RecoveryConfig, _Mapping]]=..., resilience_mode: _Optional[_Union[EnvironmentConfig.ResilienceMode, str]]=..., data_retention_config: _Optional[_Union[DataRetentionConfig, _Mapping]]=...) -> None:
        ...

class WebServerNetworkAccessControl(_message.Message):
    __slots__ = ('allowed_ip_ranges',)

    class AllowedIpRange(_message.Message):
        __slots__ = ('value', 'description')
        VALUE_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        value: str
        description: str

        def __init__(self, value: _Optional[str]=..., description: _Optional[str]=...) -> None:
            ...
    ALLOWED_IP_RANGES_FIELD_NUMBER: _ClassVar[int]
    allowed_ip_ranges: _containers.RepeatedCompositeFieldContainer[WebServerNetworkAccessControl.AllowedIpRange]

    def __init__(self, allowed_ip_ranges: _Optional[_Iterable[_Union[WebServerNetworkAccessControl.AllowedIpRange, _Mapping]]]=...) -> None:
        ...

class DatabaseConfig(_message.Message):
    __slots__ = ('machine_type', 'zone')
    MACHINE_TYPE_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    machine_type: str
    zone: str

    def __init__(self, machine_type: _Optional[str]=..., zone: _Optional[str]=...) -> None:
        ...

class WebServerConfig(_message.Message):
    __slots__ = ('machine_type',)
    MACHINE_TYPE_FIELD_NUMBER: _ClassVar[int]
    machine_type: str

    def __init__(self, machine_type: _Optional[str]=...) -> None:
        ...

class EncryptionConfig(_message.Message):
    __slots__ = ('kms_key_name',)
    KMS_KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    kms_key_name: str

    def __init__(self, kms_key_name: _Optional[str]=...) -> None:
        ...

class MaintenanceWindow(_message.Message):
    __slots__ = ('start_time', 'end_time', 'recurrence')
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    RECURRENCE_FIELD_NUMBER: _ClassVar[int]
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    recurrence: str

    def __init__(self, start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., recurrence: _Optional[str]=...) -> None:
        ...

class SoftwareConfig(_message.Message):
    __slots__ = ('image_version', 'airflow_config_overrides', 'pypi_packages', 'env_variables', 'python_version', 'scheduler_count', 'cloud_data_lineage_integration', 'web_server_plugins_mode')

    class WebServerPluginsMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        WEB_SERVER_PLUGINS_MODE_UNSPECIFIED: _ClassVar[SoftwareConfig.WebServerPluginsMode]
        PLUGINS_DISABLED: _ClassVar[SoftwareConfig.WebServerPluginsMode]
        PLUGINS_ENABLED: _ClassVar[SoftwareConfig.WebServerPluginsMode]
    WEB_SERVER_PLUGINS_MODE_UNSPECIFIED: SoftwareConfig.WebServerPluginsMode
    PLUGINS_DISABLED: SoftwareConfig.WebServerPluginsMode
    PLUGINS_ENABLED: SoftwareConfig.WebServerPluginsMode

    class AirflowConfigOverridesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...

    class PypiPackagesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...

    class EnvVariablesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    IMAGE_VERSION_FIELD_NUMBER: _ClassVar[int]
    AIRFLOW_CONFIG_OVERRIDES_FIELD_NUMBER: _ClassVar[int]
    PYPI_PACKAGES_FIELD_NUMBER: _ClassVar[int]
    ENV_VARIABLES_FIELD_NUMBER: _ClassVar[int]
    PYTHON_VERSION_FIELD_NUMBER: _ClassVar[int]
    SCHEDULER_COUNT_FIELD_NUMBER: _ClassVar[int]
    CLOUD_DATA_LINEAGE_INTEGRATION_FIELD_NUMBER: _ClassVar[int]
    WEB_SERVER_PLUGINS_MODE_FIELD_NUMBER: _ClassVar[int]
    image_version: str
    airflow_config_overrides: _containers.ScalarMap[str, str]
    pypi_packages: _containers.ScalarMap[str, str]
    env_variables: _containers.ScalarMap[str, str]
    python_version: str
    scheduler_count: int
    cloud_data_lineage_integration: CloudDataLineageIntegration
    web_server_plugins_mode: SoftwareConfig.WebServerPluginsMode

    def __init__(self, image_version: _Optional[str]=..., airflow_config_overrides: _Optional[_Mapping[str, str]]=..., pypi_packages: _Optional[_Mapping[str, str]]=..., env_variables: _Optional[_Mapping[str, str]]=..., python_version: _Optional[str]=..., scheduler_count: _Optional[int]=..., cloud_data_lineage_integration: _Optional[_Union[CloudDataLineageIntegration, _Mapping]]=..., web_server_plugins_mode: _Optional[_Union[SoftwareConfig.WebServerPluginsMode, str]]=...) -> None:
        ...

class IPAllocationPolicy(_message.Message):
    __slots__ = ('use_ip_aliases', 'cluster_secondary_range_name', 'cluster_ipv4_cidr_block', 'services_secondary_range_name', 'services_ipv4_cidr_block')
    USE_IP_ALIASES_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_SECONDARY_RANGE_NAME_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_IPV4_CIDR_BLOCK_FIELD_NUMBER: _ClassVar[int]
    SERVICES_SECONDARY_RANGE_NAME_FIELD_NUMBER: _ClassVar[int]
    SERVICES_IPV4_CIDR_BLOCK_FIELD_NUMBER: _ClassVar[int]
    use_ip_aliases: bool
    cluster_secondary_range_name: str
    cluster_ipv4_cidr_block: str
    services_secondary_range_name: str
    services_ipv4_cidr_block: str

    def __init__(self, use_ip_aliases: bool=..., cluster_secondary_range_name: _Optional[str]=..., cluster_ipv4_cidr_block: _Optional[str]=..., services_secondary_range_name: _Optional[str]=..., services_ipv4_cidr_block: _Optional[str]=...) -> None:
        ...

class NodeConfig(_message.Message):
    __slots__ = ('location', 'machine_type', 'network', 'subnetwork', 'disk_size_gb', 'oauth_scopes', 'service_account', 'tags', 'ip_allocation_policy', 'enable_ip_masq_agent', 'composer_network_attachment', 'composer_internal_ipv4_cidr_block')
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    MACHINE_TYPE_FIELD_NUMBER: _ClassVar[int]
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    SUBNETWORK_FIELD_NUMBER: _ClassVar[int]
    DISK_SIZE_GB_FIELD_NUMBER: _ClassVar[int]
    OAUTH_SCOPES_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    IP_ALLOCATION_POLICY_FIELD_NUMBER: _ClassVar[int]
    ENABLE_IP_MASQ_AGENT_FIELD_NUMBER: _ClassVar[int]
    COMPOSER_NETWORK_ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
    COMPOSER_INTERNAL_IPV4_CIDR_BLOCK_FIELD_NUMBER: _ClassVar[int]
    location: str
    machine_type: str
    network: str
    subnetwork: str
    disk_size_gb: int
    oauth_scopes: _containers.RepeatedScalarFieldContainer[str]
    service_account: str
    tags: _containers.RepeatedScalarFieldContainer[str]
    ip_allocation_policy: IPAllocationPolicy
    enable_ip_masq_agent: bool
    composer_network_attachment: str
    composer_internal_ipv4_cidr_block: str

    def __init__(self, location: _Optional[str]=..., machine_type: _Optional[str]=..., network: _Optional[str]=..., subnetwork: _Optional[str]=..., disk_size_gb: _Optional[int]=..., oauth_scopes: _Optional[_Iterable[str]]=..., service_account: _Optional[str]=..., tags: _Optional[_Iterable[str]]=..., ip_allocation_policy: _Optional[_Union[IPAllocationPolicy, _Mapping]]=..., enable_ip_masq_agent: bool=..., composer_network_attachment: _Optional[str]=..., composer_internal_ipv4_cidr_block: _Optional[str]=...) -> None:
        ...

class PrivateClusterConfig(_message.Message):
    __slots__ = ('enable_private_endpoint', 'master_ipv4_cidr_block', 'master_ipv4_reserved_range')
    ENABLE_PRIVATE_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    MASTER_IPV4_CIDR_BLOCK_FIELD_NUMBER: _ClassVar[int]
    MASTER_IPV4_RESERVED_RANGE_FIELD_NUMBER: _ClassVar[int]
    enable_private_endpoint: bool
    master_ipv4_cidr_block: str
    master_ipv4_reserved_range: str

    def __init__(self, enable_private_endpoint: bool=..., master_ipv4_cidr_block: _Optional[str]=..., master_ipv4_reserved_range: _Optional[str]=...) -> None:
        ...

class NetworkingConfig(_message.Message):
    __slots__ = ('connection_type',)

    class ConnectionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CONNECTION_TYPE_UNSPECIFIED: _ClassVar[NetworkingConfig.ConnectionType]
        VPC_PEERING: _ClassVar[NetworkingConfig.ConnectionType]
        PRIVATE_SERVICE_CONNECT: _ClassVar[NetworkingConfig.ConnectionType]
    CONNECTION_TYPE_UNSPECIFIED: NetworkingConfig.ConnectionType
    VPC_PEERING: NetworkingConfig.ConnectionType
    PRIVATE_SERVICE_CONNECT: NetworkingConfig.ConnectionType
    CONNECTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    connection_type: NetworkingConfig.ConnectionType

    def __init__(self, connection_type: _Optional[_Union[NetworkingConfig.ConnectionType, str]]=...) -> None:
        ...

class PrivateEnvironmentConfig(_message.Message):
    __slots__ = ('enable_private_environment', 'enable_private_builds_only', 'private_cluster_config', 'web_server_ipv4_cidr_block', 'cloud_sql_ipv4_cidr_block', 'web_server_ipv4_reserved_range', 'cloud_composer_network_ipv4_cidr_block', 'cloud_composer_network_ipv4_reserved_range', 'enable_privately_used_public_ips', 'cloud_composer_connection_subnetwork', 'networking_config')
    ENABLE_PRIVATE_ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    ENABLE_PRIVATE_BUILDS_ONLY_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_CLUSTER_CONFIG_FIELD_NUMBER: _ClassVar[int]
    WEB_SERVER_IPV4_CIDR_BLOCK_FIELD_NUMBER: _ClassVar[int]
    CLOUD_SQL_IPV4_CIDR_BLOCK_FIELD_NUMBER: _ClassVar[int]
    WEB_SERVER_IPV4_RESERVED_RANGE_FIELD_NUMBER: _ClassVar[int]
    CLOUD_COMPOSER_NETWORK_IPV4_CIDR_BLOCK_FIELD_NUMBER: _ClassVar[int]
    CLOUD_COMPOSER_NETWORK_IPV4_RESERVED_RANGE_FIELD_NUMBER: _ClassVar[int]
    ENABLE_PRIVATELY_USED_PUBLIC_IPS_FIELD_NUMBER: _ClassVar[int]
    CLOUD_COMPOSER_CONNECTION_SUBNETWORK_FIELD_NUMBER: _ClassVar[int]
    NETWORKING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    enable_private_environment: bool
    enable_private_builds_only: bool
    private_cluster_config: PrivateClusterConfig
    web_server_ipv4_cidr_block: str
    cloud_sql_ipv4_cidr_block: str
    web_server_ipv4_reserved_range: str
    cloud_composer_network_ipv4_cidr_block: str
    cloud_composer_network_ipv4_reserved_range: str
    enable_privately_used_public_ips: bool
    cloud_composer_connection_subnetwork: str
    networking_config: NetworkingConfig

    def __init__(self, enable_private_environment: bool=..., enable_private_builds_only: bool=..., private_cluster_config: _Optional[_Union[PrivateClusterConfig, _Mapping]]=..., web_server_ipv4_cidr_block: _Optional[str]=..., cloud_sql_ipv4_cidr_block: _Optional[str]=..., web_server_ipv4_reserved_range: _Optional[str]=..., cloud_composer_network_ipv4_cidr_block: _Optional[str]=..., cloud_composer_network_ipv4_reserved_range: _Optional[str]=..., enable_privately_used_public_ips: bool=..., cloud_composer_connection_subnetwork: _Optional[str]=..., networking_config: _Optional[_Union[NetworkingConfig, _Mapping]]=...) -> None:
        ...

class WorkloadsConfig(_message.Message):
    __slots__ = ('scheduler', 'web_server', 'worker', 'triggerer', 'dag_processor')

    class SchedulerResource(_message.Message):
        __slots__ = ('cpu', 'memory_gb', 'storage_gb', 'count')
        CPU_FIELD_NUMBER: _ClassVar[int]
        MEMORY_GB_FIELD_NUMBER: _ClassVar[int]
        STORAGE_GB_FIELD_NUMBER: _ClassVar[int]
        COUNT_FIELD_NUMBER: _ClassVar[int]
        cpu: float
        memory_gb: float
        storage_gb: float
        count: int

        def __init__(self, cpu: _Optional[float]=..., memory_gb: _Optional[float]=..., storage_gb: _Optional[float]=..., count: _Optional[int]=...) -> None:
            ...

    class WebServerResource(_message.Message):
        __slots__ = ('cpu', 'memory_gb', 'storage_gb')
        CPU_FIELD_NUMBER: _ClassVar[int]
        MEMORY_GB_FIELD_NUMBER: _ClassVar[int]
        STORAGE_GB_FIELD_NUMBER: _ClassVar[int]
        cpu: float
        memory_gb: float
        storage_gb: float

        def __init__(self, cpu: _Optional[float]=..., memory_gb: _Optional[float]=..., storage_gb: _Optional[float]=...) -> None:
            ...

    class WorkerResource(_message.Message):
        __slots__ = ('cpu', 'memory_gb', 'storage_gb', 'min_count', 'max_count')
        CPU_FIELD_NUMBER: _ClassVar[int]
        MEMORY_GB_FIELD_NUMBER: _ClassVar[int]
        STORAGE_GB_FIELD_NUMBER: _ClassVar[int]
        MIN_COUNT_FIELD_NUMBER: _ClassVar[int]
        MAX_COUNT_FIELD_NUMBER: _ClassVar[int]
        cpu: float
        memory_gb: float
        storage_gb: float
        min_count: int
        max_count: int

        def __init__(self, cpu: _Optional[float]=..., memory_gb: _Optional[float]=..., storage_gb: _Optional[float]=..., min_count: _Optional[int]=..., max_count: _Optional[int]=...) -> None:
            ...

    class TriggererResource(_message.Message):
        __slots__ = ('count', 'cpu', 'memory_gb')
        COUNT_FIELD_NUMBER: _ClassVar[int]
        CPU_FIELD_NUMBER: _ClassVar[int]
        MEMORY_GB_FIELD_NUMBER: _ClassVar[int]
        count: int
        cpu: float
        memory_gb: float

        def __init__(self, count: _Optional[int]=..., cpu: _Optional[float]=..., memory_gb: _Optional[float]=...) -> None:
            ...

    class DagProcessorResource(_message.Message):
        __slots__ = ('cpu', 'memory_gb', 'storage_gb', 'count')
        CPU_FIELD_NUMBER: _ClassVar[int]
        MEMORY_GB_FIELD_NUMBER: _ClassVar[int]
        STORAGE_GB_FIELD_NUMBER: _ClassVar[int]
        COUNT_FIELD_NUMBER: _ClassVar[int]
        cpu: float
        memory_gb: float
        storage_gb: float
        count: int

        def __init__(self, cpu: _Optional[float]=..., memory_gb: _Optional[float]=..., storage_gb: _Optional[float]=..., count: _Optional[int]=...) -> None:
            ...
    SCHEDULER_FIELD_NUMBER: _ClassVar[int]
    WEB_SERVER_FIELD_NUMBER: _ClassVar[int]
    WORKER_FIELD_NUMBER: _ClassVar[int]
    TRIGGERER_FIELD_NUMBER: _ClassVar[int]
    DAG_PROCESSOR_FIELD_NUMBER: _ClassVar[int]
    scheduler: WorkloadsConfig.SchedulerResource
    web_server: WorkloadsConfig.WebServerResource
    worker: WorkloadsConfig.WorkerResource
    triggerer: WorkloadsConfig.TriggererResource
    dag_processor: WorkloadsConfig.DagProcessorResource

    def __init__(self, scheduler: _Optional[_Union[WorkloadsConfig.SchedulerResource, _Mapping]]=..., web_server: _Optional[_Union[WorkloadsConfig.WebServerResource, _Mapping]]=..., worker: _Optional[_Union[WorkloadsConfig.WorkerResource, _Mapping]]=..., triggerer: _Optional[_Union[WorkloadsConfig.TriggererResource, _Mapping]]=..., dag_processor: _Optional[_Union[WorkloadsConfig.DagProcessorResource, _Mapping]]=...) -> None:
        ...

class RecoveryConfig(_message.Message):
    __slots__ = ('scheduled_snapshots_config',)
    SCHEDULED_SNAPSHOTS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    scheduled_snapshots_config: ScheduledSnapshotsConfig

    def __init__(self, scheduled_snapshots_config: _Optional[_Union[ScheduledSnapshotsConfig, _Mapping]]=...) -> None:
        ...

class ScheduledSnapshotsConfig(_message.Message):
    __slots__ = ('enabled', 'snapshot_location', 'snapshot_creation_schedule', 'time_zone')
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_LOCATION_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_CREATION_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    snapshot_location: str
    snapshot_creation_schedule: str
    time_zone: str

    def __init__(self, enabled: bool=..., snapshot_location: _Optional[str]=..., snapshot_creation_schedule: _Optional[str]=..., time_zone: _Optional[str]=...) -> None:
        ...

class MasterAuthorizedNetworksConfig(_message.Message):
    __slots__ = ('enabled', 'cidr_blocks')

    class CidrBlock(_message.Message):
        __slots__ = ('display_name', 'cidr_block')
        DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
        CIDR_BLOCK_FIELD_NUMBER: _ClassVar[int]
        display_name: str
        cidr_block: str

        def __init__(self, display_name: _Optional[str]=..., cidr_block: _Optional[str]=...) -> None:
            ...
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    CIDR_BLOCKS_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    cidr_blocks: _containers.RepeatedCompositeFieldContainer[MasterAuthorizedNetworksConfig.CidrBlock]

    def __init__(self, enabled: bool=..., cidr_blocks: _Optional[_Iterable[_Union[MasterAuthorizedNetworksConfig.CidrBlock, _Mapping]]]=...) -> None:
        ...

class CloudDataLineageIntegration(_message.Message):
    __slots__ = ('enabled',)
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    enabled: bool

    def __init__(self, enabled: bool=...) -> None:
        ...

class Environment(_message.Message):
    __slots__ = ('name', 'config', 'uuid', 'state', 'create_time', 'update_time', 'labels', 'satisfies_pzs', 'satisfies_pzi', 'storage_config')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Environment.State]
        CREATING: _ClassVar[Environment.State]
        RUNNING: _ClassVar[Environment.State]
        UPDATING: _ClassVar[Environment.State]
        DELETING: _ClassVar[Environment.State]
        ERROR: _ClassVar[Environment.State]
    STATE_UNSPECIFIED: Environment.State
    CREATING: Environment.State
    RUNNING: Environment.State
    UPDATING: Environment.State
    DELETING: Environment.State
    ERROR: Environment.State

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    SATISFIES_PZS_FIELD_NUMBER: _ClassVar[int]
    SATISFIES_PZI_FIELD_NUMBER: _ClassVar[int]
    STORAGE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    name: str
    config: EnvironmentConfig
    uuid: str
    state: Environment.State
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    satisfies_pzs: bool
    satisfies_pzi: bool
    storage_config: StorageConfig

    def __init__(self, name: _Optional[str]=..., config: _Optional[_Union[EnvironmentConfig, _Mapping]]=..., uuid: _Optional[str]=..., state: _Optional[_Union[Environment.State, str]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., satisfies_pzs: bool=..., satisfies_pzi: bool=..., storage_config: _Optional[_Union[StorageConfig, _Mapping]]=...) -> None:
        ...

class CheckUpgradeRequest(_message.Message):
    __slots__ = ('environment', 'image_version')
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    IMAGE_VERSION_FIELD_NUMBER: _ClassVar[int]
    environment: str
    image_version: str

    def __init__(self, environment: _Optional[str]=..., image_version: _Optional[str]=...) -> None:
        ...

class CheckUpgradeResponse(_message.Message):
    __slots__ = ('build_log_uri', 'contains_pypi_modules_conflict', 'pypi_conflict_build_log_extract', 'image_version', 'pypi_dependencies')

    class ConflictResult(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CONFLICT_RESULT_UNSPECIFIED: _ClassVar[CheckUpgradeResponse.ConflictResult]
        CONFLICT: _ClassVar[CheckUpgradeResponse.ConflictResult]
        NO_CONFLICT: _ClassVar[CheckUpgradeResponse.ConflictResult]
    CONFLICT_RESULT_UNSPECIFIED: CheckUpgradeResponse.ConflictResult
    CONFLICT: CheckUpgradeResponse.ConflictResult
    NO_CONFLICT: CheckUpgradeResponse.ConflictResult

    class PypiDependenciesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    BUILD_LOG_URI_FIELD_NUMBER: _ClassVar[int]
    CONTAINS_PYPI_MODULES_CONFLICT_FIELD_NUMBER: _ClassVar[int]
    PYPI_CONFLICT_BUILD_LOG_EXTRACT_FIELD_NUMBER: _ClassVar[int]
    IMAGE_VERSION_FIELD_NUMBER: _ClassVar[int]
    PYPI_DEPENDENCIES_FIELD_NUMBER: _ClassVar[int]
    build_log_uri: str
    contains_pypi_modules_conflict: CheckUpgradeResponse.ConflictResult
    pypi_conflict_build_log_extract: str
    image_version: str
    pypi_dependencies: _containers.ScalarMap[str, str]

    def __init__(self, build_log_uri: _Optional[str]=..., contains_pypi_modules_conflict: _Optional[_Union[CheckUpgradeResponse.ConflictResult, str]]=..., pypi_conflict_build_log_extract: _Optional[str]=..., image_version: _Optional[str]=..., pypi_dependencies: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class DataRetentionConfig(_message.Message):
    __slots__ = ('airflow_metadata_retention_config', 'task_logs_retention_config')
    AIRFLOW_METADATA_RETENTION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    TASK_LOGS_RETENTION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    airflow_metadata_retention_config: AirflowMetadataRetentionPolicyConfig
    task_logs_retention_config: TaskLogsRetentionConfig

    def __init__(self, airflow_metadata_retention_config: _Optional[_Union[AirflowMetadataRetentionPolicyConfig, _Mapping]]=..., task_logs_retention_config: _Optional[_Union[TaskLogsRetentionConfig, _Mapping]]=...) -> None:
        ...

class TaskLogsRetentionConfig(_message.Message):
    __slots__ = ('storage_mode',)

    class TaskLogsStorageMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TASK_LOGS_STORAGE_MODE_UNSPECIFIED: _ClassVar[TaskLogsRetentionConfig.TaskLogsStorageMode]
        CLOUD_LOGGING_AND_CLOUD_STORAGE: _ClassVar[TaskLogsRetentionConfig.TaskLogsStorageMode]
        CLOUD_LOGGING_ONLY: _ClassVar[TaskLogsRetentionConfig.TaskLogsStorageMode]
    TASK_LOGS_STORAGE_MODE_UNSPECIFIED: TaskLogsRetentionConfig.TaskLogsStorageMode
    CLOUD_LOGGING_AND_CLOUD_STORAGE: TaskLogsRetentionConfig.TaskLogsStorageMode
    CLOUD_LOGGING_ONLY: TaskLogsRetentionConfig.TaskLogsStorageMode
    STORAGE_MODE_FIELD_NUMBER: _ClassVar[int]
    storage_mode: TaskLogsRetentionConfig.TaskLogsStorageMode

    def __init__(self, storage_mode: _Optional[_Union[TaskLogsRetentionConfig.TaskLogsStorageMode, str]]=...) -> None:
        ...

class AirflowMetadataRetentionPolicyConfig(_message.Message):
    __slots__ = ('retention_mode', 'retention_days')

    class RetentionMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RETENTION_MODE_UNSPECIFIED: _ClassVar[AirflowMetadataRetentionPolicyConfig.RetentionMode]
        RETENTION_MODE_ENABLED: _ClassVar[AirflowMetadataRetentionPolicyConfig.RetentionMode]
        RETENTION_MODE_DISABLED: _ClassVar[AirflowMetadataRetentionPolicyConfig.RetentionMode]
    RETENTION_MODE_UNSPECIFIED: AirflowMetadataRetentionPolicyConfig.RetentionMode
    RETENTION_MODE_ENABLED: AirflowMetadataRetentionPolicyConfig.RetentionMode
    RETENTION_MODE_DISABLED: AirflowMetadataRetentionPolicyConfig.RetentionMode
    RETENTION_MODE_FIELD_NUMBER: _ClassVar[int]
    RETENTION_DAYS_FIELD_NUMBER: _ClassVar[int]
    retention_mode: AirflowMetadataRetentionPolicyConfig.RetentionMode
    retention_days: int

    def __init__(self, retention_mode: _Optional[_Union[AirflowMetadataRetentionPolicyConfig.RetentionMode, str]]=..., retention_days: _Optional[int]=...) -> None:
        ...