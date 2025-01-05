from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.dialogflow.cx.v3beta1 import environment_pb2 as _environment_pb2
from google.cloud.dialogflow.cx.v3beta1 import flow_pb2 as _flow_pb2
from google.cloud.dialogflow.cx.v3beta1 import intent_pb2 as _intent_pb2
from google.cloud.dialogflow.cx.v3beta1 import page_pb2 as _page_pb2
from google.cloud.dialogflow.cx.v3beta1 import session_pb2 as _session_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class GetConversationRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class DeleteConversationRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListConversationsRequest(_message.Message):
    __slots__ = ('parent', 'filter', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., filter: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListConversationsResponse(_message.Message):
    __slots__ = ('conversations', 'next_page_token')
    CONVERSATIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    conversations: _containers.RepeatedCompositeFieldContainer[Conversation]
    next_page_token: str

    def __init__(self, conversations: _Optional[_Iterable[_Union[Conversation, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class Conversation(_message.Message):
    __slots__ = ('name', 'type', 'language_code', 'start_time', 'duration', 'metrics', 'intents', 'flows', 'pages', 'interactions', 'environment', 'flow_versions')

    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[Conversation.Type]
        AUDIO: _ClassVar[Conversation.Type]
        TEXT: _ClassVar[Conversation.Type]
        UNDETERMINED: _ClassVar[Conversation.Type]
    TYPE_UNSPECIFIED: Conversation.Type
    AUDIO: Conversation.Type
    TEXT: Conversation.Type
    UNDETERMINED: Conversation.Type

    class Metrics(_message.Message):
        __slots__ = ('interaction_count', 'input_audio_duration', 'output_audio_duration', 'max_webhook_latency', 'has_end_interaction', 'has_live_agent_handoff', 'average_match_confidence', 'query_input_count', 'match_type_count')

        class QueryInputCount(_message.Message):
            __slots__ = ('text_count', 'intent_count', 'audio_count', 'event_count', 'dtmf_count')
            TEXT_COUNT_FIELD_NUMBER: _ClassVar[int]
            INTENT_COUNT_FIELD_NUMBER: _ClassVar[int]
            AUDIO_COUNT_FIELD_NUMBER: _ClassVar[int]
            EVENT_COUNT_FIELD_NUMBER: _ClassVar[int]
            DTMF_COUNT_FIELD_NUMBER: _ClassVar[int]
            text_count: int
            intent_count: int
            audio_count: int
            event_count: int
            dtmf_count: int

            def __init__(self, text_count: _Optional[int]=..., intent_count: _Optional[int]=..., audio_count: _Optional[int]=..., event_count: _Optional[int]=..., dtmf_count: _Optional[int]=...) -> None:
                ...

        class MatchTypeCount(_message.Message):
            __slots__ = ('unspecified_count', 'intent_count', 'direct_intent_count', 'parameter_filling_count', 'no_match_count', 'no_input_count', 'event_count')
            UNSPECIFIED_COUNT_FIELD_NUMBER: _ClassVar[int]
            INTENT_COUNT_FIELD_NUMBER: _ClassVar[int]
            DIRECT_INTENT_COUNT_FIELD_NUMBER: _ClassVar[int]
            PARAMETER_FILLING_COUNT_FIELD_NUMBER: _ClassVar[int]
            NO_MATCH_COUNT_FIELD_NUMBER: _ClassVar[int]
            NO_INPUT_COUNT_FIELD_NUMBER: _ClassVar[int]
            EVENT_COUNT_FIELD_NUMBER: _ClassVar[int]
            unspecified_count: int
            intent_count: int
            direct_intent_count: int
            parameter_filling_count: int
            no_match_count: int
            no_input_count: int
            event_count: int

            def __init__(self, unspecified_count: _Optional[int]=..., intent_count: _Optional[int]=..., direct_intent_count: _Optional[int]=..., parameter_filling_count: _Optional[int]=..., no_match_count: _Optional[int]=..., no_input_count: _Optional[int]=..., event_count: _Optional[int]=...) -> None:
                ...
        INTERACTION_COUNT_FIELD_NUMBER: _ClassVar[int]
        INPUT_AUDIO_DURATION_FIELD_NUMBER: _ClassVar[int]
        OUTPUT_AUDIO_DURATION_FIELD_NUMBER: _ClassVar[int]
        MAX_WEBHOOK_LATENCY_FIELD_NUMBER: _ClassVar[int]
        HAS_END_INTERACTION_FIELD_NUMBER: _ClassVar[int]
        HAS_LIVE_AGENT_HANDOFF_FIELD_NUMBER: _ClassVar[int]
        AVERAGE_MATCH_CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
        QUERY_INPUT_COUNT_FIELD_NUMBER: _ClassVar[int]
        MATCH_TYPE_COUNT_FIELD_NUMBER: _ClassVar[int]
        interaction_count: int
        input_audio_duration: _duration_pb2.Duration
        output_audio_duration: _duration_pb2.Duration
        max_webhook_latency: _duration_pb2.Duration
        has_end_interaction: bool
        has_live_agent_handoff: bool
        average_match_confidence: float
        query_input_count: Conversation.Metrics.QueryInputCount
        match_type_count: Conversation.Metrics.MatchTypeCount

        def __init__(self, interaction_count: _Optional[int]=..., input_audio_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., output_audio_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., max_webhook_latency: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., has_end_interaction: bool=..., has_live_agent_handoff: bool=..., average_match_confidence: _Optional[float]=..., query_input_count: _Optional[_Union[Conversation.Metrics.QueryInputCount, _Mapping]]=..., match_type_count: _Optional[_Union[Conversation.Metrics.MatchTypeCount, _Mapping]]=...) -> None:
            ...

    class Interaction(_message.Message):
        __slots__ = ('request', 'response', 'partial_responses', 'request_utterances', 'response_utterances', 'create_time', 'missing_transition')

        class MissingTransition(_message.Message):
            __slots__ = ('intent_display_name', 'score')
            INTENT_DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
            SCORE_FIELD_NUMBER: _ClassVar[int]
            intent_display_name: str
            score: float

            def __init__(self, intent_display_name: _Optional[str]=..., score: _Optional[float]=...) -> None:
                ...
        REQUEST_FIELD_NUMBER: _ClassVar[int]
        RESPONSE_FIELD_NUMBER: _ClassVar[int]
        PARTIAL_RESPONSES_FIELD_NUMBER: _ClassVar[int]
        REQUEST_UTTERANCES_FIELD_NUMBER: _ClassVar[int]
        RESPONSE_UTTERANCES_FIELD_NUMBER: _ClassVar[int]
        CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
        MISSING_TRANSITION_FIELD_NUMBER: _ClassVar[int]
        request: _session_pb2.DetectIntentRequest
        response: _session_pb2.DetectIntentResponse
        partial_responses: _containers.RepeatedCompositeFieldContainer[_session_pb2.DetectIntentResponse]
        request_utterances: str
        response_utterances: str
        create_time: _timestamp_pb2.Timestamp
        missing_transition: Conversation.Interaction.MissingTransition

        def __init__(self, request: _Optional[_Union[_session_pb2.DetectIntentRequest, _Mapping]]=..., response: _Optional[_Union[_session_pb2.DetectIntentResponse, _Mapping]]=..., partial_responses: _Optional[_Iterable[_Union[_session_pb2.DetectIntentResponse, _Mapping]]]=..., request_utterances: _Optional[str]=..., response_utterances: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., missing_transition: _Optional[_Union[Conversation.Interaction.MissingTransition, _Mapping]]=...) -> None:
            ...

    class FlowVersionsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int

        def __init__(self, key: _Optional[str]=..., value: _Optional[int]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    METRICS_FIELD_NUMBER: _ClassVar[int]
    INTENTS_FIELD_NUMBER: _ClassVar[int]
    FLOWS_FIELD_NUMBER: _ClassVar[int]
    PAGES_FIELD_NUMBER: _ClassVar[int]
    INTERACTIONS_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    FLOW_VERSIONS_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: Conversation.Type
    language_code: str
    start_time: _timestamp_pb2.Timestamp
    duration: _duration_pb2.Duration
    metrics: Conversation.Metrics
    intents: _containers.RepeatedCompositeFieldContainer[_intent_pb2.Intent]
    flows: _containers.RepeatedCompositeFieldContainer[_flow_pb2.Flow]
    pages: _containers.RepeatedCompositeFieldContainer[_page_pb2.Page]
    interactions: _containers.RepeatedCompositeFieldContainer[Conversation.Interaction]
    environment: _environment_pb2.Environment
    flow_versions: _containers.ScalarMap[str, int]

    def __init__(self, name: _Optional[str]=..., type: _Optional[_Union[Conversation.Type, str]]=..., language_code: _Optional[str]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., metrics: _Optional[_Union[Conversation.Metrics, _Mapping]]=..., intents: _Optional[_Iterable[_Union[_intent_pb2.Intent, _Mapping]]]=..., flows: _Optional[_Iterable[_Union[_flow_pb2.Flow, _Mapping]]]=..., pages: _Optional[_Iterable[_Union[_page_pb2.Page, _Mapping]]]=..., interactions: _Optional[_Iterable[_Union[Conversation.Interaction, _Mapping]]]=..., environment: _Optional[_Union[_environment_pb2.Environment, _Mapping]]=..., flow_versions: _Optional[_Mapping[str, int]]=...) -> None:
        ...