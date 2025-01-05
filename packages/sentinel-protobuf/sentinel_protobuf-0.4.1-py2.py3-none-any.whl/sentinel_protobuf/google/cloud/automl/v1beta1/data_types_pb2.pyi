from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class TypeCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TYPE_CODE_UNSPECIFIED: _ClassVar[TypeCode]
    FLOAT64: _ClassVar[TypeCode]
    TIMESTAMP: _ClassVar[TypeCode]
    STRING: _ClassVar[TypeCode]
    ARRAY: _ClassVar[TypeCode]
    STRUCT: _ClassVar[TypeCode]
    CATEGORY: _ClassVar[TypeCode]
TYPE_CODE_UNSPECIFIED: TypeCode
FLOAT64: TypeCode
TIMESTAMP: TypeCode
STRING: TypeCode
ARRAY: TypeCode
STRUCT: TypeCode
CATEGORY: TypeCode

class DataType(_message.Message):
    __slots__ = ('list_element_type', 'struct_type', 'time_format', 'type_code', 'nullable')
    LIST_ELEMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    STRUCT_TYPE_FIELD_NUMBER: _ClassVar[int]
    TIME_FORMAT_FIELD_NUMBER: _ClassVar[int]
    TYPE_CODE_FIELD_NUMBER: _ClassVar[int]
    NULLABLE_FIELD_NUMBER: _ClassVar[int]
    list_element_type: DataType
    struct_type: StructType
    time_format: str
    type_code: TypeCode
    nullable: bool

    def __init__(self, list_element_type: _Optional[_Union[DataType, _Mapping]]=..., struct_type: _Optional[_Union[StructType, _Mapping]]=..., time_format: _Optional[str]=..., type_code: _Optional[_Union[TypeCode, str]]=..., nullable: bool=...) -> None:
        ...

class StructType(_message.Message):
    __slots__ = ('fields',)

    class FieldsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: DataType

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[DataType, _Mapping]]=...) -> None:
            ...
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    fields: _containers.MessageMap[str, DataType]

    def __init__(self, fields: _Optional[_Mapping[str, DataType]]=...) -> None:
        ...