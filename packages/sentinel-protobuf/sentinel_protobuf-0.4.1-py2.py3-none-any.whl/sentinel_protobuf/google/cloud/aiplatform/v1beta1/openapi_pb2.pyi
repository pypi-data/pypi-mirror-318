from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TYPE_UNSPECIFIED: _ClassVar[Type]
    STRING: _ClassVar[Type]
    NUMBER: _ClassVar[Type]
    INTEGER: _ClassVar[Type]
    BOOLEAN: _ClassVar[Type]
    ARRAY: _ClassVar[Type]
    OBJECT: _ClassVar[Type]
TYPE_UNSPECIFIED: Type
STRING: Type
NUMBER: Type
INTEGER: Type
BOOLEAN: Type
ARRAY: Type
OBJECT: Type

class Schema(_message.Message):
    __slots__ = ('type', 'format', 'title', 'description', 'nullable', 'default', 'items', 'min_items', 'max_items', 'enum', 'properties', 'property_ordering', 'required', 'min_properties', 'max_properties', 'minimum', 'maximum', 'min_length', 'max_length', 'pattern', 'example', 'any_of')

    class PropertiesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Schema

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[Schema, _Mapping]]=...) -> None:
            ...
    TYPE_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    NULLABLE_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    MIN_ITEMS_FIELD_NUMBER: _ClassVar[int]
    MAX_ITEMS_FIELD_NUMBER: _ClassVar[int]
    ENUM_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_ORDERING_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_FIELD_NUMBER: _ClassVar[int]
    MIN_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    MAX_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_FIELD_NUMBER: _ClassVar[int]
    MIN_LENGTH_FIELD_NUMBER: _ClassVar[int]
    MAX_LENGTH_FIELD_NUMBER: _ClassVar[int]
    PATTERN_FIELD_NUMBER: _ClassVar[int]
    EXAMPLE_FIELD_NUMBER: _ClassVar[int]
    ANY_OF_FIELD_NUMBER: _ClassVar[int]
    type: Type
    format: str
    title: str
    description: str
    nullable: bool
    default: _struct_pb2.Value
    items: Schema
    min_items: int
    max_items: int
    enum: _containers.RepeatedScalarFieldContainer[str]
    properties: _containers.MessageMap[str, Schema]
    property_ordering: _containers.RepeatedScalarFieldContainer[str]
    required: _containers.RepeatedScalarFieldContainer[str]
    min_properties: int
    max_properties: int
    minimum: float
    maximum: float
    min_length: int
    max_length: int
    pattern: str
    example: _struct_pb2.Value
    any_of: _containers.RepeatedCompositeFieldContainer[Schema]

    def __init__(self, type: _Optional[_Union[Type, str]]=..., format: _Optional[str]=..., title: _Optional[str]=..., description: _Optional[str]=..., nullable: bool=..., default: _Optional[_Union[_struct_pb2.Value, _Mapping]]=..., items: _Optional[_Union[Schema, _Mapping]]=..., min_items: _Optional[int]=..., max_items: _Optional[int]=..., enum: _Optional[_Iterable[str]]=..., properties: _Optional[_Mapping[str, Schema]]=..., property_ordering: _Optional[_Iterable[str]]=..., required: _Optional[_Iterable[str]]=..., min_properties: _Optional[int]=..., max_properties: _Optional[int]=..., minimum: _Optional[float]=..., maximum: _Optional[float]=..., min_length: _Optional[int]=..., max_length: _Optional[int]=..., pattern: _Optional[str]=..., example: _Optional[_Union[_struct_pb2.Value, _Mapping]]=..., any_of: _Optional[_Iterable[_Union[Schema, _Mapping]]]=...) -> None:
        ...