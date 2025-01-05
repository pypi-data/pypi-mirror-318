from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.retail.v2alpha import common_pb2 as _common_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Model(_message.Message):
    __slots__ = ("page_optimization_config", "name", "display_name", "training_state", "serving_state", "create_time", "update_time", "type", "optimization_objective", "periodic_tuning_state", "last_tune_time", "tuning_operation", "data_state", "filtering_option", "serving_config_lists", "model_features_config")
    class ServingState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SERVING_STATE_UNSPECIFIED: _ClassVar[Model.ServingState]
        INACTIVE: _ClassVar[Model.ServingState]
        ACTIVE: _ClassVar[Model.ServingState]
        TUNED: _ClassVar[Model.ServingState]
    SERVING_STATE_UNSPECIFIED: Model.ServingState
    INACTIVE: Model.ServingState
    ACTIVE: Model.ServingState
    TUNED: Model.ServingState
    class TrainingState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TRAINING_STATE_UNSPECIFIED: _ClassVar[Model.TrainingState]
        PAUSED: _ClassVar[Model.TrainingState]
        TRAINING: _ClassVar[Model.TrainingState]
    TRAINING_STATE_UNSPECIFIED: Model.TrainingState
    PAUSED: Model.TrainingState
    TRAINING: Model.TrainingState
    class PeriodicTuningState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PERIODIC_TUNING_STATE_UNSPECIFIED: _ClassVar[Model.PeriodicTuningState]
        PERIODIC_TUNING_DISABLED: _ClassVar[Model.PeriodicTuningState]
        ALL_TUNING_DISABLED: _ClassVar[Model.PeriodicTuningState]
        PERIODIC_TUNING_ENABLED: _ClassVar[Model.PeriodicTuningState]
    PERIODIC_TUNING_STATE_UNSPECIFIED: Model.PeriodicTuningState
    PERIODIC_TUNING_DISABLED: Model.PeriodicTuningState
    ALL_TUNING_DISABLED: Model.PeriodicTuningState
    PERIODIC_TUNING_ENABLED: Model.PeriodicTuningState
    class DataState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DATA_STATE_UNSPECIFIED: _ClassVar[Model.DataState]
        DATA_OK: _ClassVar[Model.DataState]
        DATA_ERROR: _ClassVar[Model.DataState]
    DATA_STATE_UNSPECIFIED: Model.DataState
    DATA_OK: Model.DataState
    DATA_ERROR: Model.DataState
    class ContextProductsType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CONTEXT_PRODUCTS_TYPE_UNSPECIFIED: _ClassVar[Model.ContextProductsType]
        SINGLE_CONTEXT_PRODUCT: _ClassVar[Model.ContextProductsType]
        MULTIPLE_CONTEXT_PRODUCTS: _ClassVar[Model.ContextProductsType]
    CONTEXT_PRODUCTS_TYPE_UNSPECIFIED: Model.ContextProductsType
    SINGLE_CONTEXT_PRODUCT: Model.ContextProductsType
    MULTIPLE_CONTEXT_PRODUCTS: Model.ContextProductsType
    class PageOptimizationConfig(_message.Message):
        __slots__ = ("page_optimization_event_type", "panels", "restriction")
        class Restriction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            RESTRICTION_UNSPECIFIED: _ClassVar[Model.PageOptimizationConfig.Restriction]
            NO_RESTRICTION: _ClassVar[Model.PageOptimizationConfig.Restriction]
            UNIQUE_SERVING_CONFIG_RESTRICTION: _ClassVar[Model.PageOptimizationConfig.Restriction]
            UNIQUE_MODEL_RESTRICTION: _ClassVar[Model.PageOptimizationConfig.Restriction]
            UNIQUE_MODEL_TYPE_RESTRICTION: _ClassVar[Model.PageOptimizationConfig.Restriction]
        RESTRICTION_UNSPECIFIED: Model.PageOptimizationConfig.Restriction
        NO_RESTRICTION: Model.PageOptimizationConfig.Restriction
        UNIQUE_SERVING_CONFIG_RESTRICTION: Model.PageOptimizationConfig.Restriction
        UNIQUE_MODEL_RESTRICTION: Model.PageOptimizationConfig.Restriction
        UNIQUE_MODEL_TYPE_RESTRICTION: Model.PageOptimizationConfig.Restriction
        class Candidate(_message.Message):
            __slots__ = ("serving_config_id",)
            SERVING_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
            serving_config_id: str
            def __init__(self, serving_config_id: _Optional[str] = ...) -> None: ...
        class Panel(_message.Message):
            __slots__ = ("display_name", "candidates", "default_candidate")
            DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
            CANDIDATES_FIELD_NUMBER: _ClassVar[int]
            DEFAULT_CANDIDATE_FIELD_NUMBER: _ClassVar[int]
            display_name: str
            candidates: _containers.RepeatedCompositeFieldContainer[Model.PageOptimizationConfig.Candidate]
            default_candidate: Model.PageOptimizationConfig.Candidate
            def __init__(self, display_name: _Optional[str] = ..., candidates: _Optional[_Iterable[_Union[Model.PageOptimizationConfig.Candidate, _Mapping]]] = ..., default_candidate: _Optional[_Union[Model.PageOptimizationConfig.Candidate, _Mapping]] = ...) -> None: ...
        PAGE_OPTIMIZATION_EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
        PANELS_FIELD_NUMBER: _ClassVar[int]
        RESTRICTION_FIELD_NUMBER: _ClassVar[int]
        page_optimization_event_type: str
        panels: _containers.RepeatedCompositeFieldContainer[Model.PageOptimizationConfig.Panel]
        restriction: Model.PageOptimizationConfig.Restriction
        def __init__(self, page_optimization_event_type: _Optional[str] = ..., panels: _Optional[_Iterable[_Union[Model.PageOptimizationConfig.Panel, _Mapping]]] = ..., restriction: _Optional[_Union[Model.PageOptimizationConfig.Restriction, str]] = ...) -> None: ...
    class ServingConfigList(_message.Message):
        __slots__ = ("serving_config_ids",)
        SERVING_CONFIG_IDS_FIELD_NUMBER: _ClassVar[int]
        serving_config_ids: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, serving_config_ids: _Optional[_Iterable[str]] = ...) -> None: ...
    class FrequentlyBoughtTogetherFeaturesConfig(_message.Message):
        __slots__ = ("context_products_type",)
        CONTEXT_PRODUCTS_TYPE_FIELD_NUMBER: _ClassVar[int]
        context_products_type: Model.ContextProductsType
        def __init__(self, context_products_type: _Optional[_Union[Model.ContextProductsType, str]] = ...) -> None: ...
    class ModelFeaturesConfig(_message.Message):
        __slots__ = ("frequently_bought_together_config", "llm_embedding_config")
        class LlmEmbeddingConfig(_message.Message):
            __slots__ = ("llm_embedding_version",)
            LLM_EMBEDDING_VERSION_FIELD_NUMBER: _ClassVar[int]
            llm_embedding_version: str
            def __init__(self, llm_embedding_version: _Optional[str] = ...) -> None: ...
        FREQUENTLY_BOUGHT_TOGETHER_CONFIG_FIELD_NUMBER: _ClassVar[int]
        LLM_EMBEDDING_CONFIG_FIELD_NUMBER: _ClassVar[int]
        frequently_bought_together_config: Model.FrequentlyBoughtTogetherFeaturesConfig
        llm_embedding_config: Model.ModelFeaturesConfig.LlmEmbeddingConfig
        def __init__(self, frequently_bought_together_config: _Optional[_Union[Model.FrequentlyBoughtTogetherFeaturesConfig, _Mapping]] = ..., llm_embedding_config: _Optional[_Union[Model.ModelFeaturesConfig.LlmEmbeddingConfig, _Mapping]] = ...) -> None: ...
    PAGE_OPTIMIZATION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    TRAINING_STATE_FIELD_NUMBER: _ClassVar[int]
    SERVING_STATE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    OPTIMIZATION_OBJECTIVE_FIELD_NUMBER: _ClassVar[int]
    PERIODIC_TUNING_STATE_FIELD_NUMBER: _ClassVar[int]
    LAST_TUNE_TIME_FIELD_NUMBER: _ClassVar[int]
    TUNING_OPERATION_FIELD_NUMBER: _ClassVar[int]
    DATA_STATE_FIELD_NUMBER: _ClassVar[int]
    FILTERING_OPTION_FIELD_NUMBER: _ClassVar[int]
    SERVING_CONFIG_LISTS_FIELD_NUMBER: _ClassVar[int]
    MODEL_FEATURES_CONFIG_FIELD_NUMBER: _ClassVar[int]
    page_optimization_config: Model.PageOptimizationConfig
    name: str
    display_name: str
    training_state: Model.TrainingState
    serving_state: Model.ServingState
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    type: str
    optimization_objective: str
    periodic_tuning_state: Model.PeriodicTuningState
    last_tune_time: _timestamp_pb2.Timestamp
    tuning_operation: str
    data_state: Model.DataState
    filtering_option: _common_pb2.RecommendationsFilteringOption
    serving_config_lists: _containers.RepeatedCompositeFieldContainer[Model.ServingConfigList]
    model_features_config: Model.ModelFeaturesConfig
    def __init__(self, page_optimization_config: _Optional[_Union[Model.PageOptimizationConfig, _Mapping]] = ..., name: _Optional[str] = ..., display_name: _Optional[str] = ..., training_state: _Optional[_Union[Model.TrainingState, str]] = ..., serving_state: _Optional[_Union[Model.ServingState, str]] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., type: _Optional[str] = ..., optimization_objective: _Optional[str] = ..., periodic_tuning_state: _Optional[_Union[Model.PeriodicTuningState, str]] = ..., last_tune_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., tuning_operation: _Optional[str] = ..., data_state: _Optional[_Union[Model.DataState, str]] = ..., filtering_option: _Optional[_Union[_common_pb2.RecommendationsFilteringOption, str]] = ..., serving_config_lists: _Optional[_Iterable[_Union[Model.ServingConfigList, _Mapping]]] = ..., model_features_config: _Optional[_Union[Model.ModelFeaturesConfig, _Mapping]] = ...) -> None: ...
