from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.dialogflow.cx.v3beta1 import advanced_settings_pb2 as _advanced_settings_pb2
from google.cloud.dialogflow.cx.v3beta1 import import_strategy_pb2 as _import_strategy_pb2
from google.cloud.dialogflow.cx.v3beta1 import page_pb2 as _page_pb2
from google.cloud.dialogflow.cx.v3beta1 import validation_message_pb2 as _validation_message_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class NluSettings(_message.Message):
    __slots__ = ('model_type', 'classification_threshold', 'model_training_mode')

    class ModelType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MODEL_TYPE_UNSPECIFIED: _ClassVar[NluSettings.ModelType]
        MODEL_TYPE_STANDARD: _ClassVar[NluSettings.ModelType]
        MODEL_TYPE_ADVANCED: _ClassVar[NluSettings.ModelType]
    MODEL_TYPE_UNSPECIFIED: NluSettings.ModelType
    MODEL_TYPE_STANDARD: NluSettings.ModelType
    MODEL_TYPE_ADVANCED: NluSettings.ModelType

    class ModelTrainingMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MODEL_TRAINING_MODE_UNSPECIFIED: _ClassVar[NluSettings.ModelTrainingMode]
        MODEL_TRAINING_MODE_AUTOMATIC: _ClassVar[NluSettings.ModelTrainingMode]
        MODEL_TRAINING_MODE_MANUAL: _ClassVar[NluSettings.ModelTrainingMode]
    MODEL_TRAINING_MODE_UNSPECIFIED: NluSettings.ModelTrainingMode
    MODEL_TRAINING_MODE_AUTOMATIC: NluSettings.ModelTrainingMode
    MODEL_TRAINING_MODE_MANUAL: NluSettings.ModelTrainingMode
    MODEL_TYPE_FIELD_NUMBER: _ClassVar[int]
    CLASSIFICATION_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    MODEL_TRAINING_MODE_FIELD_NUMBER: _ClassVar[int]
    model_type: NluSettings.ModelType
    classification_threshold: float
    model_training_mode: NluSettings.ModelTrainingMode

    def __init__(self, model_type: _Optional[_Union[NluSettings.ModelType, str]]=..., classification_threshold: _Optional[float]=..., model_training_mode: _Optional[_Union[NluSettings.ModelTrainingMode, str]]=...) -> None:
        ...

class Flow(_message.Message):
    __slots__ = ('name', 'display_name', 'description', 'transition_routes', 'event_handlers', 'transition_route_groups', 'nlu_settings', 'advanced_settings', 'knowledge_connector_settings', 'multi_language_settings', 'locked')

    class MultiLanguageSettings(_message.Message):
        __slots__ = ('enable_multi_language_detection', 'supported_response_language_codes')
        ENABLE_MULTI_LANGUAGE_DETECTION_FIELD_NUMBER: _ClassVar[int]
        SUPPORTED_RESPONSE_LANGUAGE_CODES_FIELD_NUMBER: _ClassVar[int]
        enable_multi_language_detection: bool
        supported_response_language_codes: _containers.RepeatedScalarFieldContainer[str]

        def __init__(self, enable_multi_language_detection: bool=..., supported_response_language_codes: _Optional[_Iterable[str]]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TRANSITION_ROUTES_FIELD_NUMBER: _ClassVar[int]
    EVENT_HANDLERS_FIELD_NUMBER: _ClassVar[int]
    TRANSITION_ROUTE_GROUPS_FIELD_NUMBER: _ClassVar[int]
    NLU_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    ADVANCED_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    KNOWLEDGE_CONNECTOR_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    MULTI_LANGUAGE_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    LOCKED_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    description: str
    transition_routes: _containers.RepeatedCompositeFieldContainer[_page_pb2.TransitionRoute]
    event_handlers: _containers.RepeatedCompositeFieldContainer[_page_pb2.EventHandler]
    transition_route_groups: _containers.RepeatedScalarFieldContainer[str]
    nlu_settings: NluSettings
    advanced_settings: _advanced_settings_pb2.AdvancedSettings
    knowledge_connector_settings: _page_pb2.KnowledgeConnectorSettings
    multi_language_settings: Flow.MultiLanguageSettings
    locked: bool

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., description: _Optional[str]=..., transition_routes: _Optional[_Iterable[_Union[_page_pb2.TransitionRoute, _Mapping]]]=..., event_handlers: _Optional[_Iterable[_Union[_page_pb2.EventHandler, _Mapping]]]=..., transition_route_groups: _Optional[_Iterable[str]]=..., nlu_settings: _Optional[_Union[NluSettings, _Mapping]]=..., advanced_settings: _Optional[_Union[_advanced_settings_pb2.AdvancedSettings, _Mapping]]=..., knowledge_connector_settings: _Optional[_Union[_page_pb2.KnowledgeConnectorSettings, _Mapping]]=..., multi_language_settings: _Optional[_Union[Flow.MultiLanguageSettings, _Mapping]]=..., locked: bool=...) -> None:
        ...

class CreateFlowRequest(_message.Message):
    __slots__ = ('parent', 'flow', 'language_code')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FLOW_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    flow: Flow
    language_code: str

    def __init__(self, parent: _Optional[str]=..., flow: _Optional[_Union[Flow, _Mapping]]=..., language_code: _Optional[str]=...) -> None:
        ...

class DeleteFlowRequest(_message.Message):
    __slots__ = ('name', 'force')
    NAME_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    force: bool

    def __init__(self, name: _Optional[str]=..., force: bool=...) -> None:
        ...

class ListFlowsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'language_code')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    language_code: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., language_code: _Optional[str]=...) -> None:
        ...

class ListFlowsResponse(_message.Message):
    __slots__ = ('flows', 'next_page_token')
    FLOWS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    flows: _containers.RepeatedCompositeFieldContainer[Flow]
    next_page_token: str

    def __init__(self, flows: _Optional[_Iterable[_Union[Flow, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetFlowRequest(_message.Message):
    __slots__ = ('name', 'language_code')
    NAME_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    name: str
    language_code: str

    def __init__(self, name: _Optional[str]=..., language_code: _Optional[str]=...) -> None:
        ...

class UpdateFlowRequest(_message.Message):
    __slots__ = ('flow', 'update_mask', 'language_code')
    FLOW_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    flow: Flow
    update_mask: _field_mask_pb2.FieldMask
    language_code: str

    def __init__(self, flow: _Optional[_Union[Flow, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., language_code: _Optional[str]=...) -> None:
        ...

class TrainFlowRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ValidateFlowRequest(_message.Message):
    __slots__ = ('name', 'language_code')
    NAME_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    name: str
    language_code: str

    def __init__(self, name: _Optional[str]=..., language_code: _Optional[str]=...) -> None:
        ...

class GetFlowValidationResultRequest(_message.Message):
    __slots__ = ('name', 'language_code')
    NAME_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    name: str
    language_code: str

    def __init__(self, name: _Optional[str]=..., language_code: _Optional[str]=...) -> None:
        ...

class FlowValidationResult(_message.Message):
    __slots__ = ('name', 'validation_messages', 'update_time')
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALIDATION_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    validation_messages: _containers.RepeatedCompositeFieldContainer[_validation_message_pb2.ValidationMessage]
    update_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., validation_messages: _Optional[_Iterable[_Union[_validation_message_pb2.ValidationMessage, _Mapping]]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class ImportFlowRequest(_message.Message):
    __slots__ = ('parent', 'flow_uri', 'flow_content', 'import_option', 'flow_import_strategy')

    class ImportOption(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        IMPORT_OPTION_UNSPECIFIED: _ClassVar[ImportFlowRequest.ImportOption]
        KEEP: _ClassVar[ImportFlowRequest.ImportOption]
        FALLBACK: _ClassVar[ImportFlowRequest.ImportOption]
    IMPORT_OPTION_UNSPECIFIED: ImportFlowRequest.ImportOption
    KEEP: ImportFlowRequest.ImportOption
    FALLBACK: ImportFlowRequest.ImportOption
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FLOW_URI_FIELD_NUMBER: _ClassVar[int]
    FLOW_CONTENT_FIELD_NUMBER: _ClassVar[int]
    IMPORT_OPTION_FIELD_NUMBER: _ClassVar[int]
    FLOW_IMPORT_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    flow_uri: str
    flow_content: bytes
    import_option: ImportFlowRequest.ImportOption
    flow_import_strategy: FlowImportStrategy

    def __init__(self, parent: _Optional[str]=..., flow_uri: _Optional[str]=..., flow_content: _Optional[bytes]=..., import_option: _Optional[_Union[ImportFlowRequest.ImportOption, str]]=..., flow_import_strategy: _Optional[_Union[FlowImportStrategy, _Mapping]]=...) -> None:
        ...

class FlowImportStrategy(_message.Message):
    __slots__ = ('global_import_strategy',)
    GLOBAL_IMPORT_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    global_import_strategy: _import_strategy_pb2.ImportStrategy

    def __init__(self, global_import_strategy: _Optional[_Union[_import_strategy_pb2.ImportStrategy, str]]=...) -> None:
        ...

class ImportFlowResponse(_message.Message):
    __slots__ = ('flow',)
    FLOW_FIELD_NUMBER: _ClassVar[int]
    flow: str

    def __init__(self, flow: _Optional[str]=...) -> None:
        ...

class ExportFlowRequest(_message.Message):
    __slots__ = ('name', 'flow_uri', 'include_referenced_flows')
    NAME_FIELD_NUMBER: _ClassVar[int]
    FLOW_URI_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_REFERENCED_FLOWS_FIELD_NUMBER: _ClassVar[int]
    name: str
    flow_uri: str
    include_referenced_flows: bool

    def __init__(self, name: _Optional[str]=..., flow_uri: _Optional[str]=..., include_referenced_flows: bool=...) -> None:
        ...

class ExportFlowResponse(_message.Message):
    __slots__ = ('flow_uri', 'flow_content')
    FLOW_URI_FIELD_NUMBER: _ClassVar[int]
    FLOW_CONTENT_FIELD_NUMBER: _ClassVar[int]
    flow_uri: str
    flow_content: bytes

    def __init__(self, flow_uri: _Optional[str]=..., flow_content: _Optional[bytes]=...) -> None:
        ...