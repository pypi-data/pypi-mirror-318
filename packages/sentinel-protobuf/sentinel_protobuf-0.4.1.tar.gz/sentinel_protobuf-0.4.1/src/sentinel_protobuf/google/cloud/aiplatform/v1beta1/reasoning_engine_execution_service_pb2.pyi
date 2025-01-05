from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import httpbody_pb2 as _httpbody_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class QueryReasoningEngineRequest(_message.Message):
    __slots__ = ('name', 'input', 'class_method')
    NAME_FIELD_NUMBER: _ClassVar[int]
    INPUT_FIELD_NUMBER: _ClassVar[int]
    CLASS_METHOD_FIELD_NUMBER: _ClassVar[int]
    name: str
    input: _struct_pb2.Struct
    class_method: str

    def __init__(self, name: _Optional[str]=..., input: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=..., class_method: _Optional[str]=...) -> None:
        ...

class QueryReasoningEngineResponse(_message.Message):
    __slots__ = ('output',)
    OUTPUT_FIELD_NUMBER: _ClassVar[int]
    output: _struct_pb2.Value

    def __init__(self, output: _Optional[_Union[_struct_pb2.Value, _Mapping]]=...) -> None:
        ...

class StreamQueryReasoningEngineRequest(_message.Message):
    __slots__ = ('name', 'input', 'class_method')
    NAME_FIELD_NUMBER: _ClassVar[int]
    INPUT_FIELD_NUMBER: _ClassVar[int]
    CLASS_METHOD_FIELD_NUMBER: _ClassVar[int]
    name: str
    input: _struct_pb2.Struct
    class_method: str

    def __init__(self, name: _Optional[str]=..., input: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=..., class_method: _Optional[str]=...) -> None:
        ...