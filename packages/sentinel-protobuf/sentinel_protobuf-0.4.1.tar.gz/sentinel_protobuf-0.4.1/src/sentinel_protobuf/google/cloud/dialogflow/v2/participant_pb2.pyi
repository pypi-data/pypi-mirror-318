from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.dialogflow.v2 import audio_config_pb2 as _audio_config_pb2
from google.cloud.dialogflow.v2 import session_pb2 as _session_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Participant(_message.Message):
    __slots__ = ('name', 'role', 'sip_recording_media_label', 'obfuscated_external_user_id', 'documents_metadata_filters')

    class Role(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ROLE_UNSPECIFIED: _ClassVar[Participant.Role]
        HUMAN_AGENT: _ClassVar[Participant.Role]
        AUTOMATED_AGENT: _ClassVar[Participant.Role]
        END_USER: _ClassVar[Participant.Role]
    ROLE_UNSPECIFIED: Participant.Role
    HUMAN_AGENT: Participant.Role
    AUTOMATED_AGENT: Participant.Role
    END_USER: Participant.Role

    class DocumentsMetadataFiltersEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    SIP_RECORDING_MEDIA_LABEL_FIELD_NUMBER: _ClassVar[int]
    OBFUSCATED_EXTERNAL_USER_ID_FIELD_NUMBER: _ClassVar[int]
    DOCUMENTS_METADATA_FILTERS_FIELD_NUMBER: _ClassVar[int]
    name: str
    role: Participant.Role
    sip_recording_media_label: str
    obfuscated_external_user_id: str
    documents_metadata_filters: _containers.ScalarMap[str, str]

    def __init__(self, name: _Optional[str]=..., role: _Optional[_Union[Participant.Role, str]]=..., sip_recording_media_label: _Optional[str]=..., obfuscated_external_user_id: _Optional[str]=..., documents_metadata_filters: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class Message(_message.Message):
    __slots__ = ('name', 'content', 'language_code', 'participant', 'participant_role', 'create_time', 'send_time', 'message_annotation', 'sentiment_analysis')
    NAME_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_ROLE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    SEND_TIME_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ANNOTATION_FIELD_NUMBER: _ClassVar[int]
    SENTIMENT_ANALYSIS_FIELD_NUMBER: _ClassVar[int]
    name: str
    content: str
    language_code: str
    participant: str
    participant_role: Participant.Role
    create_time: _timestamp_pb2.Timestamp
    send_time: _timestamp_pb2.Timestamp
    message_annotation: MessageAnnotation
    sentiment_analysis: _session_pb2.SentimentAnalysisResult

    def __init__(self, name: _Optional[str]=..., content: _Optional[str]=..., language_code: _Optional[str]=..., participant: _Optional[str]=..., participant_role: _Optional[_Union[Participant.Role, str]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., send_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., message_annotation: _Optional[_Union[MessageAnnotation, _Mapping]]=..., sentiment_analysis: _Optional[_Union[_session_pb2.SentimentAnalysisResult, _Mapping]]=...) -> None:
        ...

class CreateParticipantRequest(_message.Message):
    __slots__ = ('parent', 'participant')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_FIELD_NUMBER: _ClassVar[int]
    parent: str
    participant: Participant

    def __init__(self, parent: _Optional[str]=..., participant: _Optional[_Union[Participant, _Mapping]]=...) -> None:
        ...

class GetParticipantRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListParticipantsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListParticipantsResponse(_message.Message):
    __slots__ = ('participants', 'next_page_token')
    PARTICIPANTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    participants: _containers.RepeatedCompositeFieldContainer[Participant]
    next_page_token: str

    def __init__(self, participants: _Optional[_Iterable[_Union[Participant, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class UpdateParticipantRequest(_message.Message):
    __slots__ = ('participant', 'update_mask')
    PARTICIPANT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    participant: Participant
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, participant: _Optional[_Union[Participant, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class AnalyzeContentRequest(_message.Message):
    __slots__ = ('participant', 'text_input', 'event_input', 'suggestion_input', 'reply_audio_config', 'query_params', 'assist_query_params', 'cx_parameters', 'request_id')
    PARTICIPANT_FIELD_NUMBER: _ClassVar[int]
    TEXT_INPUT_FIELD_NUMBER: _ClassVar[int]
    EVENT_INPUT_FIELD_NUMBER: _ClassVar[int]
    SUGGESTION_INPUT_FIELD_NUMBER: _ClassVar[int]
    REPLY_AUDIO_CONFIG_FIELD_NUMBER: _ClassVar[int]
    QUERY_PARAMS_FIELD_NUMBER: _ClassVar[int]
    ASSIST_QUERY_PARAMS_FIELD_NUMBER: _ClassVar[int]
    CX_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    participant: str
    text_input: _session_pb2.TextInput
    event_input: _session_pb2.EventInput
    suggestion_input: SuggestionInput
    reply_audio_config: _audio_config_pb2.OutputAudioConfig
    query_params: _session_pb2.QueryParameters
    assist_query_params: AssistQueryParameters
    cx_parameters: _struct_pb2.Struct
    request_id: str

    def __init__(self, participant: _Optional[str]=..., text_input: _Optional[_Union[_session_pb2.TextInput, _Mapping]]=..., event_input: _Optional[_Union[_session_pb2.EventInput, _Mapping]]=..., suggestion_input: _Optional[_Union[SuggestionInput, _Mapping]]=..., reply_audio_config: _Optional[_Union[_audio_config_pb2.OutputAudioConfig, _Mapping]]=..., query_params: _Optional[_Union[_session_pb2.QueryParameters, _Mapping]]=..., assist_query_params: _Optional[_Union[AssistQueryParameters, _Mapping]]=..., cx_parameters: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class DtmfParameters(_message.Message):
    __slots__ = ('accepts_dtmf_input',)
    ACCEPTS_DTMF_INPUT_FIELD_NUMBER: _ClassVar[int]
    accepts_dtmf_input: bool

    def __init__(self, accepts_dtmf_input: bool=...) -> None:
        ...

class AnalyzeContentResponse(_message.Message):
    __slots__ = ('reply_text', 'reply_audio', 'automated_agent_reply', 'message', 'human_agent_suggestion_results', 'end_user_suggestion_results', 'dtmf_parameters')
    REPLY_TEXT_FIELD_NUMBER: _ClassVar[int]
    REPLY_AUDIO_FIELD_NUMBER: _ClassVar[int]
    AUTOMATED_AGENT_REPLY_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    HUMAN_AGENT_SUGGESTION_RESULTS_FIELD_NUMBER: _ClassVar[int]
    END_USER_SUGGESTION_RESULTS_FIELD_NUMBER: _ClassVar[int]
    DTMF_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    reply_text: str
    reply_audio: OutputAudio
    automated_agent_reply: AutomatedAgentReply
    message: Message
    human_agent_suggestion_results: _containers.RepeatedCompositeFieldContainer[SuggestionResult]
    end_user_suggestion_results: _containers.RepeatedCompositeFieldContainer[SuggestionResult]
    dtmf_parameters: DtmfParameters

    def __init__(self, reply_text: _Optional[str]=..., reply_audio: _Optional[_Union[OutputAudio, _Mapping]]=..., automated_agent_reply: _Optional[_Union[AutomatedAgentReply, _Mapping]]=..., message: _Optional[_Union[Message, _Mapping]]=..., human_agent_suggestion_results: _Optional[_Iterable[_Union[SuggestionResult, _Mapping]]]=..., end_user_suggestion_results: _Optional[_Iterable[_Union[SuggestionResult, _Mapping]]]=..., dtmf_parameters: _Optional[_Union[DtmfParameters, _Mapping]]=...) -> None:
        ...

class StreamingAnalyzeContentRequest(_message.Message):
    __slots__ = ('participant', 'audio_config', 'text_config', 'reply_audio_config', 'input_audio', 'input_text', 'input_dtmf', 'query_params', 'assist_query_params', 'cx_parameters', 'enable_extended_streaming', 'enable_partial_automated_agent_reply', 'enable_debugging_info')
    PARTICIPANT_FIELD_NUMBER: _ClassVar[int]
    AUDIO_CONFIG_FIELD_NUMBER: _ClassVar[int]
    TEXT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    REPLY_AUDIO_CONFIG_FIELD_NUMBER: _ClassVar[int]
    INPUT_AUDIO_FIELD_NUMBER: _ClassVar[int]
    INPUT_TEXT_FIELD_NUMBER: _ClassVar[int]
    INPUT_DTMF_FIELD_NUMBER: _ClassVar[int]
    QUERY_PARAMS_FIELD_NUMBER: _ClassVar[int]
    ASSIST_QUERY_PARAMS_FIELD_NUMBER: _ClassVar[int]
    CX_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    ENABLE_EXTENDED_STREAMING_FIELD_NUMBER: _ClassVar[int]
    ENABLE_PARTIAL_AUTOMATED_AGENT_REPLY_FIELD_NUMBER: _ClassVar[int]
    ENABLE_DEBUGGING_INFO_FIELD_NUMBER: _ClassVar[int]
    participant: str
    audio_config: _audio_config_pb2.InputAudioConfig
    text_config: InputTextConfig
    reply_audio_config: _audio_config_pb2.OutputAudioConfig
    input_audio: bytes
    input_text: str
    input_dtmf: _audio_config_pb2.TelephonyDtmfEvents
    query_params: _session_pb2.QueryParameters
    assist_query_params: AssistQueryParameters
    cx_parameters: _struct_pb2.Struct
    enable_extended_streaming: bool
    enable_partial_automated_agent_reply: bool
    enable_debugging_info: bool

    def __init__(self, participant: _Optional[str]=..., audio_config: _Optional[_Union[_audio_config_pb2.InputAudioConfig, _Mapping]]=..., text_config: _Optional[_Union[InputTextConfig, _Mapping]]=..., reply_audio_config: _Optional[_Union[_audio_config_pb2.OutputAudioConfig, _Mapping]]=..., input_audio: _Optional[bytes]=..., input_text: _Optional[str]=..., input_dtmf: _Optional[_Union[_audio_config_pb2.TelephonyDtmfEvents, _Mapping]]=..., query_params: _Optional[_Union[_session_pb2.QueryParameters, _Mapping]]=..., assist_query_params: _Optional[_Union[AssistQueryParameters, _Mapping]]=..., cx_parameters: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=..., enable_extended_streaming: bool=..., enable_partial_automated_agent_reply: bool=..., enable_debugging_info: bool=...) -> None:
        ...

class StreamingAnalyzeContentResponse(_message.Message):
    __slots__ = ('recognition_result', 'reply_text', 'reply_audio', 'automated_agent_reply', 'message', 'human_agent_suggestion_results', 'end_user_suggestion_results', 'dtmf_parameters', 'debugging_info')
    RECOGNITION_RESULT_FIELD_NUMBER: _ClassVar[int]
    REPLY_TEXT_FIELD_NUMBER: _ClassVar[int]
    REPLY_AUDIO_FIELD_NUMBER: _ClassVar[int]
    AUTOMATED_AGENT_REPLY_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    HUMAN_AGENT_SUGGESTION_RESULTS_FIELD_NUMBER: _ClassVar[int]
    END_USER_SUGGESTION_RESULTS_FIELD_NUMBER: _ClassVar[int]
    DTMF_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    DEBUGGING_INFO_FIELD_NUMBER: _ClassVar[int]
    recognition_result: _session_pb2.StreamingRecognitionResult
    reply_text: str
    reply_audio: OutputAudio
    automated_agent_reply: AutomatedAgentReply
    message: Message
    human_agent_suggestion_results: _containers.RepeatedCompositeFieldContainer[SuggestionResult]
    end_user_suggestion_results: _containers.RepeatedCompositeFieldContainer[SuggestionResult]
    dtmf_parameters: DtmfParameters
    debugging_info: _session_pb2.CloudConversationDebuggingInfo

    def __init__(self, recognition_result: _Optional[_Union[_session_pb2.StreamingRecognitionResult, _Mapping]]=..., reply_text: _Optional[str]=..., reply_audio: _Optional[_Union[OutputAudio, _Mapping]]=..., automated_agent_reply: _Optional[_Union[AutomatedAgentReply, _Mapping]]=..., message: _Optional[_Union[Message, _Mapping]]=..., human_agent_suggestion_results: _Optional[_Iterable[_Union[SuggestionResult, _Mapping]]]=..., end_user_suggestion_results: _Optional[_Iterable[_Union[SuggestionResult, _Mapping]]]=..., dtmf_parameters: _Optional[_Union[DtmfParameters, _Mapping]]=..., debugging_info: _Optional[_Union[_session_pb2.CloudConversationDebuggingInfo, _Mapping]]=...) -> None:
        ...

class SuggestArticlesRequest(_message.Message):
    __slots__ = ('parent', 'latest_message', 'context_size', 'assist_query_params')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    LATEST_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_SIZE_FIELD_NUMBER: _ClassVar[int]
    ASSIST_QUERY_PARAMS_FIELD_NUMBER: _ClassVar[int]
    parent: str
    latest_message: str
    context_size: int
    assist_query_params: AssistQueryParameters

    def __init__(self, parent: _Optional[str]=..., latest_message: _Optional[str]=..., context_size: _Optional[int]=..., assist_query_params: _Optional[_Union[AssistQueryParameters, _Mapping]]=...) -> None:
        ...

class SuggestArticlesResponse(_message.Message):
    __slots__ = ('article_answers', 'latest_message', 'context_size')
    ARTICLE_ANSWERS_FIELD_NUMBER: _ClassVar[int]
    LATEST_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_SIZE_FIELD_NUMBER: _ClassVar[int]
    article_answers: _containers.RepeatedCompositeFieldContainer[ArticleAnswer]
    latest_message: str
    context_size: int

    def __init__(self, article_answers: _Optional[_Iterable[_Union[ArticleAnswer, _Mapping]]]=..., latest_message: _Optional[str]=..., context_size: _Optional[int]=...) -> None:
        ...

class SuggestFaqAnswersRequest(_message.Message):
    __slots__ = ('parent', 'latest_message', 'context_size', 'assist_query_params')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    LATEST_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_SIZE_FIELD_NUMBER: _ClassVar[int]
    ASSIST_QUERY_PARAMS_FIELD_NUMBER: _ClassVar[int]
    parent: str
    latest_message: str
    context_size: int
    assist_query_params: AssistQueryParameters

    def __init__(self, parent: _Optional[str]=..., latest_message: _Optional[str]=..., context_size: _Optional[int]=..., assist_query_params: _Optional[_Union[AssistQueryParameters, _Mapping]]=...) -> None:
        ...

class SuggestFaqAnswersResponse(_message.Message):
    __slots__ = ('faq_answers', 'latest_message', 'context_size')
    FAQ_ANSWERS_FIELD_NUMBER: _ClassVar[int]
    LATEST_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_SIZE_FIELD_NUMBER: _ClassVar[int]
    faq_answers: _containers.RepeatedCompositeFieldContainer[FaqAnswer]
    latest_message: str
    context_size: int

    def __init__(self, faq_answers: _Optional[_Iterable[_Union[FaqAnswer, _Mapping]]]=..., latest_message: _Optional[str]=..., context_size: _Optional[int]=...) -> None:
        ...

class SuggestSmartRepliesRequest(_message.Message):
    __slots__ = ('parent', 'current_text_input', 'latest_message', 'context_size')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CURRENT_TEXT_INPUT_FIELD_NUMBER: _ClassVar[int]
    LATEST_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_SIZE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    current_text_input: _session_pb2.TextInput
    latest_message: str
    context_size: int

    def __init__(self, parent: _Optional[str]=..., current_text_input: _Optional[_Union[_session_pb2.TextInput, _Mapping]]=..., latest_message: _Optional[str]=..., context_size: _Optional[int]=...) -> None:
        ...

class SuggestSmartRepliesResponse(_message.Message):
    __slots__ = ('smart_reply_answers', 'latest_message', 'context_size')
    SMART_REPLY_ANSWERS_FIELD_NUMBER: _ClassVar[int]
    LATEST_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_SIZE_FIELD_NUMBER: _ClassVar[int]
    smart_reply_answers: _containers.RepeatedCompositeFieldContainer[SmartReplyAnswer]
    latest_message: str
    context_size: int

    def __init__(self, smart_reply_answers: _Optional[_Iterable[_Union[SmartReplyAnswer, _Mapping]]]=..., latest_message: _Optional[str]=..., context_size: _Optional[int]=...) -> None:
        ...

class OutputAudio(_message.Message):
    __slots__ = ('config', 'audio')
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    AUDIO_FIELD_NUMBER: _ClassVar[int]
    config: _audio_config_pb2.OutputAudioConfig
    audio: bytes

    def __init__(self, config: _Optional[_Union[_audio_config_pb2.OutputAudioConfig, _Mapping]]=..., audio: _Optional[bytes]=...) -> None:
        ...

class AutomatedAgentReply(_message.Message):
    __slots__ = ('detect_intent_response', 'automated_agent_reply_type', 'allow_cancellation', 'cx_current_page')

    class AutomatedAgentReplyType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        AUTOMATED_AGENT_REPLY_TYPE_UNSPECIFIED: _ClassVar[AutomatedAgentReply.AutomatedAgentReplyType]
        PARTIAL: _ClassVar[AutomatedAgentReply.AutomatedAgentReplyType]
        FINAL: _ClassVar[AutomatedAgentReply.AutomatedAgentReplyType]
    AUTOMATED_AGENT_REPLY_TYPE_UNSPECIFIED: AutomatedAgentReply.AutomatedAgentReplyType
    PARTIAL: AutomatedAgentReply.AutomatedAgentReplyType
    FINAL: AutomatedAgentReply.AutomatedAgentReplyType
    DETECT_INTENT_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    AUTOMATED_AGENT_REPLY_TYPE_FIELD_NUMBER: _ClassVar[int]
    ALLOW_CANCELLATION_FIELD_NUMBER: _ClassVar[int]
    CX_CURRENT_PAGE_FIELD_NUMBER: _ClassVar[int]
    detect_intent_response: _session_pb2.DetectIntentResponse
    automated_agent_reply_type: AutomatedAgentReply.AutomatedAgentReplyType
    allow_cancellation: bool
    cx_current_page: str

    def __init__(self, detect_intent_response: _Optional[_Union[_session_pb2.DetectIntentResponse, _Mapping]]=..., automated_agent_reply_type: _Optional[_Union[AutomatedAgentReply.AutomatedAgentReplyType, str]]=..., allow_cancellation: bool=..., cx_current_page: _Optional[str]=...) -> None:
        ...

class ArticleAnswer(_message.Message):
    __slots__ = ('title', 'uri', 'snippets', 'confidence', 'metadata', 'answer_record')

    class MetadataEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    TITLE_FIELD_NUMBER: _ClassVar[int]
    URI_FIELD_NUMBER: _ClassVar[int]
    SNIPPETS_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    ANSWER_RECORD_FIELD_NUMBER: _ClassVar[int]
    title: str
    uri: str
    snippets: _containers.RepeatedScalarFieldContainer[str]
    confidence: float
    metadata: _containers.ScalarMap[str, str]
    answer_record: str

    def __init__(self, title: _Optional[str]=..., uri: _Optional[str]=..., snippets: _Optional[_Iterable[str]]=..., confidence: _Optional[float]=..., metadata: _Optional[_Mapping[str, str]]=..., answer_record: _Optional[str]=...) -> None:
        ...

class FaqAnswer(_message.Message):
    __slots__ = ('answer', 'confidence', 'question', 'source', 'metadata', 'answer_record')

    class MetadataEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    ANSWER_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    QUESTION_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    ANSWER_RECORD_FIELD_NUMBER: _ClassVar[int]
    answer: str
    confidence: float
    question: str
    source: str
    metadata: _containers.ScalarMap[str, str]
    answer_record: str

    def __init__(self, answer: _Optional[str]=..., confidence: _Optional[float]=..., question: _Optional[str]=..., source: _Optional[str]=..., metadata: _Optional[_Mapping[str, str]]=..., answer_record: _Optional[str]=...) -> None:
        ...

class SmartReplyAnswer(_message.Message):
    __slots__ = ('reply', 'confidence', 'answer_record')
    REPLY_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    ANSWER_RECORD_FIELD_NUMBER: _ClassVar[int]
    reply: str
    confidence: float
    answer_record: str

    def __init__(self, reply: _Optional[str]=..., confidence: _Optional[float]=..., answer_record: _Optional[str]=...) -> None:
        ...

class IntentSuggestion(_message.Message):
    __slots__ = ('display_name', 'intent_v2', 'description')
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    INTENT_V2_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    display_name: str
    intent_v2: str
    description: str

    def __init__(self, display_name: _Optional[str]=..., intent_v2: _Optional[str]=..., description: _Optional[str]=...) -> None:
        ...

class DialogflowAssistAnswer(_message.Message):
    __slots__ = ('query_result', 'intent_suggestion', 'answer_record')
    QUERY_RESULT_FIELD_NUMBER: _ClassVar[int]
    INTENT_SUGGESTION_FIELD_NUMBER: _ClassVar[int]
    ANSWER_RECORD_FIELD_NUMBER: _ClassVar[int]
    query_result: _session_pb2.QueryResult
    intent_suggestion: IntentSuggestion
    answer_record: str

    def __init__(self, query_result: _Optional[_Union[_session_pb2.QueryResult, _Mapping]]=..., intent_suggestion: _Optional[_Union[IntentSuggestion, _Mapping]]=..., answer_record: _Optional[str]=...) -> None:
        ...

class SuggestionResult(_message.Message):
    __slots__ = ('error', 'suggest_articles_response', 'suggest_knowledge_assist_response', 'suggest_faq_answers_response', 'suggest_smart_replies_response')
    ERROR_FIELD_NUMBER: _ClassVar[int]
    SUGGEST_ARTICLES_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    SUGGEST_KNOWLEDGE_ASSIST_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    SUGGEST_FAQ_ANSWERS_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    SUGGEST_SMART_REPLIES_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    error: _status_pb2.Status
    suggest_articles_response: SuggestArticlesResponse
    suggest_knowledge_assist_response: SuggestKnowledgeAssistResponse
    suggest_faq_answers_response: SuggestFaqAnswersResponse
    suggest_smart_replies_response: SuggestSmartRepliesResponse

    def __init__(self, error: _Optional[_Union[_status_pb2.Status, _Mapping]]=..., suggest_articles_response: _Optional[_Union[SuggestArticlesResponse, _Mapping]]=..., suggest_knowledge_assist_response: _Optional[_Union[SuggestKnowledgeAssistResponse, _Mapping]]=..., suggest_faq_answers_response: _Optional[_Union[SuggestFaqAnswersResponse, _Mapping]]=..., suggest_smart_replies_response: _Optional[_Union[SuggestSmartRepliesResponse, _Mapping]]=...) -> None:
        ...

class InputTextConfig(_message.Message):
    __slots__ = ('language_code',)
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    language_code: str

    def __init__(self, language_code: _Optional[str]=...) -> None:
        ...

class AnnotatedMessagePart(_message.Message):
    __slots__ = ('text', 'entity_type', 'formatted_value')
    TEXT_FIELD_NUMBER: _ClassVar[int]
    ENTITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    FORMATTED_VALUE_FIELD_NUMBER: _ClassVar[int]
    text: str
    entity_type: str
    formatted_value: _struct_pb2.Value

    def __init__(self, text: _Optional[str]=..., entity_type: _Optional[str]=..., formatted_value: _Optional[_Union[_struct_pb2.Value, _Mapping]]=...) -> None:
        ...

class MessageAnnotation(_message.Message):
    __slots__ = ('parts', 'contain_entities')
    PARTS_FIELD_NUMBER: _ClassVar[int]
    CONTAIN_ENTITIES_FIELD_NUMBER: _ClassVar[int]
    parts: _containers.RepeatedCompositeFieldContainer[AnnotatedMessagePart]
    contain_entities: bool

    def __init__(self, parts: _Optional[_Iterable[_Union[AnnotatedMessagePart, _Mapping]]]=..., contain_entities: bool=...) -> None:
        ...

class SuggestionInput(_message.Message):
    __slots__ = ('answer_record',)
    ANSWER_RECORD_FIELD_NUMBER: _ClassVar[int]
    answer_record: str

    def __init__(self, answer_record: _Optional[str]=...) -> None:
        ...

class AssistQueryParameters(_message.Message):
    __slots__ = ('documents_metadata_filters',)

    class DocumentsMetadataFiltersEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    DOCUMENTS_METADATA_FILTERS_FIELD_NUMBER: _ClassVar[int]
    documents_metadata_filters: _containers.ScalarMap[str, str]

    def __init__(self, documents_metadata_filters: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class SuggestKnowledgeAssistRequest(_message.Message):
    __slots__ = ('parent', 'latest_message', 'context_size', 'previous_suggested_query')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    LATEST_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_SIZE_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_SUGGESTED_QUERY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    latest_message: str
    context_size: int
    previous_suggested_query: str

    def __init__(self, parent: _Optional[str]=..., latest_message: _Optional[str]=..., context_size: _Optional[int]=..., previous_suggested_query: _Optional[str]=...) -> None:
        ...

class SuggestKnowledgeAssistResponse(_message.Message):
    __slots__ = ('knowledge_assist_answer', 'latest_message', 'context_size')
    KNOWLEDGE_ASSIST_ANSWER_FIELD_NUMBER: _ClassVar[int]
    LATEST_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_SIZE_FIELD_NUMBER: _ClassVar[int]
    knowledge_assist_answer: KnowledgeAssistAnswer
    latest_message: str
    context_size: int

    def __init__(self, knowledge_assist_answer: _Optional[_Union[KnowledgeAssistAnswer, _Mapping]]=..., latest_message: _Optional[str]=..., context_size: _Optional[int]=...) -> None:
        ...

class KnowledgeAssistAnswer(_message.Message):
    __slots__ = ('suggested_query', 'suggested_query_answer', 'answer_record')

    class SuggestedQuery(_message.Message):
        __slots__ = ('query_text',)
        QUERY_TEXT_FIELD_NUMBER: _ClassVar[int]
        query_text: str

        def __init__(self, query_text: _Optional[str]=...) -> None:
            ...

    class KnowledgeAnswer(_message.Message):
        __slots__ = ('answer_text', 'faq_source', 'generative_source')

        class FaqSource(_message.Message):
            __slots__ = ('question',)
            QUESTION_FIELD_NUMBER: _ClassVar[int]
            question: str

            def __init__(self, question: _Optional[str]=...) -> None:
                ...

        class GenerativeSource(_message.Message):
            __slots__ = ('snippets',)

            class Snippet(_message.Message):
                __slots__ = ('uri', 'text', 'title', 'metadata')
                URI_FIELD_NUMBER: _ClassVar[int]
                TEXT_FIELD_NUMBER: _ClassVar[int]
                TITLE_FIELD_NUMBER: _ClassVar[int]
                METADATA_FIELD_NUMBER: _ClassVar[int]
                uri: str
                text: str
                title: str
                metadata: _struct_pb2.Struct

                def __init__(self, uri: _Optional[str]=..., text: _Optional[str]=..., title: _Optional[str]=..., metadata: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=...) -> None:
                    ...
            SNIPPETS_FIELD_NUMBER: _ClassVar[int]
            snippets: _containers.RepeatedCompositeFieldContainer[KnowledgeAssistAnswer.KnowledgeAnswer.GenerativeSource.Snippet]

            def __init__(self, snippets: _Optional[_Iterable[_Union[KnowledgeAssistAnswer.KnowledgeAnswer.GenerativeSource.Snippet, _Mapping]]]=...) -> None:
                ...
        ANSWER_TEXT_FIELD_NUMBER: _ClassVar[int]
        FAQ_SOURCE_FIELD_NUMBER: _ClassVar[int]
        GENERATIVE_SOURCE_FIELD_NUMBER: _ClassVar[int]
        answer_text: str
        faq_source: KnowledgeAssistAnswer.KnowledgeAnswer.FaqSource
        generative_source: KnowledgeAssistAnswer.KnowledgeAnswer.GenerativeSource

        def __init__(self, answer_text: _Optional[str]=..., faq_source: _Optional[_Union[KnowledgeAssistAnswer.KnowledgeAnswer.FaqSource, _Mapping]]=..., generative_source: _Optional[_Union[KnowledgeAssistAnswer.KnowledgeAnswer.GenerativeSource, _Mapping]]=...) -> None:
            ...
    SUGGESTED_QUERY_FIELD_NUMBER: _ClassVar[int]
    SUGGESTED_QUERY_ANSWER_FIELD_NUMBER: _ClassVar[int]
    ANSWER_RECORD_FIELD_NUMBER: _ClassVar[int]
    suggested_query: KnowledgeAssistAnswer.SuggestedQuery
    suggested_query_answer: KnowledgeAssistAnswer.KnowledgeAnswer
    answer_record: str

    def __init__(self, suggested_query: _Optional[_Union[KnowledgeAssistAnswer.SuggestedQuery, _Mapping]]=..., suggested_query_answer: _Optional[_Union[KnowledgeAssistAnswer.KnowledgeAnswer, _Mapping]]=..., answer_record: _Optional[str]=...) -> None:
        ...