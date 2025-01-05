from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import routing_pb2 as _routing_pb2
from google.datastore.v1 import aggregation_result_pb2 as _aggregation_result_pb2
from google.datastore.v1 import entity_pb2 as _entity_pb2
from google.datastore.v1 import query_pb2 as _query_pb2
from google.datastore.v1 import query_profile_pb2 as _query_profile_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class LookupRequest(_message.Message):
    __slots__ = ('project_id', 'database_id', 'read_options', 'keys', 'property_mask')
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    DATABASE_ID_FIELD_NUMBER: _ClassVar[int]
    READ_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    KEYS_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_MASK_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    database_id: str
    read_options: ReadOptions
    keys: _containers.RepeatedCompositeFieldContainer[_entity_pb2.Key]
    property_mask: PropertyMask

    def __init__(self, project_id: _Optional[str]=..., database_id: _Optional[str]=..., read_options: _Optional[_Union[ReadOptions, _Mapping]]=..., keys: _Optional[_Iterable[_Union[_entity_pb2.Key, _Mapping]]]=..., property_mask: _Optional[_Union[PropertyMask, _Mapping]]=...) -> None:
        ...

class LookupResponse(_message.Message):
    __slots__ = ('found', 'missing', 'deferred', 'transaction', 'read_time')
    FOUND_FIELD_NUMBER: _ClassVar[int]
    MISSING_FIELD_NUMBER: _ClassVar[int]
    DEFERRED_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_FIELD_NUMBER: _ClassVar[int]
    READ_TIME_FIELD_NUMBER: _ClassVar[int]
    found: _containers.RepeatedCompositeFieldContainer[_query_pb2.EntityResult]
    missing: _containers.RepeatedCompositeFieldContainer[_query_pb2.EntityResult]
    deferred: _containers.RepeatedCompositeFieldContainer[_entity_pb2.Key]
    transaction: bytes
    read_time: _timestamp_pb2.Timestamp

    def __init__(self, found: _Optional[_Iterable[_Union[_query_pb2.EntityResult, _Mapping]]]=..., missing: _Optional[_Iterable[_Union[_query_pb2.EntityResult, _Mapping]]]=..., deferred: _Optional[_Iterable[_Union[_entity_pb2.Key, _Mapping]]]=..., transaction: _Optional[bytes]=..., read_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class RunQueryRequest(_message.Message):
    __slots__ = ('project_id', 'database_id', 'partition_id', 'read_options', 'query', 'gql_query', 'property_mask', 'explain_options')
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    DATABASE_ID_FIELD_NUMBER: _ClassVar[int]
    PARTITION_ID_FIELD_NUMBER: _ClassVar[int]
    READ_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    GQL_QUERY_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_MASK_FIELD_NUMBER: _ClassVar[int]
    EXPLAIN_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    database_id: str
    partition_id: _entity_pb2.PartitionId
    read_options: ReadOptions
    query: _query_pb2.Query
    gql_query: _query_pb2.GqlQuery
    property_mask: PropertyMask
    explain_options: _query_profile_pb2.ExplainOptions

    def __init__(self, project_id: _Optional[str]=..., database_id: _Optional[str]=..., partition_id: _Optional[_Union[_entity_pb2.PartitionId, _Mapping]]=..., read_options: _Optional[_Union[ReadOptions, _Mapping]]=..., query: _Optional[_Union[_query_pb2.Query, _Mapping]]=..., gql_query: _Optional[_Union[_query_pb2.GqlQuery, _Mapping]]=..., property_mask: _Optional[_Union[PropertyMask, _Mapping]]=..., explain_options: _Optional[_Union[_query_profile_pb2.ExplainOptions, _Mapping]]=...) -> None:
        ...

class RunQueryResponse(_message.Message):
    __slots__ = ('batch', 'query', 'transaction', 'explain_metrics')
    BATCH_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_FIELD_NUMBER: _ClassVar[int]
    EXPLAIN_METRICS_FIELD_NUMBER: _ClassVar[int]
    batch: _query_pb2.QueryResultBatch
    query: _query_pb2.Query
    transaction: bytes
    explain_metrics: _query_profile_pb2.ExplainMetrics

    def __init__(self, batch: _Optional[_Union[_query_pb2.QueryResultBatch, _Mapping]]=..., query: _Optional[_Union[_query_pb2.Query, _Mapping]]=..., transaction: _Optional[bytes]=..., explain_metrics: _Optional[_Union[_query_profile_pb2.ExplainMetrics, _Mapping]]=...) -> None:
        ...

class RunAggregationQueryRequest(_message.Message):
    __slots__ = ('project_id', 'database_id', 'partition_id', 'read_options', 'aggregation_query', 'gql_query', 'explain_options')
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    DATABASE_ID_FIELD_NUMBER: _ClassVar[int]
    PARTITION_ID_FIELD_NUMBER: _ClassVar[int]
    READ_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    AGGREGATION_QUERY_FIELD_NUMBER: _ClassVar[int]
    GQL_QUERY_FIELD_NUMBER: _ClassVar[int]
    EXPLAIN_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    database_id: str
    partition_id: _entity_pb2.PartitionId
    read_options: ReadOptions
    aggregation_query: _query_pb2.AggregationQuery
    gql_query: _query_pb2.GqlQuery
    explain_options: _query_profile_pb2.ExplainOptions

    def __init__(self, project_id: _Optional[str]=..., database_id: _Optional[str]=..., partition_id: _Optional[_Union[_entity_pb2.PartitionId, _Mapping]]=..., read_options: _Optional[_Union[ReadOptions, _Mapping]]=..., aggregation_query: _Optional[_Union[_query_pb2.AggregationQuery, _Mapping]]=..., gql_query: _Optional[_Union[_query_pb2.GqlQuery, _Mapping]]=..., explain_options: _Optional[_Union[_query_profile_pb2.ExplainOptions, _Mapping]]=...) -> None:
        ...

class RunAggregationQueryResponse(_message.Message):
    __slots__ = ('batch', 'query', 'transaction', 'explain_metrics')
    BATCH_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_FIELD_NUMBER: _ClassVar[int]
    EXPLAIN_METRICS_FIELD_NUMBER: _ClassVar[int]
    batch: _aggregation_result_pb2.AggregationResultBatch
    query: _query_pb2.AggregationQuery
    transaction: bytes
    explain_metrics: _query_profile_pb2.ExplainMetrics

    def __init__(self, batch: _Optional[_Union[_aggregation_result_pb2.AggregationResultBatch, _Mapping]]=..., query: _Optional[_Union[_query_pb2.AggregationQuery, _Mapping]]=..., transaction: _Optional[bytes]=..., explain_metrics: _Optional[_Union[_query_profile_pb2.ExplainMetrics, _Mapping]]=...) -> None:
        ...

class BeginTransactionRequest(_message.Message):
    __slots__ = ('project_id', 'database_id', 'transaction_options')
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    DATABASE_ID_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    database_id: str
    transaction_options: TransactionOptions

    def __init__(self, project_id: _Optional[str]=..., database_id: _Optional[str]=..., transaction_options: _Optional[_Union[TransactionOptions, _Mapping]]=...) -> None:
        ...

class BeginTransactionResponse(_message.Message):
    __slots__ = ('transaction',)
    TRANSACTION_FIELD_NUMBER: _ClassVar[int]
    transaction: bytes

    def __init__(self, transaction: _Optional[bytes]=...) -> None:
        ...

class RollbackRequest(_message.Message):
    __slots__ = ('project_id', 'database_id', 'transaction')
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    DATABASE_ID_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    database_id: str
    transaction: bytes

    def __init__(self, project_id: _Optional[str]=..., database_id: _Optional[str]=..., transaction: _Optional[bytes]=...) -> None:
        ...

class RollbackResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class CommitRequest(_message.Message):
    __slots__ = ('project_id', 'database_id', 'mode', 'transaction', 'single_use_transaction', 'mutations')

    class Mode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MODE_UNSPECIFIED: _ClassVar[CommitRequest.Mode]
        TRANSACTIONAL: _ClassVar[CommitRequest.Mode]
        NON_TRANSACTIONAL: _ClassVar[CommitRequest.Mode]
    MODE_UNSPECIFIED: CommitRequest.Mode
    TRANSACTIONAL: CommitRequest.Mode
    NON_TRANSACTIONAL: CommitRequest.Mode
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    DATABASE_ID_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_FIELD_NUMBER: _ClassVar[int]
    SINGLE_USE_TRANSACTION_FIELD_NUMBER: _ClassVar[int]
    MUTATIONS_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    database_id: str
    mode: CommitRequest.Mode
    transaction: bytes
    single_use_transaction: TransactionOptions
    mutations: _containers.RepeatedCompositeFieldContainer[Mutation]

    def __init__(self, project_id: _Optional[str]=..., database_id: _Optional[str]=..., mode: _Optional[_Union[CommitRequest.Mode, str]]=..., transaction: _Optional[bytes]=..., single_use_transaction: _Optional[_Union[TransactionOptions, _Mapping]]=..., mutations: _Optional[_Iterable[_Union[Mutation, _Mapping]]]=...) -> None:
        ...

class CommitResponse(_message.Message):
    __slots__ = ('mutation_results', 'index_updates', 'commit_time')
    MUTATION_RESULTS_FIELD_NUMBER: _ClassVar[int]
    INDEX_UPDATES_FIELD_NUMBER: _ClassVar[int]
    COMMIT_TIME_FIELD_NUMBER: _ClassVar[int]
    mutation_results: _containers.RepeatedCompositeFieldContainer[MutationResult]
    index_updates: int
    commit_time: _timestamp_pb2.Timestamp

    def __init__(self, mutation_results: _Optional[_Iterable[_Union[MutationResult, _Mapping]]]=..., index_updates: _Optional[int]=..., commit_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class AllocateIdsRequest(_message.Message):
    __slots__ = ('project_id', 'database_id', 'keys')
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    DATABASE_ID_FIELD_NUMBER: _ClassVar[int]
    KEYS_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    database_id: str
    keys: _containers.RepeatedCompositeFieldContainer[_entity_pb2.Key]

    def __init__(self, project_id: _Optional[str]=..., database_id: _Optional[str]=..., keys: _Optional[_Iterable[_Union[_entity_pb2.Key, _Mapping]]]=...) -> None:
        ...

class AllocateIdsResponse(_message.Message):
    __slots__ = ('keys',)
    KEYS_FIELD_NUMBER: _ClassVar[int]
    keys: _containers.RepeatedCompositeFieldContainer[_entity_pb2.Key]

    def __init__(self, keys: _Optional[_Iterable[_Union[_entity_pb2.Key, _Mapping]]]=...) -> None:
        ...

class ReserveIdsRequest(_message.Message):
    __slots__ = ('project_id', 'database_id', 'keys')
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    DATABASE_ID_FIELD_NUMBER: _ClassVar[int]
    KEYS_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    database_id: str
    keys: _containers.RepeatedCompositeFieldContainer[_entity_pb2.Key]

    def __init__(self, project_id: _Optional[str]=..., database_id: _Optional[str]=..., keys: _Optional[_Iterable[_Union[_entity_pb2.Key, _Mapping]]]=...) -> None:
        ...

class ReserveIdsResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class Mutation(_message.Message):
    __slots__ = ('insert', 'update', 'upsert', 'delete', 'base_version', 'update_time', 'conflict_resolution_strategy', 'property_mask', 'property_transforms')

    class ConflictResolutionStrategy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STRATEGY_UNSPECIFIED: _ClassVar[Mutation.ConflictResolutionStrategy]
        SERVER_VALUE: _ClassVar[Mutation.ConflictResolutionStrategy]
        FAIL: _ClassVar[Mutation.ConflictResolutionStrategy]
    STRATEGY_UNSPECIFIED: Mutation.ConflictResolutionStrategy
    SERVER_VALUE: Mutation.ConflictResolutionStrategy
    FAIL: Mutation.ConflictResolutionStrategy
    INSERT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_FIELD_NUMBER: _ClassVar[int]
    UPSERT_FIELD_NUMBER: _ClassVar[int]
    DELETE_FIELD_NUMBER: _ClassVar[int]
    BASE_VERSION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    CONFLICT_RESOLUTION_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_MASK_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_TRANSFORMS_FIELD_NUMBER: _ClassVar[int]
    insert: _entity_pb2.Entity
    update: _entity_pb2.Entity
    upsert: _entity_pb2.Entity
    delete: _entity_pb2.Key
    base_version: int
    update_time: _timestamp_pb2.Timestamp
    conflict_resolution_strategy: Mutation.ConflictResolutionStrategy
    property_mask: PropertyMask
    property_transforms: _containers.RepeatedCompositeFieldContainer[PropertyTransform]

    def __init__(self, insert: _Optional[_Union[_entity_pb2.Entity, _Mapping]]=..., update: _Optional[_Union[_entity_pb2.Entity, _Mapping]]=..., upsert: _Optional[_Union[_entity_pb2.Entity, _Mapping]]=..., delete: _Optional[_Union[_entity_pb2.Key, _Mapping]]=..., base_version: _Optional[int]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., conflict_resolution_strategy: _Optional[_Union[Mutation.ConflictResolutionStrategy, str]]=..., property_mask: _Optional[_Union[PropertyMask, _Mapping]]=..., property_transforms: _Optional[_Iterable[_Union[PropertyTransform, _Mapping]]]=...) -> None:
        ...

class PropertyTransform(_message.Message):
    __slots__ = ('property', 'set_to_server_value', 'increment', 'maximum', 'minimum', 'append_missing_elements', 'remove_all_from_array')

    class ServerValue(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SERVER_VALUE_UNSPECIFIED: _ClassVar[PropertyTransform.ServerValue]
        REQUEST_TIME: _ClassVar[PropertyTransform.ServerValue]
    SERVER_VALUE_UNSPECIFIED: PropertyTransform.ServerValue
    REQUEST_TIME: PropertyTransform.ServerValue
    PROPERTY_FIELD_NUMBER: _ClassVar[int]
    SET_TO_SERVER_VALUE_FIELD_NUMBER: _ClassVar[int]
    INCREMENT_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_FIELD_NUMBER: _ClassVar[int]
    APPEND_MISSING_ELEMENTS_FIELD_NUMBER: _ClassVar[int]
    REMOVE_ALL_FROM_ARRAY_FIELD_NUMBER: _ClassVar[int]
    property: str
    set_to_server_value: PropertyTransform.ServerValue
    increment: _entity_pb2.Value
    maximum: _entity_pb2.Value
    minimum: _entity_pb2.Value
    append_missing_elements: _entity_pb2.ArrayValue
    remove_all_from_array: _entity_pb2.ArrayValue

    def __init__(self, property: _Optional[str]=..., set_to_server_value: _Optional[_Union[PropertyTransform.ServerValue, str]]=..., increment: _Optional[_Union[_entity_pb2.Value, _Mapping]]=..., maximum: _Optional[_Union[_entity_pb2.Value, _Mapping]]=..., minimum: _Optional[_Union[_entity_pb2.Value, _Mapping]]=..., append_missing_elements: _Optional[_Union[_entity_pb2.ArrayValue, _Mapping]]=..., remove_all_from_array: _Optional[_Union[_entity_pb2.ArrayValue, _Mapping]]=...) -> None:
        ...

class MutationResult(_message.Message):
    __slots__ = ('key', 'version', 'create_time', 'update_time', 'conflict_detected', 'transform_results')
    KEY_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    CONFLICT_DETECTED_FIELD_NUMBER: _ClassVar[int]
    TRANSFORM_RESULTS_FIELD_NUMBER: _ClassVar[int]
    key: _entity_pb2.Key
    version: int
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    conflict_detected: bool
    transform_results: _containers.RepeatedCompositeFieldContainer[_entity_pb2.Value]

    def __init__(self, key: _Optional[_Union[_entity_pb2.Key, _Mapping]]=..., version: _Optional[int]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., conflict_detected: bool=..., transform_results: _Optional[_Iterable[_Union[_entity_pb2.Value, _Mapping]]]=...) -> None:
        ...

class PropertyMask(_message.Message):
    __slots__ = ('paths',)
    PATHS_FIELD_NUMBER: _ClassVar[int]
    paths: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, paths: _Optional[_Iterable[str]]=...) -> None:
        ...

class ReadOptions(_message.Message):
    __slots__ = ('read_consistency', 'transaction', 'new_transaction', 'read_time')

    class ReadConsistency(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        READ_CONSISTENCY_UNSPECIFIED: _ClassVar[ReadOptions.ReadConsistency]
        STRONG: _ClassVar[ReadOptions.ReadConsistency]
        EVENTUAL: _ClassVar[ReadOptions.ReadConsistency]
    READ_CONSISTENCY_UNSPECIFIED: ReadOptions.ReadConsistency
    STRONG: ReadOptions.ReadConsistency
    EVENTUAL: ReadOptions.ReadConsistency
    READ_CONSISTENCY_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_FIELD_NUMBER: _ClassVar[int]
    NEW_TRANSACTION_FIELD_NUMBER: _ClassVar[int]
    READ_TIME_FIELD_NUMBER: _ClassVar[int]
    read_consistency: ReadOptions.ReadConsistency
    transaction: bytes
    new_transaction: TransactionOptions
    read_time: _timestamp_pb2.Timestamp

    def __init__(self, read_consistency: _Optional[_Union[ReadOptions.ReadConsistency, str]]=..., transaction: _Optional[bytes]=..., new_transaction: _Optional[_Union[TransactionOptions, _Mapping]]=..., read_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class TransactionOptions(_message.Message):
    __slots__ = ('read_write', 'read_only')

    class ReadWrite(_message.Message):
        __slots__ = ('previous_transaction',)
        PREVIOUS_TRANSACTION_FIELD_NUMBER: _ClassVar[int]
        previous_transaction: bytes

        def __init__(self, previous_transaction: _Optional[bytes]=...) -> None:
            ...

    class ReadOnly(_message.Message):
        __slots__ = ('read_time',)
        READ_TIME_FIELD_NUMBER: _ClassVar[int]
        read_time: _timestamp_pb2.Timestamp

        def __init__(self, read_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
            ...
    READ_WRITE_FIELD_NUMBER: _ClassVar[int]
    READ_ONLY_FIELD_NUMBER: _ClassVar[int]
    read_write: TransactionOptions.ReadWrite
    read_only: TransactionOptions.ReadOnly

    def __init__(self, read_write: _Optional[_Union[TransactionOptions.ReadWrite, _Mapping]]=..., read_only: _Optional[_Union[TransactionOptions.ReadOnly, _Mapping]]=...) -> None:
        ...