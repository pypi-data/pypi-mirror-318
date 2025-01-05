from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.common import operation_metadata_pb2 as _operation_metadata_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class NetworkConfig(_message.Message):
    __slots__ = ('network', 'modes', 'reserved_ip_range', 'ip_addresses', 'connect_mode')

    class AddressMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ADDRESS_MODE_UNSPECIFIED: _ClassVar[NetworkConfig.AddressMode]
        MODE_IPV4: _ClassVar[NetworkConfig.AddressMode]
    ADDRESS_MODE_UNSPECIFIED: NetworkConfig.AddressMode
    MODE_IPV4: NetworkConfig.AddressMode

    class ConnectMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CONNECT_MODE_UNSPECIFIED: _ClassVar[NetworkConfig.ConnectMode]
        DIRECT_PEERING: _ClassVar[NetworkConfig.ConnectMode]
        PRIVATE_SERVICE_ACCESS: _ClassVar[NetworkConfig.ConnectMode]
    CONNECT_MODE_UNSPECIFIED: NetworkConfig.ConnectMode
    DIRECT_PEERING: NetworkConfig.ConnectMode
    PRIVATE_SERVICE_ACCESS: NetworkConfig.ConnectMode
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    MODES_FIELD_NUMBER: _ClassVar[int]
    RESERVED_IP_RANGE_FIELD_NUMBER: _ClassVar[int]
    IP_ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    CONNECT_MODE_FIELD_NUMBER: _ClassVar[int]
    network: str
    modes: _containers.RepeatedScalarFieldContainer[NetworkConfig.AddressMode]
    reserved_ip_range: str
    ip_addresses: _containers.RepeatedScalarFieldContainer[str]
    connect_mode: NetworkConfig.ConnectMode

    def __init__(self, network: _Optional[str]=..., modes: _Optional[_Iterable[_Union[NetworkConfig.AddressMode, str]]]=..., reserved_ip_range: _Optional[str]=..., ip_addresses: _Optional[_Iterable[str]]=..., connect_mode: _Optional[_Union[NetworkConfig.ConnectMode, str]]=...) -> None:
        ...

class FileShareConfig(_message.Message):
    __slots__ = ('name', 'capacity_gb', 'source_backup', 'nfs_export_options')
    NAME_FIELD_NUMBER: _ClassVar[int]
    CAPACITY_GB_FIELD_NUMBER: _ClassVar[int]
    SOURCE_BACKUP_FIELD_NUMBER: _ClassVar[int]
    NFS_EXPORT_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    name: str
    capacity_gb: int
    source_backup: str
    nfs_export_options: _containers.RepeatedCompositeFieldContainer[NfsExportOptions]

    def __init__(self, name: _Optional[str]=..., capacity_gb: _Optional[int]=..., source_backup: _Optional[str]=..., nfs_export_options: _Optional[_Iterable[_Union[NfsExportOptions, _Mapping]]]=...) -> None:
        ...

class NfsExportOptions(_message.Message):
    __slots__ = ('ip_ranges', 'access_mode', 'squash_mode', 'anon_uid', 'anon_gid', 'security_flavors')

    class AccessMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ACCESS_MODE_UNSPECIFIED: _ClassVar[NfsExportOptions.AccessMode]
        READ_ONLY: _ClassVar[NfsExportOptions.AccessMode]
        READ_WRITE: _ClassVar[NfsExportOptions.AccessMode]
    ACCESS_MODE_UNSPECIFIED: NfsExportOptions.AccessMode
    READ_ONLY: NfsExportOptions.AccessMode
    READ_WRITE: NfsExportOptions.AccessMode

    class SquashMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SQUASH_MODE_UNSPECIFIED: _ClassVar[NfsExportOptions.SquashMode]
        NO_ROOT_SQUASH: _ClassVar[NfsExportOptions.SquashMode]
        ROOT_SQUASH: _ClassVar[NfsExportOptions.SquashMode]
    SQUASH_MODE_UNSPECIFIED: NfsExportOptions.SquashMode
    NO_ROOT_SQUASH: NfsExportOptions.SquashMode
    ROOT_SQUASH: NfsExportOptions.SquashMode

    class SecurityFlavor(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SECURITY_FLAVOR_UNSPECIFIED: _ClassVar[NfsExportOptions.SecurityFlavor]
        AUTH_SYS: _ClassVar[NfsExportOptions.SecurityFlavor]
        KRB5: _ClassVar[NfsExportOptions.SecurityFlavor]
        KRB5I: _ClassVar[NfsExportOptions.SecurityFlavor]
        KRB5P: _ClassVar[NfsExportOptions.SecurityFlavor]
    SECURITY_FLAVOR_UNSPECIFIED: NfsExportOptions.SecurityFlavor
    AUTH_SYS: NfsExportOptions.SecurityFlavor
    KRB5: NfsExportOptions.SecurityFlavor
    KRB5I: NfsExportOptions.SecurityFlavor
    KRB5P: NfsExportOptions.SecurityFlavor
    IP_RANGES_FIELD_NUMBER: _ClassVar[int]
    ACCESS_MODE_FIELD_NUMBER: _ClassVar[int]
    SQUASH_MODE_FIELD_NUMBER: _ClassVar[int]
    ANON_UID_FIELD_NUMBER: _ClassVar[int]
    ANON_GID_FIELD_NUMBER: _ClassVar[int]
    SECURITY_FLAVORS_FIELD_NUMBER: _ClassVar[int]
    ip_ranges: _containers.RepeatedScalarFieldContainer[str]
    access_mode: NfsExportOptions.AccessMode
    squash_mode: NfsExportOptions.SquashMode
    anon_uid: int
    anon_gid: int
    security_flavors: _containers.RepeatedScalarFieldContainer[NfsExportOptions.SecurityFlavor]

    def __init__(self, ip_ranges: _Optional[_Iterable[str]]=..., access_mode: _Optional[_Union[NfsExportOptions.AccessMode, str]]=..., squash_mode: _Optional[_Union[NfsExportOptions.SquashMode, str]]=..., anon_uid: _Optional[int]=..., anon_gid: _Optional[int]=..., security_flavors: _Optional[_Iterable[_Union[NfsExportOptions.SecurityFlavor, str]]]=...) -> None:
        ...

class ManagedActiveDirectoryConfig(_message.Message):
    __slots__ = ('domain', 'computer')
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    COMPUTER_FIELD_NUMBER: _ClassVar[int]
    domain: str
    computer: str

    def __init__(self, domain: _Optional[str]=..., computer: _Optional[str]=...) -> None:
        ...

class DirectoryServicesConfig(_message.Message):
    __slots__ = ('managed_active_directory',)
    MANAGED_ACTIVE_DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    managed_active_directory: ManagedActiveDirectoryConfig

    def __init__(self, managed_active_directory: _Optional[_Union[ManagedActiveDirectoryConfig, _Mapping]]=...) -> None:
        ...

class Instance(_message.Message):
    __slots__ = ('name', 'description', 'state', 'status_message', 'create_time', 'tier', 'labels', 'file_shares', 'networks', 'etag', 'satisfies_pzs', 'satisfies_pzi', 'kms_key_name', 'suspension_reasons', 'max_capacity_gb', 'capacity_step_size_gb', 'max_share_count', 'capacity_gb', 'multi_share_enabled', 'protocol', 'directory_services')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Instance.State]
        CREATING: _ClassVar[Instance.State]
        READY: _ClassVar[Instance.State]
        REPAIRING: _ClassVar[Instance.State]
        DELETING: _ClassVar[Instance.State]
        ERROR: _ClassVar[Instance.State]
        RESTORING: _ClassVar[Instance.State]
        SUSPENDED: _ClassVar[Instance.State]
        REVERTING: _ClassVar[Instance.State]
        SUSPENDING: _ClassVar[Instance.State]
        RESUMING: _ClassVar[Instance.State]
    STATE_UNSPECIFIED: Instance.State
    CREATING: Instance.State
    READY: Instance.State
    REPAIRING: Instance.State
    DELETING: Instance.State
    ERROR: Instance.State
    RESTORING: Instance.State
    SUSPENDED: Instance.State
    REVERTING: Instance.State
    SUSPENDING: Instance.State
    RESUMING: Instance.State

    class Tier(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TIER_UNSPECIFIED: _ClassVar[Instance.Tier]
        STANDARD: _ClassVar[Instance.Tier]
        PREMIUM: _ClassVar[Instance.Tier]
        BASIC_HDD: _ClassVar[Instance.Tier]
        BASIC_SSD: _ClassVar[Instance.Tier]
        HIGH_SCALE_SSD: _ClassVar[Instance.Tier]
        ENTERPRISE: _ClassVar[Instance.Tier]
        ZONAL: _ClassVar[Instance.Tier]
        REGIONAL: _ClassVar[Instance.Tier]
    TIER_UNSPECIFIED: Instance.Tier
    STANDARD: Instance.Tier
    PREMIUM: Instance.Tier
    BASIC_HDD: Instance.Tier
    BASIC_SSD: Instance.Tier
    HIGH_SCALE_SSD: Instance.Tier
    ENTERPRISE: Instance.Tier
    ZONAL: Instance.Tier
    REGIONAL: Instance.Tier

    class SuspensionReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SUSPENSION_REASON_UNSPECIFIED: _ClassVar[Instance.SuspensionReason]
        KMS_KEY_ISSUE: _ClassVar[Instance.SuspensionReason]
    SUSPENSION_REASON_UNSPECIFIED: Instance.SuspensionReason
    KMS_KEY_ISSUE: Instance.SuspensionReason

    class FileProtocol(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FILE_PROTOCOL_UNSPECIFIED: _ClassVar[Instance.FileProtocol]
        NFS_V3: _ClassVar[Instance.FileProtocol]
        NFS_V4_1: _ClassVar[Instance.FileProtocol]
    FILE_PROTOCOL_UNSPECIFIED: Instance.FileProtocol
    NFS_V3: Instance.FileProtocol
    NFS_V4_1: Instance.FileProtocol

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
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATUS_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    TIER_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    FILE_SHARES_FIELD_NUMBER: _ClassVar[int]
    NETWORKS_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    SATISFIES_PZS_FIELD_NUMBER: _ClassVar[int]
    SATISFIES_PZI_FIELD_NUMBER: _ClassVar[int]
    KMS_KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    SUSPENSION_REASONS_FIELD_NUMBER: _ClassVar[int]
    MAX_CAPACITY_GB_FIELD_NUMBER: _ClassVar[int]
    CAPACITY_STEP_SIZE_GB_FIELD_NUMBER: _ClassVar[int]
    MAX_SHARE_COUNT_FIELD_NUMBER: _ClassVar[int]
    CAPACITY_GB_FIELD_NUMBER: _ClassVar[int]
    MULTI_SHARE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    DIRECTORY_SERVICES_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    state: Instance.State
    status_message: str
    create_time: _timestamp_pb2.Timestamp
    tier: Instance.Tier
    labels: _containers.ScalarMap[str, str]
    file_shares: _containers.RepeatedCompositeFieldContainer[FileShareConfig]
    networks: _containers.RepeatedCompositeFieldContainer[NetworkConfig]
    etag: str
    satisfies_pzs: _wrappers_pb2.BoolValue
    satisfies_pzi: bool
    kms_key_name: str
    suspension_reasons: _containers.RepeatedScalarFieldContainer[Instance.SuspensionReason]
    max_capacity_gb: int
    capacity_step_size_gb: int
    max_share_count: int
    capacity_gb: int
    multi_share_enabled: bool
    protocol: Instance.FileProtocol
    directory_services: DirectoryServicesConfig

    def __init__(self, name: _Optional[str]=..., description: _Optional[str]=..., state: _Optional[_Union[Instance.State, str]]=..., status_message: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., tier: _Optional[_Union[Instance.Tier, str]]=..., labels: _Optional[_Mapping[str, str]]=..., file_shares: _Optional[_Iterable[_Union[FileShareConfig, _Mapping]]]=..., networks: _Optional[_Iterable[_Union[NetworkConfig, _Mapping]]]=..., etag: _Optional[str]=..., satisfies_pzs: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]]=..., satisfies_pzi: bool=..., kms_key_name: _Optional[str]=..., suspension_reasons: _Optional[_Iterable[_Union[Instance.SuspensionReason, str]]]=..., max_capacity_gb: _Optional[int]=..., capacity_step_size_gb: _Optional[int]=..., max_share_count: _Optional[int]=..., capacity_gb: _Optional[int]=..., multi_share_enabled: bool=..., protocol: _Optional[_Union[Instance.FileProtocol, str]]=..., directory_services: _Optional[_Union[DirectoryServicesConfig, _Mapping]]=...) -> None:
        ...

class CreateInstanceRequest(_message.Message):
    __slots__ = ('parent', 'instance_id', 'instance')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    instance_id: str
    instance: Instance

    def __init__(self, parent: _Optional[str]=..., instance_id: _Optional[str]=..., instance: _Optional[_Union[Instance, _Mapping]]=...) -> None:
        ...

class GetInstanceRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateInstanceRequest(_message.Message):
    __slots__ = ('update_mask', 'instance')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    instance: Instance

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., instance: _Optional[_Union[Instance, _Mapping]]=...) -> None:
        ...

class RestoreInstanceRequest(_message.Message):
    __slots__ = ('name', 'file_share', 'source_snapshot', 'source_backup')
    NAME_FIELD_NUMBER: _ClassVar[int]
    FILE_SHARE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    SOURCE_BACKUP_FIELD_NUMBER: _ClassVar[int]
    name: str
    file_share: str
    source_snapshot: str
    source_backup: str

    def __init__(self, name: _Optional[str]=..., file_share: _Optional[str]=..., source_snapshot: _Optional[str]=..., source_backup: _Optional[str]=...) -> None:
        ...

class RevertInstanceRequest(_message.Message):
    __slots__ = ('name', 'target_snapshot_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    TARGET_SNAPSHOT_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    target_snapshot_id: str

    def __init__(self, name: _Optional[str]=..., target_snapshot_id: _Optional[str]=...) -> None:
        ...

class DeleteInstanceRequest(_message.Message):
    __slots__ = ('name', 'force')
    NAME_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    force: bool

    def __init__(self, name: _Optional[str]=..., force: bool=...) -> None:
        ...

class ListInstancesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'order_by', 'filter')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    order_by: str
    filter: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., order_by: _Optional[str]=..., filter: _Optional[str]=...) -> None:
        ...

class ListInstancesResponse(_message.Message):
    __slots__ = ('instances', 'next_page_token', 'unreachable')
    INSTANCES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    instances: _containers.RepeatedCompositeFieldContainer[Instance]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, instances: _Optional[_Iterable[_Union[Instance, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class Snapshot(_message.Message):
    __slots__ = ('name', 'description', 'state', 'create_time', 'labels', 'filesystem_used_bytes')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Snapshot.State]
        CREATING: _ClassVar[Snapshot.State]
        READY: _ClassVar[Snapshot.State]
        DELETING: _ClassVar[Snapshot.State]
    STATE_UNSPECIFIED: Snapshot.State
    CREATING: Snapshot.State
    READY: Snapshot.State
    DELETING: Snapshot.State

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
    STATE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    FILESYSTEM_USED_BYTES_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    state: Snapshot.State
    create_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    filesystem_used_bytes: int

    def __init__(self, name: _Optional[str]=..., description: _Optional[str]=..., state: _Optional[_Union[Snapshot.State, str]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., filesystem_used_bytes: _Optional[int]=...) -> None:
        ...

class CreateSnapshotRequest(_message.Message):
    __slots__ = ('parent', 'snapshot_id', 'snapshot')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_ID_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    parent: str
    snapshot_id: str
    snapshot: Snapshot

    def __init__(self, parent: _Optional[str]=..., snapshot_id: _Optional[str]=..., snapshot: _Optional[_Union[Snapshot, _Mapping]]=...) -> None:
        ...

class GetSnapshotRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class DeleteSnapshotRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateSnapshotRequest(_message.Message):
    __slots__ = ('update_mask', 'snapshot')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    snapshot: Snapshot

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., snapshot: _Optional[_Union[Snapshot, _Mapping]]=...) -> None:
        ...

class ListSnapshotsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'order_by', 'filter')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    order_by: str
    filter: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., order_by: _Optional[str]=..., filter: _Optional[str]=...) -> None:
        ...

class ListSnapshotsResponse(_message.Message):
    __slots__ = ('snapshots', 'next_page_token')
    SNAPSHOTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    snapshots: _containers.RepeatedCompositeFieldContainer[Snapshot]
    next_page_token: str

    def __init__(self, snapshots: _Optional[_Iterable[_Union[Snapshot, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class Backup(_message.Message):
    __slots__ = ('name', 'description', 'state', 'create_time', 'labels', 'capacity_gb', 'storage_bytes', 'source_instance', 'source_file_share', 'source_instance_tier', 'download_bytes', 'satisfies_pzs', 'satisfies_pzi', 'kms_key_name')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Backup.State]
        CREATING: _ClassVar[Backup.State]
        FINALIZING: _ClassVar[Backup.State]
        READY: _ClassVar[Backup.State]
        DELETING: _ClassVar[Backup.State]
        INVALID: _ClassVar[Backup.State]
    STATE_UNSPECIFIED: Backup.State
    CREATING: Backup.State
    FINALIZING: Backup.State
    READY: Backup.State
    DELETING: Backup.State
    INVALID: Backup.State

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
    STATE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    CAPACITY_GB_FIELD_NUMBER: _ClassVar[int]
    STORAGE_BYTES_FIELD_NUMBER: _ClassVar[int]
    SOURCE_INSTANCE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FILE_SHARE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_INSTANCE_TIER_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_BYTES_FIELD_NUMBER: _ClassVar[int]
    SATISFIES_PZS_FIELD_NUMBER: _ClassVar[int]
    SATISFIES_PZI_FIELD_NUMBER: _ClassVar[int]
    KMS_KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    state: Backup.State
    create_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    capacity_gb: int
    storage_bytes: int
    source_instance: str
    source_file_share: str
    source_instance_tier: Instance.Tier
    download_bytes: int
    satisfies_pzs: _wrappers_pb2.BoolValue
    satisfies_pzi: bool
    kms_key_name: str

    def __init__(self, name: _Optional[str]=..., description: _Optional[str]=..., state: _Optional[_Union[Backup.State, str]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., capacity_gb: _Optional[int]=..., storage_bytes: _Optional[int]=..., source_instance: _Optional[str]=..., source_file_share: _Optional[str]=..., source_instance_tier: _Optional[_Union[Instance.Tier, str]]=..., download_bytes: _Optional[int]=..., satisfies_pzs: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]]=..., satisfies_pzi: bool=..., kms_key_name: _Optional[str]=...) -> None:
        ...

class CreateBackupRequest(_message.Message):
    __slots__ = ('parent', 'backup', 'backup_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    BACKUP_FIELD_NUMBER: _ClassVar[int]
    BACKUP_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    backup: Backup
    backup_id: str

    def __init__(self, parent: _Optional[str]=..., backup: _Optional[_Union[Backup, _Mapping]]=..., backup_id: _Optional[str]=...) -> None:
        ...

class DeleteBackupRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateBackupRequest(_message.Message):
    __slots__ = ('backup', 'update_mask')
    BACKUP_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    backup: Backup
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, backup: _Optional[_Union[Backup, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class GetBackupRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListBackupsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'order_by', 'filter')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    order_by: str
    filter: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., order_by: _Optional[str]=..., filter: _Optional[str]=...) -> None:
        ...

class ListBackupsResponse(_message.Message):
    __slots__ = ('backups', 'next_page_token', 'unreachable')
    BACKUPS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    backups: _containers.RepeatedCompositeFieldContainer[Backup]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, backups: _Optional[_Iterable[_Union[Backup, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class Share(_message.Message):
    __slots__ = ('name', 'mount_name', 'description', 'capacity_gb', 'nfs_export_options', 'state', 'create_time', 'labels', 'backup')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Share.State]
        CREATING: _ClassVar[Share.State]
        READY: _ClassVar[Share.State]
        DELETING: _ClassVar[Share.State]
    STATE_UNSPECIFIED: Share.State
    CREATING: Share.State
    READY: Share.State
    DELETING: Share.State

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    MOUNT_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CAPACITY_GB_FIELD_NUMBER: _ClassVar[int]
    NFS_EXPORT_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    BACKUP_FIELD_NUMBER: _ClassVar[int]
    name: str
    mount_name: str
    description: str
    capacity_gb: int
    nfs_export_options: _containers.RepeatedCompositeFieldContainer[NfsExportOptions]
    state: Share.State
    create_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    backup: str

    def __init__(self, name: _Optional[str]=..., mount_name: _Optional[str]=..., description: _Optional[str]=..., capacity_gb: _Optional[int]=..., nfs_export_options: _Optional[_Iterable[_Union[NfsExportOptions, _Mapping]]]=..., state: _Optional[_Union[Share.State, str]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., backup: _Optional[str]=...) -> None:
        ...

class CreateShareRequest(_message.Message):
    __slots__ = ('parent', 'share_id', 'share')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SHARE_ID_FIELD_NUMBER: _ClassVar[int]
    SHARE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    share_id: str
    share: Share

    def __init__(self, parent: _Optional[str]=..., share_id: _Optional[str]=..., share: _Optional[_Union[Share, _Mapping]]=...) -> None:
        ...

class GetShareRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class DeleteShareRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListSharesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'order_by', 'filter')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    order_by: str
    filter: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., order_by: _Optional[str]=..., filter: _Optional[str]=...) -> None:
        ...

class ListSharesResponse(_message.Message):
    __slots__ = ('shares', 'next_page_token', 'unreachable')
    SHARES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    shares: _containers.RepeatedCompositeFieldContainer[Share]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, shares: _Optional[_Iterable[_Union[Share, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class UpdateShareRequest(_message.Message):
    __slots__ = ('share', 'update_mask')
    SHARE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    share: Share
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, share: _Optional[_Union[Share, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...