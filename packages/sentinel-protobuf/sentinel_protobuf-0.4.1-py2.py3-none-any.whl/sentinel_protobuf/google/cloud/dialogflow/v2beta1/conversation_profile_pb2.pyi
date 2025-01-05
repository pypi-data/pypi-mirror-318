from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.dialogflow.v2beta1 import audio_config_pb2 as _audio_config_pb2
from google.cloud.dialogflow.v2beta1 import participant_pb2 as _participant_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ConversationProfile(_message.Message):
    __slots__ = ('name', 'display_name', 'create_time', 'update_time', 'automated_agent_config', 'human_agent_assistant_config', 'human_agent_handoff_config', 'notification_config', 'logging_config', 'new_message_event_notification_config', 'new_recognition_result_notification_config', 'stt_config', 'language_code', 'time_zone', 'security_settings', 'tts_config')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    AUTOMATED_AGENT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    HUMAN_AGENT_ASSISTANT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    HUMAN_AGENT_HANDOFF_CONFIG_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    LOGGING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    NEW_MESSAGE_EVENT_NOTIFICATION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    NEW_RECOGNITION_RESULT_NOTIFICATION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    STT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    SECURITY_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    TTS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    automated_agent_config: AutomatedAgentConfig
    human_agent_assistant_config: HumanAgentAssistantConfig
    human_agent_handoff_config: HumanAgentHandoffConfig
    notification_config: NotificationConfig
    logging_config: LoggingConfig
    new_message_event_notification_config: NotificationConfig
    new_recognition_result_notification_config: NotificationConfig
    stt_config: _audio_config_pb2.SpeechToTextConfig
    language_code: str
    time_zone: str
    security_settings: str
    tts_config: _audio_config_pb2.SynthesizeSpeechConfig

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., automated_agent_config: _Optional[_Union[AutomatedAgentConfig, _Mapping]]=..., human_agent_assistant_config: _Optional[_Union[HumanAgentAssistantConfig, _Mapping]]=..., human_agent_handoff_config: _Optional[_Union[HumanAgentHandoffConfig, _Mapping]]=..., notification_config: _Optional[_Union[NotificationConfig, _Mapping]]=..., logging_config: _Optional[_Union[LoggingConfig, _Mapping]]=..., new_message_event_notification_config: _Optional[_Union[NotificationConfig, _Mapping]]=..., new_recognition_result_notification_config: _Optional[_Union[NotificationConfig, _Mapping]]=..., stt_config: _Optional[_Union[_audio_config_pb2.SpeechToTextConfig, _Mapping]]=..., language_code: _Optional[str]=..., time_zone: _Optional[str]=..., security_settings: _Optional[str]=..., tts_config: _Optional[_Union[_audio_config_pb2.SynthesizeSpeechConfig, _Mapping]]=...) -> None:
        ...

class AutomatedAgentConfig(_message.Message):
    __slots__ = ('agent', 'session_ttl')
    AGENT_FIELD_NUMBER: _ClassVar[int]
    SESSION_TTL_FIELD_NUMBER: _ClassVar[int]
    agent: str
    session_ttl: _duration_pb2.Duration

    def __init__(self, agent: _Optional[str]=..., session_ttl: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=...) -> None:
        ...

class HumanAgentAssistantConfig(_message.Message):
    __slots__ = ('notification_config', 'human_agent_suggestion_config', 'end_user_suggestion_config', 'message_analysis_config')

    class SuggestionTriggerSettings(_message.Message):
        __slots__ = ('no_small_talk', 'only_end_user')
        NO_SMALL_TALK_FIELD_NUMBER: _ClassVar[int]
        ONLY_END_USER_FIELD_NUMBER: _ClassVar[int]
        no_small_talk: bool
        only_end_user: bool

        def __init__(self, no_small_talk: bool=..., only_end_user: bool=...) -> None:
            ...

    class SuggestionFeatureConfig(_message.Message):
        __slots__ = ('suggestion_feature', 'enable_event_based_suggestion', 'disable_agent_query_logging', 'enable_query_suggestion_when_no_answer', 'enable_conversation_augmented_query', 'enable_query_suggestion_only', 'suggestion_trigger_settings', 'query_config', 'conversation_model_config', 'conversation_process_config')
        SUGGESTION_FEATURE_FIELD_NUMBER: _ClassVar[int]
        ENABLE_EVENT_BASED_SUGGESTION_FIELD_NUMBER: _ClassVar[int]
        DISABLE_AGENT_QUERY_LOGGING_FIELD_NUMBER: _ClassVar[int]
        ENABLE_QUERY_SUGGESTION_WHEN_NO_ANSWER_FIELD_NUMBER: _ClassVar[int]
        ENABLE_CONVERSATION_AUGMENTED_QUERY_FIELD_NUMBER: _ClassVar[int]
        ENABLE_QUERY_SUGGESTION_ONLY_FIELD_NUMBER: _ClassVar[int]
        SUGGESTION_TRIGGER_SETTINGS_FIELD_NUMBER: _ClassVar[int]
        QUERY_CONFIG_FIELD_NUMBER: _ClassVar[int]
        CONVERSATION_MODEL_CONFIG_FIELD_NUMBER: _ClassVar[int]
        CONVERSATION_PROCESS_CONFIG_FIELD_NUMBER: _ClassVar[int]
        suggestion_feature: _participant_pb2.SuggestionFeature
        enable_event_based_suggestion: bool
        disable_agent_query_logging: bool
        enable_query_suggestion_when_no_answer: bool
        enable_conversation_augmented_query: bool
        enable_query_suggestion_only: bool
        suggestion_trigger_settings: HumanAgentAssistantConfig.SuggestionTriggerSettings
        query_config: HumanAgentAssistantConfig.SuggestionQueryConfig
        conversation_model_config: HumanAgentAssistantConfig.ConversationModelConfig
        conversation_process_config: HumanAgentAssistantConfig.ConversationProcessConfig

        def __init__(self, suggestion_feature: _Optional[_Union[_participant_pb2.SuggestionFeature, _Mapping]]=..., enable_event_based_suggestion: bool=..., disable_agent_query_logging: bool=..., enable_query_suggestion_when_no_answer: bool=..., enable_conversation_augmented_query: bool=..., enable_query_suggestion_only: bool=..., suggestion_trigger_settings: _Optional[_Union[HumanAgentAssistantConfig.SuggestionTriggerSettings, _Mapping]]=..., query_config: _Optional[_Union[HumanAgentAssistantConfig.SuggestionQueryConfig, _Mapping]]=..., conversation_model_config: _Optional[_Union[HumanAgentAssistantConfig.ConversationModelConfig, _Mapping]]=..., conversation_process_config: _Optional[_Union[HumanAgentAssistantConfig.ConversationProcessConfig, _Mapping]]=...) -> None:
            ...

    class SuggestionConfig(_message.Message):
        __slots__ = ('feature_configs', 'group_suggestion_responses', 'generators', 'disable_high_latency_features_sync_delivery')
        FEATURE_CONFIGS_FIELD_NUMBER: _ClassVar[int]
        GROUP_SUGGESTION_RESPONSES_FIELD_NUMBER: _ClassVar[int]
        GENERATORS_FIELD_NUMBER: _ClassVar[int]
        DISABLE_HIGH_LATENCY_FEATURES_SYNC_DELIVERY_FIELD_NUMBER: _ClassVar[int]
        feature_configs: _containers.RepeatedCompositeFieldContainer[HumanAgentAssistantConfig.SuggestionFeatureConfig]
        group_suggestion_responses: bool
        generators: _containers.RepeatedScalarFieldContainer[str]
        disable_high_latency_features_sync_delivery: bool

        def __init__(self, feature_configs: _Optional[_Iterable[_Union[HumanAgentAssistantConfig.SuggestionFeatureConfig, _Mapping]]]=..., group_suggestion_responses: bool=..., generators: _Optional[_Iterable[str]]=..., disable_high_latency_features_sync_delivery: bool=...) -> None:
            ...

    class SuggestionQueryConfig(_message.Message):
        __slots__ = ('knowledge_base_query_source', 'document_query_source', 'dialogflow_query_source', 'max_results', 'confidence_threshold', 'context_filter_settings', 'sections', 'context_size')

        class KnowledgeBaseQuerySource(_message.Message):
            __slots__ = ('knowledge_bases',)
            KNOWLEDGE_BASES_FIELD_NUMBER: _ClassVar[int]
            knowledge_bases: _containers.RepeatedScalarFieldContainer[str]

            def __init__(self, knowledge_bases: _Optional[_Iterable[str]]=...) -> None:
                ...

        class DocumentQuerySource(_message.Message):
            __slots__ = ('documents',)
            DOCUMENTS_FIELD_NUMBER: _ClassVar[int]
            documents: _containers.RepeatedScalarFieldContainer[str]

            def __init__(self, documents: _Optional[_Iterable[str]]=...) -> None:
                ...

        class DialogflowQuerySource(_message.Message):
            __slots__ = ('agent', 'human_agent_side_config')

            class HumanAgentSideConfig(_message.Message):
                __slots__ = ('agent',)
                AGENT_FIELD_NUMBER: _ClassVar[int]
                agent: str

                def __init__(self, agent: _Optional[str]=...) -> None:
                    ...
            AGENT_FIELD_NUMBER: _ClassVar[int]
            HUMAN_AGENT_SIDE_CONFIG_FIELD_NUMBER: _ClassVar[int]
            agent: str
            human_agent_side_config: HumanAgentAssistantConfig.SuggestionQueryConfig.DialogflowQuerySource.HumanAgentSideConfig

            def __init__(self, agent: _Optional[str]=..., human_agent_side_config: _Optional[_Union[HumanAgentAssistantConfig.SuggestionQueryConfig.DialogflowQuerySource.HumanAgentSideConfig, _Mapping]]=...) -> None:
                ...

        class ContextFilterSettings(_message.Message):
            __slots__ = ('drop_handoff_messages', 'drop_virtual_agent_messages', 'drop_ivr_messages')
            DROP_HANDOFF_MESSAGES_FIELD_NUMBER: _ClassVar[int]
            DROP_VIRTUAL_AGENT_MESSAGES_FIELD_NUMBER: _ClassVar[int]
            DROP_IVR_MESSAGES_FIELD_NUMBER: _ClassVar[int]
            drop_handoff_messages: bool
            drop_virtual_agent_messages: bool
            drop_ivr_messages: bool

            def __init__(self, drop_handoff_messages: bool=..., drop_virtual_agent_messages: bool=..., drop_ivr_messages: bool=...) -> None:
                ...

        class Sections(_message.Message):
            __slots__ = ('section_types',)

            class SectionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                SECTION_TYPE_UNSPECIFIED: _ClassVar[HumanAgentAssistantConfig.SuggestionQueryConfig.Sections.SectionType]
                SITUATION: _ClassVar[HumanAgentAssistantConfig.SuggestionQueryConfig.Sections.SectionType]
                ACTION: _ClassVar[HumanAgentAssistantConfig.SuggestionQueryConfig.Sections.SectionType]
                RESOLUTION: _ClassVar[HumanAgentAssistantConfig.SuggestionQueryConfig.Sections.SectionType]
                REASON_FOR_CANCELLATION: _ClassVar[HumanAgentAssistantConfig.SuggestionQueryConfig.Sections.SectionType]
                CUSTOMER_SATISFACTION: _ClassVar[HumanAgentAssistantConfig.SuggestionQueryConfig.Sections.SectionType]
                ENTITIES: _ClassVar[HumanAgentAssistantConfig.SuggestionQueryConfig.Sections.SectionType]
            SECTION_TYPE_UNSPECIFIED: HumanAgentAssistantConfig.SuggestionQueryConfig.Sections.SectionType
            SITUATION: HumanAgentAssistantConfig.SuggestionQueryConfig.Sections.SectionType
            ACTION: HumanAgentAssistantConfig.SuggestionQueryConfig.Sections.SectionType
            RESOLUTION: HumanAgentAssistantConfig.SuggestionQueryConfig.Sections.SectionType
            REASON_FOR_CANCELLATION: HumanAgentAssistantConfig.SuggestionQueryConfig.Sections.SectionType
            CUSTOMER_SATISFACTION: HumanAgentAssistantConfig.SuggestionQueryConfig.Sections.SectionType
            ENTITIES: HumanAgentAssistantConfig.SuggestionQueryConfig.Sections.SectionType
            SECTION_TYPES_FIELD_NUMBER: _ClassVar[int]
            section_types: _containers.RepeatedScalarFieldContainer[HumanAgentAssistantConfig.SuggestionQueryConfig.Sections.SectionType]

            def __init__(self, section_types: _Optional[_Iterable[_Union[HumanAgentAssistantConfig.SuggestionQueryConfig.Sections.SectionType, str]]]=...) -> None:
                ...
        KNOWLEDGE_BASE_QUERY_SOURCE_FIELD_NUMBER: _ClassVar[int]
        DOCUMENT_QUERY_SOURCE_FIELD_NUMBER: _ClassVar[int]
        DIALOGFLOW_QUERY_SOURCE_FIELD_NUMBER: _ClassVar[int]
        MAX_RESULTS_FIELD_NUMBER: _ClassVar[int]
        CONFIDENCE_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
        CONTEXT_FILTER_SETTINGS_FIELD_NUMBER: _ClassVar[int]
        SECTIONS_FIELD_NUMBER: _ClassVar[int]
        CONTEXT_SIZE_FIELD_NUMBER: _ClassVar[int]
        knowledge_base_query_source: HumanAgentAssistantConfig.SuggestionQueryConfig.KnowledgeBaseQuerySource
        document_query_source: HumanAgentAssistantConfig.SuggestionQueryConfig.DocumentQuerySource
        dialogflow_query_source: HumanAgentAssistantConfig.SuggestionQueryConfig.DialogflowQuerySource
        max_results: int
        confidence_threshold: float
        context_filter_settings: HumanAgentAssistantConfig.SuggestionQueryConfig.ContextFilterSettings
        sections: HumanAgentAssistantConfig.SuggestionQueryConfig.Sections
        context_size: int

        def __init__(self, knowledge_base_query_source: _Optional[_Union[HumanAgentAssistantConfig.SuggestionQueryConfig.KnowledgeBaseQuerySource, _Mapping]]=..., document_query_source: _Optional[_Union[HumanAgentAssistantConfig.SuggestionQueryConfig.DocumentQuerySource, _Mapping]]=..., dialogflow_query_source: _Optional[_Union[HumanAgentAssistantConfig.SuggestionQueryConfig.DialogflowQuerySource, _Mapping]]=..., max_results: _Optional[int]=..., confidence_threshold: _Optional[float]=..., context_filter_settings: _Optional[_Union[HumanAgentAssistantConfig.SuggestionQueryConfig.ContextFilterSettings, _Mapping]]=..., sections: _Optional[_Union[HumanAgentAssistantConfig.SuggestionQueryConfig.Sections, _Mapping]]=..., context_size: _Optional[int]=...) -> None:
            ...

    class ConversationModelConfig(_message.Message):
        __slots__ = ('model', 'baseline_model_version')
        MODEL_FIELD_NUMBER: _ClassVar[int]
        BASELINE_MODEL_VERSION_FIELD_NUMBER: _ClassVar[int]
        model: str
        baseline_model_version: str

        def __init__(self, model: _Optional[str]=..., baseline_model_version: _Optional[str]=...) -> None:
            ...

    class ConversationProcessConfig(_message.Message):
        __slots__ = ('recent_sentences_count',)
        RECENT_SENTENCES_COUNT_FIELD_NUMBER: _ClassVar[int]
        recent_sentences_count: int

        def __init__(self, recent_sentences_count: _Optional[int]=...) -> None:
            ...

    class MessageAnalysisConfig(_message.Message):
        __slots__ = ('enable_entity_extraction', 'enable_sentiment_analysis')
        ENABLE_ENTITY_EXTRACTION_FIELD_NUMBER: _ClassVar[int]
        ENABLE_SENTIMENT_ANALYSIS_FIELD_NUMBER: _ClassVar[int]
        enable_entity_extraction: bool
        enable_sentiment_analysis: bool

        def __init__(self, enable_entity_extraction: bool=..., enable_sentiment_analysis: bool=...) -> None:
            ...
    NOTIFICATION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    HUMAN_AGENT_SUGGESTION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    END_USER_SUGGESTION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ANALYSIS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    notification_config: NotificationConfig
    human_agent_suggestion_config: HumanAgentAssistantConfig.SuggestionConfig
    end_user_suggestion_config: HumanAgentAssistantConfig.SuggestionConfig
    message_analysis_config: HumanAgentAssistantConfig.MessageAnalysisConfig

    def __init__(self, notification_config: _Optional[_Union[NotificationConfig, _Mapping]]=..., human_agent_suggestion_config: _Optional[_Union[HumanAgentAssistantConfig.SuggestionConfig, _Mapping]]=..., end_user_suggestion_config: _Optional[_Union[HumanAgentAssistantConfig.SuggestionConfig, _Mapping]]=..., message_analysis_config: _Optional[_Union[HumanAgentAssistantConfig.MessageAnalysisConfig, _Mapping]]=...) -> None:
        ...

class HumanAgentHandoffConfig(_message.Message):
    __slots__ = ('live_person_config', 'salesforce_live_agent_config')

    class LivePersonConfig(_message.Message):
        __slots__ = ('account_number',)
        ACCOUNT_NUMBER_FIELD_NUMBER: _ClassVar[int]
        account_number: str

        def __init__(self, account_number: _Optional[str]=...) -> None:
            ...

    class SalesforceLiveAgentConfig(_message.Message):
        __slots__ = ('organization_id', 'deployment_id', 'button_id', 'endpoint_domain')
        ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
        DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
        BUTTON_ID_FIELD_NUMBER: _ClassVar[int]
        ENDPOINT_DOMAIN_FIELD_NUMBER: _ClassVar[int]
        organization_id: str
        deployment_id: str
        button_id: str
        endpoint_domain: str

        def __init__(self, organization_id: _Optional[str]=..., deployment_id: _Optional[str]=..., button_id: _Optional[str]=..., endpoint_domain: _Optional[str]=...) -> None:
            ...
    LIVE_PERSON_CONFIG_FIELD_NUMBER: _ClassVar[int]
    SALESFORCE_LIVE_AGENT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    live_person_config: HumanAgentHandoffConfig.LivePersonConfig
    salesforce_live_agent_config: HumanAgentHandoffConfig.SalesforceLiveAgentConfig

    def __init__(self, live_person_config: _Optional[_Union[HumanAgentHandoffConfig.LivePersonConfig, _Mapping]]=..., salesforce_live_agent_config: _Optional[_Union[HumanAgentHandoffConfig.SalesforceLiveAgentConfig, _Mapping]]=...) -> None:
        ...

class NotificationConfig(_message.Message):
    __slots__ = ('topic', 'message_format')

    class MessageFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MESSAGE_FORMAT_UNSPECIFIED: _ClassVar[NotificationConfig.MessageFormat]
        PROTO: _ClassVar[NotificationConfig.MessageFormat]
        JSON: _ClassVar[NotificationConfig.MessageFormat]
    MESSAGE_FORMAT_UNSPECIFIED: NotificationConfig.MessageFormat
    PROTO: NotificationConfig.MessageFormat
    JSON: NotificationConfig.MessageFormat
    TOPIC_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FORMAT_FIELD_NUMBER: _ClassVar[int]
    topic: str
    message_format: NotificationConfig.MessageFormat

    def __init__(self, topic: _Optional[str]=..., message_format: _Optional[_Union[NotificationConfig.MessageFormat, str]]=...) -> None:
        ...

class LoggingConfig(_message.Message):
    __slots__ = ('enable_stackdriver_logging',)
    ENABLE_STACKDRIVER_LOGGING_FIELD_NUMBER: _ClassVar[int]
    enable_stackdriver_logging: bool

    def __init__(self, enable_stackdriver_logging: bool=...) -> None:
        ...

class ListConversationProfilesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListConversationProfilesResponse(_message.Message):
    __slots__ = ('conversation_profiles', 'next_page_token')
    CONVERSATION_PROFILES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    conversation_profiles: _containers.RepeatedCompositeFieldContainer[ConversationProfile]
    next_page_token: str

    def __init__(self, conversation_profiles: _Optional[_Iterable[_Union[ConversationProfile, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetConversationProfileRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateConversationProfileRequest(_message.Message):
    __slots__ = ('parent', 'conversation_profile')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_PROFILE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    conversation_profile: ConversationProfile

    def __init__(self, parent: _Optional[str]=..., conversation_profile: _Optional[_Union[ConversationProfile, _Mapping]]=...) -> None:
        ...

class UpdateConversationProfileRequest(_message.Message):
    __slots__ = ('conversation_profile', 'update_mask')
    CONVERSATION_PROFILE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    conversation_profile: ConversationProfile
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, conversation_profile: _Optional[_Union[ConversationProfile, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteConversationProfileRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class SetSuggestionFeatureConfigRequest(_message.Message):
    __slots__ = ('conversation_profile', 'participant_role', 'suggestion_feature_config')
    CONVERSATION_PROFILE_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_ROLE_FIELD_NUMBER: _ClassVar[int]
    SUGGESTION_FEATURE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    conversation_profile: str
    participant_role: _participant_pb2.Participant.Role
    suggestion_feature_config: HumanAgentAssistantConfig.SuggestionFeatureConfig

    def __init__(self, conversation_profile: _Optional[str]=..., participant_role: _Optional[_Union[_participant_pb2.Participant.Role, str]]=..., suggestion_feature_config: _Optional[_Union[HumanAgentAssistantConfig.SuggestionFeatureConfig, _Mapping]]=...) -> None:
        ...

class ClearSuggestionFeatureConfigRequest(_message.Message):
    __slots__ = ('conversation_profile', 'participant_role', 'suggestion_feature_type')
    CONVERSATION_PROFILE_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_ROLE_FIELD_NUMBER: _ClassVar[int]
    SUGGESTION_FEATURE_TYPE_FIELD_NUMBER: _ClassVar[int]
    conversation_profile: str
    participant_role: _participant_pb2.Participant.Role
    suggestion_feature_type: _participant_pb2.SuggestionFeature.Type

    def __init__(self, conversation_profile: _Optional[str]=..., participant_role: _Optional[_Union[_participant_pb2.Participant.Role, str]]=..., suggestion_feature_type: _Optional[_Union[_participant_pb2.SuggestionFeature.Type, str]]=...) -> None:
        ...

class SetSuggestionFeatureConfigOperationMetadata(_message.Message):
    __slots__ = ('conversation_profile', 'participant_role', 'suggestion_feature_type', 'create_time')
    CONVERSATION_PROFILE_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_ROLE_FIELD_NUMBER: _ClassVar[int]
    SUGGESTION_FEATURE_TYPE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    conversation_profile: str
    participant_role: _participant_pb2.Participant.Role
    suggestion_feature_type: _participant_pb2.SuggestionFeature.Type
    create_time: _timestamp_pb2.Timestamp

    def __init__(self, conversation_profile: _Optional[str]=..., participant_role: _Optional[_Union[_participant_pb2.Participant.Role, str]]=..., suggestion_feature_type: _Optional[_Union[_participant_pb2.SuggestionFeature.Type, str]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class ClearSuggestionFeatureConfigOperationMetadata(_message.Message):
    __slots__ = ('conversation_profile', 'participant_role', 'suggestion_feature_type', 'create_time')
    CONVERSATION_PROFILE_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_ROLE_FIELD_NUMBER: _ClassVar[int]
    SUGGESTION_FEATURE_TYPE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    conversation_profile: str
    participant_role: _participant_pb2.Participant.Role
    suggestion_feature_type: _participant_pb2.SuggestionFeature.Type
    create_time: _timestamp_pb2.Timestamp

    def __init__(self, conversation_profile: _Optional[str]=..., participant_role: _Optional[_Union[_participant_pb2.Participant.Role, str]]=..., suggestion_feature_type: _Optional[_Union[_participant_pb2.SuggestionFeature.Type, str]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...