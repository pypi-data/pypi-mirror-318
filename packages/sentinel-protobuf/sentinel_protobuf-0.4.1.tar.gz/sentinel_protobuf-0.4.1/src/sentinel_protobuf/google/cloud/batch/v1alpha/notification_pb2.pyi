from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class Notification(_message.Message):
    __slots__ = ('pubsub_topic',)
    PUBSUB_TOPIC_FIELD_NUMBER: _ClassVar[int]
    pubsub_topic: str

    def __init__(self, pubsub_topic: _Optional[str]=...) -> None:
        ...