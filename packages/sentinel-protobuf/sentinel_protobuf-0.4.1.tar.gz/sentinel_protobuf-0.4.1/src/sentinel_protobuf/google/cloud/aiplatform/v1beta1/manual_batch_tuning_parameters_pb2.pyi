from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class ManualBatchTuningParameters(_message.Message):
    __slots__ = ('batch_size',)
    BATCH_SIZE_FIELD_NUMBER: _ClassVar[int]
    batch_size: int

    def __init__(self, batch_size: _Optional[int]=...) -> None:
        ...