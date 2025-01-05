from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class SinkSettings(_message.Message):
    __slots__ = ('logging_sink_project',)
    LOGGING_SINK_PROJECT_FIELD_NUMBER: _ClassVar[int]
    logging_sink_project: str

    def __init__(self, logging_sink_project: _Optional[str]=...) -> None:
        ...