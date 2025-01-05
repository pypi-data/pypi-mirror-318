from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.rpc import status_pb2 as _status_pb2
from google.spanner.admin.database.v1 import backup_pb2 as _backup_pb2
from google.spanner.admin.database.v1 import common_pb2 as _common_pb2
from google.spanner.admin.database.v1 import spanner_database_admin_pb2 as _spanner_database_admin_pb2
from google.spanner.admin.instance.v1 import spanner_instance_admin_pb2 as _spanner_instance_admin_pb2
from google.spanner.v1 import spanner_pb2 as _spanner_pb2
from google.spanner.v1 import commit_response_pb2 as _commit_response_pb2
from google.spanner.v1 import type_pb2 as _type_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SpannerAsyncActionRequest(_message.Message):
    __slots__ = ("action_id", "action")
    ACTION_ID_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    action_id: int
    action: SpannerAction
    def __init__(self, action_id: _Optional[int] = ..., action: _Optional[_Union[SpannerAction, _Mapping]] = ...) -> None: ...

class SpannerAsyncActionResponse(_message.Message):
    __slots__ = ("action_id", "outcome")
    ACTION_ID_FIELD_NUMBER: _ClassVar[int]
    OUTCOME_FIELD_NUMBER: _ClassVar[int]
    action_id: int
    outcome: SpannerActionOutcome
    def __init__(self, action_id: _Optional[int] = ..., outcome: _Optional[_Union[SpannerActionOutcome, _Mapping]] = ...) -> None: ...

class SpannerAction(_message.Message):
    __slots__ = ("database_path", "spanner_options", "start", "finish", "read", "query", "mutation", "dml", "batch_dml", "write", "partitioned_update", "admin", "start_batch_txn", "close_batch_txn", "generate_db_partitions_read", "generate_db_partitions_query", "execute_partition", "execute_change_stream_query", "query_cancellation")
    DATABASE_PATH_FIELD_NUMBER: _ClassVar[int]
    SPANNER_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    FINISH_FIELD_NUMBER: _ClassVar[int]
    READ_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    MUTATION_FIELD_NUMBER: _ClassVar[int]
    DML_FIELD_NUMBER: _ClassVar[int]
    BATCH_DML_FIELD_NUMBER: _ClassVar[int]
    WRITE_FIELD_NUMBER: _ClassVar[int]
    PARTITIONED_UPDATE_FIELD_NUMBER: _ClassVar[int]
    ADMIN_FIELD_NUMBER: _ClassVar[int]
    START_BATCH_TXN_FIELD_NUMBER: _ClassVar[int]
    CLOSE_BATCH_TXN_FIELD_NUMBER: _ClassVar[int]
    GENERATE_DB_PARTITIONS_READ_FIELD_NUMBER: _ClassVar[int]
    GENERATE_DB_PARTITIONS_QUERY_FIELD_NUMBER: _ClassVar[int]
    EXECUTE_PARTITION_FIELD_NUMBER: _ClassVar[int]
    EXECUTE_CHANGE_STREAM_QUERY_FIELD_NUMBER: _ClassVar[int]
    QUERY_CANCELLATION_FIELD_NUMBER: _ClassVar[int]
    database_path: str
    spanner_options: SpannerOptions
    start: StartTransactionAction
    finish: FinishTransactionAction
    read: ReadAction
    query: QueryAction
    mutation: MutationAction
    dml: DmlAction
    batch_dml: BatchDmlAction
    write: WriteMutationsAction
    partitioned_update: PartitionedUpdateAction
    admin: AdminAction
    start_batch_txn: StartBatchTransactionAction
    close_batch_txn: CloseBatchTransactionAction
    generate_db_partitions_read: GenerateDbPartitionsForReadAction
    generate_db_partitions_query: GenerateDbPartitionsForQueryAction
    execute_partition: ExecutePartitionAction
    execute_change_stream_query: ExecuteChangeStreamQuery
    query_cancellation: QueryCancellationAction
    def __init__(self, database_path: _Optional[str] = ..., spanner_options: _Optional[_Union[SpannerOptions, _Mapping]] = ..., start: _Optional[_Union[StartTransactionAction, _Mapping]] = ..., finish: _Optional[_Union[FinishTransactionAction, _Mapping]] = ..., read: _Optional[_Union[ReadAction, _Mapping]] = ..., query: _Optional[_Union[QueryAction, _Mapping]] = ..., mutation: _Optional[_Union[MutationAction, _Mapping]] = ..., dml: _Optional[_Union[DmlAction, _Mapping]] = ..., batch_dml: _Optional[_Union[BatchDmlAction, _Mapping]] = ..., write: _Optional[_Union[WriteMutationsAction, _Mapping]] = ..., partitioned_update: _Optional[_Union[PartitionedUpdateAction, _Mapping]] = ..., admin: _Optional[_Union[AdminAction, _Mapping]] = ..., start_batch_txn: _Optional[_Union[StartBatchTransactionAction, _Mapping]] = ..., close_batch_txn: _Optional[_Union[CloseBatchTransactionAction, _Mapping]] = ..., generate_db_partitions_read: _Optional[_Union[GenerateDbPartitionsForReadAction, _Mapping]] = ..., generate_db_partitions_query: _Optional[_Union[GenerateDbPartitionsForQueryAction, _Mapping]] = ..., execute_partition: _Optional[_Union[ExecutePartitionAction, _Mapping]] = ..., execute_change_stream_query: _Optional[_Union[ExecuteChangeStreamQuery, _Mapping]] = ..., query_cancellation: _Optional[_Union[QueryCancellationAction, _Mapping]] = ...) -> None: ...

class ReadAction(_message.Message):
    __slots__ = ("table", "index", "column", "keys", "limit")
    TABLE_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    COLUMN_FIELD_NUMBER: _ClassVar[int]
    KEYS_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    table: str
    index: str
    column: _containers.RepeatedScalarFieldContainer[str]
    keys: KeySet
    limit: int
    def __init__(self, table: _Optional[str] = ..., index: _Optional[str] = ..., column: _Optional[_Iterable[str]] = ..., keys: _Optional[_Union[KeySet, _Mapping]] = ..., limit: _Optional[int] = ...) -> None: ...

class QueryAction(_message.Message):
    __slots__ = ("sql", "params")
    class Parameter(_message.Message):
        __slots__ = ("name", "type", "value")
        NAME_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        name: str
        type: _type_pb2.Type
        value: Value
        def __init__(self, name: _Optional[str] = ..., type: _Optional[_Union[_type_pb2.Type, _Mapping]] = ..., value: _Optional[_Union[Value, _Mapping]] = ...) -> None: ...
    SQL_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    sql: str
    params: _containers.RepeatedCompositeFieldContainer[QueryAction.Parameter]
    def __init__(self, sql: _Optional[str] = ..., params: _Optional[_Iterable[_Union[QueryAction.Parameter, _Mapping]]] = ...) -> None: ...

class DmlAction(_message.Message):
    __slots__ = ("update", "autocommit_if_supported")
    UPDATE_FIELD_NUMBER: _ClassVar[int]
    AUTOCOMMIT_IF_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    update: QueryAction
    autocommit_if_supported: bool
    def __init__(self, update: _Optional[_Union[QueryAction, _Mapping]] = ..., autocommit_if_supported: bool = ...) -> None: ...

class BatchDmlAction(_message.Message):
    __slots__ = ("updates",)
    UPDATES_FIELD_NUMBER: _ClassVar[int]
    updates: _containers.RepeatedCompositeFieldContainer[QueryAction]
    def __init__(self, updates: _Optional[_Iterable[_Union[QueryAction, _Mapping]]] = ...) -> None: ...

class Value(_message.Message):
    __slots__ = ("is_null", "int_value", "bool_value", "double_value", "bytes_value", "string_value", "struct_value", "timestamp_value", "date_days_value", "is_commit_timestamp", "array_value", "array_type")
    IS_NULL_FIELD_NUMBER: _ClassVar[int]
    INT_VALUE_FIELD_NUMBER: _ClassVar[int]
    BOOL_VALUE_FIELD_NUMBER: _ClassVar[int]
    DOUBLE_VALUE_FIELD_NUMBER: _ClassVar[int]
    BYTES_VALUE_FIELD_NUMBER: _ClassVar[int]
    STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
    STRUCT_VALUE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_VALUE_FIELD_NUMBER: _ClassVar[int]
    DATE_DAYS_VALUE_FIELD_NUMBER: _ClassVar[int]
    IS_COMMIT_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ARRAY_VALUE_FIELD_NUMBER: _ClassVar[int]
    ARRAY_TYPE_FIELD_NUMBER: _ClassVar[int]
    is_null: bool
    int_value: int
    bool_value: bool
    double_value: float
    bytes_value: bytes
    string_value: str
    struct_value: ValueList
    timestamp_value: _timestamp_pb2.Timestamp
    date_days_value: int
    is_commit_timestamp: bool
    array_value: ValueList
    array_type: _type_pb2.Type
    def __init__(self, is_null: bool = ..., int_value: _Optional[int] = ..., bool_value: bool = ..., double_value: _Optional[float] = ..., bytes_value: _Optional[bytes] = ..., string_value: _Optional[str] = ..., struct_value: _Optional[_Union[ValueList, _Mapping]] = ..., timestamp_value: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., date_days_value: _Optional[int] = ..., is_commit_timestamp: bool = ..., array_value: _Optional[_Union[ValueList, _Mapping]] = ..., array_type: _Optional[_Union[_type_pb2.Type, _Mapping]] = ...) -> None: ...

class KeyRange(_message.Message):
    __slots__ = ("start", "limit", "type")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[KeyRange.Type]
        CLOSED_CLOSED: _ClassVar[KeyRange.Type]
        CLOSED_OPEN: _ClassVar[KeyRange.Type]
        OPEN_CLOSED: _ClassVar[KeyRange.Type]
        OPEN_OPEN: _ClassVar[KeyRange.Type]
    TYPE_UNSPECIFIED: KeyRange.Type
    CLOSED_CLOSED: KeyRange.Type
    CLOSED_OPEN: KeyRange.Type
    OPEN_CLOSED: KeyRange.Type
    OPEN_OPEN: KeyRange.Type
    START_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    start: ValueList
    limit: ValueList
    type: KeyRange.Type
    def __init__(self, start: _Optional[_Union[ValueList, _Mapping]] = ..., limit: _Optional[_Union[ValueList, _Mapping]] = ..., type: _Optional[_Union[KeyRange.Type, str]] = ...) -> None: ...

class KeySet(_message.Message):
    __slots__ = ("point", "range", "all")
    POINT_FIELD_NUMBER: _ClassVar[int]
    RANGE_FIELD_NUMBER: _ClassVar[int]
    ALL_FIELD_NUMBER: _ClassVar[int]
    point: _containers.RepeatedCompositeFieldContainer[ValueList]
    range: _containers.RepeatedCompositeFieldContainer[KeyRange]
    all: bool
    def __init__(self, point: _Optional[_Iterable[_Union[ValueList, _Mapping]]] = ..., range: _Optional[_Iterable[_Union[KeyRange, _Mapping]]] = ..., all: bool = ...) -> None: ...

class ValueList(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: _containers.RepeatedCompositeFieldContainer[Value]
    def __init__(self, value: _Optional[_Iterable[_Union[Value, _Mapping]]] = ...) -> None: ...

class MutationAction(_message.Message):
    __slots__ = ("mod",)
    class InsertArgs(_message.Message):
        __slots__ = ("column", "type", "values")
        COLUMN_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        VALUES_FIELD_NUMBER: _ClassVar[int]
        column: _containers.RepeatedScalarFieldContainer[str]
        type: _containers.RepeatedCompositeFieldContainer[_type_pb2.Type]
        values: _containers.RepeatedCompositeFieldContainer[ValueList]
        def __init__(self, column: _Optional[_Iterable[str]] = ..., type: _Optional[_Iterable[_Union[_type_pb2.Type, _Mapping]]] = ..., values: _Optional[_Iterable[_Union[ValueList, _Mapping]]] = ...) -> None: ...
    class UpdateArgs(_message.Message):
        __slots__ = ("column", "type", "values")
        COLUMN_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        VALUES_FIELD_NUMBER: _ClassVar[int]
        column: _containers.RepeatedScalarFieldContainer[str]
        type: _containers.RepeatedCompositeFieldContainer[_type_pb2.Type]
        values: _containers.RepeatedCompositeFieldContainer[ValueList]
        def __init__(self, column: _Optional[_Iterable[str]] = ..., type: _Optional[_Iterable[_Union[_type_pb2.Type, _Mapping]]] = ..., values: _Optional[_Iterable[_Union[ValueList, _Mapping]]] = ...) -> None: ...
    class Mod(_message.Message):
        __slots__ = ("table", "insert", "update", "insert_or_update", "replace", "delete_keys")
        TABLE_FIELD_NUMBER: _ClassVar[int]
        INSERT_FIELD_NUMBER: _ClassVar[int]
        UPDATE_FIELD_NUMBER: _ClassVar[int]
        INSERT_OR_UPDATE_FIELD_NUMBER: _ClassVar[int]
        REPLACE_FIELD_NUMBER: _ClassVar[int]
        DELETE_KEYS_FIELD_NUMBER: _ClassVar[int]
        table: str
        insert: MutationAction.InsertArgs
        update: MutationAction.UpdateArgs
        insert_or_update: MutationAction.InsertArgs
        replace: MutationAction.InsertArgs
        delete_keys: KeySet
        def __init__(self, table: _Optional[str] = ..., insert: _Optional[_Union[MutationAction.InsertArgs, _Mapping]] = ..., update: _Optional[_Union[MutationAction.UpdateArgs, _Mapping]] = ..., insert_or_update: _Optional[_Union[MutationAction.InsertArgs, _Mapping]] = ..., replace: _Optional[_Union[MutationAction.InsertArgs, _Mapping]] = ..., delete_keys: _Optional[_Union[KeySet, _Mapping]] = ...) -> None: ...
    MOD_FIELD_NUMBER: _ClassVar[int]
    mod: _containers.RepeatedCompositeFieldContainer[MutationAction.Mod]
    def __init__(self, mod: _Optional[_Iterable[_Union[MutationAction.Mod, _Mapping]]] = ...) -> None: ...

class WriteMutationsAction(_message.Message):
    __slots__ = ("mutation",)
    MUTATION_FIELD_NUMBER: _ClassVar[int]
    mutation: MutationAction
    def __init__(self, mutation: _Optional[_Union[MutationAction, _Mapping]] = ...) -> None: ...

class PartitionedUpdateAction(_message.Message):
    __slots__ = ("options", "update")
    class ExecutePartitionedUpdateOptions(_message.Message):
        __slots__ = ("rpc_priority", "tag")
        RPC_PRIORITY_FIELD_NUMBER: _ClassVar[int]
        TAG_FIELD_NUMBER: _ClassVar[int]
        rpc_priority: _spanner_pb2.RequestOptions.Priority
        tag: str
        def __init__(self, rpc_priority: _Optional[_Union[_spanner_pb2.RequestOptions.Priority, str]] = ..., tag: _Optional[str] = ...) -> None: ...
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_FIELD_NUMBER: _ClassVar[int]
    options: PartitionedUpdateAction.ExecutePartitionedUpdateOptions
    update: QueryAction
    def __init__(self, options: _Optional[_Union[PartitionedUpdateAction.ExecutePartitionedUpdateOptions, _Mapping]] = ..., update: _Optional[_Union[QueryAction, _Mapping]] = ...) -> None: ...

class StartTransactionAction(_message.Message):
    __slots__ = ("concurrency", "table", "transaction_seed", "execution_options")
    CONCURRENCY_FIELD_NUMBER: _ClassVar[int]
    TABLE_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_SEED_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    concurrency: Concurrency
    table: _containers.RepeatedCompositeFieldContainer[TableMetadata]
    transaction_seed: str
    execution_options: TransactionExecutionOptions
    def __init__(self, concurrency: _Optional[_Union[Concurrency, _Mapping]] = ..., table: _Optional[_Iterable[_Union[TableMetadata, _Mapping]]] = ..., transaction_seed: _Optional[str] = ..., execution_options: _Optional[_Union[TransactionExecutionOptions, _Mapping]] = ...) -> None: ...

class Concurrency(_message.Message):
    __slots__ = ("staleness_seconds", "min_read_timestamp_micros", "max_staleness_seconds", "exact_timestamp_micros", "strong", "batch", "snapshot_epoch_read", "snapshot_epoch_root_table", "batch_read_timestamp_micros")
    STALENESS_SECONDS_FIELD_NUMBER: _ClassVar[int]
    MIN_READ_TIMESTAMP_MICROS_FIELD_NUMBER: _ClassVar[int]
    MAX_STALENESS_SECONDS_FIELD_NUMBER: _ClassVar[int]
    EXACT_TIMESTAMP_MICROS_FIELD_NUMBER: _ClassVar[int]
    STRONG_FIELD_NUMBER: _ClassVar[int]
    BATCH_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_EPOCH_READ_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_EPOCH_ROOT_TABLE_FIELD_NUMBER: _ClassVar[int]
    BATCH_READ_TIMESTAMP_MICROS_FIELD_NUMBER: _ClassVar[int]
    staleness_seconds: float
    min_read_timestamp_micros: int
    max_staleness_seconds: float
    exact_timestamp_micros: int
    strong: bool
    batch: bool
    snapshot_epoch_read: bool
    snapshot_epoch_root_table: str
    batch_read_timestamp_micros: int
    def __init__(self, staleness_seconds: _Optional[float] = ..., min_read_timestamp_micros: _Optional[int] = ..., max_staleness_seconds: _Optional[float] = ..., exact_timestamp_micros: _Optional[int] = ..., strong: bool = ..., batch: bool = ..., snapshot_epoch_read: bool = ..., snapshot_epoch_root_table: _Optional[str] = ..., batch_read_timestamp_micros: _Optional[int] = ...) -> None: ...

class TableMetadata(_message.Message):
    __slots__ = ("name", "column", "key_column")
    NAME_FIELD_NUMBER: _ClassVar[int]
    COLUMN_FIELD_NUMBER: _ClassVar[int]
    KEY_COLUMN_FIELD_NUMBER: _ClassVar[int]
    name: str
    column: _containers.RepeatedCompositeFieldContainer[ColumnMetadata]
    key_column: _containers.RepeatedCompositeFieldContainer[ColumnMetadata]
    def __init__(self, name: _Optional[str] = ..., column: _Optional[_Iterable[_Union[ColumnMetadata, _Mapping]]] = ..., key_column: _Optional[_Iterable[_Union[ColumnMetadata, _Mapping]]] = ...) -> None: ...

class ColumnMetadata(_message.Message):
    __slots__ = ("name", "type")
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: _type_pb2.Type
    def __init__(self, name: _Optional[str] = ..., type: _Optional[_Union[_type_pb2.Type, _Mapping]] = ...) -> None: ...

class TransactionExecutionOptions(_message.Message):
    __slots__ = ("optimistic",)
    OPTIMISTIC_FIELD_NUMBER: _ClassVar[int]
    optimistic: bool
    def __init__(self, optimistic: bool = ...) -> None: ...

class FinishTransactionAction(_message.Message):
    __slots__ = ("mode",)
    class Mode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MODE_UNSPECIFIED: _ClassVar[FinishTransactionAction.Mode]
        COMMIT: _ClassVar[FinishTransactionAction.Mode]
        ABANDON: _ClassVar[FinishTransactionAction.Mode]
    MODE_UNSPECIFIED: FinishTransactionAction.Mode
    COMMIT: FinishTransactionAction.Mode
    ABANDON: FinishTransactionAction.Mode
    MODE_FIELD_NUMBER: _ClassVar[int]
    mode: FinishTransactionAction.Mode
    def __init__(self, mode: _Optional[_Union[FinishTransactionAction.Mode, str]] = ...) -> None: ...

class AdminAction(_message.Message):
    __slots__ = ("create_user_instance_config", "update_user_instance_config", "delete_user_instance_config", "get_cloud_instance_config", "list_instance_configs", "create_cloud_instance", "update_cloud_instance", "delete_cloud_instance", "list_cloud_instances", "get_cloud_instance", "create_cloud_database", "update_cloud_database_ddl", "update_cloud_database", "drop_cloud_database", "list_cloud_databases", "list_cloud_database_operations", "restore_cloud_database", "get_cloud_database", "create_cloud_backup", "copy_cloud_backup", "get_cloud_backup", "update_cloud_backup", "delete_cloud_backup", "list_cloud_backups", "list_cloud_backup_operations", "get_operation", "cancel_operation", "change_quorum_cloud_database")
    CREATE_USER_INSTANCE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    UPDATE_USER_INSTANCE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DELETE_USER_INSTANCE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    GET_CLOUD_INSTANCE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    LIST_INSTANCE_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    CREATE_CLOUD_INSTANCE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_CLOUD_INSTANCE_FIELD_NUMBER: _ClassVar[int]
    DELETE_CLOUD_INSTANCE_FIELD_NUMBER: _ClassVar[int]
    LIST_CLOUD_INSTANCES_FIELD_NUMBER: _ClassVar[int]
    GET_CLOUD_INSTANCE_FIELD_NUMBER: _ClassVar[int]
    CREATE_CLOUD_DATABASE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_CLOUD_DATABASE_DDL_FIELD_NUMBER: _ClassVar[int]
    UPDATE_CLOUD_DATABASE_FIELD_NUMBER: _ClassVar[int]
    DROP_CLOUD_DATABASE_FIELD_NUMBER: _ClassVar[int]
    LIST_CLOUD_DATABASES_FIELD_NUMBER: _ClassVar[int]
    LIST_CLOUD_DATABASE_OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    RESTORE_CLOUD_DATABASE_FIELD_NUMBER: _ClassVar[int]
    GET_CLOUD_DATABASE_FIELD_NUMBER: _ClassVar[int]
    CREATE_CLOUD_BACKUP_FIELD_NUMBER: _ClassVar[int]
    COPY_CLOUD_BACKUP_FIELD_NUMBER: _ClassVar[int]
    GET_CLOUD_BACKUP_FIELD_NUMBER: _ClassVar[int]
    UPDATE_CLOUD_BACKUP_FIELD_NUMBER: _ClassVar[int]
    DELETE_CLOUD_BACKUP_FIELD_NUMBER: _ClassVar[int]
    LIST_CLOUD_BACKUPS_FIELD_NUMBER: _ClassVar[int]
    LIST_CLOUD_BACKUP_OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    GET_OPERATION_FIELD_NUMBER: _ClassVar[int]
    CANCEL_OPERATION_FIELD_NUMBER: _ClassVar[int]
    CHANGE_QUORUM_CLOUD_DATABASE_FIELD_NUMBER: _ClassVar[int]
    create_user_instance_config: CreateUserInstanceConfigAction
    update_user_instance_config: UpdateUserInstanceConfigAction
    delete_user_instance_config: DeleteUserInstanceConfigAction
    get_cloud_instance_config: GetCloudInstanceConfigAction
    list_instance_configs: ListCloudInstanceConfigsAction
    create_cloud_instance: CreateCloudInstanceAction
    update_cloud_instance: UpdateCloudInstanceAction
    delete_cloud_instance: DeleteCloudInstanceAction
    list_cloud_instances: ListCloudInstancesAction
    get_cloud_instance: GetCloudInstanceAction
    create_cloud_database: CreateCloudDatabaseAction
    update_cloud_database_ddl: UpdateCloudDatabaseDdlAction
    update_cloud_database: UpdateCloudDatabaseAction
    drop_cloud_database: DropCloudDatabaseAction
    list_cloud_databases: ListCloudDatabasesAction
    list_cloud_database_operations: ListCloudDatabaseOperationsAction
    restore_cloud_database: RestoreCloudDatabaseAction
    get_cloud_database: GetCloudDatabaseAction
    create_cloud_backup: CreateCloudBackupAction
    copy_cloud_backup: CopyCloudBackupAction
    get_cloud_backup: GetCloudBackupAction
    update_cloud_backup: UpdateCloudBackupAction
    delete_cloud_backup: DeleteCloudBackupAction
    list_cloud_backups: ListCloudBackupsAction
    list_cloud_backup_operations: ListCloudBackupOperationsAction
    get_operation: GetOperationAction
    cancel_operation: CancelOperationAction
    change_quorum_cloud_database: ChangeQuorumCloudDatabaseAction
    def __init__(self, create_user_instance_config: _Optional[_Union[CreateUserInstanceConfigAction, _Mapping]] = ..., update_user_instance_config: _Optional[_Union[UpdateUserInstanceConfigAction, _Mapping]] = ..., delete_user_instance_config: _Optional[_Union[DeleteUserInstanceConfigAction, _Mapping]] = ..., get_cloud_instance_config: _Optional[_Union[GetCloudInstanceConfigAction, _Mapping]] = ..., list_instance_configs: _Optional[_Union[ListCloudInstanceConfigsAction, _Mapping]] = ..., create_cloud_instance: _Optional[_Union[CreateCloudInstanceAction, _Mapping]] = ..., update_cloud_instance: _Optional[_Union[UpdateCloudInstanceAction, _Mapping]] = ..., delete_cloud_instance: _Optional[_Union[DeleteCloudInstanceAction, _Mapping]] = ..., list_cloud_instances: _Optional[_Union[ListCloudInstancesAction, _Mapping]] = ..., get_cloud_instance: _Optional[_Union[GetCloudInstanceAction, _Mapping]] = ..., create_cloud_database: _Optional[_Union[CreateCloudDatabaseAction, _Mapping]] = ..., update_cloud_database_ddl: _Optional[_Union[UpdateCloudDatabaseDdlAction, _Mapping]] = ..., update_cloud_database: _Optional[_Union[UpdateCloudDatabaseAction, _Mapping]] = ..., drop_cloud_database: _Optional[_Union[DropCloudDatabaseAction, _Mapping]] = ..., list_cloud_databases: _Optional[_Union[ListCloudDatabasesAction, _Mapping]] = ..., list_cloud_database_operations: _Optional[_Union[ListCloudDatabaseOperationsAction, _Mapping]] = ..., restore_cloud_database: _Optional[_Union[RestoreCloudDatabaseAction, _Mapping]] = ..., get_cloud_database: _Optional[_Union[GetCloudDatabaseAction, _Mapping]] = ..., create_cloud_backup: _Optional[_Union[CreateCloudBackupAction, _Mapping]] = ..., copy_cloud_backup: _Optional[_Union[CopyCloudBackupAction, _Mapping]] = ..., get_cloud_backup: _Optional[_Union[GetCloudBackupAction, _Mapping]] = ..., update_cloud_backup: _Optional[_Union[UpdateCloudBackupAction, _Mapping]] = ..., delete_cloud_backup: _Optional[_Union[DeleteCloudBackupAction, _Mapping]] = ..., list_cloud_backups: _Optional[_Union[ListCloudBackupsAction, _Mapping]] = ..., list_cloud_backup_operations: _Optional[_Union[ListCloudBackupOperationsAction, _Mapping]] = ..., get_operation: _Optional[_Union[GetOperationAction, _Mapping]] = ..., cancel_operation: _Optional[_Union[CancelOperationAction, _Mapping]] = ..., change_quorum_cloud_database: _Optional[_Union[ChangeQuorumCloudDatabaseAction, _Mapping]] = ...) -> None: ...

class CreateUserInstanceConfigAction(_message.Message):
    __slots__ = ("user_config_id", "project_id", "base_config_id", "replicas")
    USER_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    BASE_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    REPLICAS_FIELD_NUMBER: _ClassVar[int]
    user_config_id: str
    project_id: str
    base_config_id: str
    replicas: _containers.RepeatedCompositeFieldContainer[_spanner_instance_admin_pb2.ReplicaInfo]
    def __init__(self, user_config_id: _Optional[str] = ..., project_id: _Optional[str] = ..., base_config_id: _Optional[str] = ..., replicas: _Optional[_Iterable[_Union[_spanner_instance_admin_pb2.ReplicaInfo, _Mapping]]] = ...) -> None: ...

class UpdateUserInstanceConfigAction(_message.Message):
    __slots__ = ("user_config_id", "project_id", "display_name", "labels")
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    USER_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    user_config_id: str
    project_id: str
    display_name: str
    labels: _containers.ScalarMap[str, str]
    def __init__(self, user_config_id: _Optional[str] = ..., project_id: _Optional[str] = ..., display_name: _Optional[str] = ..., labels: _Optional[_Mapping[str, str]] = ...) -> None: ...

class GetCloudInstanceConfigAction(_message.Message):
    __slots__ = ("instance_config_id", "project_id")
    INSTANCE_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    instance_config_id: str
    project_id: str
    def __init__(self, instance_config_id: _Optional[str] = ..., project_id: _Optional[str] = ...) -> None: ...

class DeleteUserInstanceConfigAction(_message.Message):
    __slots__ = ("user_config_id", "project_id")
    USER_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    user_config_id: str
    project_id: str
    def __init__(self, user_config_id: _Optional[str] = ..., project_id: _Optional[str] = ...) -> None: ...

class ListCloudInstanceConfigsAction(_message.Message):
    __slots__ = ("project_id", "page_size", "page_token")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    page_size: int
    page_token: str
    def __init__(self, project_id: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class CreateCloudInstanceAction(_message.Message):
    __slots__ = ("instance_id", "project_id", "instance_config_id", "node_count", "processing_units", "autoscaling_config", "labels")
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_COUNT_FIELD_NUMBER: _ClassVar[int]
    PROCESSING_UNITS_FIELD_NUMBER: _ClassVar[int]
    AUTOSCALING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    instance_id: str
    project_id: str
    instance_config_id: str
    node_count: int
    processing_units: int
    autoscaling_config: _spanner_instance_admin_pb2.AutoscalingConfig
    labels: _containers.ScalarMap[str, str]
    def __init__(self, instance_id: _Optional[str] = ..., project_id: _Optional[str] = ..., instance_config_id: _Optional[str] = ..., node_count: _Optional[int] = ..., processing_units: _Optional[int] = ..., autoscaling_config: _Optional[_Union[_spanner_instance_admin_pb2.AutoscalingConfig, _Mapping]] = ..., labels: _Optional[_Mapping[str, str]] = ...) -> None: ...

class UpdateCloudInstanceAction(_message.Message):
    __slots__ = ("instance_id", "project_id", "display_name", "node_count", "processing_units", "autoscaling_config", "labels")
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    NODE_COUNT_FIELD_NUMBER: _ClassVar[int]
    PROCESSING_UNITS_FIELD_NUMBER: _ClassVar[int]
    AUTOSCALING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    instance_id: str
    project_id: str
    display_name: str
    node_count: int
    processing_units: int
    autoscaling_config: _spanner_instance_admin_pb2.AutoscalingConfig
    labels: _containers.ScalarMap[str, str]
    def __init__(self, instance_id: _Optional[str] = ..., project_id: _Optional[str] = ..., display_name: _Optional[str] = ..., node_count: _Optional[int] = ..., processing_units: _Optional[int] = ..., autoscaling_config: _Optional[_Union[_spanner_instance_admin_pb2.AutoscalingConfig, _Mapping]] = ..., labels: _Optional[_Mapping[str, str]] = ...) -> None: ...

class DeleteCloudInstanceAction(_message.Message):
    __slots__ = ("instance_id", "project_id")
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    instance_id: str
    project_id: str
    def __init__(self, instance_id: _Optional[str] = ..., project_id: _Optional[str] = ...) -> None: ...

class CreateCloudDatabaseAction(_message.Message):
    __slots__ = ("instance_id", "project_id", "database_id", "sdl_statement", "encryption_config", "dialect", "proto_descriptors")
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    DATABASE_ID_FIELD_NUMBER: _ClassVar[int]
    SDL_STATEMENT_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DIALECT_FIELD_NUMBER: _ClassVar[int]
    PROTO_DESCRIPTORS_FIELD_NUMBER: _ClassVar[int]
    instance_id: str
    project_id: str
    database_id: str
    sdl_statement: _containers.RepeatedScalarFieldContainer[str]
    encryption_config: _common_pb2.EncryptionConfig
    dialect: str
    proto_descriptors: bytes
    def __init__(self, instance_id: _Optional[str] = ..., project_id: _Optional[str] = ..., database_id: _Optional[str] = ..., sdl_statement: _Optional[_Iterable[str]] = ..., encryption_config: _Optional[_Union[_common_pb2.EncryptionConfig, _Mapping]] = ..., dialect: _Optional[str] = ..., proto_descriptors: _Optional[bytes] = ...) -> None: ...

class UpdateCloudDatabaseDdlAction(_message.Message):
    __slots__ = ("instance_id", "project_id", "database_id", "sdl_statement", "operation_id", "proto_descriptors")
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    DATABASE_ID_FIELD_NUMBER: _ClassVar[int]
    SDL_STATEMENT_FIELD_NUMBER: _ClassVar[int]
    OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    PROTO_DESCRIPTORS_FIELD_NUMBER: _ClassVar[int]
    instance_id: str
    project_id: str
    database_id: str
    sdl_statement: _containers.RepeatedScalarFieldContainer[str]
    operation_id: str
    proto_descriptors: bytes
    def __init__(self, instance_id: _Optional[str] = ..., project_id: _Optional[str] = ..., database_id: _Optional[str] = ..., sdl_statement: _Optional[_Iterable[str]] = ..., operation_id: _Optional[str] = ..., proto_descriptors: _Optional[bytes] = ...) -> None: ...

class UpdateCloudDatabaseAction(_message.Message):
    __slots__ = ("instance_id", "project_id", "database_name", "enable_drop_protection")
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    DATABASE_NAME_FIELD_NUMBER: _ClassVar[int]
    ENABLE_DROP_PROTECTION_FIELD_NUMBER: _ClassVar[int]
    instance_id: str
    project_id: str
    database_name: str
    enable_drop_protection: bool
    def __init__(self, instance_id: _Optional[str] = ..., project_id: _Optional[str] = ..., database_name: _Optional[str] = ..., enable_drop_protection: bool = ...) -> None: ...

class DropCloudDatabaseAction(_message.Message):
    __slots__ = ("instance_id", "project_id", "database_id")
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    DATABASE_ID_FIELD_NUMBER: _ClassVar[int]
    instance_id: str
    project_id: str
    database_id: str
    def __init__(self, instance_id: _Optional[str] = ..., project_id: _Optional[str] = ..., database_id: _Optional[str] = ...) -> None: ...

class ChangeQuorumCloudDatabaseAction(_message.Message):
    __slots__ = ("database_uri", "serving_locations")
    DATABASE_URI_FIELD_NUMBER: _ClassVar[int]
    SERVING_LOCATIONS_FIELD_NUMBER: _ClassVar[int]
    database_uri: str
    serving_locations: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, database_uri: _Optional[str] = ..., serving_locations: _Optional[_Iterable[str]] = ...) -> None: ...

class ListCloudDatabasesAction(_message.Message):
    __slots__ = ("project_id", "instance_id", "page_size", "page_token")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    instance_id: str
    page_size: int
    page_token: str
    def __init__(self, project_id: _Optional[str] = ..., instance_id: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListCloudInstancesAction(_message.Message):
    __slots__ = ("project_id", "filter", "page_size", "page_token")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    filter: str
    page_size: int
    page_token: str
    def __init__(self, project_id: _Optional[str] = ..., filter: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class GetCloudInstanceAction(_message.Message):
    __slots__ = ("project_id", "instance_id")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    instance_id: str
    def __init__(self, project_id: _Optional[str] = ..., instance_id: _Optional[str] = ...) -> None: ...

class ListCloudDatabaseOperationsAction(_message.Message):
    __slots__ = ("project_id", "instance_id", "filter", "page_size", "page_token")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    instance_id: str
    filter: str
    page_size: int
    page_token: str
    def __init__(self, project_id: _Optional[str] = ..., instance_id: _Optional[str] = ..., filter: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class RestoreCloudDatabaseAction(_message.Message):
    __slots__ = ("project_id", "backup_instance_id", "backup_id", "database_instance_id", "database_id", "encryption_config")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    BACKUP_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    BACKUP_ID_FIELD_NUMBER: _ClassVar[int]
    DATABASE_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    DATABASE_ID_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    backup_instance_id: str
    backup_id: str
    database_instance_id: str
    database_id: str
    encryption_config: _common_pb2.EncryptionConfig
    def __init__(self, project_id: _Optional[str] = ..., backup_instance_id: _Optional[str] = ..., backup_id: _Optional[str] = ..., database_instance_id: _Optional[str] = ..., database_id: _Optional[str] = ..., encryption_config: _Optional[_Union[_common_pb2.EncryptionConfig, _Mapping]] = ...) -> None: ...

class GetCloudDatabaseAction(_message.Message):
    __slots__ = ("project_id", "instance_id", "database_id")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    DATABASE_ID_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    instance_id: str
    database_id: str
    def __init__(self, project_id: _Optional[str] = ..., instance_id: _Optional[str] = ..., database_id: _Optional[str] = ...) -> None: ...

class CreateCloudBackupAction(_message.Message):
    __slots__ = ("project_id", "instance_id", "backup_id", "database_id", "expire_time", "version_time", "encryption_config")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    BACKUP_ID_FIELD_NUMBER: _ClassVar[int]
    DATABASE_ID_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
    VERSION_TIME_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    instance_id: str
    backup_id: str
    database_id: str
    expire_time: _timestamp_pb2.Timestamp
    version_time: _timestamp_pb2.Timestamp
    encryption_config: _common_pb2.EncryptionConfig
    def __init__(self, project_id: _Optional[str] = ..., instance_id: _Optional[str] = ..., backup_id: _Optional[str] = ..., database_id: _Optional[str] = ..., expire_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., version_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., encryption_config: _Optional[_Union[_common_pb2.EncryptionConfig, _Mapping]] = ...) -> None: ...

class CopyCloudBackupAction(_message.Message):
    __slots__ = ("project_id", "instance_id", "backup_id", "source_backup", "expire_time")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    BACKUP_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_BACKUP_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    instance_id: str
    backup_id: str
    source_backup: str
    expire_time: _timestamp_pb2.Timestamp
    def __init__(self, project_id: _Optional[str] = ..., instance_id: _Optional[str] = ..., backup_id: _Optional[str] = ..., source_backup: _Optional[str] = ..., expire_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class GetCloudBackupAction(_message.Message):
    __slots__ = ("project_id", "instance_id", "backup_id")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    BACKUP_ID_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    instance_id: str
    backup_id: str
    def __init__(self, project_id: _Optional[str] = ..., instance_id: _Optional[str] = ..., backup_id: _Optional[str] = ...) -> None: ...

class UpdateCloudBackupAction(_message.Message):
    __slots__ = ("project_id", "instance_id", "backup_id", "expire_time")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    BACKUP_ID_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    instance_id: str
    backup_id: str
    expire_time: _timestamp_pb2.Timestamp
    def __init__(self, project_id: _Optional[str] = ..., instance_id: _Optional[str] = ..., backup_id: _Optional[str] = ..., expire_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class DeleteCloudBackupAction(_message.Message):
    __slots__ = ("project_id", "instance_id", "backup_id")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    BACKUP_ID_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    instance_id: str
    backup_id: str
    def __init__(self, project_id: _Optional[str] = ..., instance_id: _Optional[str] = ..., backup_id: _Optional[str] = ...) -> None: ...

class ListCloudBackupsAction(_message.Message):
    __slots__ = ("project_id", "instance_id", "filter", "page_size", "page_token")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    instance_id: str
    filter: str
    page_size: int
    page_token: str
    def __init__(self, project_id: _Optional[str] = ..., instance_id: _Optional[str] = ..., filter: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListCloudBackupOperationsAction(_message.Message):
    __slots__ = ("project_id", "instance_id", "filter", "page_size", "page_token")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    instance_id: str
    filter: str
    page_size: int
    page_token: str
    def __init__(self, project_id: _Optional[str] = ..., instance_id: _Optional[str] = ..., filter: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class GetOperationAction(_message.Message):
    __slots__ = ("operation",)
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    operation: str
    def __init__(self, operation: _Optional[str] = ...) -> None: ...

class QueryCancellationAction(_message.Message):
    __slots__ = ("long_running_sql", "cancel_query")
    LONG_RUNNING_SQL_FIELD_NUMBER: _ClassVar[int]
    CANCEL_QUERY_FIELD_NUMBER: _ClassVar[int]
    long_running_sql: str
    cancel_query: str
    def __init__(self, long_running_sql: _Optional[str] = ..., cancel_query: _Optional[str] = ...) -> None: ...

class CancelOperationAction(_message.Message):
    __slots__ = ("operation",)
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    operation: str
    def __init__(self, operation: _Optional[str] = ...) -> None: ...

class StartBatchTransactionAction(_message.Message):
    __slots__ = ("batch_txn_time", "tid", "cloud_database_role")
    BATCH_TXN_TIME_FIELD_NUMBER: _ClassVar[int]
    TID_FIELD_NUMBER: _ClassVar[int]
    CLOUD_DATABASE_ROLE_FIELD_NUMBER: _ClassVar[int]
    batch_txn_time: _timestamp_pb2.Timestamp
    tid: bytes
    cloud_database_role: str
    def __init__(self, batch_txn_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., tid: _Optional[bytes] = ..., cloud_database_role: _Optional[str] = ...) -> None: ...

class CloseBatchTransactionAction(_message.Message):
    __slots__ = ("cleanup",)
    CLEANUP_FIELD_NUMBER: _ClassVar[int]
    cleanup: bool
    def __init__(self, cleanup: bool = ...) -> None: ...

class GenerateDbPartitionsForReadAction(_message.Message):
    __slots__ = ("read", "table", "desired_bytes_per_partition", "max_partition_count")
    READ_FIELD_NUMBER: _ClassVar[int]
    TABLE_FIELD_NUMBER: _ClassVar[int]
    DESIRED_BYTES_PER_PARTITION_FIELD_NUMBER: _ClassVar[int]
    MAX_PARTITION_COUNT_FIELD_NUMBER: _ClassVar[int]
    read: ReadAction
    table: _containers.RepeatedCompositeFieldContainer[TableMetadata]
    desired_bytes_per_partition: int
    max_partition_count: int
    def __init__(self, read: _Optional[_Union[ReadAction, _Mapping]] = ..., table: _Optional[_Iterable[_Union[TableMetadata, _Mapping]]] = ..., desired_bytes_per_partition: _Optional[int] = ..., max_partition_count: _Optional[int] = ...) -> None: ...

class GenerateDbPartitionsForQueryAction(_message.Message):
    __slots__ = ("query", "desired_bytes_per_partition")
    QUERY_FIELD_NUMBER: _ClassVar[int]
    DESIRED_BYTES_PER_PARTITION_FIELD_NUMBER: _ClassVar[int]
    query: QueryAction
    desired_bytes_per_partition: int
    def __init__(self, query: _Optional[_Union[QueryAction, _Mapping]] = ..., desired_bytes_per_partition: _Optional[int] = ...) -> None: ...

class BatchPartition(_message.Message):
    __slots__ = ("partition", "partition_token", "table", "index")
    PARTITION_FIELD_NUMBER: _ClassVar[int]
    PARTITION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TABLE_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    partition: bytes
    partition_token: bytes
    table: str
    index: str
    def __init__(self, partition: _Optional[bytes] = ..., partition_token: _Optional[bytes] = ..., table: _Optional[str] = ..., index: _Optional[str] = ...) -> None: ...

class ExecutePartitionAction(_message.Message):
    __slots__ = ("partition",)
    PARTITION_FIELD_NUMBER: _ClassVar[int]
    partition: BatchPartition
    def __init__(self, partition: _Optional[_Union[BatchPartition, _Mapping]] = ...) -> None: ...

class ExecuteChangeStreamQuery(_message.Message):
    __slots__ = ("name", "start_time", "end_time", "partition_token", "read_options", "heartbeat_milliseconds", "deadline_seconds", "cloud_database_role")
    NAME_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    PARTITION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    READ_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    HEARTBEAT_MILLISECONDS_FIELD_NUMBER: _ClassVar[int]
    DEADLINE_SECONDS_FIELD_NUMBER: _ClassVar[int]
    CLOUD_DATABASE_ROLE_FIELD_NUMBER: _ClassVar[int]
    name: str
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    partition_token: str
    read_options: _containers.RepeatedScalarFieldContainer[str]
    heartbeat_milliseconds: int
    deadline_seconds: int
    cloud_database_role: str
    def __init__(self, name: _Optional[str] = ..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., partition_token: _Optional[str] = ..., read_options: _Optional[_Iterable[str]] = ..., heartbeat_milliseconds: _Optional[int] = ..., deadline_seconds: _Optional[int] = ..., cloud_database_role: _Optional[str] = ...) -> None: ...

class SpannerActionOutcome(_message.Message):
    __slots__ = ("status", "commit_time", "read_result", "query_result", "transaction_restarted", "batch_txn_id", "db_partition", "admin_result", "dml_rows_modified", "change_stream_records")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    COMMIT_TIME_FIELD_NUMBER: _ClassVar[int]
    READ_RESULT_FIELD_NUMBER: _ClassVar[int]
    QUERY_RESULT_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_RESTARTED_FIELD_NUMBER: _ClassVar[int]
    BATCH_TXN_ID_FIELD_NUMBER: _ClassVar[int]
    DB_PARTITION_FIELD_NUMBER: _ClassVar[int]
    ADMIN_RESULT_FIELD_NUMBER: _ClassVar[int]
    DML_ROWS_MODIFIED_FIELD_NUMBER: _ClassVar[int]
    CHANGE_STREAM_RECORDS_FIELD_NUMBER: _ClassVar[int]
    status: _status_pb2.Status
    commit_time: _timestamp_pb2.Timestamp
    read_result: ReadResult
    query_result: QueryResult
    transaction_restarted: bool
    batch_txn_id: bytes
    db_partition: _containers.RepeatedCompositeFieldContainer[BatchPartition]
    admin_result: AdminResult
    dml_rows_modified: _containers.RepeatedScalarFieldContainer[int]
    change_stream_records: _containers.RepeatedCompositeFieldContainer[ChangeStreamRecord]
    def __init__(self, status: _Optional[_Union[_status_pb2.Status, _Mapping]] = ..., commit_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., read_result: _Optional[_Union[ReadResult, _Mapping]] = ..., query_result: _Optional[_Union[QueryResult, _Mapping]] = ..., transaction_restarted: bool = ..., batch_txn_id: _Optional[bytes] = ..., db_partition: _Optional[_Iterable[_Union[BatchPartition, _Mapping]]] = ..., admin_result: _Optional[_Union[AdminResult, _Mapping]] = ..., dml_rows_modified: _Optional[_Iterable[int]] = ..., change_stream_records: _Optional[_Iterable[_Union[ChangeStreamRecord, _Mapping]]] = ...) -> None: ...

class AdminResult(_message.Message):
    __slots__ = ("backup_response", "operation_response", "database_response", "instance_response", "instance_config_response")
    BACKUP_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    OPERATION_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    DATABASE_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_CONFIG_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    backup_response: CloudBackupResponse
    operation_response: OperationResponse
    database_response: CloudDatabaseResponse
    instance_response: CloudInstanceResponse
    instance_config_response: CloudInstanceConfigResponse
    def __init__(self, backup_response: _Optional[_Union[CloudBackupResponse, _Mapping]] = ..., operation_response: _Optional[_Union[OperationResponse, _Mapping]] = ..., database_response: _Optional[_Union[CloudDatabaseResponse, _Mapping]] = ..., instance_response: _Optional[_Union[CloudInstanceResponse, _Mapping]] = ..., instance_config_response: _Optional[_Union[CloudInstanceConfigResponse, _Mapping]] = ...) -> None: ...

class CloudBackupResponse(_message.Message):
    __slots__ = ("listed_backups", "listed_backup_operations", "next_page_token", "backup")
    LISTED_BACKUPS_FIELD_NUMBER: _ClassVar[int]
    LISTED_BACKUP_OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    BACKUP_FIELD_NUMBER: _ClassVar[int]
    listed_backups: _containers.RepeatedCompositeFieldContainer[_backup_pb2.Backup]
    listed_backup_operations: _containers.RepeatedCompositeFieldContainer[_operations_pb2.Operation]
    next_page_token: str
    backup: _backup_pb2.Backup
    def __init__(self, listed_backups: _Optional[_Iterable[_Union[_backup_pb2.Backup, _Mapping]]] = ..., listed_backup_operations: _Optional[_Iterable[_Union[_operations_pb2.Operation, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., backup: _Optional[_Union[_backup_pb2.Backup, _Mapping]] = ...) -> None: ...

class OperationResponse(_message.Message):
    __slots__ = ("listed_operations", "next_page_token", "operation")
    LISTED_OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    listed_operations: _containers.RepeatedCompositeFieldContainer[_operations_pb2.Operation]
    next_page_token: str
    operation: _operations_pb2.Operation
    def __init__(self, listed_operations: _Optional[_Iterable[_Union[_operations_pb2.Operation, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., operation: _Optional[_Union[_operations_pb2.Operation, _Mapping]] = ...) -> None: ...

class CloudInstanceResponse(_message.Message):
    __slots__ = ("listed_instances", "next_page_token", "instance")
    LISTED_INSTANCES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    listed_instances: _containers.RepeatedCompositeFieldContainer[_spanner_instance_admin_pb2.Instance]
    next_page_token: str
    instance: _spanner_instance_admin_pb2.Instance
    def __init__(self, listed_instances: _Optional[_Iterable[_Union[_spanner_instance_admin_pb2.Instance, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., instance: _Optional[_Union[_spanner_instance_admin_pb2.Instance, _Mapping]] = ...) -> None: ...

class CloudInstanceConfigResponse(_message.Message):
    __slots__ = ("listed_instance_configs", "next_page_token", "instance_config")
    LISTED_INSTANCE_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    listed_instance_configs: _containers.RepeatedCompositeFieldContainer[_spanner_instance_admin_pb2.InstanceConfig]
    next_page_token: str
    instance_config: _spanner_instance_admin_pb2.InstanceConfig
    def __init__(self, listed_instance_configs: _Optional[_Iterable[_Union[_spanner_instance_admin_pb2.InstanceConfig, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., instance_config: _Optional[_Union[_spanner_instance_admin_pb2.InstanceConfig, _Mapping]] = ...) -> None: ...

class CloudDatabaseResponse(_message.Message):
    __slots__ = ("listed_databases", "listed_database_operations", "next_page_token", "database")
    LISTED_DATABASES_FIELD_NUMBER: _ClassVar[int]
    LISTED_DATABASE_OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    DATABASE_FIELD_NUMBER: _ClassVar[int]
    listed_databases: _containers.RepeatedCompositeFieldContainer[_spanner_database_admin_pb2.Database]
    listed_database_operations: _containers.RepeatedCompositeFieldContainer[_operations_pb2.Operation]
    next_page_token: str
    database: _spanner_database_admin_pb2.Database
    def __init__(self, listed_databases: _Optional[_Iterable[_Union[_spanner_database_admin_pb2.Database, _Mapping]]] = ..., listed_database_operations: _Optional[_Iterable[_Union[_operations_pb2.Operation, _Mapping]]] = ..., next_page_token: _Optional[str] = ..., database: _Optional[_Union[_spanner_database_admin_pb2.Database, _Mapping]] = ...) -> None: ...

class ReadResult(_message.Message):
    __slots__ = ("table", "index", "request_index", "row", "row_type")
    TABLE_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    REQUEST_INDEX_FIELD_NUMBER: _ClassVar[int]
    ROW_FIELD_NUMBER: _ClassVar[int]
    ROW_TYPE_FIELD_NUMBER: _ClassVar[int]
    table: str
    index: str
    request_index: int
    row: _containers.RepeatedCompositeFieldContainer[ValueList]
    row_type: _type_pb2.StructType
    def __init__(self, table: _Optional[str] = ..., index: _Optional[str] = ..., request_index: _Optional[int] = ..., row: _Optional[_Iterable[_Union[ValueList, _Mapping]]] = ..., row_type: _Optional[_Union[_type_pb2.StructType, _Mapping]] = ...) -> None: ...

class QueryResult(_message.Message):
    __slots__ = ("row", "row_type")
    ROW_FIELD_NUMBER: _ClassVar[int]
    ROW_TYPE_FIELD_NUMBER: _ClassVar[int]
    row: _containers.RepeatedCompositeFieldContainer[ValueList]
    row_type: _type_pb2.StructType
    def __init__(self, row: _Optional[_Iterable[_Union[ValueList, _Mapping]]] = ..., row_type: _Optional[_Union[_type_pb2.StructType, _Mapping]] = ...) -> None: ...

class ChangeStreamRecord(_message.Message):
    __slots__ = ("data_change", "child_partition", "heartbeat")
    DATA_CHANGE_FIELD_NUMBER: _ClassVar[int]
    CHILD_PARTITION_FIELD_NUMBER: _ClassVar[int]
    HEARTBEAT_FIELD_NUMBER: _ClassVar[int]
    data_change: DataChangeRecord
    child_partition: ChildPartitionsRecord
    heartbeat: HeartbeatRecord
    def __init__(self, data_change: _Optional[_Union[DataChangeRecord, _Mapping]] = ..., child_partition: _Optional[_Union[ChildPartitionsRecord, _Mapping]] = ..., heartbeat: _Optional[_Union[HeartbeatRecord, _Mapping]] = ...) -> None: ...

class DataChangeRecord(_message.Message):
    __slots__ = ("commit_time", "record_sequence", "transaction_id", "is_last_record", "table", "column_types", "mods", "mod_type", "value_capture_type", "record_count", "partition_count", "transaction_tag", "is_system_transaction")
    class ColumnType(_message.Message):
        __slots__ = ("name", "type", "is_primary_key", "ordinal_position")
        NAME_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        IS_PRIMARY_KEY_FIELD_NUMBER: _ClassVar[int]
        ORDINAL_POSITION_FIELD_NUMBER: _ClassVar[int]
        name: str
        type: str
        is_primary_key: bool
        ordinal_position: int
        def __init__(self, name: _Optional[str] = ..., type: _Optional[str] = ..., is_primary_key: bool = ..., ordinal_position: _Optional[int] = ...) -> None: ...
    class Mod(_message.Message):
        __slots__ = ("keys", "new_values", "old_values")
        KEYS_FIELD_NUMBER: _ClassVar[int]
        NEW_VALUES_FIELD_NUMBER: _ClassVar[int]
        OLD_VALUES_FIELD_NUMBER: _ClassVar[int]
        keys: str
        new_values: str
        old_values: str
        def __init__(self, keys: _Optional[str] = ..., new_values: _Optional[str] = ..., old_values: _Optional[str] = ...) -> None: ...
    COMMIT_TIME_FIELD_NUMBER: _ClassVar[int]
    RECORD_SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    IS_LAST_RECORD_FIELD_NUMBER: _ClassVar[int]
    TABLE_FIELD_NUMBER: _ClassVar[int]
    COLUMN_TYPES_FIELD_NUMBER: _ClassVar[int]
    MODS_FIELD_NUMBER: _ClassVar[int]
    MOD_TYPE_FIELD_NUMBER: _ClassVar[int]
    VALUE_CAPTURE_TYPE_FIELD_NUMBER: _ClassVar[int]
    RECORD_COUNT_FIELD_NUMBER: _ClassVar[int]
    PARTITION_COUNT_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_TAG_FIELD_NUMBER: _ClassVar[int]
    IS_SYSTEM_TRANSACTION_FIELD_NUMBER: _ClassVar[int]
    commit_time: _timestamp_pb2.Timestamp
    record_sequence: str
    transaction_id: str
    is_last_record: bool
    table: str
    column_types: _containers.RepeatedCompositeFieldContainer[DataChangeRecord.ColumnType]
    mods: _containers.RepeatedCompositeFieldContainer[DataChangeRecord.Mod]
    mod_type: str
    value_capture_type: str
    record_count: int
    partition_count: int
    transaction_tag: str
    is_system_transaction: bool
    def __init__(self, commit_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., record_sequence: _Optional[str] = ..., transaction_id: _Optional[str] = ..., is_last_record: bool = ..., table: _Optional[str] = ..., column_types: _Optional[_Iterable[_Union[DataChangeRecord.ColumnType, _Mapping]]] = ..., mods: _Optional[_Iterable[_Union[DataChangeRecord.Mod, _Mapping]]] = ..., mod_type: _Optional[str] = ..., value_capture_type: _Optional[str] = ..., record_count: _Optional[int] = ..., partition_count: _Optional[int] = ..., transaction_tag: _Optional[str] = ..., is_system_transaction: bool = ...) -> None: ...

class ChildPartitionsRecord(_message.Message):
    __slots__ = ("start_time", "record_sequence", "child_partitions")
    class ChildPartition(_message.Message):
        __slots__ = ("token", "parent_partition_tokens")
        TOKEN_FIELD_NUMBER: _ClassVar[int]
        PARENT_PARTITION_TOKENS_FIELD_NUMBER: _ClassVar[int]
        token: str
        parent_partition_tokens: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, token: _Optional[str] = ..., parent_partition_tokens: _Optional[_Iterable[str]] = ...) -> None: ...
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    RECORD_SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    CHILD_PARTITIONS_FIELD_NUMBER: _ClassVar[int]
    start_time: _timestamp_pb2.Timestamp
    record_sequence: str
    child_partitions: _containers.RepeatedCompositeFieldContainer[ChildPartitionsRecord.ChildPartition]
    def __init__(self, start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., record_sequence: _Optional[str] = ..., child_partitions: _Optional[_Iterable[_Union[ChildPartitionsRecord.ChildPartition, _Mapping]]] = ...) -> None: ...

class HeartbeatRecord(_message.Message):
    __slots__ = ("heartbeat_time",)
    HEARTBEAT_TIME_FIELD_NUMBER: _ClassVar[int]
    heartbeat_time: _timestamp_pb2.Timestamp
    def __init__(self, heartbeat_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class SpannerOptions(_message.Message):
    __slots__ = ("session_pool_options",)
    SESSION_POOL_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    session_pool_options: SessionPoolOptions
    def __init__(self, session_pool_options: _Optional[_Union[SessionPoolOptions, _Mapping]] = ...) -> None: ...

class SessionPoolOptions(_message.Message):
    __slots__ = ("use_multiplexed",)
    USE_MULTIPLEXED_FIELD_NUMBER: _ClassVar[int]
    use_multiplexed: bool
    def __init__(self, use_multiplexed: bool = ...) -> None: ...
