from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class OutputState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OUTPUT_STATE_UNSPECIFIED: _ClassVar[OutputState]
    OUTPUT_STATE_OK: _ClassVar[OutputState]
    OUTPUT_STATE_CANCELLED: _ClassVar[OutputState]
    OUTPUT_STATE_FAILED: _ClassVar[OutputState]
    OUTPUT_STATE_ESCALATED: _ClassVar[OutputState]
    OUTPUT_STATE_PENDING: _ClassVar[OutputState]
OUTPUT_STATE_UNSPECIFIED: OutputState
OUTPUT_STATE_OK: OutputState
OUTPUT_STATE_CANCELLED: OutputState
OUTPUT_STATE_FAILED: OutputState
OUTPUT_STATE_ESCALATED: OutputState
OUTPUT_STATE_PENDING: OutputState

class CreateExampleRequest(_message.Message):
    __slots__ = ('parent', 'example')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    EXAMPLE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    example: Example

    def __init__(self, parent: _Optional[str]=..., example: _Optional[_Union[Example, _Mapping]]=...) -> None:
        ...

class DeleteExampleRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListExamplesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'language_code')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    language_code: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., language_code: _Optional[str]=...) -> None:
        ...

class ListExamplesResponse(_message.Message):
    __slots__ = ('examples', 'next_page_token')
    EXAMPLES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    examples: _containers.RepeatedCompositeFieldContainer[Example]
    next_page_token: str

    def __init__(self, examples: _Optional[_Iterable[_Union[Example, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetExampleRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateExampleRequest(_message.Message):
    __slots__ = ('example', 'update_mask')
    EXAMPLE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    example: Example
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, example: _Optional[_Union[Example, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class Example(_message.Message):
    __slots__ = ('name', 'playbook_input', 'playbook_output', 'actions', 'display_name', 'description', 'token_count', 'create_time', 'update_time', 'conversation_state', 'language_code')
    NAME_FIELD_NUMBER: _ClassVar[int]
    PLAYBOOK_INPUT_FIELD_NUMBER: _ClassVar[int]
    PLAYBOOK_OUTPUT_FIELD_NUMBER: _ClassVar[int]
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TOKEN_COUNT_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_STATE_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    name: str
    playbook_input: PlaybookInput
    playbook_output: PlaybookOutput
    actions: _containers.RepeatedCompositeFieldContainer[Action]
    display_name: str
    description: str
    token_count: int
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    conversation_state: OutputState
    language_code: str

    def __init__(self, name: _Optional[str]=..., playbook_input: _Optional[_Union[PlaybookInput, _Mapping]]=..., playbook_output: _Optional[_Union[PlaybookOutput, _Mapping]]=..., actions: _Optional[_Iterable[_Union[Action, _Mapping]]]=..., display_name: _Optional[str]=..., description: _Optional[str]=..., token_count: _Optional[int]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., conversation_state: _Optional[_Union[OutputState, str]]=..., language_code: _Optional[str]=...) -> None:
        ...

class PlaybookInput(_message.Message):
    __slots__ = ('preceding_conversation_summary', 'action_parameters')
    PRECEDING_CONVERSATION_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    ACTION_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    preceding_conversation_summary: str
    action_parameters: _struct_pb2.Struct

    def __init__(self, preceding_conversation_summary: _Optional[str]=..., action_parameters: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=...) -> None:
        ...

class PlaybookOutput(_message.Message):
    __slots__ = ('execution_summary', 'action_parameters')
    EXECUTION_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    ACTION_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    execution_summary: str
    action_parameters: _struct_pb2.Struct

    def __init__(self, execution_summary: _Optional[str]=..., action_parameters: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=...) -> None:
        ...

class Action(_message.Message):
    __slots__ = ('user_utterance', 'agent_utterance', 'tool_use', 'playbook_invocation', 'flow_invocation')
    USER_UTTERANCE_FIELD_NUMBER: _ClassVar[int]
    AGENT_UTTERANCE_FIELD_NUMBER: _ClassVar[int]
    TOOL_USE_FIELD_NUMBER: _ClassVar[int]
    PLAYBOOK_INVOCATION_FIELD_NUMBER: _ClassVar[int]
    FLOW_INVOCATION_FIELD_NUMBER: _ClassVar[int]
    user_utterance: UserUtterance
    agent_utterance: AgentUtterance
    tool_use: ToolUse
    playbook_invocation: PlaybookInvocation
    flow_invocation: FlowInvocation

    def __init__(self, user_utterance: _Optional[_Union[UserUtterance, _Mapping]]=..., agent_utterance: _Optional[_Union[AgentUtterance, _Mapping]]=..., tool_use: _Optional[_Union[ToolUse, _Mapping]]=..., playbook_invocation: _Optional[_Union[PlaybookInvocation, _Mapping]]=..., flow_invocation: _Optional[_Union[FlowInvocation, _Mapping]]=...) -> None:
        ...

class UserUtterance(_message.Message):
    __slots__ = ('text',)
    TEXT_FIELD_NUMBER: _ClassVar[int]
    text: str

    def __init__(self, text: _Optional[str]=...) -> None:
        ...

class AgentUtterance(_message.Message):
    __slots__ = ('text',)
    TEXT_FIELD_NUMBER: _ClassVar[int]
    text: str

    def __init__(self, text: _Optional[str]=...) -> None:
        ...

class ToolUse(_message.Message):
    __slots__ = ('tool', 'action', 'input_action_parameters', 'output_action_parameters')
    TOOL_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    INPUT_ACTION_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_ACTION_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    tool: str
    action: str
    input_action_parameters: _struct_pb2.Struct
    output_action_parameters: _struct_pb2.Struct

    def __init__(self, tool: _Optional[str]=..., action: _Optional[str]=..., input_action_parameters: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=..., output_action_parameters: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=...) -> None:
        ...

class PlaybookInvocation(_message.Message):
    __slots__ = ('playbook', 'playbook_input', 'playbook_output', 'playbook_state')
    PLAYBOOK_FIELD_NUMBER: _ClassVar[int]
    PLAYBOOK_INPUT_FIELD_NUMBER: _ClassVar[int]
    PLAYBOOK_OUTPUT_FIELD_NUMBER: _ClassVar[int]
    PLAYBOOK_STATE_FIELD_NUMBER: _ClassVar[int]
    playbook: str
    playbook_input: PlaybookInput
    playbook_output: PlaybookOutput
    playbook_state: OutputState

    def __init__(self, playbook: _Optional[str]=..., playbook_input: _Optional[_Union[PlaybookInput, _Mapping]]=..., playbook_output: _Optional[_Union[PlaybookOutput, _Mapping]]=..., playbook_state: _Optional[_Union[OutputState, str]]=...) -> None:
        ...

class FlowInvocation(_message.Message):
    __slots__ = ('flow', 'input_action_parameters', 'output_action_parameters', 'flow_state')
    FLOW_FIELD_NUMBER: _ClassVar[int]
    INPUT_ACTION_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_ACTION_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    FLOW_STATE_FIELD_NUMBER: _ClassVar[int]
    flow: str
    input_action_parameters: _struct_pb2.Struct
    output_action_parameters: _struct_pb2.Struct
    flow_state: OutputState

    def __init__(self, flow: _Optional[str]=..., input_action_parameters: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=..., output_action_parameters: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=..., flow_state: _Optional[_Union[OutputState, str]]=...) -> None:
        ...