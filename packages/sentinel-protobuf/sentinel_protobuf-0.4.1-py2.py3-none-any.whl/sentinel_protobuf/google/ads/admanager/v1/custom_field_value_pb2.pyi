from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CustomFieldValue(_message.Message):
    __slots__ = ("custom_field", "value")
    class Value(_message.Message):
        __slots__ = ("dropdown_value", "string_value", "number_value", "toggle_value")
        DROPDOWN_VALUE_FIELD_NUMBER: _ClassVar[int]
        STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
        NUMBER_VALUE_FIELD_NUMBER: _ClassVar[int]
        TOGGLE_VALUE_FIELD_NUMBER: _ClassVar[int]
        dropdown_value: int
        string_value: str
        number_value: float
        toggle_value: bool
        def __init__(self, dropdown_value: _Optional[int] = ..., string_value: _Optional[str] = ..., number_value: _Optional[float] = ..., toggle_value: bool = ...) -> None: ...
    CUSTOM_FIELD_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    custom_field: str
    value: CustomFieldValue.Value
    def __init__(self, custom_field: _Optional[str] = ..., value: _Optional[_Union[CustomFieldValue.Value, _Mapping]] = ...) -> None: ...
