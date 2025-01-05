from google.cloud.automl.v1beta1 import classification_pb2 as _classification_pb2
from google.cloud.automl.v1beta1 import column_spec_pb2 as _column_spec_pb2
from google.cloud.automl.v1beta1 import data_items_pb2 as _data_items_pb2
from google.cloud.automl.v1beta1 import data_stats_pb2 as _data_stats_pb2
from google.cloud.automl.v1beta1 import ranges_pb2 as _ranges_pb2
from google.cloud.automl.v1beta1 import regression_pb2 as _regression_pb2
from google.cloud.automl.v1beta1 import temporal_pb2 as _temporal_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class TablesDatasetMetadata(_message.Message):
    __slots__ = ('primary_table_spec_id', 'target_column_spec_id', 'weight_column_spec_id', 'ml_use_column_spec_id', 'target_column_correlations', 'stats_update_time')

    class TargetColumnCorrelationsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _data_stats_pb2.CorrelationStats

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[_data_stats_pb2.CorrelationStats, _Mapping]]=...) -> None:
            ...
    PRIMARY_TABLE_SPEC_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_COLUMN_SPEC_ID_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_COLUMN_SPEC_ID_FIELD_NUMBER: _ClassVar[int]
    ML_USE_COLUMN_SPEC_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_COLUMN_CORRELATIONS_FIELD_NUMBER: _ClassVar[int]
    STATS_UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    primary_table_spec_id: str
    target_column_spec_id: str
    weight_column_spec_id: str
    ml_use_column_spec_id: str
    target_column_correlations: _containers.MessageMap[str, _data_stats_pb2.CorrelationStats]
    stats_update_time: _timestamp_pb2.Timestamp

    def __init__(self, primary_table_spec_id: _Optional[str]=..., target_column_spec_id: _Optional[str]=..., weight_column_spec_id: _Optional[str]=..., ml_use_column_spec_id: _Optional[str]=..., target_column_correlations: _Optional[_Mapping[str, _data_stats_pb2.CorrelationStats]]=..., stats_update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class TablesModelMetadata(_message.Message):
    __slots__ = ('optimization_objective_recall_value', 'optimization_objective_precision_value', 'target_column_spec', 'input_feature_column_specs', 'optimization_objective', 'tables_model_column_info', 'train_budget_milli_node_hours', 'train_cost_milli_node_hours', 'disable_early_stopping')
    OPTIMIZATION_OBJECTIVE_RECALL_VALUE_FIELD_NUMBER: _ClassVar[int]
    OPTIMIZATION_OBJECTIVE_PRECISION_VALUE_FIELD_NUMBER: _ClassVar[int]
    TARGET_COLUMN_SPEC_FIELD_NUMBER: _ClassVar[int]
    INPUT_FEATURE_COLUMN_SPECS_FIELD_NUMBER: _ClassVar[int]
    OPTIMIZATION_OBJECTIVE_FIELD_NUMBER: _ClassVar[int]
    TABLES_MODEL_COLUMN_INFO_FIELD_NUMBER: _ClassVar[int]
    TRAIN_BUDGET_MILLI_NODE_HOURS_FIELD_NUMBER: _ClassVar[int]
    TRAIN_COST_MILLI_NODE_HOURS_FIELD_NUMBER: _ClassVar[int]
    DISABLE_EARLY_STOPPING_FIELD_NUMBER: _ClassVar[int]
    optimization_objective_recall_value: float
    optimization_objective_precision_value: float
    target_column_spec: _column_spec_pb2.ColumnSpec
    input_feature_column_specs: _containers.RepeatedCompositeFieldContainer[_column_spec_pb2.ColumnSpec]
    optimization_objective: str
    tables_model_column_info: _containers.RepeatedCompositeFieldContainer[TablesModelColumnInfo]
    train_budget_milli_node_hours: int
    train_cost_milli_node_hours: int
    disable_early_stopping: bool

    def __init__(self, optimization_objective_recall_value: _Optional[float]=..., optimization_objective_precision_value: _Optional[float]=..., target_column_spec: _Optional[_Union[_column_spec_pb2.ColumnSpec, _Mapping]]=..., input_feature_column_specs: _Optional[_Iterable[_Union[_column_spec_pb2.ColumnSpec, _Mapping]]]=..., optimization_objective: _Optional[str]=..., tables_model_column_info: _Optional[_Iterable[_Union[TablesModelColumnInfo, _Mapping]]]=..., train_budget_milli_node_hours: _Optional[int]=..., train_cost_milli_node_hours: _Optional[int]=..., disable_early_stopping: bool=...) -> None:
        ...

class TablesAnnotation(_message.Message):
    __slots__ = ('score', 'prediction_interval', 'value', 'tables_model_column_info', 'baseline_score')
    SCORE_FIELD_NUMBER: _ClassVar[int]
    PREDICTION_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    TABLES_MODEL_COLUMN_INFO_FIELD_NUMBER: _ClassVar[int]
    BASELINE_SCORE_FIELD_NUMBER: _ClassVar[int]
    score: float
    prediction_interval: _ranges_pb2.DoubleRange
    value: _struct_pb2.Value
    tables_model_column_info: _containers.RepeatedCompositeFieldContainer[TablesModelColumnInfo]
    baseline_score: float

    def __init__(self, score: _Optional[float]=..., prediction_interval: _Optional[_Union[_ranges_pb2.DoubleRange, _Mapping]]=..., value: _Optional[_Union[_struct_pb2.Value, _Mapping]]=..., tables_model_column_info: _Optional[_Iterable[_Union[TablesModelColumnInfo, _Mapping]]]=..., baseline_score: _Optional[float]=...) -> None:
        ...

class TablesModelColumnInfo(_message.Message):
    __slots__ = ('column_spec_name', 'column_display_name', 'feature_importance')
    COLUMN_SPEC_NAME_FIELD_NUMBER: _ClassVar[int]
    COLUMN_DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    FEATURE_IMPORTANCE_FIELD_NUMBER: _ClassVar[int]
    column_spec_name: str
    column_display_name: str
    feature_importance: float

    def __init__(self, column_spec_name: _Optional[str]=..., column_display_name: _Optional[str]=..., feature_importance: _Optional[float]=...) -> None:
        ...