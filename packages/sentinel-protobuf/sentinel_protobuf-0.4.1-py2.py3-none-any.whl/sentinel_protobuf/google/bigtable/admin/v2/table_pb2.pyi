from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.bigtable.admin.v2 import types_pb2 as _types_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class RestoreSourceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RESTORE_SOURCE_TYPE_UNSPECIFIED: _ClassVar[RestoreSourceType]
    BACKUP: _ClassVar[RestoreSourceType]
RESTORE_SOURCE_TYPE_UNSPECIFIED: RestoreSourceType
BACKUP: RestoreSourceType

class RestoreInfo(_message.Message):
    __slots__ = ('source_type', 'backup_info')
    SOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    BACKUP_INFO_FIELD_NUMBER: _ClassVar[int]
    source_type: RestoreSourceType
    backup_info: BackupInfo

    def __init__(self, source_type: _Optional[_Union[RestoreSourceType, str]]=..., backup_info: _Optional[_Union[BackupInfo, _Mapping]]=...) -> None:
        ...

class ChangeStreamConfig(_message.Message):
    __slots__ = ('retention_period',)
    RETENTION_PERIOD_FIELD_NUMBER: _ClassVar[int]
    retention_period: _duration_pb2.Duration

    def __init__(self, retention_period: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=...) -> None:
        ...

class Table(_message.Message):
    __slots__ = ('name', 'cluster_states', 'column_families', 'granularity', 'restore_info', 'change_stream_config', 'deletion_protection', 'automated_backup_policy')

    class TimestampGranularity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TIMESTAMP_GRANULARITY_UNSPECIFIED: _ClassVar[Table.TimestampGranularity]
        MILLIS: _ClassVar[Table.TimestampGranularity]
    TIMESTAMP_GRANULARITY_UNSPECIFIED: Table.TimestampGranularity
    MILLIS: Table.TimestampGranularity

    class View(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        VIEW_UNSPECIFIED: _ClassVar[Table.View]
        NAME_ONLY: _ClassVar[Table.View]
        SCHEMA_VIEW: _ClassVar[Table.View]
        REPLICATION_VIEW: _ClassVar[Table.View]
        ENCRYPTION_VIEW: _ClassVar[Table.View]
        FULL: _ClassVar[Table.View]
    VIEW_UNSPECIFIED: Table.View
    NAME_ONLY: Table.View
    SCHEMA_VIEW: Table.View
    REPLICATION_VIEW: Table.View
    ENCRYPTION_VIEW: Table.View
    FULL: Table.View

    class ClusterState(_message.Message):
        __slots__ = ('replication_state', 'encryption_info')

        class ReplicationState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            STATE_NOT_KNOWN: _ClassVar[Table.ClusterState.ReplicationState]
            INITIALIZING: _ClassVar[Table.ClusterState.ReplicationState]
            PLANNED_MAINTENANCE: _ClassVar[Table.ClusterState.ReplicationState]
            UNPLANNED_MAINTENANCE: _ClassVar[Table.ClusterState.ReplicationState]
            READY: _ClassVar[Table.ClusterState.ReplicationState]
            READY_OPTIMIZING: _ClassVar[Table.ClusterState.ReplicationState]
        STATE_NOT_KNOWN: Table.ClusterState.ReplicationState
        INITIALIZING: Table.ClusterState.ReplicationState
        PLANNED_MAINTENANCE: Table.ClusterState.ReplicationState
        UNPLANNED_MAINTENANCE: Table.ClusterState.ReplicationState
        READY: Table.ClusterState.ReplicationState
        READY_OPTIMIZING: Table.ClusterState.ReplicationState
        REPLICATION_STATE_FIELD_NUMBER: _ClassVar[int]
        ENCRYPTION_INFO_FIELD_NUMBER: _ClassVar[int]
        replication_state: Table.ClusterState.ReplicationState
        encryption_info: _containers.RepeatedCompositeFieldContainer[EncryptionInfo]

        def __init__(self, replication_state: _Optional[_Union[Table.ClusterState.ReplicationState, str]]=..., encryption_info: _Optional[_Iterable[_Union[EncryptionInfo, _Mapping]]]=...) -> None:
            ...

    class AutomatedBackupPolicy(_message.Message):
        __slots__ = ('retention_period', 'frequency')
        RETENTION_PERIOD_FIELD_NUMBER: _ClassVar[int]
        FREQUENCY_FIELD_NUMBER: _ClassVar[int]
        retention_period: _duration_pb2.Duration
        frequency: _duration_pb2.Duration

        def __init__(self, retention_period: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., frequency: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=...) -> None:
            ...

    class ClusterStatesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Table.ClusterState

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[Table.ClusterState, _Mapping]]=...) -> None:
            ...

    class ColumnFamiliesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ColumnFamily

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[ColumnFamily, _Mapping]]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_STATES_FIELD_NUMBER: _ClassVar[int]
    COLUMN_FAMILIES_FIELD_NUMBER: _ClassVar[int]
    GRANULARITY_FIELD_NUMBER: _ClassVar[int]
    RESTORE_INFO_FIELD_NUMBER: _ClassVar[int]
    CHANGE_STREAM_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DELETION_PROTECTION_FIELD_NUMBER: _ClassVar[int]
    AUTOMATED_BACKUP_POLICY_FIELD_NUMBER: _ClassVar[int]
    name: str
    cluster_states: _containers.MessageMap[str, Table.ClusterState]
    column_families: _containers.MessageMap[str, ColumnFamily]
    granularity: Table.TimestampGranularity
    restore_info: RestoreInfo
    change_stream_config: ChangeStreamConfig
    deletion_protection: bool
    automated_backup_policy: Table.AutomatedBackupPolicy

    def __init__(self, name: _Optional[str]=..., cluster_states: _Optional[_Mapping[str, Table.ClusterState]]=..., column_families: _Optional[_Mapping[str, ColumnFamily]]=..., granularity: _Optional[_Union[Table.TimestampGranularity, str]]=..., restore_info: _Optional[_Union[RestoreInfo, _Mapping]]=..., change_stream_config: _Optional[_Union[ChangeStreamConfig, _Mapping]]=..., deletion_protection: bool=..., automated_backup_policy: _Optional[_Union[Table.AutomatedBackupPolicy, _Mapping]]=...) -> None:
        ...

class AuthorizedView(_message.Message):
    __slots__ = ('name', 'subset_view', 'etag', 'deletion_protection')

    class ResponseView(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RESPONSE_VIEW_UNSPECIFIED: _ClassVar[AuthorizedView.ResponseView]
        NAME_ONLY: _ClassVar[AuthorizedView.ResponseView]
        BASIC: _ClassVar[AuthorizedView.ResponseView]
        FULL: _ClassVar[AuthorizedView.ResponseView]
    RESPONSE_VIEW_UNSPECIFIED: AuthorizedView.ResponseView
    NAME_ONLY: AuthorizedView.ResponseView
    BASIC: AuthorizedView.ResponseView
    FULL: AuthorizedView.ResponseView

    class FamilySubsets(_message.Message):
        __slots__ = ('qualifiers', 'qualifier_prefixes')
        QUALIFIERS_FIELD_NUMBER: _ClassVar[int]
        QUALIFIER_PREFIXES_FIELD_NUMBER: _ClassVar[int]
        qualifiers: _containers.RepeatedScalarFieldContainer[bytes]
        qualifier_prefixes: _containers.RepeatedScalarFieldContainer[bytes]

        def __init__(self, qualifiers: _Optional[_Iterable[bytes]]=..., qualifier_prefixes: _Optional[_Iterable[bytes]]=...) -> None:
            ...

    class SubsetView(_message.Message):
        __slots__ = ('row_prefixes', 'family_subsets')

        class FamilySubsetsEntry(_message.Message):
            __slots__ = ('key', 'value')
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: AuthorizedView.FamilySubsets

            def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[AuthorizedView.FamilySubsets, _Mapping]]=...) -> None:
                ...
        ROW_PREFIXES_FIELD_NUMBER: _ClassVar[int]
        FAMILY_SUBSETS_FIELD_NUMBER: _ClassVar[int]
        row_prefixes: _containers.RepeatedScalarFieldContainer[bytes]
        family_subsets: _containers.MessageMap[str, AuthorizedView.FamilySubsets]

        def __init__(self, row_prefixes: _Optional[_Iterable[bytes]]=..., family_subsets: _Optional[_Mapping[str, AuthorizedView.FamilySubsets]]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    SUBSET_VIEW_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    DELETION_PROTECTION_FIELD_NUMBER: _ClassVar[int]
    name: str
    subset_view: AuthorizedView.SubsetView
    etag: str
    deletion_protection: bool

    def __init__(self, name: _Optional[str]=..., subset_view: _Optional[_Union[AuthorizedView.SubsetView, _Mapping]]=..., etag: _Optional[str]=..., deletion_protection: bool=...) -> None:
        ...

class ColumnFamily(_message.Message):
    __slots__ = ('gc_rule', 'value_type')
    GC_RULE_FIELD_NUMBER: _ClassVar[int]
    VALUE_TYPE_FIELD_NUMBER: _ClassVar[int]
    gc_rule: GcRule
    value_type: _types_pb2.Type

    def __init__(self, gc_rule: _Optional[_Union[GcRule, _Mapping]]=..., value_type: _Optional[_Union[_types_pb2.Type, _Mapping]]=...) -> None:
        ...

class GcRule(_message.Message):
    __slots__ = ('max_num_versions', 'max_age', 'intersection', 'union')

    class Intersection(_message.Message):
        __slots__ = ('rules',)
        RULES_FIELD_NUMBER: _ClassVar[int]
        rules: _containers.RepeatedCompositeFieldContainer[GcRule]

        def __init__(self, rules: _Optional[_Iterable[_Union[GcRule, _Mapping]]]=...) -> None:
            ...

    class Union(_message.Message):
        __slots__ = ('rules',)
        RULES_FIELD_NUMBER: _ClassVar[int]
        rules: _containers.RepeatedCompositeFieldContainer[GcRule]

        def __init__(self, rules: _Optional[_Iterable[_Union[GcRule, _Mapping]]]=...) -> None:
            ...
    MAX_NUM_VERSIONS_FIELD_NUMBER: _ClassVar[int]
    MAX_AGE_FIELD_NUMBER: _ClassVar[int]
    INTERSECTION_FIELD_NUMBER: _ClassVar[int]
    UNION_FIELD_NUMBER: _ClassVar[int]
    max_num_versions: int
    max_age: _duration_pb2.Duration
    intersection: GcRule.Intersection
    union: GcRule.Union

    def __init__(self, max_num_versions: _Optional[int]=..., max_age: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., intersection: _Optional[_Union[GcRule.Intersection, _Mapping]]=..., union: _Optional[_Union[GcRule.Union, _Mapping]]=...) -> None:
        ...

class EncryptionInfo(_message.Message):
    __slots__ = ('encryption_type', 'encryption_status', 'kms_key_version')

    class EncryptionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ENCRYPTION_TYPE_UNSPECIFIED: _ClassVar[EncryptionInfo.EncryptionType]
        GOOGLE_DEFAULT_ENCRYPTION: _ClassVar[EncryptionInfo.EncryptionType]
        CUSTOMER_MANAGED_ENCRYPTION: _ClassVar[EncryptionInfo.EncryptionType]
    ENCRYPTION_TYPE_UNSPECIFIED: EncryptionInfo.EncryptionType
    GOOGLE_DEFAULT_ENCRYPTION: EncryptionInfo.EncryptionType
    CUSTOMER_MANAGED_ENCRYPTION: EncryptionInfo.EncryptionType
    ENCRYPTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_STATUS_FIELD_NUMBER: _ClassVar[int]
    KMS_KEY_VERSION_FIELD_NUMBER: _ClassVar[int]
    encryption_type: EncryptionInfo.EncryptionType
    encryption_status: _status_pb2.Status
    kms_key_version: str

    def __init__(self, encryption_type: _Optional[_Union[EncryptionInfo.EncryptionType, str]]=..., encryption_status: _Optional[_Union[_status_pb2.Status, _Mapping]]=..., kms_key_version: _Optional[str]=...) -> None:
        ...

class Snapshot(_message.Message):
    __slots__ = ('name', 'source_table', 'data_size_bytes', 'create_time', 'delete_time', 'state', 'description')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_NOT_KNOWN: _ClassVar[Snapshot.State]
        READY: _ClassVar[Snapshot.State]
        CREATING: _ClassVar[Snapshot.State]
    STATE_NOT_KNOWN: Snapshot.State
    READY: Snapshot.State
    CREATING: Snapshot.State
    NAME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_TABLE_FIELD_NUMBER: _ClassVar[int]
    DATA_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DELETE_TIME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    name: str
    source_table: Table
    data_size_bytes: int
    create_time: _timestamp_pb2.Timestamp
    delete_time: _timestamp_pb2.Timestamp
    state: Snapshot.State
    description: str

    def __init__(self, name: _Optional[str]=..., source_table: _Optional[_Union[Table, _Mapping]]=..., data_size_bytes: _Optional[int]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., delete_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., state: _Optional[_Union[Snapshot.State, str]]=..., description: _Optional[str]=...) -> None:
        ...

class Backup(_message.Message):
    __slots__ = ('name', 'source_table', 'source_backup', 'expire_time', 'start_time', 'end_time', 'size_bytes', 'state', 'encryption_info', 'backup_type', 'hot_to_standard_time')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Backup.State]
        CREATING: _ClassVar[Backup.State]
        READY: _ClassVar[Backup.State]
    STATE_UNSPECIFIED: Backup.State
    CREATING: Backup.State
    READY: Backup.State

    class BackupType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        BACKUP_TYPE_UNSPECIFIED: _ClassVar[Backup.BackupType]
        STANDARD: _ClassVar[Backup.BackupType]
        HOT: _ClassVar[Backup.BackupType]
    BACKUP_TYPE_UNSPECIFIED: Backup.BackupType
    STANDARD: Backup.BackupType
    HOT: Backup.BackupType
    NAME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_TABLE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_BACKUP_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_INFO_FIELD_NUMBER: _ClassVar[int]
    BACKUP_TYPE_FIELD_NUMBER: _ClassVar[int]
    HOT_TO_STANDARD_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    source_table: str
    source_backup: str
    expire_time: _timestamp_pb2.Timestamp
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    size_bytes: int
    state: Backup.State
    encryption_info: EncryptionInfo
    backup_type: Backup.BackupType
    hot_to_standard_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., source_table: _Optional[str]=..., source_backup: _Optional[str]=..., expire_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., size_bytes: _Optional[int]=..., state: _Optional[_Union[Backup.State, str]]=..., encryption_info: _Optional[_Union[EncryptionInfo, _Mapping]]=..., backup_type: _Optional[_Union[Backup.BackupType, str]]=..., hot_to_standard_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class BackupInfo(_message.Message):
    __slots__ = ('backup', 'start_time', 'end_time', 'source_table', 'source_backup')
    BACKUP_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_TABLE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_BACKUP_FIELD_NUMBER: _ClassVar[int]
    backup: str
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    source_table: str
    source_backup: str

    def __init__(self, backup: _Optional[str]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., source_table: _Optional[str]=..., source_backup: _Optional[str]=...) -> None:
        ...