from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.dialogflow.v2 import conversation_profile_pb2 as _conversation_profile_pb2
from google.cloud.dialogflow.v2 import generator_pb2 as _generator_pb2
from google.cloud.dialogflow.v2 import participant_pb2 as _participant_pb2
from google.cloud.dialogflow.v2 import session_pb2 as _session_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Conversation(_message.Message):
    __slots__ = ("name", "lifecycle_state", "conversation_profile", "phone_number", "start_time", "end_time", "conversation_stage")
    class LifecycleState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        LIFECYCLE_STATE_UNSPECIFIED: _ClassVar[Conversation.LifecycleState]
        IN_PROGRESS: _ClassVar[Conversation.LifecycleState]
        COMPLETED: _ClassVar[Conversation.LifecycleState]
    LIFECYCLE_STATE_UNSPECIFIED: Conversation.LifecycleState
    IN_PROGRESS: Conversation.LifecycleState
    COMPLETED: Conversation.LifecycleState
    class ConversationStage(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CONVERSATION_STAGE_UNSPECIFIED: _ClassVar[Conversation.ConversationStage]
        VIRTUAL_AGENT_STAGE: _ClassVar[Conversation.ConversationStage]
        HUMAN_ASSIST_STAGE: _ClassVar[Conversation.ConversationStage]
    CONVERSATION_STAGE_UNSPECIFIED: Conversation.ConversationStage
    VIRTUAL_AGENT_STAGE: Conversation.ConversationStage
    HUMAN_ASSIST_STAGE: Conversation.ConversationStage
    NAME_FIELD_NUMBER: _ClassVar[int]
    LIFECYCLE_STATE_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_PROFILE_FIELD_NUMBER: _ClassVar[int]
    PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_STAGE_FIELD_NUMBER: _ClassVar[int]
    name: str
    lifecycle_state: Conversation.LifecycleState
    conversation_profile: str
    phone_number: ConversationPhoneNumber
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    conversation_stage: Conversation.ConversationStage
    def __init__(self, name: _Optional[str] = ..., lifecycle_state: _Optional[_Union[Conversation.LifecycleState, str]] = ..., conversation_profile: _Optional[str] = ..., phone_number: _Optional[_Union[ConversationPhoneNumber, _Mapping]] = ..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., conversation_stage: _Optional[_Union[Conversation.ConversationStage, str]] = ...) -> None: ...

class CreateConversationRequest(_message.Message):
    __slots__ = ("parent", "conversation", "conversation_id")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    conversation: Conversation
    conversation_id: str
    def __init__(self, parent: _Optional[str] = ..., conversation: _Optional[_Union[Conversation, _Mapping]] = ..., conversation_id: _Optional[str] = ...) -> None: ...

class ListConversationsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token", "filter")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[str] = ...) -> None: ...

class ListConversationsResponse(_message.Message):
    __slots__ = ("conversations", "next_page_token")
    CONVERSATIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    conversations: _containers.RepeatedCompositeFieldContainer[Conversation]
    next_page_token: str
    def __init__(self, conversations: _Optional[_Iterable[_Union[Conversation, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class GetConversationRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CompleteConversationRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListMessagesRequest(_message.Message):
    __slots__ = ("parent", "filter", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., filter: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListMessagesResponse(_message.Message):
    __slots__ = ("messages", "next_page_token")
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    messages: _containers.RepeatedCompositeFieldContainer[_participant_pb2.Message]
    next_page_token: str
    def __init__(self, messages: _Optional[_Iterable[_Union[_participant_pb2.Message, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class ConversationPhoneNumber(_message.Message):
    __slots__ = ("phone_number",)
    PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    phone_number: str
    def __init__(self, phone_number: _Optional[str] = ...) -> None: ...

class SuggestConversationSummaryRequest(_message.Message):
    __slots__ = ("conversation", "latest_message", "context_size", "assist_query_params")
    CONVERSATION_FIELD_NUMBER: _ClassVar[int]
    LATEST_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_SIZE_FIELD_NUMBER: _ClassVar[int]
    ASSIST_QUERY_PARAMS_FIELD_NUMBER: _ClassVar[int]
    conversation: str
    latest_message: str
    context_size: int
    assist_query_params: _participant_pb2.AssistQueryParameters
    def __init__(self, conversation: _Optional[str] = ..., latest_message: _Optional[str] = ..., context_size: _Optional[int] = ..., assist_query_params: _Optional[_Union[_participant_pb2.AssistQueryParameters, _Mapping]] = ...) -> None: ...

class SuggestConversationSummaryResponse(_message.Message):
    __slots__ = ("summary", "latest_message", "context_size")
    class Summary(_message.Message):
        __slots__ = ("text", "text_sections", "answer_record", "baseline_model_version")
        class TextSectionsEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str
            def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
        TEXT_FIELD_NUMBER: _ClassVar[int]
        TEXT_SECTIONS_FIELD_NUMBER: _ClassVar[int]
        ANSWER_RECORD_FIELD_NUMBER: _ClassVar[int]
        BASELINE_MODEL_VERSION_FIELD_NUMBER: _ClassVar[int]
        text: str
        text_sections: _containers.ScalarMap[str, str]
        answer_record: str
        baseline_model_version: str
        def __init__(self, text: _Optional[str] = ..., text_sections: _Optional[_Mapping[str, str]] = ..., answer_record: _Optional[str] = ..., baseline_model_version: _Optional[str] = ...) -> None: ...
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    LATEST_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_SIZE_FIELD_NUMBER: _ClassVar[int]
    summary: SuggestConversationSummaryResponse.Summary
    latest_message: str
    context_size: int
    def __init__(self, summary: _Optional[_Union[SuggestConversationSummaryResponse.Summary, _Mapping]] = ..., latest_message: _Optional[str] = ..., context_size: _Optional[int] = ...) -> None: ...

class GenerateStatelessSummaryRequest(_message.Message):
    __slots__ = ("stateless_conversation", "conversation_profile", "latest_message", "max_context_size")
    class MinimalConversation(_message.Message):
        __slots__ = ("messages", "parent")
        MESSAGES_FIELD_NUMBER: _ClassVar[int]
        PARENT_FIELD_NUMBER: _ClassVar[int]
        messages: _containers.RepeatedCompositeFieldContainer[_participant_pb2.Message]
        parent: str
        def __init__(self, messages: _Optional[_Iterable[_Union[_participant_pb2.Message, _Mapping]]] = ..., parent: _Optional[str] = ...) -> None: ...
    STATELESS_CONVERSATION_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_PROFILE_FIELD_NUMBER: _ClassVar[int]
    LATEST_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    MAX_CONTEXT_SIZE_FIELD_NUMBER: _ClassVar[int]
    stateless_conversation: GenerateStatelessSummaryRequest.MinimalConversation
    conversation_profile: _conversation_profile_pb2.ConversationProfile
    latest_message: str
    max_context_size: int
    def __init__(self, stateless_conversation: _Optional[_Union[GenerateStatelessSummaryRequest.MinimalConversation, _Mapping]] = ..., conversation_profile: _Optional[_Union[_conversation_profile_pb2.ConversationProfile, _Mapping]] = ..., latest_message: _Optional[str] = ..., max_context_size: _Optional[int] = ...) -> None: ...

class GenerateStatelessSummaryResponse(_message.Message):
    __slots__ = ("summary", "latest_message", "context_size")
    class Summary(_message.Message):
        __slots__ = ("text", "text_sections", "baseline_model_version")
        class TextSectionsEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str
            def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
        TEXT_FIELD_NUMBER: _ClassVar[int]
        TEXT_SECTIONS_FIELD_NUMBER: _ClassVar[int]
        BASELINE_MODEL_VERSION_FIELD_NUMBER: _ClassVar[int]
        text: str
        text_sections: _containers.ScalarMap[str, str]
        baseline_model_version: str
        def __init__(self, text: _Optional[str] = ..., text_sections: _Optional[_Mapping[str, str]] = ..., baseline_model_version: _Optional[str] = ...) -> None: ...
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    LATEST_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_SIZE_FIELD_NUMBER: _ClassVar[int]
    summary: GenerateStatelessSummaryResponse.Summary
    latest_message: str
    context_size: int
    def __init__(self, summary: _Optional[_Union[GenerateStatelessSummaryResponse.Summary, _Mapping]] = ..., latest_message: _Optional[str] = ..., context_size: _Optional[int] = ...) -> None: ...

class GenerateStatelessSuggestionRequest(_message.Message):
    __slots__ = ("parent", "generator", "generator_name", "conversation_context", "trigger_events")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    GENERATOR_FIELD_NUMBER: _ClassVar[int]
    GENERATOR_NAME_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_EVENTS_FIELD_NUMBER: _ClassVar[int]
    parent: str
    generator: _generator_pb2.Generator
    generator_name: str
    conversation_context: _generator_pb2.ConversationContext
    trigger_events: _containers.RepeatedScalarFieldContainer[_generator_pb2.TriggerEvent]
    def __init__(self, parent: _Optional[str] = ..., generator: _Optional[_Union[_generator_pb2.Generator, _Mapping]] = ..., generator_name: _Optional[str] = ..., conversation_context: _Optional[_Union[_generator_pb2.ConversationContext, _Mapping]] = ..., trigger_events: _Optional[_Iterable[_Union[_generator_pb2.TriggerEvent, str]]] = ...) -> None: ...

class GenerateStatelessSuggestionResponse(_message.Message):
    __slots__ = ("generator_suggestion",)
    GENERATOR_SUGGESTION_FIELD_NUMBER: _ClassVar[int]
    generator_suggestion: _generator_pb2.GeneratorSuggestion
    def __init__(self, generator_suggestion: _Optional[_Union[_generator_pb2.GeneratorSuggestion, _Mapping]] = ...) -> None: ...

class SearchKnowledgeRequest(_message.Message):
    __slots__ = ("parent", "query", "conversation_profile", "session_id", "conversation", "latest_message", "query_source", "end_user_metadata", "search_config", "exact_search")
    class QuerySource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        QUERY_SOURCE_UNSPECIFIED: _ClassVar[SearchKnowledgeRequest.QuerySource]
        AGENT_QUERY: _ClassVar[SearchKnowledgeRequest.QuerySource]
        SUGGESTED_QUERY: _ClassVar[SearchKnowledgeRequest.QuerySource]
    QUERY_SOURCE_UNSPECIFIED: SearchKnowledgeRequest.QuerySource
    AGENT_QUERY: SearchKnowledgeRequest.QuerySource
    SUGGESTED_QUERY: SearchKnowledgeRequest.QuerySource
    class SearchConfig(_message.Message):
        __slots__ = ("boost_specs", "filter_specs")
        class BoostSpecs(_message.Message):
            __slots__ = ("data_stores", "spec")
            class BoostSpec(_message.Message):
                __slots__ = ("condition_boost_specs",)
                class ConditionBoostSpec(_message.Message):
                    __slots__ = ("condition", "boost", "boost_control_spec")
                    class BoostControlSpec(_message.Message):
                        __slots__ = ("field_name", "attribute_type", "interpolation_type", "control_points")
                        class AttributeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                            __slots__ = ()
                            ATTRIBUTE_TYPE_UNSPECIFIED: _ClassVar[SearchKnowledgeRequest.SearchConfig.BoostSpecs.BoostSpec.ConditionBoostSpec.BoostControlSpec.AttributeType]
                            NUMERICAL: _ClassVar[SearchKnowledgeRequest.SearchConfig.BoostSpecs.BoostSpec.ConditionBoostSpec.BoostControlSpec.AttributeType]
                            FRESHNESS: _ClassVar[SearchKnowledgeRequest.SearchConfig.BoostSpecs.BoostSpec.ConditionBoostSpec.BoostControlSpec.AttributeType]
                        ATTRIBUTE_TYPE_UNSPECIFIED: SearchKnowledgeRequest.SearchConfig.BoostSpecs.BoostSpec.ConditionBoostSpec.BoostControlSpec.AttributeType
                        NUMERICAL: SearchKnowledgeRequest.SearchConfig.BoostSpecs.BoostSpec.ConditionBoostSpec.BoostControlSpec.AttributeType
                        FRESHNESS: SearchKnowledgeRequest.SearchConfig.BoostSpecs.BoostSpec.ConditionBoostSpec.BoostControlSpec.AttributeType
                        class InterpolationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                            __slots__ = ()
                            INTERPOLATION_TYPE_UNSPECIFIED: _ClassVar[SearchKnowledgeRequest.SearchConfig.BoostSpecs.BoostSpec.ConditionBoostSpec.BoostControlSpec.InterpolationType]
                            LINEAR: _ClassVar[SearchKnowledgeRequest.SearchConfig.BoostSpecs.BoostSpec.ConditionBoostSpec.BoostControlSpec.InterpolationType]
                        INTERPOLATION_TYPE_UNSPECIFIED: SearchKnowledgeRequest.SearchConfig.BoostSpecs.BoostSpec.ConditionBoostSpec.BoostControlSpec.InterpolationType
                        LINEAR: SearchKnowledgeRequest.SearchConfig.BoostSpecs.BoostSpec.ConditionBoostSpec.BoostControlSpec.InterpolationType
                        class ControlPoint(_message.Message):
                            __slots__ = ()
                            def __init__(self) -> None: ...
                        FIELD_NAME_FIELD_NUMBER: _ClassVar[int]
                        ATTRIBUTE_TYPE_FIELD_NUMBER: _ClassVar[int]
                        INTERPOLATION_TYPE_FIELD_NUMBER: _ClassVar[int]
                        CONTROL_POINTS_FIELD_NUMBER: _ClassVar[int]
                        field_name: str
                        attribute_type: SearchKnowledgeRequest.SearchConfig.BoostSpecs.BoostSpec.ConditionBoostSpec.BoostControlSpec.AttributeType
                        interpolation_type: SearchKnowledgeRequest.SearchConfig.BoostSpecs.BoostSpec.ConditionBoostSpec.BoostControlSpec.InterpolationType
                        control_points: _containers.RepeatedCompositeFieldContainer[SearchKnowledgeRequest.SearchConfig.BoostSpecs.BoostSpec.ConditionBoostSpec.BoostControlSpec.ControlPoint]
                        def __init__(self, field_name: _Optional[str] = ..., attribute_type: _Optional[_Union[SearchKnowledgeRequest.SearchConfig.BoostSpecs.BoostSpec.ConditionBoostSpec.BoostControlSpec.AttributeType, str]] = ..., interpolation_type: _Optional[_Union[SearchKnowledgeRequest.SearchConfig.BoostSpecs.BoostSpec.ConditionBoostSpec.BoostControlSpec.InterpolationType, str]] = ..., control_points: _Optional[_Iterable[_Union[SearchKnowledgeRequest.SearchConfig.BoostSpecs.BoostSpec.ConditionBoostSpec.BoostControlSpec.ControlPoint, _Mapping]]] = ...) -> None: ...
                    CONDITION_FIELD_NUMBER: _ClassVar[int]
                    BOOST_FIELD_NUMBER: _ClassVar[int]
                    BOOST_CONTROL_SPEC_FIELD_NUMBER: _ClassVar[int]
                    condition: str
                    boost: float
                    boost_control_spec: SearchKnowledgeRequest.SearchConfig.BoostSpecs.BoostSpec.ConditionBoostSpec.BoostControlSpec
                    def __init__(self, condition: _Optional[str] = ..., boost: _Optional[float] = ..., boost_control_spec: _Optional[_Union[SearchKnowledgeRequest.SearchConfig.BoostSpecs.BoostSpec.ConditionBoostSpec.BoostControlSpec, _Mapping]] = ...) -> None: ...
                CONDITION_BOOST_SPECS_FIELD_NUMBER: _ClassVar[int]
                condition_boost_specs: _containers.RepeatedCompositeFieldContainer[SearchKnowledgeRequest.SearchConfig.BoostSpecs.BoostSpec.ConditionBoostSpec]
                def __init__(self, condition_boost_specs: _Optional[_Iterable[_Union[SearchKnowledgeRequest.SearchConfig.BoostSpecs.BoostSpec.ConditionBoostSpec, _Mapping]]] = ...) -> None: ...
            DATA_STORES_FIELD_NUMBER: _ClassVar[int]
            SPEC_FIELD_NUMBER: _ClassVar[int]
            data_stores: _containers.RepeatedScalarFieldContainer[str]
            spec: _containers.RepeatedCompositeFieldContainer[SearchKnowledgeRequest.SearchConfig.BoostSpecs.BoostSpec]
            def __init__(self, data_stores: _Optional[_Iterable[str]] = ..., spec: _Optional[_Iterable[_Union[SearchKnowledgeRequest.SearchConfig.BoostSpecs.BoostSpec, _Mapping]]] = ...) -> None: ...
        class FilterSpecs(_message.Message):
            __slots__ = ("data_stores", "filter")
            DATA_STORES_FIELD_NUMBER: _ClassVar[int]
            FILTER_FIELD_NUMBER: _ClassVar[int]
            data_stores: _containers.RepeatedScalarFieldContainer[str]
            filter: str
            def __init__(self, data_stores: _Optional[_Iterable[str]] = ..., filter: _Optional[str] = ...) -> None: ...
        BOOST_SPECS_FIELD_NUMBER: _ClassVar[int]
        FILTER_SPECS_FIELD_NUMBER: _ClassVar[int]
        boost_specs: _containers.RepeatedCompositeFieldContainer[SearchKnowledgeRequest.SearchConfig.BoostSpecs]
        filter_specs: _containers.RepeatedCompositeFieldContainer[SearchKnowledgeRequest.SearchConfig.FilterSpecs]
        def __init__(self, boost_specs: _Optional[_Iterable[_Union[SearchKnowledgeRequest.SearchConfig.BoostSpecs, _Mapping]]] = ..., filter_specs: _Optional[_Iterable[_Union[SearchKnowledgeRequest.SearchConfig.FilterSpecs, _Mapping]]] = ...) -> None: ...
    PARENT_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_PROFILE_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_FIELD_NUMBER: _ClassVar[int]
    LATEST_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    QUERY_SOURCE_FIELD_NUMBER: _ClassVar[int]
    END_USER_METADATA_FIELD_NUMBER: _ClassVar[int]
    SEARCH_CONFIG_FIELD_NUMBER: _ClassVar[int]
    EXACT_SEARCH_FIELD_NUMBER: _ClassVar[int]
    parent: str
    query: _session_pb2.TextInput
    conversation_profile: str
    session_id: str
    conversation: str
    latest_message: str
    query_source: SearchKnowledgeRequest.QuerySource
    end_user_metadata: _struct_pb2.Struct
    search_config: SearchKnowledgeRequest.SearchConfig
    exact_search: bool
    def __init__(self, parent: _Optional[str] = ..., query: _Optional[_Union[_session_pb2.TextInput, _Mapping]] = ..., conversation_profile: _Optional[str] = ..., session_id: _Optional[str] = ..., conversation: _Optional[str] = ..., latest_message: _Optional[str] = ..., query_source: _Optional[_Union[SearchKnowledgeRequest.QuerySource, str]] = ..., end_user_metadata: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., search_config: _Optional[_Union[SearchKnowledgeRequest.SearchConfig, _Mapping]] = ..., exact_search: bool = ...) -> None: ...

class SearchKnowledgeResponse(_message.Message):
    __slots__ = ("answers", "rewritten_query")
    ANSWERS_FIELD_NUMBER: _ClassVar[int]
    REWRITTEN_QUERY_FIELD_NUMBER: _ClassVar[int]
    answers: _containers.RepeatedCompositeFieldContainer[SearchKnowledgeAnswer]
    rewritten_query: str
    def __init__(self, answers: _Optional[_Iterable[_Union[SearchKnowledgeAnswer, _Mapping]]] = ..., rewritten_query: _Optional[str] = ...) -> None: ...

class SearchKnowledgeAnswer(_message.Message):
    __slots__ = ("answer", "answer_type", "answer_sources", "answer_record")
    class AnswerType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ANSWER_TYPE_UNSPECIFIED: _ClassVar[SearchKnowledgeAnswer.AnswerType]
        FAQ: _ClassVar[SearchKnowledgeAnswer.AnswerType]
        GENERATIVE: _ClassVar[SearchKnowledgeAnswer.AnswerType]
        INTENT: _ClassVar[SearchKnowledgeAnswer.AnswerType]
    ANSWER_TYPE_UNSPECIFIED: SearchKnowledgeAnswer.AnswerType
    FAQ: SearchKnowledgeAnswer.AnswerType
    GENERATIVE: SearchKnowledgeAnswer.AnswerType
    INTENT: SearchKnowledgeAnswer.AnswerType
    class AnswerSource(_message.Message):
        __slots__ = ("title", "uri", "snippet", "metadata")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        URI_FIELD_NUMBER: _ClassVar[int]
        SNIPPET_FIELD_NUMBER: _ClassVar[int]
        METADATA_FIELD_NUMBER: _ClassVar[int]
        title: str
        uri: str
        snippet: str
        metadata: _struct_pb2.Struct
        def __init__(self, title: _Optional[str] = ..., uri: _Optional[str] = ..., snippet: _Optional[str] = ..., metadata: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...
    ANSWER_FIELD_NUMBER: _ClassVar[int]
    ANSWER_TYPE_FIELD_NUMBER: _ClassVar[int]
    ANSWER_SOURCES_FIELD_NUMBER: _ClassVar[int]
    ANSWER_RECORD_FIELD_NUMBER: _ClassVar[int]
    answer: str
    answer_type: SearchKnowledgeAnswer.AnswerType
    answer_sources: _containers.RepeatedCompositeFieldContainer[SearchKnowledgeAnswer.AnswerSource]
    answer_record: str
    def __init__(self, answer: _Optional[str] = ..., answer_type: _Optional[_Union[SearchKnowledgeAnswer.AnswerType, str]] = ..., answer_sources: _Optional[_Iterable[_Union[SearchKnowledgeAnswer.AnswerSource, _Mapping]]] = ..., answer_record: _Optional[str] = ...) -> None: ...
