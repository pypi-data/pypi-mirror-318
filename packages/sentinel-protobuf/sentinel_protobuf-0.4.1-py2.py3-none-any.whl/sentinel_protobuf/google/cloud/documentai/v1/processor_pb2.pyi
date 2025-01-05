from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.documentai.v1 import document_schema_pb2 as _document_schema_pb2
from google.cloud.documentai.v1 import evaluation_pb2 as _evaluation_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ProcessorVersion(_message.Message):
    __slots__ = ('name', 'display_name', 'document_schema', 'state', 'create_time', 'latest_evaluation', 'kms_key_name', 'kms_key_version_name', 'google_managed', 'deprecation_info', 'model_type', 'satisfies_pzs', 'satisfies_pzi', 'gen_ai_model_info')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[ProcessorVersion.State]
        DEPLOYED: _ClassVar[ProcessorVersion.State]
        DEPLOYING: _ClassVar[ProcessorVersion.State]
        UNDEPLOYED: _ClassVar[ProcessorVersion.State]
        UNDEPLOYING: _ClassVar[ProcessorVersion.State]
        CREATING: _ClassVar[ProcessorVersion.State]
        DELETING: _ClassVar[ProcessorVersion.State]
        FAILED: _ClassVar[ProcessorVersion.State]
        IMPORTING: _ClassVar[ProcessorVersion.State]
    STATE_UNSPECIFIED: ProcessorVersion.State
    DEPLOYED: ProcessorVersion.State
    DEPLOYING: ProcessorVersion.State
    UNDEPLOYED: ProcessorVersion.State
    UNDEPLOYING: ProcessorVersion.State
    CREATING: ProcessorVersion.State
    DELETING: ProcessorVersion.State
    FAILED: ProcessorVersion.State
    IMPORTING: ProcessorVersion.State

    class ModelType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MODEL_TYPE_UNSPECIFIED: _ClassVar[ProcessorVersion.ModelType]
        MODEL_TYPE_GENERATIVE: _ClassVar[ProcessorVersion.ModelType]
        MODEL_TYPE_CUSTOM: _ClassVar[ProcessorVersion.ModelType]
    MODEL_TYPE_UNSPECIFIED: ProcessorVersion.ModelType
    MODEL_TYPE_GENERATIVE: ProcessorVersion.ModelType
    MODEL_TYPE_CUSTOM: ProcessorVersion.ModelType

    class DeprecationInfo(_message.Message):
        __slots__ = ('deprecation_time', 'replacement_processor_version')
        DEPRECATION_TIME_FIELD_NUMBER: _ClassVar[int]
        REPLACEMENT_PROCESSOR_VERSION_FIELD_NUMBER: _ClassVar[int]
        deprecation_time: _timestamp_pb2.Timestamp
        replacement_processor_version: str

        def __init__(self, deprecation_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., replacement_processor_version: _Optional[str]=...) -> None:
            ...

    class GenAiModelInfo(_message.Message):
        __slots__ = ('foundation_gen_ai_model_info', 'custom_gen_ai_model_info')

        class FoundationGenAiModelInfo(_message.Message):
            __slots__ = ('finetuning_allowed', 'min_train_labeled_documents')
            FINETUNING_ALLOWED_FIELD_NUMBER: _ClassVar[int]
            MIN_TRAIN_LABELED_DOCUMENTS_FIELD_NUMBER: _ClassVar[int]
            finetuning_allowed: bool
            min_train_labeled_documents: int

            def __init__(self, finetuning_allowed: bool=..., min_train_labeled_documents: _Optional[int]=...) -> None:
                ...

        class CustomGenAiModelInfo(_message.Message):
            __slots__ = ('custom_model_type', 'base_processor_version_id')

            class CustomModelType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                CUSTOM_MODEL_TYPE_UNSPECIFIED: _ClassVar[ProcessorVersion.GenAiModelInfo.CustomGenAiModelInfo.CustomModelType]
                VERSIONED_FOUNDATION: _ClassVar[ProcessorVersion.GenAiModelInfo.CustomGenAiModelInfo.CustomModelType]
                FINE_TUNED: _ClassVar[ProcessorVersion.GenAiModelInfo.CustomGenAiModelInfo.CustomModelType]
            CUSTOM_MODEL_TYPE_UNSPECIFIED: ProcessorVersion.GenAiModelInfo.CustomGenAiModelInfo.CustomModelType
            VERSIONED_FOUNDATION: ProcessorVersion.GenAiModelInfo.CustomGenAiModelInfo.CustomModelType
            FINE_TUNED: ProcessorVersion.GenAiModelInfo.CustomGenAiModelInfo.CustomModelType
            CUSTOM_MODEL_TYPE_FIELD_NUMBER: _ClassVar[int]
            BASE_PROCESSOR_VERSION_ID_FIELD_NUMBER: _ClassVar[int]
            custom_model_type: ProcessorVersion.GenAiModelInfo.CustomGenAiModelInfo.CustomModelType
            base_processor_version_id: str

            def __init__(self, custom_model_type: _Optional[_Union[ProcessorVersion.GenAiModelInfo.CustomGenAiModelInfo.CustomModelType, str]]=..., base_processor_version_id: _Optional[str]=...) -> None:
                ...
        FOUNDATION_GEN_AI_MODEL_INFO_FIELD_NUMBER: _ClassVar[int]
        CUSTOM_GEN_AI_MODEL_INFO_FIELD_NUMBER: _ClassVar[int]
        foundation_gen_ai_model_info: ProcessorVersion.GenAiModelInfo.FoundationGenAiModelInfo
        custom_gen_ai_model_info: ProcessorVersion.GenAiModelInfo.CustomGenAiModelInfo

        def __init__(self, foundation_gen_ai_model_info: _Optional[_Union[ProcessorVersion.GenAiModelInfo.FoundationGenAiModelInfo, _Mapping]]=..., custom_gen_ai_model_info: _Optional[_Union[ProcessorVersion.GenAiModelInfo.CustomGenAiModelInfo, _Mapping]]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LATEST_EVALUATION_FIELD_NUMBER: _ClassVar[int]
    KMS_KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    KMS_KEY_VERSION_NAME_FIELD_NUMBER: _ClassVar[int]
    GOOGLE_MANAGED_FIELD_NUMBER: _ClassVar[int]
    DEPRECATION_INFO_FIELD_NUMBER: _ClassVar[int]
    MODEL_TYPE_FIELD_NUMBER: _ClassVar[int]
    SATISFIES_PZS_FIELD_NUMBER: _ClassVar[int]
    SATISFIES_PZI_FIELD_NUMBER: _ClassVar[int]
    GEN_AI_MODEL_INFO_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    document_schema: _document_schema_pb2.DocumentSchema
    state: ProcessorVersion.State
    create_time: _timestamp_pb2.Timestamp
    latest_evaluation: _evaluation_pb2.EvaluationReference
    kms_key_name: str
    kms_key_version_name: str
    google_managed: bool
    deprecation_info: ProcessorVersion.DeprecationInfo
    model_type: ProcessorVersion.ModelType
    satisfies_pzs: bool
    satisfies_pzi: bool
    gen_ai_model_info: ProcessorVersion.GenAiModelInfo

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., document_schema: _Optional[_Union[_document_schema_pb2.DocumentSchema, _Mapping]]=..., state: _Optional[_Union[ProcessorVersion.State, str]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., latest_evaluation: _Optional[_Union[_evaluation_pb2.EvaluationReference, _Mapping]]=..., kms_key_name: _Optional[str]=..., kms_key_version_name: _Optional[str]=..., google_managed: bool=..., deprecation_info: _Optional[_Union[ProcessorVersion.DeprecationInfo, _Mapping]]=..., model_type: _Optional[_Union[ProcessorVersion.ModelType, str]]=..., satisfies_pzs: bool=..., satisfies_pzi: bool=..., gen_ai_model_info: _Optional[_Union[ProcessorVersion.GenAiModelInfo, _Mapping]]=...) -> None:
        ...

class ProcessorVersionAlias(_message.Message):
    __slots__ = ('alias', 'processor_version')
    ALIAS_FIELD_NUMBER: _ClassVar[int]
    PROCESSOR_VERSION_FIELD_NUMBER: _ClassVar[int]
    alias: str
    processor_version: str

    def __init__(self, alias: _Optional[str]=..., processor_version: _Optional[str]=...) -> None:
        ...

class Processor(_message.Message):
    __slots__ = ('name', 'type', 'display_name', 'state', 'default_processor_version', 'processor_version_aliases', 'process_endpoint', 'create_time', 'kms_key_name', 'satisfies_pzs', 'satisfies_pzi')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Processor.State]
        ENABLED: _ClassVar[Processor.State]
        DISABLED: _ClassVar[Processor.State]
        ENABLING: _ClassVar[Processor.State]
        DISABLING: _ClassVar[Processor.State]
        CREATING: _ClassVar[Processor.State]
        FAILED: _ClassVar[Processor.State]
        DELETING: _ClassVar[Processor.State]
    STATE_UNSPECIFIED: Processor.State
    ENABLED: Processor.State
    DISABLED: Processor.State
    ENABLING: Processor.State
    DISABLING: Processor.State
    CREATING: Processor.State
    FAILED: Processor.State
    DELETING: Processor.State
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_PROCESSOR_VERSION_FIELD_NUMBER: _ClassVar[int]
    PROCESSOR_VERSION_ALIASES_FIELD_NUMBER: _ClassVar[int]
    PROCESS_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    KMS_KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    SATISFIES_PZS_FIELD_NUMBER: _ClassVar[int]
    SATISFIES_PZI_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: str
    display_name: str
    state: Processor.State
    default_processor_version: str
    processor_version_aliases: _containers.RepeatedCompositeFieldContainer[ProcessorVersionAlias]
    process_endpoint: str
    create_time: _timestamp_pb2.Timestamp
    kms_key_name: str
    satisfies_pzs: bool
    satisfies_pzi: bool

    def __init__(self, name: _Optional[str]=..., type: _Optional[str]=..., display_name: _Optional[str]=..., state: _Optional[_Union[Processor.State, str]]=..., default_processor_version: _Optional[str]=..., processor_version_aliases: _Optional[_Iterable[_Union[ProcessorVersionAlias, _Mapping]]]=..., process_endpoint: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., kms_key_name: _Optional[str]=..., satisfies_pzs: bool=..., satisfies_pzi: bool=...) -> None:
        ...