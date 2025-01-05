from google.api import resource_pb2 as _resource_pb2
from google.cloud.dialogflow.cx.v3 import safety_settings_pb2 as _safety_settings_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class GenerativeSettings(_message.Message):
    __slots__ = ('name', 'fallback_settings', 'generative_safety_settings', 'knowledge_connector_settings', 'language_code')

    class FallbackSettings(_message.Message):
        __slots__ = ('selected_prompt', 'prompt_templates')

        class PromptTemplate(_message.Message):
            __slots__ = ('display_name', 'prompt_text', 'frozen')
            DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
            PROMPT_TEXT_FIELD_NUMBER: _ClassVar[int]
            FROZEN_FIELD_NUMBER: _ClassVar[int]
            display_name: str
            prompt_text: str
            frozen: bool

            def __init__(self, display_name: _Optional[str]=..., prompt_text: _Optional[str]=..., frozen: bool=...) -> None:
                ...
        SELECTED_PROMPT_FIELD_NUMBER: _ClassVar[int]
        PROMPT_TEMPLATES_FIELD_NUMBER: _ClassVar[int]
        selected_prompt: str
        prompt_templates: _containers.RepeatedCompositeFieldContainer[GenerativeSettings.FallbackSettings.PromptTemplate]

        def __init__(self, selected_prompt: _Optional[str]=..., prompt_templates: _Optional[_Iterable[_Union[GenerativeSettings.FallbackSettings.PromptTemplate, _Mapping]]]=...) -> None:
            ...

    class KnowledgeConnectorSettings(_message.Message):
        __slots__ = ('business', 'agent', 'agent_identity', 'business_description', 'agent_scope', 'disable_data_store_fallback')
        BUSINESS_FIELD_NUMBER: _ClassVar[int]
        AGENT_FIELD_NUMBER: _ClassVar[int]
        AGENT_IDENTITY_FIELD_NUMBER: _ClassVar[int]
        BUSINESS_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        AGENT_SCOPE_FIELD_NUMBER: _ClassVar[int]
        DISABLE_DATA_STORE_FALLBACK_FIELD_NUMBER: _ClassVar[int]
        business: str
        agent: str
        agent_identity: str
        business_description: str
        agent_scope: str
        disable_data_store_fallback: bool

        def __init__(self, business: _Optional[str]=..., agent: _Optional[str]=..., agent_identity: _Optional[str]=..., business_description: _Optional[str]=..., agent_scope: _Optional[str]=..., disable_data_store_fallback: bool=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    FALLBACK_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    GENERATIVE_SAFETY_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    KNOWLEDGE_CONNECTOR_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    name: str
    fallback_settings: GenerativeSettings.FallbackSettings
    generative_safety_settings: _safety_settings_pb2.SafetySettings
    knowledge_connector_settings: GenerativeSettings.KnowledgeConnectorSettings
    language_code: str

    def __init__(self, name: _Optional[str]=..., fallback_settings: _Optional[_Union[GenerativeSettings.FallbackSettings, _Mapping]]=..., generative_safety_settings: _Optional[_Union[_safety_settings_pb2.SafetySettings, _Mapping]]=..., knowledge_connector_settings: _Optional[_Union[GenerativeSettings.KnowledgeConnectorSettings, _Mapping]]=..., language_code: _Optional[str]=...) -> None:
        ...