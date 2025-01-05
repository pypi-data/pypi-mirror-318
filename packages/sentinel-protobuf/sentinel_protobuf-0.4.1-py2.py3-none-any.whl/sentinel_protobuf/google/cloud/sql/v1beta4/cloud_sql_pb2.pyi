from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.cloud.sql.v1beta4 import cloud_sql_resources_pb2 as _cloud_sql_resources_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ExternalSyncParallelLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EXTERNAL_SYNC_PARALLEL_LEVEL_UNSPECIFIED: _ClassVar[ExternalSyncParallelLevel]
    MIN: _ClassVar[ExternalSyncParallelLevel]
    OPTIMAL: _ClassVar[ExternalSyncParallelLevel]
    MAX: _ClassVar[ExternalSyncParallelLevel]
EXTERNAL_SYNC_PARALLEL_LEVEL_UNSPECIFIED: ExternalSyncParallelLevel
MIN: ExternalSyncParallelLevel
OPTIMAL: ExternalSyncParallelLevel
MAX: ExternalSyncParallelLevel

class SqlBackupRunsDeleteRequest(_message.Message):
    __slots__ = ("id", "instance", "project")
    ID_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    id: int
    instance: str
    project: str
    def __init__(self, id: _Optional[int] = ..., instance: _Optional[str] = ..., project: _Optional[str] = ...) -> None: ...

class SqlBackupRunsGetRequest(_message.Message):
    __slots__ = ("id", "instance", "project")
    ID_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    id: int
    instance: str
    project: str
    def __init__(self, id: _Optional[int] = ..., instance: _Optional[str] = ..., project: _Optional[str] = ...) -> None: ...

class SqlBackupRunsInsertRequest(_message.Message):
    __slots__ = ("instance", "project", "body")
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    instance: str
    project: str
    body: _cloud_sql_resources_pb2.BackupRun
    def __init__(self, instance: _Optional[str] = ..., project: _Optional[str] = ..., body: _Optional[_Union[_cloud_sql_resources_pb2.BackupRun, _Mapping]] = ...) -> None: ...

class SqlBackupRunsListRequest(_message.Message):
    __slots__ = ("instance", "max_results", "page_token", "project")
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    MAX_RESULTS_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    instance: str
    max_results: int
    page_token: str
    project: str
    def __init__(self, instance: _Optional[str] = ..., max_results: _Optional[int] = ..., page_token: _Optional[str] = ..., project: _Optional[str] = ...) -> None: ...

class SqlDatabasesDeleteRequest(_message.Message):
    __slots__ = ("database", "instance", "project")
    DATABASE_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    database: str
    instance: str
    project: str
    def __init__(self, database: _Optional[str] = ..., instance: _Optional[str] = ..., project: _Optional[str] = ...) -> None: ...

class SqlDatabasesGetRequest(_message.Message):
    __slots__ = ("database", "instance", "project")
    DATABASE_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    database: str
    instance: str
    project: str
    def __init__(self, database: _Optional[str] = ..., instance: _Optional[str] = ..., project: _Optional[str] = ...) -> None: ...

class SqlDatabasesInsertRequest(_message.Message):
    __slots__ = ("instance", "project", "body")
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    instance: str
    project: str
    body: _cloud_sql_resources_pb2.Database
    def __init__(self, instance: _Optional[str] = ..., project: _Optional[str] = ..., body: _Optional[_Union[_cloud_sql_resources_pb2.Database, _Mapping]] = ...) -> None: ...

class SqlDatabasesListRequest(_message.Message):
    __slots__ = ("instance", "project")
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    instance: str
    project: str
    def __init__(self, instance: _Optional[str] = ..., project: _Optional[str] = ...) -> None: ...

class SqlDatabasesUpdateRequest(_message.Message):
    __slots__ = ("database", "instance", "project", "body")
    DATABASE_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    database: str
    instance: str
    project: str
    body: _cloud_sql_resources_pb2.Database
    def __init__(self, database: _Optional[str] = ..., instance: _Optional[str] = ..., project: _Optional[str] = ..., body: _Optional[_Union[_cloud_sql_resources_pb2.Database, _Mapping]] = ...) -> None: ...

class SqlFlagsListRequest(_message.Message):
    __slots__ = ("database_version",)
    DATABASE_VERSION_FIELD_NUMBER: _ClassVar[int]
    database_version: str
    def __init__(self, database_version: _Optional[str] = ...) -> None: ...

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
    body: _cloud_sql_resources_pb2.InstancesCloneRequest
    def __init__(self, instance: _Optional[str] = ..., project: _Optional[str] = ..., body: _Optional[_Union[_cloud_sql_resources_pb2.InstancesCloneRequest, _Mapping]] = ...) -> None: ...

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
    body: _cloud_sql_resources_pb2.InstancesDemoteMasterRequest
    def __init__(self, instance: _Optional[str] = ..., project: _Optional[str] = ..., body: _Optional[_Union[_cloud_sql_resources_pb2.InstancesDemoteMasterRequest, _Mapping]] = ...) -> None: ...

class SqlInstancesDemoteRequest(_message.Message):
    __slots__ = ("instance", "project", "body")
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    instance: str
    project: str
    body: _cloud_sql_resources_pb2.InstancesDemoteRequest
    def __init__(self, instance: _Optional[str] = ..., project: _Optional[str] = ..., body: _Optional[_Union[_cloud_sql_resources_pb2.InstancesDemoteRequest, _Mapping]] = ...) -> None: ...

class SqlInstancesExportRequest(_message.Message):
    __slots__ = ("instance", "project", "body")
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    instance: str
    project: str
    body: _cloud_sql_resources_pb2.InstancesExportRequest
    def __init__(self, instance: _Optional[str] = ..., project: _Optional[str] = ..., body: _Optional[_Union[_cloud_sql_resources_pb2.InstancesExportRequest, _Mapping]] = ...) -> None: ...

class SqlInstancesFailoverRequest(_message.Message):
    __slots__ = ("instance", "project", "body")
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    instance: str
    project: str
    body: _cloud_sql_resources_pb2.InstancesFailoverRequest
    def __init__(self, instance: _Optional[str] = ..., project: _Optional[str] = ..., body: _Optional[_Union[_cloud_sql_resources_pb2.InstancesFailoverRequest, _Mapping]] = ...) -> None: ...

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
    body: _cloud_sql_resources_pb2.InstancesImportRequest
    def __init__(self, instance: _Optional[str] = ..., project: _Optional[str] = ..., body: _Optional[_Union[_cloud_sql_resources_pb2.InstancesImportRequest, _Mapping]] = ...) -> None: ...

class SqlInstancesInsertRequest(_message.Message):
    __slots__ = ("project", "body")
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    project: str
    body: _cloud_sql_resources_pb2.DatabaseInstance
    def __init__(self, project: _Optional[str] = ..., body: _Optional[_Union[_cloud_sql_resources_pb2.DatabaseInstance, _Mapping]] = ...) -> None: ...

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
    body: _cloud_sql_resources_pb2.DatabaseInstance
    def __init__(self, instance: _Optional[str] = ..., project: _Optional[str] = ..., body: _Optional[_Union[_cloud_sql_resources_pb2.DatabaseInstance, _Mapping]] = ...) -> None: ...

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
    body: _cloud_sql_resources_pb2.InstancesRestoreBackupRequest
    def __init__(self, instance: _Optional[str] = ..., project: _Optional[str] = ..., body: _Optional[_Union[_cloud_sql_resources_pb2.InstancesRestoreBackupRequest, _Mapping]] = ...) -> None: ...

class SqlInstancesRotateServerCaRequest(_message.Message):
    __slots__ = ("instance", "project", "body")
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    instance: str
    project: str
    body: _cloud_sql_resources_pb2.InstancesRotateServerCaRequest
    def __init__(self, instance: _Optional[str] = ..., project: _Optional[str] = ..., body: _Optional[_Union[_cloud_sql_resources_pb2.InstancesRotateServerCaRequest, _Mapping]] = ...) -> None: ...

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
    body: _cloud_sql_resources_pb2.InstancesTruncateLogRequest
    def __init__(self, instance: _Optional[str] = ..., project: _Optional[str] = ..., body: _Optional[_Union[_cloud_sql_resources_pb2.InstancesTruncateLogRequest, _Mapping]] = ...) -> None: ...

class SqlInstancesUpdateRequest(_message.Message):
    __slots__ = ("instance", "project", "body")
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    instance: str
    project: str
    body: _cloud_sql_resources_pb2.DatabaseInstance
    def __init__(self, instance: _Optional[str] = ..., project: _Optional[str] = ..., body: _Optional[_Union[_cloud_sql_resources_pb2.DatabaseInstance, _Mapping]] = ...) -> None: ...

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

class SqlInstancesRescheduleMaintenanceRequest(_message.Message):
    __slots__ = ("instance", "project", "body")
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    instance: str
    project: str
    body: _cloud_sql_resources_pb2.SqlInstancesRescheduleMaintenanceRequestBody
    def __init__(self, instance: _Optional[str] = ..., project: _Optional[str] = ..., body: _Optional[_Union[_cloud_sql_resources_pb2.SqlInstancesRescheduleMaintenanceRequestBody, _Mapping]] = ...) -> None: ...

class SqlInstancesPerformDiskShrinkRequest(_message.Message):
    __slots__ = ("instance", "project", "body")
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    instance: str
    project: str
    body: _cloud_sql_resources_pb2.PerformDiskShrinkContext
    def __init__(self, instance: _Optional[str] = ..., project: _Optional[str] = ..., body: _Optional[_Union[_cloud_sql_resources_pb2.PerformDiskShrinkContext, _Mapping]] = ...) -> None: ...

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

class SqlOperationsGetRequest(_message.Message):
    __slots__ = ("operation", "project")
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    operation: str
    project: str
    def __init__(self, operation: _Optional[str] = ..., project: _Optional[str] = ...) -> None: ...

class SqlOperationsListRequest(_message.Message):
    __slots__ = ("instance", "max_results", "page_token", "project")
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    MAX_RESULTS_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    instance: str
    max_results: int
    page_token: str
    project: str
    def __init__(self, instance: _Optional[str] = ..., max_results: _Optional[int] = ..., page_token: _Optional[str] = ..., project: _Optional[str] = ...) -> None: ...

class SqlOperationsCancelRequest(_message.Message):
    __slots__ = ("operation", "project")
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    operation: str
    project: str
    def __init__(self, operation: _Optional[str] = ..., project: _Optional[str] = ...) -> None: ...

class SqlInstancesCreateEphemeralCertRequest(_message.Message):
    __slots__ = ("instance", "project", "body")
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    instance: str
    project: str
    body: _cloud_sql_resources_pb2.SslCertsCreateEphemeralRequest
    def __init__(self, instance: _Optional[str] = ..., project: _Optional[str] = ..., body: _Optional[_Union[_cloud_sql_resources_pb2.SslCertsCreateEphemeralRequest, _Mapping]] = ...) -> None: ...

class SqlSslCertsDeleteRequest(_message.Message):
    __slots__ = ("instance", "project", "sha1_fingerprint")
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    SHA1_FINGERPRINT_FIELD_NUMBER: _ClassVar[int]
    instance: str
    project: str
    sha1_fingerprint: str
    def __init__(self, instance: _Optional[str] = ..., project: _Optional[str] = ..., sha1_fingerprint: _Optional[str] = ...) -> None: ...

class SqlSslCertsGetRequest(_message.Message):
    __slots__ = ("instance", "project", "sha1_fingerprint")
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    SHA1_FINGERPRINT_FIELD_NUMBER: _ClassVar[int]
    instance: str
    project: str
    sha1_fingerprint: str
    def __init__(self, instance: _Optional[str] = ..., project: _Optional[str] = ..., sha1_fingerprint: _Optional[str] = ...) -> None: ...

class SqlSslCertsInsertRequest(_message.Message):
    __slots__ = ("instance", "project", "body")
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    instance: str
    project: str
    body: _cloud_sql_resources_pb2.SslCertsInsertRequest
    def __init__(self, instance: _Optional[str] = ..., project: _Optional[str] = ..., body: _Optional[_Union[_cloud_sql_resources_pb2.SslCertsInsertRequest, _Mapping]] = ...) -> None: ...

class SqlSslCertsListRequest(_message.Message):
    __slots__ = ("instance", "project")
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    instance: str
    project: str
    def __init__(self, instance: _Optional[str] = ..., project: _Optional[str] = ...) -> None: ...

class SqlInstancesGetDiskShrinkConfigRequest(_message.Message):
    __slots__ = ("instance", "project")
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    instance: str
    project: str
    def __init__(self, instance: _Optional[str] = ..., project: _Optional[str] = ...) -> None: ...

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

class SqlInstancesAcquireSsrsLeaseRequest(_message.Message):
    __slots__ = ("instance", "project", "body")
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    instance: str
    project: str
    body: _cloud_sql_resources_pb2.InstancesAcquireSsrsLeaseRequest
    def __init__(self, instance: _Optional[str] = ..., project: _Optional[str] = ..., body: _Optional[_Union[_cloud_sql_resources_pb2.InstancesAcquireSsrsLeaseRequest, _Mapping]] = ...) -> None: ...

class SqlInstancesAcquireSsrsLeaseResponse(_message.Message):
    __slots__ = ("operation_id",)
    OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    operation_id: str
    def __init__(self, operation_id: _Optional[str] = ...) -> None: ...
