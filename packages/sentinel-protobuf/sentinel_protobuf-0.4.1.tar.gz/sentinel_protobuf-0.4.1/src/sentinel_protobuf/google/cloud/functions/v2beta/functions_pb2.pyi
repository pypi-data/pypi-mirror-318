from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.type import date_pb2 as _date_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class OperationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OPERATIONTYPE_UNSPECIFIED: _ClassVar[OperationType]
    CREATE_FUNCTION: _ClassVar[OperationType]
    UPDATE_FUNCTION: _ClassVar[OperationType]
    DELETE_FUNCTION: _ClassVar[OperationType]

class Environment(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ENVIRONMENT_UNSPECIFIED: _ClassVar[Environment]
    GEN_1: _ClassVar[Environment]
    GEN_2: _ClassVar[Environment]
OPERATIONTYPE_UNSPECIFIED: OperationType
CREATE_FUNCTION: OperationType
UPDATE_FUNCTION: OperationType
DELETE_FUNCTION: OperationType
ENVIRONMENT_UNSPECIFIED: Environment
GEN_1: Environment
GEN_2: Environment

class Function(_message.Message):
    __slots__ = ('name', 'description', 'build_config', 'service_config', 'event_trigger', 'state', 'update_time', 'labels', 'state_messages', 'environment', 'url', 'kms_key_name', 'satisfies_pzs', 'create_time')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Function.State]
        ACTIVE: _ClassVar[Function.State]
        FAILED: _ClassVar[Function.State]
        DEPLOYING: _ClassVar[Function.State]
        DELETING: _ClassVar[Function.State]
        UNKNOWN: _ClassVar[Function.State]
    STATE_UNSPECIFIED: Function.State
    ACTIVE: Function.State
    FAILED: Function.State
    DEPLOYING: Function.State
    DELETING: Function.State
    UNKNOWN: Function.State

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    BUILD_CONFIG_FIELD_NUMBER: _ClassVar[int]
    SERVICE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    EVENT_TRIGGER_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    STATE_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    KMS_KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    SATISFIES_PZS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    build_config: BuildConfig
    service_config: ServiceConfig
    event_trigger: EventTrigger
    state: Function.State
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    state_messages: _containers.RepeatedCompositeFieldContainer[StateMessage]
    environment: Environment
    url: str
    kms_key_name: str
    satisfies_pzs: bool
    create_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., description: _Optional[str]=..., build_config: _Optional[_Union[BuildConfig, _Mapping]]=..., service_config: _Optional[_Union[ServiceConfig, _Mapping]]=..., event_trigger: _Optional[_Union[EventTrigger, _Mapping]]=..., state: _Optional[_Union[Function.State, str]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., state_messages: _Optional[_Iterable[_Union[StateMessage, _Mapping]]]=..., environment: _Optional[_Union[Environment, str]]=..., url: _Optional[str]=..., kms_key_name: _Optional[str]=..., satisfies_pzs: bool=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class StateMessage(_message.Message):
    __slots__ = ('severity', 'type', 'message')

    class Severity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SEVERITY_UNSPECIFIED: _ClassVar[StateMessage.Severity]
        ERROR: _ClassVar[StateMessage.Severity]
        WARNING: _ClassVar[StateMessage.Severity]
        INFO: _ClassVar[StateMessage.Severity]
    SEVERITY_UNSPECIFIED: StateMessage.Severity
    ERROR: StateMessage.Severity
    WARNING: StateMessage.Severity
    INFO: StateMessage.Severity
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    severity: StateMessage.Severity
    type: str
    message: str

    def __init__(self, severity: _Optional[_Union[StateMessage.Severity, str]]=..., type: _Optional[str]=..., message: _Optional[str]=...) -> None:
        ...

class StorageSource(_message.Message):
    __slots__ = ('bucket', 'object', 'generation', 'source_upload_url')
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    GENERATION_FIELD_NUMBER: _ClassVar[int]
    SOURCE_UPLOAD_URL_FIELD_NUMBER: _ClassVar[int]
    bucket: str
    object: str
    generation: int
    source_upload_url: str

    def __init__(self, bucket: _Optional[str]=..., object: _Optional[str]=..., generation: _Optional[int]=..., source_upload_url: _Optional[str]=...) -> None:
        ...

class RepoSource(_message.Message):
    __slots__ = ('branch_name', 'tag_name', 'commit_sha', 'project_id', 'repo_name', 'dir', 'invert_regex')
    BRANCH_NAME_FIELD_NUMBER: _ClassVar[int]
    TAG_NAME_FIELD_NUMBER: _ClassVar[int]
    COMMIT_SHA_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    REPO_NAME_FIELD_NUMBER: _ClassVar[int]
    DIR_FIELD_NUMBER: _ClassVar[int]
    INVERT_REGEX_FIELD_NUMBER: _ClassVar[int]
    branch_name: str
    tag_name: str
    commit_sha: str
    project_id: str
    repo_name: str
    dir: str
    invert_regex: bool

    def __init__(self, branch_name: _Optional[str]=..., tag_name: _Optional[str]=..., commit_sha: _Optional[str]=..., project_id: _Optional[str]=..., repo_name: _Optional[str]=..., dir: _Optional[str]=..., invert_regex: bool=...) -> None:
        ...

class Source(_message.Message):
    __slots__ = ('storage_source', 'repo_source', 'git_uri')
    STORAGE_SOURCE_FIELD_NUMBER: _ClassVar[int]
    REPO_SOURCE_FIELD_NUMBER: _ClassVar[int]
    GIT_URI_FIELD_NUMBER: _ClassVar[int]
    storage_source: StorageSource
    repo_source: RepoSource
    git_uri: str

    def __init__(self, storage_source: _Optional[_Union[StorageSource, _Mapping]]=..., repo_source: _Optional[_Union[RepoSource, _Mapping]]=..., git_uri: _Optional[str]=...) -> None:
        ...

class SourceProvenance(_message.Message):
    __slots__ = ('resolved_storage_source', 'resolved_repo_source', 'git_uri')
    RESOLVED_STORAGE_SOURCE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_REPO_SOURCE_FIELD_NUMBER: _ClassVar[int]
    GIT_URI_FIELD_NUMBER: _ClassVar[int]
    resolved_storage_source: StorageSource
    resolved_repo_source: RepoSource
    git_uri: str

    def __init__(self, resolved_storage_source: _Optional[_Union[StorageSource, _Mapping]]=..., resolved_repo_source: _Optional[_Union[RepoSource, _Mapping]]=..., git_uri: _Optional[str]=...) -> None:
        ...

class BuildConfig(_message.Message):
    __slots__ = ('automatic_update_policy', 'on_deploy_update_policy', 'build', 'runtime', 'entry_point', 'source', 'source_provenance', 'worker_pool', 'environment_variables', 'docker_registry', 'docker_repository', 'service_account')

    class DockerRegistry(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DOCKER_REGISTRY_UNSPECIFIED: _ClassVar[BuildConfig.DockerRegistry]
        CONTAINER_REGISTRY: _ClassVar[BuildConfig.DockerRegistry]
        ARTIFACT_REGISTRY: _ClassVar[BuildConfig.DockerRegistry]
    DOCKER_REGISTRY_UNSPECIFIED: BuildConfig.DockerRegistry
    CONTAINER_REGISTRY: BuildConfig.DockerRegistry
    ARTIFACT_REGISTRY: BuildConfig.DockerRegistry

    class EnvironmentVariablesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    AUTOMATIC_UPDATE_POLICY_FIELD_NUMBER: _ClassVar[int]
    ON_DEPLOY_UPDATE_POLICY_FIELD_NUMBER: _ClassVar[int]
    BUILD_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_FIELD_NUMBER: _ClassVar[int]
    ENTRY_POINT_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_PROVENANCE_FIELD_NUMBER: _ClassVar[int]
    WORKER_POOL_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_VARIABLES_FIELD_NUMBER: _ClassVar[int]
    DOCKER_REGISTRY_FIELD_NUMBER: _ClassVar[int]
    DOCKER_REPOSITORY_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    automatic_update_policy: AutomaticUpdatePolicy
    on_deploy_update_policy: OnDeployUpdatePolicy
    build: str
    runtime: str
    entry_point: str
    source: Source
    source_provenance: SourceProvenance
    worker_pool: str
    environment_variables: _containers.ScalarMap[str, str]
    docker_registry: BuildConfig.DockerRegistry
    docker_repository: str
    service_account: str

    def __init__(self, automatic_update_policy: _Optional[_Union[AutomaticUpdatePolicy, _Mapping]]=..., on_deploy_update_policy: _Optional[_Union[OnDeployUpdatePolicy, _Mapping]]=..., build: _Optional[str]=..., runtime: _Optional[str]=..., entry_point: _Optional[str]=..., source: _Optional[_Union[Source, _Mapping]]=..., source_provenance: _Optional[_Union[SourceProvenance, _Mapping]]=..., worker_pool: _Optional[str]=..., environment_variables: _Optional[_Mapping[str, str]]=..., docker_registry: _Optional[_Union[BuildConfig.DockerRegistry, str]]=..., docker_repository: _Optional[str]=..., service_account: _Optional[str]=...) -> None:
        ...

class ServiceConfig(_message.Message):
    __slots__ = ('service', 'timeout_seconds', 'available_memory', 'available_cpu', 'environment_variables', 'max_instance_count', 'min_instance_count', 'vpc_connector', 'vpc_connector_egress_settings', 'ingress_settings', 'uri', 'service_account_email', 'all_traffic_on_latest_revision', 'secret_environment_variables', 'secret_volumes', 'revision', 'max_instance_request_concurrency', 'security_level', 'binary_authorization_policy')

    class VpcConnectorEgressSettings(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        VPC_CONNECTOR_EGRESS_SETTINGS_UNSPECIFIED: _ClassVar[ServiceConfig.VpcConnectorEgressSettings]
        PRIVATE_RANGES_ONLY: _ClassVar[ServiceConfig.VpcConnectorEgressSettings]
        ALL_TRAFFIC: _ClassVar[ServiceConfig.VpcConnectorEgressSettings]
    VPC_CONNECTOR_EGRESS_SETTINGS_UNSPECIFIED: ServiceConfig.VpcConnectorEgressSettings
    PRIVATE_RANGES_ONLY: ServiceConfig.VpcConnectorEgressSettings
    ALL_TRAFFIC: ServiceConfig.VpcConnectorEgressSettings

    class IngressSettings(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        INGRESS_SETTINGS_UNSPECIFIED: _ClassVar[ServiceConfig.IngressSettings]
        ALLOW_ALL: _ClassVar[ServiceConfig.IngressSettings]
        ALLOW_INTERNAL_ONLY: _ClassVar[ServiceConfig.IngressSettings]
        ALLOW_INTERNAL_AND_GCLB: _ClassVar[ServiceConfig.IngressSettings]
    INGRESS_SETTINGS_UNSPECIFIED: ServiceConfig.IngressSettings
    ALLOW_ALL: ServiceConfig.IngressSettings
    ALLOW_INTERNAL_ONLY: ServiceConfig.IngressSettings
    ALLOW_INTERNAL_AND_GCLB: ServiceConfig.IngressSettings

    class SecurityLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SECURITY_LEVEL_UNSPECIFIED: _ClassVar[ServiceConfig.SecurityLevel]
        SECURE_ALWAYS: _ClassVar[ServiceConfig.SecurityLevel]
        SECURE_OPTIONAL: _ClassVar[ServiceConfig.SecurityLevel]
    SECURITY_LEVEL_UNSPECIFIED: ServiceConfig.SecurityLevel
    SECURE_ALWAYS: ServiceConfig.SecurityLevel
    SECURE_OPTIONAL: ServiceConfig.SecurityLevel

    class EnvironmentVariablesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_SECONDS_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_MEMORY_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_CPU_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_VARIABLES_FIELD_NUMBER: _ClassVar[int]
    MAX_INSTANCE_COUNT_FIELD_NUMBER: _ClassVar[int]
    MIN_INSTANCE_COUNT_FIELD_NUMBER: _ClassVar[int]
    VPC_CONNECTOR_FIELD_NUMBER: _ClassVar[int]
    VPC_CONNECTOR_EGRESS_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    INGRESS_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    URI_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_EMAIL_FIELD_NUMBER: _ClassVar[int]
    ALL_TRAFFIC_ON_LATEST_REVISION_FIELD_NUMBER: _ClassVar[int]
    SECRET_ENVIRONMENT_VARIABLES_FIELD_NUMBER: _ClassVar[int]
    SECRET_VOLUMES_FIELD_NUMBER: _ClassVar[int]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    MAX_INSTANCE_REQUEST_CONCURRENCY_FIELD_NUMBER: _ClassVar[int]
    SECURITY_LEVEL_FIELD_NUMBER: _ClassVar[int]
    BINARY_AUTHORIZATION_POLICY_FIELD_NUMBER: _ClassVar[int]
    service: str
    timeout_seconds: int
    available_memory: str
    available_cpu: str
    environment_variables: _containers.ScalarMap[str, str]
    max_instance_count: int
    min_instance_count: int
    vpc_connector: str
    vpc_connector_egress_settings: ServiceConfig.VpcConnectorEgressSettings
    ingress_settings: ServiceConfig.IngressSettings
    uri: str
    service_account_email: str
    all_traffic_on_latest_revision: bool
    secret_environment_variables: _containers.RepeatedCompositeFieldContainer[SecretEnvVar]
    secret_volumes: _containers.RepeatedCompositeFieldContainer[SecretVolume]
    revision: str
    max_instance_request_concurrency: int
    security_level: ServiceConfig.SecurityLevel
    binary_authorization_policy: str

    def __init__(self, service: _Optional[str]=..., timeout_seconds: _Optional[int]=..., available_memory: _Optional[str]=..., available_cpu: _Optional[str]=..., environment_variables: _Optional[_Mapping[str, str]]=..., max_instance_count: _Optional[int]=..., min_instance_count: _Optional[int]=..., vpc_connector: _Optional[str]=..., vpc_connector_egress_settings: _Optional[_Union[ServiceConfig.VpcConnectorEgressSettings, str]]=..., ingress_settings: _Optional[_Union[ServiceConfig.IngressSettings, str]]=..., uri: _Optional[str]=..., service_account_email: _Optional[str]=..., all_traffic_on_latest_revision: bool=..., secret_environment_variables: _Optional[_Iterable[_Union[SecretEnvVar, _Mapping]]]=..., secret_volumes: _Optional[_Iterable[_Union[SecretVolume, _Mapping]]]=..., revision: _Optional[str]=..., max_instance_request_concurrency: _Optional[int]=..., security_level: _Optional[_Union[ServiceConfig.SecurityLevel, str]]=..., binary_authorization_policy: _Optional[str]=...) -> None:
        ...

class SecretEnvVar(_message.Message):
    __slots__ = ('key', 'project_id', 'secret', 'version')
    KEY_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    SECRET_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    key: str
    project_id: str
    secret: str
    version: str

    def __init__(self, key: _Optional[str]=..., project_id: _Optional[str]=..., secret: _Optional[str]=..., version: _Optional[str]=...) -> None:
        ...

class SecretVolume(_message.Message):
    __slots__ = ('mount_path', 'project_id', 'secret', 'versions')

    class SecretVersion(_message.Message):
        __slots__ = ('version', 'path')
        VERSION_FIELD_NUMBER: _ClassVar[int]
        PATH_FIELD_NUMBER: _ClassVar[int]
        version: str
        path: str

        def __init__(self, version: _Optional[str]=..., path: _Optional[str]=...) -> None:
            ...
    MOUNT_PATH_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    SECRET_FIELD_NUMBER: _ClassVar[int]
    VERSIONS_FIELD_NUMBER: _ClassVar[int]
    mount_path: str
    project_id: str
    secret: str
    versions: _containers.RepeatedCompositeFieldContainer[SecretVolume.SecretVersion]

    def __init__(self, mount_path: _Optional[str]=..., project_id: _Optional[str]=..., secret: _Optional[str]=..., versions: _Optional[_Iterable[_Union[SecretVolume.SecretVersion, _Mapping]]]=...) -> None:
        ...

class EventTrigger(_message.Message):
    __slots__ = ('trigger', 'trigger_region', 'event_type', 'event_filters', 'pubsub_topic', 'service_account_email', 'retry_policy', 'channel', 'service')

    class RetryPolicy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RETRY_POLICY_UNSPECIFIED: _ClassVar[EventTrigger.RetryPolicy]
        RETRY_POLICY_DO_NOT_RETRY: _ClassVar[EventTrigger.RetryPolicy]
        RETRY_POLICY_RETRY: _ClassVar[EventTrigger.RetryPolicy]
    RETRY_POLICY_UNSPECIFIED: EventTrigger.RetryPolicy
    RETRY_POLICY_DO_NOT_RETRY: EventTrigger.RetryPolicy
    RETRY_POLICY_RETRY: EventTrigger.RetryPolicy
    TRIGGER_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_REGION_FIELD_NUMBER: _ClassVar[int]
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    EVENT_FILTERS_FIELD_NUMBER: _ClassVar[int]
    PUBSUB_TOPIC_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_EMAIL_FIELD_NUMBER: _ClassVar[int]
    RETRY_POLICY_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    trigger: str
    trigger_region: str
    event_type: str
    event_filters: _containers.RepeatedCompositeFieldContainer[EventFilter]
    pubsub_topic: str
    service_account_email: str
    retry_policy: EventTrigger.RetryPolicy
    channel: str
    service: str

    def __init__(self, trigger: _Optional[str]=..., trigger_region: _Optional[str]=..., event_type: _Optional[str]=..., event_filters: _Optional[_Iterable[_Union[EventFilter, _Mapping]]]=..., pubsub_topic: _Optional[str]=..., service_account_email: _Optional[str]=..., retry_policy: _Optional[_Union[EventTrigger.RetryPolicy, str]]=..., channel: _Optional[str]=..., service: _Optional[str]=...) -> None:
        ...

class EventFilter(_message.Message):
    __slots__ = ('attribute', 'value', 'operator')
    ATTRIBUTE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    OPERATOR_FIELD_NUMBER: _ClassVar[int]
    attribute: str
    value: str
    operator: str

    def __init__(self, attribute: _Optional[str]=..., value: _Optional[str]=..., operator: _Optional[str]=...) -> None:
        ...

class GetFunctionRequest(_message.Message):
    __slots__ = ('name', 'revision')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    name: str
    revision: str

    def __init__(self, name: _Optional[str]=..., revision: _Optional[str]=...) -> None:
        ...

class ListFunctionsRequest(_message.Message):
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

class ListFunctionsResponse(_message.Message):
    __slots__ = ('functions', 'next_page_token', 'unreachable')
    FUNCTIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    functions: _containers.RepeatedCompositeFieldContainer[Function]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, functions: _Optional[_Iterable[_Union[Function, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class CreateFunctionRequest(_message.Message):
    __slots__ = ('parent', 'function', 'function_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FUNCTION_FIELD_NUMBER: _ClassVar[int]
    FUNCTION_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    function: Function
    function_id: str

    def __init__(self, parent: _Optional[str]=..., function: _Optional[_Union[Function, _Mapping]]=..., function_id: _Optional[str]=...) -> None:
        ...

class UpdateFunctionRequest(_message.Message):
    __slots__ = ('function', 'update_mask')
    FUNCTION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    function: Function
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, function: _Optional[_Union[Function, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteFunctionRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class GenerateUploadUrlRequest(_message.Message):
    __slots__ = ('parent', 'kms_key_name', 'environment')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    KMS_KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    parent: str
    kms_key_name: str
    environment: Environment

    def __init__(self, parent: _Optional[str]=..., kms_key_name: _Optional[str]=..., environment: _Optional[_Union[Environment, str]]=...) -> None:
        ...

class GenerateUploadUrlResponse(_message.Message):
    __slots__ = ('upload_url', 'storage_source')
    UPLOAD_URL_FIELD_NUMBER: _ClassVar[int]
    STORAGE_SOURCE_FIELD_NUMBER: _ClassVar[int]
    upload_url: str
    storage_source: StorageSource

    def __init__(self, upload_url: _Optional[str]=..., storage_source: _Optional[_Union[StorageSource, _Mapping]]=...) -> None:
        ...

class GenerateDownloadUrlRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class GenerateDownloadUrlResponse(_message.Message):
    __slots__ = ('download_url',)
    DOWNLOAD_URL_FIELD_NUMBER: _ClassVar[int]
    download_url: str

    def __init__(self, download_url: _Optional[str]=...) -> None:
        ...

class ListRuntimesRequest(_message.Message):
    __slots__ = ('parent', 'filter')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str

    def __init__(self, parent: _Optional[str]=..., filter: _Optional[str]=...) -> None:
        ...

class ListRuntimesResponse(_message.Message):
    __slots__ = ('runtimes',)

    class RuntimeStage(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RUNTIME_STAGE_UNSPECIFIED: _ClassVar[ListRuntimesResponse.RuntimeStage]
        DEVELOPMENT: _ClassVar[ListRuntimesResponse.RuntimeStage]
        ALPHA: _ClassVar[ListRuntimesResponse.RuntimeStage]
        BETA: _ClassVar[ListRuntimesResponse.RuntimeStage]
        GA: _ClassVar[ListRuntimesResponse.RuntimeStage]
        DEPRECATED: _ClassVar[ListRuntimesResponse.RuntimeStage]
        DECOMMISSIONED: _ClassVar[ListRuntimesResponse.RuntimeStage]
    RUNTIME_STAGE_UNSPECIFIED: ListRuntimesResponse.RuntimeStage
    DEVELOPMENT: ListRuntimesResponse.RuntimeStage
    ALPHA: ListRuntimesResponse.RuntimeStage
    BETA: ListRuntimesResponse.RuntimeStage
    GA: ListRuntimesResponse.RuntimeStage
    DEPRECATED: ListRuntimesResponse.RuntimeStage
    DECOMMISSIONED: ListRuntimesResponse.RuntimeStage

    class Runtime(_message.Message):
        __slots__ = ('name', 'display_name', 'stage', 'warnings', 'environment', 'deprecation_date', 'decommission_date')
        NAME_FIELD_NUMBER: _ClassVar[int]
        DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
        STAGE_FIELD_NUMBER: _ClassVar[int]
        WARNINGS_FIELD_NUMBER: _ClassVar[int]
        ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
        DEPRECATION_DATE_FIELD_NUMBER: _ClassVar[int]
        DECOMMISSION_DATE_FIELD_NUMBER: _ClassVar[int]
        name: str
        display_name: str
        stage: ListRuntimesResponse.RuntimeStage
        warnings: _containers.RepeatedScalarFieldContainer[str]
        environment: Environment
        deprecation_date: _date_pb2.Date
        decommission_date: _date_pb2.Date

        def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., stage: _Optional[_Union[ListRuntimesResponse.RuntimeStage, str]]=..., warnings: _Optional[_Iterable[str]]=..., environment: _Optional[_Union[Environment, str]]=..., deprecation_date: _Optional[_Union[_date_pb2.Date, _Mapping]]=..., decommission_date: _Optional[_Union[_date_pb2.Date, _Mapping]]=...) -> None:
            ...
    RUNTIMES_FIELD_NUMBER: _ClassVar[int]
    runtimes: _containers.RepeatedCompositeFieldContainer[ListRuntimesResponse.Runtime]

    def __init__(self, runtimes: _Optional[_Iterable[_Union[ListRuntimesResponse.Runtime, _Mapping]]]=...) -> None:
        ...

class AutomaticUpdatePolicy(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class OnDeployUpdatePolicy(_message.Message):
    __slots__ = ('runtime_version',)
    RUNTIME_VERSION_FIELD_NUMBER: _ClassVar[int]
    runtime_version: str

    def __init__(self, runtime_version: _Optional[str]=...) -> None:
        ...

class OperationMetadata(_message.Message):
    __slots__ = ('create_time', 'end_time', 'target', 'verb', 'status_detail', 'cancel_requested', 'api_version', 'request_resource', 'stages', 'build_name', 'operation_type')
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    VERB_FIELD_NUMBER: _ClassVar[int]
    STATUS_DETAIL_FIELD_NUMBER: _ClassVar[int]
    CANCEL_REQUESTED_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    REQUEST_RESOURCE_FIELD_NUMBER: _ClassVar[int]
    STAGES_FIELD_NUMBER: _ClassVar[int]
    BUILD_NAME_FIELD_NUMBER: _ClassVar[int]
    OPERATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    target: str
    verb: str
    status_detail: str
    cancel_requested: bool
    api_version: str
    request_resource: _any_pb2.Any
    stages: _containers.RepeatedCompositeFieldContainer[Stage]
    build_name: str
    operation_type: OperationType

    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., target: _Optional[str]=..., verb: _Optional[str]=..., status_detail: _Optional[str]=..., cancel_requested: bool=..., api_version: _Optional[str]=..., request_resource: _Optional[_Union[_any_pb2.Any, _Mapping]]=..., stages: _Optional[_Iterable[_Union[Stage, _Mapping]]]=..., build_name: _Optional[str]=..., operation_type: _Optional[_Union[OperationType, str]]=...) -> None:
        ...

class LocationMetadata(_message.Message):
    __slots__ = ('environments',)
    ENVIRONMENTS_FIELD_NUMBER: _ClassVar[int]
    environments: _containers.RepeatedScalarFieldContainer[Environment]

    def __init__(self, environments: _Optional[_Iterable[_Union[Environment, str]]]=...) -> None:
        ...

class Stage(_message.Message):
    __slots__ = ('name', 'message', 'state', 'resource', 'resource_uri', 'state_messages')

    class Name(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NAME_UNSPECIFIED: _ClassVar[Stage.Name]
        ARTIFACT_REGISTRY: _ClassVar[Stage.Name]
        BUILD: _ClassVar[Stage.Name]
        SERVICE: _ClassVar[Stage.Name]
        TRIGGER: _ClassVar[Stage.Name]
        SERVICE_ROLLBACK: _ClassVar[Stage.Name]
        TRIGGER_ROLLBACK: _ClassVar[Stage.Name]
    NAME_UNSPECIFIED: Stage.Name
    ARTIFACT_REGISTRY: Stage.Name
    BUILD: Stage.Name
    SERVICE: Stage.Name
    TRIGGER: Stage.Name
    SERVICE_ROLLBACK: Stage.Name
    TRIGGER_ROLLBACK: Stage.Name

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Stage.State]
        NOT_STARTED: _ClassVar[Stage.State]
        IN_PROGRESS: _ClassVar[Stage.State]
        COMPLETE: _ClassVar[Stage.State]
    STATE_UNSPECIFIED: Stage.State
    NOT_STARTED: Stage.State
    IN_PROGRESS: Stage.State
    COMPLETE: Stage.State
    NAME_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_URI_FIELD_NUMBER: _ClassVar[int]
    STATE_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    name: Stage.Name
    message: str
    state: Stage.State
    resource: str
    resource_uri: str
    state_messages: _containers.RepeatedCompositeFieldContainer[StateMessage]

    def __init__(self, name: _Optional[_Union[Stage.Name, str]]=..., message: _Optional[str]=..., state: _Optional[_Union[Stage.State, str]]=..., resource: _Optional[str]=..., resource_uri: _Optional[str]=..., state_messages: _Optional[_Iterable[_Union[StateMessage, _Mapping]]]=...) -> None:
        ...