from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class TypeCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TYPE_CODE_UNSPECIFIED: _ClassVar[TypeCode]
    BOOL: _ClassVar[TypeCode]
    INT64: _ClassVar[TypeCode]
    FLOAT64: _ClassVar[TypeCode]
    FLOAT32: _ClassVar[TypeCode]
    TIMESTAMP: _ClassVar[TypeCode]
    DATE: _ClassVar[TypeCode]
    STRING: _ClassVar[TypeCode]
    BYTES: _ClassVar[TypeCode]
    ARRAY: _ClassVar[TypeCode]
    STRUCT: _ClassVar[TypeCode]
    NUMERIC: _ClassVar[TypeCode]
    JSON: _ClassVar[TypeCode]
    PROTO: _ClassVar[TypeCode]
    ENUM: _ClassVar[TypeCode]
    INTERVAL: _ClassVar[TypeCode]
    UUID: _ClassVar[TypeCode]

class TypeAnnotationCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TYPE_ANNOTATION_CODE_UNSPECIFIED: _ClassVar[TypeAnnotationCode]
    PG_NUMERIC: _ClassVar[TypeAnnotationCode]
    PG_JSONB: _ClassVar[TypeAnnotationCode]
    PG_OID: _ClassVar[TypeAnnotationCode]
TYPE_CODE_UNSPECIFIED: TypeCode
BOOL: TypeCode
INT64: TypeCode
FLOAT64: TypeCode
FLOAT32: TypeCode
TIMESTAMP: TypeCode
DATE: TypeCode
STRING: TypeCode
BYTES: TypeCode
ARRAY: TypeCode
STRUCT: TypeCode
NUMERIC: TypeCode
JSON: TypeCode
PROTO: TypeCode
ENUM: TypeCode
INTERVAL: TypeCode
UUID: TypeCode
TYPE_ANNOTATION_CODE_UNSPECIFIED: TypeAnnotationCode
PG_NUMERIC: TypeAnnotationCode
PG_JSONB: TypeAnnotationCode
PG_OID: TypeAnnotationCode

class Type(_message.Message):
    __slots__ = ('code', 'array_element_type', 'struct_type', 'type_annotation', 'proto_type_fqn')
    CODE_FIELD_NUMBER: _ClassVar[int]
    ARRAY_ELEMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    STRUCT_TYPE_FIELD_NUMBER: _ClassVar[int]
    TYPE_ANNOTATION_FIELD_NUMBER: _ClassVar[int]
    PROTO_TYPE_FQN_FIELD_NUMBER: _ClassVar[int]
    code: TypeCode
    array_element_type: Type
    struct_type: StructType
    type_annotation: TypeAnnotationCode
    proto_type_fqn: str

    def __init__(self, code: _Optional[_Union[TypeCode, str]]=..., array_element_type: _Optional[_Union[Type, _Mapping]]=..., struct_type: _Optional[_Union[StructType, _Mapping]]=..., type_annotation: _Optional[_Union[TypeAnnotationCode, str]]=..., proto_type_fqn: _Optional[str]=...) -> None:
        ...

class StructType(_message.Message):
    __slots__ = ('fields',)

    class Field(_message.Message):
        __slots__ = ('name', 'type')
        NAME_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        name: str
        type: Type

        def __init__(self, name: _Optional[str]=..., type: _Optional[_Union[Type, _Mapping]]=...) -> None:
            ...
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    fields: _containers.RepeatedCompositeFieldContainer[StructType.Field]

    def __init__(self, fields: _Optional[_Iterable[_Union[StructType.Field, _Mapping]]]=...) -> None:
        ...