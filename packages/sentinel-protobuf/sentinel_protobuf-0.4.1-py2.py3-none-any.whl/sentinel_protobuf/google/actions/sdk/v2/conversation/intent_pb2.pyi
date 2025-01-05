from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Intent(_message.Message):
    __slots__ = ('name', 'params', 'query')

    class ParamsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: IntentParameterValue

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[IntentParameterValue, _Mapping]]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    name: str
    params: _containers.MessageMap[str, IntentParameterValue]
    query: str

    def __init__(self, name: _Optional[str]=..., params: _Optional[_Mapping[str, IntentParameterValue]]=..., query: _Optional[str]=...) -> None:
        ...

class IntentParameterValue(_message.Message):
    __slots__ = ('original', 'resolved')
    ORIGINAL_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_FIELD_NUMBER: _ClassVar[int]
    original: str
    resolved: _struct_pb2.Value

    def __init__(self, original: _Optional[str]=..., resolved: _Optional[_Union[_struct_pb2.Value, _Mapping]]=...) -> None:
        ...