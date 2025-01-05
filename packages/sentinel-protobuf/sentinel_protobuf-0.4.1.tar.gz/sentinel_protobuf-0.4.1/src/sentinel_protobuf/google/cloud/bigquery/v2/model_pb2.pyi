from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.cloud.bigquery.v2 import encryption_config_pb2 as _encryption_config_pb2
from google.cloud.bigquery.v2 import model_reference_pb2 as _model_reference_pb2
from google.cloud.bigquery.v2 import standard_sql_pb2 as _standard_sql_pb2
from google.cloud.bigquery.v2 import table_reference_pb2 as _table_reference_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RemoteModelInfo(_message.Message):
    __slots__ = ("endpoint", "remote_service_type", "connection", "max_batching_rows", "remote_model_version", "speech_recognizer")
    class RemoteServiceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        REMOTE_SERVICE_TYPE_UNSPECIFIED: _ClassVar[RemoteModelInfo.RemoteServiceType]
        CLOUD_AI_TRANSLATE_V3: _ClassVar[RemoteModelInfo.RemoteServiceType]
        CLOUD_AI_VISION_V1: _ClassVar[RemoteModelInfo.RemoteServiceType]
        CLOUD_AI_NATURAL_LANGUAGE_V1: _ClassVar[RemoteModelInfo.RemoteServiceType]
        CLOUD_AI_SPEECH_TO_TEXT_V2: _ClassVar[RemoteModelInfo.RemoteServiceType]
    REMOTE_SERVICE_TYPE_UNSPECIFIED: RemoteModelInfo.RemoteServiceType
    CLOUD_AI_TRANSLATE_V3: RemoteModelInfo.RemoteServiceType
    CLOUD_AI_VISION_V1: RemoteModelInfo.RemoteServiceType
    CLOUD_AI_NATURAL_LANGUAGE_V1: RemoteModelInfo.RemoteServiceType
    CLOUD_AI_SPEECH_TO_TEXT_V2: RemoteModelInfo.RemoteServiceType
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    REMOTE_SERVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_FIELD_NUMBER: _ClassVar[int]
    MAX_BATCHING_ROWS_FIELD_NUMBER: _ClassVar[int]
    REMOTE_MODEL_VERSION_FIELD_NUMBER: _ClassVar[int]
    SPEECH_RECOGNIZER_FIELD_NUMBER: _ClassVar[int]
    endpoint: str
    remote_service_type: RemoteModelInfo.RemoteServiceType
    connection: str
    max_batching_rows: int
    remote_model_version: str
    speech_recognizer: str
    def __init__(self, endpoint: _Optional[str] = ..., remote_service_type: _Optional[_Union[RemoteModelInfo.RemoteServiceType, str]] = ..., connection: _Optional[str] = ..., max_batching_rows: _Optional[int] = ..., remote_model_version: _Optional[str] = ..., speech_recognizer: _Optional[str] = ...) -> None: ...

class TransformColumn(_message.Message):
    __slots__ = ("name", "type", "transform_sql")
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    TRANSFORM_SQL_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: _standard_sql_pb2.StandardSqlDataType
    transform_sql: str
    def __init__(self, name: _Optional[str] = ..., type: _Optional[_Union[_standard_sql_pb2.StandardSqlDataType, _Mapping]] = ..., transform_sql: _Optional[str] = ...) -> None: ...

class Model(_message.Message):
    __slots__ = ("etag", "model_reference", "creation_time", "last_modified_time", "description", "friendly_name", "labels", "expiration_time", "location", "encryption_configuration", "model_type", "training_runs", "feature_columns", "label_columns", "transform_columns", "hparam_search_spaces", "default_trial_id", "hparam_trials", "optimal_trial_ids", "remote_model_info")
    class ModelType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MODEL_TYPE_UNSPECIFIED: _ClassVar[Model.ModelType]
        LINEAR_REGRESSION: _ClassVar[Model.ModelType]
        LOGISTIC_REGRESSION: _ClassVar[Model.ModelType]
        KMEANS: _ClassVar[Model.ModelType]
        MATRIX_FACTORIZATION: _ClassVar[Model.ModelType]
        DNN_CLASSIFIER: _ClassVar[Model.ModelType]
        TENSORFLOW: _ClassVar[Model.ModelType]
        DNN_REGRESSOR: _ClassVar[Model.ModelType]
        XGBOOST: _ClassVar[Model.ModelType]
        BOOSTED_TREE_REGRESSOR: _ClassVar[Model.ModelType]
        BOOSTED_TREE_CLASSIFIER: _ClassVar[Model.ModelType]
        ARIMA: _ClassVar[Model.ModelType]
        AUTOML_REGRESSOR: _ClassVar[Model.ModelType]
        AUTOML_CLASSIFIER: _ClassVar[Model.ModelType]
        PCA: _ClassVar[Model.ModelType]
        DNN_LINEAR_COMBINED_CLASSIFIER: _ClassVar[Model.ModelType]
        DNN_LINEAR_COMBINED_REGRESSOR: _ClassVar[Model.ModelType]
        AUTOENCODER: _ClassVar[Model.ModelType]
        ARIMA_PLUS: _ClassVar[Model.ModelType]
        ARIMA_PLUS_XREG: _ClassVar[Model.ModelType]
        RANDOM_FOREST_REGRESSOR: _ClassVar[Model.ModelType]
        RANDOM_FOREST_CLASSIFIER: _ClassVar[Model.ModelType]
        TENSORFLOW_LITE: _ClassVar[Model.ModelType]
        ONNX: _ClassVar[Model.ModelType]
        TRANSFORM_ONLY: _ClassVar[Model.ModelType]
        CONTRIBUTION_ANALYSIS: _ClassVar[Model.ModelType]
    MODEL_TYPE_UNSPECIFIED: Model.ModelType
    LINEAR_REGRESSION: Model.ModelType
    LOGISTIC_REGRESSION: Model.ModelType
    KMEANS: Model.ModelType
    MATRIX_FACTORIZATION: Model.ModelType
    DNN_CLASSIFIER: Model.ModelType
    TENSORFLOW: Model.ModelType
    DNN_REGRESSOR: Model.ModelType
    XGBOOST: Model.ModelType
    BOOSTED_TREE_REGRESSOR: Model.ModelType
    BOOSTED_TREE_CLASSIFIER: Model.ModelType
    ARIMA: Model.ModelType
    AUTOML_REGRESSOR: Model.ModelType
    AUTOML_CLASSIFIER: Model.ModelType
    PCA: Model.ModelType
    DNN_LINEAR_COMBINED_CLASSIFIER: Model.ModelType
    DNN_LINEAR_COMBINED_REGRESSOR: Model.ModelType
    AUTOENCODER: Model.ModelType
    ARIMA_PLUS: Model.ModelType
    ARIMA_PLUS_XREG: Model.ModelType
    RANDOM_FOREST_REGRESSOR: Model.ModelType
    RANDOM_FOREST_CLASSIFIER: Model.ModelType
    TENSORFLOW_LITE: Model.ModelType
    ONNX: Model.ModelType
    TRANSFORM_ONLY: Model.ModelType
    CONTRIBUTION_ANALYSIS: Model.ModelType
    class LossType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        LOSS_TYPE_UNSPECIFIED: _ClassVar[Model.LossType]
        MEAN_SQUARED_LOSS: _ClassVar[Model.LossType]
        MEAN_LOG_LOSS: _ClassVar[Model.LossType]
    LOSS_TYPE_UNSPECIFIED: Model.LossType
    MEAN_SQUARED_LOSS: Model.LossType
    MEAN_LOG_LOSS: Model.LossType
    class DistanceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DISTANCE_TYPE_UNSPECIFIED: _ClassVar[Model.DistanceType]
        EUCLIDEAN: _ClassVar[Model.DistanceType]
        COSINE: _ClassVar[Model.DistanceType]
    DISTANCE_TYPE_UNSPECIFIED: Model.DistanceType
    EUCLIDEAN: Model.DistanceType
    COSINE: Model.DistanceType
    class DataSplitMethod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DATA_SPLIT_METHOD_UNSPECIFIED: _ClassVar[Model.DataSplitMethod]
        RANDOM: _ClassVar[Model.DataSplitMethod]
        CUSTOM: _ClassVar[Model.DataSplitMethod]
        SEQUENTIAL: _ClassVar[Model.DataSplitMethod]
        NO_SPLIT: _ClassVar[Model.DataSplitMethod]
        AUTO_SPLIT: _ClassVar[Model.DataSplitMethod]
    DATA_SPLIT_METHOD_UNSPECIFIED: Model.DataSplitMethod
    RANDOM: Model.DataSplitMethod
    CUSTOM: Model.DataSplitMethod
    SEQUENTIAL: Model.DataSplitMethod
    NO_SPLIT: Model.DataSplitMethod
    AUTO_SPLIT: Model.DataSplitMethod
    class DataFrequency(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DATA_FREQUENCY_UNSPECIFIED: _ClassVar[Model.DataFrequency]
        AUTO_FREQUENCY: _ClassVar[Model.DataFrequency]
        YEARLY: _ClassVar[Model.DataFrequency]
        QUARTERLY: _ClassVar[Model.DataFrequency]
        MONTHLY: _ClassVar[Model.DataFrequency]
        WEEKLY: _ClassVar[Model.DataFrequency]
        DAILY: _ClassVar[Model.DataFrequency]
        HOURLY: _ClassVar[Model.DataFrequency]
        PER_MINUTE: _ClassVar[Model.DataFrequency]
    DATA_FREQUENCY_UNSPECIFIED: Model.DataFrequency
    AUTO_FREQUENCY: Model.DataFrequency
    YEARLY: Model.DataFrequency
    QUARTERLY: Model.DataFrequency
    MONTHLY: Model.DataFrequency
    WEEKLY: Model.DataFrequency
    DAILY: Model.DataFrequency
    HOURLY: Model.DataFrequency
    PER_MINUTE: Model.DataFrequency
    class HolidayRegion(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        HOLIDAY_REGION_UNSPECIFIED: _ClassVar[Model.HolidayRegion]
        GLOBAL: _ClassVar[Model.HolidayRegion]
        NA: _ClassVar[Model.HolidayRegion]
        JAPAC: _ClassVar[Model.HolidayRegion]
        EMEA: _ClassVar[Model.HolidayRegion]
        LAC: _ClassVar[Model.HolidayRegion]
        AE: _ClassVar[Model.HolidayRegion]
        AR: _ClassVar[Model.HolidayRegion]
        AT: _ClassVar[Model.HolidayRegion]
        AU: _ClassVar[Model.HolidayRegion]
        BE: _ClassVar[Model.HolidayRegion]
        BR: _ClassVar[Model.HolidayRegion]
        CA: _ClassVar[Model.HolidayRegion]
        CH: _ClassVar[Model.HolidayRegion]
        CL: _ClassVar[Model.HolidayRegion]
        CN: _ClassVar[Model.HolidayRegion]
        CO: _ClassVar[Model.HolidayRegion]
        CS: _ClassVar[Model.HolidayRegion]
        CZ: _ClassVar[Model.HolidayRegion]
        DE: _ClassVar[Model.HolidayRegion]
        DK: _ClassVar[Model.HolidayRegion]
        DZ: _ClassVar[Model.HolidayRegion]
        EC: _ClassVar[Model.HolidayRegion]
        EE: _ClassVar[Model.HolidayRegion]
        EG: _ClassVar[Model.HolidayRegion]
        ES: _ClassVar[Model.HolidayRegion]
        FI: _ClassVar[Model.HolidayRegion]
        FR: _ClassVar[Model.HolidayRegion]
        GB: _ClassVar[Model.HolidayRegion]
        GR: _ClassVar[Model.HolidayRegion]
        HK: _ClassVar[Model.HolidayRegion]
        HU: _ClassVar[Model.HolidayRegion]
        ID: _ClassVar[Model.HolidayRegion]
        IE: _ClassVar[Model.HolidayRegion]
        IL: _ClassVar[Model.HolidayRegion]
        IN: _ClassVar[Model.HolidayRegion]
        IR: _ClassVar[Model.HolidayRegion]
        IT: _ClassVar[Model.HolidayRegion]
        JP: _ClassVar[Model.HolidayRegion]
        KR: _ClassVar[Model.HolidayRegion]
        LV: _ClassVar[Model.HolidayRegion]
        MA: _ClassVar[Model.HolidayRegion]
        MX: _ClassVar[Model.HolidayRegion]
        MY: _ClassVar[Model.HolidayRegion]
        NG: _ClassVar[Model.HolidayRegion]
        NL: _ClassVar[Model.HolidayRegion]
        NO: _ClassVar[Model.HolidayRegion]
        NZ: _ClassVar[Model.HolidayRegion]
        PE: _ClassVar[Model.HolidayRegion]
        PH: _ClassVar[Model.HolidayRegion]
        PK: _ClassVar[Model.HolidayRegion]
        PL: _ClassVar[Model.HolidayRegion]
        PT: _ClassVar[Model.HolidayRegion]
        RO: _ClassVar[Model.HolidayRegion]
        RS: _ClassVar[Model.HolidayRegion]
        RU: _ClassVar[Model.HolidayRegion]
        SA: _ClassVar[Model.HolidayRegion]
        SE: _ClassVar[Model.HolidayRegion]
        SG: _ClassVar[Model.HolidayRegion]
        SI: _ClassVar[Model.HolidayRegion]
        SK: _ClassVar[Model.HolidayRegion]
        TH: _ClassVar[Model.HolidayRegion]
        TR: _ClassVar[Model.HolidayRegion]
        TW: _ClassVar[Model.HolidayRegion]
        UA: _ClassVar[Model.HolidayRegion]
        US: _ClassVar[Model.HolidayRegion]
        VE: _ClassVar[Model.HolidayRegion]
        VN: _ClassVar[Model.HolidayRegion]
        ZA: _ClassVar[Model.HolidayRegion]
    HOLIDAY_REGION_UNSPECIFIED: Model.HolidayRegion
    GLOBAL: Model.HolidayRegion
    NA: Model.HolidayRegion
    JAPAC: Model.HolidayRegion
    EMEA: Model.HolidayRegion
    LAC: Model.HolidayRegion
    AE: Model.HolidayRegion
    AR: Model.HolidayRegion
    AT: Model.HolidayRegion
    AU: Model.HolidayRegion
    BE: Model.HolidayRegion
    BR: Model.HolidayRegion
    CA: Model.HolidayRegion
    CH: Model.HolidayRegion
    CL: Model.HolidayRegion
    CN: Model.HolidayRegion
    CO: Model.HolidayRegion
    CS: Model.HolidayRegion
    CZ: Model.HolidayRegion
    DE: Model.HolidayRegion
    DK: Model.HolidayRegion
    DZ: Model.HolidayRegion
    EC: Model.HolidayRegion
    EE: Model.HolidayRegion
    EG: Model.HolidayRegion
    ES: Model.HolidayRegion
    FI: Model.HolidayRegion
    FR: Model.HolidayRegion
    GB: Model.HolidayRegion
    GR: Model.HolidayRegion
    HK: Model.HolidayRegion
    HU: Model.HolidayRegion
    ID: Model.HolidayRegion
    IE: Model.HolidayRegion
    IL: Model.HolidayRegion
    IN: Model.HolidayRegion
    IR: Model.HolidayRegion
    IT: Model.HolidayRegion
    JP: Model.HolidayRegion
    KR: Model.HolidayRegion
    LV: Model.HolidayRegion
    MA: Model.HolidayRegion
    MX: Model.HolidayRegion
    MY: Model.HolidayRegion
    NG: Model.HolidayRegion
    NL: Model.HolidayRegion
    NO: Model.HolidayRegion
    NZ: Model.HolidayRegion
    PE: Model.HolidayRegion
    PH: Model.HolidayRegion
    PK: Model.HolidayRegion
    PL: Model.HolidayRegion
    PT: Model.HolidayRegion
    RO: Model.HolidayRegion
    RS: Model.HolidayRegion
    RU: Model.HolidayRegion
    SA: Model.HolidayRegion
    SE: Model.HolidayRegion
    SG: Model.HolidayRegion
    SI: Model.HolidayRegion
    SK: Model.HolidayRegion
    TH: Model.HolidayRegion
    TR: Model.HolidayRegion
    TW: Model.HolidayRegion
    UA: Model.HolidayRegion
    US: Model.HolidayRegion
    VE: Model.HolidayRegion
    VN: Model.HolidayRegion
    ZA: Model.HolidayRegion
    class ColorSpace(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        COLOR_SPACE_UNSPECIFIED: _ClassVar[Model.ColorSpace]
        RGB: _ClassVar[Model.ColorSpace]
        HSV: _ClassVar[Model.ColorSpace]
        YIQ: _ClassVar[Model.ColorSpace]
        YUV: _ClassVar[Model.ColorSpace]
        GRAYSCALE: _ClassVar[Model.ColorSpace]
    COLOR_SPACE_UNSPECIFIED: Model.ColorSpace
    RGB: Model.ColorSpace
    HSV: Model.ColorSpace
    YIQ: Model.ColorSpace
    YUV: Model.ColorSpace
    GRAYSCALE: Model.ColorSpace
    class LearnRateStrategy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        LEARN_RATE_STRATEGY_UNSPECIFIED: _ClassVar[Model.LearnRateStrategy]
        LINE_SEARCH: _ClassVar[Model.LearnRateStrategy]
        CONSTANT: _ClassVar[Model.LearnRateStrategy]
    LEARN_RATE_STRATEGY_UNSPECIFIED: Model.LearnRateStrategy
    LINE_SEARCH: Model.LearnRateStrategy
    CONSTANT: Model.LearnRateStrategy
    class OptimizationStrategy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        OPTIMIZATION_STRATEGY_UNSPECIFIED: _ClassVar[Model.OptimizationStrategy]
        BATCH_GRADIENT_DESCENT: _ClassVar[Model.OptimizationStrategy]
        NORMAL_EQUATION: _ClassVar[Model.OptimizationStrategy]
    OPTIMIZATION_STRATEGY_UNSPECIFIED: Model.OptimizationStrategy
    BATCH_GRADIENT_DESCENT: Model.OptimizationStrategy
    NORMAL_EQUATION: Model.OptimizationStrategy
    class FeedbackType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FEEDBACK_TYPE_UNSPECIFIED: _ClassVar[Model.FeedbackType]
        IMPLICIT: _ClassVar[Model.FeedbackType]
        EXPLICIT: _ClassVar[Model.FeedbackType]
    FEEDBACK_TYPE_UNSPECIFIED: Model.FeedbackType
    IMPLICIT: Model.FeedbackType
    EXPLICIT: Model.FeedbackType
    class SeasonalPeriod(_message.Message):
        __slots__ = ()
        class SeasonalPeriodType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            SEASONAL_PERIOD_TYPE_UNSPECIFIED: _ClassVar[Model.SeasonalPeriod.SeasonalPeriodType]
            NO_SEASONALITY: _ClassVar[Model.SeasonalPeriod.SeasonalPeriodType]
            DAILY: _ClassVar[Model.SeasonalPeriod.SeasonalPeriodType]
            WEEKLY: _ClassVar[Model.SeasonalPeriod.SeasonalPeriodType]
            MONTHLY: _ClassVar[Model.SeasonalPeriod.SeasonalPeriodType]
            QUARTERLY: _ClassVar[Model.SeasonalPeriod.SeasonalPeriodType]
            YEARLY: _ClassVar[Model.SeasonalPeriod.SeasonalPeriodType]
        SEASONAL_PERIOD_TYPE_UNSPECIFIED: Model.SeasonalPeriod.SeasonalPeriodType
        NO_SEASONALITY: Model.SeasonalPeriod.SeasonalPeriodType
        DAILY: Model.SeasonalPeriod.SeasonalPeriodType
        WEEKLY: Model.SeasonalPeriod.SeasonalPeriodType
        MONTHLY: Model.SeasonalPeriod.SeasonalPeriodType
        QUARTERLY: Model.SeasonalPeriod.SeasonalPeriodType
        YEARLY: Model.SeasonalPeriod.SeasonalPeriodType
        def __init__(self) -> None: ...
    class KmeansEnums(_message.Message):
        __slots__ = ()
        class KmeansInitializationMethod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            KMEANS_INITIALIZATION_METHOD_UNSPECIFIED: _ClassVar[Model.KmeansEnums.KmeansInitializationMethod]
            RANDOM: _ClassVar[Model.KmeansEnums.KmeansInitializationMethod]
            CUSTOM: _ClassVar[Model.KmeansEnums.KmeansInitializationMethod]
            KMEANS_PLUS_PLUS: _ClassVar[Model.KmeansEnums.KmeansInitializationMethod]
        KMEANS_INITIALIZATION_METHOD_UNSPECIFIED: Model.KmeansEnums.KmeansInitializationMethod
        RANDOM: Model.KmeansEnums.KmeansInitializationMethod
        CUSTOM: Model.KmeansEnums.KmeansInitializationMethod
        KMEANS_PLUS_PLUS: Model.KmeansEnums.KmeansInitializationMethod
        def __init__(self) -> None: ...
    class BoostedTreeOptionEnums(_message.Message):
        __slots__ = ()
        class BoosterType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            BOOSTER_TYPE_UNSPECIFIED: _ClassVar[Model.BoostedTreeOptionEnums.BoosterType]
            GBTREE: _ClassVar[Model.BoostedTreeOptionEnums.BoosterType]
            DART: _ClassVar[Model.BoostedTreeOptionEnums.BoosterType]
        BOOSTER_TYPE_UNSPECIFIED: Model.BoostedTreeOptionEnums.BoosterType
        GBTREE: Model.BoostedTreeOptionEnums.BoosterType
        DART: Model.BoostedTreeOptionEnums.BoosterType
        class DartNormalizeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            DART_NORMALIZE_TYPE_UNSPECIFIED: _ClassVar[Model.BoostedTreeOptionEnums.DartNormalizeType]
            TREE: _ClassVar[Model.BoostedTreeOptionEnums.DartNormalizeType]
            FOREST: _ClassVar[Model.BoostedTreeOptionEnums.DartNormalizeType]
        DART_NORMALIZE_TYPE_UNSPECIFIED: Model.BoostedTreeOptionEnums.DartNormalizeType
        TREE: Model.BoostedTreeOptionEnums.DartNormalizeType
        FOREST: Model.BoostedTreeOptionEnums.DartNormalizeType
        class TreeMethod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            TREE_METHOD_UNSPECIFIED: _ClassVar[Model.BoostedTreeOptionEnums.TreeMethod]
            AUTO: _ClassVar[Model.BoostedTreeOptionEnums.TreeMethod]
            EXACT: _ClassVar[Model.BoostedTreeOptionEnums.TreeMethod]
            APPROX: _ClassVar[Model.BoostedTreeOptionEnums.TreeMethod]
            HIST: _ClassVar[Model.BoostedTreeOptionEnums.TreeMethod]
        TREE_METHOD_UNSPECIFIED: Model.BoostedTreeOptionEnums.TreeMethod
        AUTO: Model.BoostedTreeOptionEnums.TreeMethod
        EXACT: Model.BoostedTreeOptionEnums.TreeMethod
        APPROX: Model.BoostedTreeOptionEnums.TreeMethod
        HIST: Model.BoostedTreeOptionEnums.TreeMethod
        def __init__(self) -> None: ...
    class HparamTuningEnums(_message.Message):
        __slots__ = ()
        class HparamTuningObjective(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            HPARAM_TUNING_OBJECTIVE_UNSPECIFIED: _ClassVar[Model.HparamTuningEnums.HparamTuningObjective]
            MEAN_ABSOLUTE_ERROR: _ClassVar[Model.HparamTuningEnums.HparamTuningObjective]
            MEAN_SQUARED_ERROR: _ClassVar[Model.HparamTuningEnums.HparamTuningObjective]
            MEAN_SQUARED_LOG_ERROR: _ClassVar[Model.HparamTuningEnums.HparamTuningObjective]
            MEDIAN_ABSOLUTE_ERROR: _ClassVar[Model.HparamTuningEnums.HparamTuningObjective]
            R_SQUARED: _ClassVar[Model.HparamTuningEnums.HparamTuningObjective]
            EXPLAINED_VARIANCE: _ClassVar[Model.HparamTuningEnums.HparamTuningObjective]
            PRECISION: _ClassVar[Model.HparamTuningEnums.HparamTuningObjective]
            RECALL: _ClassVar[Model.HparamTuningEnums.HparamTuningObjective]
            ACCURACY: _ClassVar[Model.HparamTuningEnums.HparamTuningObjective]
            F1_SCORE: _ClassVar[Model.HparamTuningEnums.HparamTuningObjective]
            LOG_LOSS: _ClassVar[Model.HparamTuningEnums.HparamTuningObjective]
            ROC_AUC: _ClassVar[Model.HparamTuningEnums.HparamTuningObjective]
            DAVIES_BOULDIN_INDEX: _ClassVar[Model.HparamTuningEnums.HparamTuningObjective]
            MEAN_AVERAGE_PRECISION: _ClassVar[Model.HparamTuningEnums.HparamTuningObjective]
            NORMALIZED_DISCOUNTED_CUMULATIVE_GAIN: _ClassVar[Model.HparamTuningEnums.HparamTuningObjective]
            AVERAGE_RANK: _ClassVar[Model.HparamTuningEnums.HparamTuningObjective]
        HPARAM_TUNING_OBJECTIVE_UNSPECIFIED: Model.HparamTuningEnums.HparamTuningObjective
        MEAN_ABSOLUTE_ERROR: Model.HparamTuningEnums.HparamTuningObjective
        MEAN_SQUARED_ERROR: Model.HparamTuningEnums.HparamTuningObjective
        MEAN_SQUARED_LOG_ERROR: Model.HparamTuningEnums.HparamTuningObjective
        MEDIAN_ABSOLUTE_ERROR: Model.HparamTuningEnums.HparamTuningObjective
        R_SQUARED: Model.HparamTuningEnums.HparamTuningObjective
        EXPLAINED_VARIANCE: Model.HparamTuningEnums.HparamTuningObjective
        PRECISION: Model.HparamTuningEnums.HparamTuningObjective
        RECALL: Model.HparamTuningEnums.HparamTuningObjective
        ACCURACY: Model.HparamTuningEnums.HparamTuningObjective
        F1_SCORE: Model.HparamTuningEnums.HparamTuningObjective
        LOG_LOSS: Model.HparamTuningEnums.HparamTuningObjective
        ROC_AUC: Model.HparamTuningEnums.HparamTuningObjective
        DAVIES_BOULDIN_INDEX: Model.HparamTuningEnums.HparamTuningObjective
        MEAN_AVERAGE_PRECISION: Model.HparamTuningEnums.HparamTuningObjective
        NORMALIZED_DISCOUNTED_CUMULATIVE_GAIN: Model.HparamTuningEnums.HparamTuningObjective
        AVERAGE_RANK: Model.HparamTuningEnums.HparamTuningObjective
        def __init__(self) -> None: ...
    class RegressionMetrics(_message.Message):
        __slots__ = ("mean_absolute_error", "mean_squared_error", "mean_squared_log_error", "median_absolute_error", "r_squared")
        MEAN_ABSOLUTE_ERROR_FIELD_NUMBER: _ClassVar[int]
        MEAN_SQUARED_ERROR_FIELD_NUMBER: _ClassVar[int]
        MEAN_SQUARED_LOG_ERROR_FIELD_NUMBER: _ClassVar[int]
        MEDIAN_ABSOLUTE_ERROR_FIELD_NUMBER: _ClassVar[int]
        R_SQUARED_FIELD_NUMBER: _ClassVar[int]
        mean_absolute_error: _wrappers_pb2.DoubleValue
        mean_squared_error: _wrappers_pb2.DoubleValue
        mean_squared_log_error: _wrappers_pb2.DoubleValue
        median_absolute_error: _wrappers_pb2.DoubleValue
        r_squared: _wrappers_pb2.DoubleValue
        def __init__(self, mean_absolute_error: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ..., mean_squared_error: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ..., mean_squared_log_error: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ..., median_absolute_error: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ..., r_squared: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ...) -> None: ...
    class AggregateClassificationMetrics(_message.Message):
        __slots__ = ("precision", "recall", "accuracy", "threshold", "f1_score", "log_loss", "roc_auc")
        PRECISION_FIELD_NUMBER: _ClassVar[int]
        RECALL_FIELD_NUMBER: _ClassVar[int]
        ACCURACY_FIELD_NUMBER: _ClassVar[int]
        THRESHOLD_FIELD_NUMBER: _ClassVar[int]
        F1_SCORE_FIELD_NUMBER: _ClassVar[int]
        LOG_LOSS_FIELD_NUMBER: _ClassVar[int]
        ROC_AUC_FIELD_NUMBER: _ClassVar[int]
        precision: _wrappers_pb2.DoubleValue
        recall: _wrappers_pb2.DoubleValue
        accuracy: _wrappers_pb2.DoubleValue
        threshold: _wrappers_pb2.DoubleValue
        f1_score: _wrappers_pb2.DoubleValue
        log_loss: _wrappers_pb2.DoubleValue
        roc_auc: _wrappers_pb2.DoubleValue
        def __init__(self, precision: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ..., recall: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ..., accuracy: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ..., threshold: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ..., f1_score: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ..., log_loss: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ..., roc_auc: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ...) -> None: ...
    class BinaryClassificationMetrics(_message.Message):
        __slots__ = ("aggregate_classification_metrics", "binary_confusion_matrix_list", "positive_label", "negative_label")
        class BinaryConfusionMatrix(_message.Message):
            __slots__ = ("positive_class_threshold", "true_positives", "false_positives", "true_negatives", "false_negatives", "precision", "recall", "f1_score", "accuracy")
            POSITIVE_CLASS_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
            TRUE_POSITIVES_FIELD_NUMBER: _ClassVar[int]
            FALSE_POSITIVES_FIELD_NUMBER: _ClassVar[int]
            TRUE_NEGATIVES_FIELD_NUMBER: _ClassVar[int]
            FALSE_NEGATIVES_FIELD_NUMBER: _ClassVar[int]
            PRECISION_FIELD_NUMBER: _ClassVar[int]
            RECALL_FIELD_NUMBER: _ClassVar[int]
            F1_SCORE_FIELD_NUMBER: _ClassVar[int]
            ACCURACY_FIELD_NUMBER: _ClassVar[int]
            positive_class_threshold: _wrappers_pb2.DoubleValue
            true_positives: _wrappers_pb2.Int64Value
            false_positives: _wrappers_pb2.Int64Value
            true_negatives: _wrappers_pb2.Int64Value
            false_negatives: _wrappers_pb2.Int64Value
            precision: _wrappers_pb2.DoubleValue
            recall: _wrappers_pb2.DoubleValue
            f1_score: _wrappers_pb2.DoubleValue
            accuracy: _wrappers_pb2.DoubleValue
            def __init__(self, positive_class_threshold: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ..., true_positives: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., false_positives: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., true_negatives: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., false_negatives: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., precision: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ..., recall: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ..., f1_score: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ..., accuracy: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ...) -> None: ...
        AGGREGATE_CLASSIFICATION_METRICS_FIELD_NUMBER: _ClassVar[int]
        BINARY_CONFUSION_MATRIX_LIST_FIELD_NUMBER: _ClassVar[int]
        POSITIVE_LABEL_FIELD_NUMBER: _ClassVar[int]
        NEGATIVE_LABEL_FIELD_NUMBER: _ClassVar[int]
        aggregate_classification_metrics: Model.AggregateClassificationMetrics
        binary_confusion_matrix_list: _containers.RepeatedCompositeFieldContainer[Model.BinaryClassificationMetrics.BinaryConfusionMatrix]
        positive_label: str
        negative_label: str
        def __init__(self, aggregate_classification_metrics: _Optional[_Union[Model.AggregateClassificationMetrics, _Mapping]] = ..., binary_confusion_matrix_list: _Optional[_Iterable[_Union[Model.BinaryClassificationMetrics.BinaryConfusionMatrix, _Mapping]]] = ..., positive_label: _Optional[str] = ..., negative_label: _Optional[str] = ...) -> None: ...
    class MultiClassClassificationMetrics(_message.Message):
        __slots__ = ("aggregate_classification_metrics", "confusion_matrix_list")
        class ConfusionMatrix(_message.Message):
            __slots__ = ("confidence_threshold", "rows")
            class Entry(_message.Message):
                __slots__ = ("predicted_label", "item_count")
                PREDICTED_LABEL_FIELD_NUMBER: _ClassVar[int]
                ITEM_COUNT_FIELD_NUMBER: _ClassVar[int]
                predicted_label: str
                item_count: _wrappers_pb2.Int64Value
                def __init__(self, predicted_label: _Optional[str] = ..., item_count: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ...) -> None: ...
            class Row(_message.Message):
                __slots__ = ("actual_label", "entries")
                ACTUAL_LABEL_FIELD_NUMBER: _ClassVar[int]
                ENTRIES_FIELD_NUMBER: _ClassVar[int]
                actual_label: str
                entries: _containers.RepeatedCompositeFieldContainer[Model.MultiClassClassificationMetrics.ConfusionMatrix.Entry]
                def __init__(self, actual_label: _Optional[str] = ..., entries: _Optional[_Iterable[_Union[Model.MultiClassClassificationMetrics.ConfusionMatrix.Entry, _Mapping]]] = ...) -> None: ...
            CONFIDENCE_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
            ROWS_FIELD_NUMBER: _ClassVar[int]
            confidence_threshold: _wrappers_pb2.DoubleValue
            rows: _containers.RepeatedCompositeFieldContainer[Model.MultiClassClassificationMetrics.ConfusionMatrix.Row]
            def __init__(self, confidence_threshold: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ..., rows: _Optional[_Iterable[_Union[Model.MultiClassClassificationMetrics.ConfusionMatrix.Row, _Mapping]]] = ...) -> None: ...
        AGGREGATE_CLASSIFICATION_METRICS_FIELD_NUMBER: _ClassVar[int]
        CONFUSION_MATRIX_LIST_FIELD_NUMBER: _ClassVar[int]
        aggregate_classification_metrics: Model.AggregateClassificationMetrics
        confusion_matrix_list: _containers.RepeatedCompositeFieldContainer[Model.MultiClassClassificationMetrics.ConfusionMatrix]
        def __init__(self, aggregate_classification_metrics: _Optional[_Union[Model.AggregateClassificationMetrics, _Mapping]] = ..., confusion_matrix_list: _Optional[_Iterable[_Union[Model.MultiClassClassificationMetrics.ConfusionMatrix, _Mapping]]] = ...) -> None: ...
    class ClusteringMetrics(_message.Message):
        __slots__ = ("davies_bouldin_index", "mean_squared_distance", "clusters")
        class Cluster(_message.Message):
            __slots__ = ("centroid_id", "feature_values", "count")
            class FeatureValue(_message.Message):
                __slots__ = ("feature_column", "numerical_value", "categorical_value")
                class CategoricalValue(_message.Message):
                    __slots__ = ("category_counts",)
                    class CategoryCount(_message.Message):
                        __slots__ = ("category", "count")
                        CATEGORY_FIELD_NUMBER: _ClassVar[int]
                        COUNT_FIELD_NUMBER: _ClassVar[int]
                        category: str
                        count: _wrappers_pb2.Int64Value
                        def __init__(self, category: _Optional[str] = ..., count: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ...) -> None: ...
                    CATEGORY_COUNTS_FIELD_NUMBER: _ClassVar[int]
                    category_counts: _containers.RepeatedCompositeFieldContainer[Model.ClusteringMetrics.Cluster.FeatureValue.CategoricalValue.CategoryCount]
                    def __init__(self, category_counts: _Optional[_Iterable[_Union[Model.ClusteringMetrics.Cluster.FeatureValue.CategoricalValue.CategoryCount, _Mapping]]] = ...) -> None: ...
                FEATURE_COLUMN_FIELD_NUMBER: _ClassVar[int]
                NUMERICAL_VALUE_FIELD_NUMBER: _ClassVar[int]
                CATEGORICAL_VALUE_FIELD_NUMBER: _ClassVar[int]
                feature_column: str
                numerical_value: _wrappers_pb2.DoubleValue
                categorical_value: Model.ClusteringMetrics.Cluster.FeatureValue.CategoricalValue
                def __init__(self, feature_column: _Optional[str] = ..., numerical_value: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ..., categorical_value: _Optional[_Union[Model.ClusteringMetrics.Cluster.FeatureValue.CategoricalValue, _Mapping]] = ...) -> None: ...
            CENTROID_ID_FIELD_NUMBER: _ClassVar[int]
            FEATURE_VALUES_FIELD_NUMBER: _ClassVar[int]
            COUNT_FIELD_NUMBER: _ClassVar[int]
            centroid_id: int
            feature_values: _containers.RepeatedCompositeFieldContainer[Model.ClusteringMetrics.Cluster.FeatureValue]
            count: _wrappers_pb2.Int64Value
            def __init__(self, centroid_id: _Optional[int] = ..., feature_values: _Optional[_Iterable[_Union[Model.ClusteringMetrics.Cluster.FeatureValue, _Mapping]]] = ..., count: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ...) -> None: ...
        DAVIES_BOULDIN_INDEX_FIELD_NUMBER: _ClassVar[int]
        MEAN_SQUARED_DISTANCE_FIELD_NUMBER: _ClassVar[int]
        CLUSTERS_FIELD_NUMBER: _ClassVar[int]
        davies_bouldin_index: _wrappers_pb2.DoubleValue
        mean_squared_distance: _wrappers_pb2.DoubleValue
        clusters: _containers.RepeatedCompositeFieldContainer[Model.ClusteringMetrics.Cluster]
        def __init__(self, davies_bouldin_index: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ..., mean_squared_distance: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ..., clusters: _Optional[_Iterable[_Union[Model.ClusteringMetrics.Cluster, _Mapping]]] = ...) -> None: ...
    class RankingMetrics(_message.Message):
        __slots__ = ("mean_average_precision", "mean_squared_error", "normalized_discounted_cumulative_gain", "average_rank")
        MEAN_AVERAGE_PRECISION_FIELD_NUMBER: _ClassVar[int]
        MEAN_SQUARED_ERROR_FIELD_NUMBER: _ClassVar[int]
        NORMALIZED_DISCOUNTED_CUMULATIVE_GAIN_FIELD_NUMBER: _ClassVar[int]
        AVERAGE_RANK_FIELD_NUMBER: _ClassVar[int]
        mean_average_precision: _wrappers_pb2.DoubleValue
        mean_squared_error: _wrappers_pb2.DoubleValue
        normalized_discounted_cumulative_gain: _wrappers_pb2.DoubleValue
        average_rank: _wrappers_pb2.DoubleValue
        def __init__(self, mean_average_precision: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ..., mean_squared_error: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ..., normalized_discounted_cumulative_gain: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ..., average_rank: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ...) -> None: ...
    class ArimaForecastingMetrics(_message.Message):
        __slots__ = ("arima_single_model_forecasting_metrics",)
        class ArimaSingleModelForecastingMetrics(_message.Message):
            __slots__ = ("non_seasonal_order", "arima_fitting_metrics", "has_drift", "time_series_id", "time_series_ids", "seasonal_periods", "has_holiday_effect", "has_spikes_and_dips", "has_step_changes")
            NON_SEASONAL_ORDER_FIELD_NUMBER: _ClassVar[int]
            ARIMA_FITTING_METRICS_FIELD_NUMBER: _ClassVar[int]
            HAS_DRIFT_FIELD_NUMBER: _ClassVar[int]
            TIME_SERIES_ID_FIELD_NUMBER: _ClassVar[int]
            TIME_SERIES_IDS_FIELD_NUMBER: _ClassVar[int]
            SEASONAL_PERIODS_FIELD_NUMBER: _ClassVar[int]
            HAS_HOLIDAY_EFFECT_FIELD_NUMBER: _ClassVar[int]
            HAS_SPIKES_AND_DIPS_FIELD_NUMBER: _ClassVar[int]
            HAS_STEP_CHANGES_FIELD_NUMBER: _ClassVar[int]
            non_seasonal_order: Model.ArimaOrder
            arima_fitting_metrics: Model.ArimaFittingMetrics
            has_drift: _wrappers_pb2.BoolValue
            time_series_id: str
            time_series_ids: _containers.RepeatedScalarFieldContainer[str]
            seasonal_periods: _containers.RepeatedScalarFieldContainer[Model.SeasonalPeriod.SeasonalPeriodType]
            has_holiday_effect: _wrappers_pb2.BoolValue
            has_spikes_and_dips: _wrappers_pb2.BoolValue
            has_step_changes: _wrappers_pb2.BoolValue
            def __init__(self, non_seasonal_order: _Optional[_Union[Model.ArimaOrder, _Mapping]] = ..., arima_fitting_metrics: _Optional[_Union[Model.ArimaFittingMetrics, _Mapping]] = ..., has_drift: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., time_series_id: _Optional[str] = ..., time_series_ids: _Optional[_Iterable[str]] = ..., seasonal_periods: _Optional[_Iterable[_Union[Model.SeasonalPeriod.SeasonalPeriodType, str]]] = ..., has_holiday_effect: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., has_spikes_and_dips: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., has_step_changes: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...) -> None: ...
        ARIMA_SINGLE_MODEL_FORECASTING_METRICS_FIELD_NUMBER: _ClassVar[int]
        arima_single_model_forecasting_metrics: _containers.RepeatedCompositeFieldContainer[Model.ArimaForecastingMetrics.ArimaSingleModelForecastingMetrics]
        def __init__(self, arima_single_model_forecasting_metrics: _Optional[_Iterable[_Union[Model.ArimaForecastingMetrics.ArimaSingleModelForecastingMetrics, _Mapping]]] = ...) -> None: ...
    class DimensionalityReductionMetrics(_message.Message):
        __slots__ = ("total_explained_variance_ratio",)
        TOTAL_EXPLAINED_VARIANCE_RATIO_FIELD_NUMBER: _ClassVar[int]
        total_explained_variance_ratio: _wrappers_pb2.DoubleValue
        def __init__(self, total_explained_variance_ratio: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ...) -> None: ...
    class EvaluationMetrics(_message.Message):
        __slots__ = ("regression_metrics", "binary_classification_metrics", "multi_class_classification_metrics", "clustering_metrics", "ranking_metrics", "arima_forecasting_metrics", "dimensionality_reduction_metrics")
        REGRESSION_METRICS_FIELD_NUMBER: _ClassVar[int]
        BINARY_CLASSIFICATION_METRICS_FIELD_NUMBER: _ClassVar[int]
        MULTI_CLASS_CLASSIFICATION_METRICS_FIELD_NUMBER: _ClassVar[int]
        CLUSTERING_METRICS_FIELD_NUMBER: _ClassVar[int]
        RANKING_METRICS_FIELD_NUMBER: _ClassVar[int]
        ARIMA_FORECASTING_METRICS_FIELD_NUMBER: _ClassVar[int]
        DIMENSIONALITY_REDUCTION_METRICS_FIELD_NUMBER: _ClassVar[int]
        regression_metrics: Model.RegressionMetrics
        binary_classification_metrics: Model.BinaryClassificationMetrics
        multi_class_classification_metrics: Model.MultiClassClassificationMetrics
        clustering_metrics: Model.ClusteringMetrics
        ranking_metrics: Model.RankingMetrics
        arima_forecasting_metrics: Model.ArimaForecastingMetrics
        dimensionality_reduction_metrics: Model.DimensionalityReductionMetrics
        def __init__(self, regression_metrics: _Optional[_Union[Model.RegressionMetrics, _Mapping]] = ..., binary_classification_metrics: _Optional[_Union[Model.BinaryClassificationMetrics, _Mapping]] = ..., multi_class_classification_metrics: _Optional[_Union[Model.MultiClassClassificationMetrics, _Mapping]] = ..., clustering_metrics: _Optional[_Union[Model.ClusteringMetrics, _Mapping]] = ..., ranking_metrics: _Optional[_Union[Model.RankingMetrics, _Mapping]] = ..., arima_forecasting_metrics: _Optional[_Union[Model.ArimaForecastingMetrics, _Mapping]] = ..., dimensionality_reduction_metrics: _Optional[_Union[Model.DimensionalityReductionMetrics, _Mapping]] = ...) -> None: ...
    class DataSplitResult(_message.Message):
        __slots__ = ("training_table", "evaluation_table", "test_table")
        TRAINING_TABLE_FIELD_NUMBER: _ClassVar[int]
        EVALUATION_TABLE_FIELD_NUMBER: _ClassVar[int]
        TEST_TABLE_FIELD_NUMBER: _ClassVar[int]
        training_table: _table_reference_pb2.TableReference
        evaluation_table: _table_reference_pb2.TableReference
        test_table: _table_reference_pb2.TableReference
        def __init__(self, training_table: _Optional[_Union[_table_reference_pb2.TableReference, _Mapping]] = ..., evaluation_table: _Optional[_Union[_table_reference_pb2.TableReference, _Mapping]] = ..., test_table: _Optional[_Union[_table_reference_pb2.TableReference, _Mapping]] = ...) -> None: ...
    class ArimaOrder(_message.Message):
        __slots__ = ("p", "d", "q")
        P_FIELD_NUMBER: _ClassVar[int]
        D_FIELD_NUMBER: _ClassVar[int]
        Q_FIELD_NUMBER: _ClassVar[int]
        p: _wrappers_pb2.Int64Value
        d: _wrappers_pb2.Int64Value
        q: _wrappers_pb2.Int64Value
        def __init__(self, p: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., d: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., q: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ...) -> None: ...
    class ArimaFittingMetrics(_message.Message):
        __slots__ = ("log_likelihood", "aic", "variance")
        LOG_LIKELIHOOD_FIELD_NUMBER: _ClassVar[int]
        AIC_FIELD_NUMBER: _ClassVar[int]
        VARIANCE_FIELD_NUMBER: _ClassVar[int]
        log_likelihood: _wrappers_pb2.DoubleValue
        aic: _wrappers_pb2.DoubleValue
        variance: _wrappers_pb2.DoubleValue
        def __init__(self, log_likelihood: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ..., aic: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ..., variance: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ...) -> None: ...
    class GlobalExplanation(_message.Message):
        __slots__ = ("explanations", "class_label")
        class Explanation(_message.Message):
            __slots__ = ("feature_name", "attribution")
            FEATURE_NAME_FIELD_NUMBER: _ClassVar[int]
            ATTRIBUTION_FIELD_NUMBER: _ClassVar[int]
            feature_name: str
            attribution: _wrappers_pb2.DoubleValue
            def __init__(self, feature_name: _Optional[str] = ..., attribution: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ...) -> None: ...
        EXPLANATIONS_FIELD_NUMBER: _ClassVar[int]
        CLASS_LABEL_FIELD_NUMBER: _ClassVar[int]
        explanations: _containers.RepeatedCompositeFieldContainer[Model.GlobalExplanation.Explanation]
        class_label: str
        def __init__(self, explanations: _Optional[_Iterable[_Union[Model.GlobalExplanation.Explanation, _Mapping]]] = ..., class_label: _Optional[str] = ...) -> None: ...
    class CategoryEncodingMethod(_message.Message):
        __slots__ = ()
        class EncodingMethod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            ENCODING_METHOD_UNSPECIFIED: _ClassVar[Model.CategoryEncodingMethod.EncodingMethod]
            ONE_HOT_ENCODING: _ClassVar[Model.CategoryEncodingMethod.EncodingMethod]
            LABEL_ENCODING: _ClassVar[Model.CategoryEncodingMethod.EncodingMethod]
            DUMMY_ENCODING: _ClassVar[Model.CategoryEncodingMethod.EncodingMethod]
        ENCODING_METHOD_UNSPECIFIED: Model.CategoryEncodingMethod.EncodingMethod
        ONE_HOT_ENCODING: Model.CategoryEncodingMethod.EncodingMethod
        LABEL_ENCODING: Model.CategoryEncodingMethod.EncodingMethod
        DUMMY_ENCODING: Model.CategoryEncodingMethod.EncodingMethod
        def __init__(self) -> None: ...
    class PcaSolverOptionEnums(_message.Message):
        __slots__ = ()
        class PcaSolver(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNSPECIFIED: _ClassVar[Model.PcaSolverOptionEnums.PcaSolver]
            FULL: _ClassVar[Model.PcaSolverOptionEnums.PcaSolver]
            RANDOMIZED: _ClassVar[Model.PcaSolverOptionEnums.PcaSolver]
            AUTO: _ClassVar[Model.PcaSolverOptionEnums.PcaSolver]
        UNSPECIFIED: Model.PcaSolverOptionEnums.PcaSolver
        FULL: Model.PcaSolverOptionEnums.PcaSolver
        RANDOMIZED: Model.PcaSolverOptionEnums.PcaSolver
        AUTO: Model.PcaSolverOptionEnums.PcaSolver
        def __init__(self) -> None: ...
    class ModelRegistryOptionEnums(_message.Message):
        __slots__ = ()
        class ModelRegistry(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            MODEL_REGISTRY_UNSPECIFIED: _ClassVar[Model.ModelRegistryOptionEnums.ModelRegistry]
            VERTEX_AI: _ClassVar[Model.ModelRegistryOptionEnums.ModelRegistry]
        MODEL_REGISTRY_UNSPECIFIED: Model.ModelRegistryOptionEnums.ModelRegistry
        VERTEX_AI: Model.ModelRegistryOptionEnums.ModelRegistry
        def __init__(self) -> None: ...
    class TrainingRun(_message.Message):
        __slots__ = ("training_options", "start_time", "results", "evaluation_metrics", "data_split_result", "model_level_global_explanation", "class_level_global_explanations", "vertex_ai_model_id", "vertex_ai_model_version")
        class TrainingOptions(_message.Message):
            __slots__ = ("max_iterations", "loss_type", "learn_rate", "l1_regularization", "l2_regularization", "min_relative_progress", "warm_start", "early_stop", "input_label_columns", "data_split_method", "data_split_eval_fraction", "data_split_column", "learn_rate_strategy", "initial_learn_rate", "label_class_weights", "user_column", "item_column", "distance_type", "num_clusters", "model_uri", "optimization_strategy", "hidden_units", "batch_size", "dropout", "max_tree_depth", "subsample", "min_split_loss", "booster_type", "num_parallel_tree", "dart_normalize_type", "tree_method", "min_tree_child_weight", "colsample_bytree", "colsample_bylevel", "colsample_bynode", "num_factors", "feedback_type", "wals_alpha", "kmeans_initialization_method", "kmeans_initialization_column", "time_series_timestamp_column", "time_series_data_column", "auto_arima", "non_seasonal_order", "data_frequency", "calculate_p_values", "include_drift", "holiday_region", "holiday_regions", "time_series_id_column", "time_series_id_columns", "horizon", "auto_arima_max_order", "auto_arima_min_order", "num_trials", "max_parallel_trials", "hparam_tuning_objectives", "decompose_time_series", "clean_spikes_and_dips", "adjust_step_changes", "enable_global_explain", "sampled_shapley_num_paths", "integrated_gradients_num_steps", "category_encoding_method", "tf_version", "color_space", "instance_weight_column", "trend_smoothing_window_size", "time_series_length_fraction", "min_time_series_length", "max_time_series_length", "xgboost_version", "approx_global_feature_contrib", "fit_intercept", "num_principal_components", "pca_explained_variance_ratio", "scale_features", "pca_solver", "auto_class_weights", "activation_fn", "optimizer", "budget_hours", "standardize_features", "l1_reg_activation", "model_registry", "vertex_ai_model_version_aliases", "dimension_id_columns", "contribution_metric", "is_test_column", "min_apriori_support")
            class LabelClassWeightsEntry(_message.Message):
                __slots__ = ("key", "value")
                KEY_FIELD_NUMBER: _ClassVar[int]
                VALUE_FIELD_NUMBER: _ClassVar[int]
                key: str
                value: float
                def __init__(self, key: _Optional[str] = ..., value: _Optional[float] = ...) -> None: ...
            MAX_ITERATIONS_FIELD_NUMBER: _ClassVar[int]
            LOSS_TYPE_FIELD_NUMBER: _ClassVar[int]
            LEARN_RATE_FIELD_NUMBER: _ClassVar[int]
            L1_REGULARIZATION_FIELD_NUMBER: _ClassVar[int]
            L2_REGULARIZATION_FIELD_NUMBER: _ClassVar[int]
            MIN_RELATIVE_PROGRESS_FIELD_NUMBER: _ClassVar[int]
            WARM_START_FIELD_NUMBER: _ClassVar[int]
            EARLY_STOP_FIELD_NUMBER: _ClassVar[int]
            INPUT_LABEL_COLUMNS_FIELD_NUMBER: _ClassVar[int]
            DATA_SPLIT_METHOD_FIELD_NUMBER: _ClassVar[int]
            DATA_SPLIT_EVAL_FRACTION_FIELD_NUMBER: _ClassVar[int]
            DATA_SPLIT_COLUMN_FIELD_NUMBER: _ClassVar[int]
            LEARN_RATE_STRATEGY_FIELD_NUMBER: _ClassVar[int]
            INITIAL_LEARN_RATE_FIELD_NUMBER: _ClassVar[int]
            LABEL_CLASS_WEIGHTS_FIELD_NUMBER: _ClassVar[int]
            USER_COLUMN_FIELD_NUMBER: _ClassVar[int]
            ITEM_COLUMN_FIELD_NUMBER: _ClassVar[int]
            DISTANCE_TYPE_FIELD_NUMBER: _ClassVar[int]
            NUM_CLUSTERS_FIELD_NUMBER: _ClassVar[int]
            MODEL_URI_FIELD_NUMBER: _ClassVar[int]
            OPTIMIZATION_STRATEGY_FIELD_NUMBER: _ClassVar[int]
            HIDDEN_UNITS_FIELD_NUMBER: _ClassVar[int]
            BATCH_SIZE_FIELD_NUMBER: _ClassVar[int]
            DROPOUT_FIELD_NUMBER: _ClassVar[int]
            MAX_TREE_DEPTH_FIELD_NUMBER: _ClassVar[int]
            SUBSAMPLE_FIELD_NUMBER: _ClassVar[int]
            MIN_SPLIT_LOSS_FIELD_NUMBER: _ClassVar[int]
            BOOSTER_TYPE_FIELD_NUMBER: _ClassVar[int]
            NUM_PARALLEL_TREE_FIELD_NUMBER: _ClassVar[int]
            DART_NORMALIZE_TYPE_FIELD_NUMBER: _ClassVar[int]
            TREE_METHOD_FIELD_NUMBER: _ClassVar[int]
            MIN_TREE_CHILD_WEIGHT_FIELD_NUMBER: _ClassVar[int]
            COLSAMPLE_BYTREE_FIELD_NUMBER: _ClassVar[int]
            COLSAMPLE_BYLEVEL_FIELD_NUMBER: _ClassVar[int]
            COLSAMPLE_BYNODE_FIELD_NUMBER: _ClassVar[int]
            NUM_FACTORS_FIELD_NUMBER: _ClassVar[int]
            FEEDBACK_TYPE_FIELD_NUMBER: _ClassVar[int]
            WALS_ALPHA_FIELD_NUMBER: _ClassVar[int]
            KMEANS_INITIALIZATION_METHOD_FIELD_NUMBER: _ClassVar[int]
            KMEANS_INITIALIZATION_COLUMN_FIELD_NUMBER: _ClassVar[int]
            TIME_SERIES_TIMESTAMP_COLUMN_FIELD_NUMBER: _ClassVar[int]
            TIME_SERIES_DATA_COLUMN_FIELD_NUMBER: _ClassVar[int]
            AUTO_ARIMA_FIELD_NUMBER: _ClassVar[int]
            NON_SEASONAL_ORDER_FIELD_NUMBER: _ClassVar[int]
            DATA_FREQUENCY_FIELD_NUMBER: _ClassVar[int]
            CALCULATE_P_VALUES_FIELD_NUMBER: _ClassVar[int]
            INCLUDE_DRIFT_FIELD_NUMBER: _ClassVar[int]
            HOLIDAY_REGION_FIELD_NUMBER: _ClassVar[int]
            HOLIDAY_REGIONS_FIELD_NUMBER: _ClassVar[int]
            TIME_SERIES_ID_COLUMN_FIELD_NUMBER: _ClassVar[int]
            TIME_SERIES_ID_COLUMNS_FIELD_NUMBER: _ClassVar[int]
            HORIZON_FIELD_NUMBER: _ClassVar[int]
            AUTO_ARIMA_MAX_ORDER_FIELD_NUMBER: _ClassVar[int]
            AUTO_ARIMA_MIN_ORDER_FIELD_NUMBER: _ClassVar[int]
            NUM_TRIALS_FIELD_NUMBER: _ClassVar[int]
            MAX_PARALLEL_TRIALS_FIELD_NUMBER: _ClassVar[int]
            HPARAM_TUNING_OBJECTIVES_FIELD_NUMBER: _ClassVar[int]
            DECOMPOSE_TIME_SERIES_FIELD_NUMBER: _ClassVar[int]
            CLEAN_SPIKES_AND_DIPS_FIELD_NUMBER: _ClassVar[int]
            ADJUST_STEP_CHANGES_FIELD_NUMBER: _ClassVar[int]
            ENABLE_GLOBAL_EXPLAIN_FIELD_NUMBER: _ClassVar[int]
            SAMPLED_SHAPLEY_NUM_PATHS_FIELD_NUMBER: _ClassVar[int]
            INTEGRATED_GRADIENTS_NUM_STEPS_FIELD_NUMBER: _ClassVar[int]
            CATEGORY_ENCODING_METHOD_FIELD_NUMBER: _ClassVar[int]
            TF_VERSION_FIELD_NUMBER: _ClassVar[int]
            COLOR_SPACE_FIELD_NUMBER: _ClassVar[int]
            INSTANCE_WEIGHT_COLUMN_FIELD_NUMBER: _ClassVar[int]
            TREND_SMOOTHING_WINDOW_SIZE_FIELD_NUMBER: _ClassVar[int]
            TIME_SERIES_LENGTH_FRACTION_FIELD_NUMBER: _ClassVar[int]
            MIN_TIME_SERIES_LENGTH_FIELD_NUMBER: _ClassVar[int]
            MAX_TIME_SERIES_LENGTH_FIELD_NUMBER: _ClassVar[int]
            XGBOOST_VERSION_FIELD_NUMBER: _ClassVar[int]
            APPROX_GLOBAL_FEATURE_CONTRIB_FIELD_NUMBER: _ClassVar[int]
            FIT_INTERCEPT_FIELD_NUMBER: _ClassVar[int]
            NUM_PRINCIPAL_COMPONENTS_FIELD_NUMBER: _ClassVar[int]
            PCA_EXPLAINED_VARIANCE_RATIO_FIELD_NUMBER: _ClassVar[int]
            SCALE_FEATURES_FIELD_NUMBER: _ClassVar[int]
            PCA_SOLVER_FIELD_NUMBER: _ClassVar[int]
            AUTO_CLASS_WEIGHTS_FIELD_NUMBER: _ClassVar[int]
            ACTIVATION_FN_FIELD_NUMBER: _ClassVar[int]
            OPTIMIZER_FIELD_NUMBER: _ClassVar[int]
            BUDGET_HOURS_FIELD_NUMBER: _ClassVar[int]
            STANDARDIZE_FEATURES_FIELD_NUMBER: _ClassVar[int]
            L1_REG_ACTIVATION_FIELD_NUMBER: _ClassVar[int]
            MODEL_REGISTRY_FIELD_NUMBER: _ClassVar[int]
            VERTEX_AI_MODEL_VERSION_ALIASES_FIELD_NUMBER: _ClassVar[int]
            DIMENSION_ID_COLUMNS_FIELD_NUMBER: _ClassVar[int]
            CONTRIBUTION_METRIC_FIELD_NUMBER: _ClassVar[int]
            IS_TEST_COLUMN_FIELD_NUMBER: _ClassVar[int]
            MIN_APRIORI_SUPPORT_FIELD_NUMBER: _ClassVar[int]
            max_iterations: int
            loss_type: Model.LossType
            learn_rate: float
            l1_regularization: _wrappers_pb2.DoubleValue
            l2_regularization: _wrappers_pb2.DoubleValue
            min_relative_progress: _wrappers_pb2.DoubleValue
            warm_start: _wrappers_pb2.BoolValue
            early_stop: _wrappers_pb2.BoolValue
            input_label_columns: _containers.RepeatedScalarFieldContainer[str]
            data_split_method: Model.DataSplitMethod
            data_split_eval_fraction: float
            data_split_column: str
            learn_rate_strategy: Model.LearnRateStrategy
            initial_learn_rate: float
            label_class_weights: _containers.ScalarMap[str, float]
            user_column: str
            item_column: str
            distance_type: Model.DistanceType
            num_clusters: int
            model_uri: str
            optimization_strategy: Model.OptimizationStrategy
            hidden_units: _containers.RepeatedScalarFieldContainer[int]
            batch_size: int
            dropout: _wrappers_pb2.DoubleValue
            max_tree_depth: int
            subsample: float
            min_split_loss: _wrappers_pb2.DoubleValue
            booster_type: Model.BoostedTreeOptionEnums.BoosterType
            num_parallel_tree: _wrappers_pb2.Int64Value
            dart_normalize_type: Model.BoostedTreeOptionEnums.DartNormalizeType
            tree_method: Model.BoostedTreeOptionEnums.TreeMethod
            min_tree_child_weight: _wrappers_pb2.Int64Value
            colsample_bytree: _wrappers_pb2.DoubleValue
            colsample_bylevel: _wrappers_pb2.DoubleValue
            colsample_bynode: _wrappers_pb2.DoubleValue
            num_factors: int
            feedback_type: Model.FeedbackType
            wals_alpha: _wrappers_pb2.DoubleValue
            kmeans_initialization_method: Model.KmeansEnums.KmeansInitializationMethod
            kmeans_initialization_column: str
            time_series_timestamp_column: str
            time_series_data_column: str
            auto_arima: _wrappers_pb2.BoolValue
            non_seasonal_order: Model.ArimaOrder
            data_frequency: Model.DataFrequency
            calculate_p_values: _wrappers_pb2.BoolValue
            include_drift: _wrappers_pb2.BoolValue
            holiday_region: Model.HolidayRegion
            holiday_regions: _containers.RepeatedScalarFieldContainer[Model.HolidayRegion]
            time_series_id_column: str
            time_series_id_columns: _containers.RepeatedScalarFieldContainer[str]
            horizon: int
            auto_arima_max_order: int
            auto_arima_min_order: int
            num_trials: int
            max_parallel_trials: int
            hparam_tuning_objectives: _containers.RepeatedScalarFieldContainer[Model.HparamTuningEnums.HparamTuningObjective]
            decompose_time_series: _wrappers_pb2.BoolValue
            clean_spikes_and_dips: _wrappers_pb2.BoolValue
            adjust_step_changes: _wrappers_pb2.BoolValue
            enable_global_explain: _wrappers_pb2.BoolValue
            sampled_shapley_num_paths: int
            integrated_gradients_num_steps: int
            category_encoding_method: Model.CategoryEncodingMethod.EncodingMethod
            tf_version: str
            color_space: Model.ColorSpace
            instance_weight_column: str
            trend_smoothing_window_size: int
            time_series_length_fraction: float
            min_time_series_length: int
            max_time_series_length: int
            xgboost_version: str
            approx_global_feature_contrib: _wrappers_pb2.BoolValue
            fit_intercept: _wrappers_pb2.BoolValue
            num_principal_components: int
            pca_explained_variance_ratio: float
            scale_features: _wrappers_pb2.BoolValue
            pca_solver: Model.PcaSolverOptionEnums.PcaSolver
            auto_class_weights: _wrappers_pb2.BoolValue
            activation_fn: str
            optimizer: str
            budget_hours: float
            standardize_features: _wrappers_pb2.BoolValue
            l1_reg_activation: float
            model_registry: Model.ModelRegistryOptionEnums.ModelRegistry
            vertex_ai_model_version_aliases: _containers.RepeatedScalarFieldContainer[str]
            dimension_id_columns: _containers.RepeatedScalarFieldContainer[str]
            contribution_metric: str
            is_test_column: str
            min_apriori_support: float
            def __init__(self, max_iterations: _Optional[int] = ..., loss_type: _Optional[_Union[Model.LossType, str]] = ..., learn_rate: _Optional[float] = ..., l1_regularization: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ..., l2_regularization: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ..., min_relative_progress: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ..., warm_start: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., early_stop: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., input_label_columns: _Optional[_Iterable[str]] = ..., data_split_method: _Optional[_Union[Model.DataSplitMethod, str]] = ..., data_split_eval_fraction: _Optional[float] = ..., data_split_column: _Optional[str] = ..., learn_rate_strategy: _Optional[_Union[Model.LearnRateStrategy, str]] = ..., initial_learn_rate: _Optional[float] = ..., label_class_weights: _Optional[_Mapping[str, float]] = ..., user_column: _Optional[str] = ..., item_column: _Optional[str] = ..., distance_type: _Optional[_Union[Model.DistanceType, str]] = ..., num_clusters: _Optional[int] = ..., model_uri: _Optional[str] = ..., optimization_strategy: _Optional[_Union[Model.OptimizationStrategy, str]] = ..., hidden_units: _Optional[_Iterable[int]] = ..., batch_size: _Optional[int] = ..., dropout: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ..., max_tree_depth: _Optional[int] = ..., subsample: _Optional[float] = ..., min_split_loss: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ..., booster_type: _Optional[_Union[Model.BoostedTreeOptionEnums.BoosterType, str]] = ..., num_parallel_tree: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., dart_normalize_type: _Optional[_Union[Model.BoostedTreeOptionEnums.DartNormalizeType, str]] = ..., tree_method: _Optional[_Union[Model.BoostedTreeOptionEnums.TreeMethod, str]] = ..., min_tree_child_weight: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., colsample_bytree: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ..., colsample_bylevel: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ..., colsample_bynode: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ..., num_factors: _Optional[int] = ..., feedback_type: _Optional[_Union[Model.FeedbackType, str]] = ..., wals_alpha: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ..., kmeans_initialization_method: _Optional[_Union[Model.KmeansEnums.KmeansInitializationMethod, str]] = ..., kmeans_initialization_column: _Optional[str] = ..., time_series_timestamp_column: _Optional[str] = ..., time_series_data_column: _Optional[str] = ..., auto_arima: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., non_seasonal_order: _Optional[_Union[Model.ArimaOrder, _Mapping]] = ..., data_frequency: _Optional[_Union[Model.DataFrequency, str]] = ..., calculate_p_values: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., include_drift: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., holiday_region: _Optional[_Union[Model.HolidayRegion, str]] = ..., holiday_regions: _Optional[_Iterable[_Union[Model.HolidayRegion, str]]] = ..., time_series_id_column: _Optional[str] = ..., time_series_id_columns: _Optional[_Iterable[str]] = ..., horizon: _Optional[int] = ..., auto_arima_max_order: _Optional[int] = ..., auto_arima_min_order: _Optional[int] = ..., num_trials: _Optional[int] = ..., max_parallel_trials: _Optional[int] = ..., hparam_tuning_objectives: _Optional[_Iterable[_Union[Model.HparamTuningEnums.HparamTuningObjective, str]]] = ..., decompose_time_series: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., clean_spikes_and_dips: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., adjust_step_changes: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., enable_global_explain: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., sampled_shapley_num_paths: _Optional[int] = ..., integrated_gradients_num_steps: _Optional[int] = ..., category_encoding_method: _Optional[_Union[Model.CategoryEncodingMethod.EncodingMethod, str]] = ..., tf_version: _Optional[str] = ..., color_space: _Optional[_Union[Model.ColorSpace, str]] = ..., instance_weight_column: _Optional[str] = ..., trend_smoothing_window_size: _Optional[int] = ..., time_series_length_fraction: _Optional[float] = ..., min_time_series_length: _Optional[int] = ..., max_time_series_length: _Optional[int] = ..., xgboost_version: _Optional[str] = ..., approx_global_feature_contrib: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., fit_intercept: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., num_principal_components: _Optional[int] = ..., pca_explained_variance_ratio: _Optional[float] = ..., scale_features: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., pca_solver: _Optional[_Union[Model.PcaSolverOptionEnums.PcaSolver, str]] = ..., auto_class_weights: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., activation_fn: _Optional[str] = ..., optimizer: _Optional[str] = ..., budget_hours: _Optional[float] = ..., standardize_features: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., l1_reg_activation: _Optional[float] = ..., model_registry: _Optional[_Union[Model.ModelRegistryOptionEnums.ModelRegistry, str]] = ..., vertex_ai_model_version_aliases: _Optional[_Iterable[str]] = ..., dimension_id_columns: _Optional[_Iterable[str]] = ..., contribution_metric: _Optional[str] = ..., is_test_column: _Optional[str] = ..., min_apriori_support: _Optional[float] = ...) -> None: ...
        class IterationResult(_message.Message):
            __slots__ = ("index", "duration_ms", "training_loss", "eval_loss", "learn_rate", "cluster_infos", "arima_result", "principal_component_infos")
            class ClusterInfo(_message.Message):
                __slots__ = ("centroid_id", "cluster_radius", "cluster_size")
                CENTROID_ID_FIELD_NUMBER: _ClassVar[int]
                CLUSTER_RADIUS_FIELD_NUMBER: _ClassVar[int]
                CLUSTER_SIZE_FIELD_NUMBER: _ClassVar[int]
                centroid_id: int
                cluster_radius: _wrappers_pb2.DoubleValue
                cluster_size: _wrappers_pb2.Int64Value
                def __init__(self, centroid_id: _Optional[int] = ..., cluster_radius: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ..., cluster_size: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ...) -> None: ...
            class ArimaResult(_message.Message):
                __slots__ = ("arima_model_info", "seasonal_periods")
                class ArimaCoefficients(_message.Message):
                    __slots__ = ("auto_regressive_coefficients", "moving_average_coefficients", "intercept_coefficient")
                    AUTO_REGRESSIVE_COEFFICIENTS_FIELD_NUMBER: _ClassVar[int]
                    MOVING_AVERAGE_COEFFICIENTS_FIELD_NUMBER: _ClassVar[int]
                    INTERCEPT_COEFFICIENT_FIELD_NUMBER: _ClassVar[int]
                    auto_regressive_coefficients: _containers.RepeatedScalarFieldContainer[float]
                    moving_average_coefficients: _containers.RepeatedScalarFieldContainer[float]
                    intercept_coefficient: _wrappers_pb2.DoubleValue
                    def __init__(self, auto_regressive_coefficients: _Optional[_Iterable[float]] = ..., moving_average_coefficients: _Optional[_Iterable[float]] = ..., intercept_coefficient: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ...) -> None: ...
                class ArimaModelInfo(_message.Message):
                    __slots__ = ("non_seasonal_order", "arima_coefficients", "arima_fitting_metrics", "has_drift", "time_series_id", "time_series_ids", "seasonal_periods", "has_holiday_effect", "has_spikes_and_dips", "has_step_changes")
                    NON_SEASONAL_ORDER_FIELD_NUMBER: _ClassVar[int]
                    ARIMA_COEFFICIENTS_FIELD_NUMBER: _ClassVar[int]
                    ARIMA_FITTING_METRICS_FIELD_NUMBER: _ClassVar[int]
                    HAS_DRIFT_FIELD_NUMBER: _ClassVar[int]
                    TIME_SERIES_ID_FIELD_NUMBER: _ClassVar[int]
                    TIME_SERIES_IDS_FIELD_NUMBER: _ClassVar[int]
                    SEASONAL_PERIODS_FIELD_NUMBER: _ClassVar[int]
                    HAS_HOLIDAY_EFFECT_FIELD_NUMBER: _ClassVar[int]
                    HAS_SPIKES_AND_DIPS_FIELD_NUMBER: _ClassVar[int]
                    HAS_STEP_CHANGES_FIELD_NUMBER: _ClassVar[int]
                    non_seasonal_order: Model.ArimaOrder
                    arima_coefficients: Model.TrainingRun.IterationResult.ArimaResult.ArimaCoefficients
                    arima_fitting_metrics: Model.ArimaFittingMetrics
                    has_drift: _wrappers_pb2.BoolValue
                    time_series_id: str
                    time_series_ids: _containers.RepeatedScalarFieldContainer[str]
                    seasonal_periods: _containers.RepeatedScalarFieldContainer[Model.SeasonalPeriod.SeasonalPeriodType]
                    has_holiday_effect: _wrappers_pb2.BoolValue
                    has_spikes_and_dips: _wrappers_pb2.BoolValue
                    has_step_changes: _wrappers_pb2.BoolValue
                    def __init__(self, non_seasonal_order: _Optional[_Union[Model.ArimaOrder, _Mapping]] = ..., arima_coefficients: _Optional[_Union[Model.TrainingRun.IterationResult.ArimaResult.ArimaCoefficients, _Mapping]] = ..., arima_fitting_metrics: _Optional[_Union[Model.ArimaFittingMetrics, _Mapping]] = ..., has_drift: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., time_series_id: _Optional[str] = ..., time_series_ids: _Optional[_Iterable[str]] = ..., seasonal_periods: _Optional[_Iterable[_Union[Model.SeasonalPeriod.SeasonalPeriodType, str]]] = ..., has_holiday_effect: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., has_spikes_and_dips: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., has_step_changes: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...) -> None: ...
                ARIMA_MODEL_INFO_FIELD_NUMBER: _ClassVar[int]
                SEASONAL_PERIODS_FIELD_NUMBER: _ClassVar[int]
                arima_model_info: _containers.RepeatedCompositeFieldContainer[Model.TrainingRun.IterationResult.ArimaResult.ArimaModelInfo]
                seasonal_periods: _containers.RepeatedScalarFieldContainer[Model.SeasonalPeriod.SeasonalPeriodType]
                def __init__(self, arima_model_info: _Optional[_Iterable[_Union[Model.TrainingRun.IterationResult.ArimaResult.ArimaModelInfo, _Mapping]]] = ..., seasonal_periods: _Optional[_Iterable[_Union[Model.SeasonalPeriod.SeasonalPeriodType, str]]] = ...) -> None: ...
            class PrincipalComponentInfo(_message.Message):
                __slots__ = ("principal_component_id", "explained_variance", "explained_variance_ratio", "cumulative_explained_variance_ratio")
                PRINCIPAL_COMPONENT_ID_FIELD_NUMBER: _ClassVar[int]
                EXPLAINED_VARIANCE_FIELD_NUMBER: _ClassVar[int]
                EXPLAINED_VARIANCE_RATIO_FIELD_NUMBER: _ClassVar[int]
                CUMULATIVE_EXPLAINED_VARIANCE_RATIO_FIELD_NUMBER: _ClassVar[int]
                principal_component_id: _wrappers_pb2.Int64Value
                explained_variance: _wrappers_pb2.DoubleValue
                explained_variance_ratio: _wrappers_pb2.DoubleValue
                cumulative_explained_variance_ratio: _wrappers_pb2.DoubleValue
                def __init__(self, principal_component_id: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., explained_variance: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ..., explained_variance_ratio: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ..., cumulative_explained_variance_ratio: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ...) -> None: ...
            INDEX_FIELD_NUMBER: _ClassVar[int]
            DURATION_MS_FIELD_NUMBER: _ClassVar[int]
            TRAINING_LOSS_FIELD_NUMBER: _ClassVar[int]
            EVAL_LOSS_FIELD_NUMBER: _ClassVar[int]
            LEARN_RATE_FIELD_NUMBER: _ClassVar[int]
            CLUSTER_INFOS_FIELD_NUMBER: _ClassVar[int]
            ARIMA_RESULT_FIELD_NUMBER: _ClassVar[int]
            PRINCIPAL_COMPONENT_INFOS_FIELD_NUMBER: _ClassVar[int]
            index: _wrappers_pb2.Int32Value
            duration_ms: _wrappers_pb2.Int64Value
            training_loss: _wrappers_pb2.DoubleValue
            eval_loss: _wrappers_pb2.DoubleValue
            learn_rate: float
            cluster_infos: _containers.RepeatedCompositeFieldContainer[Model.TrainingRun.IterationResult.ClusterInfo]
            arima_result: Model.TrainingRun.IterationResult.ArimaResult
            principal_component_infos: _containers.RepeatedCompositeFieldContainer[Model.TrainingRun.IterationResult.PrincipalComponentInfo]
            def __init__(self, index: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., duration_ms: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., training_loss: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ..., eval_loss: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ..., learn_rate: _Optional[float] = ..., cluster_infos: _Optional[_Iterable[_Union[Model.TrainingRun.IterationResult.ClusterInfo, _Mapping]]] = ..., arima_result: _Optional[_Union[Model.TrainingRun.IterationResult.ArimaResult, _Mapping]] = ..., principal_component_infos: _Optional[_Iterable[_Union[Model.TrainingRun.IterationResult.PrincipalComponentInfo, _Mapping]]] = ...) -> None: ...
        TRAINING_OPTIONS_FIELD_NUMBER: _ClassVar[int]
        START_TIME_FIELD_NUMBER: _ClassVar[int]
        RESULTS_FIELD_NUMBER: _ClassVar[int]
        EVALUATION_METRICS_FIELD_NUMBER: _ClassVar[int]
        DATA_SPLIT_RESULT_FIELD_NUMBER: _ClassVar[int]
        MODEL_LEVEL_GLOBAL_EXPLANATION_FIELD_NUMBER: _ClassVar[int]
        CLASS_LEVEL_GLOBAL_EXPLANATIONS_FIELD_NUMBER: _ClassVar[int]
        VERTEX_AI_MODEL_ID_FIELD_NUMBER: _ClassVar[int]
        VERTEX_AI_MODEL_VERSION_FIELD_NUMBER: _ClassVar[int]
        training_options: Model.TrainingRun.TrainingOptions
        start_time: _timestamp_pb2.Timestamp
        results: _containers.RepeatedCompositeFieldContainer[Model.TrainingRun.IterationResult]
        evaluation_metrics: Model.EvaluationMetrics
        data_split_result: Model.DataSplitResult
        model_level_global_explanation: Model.GlobalExplanation
        class_level_global_explanations: _containers.RepeatedCompositeFieldContainer[Model.GlobalExplanation]
        vertex_ai_model_id: str
        vertex_ai_model_version: str
        def __init__(self, training_options: _Optional[_Union[Model.TrainingRun.TrainingOptions, _Mapping]] = ..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., results: _Optional[_Iterable[_Union[Model.TrainingRun.IterationResult, _Mapping]]] = ..., evaluation_metrics: _Optional[_Union[Model.EvaluationMetrics, _Mapping]] = ..., data_split_result: _Optional[_Union[Model.DataSplitResult, _Mapping]] = ..., model_level_global_explanation: _Optional[_Union[Model.GlobalExplanation, _Mapping]] = ..., class_level_global_explanations: _Optional[_Iterable[_Union[Model.GlobalExplanation, _Mapping]]] = ..., vertex_ai_model_id: _Optional[str] = ..., vertex_ai_model_version: _Optional[str] = ...) -> None: ...
    class DoubleHparamSearchSpace(_message.Message):
        __slots__ = ("range", "candidates")
        class DoubleRange(_message.Message):
            __slots__ = ("min", "max")
            MIN_FIELD_NUMBER: _ClassVar[int]
            MAX_FIELD_NUMBER: _ClassVar[int]
            min: _wrappers_pb2.DoubleValue
            max: _wrappers_pb2.DoubleValue
            def __init__(self, min: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ..., max: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ...) -> None: ...
        class DoubleCandidates(_message.Message):
            __slots__ = ("candidates",)
            CANDIDATES_FIELD_NUMBER: _ClassVar[int]
            candidates: _containers.RepeatedCompositeFieldContainer[_wrappers_pb2.DoubleValue]
            def __init__(self, candidates: _Optional[_Iterable[_Union[_wrappers_pb2.DoubleValue, _Mapping]]] = ...) -> None: ...
        RANGE_FIELD_NUMBER: _ClassVar[int]
        CANDIDATES_FIELD_NUMBER: _ClassVar[int]
        range: Model.DoubleHparamSearchSpace.DoubleRange
        candidates: Model.DoubleHparamSearchSpace.DoubleCandidates
        def __init__(self, range: _Optional[_Union[Model.DoubleHparamSearchSpace.DoubleRange, _Mapping]] = ..., candidates: _Optional[_Union[Model.DoubleHparamSearchSpace.DoubleCandidates, _Mapping]] = ...) -> None: ...
    class IntHparamSearchSpace(_message.Message):
        __slots__ = ("range", "candidates")
        class IntRange(_message.Message):
            __slots__ = ("min", "max")
            MIN_FIELD_NUMBER: _ClassVar[int]
            MAX_FIELD_NUMBER: _ClassVar[int]
            min: _wrappers_pb2.Int64Value
            max: _wrappers_pb2.Int64Value
            def __init__(self, min: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., max: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ...) -> None: ...
        class IntCandidates(_message.Message):
            __slots__ = ("candidates",)
            CANDIDATES_FIELD_NUMBER: _ClassVar[int]
            candidates: _containers.RepeatedCompositeFieldContainer[_wrappers_pb2.Int64Value]
            def __init__(self, candidates: _Optional[_Iterable[_Union[_wrappers_pb2.Int64Value, _Mapping]]] = ...) -> None: ...
        RANGE_FIELD_NUMBER: _ClassVar[int]
        CANDIDATES_FIELD_NUMBER: _ClassVar[int]
        range: Model.IntHparamSearchSpace.IntRange
        candidates: Model.IntHparamSearchSpace.IntCandidates
        def __init__(self, range: _Optional[_Union[Model.IntHparamSearchSpace.IntRange, _Mapping]] = ..., candidates: _Optional[_Union[Model.IntHparamSearchSpace.IntCandidates, _Mapping]] = ...) -> None: ...
    class StringHparamSearchSpace(_message.Message):
        __slots__ = ("candidates",)
        CANDIDATES_FIELD_NUMBER: _ClassVar[int]
        candidates: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, candidates: _Optional[_Iterable[str]] = ...) -> None: ...
    class IntArrayHparamSearchSpace(_message.Message):
        __slots__ = ("candidates",)
        class IntArray(_message.Message):
            __slots__ = ("elements",)
            ELEMENTS_FIELD_NUMBER: _ClassVar[int]
            elements: _containers.RepeatedScalarFieldContainer[int]
            def __init__(self, elements: _Optional[_Iterable[int]] = ...) -> None: ...
        CANDIDATES_FIELD_NUMBER: _ClassVar[int]
        candidates: _containers.RepeatedCompositeFieldContainer[Model.IntArrayHparamSearchSpace.IntArray]
        def __init__(self, candidates: _Optional[_Iterable[_Union[Model.IntArrayHparamSearchSpace.IntArray, _Mapping]]] = ...) -> None: ...
    class HparamSearchSpaces(_message.Message):
        __slots__ = ("learn_rate", "l1_reg", "l2_reg", "num_clusters", "num_factors", "hidden_units", "batch_size", "dropout", "max_tree_depth", "subsample", "min_split_loss", "wals_alpha", "booster_type", "num_parallel_tree", "dart_normalize_type", "tree_method", "min_tree_child_weight", "colsample_bytree", "colsample_bylevel", "colsample_bynode", "activation_fn", "optimizer")
        LEARN_RATE_FIELD_NUMBER: _ClassVar[int]
        L1_REG_FIELD_NUMBER: _ClassVar[int]
        L2_REG_FIELD_NUMBER: _ClassVar[int]
        NUM_CLUSTERS_FIELD_NUMBER: _ClassVar[int]
        NUM_FACTORS_FIELD_NUMBER: _ClassVar[int]
        HIDDEN_UNITS_FIELD_NUMBER: _ClassVar[int]
        BATCH_SIZE_FIELD_NUMBER: _ClassVar[int]
        DROPOUT_FIELD_NUMBER: _ClassVar[int]
        MAX_TREE_DEPTH_FIELD_NUMBER: _ClassVar[int]
        SUBSAMPLE_FIELD_NUMBER: _ClassVar[int]
        MIN_SPLIT_LOSS_FIELD_NUMBER: _ClassVar[int]
        WALS_ALPHA_FIELD_NUMBER: _ClassVar[int]
        BOOSTER_TYPE_FIELD_NUMBER: _ClassVar[int]
        NUM_PARALLEL_TREE_FIELD_NUMBER: _ClassVar[int]
        DART_NORMALIZE_TYPE_FIELD_NUMBER: _ClassVar[int]
        TREE_METHOD_FIELD_NUMBER: _ClassVar[int]
        MIN_TREE_CHILD_WEIGHT_FIELD_NUMBER: _ClassVar[int]
        COLSAMPLE_BYTREE_FIELD_NUMBER: _ClassVar[int]
        COLSAMPLE_BYLEVEL_FIELD_NUMBER: _ClassVar[int]
        COLSAMPLE_BYNODE_FIELD_NUMBER: _ClassVar[int]
        ACTIVATION_FN_FIELD_NUMBER: _ClassVar[int]
        OPTIMIZER_FIELD_NUMBER: _ClassVar[int]
        learn_rate: Model.DoubleHparamSearchSpace
        l1_reg: Model.DoubleHparamSearchSpace
        l2_reg: Model.DoubleHparamSearchSpace
        num_clusters: Model.IntHparamSearchSpace
        num_factors: Model.IntHparamSearchSpace
        hidden_units: Model.IntArrayHparamSearchSpace
        batch_size: Model.IntHparamSearchSpace
        dropout: Model.DoubleHparamSearchSpace
        max_tree_depth: Model.IntHparamSearchSpace
        subsample: Model.DoubleHparamSearchSpace
        min_split_loss: Model.DoubleHparamSearchSpace
        wals_alpha: Model.DoubleHparamSearchSpace
        booster_type: Model.StringHparamSearchSpace
        num_parallel_tree: Model.IntHparamSearchSpace
        dart_normalize_type: Model.StringHparamSearchSpace
        tree_method: Model.StringHparamSearchSpace
        min_tree_child_weight: Model.IntHparamSearchSpace
        colsample_bytree: Model.DoubleHparamSearchSpace
        colsample_bylevel: Model.DoubleHparamSearchSpace
        colsample_bynode: Model.DoubleHparamSearchSpace
        activation_fn: Model.StringHparamSearchSpace
        optimizer: Model.StringHparamSearchSpace
        def __init__(self, learn_rate: _Optional[_Union[Model.DoubleHparamSearchSpace, _Mapping]] = ..., l1_reg: _Optional[_Union[Model.DoubleHparamSearchSpace, _Mapping]] = ..., l2_reg: _Optional[_Union[Model.DoubleHparamSearchSpace, _Mapping]] = ..., num_clusters: _Optional[_Union[Model.IntHparamSearchSpace, _Mapping]] = ..., num_factors: _Optional[_Union[Model.IntHparamSearchSpace, _Mapping]] = ..., hidden_units: _Optional[_Union[Model.IntArrayHparamSearchSpace, _Mapping]] = ..., batch_size: _Optional[_Union[Model.IntHparamSearchSpace, _Mapping]] = ..., dropout: _Optional[_Union[Model.DoubleHparamSearchSpace, _Mapping]] = ..., max_tree_depth: _Optional[_Union[Model.IntHparamSearchSpace, _Mapping]] = ..., subsample: _Optional[_Union[Model.DoubleHparamSearchSpace, _Mapping]] = ..., min_split_loss: _Optional[_Union[Model.DoubleHparamSearchSpace, _Mapping]] = ..., wals_alpha: _Optional[_Union[Model.DoubleHparamSearchSpace, _Mapping]] = ..., booster_type: _Optional[_Union[Model.StringHparamSearchSpace, _Mapping]] = ..., num_parallel_tree: _Optional[_Union[Model.IntHparamSearchSpace, _Mapping]] = ..., dart_normalize_type: _Optional[_Union[Model.StringHparamSearchSpace, _Mapping]] = ..., tree_method: _Optional[_Union[Model.StringHparamSearchSpace, _Mapping]] = ..., min_tree_child_weight: _Optional[_Union[Model.IntHparamSearchSpace, _Mapping]] = ..., colsample_bytree: _Optional[_Union[Model.DoubleHparamSearchSpace, _Mapping]] = ..., colsample_bylevel: _Optional[_Union[Model.DoubleHparamSearchSpace, _Mapping]] = ..., colsample_bynode: _Optional[_Union[Model.DoubleHparamSearchSpace, _Mapping]] = ..., activation_fn: _Optional[_Union[Model.StringHparamSearchSpace, _Mapping]] = ..., optimizer: _Optional[_Union[Model.StringHparamSearchSpace, _Mapping]] = ...) -> None: ...
    class HparamTuningTrial(_message.Message):
        __slots__ = ("trial_id", "start_time_ms", "end_time_ms", "hparams", "evaluation_metrics", "status", "error_message", "training_loss", "eval_loss", "hparam_tuning_evaluation_metrics")
        class TrialStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            TRIAL_STATUS_UNSPECIFIED: _ClassVar[Model.HparamTuningTrial.TrialStatus]
            NOT_STARTED: _ClassVar[Model.HparamTuningTrial.TrialStatus]
            RUNNING: _ClassVar[Model.HparamTuningTrial.TrialStatus]
            SUCCEEDED: _ClassVar[Model.HparamTuningTrial.TrialStatus]
            FAILED: _ClassVar[Model.HparamTuningTrial.TrialStatus]
            INFEASIBLE: _ClassVar[Model.HparamTuningTrial.TrialStatus]
            STOPPED_EARLY: _ClassVar[Model.HparamTuningTrial.TrialStatus]
        TRIAL_STATUS_UNSPECIFIED: Model.HparamTuningTrial.TrialStatus
        NOT_STARTED: Model.HparamTuningTrial.TrialStatus
        RUNNING: Model.HparamTuningTrial.TrialStatus
        SUCCEEDED: Model.HparamTuningTrial.TrialStatus
        FAILED: Model.HparamTuningTrial.TrialStatus
        INFEASIBLE: Model.HparamTuningTrial.TrialStatus
        STOPPED_EARLY: Model.HparamTuningTrial.TrialStatus
        TRIAL_ID_FIELD_NUMBER: _ClassVar[int]
        START_TIME_MS_FIELD_NUMBER: _ClassVar[int]
        END_TIME_MS_FIELD_NUMBER: _ClassVar[int]
        HPARAMS_FIELD_NUMBER: _ClassVar[int]
        EVALUATION_METRICS_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        TRAINING_LOSS_FIELD_NUMBER: _ClassVar[int]
        EVAL_LOSS_FIELD_NUMBER: _ClassVar[int]
        HPARAM_TUNING_EVALUATION_METRICS_FIELD_NUMBER: _ClassVar[int]
        trial_id: int
        start_time_ms: int
        end_time_ms: int
        hparams: Model.TrainingRun.TrainingOptions
        evaluation_metrics: Model.EvaluationMetrics
        status: Model.HparamTuningTrial.TrialStatus
        error_message: str
        training_loss: _wrappers_pb2.DoubleValue
        eval_loss: _wrappers_pb2.DoubleValue
        hparam_tuning_evaluation_metrics: Model.EvaluationMetrics
        def __init__(self, trial_id: _Optional[int] = ..., start_time_ms: _Optional[int] = ..., end_time_ms: _Optional[int] = ..., hparams: _Optional[_Union[Model.TrainingRun.TrainingOptions, _Mapping]] = ..., evaluation_metrics: _Optional[_Union[Model.EvaluationMetrics, _Mapping]] = ..., status: _Optional[_Union[Model.HparamTuningTrial.TrialStatus, str]] = ..., error_message: _Optional[str] = ..., training_loss: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ..., eval_loss: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ..., hparam_tuning_evaluation_metrics: _Optional[_Union[Model.EvaluationMetrics, _Mapping]] = ...) -> None: ...
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ETAG_FIELD_NUMBER: _ClassVar[int]
    MODEL_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    CREATION_TIME_FIELD_NUMBER: _ClassVar[int]
    LAST_MODIFIED_TIME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    FRIENDLY_NAME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_TIME_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    MODEL_TYPE_FIELD_NUMBER: _ClassVar[int]
    TRAINING_RUNS_FIELD_NUMBER: _ClassVar[int]
    FEATURE_COLUMNS_FIELD_NUMBER: _ClassVar[int]
    LABEL_COLUMNS_FIELD_NUMBER: _ClassVar[int]
    TRANSFORM_COLUMNS_FIELD_NUMBER: _ClassVar[int]
    HPARAM_SEARCH_SPACES_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_TRIAL_ID_FIELD_NUMBER: _ClassVar[int]
    HPARAM_TRIALS_FIELD_NUMBER: _ClassVar[int]
    OPTIMAL_TRIAL_IDS_FIELD_NUMBER: _ClassVar[int]
    REMOTE_MODEL_INFO_FIELD_NUMBER: _ClassVar[int]
    etag: str
    model_reference: _model_reference_pb2.ModelReference
    creation_time: int
    last_modified_time: int
    description: str
    friendly_name: str
    labels: _containers.ScalarMap[str, str]
    expiration_time: int
    location: str
    encryption_configuration: _encryption_config_pb2.EncryptionConfiguration
    model_type: Model.ModelType
    training_runs: _containers.RepeatedCompositeFieldContainer[Model.TrainingRun]
    feature_columns: _containers.RepeatedCompositeFieldContainer[_standard_sql_pb2.StandardSqlField]
    label_columns: _containers.RepeatedCompositeFieldContainer[_standard_sql_pb2.StandardSqlField]
    transform_columns: _containers.RepeatedCompositeFieldContainer[TransformColumn]
    hparam_search_spaces: Model.HparamSearchSpaces
    default_trial_id: int
    hparam_trials: _containers.RepeatedCompositeFieldContainer[Model.HparamTuningTrial]
    optimal_trial_ids: _containers.RepeatedScalarFieldContainer[int]
    remote_model_info: RemoteModelInfo
    def __init__(self, etag: _Optional[str] = ..., model_reference: _Optional[_Union[_model_reference_pb2.ModelReference, _Mapping]] = ..., creation_time: _Optional[int] = ..., last_modified_time: _Optional[int] = ..., description: _Optional[str] = ..., friendly_name: _Optional[str] = ..., labels: _Optional[_Mapping[str, str]] = ..., expiration_time: _Optional[int] = ..., location: _Optional[str] = ..., encryption_configuration: _Optional[_Union[_encryption_config_pb2.EncryptionConfiguration, _Mapping]] = ..., model_type: _Optional[_Union[Model.ModelType, str]] = ..., training_runs: _Optional[_Iterable[_Union[Model.TrainingRun, _Mapping]]] = ..., feature_columns: _Optional[_Iterable[_Union[_standard_sql_pb2.StandardSqlField, _Mapping]]] = ..., label_columns: _Optional[_Iterable[_Union[_standard_sql_pb2.StandardSqlField, _Mapping]]] = ..., transform_columns: _Optional[_Iterable[_Union[TransformColumn, _Mapping]]] = ..., hparam_search_spaces: _Optional[_Union[Model.HparamSearchSpaces, _Mapping]] = ..., default_trial_id: _Optional[int] = ..., hparam_trials: _Optional[_Iterable[_Union[Model.HparamTuningTrial, _Mapping]]] = ..., optimal_trial_ids: _Optional[_Iterable[int]] = ..., remote_model_info: _Optional[_Union[RemoteModelInfo, _Mapping]] = ...) -> None: ...

class GetModelRequest(_message.Message):
    __slots__ = ("project_id", "dataset_id", "model_id")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    DATASET_ID_FIELD_NUMBER: _ClassVar[int]
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    dataset_id: str
    model_id: str
    def __init__(self, project_id: _Optional[str] = ..., dataset_id: _Optional[str] = ..., model_id: _Optional[str] = ...) -> None: ...

class PatchModelRequest(_message.Message):
    __slots__ = ("project_id", "dataset_id", "model_id", "model")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    DATASET_ID_FIELD_NUMBER: _ClassVar[int]
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    dataset_id: str
    model_id: str
    model: Model
    def __init__(self, project_id: _Optional[str] = ..., dataset_id: _Optional[str] = ..., model_id: _Optional[str] = ..., model: _Optional[_Union[Model, _Mapping]] = ...) -> None: ...

class DeleteModelRequest(_message.Message):
    __slots__ = ("project_id", "dataset_id", "model_id")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    DATASET_ID_FIELD_NUMBER: _ClassVar[int]
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    dataset_id: str
    model_id: str
    def __init__(self, project_id: _Optional[str] = ..., dataset_id: _Optional[str] = ..., model_id: _Optional[str] = ...) -> None: ...

class ListModelsRequest(_message.Message):
    __slots__ = ("project_id", "dataset_id", "max_results", "page_token")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    DATASET_ID_FIELD_NUMBER: _ClassVar[int]
    MAX_RESULTS_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    dataset_id: str
    max_results: _wrappers_pb2.UInt32Value
    page_token: str
    def __init__(self, project_id: _Optional[str] = ..., dataset_id: _Optional[str] = ..., max_results: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListModelsResponse(_message.Message):
    __slots__ = ("models", "next_page_token")
    MODELS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    models: _containers.RepeatedCompositeFieldContainer[Model]
    next_page_token: str
    def __init__(self, models: _Optional[_Iterable[_Union[Model, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...
