from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DatasetValidationWarning(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DATASET_VALIDATION_WARNING_UNSPECIFIED: _ClassVar[DatasetValidationWarning]
    TOO_MANY_INVALID_FEEDBACK_LABELS: _ClassVar[DatasetValidationWarning]
    INSUFFICIENT_FEEDBACK_LABELS: _ClassVar[DatasetValidationWarning]
    INSUFFICIENT_FEEDBACK_LABELS_PER_ANSWER: _ClassVar[DatasetValidationWarning]
    ALL_FEEDBACK_LABELS_HAVE_THE_SAME_ANSWER: _ClassVar[DatasetValidationWarning]
DATASET_VALIDATION_WARNING_UNSPECIFIED: DatasetValidationWarning
TOO_MANY_INVALID_FEEDBACK_LABELS: DatasetValidationWarning
INSUFFICIENT_FEEDBACK_LABELS: DatasetValidationWarning
INSUFFICIENT_FEEDBACK_LABELS_PER_ANSWER: DatasetValidationWarning
ALL_FEEDBACK_LABELS_HAVE_THE_SAME_ANSWER: DatasetValidationWarning

class Conversation(_message.Message):
    __slots__ = ("call_metadata", "expire_time", "ttl", "name", "data_source", "create_time", "update_time", "start_time", "language_code", "agent_id", "labels", "quality_metadata", "metadata_json", "transcript", "medium", "duration", "turn_count", "latest_analysis", "latest_summary", "runtime_annotations", "dialogflow_intents", "obfuscated_user_id")
    class Medium(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MEDIUM_UNSPECIFIED: _ClassVar[Conversation.Medium]
        PHONE_CALL: _ClassVar[Conversation.Medium]
        CHAT: _ClassVar[Conversation.Medium]
    MEDIUM_UNSPECIFIED: Conversation.Medium
    PHONE_CALL: Conversation.Medium
    CHAT: Conversation.Medium
    class CallMetadata(_message.Message):
        __slots__ = ("customer_channel", "agent_channel")
        CUSTOMER_CHANNEL_FIELD_NUMBER: _ClassVar[int]
        AGENT_CHANNEL_FIELD_NUMBER: _ClassVar[int]
        customer_channel: int
        agent_channel: int
        def __init__(self, customer_channel: _Optional[int] = ..., agent_channel: _Optional[int] = ...) -> None: ...
    class QualityMetadata(_message.Message):
        __slots__ = ("customer_satisfaction_rating", "wait_duration", "menu_path", "agent_info")
        class AgentInfo(_message.Message):
            __slots__ = ("agent_id", "display_name", "team", "disposition_code", "agent_type")
            AGENT_ID_FIELD_NUMBER: _ClassVar[int]
            DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
            TEAM_FIELD_NUMBER: _ClassVar[int]
            DISPOSITION_CODE_FIELD_NUMBER: _ClassVar[int]
            AGENT_TYPE_FIELD_NUMBER: _ClassVar[int]
            agent_id: str
            display_name: str
            team: str
            disposition_code: str
            agent_type: ConversationParticipant.Role
            def __init__(self, agent_id: _Optional[str] = ..., display_name: _Optional[str] = ..., team: _Optional[str] = ..., disposition_code: _Optional[str] = ..., agent_type: _Optional[_Union[ConversationParticipant.Role, str]] = ...) -> None: ...
        CUSTOMER_SATISFACTION_RATING_FIELD_NUMBER: _ClassVar[int]
        WAIT_DURATION_FIELD_NUMBER: _ClassVar[int]
        MENU_PATH_FIELD_NUMBER: _ClassVar[int]
        AGENT_INFO_FIELD_NUMBER: _ClassVar[int]
        customer_satisfaction_rating: int
        wait_duration: _duration_pb2.Duration
        menu_path: str
        agent_info: _containers.RepeatedCompositeFieldContainer[Conversation.QualityMetadata.AgentInfo]
        def __init__(self, customer_satisfaction_rating: _Optional[int] = ..., wait_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., menu_path: _Optional[str] = ..., agent_info: _Optional[_Iterable[_Union[Conversation.QualityMetadata.AgentInfo, _Mapping]]] = ...) -> None: ...
    class Transcript(_message.Message):
        __slots__ = ("transcript_segments",)
        class TranscriptSegment(_message.Message):
            __slots__ = ("message_time", "text", "confidence", "words", "language_code", "channel_tag", "segment_participant", "dialogflow_segment_metadata", "sentiment")
            class WordInfo(_message.Message):
                __slots__ = ("start_offset", "end_offset", "word", "confidence")
                START_OFFSET_FIELD_NUMBER: _ClassVar[int]
                END_OFFSET_FIELD_NUMBER: _ClassVar[int]
                WORD_FIELD_NUMBER: _ClassVar[int]
                CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
                start_offset: _duration_pb2.Duration
                end_offset: _duration_pb2.Duration
                word: str
                confidence: float
                def __init__(self, start_offset: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., end_offset: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., word: _Optional[str] = ..., confidence: _Optional[float] = ...) -> None: ...
            class DialogflowSegmentMetadata(_message.Message):
                __slots__ = ("smart_reply_allowlist_covered",)
                SMART_REPLY_ALLOWLIST_COVERED_FIELD_NUMBER: _ClassVar[int]
                smart_reply_allowlist_covered: bool
                def __init__(self, smart_reply_allowlist_covered: bool = ...) -> None: ...
            MESSAGE_TIME_FIELD_NUMBER: _ClassVar[int]
            TEXT_FIELD_NUMBER: _ClassVar[int]
            CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
            WORDS_FIELD_NUMBER: _ClassVar[int]
            LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
            CHANNEL_TAG_FIELD_NUMBER: _ClassVar[int]
            SEGMENT_PARTICIPANT_FIELD_NUMBER: _ClassVar[int]
            DIALOGFLOW_SEGMENT_METADATA_FIELD_NUMBER: _ClassVar[int]
            SENTIMENT_FIELD_NUMBER: _ClassVar[int]
            message_time: _timestamp_pb2.Timestamp
            text: str
            confidence: float
            words: _containers.RepeatedCompositeFieldContainer[Conversation.Transcript.TranscriptSegment.WordInfo]
            language_code: str
            channel_tag: int
            segment_participant: ConversationParticipant
            dialogflow_segment_metadata: Conversation.Transcript.TranscriptSegment.DialogflowSegmentMetadata
            sentiment: SentimentData
            def __init__(self, message_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., text: _Optional[str] = ..., confidence: _Optional[float] = ..., words: _Optional[_Iterable[_Union[Conversation.Transcript.TranscriptSegment.WordInfo, _Mapping]]] = ..., language_code: _Optional[str] = ..., channel_tag: _Optional[int] = ..., segment_participant: _Optional[_Union[ConversationParticipant, _Mapping]] = ..., dialogflow_segment_metadata: _Optional[_Union[Conversation.Transcript.TranscriptSegment.DialogflowSegmentMetadata, _Mapping]] = ..., sentiment: _Optional[_Union[SentimentData, _Mapping]] = ...) -> None: ...
        TRANSCRIPT_SEGMENTS_FIELD_NUMBER: _ClassVar[int]
        transcript_segments: _containers.RepeatedCompositeFieldContainer[Conversation.Transcript.TranscriptSegment]
        def __init__(self, transcript_segments: _Optional[_Iterable[_Union[Conversation.Transcript.TranscriptSegment, _Mapping]]] = ...) -> None: ...
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class DialogflowIntentsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: DialogflowIntent
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[DialogflowIntent, _Mapping]] = ...) -> None: ...
    CALL_METADATA_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
    TTL_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DATA_SOURCE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    QUALITY_METADATA_FIELD_NUMBER: _ClassVar[int]
    METADATA_JSON_FIELD_NUMBER: _ClassVar[int]
    TRANSCRIPT_FIELD_NUMBER: _ClassVar[int]
    MEDIUM_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    TURN_COUNT_FIELD_NUMBER: _ClassVar[int]
    LATEST_ANALYSIS_FIELD_NUMBER: _ClassVar[int]
    LATEST_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    DIALOGFLOW_INTENTS_FIELD_NUMBER: _ClassVar[int]
    OBFUSCATED_USER_ID_FIELD_NUMBER: _ClassVar[int]
    call_metadata: Conversation.CallMetadata
    expire_time: _timestamp_pb2.Timestamp
    ttl: _duration_pb2.Duration
    name: str
    data_source: ConversationDataSource
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    start_time: _timestamp_pb2.Timestamp
    language_code: str
    agent_id: str
    labels: _containers.ScalarMap[str, str]
    quality_metadata: Conversation.QualityMetadata
    metadata_json: str
    transcript: Conversation.Transcript
    medium: Conversation.Medium
    duration: _duration_pb2.Duration
    turn_count: int
    latest_analysis: Analysis
    latest_summary: ConversationSummarizationSuggestionData
    runtime_annotations: _containers.RepeatedCompositeFieldContainer[RuntimeAnnotation]
    dialogflow_intents: _containers.MessageMap[str, DialogflowIntent]
    obfuscated_user_id: str
    def __init__(self, call_metadata: _Optional[_Union[Conversation.CallMetadata, _Mapping]] = ..., expire_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., ttl: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., name: _Optional[str] = ..., data_source: _Optional[_Union[ConversationDataSource, _Mapping]] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., language_code: _Optional[str] = ..., agent_id: _Optional[str] = ..., labels: _Optional[_Mapping[str, str]] = ..., quality_metadata: _Optional[_Union[Conversation.QualityMetadata, _Mapping]] = ..., metadata_json: _Optional[str] = ..., transcript: _Optional[_Union[Conversation.Transcript, _Mapping]] = ..., medium: _Optional[_Union[Conversation.Medium, str]] = ..., duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., turn_count: _Optional[int] = ..., latest_analysis: _Optional[_Union[Analysis, _Mapping]] = ..., latest_summary: _Optional[_Union[ConversationSummarizationSuggestionData, _Mapping]] = ..., runtime_annotations: _Optional[_Iterable[_Union[RuntimeAnnotation, _Mapping]]] = ..., dialogflow_intents: _Optional[_Mapping[str, DialogflowIntent]] = ..., obfuscated_user_id: _Optional[str] = ...) -> None: ...

class Analysis(_message.Message):
    __slots__ = ("name", "request_time", "create_time", "analysis_result", "annotator_selector")
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_TIME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    ANALYSIS_RESULT_FIELD_NUMBER: _ClassVar[int]
    ANNOTATOR_SELECTOR_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_time: _timestamp_pb2.Timestamp
    create_time: _timestamp_pb2.Timestamp
    analysis_result: AnalysisResult
    annotator_selector: AnnotatorSelector
    def __init__(self, name: _Optional[str] = ..., request_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., analysis_result: _Optional[_Union[AnalysisResult, _Mapping]] = ..., annotator_selector: _Optional[_Union[AnnotatorSelector, _Mapping]] = ...) -> None: ...

class ConversationDataSource(_message.Message):
    __slots__ = ("gcs_source", "dialogflow_source")
    GCS_SOURCE_FIELD_NUMBER: _ClassVar[int]
    DIALOGFLOW_SOURCE_FIELD_NUMBER: _ClassVar[int]
    gcs_source: GcsSource
    dialogflow_source: DialogflowSource
    def __init__(self, gcs_source: _Optional[_Union[GcsSource, _Mapping]] = ..., dialogflow_source: _Optional[_Union[DialogflowSource, _Mapping]] = ...) -> None: ...

class GcsSource(_message.Message):
    __slots__ = ("audio_uri", "transcript_uri")
    AUDIO_URI_FIELD_NUMBER: _ClassVar[int]
    TRANSCRIPT_URI_FIELD_NUMBER: _ClassVar[int]
    audio_uri: str
    transcript_uri: str
    def __init__(self, audio_uri: _Optional[str] = ..., transcript_uri: _Optional[str] = ...) -> None: ...

class DialogflowSource(_message.Message):
    __slots__ = ("dialogflow_conversation", "audio_uri")
    DIALOGFLOW_CONVERSATION_FIELD_NUMBER: _ClassVar[int]
    AUDIO_URI_FIELD_NUMBER: _ClassVar[int]
    dialogflow_conversation: str
    audio_uri: str
    def __init__(self, dialogflow_conversation: _Optional[str] = ..., audio_uri: _Optional[str] = ...) -> None: ...

class AnalysisResult(_message.Message):
    __slots__ = ("call_analysis_metadata", "end_time")
    class CallAnalysisMetadata(_message.Message):
        __slots__ = ("annotations", "entities", "sentiments", "silence", "intents", "phrase_matchers", "issue_model_result", "qa_scorecard_results")
        class EntitiesEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: Entity
            def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Entity, _Mapping]] = ...) -> None: ...
        class IntentsEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: Intent
            def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Intent, _Mapping]] = ...) -> None: ...
        class PhraseMatchersEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: PhraseMatchData
            def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[PhraseMatchData, _Mapping]] = ...) -> None: ...
        ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
        ENTITIES_FIELD_NUMBER: _ClassVar[int]
        SENTIMENTS_FIELD_NUMBER: _ClassVar[int]
        SILENCE_FIELD_NUMBER: _ClassVar[int]
        INTENTS_FIELD_NUMBER: _ClassVar[int]
        PHRASE_MATCHERS_FIELD_NUMBER: _ClassVar[int]
        ISSUE_MODEL_RESULT_FIELD_NUMBER: _ClassVar[int]
        QA_SCORECARD_RESULTS_FIELD_NUMBER: _ClassVar[int]
        annotations: _containers.RepeatedCompositeFieldContainer[CallAnnotation]
        entities: _containers.MessageMap[str, Entity]
        sentiments: _containers.RepeatedCompositeFieldContainer[ConversationLevelSentiment]
        silence: ConversationLevelSilence
        intents: _containers.MessageMap[str, Intent]
        phrase_matchers: _containers.MessageMap[str, PhraseMatchData]
        issue_model_result: IssueModelResult
        qa_scorecard_results: _containers.RepeatedCompositeFieldContainer[QaScorecardResult]
        def __init__(self, annotations: _Optional[_Iterable[_Union[CallAnnotation, _Mapping]]] = ..., entities: _Optional[_Mapping[str, Entity]] = ..., sentiments: _Optional[_Iterable[_Union[ConversationLevelSentiment, _Mapping]]] = ..., silence: _Optional[_Union[ConversationLevelSilence, _Mapping]] = ..., intents: _Optional[_Mapping[str, Intent]] = ..., phrase_matchers: _Optional[_Mapping[str, PhraseMatchData]] = ..., issue_model_result: _Optional[_Union[IssueModelResult, _Mapping]] = ..., qa_scorecard_results: _Optional[_Iterable[_Union[QaScorecardResult, _Mapping]]] = ...) -> None: ...
    CALL_ANALYSIS_METADATA_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    call_analysis_metadata: AnalysisResult.CallAnalysisMetadata
    end_time: _timestamp_pb2.Timestamp
    def __init__(self, call_analysis_metadata: _Optional[_Union[AnalysisResult.CallAnalysisMetadata, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class IssueModelResult(_message.Message):
    __slots__ = ("issue_model", "issues")
    ISSUE_MODEL_FIELD_NUMBER: _ClassVar[int]
    ISSUES_FIELD_NUMBER: _ClassVar[int]
    issue_model: str
    issues: _containers.RepeatedCompositeFieldContainer[IssueAssignment]
    def __init__(self, issue_model: _Optional[str] = ..., issues: _Optional[_Iterable[_Union[IssueAssignment, _Mapping]]] = ...) -> None: ...

class FeedbackLabel(_message.Message):
    __slots__ = ("label", "qa_answer_label", "name", "labeled_resource", "create_time", "update_time")
    LABEL_FIELD_NUMBER: _ClassVar[int]
    QA_ANSWER_LABEL_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    LABELED_RESOURCE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    label: str
    qa_answer_label: QaAnswer.AnswerValue
    name: str
    labeled_resource: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    def __init__(self, label: _Optional[str] = ..., qa_answer_label: _Optional[_Union[QaAnswer.AnswerValue, _Mapping]] = ..., name: _Optional[str] = ..., labeled_resource: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ConversationLevelSentiment(_message.Message):
    __slots__ = ("channel_tag", "sentiment_data")
    CHANNEL_TAG_FIELD_NUMBER: _ClassVar[int]
    SENTIMENT_DATA_FIELD_NUMBER: _ClassVar[int]
    channel_tag: int
    sentiment_data: SentimentData
    def __init__(self, channel_tag: _Optional[int] = ..., sentiment_data: _Optional[_Union[SentimentData, _Mapping]] = ...) -> None: ...

class ConversationLevelSilence(_message.Message):
    __slots__ = ("silence_duration", "silence_percentage")
    SILENCE_DURATION_FIELD_NUMBER: _ClassVar[int]
    SILENCE_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    silence_duration: _duration_pb2.Duration
    silence_percentage: float
    def __init__(self, silence_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., silence_percentage: _Optional[float] = ...) -> None: ...

class IssueAssignment(_message.Message):
    __slots__ = ("issue", "score", "display_name")
    ISSUE_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    issue: str
    score: float
    display_name: str
    def __init__(self, issue: _Optional[str] = ..., score: _Optional[float] = ..., display_name: _Optional[str] = ...) -> None: ...

class CallAnnotation(_message.Message):
    __slots__ = ("interruption_data", "sentiment_data", "silence_data", "hold_data", "entity_mention_data", "intent_match_data", "phrase_match_data", "issue_match_data", "channel_tag", "annotation_start_boundary", "annotation_end_boundary")
    INTERRUPTION_DATA_FIELD_NUMBER: _ClassVar[int]
    SENTIMENT_DATA_FIELD_NUMBER: _ClassVar[int]
    SILENCE_DATA_FIELD_NUMBER: _ClassVar[int]
    HOLD_DATA_FIELD_NUMBER: _ClassVar[int]
    ENTITY_MENTION_DATA_FIELD_NUMBER: _ClassVar[int]
    INTENT_MATCH_DATA_FIELD_NUMBER: _ClassVar[int]
    PHRASE_MATCH_DATA_FIELD_NUMBER: _ClassVar[int]
    ISSUE_MATCH_DATA_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_TAG_FIELD_NUMBER: _ClassVar[int]
    ANNOTATION_START_BOUNDARY_FIELD_NUMBER: _ClassVar[int]
    ANNOTATION_END_BOUNDARY_FIELD_NUMBER: _ClassVar[int]
    interruption_data: InterruptionData
    sentiment_data: SentimentData
    silence_data: SilenceData
    hold_data: HoldData
    entity_mention_data: EntityMentionData
    intent_match_data: IntentMatchData
    phrase_match_data: PhraseMatchData
    issue_match_data: IssueMatchData
    channel_tag: int
    annotation_start_boundary: AnnotationBoundary
    annotation_end_boundary: AnnotationBoundary
    def __init__(self, interruption_data: _Optional[_Union[InterruptionData, _Mapping]] = ..., sentiment_data: _Optional[_Union[SentimentData, _Mapping]] = ..., silence_data: _Optional[_Union[SilenceData, _Mapping]] = ..., hold_data: _Optional[_Union[HoldData, _Mapping]] = ..., entity_mention_data: _Optional[_Union[EntityMentionData, _Mapping]] = ..., intent_match_data: _Optional[_Union[IntentMatchData, _Mapping]] = ..., phrase_match_data: _Optional[_Union[PhraseMatchData, _Mapping]] = ..., issue_match_data: _Optional[_Union[IssueMatchData, _Mapping]] = ..., channel_tag: _Optional[int] = ..., annotation_start_boundary: _Optional[_Union[AnnotationBoundary, _Mapping]] = ..., annotation_end_boundary: _Optional[_Union[AnnotationBoundary, _Mapping]] = ...) -> None: ...

class AnnotationBoundary(_message.Message):
    __slots__ = ("word_index", "transcript_index")
    WORD_INDEX_FIELD_NUMBER: _ClassVar[int]
    TRANSCRIPT_INDEX_FIELD_NUMBER: _ClassVar[int]
    word_index: int
    transcript_index: int
    def __init__(self, word_index: _Optional[int] = ..., transcript_index: _Optional[int] = ...) -> None: ...

class Entity(_message.Message):
    __slots__ = ("display_name", "type", "metadata", "salience", "sentiment")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[Entity.Type]
        PERSON: _ClassVar[Entity.Type]
        LOCATION: _ClassVar[Entity.Type]
        ORGANIZATION: _ClassVar[Entity.Type]
        EVENT: _ClassVar[Entity.Type]
        WORK_OF_ART: _ClassVar[Entity.Type]
        CONSUMER_GOOD: _ClassVar[Entity.Type]
        OTHER: _ClassVar[Entity.Type]
        PHONE_NUMBER: _ClassVar[Entity.Type]
        ADDRESS: _ClassVar[Entity.Type]
        DATE: _ClassVar[Entity.Type]
        NUMBER: _ClassVar[Entity.Type]
        PRICE: _ClassVar[Entity.Type]
    TYPE_UNSPECIFIED: Entity.Type
    PERSON: Entity.Type
    LOCATION: Entity.Type
    ORGANIZATION: Entity.Type
    EVENT: Entity.Type
    WORK_OF_ART: Entity.Type
    CONSUMER_GOOD: Entity.Type
    OTHER: Entity.Type
    PHONE_NUMBER: Entity.Type
    ADDRESS: Entity.Type
    DATE: Entity.Type
    NUMBER: Entity.Type
    PRICE: Entity.Type
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    SALIENCE_FIELD_NUMBER: _ClassVar[int]
    SENTIMENT_FIELD_NUMBER: _ClassVar[int]
    display_name: str
    type: Entity.Type
    metadata: _containers.ScalarMap[str, str]
    salience: float
    sentiment: SentimentData
    def __init__(self, display_name: _Optional[str] = ..., type: _Optional[_Union[Entity.Type, str]] = ..., metadata: _Optional[_Mapping[str, str]] = ..., salience: _Optional[float] = ..., sentiment: _Optional[_Union[SentimentData, _Mapping]] = ...) -> None: ...

class Intent(_message.Message):
    __slots__ = ("id", "display_name")
    ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    display_name: str
    def __init__(self, id: _Optional[str] = ..., display_name: _Optional[str] = ...) -> None: ...

class PhraseMatchData(_message.Message):
    __slots__ = ("phrase_matcher", "display_name")
    PHRASE_MATCHER_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    phrase_matcher: str
    display_name: str
    def __init__(self, phrase_matcher: _Optional[str] = ..., display_name: _Optional[str] = ...) -> None: ...

class DialogflowIntent(_message.Message):
    __slots__ = ("display_name",)
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    display_name: str
    def __init__(self, display_name: _Optional[str] = ...) -> None: ...

class InterruptionData(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SilenceData(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class HoldData(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class EntityMentionData(_message.Message):
    __slots__ = ("entity_unique_id", "type", "sentiment")
    class MentionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MENTION_TYPE_UNSPECIFIED: _ClassVar[EntityMentionData.MentionType]
        PROPER: _ClassVar[EntityMentionData.MentionType]
        COMMON: _ClassVar[EntityMentionData.MentionType]
    MENTION_TYPE_UNSPECIFIED: EntityMentionData.MentionType
    PROPER: EntityMentionData.MentionType
    COMMON: EntityMentionData.MentionType
    ENTITY_UNIQUE_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SENTIMENT_FIELD_NUMBER: _ClassVar[int]
    entity_unique_id: str
    type: EntityMentionData.MentionType
    sentiment: SentimentData
    def __init__(self, entity_unique_id: _Optional[str] = ..., type: _Optional[_Union[EntityMentionData.MentionType, str]] = ..., sentiment: _Optional[_Union[SentimentData, _Mapping]] = ...) -> None: ...

class IntentMatchData(_message.Message):
    __slots__ = ("intent_unique_id",)
    INTENT_UNIQUE_ID_FIELD_NUMBER: _ClassVar[int]
    intent_unique_id: str
    def __init__(self, intent_unique_id: _Optional[str] = ...) -> None: ...

class SentimentData(_message.Message):
    __slots__ = ("magnitude", "score")
    MAGNITUDE_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    magnitude: float
    score: float
    def __init__(self, magnitude: _Optional[float] = ..., score: _Optional[float] = ...) -> None: ...

class IssueMatchData(_message.Message):
    __slots__ = ("issue_assignment",)
    ISSUE_ASSIGNMENT_FIELD_NUMBER: _ClassVar[int]
    issue_assignment: IssueAssignment
    def __init__(self, issue_assignment: _Optional[_Union[IssueAssignment, _Mapping]] = ...) -> None: ...

class IssueModel(_message.Message):
    __slots__ = ("name", "display_name", "create_time", "update_time", "issue_count", "state", "input_data_config", "training_stats", "model_type", "language_code")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[IssueModel.State]
        UNDEPLOYED: _ClassVar[IssueModel.State]
        DEPLOYING: _ClassVar[IssueModel.State]
        DEPLOYED: _ClassVar[IssueModel.State]
        UNDEPLOYING: _ClassVar[IssueModel.State]
        DELETING: _ClassVar[IssueModel.State]
    STATE_UNSPECIFIED: IssueModel.State
    UNDEPLOYED: IssueModel.State
    DEPLOYING: IssueModel.State
    DEPLOYED: IssueModel.State
    UNDEPLOYING: IssueModel.State
    DELETING: IssueModel.State
    class ModelType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MODEL_TYPE_UNSPECIFIED: _ClassVar[IssueModel.ModelType]
        TYPE_V1: _ClassVar[IssueModel.ModelType]
        TYPE_V2: _ClassVar[IssueModel.ModelType]
    MODEL_TYPE_UNSPECIFIED: IssueModel.ModelType
    TYPE_V1: IssueModel.ModelType
    TYPE_V2: IssueModel.ModelType
    class InputDataConfig(_message.Message):
        __slots__ = ("medium", "training_conversations_count", "filter")
        MEDIUM_FIELD_NUMBER: _ClassVar[int]
        TRAINING_CONVERSATIONS_COUNT_FIELD_NUMBER: _ClassVar[int]
        FILTER_FIELD_NUMBER: _ClassVar[int]
        medium: Conversation.Medium
        training_conversations_count: int
        filter: str
        def __init__(self, medium: _Optional[_Union[Conversation.Medium, str]] = ..., training_conversations_count: _Optional[int] = ..., filter: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    ISSUE_COUNT_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    INPUT_DATA_CONFIG_FIELD_NUMBER: _ClassVar[int]
    TRAINING_STATS_FIELD_NUMBER: _ClassVar[int]
    MODEL_TYPE_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    issue_count: int
    state: IssueModel.State
    input_data_config: IssueModel.InputDataConfig
    training_stats: IssueModelLabelStats
    model_type: IssueModel.ModelType
    language_code: str
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., issue_count: _Optional[int] = ..., state: _Optional[_Union[IssueModel.State, str]] = ..., input_data_config: _Optional[_Union[IssueModel.InputDataConfig, _Mapping]] = ..., training_stats: _Optional[_Union[IssueModelLabelStats, _Mapping]] = ..., model_type: _Optional[_Union[IssueModel.ModelType, str]] = ..., language_code: _Optional[str] = ...) -> None: ...

class Issue(_message.Message):
    __slots__ = ("name", "display_name", "create_time", "update_time", "sample_utterances", "display_description")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_UTTERANCES_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    sample_utterances: _containers.RepeatedScalarFieldContainer[str]
    display_description: str
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., sample_utterances: _Optional[_Iterable[str]] = ..., display_description: _Optional[str] = ...) -> None: ...

class IssueModelLabelStats(_message.Message):
    __slots__ = ("analyzed_conversations_count", "unclassified_conversations_count", "issue_stats")
    class IssueStats(_message.Message):
        __slots__ = ("issue", "labeled_conversations_count", "display_name")
        ISSUE_FIELD_NUMBER: _ClassVar[int]
        LABELED_CONVERSATIONS_COUNT_FIELD_NUMBER: _ClassVar[int]
        DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
        issue: str
        labeled_conversations_count: int
        display_name: str
        def __init__(self, issue: _Optional[str] = ..., labeled_conversations_count: _Optional[int] = ..., display_name: _Optional[str] = ...) -> None: ...
    class IssueStatsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: IssueModelLabelStats.IssueStats
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[IssueModelLabelStats.IssueStats, _Mapping]] = ...) -> None: ...
    ANALYZED_CONVERSATIONS_COUNT_FIELD_NUMBER: _ClassVar[int]
    UNCLASSIFIED_CONVERSATIONS_COUNT_FIELD_NUMBER: _ClassVar[int]
    ISSUE_STATS_FIELD_NUMBER: _ClassVar[int]
    analyzed_conversations_count: int
    unclassified_conversations_count: int
    issue_stats: _containers.MessageMap[str, IssueModelLabelStats.IssueStats]
    def __init__(self, analyzed_conversations_count: _Optional[int] = ..., unclassified_conversations_count: _Optional[int] = ..., issue_stats: _Optional[_Mapping[str, IssueModelLabelStats.IssueStats]] = ...) -> None: ...

class PhraseMatcher(_message.Message):
    __slots__ = ("name", "revision_id", "version_tag", "revision_create_time", "display_name", "type", "active", "phrase_match_rule_groups", "activation_update_time", "role_match", "update_time")
    class PhraseMatcherType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PHRASE_MATCHER_TYPE_UNSPECIFIED: _ClassVar[PhraseMatcher.PhraseMatcherType]
        ALL_OF: _ClassVar[PhraseMatcher.PhraseMatcherType]
        ANY_OF: _ClassVar[PhraseMatcher.PhraseMatcherType]
    PHRASE_MATCHER_TYPE_UNSPECIFIED: PhraseMatcher.PhraseMatcherType
    ALL_OF: PhraseMatcher.PhraseMatcherType
    ANY_OF: PhraseMatcher.PhraseMatcherType
    NAME_FIELD_NUMBER: _ClassVar[int]
    REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_TAG_FIELD_NUMBER: _ClassVar[int]
    REVISION_CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    PHRASE_MATCH_RULE_GROUPS_FIELD_NUMBER: _ClassVar[int]
    ACTIVATION_UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    ROLE_MATCH_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    revision_id: str
    version_tag: str
    revision_create_time: _timestamp_pb2.Timestamp
    display_name: str
    type: PhraseMatcher.PhraseMatcherType
    active: bool
    phrase_match_rule_groups: _containers.RepeatedCompositeFieldContainer[PhraseMatchRuleGroup]
    activation_update_time: _timestamp_pb2.Timestamp
    role_match: ConversationParticipant.Role
    update_time: _timestamp_pb2.Timestamp
    def __init__(self, name: _Optional[str] = ..., revision_id: _Optional[str] = ..., version_tag: _Optional[str] = ..., revision_create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., display_name: _Optional[str] = ..., type: _Optional[_Union[PhraseMatcher.PhraseMatcherType, str]] = ..., active: bool = ..., phrase_match_rule_groups: _Optional[_Iterable[_Union[PhraseMatchRuleGroup, _Mapping]]] = ..., activation_update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., role_match: _Optional[_Union[ConversationParticipant.Role, str]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class PhraseMatchRuleGroup(_message.Message):
    __slots__ = ("type", "phrase_match_rules")
    class PhraseMatchRuleGroupType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PHRASE_MATCH_RULE_GROUP_TYPE_UNSPECIFIED: _ClassVar[PhraseMatchRuleGroup.PhraseMatchRuleGroupType]
        ALL_OF: _ClassVar[PhraseMatchRuleGroup.PhraseMatchRuleGroupType]
        ANY_OF: _ClassVar[PhraseMatchRuleGroup.PhraseMatchRuleGroupType]
    PHRASE_MATCH_RULE_GROUP_TYPE_UNSPECIFIED: PhraseMatchRuleGroup.PhraseMatchRuleGroupType
    ALL_OF: PhraseMatchRuleGroup.PhraseMatchRuleGroupType
    ANY_OF: PhraseMatchRuleGroup.PhraseMatchRuleGroupType
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PHRASE_MATCH_RULES_FIELD_NUMBER: _ClassVar[int]
    type: PhraseMatchRuleGroup.PhraseMatchRuleGroupType
    phrase_match_rules: _containers.RepeatedCompositeFieldContainer[PhraseMatchRule]
    def __init__(self, type: _Optional[_Union[PhraseMatchRuleGroup.PhraseMatchRuleGroupType, str]] = ..., phrase_match_rules: _Optional[_Iterable[_Union[PhraseMatchRule, _Mapping]]] = ...) -> None: ...

class PhraseMatchRule(_message.Message):
    __slots__ = ("query", "negated", "config")
    QUERY_FIELD_NUMBER: _ClassVar[int]
    NEGATED_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    query: str
    negated: bool
    config: PhraseMatchRuleConfig
    def __init__(self, query: _Optional[str] = ..., negated: bool = ..., config: _Optional[_Union[PhraseMatchRuleConfig, _Mapping]] = ...) -> None: ...

class PhraseMatchRuleConfig(_message.Message):
    __slots__ = ("exact_match_config",)
    EXACT_MATCH_CONFIG_FIELD_NUMBER: _ClassVar[int]
    exact_match_config: ExactMatchConfig
    def __init__(self, exact_match_config: _Optional[_Union[ExactMatchConfig, _Mapping]] = ...) -> None: ...

class ExactMatchConfig(_message.Message):
    __slots__ = ("case_sensitive",)
    CASE_SENSITIVE_FIELD_NUMBER: _ClassVar[int]
    case_sensitive: bool
    def __init__(self, case_sensitive: bool = ...) -> None: ...

class Settings(_message.Message):
    __slots__ = ("name", "create_time", "update_time", "language_code", "conversation_ttl", "pubsub_notification_settings", "analysis_config", "redaction_config", "speech_config")
    class AnalysisConfig(_message.Message):
        __slots__ = ("runtime_integration_analysis_percentage", "upload_conversation_analysis_percentage", "annotator_selector")
        RUNTIME_INTEGRATION_ANALYSIS_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
        UPLOAD_CONVERSATION_ANALYSIS_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
        ANNOTATOR_SELECTOR_FIELD_NUMBER: _ClassVar[int]
        runtime_integration_analysis_percentage: float
        upload_conversation_analysis_percentage: float
        annotator_selector: AnnotatorSelector
        def __init__(self, runtime_integration_analysis_percentage: _Optional[float] = ..., upload_conversation_analysis_percentage: _Optional[float] = ..., annotator_selector: _Optional[_Union[AnnotatorSelector, _Mapping]] = ...) -> None: ...
    class PubsubNotificationSettingsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_TTL_FIELD_NUMBER: _ClassVar[int]
    PUBSUB_NOTIFICATION_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    ANALYSIS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    REDACTION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    SPEECH_CONFIG_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    language_code: str
    conversation_ttl: _duration_pb2.Duration
    pubsub_notification_settings: _containers.ScalarMap[str, str]
    analysis_config: Settings.AnalysisConfig
    redaction_config: RedactionConfig
    speech_config: SpeechConfig
    def __init__(self, name: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., language_code: _Optional[str] = ..., conversation_ttl: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., pubsub_notification_settings: _Optional[_Mapping[str, str]] = ..., analysis_config: _Optional[_Union[Settings.AnalysisConfig, _Mapping]] = ..., redaction_config: _Optional[_Union[RedactionConfig, _Mapping]] = ..., speech_config: _Optional[_Union[SpeechConfig, _Mapping]] = ...) -> None: ...

class AnalysisRule(_message.Message):
    __slots__ = ("name", "create_time", "update_time", "display_name", "conversation_filter", "annotator_selector", "analysis_percentage", "active")
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_FILTER_FIELD_NUMBER: _ClassVar[int]
    ANNOTATOR_SELECTOR_FIELD_NUMBER: _ClassVar[int]
    ANALYSIS_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    display_name: str
    conversation_filter: str
    annotator_selector: AnnotatorSelector
    analysis_percentage: float
    active: bool
    def __init__(self, name: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., display_name: _Optional[str] = ..., conversation_filter: _Optional[str] = ..., annotator_selector: _Optional[_Union[AnnotatorSelector, _Mapping]] = ..., analysis_percentage: _Optional[float] = ..., active: bool = ...) -> None: ...

class EncryptionSpec(_message.Message):
    __slots__ = ("name", "kms_key")
    NAME_FIELD_NUMBER: _ClassVar[int]
    KMS_KEY_FIELD_NUMBER: _ClassVar[int]
    name: str
    kms_key: str
    def __init__(self, name: _Optional[str] = ..., kms_key: _Optional[str] = ...) -> None: ...

class RedactionConfig(_message.Message):
    __slots__ = ("deidentify_template", "inspect_template")
    DEIDENTIFY_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    INSPECT_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    deidentify_template: str
    inspect_template: str
    def __init__(self, deidentify_template: _Optional[str] = ..., inspect_template: _Optional[str] = ...) -> None: ...

class SpeechConfig(_message.Message):
    __slots__ = ("speech_recognizer",)
    SPEECH_RECOGNIZER_FIELD_NUMBER: _ClassVar[int]
    speech_recognizer: str
    def __init__(self, speech_recognizer: _Optional[str] = ...) -> None: ...

class RuntimeAnnotation(_message.Message):
    __slots__ = ("article_suggestion", "faq_answer", "smart_reply", "smart_compose_suggestion", "dialogflow_interaction", "conversation_summarization_suggestion", "annotation_id", "create_time", "start_boundary", "end_boundary", "answer_feedback", "user_input")
    class UserInput(_message.Message):
        __slots__ = ("query", "generator_name", "query_source")
        class QuerySource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            QUERY_SOURCE_UNSPECIFIED: _ClassVar[RuntimeAnnotation.UserInput.QuerySource]
            AGENT_QUERY: _ClassVar[RuntimeAnnotation.UserInput.QuerySource]
            SUGGESTED_QUERY: _ClassVar[RuntimeAnnotation.UserInput.QuerySource]
        QUERY_SOURCE_UNSPECIFIED: RuntimeAnnotation.UserInput.QuerySource
        AGENT_QUERY: RuntimeAnnotation.UserInput.QuerySource
        SUGGESTED_QUERY: RuntimeAnnotation.UserInput.QuerySource
        QUERY_FIELD_NUMBER: _ClassVar[int]
        GENERATOR_NAME_FIELD_NUMBER: _ClassVar[int]
        QUERY_SOURCE_FIELD_NUMBER: _ClassVar[int]
        query: str
        generator_name: str
        query_source: RuntimeAnnotation.UserInput.QuerySource
        def __init__(self, query: _Optional[str] = ..., generator_name: _Optional[str] = ..., query_source: _Optional[_Union[RuntimeAnnotation.UserInput.QuerySource, str]] = ...) -> None: ...
    ARTICLE_SUGGESTION_FIELD_NUMBER: _ClassVar[int]
    FAQ_ANSWER_FIELD_NUMBER: _ClassVar[int]
    SMART_REPLY_FIELD_NUMBER: _ClassVar[int]
    SMART_COMPOSE_SUGGESTION_FIELD_NUMBER: _ClassVar[int]
    DIALOGFLOW_INTERACTION_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_SUMMARIZATION_SUGGESTION_FIELD_NUMBER: _ClassVar[int]
    ANNOTATION_ID_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    START_BOUNDARY_FIELD_NUMBER: _ClassVar[int]
    END_BOUNDARY_FIELD_NUMBER: _ClassVar[int]
    ANSWER_FEEDBACK_FIELD_NUMBER: _ClassVar[int]
    USER_INPUT_FIELD_NUMBER: _ClassVar[int]
    article_suggestion: ArticleSuggestionData
    faq_answer: FaqAnswerData
    smart_reply: SmartReplyData
    smart_compose_suggestion: SmartComposeSuggestionData
    dialogflow_interaction: DialogflowInteractionData
    conversation_summarization_suggestion: ConversationSummarizationSuggestionData
    annotation_id: str
    create_time: _timestamp_pb2.Timestamp
    start_boundary: AnnotationBoundary
    end_boundary: AnnotationBoundary
    answer_feedback: AnswerFeedback
    user_input: RuntimeAnnotation.UserInput
    def __init__(self, article_suggestion: _Optional[_Union[ArticleSuggestionData, _Mapping]] = ..., faq_answer: _Optional[_Union[FaqAnswerData, _Mapping]] = ..., smart_reply: _Optional[_Union[SmartReplyData, _Mapping]] = ..., smart_compose_suggestion: _Optional[_Union[SmartComposeSuggestionData, _Mapping]] = ..., dialogflow_interaction: _Optional[_Union[DialogflowInteractionData, _Mapping]] = ..., conversation_summarization_suggestion: _Optional[_Union[ConversationSummarizationSuggestionData, _Mapping]] = ..., annotation_id: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., start_boundary: _Optional[_Union[AnnotationBoundary, _Mapping]] = ..., end_boundary: _Optional[_Union[AnnotationBoundary, _Mapping]] = ..., answer_feedback: _Optional[_Union[AnswerFeedback, _Mapping]] = ..., user_input: _Optional[_Union[RuntimeAnnotation.UserInput, _Mapping]] = ...) -> None: ...

class AnswerFeedback(_message.Message):
    __slots__ = ("correctness_level", "clicked", "displayed")
    class CorrectnessLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CORRECTNESS_LEVEL_UNSPECIFIED: _ClassVar[AnswerFeedback.CorrectnessLevel]
        NOT_CORRECT: _ClassVar[AnswerFeedback.CorrectnessLevel]
        PARTIALLY_CORRECT: _ClassVar[AnswerFeedback.CorrectnessLevel]
        FULLY_CORRECT: _ClassVar[AnswerFeedback.CorrectnessLevel]
    CORRECTNESS_LEVEL_UNSPECIFIED: AnswerFeedback.CorrectnessLevel
    NOT_CORRECT: AnswerFeedback.CorrectnessLevel
    PARTIALLY_CORRECT: AnswerFeedback.CorrectnessLevel
    FULLY_CORRECT: AnswerFeedback.CorrectnessLevel
    CORRECTNESS_LEVEL_FIELD_NUMBER: _ClassVar[int]
    CLICKED_FIELD_NUMBER: _ClassVar[int]
    DISPLAYED_FIELD_NUMBER: _ClassVar[int]
    correctness_level: AnswerFeedback.CorrectnessLevel
    clicked: bool
    displayed: bool
    def __init__(self, correctness_level: _Optional[_Union[AnswerFeedback.CorrectnessLevel, str]] = ..., clicked: bool = ..., displayed: bool = ...) -> None: ...

class ArticleSuggestionData(_message.Message):
    __slots__ = ("title", "uri", "confidence_score", "metadata", "query_record", "source")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    TITLE_FIELD_NUMBER: _ClassVar[int]
    URI_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_SCORE_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    QUERY_RECORD_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    title: str
    uri: str
    confidence_score: float
    metadata: _containers.ScalarMap[str, str]
    query_record: str
    source: str
    def __init__(self, title: _Optional[str] = ..., uri: _Optional[str] = ..., confidence_score: _Optional[float] = ..., metadata: _Optional[_Mapping[str, str]] = ..., query_record: _Optional[str] = ..., source: _Optional[str] = ...) -> None: ...

class FaqAnswerData(_message.Message):
    __slots__ = ("answer", "confidence_score", "question", "metadata", "query_record", "source")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ANSWER_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_SCORE_FIELD_NUMBER: _ClassVar[int]
    QUESTION_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    QUERY_RECORD_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    answer: str
    confidence_score: float
    question: str
    metadata: _containers.ScalarMap[str, str]
    query_record: str
    source: str
    def __init__(self, answer: _Optional[str] = ..., confidence_score: _Optional[float] = ..., question: _Optional[str] = ..., metadata: _Optional[_Mapping[str, str]] = ..., query_record: _Optional[str] = ..., source: _Optional[str] = ...) -> None: ...

class SmartReplyData(_message.Message):
    __slots__ = ("reply", "confidence_score", "metadata", "query_record")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    REPLY_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_SCORE_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    QUERY_RECORD_FIELD_NUMBER: _ClassVar[int]
    reply: str
    confidence_score: float
    metadata: _containers.ScalarMap[str, str]
    query_record: str
    def __init__(self, reply: _Optional[str] = ..., confidence_score: _Optional[float] = ..., metadata: _Optional[_Mapping[str, str]] = ..., query_record: _Optional[str] = ...) -> None: ...

class SmartComposeSuggestionData(_message.Message):
    __slots__ = ("suggestion", "confidence_score", "metadata", "query_record")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    SUGGESTION_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_SCORE_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    QUERY_RECORD_FIELD_NUMBER: _ClassVar[int]
    suggestion: str
    confidence_score: float
    metadata: _containers.ScalarMap[str, str]
    query_record: str
    def __init__(self, suggestion: _Optional[str] = ..., confidence_score: _Optional[float] = ..., metadata: _Optional[_Mapping[str, str]] = ..., query_record: _Optional[str] = ...) -> None: ...

class DialogflowInteractionData(_message.Message):
    __slots__ = ("dialogflow_intent_id", "confidence")
    DIALOGFLOW_INTENT_ID_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    dialogflow_intent_id: str
    confidence: float
    def __init__(self, dialogflow_intent_id: _Optional[str] = ..., confidence: _Optional[float] = ...) -> None: ...

class ConversationSummarizationSuggestionData(_message.Message):
    __slots__ = ("text", "text_sections", "confidence", "metadata", "answer_record", "conversation_model")
    class TextSectionsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    TEXT_FIELD_NUMBER: _ClassVar[int]
    TEXT_SECTIONS_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    ANSWER_RECORD_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_MODEL_FIELD_NUMBER: _ClassVar[int]
    text: str
    text_sections: _containers.ScalarMap[str, str]
    confidence: float
    metadata: _containers.ScalarMap[str, str]
    answer_record: str
    conversation_model: str
    def __init__(self, text: _Optional[str] = ..., text_sections: _Optional[_Mapping[str, str]] = ..., confidence: _Optional[float] = ..., metadata: _Optional[_Mapping[str, str]] = ..., answer_record: _Optional[str] = ..., conversation_model: _Optional[str] = ...) -> None: ...

class ConversationParticipant(_message.Message):
    __slots__ = ("dialogflow_participant_name", "user_id", "dialogflow_participant", "obfuscated_external_user_id", "role")
    class Role(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ROLE_UNSPECIFIED: _ClassVar[ConversationParticipant.Role]
        HUMAN_AGENT: _ClassVar[ConversationParticipant.Role]
        AUTOMATED_AGENT: _ClassVar[ConversationParticipant.Role]
        END_USER: _ClassVar[ConversationParticipant.Role]
        ANY_AGENT: _ClassVar[ConversationParticipant.Role]
    ROLE_UNSPECIFIED: ConversationParticipant.Role
    HUMAN_AGENT: ConversationParticipant.Role
    AUTOMATED_AGENT: ConversationParticipant.Role
    END_USER: ConversationParticipant.Role
    ANY_AGENT: ConversationParticipant.Role
    DIALOGFLOW_PARTICIPANT_NAME_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    DIALOGFLOW_PARTICIPANT_FIELD_NUMBER: _ClassVar[int]
    OBFUSCATED_EXTERNAL_USER_ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    dialogflow_participant_name: str
    user_id: str
    dialogflow_participant: str
    obfuscated_external_user_id: str
    role: ConversationParticipant.Role
    def __init__(self, dialogflow_participant_name: _Optional[str] = ..., user_id: _Optional[str] = ..., dialogflow_participant: _Optional[str] = ..., obfuscated_external_user_id: _Optional[str] = ..., role: _Optional[_Union[ConversationParticipant.Role, str]] = ...) -> None: ...

class View(_message.Message):
    __slots__ = ("name", "display_name", "create_time", "update_time", "value")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    value: str
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., value: _Optional[str] = ...) -> None: ...

class AnnotatorSelector(_message.Message):
    __slots__ = ("run_interruption_annotator", "run_silence_annotator", "run_phrase_matcher_annotator", "phrase_matchers", "run_sentiment_annotator", "run_entity_annotator", "run_intent_annotator", "run_issue_model_annotator", "issue_models", "run_summarization_annotator", "summarization_config", "run_qa_annotator", "qa_config")
    class SummarizationConfig(_message.Message):
        __slots__ = ("conversation_profile", "summarization_model")
        class SummarizationModel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            SUMMARIZATION_MODEL_UNSPECIFIED: _ClassVar[AnnotatorSelector.SummarizationConfig.SummarizationModel]
            BASELINE_MODEL: _ClassVar[AnnotatorSelector.SummarizationConfig.SummarizationModel]
            BASELINE_MODEL_V2_0: _ClassVar[AnnotatorSelector.SummarizationConfig.SummarizationModel]
        SUMMARIZATION_MODEL_UNSPECIFIED: AnnotatorSelector.SummarizationConfig.SummarizationModel
        BASELINE_MODEL: AnnotatorSelector.SummarizationConfig.SummarizationModel
        BASELINE_MODEL_V2_0: AnnotatorSelector.SummarizationConfig.SummarizationModel
        CONVERSATION_PROFILE_FIELD_NUMBER: _ClassVar[int]
        SUMMARIZATION_MODEL_FIELD_NUMBER: _ClassVar[int]
        conversation_profile: str
        summarization_model: AnnotatorSelector.SummarizationConfig.SummarizationModel
        def __init__(self, conversation_profile: _Optional[str] = ..., summarization_model: _Optional[_Union[AnnotatorSelector.SummarizationConfig.SummarizationModel, str]] = ...) -> None: ...
    class QaConfig(_message.Message):
        __slots__ = ("scorecard_list",)
        class ScorecardList(_message.Message):
            __slots__ = ("qa_scorecard_revisions",)
            QA_SCORECARD_REVISIONS_FIELD_NUMBER: _ClassVar[int]
            qa_scorecard_revisions: _containers.RepeatedScalarFieldContainer[str]
            def __init__(self, qa_scorecard_revisions: _Optional[_Iterable[str]] = ...) -> None: ...
        SCORECARD_LIST_FIELD_NUMBER: _ClassVar[int]
        scorecard_list: AnnotatorSelector.QaConfig.ScorecardList
        def __init__(self, scorecard_list: _Optional[_Union[AnnotatorSelector.QaConfig.ScorecardList, _Mapping]] = ...) -> None: ...
    RUN_INTERRUPTION_ANNOTATOR_FIELD_NUMBER: _ClassVar[int]
    RUN_SILENCE_ANNOTATOR_FIELD_NUMBER: _ClassVar[int]
    RUN_PHRASE_MATCHER_ANNOTATOR_FIELD_NUMBER: _ClassVar[int]
    PHRASE_MATCHERS_FIELD_NUMBER: _ClassVar[int]
    RUN_SENTIMENT_ANNOTATOR_FIELD_NUMBER: _ClassVar[int]
    RUN_ENTITY_ANNOTATOR_FIELD_NUMBER: _ClassVar[int]
    RUN_INTENT_ANNOTATOR_FIELD_NUMBER: _ClassVar[int]
    RUN_ISSUE_MODEL_ANNOTATOR_FIELD_NUMBER: _ClassVar[int]
    ISSUE_MODELS_FIELD_NUMBER: _ClassVar[int]
    RUN_SUMMARIZATION_ANNOTATOR_FIELD_NUMBER: _ClassVar[int]
    SUMMARIZATION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    RUN_QA_ANNOTATOR_FIELD_NUMBER: _ClassVar[int]
    QA_CONFIG_FIELD_NUMBER: _ClassVar[int]
    run_interruption_annotator: bool
    run_silence_annotator: bool
    run_phrase_matcher_annotator: bool
    phrase_matchers: _containers.RepeatedScalarFieldContainer[str]
    run_sentiment_annotator: bool
    run_entity_annotator: bool
    run_intent_annotator: bool
    run_issue_model_annotator: bool
    issue_models: _containers.RepeatedScalarFieldContainer[str]
    run_summarization_annotator: bool
    summarization_config: AnnotatorSelector.SummarizationConfig
    run_qa_annotator: bool
    qa_config: AnnotatorSelector.QaConfig
    def __init__(self, run_interruption_annotator: bool = ..., run_silence_annotator: bool = ..., run_phrase_matcher_annotator: bool = ..., phrase_matchers: _Optional[_Iterable[str]] = ..., run_sentiment_annotator: bool = ..., run_entity_annotator: bool = ..., run_intent_annotator: bool = ..., run_issue_model_annotator: bool = ..., issue_models: _Optional[_Iterable[str]] = ..., run_summarization_annotator: bool = ..., summarization_config: _Optional[_Union[AnnotatorSelector.SummarizationConfig, _Mapping]] = ..., run_qa_annotator: bool = ..., qa_config: _Optional[_Union[AnnotatorSelector.QaConfig, _Mapping]] = ...) -> None: ...

class QaQuestion(_message.Message):
    __slots__ = ("name", "abbreviation", "create_time", "update_time", "question_body", "answer_instructions", "answer_choices", "tags", "order", "metrics", "tuning_metadata")
    class AnswerChoice(_message.Message):
        __slots__ = ("str_value", "num_value", "bool_value", "na_value", "key", "score")
        STR_VALUE_FIELD_NUMBER: _ClassVar[int]
        NUM_VALUE_FIELD_NUMBER: _ClassVar[int]
        BOOL_VALUE_FIELD_NUMBER: _ClassVar[int]
        NA_VALUE_FIELD_NUMBER: _ClassVar[int]
        KEY_FIELD_NUMBER: _ClassVar[int]
        SCORE_FIELD_NUMBER: _ClassVar[int]
        str_value: str
        num_value: float
        bool_value: bool
        na_value: bool
        key: str
        score: float
        def __init__(self, str_value: _Optional[str] = ..., num_value: _Optional[float] = ..., bool_value: bool = ..., na_value: bool = ..., key: _Optional[str] = ..., score: _Optional[float] = ...) -> None: ...
    class Metrics(_message.Message):
        __slots__ = ("accuracy",)
        ACCURACY_FIELD_NUMBER: _ClassVar[int]
        accuracy: float
        def __init__(self, accuracy: _Optional[float] = ...) -> None: ...
    class TuningMetadata(_message.Message):
        __slots__ = ("total_valid_label_count", "dataset_validation_warnings", "tuning_error")
        TOTAL_VALID_LABEL_COUNT_FIELD_NUMBER: _ClassVar[int]
        DATASET_VALIDATION_WARNINGS_FIELD_NUMBER: _ClassVar[int]
        TUNING_ERROR_FIELD_NUMBER: _ClassVar[int]
        total_valid_label_count: int
        dataset_validation_warnings: _containers.RepeatedScalarFieldContainer[DatasetValidationWarning]
        tuning_error: str
        def __init__(self, total_valid_label_count: _Optional[int] = ..., dataset_validation_warnings: _Optional[_Iterable[_Union[DatasetValidationWarning, str]]] = ..., tuning_error: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    ABBREVIATION_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    QUESTION_BODY_FIELD_NUMBER: _ClassVar[int]
    ANSWER_INSTRUCTIONS_FIELD_NUMBER: _ClassVar[int]
    ANSWER_CHOICES_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    METRICS_FIELD_NUMBER: _ClassVar[int]
    TUNING_METADATA_FIELD_NUMBER: _ClassVar[int]
    name: str
    abbreviation: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    question_body: str
    answer_instructions: str
    answer_choices: _containers.RepeatedCompositeFieldContainer[QaQuestion.AnswerChoice]
    tags: _containers.RepeatedScalarFieldContainer[str]
    order: int
    metrics: QaQuestion.Metrics
    tuning_metadata: QaQuestion.TuningMetadata
    def __init__(self, name: _Optional[str] = ..., abbreviation: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., question_body: _Optional[str] = ..., answer_instructions: _Optional[str] = ..., answer_choices: _Optional[_Iterable[_Union[QaQuestion.AnswerChoice, _Mapping]]] = ..., tags: _Optional[_Iterable[str]] = ..., order: _Optional[int] = ..., metrics: _Optional[_Union[QaQuestion.Metrics, _Mapping]] = ..., tuning_metadata: _Optional[_Union[QaQuestion.TuningMetadata, _Mapping]] = ...) -> None: ...

class QaScorecard(_message.Message):
    __slots__ = ("name", "display_name", "description", "create_time", "update_time")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    description: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., description: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class QaScorecardRevision(_message.Message):
    __slots__ = ("name", "snapshot", "create_time", "alternate_ids", "state")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[QaScorecardRevision.State]
        EDITABLE: _ClassVar[QaScorecardRevision.State]
        TRAINING: _ClassVar[QaScorecardRevision.State]
        TRAINING_FAILED: _ClassVar[QaScorecardRevision.State]
        READY: _ClassVar[QaScorecardRevision.State]
        DELETING: _ClassVar[QaScorecardRevision.State]
        TRAINING_CANCELLED: _ClassVar[QaScorecardRevision.State]
    STATE_UNSPECIFIED: QaScorecardRevision.State
    EDITABLE: QaScorecardRevision.State
    TRAINING: QaScorecardRevision.State
    TRAINING_FAILED: QaScorecardRevision.State
    READY: QaScorecardRevision.State
    DELETING: QaScorecardRevision.State
    TRAINING_CANCELLED: QaScorecardRevision.State
    NAME_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    ALTERNATE_IDS_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    name: str
    snapshot: QaScorecard
    create_time: _timestamp_pb2.Timestamp
    alternate_ids: _containers.RepeatedScalarFieldContainer[str]
    state: QaScorecardRevision.State
    def __init__(self, name: _Optional[str] = ..., snapshot: _Optional[_Union[QaScorecard, _Mapping]] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., alternate_ids: _Optional[_Iterable[str]] = ..., state: _Optional[_Union[QaScorecardRevision.State, str]] = ...) -> None: ...

class QaAnswer(_message.Message):
    __slots__ = ("qa_question", "conversation", "question_body", "answer_value", "tags", "answer_sources")
    class AnswerValue(_message.Message):
        __slots__ = ("str_value", "num_value", "bool_value", "na_value", "key", "score", "potential_score", "normalized_score")
        STR_VALUE_FIELD_NUMBER: _ClassVar[int]
        NUM_VALUE_FIELD_NUMBER: _ClassVar[int]
        BOOL_VALUE_FIELD_NUMBER: _ClassVar[int]
        NA_VALUE_FIELD_NUMBER: _ClassVar[int]
        KEY_FIELD_NUMBER: _ClassVar[int]
        SCORE_FIELD_NUMBER: _ClassVar[int]
        POTENTIAL_SCORE_FIELD_NUMBER: _ClassVar[int]
        NORMALIZED_SCORE_FIELD_NUMBER: _ClassVar[int]
        str_value: str
        num_value: float
        bool_value: bool
        na_value: bool
        key: str
        score: float
        potential_score: float
        normalized_score: float
        def __init__(self, str_value: _Optional[str] = ..., num_value: _Optional[float] = ..., bool_value: bool = ..., na_value: bool = ..., key: _Optional[str] = ..., score: _Optional[float] = ..., potential_score: _Optional[float] = ..., normalized_score: _Optional[float] = ...) -> None: ...
    class AnswerSource(_message.Message):
        __slots__ = ("source_type", "answer_value")
        class SourceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            SOURCE_TYPE_UNSPECIFIED: _ClassVar[QaAnswer.AnswerSource.SourceType]
            SYSTEM_GENERATED: _ClassVar[QaAnswer.AnswerSource.SourceType]
            MANUAL_EDIT: _ClassVar[QaAnswer.AnswerSource.SourceType]
        SOURCE_TYPE_UNSPECIFIED: QaAnswer.AnswerSource.SourceType
        SYSTEM_GENERATED: QaAnswer.AnswerSource.SourceType
        MANUAL_EDIT: QaAnswer.AnswerSource.SourceType
        SOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
        ANSWER_VALUE_FIELD_NUMBER: _ClassVar[int]
        source_type: QaAnswer.AnswerSource.SourceType
        answer_value: QaAnswer.AnswerValue
        def __init__(self, source_type: _Optional[_Union[QaAnswer.AnswerSource.SourceType, str]] = ..., answer_value: _Optional[_Union[QaAnswer.AnswerValue, _Mapping]] = ...) -> None: ...
    QA_QUESTION_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_FIELD_NUMBER: _ClassVar[int]
    QUESTION_BODY_FIELD_NUMBER: _ClassVar[int]
    ANSWER_VALUE_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    ANSWER_SOURCES_FIELD_NUMBER: _ClassVar[int]
    qa_question: str
    conversation: str
    question_body: str
    answer_value: QaAnswer.AnswerValue
    tags: _containers.RepeatedScalarFieldContainer[str]
    answer_sources: _containers.RepeatedCompositeFieldContainer[QaAnswer.AnswerSource]
    def __init__(self, qa_question: _Optional[str] = ..., conversation: _Optional[str] = ..., question_body: _Optional[str] = ..., answer_value: _Optional[_Union[QaAnswer.AnswerValue, _Mapping]] = ..., tags: _Optional[_Iterable[str]] = ..., answer_sources: _Optional[_Iterable[_Union[QaAnswer.AnswerSource, _Mapping]]] = ...) -> None: ...

class QaScorecardResult(_message.Message):
    __slots__ = ("name", "qa_scorecard_revision", "conversation", "create_time", "agent_id", "qa_answers", "score", "potential_score", "normalized_score", "qa_tag_results", "score_sources")
    class QaTagResult(_message.Message):
        __slots__ = ("tag", "score", "potential_score", "normalized_score")
        TAG_FIELD_NUMBER: _ClassVar[int]
        SCORE_FIELD_NUMBER: _ClassVar[int]
        POTENTIAL_SCORE_FIELD_NUMBER: _ClassVar[int]
        NORMALIZED_SCORE_FIELD_NUMBER: _ClassVar[int]
        tag: str
        score: float
        potential_score: float
        normalized_score: float
        def __init__(self, tag: _Optional[str] = ..., score: _Optional[float] = ..., potential_score: _Optional[float] = ..., normalized_score: _Optional[float] = ...) -> None: ...
    class ScoreSource(_message.Message):
        __slots__ = ("source_type", "score", "potential_score", "normalized_score", "qa_tag_results")
        class SourceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            SOURCE_TYPE_UNSPECIFIED: _ClassVar[QaScorecardResult.ScoreSource.SourceType]
            SYSTEM_GENERATED_ONLY: _ClassVar[QaScorecardResult.ScoreSource.SourceType]
            INCLUDES_MANUAL_EDITS: _ClassVar[QaScorecardResult.ScoreSource.SourceType]
        SOURCE_TYPE_UNSPECIFIED: QaScorecardResult.ScoreSource.SourceType
        SYSTEM_GENERATED_ONLY: QaScorecardResult.ScoreSource.SourceType
        INCLUDES_MANUAL_EDITS: QaScorecardResult.ScoreSource.SourceType
        SOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
        SCORE_FIELD_NUMBER: _ClassVar[int]
        POTENTIAL_SCORE_FIELD_NUMBER: _ClassVar[int]
        NORMALIZED_SCORE_FIELD_NUMBER: _ClassVar[int]
        QA_TAG_RESULTS_FIELD_NUMBER: _ClassVar[int]
        source_type: QaScorecardResult.ScoreSource.SourceType
        score: float
        potential_score: float
        normalized_score: float
        qa_tag_results: _containers.RepeatedCompositeFieldContainer[QaScorecardResult.QaTagResult]
        def __init__(self, source_type: _Optional[_Union[QaScorecardResult.ScoreSource.SourceType, str]] = ..., score: _Optional[float] = ..., potential_score: _Optional[float] = ..., normalized_score: _Optional[float] = ..., qa_tag_results: _Optional[_Iterable[_Union[QaScorecardResult.QaTagResult, _Mapping]]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    QA_SCORECARD_REVISION_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    QA_ANSWERS_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    POTENTIAL_SCORE_FIELD_NUMBER: _ClassVar[int]
    NORMALIZED_SCORE_FIELD_NUMBER: _ClassVar[int]
    QA_TAG_RESULTS_FIELD_NUMBER: _ClassVar[int]
    SCORE_SOURCES_FIELD_NUMBER: _ClassVar[int]
    name: str
    qa_scorecard_revision: str
    conversation: str
    create_time: _timestamp_pb2.Timestamp
    agent_id: str
    qa_answers: _containers.RepeatedCompositeFieldContainer[QaAnswer]
    score: float
    potential_score: float
    normalized_score: float
    qa_tag_results: _containers.RepeatedCompositeFieldContainer[QaScorecardResult.QaTagResult]
    score_sources: _containers.RepeatedCompositeFieldContainer[QaScorecardResult.ScoreSource]
    def __init__(self, name: _Optional[str] = ..., qa_scorecard_revision: _Optional[str] = ..., conversation: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., agent_id: _Optional[str] = ..., qa_answers: _Optional[_Iterable[_Union[QaAnswer, _Mapping]]] = ..., score: _Optional[float] = ..., potential_score: _Optional[float] = ..., normalized_score: _Optional[float] = ..., qa_tag_results: _Optional[_Iterable[_Union[QaScorecardResult.QaTagResult, _Mapping]]] = ..., score_sources: _Optional[_Iterable[_Union[QaScorecardResult.ScoreSource, _Mapping]]] = ...) -> None: ...
