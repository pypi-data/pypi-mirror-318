from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.devtools.clouddebugger.v2 import data_pb2 as _data_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class SetBreakpointRequest(_message.Message):
    __slots__ = ('debuggee_id', 'breakpoint', 'client_version')
    DEBUGGEE_ID_FIELD_NUMBER: _ClassVar[int]
    BREAKPOINT_FIELD_NUMBER: _ClassVar[int]
    CLIENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    debuggee_id: str
    breakpoint: _data_pb2.Breakpoint
    client_version: str

    def __init__(self, debuggee_id: _Optional[str]=..., breakpoint: _Optional[_Union[_data_pb2.Breakpoint, _Mapping]]=..., client_version: _Optional[str]=...) -> None:
        ...

class SetBreakpointResponse(_message.Message):
    __slots__ = ('breakpoint',)
    BREAKPOINT_FIELD_NUMBER: _ClassVar[int]
    breakpoint: _data_pb2.Breakpoint

    def __init__(self, breakpoint: _Optional[_Union[_data_pb2.Breakpoint, _Mapping]]=...) -> None:
        ...

class GetBreakpointRequest(_message.Message):
    __slots__ = ('debuggee_id', 'breakpoint_id', 'client_version')
    DEBUGGEE_ID_FIELD_NUMBER: _ClassVar[int]
    BREAKPOINT_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    debuggee_id: str
    breakpoint_id: str
    client_version: str

    def __init__(self, debuggee_id: _Optional[str]=..., breakpoint_id: _Optional[str]=..., client_version: _Optional[str]=...) -> None:
        ...

class GetBreakpointResponse(_message.Message):
    __slots__ = ('breakpoint',)
    BREAKPOINT_FIELD_NUMBER: _ClassVar[int]
    breakpoint: _data_pb2.Breakpoint

    def __init__(self, breakpoint: _Optional[_Union[_data_pb2.Breakpoint, _Mapping]]=...) -> None:
        ...

class DeleteBreakpointRequest(_message.Message):
    __slots__ = ('debuggee_id', 'breakpoint_id', 'client_version')
    DEBUGGEE_ID_FIELD_NUMBER: _ClassVar[int]
    BREAKPOINT_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    debuggee_id: str
    breakpoint_id: str
    client_version: str

    def __init__(self, debuggee_id: _Optional[str]=..., breakpoint_id: _Optional[str]=..., client_version: _Optional[str]=...) -> None:
        ...

class ListBreakpointsRequest(_message.Message):
    __slots__ = ('debuggee_id', 'include_all_users', 'include_inactive', 'action', 'strip_results', 'wait_token', 'client_version')

    class BreakpointActionValue(_message.Message):
        __slots__ = ('value',)
        VALUE_FIELD_NUMBER: _ClassVar[int]
        value: _data_pb2.Breakpoint.Action

        def __init__(self, value: _Optional[_Union[_data_pb2.Breakpoint.Action, str]]=...) -> None:
            ...
    DEBUGGEE_ID_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_ALL_USERS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_INACTIVE_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    STRIP_RESULTS_FIELD_NUMBER: _ClassVar[int]
    WAIT_TOKEN_FIELD_NUMBER: _ClassVar[int]
    CLIENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    debuggee_id: str
    include_all_users: bool
    include_inactive: bool
    action: ListBreakpointsRequest.BreakpointActionValue
    strip_results: bool
    wait_token: str
    client_version: str

    def __init__(self, debuggee_id: _Optional[str]=..., include_all_users: bool=..., include_inactive: bool=..., action: _Optional[_Union[ListBreakpointsRequest.BreakpointActionValue, _Mapping]]=..., strip_results: bool=..., wait_token: _Optional[str]=..., client_version: _Optional[str]=...) -> None:
        ...

class ListBreakpointsResponse(_message.Message):
    __slots__ = ('breakpoints', 'next_wait_token')
    BREAKPOINTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_WAIT_TOKEN_FIELD_NUMBER: _ClassVar[int]
    breakpoints: _containers.RepeatedCompositeFieldContainer[_data_pb2.Breakpoint]
    next_wait_token: str

    def __init__(self, breakpoints: _Optional[_Iterable[_Union[_data_pb2.Breakpoint, _Mapping]]]=..., next_wait_token: _Optional[str]=...) -> None:
        ...

class ListDebuggeesRequest(_message.Message):
    __slots__ = ('project', 'include_inactive', 'client_version')
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_INACTIVE_FIELD_NUMBER: _ClassVar[int]
    CLIENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    project: str
    include_inactive: bool
    client_version: str

    def __init__(self, project: _Optional[str]=..., include_inactive: bool=..., client_version: _Optional[str]=...) -> None:
        ...

class ListDebuggeesResponse(_message.Message):
    __slots__ = ('debuggees',)
    DEBUGGEES_FIELD_NUMBER: _ClassVar[int]
    debuggees: _containers.RepeatedCompositeFieldContainer[_data_pb2.Debuggee]

    def __init__(self, debuggees: _Optional[_Iterable[_Union[_data_pb2.Debuggee, _Mapping]]]=...) -> None:
        ...