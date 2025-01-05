from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class Value(_message.Message):
    __slots__ = ('boolean_value', 'int64_value', 'float_value', 'double_value', 'string_value')
    BOOLEAN_VALUE_FIELD_NUMBER: _ClassVar[int]
    INT64_VALUE_FIELD_NUMBER: _ClassVar[int]
    FLOAT_VALUE_FIELD_NUMBER: _ClassVar[int]
    DOUBLE_VALUE_FIELD_NUMBER: _ClassVar[int]
    STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
    boolean_value: bool
    int64_value: int
    float_value: float
    double_value: float
    string_value: str

    def __init__(self, boolean_value: bool=..., int64_value: _Optional[int]=..., float_value: _Optional[float]=..., double_value: _Optional[float]=..., string_value: _Optional[str]=...) -> None:
        ...