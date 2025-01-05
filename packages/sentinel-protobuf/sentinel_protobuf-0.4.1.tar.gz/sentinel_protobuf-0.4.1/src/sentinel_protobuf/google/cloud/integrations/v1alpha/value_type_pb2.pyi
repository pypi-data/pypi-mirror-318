from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ValueType(_message.Message):
    __slots__ = ('string_value', 'int_value', 'double_value', 'boolean_value', 'string_array', 'int_array', 'double_array', 'boolean_array', 'json_value')
    STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
    INT_VALUE_FIELD_NUMBER: _ClassVar[int]
    DOUBLE_VALUE_FIELD_NUMBER: _ClassVar[int]
    BOOLEAN_VALUE_FIELD_NUMBER: _ClassVar[int]
    STRING_ARRAY_FIELD_NUMBER: _ClassVar[int]
    INT_ARRAY_FIELD_NUMBER: _ClassVar[int]
    DOUBLE_ARRAY_FIELD_NUMBER: _ClassVar[int]
    BOOLEAN_ARRAY_FIELD_NUMBER: _ClassVar[int]
    JSON_VALUE_FIELD_NUMBER: _ClassVar[int]
    string_value: str
    int_value: int
    double_value: float
    boolean_value: bool
    string_array: StringParameterArray
    int_array: IntParameterArray
    double_array: DoubleParameterArray
    boolean_array: BooleanParameterArray
    json_value: str

    def __init__(self, string_value: _Optional[str]=..., int_value: _Optional[int]=..., double_value: _Optional[float]=..., boolean_value: bool=..., string_array: _Optional[_Union[StringParameterArray, _Mapping]]=..., int_array: _Optional[_Union[IntParameterArray, _Mapping]]=..., double_array: _Optional[_Union[DoubleParameterArray, _Mapping]]=..., boolean_array: _Optional[_Union[BooleanParameterArray, _Mapping]]=..., json_value: _Optional[str]=...) -> None:
        ...

class StringParameterArray(_message.Message):
    __slots__ = ('string_values',)
    STRING_VALUES_FIELD_NUMBER: _ClassVar[int]
    string_values: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, string_values: _Optional[_Iterable[str]]=...) -> None:
        ...

class IntParameterArray(_message.Message):
    __slots__ = ('int_values',)
    INT_VALUES_FIELD_NUMBER: _ClassVar[int]
    int_values: _containers.RepeatedScalarFieldContainer[int]

    def __init__(self, int_values: _Optional[_Iterable[int]]=...) -> None:
        ...

class DoubleParameterArray(_message.Message):
    __slots__ = ('double_values',)
    DOUBLE_VALUES_FIELD_NUMBER: _ClassVar[int]
    double_values: _containers.RepeatedScalarFieldContainer[float]

    def __init__(self, double_values: _Optional[_Iterable[float]]=...) -> None:
        ...

class BooleanParameterArray(_message.Message):
    __slots__ = ('boolean_values',)
    BOOLEAN_VALUES_FIELD_NUMBER: _ClassVar[int]
    boolean_values: _containers.RepeatedScalarFieldContainer[bool]

    def __init__(self, boolean_values: _Optional[_Iterable[bool]]=...) -> None:
        ...