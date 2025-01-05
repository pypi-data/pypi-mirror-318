from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.functions.v1 import operations_pb2 as _operations_pb2
from google.iam.v1 import iam_policy_pb2 as _iam_policy_pb2
from google.iam.v1 import policy_pb2 as _policy_pb2
from google.longrunning import operations_pb2 as _operations_pb2_1
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CloudFunctionStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CLOUD_FUNCTION_STATUS_UNSPECIFIED: _ClassVar[CloudFunctionStatus]
    ACTIVE: _ClassVar[CloudFunctionStatus]
    OFFLINE: _ClassVar[CloudFunctionStatus]
    DEPLOY_IN_PROGRESS: _ClassVar[CloudFunctionStatus]
    DELETE_IN_PROGRESS: _ClassVar[CloudFunctionStatus]
    UNKNOWN: _ClassVar[CloudFunctionStatus]
CLOUD_FUNCTION_STATUS_UNSPECIFIED: CloudFunctionStatus
ACTIVE: CloudFunctionStatus
OFFLINE: CloudFunctionStatus
DEPLOY_IN_PROGRESS: CloudFunctionStatus
DELETE_IN_PROGRESS: CloudFunctionStatus
UNKNOWN: CloudFunctionStatus

class CloudFunction(_message.Message):
    __slots__ = ('name', 'description', 'source_archive_url', 'source_repository', 'source_upload_url', 'https_trigger', 'event_trigger', 'status', 'entry_point', 'runtime', 'timeout', 'available_memory_mb', 'service_account_email', 'update_time', 'version_id', 'labels', 'environment_variables', 'build_environment_variables', 'network', 'max_instances', 'min_instances', 'vpc_connector', 'vpc_connector_egress_settings', 'ingress_settings', 'kms_key_name', 'build_worker_pool', 'build_id', 'build_name', 'secret_environment_variables', 'secret_volumes', 'source_token', 'docker_repository', 'docker_registry', 'automatic_update_policy', 'on_deploy_update_policy', 'build_service_account')

    class VpcConnectorEgressSettings(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        VPC_CONNECTOR_EGRESS_SETTINGS_UNSPECIFIED: _ClassVar[CloudFunction.VpcConnectorEgressSettings]
        PRIVATE_RANGES_ONLY: _ClassVar[CloudFunction.VpcConnectorEgressSettings]
        ALL_TRAFFIC: _ClassVar[CloudFunction.VpcConnectorEgressSettings]
    VPC_CONNECTOR_EGRESS_SETTINGS_UNSPECIFIED: CloudFunction.VpcConnectorEgressSettings
    PRIVATE_RANGES_ONLY: CloudFunction.VpcConnectorEgressSettings
    ALL_TRAFFIC: CloudFunction.VpcConnectorEgressSettings

    class IngressSettings(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        INGRESS_SETTINGS_UNSPECIFIED: _ClassVar[CloudFunction.IngressSettings]
        ALLOW_ALL: _ClassVar[CloudFunction.IngressSettings]
        ALLOW_INTERNAL_ONLY: _ClassVar[CloudFunction.IngressSettings]
        ALLOW_INTERNAL_AND_GCLB: _ClassVar[CloudFunction.IngressSettings]
    INGRESS_SETTINGS_UNSPECIFIED: CloudFunction.IngressSettings
    ALLOW_ALL: CloudFunction.IngressSettings
    ALLOW_INTERNAL_ONLY: CloudFunction.IngressSettings
    ALLOW_INTERNAL_AND_GCLB: CloudFunction.IngressSettings

    class DockerRegistry(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DOCKER_REGISTRY_UNSPECIFIED: _ClassVar[CloudFunction.DockerRegistry]
        CONTAINER_REGISTRY: _ClassVar[CloudFunction.DockerRegistry]
        ARTIFACT_REGISTRY: _ClassVar[CloudFunction.DockerRegistry]
    DOCKER_REGISTRY_UNSPECIFIED: CloudFunction.DockerRegistry
    CONTAINER_REGISTRY: CloudFunction.DockerRegistry
    ARTIFACT_REGISTRY: CloudFunction.DockerRegistry

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

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...

    class EnvironmentVariablesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...

    class BuildEnvironmentVariablesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ARCHIVE_URL_FIELD_NUMBER: _ClassVar[int]
    SOURCE_REPOSITORY_FIELD_NUMBER: _ClassVar[int]
    SOURCE_UPLOAD_URL_FIELD_NUMBER: _ClassVar[int]
    HTTPS_TRIGGER_FIELD_NUMBER: _ClassVar[int]
    EVENT_TRIGGER_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ENTRY_POINT_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_MEMORY_MB_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_EMAIL_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_VARIABLES_FIELD_NUMBER: _ClassVar[int]
    BUILD_ENVIRONMENT_VARIABLES_FIELD_NUMBER: _ClassVar[int]
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    MAX_INSTANCES_FIELD_NUMBER: _ClassVar[int]
    MIN_INSTANCES_FIELD_NUMBER: _ClassVar[int]
    VPC_CONNECTOR_FIELD_NUMBER: _ClassVar[int]
    VPC_CONNECTOR_EGRESS_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    INGRESS_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    KMS_KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    BUILD_WORKER_POOL_FIELD_NUMBER: _ClassVar[int]
    BUILD_ID_FIELD_NUMBER: _ClassVar[int]
    BUILD_NAME_FIELD_NUMBER: _ClassVar[int]
    SECRET_ENVIRONMENT_VARIABLES_FIELD_NUMBER: _ClassVar[int]
    SECRET_VOLUMES_FIELD_NUMBER: _ClassVar[int]
    SOURCE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    DOCKER_REPOSITORY_FIELD_NUMBER: _ClassVar[int]
    DOCKER_REGISTRY_FIELD_NUMBER: _ClassVar[int]
    AUTOMATIC_UPDATE_POLICY_FIELD_NUMBER: _ClassVar[int]
    ON_DEPLOY_UPDATE_POLICY_FIELD_NUMBER: _ClassVar[int]
    BUILD_SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    source_archive_url: str
    source_repository: SourceRepository
    source_upload_url: str
    https_trigger: HttpsTrigger
    event_trigger: EventTrigger
    status: CloudFunctionStatus
    entry_point: str
    runtime: str
    timeout: _duration_pb2.Duration
    available_memory_mb: int
    service_account_email: str
    update_time: _timestamp_pb2.Timestamp
    version_id: int
    labels: _containers.ScalarMap[str, str]
    environment_variables: _containers.ScalarMap[str, str]
    build_environment_variables: _containers.ScalarMap[str, str]
    network: str
    max_instances: int
    min_instances: int
    vpc_connector: str
    vpc_connector_egress_settings: CloudFunction.VpcConnectorEgressSettings
    ingress_settings: CloudFunction.IngressSettings
    kms_key_name: str
    build_worker_pool: str
    build_id: str
    build_name: str
    secret_environment_variables: _containers.RepeatedCompositeFieldContainer[SecretEnvVar]
    secret_volumes: _containers.RepeatedCompositeFieldContainer[SecretVolume]
    source_token: str
    docker_repository: str
    docker_registry: CloudFunction.DockerRegistry
    automatic_update_policy: CloudFunction.AutomaticUpdatePolicy
    on_deploy_update_policy: CloudFunction.OnDeployUpdatePolicy
    build_service_account: str

    def __init__(self, name: _Optional[str]=..., description: _Optional[str]=..., source_archive_url: _Optional[str]=..., source_repository: _Optional[_Union[SourceRepository, _Mapping]]=..., source_upload_url: _Optional[str]=..., https_trigger: _Optional[_Union[HttpsTrigger, _Mapping]]=..., event_trigger: _Optional[_Union[EventTrigger, _Mapping]]=..., status: _Optional[_Union[CloudFunctionStatus, str]]=..., entry_point: _Optional[str]=..., runtime: _Optional[str]=..., timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., available_memory_mb: _Optional[int]=..., service_account_email: _Optional[str]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., version_id: _Optional[int]=..., labels: _Optional[_Mapping[str, str]]=..., environment_variables: _Optional[_Mapping[str, str]]=..., build_environment_variables: _Optional[_Mapping[str, str]]=..., network: _Optional[str]=..., max_instances: _Optional[int]=..., min_instances: _Optional[int]=..., vpc_connector: _Optional[str]=..., vpc_connector_egress_settings: _Optional[_Union[CloudFunction.VpcConnectorEgressSettings, str]]=..., ingress_settings: _Optional[_Union[CloudFunction.IngressSettings, str]]=..., kms_key_name: _Optional[str]=..., build_worker_pool: _Optional[str]=..., build_id: _Optional[str]=..., build_name: _Optional[str]=..., secret_environment_variables: _Optional[_Iterable[_Union[SecretEnvVar, _Mapping]]]=..., secret_volumes: _Optional[_Iterable[_Union[SecretVolume, _Mapping]]]=..., source_token: _Optional[str]=..., docker_repository: _Optional[str]=..., docker_registry: _Optional[_Union[CloudFunction.DockerRegistry, str]]=..., automatic_update_policy: _Optional[_Union[CloudFunction.AutomaticUpdatePolicy, _Mapping]]=..., on_deploy_update_policy: _Optional[_Union[CloudFunction.OnDeployUpdatePolicy, _Mapping]]=..., build_service_account: _Optional[str]=...) -> None:
        ...

class SourceRepository(_message.Message):
    __slots__ = ('url', 'deployed_url')
    URL_FIELD_NUMBER: _ClassVar[int]
    DEPLOYED_URL_FIELD_NUMBER: _ClassVar[int]
    url: str
    deployed_url: str

    def __init__(self, url: _Optional[str]=..., deployed_url: _Optional[str]=...) -> None:
        ...

class HttpsTrigger(_message.Message):
    __slots__ = ('url', 'security_level')

    class SecurityLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SECURITY_LEVEL_UNSPECIFIED: _ClassVar[HttpsTrigger.SecurityLevel]
        SECURE_ALWAYS: _ClassVar[HttpsTrigger.SecurityLevel]
        SECURE_OPTIONAL: _ClassVar[HttpsTrigger.SecurityLevel]
    SECURITY_LEVEL_UNSPECIFIED: HttpsTrigger.SecurityLevel
    SECURE_ALWAYS: HttpsTrigger.SecurityLevel
    SECURE_OPTIONAL: HttpsTrigger.SecurityLevel
    URL_FIELD_NUMBER: _ClassVar[int]
    SECURITY_LEVEL_FIELD_NUMBER: _ClassVar[int]
    url: str
    security_level: HttpsTrigger.SecurityLevel

    def __init__(self, url: _Optional[str]=..., security_level: _Optional[_Union[HttpsTrigger.SecurityLevel, str]]=...) -> None:
        ...

class EventTrigger(_message.Message):
    __slots__ = ('event_type', 'resource', 'service', 'failure_policy')
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    FAILURE_POLICY_FIELD_NUMBER: _ClassVar[int]
    event_type: str
    resource: str
    service: str
    failure_policy: FailurePolicy

    def __init__(self, event_type: _Optional[str]=..., resource: _Optional[str]=..., service: _Optional[str]=..., failure_policy: _Optional[_Union[FailurePolicy, _Mapping]]=...) -> None:
        ...

class FailurePolicy(_message.Message):
    __slots__ = ('retry',)

    class Retry(_message.Message):
        __slots__ = ()

        def __init__(self) -> None:
            ...
    RETRY_FIELD_NUMBER: _ClassVar[int]
    retry: FailurePolicy.Retry

    def __init__(self, retry: _Optional[_Union[FailurePolicy.Retry, _Mapping]]=...) -> None:
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

class CreateFunctionRequest(_message.Message):
    __slots__ = ('location', 'function')
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    FUNCTION_FIELD_NUMBER: _ClassVar[int]
    location: str
    function: CloudFunction

    def __init__(self, location: _Optional[str]=..., function: _Optional[_Union[CloudFunction, _Mapping]]=...) -> None:
        ...

class UpdateFunctionRequest(_message.Message):
    __slots__ = ('function', 'update_mask')
    FUNCTION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    function: CloudFunction
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, function: _Optional[_Union[CloudFunction, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class GetFunctionRequest(_message.Message):
    __slots__ = ('name', 'version_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    version_id: int

    def __init__(self, name: _Optional[str]=..., version_id: _Optional[int]=...) -> None:
        ...

class ListFunctionsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListFunctionsResponse(_message.Message):
    __slots__ = ('functions', 'next_page_token', 'unreachable')
    FUNCTIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    functions: _containers.RepeatedCompositeFieldContainer[CloudFunction]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, functions: _Optional[_Iterable[_Union[CloudFunction, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class DeleteFunctionRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CallFunctionRequest(_message.Message):
    __slots__ = ('name', 'data')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    name: str
    data: str

    def __init__(self, name: _Optional[str]=..., data: _Optional[str]=...) -> None:
        ...

class CallFunctionResponse(_message.Message):
    __slots__ = ('execution_id', 'result', 'error')
    EXECUTION_ID_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    execution_id: str
    result: str
    error: str

    def __init__(self, execution_id: _Optional[str]=..., result: _Optional[str]=..., error: _Optional[str]=...) -> None:
        ...

class GenerateUploadUrlRequest(_message.Message):
    __slots__ = ('parent', 'kms_key_name')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    KMS_KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    parent: str
    kms_key_name: str

    def __init__(self, parent: _Optional[str]=..., kms_key_name: _Optional[str]=...) -> None:
        ...

class GenerateUploadUrlResponse(_message.Message):
    __slots__ = ('upload_url',)
    UPLOAD_URL_FIELD_NUMBER: _ClassVar[int]
    upload_url: str

    def __init__(self, upload_url: _Optional[str]=...) -> None:
        ...

class GenerateDownloadUrlRequest(_message.Message):
    __slots__ = ('name', 'version_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    version_id: int

    def __init__(self, name: _Optional[str]=..., version_id: _Optional[int]=...) -> None:
        ...

class GenerateDownloadUrlResponse(_message.Message):
    __slots__ = ('download_url',)
    DOWNLOAD_URL_FIELD_NUMBER: _ClassVar[int]
    download_url: str

    def __init__(self, download_url: _Optional[str]=...) -> None:
        ...