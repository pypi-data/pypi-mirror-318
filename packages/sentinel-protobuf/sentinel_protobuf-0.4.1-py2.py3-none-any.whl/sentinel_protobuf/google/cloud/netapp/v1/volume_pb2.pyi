from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import field_info_pb2 as _field_info_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.netapp.v1 import common_pb2 as _common_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Protocols(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PROTOCOLS_UNSPECIFIED: _ClassVar[Protocols]
    NFSV3: _ClassVar[Protocols]
    NFSV4: _ClassVar[Protocols]
    SMB: _ClassVar[Protocols]

class AccessType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ACCESS_TYPE_UNSPECIFIED: _ClassVar[AccessType]
    READ_ONLY: _ClassVar[AccessType]
    READ_WRITE: _ClassVar[AccessType]
    READ_NONE: _ClassVar[AccessType]

class SMBSettings(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SMB_SETTINGS_UNSPECIFIED: _ClassVar[SMBSettings]
    ENCRYPT_DATA: _ClassVar[SMBSettings]
    BROWSABLE: _ClassVar[SMBSettings]
    CHANGE_NOTIFY: _ClassVar[SMBSettings]
    NON_BROWSABLE: _ClassVar[SMBSettings]
    OPLOCKS: _ClassVar[SMBSettings]
    SHOW_SNAPSHOT: _ClassVar[SMBSettings]
    SHOW_PREVIOUS_VERSIONS: _ClassVar[SMBSettings]
    ACCESS_BASED_ENUMERATION: _ClassVar[SMBSettings]
    CONTINUOUSLY_AVAILABLE: _ClassVar[SMBSettings]

class SecurityStyle(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SECURITY_STYLE_UNSPECIFIED: _ClassVar[SecurityStyle]
    NTFS: _ClassVar[SecurityStyle]
    UNIX: _ClassVar[SecurityStyle]

class RestrictedAction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RESTRICTED_ACTION_UNSPECIFIED: _ClassVar[RestrictedAction]
    DELETE: _ClassVar[RestrictedAction]
PROTOCOLS_UNSPECIFIED: Protocols
NFSV3: Protocols
NFSV4: Protocols
SMB: Protocols
ACCESS_TYPE_UNSPECIFIED: AccessType
READ_ONLY: AccessType
READ_WRITE: AccessType
READ_NONE: AccessType
SMB_SETTINGS_UNSPECIFIED: SMBSettings
ENCRYPT_DATA: SMBSettings
BROWSABLE: SMBSettings
CHANGE_NOTIFY: SMBSettings
NON_BROWSABLE: SMBSettings
OPLOCKS: SMBSettings
SHOW_SNAPSHOT: SMBSettings
SHOW_PREVIOUS_VERSIONS: SMBSettings
ACCESS_BASED_ENUMERATION: SMBSettings
CONTINUOUSLY_AVAILABLE: SMBSettings
SECURITY_STYLE_UNSPECIFIED: SecurityStyle
NTFS: SecurityStyle
UNIX: SecurityStyle
RESTRICTED_ACTION_UNSPECIFIED: RestrictedAction
DELETE: RestrictedAction

class ListVolumesRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token", "filter", "order_by")
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
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[str] = ..., order_by: _Optional[str] = ...) -> None: ...

class ListVolumesResponse(_message.Message):
    __slots__ = ("volumes", "next_page_token", "unreachable")
    VOLUMES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    volumes: _containers.RepeatedCompositeFieldContainer[Volume]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, volumes: _Optional[_Iterable[_Union[Volume, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., unreachable: _Optional[_Iterable[str]] = ...) -> None: ...

class GetVolumeRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CreateVolumeRequest(_message.Message):
    __slots__ = ("parent", "volume_id", "volume")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    VOLUME_ID_FIELD_NUMBER: _ClassVar[int]
    VOLUME_FIELD_NUMBER: _ClassVar[int]
    parent: str
    volume_id: str
    volume: Volume
    def __init__(self, parent: _Optional[str] = ..., volume_id: _Optional[str] = ..., volume: _Optional[_Union[Volume, _Mapping]] = ...) -> None: ...

class UpdateVolumeRequest(_message.Message):
    __slots__ = ("update_mask", "volume")
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    VOLUME_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    volume: Volume
    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., volume: _Optional[_Union[Volume, _Mapping]] = ...) -> None: ...

class DeleteVolumeRequest(_message.Message):
    __slots__ = ("name", "force")
    NAME_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    force: bool
    def __init__(self, name: _Optional[str] = ..., force: bool = ...) -> None: ...

class RevertVolumeRequest(_message.Message):
    __slots__ = ("name", "snapshot_id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    snapshot_id: str
    def __init__(self, name: _Optional[str] = ..., snapshot_id: _Optional[str] = ...) -> None: ...

class Volume(_message.Message):
    __slots__ = ("name", "state", "state_details", "create_time", "share_name", "psa_range", "storage_pool", "network", "service_level", "capacity_gib", "export_policy", "protocols", "smb_settings", "mount_options", "unix_permissions", "labels", "description", "snapshot_policy", "snap_reserve", "snapshot_directory", "used_gib", "security_style", "kerberos_enabled", "ldap_enabled", "active_directory", "restore_parameters", "kms_config", "encryption_type", "has_replication", "backup_config", "restricted_actions", "large_capacity", "multiple_endpoints", "tiering_policy", "replica_zone", "zone", "cold_tier_size_gib", "hybrid_replication_parameters")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Volume.State]
        READY: _ClassVar[Volume.State]
        CREATING: _ClassVar[Volume.State]
        DELETING: _ClassVar[Volume.State]
        UPDATING: _ClassVar[Volume.State]
        RESTORING: _ClassVar[Volume.State]
        DISABLED: _ClassVar[Volume.State]
        ERROR: _ClassVar[Volume.State]
        PREPARING: _ClassVar[Volume.State]
        READ_ONLY: _ClassVar[Volume.State]
    STATE_UNSPECIFIED: Volume.State
    READY: Volume.State
    CREATING: Volume.State
    DELETING: Volume.State
    UPDATING: Volume.State
    RESTORING: Volume.State
    DISABLED: Volume.State
    ERROR: Volume.State
    PREPARING: Volume.State
    READ_ONLY: Volume.State
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATE_DETAILS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    SHARE_NAME_FIELD_NUMBER: _ClassVar[int]
    PSA_RANGE_FIELD_NUMBER: _ClassVar[int]
    STORAGE_POOL_FIELD_NUMBER: _ClassVar[int]
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    SERVICE_LEVEL_FIELD_NUMBER: _ClassVar[int]
    CAPACITY_GIB_FIELD_NUMBER: _ClassVar[int]
    EXPORT_POLICY_FIELD_NUMBER: _ClassVar[int]
    PROTOCOLS_FIELD_NUMBER: _ClassVar[int]
    SMB_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    MOUNT_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    UNIX_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_POLICY_FIELD_NUMBER: _ClassVar[int]
    SNAP_RESERVE_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    USED_GIB_FIELD_NUMBER: _ClassVar[int]
    SECURITY_STYLE_FIELD_NUMBER: _ClassVar[int]
    KERBEROS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    LDAP_ENABLED_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    RESTORE_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    KMS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    HAS_REPLICATION_FIELD_NUMBER: _ClassVar[int]
    BACKUP_CONFIG_FIELD_NUMBER: _ClassVar[int]
    RESTRICTED_ACTIONS_FIELD_NUMBER: _ClassVar[int]
    LARGE_CAPACITY_FIELD_NUMBER: _ClassVar[int]
    MULTIPLE_ENDPOINTS_FIELD_NUMBER: _ClassVar[int]
    TIERING_POLICY_FIELD_NUMBER: _ClassVar[int]
    REPLICA_ZONE_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    COLD_TIER_SIZE_GIB_FIELD_NUMBER: _ClassVar[int]
    HYBRID_REPLICATION_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    name: str
    state: Volume.State
    state_details: str
    create_time: _timestamp_pb2.Timestamp
    share_name: str
    psa_range: str
    storage_pool: str
    network: str
    service_level: _common_pb2.ServiceLevel
    capacity_gib: int
    export_policy: ExportPolicy
    protocols: _containers.RepeatedScalarFieldContainer[Protocols]
    smb_settings: _containers.RepeatedScalarFieldContainer[SMBSettings]
    mount_options: _containers.RepeatedCompositeFieldContainer[MountOption]
    unix_permissions: str
    labels: _containers.ScalarMap[str, str]
    description: str
    snapshot_policy: SnapshotPolicy
    snap_reserve: float
    snapshot_directory: bool
    used_gib: int
    security_style: SecurityStyle
    kerberos_enabled: bool
    ldap_enabled: bool
    active_directory: str
    restore_parameters: RestoreParameters
    kms_config: str
    encryption_type: _common_pb2.EncryptionType
    has_replication: bool
    backup_config: BackupConfig
    restricted_actions: _containers.RepeatedScalarFieldContainer[RestrictedAction]
    large_capacity: bool
    multiple_endpoints: bool
    tiering_policy: TieringPolicy
    replica_zone: str
    zone: str
    cold_tier_size_gib: int
    hybrid_replication_parameters: HybridReplicationParameters
    def __init__(self, name: _Optional[str] = ..., state: _Optional[_Union[Volume.State, str]] = ..., state_details: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., share_name: _Optional[str] = ..., psa_range: _Optional[str] = ..., storage_pool: _Optional[str] = ..., network: _Optional[str] = ..., service_level: _Optional[_Union[_common_pb2.ServiceLevel, str]] = ..., capacity_gib: _Optional[int] = ..., export_policy: _Optional[_Union[ExportPolicy, _Mapping]] = ..., protocols: _Optional[_Iterable[_Union[Protocols, str]]] = ..., smb_settings: _Optional[_Iterable[_Union[SMBSettings, str]]] = ..., mount_options: _Optional[_Iterable[_Union[MountOption, _Mapping]]] = ..., unix_permissions: _Optional[str] = ..., labels: _Optional[_Mapping[str, str]] = ..., description: _Optional[str] = ..., snapshot_policy: _Optional[_Union[SnapshotPolicy, _Mapping]] = ..., snap_reserve: _Optional[float] = ..., snapshot_directory: bool = ..., used_gib: _Optional[int] = ..., security_style: _Optional[_Union[SecurityStyle, str]] = ..., kerberos_enabled: bool = ..., ldap_enabled: bool = ..., active_directory: _Optional[str] = ..., restore_parameters: _Optional[_Union[RestoreParameters, _Mapping]] = ..., kms_config: _Optional[str] = ..., encryption_type: _Optional[_Union[_common_pb2.EncryptionType, str]] = ..., has_replication: bool = ..., backup_config: _Optional[_Union[BackupConfig, _Mapping]] = ..., restricted_actions: _Optional[_Iterable[_Union[RestrictedAction, str]]] = ..., large_capacity: bool = ..., multiple_endpoints: bool = ..., tiering_policy: _Optional[_Union[TieringPolicy, _Mapping]] = ..., replica_zone: _Optional[str] = ..., zone: _Optional[str] = ..., cold_tier_size_gib: _Optional[int] = ..., hybrid_replication_parameters: _Optional[_Union[HybridReplicationParameters, _Mapping]] = ...) -> None: ...

class ExportPolicy(_message.Message):
    __slots__ = ("rules",)
    RULES_FIELD_NUMBER: _ClassVar[int]
    rules: _containers.RepeatedCompositeFieldContainer[SimpleExportPolicyRule]
    def __init__(self, rules: _Optional[_Iterable[_Union[SimpleExportPolicyRule, _Mapping]]] = ...) -> None: ...

class SimpleExportPolicyRule(_message.Message):
    __slots__ = ("allowed_clients", "has_root_access", "access_type", "nfsv3", "nfsv4", "kerberos_5_read_only", "kerberos_5_read_write", "kerberos_5i_read_only", "kerberos_5i_read_write", "kerberos_5p_read_only", "kerberos_5p_read_write")
    ALLOWED_CLIENTS_FIELD_NUMBER: _ClassVar[int]
    HAS_ROOT_ACCESS_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TYPE_FIELD_NUMBER: _ClassVar[int]
    NFSV3_FIELD_NUMBER: _ClassVar[int]
    NFSV4_FIELD_NUMBER: _ClassVar[int]
    KERBEROS_5_READ_ONLY_FIELD_NUMBER: _ClassVar[int]
    KERBEROS_5_READ_WRITE_FIELD_NUMBER: _ClassVar[int]
    KERBEROS_5I_READ_ONLY_FIELD_NUMBER: _ClassVar[int]
    KERBEROS_5I_READ_WRITE_FIELD_NUMBER: _ClassVar[int]
    KERBEROS_5P_READ_ONLY_FIELD_NUMBER: _ClassVar[int]
    KERBEROS_5P_READ_WRITE_FIELD_NUMBER: _ClassVar[int]
    allowed_clients: str
    has_root_access: str
    access_type: AccessType
    nfsv3: bool
    nfsv4: bool
    kerberos_5_read_only: bool
    kerberos_5_read_write: bool
    kerberos_5i_read_only: bool
    kerberos_5i_read_write: bool
    kerberos_5p_read_only: bool
    kerberos_5p_read_write: bool
    def __init__(self, allowed_clients: _Optional[str] = ..., has_root_access: _Optional[str] = ..., access_type: _Optional[_Union[AccessType, str]] = ..., nfsv3: bool = ..., nfsv4: bool = ..., kerberos_5_read_only: bool = ..., kerberos_5_read_write: bool = ..., kerberos_5i_read_only: bool = ..., kerberos_5i_read_write: bool = ..., kerberos_5p_read_only: bool = ..., kerberos_5p_read_write: bool = ...) -> None: ...

class SnapshotPolicy(_message.Message):
    __slots__ = ("enabled", "hourly_schedule", "daily_schedule", "weekly_schedule", "monthly_schedule")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    HOURLY_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    DAILY_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    WEEKLY_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    MONTHLY_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    hourly_schedule: HourlySchedule
    daily_schedule: DailySchedule
    weekly_schedule: WeeklySchedule
    monthly_schedule: MonthlySchedule
    def __init__(self, enabled: bool = ..., hourly_schedule: _Optional[_Union[HourlySchedule, _Mapping]] = ..., daily_schedule: _Optional[_Union[DailySchedule, _Mapping]] = ..., weekly_schedule: _Optional[_Union[WeeklySchedule, _Mapping]] = ..., monthly_schedule: _Optional[_Union[MonthlySchedule, _Mapping]] = ...) -> None: ...

class HourlySchedule(_message.Message):
    __slots__ = ("snapshots_to_keep", "minute")
    SNAPSHOTS_TO_KEEP_FIELD_NUMBER: _ClassVar[int]
    MINUTE_FIELD_NUMBER: _ClassVar[int]
    snapshots_to_keep: float
    minute: float
    def __init__(self, snapshots_to_keep: _Optional[float] = ..., minute: _Optional[float] = ...) -> None: ...

class DailySchedule(_message.Message):
    __slots__ = ("snapshots_to_keep", "minute", "hour")
    SNAPSHOTS_TO_KEEP_FIELD_NUMBER: _ClassVar[int]
    MINUTE_FIELD_NUMBER: _ClassVar[int]
    HOUR_FIELD_NUMBER: _ClassVar[int]
    snapshots_to_keep: float
    minute: float
    hour: float
    def __init__(self, snapshots_to_keep: _Optional[float] = ..., minute: _Optional[float] = ..., hour: _Optional[float] = ...) -> None: ...

class WeeklySchedule(_message.Message):
    __slots__ = ("snapshots_to_keep", "minute", "hour", "day")
    SNAPSHOTS_TO_KEEP_FIELD_NUMBER: _ClassVar[int]
    MINUTE_FIELD_NUMBER: _ClassVar[int]
    HOUR_FIELD_NUMBER: _ClassVar[int]
    DAY_FIELD_NUMBER: _ClassVar[int]
    snapshots_to_keep: float
    minute: float
    hour: float
    day: str
    def __init__(self, snapshots_to_keep: _Optional[float] = ..., minute: _Optional[float] = ..., hour: _Optional[float] = ..., day: _Optional[str] = ...) -> None: ...

class MonthlySchedule(_message.Message):
    __slots__ = ("snapshots_to_keep", "minute", "hour", "days_of_month")
    SNAPSHOTS_TO_KEEP_FIELD_NUMBER: _ClassVar[int]
    MINUTE_FIELD_NUMBER: _ClassVar[int]
    HOUR_FIELD_NUMBER: _ClassVar[int]
    DAYS_OF_MONTH_FIELD_NUMBER: _ClassVar[int]
    snapshots_to_keep: float
    minute: float
    hour: float
    days_of_month: str
    def __init__(self, snapshots_to_keep: _Optional[float] = ..., minute: _Optional[float] = ..., hour: _Optional[float] = ..., days_of_month: _Optional[str] = ...) -> None: ...

class MountOption(_message.Message):
    __slots__ = ("export", "export_full", "protocol", "instructions")
    EXPORT_FIELD_NUMBER: _ClassVar[int]
    EXPORT_FULL_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    INSTRUCTIONS_FIELD_NUMBER: _ClassVar[int]
    export: str
    export_full: str
    protocol: Protocols
    instructions: str
    def __init__(self, export: _Optional[str] = ..., export_full: _Optional[str] = ..., protocol: _Optional[_Union[Protocols, str]] = ..., instructions: _Optional[str] = ...) -> None: ...

class RestoreParameters(_message.Message):
    __slots__ = ("source_snapshot", "source_backup")
    SOURCE_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    SOURCE_BACKUP_FIELD_NUMBER: _ClassVar[int]
    source_snapshot: str
    source_backup: str
    def __init__(self, source_snapshot: _Optional[str] = ..., source_backup: _Optional[str] = ...) -> None: ...

class BackupConfig(_message.Message):
    __slots__ = ("backup_policies", "backup_vault", "scheduled_backup_enabled", "backup_chain_bytes")
    BACKUP_POLICIES_FIELD_NUMBER: _ClassVar[int]
    BACKUP_VAULT_FIELD_NUMBER: _ClassVar[int]
    SCHEDULED_BACKUP_ENABLED_FIELD_NUMBER: _ClassVar[int]
    BACKUP_CHAIN_BYTES_FIELD_NUMBER: _ClassVar[int]
    backup_policies: _containers.RepeatedScalarFieldContainer[str]
    backup_vault: str
    scheduled_backup_enabled: bool
    backup_chain_bytes: int
    def __init__(self, backup_policies: _Optional[_Iterable[str]] = ..., backup_vault: _Optional[str] = ..., scheduled_backup_enabled: bool = ..., backup_chain_bytes: _Optional[int] = ...) -> None: ...

class TieringPolicy(_message.Message):
    __slots__ = ("tier_action", "cooling_threshold_days")
    class TierAction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TIER_ACTION_UNSPECIFIED: _ClassVar[TieringPolicy.TierAction]
        ENABLED: _ClassVar[TieringPolicy.TierAction]
        PAUSED: _ClassVar[TieringPolicy.TierAction]
    TIER_ACTION_UNSPECIFIED: TieringPolicy.TierAction
    ENABLED: TieringPolicy.TierAction
    PAUSED: TieringPolicy.TierAction
    TIER_ACTION_FIELD_NUMBER: _ClassVar[int]
    COOLING_THRESHOLD_DAYS_FIELD_NUMBER: _ClassVar[int]
    tier_action: TieringPolicy.TierAction
    cooling_threshold_days: int
    def __init__(self, tier_action: _Optional[_Union[TieringPolicy.TierAction, str]] = ..., cooling_threshold_days: _Optional[int] = ...) -> None: ...

class HybridReplicationParameters(_message.Message):
    __slots__ = ("replication", "peer_volume_name", "peer_cluster_name", "peer_svm_name", "peer_ip_addresses", "cluster_location", "description", "labels")
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    REPLICATION_FIELD_NUMBER: _ClassVar[int]
    PEER_VOLUME_NAME_FIELD_NUMBER: _ClassVar[int]
    PEER_CLUSTER_NAME_FIELD_NUMBER: _ClassVar[int]
    PEER_SVM_NAME_FIELD_NUMBER: _ClassVar[int]
    PEER_IP_ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_LOCATION_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    replication: str
    peer_volume_name: str
    peer_cluster_name: str
    peer_svm_name: str
    peer_ip_addresses: _containers.RepeatedScalarFieldContainer[str]
    cluster_location: str
    description: str
    labels: _containers.ScalarMap[str, str]
    def __init__(self, replication: _Optional[str] = ..., peer_volume_name: _Optional[str] = ..., peer_cluster_name: _Optional[str] = ..., peer_svm_name: _Optional[str] = ..., peer_ip_addresses: _Optional[_Iterable[str]] = ..., cluster_location: _Optional[str] = ..., description: _Optional[str] = ..., labels: _Optional[_Mapping[str, str]] = ...) -> None: ...
