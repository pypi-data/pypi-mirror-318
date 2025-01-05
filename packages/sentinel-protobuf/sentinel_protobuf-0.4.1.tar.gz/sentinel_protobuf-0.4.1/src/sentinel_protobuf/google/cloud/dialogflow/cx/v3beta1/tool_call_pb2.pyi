from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ToolCall(_message.Message):
    __slots__ = ('tool', 'action', 'input_parameters')
    TOOL_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    INPUT_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    tool: str
    action: str
    input_parameters: _struct_pb2.Struct

    def __init__(self, tool: _Optional[str]=..., action: _Optional[str]=..., input_parameters: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=...) -> None:
        ...

class ToolCallResult(_message.Message):
    __slots__ = ('tool', 'action', 'error', 'output_parameters')

    class Error(_message.Message):
        __slots__ = ('message',)
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        message: str

        def __init__(self, message: _Optional[str]=...) -> None:
            ...
    TOOL_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    tool: str
    action: str
    error: ToolCallResult.Error
    output_parameters: _struct_pb2.Struct

    def __init__(self, tool: _Optional[str]=..., action: _Optional[str]=..., error: _Optional[_Union[ToolCallResult.Error, _Mapping]]=..., output_parameters: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=...) -> None:
        ...