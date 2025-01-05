from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ConversationModel(_message.Message):
    __slots__ = ("name", "display_name", "create_time", "datasets", "state", "language_code", "article_suggestion_model_metadata", "smart_reply_model_metadata", "satisfies_pzs", "satisfies_pzi")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[ConversationModel.State]
        CREATING: _ClassVar[ConversationModel.State]
        UNDEPLOYED: _ClassVar[ConversationModel.State]
        DEPLOYING: _ClassVar[ConversationModel.State]
        DEPLOYED: _ClassVar[ConversationModel.State]
        UNDEPLOYING: _ClassVar[ConversationModel.State]
        DELETING: _ClassVar[ConversationModel.State]
        FAILED: _ClassVar[ConversationModel.State]
        PENDING: _ClassVar[ConversationModel.State]
    STATE_UNSPECIFIED: ConversationModel.State
    CREATING: ConversationModel.State
    UNDEPLOYED: ConversationModel.State
    DEPLOYING: ConversationModel.State
    DEPLOYED: ConversationModel.State
    UNDEPLOYING: ConversationModel.State
    DELETING: ConversationModel.State
    FAILED: ConversationModel.State
    PENDING: ConversationModel.State
    class ModelType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MODEL_TYPE_UNSPECIFIED: _ClassVar[ConversationModel.ModelType]
        SMART_REPLY_DUAL_ENCODER_MODEL: _ClassVar[ConversationModel.ModelType]
        SMART_REPLY_BERT_MODEL: _ClassVar[ConversationModel.ModelType]
    MODEL_TYPE_UNSPECIFIED: ConversationModel.ModelType
    SMART_REPLY_DUAL_ENCODER_MODEL: ConversationModel.ModelType
    SMART_REPLY_BERT_MODEL: ConversationModel.ModelType
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DATASETS_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    ARTICLE_SUGGESTION_MODEL_METADATA_FIELD_NUMBER: _ClassVar[int]
    SMART_REPLY_MODEL_METADATA_FIELD_NUMBER: _ClassVar[int]
    SATISFIES_PZS_FIELD_NUMBER: _ClassVar[int]
    SATISFIES_PZI_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    create_time: _timestamp_pb2.Timestamp
    datasets: _containers.RepeatedCompositeFieldContainer[InputDataset]
    state: ConversationModel.State
    language_code: str
    article_suggestion_model_metadata: ArticleSuggestionModelMetadata
    smart_reply_model_metadata: SmartReplyModelMetadata
    satisfies_pzs: bool
    satisfies_pzi: bool
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., datasets: _Optional[_Iterable[_Union[InputDataset, _Mapping]]] = ..., state: _Optional[_Union[ConversationModel.State, str]] = ..., language_code: _Optional[str] = ..., article_suggestion_model_metadata: _Optional[_Union[ArticleSuggestionModelMetadata, _Mapping]] = ..., smart_reply_model_metadata: _Optional[_Union[SmartReplyModelMetadata, _Mapping]] = ..., satisfies_pzs: bool = ..., satisfies_pzi: bool = ...) -> None: ...

class ConversationModelEvaluation(_message.Message):
    __slots__ = ("name", "display_name", "evaluation_config", "create_time", "smart_reply_metrics", "raw_human_eval_template_csv")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    EVALUATION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    SMART_REPLY_METRICS_FIELD_NUMBER: _ClassVar[int]
    RAW_HUMAN_EVAL_TEMPLATE_CSV_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    evaluation_config: EvaluationConfig
    create_time: _timestamp_pb2.Timestamp
    smart_reply_metrics: SmartReplyMetrics
    raw_human_eval_template_csv: str
    def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., evaluation_config: _Optional[_Union[EvaluationConfig, _Mapping]] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., smart_reply_metrics: _Optional[_Union[SmartReplyMetrics, _Mapping]] = ..., raw_human_eval_template_csv: _Optional[str] = ...) -> None: ...

class EvaluationConfig(_message.Message):
    __slots__ = ("datasets", "smart_reply_config", "smart_compose_config")
    class SmartReplyConfig(_message.Message):
        __slots__ = ("allowlist_document", "max_result_count")
        ALLOWLIST_DOCUMENT_FIELD_NUMBER: _ClassVar[int]
        MAX_RESULT_COUNT_FIELD_NUMBER: _ClassVar[int]
        allowlist_document: str
        max_result_count: int
        def __init__(self, allowlist_document: _Optional[str] = ..., max_result_count: _Optional[int] = ...) -> None: ...
    class SmartComposeConfig(_message.Message):
        __slots__ = ("allowlist_document", "max_result_count")
        ALLOWLIST_DOCUMENT_FIELD_NUMBER: _ClassVar[int]
        MAX_RESULT_COUNT_FIELD_NUMBER: _ClassVar[int]
        allowlist_document: str
        max_result_count: int
        def __init__(self, allowlist_document: _Optional[str] = ..., max_result_count: _Optional[int] = ...) -> None: ...
    DATASETS_FIELD_NUMBER: _ClassVar[int]
    SMART_REPLY_CONFIG_FIELD_NUMBER: _ClassVar[int]
    SMART_COMPOSE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    datasets: _containers.RepeatedCompositeFieldContainer[InputDataset]
    smart_reply_config: EvaluationConfig.SmartReplyConfig
    smart_compose_config: EvaluationConfig.SmartComposeConfig
    def __init__(self, datasets: _Optional[_Iterable[_Union[InputDataset, _Mapping]]] = ..., smart_reply_config: _Optional[_Union[EvaluationConfig.SmartReplyConfig, _Mapping]] = ..., smart_compose_config: _Optional[_Union[EvaluationConfig.SmartComposeConfig, _Mapping]] = ...) -> None: ...

class InputDataset(_message.Message):
    __slots__ = ("dataset",)
    DATASET_FIELD_NUMBER: _ClassVar[int]
    dataset: str
    def __init__(self, dataset: _Optional[str] = ...) -> None: ...

class ArticleSuggestionModelMetadata(_message.Message):
    __slots__ = ("training_model_type",)
    TRAINING_MODEL_TYPE_FIELD_NUMBER: _ClassVar[int]
    training_model_type: ConversationModel.ModelType
    def __init__(self, training_model_type: _Optional[_Union[ConversationModel.ModelType, str]] = ...) -> None: ...

class SmartReplyModelMetadata(_message.Message):
    __slots__ = ("training_model_type",)
    TRAINING_MODEL_TYPE_FIELD_NUMBER: _ClassVar[int]
    training_model_type: ConversationModel.ModelType
    def __init__(self, training_model_type: _Optional[_Union[ConversationModel.ModelType, str]] = ...) -> None: ...

class SmartReplyMetrics(_message.Message):
    __slots__ = ("allowlist_coverage", "top_n_metrics", "conversation_count")
    class TopNMetrics(_message.Message):
        __slots__ = ("n", "recall")
        N_FIELD_NUMBER: _ClassVar[int]
        RECALL_FIELD_NUMBER: _ClassVar[int]
        n: int
        recall: float
        def __init__(self, n: _Optional[int] = ..., recall: _Optional[float] = ...) -> None: ...
    ALLOWLIST_COVERAGE_FIELD_NUMBER: _ClassVar[int]
    TOP_N_METRICS_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_COUNT_FIELD_NUMBER: _ClassVar[int]
    allowlist_coverage: float
    top_n_metrics: _containers.RepeatedCompositeFieldContainer[SmartReplyMetrics.TopNMetrics]
    conversation_count: int
    def __init__(self, allowlist_coverage: _Optional[float] = ..., top_n_metrics: _Optional[_Iterable[_Union[SmartReplyMetrics.TopNMetrics, _Mapping]]] = ..., conversation_count: _Optional[int] = ...) -> None: ...

class CreateConversationModelRequest(_message.Message):
    __slots__ = ("parent", "conversation_model")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_MODEL_FIELD_NUMBER: _ClassVar[int]
    parent: str
    conversation_model: ConversationModel
    def __init__(self, parent: _Optional[str] = ..., conversation_model: _Optional[_Union[ConversationModel, _Mapping]] = ...) -> None: ...

class GetConversationModelRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListConversationModelsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListConversationModelsResponse(_message.Message):
    __slots__ = ("conversation_models", "next_page_token")
    CONVERSATION_MODELS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    conversation_models: _containers.RepeatedCompositeFieldContainer[ConversationModel]
    next_page_token: str
    def __init__(self, conversation_models: _Optional[_Iterable[_Union[ConversationModel, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class DeleteConversationModelRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class DeployConversationModelRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class UndeployConversationModelRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class GetConversationModelEvaluationRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListConversationModelEvaluationsRequest(_message.Message):
    __slots__ = ("parent", "page_size", "page_token")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    def __init__(self, parent: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListConversationModelEvaluationsResponse(_message.Message):
    __slots__ = ("conversation_model_evaluations", "next_page_token")
    CONVERSATION_MODEL_EVALUATIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    conversation_model_evaluations: _containers.RepeatedCompositeFieldContainer[ConversationModelEvaluation]
    next_page_token: str
    def __init__(self, conversation_model_evaluations: _Optional[_Iterable[_Union[ConversationModelEvaluation, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class CreateConversationModelEvaluationRequest(_message.Message):
    __slots__ = ("parent", "conversation_model_evaluation")
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_MODEL_EVALUATION_FIELD_NUMBER: _ClassVar[int]
    parent: str
    conversation_model_evaluation: ConversationModelEvaluation
    def __init__(self, parent: _Optional[str] = ..., conversation_model_evaluation: _Optional[_Union[ConversationModelEvaluation, _Mapping]] = ...) -> None: ...

class CreateConversationModelOperationMetadata(_message.Message):
    __slots__ = ("conversation_model", "state", "create_time")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[CreateConversationModelOperationMetadata.State]
        PENDING: _ClassVar[CreateConversationModelOperationMetadata.State]
        SUCCEEDED: _ClassVar[CreateConversationModelOperationMetadata.State]
        FAILED: _ClassVar[CreateConversationModelOperationMetadata.State]
        CANCELLED: _ClassVar[CreateConversationModelOperationMetadata.State]
        CANCELLING: _ClassVar[CreateConversationModelOperationMetadata.State]
        TRAINING: _ClassVar[CreateConversationModelOperationMetadata.State]
    STATE_UNSPECIFIED: CreateConversationModelOperationMetadata.State
    PENDING: CreateConversationModelOperationMetadata.State
    SUCCEEDED: CreateConversationModelOperationMetadata.State
    FAILED: CreateConversationModelOperationMetadata.State
    CANCELLED: CreateConversationModelOperationMetadata.State
    CANCELLING: CreateConversationModelOperationMetadata.State
    TRAINING: CreateConversationModelOperationMetadata.State
    CONVERSATION_MODEL_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    conversation_model: str
    state: CreateConversationModelOperationMetadata.State
    create_time: _timestamp_pb2.Timestamp
    def __init__(self, conversation_model: _Optional[str] = ..., state: _Optional[_Union[CreateConversationModelOperationMetadata.State, str]] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class DeployConversationModelOperationMetadata(_message.Message):
    __slots__ = ("conversation_model", "create_time")
    CONVERSATION_MODEL_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    conversation_model: str
    create_time: _timestamp_pb2.Timestamp
    def __init__(self, conversation_model: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class UndeployConversationModelOperationMetadata(_message.Message):
    __slots__ = ("conversation_model", "create_time")
    CONVERSATION_MODEL_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    conversation_model: str
    create_time: _timestamp_pb2.Timestamp
    def __init__(self, conversation_model: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class DeleteConversationModelOperationMetadata(_message.Message):
    __slots__ = ("conversation_model", "create_time")
    CONVERSATION_MODEL_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    conversation_model: str
    create_time: _timestamp_pb2.Timestamp
    def __init__(self, conversation_model: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class CreateConversationModelEvaluationOperationMetadata(_message.Message):
    __slots__ = ("conversation_model_evaluation", "conversation_model", "state", "create_time")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[CreateConversationModelEvaluationOperationMetadata.State]
        INITIALIZING: _ClassVar[CreateConversationModelEvaluationOperationMetadata.State]
        RUNNING: _ClassVar[CreateConversationModelEvaluationOperationMetadata.State]
        CANCELLED: _ClassVar[CreateConversationModelEvaluationOperationMetadata.State]
        SUCCEEDED: _ClassVar[CreateConversationModelEvaluationOperationMetadata.State]
        FAILED: _ClassVar[CreateConversationModelEvaluationOperationMetadata.State]
    STATE_UNSPECIFIED: CreateConversationModelEvaluationOperationMetadata.State
    INITIALIZING: CreateConversationModelEvaluationOperationMetadata.State
    RUNNING: CreateConversationModelEvaluationOperationMetadata.State
    CANCELLED: CreateConversationModelEvaluationOperationMetadata.State
    SUCCEEDED: CreateConversationModelEvaluationOperationMetadata.State
    FAILED: CreateConversationModelEvaluationOperationMetadata.State
    CONVERSATION_MODEL_EVALUATION_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_MODEL_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    conversation_model_evaluation: str
    conversation_model: str
    state: CreateConversationModelEvaluationOperationMetadata.State
    create_time: _timestamp_pb2.Timestamp
    def __init__(self, conversation_model_evaluation: _Optional[str] = ..., conversation_model: _Optional[str] = ..., state: _Optional[_Union[CreateConversationModelEvaluationOperationMetadata.State, str]] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
