from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class QueryParameterStructType(_message.Message):
    __slots__ = ('name', 'type', 'description')
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: QueryParameterType
    description: str

    def __init__(self, name: _Optional[str]=..., type: _Optional[_Union[QueryParameterType, _Mapping]]=..., description: _Optional[str]=...) -> None:
        ...

class QueryParameterType(_message.Message):
    __slots__ = ('type', 'array_type', 'struct_types', 'range_element_type')
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ARRAY_TYPE_FIELD_NUMBER: _ClassVar[int]
    STRUCT_TYPES_FIELD_NUMBER: _ClassVar[int]
    RANGE_ELEMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    type: str
    array_type: QueryParameterType
    struct_types: _containers.RepeatedCompositeFieldContainer[QueryParameterStructType]
    range_element_type: QueryParameterType

    def __init__(self, type: _Optional[str]=..., array_type: _Optional[_Union[QueryParameterType, _Mapping]]=..., struct_types: _Optional[_Iterable[_Union[QueryParameterStructType, _Mapping]]]=..., range_element_type: _Optional[_Union[QueryParameterType, _Mapping]]=...) -> None:
        ...

class RangeValue(_message.Message):
    __slots__ = ('start', 'end')
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    start: QueryParameterValue
    end: QueryParameterValue

    def __init__(self, start: _Optional[_Union[QueryParameterValue, _Mapping]]=..., end: _Optional[_Union[QueryParameterValue, _Mapping]]=...) -> None:
        ...

class QueryParameterValue(_message.Message):
    __slots__ = ('value', 'array_values', 'struct_values', 'range_value', 'alt_struct_values')

    class StructValuesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: QueryParameterValue

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[QueryParameterValue, _Mapping]]=...) -> None:
            ...
    VALUE_FIELD_NUMBER: _ClassVar[int]
    ARRAY_VALUES_FIELD_NUMBER: _ClassVar[int]
    STRUCT_VALUES_FIELD_NUMBER: _ClassVar[int]
    RANGE_VALUE_FIELD_NUMBER: _ClassVar[int]
    ALT_STRUCT_VALUES_FIELD_NUMBER: _ClassVar[int]
    value: _wrappers_pb2.StringValue
    array_values: _containers.RepeatedCompositeFieldContainer[QueryParameterValue]
    struct_values: _containers.MessageMap[str, QueryParameterValue]
    range_value: RangeValue
    alt_struct_values: _containers.RepeatedCompositeFieldContainer[_struct_pb2.Value]

    def __init__(self, value: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]]=..., array_values: _Optional[_Iterable[_Union[QueryParameterValue, _Mapping]]]=..., struct_values: _Optional[_Mapping[str, QueryParameterValue]]=..., range_value: _Optional[_Union[RangeValue, _Mapping]]=..., alt_struct_values: _Optional[_Iterable[_Union[_struct_pb2.Value, _Mapping]]]=...) -> None:
        ...

class QueryParameter(_message.Message):
    __slots__ = ('name', 'parameter_type', 'parameter_value')
    NAME_FIELD_NUMBER: _ClassVar[int]
    PARAMETER_TYPE_FIELD_NUMBER: _ClassVar[int]
    PARAMETER_VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    parameter_type: QueryParameterType
    parameter_value: QueryParameterValue

    def __init__(self, name: _Optional[str]=..., parameter_type: _Optional[_Union[QueryParameterType, _Mapping]]=..., parameter_value: _Optional[_Union[QueryParameterValue, _Mapping]]=...) -> None:
        ...