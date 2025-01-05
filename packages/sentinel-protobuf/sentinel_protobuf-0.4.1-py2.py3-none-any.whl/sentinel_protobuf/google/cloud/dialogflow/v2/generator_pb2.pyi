from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TriggerEvent(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TRIGGER_EVENT_UNSPECIFIED: _ClassVar[TriggerEvent]
    END_OF_UTTERANCE: _ClassVar[TriggerEvent]
    MANUAL_CALL: _ClassVar[TriggerEvent]
TRIGGER_EVENT_UNSPECIFIED: TriggerEvent
END_OF_UTTERANCE: TriggerEvent
MANUAL_CALL: TriggerEvent

class CreateGeneratorRequest(_message.Message):
    __slots__ = ("parent", "generator", "generator_id")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    GENERATOR_FIELD_NUMBER: _ClassVar[int]
    GENERATOR_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    generator: Generator
    generator_id: str
    def __init__(self, parent: _Optional[str] = ..., generator: _Optional[_Union[Generator, _Mapping]] = ..., generator_id: _Optional[str] = ...) -> None: ...

class GetGeneratorRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListGeneratorsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListGeneratorsResponse(_message.Message):
    __slots__ = ("generators", "next_page_token")
    GENERATORS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    generators: _containers.RepeatedCompositeFieldContainer[Generator]
    next_page_token: str
    def __init__(self, generators: _Optional[_Iterable[_Union[Generator, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class DeleteGeneratorRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class UpdateGeneratorRequest(_message.Message):
    __slots__ = ("generator", "update_mask")
    GENERATOR_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    generator: Generator
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, generator: _Optional[_Union[Generator, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class MessageEntry(_message.Message):
    __slots__ = ("role", "text", "language_code", "create_time")
    class Role(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ROLE_UNSPECIFIED: _ClassVar[MessageEntry.Role]
        HUMAN_AGENT: _ClassVar[MessageEntry.Role]
        AUTOMATED_AGENT: _ClassVar[MessageEntry.Role]
        END_USER: _ClassVar[MessageEntry.Role]
    ROLE_UNSPECIFIED: MessageEntry.Role
    HUMAN_AGENT: MessageEntry.Role
    AUTOMATED_AGENT: MessageEntry.Role
    END_USER: MessageEntry.Role
    ROLE_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    role: MessageEntry.Role
    text: str
    language_code: str
    create_time: _timestamp_pb2.Timestamp
    def __init__(self, role: _Optional[_Union[MessageEntry.Role, str]] = ..., text: _Optional[str] = ..., language_code: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ConversationContext(_message.Message):
    __slots__ = ("message_entries",)
    MESSAGE_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    message_entries: _containers.RepeatedCompositeFieldContainer[MessageEntry]
    def __init__(self, message_entries: _Optional[_Iterable[_Union[MessageEntry, _Mapping]]] = ...) -> None: ...

class SummarizationSectionList(_message.Message):
    __slots__ = ("summarization_sections",)
    SUMMARIZATION_SECTIONS_FIELD_NUMBER: _ClassVar[int]
    summarization_sections: _containers.RepeatedCompositeFieldContainer[SummarizationSection]
    def __init__(self, summarization_sections: _Optional[_Iterable[_Union[SummarizationSection, _Mapping]]] = ...) -> None: ...

class FewShotExample(_message.Message):
    __slots__ = ("conversation_context", "extra_info", "summarization_section_list", "output")
    class ExtraInfoEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    CONVERSATION_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    EXTRA_INFO_FIELD_NUMBER: _ClassVar[int]
    SUMMARIZATION_SECTION_LIST_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_FIELD_NUMBER: _ClassVar[int]
    conversation_context: ConversationContext
    extra_info: _containers.ScalarMap[str, str]
    summarization_section_list: SummarizationSectionList
    output: GeneratorSuggestion
    def __init__(self, conversation_context: _Optional[_Union[ConversationContext, _Mapping]] = ..., extra_info: _Optional[_Mapping[str, str]] = ..., summarization_section_list: _Optional[_Union[SummarizationSectionList, _Mapping]] = ..., output: _Optional[_Union[GeneratorSuggestion, _Mapping]] = ...) -> None: ...

class InferenceParameter(_message.Message):
    __slots__ = ("max_output_tokens", "temperature", "top_k", "top_p")
    MAX_OUTPUT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    TOP_K_FIELD_NUMBER: _ClassVar[int]
    TOP_P_FIELD_NUMBER: _ClassVar[int]
    max_output_tokens: int
    temperature: float
    top_k: int
    top_p: float
    def __init__(self, max_output_tokens: _Optional[int] = ..., temperature: _Optional[float] = ..., top_k: _Optional[int] = ..., top_p: _Optional[float] = ...) -> None: ...

class SummarizationSection(_message.Message):
    __slots__ = ("key", "definition", "type")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[SummarizationSection.Type]
        SITUATION: _ClassVar[SummarizationSection.Type]
        ACTION: _ClassVar[SummarizationSection.Type]
        RESOLUTION: _ClassVar[SummarizationSection.Type]
        REASON_FOR_CANCELLATION: _ClassVar[SummarizationSection.Type]
        CUSTOMER_SATISFACTION: _ClassVar[SummarizationSection.Type]
        ENTITIES: _ClassVar[SummarizationSection.Type]
        CUSTOMER_DEFINED: _ClassVar[SummarizationSection.Type]
    TYPE_UNSPECIFIED: SummarizationSection.Type
    SITUATION: SummarizationSection.Type
    ACTION: SummarizationSection.Type
    RESOLUTION: SummarizationSection.Type
    REASON_FOR_CANCELLATION: SummarizationSection.Type
    CUSTOMER_SATISFACTION: SummarizationSection.Type
    ENTITIES: SummarizationSection.Type
    CUSTOMER_DEFINED: SummarizationSection.Type
    KEY_FIELD_NUMBER: _ClassVar[int]
    DEFINITION_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    key: str
    definition: str
    type: SummarizationSection.Type
    def __init__(self, key: _Optional[str] = ..., definition: _Optional[str] = ..., type: _Optional[_Union[SummarizationSection.Type, str]] = ...) -> None: ...

class SummarizationContext(_message.Message):
    __slots__ = ("summarization_sections", "few_shot_examples", "version", "output_language_code")
    SUMMARIZATION_SECTIONS_FIELD_NUMBER: _ClassVar[int]
    FEW_SHOT_EXAMPLES_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    summarization_sections: _containers.RepeatedCompositeFieldContainer[SummarizationSection]
    few_shot_examples: _containers.RepeatedCompositeFieldContainer[FewShotExample]
    version: str
    output_language_code: str
    def __init__(self, summarization_sections: _Optional[_Iterable[_Union[SummarizationSection, _Mapping]]] = ..., few_shot_examples: _Optional[_Iterable[_Union[FewShotExample, _Mapping]]] = ..., version: _Optional[str] = ..., output_language_code: _Optional[str] = ...) -> None: ...

class Generator(_message.Message):
    __slots__ = ("name", "description", "summarization_context", "inference_parameter", "trigger_event", "create_time", "update_time")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SUMMARIZATION_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    INFERENCE_PARAMETER_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_EVENT_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    summarization_context: SummarizationContext
    inference_parameter: InferenceParameter
    trigger_event: TriggerEvent
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., summarization_context: _Optional[_Union[SummarizationContext, _Mapping]] = ..., inference_parameter: _Optional[_Union[InferenceParameter, _Mapping]] = ..., trigger_event: _Optional[_Union[TriggerEvent, str]] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class SummarySuggestion(_message.Message):
    __slots__ = ("summary_sections",)
    class SummarySection(_message.Message):
        __slots__ = ("section", "summary")
        SECTION_FIELD_NUMBER: _ClassVar[int]
        SUMMARY_FIELD_NUMBER: _ClassVar[int]
        section: str
        summary: str
        def __init__(self, section: _Optional[str] = ..., summary: _Optional[str] = ...) -> None: ...
    SUMMARY_SECTIONS_FIELD_NUMBER: _ClassVar[int]
    summary_sections: _containers.RepeatedCompositeFieldContainer[SummarySuggestion.SummarySection]
    def __init__(self, summary_sections: _Optional[_Iterable[_Union[SummarySuggestion.SummarySection, _Mapping]]] = ...) -> None: ...

class GeneratorSuggestion(_message.Message):
    __slots__ = ("summary_suggestion",)
    SUMMARY_SUGGESTION_FIELD_NUMBER: _ClassVar[int]
    summary_suggestion: SummarySuggestion
    def __init__(self, summary_suggestion: _Optional[_Union[SummarySuggestion, _Mapping]] = ...) -> None: ...
