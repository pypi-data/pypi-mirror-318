from google.spanner.v1 import commit_response_pb2 as _commit_response_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.rpc import status_pb2 as _status_pb2
from google.spanner.v1 import keys_pb2 as _keys_pb2
from google.spanner.v1 import mutation_pb2 as _mutation_pb2
from google.spanner.v1 import result_set_pb2 as _result_set_pb2
from google.spanner.v1 import transaction_pb2 as _transaction_pb2
from google.spanner.v1 import type_pb2 as _type_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
from google.spanner.v1.commit_response_pb2 import CommitResponse as CommitResponse
DESCRIPTOR: _descriptor.FileDescriptor

class CreateSessionRequest(_message.Message):
    __slots__ = ('database', 'session')
    DATABASE_FIELD_NUMBER: _ClassVar[int]
    SESSION_FIELD_NUMBER: _ClassVar[int]
    database: str
    session: Session

    def __init__(self, database: _Optional[str]=..., session: _Optional[_Union[Session, _Mapping]]=...) -> None:
        ...

class BatchCreateSessionsRequest(_message.Message):
    __slots__ = ('database', 'session_template', 'session_count')
    DATABASE_FIELD_NUMBER: _ClassVar[int]
    SESSION_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    SESSION_COUNT_FIELD_NUMBER: _ClassVar[int]
    database: str
    session_template: Session
    session_count: int

    def __init__(self, database: _Optional[str]=..., session_template: _Optional[_Union[Session, _Mapping]]=..., session_count: _Optional[int]=...) -> None:
        ...

class BatchCreateSessionsResponse(_message.Message):
    __slots__ = ('session',)
    SESSION_FIELD_NUMBER: _ClassVar[int]
    session: _containers.RepeatedCompositeFieldContainer[Session]

    def __init__(self, session: _Optional[_Iterable[_Union[Session, _Mapping]]]=...) -> None:
        ...

class Session(_message.Message):
    __slots__ = ('name', 'labels', 'create_time', 'approximate_last_use_time', 'creator_role', 'multiplexed')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    APPROXIMATE_LAST_USE_TIME_FIELD_NUMBER: _ClassVar[int]
    CREATOR_ROLE_FIELD_NUMBER: _ClassVar[int]
    MULTIPLEXED_FIELD_NUMBER: _ClassVar[int]
    name: str
    labels: _containers.ScalarMap[str, str]
    create_time: _timestamp_pb2.Timestamp
    approximate_last_use_time: _timestamp_pb2.Timestamp
    creator_role: str
    multiplexed: bool

    def __init__(self, name: _Optional[str]=..., labels: _Optional[_Mapping[str, str]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., approximate_last_use_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., creator_role: _Optional[str]=..., multiplexed: bool=...) -> None:
        ...

class GetSessionRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListSessionsRequest(_message.Message):
    __slots__ = ('database', 'page_size', 'page_token', 'filter')
    DATABASE_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    database: str
    page_size: int
    page_token: str
    filter: str

    def __init__(self, database: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=...) -> None:
        ...

class ListSessionsResponse(_message.Message):
    __slots__ = ('sessions', 'next_page_token')
    SESSIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    sessions: _containers.RepeatedCompositeFieldContainer[Session]
    next_page_token: str

    def __init__(self, sessions: _Optional[_Iterable[_Union[Session, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class DeleteSessionRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class RequestOptions(_message.Message):
    __slots__ = ('priority', 'request_tag', 'transaction_tag')

    class Priority(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PRIORITY_UNSPECIFIED: _ClassVar[RequestOptions.Priority]
        PRIORITY_LOW: _ClassVar[RequestOptions.Priority]
        PRIORITY_MEDIUM: _ClassVar[RequestOptions.Priority]
        PRIORITY_HIGH: _ClassVar[RequestOptions.Priority]
    PRIORITY_UNSPECIFIED: RequestOptions.Priority
    PRIORITY_LOW: RequestOptions.Priority
    PRIORITY_MEDIUM: RequestOptions.Priority
    PRIORITY_HIGH: RequestOptions.Priority
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    REQUEST_TAG_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_TAG_FIELD_NUMBER: _ClassVar[int]
    priority: RequestOptions.Priority
    request_tag: str
    transaction_tag: str

    def __init__(self, priority: _Optional[_Union[RequestOptions.Priority, str]]=..., request_tag: _Optional[str]=..., transaction_tag: _Optional[str]=...) -> None:
        ...

class DirectedReadOptions(_message.Message):
    __slots__ = ('include_replicas', 'exclude_replicas')

    class ReplicaSelection(_message.Message):
        __slots__ = ('location', 'type')

        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            TYPE_UNSPECIFIED: _ClassVar[DirectedReadOptions.ReplicaSelection.Type]
            READ_WRITE: _ClassVar[DirectedReadOptions.ReplicaSelection.Type]
            READ_ONLY: _ClassVar[DirectedReadOptions.ReplicaSelection.Type]
        TYPE_UNSPECIFIED: DirectedReadOptions.ReplicaSelection.Type
        READ_WRITE: DirectedReadOptions.ReplicaSelection.Type
        READ_ONLY: DirectedReadOptions.ReplicaSelection.Type
        LOCATION_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        location: str
        type: DirectedReadOptions.ReplicaSelection.Type

        def __init__(self, location: _Optional[str]=..., type: _Optional[_Union[DirectedReadOptions.ReplicaSelection.Type, str]]=...) -> None:
            ...

    class IncludeReplicas(_message.Message):
        __slots__ = ('replica_selections', 'auto_failover_disabled')
        REPLICA_SELECTIONS_FIELD_NUMBER: _ClassVar[int]
        AUTO_FAILOVER_DISABLED_FIELD_NUMBER: _ClassVar[int]
        replica_selections: _containers.RepeatedCompositeFieldContainer[DirectedReadOptions.ReplicaSelection]
        auto_failover_disabled: bool

        def __init__(self, replica_selections: _Optional[_Iterable[_Union[DirectedReadOptions.ReplicaSelection, _Mapping]]]=..., auto_failover_disabled: bool=...) -> None:
            ...

    class ExcludeReplicas(_message.Message):
        __slots__ = ('replica_selections',)
        REPLICA_SELECTIONS_FIELD_NUMBER: _ClassVar[int]
        replica_selections: _containers.RepeatedCompositeFieldContainer[DirectedReadOptions.ReplicaSelection]

        def __init__(self, replica_selections: _Optional[_Iterable[_Union[DirectedReadOptions.ReplicaSelection, _Mapping]]]=...) -> None:
            ...
    INCLUDE_REPLICAS_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_REPLICAS_FIELD_NUMBER: _ClassVar[int]
    include_replicas: DirectedReadOptions.IncludeReplicas
    exclude_replicas: DirectedReadOptions.ExcludeReplicas

    def __init__(self, include_replicas: _Optional[_Union[DirectedReadOptions.IncludeReplicas, _Mapping]]=..., exclude_replicas: _Optional[_Union[DirectedReadOptions.ExcludeReplicas, _Mapping]]=...) -> None:
        ...

class ExecuteSqlRequest(_message.Message):
    __slots__ = ('session', 'transaction', 'sql', 'params', 'param_types', 'resume_token', 'query_mode', 'partition_token', 'seqno', 'query_options', 'request_options', 'directed_read_options', 'data_boost_enabled', 'last_statement')

    class QueryMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NORMAL: _ClassVar[ExecuteSqlRequest.QueryMode]
        PLAN: _ClassVar[ExecuteSqlRequest.QueryMode]
        PROFILE: _ClassVar[ExecuteSqlRequest.QueryMode]
        WITH_STATS: _ClassVar[ExecuteSqlRequest.QueryMode]
        WITH_PLAN_AND_STATS: _ClassVar[ExecuteSqlRequest.QueryMode]
    NORMAL: ExecuteSqlRequest.QueryMode
    PLAN: ExecuteSqlRequest.QueryMode
    PROFILE: ExecuteSqlRequest.QueryMode
    WITH_STATS: ExecuteSqlRequest.QueryMode
    WITH_PLAN_AND_STATS: ExecuteSqlRequest.QueryMode

    class QueryOptions(_message.Message):
        __slots__ = ('optimizer_version', 'optimizer_statistics_package')
        OPTIMIZER_VERSION_FIELD_NUMBER: _ClassVar[int]
        OPTIMIZER_STATISTICS_PACKAGE_FIELD_NUMBER: _ClassVar[int]
        optimizer_version: str
        optimizer_statistics_package: str

        def __init__(self, optimizer_version: _Optional[str]=..., optimizer_statistics_package: _Optional[str]=...) -> None:
            ...

    class ParamTypesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _type_pb2.Type

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[_type_pb2.Type, _Mapping]]=...) -> None:
            ...
    SESSION_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_FIELD_NUMBER: _ClassVar[int]
    SQL_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    PARAM_TYPES_FIELD_NUMBER: _ClassVar[int]
    RESUME_TOKEN_FIELD_NUMBER: _ClassVar[int]
    QUERY_MODE_FIELD_NUMBER: _ClassVar[int]
    PARTITION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    SEQNO_FIELD_NUMBER: _ClassVar[int]
    QUERY_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    DIRECTED_READ_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    DATA_BOOST_ENABLED_FIELD_NUMBER: _ClassVar[int]
    LAST_STATEMENT_FIELD_NUMBER: _ClassVar[int]
    session: str
    transaction: _transaction_pb2.TransactionSelector
    sql: str
    params: _struct_pb2.Struct
    param_types: _containers.MessageMap[str, _type_pb2.Type]
    resume_token: bytes
    query_mode: ExecuteSqlRequest.QueryMode
    partition_token: bytes
    seqno: int
    query_options: ExecuteSqlRequest.QueryOptions
    request_options: RequestOptions
    directed_read_options: DirectedReadOptions
    data_boost_enabled: bool
    last_statement: bool

    def __init__(self, session: _Optional[str]=..., transaction: _Optional[_Union[_transaction_pb2.TransactionSelector, _Mapping]]=..., sql: _Optional[str]=..., params: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=..., param_types: _Optional[_Mapping[str, _type_pb2.Type]]=..., resume_token: _Optional[bytes]=..., query_mode: _Optional[_Union[ExecuteSqlRequest.QueryMode, str]]=..., partition_token: _Optional[bytes]=..., seqno: _Optional[int]=..., query_options: _Optional[_Union[ExecuteSqlRequest.QueryOptions, _Mapping]]=..., request_options: _Optional[_Union[RequestOptions, _Mapping]]=..., directed_read_options: _Optional[_Union[DirectedReadOptions, _Mapping]]=..., data_boost_enabled: bool=..., last_statement: bool=...) -> None:
        ...

class ExecuteBatchDmlRequest(_message.Message):
    __slots__ = ('session', 'transaction', 'statements', 'seqno', 'request_options', 'last_statements')

    class Statement(_message.Message):
        __slots__ = ('sql', 'params', 'param_types')

        class ParamTypesEntry(_message.Message):
            __slots__ = ('key', 'value')
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: _type_pb2.Type

            def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[_type_pb2.Type, _Mapping]]=...) -> None:
                ...
        SQL_FIELD_NUMBER: _ClassVar[int]
        PARAMS_FIELD_NUMBER: _ClassVar[int]
        PARAM_TYPES_FIELD_NUMBER: _ClassVar[int]
        sql: str
        params: _struct_pb2.Struct
        param_types: _containers.MessageMap[str, _type_pb2.Type]

        def __init__(self, sql: _Optional[str]=..., params: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=..., param_types: _Optional[_Mapping[str, _type_pb2.Type]]=...) -> None:
            ...
    SESSION_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_FIELD_NUMBER: _ClassVar[int]
    STATEMENTS_FIELD_NUMBER: _ClassVar[int]
    SEQNO_FIELD_NUMBER: _ClassVar[int]
    REQUEST_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    LAST_STATEMENTS_FIELD_NUMBER: _ClassVar[int]
    session: str
    transaction: _transaction_pb2.TransactionSelector
    statements: _containers.RepeatedCompositeFieldContainer[ExecuteBatchDmlRequest.Statement]
    seqno: int
    request_options: RequestOptions
    last_statements: bool

    def __init__(self, session: _Optional[str]=..., transaction: _Optional[_Union[_transaction_pb2.TransactionSelector, _Mapping]]=..., statements: _Optional[_Iterable[_Union[ExecuteBatchDmlRequest.Statement, _Mapping]]]=..., seqno: _Optional[int]=..., request_options: _Optional[_Union[RequestOptions, _Mapping]]=..., last_statements: bool=...) -> None:
        ...

class ExecuteBatchDmlResponse(_message.Message):
    __slots__ = ('result_sets', 'status', 'precommit_token')
    RESULT_SETS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    PRECOMMIT_TOKEN_FIELD_NUMBER: _ClassVar[int]
    result_sets: _containers.RepeatedCompositeFieldContainer[_result_set_pb2.ResultSet]
    status: _status_pb2.Status
    precommit_token: _transaction_pb2.MultiplexedSessionPrecommitToken

    def __init__(self, result_sets: _Optional[_Iterable[_Union[_result_set_pb2.ResultSet, _Mapping]]]=..., status: _Optional[_Union[_status_pb2.Status, _Mapping]]=..., precommit_token: _Optional[_Union[_transaction_pb2.MultiplexedSessionPrecommitToken, _Mapping]]=...) -> None:
        ...

class PartitionOptions(_message.Message):
    __slots__ = ('partition_size_bytes', 'max_partitions')
    PARTITION_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    MAX_PARTITIONS_FIELD_NUMBER: _ClassVar[int]
    partition_size_bytes: int
    max_partitions: int

    def __init__(self, partition_size_bytes: _Optional[int]=..., max_partitions: _Optional[int]=...) -> None:
        ...

class PartitionQueryRequest(_message.Message):
    __slots__ = ('session', 'transaction', 'sql', 'params', 'param_types', 'partition_options')

    class ParamTypesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _type_pb2.Type

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[_type_pb2.Type, _Mapping]]=...) -> None:
            ...
    SESSION_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_FIELD_NUMBER: _ClassVar[int]
    SQL_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    PARAM_TYPES_FIELD_NUMBER: _ClassVar[int]
    PARTITION_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    session: str
    transaction: _transaction_pb2.TransactionSelector
    sql: str
    params: _struct_pb2.Struct
    param_types: _containers.MessageMap[str, _type_pb2.Type]
    partition_options: PartitionOptions

    def __init__(self, session: _Optional[str]=..., transaction: _Optional[_Union[_transaction_pb2.TransactionSelector, _Mapping]]=..., sql: _Optional[str]=..., params: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=..., param_types: _Optional[_Mapping[str, _type_pb2.Type]]=..., partition_options: _Optional[_Union[PartitionOptions, _Mapping]]=...) -> None:
        ...

class PartitionReadRequest(_message.Message):
    __slots__ = ('session', 'transaction', 'table', 'index', 'columns', 'key_set', 'partition_options')
    SESSION_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_FIELD_NUMBER: _ClassVar[int]
    TABLE_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    COLUMNS_FIELD_NUMBER: _ClassVar[int]
    KEY_SET_FIELD_NUMBER: _ClassVar[int]
    PARTITION_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    session: str
    transaction: _transaction_pb2.TransactionSelector
    table: str
    index: str
    columns: _containers.RepeatedScalarFieldContainer[str]
    key_set: _keys_pb2.KeySet
    partition_options: PartitionOptions

    def __init__(self, session: _Optional[str]=..., transaction: _Optional[_Union[_transaction_pb2.TransactionSelector, _Mapping]]=..., table: _Optional[str]=..., index: _Optional[str]=..., columns: _Optional[_Iterable[str]]=..., key_set: _Optional[_Union[_keys_pb2.KeySet, _Mapping]]=..., partition_options: _Optional[_Union[PartitionOptions, _Mapping]]=...) -> None:
        ...

class Partition(_message.Message):
    __slots__ = ('partition_token',)
    PARTITION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    partition_token: bytes

    def __init__(self, partition_token: _Optional[bytes]=...) -> None:
        ...

class PartitionResponse(_message.Message):
    __slots__ = ('partitions', 'transaction')
    PARTITIONS_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_FIELD_NUMBER: _ClassVar[int]
    partitions: _containers.RepeatedCompositeFieldContainer[Partition]
    transaction: _transaction_pb2.Transaction

    def __init__(self, partitions: _Optional[_Iterable[_Union[Partition, _Mapping]]]=..., transaction: _Optional[_Union[_transaction_pb2.Transaction, _Mapping]]=...) -> None:
        ...

class ReadRequest(_message.Message):
    __slots__ = ('session', 'transaction', 'table', 'index', 'columns', 'key_set', 'limit', 'resume_token', 'partition_token', 'request_options', 'directed_read_options', 'data_boost_enabled', 'order_by', 'lock_hint')

    class OrderBy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ORDER_BY_UNSPECIFIED: _ClassVar[ReadRequest.OrderBy]
        ORDER_BY_PRIMARY_KEY: _ClassVar[ReadRequest.OrderBy]
        ORDER_BY_NO_ORDER: _ClassVar[ReadRequest.OrderBy]
    ORDER_BY_UNSPECIFIED: ReadRequest.OrderBy
    ORDER_BY_PRIMARY_KEY: ReadRequest.OrderBy
    ORDER_BY_NO_ORDER: ReadRequest.OrderBy

    class LockHint(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        LOCK_HINT_UNSPECIFIED: _ClassVar[ReadRequest.LockHint]
        LOCK_HINT_SHARED: _ClassVar[ReadRequest.LockHint]
        LOCK_HINT_EXCLUSIVE: _ClassVar[ReadRequest.LockHint]
    LOCK_HINT_UNSPECIFIED: ReadRequest.LockHint
    LOCK_HINT_SHARED: ReadRequest.LockHint
    LOCK_HINT_EXCLUSIVE: ReadRequest.LockHint
    SESSION_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_FIELD_NUMBER: _ClassVar[int]
    TABLE_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    COLUMNS_FIELD_NUMBER: _ClassVar[int]
    KEY_SET_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    RESUME_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PARTITION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    REQUEST_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    DIRECTED_READ_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    DATA_BOOST_ENABLED_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    LOCK_HINT_FIELD_NUMBER: _ClassVar[int]
    session: str
    transaction: _transaction_pb2.TransactionSelector
    table: str
    index: str
    columns: _containers.RepeatedScalarFieldContainer[str]
    key_set: _keys_pb2.KeySet
    limit: int
    resume_token: bytes
    partition_token: bytes
    request_options: RequestOptions
    directed_read_options: DirectedReadOptions
    data_boost_enabled: bool
    order_by: ReadRequest.OrderBy
    lock_hint: ReadRequest.LockHint

    def __init__(self, session: _Optional[str]=..., transaction: _Optional[_Union[_transaction_pb2.TransactionSelector, _Mapping]]=..., table: _Optional[str]=..., index: _Optional[str]=..., columns: _Optional[_Iterable[str]]=..., key_set: _Optional[_Union[_keys_pb2.KeySet, _Mapping]]=..., limit: _Optional[int]=..., resume_token: _Optional[bytes]=..., partition_token: _Optional[bytes]=..., request_options: _Optional[_Union[RequestOptions, _Mapping]]=..., directed_read_options: _Optional[_Union[DirectedReadOptions, _Mapping]]=..., data_boost_enabled: bool=..., order_by: _Optional[_Union[ReadRequest.OrderBy, str]]=..., lock_hint: _Optional[_Union[ReadRequest.LockHint, str]]=...) -> None:
        ...

class BeginTransactionRequest(_message.Message):
    __slots__ = ('session', 'options', 'request_options', 'mutation_key')
    SESSION_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    MUTATION_KEY_FIELD_NUMBER: _ClassVar[int]
    session: str
    options: _transaction_pb2.TransactionOptions
    request_options: RequestOptions
    mutation_key: _mutation_pb2.Mutation

    def __init__(self, session: _Optional[str]=..., options: _Optional[_Union[_transaction_pb2.TransactionOptions, _Mapping]]=..., request_options: _Optional[_Union[RequestOptions, _Mapping]]=..., mutation_key: _Optional[_Union[_mutation_pb2.Mutation, _Mapping]]=...) -> None:
        ...

class CommitRequest(_message.Message):
    __slots__ = ('session', 'transaction_id', 'single_use_transaction', 'mutations', 'return_commit_stats', 'max_commit_delay', 'request_options', 'precommit_token')
    SESSION_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    SINGLE_USE_TRANSACTION_FIELD_NUMBER: _ClassVar[int]
    MUTATIONS_FIELD_NUMBER: _ClassVar[int]
    RETURN_COMMIT_STATS_FIELD_NUMBER: _ClassVar[int]
    MAX_COMMIT_DELAY_FIELD_NUMBER: _ClassVar[int]
    REQUEST_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    PRECOMMIT_TOKEN_FIELD_NUMBER: _ClassVar[int]
    session: str
    transaction_id: bytes
    single_use_transaction: _transaction_pb2.TransactionOptions
    mutations: _containers.RepeatedCompositeFieldContainer[_mutation_pb2.Mutation]
    return_commit_stats: bool
    max_commit_delay: _duration_pb2.Duration
    request_options: RequestOptions
    precommit_token: _transaction_pb2.MultiplexedSessionPrecommitToken

    def __init__(self, session: _Optional[str]=..., transaction_id: _Optional[bytes]=..., single_use_transaction: _Optional[_Union[_transaction_pb2.TransactionOptions, _Mapping]]=..., mutations: _Optional[_Iterable[_Union[_mutation_pb2.Mutation, _Mapping]]]=..., return_commit_stats: bool=..., max_commit_delay: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., request_options: _Optional[_Union[RequestOptions, _Mapping]]=..., precommit_token: _Optional[_Union[_transaction_pb2.MultiplexedSessionPrecommitToken, _Mapping]]=...) -> None:
        ...

class RollbackRequest(_message.Message):
    __slots__ = ('session', 'transaction_id')
    SESSION_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    session: str
    transaction_id: bytes

    def __init__(self, session: _Optional[str]=..., transaction_id: _Optional[bytes]=...) -> None:
        ...

class BatchWriteRequest(_message.Message):
    __slots__ = ('session', 'request_options', 'mutation_groups', 'exclude_txn_from_change_streams')

    class MutationGroup(_message.Message):
        __slots__ = ('mutations',)
        MUTATIONS_FIELD_NUMBER: _ClassVar[int]
        mutations: _containers.RepeatedCompositeFieldContainer[_mutation_pb2.Mutation]

        def __init__(self, mutations: _Optional[_Iterable[_Union[_mutation_pb2.Mutation, _Mapping]]]=...) -> None:
            ...
    SESSION_FIELD_NUMBER: _ClassVar[int]
    REQUEST_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    MUTATION_GROUPS_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_TXN_FROM_CHANGE_STREAMS_FIELD_NUMBER: _ClassVar[int]
    session: str
    request_options: RequestOptions
    mutation_groups: _containers.RepeatedCompositeFieldContainer[BatchWriteRequest.MutationGroup]
    exclude_txn_from_change_streams: bool

    def __init__(self, session: _Optional[str]=..., request_options: _Optional[_Union[RequestOptions, _Mapping]]=..., mutation_groups: _Optional[_Iterable[_Union[BatchWriteRequest.MutationGroup, _Mapping]]]=..., exclude_txn_from_change_streams: bool=...) -> None:
        ...

class BatchWriteResponse(_message.Message):
    __slots__ = ('indexes', 'status', 'commit_timestamp')
    INDEXES_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    COMMIT_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    indexes: _containers.RepeatedScalarFieldContainer[int]
    status: _status_pb2.Status
    commit_timestamp: _timestamp_pb2.Timestamp

    def __init__(self, indexes: _Optional[_Iterable[int]]=..., status: _Optional[_Union[_status_pb2.Status, _Mapping]]=..., commit_timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...