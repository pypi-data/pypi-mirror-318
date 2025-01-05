from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Schema(_message.Message):
    __slots__ = ('columns',)
    COLUMNS_FIELD_NUMBER: _ClassVar[int]
    columns: _containers.RepeatedCompositeFieldContainer[ColumnSchema]

    def __init__(self, columns: _Optional[_Iterable[_Union[ColumnSchema, _Mapping]]]=...) -> None:
        ...

class ColumnSchema(_message.Message):
    __slots__ = ('column', 'type', 'description', 'mode', 'default_value', 'ordinal_position', 'highest_indexing_type', 'subcolumns', 'looker_column_spec', 'range_element_type', 'gc_rule')

    class IndexingType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        INDEXING_TYPE_UNSPECIFIED: _ClassVar[ColumnSchema.IndexingType]
        INDEXING_TYPE_NONE: _ClassVar[ColumnSchema.IndexingType]
        INDEXING_TYPE_NON_UNIQUE: _ClassVar[ColumnSchema.IndexingType]
        INDEXING_TYPE_UNIQUE: _ClassVar[ColumnSchema.IndexingType]
        INDEXING_TYPE_PRIMARY_KEY: _ClassVar[ColumnSchema.IndexingType]
    INDEXING_TYPE_UNSPECIFIED: ColumnSchema.IndexingType
    INDEXING_TYPE_NONE: ColumnSchema.IndexingType
    INDEXING_TYPE_NON_UNIQUE: ColumnSchema.IndexingType
    INDEXING_TYPE_UNIQUE: ColumnSchema.IndexingType
    INDEXING_TYPE_PRIMARY_KEY: ColumnSchema.IndexingType

    class LookerColumnSpec(_message.Message):
        __slots__ = ('type',)

        class LookerColumnType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            LOOKER_COLUMN_TYPE_UNSPECIFIED: _ClassVar[ColumnSchema.LookerColumnSpec.LookerColumnType]
            DIMENSION: _ClassVar[ColumnSchema.LookerColumnSpec.LookerColumnType]
            DIMENSION_GROUP: _ClassVar[ColumnSchema.LookerColumnSpec.LookerColumnType]
            FILTER: _ClassVar[ColumnSchema.LookerColumnSpec.LookerColumnType]
            MEASURE: _ClassVar[ColumnSchema.LookerColumnSpec.LookerColumnType]
            PARAMETER: _ClassVar[ColumnSchema.LookerColumnSpec.LookerColumnType]
        LOOKER_COLUMN_TYPE_UNSPECIFIED: ColumnSchema.LookerColumnSpec.LookerColumnType
        DIMENSION: ColumnSchema.LookerColumnSpec.LookerColumnType
        DIMENSION_GROUP: ColumnSchema.LookerColumnSpec.LookerColumnType
        FILTER: ColumnSchema.LookerColumnSpec.LookerColumnType
        MEASURE: ColumnSchema.LookerColumnSpec.LookerColumnType
        PARAMETER: ColumnSchema.LookerColumnSpec.LookerColumnType
        TYPE_FIELD_NUMBER: _ClassVar[int]
        type: ColumnSchema.LookerColumnSpec.LookerColumnType

        def __init__(self, type: _Optional[_Union[ColumnSchema.LookerColumnSpec.LookerColumnType, str]]=...) -> None:
            ...

    class FieldElementType(_message.Message):
        __slots__ = ('type',)
        TYPE_FIELD_NUMBER: _ClassVar[int]
        type: str

        def __init__(self, type: _Optional[str]=...) -> None:
            ...
    COLUMN_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_VALUE_FIELD_NUMBER: _ClassVar[int]
    ORDINAL_POSITION_FIELD_NUMBER: _ClassVar[int]
    HIGHEST_INDEXING_TYPE_FIELD_NUMBER: _ClassVar[int]
    SUBCOLUMNS_FIELD_NUMBER: _ClassVar[int]
    LOOKER_COLUMN_SPEC_FIELD_NUMBER: _ClassVar[int]
    RANGE_ELEMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    GC_RULE_FIELD_NUMBER: _ClassVar[int]
    column: str
    type: str
    description: str
    mode: str
    default_value: str
    ordinal_position: int
    highest_indexing_type: ColumnSchema.IndexingType
    subcolumns: _containers.RepeatedCompositeFieldContainer[ColumnSchema]
    looker_column_spec: ColumnSchema.LookerColumnSpec
    range_element_type: ColumnSchema.FieldElementType
    gc_rule: str

    def __init__(self, column: _Optional[str]=..., type: _Optional[str]=..., description: _Optional[str]=..., mode: _Optional[str]=..., default_value: _Optional[str]=..., ordinal_position: _Optional[int]=..., highest_indexing_type: _Optional[_Union[ColumnSchema.IndexingType, str]]=..., subcolumns: _Optional[_Iterable[_Union[ColumnSchema, _Mapping]]]=..., looker_column_spec: _Optional[_Union[ColumnSchema.LookerColumnSpec, _Mapping]]=..., range_element_type: _Optional[_Union[ColumnSchema.FieldElementType, _Mapping]]=..., gc_rule: _Optional[str]=...) -> None:
        ...