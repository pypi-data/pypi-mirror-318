from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class RevisionScalingStatus(_message.Message):
    __slots__ = ('desired_min_instance_count',)
    DESIRED_MIN_INSTANCE_COUNT_FIELD_NUMBER: _ClassVar[int]
    desired_min_instance_count: int

    def __init__(self, desired_min_instance_count: _Optional[int]=...) -> None:
        ...