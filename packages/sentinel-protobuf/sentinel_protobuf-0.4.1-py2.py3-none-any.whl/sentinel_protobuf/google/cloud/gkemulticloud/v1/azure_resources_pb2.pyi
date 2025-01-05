from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.gkemulticloud.v1 import common_resources_pb2 as _common_resources_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.type import date_pb2 as _date_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AzureCluster(_message.Message):
    __slots__ = ("name", "description", "azure_region", "resource_group_id", "azure_client", "networking", "control_plane", "authorization", "azure_services_authentication", "state", "endpoint", "uid", "reconciling", "create_time", "update_time", "etag", "annotations", "workload_identity_config", "cluster_ca_certificate", "fleet", "managed_resources", "logging_config", "errors", "monitoring_config")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[AzureCluster.State]
        PROVISIONING: _ClassVar[AzureCluster.State]
        RUNNING: _ClassVar[AzureCluster.State]
        RECONCILING: _ClassVar[AzureCluster.State]
        STOPPING: _ClassVar[AzureCluster.State]
        ERROR: _ClassVar[AzureCluster.State]
        DEGRADED: _ClassVar[AzureCluster.State]
    STATE_UNSPECIFIED: AzureCluster.State
    PROVISIONING: AzureCluster.State
    RUNNING: AzureCluster.State
    RECONCILING: AzureCluster.State
    STOPPING: AzureCluster.State
    ERROR: AzureCluster.State
    DEGRADED: AzureCluster.State
    class AnnotationsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    AZURE_REGION_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    AZURE_CLIENT_FIELD_NUMBER: _ClassVar[int]
    NETWORKING_FIELD_NUMBER: _ClassVar[int]
    CONTROL_PLANE_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZATION_FIELD_NUMBER: _ClassVar[int]
    AZURE_SERVICES_AUTHENTICATION_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    RECONCILING_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    WORKLOAD_IDENTITY_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_CA_CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    FLEET_FIELD_NUMBER: _ClassVar[int]
    MANAGED_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    LOGGING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    MONITORING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    azure_region: str
    resource_group_id: str
    azure_client: str
    networking: AzureClusterNetworking
    control_plane: AzureControlPlane
    authorization: AzureAuthorization
    azure_services_authentication: AzureServicesAuthentication
    state: AzureCluster.State
    endpoint: str
    uid: str
    reconciling: bool
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    etag: str
    annotations: _containers.ScalarMap[str, str]
    workload_identity_config: _common_resources_pb2.WorkloadIdentityConfig
    cluster_ca_certificate: str
    fleet: _common_resources_pb2.Fleet
    managed_resources: AzureClusterResources
    logging_config: _common_resources_pb2.LoggingConfig
    errors: _containers.RepeatedCompositeFieldContainer[AzureClusterError]
    monitoring_config: _common_resources_pb2.MonitoringConfig
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., azure_region: _Optional[str] = ..., resource_group_id: _Optional[str] = ..., azure_client: _Optional[str] = ..., networking: _Optional[_Union[AzureClusterNetworking, _Mapping]] = ..., control_plane: _Optional[_Union[AzureControlPlane, _Mapping]] = ..., authorization: _Optional[_Union[AzureAuthorization, _Mapping]] = ..., azure_services_authentication: _Optional[_Union[AzureServicesAuthentication, _Mapping]] = ..., state: _Optional[_Union[AzureCluster.State, str]] = ..., endpoint: _Optional[str] = ..., uid: _Optional[str] = ..., reconciling: bool = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., etag: _Optional[str] = ..., annotations: _Optional[_Mapping[str, str]] = ..., workload_identity_config: _Optional[_Union[_common_resources_pb2.WorkloadIdentityConfig, _Mapping]] = ..., cluster_ca_certificate: _Optional[str] = ..., fleet: _Optional[_Union[_common_resources_pb2.Fleet, _Mapping]] = ..., managed_resources: _Optional[_Union[AzureClusterResources, _Mapping]] = ..., logging_config: _Optional[_Union[_common_resources_pb2.LoggingConfig, _Mapping]] = ..., errors: _Optional[_Iterable[_Union[AzureClusterError, _Mapping]]] = ..., monitoring_config: _Optional[_Union[_common_resources_pb2.MonitoringConfig, _Mapping]] = ...) -> None: ...

class AzureClusterNetworking(_message.Message):
    __slots__ = ("virtual_network_id", "pod_address_cidr_blocks", "service_address_cidr_blocks", "service_load_balancer_subnet_id")
    VIRTUAL_NETWORK_ID_FIELD_NUMBER: _ClassVar[int]
    POD_ADDRESS_CIDR_BLOCKS_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ADDRESS_CIDR_BLOCKS_FIELD_NUMBER: _ClassVar[int]
    SERVICE_LOAD_BALANCER_SUBNET_ID_FIELD_NUMBER: _ClassVar[int]
    virtual_network_id: str
    pod_address_cidr_blocks: _containers.RepeatedScalarFieldContainer[str]
    service_address_cidr_blocks: _containers.RepeatedScalarFieldContainer[str]
    service_load_balancer_subnet_id: str
    def __init__(self, virtual_network_id: _Optional[str] = ..., pod_address_cidr_blocks: _Optional[_Iterable[str]] = ..., service_address_cidr_blocks: _Optional[_Iterable[str]] = ..., service_load_balancer_subnet_id: _Optional[str] = ...) -> None: ...

class AzureControlPlane(_message.Message):
    __slots__ = ("version", "subnet_id", "vm_size", "ssh_config", "root_volume", "main_volume", "database_encryption", "proxy_config", "config_encryption", "tags", "replica_placements", "endpoint_subnet_id")
    class TagsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    VERSION_FIELD_NUMBER: _ClassVar[int]
    SUBNET_ID_FIELD_NUMBER: _ClassVar[int]
    VM_SIZE_FIELD_NUMBER: _ClassVar[int]
    SSH_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ROOT_VOLUME_FIELD_NUMBER: _ClassVar[int]
    MAIN_VOLUME_FIELD_NUMBER: _ClassVar[int]
    DATABASE_ENCRYPTION_FIELD_NUMBER: _ClassVar[int]
    PROXY_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CONFIG_ENCRYPTION_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    REPLICA_PLACEMENTS_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_SUBNET_ID_FIELD_NUMBER: _ClassVar[int]
    version: str
    subnet_id: str
    vm_size: str
    ssh_config: AzureSshConfig
    root_volume: AzureDiskTemplate
    main_volume: AzureDiskTemplate
    database_encryption: AzureDatabaseEncryption
    proxy_config: AzureProxyConfig
    config_encryption: AzureConfigEncryption
    tags: _containers.ScalarMap[str, str]
    replica_placements: _containers.RepeatedCompositeFieldContainer[ReplicaPlacement]
    endpoint_subnet_id: str
    def __init__(self, version: _Optional[str] = ..., subnet_id: _Optional[str] = ..., vm_size: _Optional[str] = ..., ssh_config: _Optional[_Union[AzureSshConfig, _Mapping]] = ..., root_volume: _Optional[_Union[AzureDiskTemplate, _Mapping]] = ..., main_volume: _Optional[_Union[AzureDiskTemplate, _Mapping]] = ..., database_encryption: _Optional[_Union[AzureDatabaseEncryption, _Mapping]] = ..., proxy_config: _Optional[_Union[AzureProxyConfig, _Mapping]] = ..., config_encryption: _Optional[_Union[AzureConfigEncryption, _Mapping]] = ..., tags: _Optional[_Mapping[str, str]] = ..., replica_placements: _Optional[_Iterable[_Union[ReplicaPlacement, _Mapping]]] = ..., endpoint_subnet_id: _Optional[str] = ...) -> None: ...

class ReplicaPlacement(_message.Message):
    __slots__ = ("subnet_id", "azure_availability_zone")
    SUBNET_ID_FIELD_NUMBER: _ClassVar[int]
    AZURE_AVAILABILITY_ZONE_FIELD_NUMBER: _ClassVar[int]
    subnet_id: str
    azure_availability_zone: str
    def __init__(self, subnet_id: _Optional[str] = ..., azure_availability_zone: _Optional[str] = ...) -> None: ...

class AzureProxyConfig(_message.Message):
    __slots__ = ("resource_group_id", "secret_id")
    RESOURCE_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    SECRET_ID_FIELD_NUMBER: _ClassVar[int]
    resource_group_id: str
    secret_id: str
    def __init__(self, resource_group_id: _Optional[str] = ..., secret_id: _Optional[str] = ...) -> None: ...

class AzureDatabaseEncryption(_message.Message):
    __slots__ = ("key_id",)
    KEY_ID_FIELD_NUMBER: _ClassVar[int]
    key_id: str
    def __init__(self, key_id: _Optional[str] = ...) -> None: ...

class AzureConfigEncryption(_message.Message):
    __slots__ = ("key_id", "public_key")
    KEY_ID_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    key_id: str
    public_key: str
    def __init__(self, key_id: _Optional[str] = ..., public_key: _Optional[str] = ...) -> None: ...

class AzureDiskTemplate(_message.Message):
    __slots__ = ("size_gib",)
    SIZE_GIB_FIELD_NUMBER: _ClassVar[int]
    size_gib: int
    def __init__(self, size_gib: _Optional[int] = ...) -> None: ...

class AzureClient(_message.Message):
    __slots__ = ("name", "tenant_id", "application_id", "reconciling", "annotations", "pem_certificate", "uid", "create_time", "update_time")
    class AnnotationsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    RECONCILING_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    PEM_CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    tenant_id: str
    application_id: str
    reconciling: bool
    annotations: _containers.ScalarMap[str, str]
    pem_certificate: str
    uid: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    def __init__(self, name: _Optional[str] = ..., tenant_id: _Optional[str] = ..., application_id: _Optional[str] = ..., reconciling: bool = ..., annotations: _Optional[_Mapping[str, str]] = ..., pem_certificate: _Optional[str] = ..., uid: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class AzureAuthorization(_message.Message):
    __slots__ = ("admin_users", "admin_groups")
    ADMIN_USERS_FIELD_NUMBER: _ClassVar[int]
    ADMIN_GROUPS_FIELD_NUMBER: _ClassVar[int]
    admin_users: _containers.RepeatedCompositeFieldContainer[AzureClusterUser]
    admin_groups: _containers.RepeatedCompositeFieldContainer[AzureClusterGroup]
    def __init__(self, admin_users: _Optional[_Iterable[_Union[AzureClusterUser, _Mapping]]] = ..., admin_groups: _Optional[_Iterable[_Union[AzureClusterGroup, _Mapping]]] = ...) -> None: ...

class AzureServicesAuthentication(_message.Message):
    __slots__ = ("tenant_id", "application_id")
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    tenant_id: str
    application_id: str
    def __init__(self, tenant_id: _Optional[str] = ..., application_id: _Optional[str] = ...) -> None: ...

class AzureClusterUser(_message.Message):
    __slots__ = ("username",)
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    username: str
    def __init__(self, username: _Optional[str] = ...) -> None: ...

class AzureClusterGroup(_message.Message):
    __slots__ = ("group",)
    GROUP_FIELD_NUMBER: _ClassVar[int]
    group: str
    def __init__(self, group: _Optional[str] = ...) -> None: ...

class AzureNodePool(_message.Message):
    __slots__ = ("name", "version", "config", "subnet_id", "autoscaling", "state", "uid", "reconciling", "create_time", "update_time", "etag", "annotations", "max_pods_constraint", "azure_availability_zone", "errors", "management")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[AzureNodePool.State]
        PROVISIONING: _ClassVar[AzureNodePool.State]
        RUNNING: _ClassVar[AzureNodePool.State]
        RECONCILING: _ClassVar[AzureNodePool.State]
        STOPPING: _ClassVar[AzureNodePool.State]
        ERROR: _ClassVar[AzureNodePool.State]
        DEGRADED: _ClassVar[AzureNodePool.State]
    STATE_UNSPECIFIED: AzureNodePool.State
    PROVISIONING: AzureNodePool.State
    RUNNING: AzureNodePool.State
    RECONCILING: AzureNodePool.State
    STOPPING: AzureNodePool.State
    ERROR: AzureNodePool.State
    DEGRADED: AzureNodePool.State
    class AnnotationsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    SUBNET_ID_FIELD_NUMBER: _ClassVar[int]
    AUTOSCALING_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    RECONCILING_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    MAX_PODS_CONSTRAINT_FIELD_NUMBER: _ClassVar[int]
    AZURE_AVAILABILITY_ZONE_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    MANAGEMENT_FIELD_NUMBER: _ClassVar[int]
    name: str
    version: str
    config: AzureNodeConfig
    subnet_id: str
    autoscaling: AzureNodePoolAutoscaling
    state: AzureNodePool.State
    uid: str
    reconciling: bool
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    etag: str
    annotations: _containers.ScalarMap[str, str]
    max_pods_constraint: _common_resources_pb2.MaxPodsConstraint
    azure_availability_zone: str
    errors: _containers.RepeatedCompositeFieldContainer[AzureNodePoolError]
    management: AzureNodeManagement
    def __init__(self, name: _Optional[str] = ..., version: _Optional[str] = ..., config: _Optional[_Union[AzureNodeConfig, _Mapping]] = ..., subnet_id: _Optional[str] = ..., autoscaling: _Optional[_Union[AzureNodePoolAutoscaling, _Mapping]] = ..., state: _Optional[_Union[AzureNodePool.State, str]] = ..., uid: _Optional[str] = ..., reconciling: bool = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., etag: _Optional[str] = ..., annotations: _Optional[_Mapping[str, str]] = ..., max_pods_constraint: _Optional[_Union[_common_resources_pb2.MaxPodsConstraint, _Mapping]] = ..., azure_availability_zone: _Optional[str] = ..., errors: _Optional[_Iterable[_Union[AzureNodePoolError, _Mapping]]] = ..., management: _Optional[_Union[AzureNodeManagement, _Mapping]] = ...) -> None: ...

class AzureNodeManagement(_message.Message):
    __slots__ = ("auto_repair",)
    AUTO_REPAIR_FIELD_NUMBER: _ClassVar[int]
    auto_repair: bool
    def __init__(self, auto_repair: bool = ...) -> None: ...

class AzureNodeConfig(_message.Message):
    __slots__ = ("vm_size", "root_volume", "tags", "image_type", "ssh_config", "proxy_config", "config_encryption", "taints", "labels")
    class TagsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    VM_SIZE_FIELD_NUMBER: _ClassVar[int]
    ROOT_VOLUME_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    IMAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    SSH_CONFIG_FIELD_NUMBER: _ClassVar[int]
    PROXY_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CONFIG_ENCRYPTION_FIELD_NUMBER: _ClassVar[int]
    TAINTS_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    vm_size: str
    root_volume: AzureDiskTemplate
    tags: _containers.ScalarMap[str, str]
    image_type: str
    ssh_config: AzureSshConfig
    proxy_config: AzureProxyConfig
    config_encryption: AzureConfigEncryption
    taints: _containers.RepeatedCompositeFieldContainer[_common_resources_pb2.NodeTaint]
    labels: _containers.ScalarMap[str, str]
    def __init__(self, vm_size: _Optional[str] = ..., root_volume: _Optional[_Union[AzureDiskTemplate, _Mapping]] = ..., tags: _Optional[_Mapping[str, str]] = ..., image_type: _Optional[str] = ..., ssh_config: _Optional[_Union[AzureSshConfig, _Mapping]] = ..., proxy_config: _Optional[_Union[AzureProxyConfig, _Mapping]] = ..., config_encryption: _Optional[_Union[AzureConfigEncryption, _Mapping]] = ..., taints: _Optional[_Iterable[_Union[_common_resources_pb2.NodeTaint, _Mapping]]] = ..., labels: _Optional[_Mapping[str, str]] = ...) -> None: ...

class AzureNodePoolAutoscaling(_message.Message):
    __slots__ = ("min_node_count", "max_node_count")
    MIN_NODE_COUNT_FIELD_NUMBER: _ClassVar[int]
    MAX_NODE_COUNT_FIELD_NUMBER: _ClassVar[int]
    min_node_count: int
    max_node_count: int
    def __init__(self, min_node_count: _Optional[int] = ..., max_node_count: _Optional[int] = ...) -> None: ...

class AzureOpenIdConfig(_message.Message):
    __slots__ = ("issuer", "jwks_uri", "response_types_supported", "subject_types_supported", "id_token_signing_alg_values_supported", "claims_supported", "grant_types")
    ISSUER_FIELD_NUMBER: _ClassVar[int]
    JWKS_URI_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_TYPES_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_TYPES_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    ID_TOKEN_SIGNING_ALG_VALUES_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    CLAIMS_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    GRANT_TYPES_FIELD_NUMBER: _ClassVar[int]
    issuer: str
    jwks_uri: str
    response_types_supported: _containers.RepeatedScalarFieldContainer[str]
    subject_types_supported: _containers.RepeatedScalarFieldContainer[str]
    id_token_signing_alg_values_supported: _containers.RepeatedScalarFieldContainer[str]
    claims_supported: _containers.RepeatedScalarFieldContainer[str]
    grant_types: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, issuer: _Optional[str] = ..., jwks_uri: _Optional[str] = ..., response_types_supported: _Optional[_Iterable[str]] = ..., subject_types_supported: _Optional[_Iterable[str]] = ..., id_token_signing_alg_values_supported: _Optional[_Iterable[str]] = ..., claims_supported: _Optional[_Iterable[str]] = ..., grant_types: _Optional[_Iterable[str]] = ...) -> None: ...

class AzureJsonWebKeys(_message.Message):
    __slots__ = ("keys",)
    KEYS_FIELD_NUMBER: _ClassVar[int]
    keys: _containers.RepeatedCompositeFieldContainer[_common_resources_pb2.Jwk]
    def __init__(self, keys: _Optional[_Iterable[_Union[_common_resources_pb2.Jwk, _Mapping]]] = ...) -> None: ...

class AzureServerConfig(_message.Message):
    __slots__ = ("name", "valid_versions", "supported_azure_regions")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALID_VERSIONS_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_AZURE_REGIONS_FIELD_NUMBER: _ClassVar[int]
    name: str
    valid_versions: _containers.RepeatedCompositeFieldContainer[AzureK8sVersionInfo]
    supported_azure_regions: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, name: _Optional[str] = ..., valid_versions: _Optional[_Iterable[_Union[AzureK8sVersionInfo, _Mapping]]] = ..., supported_azure_regions: _Optional[_Iterable[str]] = ...) -> None: ...

class AzureK8sVersionInfo(_message.Message):
    __slots__ = ("version", "enabled", "end_of_life", "end_of_life_date", "release_date")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    END_OF_LIFE_FIELD_NUMBER: _ClassVar[int]
    END_OF_LIFE_DATE_FIELD_NUMBER: _ClassVar[int]
    RELEASE_DATE_FIELD_NUMBER: _ClassVar[int]
    version: str
    enabled: bool
    end_of_life: bool
    end_of_life_date: _date_pb2.Date
    release_date: _date_pb2.Date
    def __init__(self, version: _Optional[str] = ..., enabled: bool = ..., end_of_life: bool = ..., end_of_life_date: _Optional[_Union[_date_pb2.Date, _Mapping]] = ..., release_date: _Optional[_Union[_date_pb2.Date, _Mapping]] = ...) -> None: ...

class AzureSshConfig(_message.Message):
    __slots__ = ("authorized_key",)
    AUTHORIZED_KEY_FIELD_NUMBER: _ClassVar[int]
    authorized_key: str
    def __init__(self, authorized_key: _Optional[str] = ...) -> None: ...

class AzureClusterResources(_message.Message):
    __slots__ = ("network_security_group_id", "control_plane_application_security_group_id")
    NETWORK_SECURITY_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    CONTROL_PLANE_APPLICATION_SECURITY_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    network_security_group_id: str
    control_plane_application_security_group_id: str
    def __init__(self, network_security_group_id: _Optional[str] = ..., control_plane_application_security_group_id: _Optional[str] = ...) -> None: ...

class AzureClusterError(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class AzureNodePoolError(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...
