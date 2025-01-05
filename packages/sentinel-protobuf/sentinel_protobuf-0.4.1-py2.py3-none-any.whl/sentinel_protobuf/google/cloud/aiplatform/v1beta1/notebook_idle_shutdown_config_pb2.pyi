from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class NotebookIdleShutdownConfig(_message.Message):
    __slots__ = ('idle_timeout', 'idle_shutdown_disabled')
    IDLE_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    IDLE_SHUTDOWN_DISABLED_FIELD_NUMBER: _ClassVar[int]
    idle_timeout: _duration_pb2.Duration
    idle_shutdown_disabled: bool

    def __init__(self, idle_timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., idle_shutdown_disabled: bool=...) -> None:
        ...