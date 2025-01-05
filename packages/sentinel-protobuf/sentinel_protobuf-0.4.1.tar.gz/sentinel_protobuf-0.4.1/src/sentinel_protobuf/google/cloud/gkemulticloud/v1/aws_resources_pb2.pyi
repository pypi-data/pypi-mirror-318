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

class AwsCluster(_message.Message):
    __slots__ = ("name", "description", "networking", "aws_region", "control_plane", "authorization", "state", "endpoint", "uid", "reconciling", "create_time", "update_time", "etag", "annotations", "workload_identity_config", "cluster_ca_certificate", "fleet", "logging_config", "errors", "monitoring_config", "binary_authorization")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[AwsCluster.State]
        PROVISIONING: _ClassVar[AwsCluster.State]
        RUNNING: _ClassVar[AwsCluster.State]
        RECONCILING: _ClassVar[AwsCluster.State]
        STOPPING: _ClassVar[AwsCluster.State]
        ERROR: _ClassVar[AwsCluster.State]
        DEGRADED: _ClassVar[AwsCluster.State]
    STATE_UNSPECIFIED: AwsCluster.State
    PROVISIONING: AwsCluster.State
    RUNNING: AwsCluster.State
    RECONCILING: AwsCluster.State
    STOPPING: AwsCluster.State
    ERROR: AwsCluster.State
    DEGRADED: AwsCluster.State
    class AnnotationsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    NETWORKING_FIELD_NUMBER: _ClassVar[int]
    AWS_REGION_FIELD_NUMBER: _ClassVar[int]
    CONTROL_PLANE_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZATION_FIELD_NUMBER: _ClassVar[int]
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
    LOGGING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    MONITORING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    BINARY_AUTHORIZATION_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    networking: AwsClusterNetworking
    aws_region: str
    control_plane: AwsControlPlane
    authorization: AwsAuthorization
    state: AwsCluster.State
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
    logging_config: _common_resources_pb2.LoggingConfig
    errors: _containers.RepeatedCompositeFieldContainer[AwsClusterError]
    monitoring_config: _common_resources_pb2.MonitoringConfig
    binary_authorization: _common_resources_pb2.BinaryAuthorization
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., networking: _Optional[_Union[AwsClusterNetworking, _Mapping]] = ..., aws_region: _Optional[str] = ..., control_plane: _Optional[_Union[AwsControlPlane, _Mapping]] = ..., authorization: _Optional[_Union[AwsAuthorization, _Mapping]] = ..., state: _Optional[_Union[AwsCluster.State, str]] = ..., endpoint: _Optional[str] = ..., uid: _Optional[str] = ..., reconciling: bool = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., etag: _Optional[str] = ..., annotations: _Optional[_Mapping[str, str]] = ..., workload_identity_config: _Optional[_Union[_common_resources_pb2.WorkloadIdentityConfig, _Mapping]] = ..., cluster_ca_certificate: _Optional[str] = ..., fleet: _Optional[_Union[_common_resources_pb2.Fleet, _Mapping]] = ..., logging_config: _Optional[_Union[_common_resources_pb2.LoggingConfig, _Mapping]] = ..., errors: _Optional[_Iterable[_Union[AwsClusterError, _Mapping]]] = ..., monitoring_config: _Optional[_Union[_common_resources_pb2.MonitoringConfig, _Mapping]] = ..., binary_authorization: _Optional[_Union[_common_resources_pb2.BinaryAuthorization, _Mapping]] = ...) -> None: ...

class AwsControlPlane(_message.Message):
    __slots__ = ("version", "instance_type", "ssh_config", "subnet_ids", "security_group_ids", "iam_instance_profile", "root_volume", "main_volume", "database_encryption", "tags", "aws_services_authentication", "proxy_config", "config_encryption", "instance_placement")
    class TagsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    VERSION_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    SSH_CONFIG_FIELD_NUMBER: _ClassVar[int]
    SUBNET_IDS_FIELD_NUMBER: _ClassVar[int]
    SECURITY_GROUP_IDS_FIELD_NUMBER: _ClassVar[int]
    IAM_INSTANCE_PROFILE_FIELD_NUMBER: _ClassVar[int]
    ROOT_VOLUME_FIELD_NUMBER: _ClassVar[int]
    MAIN_VOLUME_FIELD_NUMBER: _ClassVar[int]
    DATABASE_ENCRYPTION_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    AWS_SERVICES_AUTHENTICATION_FIELD_NUMBER: _ClassVar[int]
    PROXY_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CONFIG_ENCRYPTION_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_PLACEMENT_FIELD_NUMBER: _ClassVar[int]
    version: str
    instance_type: str
    ssh_config: AwsSshConfig
    subnet_ids: _containers.RepeatedScalarFieldContainer[str]
    security_group_ids: _containers.RepeatedScalarFieldContainer[str]
    iam_instance_profile: str
    root_volume: AwsVolumeTemplate
    main_volume: AwsVolumeTemplate
    database_encryption: AwsDatabaseEncryption
    tags: _containers.ScalarMap[str, str]
    aws_services_authentication: AwsServicesAuthentication
    proxy_config: AwsProxyConfig
    config_encryption: AwsConfigEncryption
    instance_placement: AwsInstancePlacement
    def __init__(self, version: _Optional[str] = ..., instance_type: _Optional[str] = ..., ssh_config: _Optional[_Union[AwsSshConfig, _Mapping]] = ..., subnet_ids: _Optional[_Iterable[str]] = ..., security_group_ids: _Optional[_Iterable[str]] = ..., iam_instance_profile: _Optional[str] = ..., root_volume: _Optional[_Union[AwsVolumeTemplate, _Mapping]] = ..., main_volume: _Optional[_Union[AwsVolumeTemplate, _Mapping]] = ..., database_encryption: _Optional[_Union[AwsDatabaseEncryption, _Mapping]] = ..., tags: _Optional[_Mapping[str, str]] = ..., aws_services_authentication: _Optional[_Union[AwsServicesAuthentication, _Mapping]] = ..., proxy_config: _Optional[_Union[AwsProxyConfig, _Mapping]] = ..., config_encryption: _Optional[_Union[AwsConfigEncryption, _Mapping]] = ..., instance_placement: _Optional[_Union[AwsInstancePlacement, _Mapping]] = ...) -> None: ...

class AwsServicesAuthentication(_message.Message):
    __slots__ = ("role_arn", "role_session_name")
    ROLE_ARN_FIELD_NUMBER: _ClassVar[int]
    ROLE_SESSION_NAME_FIELD_NUMBER: _ClassVar[int]
    role_arn: str
    role_session_name: str
    def __init__(self, role_arn: _Optional[str] = ..., role_session_name: _Optional[str] = ...) -> None: ...

class AwsAuthorization(_message.Message):
    __slots__ = ("admin_users", "admin_groups")
    ADMIN_USERS_FIELD_NUMBER: _ClassVar[int]
    ADMIN_GROUPS_FIELD_NUMBER: _ClassVar[int]
    admin_users: _containers.RepeatedCompositeFieldContainer[AwsClusterUser]
    admin_groups: _containers.RepeatedCompositeFieldContainer[AwsClusterGroup]
    def __init__(self, admin_users: _Optional[_Iterable[_Union[AwsClusterUser, _Mapping]]] = ..., admin_groups: _Optional[_Iterable[_Union[AwsClusterGroup, _Mapping]]] = ...) -> None: ...

class AwsClusterUser(_message.Message):
    __slots__ = ("username",)
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    username: str
    def __init__(self, username: _Optional[str] = ...) -> None: ...

class AwsClusterGroup(_message.Message):
    __slots__ = ("group",)
    GROUP_FIELD_NUMBER: _ClassVar[int]
    group: str
    def __init__(self, group: _Optional[str] = ...) -> None: ...

class AwsDatabaseEncryption(_message.Message):
    __slots__ = ("kms_key_arn",)
    KMS_KEY_ARN_FIELD_NUMBER: _ClassVar[int]
    kms_key_arn: str
    def __init__(self, kms_key_arn: _Optional[str] = ...) -> None: ...

class AwsVolumeTemplate(_message.Message):
    __slots__ = ("size_gib", "volume_type", "iops", "throughput", "kms_key_arn")
    class VolumeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        VOLUME_TYPE_UNSPECIFIED: _ClassVar[AwsVolumeTemplate.VolumeType]
        GP2: _ClassVar[AwsVolumeTemplate.VolumeType]
        GP3: _ClassVar[AwsVolumeTemplate.VolumeType]
    VOLUME_TYPE_UNSPECIFIED: AwsVolumeTemplate.VolumeType
    GP2: AwsVolumeTemplate.VolumeType
    GP3: AwsVolumeTemplate.VolumeType
    SIZE_GIB_FIELD_NUMBER: _ClassVar[int]
    VOLUME_TYPE_FIELD_NUMBER: _ClassVar[int]
    IOPS_FIELD_NUMBER: _ClassVar[int]
    THROUGHPUT_FIELD_NUMBER: _ClassVar[int]
    KMS_KEY_ARN_FIELD_NUMBER: _ClassVar[int]
    size_gib: int
    volume_type: AwsVolumeTemplate.VolumeType
    iops: int
    throughput: int
    kms_key_arn: str
    def __init__(self, size_gib: _Optional[int] = ..., volume_type: _Optional[_Union[AwsVolumeTemplate.VolumeType, str]] = ..., iops: _Optional[int] = ..., throughput: _Optional[int] = ..., kms_key_arn: _Optional[str] = ...) -> None: ...

class AwsClusterNetworking(_message.Message):
    __slots__ = ("vpc_id", "pod_address_cidr_blocks", "service_address_cidr_blocks", "per_node_pool_sg_rules_disabled")
    VPC_ID_FIELD_NUMBER: _ClassVar[int]
    POD_ADDRESS_CIDR_BLOCKS_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ADDRESS_CIDR_BLOCKS_FIELD_NUMBER: _ClassVar[int]
    PER_NODE_POOL_SG_RULES_DISABLED_FIELD_NUMBER: _ClassVar[int]
    vpc_id: str
    pod_address_cidr_blocks: _containers.RepeatedScalarFieldContainer[str]
    service_address_cidr_blocks: _containers.RepeatedScalarFieldContainer[str]
    per_node_pool_sg_rules_disabled: bool
    def __init__(self, vpc_id: _Optional[str] = ..., pod_address_cidr_blocks: _Optional[_Iterable[str]] = ..., service_address_cidr_blocks: _Optional[_Iterable[str]] = ..., per_node_pool_sg_rules_disabled: bool = ...) -> None: ...

class AwsNodePool(_message.Message):
    __slots__ = ("name", "version", "config", "autoscaling", "subnet_id", "state", "uid", "reconciling", "create_time", "update_time", "etag", "annotations", "max_pods_constraint", "errors", "management", "kubelet_config", "update_settings")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[AwsNodePool.State]
        PROVISIONING: _ClassVar[AwsNodePool.State]
        RUNNING: _ClassVar[AwsNodePool.State]
        RECONCILING: _ClassVar[AwsNodePool.State]
        STOPPING: _ClassVar[AwsNodePool.State]
        ERROR: _ClassVar[AwsNodePool.State]
        DEGRADED: _ClassVar[AwsNodePool.State]
    STATE_UNSPECIFIED: AwsNodePool.State
    PROVISIONING: AwsNodePool.State
    RUNNING: AwsNodePool.State
    RECONCILING: AwsNodePool.State
    STOPPING: AwsNodePool.State
    ERROR: AwsNodePool.State
    DEGRADED: AwsNodePool.State
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
    AUTOSCALING_FIELD_NUMBER: _ClassVar[int]
    SUBNET_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    RECONCILING_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    MAX_PODS_CONSTRAINT_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    MANAGEMENT_FIELD_NUMBER: _ClassVar[int]
    KUBELET_CONFIG_FIELD_NUMBER: _ClassVar[int]
    UPDATE_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    name: str
    version: str
    config: AwsNodeConfig
    autoscaling: AwsNodePoolAutoscaling
    subnet_id: str
    state: AwsNodePool.State
    uid: str
    reconciling: bool
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    etag: str
    annotations: _containers.ScalarMap[str, str]
    max_pods_constraint: _common_resources_pb2.MaxPodsConstraint
    errors: _containers.RepeatedCompositeFieldContainer[AwsNodePoolError]
    management: AwsNodeManagement
    kubelet_config: _common_resources_pb2.NodeKubeletConfig
    update_settings: UpdateSettings
    def __init__(self, name: _Optional[str] = ..., version: _Optional[str] = ..., config: _Optional[_Union[AwsNodeConfig, _Mapping]] = ..., autoscaling: _Optional[_Union[AwsNodePoolAutoscaling, _Mapping]] = ..., subnet_id: _Optional[str] = ..., state: _Optional[_Union[AwsNodePool.State, str]] = ..., uid: _Optional[str] = ..., reconciling: bool = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., etag: _Optional[str] = ..., annotations: _Optional[_Mapping[str, str]] = ..., max_pods_constraint: _Optional[_Union[_common_resources_pb2.MaxPodsConstraint, _Mapping]] = ..., errors: _Optional[_Iterable[_Union[AwsNodePoolError, _Mapping]]] = ..., management: _Optional[_Union[AwsNodeManagement, _Mapping]] = ..., kubelet_config: _Optional[_Union[_common_resources_pb2.NodeKubeletConfig, _Mapping]] = ..., update_settings: _Optional[_Union[UpdateSettings, _Mapping]] = ...) -> None: ...

class UpdateSettings(_message.Message):
    __slots__ = ("surge_settings",)
    SURGE_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    surge_settings: SurgeSettings
    def __init__(self, surge_settings: _Optional[_Union[SurgeSettings, _Mapping]] = ...) -> None: ...

class SurgeSettings(_message.Message):
    __slots__ = ("max_surge", "max_unavailable")
    MAX_SURGE_FIELD_NUMBER: _ClassVar[int]
    MAX_UNAVAILABLE_FIELD_NUMBER: _ClassVar[int]
    max_surge: int
    max_unavailable: int
    def __init__(self, max_surge: _Optional[int] = ..., max_unavailable: _Optional[int] = ...) -> None: ...

class AwsNodeManagement(_message.Message):
    __slots__ = ("auto_repair",)
    AUTO_REPAIR_FIELD_NUMBER: _ClassVar[int]
    auto_repair: bool
    def __init__(self, auto_repair: bool = ...) -> None: ...

class AwsNodeConfig(_message.Message):
    __slots__ = ("instance_type", "root_volume", "taints", "labels", "tags", "iam_instance_profile", "image_type", "ssh_config", "security_group_ids", "proxy_config", "config_encryption", "instance_placement", "autoscaling_metrics_collection", "spot_config")
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class TagsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    INSTANCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    ROOT_VOLUME_FIELD_NUMBER: _ClassVar[int]
    TAINTS_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    IAM_INSTANCE_PROFILE_FIELD_NUMBER: _ClassVar[int]
    IMAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    SSH_CONFIG_FIELD_NUMBER: _ClassVar[int]
    SECURITY_GROUP_IDS_FIELD_NUMBER: _ClassVar[int]
    PROXY_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CONFIG_ENCRYPTION_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_PLACEMENT_FIELD_NUMBER: _ClassVar[int]
    AUTOSCALING_METRICS_COLLECTION_FIELD_NUMBER: _ClassVar[int]
    SPOT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    instance_type: str
    root_volume: AwsVolumeTemplate
    taints: _containers.RepeatedCompositeFieldContainer[_common_resources_pb2.NodeTaint]
    labels: _containers.ScalarMap[str, str]
    tags: _containers.ScalarMap[str, str]
    iam_instance_profile: str
    image_type: str
    ssh_config: AwsSshConfig
    security_group_ids: _containers.RepeatedScalarFieldContainer[str]
    proxy_config: AwsProxyConfig
    config_encryption: AwsConfigEncryption
    instance_placement: AwsInstancePlacement
    autoscaling_metrics_collection: AwsAutoscalingGroupMetricsCollection
    spot_config: SpotConfig
    def __init__(self, instance_type: _Optional[str] = ..., root_volume: _Optional[_Union[AwsVolumeTemplate, _Mapping]] = ..., taints: _Optional[_Iterable[_Union[_common_resources_pb2.NodeTaint, _Mapping]]] = ..., labels: _Optional[_Mapping[str, str]] = ..., tags: _Optional[_Mapping[str, str]] = ..., iam_instance_profile: _Optional[str] = ..., image_type: _Optional[str] = ..., ssh_config: _Optional[_Union[AwsSshConfig, _Mapping]] = ..., security_group_ids: _Optional[_Iterable[str]] = ..., proxy_config: _Optional[_Union[AwsProxyConfig, _Mapping]] = ..., config_encryption: _Optional[_Union[AwsConfigEncryption, _Mapping]] = ..., instance_placement: _Optional[_Union[AwsInstancePlacement, _Mapping]] = ..., autoscaling_metrics_collection: _Optional[_Union[AwsAutoscalingGroupMetricsCollection, _Mapping]] = ..., spot_config: _Optional[_Union[SpotConfig, _Mapping]] = ...) -> None: ...

class AwsNodePoolAutoscaling(_message.Message):
    __slots__ = ("min_node_count", "max_node_count")
    MIN_NODE_COUNT_FIELD_NUMBER: _ClassVar[int]
    MAX_NODE_COUNT_FIELD_NUMBER: _ClassVar[int]
    min_node_count: int
    max_node_count: int
    def __init__(self, min_node_count: _Optional[int] = ..., max_node_count: _Optional[int] = ...) -> None: ...

class AwsOpenIdConfig(_message.Message):
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

class AwsJsonWebKeys(_message.Message):
    __slots__ = ("keys",)
    KEYS_FIELD_NUMBER: _ClassVar[int]
    keys: _containers.RepeatedCompositeFieldContainer[_common_resources_pb2.Jwk]
    def __init__(self, keys: _Optional[_Iterable[_Union[_common_resources_pb2.Jwk, _Mapping]]] = ...) -> None: ...

class AwsServerConfig(_message.Message):
    __slots__ = ("name", "valid_versions", "supported_aws_regions")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALID_VERSIONS_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_AWS_REGIONS_FIELD_NUMBER: _ClassVar[int]
    name: str
    valid_versions: _containers.RepeatedCompositeFieldContainer[AwsK8sVersionInfo]
    supported_aws_regions: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, name: _Optional[str] = ..., valid_versions: _Optional[_Iterable[_Union[AwsK8sVersionInfo, _Mapping]]] = ..., supported_aws_regions: _Optional[_Iterable[str]] = ...) -> None: ...

class AwsK8sVersionInfo(_message.Message):
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

class AwsSshConfig(_message.Message):
    __slots__ = ("ec2_key_pair",)
    EC2_KEY_PAIR_FIELD_NUMBER: _ClassVar[int]
    ec2_key_pair: str
    def __init__(self, ec2_key_pair: _Optional[str] = ...) -> None: ...

class AwsProxyConfig(_message.Message):
    __slots__ = ("secret_arn", "secret_version")
    SECRET_ARN_FIELD_NUMBER: _ClassVar[int]
    SECRET_VERSION_FIELD_NUMBER: _ClassVar[int]
    secret_arn: str
    secret_version: str
    def __init__(self, secret_arn: _Optional[str] = ..., secret_version: _Optional[str] = ...) -> None: ...

class AwsConfigEncryption(_message.Message):
    __slots__ = ("kms_key_arn",)
    KMS_KEY_ARN_FIELD_NUMBER: _ClassVar[int]
    kms_key_arn: str
    def __init__(self, kms_key_arn: _Optional[str] = ...) -> None: ...

class AwsInstancePlacement(_message.Message):
    __slots__ = ("tenancy",)
    class Tenancy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TENANCY_UNSPECIFIED: _ClassVar[AwsInstancePlacement.Tenancy]
        DEFAULT: _ClassVar[AwsInstancePlacement.Tenancy]
        DEDICATED: _ClassVar[AwsInstancePlacement.Tenancy]
        HOST: _ClassVar[AwsInstancePlacement.Tenancy]
    TENANCY_UNSPECIFIED: AwsInstancePlacement.Tenancy
    DEFAULT: AwsInstancePlacement.Tenancy
    DEDICATED: AwsInstancePlacement.Tenancy
    HOST: AwsInstancePlacement.Tenancy
    TENANCY_FIELD_NUMBER: _ClassVar[int]
    tenancy: AwsInstancePlacement.Tenancy
    def __init__(self, tenancy: _Optional[_Union[AwsInstancePlacement.Tenancy, str]] = ...) -> None: ...

class AwsAutoscalingGroupMetricsCollection(_message.Message):
    __slots__ = ("granularity", "metrics")
    GRANULARITY_FIELD_NUMBER: _ClassVar[int]
    METRICS_FIELD_NUMBER: _ClassVar[int]
    granularity: str
    metrics: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, granularity: _Optional[str] = ..., metrics: _Optional[_Iterable[str]] = ...) -> None: ...

class SpotConfig(_message.Message):
    __slots__ = ("instance_types",)
    INSTANCE_TYPES_FIELD_NUMBER: _ClassVar[int]
    instance_types: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, instance_types: _Optional[_Iterable[str]] = ...) -> None: ...

class AwsClusterError(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class AwsNodePoolError(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...
