from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ExecutionView(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EXECUTION_VIEW_UNSPECIFIED: _ClassVar[ExecutionView]
    BASIC: _ClassVar[ExecutionView]
    FULL: _ClassVar[ExecutionView]
EXECUTION_VIEW_UNSPECIFIED: ExecutionView
BASIC: ExecutionView
FULL: ExecutionView

class Execution(_message.Message):
    __slots__ = ('name', 'start_time', 'end_time', 'state', 'argument', 'result', 'error', 'workflow_revision_id')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Execution.State]
        ACTIVE: _ClassVar[Execution.State]
        SUCCEEDED: _ClassVar[Execution.State]
        FAILED: _ClassVar[Execution.State]
        CANCELLED: _ClassVar[Execution.State]
    STATE_UNSPECIFIED: Execution.State
    ACTIVE: Execution.State
    SUCCEEDED: Execution.State
    FAILED: Execution.State
    CANCELLED: Execution.State

    class Error(_message.Message):
        __slots__ = ('payload', 'context')
        PAYLOAD_FIELD_NUMBER: _ClassVar[int]
        CONTEXT_FIELD_NUMBER: _ClassVar[int]
        payload: str
        context: str

        def __init__(self, payload: _Optional[str]=..., context: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ARGUMENT_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    state: Execution.State
    argument: str
    result: str
    error: Execution.Error
    workflow_revision_id: str

    def __init__(self, name: _Optional[str]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., state: _Optional[_Union[Execution.State, str]]=..., argument: _Optional[str]=..., result: _Optional[str]=..., error: _Optional[_Union[Execution.Error, _Mapping]]=..., workflow_revision_id: _Optional[str]=...) -> None:
        ...

class ListExecutionsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'view')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    view: ExecutionView

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., view: _Optional[_Union[ExecutionView, str]]=...) -> None:
        ...

class ListExecutionsResponse(_message.Message):
    __slots__ = ('executions', 'next_page_token')
    EXECUTIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    executions: _containers.RepeatedCompositeFieldContainer[Execution]
    next_page_token: str

    def __init__(self, executions: _Optional[_Iterable[_Union[Execution, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class CreateExecutionRequest(_message.Message):
    __slots__ = ('parent', 'execution')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    parent: str
    execution: Execution

    def __init__(self, parent: _Optional[str]=..., execution: _Optional[_Union[Execution, _Mapping]]=...) -> None:
        ...

class GetExecutionRequest(_message.Message):
    __slots__ = ('name', 'view')
    NAME_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    name: str
    view: ExecutionView

    def __init__(self, name: _Optional[str]=..., view: _Optional[_Union[ExecutionView, str]]=...) -> None:
        ...

class CancelExecutionRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...