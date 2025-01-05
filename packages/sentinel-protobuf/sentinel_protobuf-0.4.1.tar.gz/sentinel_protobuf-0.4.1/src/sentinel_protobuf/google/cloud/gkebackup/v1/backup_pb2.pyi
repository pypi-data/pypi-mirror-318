from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.gkebackup.v1 import common_pb2 as _common_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Backup(_message.Message):
    __slots__ = ('name', 'uid', 'create_time', 'update_time', 'manual', 'labels', 'delete_lock_days', 'delete_lock_expire_time', 'retain_days', 'retain_expire_time', 'encryption_key', 'all_namespaces', 'selected_namespaces', 'selected_applications', 'contains_volume_data', 'contains_secrets', 'cluster_metadata', 'state', 'state_reason', 'complete_time', 'resource_count', 'volume_count', 'size_bytes', 'etag', 'description', 'pod_count', 'config_backup_size_bytes', 'permissive_mode')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Backup.State]
        CREATING: _ClassVar[Backup.State]
        IN_PROGRESS: _ClassVar[Backup.State]
        SUCCEEDED: _ClassVar[Backup.State]
        FAILED: _ClassVar[Backup.State]
        DELETING: _ClassVar[Backup.State]
    STATE_UNSPECIFIED: Backup.State
    CREATING: Backup.State
    IN_PROGRESS: Backup.State
    SUCCEEDED: Backup.State
    FAILED: Backup.State
    DELETING: Backup.State

    class ClusterMetadata(_message.Message):
        __slots__ = ('cluster', 'k8s_version', 'backup_crd_versions', 'gke_version', 'anthos_version')

        class BackupCrdVersionsEntry(_message.Message):
            __slots__ = ('key', 'value')
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str

            def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
                ...
        CLUSTER_FIELD_NUMBER: _ClassVar[int]
        K8S_VERSION_FIELD_NUMBER: _ClassVar[int]
        BACKUP_CRD_VERSIONS_FIELD_NUMBER: _ClassVar[int]
        GKE_VERSION_FIELD_NUMBER: _ClassVar[int]
        ANTHOS_VERSION_FIELD_NUMBER: _ClassVar[int]
        cluster: str
        k8s_version: str
        backup_crd_versions: _containers.ScalarMap[str, str]
        gke_version: str
        anthos_version: str

        def __init__(self, cluster: _Optional[str]=..., k8s_version: _Optional[str]=..., backup_crd_versions: _Optional[_Mapping[str, str]]=..., gke_version: _Optional[str]=..., anthos_version: _Optional[str]=...) -> None:
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
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    MANUAL_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    DELETE_LOCK_DAYS_FIELD_NUMBER: _ClassVar[int]
    DELETE_LOCK_EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
    RETAIN_DAYS_FIELD_NUMBER: _ClassVar[int]
    RETAIN_EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_KEY_FIELD_NUMBER: _ClassVar[int]
    ALL_NAMESPACES_FIELD_NUMBER: _ClassVar[int]
    SELECTED_NAMESPACES_FIELD_NUMBER: _ClassVar[int]
    SELECTED_APPLICATIONS_FIELD_NUMBER: _ClassVar[int]
    CONTAINS_VOLUME_DATA_FIELD_NUMBER: _ClassVar[int]
    CONTAINS_SECRETS_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_METADATA_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATE_REASON_FIELD_NUMBER: _ClassVar[int]
    COMPLETE_TIME_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_COUNT_FIELD_NUMBER: _ClassVar[int]
    VOLUME_COUNT_FIELD_NUMBER: _ClassVar[int]
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    POD_COUNT_FIELD_NUMBER: _ClassVar[int]
    CONFIG_BACKUP_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    PERMISSIVE_MODE_FIELD_NUMBER: _ClassVar[int]
    name: str
    uid: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    manual: bool
    labels: _containers.ScalarMap[str, str]
    delete_lock_days: int
    delete_lock_expire_time: _timestamp_pb2.Timestamp
    retain_days: int
    retain_expire_time: _timestamp_pb2.Timestamp
    encryption_key: _common_pb2.EncryptionKey
    all_namespaces: bool
    selected_namespaces: _common_pb2.Namespaces
    selected_applications: _common_pb2.NamespacedNames
    contains_volume_data: bool
    contains_secrets: bool
    cluster_metadata: Backup.ClusterMetadata
    state: Backup.State
    state_reason: str
    complete_time: _timestamp_pb2.Timestamp
    resource_count: int
    volume_count: int
    size_bytes: int
    etag: str
    description: str
    pod_count: int
    config_backup_size_bytes: int
    permissive_mode: bool

    def __init__(self, name: _Optional[str]=..., uid: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., manual: bool=..., labels: _Optional[_Mapping[str, str]]=..., delete_lock_days: _Optional[int]=..., delete_lock_expire_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., retain_days: _Optional[int]=..., retain_expire_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., encryption_key: _Optional[_Union[_common_pb2.EncryptionKey, _Mapping]]=..., all_namespaces: bool=..., selected_namespaces: _Optional[_Union[_common_pb2.Namespaces, _Mapping]]=..., selected_applications: _Optional[_Union[_common_pb2.NamespacedNames, _Mapping]]=..., contains_volume_data: bool=..., contains_secrets: bool=..., cluster_metadata: _Optional[_Union[Backup.ClusterMetadata, _Mapping]]=..., state: _Optional[_Union[Backup.State, str]]=..., state_reason: _Optional[str]=..., complete_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., resource_count: _Optional[int]=..., volume_count: _Optional[int]=..., size_bytes: _Optional[int]=..., etag: _Optional[str]=..., description: _Optional[str]=..., pod_count: _Optional[int]=..., config_backup_size_bytes: _Optional[int]=..., permissive_mode: bool=...) -> None:
        ...