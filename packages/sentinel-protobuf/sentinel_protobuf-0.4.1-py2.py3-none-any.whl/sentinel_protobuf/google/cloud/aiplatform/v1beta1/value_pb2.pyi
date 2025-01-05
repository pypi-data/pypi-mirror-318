from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class Value(_message.Message):
    __slots__ = ('int_value', 'double_value', 'string_value')
    INT_VALUE_FIELD_NUMBER: _ClassVar[int]
    DOUBLE_VALUE_FIELD_NUMBER: _ClassVar[int]
    STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
    int_value: int
    double_value: float
    string_value: str

    def __init__(self, int_value: _Optional[int]=..., double_value: _Optional[float]=..., string_value: _Optional[str]=...) -> None:
        ...