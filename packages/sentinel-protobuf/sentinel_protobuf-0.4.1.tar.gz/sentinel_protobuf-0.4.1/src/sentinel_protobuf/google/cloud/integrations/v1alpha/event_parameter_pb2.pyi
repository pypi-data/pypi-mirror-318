from google.cloud.integrations.v1alpha import value_type_pb2 as _value_type_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class EventParameter(_message.Message):
    __slots__ = ('key', 'value', 'masked')
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    MASKED_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: _value_type_pb2.ValueType
    masked: bool

    def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[_value_type_pb2.ValueType, _Mapping]]=..., masked: bool=...) -> None:
        ...