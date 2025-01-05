from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class WorkflowInvocationCompletionLogEntry(_message.Message):
    __slots__ = ('workflow_invocation_id', 'workflow_config_id', 'release_config_id', 'terminal_state')

    class TerminalState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TERMINAL_STATE_UNSPECIFIED: _ClassVar[WorkflowInvocationCompletionLogEntry.TerminalState]
        SUCCEEDED: _ClassVar[WorkflowInvocationCompletionLogEntry.TerminalState]
        CANCELLED: _ClassVar[WorkflowInvocationCompletionLogEntry.TerminalState]
        FAILED: _ClassVar[WorkflowInvocationCompletionLogEntry.TerminalState]
    TERMINAL_STATE_UNSPECIFIED: WorkflowInvocationCompletionLogEntry.TerminalState
    SUCCEEDED: WorkflowInvocationCompletionLogEntry.TerminalState
    CANCELLED: WorkflowInvocationCompletionLogEntry.TerminalState
    FAILED: WorkflowInvocationCompletionLogEntry.TerminalState
    WORKFLOW_INVOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    RELEASE_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    TERMINAL_STATE_FIELD_NUMBER: _ClassVar[int]
    workflow_invocation_id: str
    workflow_config_id: str
    release_config_id: str
    terminal_state: WorkflowInvocationCompletionLogEntry.TerminalState

    def __init__(self, workflow_invocation_id: _Optional[str]=..., workflow_config_id: _Optional[str]=..., release_config_id: _Optional[str]=..., terminal_state: _Optional[_Union[WorkflowInvocationCompletionLogEntry.TerminalState, str]]=...) -> None:
        ...