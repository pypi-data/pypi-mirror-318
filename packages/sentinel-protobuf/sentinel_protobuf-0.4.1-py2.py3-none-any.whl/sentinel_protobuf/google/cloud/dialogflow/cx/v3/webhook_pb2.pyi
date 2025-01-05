from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.dialogflow.cx.v3 import response_message_pb2 as _response_message_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Webhook(_message.Message):
    __slots__ = ('name', 'display_name', 'generic_web_service', 'service_directory', 'timeout', 'disabled')

    class GenericWebService(_message.Message):
        __slots__ = ('uri', 'username', 'password', 'request_headers', 'allowed_ca_certs', 'oauth_config', 'service_agent_auth', 'webhook_type', 'http_method', 'request_body', 'parameter_mapping')

        class ServiceAgentAuth(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            SERVICE_AGENT_AUTH_UNSPECIFIED: _ClassVar[Webhook.GenericWebService.ServiceAgentAuth]
            NONE: _ClassVar[Webhook.GenericWebService.ServiceAgentAuth]
            ID_TOKEN: _ClassVar[Webhook.GenericWebService.ServiceAgentAuth]
            ACCESS_TOKEN: _ClassVar[Webhook.GenericWebService.ServiceAgentAuth]
        SERVICE_AGENT_AUTH_UNSPECIFIED: Webhook.GenericWebService.ServiceAgentAuth
        NONE: Webhook.GenericWebService.ServiceAgentAuth
        ID_TOKEN: Webhook.GenericWebService.ServiceAgentAuth
        ACCESS_TOKEN: Webhook.GenericWebService.ServiceAgentAuth

        class WebhookType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            WEBHOOK_TYPE_UNSPECIFIED: _ClassVar[Webhook.GenericWebService.WebhookType]
            STANDARD: _ClassVar[Webhook.GenericWebService.WebhookType]
            FLEXIBLE: _ClassVar[Webhook.GenericWebService.WebhookType]
        WEBHOOK_TYPE_UNSPECIFIED: Webhook.GenericWebService.WebhookType
        STANDARD: Webhook.GenericWebService.WebhookType
        FLEXIBLE: Webhook.GenericWebService.WebhookType

        class HttpMethod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            HTTP_METHOD_UNSPECIFIED: _ClassVar[Webhook.GenericWebService.HttpMethod]
            POST: _ClassVar[Webhook.GenericWebService.HttpMethod]
            GET: _ClassVar[Webhook.GenericWebService.HttpMethod]
            HEAD: _ClassVar[Webhook.GenericWebService.HttpMethod]
            PUT: _ClassVar[Webhook.GenericWebService.HttpMethod]
            DELETE: _ClassVar[Webhook.GenericWebService.HttpMethod]
            PATCH: _ClassVar[Webhook.GenericWebService.HttpMethod]
            OPTIONS: _ClassVar[Webhook.GenericWebService.HttpMethod]
        HTTP_METHOD_UNSPECIFIED: Webhook.GenericWebService.HttpMethod
        POST: Webhook.GenericWebService.HttpMethod
        GET: Webhook.GenericWebService.HttpMethod
        HEAD: Webhook.GenericWebService.HttpMethod
        PUT: Webhook.GenericWebService.HttpMethod
        DELETE: Webhook.GenericWebService.HttpMethod
        PATCH: Webhook.GenericWebService.HttpMethod
        OPTIONS: Webhook.GenericWebService.HttpMethod

        class OAuthConfig(_message.Message):
            __slots__ = ('client_id', 'client_secret', 'token_endpoint', 'scopes')
            CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
            CLIENT_SECRET_FIELD_NUMBER: _ClassVar[int]
            TOKEN_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
            SCOPES_FIELD_NUMBER: _ClassVar[int]
            client_id: str
            client_secret: str
            token_endpoint: str
            scopes: _containers.RepeatedScalarFieldContainer[str]

            def __init__(self, client_id: _Optional[str]=..., client_secret: _Optional[str]=..., token_endpoint: _Optional[str]=..., scopes: _Optional[_Iterable[str]]=...) -> None:
                ...

        class RequestHeadersEntry(_message.Message):
            __slots__ = ('key', 'value')
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str

            def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
                ...

        class ParameterMappingEntry(_message.Message):
            __slots__ = ('key', 'value')
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str

            def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
                ...
        URI_FIELD_NUMBER: _ClassVar[int]
        USERNAME_FIELD_NUMBER: _ClassVar[int]
        PASSWORD_FIELD_NUMBER: _ClassVar[int]
        REQUEST_HEADERS_FIELD_NUMBER: _ClassVar[int]
        ALLOWED_CA_CERTS_FIELD_NUMBER: _ClassVar[int]
        OAUTH_CONFIG_FIELD_NUMBER: _ClassVar[int]
        SERVICE_AGENT_AUTH_FIELD_NUMBER: _ClassVar[int]
        WEBHOOK_TYPE_FIELD_NUMBER: _ClassVar[int]
        HTTP_METHOD_FIELD_NUMBER: _ClassVar[int]
        REQUEST_BODY_FIELD_NUMBER: _ClassVar[int]
        PARAMETER_MAPPING_FIELD_NUMBER: _ClassVar[int]
        uri: str
        username: str
        password: str
        request_headers: _containers.ScalarMap[str, str]
        allowed_ca_certs: _containers.RepeatedScalarFieldContainer[bytes]
        oauth_config: Webhook.GenericWebService.OAuthConfig
        service_agent_auth: Webhook.GenericWebService.ServiceAgentAuth
        webhook_type: Webhook.GenericWebService.WebhookType
        http_method: Webhook.GenericWebService.HttpMethod
        request_body: str
        parameter_mapping: _containers.ScalarMap[str, str]

        def __init__(self, uri: _Optional[str]=..., username: _Optional[str]=..., password: _Optional[str]=..., request_headers: _Optional[_Mapping[str, str]]=..., allowed_ca_certs: _Optional[_Iterable[bytes]]=..., oauth_config: _Optional[_Union[Webhook.GenericWebService.OAuthConfig, _Mapping]]=..., service_agent_auth: _Optional[_Union[Webhook.GenericWebService.ServiceAgentAuth, str]]=..., webhook_type: _Optional[_Union[Webhook.GenericWebService.WebhookType, str]]=..., http_method: _Optional[_Union[Webhook.GenericWebService.HttpMethod, str]]=..., request_body: _Optional[str]=..., parameter_mapping: _Optional[_Mapping[str, str]]=...) -> None:
            ...

    class ServiceDirectoryConfig(_message.Message):
        __slots__ = ('service', 'generic_web_service')
        SERVICE_FIELD_NUMBER: _ClassVar[int]
        GENERIC_WEB_SERVICE_FIELD_NUMBER: _ClassVar[int]
        service: str
        generic_web_service: Webhook.GenericWebService

        def __init__(self, service: _Optional[str]=..., generic_web_service: _Optional[_Union[Webhook.GenericWebService, _Mapping]]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    GENERIC_WEB_SERVICE_FIELD_NUMBER: _ClassVar[int]
    SERVICE_DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    DISABLED_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    generic_web_service: Webhook.GenericWebService
    service_directory: Webhook.ServiceDirectoryConfig
    timeout: _duration_pb2.Duration
    disabled: bool

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., generic_web_service: _Optional[_Union[Webhook.GenericWebService, _Mapping]]=..., service_directory: _Optional[_Union[Webhook.ServiceDirectoryConfig, _Mapping]]=..., timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., disabled: bool=...) -> None:
        ...

class ListWebhooksRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListWebhooksResponse(_message.Message):
    __slots__ = ('webhooks', 'next_page_token')
    WEBHOOKS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    webhooks: _containers.RepeatedCompositeFieldContainer[Webhook]
    next_page_token: str

    def __init__(self, webhooks: _Optional[_Iterable[_Union[Webhook, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetWebhookRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateWebhookRequest(_message.Message):
    __slots__ = ('parent', 'webhook')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    WEBHOOK_FIELD_NUMBER: _ClassVar[int]
    parent: str
    webhook: Webhook

    def __init__(self, parent: _Optional[str]=..., webhook: _Optional[_Union[Webhook, _Mapping]]=...) -> None:
        ...

class UpdateWebhookRequest(_message.Message):
    __slots__ = ('webhook', 'update_mask')
    WEBHOOK_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    webhook: Webhook
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, webhook: _Optional[_Union[Webhook, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteWebhookRequest(_message.Message):
    __slots__ = ('name', 'force')
    NAME_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    force: bool

    def __init__(self, name: _Optional[str]=..., force: bool=...) -> None:
        ...

class WebhookRequest(_message.Message):
    __slots__ = ('detect_intent_response_id', 'text', 'trigger_intent', 'transcript', 'trigger_event', 'dtmf_digits', 'language_code', 'fulfillment_info', 'intent_info', 'page_info', 'session_info', 'messages', 'payload', 'sentiment_analysis_result', 'language_info')

    class FulfillmentInfo(_message.Message):
        __slots__ = ('tag',)
        TAG_FIELD_NUMBER: _ClassVar[int]
        tag: str

        def __init__(self, tag: _Optional[str]=...) -> None:
            ...

    class IntentInfo(_message.Message):
        __slots__ = ('last_matched_intent', 'display_name', 'parameters', 'confidence')

        class IntentParameterValue(_message.Message):
            __slots__ = ('original_value', 'resolved_value')
            ORIGINAL_VALUE_FIELD_NUMBER: _ClassVar[int]
            RESOLVED_VALUE_FIELD_NUMBER: _ClassVar[int]
            original_value: str
            resolved_value: _struct_pb2.Value

            def __init__(self, original_value: _Optional[str]=..., resolved_value: _Optional[_Union[_struct_pb2.Value, _Mapping]]=...) -> None:
                ...

        class ParametersEntry(_message.Message):
            __slots__ = ('key', 'value')
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: WebhookRequest.IntentInfo.IntentParameterValue

            def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[WebhookRequest.IntentInfo.IntentParameterValue, _Mapping]]=...) -> None:
                ...
        LAST_MATCHED_INTENT_FIELD_NUMBER: _ClassVar[int]
        DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
        PARAMETERS_FIELD_NUMBER: _ClassVar[int]
        CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
        last_matched_intent: str
        display_name: str
        parameters: _containers.MessageMap[str, WebhookRequest.IntentInfo.IntentParameterValue]
        confidence: float

        def __init__(self, last_matched_intent: _Optional[str]=..., display_name: _Optional[str]=..., parameters: _Optional[_Mapping[str, WebhookRequest.IntentInfo.IntentParameterValue]]=..., confidence: _Optional[float]=...) -> None:
            ...

    class SentimentAnalysisResult(_message.Message):
        __slots__ = ('score', 'magnitude')
        SCORE_FIELD_NUMBER: _ClassVar[int]
        MAGNITUDE_FIELD_NUMBER: _ClassVar[int]
        score: float
        magnitude: float

        def __init__(self, score: _Optional[float]=..., magnitude: _Optional[float]=...) -> None:
            ...
    DETECT_INTENT_RESPONSE_ID_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_INTENT_FIELD_NUMBER: _ClassVar[int]
    TRANSCRIPT_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_EVENT_FIELD_NUMBER: _ClassVar[int]
    DTMF_DIGITS_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    FULFILLMENT_INFO_FIELD_NUMBER: _ClassVar[int]
    INTENT_INFO_FIELD_NUMBER: _ClassVar[int]
    PAGE_INFO_FIELD_NUMBER: _ClassVar[int]
    SESSION_INFO_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    SENTIMENT_ANALYSIS_RESULT_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_INFO_FIELD_NUMBER: _ClassVar[int]
    detect_intent_response_id: str
    text: str
    trigger_intent: str
    transcript: str
    trigger_event: str
    dtmf_digits: str
    language_code: str
    fulfillment_info: WebhookRequest.FulfillmentInfo
    intent_info: WebhookRequest.IntentInfo
    page_info: PageInfo
    session_info: SessionInfo
    messages: _containers.RepeatedCompositeFieldContainer[_response_message_pb2.ResponseMessage]
    payload: _struct_pb2.Struct
    sentiment_analysis_result: WebhookRequest.SentimentAnalysisResult
    language_info: LanguageInfo

    def __init__(self, detect_intent_response_id: _Optional[str]=..., text: _Optional[str]=..., trigger_intent: _Optional[str]=..., transcript: _Optional[str]=..., trigger_event: _Optional[str]=..., dtmf_digits: _Optional[str]=..., language_code: _Optional[str]=..., fulfillment_info: _Optional[_Union[WebhookRequest.FulfillmentInfo, _Mapping]]=..., intent_info: _Optional[_Union[WebhookRequest.IntentInfo, _Mapping]]=..., page_info: _Optional[_Union[PageInfo, _Mapping]]=..., session_info: _Optional[_Union[SessionInfo, _Mapping]]=..., messages: _Optional[_Iterable[_Union[_response_message_pb2.ResponseMessage, _Mapping]]]=..., payload: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=..., sentiment_analysis_result: _Optional[_Union[WebhookRequest.SentimentAnalysisResult, _Mapping]]=..., language_info: _Optional[_Union[LanguageInfo, _Mapping]]=...) -> None:
        ...

class WebhookResponse(_message.Message):
    __slots__ = ('fulfillment_response', 'page_info', 'session_info', 'payload', 'target_page', 'target_flow')

    class FulfillmentResponse(_message.Message):
        __slots__ = ('messages', 'merge_behavior')

        class MergeBehavior(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            MERGE_BEHAVIOR_UNSPECIFIED: _ClassVar[WebhookResponse.FulfillmentResponse.MergeBehavior]
            APPEND: _ClassVar[WebhookResponse.FulfillmentResponse.MergeBehavior]
            REPLACE: _ClassVar[WebhookResponse.FulfillmentResponse.MergeBehavior]
        MERGE_BEHAVIOR_UNSPECIFIED: WebhookResponse.FulfillmentResponse.MergeBehavior
        APPEND: WebhookResponse.FulfillmentResponse.MergeBehavior
        REPLACE: WebhookResponse.FulfillmentResponse.MergeBehavior
        MESSAGES_FIELD_NUMBER: _ClassVar[int]
        MERGE_BEHAVIOR_FIELD_NUMBER: _ClassVar[int]
        messages: _containers.RepeatedCompositeFieldContainer[_response_message_pb2.ResponseMessage]
        merge_behavior: WebhookResponse.FulfillmentResponse.MergeBehavior

        def __init__(self, messages: _Optional[_Iterable[_Union[_response_message_pb2.ResponseMessage, _Mapping]]]=..., merge_behavior: _Optional[_Union[WebhookResponse.FulfillmentResponse.MergeBehavior, str]]=...) -> None:
            ...
    FULFILLMENT_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    PAGE_INFO_FIELD_NUMBER: _ClassVar[int]
    SESSION_INFO_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    TARGET_PAGE_FIELD_NUMBER: _ClassVar[int]
    TARGET_FLOW_FIELD_NUMBER: _ClassVar[int]
    fulfillment_response: WebhookResponse.FulfillmentResponse
    page_info: PageInfo
    session_info: SessionInfo
    payload: _struct_pb2.Struct
    target_page: str
    target_flow: str

    def __init__(self, fulfillment_response: _Optional[_Union[WebhookResponse.FulfillmentResponse, _Mapping]]=..., page_info: _Optional[_Union[PageInfo, _Mapping]]=..., session_info: _Optional[_Union[SessionInfo, _Mapping]]=..., payload: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=..., target_page: _Optional[str]=..., target_flow: _Optional[str]=...) -> None:
        ...

class PageInfo(_message.Message):
    __slots__ = ('current_page', 'display_name', 'form_info')

    class FormInfo(_message.Message):
        __slots__ = ('parameter_info',)

        class ParameterInfo(_message.Message):
            __slots__ = ('display_name', 'required', 'state', 'value', 'just_collected')

            class ParameterState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                PARAMETER_STATE_UNSPECIFIED: _ClassVar[PageInfo.FormInfo.ParameterInfo.ParameterState]
                EMPTY: _ClassVar[PageInfo.FormInfo.ParameterInfo.ParameterState]
                INVALID: _ClassVar[PageInfo.FormInfo.ParameterInfo.ParameterState]
                FILLED: _ClassVar[PageInfo.FormInfo.ParameterInfo.ParameterState]
            PARAMETER_STATE_UNSPECIFIED: PageInfo.FormInfo.ParameterInfo.ParameterState
            EMPTY: PageInfo.FormInfo.ParameterInfo.ParameterState
            INVALID: PageInfo.FormInfo.ParameterInfo.ParameterState
            FILLED: PageInfo.FormInfo.ParameterInfo.ParameterState
            DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
            REQUIRED_FIELD_NUMBER: _ClassVar[int]
            STATE_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            JUST_COLLECTED_FIELD_NUMBER: _ClassVar[int]
            display_name: str
            required: bool
            state: PageInfo.FormInfo.ParameterInfo.ParameterState
            value: _struct_pb2.Value
            just_collected: bool

            def __init__(self, display_name: _Optional[str]=..., required: bool=..., state: _Optional[_Union[PageInfo.FormInfo.ParameterInfo.ParameterState, str]]=..., value: _Optional[_Union[_struct_pb2.Value, _Mapping]]=..., just_collected: bool=...) -> None:
                ...
        PARAMETER_INFO_FIELD_NUMBER: _ClassVar[int]
        parameter_info: _containers.RepeatedCompositeFieldContainer[PageInfo.FormInfo.ParameterInfo]

        def __init__(self, parameter_info: _Optional[_Iterable[_Union[PageInfo.FormInfo.ParameterInfo, _Mapping]]]=...) -> None:
            ...
    CURRENT_PAGE_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    FORM_INFO_FIELD_NUMBER: _ClassVar[int]
    current_page: str
    display_name: str
    form_info: PageInfo.FormInfo

    def __init__(self, current_page: _Optional[str]=..., display_name: _Optional[str]=..., form_info: _Optional[_Union[PageInfo.FormInfo, _Mapping]]=...) -> None:
        ...

class SessionInfo(_message.Message):
    __slots__ = ('session', 'parameters')

    class ParametersEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _struct_pb2.Value

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[_struct_pb2.Value, _Mapping]]=...) -> None:
            ...
    SESSION_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    session: str
    parameters: _containers.MessageMap[str, _struct_pb2.Value]

    def __init__(self, session: _Optional[str]=..., parameters: _Optional[_Mapping[str, _struct_pb2.Value]]=...) -> None:
        ...

class LanguageInfo(_message.Message):
    __slots__ = ('input_language_code', 'resolved_language_code', 'confidence_score')
    INPUT_LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_SCORE_FIELD_NUMBER: _ClassVar[int]
    input_language_code: str
    resolved_language_code: str
    confidence_score: float

    def __init__(self, input_language_code: _Optional[str]=..., resolved_language_code: _Optional[str]=..., confidence_score: _Optional[float]=...) -> None:
        ...