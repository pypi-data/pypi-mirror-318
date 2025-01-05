from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class InstanceEvent(_message.Message):
    __slots__ = ('verb', 'stage', 'msg', 'trace_id', 'node_id')
    VERB_FIELD_NUMBER: _ClassVar[int]
    STAGE_FIELD_NUMBER: _ClassVar[int]
    MSG_FIELD_NUMBER: _ClassVar[int]
    TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    verb: str
    stage: str
    msg: str
    trace_id: str
    node_id: str

    def __init__(self, verb: _Optional[str]=..., stage: _Optional[str]=..., msg: _Optional[str]=..., trace_id: _Optional[str]=..., node_id: _Optional[str]=...) -> None:
        ...