from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.bigtable.v2 import types_pb2 as _types_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.type import date_pb2 as _date_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Row(_message.Message):
    __slots__ = ('key', 'families')
    KEY_FIELD_NUMBER: _ClassVar[int]
    FAMILIES_FIELD_NUMBER: _ClassVar[int]
    key: bytes
    families: _containers.RepeatedCompositeFieldContainer[Family]

    def __init__(self, key: _Optional[bytes]=..., families: _Optional[_Iterable[_Union[Family, _Mapping]]]=...) -> None:
        ...

class Family(_message.Message):
    __slots__ = ('name', 'columns')
    NAME_FIELD_NUMBER: _ClassVar[int]
    COLUMNS_FIELD_NUMBER: _ClassVar[int]
    name: str
    columns: _containers.RepeatedCompositeFieldContainer[Column]

    def __init__(self, name: _Optional[str]=..., columns: _Optional[_Iterable[_Union[Column, _Mapping]]]=...) -> None:
        ...

class Column(_message.Message):
    __slots__ = ('qualifier', 'cells')
    QUALIFIER_FIELD_NUMBER: _ClassVar[int]
    CELLS_FIELD_NUMBER: _ClassVar[int]
    qualifier: bytes
    cells: _containers.RepeatedCompositeFieldContainer[Cell]

    def __init__(self, qualifier: _Optional[bytes]=..., cells: _Optional[_Iterable[_Union[Cell, _Mapping]]]=...) -> None:
        ...

class Cell(_message.Message):
    __slots__ = ('timestamp_micros', 'value', 'labels')
    TIMESTAMP_MICROS_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    timestamp_micros: int
    value: bytes
    labels: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, timestamp_micros: _Optional[int]=..., value: _Optional[bytes]=..., labels: _Optional[_Iterable[str]]=...) -> None:
        ...

class Value(_message.Message):
    __slots__ = ('type', 'raw_value', 'raw_timestamp_micros', 'bytes_value', 'string_value', 'int_value', 'bool_value', 'float_value', 'timestamp_value', 'date_value', 'array_value')
    TYPE_FIELD_NUMBER: _ClassVar[int]
    RAW_VALUE_FIELD_NUMBER: _ClassVar[int]
    RAW_TIMESTAMP_MICROS_FIELD_NUMBER: _ClassVar[int]
    BYTES_VALUE_FIELD_NUMBER: _ClassVar[int]
    STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
    INT_VALUE_FIELD_NUMBER: _ClassVar[int]
    BOOL_VALUE_FIELD_NUMBER: _ClassVar[int]
    FLOAT_VALUE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_VALUE_FIELD_NUMBER: _ClassVar[int]
    DATE_VALUE_FIELD_NUMBER: _ClassVar[int]
    ARRAY_VALUE_FIELD_NUMBER: _ClassVar[int]
    type: _types_pb2.Type
    raw_value: bytes
    raw_timestamp_micros: int
    bytes_value: bytes
    string_value: str
    int_value: int
    bool_value: bool
    float_value: float
    timestamp_value: _timestamp_pb2.Timestamp
    date_value: _date_pb2.Date
    array_value: ArrayValue

    def __init__(self, type: _Optional[_Union[_types_pb2.Type, _Mapping]]=..., raw_value: _Optional[bytes]=..., raw_timestamp_micros: _Optional[int]=..., bytes_value: _Optional[bytes]=..., string_value: _Optional[str]=..., int_value: _Optional[int]=..., bool_value: bool=..., float_value: _Optional[float]=..., timestamp_value: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., date_value: _Optional[_Union[_date_pb2.Date, _Mapping]]=..., array_value: _Optional[_Union[ArrayValue, _Mapping]]=...) -> None:
        ...

class ArrayValue(_message.Message):
    __slots__ = ('values',)
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedCompositeFieldContainer[Value]

    def __init__(self, values: _Optional[_Iterable[_Union[Value, _Mapping]]]=...) -> None:
        ...

class RowRange(_message.Message):
    __slots__ = ('start_key_closed', 'start_key_open', 'end_key_open', 'end_key_closed')
    START_KEY_CLOSED_FIELD_NUMBER: _ClassVar[int]
    START_KEY_OPEN_FIELD_NUMBER: _ClassVar[int]
    END_KEY_OPEN_FIELD_NUMBER: _ClassVar[int]
    END_KEY_CLOSED_FIELD_NUMBER: _ClassVar[int]
    start_key_closed: bytes
    start_key_open: bytes
    end_key_open: bytes
    end_key_closed: bytes

    def __init__(self, start_key_closed: _Optional[bytes]=..., start_key_open: _Optional[bytes]=..., end_key_open: _Optional[bytes]=..., end_key_closed: _Optional[bytes]=...) -> None:
        ...

class RowSet(_message.Message):
    __slots__ = ('row_keys', 'row_ranges')
    ROW_KEYS_FIELD_NUMBER: _ClassVar[int]
    ROW_RANGES_FIELD_NUMBER: _ClassVar[int]
    row_keys: _containers.RepeatedScalarFieldContainer[bytes]
    row_ranges: _containers.RepeatedCompositeFieldContainer[RowRange]

    def __init__(self, row_keys: _Optional[_Iterable[bytes]]=..., row_ranges: _Optional[_Iterable[_Union[RowRange, _Mapping]]]=...) -> None:
        ...

class ColumnRange(_message.Message):
    __slots__ = ('family_name', 'start_qualifier_closed', 'start_qualifier_open', 'end_qualifier_closed', 'end_qualifier_open')
    FAMILY_NAME_FIELD_NUMBER: _ClassVar[int]
    START_QUALIFIER_CLOSED_FIELD_NUMBER: _ClassVar[int]
    START_QUALIFIER_OPEN_FIELD_NUMBER: _ClassVar[int]
    END_QUALIFIER_CLOSED_FIELD_NUMBER: _ClassVar[int]
    END_QUALIFIER_OPEN_FIELD_NUMBER: _ClassVar[int]
    family_name: str
    start_qualifier_closed: bytes
    start_qualifier_open: bytes
    end_qualifier_closed: bytes
    end_qualifier_open: bytes

    def __init__(self, family_name: _Optional[str]=..., start_qualifier_closed: _Optional[bytes]=..., start_qualifier_open: _Optional[bytes]=..., end_qualifier_closed: _Optional[bytes]=..., end_qualifier_open: _Optional[bytes]=...) -> None:
        ...

class TimestampRange(_message.Message):
    __slots__ = ('start_timestamp_micros', 'end_timestamp_micros')
    START_TIMESTAMP_MICROS_FIELD_NUMBER: _ClassVar[int]
    END_TIMESTAMP_MICROS_FIELD_NUMBER: _ClassVar[int]
    start_timestamp_micros: int
    end_timestamp_micros: int

    def __init__(self, start_timestamp_micros: _Optional[int]=..., end_timestamp_micros: _Optional[int]=...) -> None:
        ...

class ValueRange(_message.Message):
    __slots__ = ('start_value_closed', 'start_value_open', 'end_value_closed', 'end_value_open')
    START_VALUE_CLOSED_FIELD_NUMBER: _ClassVar[int]
    START_VALUE_OPEN_FIELD_NUMBER: _ClassVar[int]
    END_VALUE_CLOSED_FIELD_NUMBER: _ClassVar[int]
    END_VALUE_OPEN_FIELD_NUMBER: _ClassVar[int]
    start_value_closed: bytes
    start_value_open: bytes
    end_value_closed: bytes
    end_value_open: bytes

    def __init__(self, start_value_closed: _Optional[bytes]=..., start_value_open: _Optional[bytes]=..., end_value_closed: _Optional[bytes]=..., end_value_open: _Optional[bytes]=...) -> None:
        ...

class RowFilter(_message.Message):
    __slots__ = ('chain', 'interleave', 'condition', 'sink', 'pass_all_filter', 'block_all_filter', 'row_key_regex_filter', 'row_sample_filter', 'family_name_regex_filter', 'column_qualifier_regex_filter', 'column_range_filter', 'timestamp_range_filter', 'value_regex_filter', 'value_range_filter', 'cells_per_row_offset_filter', 'cells_per_row_limit_filter', 'cells_per_column_limit_filter', 'strip_value_transformer', 'apply_label_transformer')

    class Chain(_message.Message):
        __slots__ = ('filters',)
        FILTERS_FIELD_NUMBER: _ClassVar[int]
        filters: _containers.RepeatedCompositeFieldContainer[RowFilter]

        def __init__(self, filters: _Optional[_Iterable[_Union[RowFilter, _Mapping]]]=...) -> None:
            ...

    class Interleave(_message.Message):
        __slots__ = ('filters',)
        FILTERS_FIELD_NUMBER: _ClassVar[int]
        filters: _containers.RepeatedCompositeFieldContainer[RowFilter]

        def __init__(self, filters: _Optional[_Iterable[_Union[RowFilter, _Mapping]]]=...) -> None:
            ...

    class Condition(_message.Message):
        __slots__ = ('predicate_filter', 'true_filter', 'false_filter')
        PREDICATE_FILTER_FIELD_NUMBER: _ClassVar[int]
        TRUE_FILTER_FIELD_NUMBER: _ClassVar[int]
        FALSE_FILTER_FIELD_NUMBER: _ClassVar[int]
        predicate_filter: RowFilter
        true_filter: RowFilter
        false_filter: RowFilter

        def __init__(self, predicate_filter: _Optional[_Union[RowFilter, _Mapping]]=..., true_filter: _Optional[_Union[RowFilter, _Mapping]]=..., false_filter: _Optional[_Union[RowFilter, _Mapping]]=...) -> None:
            ...
    CHAIN_FIELD_NUMBER: _ClassVar[int]
    INTERLEAVE_FIELD_NUMBER: _ClassVar[int]
    CONDITION_FIELD_NUMBER: _ClassVar[int]
    SINK_FIELD_NUMBER: _ClassVar[int]
    PASS_ALL_FILTER_FIELD_NUMBER: _ClassVar[int]
    BLOCK_ALL_FILTER_FIELD_NUMBER: _ClassVar[int]
    ROW_KEY_REGEX_FILTER_FIELD_NUMBER: _ClassVar[int]
    ROW_SAMPLE_FILTER_FIELD_NUMBER: _ClassVar[int]
    FAMILY_NAME_REGEX_FILTER_FIELD_NUMBER: _ClassVar[int]
    COLUMN_QUALIFIER_REGEX_FILTER_FIELD_NUMBER: _ClassVar[int]
    COLUMN_RANGE_FILTER_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_RANGE_FILTER_FIELD_NUMBER: _ClassVar[int]
    VALUE_REGEX_FILTER_FIELD_NUMBER: _ClassVar[int]
    VALUE_RANGE_FILTER_FIELD_NUMBER: _ClassVar[int]
    CELLS_PER_ROW_OFFSET_FILTER_FIELD_NUMBER: _ClassVar[int]
    CELLS_PER_ROW_LIMIT_FILTER_FIELD_NUMBER: _ClassVar[int]
    CELLS_PER_COLUMN_LIMIT_FILTER_FIELD_NUMBER: _ClassVar[int]
    STRIP_VALUE_TRANSFORMER_FIELD_NUMBER: _ClassVar[int]
    APPLY_LABEL_TRANSFORMER_FIELD_NUMBER: _ClassVar[int]
    chain: RowFilter.Chain
    interleave: RowFilter.Interleave
    condition: RowFilter.Condition
    sink: bool
    pass_all_filter: bool
    block_all_filter: bool
    row_key_regex_filter: bytes
    row_sample_filter: float
    family_name_regex_filter: str
    column_qualifier_regex_filter: bytes
    column_range_filter: ColumnRange
    timestamp_range_filter: TimestampRange
    value_regex_filter: bytes
    value_range_filter: ValueRange
    cells_per_row_offset_filter: int
    cells_per_row_limit_filter: int
    cells_per_column_limit_filter: int
    strip_value_transformer: bool
    apply_label_transformer: str

    def __init__(self, chain: _Optional[_Union[RowFilter.Chain, _Mapping]]=..., interleave: _Optional[_Union[RowFilter.Interleave, _Mapping]]=..., condition: _Optional[_Union[RowFilter.Condition, _Mapping]]=..., sink: bool=..., pass_all_filter: bool=..., block_all_filter: bool=..., row_key_regex_filter: _Optional[bytes]=..., row_sample_filter: _Optional[float]=..., family_name_regex_filter: _Optional[str]=..., column_qualifier_regex_filter: _Optional[bytes]=..., column_range_filter: _Optional[_Union[ColumnRange, _Mapping]]=..., timestamp_range_filter: _Optional[_Union[TimestampRange, _Mapping]]=..., value_regex_filter: _Optional[bytes]=..., value_range_filter: _Optional[_Union[ValueRange, _Mapping]]=..., cells_per_row_offset_filter: _Optional[int]=..., cells_per_row_limit_filter: _Optional[int]=..., cells_per_column_limit_filter: _Optional[int]=..., strip_value_transformer: bool=..., apply_label_transformer: _Optional[str]=...) -> None:
        ...

class Mutation(_message.Message):
    __slots__ = ('set_cell', 'add_to_cell', 'merge_to_cell', 'delete_from_column', 'delete_from_family', 'delete_from_row')

    class SetCell(_message.Message):
        __slots__ = ('family_name', 'column_qualifier', 'timestamp_micros', 'value')
        FAMILY_NAME_FIELD_NUMBER: _ClassVar[int]
        COLUMN_QUALIFIER_FIELD_NUMBER: _ClassVar[int]
        TIMESTAMP_MICROS_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        family_name: str
        column_qualifier: bytes
        timestamp_micros: int
        value: bytes

        def __init__(self, family_name: _Optional[str]=..., column_qualifier: _Optional[bytes]=..., timestamp_micros: _Optional[int]=..., value: _Optional[bytes]=...) -> None:
            ...

    class AddToCell(_message.Message):
        __slots__ = ('family_name', 'column_qualifier', 'timestamp', 'input')
        FAMILY_NAME_FIELD_NUMBER: _ClassVar[int]
        COLUMN_QUALIFIER_FIELD_NUMBER: _ClassVar[int]
        TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        INPUT_FIELD_NUMBER: _ClassVar[int]
        family_name: str
        column_qualifier: Value
        timestamp: Value
        input: Value

        def __init__(self, family_name: _Optional[str]=..., column_qualifier: _Optional[_Union[Value, _Mapping]]=..., timestamp: _Optional[_Union[Value, _Mapping]]=..., input: _Optional[_Union[Value, _Mapping]]=...) -> None:
            ...

    class MergeToCell(_message.Message):
        __slots__ = ('family_name', 'column_qualifier', 'timestamp', 'input')
        FAMILY_NAME_FIELD_NUMBER: _ClassVar[int]
        COLUMN_QUALIFIER_FIELD_NUMBER: _ClassVar[int]
        TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        INPUT_FIELD_NUMBER: _ClassVar[int]
        family_name: str
        column_qualifier: Value
        timestamp: Value
        input: Value

        def __init__(self, family_name: _Optional[str]=..., column_qualifier: _Optional[_Union[Value, _Mapping]]=..., timestamp: _Optional[_Union[Value, _Mapping]]=..., input: _Optional[_Union[Value, _Mapping]]=...) -> None:
            ...

    class DeleteFromColumn(_message.Message):
        __slots__ = ('family_name', 'column_qualifier', 'time_range')
        FAMILY_NAME_FIELD_NUMBER: _ClassVar[int]
        COLUMN_QUALIFIER_FIELD_NUMBER: _ClassVar[int]
        TIME_RANGE_FIELD_NUMBER: _ClassVar[int]
        family_name: str
        column_qualifier: bytes
        time_range: TimestampRange

        def __init__(self, family_name: _Optional[str]=..., column_qualifier: _Optional[bytes]=..., time_range: _Optional[_Union[TimestampRange, _Mapping]]=...) -> None:
            ...

    class DeleteFromFamily(_message.Message):
        __slots__ = ('family_name',)
        FAMILY_NAME_FIELD_NUMBER: _ClassVar[int]
        family_name: str

        def __init__(self, family_name: _Optional[str]=...) -> None:
            ...

    class DeleteFromRow(_message.Message):
        __slots__ = ()

        def __init__(self) -> None:
            ...
    SET_CELL_FIELD_NUMBER: _ClassVar[int]
    ADD_TO_CELL_FIELD_NUMBER: _ClassVar[int]
    MERGE_TO_CELL_FIELD_NUMBER: _ClassVar[int]
    DELETE_FROM_COLUMN_FIELD_NUMBER: _ClassVar[int]
    DELETE_FROM_FAMILY_FIELD_NUMBER: _ClassVar[int]
    DELETE_FROM_ROW_FIELD_NUMBER: _ClassVar[int]
    set_cell: Mutation.SetCell
    add_to_cell: Mutation.AddToCell
    merge_to_cell: Mutation.MergeToCell
    delete_from_column: Mutation.DeleteFromColumn
    delete_from_family: Mutation.DeleteFromFamily
    delete_from_row: Mutation.DeleteFromRow

    def __init__(self, set_cell: _Optional[_Union[Mutation.SetCell, _Mapping]]=..., add_to_cell: _Optional[_Union[Mutation.AddToCell, _Mapping]]=..., merge_to_cell: _Optional[_Union[Mutation.MergeToCell, _Mapping]]=..., delete_from_column: _Optional[_Union[Mutation.DeleteFromColumn, _Mapping]]=..., delete_from_family: _Optional[_Union[Mutation.DeleteFromFamily, _Mapping]]=..., delete_from_row: _Optional[_Union[Mutation.DeleteFromRow, _Mapping]]=...) -> None:
        ...

class ReadModifyWriteRule(_message.Message):
    __slots__ = ('family_name', 'column_qualifier', 'append_value', 'increment_amount')
    FAMILY_NAME_FIELD_NUMBER: _ClassVar[int]
    COLUMN_QUALIFIER_FIELD_NUMBER: _ClassVar[int]
    APPEND_VALUE_FIELD_NUMBER: _ClassVar[int]
    INCREMENT_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    family_name: str
    column_qualifier: bytes
    append_value: bytes
    increment_amount: int

    def __init__(self, family_name: _Optional[str]=..., column_qualifier: _Optional[bytes]=..., append_value: _Optional[bytes]=..., increment_amount: _Optional[int]=...) -> None:
        ...

class StreamPartition(_message.Message):
    __slots__ = ('row_range',)
    ROW_RANGE_FIELD_NUMBER: _ClassVar[int]
    row_range: RowRange

    def __init__(self, row_range: _Optional[_Union[RowRange, _Mapping]]=...) -> None:
        ...

class StreamContinuationTokens(_message.Message):
    __slots__ = ('tokens',)
    TOKENS_FIELD_NUMBER: _ClassVar[int]
    tokens: _containers.RepeatedCompositeFieldContainer[StreamContinuationToken]

    def __init__(self, tokens: _Optional[_Iterable[_Union[StreamContinuationToken, _Mapping]]]=...) -> None:
        ...

class StreamContinuationToken(_message.Message):
    __slots__ = ('partition', 'token')
    PARTITION_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    partition: StreamPartition
    token: str

    def __init__(self, partition: _Optional[_Union[StreamPartition, _Mapping]]=..., token: _Optional[str]=...) -> None:
        ...

class ProtoFormat(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class ColumnMetadata(_message.Message):
    __slots__ = ('name', 'type')
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: _types_pb2.Type

    def __init__(self, name: _Optional[str]=..., type: _Optional[_Union[_types_pb2.Type, _Mapping]]=...) -> None:
        ...

class ProtoSchema(_message.Message):
    __slots__ = ('columns',)
    COLUMNS_FIELD_NUMBER: _ClassVar[int]
    columns: _containers.RepeatedCompositeFieldContainer[ColumnMetadata]

    def __init__(self, columns: _Optional[_Iterable[_Union[ColumnMetadata, _Mapping]]]=...) -> None:
        ...

class ResultSetMetadata(_message.Message):
    __slots__ = ('proto_schema',)
    PROTO_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    proto_schema: ProtoSchema

    def __init__(self, proto_schema: _Optional[_Union[ProtoSchema, _Mapping]]=...) -> None:
        ...

class ProtoRows(_message.Message):
    __slots__ = ('values',)
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedCompositeFieldContainer[Value]

    def __init__(self, values: _Optional[_Iterable[_Union[Value, _Mapping]]]=...) -> None:
        ...

class ProtoRowsBatch(_message.Message):
    __slots__ = ('batch_data',)
    BATCH_DATA_FIELD_NUMBER: _ClassVar[int]
    batch_data: bytes

    def __init__(self, batch_data: _Optional[bytes]=...) -> None:
        ...

class PartialResultSet(_message.Message):
    __slots__ = ('proto_rows_batch', 'resume_token', 'estimated_batch_size')
    PROTO_ROWS_BATCH_FIELD_NUMBER: _ClassVar[int]
    RESUME_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ESTIMATED_BATCH_SIZE_FIELD_NUMBER: _ClassVar[int]
    proto_rows_batch: ProtoRowsBatch
    resume_token: bytes
    estimated_batch_size: int

    def __init__(self, proto_rows_batch: _Optional[_Union[ProtoRowsBatch, _Mapping]]=..., resume_token: _Optional[bytes]=..., estimated_batch_size: _Optional[int]=...) -> None:
        ...