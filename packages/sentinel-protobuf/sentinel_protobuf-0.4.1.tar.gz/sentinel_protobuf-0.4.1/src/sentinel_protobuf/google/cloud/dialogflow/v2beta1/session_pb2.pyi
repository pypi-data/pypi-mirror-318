from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.dialogflow.v2beta1 import agent_pb2 as _agent_pb2
from google.cloud.dialogflow.v2beta1 import audio_config_pb2 as _audio_config_pb2
from google.cloud.dialogflow.v2beta1 import context_pb2 as _context_pb2
from google.cloud.dialogflow.v2beta1 import intent_pb2 as _intent_pb2
from google.cloud.dialogflow.v2beta1 import session_entity_type_pb2 as _session_entity_type_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.rpc import status_pb2 as _status_pb2
from google.type import latlng_pb2 as _latlng_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class DetectIntentRequest(_message.Message):
    __slots__ = ('session', 'query_params', 'query_input', 'output_audio_config', 'output_audio_config_mask', 'input_audio')
    SESSION_FIELD_NUMBER: _ClassVar[int]
    QUERY_PARAMS_FIELD_NUMBER: _ClassVar[int]
    QUERY_INPUT_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_AUDIO_CONFIG_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_AUDIO_CONFIG_MASK_FIELD_NUMBER: _ClassVar[int]
    INPUT_AUDIO_FIELD_NUMBER: _ClassVar[int]
    session: str
    query_params: QueryParameters
    query_input: QueryInput
    output_audio_config: _audio_config_pb2.OutputAudioConfig
    output_audio_config_mask: _field_mask_pb2.FieldMask
    input_audio: bytes

    def __init__(self, session: _Optional[str]=..., query_params: _Optional[_Union[QueryParameters, _Mapping]]=..., query_input: _Optional[_Union[QueryInput, _Mapping]]=..., output_audio_config: _Optional[_Union[_audio_config_pb2.OutputAudioConfig, _Mapping]]=..., output_audio_config_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., input_audio: _Optional[bytes]=...) -> None:
        ...

class DetectIntentResponse(_message.Message):
    __slots__ = ('response_id', 'query_result', 'alternative_query_results', 'webhook_status', 'output_audio', 'output_audio_config')
    RESPONSE_ID_FIELD_NUMBER: _ClassVar[int]
    QUERY_RESULT_FIELD_NUMBER: _ClassVar[int]
    ALTERNATIVE_QUERY_RESULTS_FIELD_NUMBER: _ClassVar[int]
    WEBHOOK_STATUS_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_AUDIO_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_AUDIO_CONFIG_FIELD_NUMBER: _ClassVar[int]
    response_id: str
    query_result: QueryResult
    alternative_query_results: _containers.RepeatedCompositeFieldContainer[QueryResult]
    webhook_status: _status_pb2.Status
    output_audio: bytes
    output_audio_config: _audio_config_pb2.OutputAudioConfig

    def __init__(self, response_id: _Optional[str]=..., query_result: _Optional[_Union[QueryResult, _Mapping]]=..., alternative_query_results: _Optional[_Iterable[_Union[QueryResult, _Mapping]]]=..., webhook_status: _Optional[_Union[_status_pb2.Status, _Mapping]]=..., output_audio: _Optional[bytes]=..., output_audio_config: _Optional[_Union[_audio_config_pb2.OutputAudioConfig, _Mapping]]=...) -> None:
        ...

class QueryParameters(_message.Message):
    __slots__ = ('time_zone', 'geo_location', 'contexts', 'reset_contexts', 'session_entity_types', 'payload', 'knowledge_base_names', 'sentiment_analysis_request_config', 'sub_agents', 'webhook_headers', 'platform')

    class WebhookHeadersEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    GEO_LOCATION_FIELD_NUMBER: _ClassVar[int]
    CONTEXTS_FIELD_NUMBER: _ClassVar[int]
    RESET_CONTEXTS_FIELD_NUMBER: _ClassVar[int]
    SESSION_ENTITY_TYPES_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    KNOWLEDGE_BASE_NAMES_FIELD_NUMBER: _ClassVar[int]
    SENTIMENT_ANALYSIS_REQUEST_CONFIG_FIELD_NUMBER: _ClassVar[int]
    SUB_AGENTS_FIELD_NUMBER: _ClassVar[int]
    WEBHOOK_HEADERS_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_FIELD_NUMBER: _ClassVar[int]
    time_zone: str
    geo_location: _latlng_pb2.LatLng
    contexts: _containers.RepeatedCompositeFieldContainer[_context_pb2.Context]
    reset_contexts: bool
    session_entity_types: _containers.RepeatedCompositeFieldContainer[_session_entity_type_pb2.SessionEntityType]
    payload: _struct_pb2.Struct
    knowledge_base_names: _containers.RepeatedScalarFieldContainer[str]
    sentiment_analysis_request_config: SentimentAnalysisRequestConfig
    sub_agents: _containers.RepeatedCompositeFieldContainer[_agent_pb2.SubAgent]
    webhook_headers: _containers.ScalarMap[str, str]
    platform: str

    def __init__(self, time_zone: _Optional[str]=..., geo_location: _Optional[_Union[_latlng_pb2.LatLng, _Mapping]]=..., contexts: _Optional[_Iterable[_Union[_context_pb2.Context, _Mapping]]]=..., reset_contexts: bool=..., session_entity_types: _Optional[_Iterable[_Union[_session_entity_type_pb2.SessionEntityType, _Mapping]]]=..., payload: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=..., knowledge_base_names: _Optional[_Iterable[str]]=..., sentiment_analysis_request_config: _Optional[_Union[SentimentAnalysisRequestConfig, _Mapping]]=..., sub_agents: _Optional[_Iterable[_Union[_agent_pb2.SubAgent, _Mapping]]]=..., webhook_headers: _Optional[_Mapping[str, str]]=..., platform: _Optional[str]=...) -> None:
        ...

class QueryInput(_message.Message):
    __slots__ = ('audio_config', 'text', 'event', 'dtmf')
    AUDIO_CONFIG_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    EVENT_FIELD_NUMBER: _ClassVar[int]
    DTMF_FIELD_NUMBER: _ClassVar[int]
    audio_config: _audio_config_pb2.InputAudioConfig
    text: TextInput
    event: EventInput
    dtmf: _audio_config_pb2.TelephonyDtmfEvents

    def __init__(self, audio_config: _Optional[_Union[_audio_config_pb2.InputAudioConfig, _Mapping]]=..., text: _Optional[_Union[TextInput, _Mapping]]=..., event: _Optional[_Union[EventInput, _Mapping]]=..., dtmf: _Optional[_Union[_audio_config_pb2.TelephonyDtmfEvents, _Mapping]]=...) -> None:
        ...

class QueryResult(_message.Message):
    __slots__ = ('query_text', 'language_code', 'speech_recognition_confidence', 'action', 'parameters', 'all_required_params_present', 'cancels_slot_filling', 'fulfillment_text', 'fulfillment_messages', 'webhook_source', 'webhook_payload', 'output_contexts', 'intent', 'intent_detection_confidence', 'diagnostic_info', 'sentiment_analysis_result', 'knowledge_answers')
    QUERY_TEXT_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    SPEECH_RECOGNITION_CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    ALL_REQUIRED_PARAMS_PRESENT_FIELD_NUMBER: _ClassVar[int]
    CANCELS_SLOT_FILLING_FIELD_NUMBER: _ClassVar[int]
    FULFILLMENT_TEXT_FIELD_NUMBER: _ClassVar[int]
    FULFILLMENT_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    WEBHOOK_SOURCE_FIELD_NUMBER: _ClassVar[int]
    WEBHOOK_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_CONTEXTS_FIELD_NUMBER: _ClassVar[int]
    INTENT_FIELD_NUMBER: _ClassVar[int]
    INTENT_DETECTION_CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    DIAGNOSTIC_INFO_FIELD_NUMBER: _ClassVar[int]
    SENTIMENT_ANALYSIS_RESULT_FIELD_NUMBER: _ClassVar[int]
    KNOWLEDGE_ANSWERS_FIELD_NUMBER: _ClassVar[int]
    query_text: str
    language_code: str
    speech_recognition_confidence: float
    action: str
    parameters: _struct_pb2.Struct
    all_required_params_present: bool
    cancels_slot_filling: bool
    fulfillment_text: str
    fulfillment_messages: _containers.RepeatedCompositeFieldContainer[_intent_pb2.Intent.Message]
    webhook_source: str
    webhook_payload: _struct_pb2.Struct
    output_contexts: _containers.RepeatedCompositeFieldContainer[_context_pb2.Context]
    intent: _intent_pb2.Intent
    intent_detection_confidence: float
    diagnostic_info: _struct_pb2.Struct
    sentiment_analysis_result: SentimentAnalysisResult
    knowledge_answers: KnowledgeAnswers

    def __init__(self, query_text: _Optional[str]=..., language_code: _Optional[str]=..., speech_recognition_confidence: _Optional[float]=..., action: _Optional[str]=..., parameters: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=..., all_required_params_present: bool=..., cancels_slot_filling: bool=..., fulfillment_text: _Optional[str]=..., fulfillment_messages: _Optional[_Iterable[_Union[_intent_pb2.Intent.Message, _Mapping]]]=..., webhook_source: _Optional[str]=..., webhook_payload: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=..., output_contexts: _Optional[_Iterable[_Union[_context_pb2.Context, _Mapping]]]=..., intent: _Optional[_Union[_intent_pb2.Intent, _Mapping]]=..., intent_detection_confidence: _Optional[float]=..., diagnostic_info: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=..., sentiment_analysis_result: _Optional[_Union[SentimentAnalysisResult, _Mapping]]=..., knowledge_answers: _Optional[_Union[KnowledgeAnswers, _Mapping]]=...) -> None:
        ...

class KnowledgeAnswers(_message.Message):
    __slots__ = ('answers',)

    class Answer(_message.Message):
        __slots__ = ('source', 'faq_question', 'answer', 'match_confidence_level', 'match_confidence')

        class MatchConfidenceLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            MATCH_CONFIDENCE_LEVEL_UNSPECIFIED: _ClassVar[KnowledgeAnswers.Answer.MatchConfidenceLevel]
            LOW: _ClassVar[KnowledgeAnswers.Answer.MatchConfidenceLevel]
            MEDIUM: _ClassVar[KnowledgeAnswers.Answer.MatchConfidenceLevel]
            HIGH: _ClassVar[KnowledgeAnswers.Answer.MatchConfidenceLevel]
        MATCH_CONFIDENCE_LEVEL_UNSPECIFIED: KnowledgeAnswers.Answer.MatchConfidenceLevel
        LOW: KnowledgeAnswers.Answer.MatchConfidenceLevel
        MEDIUM: KnowledgeAnswers.Answer.MatchConfidenceLevel
        HIGH: KnowledgeAnswers.Answer.MatchConfidenceLevel
        SOURCE_FIELD_NUMBER: _ClassVar[int]
        FAQ_QUESTION_FIELD_NUMBER: _ClassVar[int]
        ANSWER_FIELD_NUMBER: _ClassVar[int]
        MATCH_CONFIDENCE_LEVEL_FIELD_NUMBER: _ClassVar[int]
        MATCH_CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
        source: str
        faq_question: str
        answer: str
        match_confidence_level: KnowledgeAnswers.Answer.MatchConfidenceLevel
        match_confidence: float

        def __init__(self, source: _Optional[str]=..., faq_question: _Optional[str]=..., answer: _Optional[str]=..., match_confidence_level: _Optional[_Union[KnowledgeAnswers.Answer.MatchConfidenceLevel, str]]=..., match_confidence: _Optional[float]=...) -> None:
            ...
    ANSWERS_FIELD_NUMBER: _ClassVar[int]
    answers: _containers.RepeatedCompositeFieldContainer[KnowledgeAnswers.Answer]

    def __init__(self, answers: _Optional[_Iterable[_Union[KnowledgeAnswers.Answer, _Mapping]]]=...) -> None:
        ...

class StreamingDetectIntentRequest(_message.Message):
    __slots__ = ('session', 'query_params', 'query_input', 'single_utterance', 'output_audio_config', 'output_audio_config_mask', 'input_audio', 'enable_debugging_info')
    SESSION_FIELD_NUMBER: _ClassVar[int]
    QUERY_PARAMS_FIELD_NUMBER: _ClassVar[int]
    QUERY_INPUT_FIELD_NUMBER: _ClassVar[int]
    SINGLE_UTTERANCE_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_AUDIO_CONFIG_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_AUDIO_CONFIG_MASK_FIELD_NUMBER: _ClassVar[int]
    INPUT_AUDIO_FIELD_NUMBER: _ClassVar[int]
    ENABLE_DEBUGGING_INFO_FIELD_NUMBER: _ClassVar[int]
    session: str
    query_params: QueryParameters
    query_input: QueryInput
    single_utterance: bool
    output_audio_config: _audio_config_pb2.OutputAudioConfig
    output_audio_config_mask: _field_mask_pb2.FieldMask
    input_audio: bytes
    enable_debugging_info: bool

    def __init__(self, session: _Optional[str]=..., query_params: _Optional[_Union[QueryParameters, _Mapping]]=..., query_input: _Optional[_Union[QueryInput, _Mapping]]=..., single_utterance: bool=..., output_audio_config: _Optional[_Union[_audio_config_pb2.OutputAudioConfig, _Mapping]]=..., output_audio_config_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., input_audio: _Optional[bytes]=..., enable_debugging_info: bool=...) -> None:
        ...

class CloudConversationDebuggingInfo(_message.Message):
    __slots__ = ('audio_data_chunks', 'result_end_time_offset', 'first_audio_duration', 'single_utterance', 'speech_partial_results_end_times', 'speech_final_results_end_times', 'partial_responses', 'speaker_id_passive_latency_ms_offset', 'bargein_event_triggered', 'speech_single_utterance', 'dtmf_partial_results_times', 'dtmf_final_results_times', 'single_utterance_end_time_offset', 'no_speech_timeout', 'endpointing_timeout', 'is_input_text', 'client_half_close_time_offset', 'client_half_close_streaming_time_offset')
    AUDIO_DATA_CHUNKS_FIELD_NUMBER: _ClassVar[int]
    RESULT_END_TIME_OFFSET_FIELD_NUMBER: _ClassVar[int]
    FIRST_AUDIO_DURATION_FIELD_NUMBER: _ClassVar[int]
    SINGLE_UTTERANCE_FIELD_NUMBER: _ClassVar[int]
    SPEECH_PARTIAL_RESULTS_END_TIMES_FIELD_NUMBER: _ClassVar[int]
    SPEECH_FINAL_RESULTS_END_TIMES_FIELD_NUMBER: _ClassVar[int]
    PARTIAL_RESPONSES_FIELD_NUMBER: _ClassVar[int]
    SPEAKER_ID_PASSIVE_LATENCY_MS_OFFSET_FIELD_NUMBER: _ClassVar[int]
    BARGEIN_EVENT_TRIGGERED_FIELD_NUMBER: _ClassVar[int]
    SPEECH_SINGLE_UTTERANCE_FIELD_NUMBER: _ClassVar[int]
    DTMF_PARTIAL_RESULTS_TIMES_FIELD_NUMBER: _ClassVar[int]
    DTMF_FINAL_RESULTS_TIMES_FIELD_NUMBER: _ClassVar[int]
    SINGLE_UTTERANCE_END_TIME_OFFSET_FIELD_NUMBER: _ClassVar[int]
    NO_SPEECH_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    ENDPOINTING_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    IS_INPUT_TEXT_FIELD_NUMBER: _ClassVar[int]
    CLIENT_HALF_CLOSE_TIME_OFFSET_FIELD_NUMBER: _ClassVar[int]
    CLIENT_HALF_CLOSE_STREAMING_TIME_OFFSET_FIELD_NUMBER: _ClassVar[int]
    audio_data_chunks: int
    result_end_time_offset: _duration_pb2.Duration
    first_audio_duration: _duration_pb2.Duration
    single_utterance: bool
    speech_partial_results_end_times: _containers.RepeatedCompositeFieldContainer[_duration_pb2.Duration]
    speech_final_results_end_times: _containers.RepeatedCompositeFieldContainer[_duration_pb2.Duration]
    partial_responses: int
    speaker_id_passive_latency_ms_offset: int
    bargein_event_triggered: bool
    speech_single_utterance: bool
    dtmf_partial_results_times: _containers.RepeatedCompositeFieldContainer[_duration_pb2.Duration]
    dtmf_final_results_times: _containers.RepeatedCompositeFieldContainer[_duration_pb2.Duration]
    single_utterance_end_time_offset: _duration_pb2.Duration
    no_speech_timeout: _duration_pb2.Duration
    endpointing_timeout: _duration_pb2.Duration
    is_input_text: bool
    client_half_close_time_offset: _duration_pb2.Duration
    client_half_close_streaming_time_offset: _duration_pb2.Duration

    def __init__(self, audio_data_chunks: _Optional[int]=..., result_end_time_offset: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., first_audio_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., single_utterance: bool=..., speech_partial_results_end_times: _Optional[_Iterable[_Union[_duration_pb2.Duration, _Mapping]]]=..., speech_final_results_end_times: _Optional[_Iterable[_Union[_duration_pb2.Duration, _Mapping]]]=..., partial_responses: _Optional[int]=..., speaker_id_passive_latency_ms_offset: _Optional[int]=..., bargein_event_triggered: bool=..., speech_single_utterance: bool=..., dtmf_partial_results_times: _Optional[_Iterable[_Union[_duration_pb2.Duration, _Mapping]]]=..., dtmf_final_results_times: _Optional[_Iterable[_Union[_duration_pb2.Duration, _Mapping]]]=..., single_utterance_end_time_offset: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., no_speech_timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., endpointing_timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., is_input_text: bool=..., client_half_close_time_offset: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., client_half_close_streaming_time_offset: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=...) -> None:
        ...

class StreamingDetectIntentResponse(_message.Message):
    __slots__ = ('response_id', 'recognition_result', 'query_result', 'alternative_query_results', 'webhook_status', 'output_audio', 'output_audio_config', 'debugging_info')
    RESPONSE_ID_FIELD_NUMBER: _ClassVar[int]
    RECOGNITION_RESULT_FIELD_NUMBER: _ClassVar[int]
    QUERY_RESULT_FIELD_NUMBER: _ClassVar[int]
    ALTERNATIVE_QUERY_RESULTS_FIELD_NUMBER: _ClassVar[int]
    WEBHOOK_STATUS_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_AUDIO_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_AUDIO_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DEBUGGING_INFO_FIELD_NUMBER: _ClassVar[int]
    response_id: str
    recognition_result: StreamingRecognitionResult
    query_result: QueryResult
    alternative_query_results: _containers.RepeatedCompositeFieldContainer[QueryResult]
    webhook_status: _status_pb2.Status
    output_audio: bytes
    output_audio_config: _audio_config_pb2.OutputAudioConfig
    debugging_info: CloudConversationDebuggingInfo

    def __init__(self, response_id: _Optional[str]=..., recognition_result: _Optional[_Union[StreamingRecognitionResult, _Mapping]]=..., query_result: _Optional[_Union[QueryResult, _Mapping]]=..., alternative_query_results: _Optional[_Iterable[_Union[QueryResult, _Mapping]]]=..., webhook_status: _Optional[_Union[_status_pb2.Status, _Mapping]]=..., output_audio: _Optional[bytes]=..., output_audio_config: _Optional[_Union[_audio_config_pb2.OutputAudioConfig, _Mapping]]=..., debugging_info: _Optional[_Union[CloudConversationDebuggingInfo, _Mapping]]=...) -> None:
        ...

class StreamingRecognitionResult(_message.Message):
    __slots__ = ('message_type', 'transcript', 'is_final', 'confidence', 'stability', 'speech_word_info', 'speech_end_offset', 'language_code', 'dtmf_digits')

    class MessageType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MESSAGE_TYPE_UNSPECIFIED: _ClassVar[StreamingRecognitionResult.MessageType]
        TRANSCRIPT: _ClassVar[StreamingRecognitionResult.MessageType]
        DTMF_DIGITS: _ClassVar[StreamingRecognitionResult.MessageType]
        END_OF_SINGLE_UTTERANCE: _ClassVar[StreamingRecognitionResult.MessageType]
        PARTIAL_DTMF_DIGITS: _ClassVar[StreamingRecognitionResult.MessageType]
    MESSAGE_TYPE_UNSPECIFIED: StreamingRecognitionResult.MessageType
    TRANSCRIPT: StreamingRecognitionResult.MessageType
    DTMF_DIGITS: StreamingRecognitionResult.MessageType
    END_OF_SINGLE_UTTERANCE: StreamingRecognitionResult.MessageType
    PARTIAL_DTMF_DIGITS: StreamingRecognitionResult.MessageType
    MESSAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    TRANSCRIPT_FIELD_NUMBER: _ClassVar[int]
    IS_FINAL_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    STABILITY_FIELD_NUMBER: _ClassVar[int]
    SPEECH_WORD_INFO_FIELD_NUMBER: _ClassVar[int]
    SPEECH_END_OFFSET_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    DTMF_DIGITS_FIELD_NUMBER: _ClassVar[int]
    message_type: StreamingRecognitionResult.MessageType
    transcript: str
    is_final: bool
    confidence: float
    stability: float
    speech_word_info: _containers.RepeatedCompositeFieldContainer[_audio_config_pb2.SpeechWordInfo]
    speech_end_offset: _duration_pb2.Duration
    language_code: str
    dtmf_digits: _audio_config_pb2.TelephonyDtmfEvents

    def __init__(self, message_type: _Optional[_Union[StreamingRecognitionResult.MessageType, str]]=..., transcript: _Optional[str]=..., is_final: bool=..., confidence: _Optional[float]=..., stability: _Optional[float]=..., speech_word_info: _Optional[_Iterable[_Union[_audio_config_pb2.SpeechWordInfo, _Mapping]]]=..., speech_end_offset: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., language_code: _Optional[str]=..., dtmf_digits: _Optional[_Union[_audio_config_pb2.TelephonyDtmfEvents, _Mapping]]=...) -> None:
        ...

class TextInput(_message.Message):
    __slots__ = ('text', 'language_code')
    TEXT_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    text: str
    language_code: str

    def __init__(self, text: _Optional[str]=..., language_code: _Optional[str]=...) -> None:
        ...

class EventInput(_message.Message):
    __slots__ = ('name', 'parameters', 'language_code')
    NAME_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    name: str
    parameters: _struct_pb2.Struct
    language_code: str

    def __init__(self, name: _Optional[str]=..., parameters: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=..., language_code: _Optional[str]=...) -> None:
        ...

class SentimentAnalysisRequestConfig(_message.Message):
    __slots__ = ('analyze_query_text_sentiment',)
    ANALYZE_QUERY_TEXT_SENTIMENT_FIELD_NUMBER: _ClassVar[int]
    analyze_query_text_sentiment: bool

    def __init__(self, analyze_query_text_sentiment: bool=...) -> None:
        ...

class SentimentAnalysisResult(_message.Message):
    __slots__ = ('query_text_sentiment',)
    QUERY_TEXT_SENTIMENT_FIELD_NUMBER: _ClassVar[int]
    query_text_sentiment: Sentiment

    def __init__(self, query_text_sentiment: _Optional[_Union[Sentiment, _Mapping]]=...) -> None:
        ...

class Sentiment(_message.Message):
    __slots__ = ('score', 'magnitude')
    SCORE_FIELD_NUMBER: _ClassVar[int]
    MAGNITUDE_FIELD_NUMBER: _ClassVar[int]
    score: float
    magnitude: float

    def __init__(self, score: _Optional[float]=..., magnitude: _Optional[float]=...) -> None:
        ...