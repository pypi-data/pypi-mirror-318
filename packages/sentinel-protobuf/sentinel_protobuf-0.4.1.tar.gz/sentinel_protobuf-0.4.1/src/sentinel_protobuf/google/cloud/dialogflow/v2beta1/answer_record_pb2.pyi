from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.dialogflow.v2beta1 import participant_pb2 as _participant_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class AnswerRecord(_message.Message):
    __slots__ = ('name', 'answer_feedback', 'agent_assistant_record')
    NAME_FIELD_NUMBER: _ClassVar[int]
    ANSWER_FEEDBACK_FIELD_NUMBER: _ClassVar[int]
    AGENT_ASSISTANT_RECORD_FIELD_NUMBER: _ClassVar[int]
    name: str
    answer_feedback: AnswerFeedback
    agent_assistant_record: AgentAssistantRecord

    def __init__(self, name: _Optional[str]=..., answer_feedback: _Optional[_Union[AnswerFeedback, _Mapping]]=..., agent_assistant_record: _Optional[_Union[AgentAssistantRecord, _Mapping]]=...) -> None:
        ...

class AgentAssistantRecord(_message.Message):
    __slots__ = ('article_suggestion_answer', 'faq_answer', 'dialogflow_assist_answer')
    ARTICLE_SUGGESTION_ANSWER_FIELD_NUMBER: _ClassVar[int]
    FAQ_ANSWER_FIELD_NUMBER: _ClassVar[int]
    DIALOGFLOW_ASSIST_ANSWER_FIELD_NUMBER: _ClassVar[int]
    article_suggestion_answer: _participant_pb2.ArticleAnswer
    faq_answer: _participant_pb2.FaqAnswer
    dialogflow_assist_answer: _participant_pb2.DialogflowAssistAnswer

    def __init__(self, article_suggestion_answer: _Optional[_Union[_participant_pb2.ArticleAnswer, _Mapping]]=..., faq_answer: _Optional[_Union[_participant_pb2.FaqAnswer, _Mapping]]=..., dialogflow_assist_answer: _Optional[_Union[_participant_pb2.DialogflowAssistAnswer, _Mapping]]=...) -> None:
        ...

class AnswerFeedback(_message.Message):
    __slots__ = ('correctness_level', 'agent_assistant_detail_feedback', 'clicked', 'click_time', 'displayed', 'display_time')

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
    AGENT_ASSISTANT_DETAIL_FEEDBACK_FIELD_NUMBER: _ClassVar[int]
    CLICKED_FIELD_NUMBER: _ClassVar[int]
    CLICK_TIME_FIELD_NUMBER: _ClassVar[int]
    DISPLAYED_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_TIME_FIELD_NUMBER: _ClassVar[int]
    correctness_level: AnswerFeedback.CorrectnessLevel
    agent_assistant_detail_feedback: AgentAssistantFeedback
    clicked: bool
    click_time: _timestamp_pb2.Timestamp
    displayed: bool
    display_time: _timestamp_pb2.Timestamp

    def __init__(self, correctness_level: _Optional[_Union[AnswerFeedback.CorrectnessLevel, str]]=..., agent_assistant_detail_feedback: _Optional[_Union[AgentAssistantFeedback, _Mapping]]=..., clicked: bool=..., click_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., displayed: bool=..., display_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class AgentAssistantFeedback(_message.Message):
    __slots__ = ('answer_relevance', 'document_correctness', 'document_efficiency', 'summarization_feedback', 'knowledge_search_feedback', 'knowledge_assist_feedback')

    class AnswerRelevance(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ANSWER_RELEVANCE_UNSPECIFIED: _ClassVar[AgentAssistantFeedback.AnswerRelevance]
        IRRELEVANT: _ClassVar[AgentAssistantFeedback.AnswerRelevance]
        RELEVANT: _ClassVar[AgentAssistantFeedback.AnswerRelevance]
    ANSWER_RELEVANCE_UNSPECIFIED: AgentAssistantFeedback.AnswerRelevance
    IRRELEVANT: AgentAssistantFeedback.AnswerRelevance
    RELEVANT: AgentAssistantFeedback.AnswerRelevance

    class DocumentCorrectness(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DOCUMENT_CORRECTNESS_UNSPECIFIED: _ClassVar[AgentAssistantFeedback.DocumentCorrectness]
        INCORRECT: _ClassVar[AgentAssistantFeedback.DocumentCorrectness]
        CORRECT: _ClassVar[AgentAssistantFeedback.DocumentCorrectness]
    DOCUMENT_CORRECTNESS_UNSPECIFIED: AgentAssistantFeedback.DocumentCorrectness
    INCORRECT: AgentAssistantFeedback.DocumentCorrectness
    CORRECT: AgentAssistantFeedback.DocumentCorrectness

    class DocumentEfficiency(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DOCUMENT_EFFICIENCY_UNSPECIFIED: _ClassVar[AgentAssistantFeedback.DocumentEfficiency]
        INEFFICIENT: _ClassVar[AgentAssistantFeedback.DocumentEfficiency]
        EFFICIENT: _ClassVar[AgentAssistantFeedback.DocumentEfficiency]
    DOCUMENT_EFFICIENCY_UNSPECIFIED: AgentAssistantFeedback.DocumentEfficiency
    INEFFICIENT: AgentAssistantFeedback.DocumentEfficiency
    EFFICIENT: AgentAssistantFeedback.DocumentEfficiency

    class SummarizationFeedback(_message.Message):
        __slots__ = ('start_timestamp', 'submit_timestamp', 'summary_text', 'text_sections')

        class TextSectionsEntry(_message.Message):
            __slots__ = ('key', 'value')
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str

            def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
                ...
        START_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        SUBMIT_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        SUMMARY_TEXT_FIELD_NUMBER: _ClassVar[int]
        TEXT_SECTIONS_FIELD_NUMBER: _ClassVar[int]
        start_timestamp: _timestamp_pb2.Timestamp
        submit_timestamp: _timestamp_pb2.Timestamp
        summary_text: str
        text_sections: _containers.ScalarMap[str, str]

        def __init__(self, start_timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., submit_timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., summary_text: _Optional[str]=..., text_sections: _Optional[_Mapping[str, str]]=...) -> None:
            ...

    class KnowledgeSearchFeedback(_message.Message):
        __slots__ = ('answer_copied', 'clicked_uris')
        ANSWER_COPIED_FIELD_NUMBER: _ClassVar[int]
        CLICKED_URIS_FIELD_NUMBER: _ClassVar[int]
        answer_copied: bool
        clicked_uris: _containers.RepeatedScalarFieldContainer[str]

        def __init__(self, answer_copied: bool=..., clicked_uris: _Optional[_Iterable[str]]=...) -> None:
            ...

    class KnowledgeAssistFeedback(_message.Message):
        __slots__ = ('answer_copied', 'clicked_uris')
        ANSWER_COPIED_FIELD_NUMBER: _ClassVar[int]
        CLICKED_URIS_FIELD_NUMBER: _ClassVar[int]
        answer_copied: bool
        clicked_uris: _containers.RepeatedScalarFieldContainer[str]

        def __init__(self, answer_copied: bool=..., clicked_uris: _Optional[_Iterable[str]]=...) -> None:
            ...
    ANSWER_RELEVANCE_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_CORRECTNESS_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_EFFICIENCY_FIELD_NUMBER: _ClassVar[int]
    SUMMARIZATION_FEEDBACK_FIELD_NUMBER: _ClassVar[int]
    KNOWLEDGE_SEARCH_FEEDBACK_FIELD_NUMBER: _ClassVar[int]
    KNOWLEDGE_ASSIST_FEEDBACK_FIELD_NUMBER: _ClassVar[int]
    answer_relevance: AgentAssistantFeedback.AnswerRelevance
    document_correctness: AgentAssistantFeedback.DocumentCorrectness
    document_efficiency: AgentAssistantFeedback.DocumentEfficiency
    summarization_feedback: AgentAssistantFeedback.SummarizationFeedback
    knowledge_search_feedback: AgentAssistantFeedback.KnowledgeSearchFeedback
    knowledge_assist_feedback: AgentAssistantFeedback.KnowledgeAssistFeedback

    def __init__(self, answer_relevance: _Optional[_Union[AgentAssistantFeedback.AnswerRelevance, str]]=..., document_correctness: _Optional[_Union[AgentAssistantFeedback.DocumentCorrectness, str]]=..., document_efficiency: _Optional[_Union[AgentAssistantFeedback.DocumentEfficiency, str]]=..., summarization_feedback: _Optional[_Union[AgentAssistantFeedback.SummarizationFeedback, _Mapping]]=..., knowledge_search_feedback: _Optional[_Union[AgentAssistantFeedback.KnowledgeSearchFeedback, _Mapping]]=..., knowledge_assist_feedback: _Optional[_Union[AgentAssistantFeedback.KnowledgeAssistFeedback, _Mapping]]=...) -> None:
        ...

class GetAnswerRecordRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListAnswerRecordsRequest(_message.Message):
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

class ListAnswerRecordsResponse(_message.Message):
    __slots__ = ('answer_records', 'next_page_token')
    ANSWER_RECORDS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    answer_records: _containers.RepeatedCompositeFieldContainer[AnswerRecord]
    next_page_token: str

    def __init__(self, answer_records: _Optional[_Iterable[_Union[AnswerRecord, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class UpdateAnswerRecordRequest(_message.Message):
    __slots__ = ('answer_record', 'update_mask')
    ANSWER_RECORD_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    answer_record: AnswerRecord
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, answer_record: _Optional[_Union[AnswerRecord, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...