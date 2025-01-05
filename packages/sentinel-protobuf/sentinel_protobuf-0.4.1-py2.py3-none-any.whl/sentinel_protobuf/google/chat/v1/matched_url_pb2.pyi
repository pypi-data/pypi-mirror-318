from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class MatchedUrl(_message.Message):
    __slots__ = ('url',)
    URL_FIELD_NUMBER: _ClassVar[int]
    url: str

    def __init__(self, url: _Optional[str]=...) -> None:
        ...