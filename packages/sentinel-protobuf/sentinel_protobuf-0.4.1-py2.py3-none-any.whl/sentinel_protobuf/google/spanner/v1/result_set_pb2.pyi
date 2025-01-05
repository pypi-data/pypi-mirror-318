from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.spanner.v1 import query_plan_pb2 as _query_plan_pb2
from google.spanner.v1 import transaction_pb2 as _transaction_pb2
from google.spanner.v1 import type_pb2 as _type_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ResultSet(_message.Message):
    __slots__ = ('metadata', 'rows', 'stats', 'precommit_token')
    METADATA_FIELD_NUMBER: _ClassVar[int]
    ROWS_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    PRECOMMIT_TOKEN_FIELD_NUMBER: _ClassVar[int]
    metadata: ResultSetMetadata
    rows: _containers.RepeatedCompositeFieldContainer[_struct_pb2.ListValue]
    stats: ResultSetStats
    precommit_token: _transaction_pb2.MultiplexedSessionPrecommitToken

    def __init__(self, metadata: _Optional[_Union[ResultSetMetadata, _Mapping]]=..., rows: _Optional[_Iterable[_Union[_struct_pb2.ListValue, _Mapping]]]=..., stats: _Optional[_Union[ResultSetStats, _Mapping]]=..., precommit_token: _Optional[_Union[_transaction_pb2.MultiplexedSessionPrecommitToken, _Mapping]]=...) -> None:
        ...

class PartialResultSet(_message.Message):
    __slots__ = ('metadata', 'values', 'chunked_value', 'resume_token', 'stats', 'precommit_token')
    METADATA_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    CHUNKED_VALUE_FIELD_NUMBER: _ClassVar[int]
    RESUME_TOKEN_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    PRECOMMIT_TOKEN_FIELD_NUMBER: _ClassVar[int]
    metadata: ResultSetMetadata
    values: _containers.RepeatedCompositeFieldContainer[_struct_pb2.Value]
    chunked_value: bool
    resume_token: bytes
    stats: ResultSetStats
    precommit_token: _transaction_pb2.MultiplexedSessionPrecommitToken

    def __init__(self, metadata: _Optional[_Union[ResultSetMetadata, _Mapping]]=..., values: _Optional[_Iterable[_Union[_struct_pb2.Value, _Mapping]]]=..., chunked_value: bool=..., resume_token: _Optional[bytes]=..., stats: _Optional[_Union[ResultSetStats, _Mapping]]=..., precommit_token: _Optional[_Union[_transaction_pb2.MultiplexedSessionPrecommitToken, _Mapping]]=...) -> None:
        ...

class ResultSetMetadata(_message.Message):
    __slots__ = ('row_type', 'transaction', 'undeclared_parameters')
    ROW_TYPE_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_FIELD_NUMBER: _ClassVar[int]
    UNDECLARED_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    row_type: _type_pb2.StructType
    transaction: _transaction_pb2.Transaction
    undeclared_parameters: _type_pb2.StructType

    def __init__(self, row_type: _Optional[_Union[_type_pb2.StructType, _Mapping]]=..., transaction: _Optional[_Union[_transaction_pb2.Transaction, _Mapping]]=..., undeclared_parameters: _Optional[_Union[_type_pb2.StructType, _Mapping]]=...) -> None:
        ...

class ResultSetStats(_message.Message):
    __slots__ = ('query_plan', 'query_stats', 'row_count_exact', 'row_count_lower_bound')
    QUERY_PLAN_FIELD_NUMBER: _ClassVar[int]
    QUERY_STATS_FIELD_NUMBER: _ClassVar[int]
    ROW_COUNT_EXACT_FIELD_NUMBER: _ClassVar[int]
    ROW_COUNT_LOWER_BOUND_FIELD_NUMBER: _ClassVar[int]
    query_plan: _query_plan_pb2.QueryPlan
    query_stats: _struct_pb2.Struct
    row_count_exact: int
    row_count_lower_bound: int

    def __init__(self, query_plan: _Optional[_Union[_query_plan_pb2.QueryPlan, _Mapping]]=..., query_stats: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=..., row_count_exact: _Optional[int]=..., row_count_lower_bound: _Optional[int]=...) -> None:
        ...