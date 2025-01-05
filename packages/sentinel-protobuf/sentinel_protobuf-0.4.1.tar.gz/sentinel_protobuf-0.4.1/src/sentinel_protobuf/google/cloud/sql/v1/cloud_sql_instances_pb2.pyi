from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.cloud.sql.v1 import cloud_sql_resources_pb2 as _cloud_sql_resources_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ExternalSyncParallelLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EXTERNAL_SYNC_PARALLEL_LEVEL_UNSPECIFIED: _ClassVar[ExternalSyncParallelLevel]
    MIN: _ClassVar[ExternalSyncParallelLevel]
    OPTIMAL: _ClassVar[ExternalSyncParallelLevel]
    MAX: _ClassVar[ExternalSyncParallelLevel]

class SqlInstanceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SQL_INSTANCE_TYPE_UNSPECIFIED: _ClassVar[SqlInstanceType]
    CLOUD_SQL_INSTANCE: _ClassVar[SqlInstanceType]
    ON_PREMISES_INSTANCE: _ClassVar[SqlInstanceType]
    READ_REPLICA_INSTANCE: _ClassVar[SqlInstanceType]

class SqlSuspensionReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SQL_SUSPENSION_REASON_UNSPECIFIED: _ClassVar[SqlSuspensionReason]
    BILLING_ISSUE: _ClassVar[SqlSuspensionReason]
    LEGAL_ISSUE: _ClassVar[SqlSuspensionReason]
    OPERATIONAL_ISSUE: _ClassVar[SqlSuspensionReason]
    KMS_KEY_ISSUE: _ClassVar[SqlSuspensionReason]
EXTERNAL_SYNC_PARALLEL_LEVEL_UNSPECIFIED: ExternalSyncParallelLevel
MIN: ExternalSyncParallelLevel
OPTIMAL: ExternalSyncParallelLevel
MAX: ExternalSyncParallelLevel
SQL_INSTANCE_TYPE_UNSPECIFIED: SqlInstanceType
CLOUD_SQL_INSTANCE: SqlInstanceType
ON_PREMISES_INSTANCE: SqlInstanceType
READ_REPLICA_INSTANCE: SqlInstanceType
SQL_SUSPENSION_REASON_UNSPECIFIED: SqlSuspensionReason
BILLING_ISSUE: SqlSuspensionReason
LEGAL_ISSUE: SqlSuspensionReason
OPERATIONAL_ISSUE: SqlSuspensionReason
KMS_KEY_ISSUE: SqlSuspensionReason

class SqlInstancesAddServerCaRequest(_message.Message):
    __slots__ = ("instance", "project")
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    instance: str
    project: str
    def __init__(self, instance: _Optional[str] = ..., project: _Optional[str] = ...) -> None: ...

class SqlInstancesCloneRequest(_message.Message):
    __slots__ = ("instance", "project", "body")
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    instance: str
    project: str
    body: InstancesCloneRequest
    def __init__(self, instance: _Optional[str] = ..., project: _Optional[str] = ..., body: _Optional[_Union[InstancesCloneRequest, _Mapping]] = ...) -> None: ...

class SqlInstancesDeleteRequest(_message.Message):
    __slots__ = ("instance", "project")
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    instance: str
    project: str
    def __init__(self, instance: _Optional[str] = ..., project: _Optional[str] = ...) -> None: ...

class SqlInstancesDemoteMasterRequest(_message.Message):
    __slots__ = ("instance", "project", "body")
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    instance: str
    project: str
    body: InstancesDemoteMasterRequest
    def __init__(self, instance: _Optional[str] = ..., project: _Optional[str] = ..., body: _Optional[_Union[InstancesDemoteMasterRequest, _Mapping]] = ...) -> None: ...

class SqlInstancesDemoteRequest(_message.Message):
    __slots__ = ("instance", "project", "body")
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    instance: str
    project: str
    body: InstancesDemoteRequest
    def __init__(self, instance: _Optional[str] = ..., project: _Optional[str] = ..., body: _Optional[_Union[InstancesDemoteRequest, _Mapping]] = ...) -> None: ...

class SqlInstancesExportRequest(_message.Message):
    __slots__ = ("instance", "project", "body")
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    instance: str
    project: str
    body: InstancesExportRequest
    def __init__(self, instance: _Optional[str] = ..., project: _Optional[str] = ..., body: _Optional[_Union[InstancesExportRequest, _Mapping]] = ...) -> None: ...

class SqlInstancesFailoverRequest(_message.Message):
    __slots__ = ("instance", "project", "body")
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    instance: str
    project: str
    body: InstancesFailoverRequest
    def __init__(self, instance: _Optional[str] = ..., project: _Optional[str] = ..., body: _Optional[_Union[InstancesFailoverRequest, _Mapping]] = ...) -> None: ...

class SqlInstancesGetRequest(_message.Message):
    __slots__ = ("instance", "project")
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    instance: str
    project: str
    def __init__(self, instance: _Optional[str] = ..., project: _Optional[str] = ...) -> None: ...

class SqlInstancesImportRequest(_message.Message):
    __slots__ = ("instance", "project", "body")
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    instance: str
    project: str
    body: InstancesImportRequest
    def __init__(self, instance: _Optional[str] = ..., project: _Optional[str] = ..., body: _Optional[_Union[InstancesImportRequest, _Mapping]] = ...) -> None: ...

class SqlInstancesInsertRequest(_message.Message):
    __slots__ = ("project", "body")
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    project: str
    body: DatabaseInstance
    def __init__(self, project: _Optional[str] = ..., body: _Optional[_Union[DatabaseInstance, _Mapping]] = ...) -> None: ...

class SqlInstancesListRequest(_message.Message):
    __slots__ = ("filter", "max_results", "page_token", "project")
    FILTER_FIELD_NUMBER: _ClassVar[int]
    MAX_RESULTS_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    filter: str
    max_results: int
    page_token: str
    project: str
    def __init__(self, filter: _Optional[str] = ..., max_results: _Optional[int] = ..., page_token: _Optional[str] = ..., project: _Optional[str] = ...) -> None: ...

class SqlInstancesListServerCasRequest(_message.Message):
    __slots__ = ("instance", "project")
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    instance: str
    project: str
    def __init__(self, instance: _Optional[str] = ..., project: _Optional[str] = ...) -> None: ...

class SqlInstancesPatchRequest(_message.Message):
    __slots__ = ("instance", "project", "body")
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    instance: str
    project: str
    body: DatabaseInstance
    def __init__(self, instance: _Optional[str] = ..., project: _Optional[str] = ..., body: _Optional[_Union[DatabaseInstance, _Mapping]] = ...) -> None: ...

class SqlInstancesPromoteReplicaRequest(_message.Message):
    __slots__ = ("instance", "project", "failover")
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    FAILOVER_FIELD_NUMBER: _ClassVar[int]
    instance: str
    project: str
    failover: bool
    def __init__(self, instance: _Optional[str] = ..., project: _Optional[str] = ..., failover: bool = ...) -> None: ...

class SqlInstancesSwitchoverRequest(_message.Message):
    __slots__ = ("instance", "project", "db_timeout")
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    DB_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    instance: str
    project: str
    db_timeout: _duration_pb2.Duration
    def __init__(self, instance: _Optional[str] = ..., project: _Optional[str] = ..., db_timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...

class SqlInstancesResetSslConfigRequest(_message.Message):
    __slots__ = ("instance", "project")
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    instance: str
    project: str
    def __init__(self, instance: _Optional[str] = ..., project: _Optional[str] = ...) -> None: ...

class SqlInstancesRestartRequest(_message.Message):
    __slots__ = ("instance", "project")
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    instance: str
    project: str
    def __init__(self, instance: _Optional[str] = ..., project: _Optional[str] = ...) -> None: ...

class SqlInstancesRestoreBackupRequest(_message.Message):
    __slots__ = ("instance", "project", "body")
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    instance: str
    project: str
    body: InstancesRestoreBackupRequest
    def __init__(self, instance: _Optional[str] = ..., project: _Optional[str] = ..., body: _Optional[_Union[InstancesRestoreBackupRequest, _Mapping]] = ...) -> None: ...

class SqlInstancesRotateServerCaRequest(_message.Message):
    __slots__ = ("instance", "project", "body")
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    instance: str
    project: str
    body: InstancesRotateServerCaRequest
    def __init__(self, instance: _Optional[str] = ..., project: _Optional[str] = ..., body: _Optional[_Union[InstancesRotateServerCaRequest, _Mapping]] = ...) -> None: ...

class SqlInstancesStartReplicaRequest(_message.Message):
    __slots__ = ("instance", "project")
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    instance: str
    project: str
    def __init__(self, instance: _Optional[str] = ..., project: _Optional[str] = ...) -> None: ...

class SqlInstancesStopReplicaRequest(_message.Message):
    __slots__ = ("instance", "project")
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    instance: str
    project: str
    def __init__(self, instance: _Optional[str] = ..., project: _Optional[str] = ...) -> None: ...

class SqlInstancesTruncateLogRequest(_message.Message):
    __slots__ = ("instance", "project", "body")
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    instance: str
    project: str
    body: InstancesTruncateLogRequest
    def __init__(self, instance: _Optional[str] = ..., project: _Optional[str] = ..., body: _Optional[_Union[InstancesTruncateLogRequest, _Mapping]] = ...) -> None: ...

class SqlInstancesPerformDiskShrinkRequest(_message.Message):
    __slots__ = ("instance", "project", "body")
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    instance: str
    project: str
    body: _cloud_sql_resources_pb2.PerformDiskShrinkContext
    def __init__(self, instance: _Optional[str] = ..., project: _Optional[str] = ..., body: _Optional[_Union[_cloud_sql_resources_pb2.PerformDiskShrinkContext, _Mapping]] = ...) -> None: ...

class SqlInstancesUpdateRequest(_message.Message):
    __slots__ = ("instance", "project", "body")
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    instance: str
    project: str
    body: DatabaseInstance
    def __init__(self, instance: _Optional[str] = ..., project: _Optional[str] = ..., body: _Optional[_Union[DatabaseInstance, _Mapping]] = ...) -> None: ...

class SqlInstancesRescheduleMaintenanceRequest(_message.Message):
    __slots__ = ("instance", "project", "body")
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    instance: str
    project: str
    body: SqlInstancesRescheduleMaintenanceRequestBody
    def __init__(self, instance: _Optional[str] = ..., project: _Optional[str] = ..., body: _Optional[_Union[SqlInstancesRescheduleMaintenanceRequestBody, _Mapping]] = ...) -> None: ...

class SqlInstancesReencryptRequest(_message.Message):
    __slots__ = ("instance", "project", "body")
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    instance: str
    project: str
    body: InstancesReencryptRequest
    def __init__(self, instance: _Optional[str] = ..., project: _Optional[str] = ..., body: _Optional[_Union[InstancesReencryptRequest, _Mapping]] = ...) -> None: ...

class InstancesReencryptRequest(_message.Message):
    __slots__ = ("backup_reencryption_config",)
    BACKUP_REENCRYPTION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    backup_reencryption_config: BackupReencryptionConfig
    def __init__(self, backup_reencryption_config: _Optional[_Union[BackupReencryptionConfig, _Mapping]] = ...) -> None: ...

class BackupReencryptionConfig(_message.Message):
    __slots__ = ("backup_limit", "backup_type")
    class BackupType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        BACKUP_TYPE_UNSPECIFIED: _ClassVar[BackupReencryptionConfig.BackupType]
        AUTOMATED: _ClassVar[BackupReencryptionConfig.BackupType]
        ON_DEMAND: _ClassVar[BackupReencryptionConfig.BackupType]
    BACKUP_TYPE_UNSPECIFIED: BackupReencryptionConfig.BackupType
    AUTOMATED: BackupReencryptionConfig.BackupType
    ON_DEMAND: BackupReencryptionConfig.BackupType
    BACKUP_LIMIT_FIELD_NUMBER: _ClassVar[int]
    BACKUP_TYPE_FIELD_NUMBER: _ClassVar[int]
    backup_limit: int
    backup_type: BackupReencryptionConfig.BackupType
    def __init__(self, backup_limit: _Optional[int] = ..., backup_type: _Optional[_Union[BackupReencryptionConfig.BackupType, str]] = ...) -> None: ...

class SqlInstancesGetDiskShrinkConfigRequest(_message.Message):
    __slots__ = ("instance", "project")
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    instance: str
    project: str
    def __init__(self, instance: _Optional[str] = ..., project: _Optional[str] = ...) -> None: ...

class SqlInstancesVerifyExternalSyncSettingsRequest(_message.Message):
    __slots__ = ("instance", "project", "verify_connection_only", "sync_mode", "verify_replication_only", "mysql_sync_config", "migration_type", "sync_parallel_level")
    class ExternalSyncMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        EXTERNAL_SYNC_MODE_UNSPECIFIED: _ClassVar[SqlInstancesVerifyExternalSyncSettingsRequest.ExternalSyncMode]
        ONLINE: _ClassVar[SqlInstancesVerifyExternalSyncSettingsRequest.ExternalSyncMode]
        OFFLINE: _ClassVar[SqlInstancesVerifyExternalSyncSettingsRequest.ExternalSyncMode]
    EXTERNAL_SYNC_MODE_UNSPECIFIED: SqlInstancesVerifyExternalSyncSettingsRequest.ExternalSyncMode
    ONLINE: SqlInstancesVerifyExternalSyncSettingsRequest.ExternalSyncMode
    OFFLINE: SqlInstancesVerifyExternalSyncSettingsRequest.ExternalSyncMode
    class MigrationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MIGRATION_TYPE_UNSPECIFIED: _ClassVar[SqlInstancesVerifyExternalSyncSettingsRequest.MigrationType]
        LOGICAL: _ClassVar[SqlInstancesVerifyExternalSyncSettingsRequest.MigrationType]
        PHYSICAL: _ClassVar[SqlInstancesVerifyExternalSyncSettingsRequest.MigrationType]
    MIGRATION_TYPE_UNSPECIFIED: SqlInstancesVerifyExternalSyncSettingsRequest.MigrationType
    LOGICAL: SqlInstancesVerifyExternalSyncSettingsRequest.MigrationType
    PHYSICAL: SqlInstancesVerifyExternalSyncSettingsRequest.MigrationType
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    VERIFY_CONNECTION_ONLY_FIELD_NUMBER: _ClassVar[int]
    SYNC_MODE_FIELD_NUMBER: _ClassVar[int]
    VERIFY_REPLICATION_ONLY_FIELD_NUMBER: _ClassVar[int]
    MYSQL_SYNC_CONFIG_FIELD_NUMBER: _ClassVar[int]
    MIGRATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    SYNC_PARALLEL_LEVEL_FIELD_NUMBER: _ClassVar[int]
    instance: str
    project: str
    verify_connection_only: bool
    sync_mode: SqlInstancesVerifyExternalSyncSettingsRequest.ExternalSyncMode
    verify_replication_only: bool
    mysql_sync_config: _cloud_sql_resources_pb2.MySqlSyncConfig
    migration_type: SqlInstancesVerifyExternalSyncSettingsRequest.MigrationType
    sync_parallel_level: ExternalSyncParallelLevel
    def __init__(self, instance: _Optional[str] = ..., project: _Optional[str] = ..., verify_connection_only: bool = ..., sync_mode: _Optional[_Union[SqlInstancesVerifyExternalSyncSettingsRequest.ExternalSyncMode, str]] = ..., verify_replication_only: bool = ..., mysql_sync_config: _Optional[_Union[_cloud_sql_resources_pb2.MySqlSyncConfig, _Mapping]] = ..., migration_type: _Optional[_Union[SqlInstancesVerifyExternalSyncSettingsRequest.MigrationType, str]] = ..., sync_parallel_level: _Optional[_Union[ExternalSyncParallelLevel, str]] = ...) -> None: ...

class SqlInstancesStartExternalSyncRequest(_message.Message):
    __slots__ = ("instance", "project", "sync_mode", "skip_verification", "mysql_sync_config", "sync_parallel_level", "migration_type")
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    SYNC_MODE_FIELD_NUMBER: _ClassVar[int]
    SKIP_VERIFICATION_FIELD_NUMBER: _ClassVar[int]
    MYSQL_SYNC_CONFIG_FIELD_NUMBER: _ClassVar[int]
    SYNC_PARALLEL_LEVEL_FIELD_NUMBER: _ClassVar[int]
    MIGRATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    instance: str
    project: str
    sync_mode: SqlInstancesVerifyExternalSyncSettingsRequest.ExternalSyncMode
    skip_verification: bool
    mysql_sync_config: _cloud_sql_resources_pb2.MySqlSyncConfig
    sync_parallel_level: ExternalSyncParallelLevel
    migration_type: SqlInstancesVerifyExternalSyncSettingsRequest.MigrationType
    def __init__(self, instance: _Optional[str] = ..., project: _Optional[str] = ..., sync_mode: _Optional[_Union[SqlInstancesVerifyExternalSyncSettingsRequest.ExternalSyncMode, str]] = ..., skip_verification: bool = ..., mysql_sync_config: _Optional[_Union[_cloud_sql_resources_pb2.MySqlSyncConfig, _Mapping]] = ..., sync_parallel_level: _Optional[_Union[ExternalSyncParallelLevel, str]] = ..., migration_type: _Optional[_Union[SqlInstancesVerifyExternalSyncSettingsRequest.MigrationType, str]] = ...) -> None: ...

class SqlInstancesResetReplicaSizeRequest(_message.Message):
    __slots__ = ("instance", "project")
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    instance: str
    project: str
    def __init__(self, instance: _Optional[str] = ..., project: _Optional[str] = ...) -> None: ...

class SqlInstancesCreateEphemeralCertRequest(_message.Message):
    __slots__ = ("instance", "project", "body")
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    instance: str
    project: str
    body: SslCertsCreateEphemeralRequest
    def __init__(self, instance: _Optional[str] = ..., project: _Optional[str] = ..., body: _Optional[_Union[SslCertsCreateEphemeralRequest, _Mapping]] = ...) -> None: ...

class InstancesCloneRequest(_message.Message):
    __slots__ = ("clone_context",)
    CLONE_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    clone_context: CloneContext
    def __init__(self, clone_context: _Optional[_Union[CloneContext, _Mapping]] = ...) -> None: ...

class InstancesDemoteMasterRequest(_message.Message):
    __slots__ = ("demote_master_context",)
    DEMOTE_MASTER_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    demote_master_context: DemoteMasterContext
    def __init__(self, demote_master_context: _Optional[_Union[DemoteMasterContext, _Mapping]] = ...) -> None: ...

class InstancesDemoteRequest(_message.Message):
    __slots__ = ("demote_context",)
    DEMOTE_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    demote_context: DemoteContext
    def __init__(self, demote_context: _Optional[_Union[DemoteContext, _Mapping]] = ...) -> None: ...

class InstancesExportRequest(_message.Message):
    __slots__ = ("export_context",)
    EXPORT_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    export_context: _cloud_sql_resources_pb2.ExportContext
    def __init__(self, export_context: _Optional[_Union[_cloud_sql_resources_pb2.ExportContext, _Mapping]] = ...) -> None: ...

class InstancesFailoverRequest(_message.Message):
    __slots__ = ("failover_context",)
    FAILOVER_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    failover_context: FailoverContext
    def __init__(self, failover_context: _Optional[_Union[FailoverContext, _Mapping]] = ...) -> None: ...

class SslCertsCreateEphemeralRequest(_message.Message):
    __slots__ = ("public_key", "access_token")
    PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    public_key: str
    access_token: str
    def __init__(self, public_key: _Optional[str] = ..., access_token: _Optional[str] = ...) -> None: ...

class InstancesImportRequest(_message.Message):
    __slots__ = ("import_context",)
    IMPORT_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    import_context: _cloud_sql_resources_pb2.ImportContext
    def __init__(self, import_context: _Optional[_Union[_cloud_sql_resources_pb2.ImportContext, _Mapping]] = ...) -> None: ...

class InstancesListResponse(_message.Message):
    __slots__ = ("kind", "warnings", "items", "next_page_token")
    KIND_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    kind: str
    warnings: _containers.RepeatedCompositeFieldContainer[_cloud_sql_resources_pb2.ApiWarning]
    items: _containers.RepeatedCompositeFieldContainer[DatabaseInstance]
    next_page_token: str
    def __init__(self, kind: _Optional[str] = ..., warnings: _Optional[_Iterable[_Union[_cloud_sql_resources_pb2.ApiWarning, _Mapping]]] = ..., items: _Optional[_Iterable[_Union[DatabaseInstance, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class InstancesListServerCasResponse(_message.Message):
    __slots__ = ("certs", "active_version", "kind")
    CERTS_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_VERSION_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    certs: _containers.RepeatedCompositeFieldContainer[_cloud_sql_resources_pb2.SslCert]
    active_version: str
    kind: str
    def __init__(self, certs: _Optional[_Iterable[_Union[_cloud_sql_resources_pb2.SslCert, _Mapping]]] = ..., active_version: _Optional[str] = ..., kind: _Optional[str] = ...) -> None: ...

class InstancesRestoreBackupRequest(_message.Message):
    __slots__ = ("restore_backup_context",)
    RESTORE_BACKUP_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    restore_backup_context: RestoreBackupContext
    def __init__(self, restore_backup_context: _Optional[_Union[RestoreBackupContext, _Mapping]] = ...) -> None: ...

class InstancesRotateServerCaRequest(_message.Message):
    __slots__ = ("rotate_server_ca_context",)
    ROTATE_SERVER_CA_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    rotate_server_ca_context: RotateServerCaContext
    def __init__(self, rotate_server_ca_context: _Optional[_Union[RotateServerCaContext, _Mapping]] = ...) -> None: ...

class InstancesTruncateLogRequest(_message.Message):
    __slots__ = ("truncate_log_context",)
    TRUNCATE_LOG_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    truncate_log_context: TruncateLogContext
    def __init__(self, truncate_log_context: _Optional[_Union[TruncateLogContext, _Mapping]] = ...) -> None: ...

class InstancesAcquireSsrsLeaseRequest(_message.Message):
    __slots__ = ("acquire_ssrs_lease_context",)
    ACQUIRE_SSRS_LEASE_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    acquire_ssrs_lease_context: _cloud_sql_resources_pb2.AcquireSsrsLeaseContext
    def __init__(self, acquire_ssrs_lease_context: _Optional[_Union[_cloud_sql_resources_pb2.AcquireSsrsLeaseContext, _Mapping]] = ...) -> None: ...

class SqlInstancesVerifyExternalSyncSettingsResponse(_message.Message):
    __slots__ = ("kind", "errors", "warnings")
    KIND_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    kind: str
    errors: _containers.RepeatedCompositeFieldContainer[SqlExternalSyncSettingError]
    warnings: _containers.RepeatedCompositeFieldContainer[SqlExternalSyncSettingError]
    def __init__(self, kind: _Optional[str] = ..., errors: _Optional[_Iterable[_Union[SqlExternalSyncSettingError, _Mapping]]] = ..., warnings: _Optional[_Iterable[_Union[SqlExternalSyncSettingError, _Mapping]]] = ...) -> None: ...

class SqlInstancesGetDiskShrinkConfigResponse(_message.Message):
    __slots__ = ("kind", "minimal_target_size_gb", "message")
    KIND_FIELD_NUMBER: _ClassVar[int]
    MINIMAL_TARGET_SIZE_GB_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    kind: str
    minimal_target_size_gb: int
    message: str
    def __init__(self, kind: _Optional[str] = ..., minimal_target_size_gb: _Optional[int] = ..., message: _Optional[str] = ...) -> None: ...

class SqlInstancesGetLatestRecoveryTimeRequest(_message.Message):
    __slots__ = ("instance", "project")
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    instance: str
    project: str
    def __init__(self, instance: _Optional[str] = ..., project: _Optional[str] = ...) -> None: ...

class SqlInstancesGetLatestRecoveryTimeResponse(_message.Message):
    __slots__ = ("kind", "latest_recovery_time")
    KIND_FIELD_NUMBER: _ClassVar[int]
    LATEST_RECOVERY_TIME_FIELD_NUMBER: _ClassVar[int]
    kind: str
    latest_recovery_time: _timestamp_pb2.Timestamp
    def __init__(self, kind: _Optional[str] = ..., latest_recovery_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class CloneContext(_message.Message):
    __slots__ = ("kind", "pitr_timestamp_ms", "destination_instance_name", "bin_log_coordinates", "point_in_time", "allocated_ip_range", "database_names", "preferred_zone")
    KIND_FIELD_NUMBER: _ClassVar[int]
    PITR_TIMESTAMP_MS_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_INSTANCE_NAME_FIELD_NUMBER: _ClassVar[int]
    BIN_LOG_COORDINATES_FIELD_NUMBER: _ClassVar[int]
    POINT_IN_TIME_FIELD_NUMBER: _ClassVar[int]
    ALLOCATED_IP_RANGE_FIELD_NUMBER: _ClassVar[int]
    DATABASE_NAMES_FIELD_NUMBER: _ClassVar[int]
    PREFERRED_ZONE_FIELD_NUMBER: _ClassVar[int]
    kind: str
    pitr_timestamp_ms: int
    destination_instance_name: str
    bin_log_coordinates: BinLogCoordinates
    point_in_time: _timestamp_pb2.Timestamp
    allocated_ip_range: str
    database_names: _containers.RepeatedScalarFieldContainer[str]
    preferred_zone: str
    def __init__(self, kind: _Optional[str] = ..., pitr_timestamp_ms: _Optional[int] = ..., destination_instance_name: _Optional[str] = ..., bin_log_coordinates: _Optional[_Union[BinLogCoordinates, _Mapping]] = ..., point_in_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., allocated_ip_range: _Optional[str] = ..., database_names: _Optional[_Iterable[str]] = ..., preferred_zone: _Optional[str] = ...) -> None: ...

class BinLogCoordinates(_message.Message):
    __slots__ = ("bin_log_file_name", "bin_log_position", "kind")
    BIN_LOG_FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    BIN_LOG_POSITION_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    bin_log_file_name: str
    bin_log_position: int
    kind: str
    def __init__(self, bin_log_file_name: _Optional[str] = ..., bin_log_position: _Optional[int] = ..., kind: _Optional[str] = ...) -> None: ...

class DatabaseInstance(_message.Message):
    __slots__ = ("kind", "state", "database_version", "settings", "etag", "failover_replica", "master_instance_name", "replica_names", "max_disk_size", "current_disk_size", "ip_addresses", "server_ca_cert", "instance_type", "project", "ipv6_address", "service_account_email_address", "on_premises_configuration", "replica_configuration", "backend_type", "self_link", "suspension_reason", "connection_name", "name", "region", "gce_zone", "secondary_gce_zone", "disk_encryption_configuration", "disk_encryption_status", "root_password", "scheduled_maintenance", "satisfies_pzs", "database_installed_version", "out_of_disk_report", "create_time", "available_maintenance_versions", "maintenance_version", "upgradable_database_versions", "sql_network_architecture", "psc_service_attachment_link", "dns_name", "primary_dns_name", "write_endpoint", "replication_cluster", "gemini_config", "satisfies_pzi", "switch_transaction_logs_to_cloud_storage_enabled")
    class SqlInstanceState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SQL_INSTANCE_STATE_UNSPECIFIED: _ClassVar[DatabaseInstance.SqlInstanceState]
        RUNNABLE: _ClassVar[DatabaseInstance.SqlInstanceState]
        SUSPENDED: _ClassVar[DatabaseInstance.SqlInstanceState]
        PENDING_DELETE: _ClassVar[DatabaseInstance.SqlInstanceState]
        PENDING_CREATE: _ClassVar[DatabaseInstance.SqlInstanceState]
        MAINTENANCE: _ClassVar[DatabaseInstance.SqlInstanceState]
        FAILED: _ClassVar[DatabaseInstance.SqlInstanceState]
        ONLINE_MAINTENANCE: _ClassVar[DatabaseInstance.SqlInstanceState]
    SQL_INSTANCE_STATE_UNSPECIFIED: DatabaseInstance.SqlInstanceState
    RUNNABLE: DatabaseInstance.SqlInstanceState
    SUSPENDED: DatabaseInstance.SqlInstanceState
    PENDING_DELETE: DatabaseInstance.SqlInstanceState
    PENDING_CREATE: DatabaseInstance.SqlInstanceState
    MAINTENANCE: DatabaseInstance.SqlInstanceState
    FAILED: DatabaseInstance.SqlInstanceState
    ONLINE_MAINTENANCE: DatabaseInstance.SqlInstanceState
    class SqlNetworkArchitecture(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SQL_NETWORK_ARCHITECTURE_UNSPECIFIED: _ClassVar[DatabaseInstance.SqlNetworkArchitecture]
        NEW_NETWORK_ARCHITECTURE: _ClassVar[DatabaseInstance.SqlNetworkArchitecture]
        OLD_NETWORK_ARCHITECTURE: _ClassVar[DatabaseInstance.SqlNetworkArchitecture]
    SQL_NETWORK_ARCHITECTURE_UNSPECIFIED: DatabaseInstance.SqlNetworkArchitecture
    NEW_NETWORK_ARCHITECTURE: DatabaseInstance.SqlNetworkArchitecture
    OLD_NETWORK_ARCHITECTURE: DatabaseInstance.SqlNetworkArchitecture
    class SqlFailoverReplica(_message.Message):
        __slots__ = ("name", "available")
        NAME_FIELD_NUMBER: _ClassVar[int]
        AVAILABLE_FIELD_NUMBER: _ClassVar[int]
        name: str
        available: _wrappers_pb2.BoolValue
        def __init__(self, name: _Optional[str] = ..., available: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...) -> None: ...
    class SqlScheduledMaintenance(_message.Message):
        __slots__ = ("start_time", "can_defer", "can_reschedule", "schedule_deadline_time")
        START_TIME_FIELD_NUMBER: _ClassVar[int]
        CAN_DEFER_FIELD_NUMBER: _ClassVar[int]
        CAN_RESCHEDULE_FIELD_NUMBER: _ClassVar[int]
        SCHEDULE_DEADLINE_TIME_FIELD_NUMBER: _ClassVar[int]
        start_time: _timestamp_pb2.Timestamp
        can_defer: bool
        can_reschedule: bool
        schedule_deadline_time: _timestamp_pb2.Timestamp
        def __init__(self, start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., can_defer: bool = ..., can_reschedule: bool = ..., schedule_deadline_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    class SqlOutOfDiskReport(_message.Message):
        __slots__ = ("sql_out_of_disk_state", "sql_min_recommended_increase_size_gb")
        class SqlOutOfDiskState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            SQL_OUT_OF_DISK_STATE_UNSPECIFIED: _ClassVar[DatabaseInstance.SqlOutOfDiskReport.SqlOutOfDiskState]
            NORMAL: _ClassVar[DatabaseInstance.SqlOutOfDiskReport.SqlOutOfDiskState]
            SOFT_SHUTDOWN: _ClassVar[DatabaseInstance.SqlOutOfDiskReport.SqlOutOfDiskState]
        SQL_OUT_OF_DISK_STATE_UNSPECIFIED: DatabaseInstance.SqlOutOfDiskReport.SqlOutOfDiskState
        NORMAL: DatabaseInstance.SqlOutOfDiskReport.SqlOutOfDiskState
        SOFT_SHUTDOWN: DatabaseInstance.SqlOutOfDiskReport.SqlOutOfDiskState
        SQL_OUT_OF_DISK_STATE_FIELD_NUMBER: _ClassVar[int]
        SQL_MIN_RECOMMENDED_INCREASE_SIZE_GB_FIELD_NUMBER: _ClassVar[int]
        sql_out_of_disk_state: DatabaseInstance.SqlOutOfDiskReport.SqlOutOfDiskState
        sql_min_recommended_increase_size_gb: int
        def __init__(self, sql_out_of_disk_state: _Optional[_Union[DatabaseInstance.SqlOutOfDiskReport.SqlOutOfDiskState, str]] = ..., sql_min_recommended_increase_size_gb: _Optional[int] = ...) -> None: ...
    KIND_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    DATABASE_VERSION_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    FAILOVER_REPLICA_FIELD_NUMBER: _ClassVar[int]
    MASTER_INSTANCE_NAME_FIELD_NUMBER: _ClassVar[int]
    REPLICA_NAMES_FIELD_NUMBER: _ClassVar[int]
    MAX_DISK_SIZE_FIELD_NUMBER: _ClassVar[int]
    CURRENT_DISK_SIZE_FIELD_NUMBER: _ClassVar[int]
    IP_ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    SERVER_CA_CERT_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    IPV6_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_EMAIL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    ON_PREMISES_CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    REPLICA_CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    BACKEND_TYPE_FIELD_NUMBER: _ClassVar[int]
    SELF_LINK_FIELD_NUMBER: _ClassVar[int]
    SUSPENSION_REASON_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    GCE_ZONE_FIELD_NUMBER: _ClassVar[int]
    SECONDARY_GCE_ZONE_FIELD_NUMBER: _ClassVar[int]
    DISK_ENCRYPTION_CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    DISK_ENCRYPTION_STATUS_FIELD_NUMBER: _ClassVar[int]
    ROOT_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    SCHEDULED_MAINTENANCE_FIELD_NUMBER: _ClassVar[int]
    SATISFIES_PZS_FIELD_NUMBER: _ClassVar[int]
    DATABASE_INSTALLED_VERSION_FIELD_NUMBER: _ClassVar[int]
    OUT_OF_DISK_REPORT_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_MAINTENANCE_VERSIONS_FIELD_NUMBER: _ClassVar[int]
    MAINTENANCE_VERSION_FIELD_NUMBER: _ClassVar[int]
    UPGRADABLE_DATABASE_VERSIONS_FIELD_NUMBER: _ClassVar[int]
    SQL_NETWORK_ARCHITECTURE_FIELD_NUMBER: _ClassVar[int]
    PSC_SERVICE_ATTACHMENT_LINK_FIELD_NUMBER: _ClassVar[int]
    DNS_NAME_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_DNS_NAME_FIELD_NUMBER: _ClassVar[int]
    WRITE_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    REPLICATION_CLUSTER_FIELD_NUMBER: _ClassVar[int]
    GEMINI_CONFIG_FIELD_NUMBER: _ClassVar[int]
    SATISFIES_PZI_FIELD_NUMBER: _ClassVar[int]
    SWITCH_TRANSACTION_LOGS_TO_CLOUD_STORAGE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    kind: str
    state: DatabaseInstance.SqlInstanceState
    database_version: _cloud_sql_resources_pb2.SqlDatabaseVersion
    settings: _cloud_sql_resources_pb2.Settings
    etag: str
    failover_replica: DatabaseInstance.SqlFailoverReplica
    master_instance_name: str
    replica_names: _containers.RepeatedScalarFieldContainer[str]
    max_disk_size: _wrappers_pb2.Int64Value
    current_disk_size: _wrappers_pb2.Int64Value
    ip_addresses: _containers.RepeatedCompositeFieldContainer[_cloud_sql_resources_pb2.IpMapping]
    server_ca_cert: _cloud_sql_resources_pb2.SslCert
    instance_type: SqlInstanceType
    project: str
    ipv6_address: str
    service_account_email_address: str
    on_premises_configuration: OnPremisesConfiguration
    replica_configuration: ReplicaConfiguration
    backend_type: _cloud_sql_resources_pb2.SqlBackendType
    self_link: str
    suspension_reason: _containers.RepeatedScalarFieldContainer[SqlSuspensionReason]
    connection_name: str
    name: str
    region: str
    gce_zone: str
    secondary_gce_zone: str
    disk_encryption_configuration: _cloud_sql_resources_pb2.DiskEncryptionConfiguration
    disk_encryption_status: _cloud_sql_resources_pb2.DiskEncryptionStatus
    root_password: str
    scheduled_maintenance: DatabaseInstance.SqlScheduledMaintenance
    satisfies_pzs: _wrappers_pb2.BoolValue
    database_installed_version: str
    out_of_disk_report: DatabaseInstance.SqlOutOfDiskReport
    create_time: _timestamp_pb2.Timestamp
    available_maintenance_versions: _containers.RepeatedScalarFieldContainer[str]
    maintenance_version: str
    upgradable_database_versions: _containers.RepeatedCompositeFieldContainer[AvailableDatabaseVersion]
    sql_network_architecture: DatabaseInstance.SqlNetworkArchitecture
    psc_service_attachment_link: str
    dns_name: str
    primary_dns_name: str
    write_endpoint: str
    replication_cluster: ReplicationCluster
    gemini_config: GeminiInstanceConfig
    satisfies_pzi: _wrappers_pb2.BoolValue
    switch_transaction_logs_to_cloud_storage_enabled: _wrappers_pb2.BoolValue
    def __init__(self, kind: _Optional[str] = ..., state: _Optional[_Union[DatabaseInstance.SqlInstanceState, str]] = ..., database_version: _Optional[_Union[_cloud_sql_resources_pb2.SqlDatabaseVersion, str]] = ..., settings: _Optional[_Union[_cloud_sql_resources_pb2.Settings, _Mapping]] = ..., etag: _Optional[str] = ..., failover_replica: _Optional[_Union[DatabaseInstance.SqlFailoverReplica, _Mapping]] = ..., master_instance_name: _Optional[str] = ..., replica_names: _Optional[_Iterable[str]] = ..., max_disk_size: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., current_disk_size: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., ip_addresses: _Optional[_Iterable[_Union[_cloud_sql_resources_pb2.IpMapping, _Mapping]]] = ..., server_ca_cert: _Optional[_Union[_cloud_sql_resources_pb2.SslCert, _Mapping]] = ..., instance_type: _Optional[_Union[SqlInstanceType, str]] = ..., project: _Optional[str] = ..., ipv6_address: _Optional[str] = ..., service_account_email_address: _Optional[str] = ..., on_premises_configuration: _Optional[_Union[OnPremisesConfiguration, _Mapping]] = ..., replica_configuration: _Optional[_Union[ReplicaConfiguration, _Mapping]] = ..., backend_type: _Optional[_Union[_cloud_sql_resources_pb2.SqlBackendType, str]] = ..., self_link: _Optional[str] = ..., suspension_reason: _Optional[_Iterable[_Union[SqlSuspensionReason, str]]] = ..., connection_name: _Optional[str] = ..., name: _Optional[str] = ..., region: _Optional[str] = ..., gce_zone: _Optional[str] = ..., secondary_gce_zone: _Optional[str] = ..., disk_encryption_configuration: _Optional[_Union[_cloud_sql_resources_pb2.DiskEncryptionConfiguration, _Mapping]] = ..., disk_encryption_status: _Optional[_Union[_cloud_sql_resources_pb2.DiskEncryptionStatus, _Mapping]] = ..., root_password: _Optional[str] = ..., scheduled_maintenance: _Optional[_Union[DatabaseInstance.SqlScheduledMaintenance, _Mapping]] = ..., satisfies_pzs: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., database_installed_version: _Optional[str] = ..., out_of_disk_report: _Optional[_Union[DatabaseInstance.SqlOutOfDiskReport, _Mapping]] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., available_maintenance_versions: _Optional[_Iterable[str]] = ..., maintenance_version: _Optional[str] = ..., upgradable_database_versions: _Optional[_Iterable[_Union[AvailableDatabaseVersion, _Mapping]]] = ..., sql_network_architecture: _Optional[_Union[DatabaseInstance.SqlNetworkArchitecture, str]] = ..., psc_service_attachment_link: _Optional[str] = ..., dns_name: _Optional[str] = ..., primary_dns_name: _Optional[str] = ..., write_endpoint: _Optional[str] = ..., replication_cluster: _Optional[_Union[ReplicationCluster, _Mapping]] = ..., gemini_config: _Optional[_Union[GeminiInstanceConfig, _Mapping]] = ..., satisfies_pzi: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., switch_transaction_logs_to_cloud_storage_enabled: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...) -> None: ...

class GeminiInstanceConfig(_message.Message):
    __slots__ = ("entitled", "google_vacuum_mgmt_enabled", "oom_session_cancel_enabled", "active_query_enabled", "index_advisor_enabled", "flag_recommender_enabled")
    ENTITLED_FIELD_NUMBER: _ClassVar[int]
    GOOGLE_VACUUM_MGMT_ENABLED_FIELD_NUMBER: _ClassVar[int]
    OOM_SESSION_CANCEL_ENABLED_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_QUERY_ENABLED_FIELD_NUMBER: _ClassVar[int]
    INDEX_ADVISOR_ENABLED_FIELD_NUMBER: _ClassVar[int]
    FLAG_RECOMMENDER_ENABLED_FIELD_NUMBER: _ClassVar[int]
    entitled: bool
    google_vacuum_mgmt_enabled: bool
    oom_session_cancel_enabled: bool
    active_query_enabled: bool
    index_advisor_enabled: bool
    flag_recommender_enabled: bool
    def __init__(self, entitled: bool = ..., google_vacuum_mgmt_enabled: bool = ..., oom_session_cancel_enabled: bool = ..., active_query_enabled: bool = ..., index_advisor_enabled: bool = ..., flag_recommender_enabled: bool = ...) -> None: ...

class ReplicationCluster(_message.Message):
    __slots__ = ("psa_write_endpoint", "failover_dr_replica_name", "dr_replica")
    PSA_WRITE_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    FAILOVER_DR_REPLICA_NAME_FIELD_NUMBER: _ClassVar[int]
    DR_REPLICA_FIELD_NUMBER: _ClassVar[int]
    psa_write_endpoint: str
    failover_dr_replica_name: str
    dr_replica: bool
    def __init__(self, psa_write_endpoint: _Optional[str] = ..., failover_dr_replica_name: _Optional[str] = ..., dr_replica: bool = ...) -> None: ...

class AvailableDatabaseVersion(_message.Message):
    __slots__ = ("major_version", "name", "display_name")
    MAJOR_VERSION_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    major_version: str
    name: str
    display_name: str
    def __init__(self, major_version: _Optional[str] = ..., name: _Optional[str] = ..., display_name: _Optional[str] = ...) -> None: ...

class SqlInstancesRescheduleMaintenanceRequestBody(_message.Message):
    __slots__ = ("reschedule",)
    class RescheduleType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RESCHEDULE_TYPE_UNSPECIFIED: _ClassVar[SqlInstancesRescheduleMaintenanceRequestBody.RescheduleType]
        IMMEDIATE: _ClassVar[SqlInstancesRescheduleMaintenanceRequestBody.RescheduleType]
        NEXT_AVAILABLE_WINDOW: _ClassVar[SqlInstancesRescheduleMaintenanceRequestBody.RescheduleType]
        SPECIFIC_TIME: _ClassVar[SqlInstancesRescheduleMaintenanceRequestBody.RescheduleType]
    RESCHEDULE_TYPE_UNSPECIFIED: SqlInstancesRescheduleMaintenanceRequestBody.RescheduleType
    IMMEDIATE: SqlInstancesRescheduleMaintenanceRequestBody.RescheduleType
    NEXT_AVAILABLE_WINDOW: SqlInstancesRescheduleMaintenanceRequestBody.RescheduleType
    SPECIFIC_TIME: SqlInstancesRescheduleMaintenanceRequestBody.RescheduleType
    class Reschedule(_message.Message):
        __slots__ = ("reschedule_type", "schedule_time")
        RESCHEDULE_TYPE_FIELD_NUMBER: _ClassVar[int]
        SCHEDULE_TIME_FIELD_NUMBER: _ClassVar[int]
        reschedule_type: SqlInstancesRescheduleMaintenanceRequestBody.RescheduleType
        schedule_time: _timestamp_pb2.Timestamp
        def __init__(self, reschedule_type: _Optional[_Union[SqlInstancesRescheduleMaintenanceRequestBody.RescheduleType, str]] = ..., schedule_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    RESCHEDULE_FIELD_NUMBER: _ClassVar[int]
    reschedule: SqlInstancesRescheduleMaintenanceRequestBody.Reschedule
    def __init__(self, reschedule: _Optional[_Union[SqlInstancesRescheduleMaintenanceRequestBody.Reschedule, _Mapping]] = ...) -> None: ...

class DemoteMasterContext(_message.Message):
    __slots__ = ("kind", "verify_gtid_consistency", "master_instance_name", "replica_configuration", "skip_replication_setup")
    KIND_FIELD_NUMBER: _ClassVar[int]
    VERIFY_GTID_CONSISTENCY_FIELD_NUMBER: _ClassVar[int]
    MASTER_INSTANCE_NAME_FIELD_NUMBER: _ClassVar[int]
    REPLICA_CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    SKIP_REPLICATION_SETUP_FIELD_NUMBER: _ClassVar[int]
    kind: str
    verify_gtid_consistency: _wrappers_pb2.BoolValue
    master_instance_name: str
    replica_configuration: _cloud_sql_resources_pb2.DemoteMasterConfiguration
    skip_replication_setup: bool
    def __init__(self, kind: _Optional[str] = ..., verify_gtid_consistency: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., master_instance_name: _Optional[str] = ..., replica_configuration: _Optional[_Union[_cloud_sql_resources_pb2.DemoteMasterConfiguration, _Mapping]] = ..., skip_replication_setup: bool = ...) -> None: ...

class DemoteContext(_message.Message):
    __slots__ = ("kind", "source_representative_instance_name")
    KIND_FIELD_NUMBER: _ClassVar[int]
    SOURCE_REPRESENTATIVE_INSTANCE_NAME_FIELD_NUMBER: _ClassVar[int]
    kind: str
    source_representative_instance_name: str
    def __init__(self, kind: _Optional[str] = ..., source_representative_instance_name: _Optional[str] = ...) -> None: ...

class FailoverContext(_message.Message):
    __slots__ = ("settings_version", "kind")
    SETTINGS_VERSION_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    settings_version: int
    kind: str
    def __init__(self, settings_version: _Optional[int] = ..., kind: _Optional[str] = ...) -> None: ...

class RestoreBackupContext(_message.Message):
    __slots__ = ("kind", "backup_run_id", "instance_id", "project")
    KIND_FIELD_NUMBER: _ClassVar[int]
    BACKUP_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    kind: str
    backup_run_id: int
    instance_id: str
    project: str
    def __init__(self, kind: _Optional[str] = ..., backup_run_id: _Optional[int] = ..., instance_id: _Optional[str] = ..., project: _Optional[str] = ...) -> None: ...

class RotateServerCaContext(_message.Message):
    __slots__ = ("kind", "next_version")
    KIND_FIELD_NUMBER: _ClassVar[int]
    NEXT_VERSION_FIELD_NUMBER: _ClassVar[int]
    kind: str
    next_version: str
    def __init__(self, kind: _Optional[str] = ..., next_version: _Optional[str] = ...) -> None: ...

class TruncateLogContext(_message.Message):
    __slots__ = ("kind", "log_type")
    KIND_FIELD_NUMBER: _ClassVar[int]
    LOG_TYPE_FIELD_NUMBER: _ClassVar[int]
    kind: str
    log_type: str
    def __init__(self, kind: _Optional[str] = ..., log_type: _Optional[str] = ...) -> None: ...

class SqlExternalSyncSettingError(_message.Message):
    __slots__ = ("kind", "type", "detail")
    class SqlExternalSyncSettingErrorType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SQL_EXTERNAL_SYNC_SETTING_ERROR_TYPE_UNSPECIFIED: _ClassVar[SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType]
        CONNECTION_FAILURE: _ClassVar[SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType]
        BINLOG_NOT_ENABLED: _ClassVar[SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType]
        INCOMPATIBLE_DATABASE_VERSION: _ClassVar[SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType]
        REPLICA_ALREADY_SETUP: _ClassVar[SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType]
        INSUFFICIENT_PRIVILEGE: _ClassVar[SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType]
        UNSUPPORTED_MIGRATION_TYPE: _ClassVar[SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType]
        NO_PGLOGICAL_INSTALLED: _ClassVar[SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType]
        PGLOGICAL_NODE_ALREADY_EXISTS: _ClassVar[SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType]
        INVALID_WAL_LEVEL: _ClassVar[SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType]
        INVALID_SHARED_PRELOAD_LIBRARY: _ClassVar[SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType]
        INSUFFICIENT_MAX_REPLICATION_SLOTS: _ClassVar[SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType]
        INSUFFICIENT_MAX_WAL_SENDERS: _ClassVar[SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType]
        INSUFFICIENT_MAX_WORKER_PROCESSES: _ClassVar[SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType]
        UNSUPPORTED_EXTENSIONS: _ClassVar[SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType]
        INVALID_RDS_LOGICAL_REPLICATION: _ClassVar[SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType]
        INVALID_LOGGING_SETUP: _ClassVar[SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType]
        INVALID_DB_PARAM: _ClassVar[SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType]
        UNSUPPORTED_GTID_MODE: _ClassVar[SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType]
        SQLSERVER_AGENT_NOT_RUNNING: _ClassVar[SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType]
        UNSUPPORTED_TABLE_DEFINITION: _ClassVar[SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType]
        UNSUPPORTED_DEFINER: _ClassVar[SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType]
        SQLSERVER_SERVERNAME_MISMATCH: _ClassVar[SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType]
        PRIMARY_ALREADY_SETUP: _ClassVar[SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType]
        UNSUPPORTED_BINLOG_FORMAT: _ClassVar[SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType]
        BINLOG_RETENTION_SETTING: _ClassVar[SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType]
        UNSUPPORTED_STORAGE_ENGINE: _ClassVar[SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType]
        LIMITED_SUPPORT_TABLES: _ClassVar[SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType]
        EXISTING_DATA_IN_REPLICA: _ClassVar[SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType]
        MISSING_OPTIONAL_PRIVILEGES: _ClassVar[SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType]
        RISKY_BACKUP_ADMIN_PRIVILEGE: _ClassVar[SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType]
        INSUFFICIENT_GCS_PERMISSIONS: _ClassVar[SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType]
        INVALID_FILE_INFO: _ClassVar[SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType]
        UNSUPPORTED_DATABASE_SETTINGS: _ClassVar[SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType]
        MYSQL_PARALLEL_IMPORT_INSUFFICIENT_PRIVILEGE: _ClassVar[SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType]
        LOCAL_INFILE_OFF: _ClassVar[SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType]
        TURN_ON_PITR_AFTER_PROMOTE: _ClassVar[SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType]
        INCOMPATIBLE_DATABASE_MINOR_VERSION: _ClassVar[SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType]
        SOURCE_MAX_SUBSCRIPTIONS: _ClassVar[SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType]
        UNABLE_TO_VERIFY_DEFINERS: _ClassVar[SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType]
        SUBSCRIPTION_CALCULATION_STATUS: _ClassVar[SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType]
        PG_SUBSCRIPTION_COUNT: _ClassVar[SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType]
        PG_SYNC_PARALLEL_LEVEL: _ClassVar[SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType]
        INSUFFICIENT_DISK_SIZE: _ClassVar[SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType]
        INSUFFICIENT_MACHINE_TIER: _ClassVar[SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType]
        UNSUPPORTED_EXTENSIONS_NOT_MIGRATED: _ClassVar[SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType]
        EXTENSIONS_NOT_MIGRATED: _ClassVar[SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType]
        PG_CRON_FLAG_ENABLED_IN_REPLICA: _ClassVar[SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType]
        EXTENSIONS_NOT_ENABLED_IN_REPLICA: _ClassVar[SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType]
        UNSUPPORTED_COLUMNS: _ClassVar[SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType]
    SQL_EXTERNAL_SYNC_SETTING_ERROR_TYPE_UNSPECIFIED: SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType
    CONNECTION_FAILURE: SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType
    BINLOG_NOT_ENABLED: SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType
    INCOMPATIBLE_DATABASE_VERSION: SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType
    REPLICA_ALREADY_SETUP: SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType
    INSUFFICIENT_PRIVILEGE: SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType
    UNSUPPORTED_MIGRATION_TYPE: SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType
    NO_PGLOGICAL_INSTALLED: SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType
    PGLOGICAL_NODE_ALREADY_EXISTS: SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType
    INVALID_WAL_LEVEL: SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType
    INVALID_SHARED_PRELOAD_LIBRARY: SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType
    INSUFFICIENT_MAX_REPLICATION_SLOTS: SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType
    INSUFFICIENT_MAX_WAL_SENDERS: SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType
    INSUFFICIENT_MAX_WORKER_PROCESSES: SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType
    UNSUPPORTED_EXTENSIONS: SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType
    INVALID_RDS_LOGICAL_REPLICATION: SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType
    INVALID_LOGGING_SETUP: SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType
    INVALID_DB_PARAM: SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType
    UNSUPPORTED_GTID_MODE: SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType
    SQLSERVER_AGENT_NOT_RUNNING: SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType
    UNSUPPORTED_TABLE_DEFINITION: SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType
    UNSUPPORTED_DEFINER: SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType
    SQLSERVER_SERVERNAME_MISMATCH: SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType
    PRIMARY_ALREADY_SETUP: SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType
    UNSUPPORTED_BINLOG_FORMAT: SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType
    BINLOG_RETENTION_SETTING: SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType
    UNSUPPORTED_STORAGE_ENGINE: SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType
    LIMITED_SUPPORT_TABLES: SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType
    EXISTING_DATA_IN_REPLICA: SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType
    MISSING_OPTIONAL_PRIVILEGES: SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType
    RISKY_BACKUP_ADMIN_PRIVILEGE: SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType
    INSUFFICIENT_GCS_PERMISSIONS: SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType
    INVALID_FILE_INFO: SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType
    UNSUPPORTED_DATABASE_SETTINGS: SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType
    MYSQL_PARALLEL_IMPORT_INSUFFICIENT_PRIVILEGE: SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType
    LOCAL_INFILE_OFF: SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType
    TURN_ON_PITR_AFTER_PROMOTE: SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType
    INCOMPATIBLE_DATABASE_MINOR_VERSION: SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType
    SOURCE_MAX_SUBSCRIPTIONS: SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType
    UNABLE_TO_VERIFY_DEFINERS: SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType
    SUBSCRIPTION_CALCULATION_STATUS: SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType
    PG_SUBSCRIPTION_COUNT: SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType
    PG_SYNC_PARALLEL_LEVEL: SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType
    INSUFFICIENT_DISK_SIZE: SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType
    INSUFFICIENT_MACHINE_TIER: SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType
    UNSUPPORTED_EXTENSIONS_NOT_MIGRATED: SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType
    EXTENSIONS_NOT_MIGRATED: SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType
    PG_CRON_FLAG_ENABLED_IN_REPLICA: SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType
    EXTENSIONS_NOT_ENABLED_IN_REPLICA: SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType
    UNSUPPORTED_COLUMNS: SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType
    KIND_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DETAIL_FIELD_NUMBER: _ClassVar[int]
    kind: str
    type: SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType
    detail: str
    def __init__(self, kind: _Optional[str] = ..., type: _Optional[_Union[SqlExternalSyncSettingError.SqlExternalSyncSettingErrorType, str]] = ..., detail: _Optional[str] = ...) -> None: ...

class OnPremisesConfiguration(_message.Message):
    __slots__ = ("host_port", "kind", "username", "password", "ca_certificate", "client_certificate", "client_key", "dump_file_path", "source_instance")
    HOST_PORT_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    CA_CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    CLIENT_CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    CLIENT_KEY_FIELD_NUMBER: _ClassVar[int]
    DUMP_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    SOURCE_INSTANCE_FIELD_NUMBER: _ClassVar[int]
    host_port: str
    kind: str
    username: str
    password: str
    ca_certificate: str
    client_certificate: str
    client_key: str
    dump_file_path: str
    source_instance: _cloud_sql_resources_pb2.InstanceReference
    def __init__(self, host_port: _Optional[str] = ..., kind: _Optional[str] = ..., username: _Optional[str] = ..., password: _Optional[str] = ..., ca_certificate: _Optional[str] = ..., client_certificate: _Optional[str] = ..., client_key: _Optional[str] = ..., dump_file_path: _Optional[str] = ..., source_instance: _Optional[_Union[_cloud_sql_resources_pb2.InstanceReference, _Mapping]] = ...) -> None: ...

class ReplicaConfiguration(_message.Message):
    __slots__ = ("kind", "mysql_replica_configuration", "failover_target", "cascadable_replica")
    KIND_FIELD_NUMBER: _ClassVar[int]
    MYSQL_REPLICA_CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    FAILOVER_TARGET_FIELD_NUMBER: _ClassVar[int]
    CASCADABLE_REPLICA_FIELD_NUMBER: _ClassVar[int]
    kind: str
    mysql_replica_configuration: _cloud_sql_resources_pb2.MySqlReplicaConfiguration
    failover_target: _wrappers_pb2.BoolValue
    cascadable_replica: _wrappers_pb2.BoolValue
    def __init__(self, kind: _Optional[str] = ..., mysql_replica_configuration: _Optional[_Union[_cloud_sql_resources_pb2.MySqlReplicaConfiguration, _Mapping]] = ..., failover_target: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., cascadable_replica: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...) -> None: ...

class SqlInstancesAcquireSsrsLeaseRequest(_message.Message):
    __slots__ = ("instance", "project", "body")
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    instance: str
    project: str
    body: InstancesAcquireSsrsLeaseRequest
    def __init__(self, instance: _Optional[str] = ..., project: _Optional[str] = ..., body: _Optional[_Union[InstancesAcquireSsrsLeaseRequest, _Mapping]] = ...) -> None: ...

class SqlInstancesAcquireSsrsLeaseResponse(_message.Message):
    __slots__ = ("operation_id",)
    OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    operation_id: str
    def __init__(self, operation_id: _Optional[str] = ...) -> None: ...

class SqlInstancesReleaseSsrsLeaseRequest(_message.Message):
    __slots__ = ("instance", "project")
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    instance: str
    project: str
    def __init__(self, instance: _Optional[str] = ..., project: _Optional[str] = ...) -> None: ...

class SqlInstancesReleaseSsrsLeaseResponse(_message.Message):
    __slots__ = ("operation_id",)
    OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    operation_id: str
    def __init__(self, operation_id: _Optional[str] = ...) -> None: ...
