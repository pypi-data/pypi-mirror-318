from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.dialogflow.cx.v3beta1 import advanced_settings_pb2 as _advanced_settings_pb2
from google.cloud.dialogflow.cx.v3beta1 import audio_config_pb2 as _audio_config_pb2
from google.cloud.dialogflow.cx.v3beta1 import data_store_connection_pb2 as _data_store_connection_pb2
from google.cloud.dialogflow.cx.v3beta1 import example_pb2 as _example_pb2
from google.cloud.dialogflow.cx.v3beta1 import flow_pb2 as _flow_pb2
from google.cloud.dialogflow.cx.v3beta1 import generative_settings_pb2 as _generative_settings_pb2
from google.cloud.dialogflow.cx.v3beta1 import intent_pb2 as _intent_pb2
from google.cloud.dialogflow.cx.v3beta1 import page_pb2 as _page_pb2
from google.cloud.dialogflow.cx.v3beta1 import response_message_pb2 as _response_message_pb2
from google.cloud.dialogflow.cx.v3beta1 import session_entity_type_pb2 as _session_entity_type_pb2
from google.cloud.dialogflow.cx.v3beta1 import tool_call_pb2 as _tool_call_pb2
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

class AnswerFeedback(_message.Message):
    __slots__ = ('rating', 'rating_reason', 'custom_rating')

    class Rating(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RATING_UNSPECIFIED: _ClassVar[AnswerFeedback.Rating]
        THUMBS_UP: _ClassVar[AnswerFeedback.Rating]
        THUMBS_DOWN: _ClassVar[AnswerFeedback.Rating]
    RATING_UNSPECIFIED: AnswerFeedback.Rating
    THUMBS_UP: AnswerFeedback.Rating
    THUMBS_DOWN: AnswerFeedback.Rating

    class RatingReason(_message.Message):
        __slots__ = ('reason_labels', 'feedback')
        REASON_LABELS_FIELD_NUMBER: _ClassVar[int]
        FEEDBACK_FIELD_NUMBER: _ClassVar[int]
        reason_labels: _containers.RepeatedScalarFieldContainer[str]
        feedback: str

        def __init__(self, reason_labels: _Optional[_Iterable[str]]=..., feedback: _Optional[str]=...) -> None:
            ...
    RATING_FIELD_NUMBER: _ClassVar[int]
    RATING_REASON_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_RATING_FIELD_NUMBER: _ClassVar[int]
    rating: AnswerFeedback.Rating
    rating_reason: AnswerFeedback.RatingReason
    custom_rating: str

    def __init__(self, rating: _Optional[_Union[AnswerFeedback.Rating, str]]=..., rating_reason: _Optional[_Union[AnswerFeedback.RatingReason, _Mapping]]=..., custom_rating: _Optional[str]=...) -> None:
        ...

class SubmitAnswerFeedbackRequest(_message.Message):
    __slots__ = ('session', 'response_id', 'answer_feedback', 'update_mask')
    SESSION_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_ID_FIELD_NUMBER: _ClassVar[int]
    ANSWER_FEEDBACK_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    session: str
    response_id: str
    answer_feedback: AnswerFeedback
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, session: _Optional[str]=..., response_id: _Optional[str]=..., answer_feedback: _Optional[_Union[AnswerFeedback, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DetectIntentRequest(_message.Message):
    __slots__ = ('session', 'query_params', 'query_input', 'output_audio_config')
    SESSION_FIELD_NUMBER: _ClassVar[int]
    QUERY_PARAMS_FIELD_NUMBER: _ClassVar[int]
    QUERY_INPUT_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_AUDIO_CONFIG_FIELD_NUMBER: _ClassVar[int]
    session: str
    query_params: QueryParameters
    query_input: QueryInput
    output_audio_config: _audio_config_pb2.OutputAudioConfig

    def __init__(self, session: _Optional[str]=..., query_params: _Optional[_Union[QueryParameters, _Mapping]]=..., query_input: _Optional[_Union[QueryInput, _Mapping]]=..., output_audio_config: _Optional[_Union[_audio_config_pb2.OutputAudioConfig, _Mapping]]=...) -> None:
        ...

class DetectIntentResponse(_message.Message):
    __slots__ = ('response_id', 'query_result', 'output_audio', 'output_audio_config', 'response_type', 'allow_cancellation')

    class ResponseType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RESPONSE_TYPE_UNSPECIFIED: _ClassVar[DetectIntentResponse.ResponseType]
        PARTIAL: _ClassVar[DetectIntentResponse.ResponseType]
        FINAL: _ClassVar[DetectIntentResponse.ResponseType]
    RESPONSE_TYPE_UNSPECIFIED: DetectIntentResponse.ResponseType
    PARTIAL: DetectIntentResponse.ResponseType
    FINAL: DetectIntentResponse.ResponseType
    RESPONSE_ID_FIELD_NUMBER: _ClassVar[int]
    QUERY_RESULT_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_AUDIO_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_AUDIO_CONFIG_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_TYPE_FIELD_NUMBER: _ClassVar[int]
    ALLOW_CANCELLATION_FIELD_NUMBER: _ClassVar[int]
    response_id: str
    query_result: QueryResult
    output_audio: bytes
    output_audio_config: _audio_config_pb2.OutputAudioConfig
    response_type: DetectIntentResponse.ResponseType
    allow_cancellation: bool

    def __init__(self, response_id: _Optional[str]=..., query_result: _Optional[_Union[QueryResult, _Mapping]]=..., output_audio: _Optional[bytes]=..., output_audio_config: _Optional[_Union[_audio_config_pb2.OutputAudioConfig, _Mapping]]=..., response_type: _Optional[_Union[DetectIntentResponse.ResponseType, str]]=..., allow_cancellation: bool=...) -> None:
        ...

class StreamingDetectIntentRequest(_message.Message):
    __slots__ = ('session', 'query_params', 'query_input', 'output_audio_config', 'enable_partial_response', 'enable_debugging_info')
    SESSION_FIELD_NUMBER: _ClassVar[int]
    QUERY_PARAMS_FIELD_NUMBER: _ClassVar[int]
    QUERY_INPUT_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_AUDIO_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ENABLE_PARTIAL_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    ENABLE_DEBUGGING_INFO_FIELD_NUMBER: _ClassVar[int]
    session: str
    query_params: QueryParameters
    query_input: QueryInput
    output_audio_config: _audio_config_pb2.OutputAudioConfig
    enable_partial_response: bool
    enable_debugging_info: bool

    def __init__(self, session: _Optional[str]=..., query_params: _Optional[_Union[QueryParameters, _Mapping]]=..., query_input: _Optional[_Union[QueryInput, _Mapping]]=..., output_audio_config: _Optional[_Union[_audio_config_pb2.OutputAudioConfig, _Mapping]]=..., enable_partial_response: bool=..., enable_debugging_info: bool=...) -> None:
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
    __slots__ = ('recognition_result', 'detect_intent_response', 'debugging_info')
    RECOGNITION_RESULT_FIELD_NUMBER: _ClassVar[int]
    DETECT_INTENT_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    DEBUGGING_INFO_FIELD_NUMBER: _ClassVar[int]
    recognition_result: StreamingRecognitionResult
    detect_intent_response: DetectIntentResponse
    debugging_info: CloudConversationDebuggingInfo

    def __init__(self, recognition_result: _Optional[_Union[StreamingRecognitionResult, _Mapping]]=..., detect_intent_response: _Optional[_Union[DetectIntentResponse, _Mapping]]=..., debugging_info: _Optional[_Union[CloudConversationDebuggingInfo, _Mapping]]=...) -> None:
        ...

class StreamingRecognitionResult(_message.Message):
    __slots__ = ('message_type', 'transcript', 'is_final', 'confidence', 'stability', 'speech_word_info', 'speech_end_offset', 'language_code')

    class MessageType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MESSAGE_TYPE_UNSPECIFIED: _ClassVar[StreamingRecognitionResult.MessageType]
        TRANSCRIPT: _ClassVar[StreamingRecognitionResult.MessageType]
        END_OF_SINGLE_UTTERANCE: _ClassVar[StreamingRecognitionResult.MessageType]
    MESSAGE_TYPE_UNSPECIFIED: StreamingRecognitionResult.MessageType
    TRANSCRIPT: StreamingRecognitionResult.MessageType
    END_OF_SINGLE_UTTERANCE: StreamingRecognitionResult.MessageType
    MESSAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    TRANSCRIPT_FIELD_NUMBER: _ClassVar[int]
    IS_FINAL_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    STABILITY_FIELD_NUMBER: _ClassVar[int]
    SPEECH_WORD_INFO_FIELD_NUMBER: _ClassVar[int]
    SPEECH_END_OFFSET_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    message_type: StreamingRecognitionResult.MessageType
    transcript: str
    is_final: bool
    confidence: float
    stability: float
    speech_word_info: _containers.RepeatedCompositeFieldContainer[_audio_config_pb2.SpeechWordInfo]
    speech_end_offset: _duration_pb2.Duration
    language_code: str

    def __init__(self, message_type: _Optional[_Union[StreamingRecognitionResult.MessageType, str]]=..., transcript: _Optional[str]=..., is_final: bool=..., confidence: _Optional[float]=..., stability: _Optional[float]=..., speech_word_info: _Optional[_Iterable[_Union[_audio_config_pb2.SpeechWordInfo, _Mapping]]]=..., speech_end_offset: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., language_code: _Optional[str]=...) -> None:
        ...

class QueryParameters(_message.Message):
    __slots__ = ('time_zone', 'geo_location', 'session_entity_types', 'payload', 'parameters', 'current_page', 'disable_webhook', 'analyze_query_text_sentiment', 'webhook_headers', 'flow_versions', 'current_playbook', 'llm_model_settings', 'channel', 'session_ttl', 'end_user_metadata', 'search_config', 'populate_data_store_connection_signals')

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
    SESSION_ENTITY_TYPES_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    CURRENT_PAGE_FIELD_NUMBER: _ClassVar[int]
    DISABLE_WEBHOOK_FIELD_NUMBER: _ClassVar[int]
    ANALYZE_QUERY_TEXT_SENTIMENT_FIELD_NUMBER: _ClassVar[int]
    WEBHOOK_HEADERS_FIELD_NUMBER: _ClassVar[int]
    FLOW_VERSIONS_FIELD_NUMBER: _ClassVar[int]
    CURRENT_PLAYBOOK_FIELD_NUMBER: _ClassVar[int]
    LLM_MODEL_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    SESSION_TTL_FIELD_NUMBER: _ClassVar[int]
    END_USER_METADATA_FIELD_NUMBER: _ClassVar[int]
    SEARCH_CONFIG_FIELD_NUMBER: _ClassVar[int]
    POPULATE_DATA_STORE_CONNECTION_SIGNALS_FIELD_NUMBER: _ClassVar[int]
    time_zone: str
    geo_location: _latlng_pb2.LatLng
    session_entity_types: _containers.RepeatedCompositeFieldContainer[_session_entity_type_pb2.SessionEntityType]
    payload: _struct_pb2.Struct
    parameters: _struct_pb2.Struct
    current_page: str
    disable_webhook: bool
    analyze_query_text_sentiment: bool
    webhook_headers: _containers.ScalarMap[str, str]
    flow_versions: _containers.RepeatedScalarFieldContainer[str]
    current_playbook: str
    llm_model_settings: _generative_settings_pb2.LlmModelSettings
    channel: str
    session_ttl: _duration_pb2.Duration
    end_user_metadata: _struct_pb2.Struct
    search_config: SearchConfig
    populate_data_store_connection_signals: bool

    def __init__(self, time_zone: _Optional[str]=..., geo_location: _Optional[_Union[_latlng_pb2.LatLng, _Mapping]]=..., session_entity_types: _Optional[_Iterable[_Union[_session_entity_type_pb2.SessionEntityType, _Mapping]]]=..., payload: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=..., parameters: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=..., current_page: _Optional[str]=..., disable_webhook: bool=..., analyze_query_text_sentiment: bool=..., webhook_headers: _Optional[_Mapping[str, str]]=..., flow_versions: _Optional[_Iterable[str]]=..., current_playbook: _Optional[str]=..., llm_model_settings: _Optional[_Union[_generative_settings_pb2.LlmModelSettings, _Mapping]]=..., channel: _Optional[str]=..., session_ttl: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., end_user_metadata: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=..., search_config: _Optional[_Union[SearchConfig, _Mapping]]=..., populate_data_store_connection_signals: bool=...) -> None:
        ...

class SearchConfig(_message.Message):
    __slots__ = ('boost_specs', 'filter_specs')
    BOOST_SPECS_FIELD_NUMBER: _ClassVar[int]
    FILTER_SPECS_FIELD_NUMBER: _ClassVar[int]
    boost_specs: _containers.RepeatedCompositeFieldContainer[BoostSpecs]
    filter_specs: _containers.RepeatedCompositeFieldContainer[FilterSpecs]

    def __init__(self, boost_specs: _Optional[_Iterable[_Union[BoostSpecs, _Mapping]]]=..., filter_specs: _Optional[_Iterable[_Union[FilterSpecs, _Mapping]]]=...) -> None:
        ...

class BoostSpec(_message.Message):
    __slots__ = ('condition_boost_specs',)

    class ConditionBoostSpec(_message.Message):
        __slots__ = ('condition', 'boost', 'boost_control_spec')

        class BoostControlSpec(_message.Message):
            __slots__ = ('field_name', 'attribute_type', 'interpolation_type', 'control_points')

            class AttributeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                ATTRIBUTE_TYPE_UNSPECIFIED: _ClassVar[BoostSpec.ConditionBoostSpec.BoostControlSpec.AttributeType]
                NUMERICAL: _ClassVar[BoostSpec.ConditionBoostSpec.BoostControlSpec.AttributeType]
                FRESHNESS: _ClassVar[BoostSpec.ConditionBoostSpec.BoostControlSpec.AttributeType]
            ATTRIBUTE_TYPE_UNSPECIFIED: BoostSpec.ConditionBoostSpec.BoostControlSpec.AttributeType
            NUMERICAL: BoostSpec.ConditionBoostSpec.BoostControlSpec.AttributeType
            FRESHNESS: BoostSpec.ConditionBoostSpec.BoostControlSpec.AttributeType

            class InterpolationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                INTERPOLATION_TYPE_UNSPECIFIED: _ClassVar[BoostSpec.ConditionBoostSpec.BoostControlSpec.InterpolationType]
                LINEAR: _ClassVar[BoostSpec.ConditionBoostSpec.BoostControlSpec.InterpolationType]
            INTERPOLATION_TYPE_UNSPECIFIED: BoostSpec.ConditionBoostSpec.BoostControlSpec.InterpolationType
            LINEAR: BoostSpec.ConditionBoostSpec.BoostControlSpec.InterpolationType

            class ControlPoint(_message.Message):
                __slots__ = ('attribute_value', 'boost_amount')
                ATTRIBUTE_VALUE_FIELD_NUMBER: _ClassVar[int]
                BOOST_AMOUNT_FIELD_NUMBER: _ClassVar[int]
                attribute_value: str
                boost_amount: float

                def __init__(self, attribute_value: _Optional[str]=..., boost_amount: _Optional[float]=...) -> None:
                    ...
            FIELD_NAME_FIELD_NUMBER: _ClassVar[int]
            ATTRIBUTE_TYPE_FIELD_NUMBER: _ClassVar[int]
            INTERPOLATION_TYPE_FIELD_NUMBER: _ClassVar[int]
            CONTROL_POINTS_FIELD_NUMBER: _ClassVar[int]
            field_name: str
            attribute_type: BoostSpec.ConditionBoostSpec.BoostControlSpec.AttributeType
            interpolation_type: BoostSpec.ConditionBoostSpec.BoostControlSpec.InterpolationType
            control_points: _containers.RepeatedCompositeFieldContainer[BoostSpec.ConditionBoostSpec.BoostControlSpec.ControlPoint]

            def __init__(self, field_name: _Optional[str]=..., attribute_type: _Optional[_Union[BoostSpec.ConditionBoostSpec.BoostControlSpec.AttributeType, str]]=..., interpolation_type: _Optional[_Union[BoostSpec.ConditionBoostSpec.BoostControlSpec.InterpolationType, str]]=..., control_points: _Optional[_Iterable[_Union[BoostSpec.ConditionBoostSpec.BoostControlSpec.ControlPoint, _Mapping]]]=...) -> None:
                ...
        CONDITION_FIELD_NUMBER: _ClassVar[int]
        BOOST_FIELD_NUMBER: _ClassVar[int]
        BOOST_CONTROL_SPEC_FIELD_NUMBER: _ClassVar[int]
        condition: str
        boost: float
        boost_control_spec: BoostSpec.ConditionBoostSpec.BoostControlSpec

        def __init__(self, condition: _Optional[str]=..., boost: _Optional[float]=..., boost_control_spec: _Optional[_Union[BoostSpec.ConditionBoostSpec.BoostControlSpec, _Mapping]]=...) -> None:
            ...
    CONDITION_BOOST_SPECS_FIELD_NUMBER: _ClassVar[int]
    condition_boost_specs: _containers.RepeatedCompositeFieldContainer[BoostSpec.ConditionBoostSpec]

    def __init__(self, condition_boost_specs: _Optional[_Iterable[_Union[BoostSpec.ConditionBoostSpec, _Mapping]]]=...) -> None:
        ...

class BoostSpecs(_message.Message):
    __slots__ = ('data_stores', 'spec')
    DATA_STORES_FIELD_NUMBER: _ClassVar[int]
    SPEC_FIELD_NUMBER: _ClassVar[int]
    data_stores: _containers.RepeatedScalarFieldContainer[str]
    spec: _containers.RepeatedCompositeFieldContainer[BoostSpec]

    def __init__(self, data_stores: _Optional[_Iterable[str]]=..., spec: _Optional[_Iterable[_Union[BoostSpec, _Mapping]]]=...) -> None:
        ...

class FilterSpecs(_message.Message):
    __slots__ = ('data_stores', 'filter')
    DATA_STORES_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    data_stores: _containers.RepeatedScalarFieldContainer[str]
    filter: str

    def __init__(self, data_stores: _Optional[_Iterable[str]]=..., filter: _Optional[str]=...) -> None:
        ...

class QueryInput(_message.Message):
    __slots__ = ('text', 'intent', 'audio', 'event', 'dtmf', 'tool_call_result', 'language_code')
    TEXT_FIELD_NUMBER: _ClassVar[int]
    INTENT_FIELD_NUMBER: _ClassVar[int]
    AUDIO_FIELD_NUMBER: _ClassVar[int]
    EVENT_FIELD_NUMBER: _ClassVar[int]
    DTMF_FIELD_NUMBER: _ClassVar[int]
    TOOL_CALL_RESULT_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    text: TextInput
    intent: IntentInput
    audio: AudioInput
    event: EventInput
    dtmf: DtmfInput
    tool_call_result: _tool_call_pb2.ToolCallResult
    language_code: str

    def __init__(self, text: _Optional[_Union[TextInput, _Mapping]]=..., intent: _Optional[_Union[IntentInput, _Mapping]]=..., audio: _Optional[_Union[AudioInput, _Mapping]]=..., event: _Optional[_Union[EventInput, _Mapping]]=..., dtmf: _Optional[_Union[DtmfInput, _Mapping]]=..., tool_call_result: _Optional[_Union[_tool_call_pb2.ToolCallResult, _Mapping]]=..., language_code: _Optional[str]=...) -> None:
        ...

class GenerativeInfo(_message.Message):
    __slots__ = ('current_playbooks', 'action_tracing_info')
    CURRENT_PLAYBOOKS_FIELD_NUMBER: _ClassVar[int]
    ACTION_TRACING_INFO_FIELD_NUMBER: _ClassVar[int]
    current_playbooks: _containers.RepeatedScalarFieldContainer[str]
    action_tracing_info: _example_pb2.Example

    def __init__(self, current_playbooks: _Optional[_Iterable[str]]=..., action_tracing_info: _Optional[_Union[_example_pb2.Example, _Mapping]]=...) -> None:
        ...

class QueryResult(_message.Message):
    __slots__ = ('text', 'trigger_intent', 'transcript', 'trigger_event', 'dtmf', 'language_code', 'parameters', 'response_messages', 'webhook_ids', 'webhook_display_names', 'webhook_latencies', 'webhook_tags', 'webhook_statuses', 'webhook_payloads', 'current_page', 'current_flow', 'intent', 'intent_detection_confidence', 'match', 'diagnostic_info', 'generative_info', 'sentiment_analysis_result', 'advanced_settings', 'allow_answer_feedback', 'data_store_connection_signals')
    TEXT_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_INTENT_FIELD_NUMBER: _ClassVar[int]
    TRANSCRIPT_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_EVENT_FIELD_NUMBER: _ClassVar[int]
    DTMF_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    WEBHOOK_IDS_FIELD_NUMBER: _ClassVar[int]
    WEBHOOK_DISPLAY_NAMES_FIELD_NUMBER: _ClassVar[int]
    WEBHOOK_LATENCIES_FIELD_NUMBER: _ClassVar[int]
    WEBHOOK_TAGS_FIELD_NUMBER: _ClassVar[int]
    WEBHOOK_STATUSES_FIELD_NUMBER: _ClassVar[int]
    WEBHOOK_PAYLOADS_FIELD_NUMBER: _ClassVar[int]
    CURRENT_PAGE_FIELD_NUMBER: _ClassVar[int]
    CURRENT_FLOW_FIELD_NUMBER: _ClassVar[int]
    INTENT_FIELD_NUMBER: _ClassVar[int]
    INTENT_DETECTION_CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    MATCH_FIELD_NUMBER: _ClassVar[int]
    DIAGNOSTIC_INFO_FIELD_NUMBER: _ClassVar[int]
    GENERATIVE_INFO_FIELD_NUMBER: _ClassVar[int]
    SENTIMENT_ANALYSIS_RESULT_FIELD_NUMBER: _ClassVar[int]
    ADVANCED_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    ALLOW_ANSWER_FEEDBACK_FIELD_NUMBER: _ClassVar[int]
    DATA_STORE_CONNECTION_SIGNALS_FIELD_NUMBER: _ClassVar[int]
    text: str
    trigger_intent: str
    transcript: str
    trigger_event: str
    dtmf: DtmfInput
    language_code: str
    parameters: _struct_pb2.Struct
    response_messages: _containers.RepeatedCompositeFieldContainer[_response_message_pb2.ResponseMessage]
    webhook_ids: _containers.RepeatedScalarFieldContainer[str]
    webhook_display_names: _containers.RepeatedScalarFieldContainer[str]
    webhook_latencies: _containers.RepeatedCompositeFieldContainer[_duration_pb2.Duration]
    webhook_tags: _containers.RepeatedScalarFieldContainer[str]
    webhook_statuses: _containers.RepeatedCompositeFieldContainer[_status_pb2.Status]
    webhook_payloads: _containers.RepeatedCompositeFieldContainer[_struct_pb2.Struct]
    current_page: _page_pb2.Page
    current_flow: _flow_pb2.Flow
    intent: _intent_pb2.Intent
    intent_detection_confidence: float
    match: Match
    diagnostic_info: _struct_pb2.Struct
    generative_info: GenerativeInfo
    sentiment_analysis_result: SentimentAnalysisResult
    advanced_settings: _advanced_settings_pb2.AdvancedSettings
    allow_answer_feedback: bool
    data_store_connection_signals: _data_store_connection_pb2.DataStoreConnectionSignals

    def __init__(self, text: _Optional[str]=..., trigger_intent: _Optional[str]=..., transcript: _Optional[str]=..., trigger_event: _Optional[str]=..., dtmf: _Optional[_Union[DtmfInput, _Mapping]]=..., language_code: _Optional[str]=..., parameters: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=..., response_messages: _Optional[_Iterable[_Union[_response_message_pb2.ResponseMessage, _Mapping]]]=..., webhook_ids: _Optional[_Iterable[str]]=..., webhook_display_names: _Optional[_Iterable[str]]=..., webhook_latencies: _Optional[_Iterable[_Union[_duration_pb2.Duration, _Mapping]]]=..., webhook_tags: _Optional[_Iterable[str]]=..., webhook_statuses: _Optional[_Iterable[_Union[_status_pb2.Status, _Mapping]]]=..., webhook_payloads: _Optional[_Iterable[_Union[_struct_pb2.Struct, _Mapping]]]=..., current_page: _Optional[_Union[_page_pb2.Page, _Mapping]]=..., current_flow: _Optional[_Union[_flow_pb2.Flow, _Mapping]]=..., intent: _Optional[_Union[_intent_pb2.Intent, _Mapping]]=..., intent_detection_confidence: _Optional[float]=..., match: _Optional[_Union[Match, _Mapping]]=..., diagnostic_info: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=..., generative_info: _Optional[_Union[GenerativeInfo, _Mapping]]=..., sentiment_analysis_result: _Optional[_Union[SentimentAnalysisResult, _Mapping]]=..., advanced_settings: _Optional[_Union[_advanced_settings_pb2.AdvancedSettings, _Mapping]]=..., allow_answer_feedback: bool=..., data_store_connection_signals: _Optional[_Union[_data_store_connection_pb2.DataStoreConnectionSignals, _Mapping]]=...) -> None:
        ...

class TextInput(_message.Message):
    __slots__ = ('text',)
    TEXT_FIELD_NUMBER: _ClassVar[int]
    text: str

    def __init__(self, text: _Optional[str]=...) -> None:
        ...

class IntentInput(_message.Message):
    __slots__ = ('intent',)
    INTENT_FIELD_NUMBER: _ClassVar[int]
    intent: str

    def __init__(self, intent: _Optional[str]=...) -> None:
        ...

class AudioInput(_message.Message):
    __slots__ = ('config', 'audio')
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    AUDIO_FIELD_NUMBER: _ClassVar[int]
    config: _audio_config_pb2.InputAudioConfig
    audio: bytes

    def __init__(self, config: _Optional[_Union[_audio_config_pb2.InputAudioConfig, _Mapping]]=..., audio: _Optional[bytes]=...) -> None:
        ...

class EventInput(_message.Message):
    __slots__ = ('event',)
    EVENT_FIELD_NUMBER: _ClassVar[int]
    event: str

    def __init__(self, event: _Optional[str]=...) -> None:
        ...

class DtmfInput(_message.Message):
    __slots__ = ('digits', 'finish_digit')
    DIGITS_FIELD_NUMBER: _ClassVar[int]
    FINISH_DIGIT_FIELD_NUMBER: _ClassVar[int]
    digits: str
    finish_digit: str

    def __init__(self, digits: _Optional[str]=..., finish_digit: _Optional[str]=...) -> None:
        ...

class Match(_message.Message):
    __slots__ = ('intent', 'event', 'parameters', 'resolved_input', 'match_type', 'confidence')

    class MatchType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MATCH_TYPE_UNSPECIFIED: _ClassVar[Match.MatchType]
        INTENT: _ClassVar[Match.MatchType]
        DIRECT_INTENT: _ClassVar[Match.MatchType]
        PARAMETER_FILLING: _ClassVar[Match.MatchType]
        NO_MATCH: _ClassVar[Match.MatchType]
        NO_INPUT: _ClassVar[Match.MatchType]
        EVENT: _ClassVar[Match.MatchType]
        KNOWLEDGE_CONNECTOR: _ClassVar[Match.MatchType]
        PLAYBOOK: _ClassVar[Match.MatchType]
    MATCH_TYPE_UNSPECIFIED: Match.MatchType
    INTENT: Match.MatchType
    DIRECT_INTENT: Match.MatchType
    PARAMETER_FILLING: Match.MatchType
    NO_MATCH: Match.MatchType
    NO_INPUT: Match.MatchType
    EVENT: Match.MatchType
    KNOWLEDGE_CONNECTOR: Match.MatchType
    PLAYBOOK: Match.MatchType
    INTENT_FIELD_NUMBER: _ClassVar[int]
    EVENT_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_INPUT_FIELD_NUMBER: _ClassVar[int]
    MATCH_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    intent: _intent_pb2.Intent
    event: str
    parameters: _struct_pb2.Struct
    resolved_input: str
    match_type: Match.MatchType
    confidence: float

    def __init__(self, intent: _Optional[_Union[_intent_pb2.Intent, _Mapping]]=..., event: _Optional[str]=..., parameters: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=..., resolved_input: _Optional[str]=..., match_type: _Optional[_Union[Match.MatchType, str]]=..., confidence: _Optional[float]=...) -> None:
        ...

class MatchIntentRequest(_message.Message):
    __slots__ = ('session', 'query_params', 'query_input', 'persist_parameter_changes')
    SESSION_FIELD_NUMBER: _ClassVar[int]
    QUERY_PARAMS_FIELD_NUMBER: _ClassVar[int]
    QUERY_INPUT_FIELD_NUMBER: _ClassVar[int]
    PERSIST_PARAMETER_CHANGES_FIELD_NUMBER: _ClassVar[int]
    session: str
    query_params: QueryParameters
    query_input: QueryInput
    persist_parameter_changes: bool

    def __init__(self, session: _Optional[str]=..., query_params: _Optional[_Union[QueryParameters, _Mapping]]=..., query_input: _Optional[_Union[QueryInput, _Mapping]]=..., persist_parameter_changes: bool=...) -> None:
        ...

class MatchIntentResponse(_message.Message):
    __slots__ = ('text', 'trigger_intent', 'transcript', 'trigger_event', 'matches', 'current_page')
    TEXT_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_INTENT_FIELD_NUMBER: _ClassVar[int]
    TRANSCRIPT_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_EVENT_FIELD_NUMBER: _ClassVar[int]
    MATCHES_FIELD_NUMBER: _ClassVar[int]
    CURRENT_PAGE_FIELD_NUMBER: _ClassVar[int]
    text: str
    trigger_intent: str
    transcript: str
    trigger_event: str
    matches: _containers.RepeatedCompositeFieldContainer[Match]
    current_page: _page_pb2.Page

    def __init__(self, text: _Optional[str]=..., trigger_intent: _Optional[str]=..., transcript: _Optional[str]=..., trigger_event: _Optional[str]=..., matches: _Optional[_Iterable[_Union[Match, _Mapping]]]=..., current_page: _Optional[_Union[_page_pb2.Page, _Mapping]]=...) -> None:
        ...

class FulfillIntentRequest(_message.Message):
    __slots__ = ('match_intent_request', 'match', 'output_audio_config')
    MATCH_INTENT_REQUEST_FIELD_NUMBER: _ClassVar[int]
    MATCH_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_AUDIO_CONFIG_FIELD_NUMBER: _ClassVar[int]
    match_intent_request: MatchIntentRequest
    match: Match
    output_audio_config: _audio_config_pb2.OutputAudioConfig

    def __init__(self, match_intent_request: _Optional[_Union[MatchIntentRequest, _Mapping]]=..., match: _Optional[_Union[Match, _Mapping]]=..., output_audio_config: _Optional[_Union[_audio_config_pb2.OutputAudioConfig, _Mapping]]=...) -> None:
        ...

class FulfillIntentResponse(_message.Message):
    __slots__ = ('response_id', 'query_result', 'output_audio', 'output_audio_config')
    RESPONSE_ID_FIELD_NUMBER: _ClassVar[int]
    QUERY_RESULT_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_AUDIO_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_AUDIO_CONFIG_FIELD_NUMBER: _ClassVar[int]
    response_id: str
    query_result: QueryResult
    output_audio: bytes
    output_audio_config: _audio_config_pb2.OutputAudioConfig

    def __init__(self, response_id: _Optional[str]=..., query_result: _Optional[_Union[QueryResult, _Mapping]]=..., output_audio: _Optional[bytes]=..., output_audio_config: _Optional[_Union[_audio_config_pb2.OutputAudioConfig, _Mapping]]=...) -> None:
        ...

class SentimentAnalysisResult(_message.Message):
    __slots__ = ('score', 'magnitude')
    SCORE_FIELD_NUMBER: _ClassVar[int]
    MAGNITUDE_FIELD_NUMBER: _ClassVar[int]
    score: float
    magnitude: float

    def __init__(self, score: _Optional[float]=..., magnitude: _Optional[float]=...) -> None:
        ...