from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.cloud.sql.v1 import cloud_sql_resources_pb2 as _cloud_sql_resources_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SqlBackupRunStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SQL_BACKUP_RUN_STATUS_UNSPECIFIED: _ClassVar[SqlBackupRunStatus]
    ENQUEUED: _ClassVar[SqlBackupRunStatus]
    OVERDUE: _ClassVar[SqlBackupRunStatus]
    RUNNING: _ClassVar[SqlBackupRunStatus]
    FAILED: _ClassVar[SqlBackupRunStatus]
    SUCCESSFUL: _ClassVar[SqlBackupRunStatus]
    SKIPPED: _ClassVar[SqlBackupRunStatus]
    DELETION_PENDING: _ClassVar[SqlBackupRunStatus]
    DELETION_FAILED: _ClassVar[SqlBackupRunStatus]
    DELETED: _ClassVar[SqlBackupRunStatus]

class SqlBackupKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SQL_BACKUP_KIND_UNSPECIFIED: _ClassVar[SqlBackupKind]
    SNAPSHOT: _ClassVar[SqlBackupKind]
    PHYSICAL: _ClassVar[SqlBackupKind]

class SqlBackupRunType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SQL_BACKUP_RUN_TYPE_UNSPECIFIED: _ClassVar[SqlBackupRunType]
    AUTOMATED: _ClassVar[SqlBackupRunType]
    ON_DEMAND: _ClassVar[SqlBackupRunType]
SQL_BACKUP_RUN_STATUS_UNSPECIFIED: SqlBackupRunStatus
ENQUEUED: SqlBackupRunStatus
OVERDUE: SqlBackupRunStatus
RUNNING: SqlBackupRunStatus
FAILED: SqlBackupRunStatus
SUCCESSFUL: SqlBackupRunStatus
SKIPPED: SqlBackupRunStatus
DELETION_PENDING: SqlBackupRunStatus
DELETION_FAILED: SqlBackupRunStatus
DELETED: SqlBackupRunStatus
SQL_BACKUP_KIND_UNSPECIFIED: SqlBackupKind
SNAPSHOT: SqlBackupKind
PHYSICAL: SqlBackupKind
SQL_BACKUP_RUN_TYPE_UNSPECIFIED: SqlBackupRunType
AUTOMATED: SqlBackupRunType
ON_DEMAND: SqlBackupRunType

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
    body: BackupRun
    def __init__(self, instance: _Optional[str] = ..., project: _Optional[str] = ..., body: _Optional[_Union[BackupRun, _Mapping]] = ...) -> None: ...

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

class BackupRun(_message.Message):
    __slots__ = ("kind", "status", "enqueued_time", "id", "start_time", "end_time", "error", "type", "description", "window_start_time", "instance", "self_link", "location", "disk_encryption_configuration", "disk_encryption_status", "backup_kind", "time_zone", "max_chargeable_bytes")
    KIND_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ENQUEUED_TIME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    WINDOW_START_TIME_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    SELF_LINK_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    DISK_ENCRYPTION_CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    DISK_ENCRYPTION_STATUS_FIELD_NUMBER: _ClassVar[int]
    BACKUP_KIND_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    MAX_CHARGEABLE_BYTES_FIELD_NUMBER: _ClassVar[int]
    kind: str
    status: SqlBackupRunStatus
    enqueued_time: _timestamp_pb2.Timestamp
    id: int
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    error: _cloud_sql_resources_pb2.OperationError
    type: SqlBackupRunType
    description: str
    window_start_time: _timestamp_pb2.Timestamp
    instance: str
    self_link: str
    location: str
    disk_encryption_configuration: _cloud_sql_resources_pb2.DiskEncryptionConfiguration
    disk_encryption_status: _cloud_sql_resources_pb2.DiskEncryptionStatus
    backup_kind: SqlBackupKind
    time_zone: str
    max_chargeable_bytes: int
    def __init__(self, kind: _Optional[str] = ..., status: _Optional[_Union[SqlBackupRunStatus, str]] = ..., enqueued_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., id: _Optional[int] = ..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., error: _Optional[_Union[_cloud_sql_resources_pb2.OperationError, _Mapping]] = ..., type: _Optional[_Union[SqlBackupRunType, str]] = ..., description: _Optional[str] = ..., window_start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., instance: _Optional[str] = ..., self_link: _Optional[str] = ..., location: _Optional[str] = ..., disk_encryption_configuration: _Optional[_Union[_cloud_sql_resources_pb2.DiskEncryptionConfiguration, _Mapping]] = ..., disk_encryption_status: _Optional[_Union[_cloud_sql_resources_pb2.DiskEncryptionStatus, _Mapping]] = ..., backup_kind: _Optional[_Union[SqlBackupKind, str]] = ..., time_zone: _Optional[str] = ..., max_chargeable_bytes: _Optional[int] = ...) -> None: ...

class BackupRunsListResponse(_message.Message):
    __slots__ = ("kind", "items", "next_page_token")
    KIND_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    kind: str
    items: _containers.RepeatedCompositeFieldContainer[BackupRun]
    next_page_token: str
    def __init__(self, kind: _Optional[str] = ..., items: _Optional[_Iterable[_Union[BackupRun, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...
