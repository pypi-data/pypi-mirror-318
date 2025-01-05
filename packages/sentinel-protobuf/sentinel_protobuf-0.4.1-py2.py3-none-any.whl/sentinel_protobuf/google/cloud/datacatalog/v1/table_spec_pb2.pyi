from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class TableSourceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TABLE_SOURCE_TYPE_UNSPECIFIED: _ClassVar[TableSourceType]
    BIGQUERY_VIEW: _ClassVar[TableSourceType]
    BIGQUERY_TABLE: _ClassVar[TableSourceType]
    BIGQUERY_MATERIALIZED_VIEW: _ClassVar[TableSourceType]
TABLE_SOURCE_TYPE_UNSPECIFIED: TableSourceType
BIGQUERY_VIEW: TableSourceType
BIGQUERY_TABLE: TableSourceType
BIGQUERY_MATERIALIZED_VIEW: TableSourceType

class BigQueryTableSpec(_message.Message):
    __slots__ = ('table_source_type', 'view_spec', 'table_spec')
    TABLE_SOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    VIEW_SPEC_FIELD_NUMBER: _ClassVar[int]
    TABLE_SPEC_FIELD_NUMBER: _ClassVar[int]
    table_source_type: TableSourceType
    view_spec: ViewSpec
    table_spec: TableSpec

    def __init__(self, table_source_type: _Optional[_Union[TableSourceType, str]]=..., view_spec: _Optional[_Union[ViewSpec, _Mapping]]=..., table_spec: _Optional[_Union[TableSpec, _Mapping]]=...) -> None:
        ...

class ViewSpec(_message.Message):
    __slots__ = ('view_query',)
    VIEW_QUERY_FIELD_NUMBER: _ClassVar[int]
    view_query: str

    def __init__(self, view_query: _Optional[str]=...) -> None:
        ...

class TableSpec(_message.Message):
    __slots__ = ('grouped_entry',)
    GROUPED_ENTRY_FIELD_NUMBER: _ClassVar[int]
    grouped_entry: str

    def __init__(self, grouped_entry: _Optional[str]=...) -> None:
        ...

class BigQueryDateShardedSpec(_message.Message):
    __slots__ = ('dataset', 'table_prefix', 'shard_count', 'latest_shard_resource')
    DATASET_FIELD_NUMBER: _ClassVar[int]
    TABLE_PREFIX_FIELD_NUMBER: _ClassVar[int]
    SHARD_COUNT_FIELD_NUMBER: _ClassVar[int]
    LATEST_SHARD_RESOURCE_FIELD_NUMBER: _ClassVar[int]
    dataset: str
    table_prefix: str
    shard_count: int
    latest_shard_resource: str

    def __init__(self, dataset: _Optional[str]=..., table_prefix: _Optional[str]=..., shard_count: _Optional[int]=..., latest_shard_resource: _Optional[str]=...) -> None:
        ...