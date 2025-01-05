from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Schema(_message.Message):
    __slots__ = ('struct_schema', 'json_schema', 'name')
    STRUCT_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    JSON_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    struct_schema: _struct_pb2.Struct
    json_schema: str
    name: str

    def __init__(self, struct_schema: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=..., json_schema: _Optional[str]=..., name: _Optional[str]=...) -> None:
        ...