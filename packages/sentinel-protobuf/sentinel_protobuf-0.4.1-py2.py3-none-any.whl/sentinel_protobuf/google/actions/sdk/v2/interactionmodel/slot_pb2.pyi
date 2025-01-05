from google.actions.sdk.v2.interactionmodel import event_handler_pb2 as _event_handler_pb2
from google.actions.sdk.v2.interactionmodel.type import class_reference_pb2 as _class_reference_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Slot(_message.Message):
    __slots__ = ('name', 'type', 'required', 'prompt_settings', 'commit_behavior', 'config', 'default_value')

    class PromptSettings(_message.Message):
        __slots__ = ('initial_prompt', 'no_match_prompt1', 'no_match_prompt2', 'no_match_final_prompt', 'no_input_prompt1', 'no_input_prompt2', 'no_input_final_prompt')
        INITIAL_PROMPT_FIELD_NUMBER: _ClassVar[int]
        NO_MATCH_PROMPT1_FIELD_NUMBER: _ClassVar[int]
        NO_MATCH_PROMPT2_FIELD_NUMBER: _ClassVar[int]
        NO_MATCH_FINAL_PROMPT_FIELD_NUMBER: _ClassVar[int]
        NO_INPUT_PROMPT1_FIELD_NUMBER: _ClassVar[int]
        NO_INPUT_PROMPT2_FIELD_NUMBER: _ClassVar[int]
        NO_INPUT_FINAL_PROMPT_FIELD_NUMBER: _ClassVar[int]
        initial_prompt: _event_handler_pb2.EventHandler
        no_match_prompt1: _event_handler_pb2.EventHandler
        no_match_prompt2: _event_handler_pb2.EventHandler
        no_match_final_prompt: _event_handler_pb2.EventHandler
        no_input_prompt1: _event_handler_pb2.EventHandler
        no_input_prompt2: _event_handler_pb2.EventHandler
        no_input_final_prompt: _event_handler_pb2.EventHandler

        def __init__(self, initial_prompt: _Optional[_Union[_event_handler_pb2.EventHandler, _Mapping]]=..., no_match_prompt1: _Optional[_Union[_event_handler_pb2.EventHandler, _Mapping]]=..., no_match_prompt2: _Optional[_Union[_event_handler_pb2.EventHandler, _Mapping]]=..., no_match_final_prompt: _Optional[_Union[_event_handler_pb2.EventHandler, _Mapping]]=..., no_input_prompt1: _Optional[_Union[_event_handler_pb2.EventHandler, _Mapping]]=..., no_input_prompt2: _Optional[_Union[_event_handler_pb2.EventHandler, _Mapping]]=..., no_input_final_prompt: _Optional[_Union[_event_handler_pb2.EventHandler, _Mapping]]=...) -> None:
            ...

    class CommitBehavior(_message.Message):
        __slots__ = ('write_session_param',)
        WRITE_SESSION_PARAM_FIELD_NUMBER: _ClassVar[int]
        write_session_param: str

        def __init__(self, write_session_param: _Optional[str]=...) -> None:
            ...

    class DefaultValue(_message.Message):
        __slots__ = ('session_param', 'constant')
        SESSION_PARAM_FIELD_NUMBER: _ClassVar[int]
        CONSTANT_FIELD_NUMBER: _ClassVar[int]
        session_param: str
        constant: _struct_pb2.Value

        def __init__(self, session_param: _Optional[str]=..., constant: _Optional[_Union[_struct_pb2.Value, _Mapping]]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_FIELD_NUMBER: _ClassVar[int]
    PROMPT_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    COMMIT_BEHAVIOR_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: _class_reference_pb2.ClassReference
    required: bool
    prompt_settings: Slot.PromptSettings
    commit_behavior: Slot.CommitBehavior
    config: _struct_pb2.Value
    default_value: Slot.DefaultValue

    def __init__(self, name: _Optional[str]=..., type: _Optional[_Union[_class_reference_pb2.ClassReference, _Mapping]]=..., required: bool=..., prompt_settings: _Optional[_Union[Slot.PromptSettings, _Mapping]]=..., commit_behavior: _Optional[_Union[Slot.CommitBehavior, _Mapping]]=..., config: _Optional[_Union[_struct_pb2.Value, _Mapping]]=..., default_value: _Optional[_Union[Slot.DefaultValue, _Mapping]]=...) -> None:
        ...