from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class StandardSqlDataType(_message.Message):
    __slots__ = ('type_kind', 'array_element_type', 'struct_type', 'range_element_type')

    class TypeKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_KIND_UNSPECIFIED: _ClassVar[StandardSqlDataType.TypeKind]
        INT64: _ClassVar[StandardSqlDataType.TypeKind]
        BOOL: _ClassVar[StandardSqlDataType.TypeKind]
        FLOAT64: _ClassVar[StandardSqlDataType.TypeKind]
        STRING: _ClassVar[StandardSqlDataType.TypeKind]
        BYTES: _ClassVar[StandardSqlDataType.TypeKind]
        TIMESTAMP: _ClassVar[StandardSqlDataType.TypeKind]
        DATE: _ClassVar[StandardSqlDataType.TypeKind]
        TIME: _ClassVar[StandardSqlDataType.TypeKind]
        DATETIME: _ClassVar[StandardSqlDataType.TypeKind]
        INTERVAL: _ClassVar[StandardSqlDataType.TypeKind]
        GEOGRAPHY: _ClassVar[StandardSqlDataType.TypeKind]
        NUMERIC: _ClassVar[StandardSqlDataType.TypeKind]
        BIGNUMERIC: _ClassVar[StandardSqlDataType.TypeKind]
        JSON: _ClassVar[StandardSqlDataType.TypeKind]
        ARRAY: _ClassVar[StandardSqlDataType.TypeKind]
        STRUCT: _ClassVar[StandardSqlDataType.TypeKind]
        RANGE: _ClassVar[StandardSqlDataType.TypeKind]
    TYPE_KIND_UNSPECIFIED: StandardSqlDataType.TypeKind
    INT64: StandardSqlDataType.TypeKind
    BOOL: StandardSqlDataType.TypeKind
    FLOAT64: StandardSqlDataType.TypeKind
    STRING: StandardSqlDataType.TypeKind
    BYTES: StandardSqlDataType.TypeKind
    TIMESTAMP: StandardSqlDataType.TypeKind
    DATE: StandardSqlDataType.TypeKind
    TIME: StandardSqlDataType.TypeKind
    DATETIME: StandardSqlDataType.TypeKind
    INTERVAL: StandardSqlDataType.TypeKind
    GEOGRAPHY: StandardSqlDataType.TypeKind
    NUMERIC: StandardSqlDataType.TypeKind
    BIGNUMERIC: StandardSqlDataType.TypeKind
    JSON: StandardSqlDataType.TypeKind
    ARRAY: StandardSqlDataType.TypeKind
    STRUCT: StandardSqlDataType.TypeKind
    RANGE: StandardSqlDataType.TypeKind
    TYPE_KIND_FIELD_NUMBER: _ClassVar[int]
    ARRAY_ELEMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    STRUCT_TYPE_FIELD_NUMBER: _ClassVar[int]
    RANGE_ELEMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    type_kind: StandardSqlDataType.TypeKind
    array_element_type: StandardSqlDataType
    struct_type: StandardSqlStructType
    range_element_type: StandardSqlDataType

    def __init__(self, type_kind: _Optional[_Union[StandardSqlDataType.TypeKind, str]]=..., array_element_type: _Optional[_Union[StandardSqlDataType, _Mapping]]=..., struct_type: _Optional[_Union[StandardSqlStructType, _Mapping]]=..., range_element_type: _Optional[_Union[StandardSqlDataType, _Mapping]]=...) -> None:
        ...

class StandardSqlField(_message.Message):
    __slots__ = ('name', 'type')
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: StandardSqlDataType

    def __init__(self, name: _Optional[str]=..., type: _Optional[_Union[StandardSqlDataType, _Mapping]]=...) -> None:
        ...

class StandardSqlStructType(_message.Message):
    __slots__ = ('fields',)
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    fields: _containers.RepeatedCompositeFieldContainer[StandardSqlField]

    def __init__(self, fields: _Optional[_Iterable[_Union[StandardSqlField, _Mapping]]]=...) -> None:
        ...

class StandardSqlTableType(_message.Message):
    __slots__ = ('columns',)
    COLUMNS_FIELD_NUMBER: _ClassVar[int]
    columns: _containers.RepeatedCompositeFieldContainer[StandardSqlField]

    def __init__(self, columns: _Optional[_Iterable[_Union[StandardSqlField, _Mapping]]]=...) -> None:
        ...