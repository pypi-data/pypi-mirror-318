from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.dialogflow.cx.v3beta1 import advanced_settings_pb2 as _advanced_settings_pb2
from google.cloud.dialogflow.cx.v3beta1 import audio_config_pb2 as _audio_config_pb2
from google.cloud.dialogflow.cx.v3beta1 import bigquery_export_pb2 as _bigquery_export_pb2
from google.cloud.dialogflow.cx.v3beta1 import flow_pb2 as _flow_pb2
from google.cloud.dialogflow.cx.v3beta1 import generative_settings_pb2 as _generative_settings_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SpeechToTextSettings(_message.Message):
    __slots__ = ("enable_speech_adaptation",)
    ENABLE_SPEECH_ADAPTATION_FIELD_NUMBER: _ClassVar[int]
    enable_speech_adaptation: bool
    def __init__(self, enable_speech_adaptation: bool = ...) -> None: ...

class Agent(_message.Message):
    __slots__ = ("name", "display_name", "default_language_code", "supported_language_codes", "time_zone", "description", "avatar_uri", "speech_to_text_settings", "start_flow", "start_playbook", "security_settings", "enable_stackdriver_logging", "enable_spell_correction", "enable_multi_language_training", "locked", "advanced_settings", "git_integration_settings", "bigquery_export_settings", "text_to_speech_settings", "gen_app_builder_settings", "answer_feedback_settings", "personalization_settings", "client_certificate_settings")
    class GitIntegrationSettings(_message.Message):
        __slots__ = ("github_settings",)
        class GithubSettings(_message.Message):
            __slots__ = ("display_name", "repository_uri", "tracking_branch", "access_token", "branches")
            DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
            REPOSITORY_URI_FIELD_NUMBER: _ClassVar[int]
            TRACKING_BRANCH_FIELD_NUMBER: _ClassVar[int]
            ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
            BRANCHES_FIELD_NUMBER: _ClassVar[int]
            display_name: str
            repository_uri: str
            tracking_branch: str
            access_token: str
            branches: _containers.RepeatedScalarFieldContainer[str]
            def __init__(self, display_name: _Optional[str] = ..., repository_uri: _Optional[str] = ..., tracking_branch: _Optional[str] = ..., access_token: _Optional[str] = ..., branches: _Optional[_Iterable[str]] = ...) -> None: ...
        GITHUB_SETTINGS_FIELD_NUMBER: _ClassVar[int]
        github_settings: Agent.GitIntegrationSettings.GithubSettings
        def __init__(self, github_settings: _Optional[_Union[Agent.GitIntegrationSettings.GithubSettings, _Mapping]] = ...) -> None: ...
    class GenAppBuilderSettings(_message.Message):
        __slots__ = ("engine",)
        ENGINE_FIELD_NUMBER: _ClassVar[int]
        engine: str
        def __init__(self, engine: _Optional[str] = ...) -> None: ...
    class AnswerFeedbackSettings(_message.Message):
        __slots__ = ("enable_answer_feedback",)
        ENABLE_ANSWER_FEEDBACK_FIELD_NUMBER: _ClassVar[int]
        enable_answer_feedback: bool
        def __init__(self, enable_answer_feedback: bool = ...) -> None: ...
    class PersonalizationSettings(_message.Message):
        __slots__ = ("default_end_user_metadata",)
        DEFAULT_END_USER_METADATA_FIELD_NUMBER: _ClassVar[int]
        default_end_user_metadata: _struct_pb2.Struct
        def __init__(self, default_end_user_metadata: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...
    class ClientCertificateSettings(_message.Message):
        __slots__ = ("ssl_certificate", "private_key", "passphrase")
        SSL_CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
        PRIVATE_KEY_FIELD_NUMBER: _ClassVar[int]
        PASSPHRASE_FIELD_NUMBER: _ClassVar[int]
        ssl_certificate: str
        private_key: str
        passphrase: str
        def __init__(self, ssl_certificate: _Optional[str] = ..., private_key: _Optional[str] = ..., passphrase: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_LANGUAGE_CODES_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    AVATAR_URI_FIELD_NUMBER: _ClassVar[int]
    SPEECH_TO_TEXT_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    START_FLOW_FIELD_NUMBER: _ClassVar[int]
    START_PLAYBOOK_FIELD_NUMBER: _ClassVar[int]
    SECURITY_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    ENABLE_STACKDRIVER_LOGGING_FIELD_NUMBER: _ClassVar[int]
    ENABLE_SPELL_CORRECTION_FIELD_NUMBER: _ClassVar[int]
    ENABLE_MULTI_LANGUAGE_TRAINING_FIELD_NUMBER: _ClassVar[int]
    LOCKED_FIELD_NUMBER: _ClassVar[int]
    ADVANCED_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    GIT_INTEGRATION_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    BIGQUERY_EXPORT_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    TEXT_TO_SPEECH_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    GEN_APP_BUILDER_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    ANSWER_FEEDBACK_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    PERSONALIZATION_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    CLIENT_CERTIFICATE_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    default_language_code: str
    supported_language_codes: _containers.RepeatedScalarFieldContainer[str]
    time_zone: str
    description: str
    avatar_uri: str
    speech_to_text_settings: SpeechToTextSettings
    start_flow: str
    start_playbook: str
    security_settings: str
    enable_stackdriver_logging: bool
    enable_spell_correction: bool
    enable_multi_language_training: bool
    locked: bool
    advanced_settings: _advanced_settings_pb2.AdvancedSettings
    git_integration_settings: Agent.GitIntegrationSettings
    bigquery_export_settings: _bigquery_export_pb2.BigQueryExportSettings
    text_to_speech_settings: _audio_config_pb2.TextToSpeechSettings
    gen_app_builder_settings: Agent.GenAppBuilderSettings
    answer_feedback_settings: Agent.AnswerFeedbackSettings
    personalization_settings: Agent.PersonalizationSettings
    client_certificate_settings: Agent.ClientCertificateSettings
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., default_language_code: _Optional[str] = ..., supported_language_codes: _Optional[_Iterable[str]] = ..., time_zone: _Optional[str] = ..., description: _Optional[str] = ..., avatar_uri: _Optional[str] = ..., speech_to_text_settings: _Optional[_Union[SpeechToTextSettings, _Mapping]] = ..., start_flow: _Optional[str] = ..., start_playbook: _Optional[str] = ..., security_settings: _Optional[str] = ..., enable_stackdriver_logging: bool = ..., enable_spell_correction: bool = ..., enable_multi_language_training: bool = ..., locked: bool = ..., advanced_settings: _Optional[_Union[_advanced_settings_pb2.AdvancedSettings, _Mapping]] = ..., git_integration_settings: _Optional[_Union[Agent.GitIntegrationSettings, _Mapping]] = ..., bigquery_export_settings: _Optional[_Union[_bigquery_export_pb2.BigQueryExportSettings, _Mapping]] = ..., text_to_speech_settings: _Optional[_Union[_audio_config_pb2.TextToSpeechSettings, _Mapping]] = ..., gen_app_builder_settings: _Optional[_Union[Agent.GenAppBuilderSettings, _Mapping]] = ..., answer_feedback_settings: _Optional[_Union[Agent.AnswerFeedbackSettings, _Mapping]] = ..., personalization_settings: _Optional[_Union[Agent.PersonalizationSettings, _Mapping]] = ..., client_certificate_settings: _Optional[_Union[Agent.ClientCertificateSettings, _Mapping]] = ...) -> None: ...

class ListAgentsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListAgentsResponse(_message.Message):
    __slots__ = ("agents", "next_page_token")
    AGENTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    agents: _containers.RepeatedCompositeFieldContainer[Agent]
    next_page_token: str
    def __init__(self, agents: _Optional[_Iterable[_Union[Agent, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class GetAgentRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CreateAgentRequest(_message.Message):
    __slots__ = ("parent", "agent")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    AGENT_FIELD_NUMBER: _ClassVar[int]
    parent: str
    agent: Agent
    def __init__(self, parent: _Optional[str] = ..., agent: _Optional[_Union[Agent, _Mapping]] = ...) -> None: ...

class UpdateAgentRequest(_message.Message):
    __slots__ = ("agent", "update_mask")
    AGENT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    agent: Agent
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, agent: _Optional[_Union[Agent, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeleteAgentRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ExportAgentRequest(_message.Message):
    __slots__ = ("name", "agent_uri", "data_format", "environment", "git_destination", "include_bigquery_export_settings")
    class DataFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DATA_FORMAT_UNSPECIFIED: _ClassVar[ExportAgentRequest.DataFormat]
        BLOB: _ClassVar[ExportAgentRequest.DataFormat]
        JSON_PACKAGE: _ClassVar[ExportAgentRequest.DataFormat]
    DATA_FORMAT_UNSPECIFIED: ExportAgentRequest.DataFormat
    BLOB: ExportAgentRequest.DataFormat
    JSON_PACKAGE: ExportAgentRequest.DataFormat
    class GitDestination(_message.Message):
        __slots__ = ("tracking_branch", "commit_message")
        TRACKING_BRANCH_FIELD_NUMBER: _ClassVar[int]
        COMMIT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        tracking_branch: str
        commit_message: str
        def __init__(self, tracking_branch: _Optional[str] = ..., commit_message: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    AGENT_URI_FIELD_NUMBER: _ClassVar[int]
    DATA_FORMAT_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    GIT_DESTINATION_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_BIGQUERY_EXPORT_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    name: str
    agent_uri: str
    data_format: ExportAgentRequest.DataFormat
    environment: str
    git_destination: ExportAgentRequest.GitDestination
    include_bigquery_export_settings: bool
    def __init__(self, name: _Optional[str] = ..., agent_uri: _Optional[str] = ..., data_format: _Optional[_Union[ExportAgentRequest.DataFormat, str]] = ..., environment: _Optional[str] = ..., git_destination: _Optional[_Union[ExportAgentRequest.GitDestination, _Mapping]] = ..., include_bigquery_export_settings: bool = ...) -> None: ...

class ExportAgentResponse(_message.Message):
    __slots__ = ("agent_uri", "agent_content", "commit_sha")
    AGENT_URI_FIELD_NUMBER: _ClassVar[int]
    AGENT_CONTENT_FIELD_NUMBER: _ClassVar[int]
    COMMIT_SHA_FIELD_NUMBER: _ClassVar[int]
    agent_uri: str
    agent_content: bytes
    commit_sha: str
    def __init__(self, agent_uri: _Optional[str] = ..., agent_content: _Optional[bytes] = ..., commit_sha: _Optional[str] = ...) -> None: ...

class RestoreAgentRequest(_message.Message):
    __slots__ = ("name", "agent_uri", "agent_content", "git_source", "restore_option")
    class RestoreOption(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RESTORE_OPTION_UNSPECIFIED: _ClassVar[RestoreAgentRequest.RestoreOption]
        KEEP: _ClassVar[RestoreAgentRequest.RestoreOption]
        FALLBACK: _ClassVar[RestoreAgentRequest.RestoreOption]
    RESTORE_OPTION_UNSPECIFIED: RestoreAgentRequest.RestoreOption
    KEEP: RestoreAgentRequest.RestoreOption
    FALLBACK: RestoreAgentRequest.RestoreOption
    class GitSource(_message.Message):
        __slots__ = ("tracking_branch",)
        TRACKING_BRANCH_FIELD_NUMBER: _ClassVar[int]
        tracking_branch: str
        def __init__(self, tracking_branch: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    AGENT_URI_FIELD_NUMBER: _ClassVar[int]
    AGENT_CONTENT_FIELD_NUMBER: _ClassVar[int]
    GIT_SOURCE_FIELD_NUMBER: _ClassVar[int]
    RESTORE_OPTION_FIELD_NUMBER: _ClassVar[int]
    name: str
    agent_uri: str
    agent_content: bytes
    git_source: RestoreAgentRequest.GitSource
    restore_option: RestoreAgentRequest.RestoreOption
    def __init__(self, name: _Optional[str] = ..., agent_uri: _Optional[str] = ..., agent_content: _Optional[bytes] = ..., git_source: _Optional[_Union[RestoreAgentRequest.GitSource, _Mapping]] = ..., restore_option: _Optional[_Union[RestoreAgentRequest.RestoreOption, str]] = ...) -> None: ...

class ValidateAgentRequest(_message.Message):
    __slots__ = ("name", "language_code")
    NAME_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    name: str
    language_code: str
    def __init__(self, name: _Optional[str] = ..., language_code: _Optional[str] = ...) -> None: ...

class GetAgentValidationResultRequest(_message.Message):
    __slots__ = ("name", "language_code")
    NAME_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    name: str
    language_code: str
    def __init__(self, name: _Optional[str] = ..., language_code: _Optional[str] = ...) -> None: ...

class AgentValidationResult(_message.Message):
    __slots__ = ("name", "flow_validation_results")
    NAME_FIELD_NUMBER: _ClassVar[int]
    FLOW_VALIDATION_RESULTS_FIELD_NUMBER: _ClassVar[int]
    name: str
    flow_validation_results: _containers.RepeatedCompositeFieldContainer[_flow_pb2.FlowValidationResult]
    def __init__(self, name: _Optional[str] = ..., flow_validation_results: _Optional[_Iterable[_Union[_flow_pb2.FlowValidationResult, _Mapping]]] = ...) -> None: ...

class GetGenerativeSettingsRequest(_message.Message):
    __slots__ = ("name", "language_code")
    NAME_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    name: str
    language_code: str
    def __init__(self, name: _Optional[str] = ..., language_code: _Optional[str] = ...) -> None: ...

class UpdateGenerativeSettingsRequest(_message.Message):
    __slots__ = ("generative_settings", "update_mask")
    GENERATIVE_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    generative_settings: _generative_settings_pb2.GenerativeSettings
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, generative_settings: _Optional[_Union[_generative_settings_pb2.GenerativeSettings, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...
