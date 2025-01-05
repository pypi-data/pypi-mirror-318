from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.devtools.clouddebugger.v2 import data_pb2 as _data_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class RegisterDebuggeeRequest(_message.Message):
    __slots__ = ('debuggee',)
    DEBUGGEE_FIELD_NUMBER: _ClassVar[int]
    debuggee: _data_pb2.Debuggee

    def __init__(self, debuggee: _Optional[_Union[_data_pb2.Debuggee, _Mapping]]=...) -> None:
        ...

class RegisterDebuggeeResponse(_message.Message):
    __slots__ = ('debuggee',)
    DEBUGGEE_FIELD_NUMBER: _ClassVar[int]
    debuggee: _data_pb2.Debuggee

    def __init__(self, debuggee: _Optional[_Union[_data_pb2.Debuggee, _Mapping]]=...) -> None:
        ...

class ListActiveBreakpointsRequest(_message.Message):
    __slots__ = ('debuggee_id', 'wait_token', 'success_on_timeout')
    DEBUGGEE_ID_FIELD_NUMBER: _ClassVar[int]
    WAIT_TOKEN_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_ON_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    debuggee_id: str
    wait_token: str
    success_on_timeout: bool

    def __init__(self, debuggee_id: _Optional[str]=..., wait_token: _Optional[str]=..., success_on_timeout: bool=...) -> None:
        ...

class ListActiveBreakpointsResponse(_message.Message):
    __slots__ = ('breakpoints', 'next_wait_token', 'wait_expired')
    BREAKPOINTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_WAIT_TOKEN_FIELD_NUMBER: _ClassVar[int]
    WAIT_EXPIRED_FIELD_NUMBER: _ClassVar[int]
    breakpoints: _containers.RepeatedCompositeFieldContainer[_data_pb2.Breakpoint]
    next_wait_token: str
    wait_expired: bool

    def __init__(self, breakpoints: _Optional[_Iterable[_Union[_data_pb2.Breakpoint, _Mapping]]]=..., next_wait_token: _Optional[str]=..., wait_expired: bool=...) -> None:
        ...

class UpdateActiveBreakpointRequest(_message.Message):
    __slots__ = ('debuggee_id', 'breakpoint')
    DEBUGGEE_ID_FIELD_NUMBER: _ClassVar[int]
    BREAKPOINT_FIELD_NUMBER: _ClassVar[int]
    debuggee_id: str
    breakpoint: _data_pb2.Breakpoint

    def __init__(self, debuggee_id: _Optional[str]=..., breakpoint: _Optional[_Union[_data_pb2.Breakpoint, _Mapping]]=...) -> None:
        ...

class UpdateActiveBreakpointResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...