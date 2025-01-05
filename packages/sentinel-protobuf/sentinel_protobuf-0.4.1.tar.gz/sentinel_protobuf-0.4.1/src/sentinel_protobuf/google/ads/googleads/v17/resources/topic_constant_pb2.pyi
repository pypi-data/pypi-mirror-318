from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TopicConstant(_message.Message):
    __slots__ = ("resource_name", "id", "topic_constant_parent", "path")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    TOPIC_CONSTANT_PARENT_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    id: int
    topic_constant_parent: str
    path: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, resource_name: _Optional[str] = ..., id: _Optional[int] = ..., topic_constant_parent: _Optional[str] = ..., path: _Optional[_Iterable[str]] = ...) -> None: ...
