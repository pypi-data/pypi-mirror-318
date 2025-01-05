from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.dialogflow.cx.v3beta1 import advanced_settings_pb2 as _advanced_settings_pb2
from google.cloud.dialogflow.cx.v3beta1 import data_store_connection_pb2 as _data_store_connection_pb2
from google.cloud.dialogflow.cx.v3beta1 import fulfillment_pb2 as _fulfillment_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Page(_message.Message):
    __slots__ = ('name', 'display_name', 'description', 'entry_fulfillment', 'form', 'transition_route_groups', 'transition_routes', 'event_handlers', 'advanced_settings', 'knowledge_connector_settings')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ENTRY_FULFILLMENT_FIELD_NUMBER: _ClassVar[int]
    FORM_FIELD_NUMBER: _ClassVar[int]
    TRANSITION_ROUTE_GROUPS_FIELD_NUMBER: _ClassVar[int]
    TRANSITION_ROUTES_FIELD_NUMBER: _ClassVar[int]
    EVENT_HANDLERS_FIELD_NUMBER: _ClassVar[int]
    ADVANCED_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    KNOWLEDGE_CONNECTOR_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    description: str
    entry_fulfillment: _fulfillment_pb2.Fulfillment
    form: Form
    transition_route_groups: _containers.RepeatedScalarFieldContainer[str]
    transition_routes: _containers.RepeatedCompositeFieldContainer[TransitionRoute]
    event_handlers: _containers.RepeatedCompositeFieldContainer[EventHandler]
    advanced_settings: _advanced_settings_pb2.AdvancedSettings
    knowledge_connector_settings: KnowledgeConnectorSettings

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., description: _Optional[str]=..., entry_fulfillment: _Optional[_Union[_fulfillment_pb2.Fulfillment, _Mapping]]=..., form: _Optional[_Union[Form, _Mapping]]=..., transition_route_groups: _Optional[_Iterable[str]]=..., transition_routes: _Optional[_Iterable[_Union[TransitionRoute, _Mapping]]]=..., event_handlers: _Optional[_Iterable[_Union[EventHandler, _Mapping]]]=..., advanced_settings: _Optional[_Union[_advanced_settings_pb2.AdvancedSettings, _Mapping]]=..., knowledge_connector_settings: _Optional[_Union[KnowledgeConnectorSettings, _Mapping]]=...) -> None:
        ...

class Form(_message.Message):
    __slots__ = ('parameters',)

    class Parameter(_message.Message):
        __slots__ = ('display_name', 'required', 'entity_type', 'is_list', 'fill_behavior', 'default_value', 'redact', 'advanced_settings')

        class FillBehavior(_message.Message):
            __slots__ = ('initial_prompt_fulfillment', 'reprompt_event_handlers')
            INITIAL_PROMPT_FULFILLMENT_FIELD_NUMBER: _ClassVar[int]
            REPROMPT_EVENT_HANDLERS_FIELD_NUMBER: _ClassVar[int]
            initial_prompt_fulfillment: _fulfillment_pb2.Fulfillment
            reprompt_event_handlers: _containers.RepeatedCompositeFieldContainer[EventHandler]

            def __init__(self, initial_prompt_fulfillment: _Optional[_Union[_fulfillment_pb2.Fulfillment, _Mapping]]=..., reprompt_event_handlers: _Optional[_Iterable[_Union[EventHandler, _Mapping]]]=...) -> None:
                ...
        DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
        REQUIRED_FIELD_NUMBER: _ClassVar[int]
        ENTITY_TYPE_FIELD_NUMBER: _ClassVar[int]
        IS_LIST_FIELD_NUMBER: _ClassVar[int]
        FILL_BEHAVIOR_FIELD_NUMBER: _ClassVar[int]
        DEFAULT_VALUE_FIELD_NUMBER: _ClassVar[int]
        REDACT_FIELD_NUMBER: _ClassVar[int]
        ADVANCED_SETTINGS_FIELD_NUMBER: _ClassVar[int]
        display_name: str
        required: bool
        entity_type: str
        is_list: bool
        fill_behavior: Form.Parameter.FillBehavior
        default_value: _struct_pb2.Value
        redact: bool
        advanced_settings: _advanced_settings_pb2.AdvancedSettings

        def __init__(self, display_name: _Optional[str]=..., required: bool=..., entity_type: _Optional[str]=..., is_list: bool=..., fill_behavior: _Optional[_Union[Form.Parameter.FillBehavior, _Mapping]]=..., default_value: _Optional[_Union[_struct_pb2.Value, _Mapping]]=..., redact: bool=..., advanced_settings: _Optional[_Union[_advanced_settings_pb2.AdvancedSettings, _Mapping]]=...) -> None:
            ...
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    parameters: _containers.RepeatedCompositeFieldContainer[Form.Parameter]

    def __init__(self, parameters: _Optional[_Iterable[_Union[Form.Parameter, _Mapping]]]=...) -> None:
        ...

class EventHandler(_message.Message):
    __slots__ = ('name', 'event', 'trigger_fulfillment', 'target_page', 'target_flow', 'target_playbook')
    NAME_FIELD_NUMBER: _ClassVar[int]
    EVENT_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_FULFILLMENT_FIELD_NUMBER: _ClassVar[int]
    TARGET_PAGE_FIELD_NUMBER: _ClassVar[int]
    TARGET_FLOW_FIELD_NUMBER: _ClassVar[int]
    TARGET_PLAYBOOK_FIELD_NUMBER: _ClassVar[int]
    name: str
    event: str
    trigger_fulfillment: _fulfillment_pb2.Fulfillment
    target_page: str
    target_flow: str
    target_playbook: str

    def __init__(self, name: _Optional[str]=..., event: _Optional[str]=..., trigger_fulfillment: _Optional[_Union[_fulfillment_pb2.Fulfillment, _Mapping]]=..., target_page: _Optional[str]=..., target_flow: _Optional[str]=..., target_playbook: _Optional[str]=...) -> None:
        ...

class TransitionRoute(_message.Message):
    __slots__ = ('name', 'description', 'intent', 'condition', 'trigger_fulfillment', 'target_page', 'target_flow')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    INTENT_FIELD_NUMBER: _ClassVar[int]
    CONDITION_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_FULFILLMENT_FIELD_NUMBER: _ClassVar[int]
    TARGET_PAGE_FIELD_NUMBER: _ClassVar[int]
    TARGET_FLOW_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    intent: str
    condition: str
    trigger_fulfillment: _fulfillment_pb2.Fulfillment
    target_page: str
    target_flow: str

    def __init__(self, name: _Optional[str]=..., description: _Optional[str]=..., intent: _Optional[str]=..., condition: _Optional[str]=..., trigger_fulfillment: _Optional[_Union[_fulfillment_pb2.Fulfillment, _Mapping]]=..., target_page: _Optional[str]=..., target_flow: _Optional[str]=...) -> None:
        ...

class ListPagesRequest(_message.Message):
    __slots__ = ('parent', 'language_code', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    language_code: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., language_code: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListPagesResponse(_message.Message):
    __slots__ = ('pages', 'next_page_token')
    PAGES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    pages: _containers.RepeatedCompositeFieldContainer[Page]
    next_page_token: str

    def __init__(self, pages: _Optional[_Iterable[_Union[Page, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetPageRequest(_message.Message):
    __slots__ = ('name', 'language_code')
    NAME_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    name: str
    language_code: str

    def __init__(self, name: _Optional[str]=..., language_code: _Optional[str]=...) -> None:
        ...

class CreatePageRequest(_message.Message):
    __slots__ = ('parent', 'page', 'language_code')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page: Page
    language_code: str

    def __init__(self, parent: _Optional[str]=..., page: _Optional[_Union[Page, _Mapping]]=..., language_code: _Optional[str]=...) -> None:
        ...

class UpdatePageRequest(_message.Message):
    __slots__ = ('page', 'language_code', 'update_mask')
    PAGE_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    page: Page
    language_code: str
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, page: _Optional[_Union[Page, _Mapping]]=..., language_code: _Optional[str]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeletePageRequest(_message.Message):
    __slots__ = ('name', 'force')
    NAME_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    force: bool

    def __init__(self, name: _Optional[str]=..., force: bool=...) -> None:
        ...

class KnowledgeConnectorSettings(_message.Message):
    __slots__ = ('enabled', 'trigger_fulfillment', 'target_page', 'target_flow', 'data_store_connections')
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_FULFILLMENT_FIELD_NUMBER: _ClassVar[int]
    TARGET_PAGE_FIELD_NUMBER: _ClassVar[int]
    TARGET_FLOW_FIELD_NUMBER: _ClassVar[int]
    DATA_STORE_CONNECTIONS_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    trigger_fulfillment: _fulfillment_pb2.Fulfillment
    target_page: str
    target_flow: str
    data_store_connections: _containers.RepeatedCompositeFieldContainer[_data_store_connection_pb2.DataStoreConnection]

    def __init__(self, enabled: bool=..., trigger_fulfillment: _Optional[_Union[_fulfillment_pb2.Fulfillment, _Mapping]]=..., target_page: _Optional[str]=..., target_flow: _Optional[str]=..., data_store_connections: _Optional[_Iterable[_Union[_data_store_connection_pb2.DataStoreConnection, _Mapping]]]=...) -> None:
        ...