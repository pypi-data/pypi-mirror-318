from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class WorkstationCluster(_message.Message):
    __slots__ = ('name', 'display_name', 'uid', 'reconciling', 'annotations', 'labels', 'create_time', 'update_time', 'delete_time', 'etag', 'network', 'subnetwork', 'control_plane_ip', 'private_cluster_config', 'degraded', 'conditions')

    class PrivateClusterConfig(_message.Message):
        __slots__ = ('enable_private_endpoint', 'cluster_hostname', 'service_attachment_uri', 'allowed_projects')
        ENABLE_PRIVATE_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
        CLUSTER_HOSTNAME_FIELD_NUMBER: _ClassVar[int]
        SERVICE_ATTACHMENT_URI_FIELD_NUMBER: _ClassVar[int]
        ALLOWED_PROJECTS_FIELD_NUMBER: _ClassVar[int]
        enable_private_endpoint: bool
        cluster_hostname: str
        service_attachment_uri: str
        allowed_projects: _containers.RepeatedScalarFieldContainer[str]

        def __init__(self, enable_private_endpoint: bool=..., cluster_hostname: _Optional[str]=..., service_attachment_uri: _Optional[str]=..., allowed_projects: _Optional[_Iterable[str]]=...) -> None:
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
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    RECONCILING_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DELETE_TIME_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    SUBNETWORK_FIELD_NUMBER: _ClassVar[int]
    CONTROL_PLANE_IP_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_CLUSTER_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DEGRADED_FIELD_NUMBER: _ClassVar[int]
    CONDITIONS_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    uid: str
    reconciling: bool
    annotations: _containers.ScalarMap[str, str]
    labels: _containers.ScalarMap[str, str]
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    delete_time: _timestamp_pb2.Timestamp
    etag: str
    network: str
    subnetwork: str
    control_plane_ip: str
    private_cluster_config: WorkstationCluster.PrivateClusterConfig
    degraded: bool
    conditions: _containers.RepeatedCompositeFieldContainer[_status_pb2.Status]

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., uid: _Optional[str]=..., reconciling: bool=..., annotations: _Optional[_Mapping[str, str]]=..., labels: _Optional[_Mapping[str, str]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., delete_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., etag: _Optional[str]=..., network: _Optional[str]=..., subnetwork: _Optional[str]=..., control_plane_ip: _Optional[str]=..., private_cluster_config: _Optional[_Union[WorkstationCluster.PrivateClusterConfig, _Mapping]]=..., degraded: bool=..., conditions: _Optional[_Iterable[_Union[_status_pb2.Status, _Mapping]]]=...) -> None:
        ...

class WorkstationConfig(_message.Message):
    __slots__ = ('name', 'display_name', 'uid', 'reconciling', 'annotations', 'labels', 'create_time', 'update_time', 'delete_time', 'etag', 'idle_timeout', 'running_timeout', 'host', 'persistent_directories', 'container', 'encryption_key', 'readiness_checks', 'replica_zones', 'degraded', 'conditions')

    class Host(_message.Message):
        __slots__ = ('gce_instance',)

        class GceInstance(_message.Message):
            __slots__ = ('machine_type', 'service_account', 'service_account_scopes', 'tags', 'pool_size', 'pooled_instances', 'disable_public_ip_addresses', 'enable_nested_virtualization', 'shielded_instance_config', 'confidential_instance_config', 'boot_disk_size_gb')

            class GceShieldedInstanceConfig(_message.Message):
                __slots__ = ('enable_secure_boot', 'enable_vtpm', 'enable_integrity_monitoring')
                ENABLE_SECURE_BOOT_FIELD_NUMBER: _ClassVar[int]
                ENABLE_VTPM_FIELD_NUMBER: _ClassVar[int]
                ENABLE_INTEGRITY_MONITORING_FIELD_NUMBER: _ClassVar[int]
                enable_secure_boot: bool
                enable_vtpm: bool
                enable_integrity_monitoring: bool

                def __init__(self, enable_secure_boot: bool=..., enable_vtpm: bool=..., enable_integrity_monitoring: bool=...) -> None:
                    ...

            class GceConfidentialInstanceConfig(_message.Message):
                __slots__ = ('enable_confidential_compute',)
                ENABLE_CONFIDENTIAL_COMPUTE_FIELD_NUMBER: _ClassVar[int]
                enable_confidential_compute: bool

                def __init__(self, enable_confidential_compute: bool=...) -> None:
                    ...
            MACHINE_TYPE_FIELD_NUMBER: _ClassVar[int]
            SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
            SERVICE_ACCOUNT_SCOPES_FIELD_NUMBER: _ClassVar[int]
            TAGS_FIELD_NUMBER: _ClassVar[int]
            POOL_SIZE_FIELD_NUMBER: _ClassVar[int]
            POOLED_INSTANCES_FIELD_NUMBER: _ClassVar[int]
            DISABLE_PUBLIC_IP_ADDRESSES_FIELD_NUMBER: _ClassVar[int]
            ENABLE_NESTED_VIRTUALIZATION_FIELD_NUMBER: _ClassVar[int]
            SHIELDED_INSTANCE_CONFIG_FIELD_NUMBER: _ClassVar[int]
            CONFIDENTIAL_INSTANCE_CONFIG_FIELD_NUMBER: _ClassVar[int]
            BOOT_DISK_SIZE_GB_FIELD_NUMBER: _ClassVar[int]
            machine_type: str
            service_account: str
            service_account_scopes: _containers.RepeatedScalarFieldContainer[str]
            tags: _containers.RepeatedScalarFieldContainer[str]
            pool_size: int
            pooled_instances: int
            disable_public_ip_addresses: bool
            enable_nested_virtualization: bool
            shielded_instance_config: WorkstationConfig.Host.GceInstance.GceShieldedInstanceConfig
            confidential_instance_config: WorkstationConfig.Host.GceInstance.GceConfidentialInstanceConfig
            boot_disk_size_gb: int

            def __init__(self, machine_type: _Optional[str]=..., service_account: _Optional[str]=..., service_account_scopes: _Optional[_Iterable[str]]=..., tags: _Optional[_Iterable[str]]=..., pool_size: _Optional[int]=..., pooled_instances: _Optional[int]=..., disable_public_ip_addresses: bool=..., enable_nested_virtualization: bool=..., shielded_instance_config: _Optional[_Union[WorkstationConfig.Host.GceInstance.GceShieldedInstanceConfig, _Mapping]]=..., confidential_instance_config: _Optional[_Union[WorkstationConfig.Host.GceInstance.GceConfidentialInstanceConfig, _Mapping]]=..., boot_disk_size_gb: _Optional[int]=...) -> None:
                ...
        GCE_INSTANCE_FIELD_NUMBER: _ClassVar[int]
        gce_instance: WorkstationConfig.Host.GceInstance

        def __init__(self, gce_instance: _Optional[_Union[WorkstationConfig.Host.GceInstance, _Mapping]]=...) -> None:
            ...

    class PersistentDirectory(_message.Message):
        __slots__ = ('gce_pd', 'mount_path')

        class GceRegionalPersistentDisk(_message.Message):
            __slots__ = ('size_gb', 'fs_type', 'disk_type', 'source_snapshot', 'reclaim_policy')

            class ReclaimPolicy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                RECLAIM_POLICY_UNSPECIFIED: _ClassVar[WorkstationConfig.PersistentDirectory.GceRegionalPersistentDisk.ReclaimPolicy]
                DELETE: _ClassVar[WorkstationConfig.PersistentDirectory.GceRegionalPersistentDisk.ReclaimPolicy]
                RETAIN: _ClassVar[WorkstationConfig.PersistentDirectory.GceRegionalPersistentDisk.ReclaimPolicy]
            RECLAIM_POLICY_UNSPECIFIED: WorkstationConfig.PersistentDirectory.GceRegionalPersistentDisk.ReclaimPolicy
            DELETE: WorkstationConfig.PersistentDirectory.GceRegionalPersistentDisk.ReclaimPolicy
            RETAIN: WorkstationConfig.PersistentDirectory.GceRegionalPersistentDisk.ReclaimPolicy
            SIZE_GB_FIELD_NUMBER: _ClassVar[int]
            FS_TYPE_FIELD_NUMBER: _ClassVar[int]
            DISK_TYPE_FIELD_NUMBER: _ClassVar[int]
            SOURCE_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
            RECLAIM_POLICY_FIELD_NUMBER: _ClassVar[int]
            size_gb: int
            fs_type: str
            disk_type: str
            source_snapshot: str
            reclaim_policy: WorkstationConfig.PersistentDirectory.GceRegionalPersistentDisk.ReclaimPolicy

            def __init__(self, size_gb: _Optional[int]=..., fs_type: _Optional[str]=..., disk_type: _Optional[str]=..., source_snapshot: _Optional[str]=..., reclaim_policy: _Optional[_Union[WorkstationConfig.PersistentDirectory.GceRegionalPersistentDisk.ReclaimPolicy, str]]=...) -> None:
                ...
        GCE_PD_FIELD_NUMBER: _ClassVar[int]
        MOUNT_PATH_FIELD_NUMBER: _ClassVar[int]
        gce_pd: WorkstationConfig.PersistentDirectory.GceRegionalPersistentDisk
        mount_path: str

        def __init__(self, gce_pd: _Optional[_Union[WorkstationConfig.PersistentDirectory.GceRegionalPersistentDisk, _Mapping]]=..., mount_path: _Optional[str]=...) -> None:
            ...

    class Container(_message.Message):
        __slots__ = ('image', 'command', 'args', 'env', 'working_dir', 'run_as_user')

        class EnvEntry(_message.Message):
            __slots__ = ('key', 'value')
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str

            def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
                ...
        IMAGE_FIELD_NUMBER: _ClassVar[int]
        COMMAND_FIELD_NUMBER: _ClassVar[int]
        ARGS_FIELD_NUMBER: _ClassVar[int]
        ENV_FIELD_NUMBER: _ClassVar[int]
        WORKING_DIR_FIELD_NUMBER: _ClassVar[int]
        RUN_AS_USER_FIELD_NUMBER: _ClassVar[int]
        image: str
        command: _containers.RepeatedScalarFieldContainer[str]
        args: _containers.RepeatedScalarFieldContainer[str]
        env: _containers.ScalarMap[str, str]
        working_dir: str
        run_as_user: int

        def __init__(self, image: _Optional[str]=..., command: _Optional[_Iterable[str]]=..., args: _Optional[_Iterable[str]]=..., env: _Optional[_Mapping[str, str]]=..., working_dir: _Optional[str]=..., run_as_user: _Optional[int]=...) -> None:
            ...

    class CustomerEncryptionKey(_message.Message):
        __slots__ = ('kms_key', 'kms_key_service_account')
        KMS_KEY_FIELD_NUMBER: _ClassVar[int]
        KMS_KEY_SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
        kms_key: str
        kms_key_service_account: str

        def __init__(self, kms_key: _Optional[str]=..., kms_key_service_account: _Optional[str]=...) -> None:
            ...

    class ReadinessCheck(_message.Message):
        __slots__ = ('path', 'port')
        PATH_FIELD_NUMBER: _ClassVar[int]
        PORT_FIELD_NUMBER: _ClassVar[int]
        path: str
        port: int

        def __init__(self, path: _Optional[str]=..., port: _Optional[int]=...) -> None:
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
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    RECONCILING_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DELETE_TIME_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    IDLE_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    RUNNING_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    HOST_FIELD_NUMBER: _ClassVar[int]
    PERSISTENT_DIRECTORIES_FIELD_NUMBER: _ClassVar[int]
    CONTAINER_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_KEY_FIELD_NUMBER: _ClassVar[int]
    READINESS_CHECKS_FIELD_NUMBER: _ClassVar[int]
    REPLICA_ZONES_FIELD_NUMBER: _ClassVar[int]
    DEGRADED_FIELD_NUMBER: _ClassVar[int]
    CONDITIONS_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    uid: str
    reconciling: bool
    annotations: _containers.ScalarMap[str, str]
    labels: _containers.ScalarMap[str, str]
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    delete_time: _timestamp_pb2.Timestamp
    etag: str
    idle_timeout: _duration_pb2.Duration
    running_timeout: _duration_pb2.Duration
    host: WorkstationConfig.Host
    persistent_directories: _containers.RepeatedCompositeFieldContainer[WorkstationConfig.PersistentDirectory]
    container: WorkstationConfig.Container
    encryption_key: WorkstationConfig.CustomerEncryptionKey
    readiness_checks: _containers.RepeatedCompositeFieldContainer[WorkstationConfig.ReadinessCheck]
    replica_zones: _containers.RepeatedScalarFieldContainer[str]
    degraded: bool
    conditions: _containers.RepeatedCompositeFieldContainer[_status_pb2.Status]

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., uid: _Optional[str]=..., reconciling: bool=..., annotations: _Optional[_Mapping[str, str]]=..., labels: _Optional[_Mapping[str, str]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., delete_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., etag: _Optional[str]=..., idle_timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., running_timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., host: _Optional[_Union[WorkstationConfig.Host, _Mapping]]=..., persistent_directories: _Optional[_Iterable[_Union[WorkstationConfig.PersistentDirectory, _Mapping]]]=..., container: _Optional[_Union[WorkstationConfig.Container, _Mapping]]=..., encryption_key: _Optional[_Union[WorkstationConfig.CustomerEncryptionKey, _Mapping]]=..., readiness_checks: _Optional[_Iterable[_Union[WorkstationConfig.ReadinessCheck, _Mapping]]]=..., replica_zones: _Optional[_Iterable[str]]=..., degraded: bool=..., conditions: _Optional[_Iterable[_Union[_status_pb2.Status, _Mapping]]]=...) -> None:
        ...

class Workstation(_message.Message):
    __slots__ = ('name', 'display_name', 'uid', 'reconciling', 'annotations', 'labels', 'create_time', 'update_time', 'start_time', 'delete_time', 'etag', 'state', 'host')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Workstation.State]
        STATE_STARTING: _ClassVar[Workstation.State]
        STATE_RUNNING: _ClassVar[Workstation.State]
        STATE_STOPPING: _ClassVar[Workstation.State]
        STATE_STOPPED: _ClassVar[Workstation.State]
    STATE_UNSPECIFIED: Workstation.State
    STATE_STARTING: Workstation.State
    STATE_RUNNING: Workstation.State
    STATE_STOPPING: Workstation.State
    STATE_STOPPED: Workstation.State

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
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    RECONCILING_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    DELETE_TIME_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    HOST_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    uid: str
    reconciling: bool
    annotations: _containers.ScalarMap[str, str]
    labels: _containers.ScalarMap[str, str]
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    start_time: _timestamp_pb2.Timestamp
    delete_time: _timestamp_pb2.Timestamp
    etag: str
    state: Workstation.State
    host: str

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., uid: _Optional[str]=..., reconciling: bool=..., annotations: _Optional[_Mapping[str, str]]=..., labels: _Optional[_Mapping[str, str]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., delete_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., etag: _Optional[str]=..., state: _Optional[_Union[Workstation.State, str]]=..., host: _Optional[str]=...) -> None:
        ...

class GetWorkstationClusterRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListWorkstationClustersRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListWorkstationClustersResponse(_message.Message):
    __slots__ = ('workstation_clusters', 'next_page_token', 'unreachable')
    WORKSTATION_CLUSTERS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    workstation_clusters: _containers.RepeatedCompositeFieldContainer[WorkstationCluster]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, workstation_clusters: _Optional[_Iterable[_Union[WorkstationCluster, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class CreateWorkstationClusterRequest(_message.Message):
    __slots__ = ('parent', 'workstation_cluster_id', 'workstation_cluster', 'validate_only')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    WORKSTATION_CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    WORKSTATION_CLUSTER_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    workstation_cluster_id: str
    workstation_cluster: WorkstationCluster
    validate_only: bool

    def __init__(self, parent: _Optional[str]=..., workstation_cluster_id: _Optional[str]=..., workstation_cluster: _Optional[_Union[WorkstationCluster, _Mapping]]=..., validate_only: bool=...) -> None:
        ...

class UpdateWorkstationClusterRequest(_message.Message):
    __slots__ = ('workstation_cluster', 'update_mask', 'validate_only', 'allow_missing')
    WORKSTATION_CLUSTER_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MISSING_FIELD_NUMBER: _ClassVar[int]
    workstation_cluster: WorkstationCluster
    update_mask: _field_mask_pb2.FieldMask
    validate_only: bool
    allow_missing: bool

    def __init__(self, workstation_cluster: _Optional[_Union[WorkstationCluster, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., validate_only: bool=..., allow_missing: bool=...) -> None:
        ...

class DeleteWorkstationClusterRequest(_message.Message):
    __slots__ = ('name', 'validate_only', 'etag', 'force')
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    validate_only: bool
    etag: str
    force: bool

    def __init__(self, name: _Optional[str]=..., validate_only: bool=..., etag: _Optional[str]=..., force: bool=...) -> None:
        ...

class GetWorkstationConfigRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListWorkstationConfigsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListWorkstationConfigsResponse(_message.Message):
    __slots__ = ('workstation_configs', 'next_page_token', 'unreachable')
    WORKSTATION_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    workstation_configs: _containers.RepeatedCompositeFieldContainer[WorkstationConfig]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, workstation_configs: _Optional[_Iterable[_Union[WorkstationConfig, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class ListUsableWorkstationConfigsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListUsableWorkstationConfigsResponse(_message.Message):
    __slots__ = ('workstation_configs', 'next_page_token', 'unreachable')
    WORKSTATION_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    workstation_configs: _containers.RepeatedCompositeFieldContainer[WorkstationConfig]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, workstation_configs: _Optional[_Iterable[_Union[WorkstationConfig, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class CreateWorkstationConfigRequest(_message.Message):
    __slots__ = ('parent', 'workstation_config_id', 'workstation_config', 'validate_only')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    WORKSTATION_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    WORKSTATION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    workstation_config_id: str
    workstation_config: WorkstationConfig
    validate_only: bool

    def __init__(self, parent: _Optional[str]=..., workstation_config_id: _Optional[str]=..., workstation_config: _Optional[_Union[WorkstationConfig, _Mapping]]=..., validate_only: bool=...) -> None:
        ...

class UpdateWorkstationConfigRequest(_message.Message):
    __slots__ = ('workstation_config', 'update_mask', 'validate_only', 'allow_missing')
    WORKSTATION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MISSING_FIELD_NUMBER: _ClassVar[int]
    workstation_config: WorkstationConfig
    update_mask: _field_mask_pb2.FieldMask
    validate_only: bool
    allow_missing: bool

    def __init__(self, workstation_config: _Optional[_Union[WorkstationConfig, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., validate_only: bool=..., allow_missing: bool=...) -> None:
        ...

class DeleteWorkstationConfigRequest(_message.Message):
    __slots__ = ('name', 'validate_only', 'etag', 'force')
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    validate_only: bool
    etag: str
    force: bool

    def __init__(self, name: _Optional[str]=..., validate_only: bool=..., etag: _Optional[str]=..., force: bool=...) -> None:
        ...

class GetWorkstationRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListWorkstationsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListWorkstationsResponse(_message.Message):
    __slots__ = ('workstations', 'next_page_token', 'unreachable')
    WORKSTATIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    workstations: _containers.RepeatedCompositeFieldContainer[Workstation]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, workstations: _Optional[_Iterable[_Union[Workstation, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class ListUsableWorkstationsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListUsableWorkstationsResponse(_message.Message):
    __slots__ = ('workstations', 'next_page_token', 'unreachable')
    WORKSTATIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    workstations: _containers.RepeatedCompositeFieldContainer[Workstation]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, workstations: _Optional[_Iterable[_Union[Workstation, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class CreateWorkstationRequest(_message.Message):
    __slots__ = ('parent', 'workstation_id', 'workstation', 'validate_only')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    WORKSTATION_ID_FIELD_NUMBER: _ClassVar[int]
    WORKSTATION_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    workstation_id: str
    workstation: Workstation
    validate_only: bool

    def __init__(self, parent: _Optional[str]=..., workstation_id: _Optional[str]=..., workstation: _Optional[_Union[Workstation, _Mapping]]=..., validate_only: bool=...) -> None:
        ...

class UpdateWorkstationRequest(_message.Message):
    __slots__ = ('workstation', 'update_mask', 'validate_only', 'allow_missing')
    WORKSTATION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MISSING_FIELD_NUMBER: _ClassVar[int]
    workstation: Workstation
    update_mask: _field_mask_pb2.FieldMask
    validate_only: bool
    allow_missing: bool

    def __init__(self, workstation: _Optional[_Union[Workstation, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., validate_only: bool=..., allow_missing: bool=...) -> None:
        ...

class DeleteWorkstationRequest(_message.Message):
    __slots__ = ('name', 'validate_only', 'etag')
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    validate_only: bool
    etag: str

    def __init__(self, name: _Optional[str]=..., validate_only: bool=..., etag: _Optional[str]=...) -> None:
        ...

class StartWorkstationRequest(_message.Message):
    __slots__ = ('name', 'validate_only', 'etag')
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    validate_only: bool
    etag: str

    def __init__(self, name: _Optional[str]=..., validate_only: bool=..., etag: _Optional[str]=...) -> None:
        ...

class StopWorkstationRequest(_message.Message):
    __slots__ = ('name', 'validate_only', 'etag')
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    validate_only: bool
    etag: str

    def __init__(self, name: _Optional[str]=..., validate_only: bool=..., etag: _Optional[str]=...) -> None:
        ...

class GenerateAccessTokenRequest(_message.Message):
    __slots__ = ('expire_time', 'ttl', 'workstation')
    EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
    TTL_FIELD_NUMBER: _ClassVar[int]
    WORKSTATION_FIELD_NUMBER: _ClassVar[int]
    expire_time: _timestamp_pb2.Timestamp
    ttl: _duration_pb2.Duration
    workstation: str

    def __init__(self, expire_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., ttl: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., workstation: _Optional[str]=...) -> None:
        ...

class GenerateAccessTokenResponse(_message.Message):
    __slots__ = ('access_token', 'expire_time')
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
    access_token: str
    expire_time: _timestamp_pb2.Timestamp

    def __init__(self, access_token: _Optional[str]=..., expire_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
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