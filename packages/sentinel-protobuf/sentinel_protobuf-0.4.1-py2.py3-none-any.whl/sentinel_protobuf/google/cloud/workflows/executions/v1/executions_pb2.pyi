from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import duration_pb2 as _duration_pb2
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
    __slots__ = ('name', 'start_time', 'end_time', 'duration', 'state', 'argument', 'result', 'error', 'workflow_revision_id', 'call_log_level', 'status', 'labels', 'state_error')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Execution.State]
        ACTIVE: _ClassVar[Execution.State]
        SUCCEEDED: _ClassVar[Execution.State]
        FAILED: _ClassVar[Execution.State]
        CANCELLED: _ClassVar[Execution.State]
        UNAVAILABLE: _ClassVar[Execution.State]
        QUEUED: _ClassVar[Execution.State]
    STATE_UNSPECIFIED: Execution.State
    ACTIVE: Execution.State
    SUCCEEDED: Execution.State
    FAILED: Execution.State
    CANCELLED: Execution.State
    UNAVAILABLE: Execution.State
    QUEUED: Execution.State

    class CallLogLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CALL_LOG_LEVEL_UNSPECIFIED: _ClassVar[Execution.CallLogLevel]
        LOG_ALL_CALLS: _ClassVar[Execution.CallLogLevel]
        LOG_ERRORS_ONLY: _ClassVar[Execution.CallLogLevel]
        LOG_NONE: _ClassVar[Execution.CallLogLevel]
    CALL_LOG_LEVEL_UNSPECIFIED: Execution.CallLogLevel
    LOG_ALL_CALLS: Execution.CallLogLevel
    LOG_ERRORS_ONLY: Execution.CallLogLevel
    LOG_NONE: Execution.CallLogLevel

    class StackTraceElement(_message.Message):
        __slots__ = ('step', 'routine', 'position')

        class Position(_message.Message):
            __slots__ = ('line', 'column', 'length')
            LINE_FIELD_NUMBER: _ClassVar[int]
            COLUMN_FIELD_NUMBER: _ClassVar[int]
            LENGTH_FIELD_NUMBER: _ClassVar[int]
            line: int
            column: int
            length: int

            def __init__(self, line: _Optional[int]=..., column: _Optional[int]=..., length: _Optional[int]=...) -> None:
                ...
        STEP_FIELD_NUMBER: _ClassVar[int]
        ROUTINE_FIELD_NUMBER: _ClassVar[int]
        POSITION_FIELD_NUMBER: _ClassVar[int]
        step: str
        routine: str
        position: Execution.StackTraceElement.Position

        def __init__(self, step: _Optional[str]=..., routine: _Optional[str]=..., position: _Optional[_Union[Execution.StackTraceElement.Position, _Mapping]]=...) -> None:
            ...

    class StackTrace(_message.Message):
        __slots__ = ('elements',)
        ELEMENTS_FIELD_NUMBER: _ClassVar[int]
        elements: _containers.RepeatedCompositeFieldContainer[Execution.StackTraceElement]

        def __init__(self, elements: _Optional[_Iterable[_Union[Execution.StackTraceElement, _Mapping]]]=...) -> None:
            ...

    class Error(_message.Message):
        __slots__ = ('payload', 'context', 'stack_trace')
        PAYLOAD_FIELD_NUMBER: _ClassVar[int]
        CONTEXT_FIELD_NUMBER: _ClassVar[int]
        STACK_TRACE_FIELD_NUMBER: _ClassVar[int]
        payload: str
        context: str
        stack_trace: Execution.StackTrace

        def __init__(self, payload: _Optional[str]=..., context: _Optional[str]=..., stack_trace: _Optional[_Union[Execution.StackTrace, _Mapping]]=...) -> None:
            ...

    class Status(_message.Message):
        __slots__ = ('current_steps',)

        class Step(_message.Message):
            __slots__ = ('routine', 'step')
            ROUTINE_FIELD_NUMBER: _ClassVar[int]
            STEP_FIELD_NUMBER: _ClassVar[int]
            routine: str
            step: str

            def __init__(self, routine: _Optional[str]=..., step: _Optional[str]=...) -> None:
                ...
        CURRENT_STEPS_FIELD_NUMBER: _ClassVar[int]
        current_steps: _containers.RepeatedCompositeFieldContainer[Execution.Status.Step]

        def __init__(self, current_steps: _Optional[_Iterable[_Union[Execution.Status.Step, _Mapping]]]=...) -> None:
            ...

    class StateError(_message.Message):
        __slots__ = ('details', 'type')

        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            TYPE_UNSPECIFIED: _ClassVar[Execution.StateError.Type]
            KMS_ERROR: _ClassVar[Execution.StateError.Type]
        TYPE_UNSPECIFIED: Execution.StateError.Type
        KMS_ERROR: Execution.StateError.Type
        DETAILS_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        details: str
        type: Execution.StateError.Type

        def __init__(self, details: _Optional[str]=..., type: _Optional[_Union[Execution.StateError.Type, str]]=...) -> None:
            ...

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ARGUMENT_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    CALL_LOG_LEVEL_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    STATE_ERROR_FIELD_NUMBER: _ClassVar[int]
    name: str
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    duration: _duration_pb2.Duration
    state: Execution.State
    argument: str
    result: str
    error: Execution.Error
    workflow_revision_id: str
    call_log_level: Execution.CallLogLevel
    status: Execution.Status
    labels: _containers.ScalarMap[str, str]
    state_error: Execution.StateError

    def __init__(self, name: _Optional[str]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., state: _Optional[_Union[Execution.State, str]]=..., argument: _Optional[str]=..., result: _Optional[str]=..., error: _Optional[_Union[Execution.Error, _Mapping]]=..., workflow_revision_id: _Optional[str]=..., call_log_level: _Optional[_Union[Execution.CallLogLevel, str]]=..., status: _Optional[_Union[Execution.Status, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., state_error: _Optional[_Union[Execution.StateError, _Mapping]]=...) -> None:
        ...

class ListExecutionsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'view', 'filter', 'order_by')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    view: ExecutionView
    filter: str
    order_by: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., view: _Optional[_Union[ExecutionView, str]]=..., filter: _Optional[str]=..., order_by: _Optional[str]=...) -> None:
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