from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class AppliedLabel(_message.Message):
    __slots__ = ('label', 'negated')
    LABEL_FIELD_NUMBER: _ClassVar[int]
    NEGATED_FIELD_NUMBER: _ClassVar[int]
    label: str
    negated: bool

    def __init__(self, label: _Optional[str]=..., negated: bool=...) -> None:
        ...