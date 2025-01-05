from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.bigtable.admin.v2 import common_pb2 as _common_pb2
from google.bigtable.admin.v2 import table_pb2 as _table_pb2
from google.iam.v1 import iam_policy_pb2 as _iam_policy_pb2
from google.iam.v1 import policy_pb2 as _policy_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class RestoreTableRequest(_message.Message):
    __slots__ = ('parent', 'table_id', 'backup')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TABLE_ID_FIELD_NUMBER: _ClassVar[int]
    BACKUP_FIELD_NUMBER: _ClassVar[int]
    parent: str
    table_id: str
    backup: str

    def __init__(self, parent: _Optional[str]=..., table_id: _Optional[str]=..., backup: _Optional[str]=...) -> None:
        ...

class RestoreTableMetadata(_message.Message):
    __slots__ = ('name', 'source_type', 'backup_info', 'optimize_table_operation_name', 'progress')
    NAME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    BACKUP_INFO_FIELD_NUMBER: _ClassVar[int]
    OPTIMIZE_TABLE_OPERATION_NAME_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    name: str
    source_type: _table_pb2.RestoreSourceType
    backup_info: _table_pb2.BackupInfo
    optimize_table_operation_name: str
    progress: _common_pb2.OperationProgress

    def __init__(self, name: _Optional[str]=..., source_type: _Optional[_Union[_table_pb2.RestoreSourceType, str]]=..., backup_info: _Optional[_Union[_table_pb2.BackupInfo, _Mapping]]=..., optimize_table_operation_name: _Optional[str]=..., progress: _Optional[_Union[_common_pb2.OperationProgress, _Mapping]]=...) -> None:
        ...

class OptimizeRestoredTableMetadata(_message.Message):
    __slots__ = ('name', 'progress')
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    name: str
    progress: _common_pb2.OperationProgress

    def __init__(self, name: _Optional[str]=..., progress: _Optional[_Union[_common_pb2.OperationProgress, _Mapping]]=...) -> None:
        ...

class CreateTableRequest(_message.Message):
    __slots__ = ('parent', 'table_id', 'table', 'initial_splits')

    class Split(_message.Message):
        __slots__ = ('key',)
        KEY_FIELD_NUMBER: _ClassVar[int]
        key: bytes

        def __init__(self, key: _Optional[bytes]=...) -> None:
            ...
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TABLE_ID_FIELD_NUMBER: _ClassVar[int]
    TABLE_FIELD_NUMBER: _ClassVar[int]
    INITIAL_SPLITS_FIELD_NUMBER: _ClassVar[int]
    parent: str
    table_id: str
    table: _table_pb2.Table
    initial_splits: _containers.RepeatedCompositeFieldContainer[CreateTableRequest.Split]

    def __init__(self, parent: _Optional[str]=..., table_id: _Optional[str]=..., table: _Optional[_Union[_table_pb2.Table, _Mapping]]=..., initial_splits: _Optional[_Iterable[_Union[CreateTableRequest.Split, _Mapping]]]=...) -> None:
        ...

class CreateTableFromSnapshotRequest(_message.Message):
    __slots__ = ('parent', 'table_id', 'source_snapshot')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TABLE_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    parent: str
    table_id: str
    source_snapshot: str

    def __init__(self, parent: _Optional[str]=..., table_id: _Optional[str]=..., source_snapshot: _Optional[str]=...) -> None:
        ...

class DropRowRangeRequest(_message.Message):
    __slots__ = ('name', 'row_key_prefix', 'delete_all_data_from_table')
    NAME_FIELD_NUMBER: _ClassVar[int]
    ROW_KEY_PREFIX_FIELD_NUMBER: _ClassVar[int]
    DELETE_ALL_DATA_FROM_TABLE_FIELD_NUMBER: _ClassVar[int]
    name: str
    row_key_prefix: bytes
    delete_all_data_from_table: bool

    def __init__(self, name: _Optional[str]=..., row_key_prefix: _Optional[bytes]=..., delete_all_data_from_table: bool=...) -> None:
        ...

class ListTablesRequest(_message.Message):
    __slots__ = ('parent', 'view', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    view: _table_pb2.Table.View
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., view: _Optional[_Union[_table_pb2.Table.View, str]]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListTablesResponse(_message.Message):
    __slots__ = ('tables', 'next_page_token')
    TABLES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    tables: _containers.RepeatedCompositeFieldContainer[_table_pb2.Table]
    next_page_token: str

    def __init__(self, tables: _Optional[_Iterable[_Union[_table_pb2.Table, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetTableRequest(_message.Message):
    __slots__ = ('name', 'view')
    NAME_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    name: str
    view: _table_pb2.Table.View

    def __init__(self, name: _Optional[str]=..., view: _Optional[_Union[_table_pb2.Table.View, str]]=...) -> None:
        ...

class UpdateTableRequest(_message.Message):
    __slots__ = ('table', 'update_mask')
    TABLE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    table: _table_pb2.Table
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, table: _Optional[_Union[_table_pb2.Table, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class UpdateTableMetadata(_message.Message):
    __slots__ = ('name', 'start_time', 'end_time')
    NAME_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class DeleteTableRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UndeleteTableRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UndeleteTableMetadata(_message.Message):
    __slots__ = ('name', 'start_time', 'end_time')
    NAME_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class ModifyColumnFamiliesRequest(_message.Message):
    __slots__ = ('name', 'modifications', 'ignore_warnings')

    class Modification(_message.Message):
        __slots__ = ('id', 'create', 'update', 'drop', 'update_mask')
        ID_FIELD_NUMBER: _ClassVar[int]
        CREATE_FIELD_NUMBER: _ClassVar[int]
        UPDATE_FIELD_NUMBER: _ClassVar[int]
        DROP_FIELD_NUMBER: _ClassVar[int]
        UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
        id: str
        create: _table_pb2.ColumnFamily
        update: _table_pb2.ColumnFamily
        drop: bool
        update_mask: _field_mask_pb2.FieldMask

        def __init__(self, id: _Optional[str]=..., create: _Optional[_Union[_table_pb2.ColumnFamily, _Mapping]]=..., update: _Optional[_Union[_table_pb2.ColumnFamily, _Mapping]]=..., drop: bool=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    MODIFICATIONS_FIELD_NUMBER: _ClassVar[int]
    IGNORE_WARNINGS_FIELD_NUMBER: _ClassVar[int]
    name: str
    modifications: _containers.RepeatedCompositeFieldContainer[ModifyColumnFamiliesRequest.Modification]
    ignore_warnings: bool

    def __init__(self, name: _Optional[str]=..., modifications: _Optional[_Iterable[_Union[ModifyColumnFamiliesRequest.Modification, _Mapping]]]=..., ignore_warnings: bool=...) -> None:
        ...

class GenerateConsistencyTokenRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class GenerateConsistencyTokenResponse(_message.Message):
    __slots__ = ('consistency_token',)
    CONSISTENCY_TOKEN_FIELD_NUMBER: _ClassVar[int]
    consistency_token: str

    def __init__(self, consistency_token: _Optional[str]=...) -> None:
        ...

class CheckConsistencyRequest(_message.Message):
    __slots__ = ('name', 'consistency_token', 'standard_read_remote_writes', 'data_boost_read_local_writes')
    NAME_FIELD_NUMBER: _ClassVar[int]
    CONSISTENCY_TOKEN_FIELD_NUMBER: _ClassVar[int]
    STANDARD_READ_REMOTE_WRITES_FIELD_NUMBER: _ClassVar[int]
    DATA_BOOST_READ_LOCAL_WRITES_FIELD_NUMBER: _ClassVar[int]
    name: str
    consistency_token: str
    standard_read_remote_writes: StandardReadRemoteWrites
    data_boost_read_local_writes: DataBoostReadLocalWrites

    def __init__(self, name: _Optional[str]=..., consistency_token: _Optional[str]=..., standard_read_remote_writes: _Optional[_Union[StandardReadRemoteWrites, _Mapping]]=..., data_boost_read_local_writes: _Optional[_Union[DataBoostReadLocalWrites, _Mapping]]=...) -> None:
        ...

class StandardReadRemoteWrites(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class DataBoostReadLocalWrites(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class CheckConsistencyResponse(_message.Message):
    __slots__ = ('consistent',)
    CONSISTENT_FIELD_NUMBER: _ClassVar[int]
    consistent: bool

    def __init__(self, consistent: bool=...) -> None:
        ...

class SnapshotTableRequest(_message.Message):
    __slots__ = ('name', 'cluster', 'snapshot_id', 'ttl', 'description')
    NAME_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_ID_FIELD_NUMBER: _ClassVar[int]
    TTL_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    name: str
    cluster: str
    snapshot_id: str
    ttl: _duration_pb2.Duration
    description: str

    def __init__(self, name: _Optional[str]=..., cluster: _Optional[str]=..., snapshot_id: _Optional[str]=..., ttl: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., description: _Optional[str]=...) -> None:
        ...

class GetSnapshotRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListSnapshotsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListSnapshotsResponse(_message.Message):
    __slots__ = ('snapshots', 'next_page_token')
    SNAPSHOTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    snapshots: _containers.RepeatedCompositeFieldContainer[_table_pb2.Snapshot]
    next_page_token: str

    def __init__(self, snapshots: _Optional[_Iterable[_Union[_table_pb2.Snapshot, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class DeleteSnapshotRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class SnapshotTableMetadata(_message.Message):
    __slots__ = ('original_request', 'request_time', 'finish_time')
    ORIGINAL_REQUEST_FIELD_NUMBER: _ClassVar[int]
    REQUEST_TIME_FIELD_NUMBER: _ClassVar[int]
    FINISH_TIME_FIELD_NUMBER: _ClassVar[int]
    original_request: SnapshotTableRequest
    request_time: _timestamp_pb2.Timestamp
    finish_time: _timestamp_pb2.Timestamp

    def __init__(self, original_request: _Optional[_Union[SnapshotTableRequest, _Mapping]]=..., request_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., finish_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class CreateTableFromSnapshotMetadata(_message.Message):
    __slots__ = ('original_request', 'request_time', 'finish_time')
    ORIGINAL_REQUEST_FIELD_NUMBER: _ClassVar[int]
    REQUEST_TIME_FIELD_NUMBER: _ClassVar[int]
    FINISH_TIME_FIELD_NUMBER: _ClassVar[int]
    original_request: CreateTableFromSnapshotRequest
    request_time: _timestamp_pb2.Timestamp
    finish_time: _timestamp_pb2.Timestamp

    def __init__(self, original_request: _Optional[_Union[CreateTableFromSnapshotRequest, _Mapping]]=..., request_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., finish_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class CreateBackupRequest(_message.Message):
    __slots__ = ('parent', 'backup_id', 'backup')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    BACKUP_ID_FIELD_NUMBER: _ClassVar[int]
    BACKUP_FIELD_NUMBER: _ClassVar[int]
    parent: str
    backup_id: str
    backup: _table_pb2.Backup

    def __init__(self, parent: _Optional[str]=..., backup_id: _Optional[str]=..., backup: _Optional[_Union[_table_pb2.Backup, _Mapping]]=...) -> None:
        ...

class CreateBackupMetadata(_message.Message):
    __slots__ = ('name', 'source_table', 'start_time', 'end_time')
    NAME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_TABLE_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    source_table: str
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., source_table: _Optional[str]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class UpdateBackupRequest(_message.Message):
    __slots__ = ('backup', 'update_mask')
    BACKUP_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    backup: _table_pb2.Backup
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, backup: _Optional[_Union[_table_pb2.Backup, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class GetBackupRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class DeleteBackupRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListBackupsRequest(_message.Message):
    __slots__ = ('parent', 'filter', 'order_by', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    order_by: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListBackupsResponse(_message.Message):
    __slots__ = ('backups', 'next_page_token')
    BACKUPS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    backups: _containers.RepeatedCompositeFieldContainer[_table_pb2.Backup]
    next_page_token: str

    def __init__(self, backups: _Optional[_Iterable[_Union[_table_pb2.Backup, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class CopyBackupRequest(_message.Message):
    __slots__ = ('parent', 'backup_id', 'source_backup', 'expire_time')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    BACKUP_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_BACKUP_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
    parent: str
    backup_id: str
    source_backup: str
    expire_time: _timestamp_pb2.Timestamp

    def __init__(self, parent: _Optional[str]=..., backup_id: _Optional[str]=..., source_backup: _Optional[str]=..., expire_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class CopyBackupMetadata(_message.Message):
    __slots__ = ('name', 'source_backup_info', 'progress')
    NAME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_BACKUP_INFO_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    name: str
    source_backup_info: _table_pb2.BackupInfo
    progress: _common_pb2.OperationProgress

    def __init__(self, name: _Optional[str]=..., source_backup_info: _Optional[_Union[_table_pb2.BackupInfo, _Mapping]]=..., progress: _Optional[_Union[_common_pb2.OperationProgress, _Mapping]]=...) -> None:
        ...

class CreateAuthorizedViewRequest(_message.Message):
    __slots__ = ('parent', 'authorized_view_id', 'authorized_view')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZED_VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZED_VIEW_FIELD_NUMBER: _ClassVar[int]
    parent: str
    authorized_view_id: str
    authorized_view: _table_pb2.AuthorizedView

    def __init__(self, parent: _Optional[str]=..., authorized_view_id: _Optional[str]=..., authorized_view: _Optional[_Union[_table_pb2.AuthorizedView, _Mapping]]=...) -> None:
        ...

class CreateAuthorizedViewMetadata(_message.Message):
    __slots__ = ('original_request', 'request_time', 'finish_time')
    ORIGINAL_REQUEST_FIELD_NUMBER: _ClassVar[int]
    REQUEST_TIME_FIELD_NUMBER: _ClassVar[int]
    FINISH_TIME_FIELD_NUMBER: _ClassVar[int]
    original_request: CreateAuthorizedViewRequest
    request_time: _timestamp_pb2.Timestamp
    finish_time: _timestamp_pb2.Timestamp

    def __init__(self, original_request: _Optional[_Union[CreateAuthorizedViewRequest, _Mapping]]=..., request_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., finish_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class ListAuthorizedViewsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'view')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    view: _table_pb2.AuthorizedView.ResponseView

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., view: _Optional[_Union[_table_pb2.AuthorizedView.ResponseView, str]]=...) -> None:
        ...

class ListAuthorizedViewsResponse(_message.Message):
    __slots__ = ('authorized_views', 'next_page_token')
    AUTHORIZED_VIEWS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    authorized_views: _containers.RepeatedCompositeFieldContainer[_table_pb2.AuthorizedView]
    next_page_token: str

    def __init__(self, authorized_views: _Optional[_Iterable[_Union[_table_pb2.AuthorizedView, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetAuthorizedViewRequest(_message.Message):
    __slots__ = ('name', 'view')
    NAME_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    name: str
    view: _table_pb2.AuthorizedView.ResponseView

    def __init__(self, name: _Optional[str]=..., view: _Optional[_Union[_table_pb2.AuthorizedView.ResponseView, str]]=...) -> None:
        ...

class UpdateAuthorizedViewRequest(_message.Message):
    __slots__ = ('authorized_view', 'update_mask', 'ignore_warnings')
    AUTHORIZED_VIEW_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    IGNORE_WARNINGS_FIELD_NUMBER: _ClassVar[int]
    authorized_view: _table_pb2.AuthorizedView
    update_mask: _field_mask_pb2.FieldMask
    ignore_warnings: bool

    def __init__(self, authorized_view: _Optional[_Union[_table_pb2.AuthorizedView, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., ignore_warnings: bool=...) -> None:
        ...

class UpdateAuthorizedViewMetadata(_message.Message):
    __slots__ = ('original_request', 'request_time', 'finish_time')
    ORIGINAL_REQUEST_FIELD_NUMBER: _ClassVar[int]
    REQUEST_TIME_FIELD_NUMBER: _ClassVar[int]
    FINISH_TIME_FIELD_NUMBER: _ClassVar[int]
    original_request: UpdateAuthorizedViewRequest
    request_time: _timestamp_pb2.Timestamp
    finish_time: _timestamp_pb2.Timestamp

    def __init__(self, original_request: _Optional[_Union[UpdateAuthorizedViewRequest, _Mapping]]=..., request_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., finish_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class DeleteAuthorizedViewRequest(_message.Message):
    __slots__ = ('name', 'etag')
    NAME_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    etag: str

    def __init__(self, name: _Optional[str]=..., etag: _Optional[str]=...) -> None:
        ...