from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.cloud.bigquery.v2 import table_reference_pb2 as _table_reference_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class PrimaryKey(_message.Message):
    __slots__ = ('columns',)
    COLUMNS_FIELD_NUMBER: _ClassVar[int]
    columns: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, columns: _Optional[_Iterable[str]]=...) -> None:
        ...

class ColumnReference(_message.Message):
    __slots__ = ('referencing_column', 'referenced_column')
    REFERENCING_COLUMN_FIELD_NUMBER: _ClassVar[int]
    REFERENCED_COLUMN_FIELD_NUMBER: _ClassVar[int]
    referencing_column: str
    referenced_column: str

    def __init__(self, referencing_column: _Optional[str]=..., referenced_column: _Optional[str]=...) -> None:
        ...

class ForeignKey(_message.Message):
    __slots__ = ('name', 'referenced_table', 'column_references')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REFERENCED_TABLE_FIELD_NUMBER: _ClassVar[int]
    COLUMN_REFERENCES_FIELD_NUMBER: _ClassVar[int]
    name: str
    referenced_table: _table_reference_pb2.TableReference
    column_references: _containers.RepeatedCompositeFieldContainer[ColumnReference]

    def __init__(self, name: _Optional[str]=..., referenced_table: _Optional[_Union[_table_reference_pb2.TableReference, _Mapping]]=..., column_references: _Optional[_Iterable[_Union[ColumnReference, _Mapping]]]=...) -> None:
        ...

class TableConstraints(_message.Message):
    __slots__ = ('primary_key', 'foreign_keys')
    PRIMARY_KEY_FIELD_NUMBER: _ClassVar[int]
    FOREIGN_KEYS_FIELD_NUMBER: _ClassVar[int]
    primary_key: PrimaryKey
    foreign_keys: _containers.RepeatedCompositeFieldContainer[ForeignKey]

    def __init__(self, primary_key: _Optional[_Union[PrimaryKey, _Mapping]]=..., foreign_keys: _Optional[_Iterable[_Union[ForeignKey, _Mapping]]]=...) -> None:
        ...