from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class TimePartitioning(_message.Message):
    __slots__ = ('type', 'expiration_ms', 'field')
    TYPE_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_MS_FIELD_NUMBER: _ClassVar[int]
    FIELD_FIELD_NUMBER: _ClassVar[int]
    type: str
    expiration_ms: _wrappers_pb2.Int64Value
    field: _wrappers_pb2.StringValue

    def __init__(self, type: _Optional[str]=..., expiration_ms: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]]=..., field: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]]=...) -> None:
        ...