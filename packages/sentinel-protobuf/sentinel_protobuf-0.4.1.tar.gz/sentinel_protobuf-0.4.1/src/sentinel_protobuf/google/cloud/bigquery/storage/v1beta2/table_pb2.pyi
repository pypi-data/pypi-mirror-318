from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class TableSchema(_message.Message):
    __slots__ = ('fields',)
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    fields: _containers.RepeatedCompositeFieldContainer[TableFieldSchema]

    def __init__(self, fields: _Optional[_Iterable[_Union[TableFieldSchema, _Mapping]]]=...) -> None:
        ...

class TableFieldSchema(_message.Message):
    __slots__ = ('name', 'type', 'mode', 'fields', 'description')

    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[TableFieldSchema.Type]
        STRING: _ClassVar[TableFieldSchema.Type]
        INT64: _ClassVar[TableFieldSchema.Type]
        DOUBLE: _ClassVar[TableFieldSchema.Type]
        STRUCT: _ClassVar[TableFieldSchema.Type]
        BYTES: _ClassVar[TableFieldSchema.Type]
        BOOL: _ClassVar[TableFieldSchema.Type]
        TIMESTAMP: _ClassVar[TableFieldSchema.Type]
        DATE: _ClassVar[TableFieldSchema.Type]
        TIME: _ClassVar[TableFieldSchema.Type]
        DATETIME: _ClassVar[TableFieldSchema.Type]
        GEOGRAPHY: _ClassVar[TableFieldSchema.Type]
        NUMERIC: _ClassVar[TableFieldSchema.Type]
        BIGNUMERIC: _ClassVar[TableFieldSchema.Type]
        INTERVAL: _ClassVar[TableFieldSchema.Type]
        JSON: _ClassVar[TableFieldSchema.Type]
    TYPE_UNSPECIFIED: TableFieldSchema.Type
    STRING: TableFieldSchema.Type
    INT64: TableFieldSchema.Type
    DOUBLE: TableFieldSchema.Type
    STRUCT: TableFieldSchema.Type
    BYTES: TableFieldSchema.Type
    BOOL: TableFieldSchema.Type
    TIMESTAMP: TableFieldSchema.Type
    DATE: TableFieldSchema.Type
    TIME: TableFieldSchema.Type
    DATETIME: TableFieldSchema.Type
    GEOGRAPHY: TableFieldSchema.Type
    NUMERIC: TableFieldSchema.Type
    BIGNUMERIC: TableFieldSchema.Type
    INTERVAL: TableFieldSchema.Type
    JSON: TableFieldSchema.Type

    class Mode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MODE_UNSPECIFIED: _ClassVar[TableFieldSchema.Mode]
        NULLABLE: _ClassVar[TableFieldSchema.Mode]
        REQUIRED: _ClassVar[TableFieldSchema.Mode]
        REPEATED: _ClassVar[TableFieldSchema.Mode]
    MODE_UNSPECIFIED: TableFieldSchema.Mode
    NULLABLE: TableFieldSchema.Mode
    REQUIRED: TableFieldSchema.Mode
    REPEATED: TableFieldSchema.Mode
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: TableFieldSchema.Type
    mode: TableFieldSchema.Mode
    fields: _containers.RepeatedCompositeFieldContainer[TableFieldSchema]
    description: str

    def __init__(self, name: _Optional[str]=..., type: _Optional[_Union[TableFieldSchema.Type, str]]=..., mode: _Optional[_Union[TableFieldSchema.Mode, str]]=..., fields: _Optional[_Iterable[_Union[TableFieldSchema, _Mapping]]]=..., description: _Optional[str]=...) -> None:
        ...