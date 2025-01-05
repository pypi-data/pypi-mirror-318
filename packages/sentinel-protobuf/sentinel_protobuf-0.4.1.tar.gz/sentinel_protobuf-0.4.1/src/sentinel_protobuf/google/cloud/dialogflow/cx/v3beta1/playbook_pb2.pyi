from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.dialogflow.cx.v3beta1 import example_pb2 as _example_pb2
from google.cloud.dialogflow.cx.v3beta1 import generative_settings_pb2 as _generative_settings_pb2
from google.cloud.dialogflow.cx.v3beta1 import parameter_definition_pb2 as _parameter_definition_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CreatePlaybookRequest(_message.Message):
    __slots__ = ('parent', 'playbook')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PLAYBOOK_FIELD_NUMBER: _ClassVar[int]
    parent: str
    playbook: Playbook

    def __init__(self, parent: _Optional[str]=..., playbook: _Optional[_Union[Playbook, _Mapping]]=...) -> None:
        ...

class DeletePlaybookRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListPlaybooksRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListPlaybooksResponse(_message.Message):
    __slots__ = ('playbooks', 'next_page_token')
    PLAYBOOKS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    playbooks: _containers.RepeatedCompositeFieldContainer[Playbook]
    next_page_token: str

    def __init__(self, playbooks: _Optional[_Iterable[_Union[Playbook, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetPlaybookRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdatePlaybookRequest(_message.Message):
    __slots__ = ('playbook', 'update_mask')
    PLAYBOOK_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    playbook: Playbook
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, playbook: _Optional[_Union[Playbook, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class Playbook(_message.Message):
    __slots__ = ('name', 'display_name', 'goal', 'input_parameter_definitions', 'output_parameter_definitions', 'instruction', 'token_count', 'create_time', 'update_time', 'referenced_playbooks', 'referenced_flows', 'referenced_tools', 'llm_model_settings')

    class Step(_message.Message):
        __slots__ = ('text', 'steps')
        TEXT_FIELD_NUMBER: _ClassVar[int]
        STEPS_FIELD_NUMBER: _ClassVar[int]
        text: str
        steps: _containers.RepeatedCompositeFieldContainer[Playbook.Step]

        def __init__(self, text: _Optional[str]=..., steps: _Optional[_Iterable[_Union[Playbook.Step, _Mapping]]]=...) -> None:
            ...

    class Instruction(_message.Message):
        __slots__ = ('steps',)
        STEPS_FIELD_NUMBER: _ClassVar[int]
        steps: _containers.RepeatedCompositeFieldContainer[Playbook.Step]

        def __init__(self, steps: _Optional[_Iterable[_Union[Playbook.Step, _Mapping]]]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    GOAL_FIELD_NUMBER: _ClassVar[int]
    INPUT_PARAMETER_DEFINITIONS_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_PARAMETER_DEFINITIONS_FIELD_NUMBER: _ClassVar[int]
    INSTRUCTION_FIELD_NUMBER: _ClassVar[int]
    TOKEN_COUNT_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    REFERENCED_PLAYBOOKS_FIELD_NUMBER: _ClassVar[int]
    REFERENCED_FLOWS_FIELD_NUMBER: _ClassVar[int]
    REFERENCED_TOOLS_FIELD_NUMBER: _ClassVar[int]
    LLM_MODEL_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    goal: str
    input_parameter_definitions: _containers.RepeatedCompositeFieldContainer[_parameter_definition_pb2.ParameterDefinition]
    output_parameter_definitions: _containers.RepeatedCompositeFieldContainer[_parameter_definition_pb2.ParameterDefinition]
    instruction: Playbook.Instruction
    token_count: int
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    referenced_playbooks: _containers.RepeatedScalarFieldContainer[str]
    referenced_flows: _containers.RepeatedScalarFieldContainer[str]
    referenced_tools: _containers.RepeatedScalarFieldContainer[str]
    llm_model_settings: _generative_settings_pb2.LlmModelSettings

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., goal: _Optional[str]=..., input_parameter_definitions: _Optional[_Iterable[_Union[_parameter_definition_pb2.ParameterDefinition, _Mapping]]]=..., output_parameter_definitions: _Optional[_Iterable[_Union[_parameter_definition_pb2.ParameterDefinition, _Mapping]]]=..., instruction: _Optional[_Union[Playbook.Instruction, _Mapping]]=..., token_count: _Optional[int]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., referenced_playbooks: _Optional[_Iterable[str]]=..., referenced_flows: _Optional[_Iterable[str]]=..., referenced_tools: _Optional[_Iterable[str]]=..., llm_model_settings: _Optional[_Union[_generative_settings_pb2.LlmModelSettings, _Mapping]]=...) -> None:
        ...

class CreatePlaybookVersionRequest(_message.Message):
    __slots__ = ('parent', 'playbook_version')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PLAYBOOK_VERSION_FIELD_NUMBER: _ClassVar[int]
    parent: str
    playbook_version: PlaybookVersion

    def __init__(self, parent: _Optional[str]=..., playbook_version: _Optional[_Union[PlaybookVersion, _Mapping]]=...) -> None:
        ...

class PlaybookVersion(_message.Message):
    __slots__ = ('name', 'description', 'playbook', 'examples', 'update_time')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PLAYBOOK_FIELD_NUMBER: _ClassVar[int]
    EXAMPLES_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    playbook: Playbook
    examples: _containers.RepeatedCompositeFieldContainer[_example_pb2.Example]
    update_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., description: _Optional[str]=..., playbook: _Optional[_Union[Playbook, _Mapping]]=..., examples: _Optional[_Iterable[_Union[_example_pb2.Example, _Mapping]]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class GetPlaybookVersionRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListPlaybookVersionsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListPlaybookVersionsResponse(_message.Message):
    __slots__ = ('playbook_versions', 'next_page_token')
    PLAYBOOK_VERSIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    playbook_versions: _containers.RepeatedCompositeFieldContainer[PlaybookVersion]
    next_page_token: str

    def __init__(self, playbook_versions: _Optional[_Iterable[_Union[PlaybookVersion, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class DeletePlaybookVersionRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...