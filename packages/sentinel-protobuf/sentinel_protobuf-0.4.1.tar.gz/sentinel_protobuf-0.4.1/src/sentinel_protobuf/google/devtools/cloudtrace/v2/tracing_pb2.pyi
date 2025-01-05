from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.devtools.cloudtrace.v2 import trace_pb2 as _trace_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class BatchWriteSpansRequest(_message.Message):
    __slots__ = ('name', 'spans')
    NAME_FIELD_NUMBER: _ClassVar[int]
    SPANS_FIELD_NUMBER: _ClassVar[int]
    name: str
    spans: _containers.RepeatedCompositeFieldContainer[_trace_pb2.Span]

    def __init__(self, name: _Optional[str]=..., spans: _Optional[_Iterable[_Union[_trace_pb2.Span, _Mapping]]]=...) -> None:
        ...